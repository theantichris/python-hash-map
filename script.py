class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for i in range(self.array_size)]

  def assign(self, key, value):
      hash_code = self.hash(key)
      index = self.compress(hash_code)
      self.array[index] = value

  def hash(self, key):
    key_bytes = key.encode() # Convert key into list of bytes
    hash_code = sum(key_bytes) # Add the bytes together
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size # Compress the hash code using modulus
