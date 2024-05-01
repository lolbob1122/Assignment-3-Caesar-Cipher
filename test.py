
message = list(input('Type your message:'))
code = ['t', 'e', 's', 't']
print(message)
for i in message:
    code[i] = chr(ord(message[i]) + 3)

print(str(code))