class MyHashMap: # Same as MyHashSet, but this time we will store a tuple (key,value)

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
                        (key,value) = self.data[i][j]
                        new_data[self._my_hash_function(key)].append((key,value))
                        counter_num_elements += 1
            self.data = new_data
            self.num_elements = counter_num_elements
            return


    def __init__(self):
        self._rebuild(self.MIN_NUM_ELEMENTS)

    def _find_by_key(self,key):
        for element in self.data[self._my_hash_function(key)]:
            if element[0] == key:
                return element
        return None
    
    def remove(self, key: int):
        element_found = self._find_by_key(key) 
        if element_found!= None:
             self.data[self._my_hash_function(key)].remove(element_found) #I could just update element if it was a dict, but i wanted to be a "purist" in the sense of not using a hashmap to implement a hashmap....
        


    def put(self, key: int, value: int):
         self.remove(key) #if i implemented it using a dictionary, I would save a bit of a time, but see comment at remove
         if self.num_elements+1 > self.allocated_memory_size*2:
            self._rebuild(new_allocated_memory_size = self.num_elements * 2 )
         
         self.data[self._my_hash_function(key)].append((key,value))
         
        

    def get(self, key: int) -> int:
        element = self._find_by_key(key)
        if element == None:
            return -1
        return element[1] #the value since we save the data as a tuple of (key,value)
        

    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)