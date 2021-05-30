from app.extra.utils.config import ConfigUtils


TITLE_API = ConfigUtils.env("TITLE_API", str)
VERSION_API = ConfigUtils.env("VERSION_API", str)
DESCRIPTION_API = ConfigUtils.env("DESCRIPTION_API", str)
DEBUG = ConfigUtils.env("DEBUG", bool)
