from passlib.context import CryptContext

pwdContext = CryptContext(schemes=["bcrypt"], deprecated='auto')

def appHash(content:str):
    return pwdContext.hash(content)