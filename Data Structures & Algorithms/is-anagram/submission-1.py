class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_map = {}
        t_char_map = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            if char in s_char_map:
                s_char_map[char] += 1
            else:
                s_char_map[char] = 1
        print("s_char_map =>", s_char_map)
        
        for char in t:
            if char in t_char_map:
                t_char_map[char] += 1
            else:
                t_char_map[char] = 1
        print("t_char_map =>", t_char_map)
        
        for char in t_char_map:
            if char not in s_char_map:
                return False
            if s_char_map[char] != t_char_map[char]:
                return False
        return True
        