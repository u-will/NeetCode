Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def hashMaker(vals):
            hashMap = {}
            for val in vals:
                if val in hashMap:
                    hashMap[val] += 1
                else:
                    hashMap[val] = 1
            return hashMap
        
        def checker(hashA, hashB):
            if len(hashA) != len(hashB):
                return False

            for val in hashA.keys():
                if val not in hashB:
                    return False
                if hashA[val] != hashB[val]:
                    return False
            return True

        hashMapS = hashMaker(s)
        hashMapT = hashMaker(t)
        print(hashMapS)
        print(hashMapT)
        return checker(hashMapS, hashMapT)
