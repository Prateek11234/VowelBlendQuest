#get sentence from user

sentence=input("tell me the sentence..? ").strip().lower()

#split sentence into words

#for word in sentence:         #=way to move through every word in a single line code
#    print(word)

words = sentence.split()  #way to split all the words in the sentence

#loop through words and convert to pig latin

newwords = []

for word in words:
    # print(word)
    if word[0] in "aeiou":
        newword = word + "yay"
        newwords.append(newword)
    else:
        vowelspos = 0
        for letter in word:
            if letter not in "aeiou":
                vowelspos = vowelspos + 1
            else:
                break       #break statement is the one which is used to break the loop here the loop breaks due to use  of break statement and for loop ends
#and theere is another statement like this which is continue which does work oppositw to break statement that is break statement breaks the loop while the continue statement continues the loop
        cons = word[:vowelspos]
        therest = word[vowelspos:]
        newword = therest + cons + "ay"
        newwords.append(newword)

#print(newwords)
            
#if starts with vowel, just add yay

#otherwise ,move the first consonant cluser to end and add ay

#stick words back together

output = " ".join(newwords)           #this join keyword joins all the words or string in a list
#output the final string

print(output)
