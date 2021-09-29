#Problem 1
def power(a, b, n):
    '''compute a**b (mod n)'''
    b1 = bin(b).replace("0b","") #change b into binary
    b1 = (str(b1))[::-1] #reverse b1

    mod = [a % n] #initial value
    i = 1
    while i < len(b1):
        mod.append(mod[i-1]**2 % n) #square the previous element and take its mod
        i += 1

    product = 1

    j = 0
    while j < len(str(b1)):
        if int(b1[j]) != 0: #check if the digit is 1
            product = product * mod[j] % n
        j += 1

    return product

print(power(6, 73, 11))
print(power(2, 1234567890, 1234567891))



#Problem 2
def gcd_it(a,b):
  if a==0 and b==0:
    raise Exception("Error: a and be cannot both be zero")
  while a % b != 0:
    r = a % b
    a = b
    b = r
  return abs(b)

def eulerphi(n):
    rel_pri = []
    for i in range(1, n):
        if gcd_it(i, n) == 1:
            rel_pri.append(i)
    return len(rel_pri)

print(eulerphi(11))
print(eulerphi(56))
print(eulerphi(120))

#if p is prime, ϕ(p) = p - 1



#Problem 3
def order(a, n):
    if gcd_it(a, n) != 1:
        raise Exception("Error: Number not relatively prime to modulus")
    else:
        i = 1
        t = a % n #temporary variable
        while t != 1:
            t = t * a % n
            i += 1
        return i

print(order(4, 11))
print(order(33, 56))
print(order(7, 120))



#Problem 4
def gen(n):
    i = 2
    while i < n:
        if gcd_it(i, n) == 1 and order(i, n) == eulerphi(n):
            '''see if i and n are relatively prime and order of i (mod n) is equal to the order of Z mod n Z'''
            return i
        i += 1
    return False

for k in range(2, 100):
    print(k, gen(k))
