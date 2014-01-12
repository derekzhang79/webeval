from getenv import env
import dj_database_url

DEVELOPMENT = {
    'default': dj_database_url.config(default=env('DATABASE_URL'))
}
