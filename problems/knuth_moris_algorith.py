"""
    Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.

    Examples:

    Input:  txt[] = "THIS IS A TEST TEXT"
            pat[] = "TEST"
    Output: Pattern found at index 10

    Input:  txt[] =  "AABCAACAADAABAABA"
            pat[] =  "AABA"
    Output: Pattern found at index 0
            Pattern found at index 9
            Pattern found at index 12

    Explaination:
        A->A->B->A->*
        {
            A: {
                A: {
                    B:{
                        A:{
                            *: "AABA"
                        }
                    }
                }
            }
        }

"""

# Time complexity: O(n*L)
#   -> L = length of the substring word
# Space complexity: O(L)
# Brute Force Approach
# def knuthMorrisPrattAlgorithm(string, substring):
#     # Write your code here.
#     trie = Trie()
#     trie.add(substring)
#     final_list = {}
#     for i in range(len(string)):
#         explore(i, string, trie.node, final_list)
#         if final_list:
#             return True
#     return False

# def explore(i, string, trie_node, final_list):
#     letter = string[i]

#     if letter not in trie_node:
#         return
#     trie_node = trie_node[letter]
#     if "*" in trie_node:
#         final_list[i] = True
#         return
#     if i+1== len(string):
#         return
#     explore(i+1, string, trie_node, final_list)

# class Trie:
#     def __init__(self):
#         self.node = {}
#         self.end_point = "*"
    
#     def add(self, word):
#         current = self.node
#         for letter in word:
#             if letter not in current:
#                 current[letter] = {}
            
#             current = current[letter]
#         current[self.end_point] = word


# print(knuthMorrisPrattAlgorithm("aefoaefcdaefcdaed", "aefcdaed"))


def knuthMorrisPrattAlgorithm(string, substring):
    pattern = create_pattern(substring)
    return is_substring(string, substring, pattern)



def is_substring(string, substring, pattern):
    i=j=0
    while i + len(substring) -j <len(string):
        if string[i] == substring[j]:
            if j == len(substring)-1:
                return True
            i+=1
            j+=1
        elif j>0:
            j = pattern[j-1]
        else:
            i+=1
    
    return False


def create_pattern(substring):
    pattern = [0 for i in substring]
    i=1
    j=0
    while i<len(substring):
        if substring[i] == substring[j]:
            i+=1
            j+=1
        elif j>0:
            j = pattern[j-1]
        else:
            i+=1
    
    return pattern
