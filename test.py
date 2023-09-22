from vritools.mutation_code import parse_mutation_code as mc

mutation = mc("G123C")
a, b, c = mutation.as_tuple()

x = mutation.wtres
y = mutation.pos
z = mutation.msres

print(a)  # G
print(b)  # 123
print(c)  # C
print("\n")
print(x)  # G
print(y)  # 123
print(z)  # C