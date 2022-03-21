import time

def collatz(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n+1
        sequence.append(n)
    return sequence
    
start = time.time()

maior = 1
list = []
for i in range(1, 10000001):
    L = collatz(i)
    if len(L) > maior:
        maior = len(L)
    list = L
    
final = time.time()

print(list)
print()
print('Tamanho: %d' %maior)
print('Tempo: %f' %(final - start))