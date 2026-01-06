#Int 1231241 -3232 Float 1234.9 -2.2 String 'hello' "hello" "2.3" bool true 1 flase 0
print('   /|')
print('  / |')
print(' /  |')
print('/___|')
#shape





#variables
character_name = 'John'
character_age = '35'
is_male = True




#data types
print('You have 20 feet from ' + character_name +'.')
print( character_name + ' enjoys his space.')
print(character_name + ' is ' + character_age +'.')
print('You have 15 feet from ' + character_name +'.')
print(character_name + ' is getting closer.')
print('He loves his visitors.')
print('He sees you now.')
print('You have 10 feet from ' + character_name +'.')
print('You ask to see him now.')
print('He agrees.')





#strings
print('Giraffe\nAcademy')
phrase = 'Gumbo'
print(phrase + ' is good')




#function
print(phrase.upper())
print(phrase.lower().islower())
print(phrase.isupper())




#length of a str
print(len(phrase))




#find char in str 01234=gumbo 0=g
print(phrase[0])




#give number value of selected letter
print(phrase.index('G'))




#replace letters/words
print(phrase.replace("G", "W"))




#working with numbers
print(2.0987)
print(3 * 4 + (4 * 5))




#finding the remainder
print(10 % 3)



#printing numbers with strings
my_num = 5
print(str(my_num) + " is my fav number")



#finding absolute value
my_new_num = -10
print(abs(my_new_num))


print(pow(3, 10)) #3^10

print(max(4, 6, 100)) #gives you the biggest num max(1,2,3)=3

print(round(3.6)) #rounding up from 4 down or 5 up

from math import *
#^ acessing the math code for advanced math


#grab lowest num if 3.6=3
print(floor(3.6))

print(ceil(3.6)) #always round up if 3.1=4 or 3.8=4

print(sqrt(36)) #sqare root



#user input
user_nm = input('What is your name?  ')
user_age = input('What is your age?  ')
print('hello ' + user_nm)
print('you are ' + user_age + ' years old')


#lists
lucky_numbers = [4,2,1]
lucky_people = ["kelly", " barb", "Jahlet"]


print(lucky_people.extend(lucky_numbers))




