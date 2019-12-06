class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(self.array_size)]

    def assign(self, key, value, number_collisions=0):
        index = self.get_index(key, number_collisions)
        current_array_value = self.array[index]

        if current_array_value is None:
            self.array[index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[index] = [key, value]
            return

        number_collisions += 1
        self.assign(key, value, number_collisions)

    def retrieve(self, key, number_collisions=0):
        index = self.get_index(key, number_collisions)
        possible_return_value = self.array[index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        number_collisions += 1
        self.retrieve(key, number_collisions)

    def get_index(self, key, count_collisions=0):
        key_bytes = key.encode()  # Convert key into list of bytes
        hash_code = sum(key_bytes) + count_collisions  # Add the bytes together

        return hash_code % self.array_size  # Compress the hash code using modulus
