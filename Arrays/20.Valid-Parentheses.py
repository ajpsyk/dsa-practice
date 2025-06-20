class Solution:
    def isValid(self, s: str) -> bool:
        #hash Table of pairs
        pairs = {")":"(", "}":"{", "]":"["}
        #iterate over input string
        stack = []
        for char in s:
            #if open paren
            if char == "(" or char == "[" or char == "{":
                # push to stack
                stack.append(char)
            #else
            else:
                # if matching pair
                if len(stack) and pairs[char] == stack[-1]:
                    # pop stack
                    stack.pop()
                else:
                    return False
        # return stack is Empty
        return len(stack) == 0