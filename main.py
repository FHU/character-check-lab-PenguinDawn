def check_character(word, index):
   chari = word[index]
   typing = ""

   #statements
   
   if chari.isspace():
       typing = "whitespace"
   elif chari.isdigit():
       typing = "digit"
   elif chari.isalpha():
       typing = "letter"
   else:
       typing = "unknown"
   
   return typing

          




if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))