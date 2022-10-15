# Modulschlussprüfung Dump

# Aufgabe 1c
lst = [[1, 2, 3], [4, 5], [6]]
lst[2].append(len(lst[-1]))
print(lst) # Ergibt [[1, 2, 3], [4, 5], [0, 6]]

l2 = lst[1]
l2[0] = 0
del lst[0]
print(l2) # Ergibt [0, 5]

print(lst) # Ergibt [[1, 2, 3], [0, 5], [0, 6]]

#Advent of Code 2020, Day 1
file = open('aoc_input.txt');
list = []
for line in file:
    list.append(int(line.replace(line[-1],"")))
    for item in list:
        for item1 in list:
            if item+int(line.replace(line[-1],""))+item1 == 2020:
                print('its', item*int(line.replace(line[-1],""))*item1, 'gives: ', item+int(line.replace(line[-1],""))+item1)
                break;

print(list)