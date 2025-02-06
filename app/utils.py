from passlib.context import CryptContext

pwdContext = CryptContext(schemes=["bcrypt"], deprecated='auto')

def appHash(content:str):
    return pwdContext.hash(content)

def verifyPassword(plain_pass, hashed_pass):
    return pwdContext.verify(plain_pass, hashed_pass)