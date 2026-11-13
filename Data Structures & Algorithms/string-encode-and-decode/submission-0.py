import base64
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += base64.b64encode(str.encode(string)).decode()
            result += "~"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        string = s.split("~")[:-1]
        for s in string:
            result.append(base64.b64decode(s).decode())
        print(result)
        return result
