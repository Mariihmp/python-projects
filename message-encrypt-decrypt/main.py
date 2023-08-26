# encrypt or decrypt
import pyperclip

try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("""
      encrypting the message --> 
      encrypts letters by shifting them over by a key number 
      for example a key of 2 means the lettedr A is encrypted 
      into C b1 c2 -- the letter b into the c just goes over the alphabet 

      """)
while True:  # here I'm getting encryption or decryption
    print("do you want to encrypt or decrypt (e) (d)")
    response = input('--').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print("please enter letter e or d")

# let user enter the key to use like 1 2 3 4 5 ....symbole -1
# getting a valid key
while True:
    max_key = len(SYMBOLS) - 1
    print(f"please enter a key (0 to {max_key})")
    response = input('---').upper()
    if response.isdecimal():
        continue
    elif 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
# getting the message from user

print(f"enter the message that you want to {mode}")
message = input('---')
message = message.upper()

translate = ''
for i in message:
    if i in SYMBOLS:
        number = SYMBOLS.find(i)
        if mode == 'encrypt':
            number += key
        elif mode == 'decrypt':
            number -= key

        translate += SYMBOLS[number]
    else:
        translate += i

print(translate)
pyperclip.copy(translate)