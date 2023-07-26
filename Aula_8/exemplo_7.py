altura1 = float(input('digite a estatura da 1 pessoa:'))

altura2 = float(input('digite a estatura da 2 pessoa:'))

altura3 = float(input('digite a estatura da 3 pessoa:'))

if altura1 == altura2 or altura1 == altura3 or altura2 == altura3:
    print('\n Há pelo menos, duas pessoas com a mesma altura')
elif altura1 > altura2 and altura1 < altura3:
    print(f' A pessoa mais alta tem {altura1} m.')
elif altura2 < altura1 and altura2 > altura3:
    print(f' A pessoa mais alta tem {altura2} m.')
else:
    print(f' A pessoa mais alta tem {altura3} m.')
