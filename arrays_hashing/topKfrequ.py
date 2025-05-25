class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies_hashed = dict()
        for num in nums:
            frequencies_hashed[num] = frequencies_hashed.get(num,0)+1

        #Here's a naive solution which beats 94% of others in leetcode
        # possible_frequencies = list(frequencies_hashed.values())
        # possible_frequencies.sort(reverse=True)
        # cutoff_frequency =possible_frequencies[:k][-1]
        # ans = []
        # for num,frequency in frequencies_hashed.items():
        #     if frequency>=cutoff_frequency:
        #         ans.append(num)
        # return ans
        buckets_by_frequency = [[] for _ in range(len(nums)+1)] #a bucket-sort solution which is theoretically better but in practice runs way
        print(len(buckets_by_frequency))
        for num,freq in frequencies_hashed.items():
            buckets_by_frequency[freq].append(num)
        ans = []
        for i in range(len(nums),-1,-1):
            for num in buckets_by_frequency[i]:
                ans.append(num)
            if len(ans) >= k:
                return ans
        return ans 