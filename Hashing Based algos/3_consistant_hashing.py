import hashlib
import json
import bisect

with open("MOCK_DATA.json","r") as f:
    data = json.load(f)

ip_list = [
    "192.168.5.1",
    "192.168.5.2",
    "192.168.5.3",
    "192.168.5.4",
    "192.168.5.5",
    "192.168.5.6",
    "192.168.5.7",
    "192.168.5.8",
    "192.168.5.9",
    "192.168.5.10"
]


NUM_SERVERS = 10
VIRTUAL_NODES = 10

class ConsistantHashing():
    def __init__(self,num_servers: int, virt_nodes: int):
        self.num_servers = num_servers
        self.virt_nodes = virt_nodes
        self.ring = {}   #maps hash of all(v and phy) -> phy server
        self.sorted_key = []   #sorted list of hash values (v + phy)

        for server_id in range(num_servers):
            for v in range(virt_nodes):
                vnode_key = f"Server-{server_id}-VN{ip_list[server_id]}-{server_id+10}"
                vnode_hash = self.hash_key_gen(vnode_key)
                self.ring[vnode_hash] = server_id
                self.sorted_key.append(vnode_hash)

        self.sorted_key.sort()
        # print(self.ring,"\n\n")
        # print(self.sorted_key,"\n\n")
        
    
    @staticmethod
    def hash_key_gen(key: str) -> int:
        #Generate sha hash
        return int(hashlib.sha256(key.encode()).hexdigest(), 16)
    
    def get_server_key(self,key:str) -> int:
        #Find closest server in ring
        key_hash = self.hash_key_gen(key)
        index = bisect.bisect_right(self.sorted_key, key_hash)

        if index == len(self.sorted_key):
            index = 0

        vnode_hash = self.sorted_key[index]
        return self.ring[vnode_hash]
    
hashing = ConsistantHashing(NUM_SERVERS, VIRTUAL_NODES)


dictio = {i: [] for i in range(NUM_SERVERS)}

for entry in data:
    server_num = hashing.get_server_key(entry["email"])
    dictio[server_num].append(entry)

for key in dictio:
    print(f"Server {key} -> {len(dictio[key])}\n")

        
