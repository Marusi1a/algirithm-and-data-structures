#a
k += 1 #/4
i = n  #/2
while i > 0: #/3*(n+1)
    i -= 1  #/4*n

sum = 7n + 9

#b
i = n #/2
while i > 1: #/3* (m+1)
    k += 1 #/4 *m
    i //= 2 #/4*m

1)n = 2^m -> m = log(n)
n = 1, m= 0 -> loop block: 0
n = 2, m= 1 -> loop block: 1
n = 4, m= 2 -> loop block: 2
n = 8, m= 3 -> loop block: 3
n = 2*m, m= 2 -> loop block: m

sum = 11*m + 5 = 11*log(n) + 5

2) n = 2 ^m + b? 0< b <2^m ->m = log(n-b) =floor(log(n))


#c
i = 0 #/ 2
while i < n:#/3 * (n+1)
    j = 0 #/2*n
    while j < n: #/3*n*(n+1)
        k += 2 /#4*n*n
        j += 2 /  # 4*n*n
    i += 2 #/4*n
sum = 11*n^2 + 12*n + 5

#d
i = 0 #/2
while i < n: #/3*(n+1)
    j = 0 #/2*n
    while j < i*i: #/5*(n-1)*n*(2*n-1)/6
        k += 1 #/4*(n-1)*n*(2*n-1)/6
        j += 1 #/4*(n-1)*n*(2*n-1)/6
    i += 1 #/4*n
#сума квадратів перших n натуральних чисел
sum = 8,66*n^3 + 13*n^2 + 13,16*n + 5
    
#e
i = 1 #/ 2
while i < n: #/ 3*(m+1)
    j = 1 #/ 2*m
    while j < n: #/3*(m+1)*m
        k += 1 #/4*m^2
        j *= 2 #/4*m^2
    i *= 2 #/4*m
sum = 11*(log(n))^2 + 12*log(n) + 3

n = 2^m -> m = log(n)
n = 1, m= 0 -> loop block: 0
n = 2, m= 1 -> loop block: 1
n = 4, m= 2 -> loop block: 2
n = 8, m= 3 -> loop block: 3
n = 2*m, m= 2 -> loop block: m

#f
i = 1 #/2
while i < n: #/3*(m+1)
    j = i #/2*m
    while j < n: #/3*(p+1)m
        k += 1 #/4*p*m
        j *= 3 #/4*p*m
    i *= 2 #/4*m
sum = 11*log3(n/(log(n))^2) + 12*log(n) + 2

n = 2^m -> m = log(n)
p = log3(n/2^m)
n = 1, m= 0 -> loop block: 0
n = 2, m= 1 -> loop block: 1
n = 4, m= 2 -> loop block: 2
n = 8, m= 3 -> loop block: 3
n = 2*m, m= 2 -> loop block: m
