#Neetcode number 705

class MyHashSet:

    MIN_NUM_ELEMENTS = 5

    def _my_hash_function(self,int_key): #Simply perform a modulo operation
        return int_key % self.allocated_memory_size

    def _rebuild(self,new_allocated_memory_size):
            counter_num_elements = 0 
            new_data = [[] for i in range(new_allocated_memory_size)]
            self.allocated_memory_size = new_allocated_memory_size
            if getattr(self, "data", None) is not None:
                for i in range(len(self.data)): #iterate over all of the array
                    for j in range(len(self.data[i])): # iterate over all of the chained data
                        some_key = self.data[i][j]
                        new_data[self._my_hash_function(some_key)].append(some_key)
                        counter_num_elements += 1
            self.data = new_data
            self.num_elements = counter_num_elements
            return

    def __init__(self):
        self._rebuild(self.MIN_NUM_ELEMENTS)
        return


    def add(self, key: int):
        if self.num_elements+1 > self.allocated_memory_size*2:
            self._rebuild(new_allocated_memory_size = self.num_elements * 2 )
        if key in self.data[self._my_hash_function(key)]:
            #no need to add, potentially throw sth?
            return
        self.data[self._my_hash_function(key)].append(key)
        self.num_elements += 1 
        

    def remove(self, key: int):
        if not key in self.data[self._my_hash_function(key)]:
            return
        self.data[self._my_hash_function(key)].remove(key)
        self.num_elements -= 1
        if self.allocated_memory_size> MIN_NUM_ELEMENTS and self.num_elements < self.allocated_memory_size/2:
            self._rebuild(new_allocated_memory_size = self.num_elements * 2 )

        

    def contains(self, key: int) -> bool:
        return key in self.data[self._my_hash_function(key)]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)