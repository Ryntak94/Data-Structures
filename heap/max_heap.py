class Heap:
  def __init__(self):
    self.storage = []

  def _bubble_up(self, index):
     while index > 0:
         parent = (index-1) // 2
         if self.storage[index] > self.storage[parent]:
             self.swap(index, parent)
             index = parent
         else:
             break

  def _sift_down(self, index):
    length = len(self.storage)
    left = 2 * index + 1
    right = 2 * index + 2
    if right <= length - 1:
         if self.storage[left] > self.storage[right]:
             if self.storage[index] < self.storage[left]:
                 self.swap(left, index)
                 self._sift_down(left)
         else:
             if self.storage[index] < self.storage[right]:
                 self.swap(right, index)
                 self._sift_down(right)
    elif left <= length -1:
         if self.storage[index] < self.storage[left]:
             self.swap(left, index)
             self._sift_down(left)

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    res = self.storage[0]
    last = self.storage.pop()
    length = len(self.storage)
    if length > 0:
        self.storage[0] = last
        self._sift_down(0)
    else:
        return last
    return res


  def get_max(self):
    return self.storage[0]

  def get_size(self):
    size = len(self.storage)
    return size

  def swap(self, index, parent):
       store = self.storage[index]
       self.storage[index] = self.storage[parent]
       self.storage[parent] = store
