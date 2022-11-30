class Solution:
    def uniqueOccurrences(self, arr):
        countOfChars = dict()
        for e in arr:
            if countOfChars.get(e):
                countOfChars[e] +=1
            else:
                countOfChars[e] = 1
        countDictList = list(countOfChars.values())
        if len(countDictList) == len(set(countDictList)):
            return 'true'
        else:
            return 'false'
s = Solution()
print(s.uniqueOccurrences([1,2]))