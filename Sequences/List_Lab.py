#!/usr/bin/env python

#Series 1
og_fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits = og_fruits[:]
print(fruits)

new_fruit = input("What fruit would you like to add: ")
fruits.append(new_fruit)
print(fruits)

user_number = int(input("Pick a number any number: "))

if user_number >= len(fruits):
    user_number = 0
    print("Longer than the list so Imma default it to the first one cause why not")
    print(user_number)
    print(fruits[user_number])
else:
    print(user_number)
    print(fruits[user_number])


#Series 2
fruits = og_fruits[:]
print(fruits)
del fruits[-1]
print(fruits)

to_delete = input("What fruit do you wanna delete: ")

for i in range(len(fruits)-):
    if to_delete == fruits[i]:
        del fruits[i]

#Series 3
fruits = og_fruits[:]


for i in range(len(fruits)-1):
    do_like = input("Do you like " + fruits[i].lower() + ": ")
    if do_like == "no":
        del fruits[i]
    elif do_like != "yes":
        print("Please say only yes or no")

print(fruits)


#Series 4
fruits = og_fruits[:]
fruits = [i[::-1] for i in fruits]

del og_fruits[-1]
print(og_fruits)
print(fruits)
