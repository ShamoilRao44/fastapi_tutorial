from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "9023764djka80kfkjshf725yeiubcka89280mdbiauge8763ksdbdkfja;lei34y83dncuo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_jwt_token(data:dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({'exp':expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)