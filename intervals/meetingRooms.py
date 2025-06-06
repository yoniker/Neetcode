"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


"""

Solution for the meeting rooms 2 problem:
Meeting Rooms II
Solved 
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000



Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000

"""







class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        meetings_to_book = intervals.copy()
        meetings_to_reschedule = set()
        booked_days = 1
        meetings_to_book.sort(key=lambda x:x.start)
        while len(meetings_to_book)>0 or len(meetings_to_reschedule)>0:
            if len(meetings_to_book)==0:
                booked_days+=1
                meetings_to_book = list(meetings_to_reschedule)
                meetings_to_book.sort(key=lambda x:x.start)
                meetings_to_reschedule = set()
            current_meeting_booked = meetings_to_book.pop(0)
            #while there's a conflict, add the conflicted meeting into a to-be-rescheduled set
            while len(meetings_to_book)>0 and meetings_to_book[0].start<current_meeting_booked.end:
                meetings_to_reschedule.add(meetings_to_book.pop(0))
        return booked_days
            
