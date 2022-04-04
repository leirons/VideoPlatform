

# Want to use this project?

На данный момент используется sqlite, но в docker-compose.yml лежит образ postgres и настройки к нему, что бы изменить sqlite на postgres зайди в `core/config.py` и в db_url возьму с env ```DATABASE_URL```

``` 
docker-compose up -d --build
```
