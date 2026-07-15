class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        final_list = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        print(count)

        for key, value in sorted(count.items(), key=lambda item: item[1], reverse=True):
            print(key,value)
            if k>0:
                final_list.append(key)
            k-=1

        return final_list