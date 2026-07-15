class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        matching_dict = {}
        for word in strs:
            letters = list(word)
            letters.sort()
            signature_word = ''.join(letters)
            if signature_word not in matching_dict:
                matching_dict[signature_word] = []
            matching_dict[signature_word].append(word)
        return list(matching_dict.values())