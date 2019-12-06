from hash_map import HashMap

hash_map = HashMap(15)
hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")

print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))
