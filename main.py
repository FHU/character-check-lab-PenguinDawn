def check_character(word, index):
   chari = word[index]
   typing = ""

   #statements here
   
   if chari.isspace():
       typing = "white space"
   elif chari.isdigit():
       typing = "digit"
   elif chari.isalpha():
       typing = "letter"
   else:
       typing = "unknown"
   #end
   return typing

          


#checks

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))