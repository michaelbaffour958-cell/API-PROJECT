# works = ['engineer','doctor','nurse','fireman']
# for job in works:
#     print(job)
#     if job == 'doctor':
#         break
    
       
# print('I just completed my loop lesson')

# languages = ['Swift', 'Python', 'Go']

# # start of the loop
# languages = ['French','Italian','German','Spanish']
# for lang in languages:
#     print(lang)
#     print('-----')
# # end of the for loop

# print('Last statement')

# Words = 'Trypanasomiasis'
# for word in Words:
#     if word == 'i':
#         continue
#     print(word)
     
# print('correct')

# values = range(0,7)
# for i in values:
#     print(i)

# number = int(input('Enter your number: '))

# while number >= 0:
#     print(f"You've entered the {number}" )
#     number = int(input('Enter your number: '))

# print('THE END')

# number = int(input('Enter your number: '))

# while number < 2:
#     print('This is inside loop')
#     number = int(input('Enter your number: '))
# else:
#     print('This is inside else block')

#Python programme to check Armstrong number
# number = int(input('Enter your number: '))

# for i in range(1,20):
#     print(number, 'x', i, '=', number*i )


#for loop to calculate the square of numbers
# numbers = [1,2,3,4,5]
# for num in numbers:
#     num = int(num * num)
#     print(num)

#for loop for adding the total
# numbers = [4, 8, 15, 16, 23, 42]
# total = 0
# for num in numbers:
#     total = total + num
#     print(total)

# #list of fruits and slicing
# fruits = ['mango','orange','pear']
# print('original list: ',fruits)
# fruits.append('mike')
# print('updated list: ',fruits)

# for loop that counts vowels
# words = 'programming'
# count = 0
# for word in words:
#     if word in ['a','e','i','o','u']:
#         count = count + 1
# print(count)

for nums in range(1,21):
    if nums % 3 == 0:
        continue

    if nums == 15:
        break
    print(nums)


    