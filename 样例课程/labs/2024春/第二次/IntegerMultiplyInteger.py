def classic_big_integer_multiply_big_integer(x: str, y: str) -> str:
    x = x[::-1]
    y = y[::-1]
    result = [0] * (len(x) + len(y))
    for i in range(len(x)):
        for j in range(len(y)):
            result[i+j] += int(x[i]) * int(y[j])
            result[i+j+1] += result[i+j] // 10
            result[i+j] %= 10
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return ''.join(map(str, result[::-1]))


def Karatsuba_integer_multiply_integer(x: str, y: str):
    n = max(len(x), len(y))
    m = n//2
    a = x[:-m]
    b = x[-m:]
    c = y[:-m]
    d = y[-m:]
    a, b, c, d = int(a), int(b), int(c), int(d)
    ac = a*c
    bd = b*d
    ad_bc = (a+b)*(c+d)-ac-bd
    return ac*10**(2*m)+ad_bc*10**m+bd


print(classic_big_integer_multiply_big_integer("123", "456"))
print(Karatsuba_integer_multiply_integer("123", "456"))
