from starlette.routing import Router, Route
from controllers.user_controllers import *

user_routes = [
    Route('/register', register, methods=['POST']),
    Route('/login', login, methods=['POST']),
]