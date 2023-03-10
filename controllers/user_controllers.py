# from starlette.requests import Request
from starlette.requests import Request 
from starlette.responses import JSONResponse
from services.user_services import *
import jwt
import datetime
from starlette.authentication import (
    AuthCredentials, AuthenticationBackend, AuthenticationError, SimpleUser
)
from starlette.authentication import requires

import base64
import binascii

SECRET = 'adfjkasdfkhjsdf123kjh1ljkhkhdkjsd'

class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        if "Authorization" not in conn.headers:
            print("No auth header!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return
        auth = conn.headers["Authorization"]
        scheme, token = auth.split()
        token = token.strip()

        # try:
        # Decoding JWT.
        decoded_token = jwt.decode(token, SECRET, algorithms=['HS256'])
        payload = decoded_token.get('id') # retrieve user id from payload.
        return AuthCredentials(["authenticated"]), payload
        # except Exception:
        #     return Exception("skjdfhaskdfj")


async def register(request:Request):
    body = await request.json()
    username = body['username']
    email = body['email']
    password = body['password']
    new_user = create_user(username, email, password)
    return JSONResponse({"mesage": "User created.", "id": new_user.id}, status_code=201)

@requires('authenticated')
async def login(request:Request):
    if request.user.is_authenticated:
        print(f"From Login URL: {request.user}")
    else:
        print("Not Authenticated")
    body = await request.json()
    username = body['username']
    password = body['password']
    log = loginUser(username, password)
    if log:
        if bcrypt.checkpw(password.encode('utf-8'), log.password.encode('utf-8')):
            payload = {'id': log.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
            token = jwt.encode(payload, SECRET, algorithm='HS256')
            return JSONResponse({'token': token})
    return JSONResponse({'user': 'Invalid Credentials.'})
    