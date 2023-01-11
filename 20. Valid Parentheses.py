class Solution:
    def isValid(self, s: str) -> bool:
        par = 0
        cha = 0
        col = 0

        lst = []

        for i in range(len(s)):
            if s[i] == '(':
                par += 1
                lst.append('p')
            elif s[i] == '{':
                cha += 1
                lst.append('x')
            elif s[i] == '[':
                col += 1
                lst.append('c')
            elif s[i] == ')' and len(lst) > 0:
                if lst.pop() == 'p':
                    par -= 1
            elif s[i] == '}' and len(lst) > 0:
                if lst.pop() == 'x':
                    cha -= 1
            elif s[i] == ']' and len(lst) > 0:
                if lst.pop() == 'c':
                    col -= 1
            else:
                return False

        if (par == 0) and (cha == 0) and (col == 0):
            return True
        else:
            return False
