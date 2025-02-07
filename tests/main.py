from src.functions import *

#Uppgift 2.1a
#testdata:
#C=37 grader motsvarar ca F=100 grader
#C=0 grader motsvarar F=32 grader
#
#Uppgift 2.1b
#ekvivalensklasser för degree:
#<-273.15 och >-273.15

#Uppgift 2.1c
def test_37_point_8c_to_f():
    assert int(c_to_f(37.8)) == 100

def test_0c_to_f():
    assert c_to_f(0) == 32

#uppgift 2.2: test av count_words(sentence)
#funktionen ska returnera antalet ord i en sträng på 20 ord separarade av mellanslag
#funktionen ska returnera "0" om strängen är tom
#

def test_count_20words():
    assert count_words("hej på dig din ost hej på dig din ost hej på dig din ost hej på dig din ost") == 20

def test_count_0words():
    assert count_words("") == 0



#uppgift 2.3a: AK för funktionen: find_median(numbers)
#Om en lista har udda antal element ska det mittersta returneras
#Om en lista har jämnt antal element ska de två mittersta returneras
#Om en lista är tom ska funktionen returnera [] (tom lista)

def test_find_median_odd():
    assert find_median([1,4,7,9,1000]) == [7]

def test_find_median_even():
    assert find_median([0,1,4,7,9,1000]) == [4,7]

def test_find_median_empty():
    assert find_median([]) == []


#uppgift 2.4
#2.4a ekvivalensklasser: True/False
#krav1: Om listan (argumentet) är sorterad i stigande ordning skall funktionen returnera True
#krav2: Om listan (argumentet) inte är sorterad i stigande ordning skall funktionen returnera False
#krav3: Om listan (argumentet) är tom skall funktionen returnera False
def test_is_sorted_ascending_true():
    assert is_sorted_ascending([1,2,3,4,5,17]) == True

#def test_is_sorted_ascending_false():
 #   assert is_sorted_ascending([1, 2, 3, 4, 17, 5]) == False

#def test_is_sorted_ascending_empty():
#    assert is_sorted_ascending([]) == False

######################################
#Tänk dig en funktion som kan användas för att visa sökresultat medan användaren skriver i ett sökfält.
# Funktionen ska ta två parametrar: input är det användaren skriver,
# master_list är en lista med alternativ som kan hittas
#krav1: funktionen ska göra autocomplete för en bokstav som återfinns i listan
#krav2: funktionen ska klara matchning med flera bokstäver

def test_autocomplete_list_one_char():
    assert autocomplete_list("a", ["lejon", "apa", "gris"]) == "apa"

def test_autocomplete_list_many_chars():
    assert autocomplete_list("ar", ["lejon", "apa", "ara", "gris"]) == "ara"

###############################
# Multiplikationstabellen
#krav1: fkn ska returnera en lista med multiplikationstabellen för argument #1
#krav2: längden på resultatlistan definieras av argument #2

def test_muliplication_table_4table():
    assert  muliplication_table(4, 4) == [4, 8, 12, 16]

def test_muliplication_table_size():
    assert  len(muliplication_table(17, 300)) == 300

