from inputimeout import inputimeout,TimeoutOccurred
import random
import sys
##################
dictionary_file=open("dictionary.txt","r")
dictionary1=dictionary_file.readlines()
dictionary2=[]
comp_word=""
user_word=""
user_last_char=""
comp_last_char=""
user_score=0
timeout=10
while True:
    try:
        rounds=int(input("how many rounds?"))
        break
    except ValueError:
        print("invalid")
        print("try again")
        print()
print("start)
print()

for x in dictionary1:
      word=x.replace("\n","")
      dictionary2.append(word)
      for x in range(0,rounds,1):
            if x==0:
                 comp_word=random.choice(dictionary2)
                 comp_last_char=comp_word[-1]
                 print("comp>>",comp_word)
            else:
                possible_comp_words=list
