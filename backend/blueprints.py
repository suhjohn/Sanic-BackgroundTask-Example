from sanic import Blueprint

from .views import increment

bp = Blueprint(__name__.split('.')[0], url_prefix='/')
bp.add_websocket_route(handler=increment, uri="increment")
