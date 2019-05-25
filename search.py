import sys
import re
import itertools
import requests

print("Starting...")

f = open('brut.txt', 'w')

#strone = sys.argv[1]
strone = "gitter*ub*er"
sym = ['h', 'b', 'a']

itog = []

def count_words(text, words):
    return len(text.split(words))-1
 
def join(arr, sq):
    #del arr[-1]
    pr = ""
    for s in arr:
        pr += s + sq
    return pr
    
def repl(arr, star, new):
    del arr[-1]
    q = 0
    for s in arr:
        if s == star:
            arr[q] = new
    q += 1        
    return arr 
    
def remov(arr, elem):
    q = 0
    for s in arr:
        if s == elem:
            del arr[q]
    q += 1        
    return list(arr)
    
def rep(strr, star, new, ind):
    arr = strr.split(star)
    arr[ind] = arr[ind] + new + arr[ind+1]
    del arr[ind+1]
    return join(arr, star)[:-1]
    
def reparr(strr, star, new, inde):
    arr = strr.split(star)
    for ind in inde:
        arr[ind] = arr[ind] + new + arr[ind+1]
        del arr[ind+1]
    return join(arr, star)[:-1]
 
def isarray(array, key):
    for item in array:
        if item == key:
            return True
    return False
    
#print("Всего доступно " + str(count_words(strone, '*') ** len(sym)) + " решений")
print("Начинаю перебор...")

print("Алгоритм 1:")
r = 0
pr = ""

for w in sym:
    r = 0
    for s in strone:
        if s == '*':
            for wa in sym:               
                #print(strone[0:r].replace(s, wa) + strone[r:].replace(s, w))
                itog.append(strone[0:r].replace(s, wa) + strone[r:].replace(s, w))
            
        r += 1
print("Выполнено") 

print("Алгоритм 2:")

for w in sym:
    pr = strone.replace('*', w)
    for wa in sym:
        for s in range(count_words(strone, '*')):    
            #print(rep(pr, w, wa, s))
            itog.append(rep(pr, w, wa, s))
print("Выполнено") 
    
print("Алгоритм 3:")

for w in sym:
    pr = strone.replace('*', w)
    
    for wa in sym:
        for s in range(count_words(strone, '*')):
            for sa in range(count_words(strone, '*')-1):        
                #print(reparr(pr, w, wa, [s, sa]))
                itog.append(reparr(pr, w, wa, [s, sa]))
print("Выполнено")                

print("Найденно " + str(len(itog)) + " вариантов страниц")
print("Найденно " + str(len(list(set(itog)))) + " уникальных вариантов страниц")

itog = list(set(itog))

for item in itog:
    f.write(item + "\r\n")
    
f.close()

print("Начать поиск?")
input()
print("Начинаю поиск в Instagram...")

naided = []

for s in itog:
    print("--------------------")
    print("Страница "+s)
    r = requests.get('https://instagram.com/'+s)
    if r.status_code == 404:
        print("Страницы не существует")
    else:
        print("Страницы найдена")
        naided.append(s)
    print("--------------------")

print("Найдено "+str(len(naided)) + " страниц")
f = open('account.txt', 'w')
for nai in naided:   
    f.write(nai)
    print(nai)
f.close()
#input()