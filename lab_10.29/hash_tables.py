# Лабораторная работа от 29 октября 2024 г.
# Реализация динамической хеш-таблицы с функциями расширения и сокращения.

class DynamicHashTable:
    def __init__(self, capacity = 256):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash_256(self, key):
        return hash(key) % 256

    def hash_128(self, key):
        return hash(key) % 128

    def hash_function(self, key):
        if self.capacity == 256:
            return self.hash_256(key)
        else:
            return self.hash_128(key)

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        # Проверяем, существует ли уже ключ, и обновляем значение
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.size += 1
        if self.size > self.capacity * 0.7:  # Увеличиваем размер, если заполненность > 70%
            self.resize(self.capacity * 2)

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    self.size -= 1
                    if self.size < self.capacity * 0.3:  # Уменьшаем размер, если заполненность < 30%
                        self.resize(max(128, self.capacity // 2))
                    return

    def resize(self, new_capacity):
        old_table = self.table
        self.capacity = new_capacity
        self.table = [None] * self.capacity
        self.size = 0

        for bucket in old_table:
            if bucket is not None:
                for key, value in bucket:
                    self.insert(key, value)

# Демо
hash_table = DynamicHashTable()

hash_table.insert("Заяц", 1)
hash_table.insert("Волк", 2)
hash_table.insert("Лиса", 3)

print(hash_table.get("Лиса"))  # Вывод: 2

hash_table.delete("Волк")
print(hash_table.get("Волк"))

