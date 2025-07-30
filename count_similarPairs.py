class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def get_char_set(word:str)-> frozenset:
            return frozenset(word)
        char_sets=[get_char_set(word) for word in words]
        count=0
        for i in range(len(char_sets)):
            for j in range(i+1,len(char_sets)):
                if char_sets[i]==char_sets[j]:
                    count +=1
        return count
