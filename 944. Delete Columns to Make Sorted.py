'''
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae

You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.
'''

#FIRST SOLUTION. TWO LOOPS ITERATING THROUGH MATRIX (WITH BREAK)
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

	#Size of words
        tamanho = len(strs[0])

	#Number of columns to delete
        cont = 0
    
	#Loop through X number of columns times
        for column in range(0, tamanho):
            #Obs-1
            for row in range(1, len(strs)):
       
       		#Compare each row index with the anterior row-1
		#Obs-1: only starts comparing from the second row(index:1) to the final
                if strs[row][column] < strs[row-1][column]:
                
                    #If is not alphabetical ordered add +1 in count
                    cont += 1
                    
                    #Break to avoid unnecessary loops
                    break

        return cont

        
#SECOND SOLUTION. COUNT UNSORTED COLUMNS

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
    	#Using zip() function to transpose the matrix
    	#Return the number of unsorted columns
        return sum(list(col) != sorted(col) for col in zip(*strs))
