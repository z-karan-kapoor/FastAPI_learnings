from passlib.context import CryptContext

pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:

    @staticmethod
    def get_hash_password(plain_password):
        """To store User password as Hashed"""
        return pwd_context.hash(plain_password)
    
    @staticmethod
    def verify_password(plain_password, hash_password):
        """To verify User Password"""
        return pwd_context.verify(plain_password,hash_password)