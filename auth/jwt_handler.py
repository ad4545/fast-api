import time
import jwt
from decouple import config

JWT_SECRET = config('secret')
JWT_ALGO = config('algorithm')


def token_res(token:str):
    return {
        "access_token":token
    }

def signJWT(userId:str):
    payload = {
        "userId":userId,
        "expiry":time.time() + 600
    }
    token = jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGO)

    return token_res(token)


def decodeJwt(token:str):
    decode_token = jwt.decode(token,JWT_SECRET,algorithms=JWT_ALGO)
    return decode_token if decode_token['expires'] >=time.time() else None 