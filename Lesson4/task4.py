var_input = input()
key = int(input())
result = ""

for simvol in var_input:
    if 'a' <= simvol <= 'z':
        result += chr((ord(simvol) - ord('a') + key) % 26 + ord('a'))
    elif 'A' <= simvol <= 'Z':
        result += chr((ord(simvol) - ord('A') + key) % 26 + ord('A'))
    else:
        result += simvol

print(result)