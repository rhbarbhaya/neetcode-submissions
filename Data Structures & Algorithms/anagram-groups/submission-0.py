class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in result:
                result[key] = [string]
            else:
                result[key].append(string)
        result = list(result.values())
        print(result)
        return(result)
        