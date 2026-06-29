class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        char_map = defaultdict(list)
        for string in strs:
            char_map["".join(sorted(string))].append(string)
        return list(char_map.values())
