class Solution:
    def romanToInt(self, s: str) -> int:
         d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}

         summ = 0
         n = len(s)
         i = 0

         while i < n:
              if i < n - 1 and d[s[i]] < d[s[i+1]]:
                   summ += d[s[i+1]] - d[s[i]]
                   i += 2
              else:
                   summ += d[s[i]]
                   i += 1

         return summ
    


class Solution:
     def isSubsequence(self, s: str, t: str) -> bool:
          S = len(s)
          T = len(t)

          if s == '': return True
          if S > T: return False

          j = 0
          for i in range(T):
               if t[i] ==s[j]:
                    if j == S-1:
                         return True
                    j += 1

          return False





