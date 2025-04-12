from math import sqrt, ceil


def prime_divisor(divisor):
    num = 0
    if 2 in divisor: num += 1
    for b in range(len(divisor)):
        for c in range(2, ceil(sqrt(divisor[b])) + 1):
            if divisor[b] % c == 0:
                break
        else:
            num += 1
    return num


def find_divisor(store):
    divisor = [store]
    for a in range(2, int(store / 2) + 1):
        if store % a == 0:
            divisor.append(a)
    num = prime_divisor(divisor)         
    return num


store = list(range(10))

for i in store:
    store[i] = int(input())
    if store[i] == 1:
        store[i] = (store[i], 0)
    else:    
        store[i] = (store[i], find_divisor(store[i]))

sorted_store = sorted(store, key=lambda x: (x[1], x[0]))
print(sorted_store[9][0], sorted_store[9][1])