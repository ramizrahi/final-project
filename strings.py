"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""


def no_duplicates(a_string):
    a_string = sorted(set(a_string))
    print(''.join(a_string))
    pass


def reversed_words(a_string):
    print(a_string.split(" ")[::-1])
    pass


def four_char_strings(a_string):
    devided = [a_string[i:i+4] for i in range(0, len(a_string), 4)]
    print(devided)
    pass