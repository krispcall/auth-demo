from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route, Router, Mount
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware import Middleware
from controllers.user_controllers import BasicAuthBackend

from routes.user_routes import user_routes
async def home(request:Request):
    return JSONResponse({'home': 'homepage'})

routes = [
    Route('/', endpoint=home),
    Mount('/user', routes=user_routes)
]

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]

app = Starlette(
    debug=True,
    routes=routes,
    middleware=middleware
)