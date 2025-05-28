# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #1. Count the list size
        num_elements = 0
        current_node = head
        while current_node:
            num_elements += 1
            current_node = current_node.next
        if num_elements <=1:
            return head
        index_element_divide_from = num_elements//2 + num_elements%2
        current_node = head
        for i in range(index_element_divide_from-1):
            current_node = current_node.next
        start_second_list = current_node.next
        current_node.next = None #Cut off the first list
        #step 2: reverse the second list
        current_node = start_second_list
        previous_node = None
        while current_node:
            current_next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = current_next
        start_second_list = previous_node
        #step 3: Iterate through both lists
        list1_iterator = head
        list2_iterator = start_second_list
        while list1_iterator and list2_iterator:
            list1_iterator_next = list1_iterator.next
            list2_iterator_next = list2_iterator.next
            list1_iterator.next = list2_iterator
            list2_iterator.next = list1_iterator_next
            list1_iterator = list1_iterator_next
            list2_iterator = list2_iterator_next
        
            


        