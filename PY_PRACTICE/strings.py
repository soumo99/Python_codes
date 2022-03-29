word = "St Thomas Boys School"
#string slicing
print(word[1:5])
print(word[:5])
print(word[2:])
print(word[-4:-2])

#changing to upper and lower case by using functions
print(word.lower())
print(word.upper())

#removing white space
print(word.strip())

#Split the string in the form of a list
print(word.split(","))

#Returns the length of the string
print(len(word))

#checking present or not
if "geeks" in word:
    print("Hola, yes the word is present")
else:
    print("Sorry , the word is not present")

if "apple" in word:
    print("Hola, yes the word is present")
else:
    print("Sorry , the word is not present")


#loops
for x in word:
    print(x, end=" ")

#replacing a letter with another letter
print(word.replace("s","S"))


#String contatenation
word_1 = "Geeks"
word_2 = "for"
word_3 = "geeks"
final_word = word_1 + " " + word_2 + " " + word_3
print(final_word)

#String Formatting
name = "Soumobrata"
standard = 12
subject = "Maths"
marks = 99

order = "Student",name,"of {} got {} in ",subject
print(order.format(name,standard,marks,subject))
