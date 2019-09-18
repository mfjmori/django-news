from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from django.utils import timezone
from urllib.parse import urlparse
import requests, re, dateutil.parser
from bs4 import BeautifulSoup
from scraping.models import Scraping
from scraping.forms import ScrapingForm

class Command(BaseCommand):

  def handle(self, *args, **options):
    topics = self.getYahooTopics()
    for topic in topics:
      topicAttributes = self.getTopicAttributes(topic)
      self.createScraping(*topicAttributes)
    print('バッチ処理が完了しました')
  
  def getYahooTopics(self):
    sourceUrl = 'https://news.yahoo.co.jp'
    html = requests.get(sourceUrl)
    content = BeautifulSoup(html.content, "html.parser")
    topics = content.find_all(class_='topicsListItem')
    return topics
  
  def getTopicAttributes(self, topic):
    topicUrl = topic.a.get('href')
    topicHtml = requests.get(topicUrl)
    topicContent = BeautifulSoup(topicHtml.content, "html.parser")
    detailUrl = topicContent.find(class_='tpcNews_detailLink').a.get('href')
    detailHtml = requests.get(detailUrl)
    detailContent = BeautifulSoup(detailHtml.content, "html.parser")

    title = detailContent.find(class_="hd").h1.getText().strip("\n")
    bodyList = detailContent.find_all(class_="yjDirectSLinkTarget")
    body = ''
    for pTag in bodyList:
      body += pTag.getText().strip("\n")
    publish_at = detailContent.find(class_="source").getText().strip("\n")
    publish_at = re.sub('\(.\)|配信', '', publish_at)
    publish_at = dateutil.parser.parse(str(timezone.datetime.now().year) + "/" + publish_at + '+0900')
    photosContainer = detailContent.find(class_="PhotosContainerMain")
    if photosContainer:
      imageUrl = photosContainer.find("img").get('src')
    else:
      imageUrl = None
    topicAttributes = [title, body, imageUrl, publish_at, detailUrl]
    return topicAttributes

  def createScraping(self, title, body, imageUrl, publish_at, url):
    print(title)
    print(url)
    form = ScrapingForm(data={
      'title' : title,
      'body' : body,
      'publish_at' : publish_at,
      'url' : url,
    })
    if form.is_valid():
      print('バリデーションOK')
      if imageUrl:
        imageName = urlparse(imageUrl).path.split('/')[-1]
        scraping = form.save(commit=False)
        response = requests.get(imageUrl)
        if response.status_code == 200:
          scraping.image.save(imageName, ContentFile(response.content), save=True)
          print('保存しました')
      else:
        scraping = form.save()
        print('保存しました')
    else:
      print('バリデーションエラー')
      print(form.errors)
    print('----------------------')
