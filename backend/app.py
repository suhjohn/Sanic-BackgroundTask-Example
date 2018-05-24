from sanic import Sanic

app = Sanic(__name__)

from .tasks import producer
from .blueprints import bp

app.add_task(producer.stream_task)
app.blueprint(bp)
