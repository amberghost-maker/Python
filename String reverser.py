class WordReverser:
 
    
    def reverse_words(self, sentence: str) -> str:
   
        if not sentence:
            return ""
        
        words = sentence.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == "__main__":
    reverser = WordReverser()
    
    print(reverser.reverse_words("hello world"))         
    print(reverser.reverse_words("  python   is   fun  ")) 
    print(reverser.reverse_words("single"))               
    print(reverser.reverse_words(""))                     