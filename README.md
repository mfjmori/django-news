# django-news

## usersテーブル
|Column|Type|PK|FK|Options|
|---|---|---|---|---|
|id|serial|○||NOT NULL, INDEX|
|username|varchar|||NOT NULL|
|email|varchar|||NOT NULL|
|password|varchar|||NOT NULL|

## stocksテーブル
|Column|Type|PK|FK|Options|
|---|---|---|---|---|
|id|serial|○||NOT NULL, INDEX|
|user_id|integer||○|NOT NULL, INDEX|
|url|varchar|||NOT NULL|
|image_url|varchar||||
|title|varchar|||NOT NULL|
|body|text||||
|source|varchar||||
|likes_count|integer||||
|publish_at|timestamp|||NOT NULL|
- UNIQUE ("user_id", "url")

## postテーブル
|Column|Type|PK|FK|Options|
|---|---|---|---|---|
|id|serial|○||NOT NULL, INDEX|
|author_id|integer||○|NOT NULL, INDEX|
|title|varchar|||NOT NULL|
|body|text|||NOT NULL|
|publish_at|timestamp|||NOT NULL|
