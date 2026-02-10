from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os, logging, sys # edit

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

def hello_world(request):
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    logger.info("api called")
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    logger.info(f"running main application and listening on port {os.environ.get('PORT')}") # edit
    logger.info(f"value of my port {os.environ.get('MY_PORT')}") # edit
    with Configurator() as config:
        logger.info("configuring apis")
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    logger.info("starting server")
    server.serve_forever()
