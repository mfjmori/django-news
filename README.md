# django-news

## usersテーブル
|Column|Type|Options|
|---|---|---|
|username|varchar|NOT NULL|
|email|varchar|NOT NULL|
|password|varchar|NOT NULL|

## stocsテーブル
|Column|Type|Options|
|---|---|---|
|user_id|bigint|NOT NULL, FOREIGN KEY|
|url|varchar|NOT NULL|
|image_url|varchar||
|title|varchar|NOT NULL|
|body|text||
|source|varchar||
|likes_count|integer||
|publish_at|date|NOT NULL|
- UNIQUE ("user_id", "url")
