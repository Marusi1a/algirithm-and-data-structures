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
n = 3, m= 1 -> loop block: 0

#c
i = 0 #/ 2
while i < n:#/3 *
    j = 0 #/
    while j < n #/
        k += 2 /#4*
        j += 2 /  # 4*
    i += 2 #/4*

#d
i = 0
while i < n:
    j = 0
    while j < i*i:
        k += 1
        j += 1
    i += 1

#e
i = 1 #/ 2
while i < n: #/ 3*
    j = 1 #/ 2*
    while j < n: #/3*
        k += 1 #/4*
        j *= 2 #/4*
    i *= 2 #/4*

#f
i = 1 #/2
while i < n: #/3*
    j = i #/2*
    while j < n: #/3*
        k += 1 #/4*
        j *= 3 #/4*
    i *= 2 #/4*