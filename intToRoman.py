#Given an integer, convert it to a roman numeral.
#link to this task https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)
        sol = ""
        x = ["I", "V", "X", "L", "C", "D", "M"]  #list of possible roman numerals
        for i in range(len(num)):
            l = num[-1-i]      #check for each character from the end and assign respectively, extend the solution
            if l in "123":
                sol += int(l) * x[2*i]
            elif l == "4":
                sol += x[2*i+1] + x[2*i]
            elif l == "5":
                sol += x[2*i+1]
            elif l in "678":
                sol += (int(l)-5) * x[2*i] + x[2*i+1] 
            elif l == "9":
                sol += x[2*i+2] + x[2*i]
            elif l == "0":
                continue
        return sol[::-1]     #reverse to receive the solution
