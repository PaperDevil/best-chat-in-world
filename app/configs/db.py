from app.extra.utils.config import ConfigUtils

DB_HOST = ConfigUtils.env('DB_HOST', str)
DB_PORT = ConfigUtils.env('DB_PORT', int)
DB_USER = ConfigUtils.env('DB_USER', str)
DB_PASSWORD = ConfigUtils.env('DB_PASSWORD', str)
PRIMARY_DB_NAME = ConfigUtils.env('PRIMARY_DB_NAME', str)
