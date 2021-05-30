from fastapi import APIRouter

from app.configs.server import VERSION_API
from app.extra.entities.response.exception_response import ExceptionResponse

general_router = APIRouter(prefix=f'/{VERSION_API}', responses={400: {'model': ExceptionResponse},
                                                                500: {'model': ExceptionResponse}})
