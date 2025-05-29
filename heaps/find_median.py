import heapq

class MedianFinder:


    def __init__(self):
        self.minHeap =[] #I will save here the largest n/2 values,
        self.maxHeap=[]  #I will save here the smallest n/2 values. Since python's implementation supports only minheap, the actual values will be multiplied by -1

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 or len(self.maxHeap)==0:
            newHeap = [num]
            if len(self.minHeap)==0 and len(self.maxHeap)==0:
                self.minHeap=newHeap
                return
            currentHeapData = self.minHeap+[-1*x for x in self.maxHeap]
            if newHeap[0]>currentHeapData[0]:
                self.minHeap = newHeap
                self.maxHeap = [currentHeapData[0]*-1]
            else:
                self.minHeap = currentHeapData
                self.maxHeap = [newHeap[0]*-1]
            return
        #Let's find out where I want to add the new number
        if num>self.minHeap[0]: #If my num is bigger than that number, i want to add it to the larger numbers heap (minheap), otherwise i want to add it to the smaller numbers heap
            heapq.heappush(self.minHeap,num)
        else:
            heapq.heappush(self.maxHeap,-1*num)
        
        #and now I want to balance the heaps eg, if the difference between the len of my heaps is more than one, I want to move the smallest of the largest numbers to the smaller numbers heap or vice versa
        if len(self.minHeap) > len(self.maxHeap) + 1 :
            #move on number from maxheap to minheap
            move_num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,move_num*-1)
        
        

        if len(self.maxHeap) > len(self.minHeap) + 1 :
            move_num = -1* heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,move_num)
        
        
        

    def findMedian(self) -> float:
        if len(self.minHeap) ==0 and len(self.maxHeap)==0:
            return 0
        if len(self.minHeap) ==0:
            return self.maxHeap[0]*-1
        if len(self.maxHeap)==0:
            return self.minHeap[0]
        if (len(self.minHeap) + len(self.maxHeap))%2==0:
            #something like [0 1 6 8] - i need to return the average
            return (self.minHeap[0]+self.maxHeap[0]*-1)/2
        #[odd number, something like [0 1 6]] - i need to return whatever number that is in my larger heap
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return self.maxHeap[0] * -1
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()