# Лабораторная работа от 29 октября 2024 г.
# Реализация динамической хеш-таблицы с функциями расширения и сокращения.

STEP = 128  # Шаг размерности таблицы
LOAD_FACTOR = 0.3 # Коэффициент заполнения, от которого зависит размерность

class DynamicHashTable:
    def __init__(self, capacity=128):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash(self, value):
        return value % self.capacity

    def insert(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.size += 1
        if self.size > self.capacity * (1 - LOAD_FACTOR):
            self.resize(self.capacity + STEP)
        return

    def get(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    self.size -= 1
                    if self.size < self.capacity * LOAD_FACTOR:
                        self.resize(max(128, self.capacity - STEP))
                    return
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

hash_table.insert(1, "Заяц")
hash_table.insert(2, "Волк")
hash_table.insert(3, "Лиса")

print(hash_table.get(3))

hash_table.delete(2)
print(hash_table.get(2))

