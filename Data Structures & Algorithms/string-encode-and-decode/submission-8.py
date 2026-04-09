class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""
        for item in strs:
            result += (str(len(item)) + "#" + item)
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        
        def add_result(start, end):
            temp = ""
            for i in range(start, end+1):
                temp += s[i]
            result.append(temp)
            
        result = []
        index = 0
        while index < len(s):
            num = ""
            k = index
            while s[k] != "#":
                num += s[k]
                k += 1
            num = int(num)
            add_result(k+1, k+num)
            index = (k+1+num)
        
        return result
                
                


