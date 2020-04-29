import random
import math

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encoder(word):
    encoded_word = ''
    for i in word:
        num = math.floor(random.random() * 26)
        print(num)
        encoded_word = encoded_word + alphabet[num]

    print (encoded_word)

encoder('pie')
