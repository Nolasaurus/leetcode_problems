class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        while ransomNote: #while len > 0
            spl_str = [*ransomNote]
            letter = spl_str.pop() #remove each letter of ransom
            if letter not in magazine: #if letter not in magazine
                return False
            else:
                    #delete letter in both ransomNote and magazine
                    #find letter in magazine
                    index = magazine.find(letter)
                    #delete that letter from magazine
                    magazine = magazine[0:index]+magazine[index+1:]
                
                #loop ends. go to top

            ransomNote = spl_str
            
        return True
        
tester = Solution()

rNotes = ['a','aa', 'aa', 'faang', 'square']
magz = ['b','ab', 'aab', 'fang', 'sqquare']
corr = [False, False, True, False, True]
for i in range(len(rNotes)):
    print("next case")
    print(tester.canConstruct(rNotes[i], magz[i]))