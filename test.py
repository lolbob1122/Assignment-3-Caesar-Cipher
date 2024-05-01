
message = str(input('Type your message:'))
code = ['t', 'e', 's', 't']
print(message)
for ch in message:
    code = chr(ord(ch) + 3)

print(str(code))