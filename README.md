# Notes

## JWT Authentication

I wasn't able to make the custom JWT work properly, wanted to customize it to use `email` instead of `username`. Will try doing it in a next iteration.

I also put together a quick [TODO-list](./TODO.md) with next iteration improvements.


## MySQL Database

I had many issues trying to setup a MySQL database – tried both the Django recommended connector as well as the MySQL official connector (no C dependencies) but still couldn't make it work. So, for the sake of time, I decided to pivot to Postgres, which I am more used to work with and was able to solve any setup issues faster.


## Testing

All tests are under `./tests` folder. I created some functional tests (non-unit for the more purists) for the main features and one end-to-end test, which is in the `e2e` folder.


# Running on Docker

```bash
docker-compose build
docker-compose up
```

Access `localhost:8000/products`, for instance (or use cURL/Postman, etc.)


# Running on host

```bash
pip install -r requirements.txt
DJANGO_SETTINGS_MODULE=stock_system.dev_settings ./runserver.sh
```

```bash
# django shell
DJANGO_SETTINGS_MODULE=stock_system.dev_settings python manage.py shell 
```


# Running tests

For now, tests are executed on host using SQLite database.

```bash
pip install -r requirements.txt
pytest
```
