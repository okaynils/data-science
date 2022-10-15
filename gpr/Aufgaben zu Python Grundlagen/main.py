# Aufgaben zu Python Grundlagen
# -> https://spaces.technik.fhnw.ch/storage/uploads/mml/2022/09/Python-Grundlagen-1664293129.pdf

import turtle as t

# Aufgabe 4 – Slicing mit Strings
def rotate_left_str(s, n):
    return s[n:]+s[:n]

def move2_str(s):
    even = ''
    uneven = ''
    for i in range(len(s)):
        if i%2==0 or i==0:
            even += s[i]
        else:
            uneven += s[i]
    return even+uneven

# Aufgabe 5 – str.count('x') selbst programmiert
def str_count(string, pattern):
    number = 0
    current_pointer = 0
    for i in range(len(string)):
        if string[i] == pattern[current_pointer]:
            current_pointer += 1
            if current_pointer == len(pattern):
                number += 1
                current_pointer = 0
    return number

def str_count_any(string, pattern):
    count = 0
    for i in range(len(string)):
        for x in range(len(pattern)):
            if string[i] == pattern[x]:
                count += 1
    return count

# Aufgabe 6 –max(lst) selbst programmiert
def max_index(list):
    newest_max = 0
    index_of_max = 0
    for i in range(len(list)):
        if list[i] >= newest_max:
            newest_max = list[i]
            index_of_max = i
    return index_of_max

# Aufgabe 7 – String-Zerlegung
def split_into_list(string):
    return string.replace(":","").replace("-"," ").split(" ")

# Aufgabe 8 – Liste aller ganzen Zahlen i < N, bei denen i^2 mod 5 = 4
def get_numbers(n):
    list = []
    for i in range(0,n):
        if i**2%5 == 4:
            list.append(i)
    return list

# Aufgabe 9 – Turtle-Programm-Interpreter
def turtle_interpret(instructions):
    for i in instructions:
        t.left(i[0])
        t.forward(i[1])
    t.done()

# Aufgabe 10 – Kaprekar-Zahlen
def kaprekar_num(number,iteration):
    if number == 6174:
        return ('Found 6174 after '+str(iteration)+' iterations.')
    else:
        while len(str(number)) < 4:
            number = "0" + str(number)
        res = int("".join(sorted(str(number), reverse=True))) - int("".join(sorted(str(number))))
        return kaprekar_num(res,iteration+1)