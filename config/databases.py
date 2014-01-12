from getenv import env
import dj_database_url

SETTINGS = {
    "development": {
        'default': dj_database_url.config(default=env('DATABASE_URL'))
    }
}
