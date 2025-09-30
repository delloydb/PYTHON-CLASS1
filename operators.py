# comparision operators

a = 10
b = 20
print("a =", a)
print("b =", b)
print("a == b:", a == b)  # equal
print("a != b:", a != b)  # not equal
print("a > b:", a > b)  # greater than
print("a < b:", a < b)  # less than
print("a >= b:", a >= b)  # greater than or equal to
print("a <= b:", a <= b)  # less than or equal to


# logical operators
x = True
y = False
print("x =", x)
print("y =", y)
print("x and y:", x and y)  # logical AND
print("x or y:", x or y)  # logical OR
print("not x:", not x)  # logical NOT
print("not y:", not y)  # logical NOT


# arithmetic operators
m = 15
n = 4
print("m =", m)
print("n =", n)
print("m + n:", m + n)  # addition
print("m - n:", m - n)  # subtraction
print("m * n:", m * n)  # multiplication
print("m / n:", m / n)  # division
print("m // n:", m // n)  # floor division
print("m % n:", m % n)  # modulus
print("m ** n:", m**n)  # exponentiation


# assignment operators
p = 5
print("Initial p =", p)
p += 3
print("p after p += 3:", p)  # p = p + 3
p -= 2
print("p after p -= 2:", p)  # p = p - 2
p *= 4
print("p after p *= 4:", p)  # p = p * 4
p /= 3
print("p after p /= 3:", p)  # p = p / 3
p //= 2
print("p after p //= 2:", p)  # p = p // 2
p %= 3
print("p after p %= 3:", p)  # p = p % 3
p **= 2
print("p after p **= 2:", p)  # p = p ** 2


# bitwise operators
u = 6  # in binary: 110
v = 3  # in binary: 011
print("u =", u)
print("v =", v)
print("u & v:", u & v)  # bitwise AND
print("u | v:", u | v)  # bitwise OR
print("u ^ v:", u ^ v)  # bitwise XOR
print("~u:", ~u)  # bitwise NOT
print("u << 1:", u << 1)  # left shift
print("u >> 1:", u >> 1)  # right shift


# membership operators
my_list = [1, 2, 3, 4, 5]
print("my_list =", my_list)
print("3 in my_list:", 3 in my_list)  # membership test
print("6 in my_list:", 6 in my_list)  # membership test
print("3 not in my_list:", 3 not in my_list)  # membership test
print("6 not in my_list:", 6 not in my_list)  # membership test


# identity operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("list1 =", list1)
print("list2 =", list2)
print("list3 =", list3)
print("list1 is list2:", list1 is list2)  # identity test
print("list1 is list3:", list1 is list3)  # identity test
