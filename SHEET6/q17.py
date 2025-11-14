#  Akash likes playing with strings. One day he thought of applying following operations on the
#  string in the given order:
#  Concatenate the string with itself.
#  Delete all the uppercase letters.
#  Replace each vowel with '#'.
#  You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the
#  resultant string after applying the above operations.
#  NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
#  Input:
#  A="aeiOUz"
#  Output:
#  "###z###z
s=input()
r= s+s
p="" 
for i in r:
    if not i.isupper():
        if i in "aieou":
            p+="#"
        else:
            p+=i
      
print(p)
    