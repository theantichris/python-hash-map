class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for i in range(self.array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code
