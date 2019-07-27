"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. 
For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). 
We'll call such a concatenation, the transformation of a word.
"""

Return the number of different transformations among all words we have.
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        def letter_to_morse(l):
            abc = {
            "a":".-",
            "b":"-...",
            "c":"-.-.",
            "d":"-..",
            "e":".",
            "f":"..-.",
            "g":"--.",
            "h":"....",
            "i":"..",
            "j":".---",
            "k":"-.-",
            "l":".-..",
            "m":"--",
            "n":"-.",
            "o":"---",
            "p":".--.",
            "q":"--.-",
            "r":".-.",
            "s":"...",
            "t":"-",
            "u":"..-",
            "v":"...-",
            "w":".--",
            "x":"-..-",
            "y":"-.--",
            "z":"--.."
            }
            out = abc[l]
            return out

        morses = []
        for word in words:
            morse = []
            for l in word:
                morsestr = letter_to_morse(l)
                morse.append(morsestr)
            morses.append(''.join(morse))

        return (len(set(morses)))
