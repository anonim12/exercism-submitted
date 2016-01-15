# -*- coding: utf-8 -*
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    catch = ""
    c= 0
    for word in sentence:
        for letter in alphabet:
            if word == letter and word not in catch:
             catch += word
    for char in catch:
        for letter in alphabet:
            if char == letter:
                c += 1
    if c >= 26:
        return True
    else:
        print catch, alphabet, c
        return False


#ALTERNATIVE
#from string import ascii_lowercase
#
#
# def is_pangram(sentence):
#    return all(char in sentence.lower() for char in ascii_lowercase)
