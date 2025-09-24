strIP   = '192.168.1.10'
intCIDR = 24


intIP = int.from_bytes(bytes([int(x) for x in strIP.split('.')]) ,'big')

intMascara = 0xFFFFFFFF >> (32 - intCIDR) << (32 - intCIDR)
print(intIP)
print(intMascara)