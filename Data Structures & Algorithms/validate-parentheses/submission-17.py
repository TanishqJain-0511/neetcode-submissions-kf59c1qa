class Solution:
    def isValid(self, s: str) -> bool:
        
        open_1 = {"(", "[", "{"}
        close_1 = {")", "]", "}"}

        open_close = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        x_list = []

        for ch in s:
            if ch in open_1:
                x_list.append(ch)
            elif ch in close_1:
                if not x_list:
                    return False
                to_compare = open_close[x_list[-1]] 
              
                if ch == to_compare:
                    x_list.pop()
                else:
                    return False
           
        
        return len(x_list)==0

