class Solution:
    def uniqueOccurrences(self, arr):
        lst = arr
        arr_len = len(lst)
        uniq_arr = list(set(lst))
        uniq_arr_len = len(uniq_arr)
        if uniq_arr_len != arr_len:
            return 'true'
        elif uniq_arr_len == arr_len:
            return 'false'
s = Solution()
print(s.uniqueOccurrences([1,2]))