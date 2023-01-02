'''
We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.
'''

#FIRST SOLUTION. CASE BY CASE

class Solution:
    def detectCapitalUse(self, word: str) -> bool:

	#1 case. One letter words(Ex:'A', 'a')
        if len(word) == 1:
            return True

	#2 case. First letter low and second upper(Ex: 'aAAAA', 'aAaaa', 'aAaAa...')
        if word[0].islower() and word[1].isupper():
            return False

	#3 case. Any word that letter are merged low and upper excluding the first letter
	#(Ex: 'AaA', 'AaaAaa', 'aaaA')
        for i in range(2, len(word)):
            #Compare each letter with the next one
            if word[i].isupper() and word[i-1].islower():
                return False
            elif word[i].islower() and word[i-1].isupper():
                return False

        return True
        
#SECOND SOLUTION. USEFUL METHODS IN PYTHON (istitle())

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


