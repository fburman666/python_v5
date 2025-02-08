from logging import NullHandler

def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32

#########################################
#uppgift 2.2c
def count_words(sentence):
    if sentence == "":
        return 0
    word_list = sentence.split(" ")
    sum = 0
    for word in word_list:
        sum += 1
    return sum

########################################
#uppgift 2.3
def find_median(numbers):
    if numbers == []:
        return []
    else:
        short_list = numbers[1:-1]
        if short_list == []:
            return numbers
        else:
            return find_median(short_list)

#print(f"Funktionen returnerade {find_median([1, 4, 7, 9, 1000])}")

#######################################
#2.4
def is_sorted_ascending(numbers):
    return True

##############################################
# Söka efter en användare
import re
def autocomplete_list(input, master_list):
    for element in master_list:
        if re.match(input, element):
         #   print(f"Match!")
            return element
    return 0
#print(autocomplete_list("a", ["lejon", "apa", "gris"]))

############################################
#multiplikationstabellen
def muliplication_table(n, limit):
    index = 1
    result_list = []
    while index <= limit:
        result_list.append(n * index)
        index += 1
    return result_list
#print(muliplication_table(4, 4))

#############################################
#Balansera listor
import math
def list_balancer(list1, list2):
    while abs(len(list1) - len(list2)) > 1:
        if len(list1) > len(list2):
            list2.append(list1.pop(0))
        else:
            list1.append(list2.pop(0))

    return [list1, list2]

#longlist = [1,2,3,4,5,6,67,78,99]
#shortlist = [12,45, 67]
#print (list_balancer(longlist, shortlist))
