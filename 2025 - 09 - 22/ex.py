import sys
try:
    v = int(input('digite: '))
except ValueError:
    sys.exit('errou')
except KeyboardInterrupt:
    sys.exit('errou')
except Exception as e:
    sys.exit(f'errou {e}')
else:
    if v <= 0:
        sys.exit(1)

b = v.bit_length()
print(b)

print(f'\n{v} em binarios: {bin(v)}\n')
bv = bin(v)[2:]

zeros = 0
if len(bv) % 8 != 0:
    zeros = 8 - len(bv) % 8

bv = ('0' * zeros) + bv

print(f'\n{v}....ob{bv}\n')

     