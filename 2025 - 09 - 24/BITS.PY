strIP = '192.168.1.10'

# --------------------------------------------------
# Gerando uma lista com 4 posições
# Cada posição é o inteiro correspondente a cada octeto do IP
lstIP = [int(x) for x in strIP.split(".")]
print(lstIP)

# Será impresso -> [192, 168, 1, 10]

# --------------------------------------------------
# Convertendo a lista em bytes, onde cada posição da 
# lista vira um byte
bytesIP = bytes(lstIP)

print(bytesIP)

# Será impresso -> b'\xc0\xa8\x01\n'


# --------------------------------------------------
# Convertendo os bytes em um inteiro
# big -> big-endian (o byte mais significativo vem primeiro)
intIP = int.from_bytes(bytes(lstIP), byteorder='big')

print(intIP)

# Será impresso -> 3232235786 (3.232.235.786)