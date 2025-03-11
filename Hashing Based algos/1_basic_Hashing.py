import hashlib


class Hashing():
    def get_sha256_hash(self,key: str) -> str:
        return hashlib.sha256(key.encode()).hexdigest()


hash1 = Hashing()

print(hash1.get_sha256_hash("Hello"))

