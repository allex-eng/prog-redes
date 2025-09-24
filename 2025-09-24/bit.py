intCIDR = 24

intMascara = 0xFFFFFFFF >> (32 - intCIDR)

intMascara = intMascara << (32 - intCIDR)

print(intMascara)

# Será impresso -> 4294967040 (4.294.967.040)