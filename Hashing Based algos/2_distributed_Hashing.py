import hashlib
import json

with open("data.json","r") as f:
    data = json.load(f)


dictio = {0:[],1:[],2:[]}
servers = 3

lis = [
    "hell there",
    "132opajkbr",
    "aliergha",
    "xzi90mndq",
    "wqertplmza",
    "87yuhjnbvc",
    "pasodkqwe",
    "zxcvbnm123",
    "ujmklop987",
    "ghytredfvc"
]


class distributedHashiing():
    def __init__(self,num_ser: int):
        self.num = num_ser

    @staticmethod
    def hash_key_gen(key: str) -> int:
        return int(hashlib.sha256(key.encode()).hexdigest(),16)


    def get_server_for_key(self,key: str) -> int:
        key_hash = self.hash_key_gen(key)
        return key_hash % self.num
    

hash = distributedHashiing(servers)

for i in data:
    server_num = hash.get_server_for_key(i["_id"])
    dictio[server_num].append(i)

for key in dictio:
    print(key,"->",dictio[key],"\n")





