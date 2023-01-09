class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0

        for i in range(len(s)-1, -1, -1):
            if(s[i]=='I'):
                num+=1
            elif(s[i]=='V'):
                if(s[i-1]=='I' and i != 0):
                    num+=3
                else:
                    num+=5
            elif(s[i]=='X'):
                if(s[i-1]=='I' and i != 0):
                    num+=8
                else:
                    num+=10
            elif(s[i]=='L'):
                if(s[i-1]=='X' and i != 0):
                    num+=30
                else:
                    num+=50
            elif(s[i]=='C'):
                if(s[i-1]=='X' and i != 0):
                    num+=80
                else:
                    num+=100
            elif(s[i]=='D'):
                if(s[i-1]=='C' and i != 0):
                    num+=300
                else:
                    num+=500
            elif(s[i]=='M'):
                if(s[i-1]=='C' and i != 0):
                    num+=800
                else:
                    num+=1000
        return num
