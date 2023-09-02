class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        sorted_list = sorted(words, key=len)
        reversed_list = sorted(words, key=len, reverse = True)
        max_length = len(sorted_list[0])
        prefix = ""

        if len(sorted_list) == 1:
            print(sorted_list[0])
        elif reversed_list[0] == "":
            print("")

        for i in range(max_length):
            current_char = sorted_list[0][i]
            for word in sorted_list:
                if current_char != word[i]:
                    return (prefix)
            prefix += current_char

        return prefix