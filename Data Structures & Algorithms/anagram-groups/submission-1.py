class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for i in word:
                val = ord(i) - ord('a')
                freq[val] += 1
            group[tuple(freq)].append(word)
        return list(group.values())