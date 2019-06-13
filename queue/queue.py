import sys
sys.path.append("..")
from LinkedList import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size = self.storage.length()
    if self.size == 0:
        self.storage.add_to_head(item)
    else:
        self.storage.add_to_tail(item)

  def dequeue(self):
    if self.size == 0:
        return None
    head = self.storage.head.value
    print(head)
    self.storage.delete_from_head()
    self.size = self.storage.length()
    return head

  def len(self):
    return self.storage.length()
