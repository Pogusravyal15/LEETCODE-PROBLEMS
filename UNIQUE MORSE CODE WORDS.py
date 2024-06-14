from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
       letters="abcdefghijklmnopqrstuvwxyz"
       moorse_code={'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
       morse_dict=dict(zip(letters,morse_code))
       words2=[]
       for word in words:
           k=""
           for i in word:
               k+=morse_dict[i]
               words2.append(k)
       return len(set(words2))
