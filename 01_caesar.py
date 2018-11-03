import string
list = string.ascii_lowercase
word = input("Enter a word : ")
if len(word)>0 and word.isalpha():
    count = 0
    i = 0
    ciper = ''
    while count < len(word):
        letter = word[count].lower()
        i = list.index(letter)

        if (i + 3)> 25 :
            i = -1 + (3 - (25 - i)) 
            
        else :
            i += 3     
        

        
        ciper = ciper + list[i]
        count += 1
    print("Encrypted word : " + ciper)

else :
    print("invalid")
        
