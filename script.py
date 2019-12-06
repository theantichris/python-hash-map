class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for i in range(self.array_size)]

  def assign(self, key, value):
      index = self.get_index(key)
      current_array_value = self.array[index]
      if current_array_value and current_array_value[0] == key:
          self.array[index][1] = value
      else:
          self.array[index] = [key, value]

  def retrieve(self, key):
      index = self.get_index(key)
      return self.array[index]

  def hash(self, key):
    key_bytes = key.encode() # Convert key into list of bytes
    hash_code = sum(key_bytes) # Add the bytes together
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size # Compress the hash code using modulus

  def get_index(self, key):
      return self.compress(self.hash(key))
