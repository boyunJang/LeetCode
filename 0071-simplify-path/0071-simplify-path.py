class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")

        stack = []
        for elem in path_list:
            if elem == '' or elem == '.': continue
            if elem == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(elem)

        return "/" + "/".join(stack)
            