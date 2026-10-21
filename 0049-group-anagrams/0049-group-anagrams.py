class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        temp_d = {}
        temp_a = []
        output = []
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in temp_d:
                temp_d[sorted_str].append(strs[i])
            else:
                temp_a.append(sorted_str)
                temp_d[sorted_str] = []
                temp_d[sorted_str].append(strs[i])
        for i in temp_a:
            output.append(temp_d[i])
        return output
