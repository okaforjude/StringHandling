
# The programme reads a string and makes each alternate character an UPPERCASE character and each other alternate character a lowercase character.
# Then, starting with the same string but making each alternative word lower and upper case

string = ("I am on a data science bootcamp")

new_string = " "

final_string = " "


for i in range(len(string)):
    
    if i % 2 == 0: 
      new_string += string[i].upper()

    else:
       new_string += string[i].lower()

print(new_string)


split_string = string.split()


for i in range(len(split_string)):
   if i % 2 == 0:
      final_string += split_string[i].lower() + " "

   else:
      final_string += split_string[i].upper() + " "

print(final_string)
