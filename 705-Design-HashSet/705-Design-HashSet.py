class MyHashSet:

    def __init__(self):
        self.hashset=[]

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)
        return self.hashset

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)
        return self.hashset
    def contains(self, key: int) -> bool:
        return key in self.hashset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)