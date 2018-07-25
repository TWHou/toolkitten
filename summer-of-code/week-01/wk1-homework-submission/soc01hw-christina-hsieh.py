import random

### Day 1 ###

hours = 24 * 365
print(f'There are {hours} hours in a year.')

minutes = 10 * hours * 60
print(f'There are {minutes} minutes in a decade.')

seconds = 33 * hours * 60 * 60
print(f'I am {seconds} seconds old.')

andreea = 48618000 / 60 / 60 / 24 / 365
print(f'Andreea is {andreea} years old.')

# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
# How about a 64-bit system?
# Calculate your age accurately based on your birthday (maybe use time of day
# e.g. 8:23am if you know it, use 12:00 noon midday) - you will need Python modules.

### Day 3 ###

first = input("What is your first name? ")
middle = input("What is your middle name? ")
last = input("What is your last name? ")
print(f'Hello, {first} {middle} {last}')

fav = input("Tell me your favorite number: ")
print(f'Wouldn\'t you consider {int(fav) + 1} as a bigger, better number?')

emp = input("The Hell You Want?! ")
print(f'WHADDAYA MEAN "{emp.upper()}"?!? YOU\'RE FIRED!!')

print('Tale of Contents'.center(60))
print('Chapter 1: Getting Started'.ljust(53) + 'page 1')
print('Chapter 2: Numbers'.ljust(53) + 'page 9')
print('Chapter 3: Letters'.ljust(53) + 'page 13')

### Day 4 ###

bottles = 100
while bottles > 0:
  print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.')
  bottles -= 1
  print(f'Take one down, pass it around, {bottles} bottles of beer on the wall...')
print('No more bottles of beer on the wall, no more bottles of beer.')
print('Go to the store and buy some more, 99 bottles of beer on the wall...')

def grandma(bye):
  say = input('Say something to Grandma: ')
  if say == "BYE":
    bye += 1
    if bye == 3:
      print('BYE DEAR')
      return
    else:
      return grandma(bye)
  elif say.isupper():
    print(f'NO, NOT SINCE {random.randint(1930,1950)}')
    return grandma(0)
  else:
    print('HUH?! SPEAK UP, GIRL!')
    return grandma(0)

grandma(0)

def leap_counter():
  start = int(input('Enter start year: '))
  end = int(input('Enter end year: '))
  for i in range(start, end + 1):
    if i % 4 == 0:
      if i % 100 == 0:
        if i % 400 == 0:
          print(i)
      else:
        print(i)

leap_counter()

def binge():
  hours = int(input('How many hours do you have? '))
  print(f'You might be able to sqeeze in {hours * 2} episodes.')

binge()

def sort_words(words = []):
  word = input('Give me a word: ').strip()
  if word:
    words.append(word)
    return sort_words(words)
  else:
    words.sort()
    print(words)
    return

sort_words()
