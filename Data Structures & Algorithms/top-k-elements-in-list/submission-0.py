class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            if num not in result:
                result[num] = 0
            result[num] += 1
        result = sorted(result.items(), key=lambda x: x[1], reverse=True)
        final_result = []
        for i in range(k):
            final_result.append(result[i][0])
        return(final_result)