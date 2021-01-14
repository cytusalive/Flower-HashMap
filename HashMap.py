from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for a in range(size)] 

  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for l in list_at_array:
      if l[0] == key:
        l[1] = value
        return
    list_at_array.insert(payload)

  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    for l in list_at_index:
      if l[0] == key:
        return l[1]
    return None
        

blossom = HashMap(len(flower_definitions))
for f in flower_definitions:
  blossom.assign(f[0], f[1])

print(blossom.retrieve('lavender'))

