import sys
try:
    v = int(input('digit: '))
except ValueError:
    sys.exit(1)
else:
    print(bin(v))  
    print(hex(v))  
    print(oct(v))  
