class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for string in strs:
            length_prefix=f"{len(string):4}"
            encoded.append(length_prefix+string)
        return"".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded=[]
        index=0
        total_length=len(s)
        while index<total_length:
            str_length = int(s[index:index+4])
            index+=4
            decoded_s = s[index:index+str_length]
            decoded.append(decoded_s)
            index += str_length
        return decoded
