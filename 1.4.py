a)
T(n) = | 1,            n<=a, a>0
       | T(n - a) + 1, n > a

n > a
T(n) = T(n - 2a) + 1 +1 = T(n-2a) +2
T(n) = T(n-3a) +3
T(n) = T(n-ka) +k
n-ka<= a закінчення рекурсії тобто n-ka = a закінчення => k = (n-a)/a = n/a -1
=> T(n) = 1+k  = 1  + n/a-1 = n/a



b)
T(n) = | 1,               n = 0
       | 2T(n - 1) + 2^n, n >= 1


T(n) = 2 T(n - 1) + 2^n =
     =  2T(n-2) + 2^(n-1) =
     = 2 (2T(n-2 )+ 2 ^(n-1) +  2^n=
     = 4 T(n-2) + 2 * 2 ^n =
     = 4(2T(n-3)+2^(n-2)) + 2*2^n =
     = 8T(n-3) + 4 * 2^(n-2) + 2 * 2^n=
     = 8T(n-3) + 2^n + 2*2^n =
     = 8 T(n-3) + 3 * 2^n=
     = 2^kT(n-k) sum((i = 0, k-1) 2^(n-1)=
     = 2n * sum((i = 0, n-1) 2^(-i)


c)
T(n) = | 1,            n = 1
       | 2*T(n/2) + 1, n >= 2

T(n) = 2T(n/2) + 1 =
T(n/2)= 2T(n/4) +1=
     = 2(2T(n/4)+1) +1 = 4T(n/4) + 3 =
T9n/4= 2T(n/8) + 1 =
     = 4(2T(n/8)=1)  + 3= 8T(n/8) + 7
     = 2^k(n/2^k) + (2^k -1) =
T(n)= 2^(lognT(1) ) 2^(log)-1) = 2n-1


d)
T(n) = | 1,            n = 1
       | T([n/a]) + n, n >= 2, a >= 2


n = a^m -> m = log_a(n)

T(n) = T([n/a]) + n = T(a^{m-1}) + 1 =
     = T(a^{m-2}) + 1 + 1 =
     = T(a^{m-3}) + 1 + 1 + 1 =
     = T(a^{m-3}) + 3 =
     = T(a^{m-k}) + k =
     = T(a^{m-m}) + m = T(1) + m = m + 1 =
     = log_a(n) + 1