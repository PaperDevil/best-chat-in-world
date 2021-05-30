import sys

from fastapi import FastAPI
from loguru import logger

from app.configs.server import DEBUG, TITLE_API, VERSION_API, DESCRIPTION_API
from app.configs.db import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, PRIMARY_DB_NAME
from app.internal.drivers.async_pg import AsyncPg
from app.internal.servers.http.general import general_router


class FastAPIServer:

    @staticmethod
    @logger.catch
    def get_app() -> FastAPI:
        logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
        app = FastAPI(
            debug=DEBUG,
            title=TITLE_API,
            version=VERSION_API,
            description=DESCRIPTION_API,
            docs_url=f"/v{VERSION_API}/docs",
            redoc_url=f"/v{VERSION_API}/redoc",
            openapi_url=f"/v{VERSION_API}/openapi.json"
        )

        app.include_router(general_router)
        # TODO: add_logs(app)

        @app.on_event('startup')
        async def init_primary_db():
            await AsyncPg.init_primary_db(host=DB_HOST, port=DB_PORT,
                                          user=DB_USER, password=DB_PASSWORD,
                                          database=PRIMARY_DB_NAME)

        @app.on_event('shutdown')
        async def close_primary_db():
            await AsyncPg.close_primary_db()

        return app
