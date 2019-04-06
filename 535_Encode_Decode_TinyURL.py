import random
import string

class Codec:
    ###Solution 1###
    # def __init__(self):
    #     self.dic = {}
    #
    # def encode(self, longUrl):
    #     """Encodes a URL to a shortened URL.
    #
    #     :type longUrl: str
    #     :rtype: str
    #     """
    #     self.dic['a'] = longUrl
    #     return "a"
    #
    # def decode(self, shortUrl):
    #     """Decodes a shortened URL to its original URL.
    #
    #     :type shortUrl: str
    #     :rtype: str
    #     """
    #     return self.dic[shortUrl]

    ###Solution 2###
    #https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/100268/Two-solutions-and-thoughts
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            print(Codec.alphabet)
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


if __name__ == "__main__":
    x = Codec()
    shortUrl = x.encode("https://medium.com/@roger35972134/leetcode-535-encode-and-decode-tinyurl-90113d08b1c")
    print(shortUrl)
    print(x.decode(shortUrl))
