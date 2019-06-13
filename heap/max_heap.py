class Heap:
  def __init__(self):
    self.storage = []

  def _bubble_up(self, index):
     while index > 0:
         parent = (index-1) // 2
         print(self.storage)
         print(index)
         if self.storage[index] > self.storage[parent]:
             self.swap(index, parent)
             index = parent
         else:
             break

  def _sift_down(self, index):
    length = len(self.storage)
    left = 2 * index + 1
    right = 2 * index + 2
    if right <= length:
        if self.storage[left] > self.storage[right]:
            if self.storage[index] < self.storage[left]:
                self.swap(left)
        else:
            if self.storage[index] < self.storage[right]:
                self.swap(right)
    elif left <= length:
        if self.storage[left] > self.storage[index]:
            self.swap(left)
    else:
        break

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    res = self.storage[0]
    self.storage[0] = self.storage.pop()
    self._sift_down(0)


  def get_max(self):
    pass

  def get_size(self):
    pass

  def swap(self, index, parent):
       store = self.storage[index]
       self.storage[index] = self.storage[parent]
       self.storage[parent] = store
