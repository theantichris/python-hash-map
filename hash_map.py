class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(self.array_size)]

    def assign(self, key, value):
        index = self.get_index(key)
        current_array_value = self.array[index]

        if current_array_value is None:
            self.array[index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[index] = [key, value]
            return

        number_collisions = 1
        while current_array_value[0] != key:
            new_index = self.compress(self.hash(key, number_collisions))
            current_array_value = self.array[new_index]

            if current_array_value is None:
                self.array[new_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_index] = [key, value]
                return

            number_collisions += 1

        return

    def retrieve(self, key):
        index = self.get_index(key)
        possible_return_value = self.array[index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        number_collisions = 1
        while possible_return_value[0] != key:
            new_index = self.compress(self.hash(key, number_collisions))
            possible_return_value = self.array[new_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            number_collisions += 1

        return

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()  # Convert key into list of bytes
        hash_code = sum(key_bytes)  # Add the bytes together
        return hash_code + count_collisions

    def compress(self, hash_code):
        return hash_code % self.array_size  # Compress the hash code using modulus

    def get_index(self, key):
        return self.compress(self.hash(key))
