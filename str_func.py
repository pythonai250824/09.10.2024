text: str = "Hello, World!!"
print("Hello, World!!", '**len', len(text))

text1: str = "   Hello, World!!   "
print("   Hello, World!!   ", '**strip:', text1.strip())

text2: str = "Hello, World!!"
print(text2, '**lower:', text2.lower())

text3: str = "Hello, World!!"
print(text3, '**upper:', text3.upper())

text4: str = "Hello, World!!"
print("Hello, World!!", '**text4.replace("World", "Python"):',  text4.replace("World", "Python"))
print("Hello, World!!", '**text4.replace("l", "t"):', text4.replace("l", "t"))
print("Hello, World!!", '**text4.replace("l", "t"):', text4.replace("t", ""))

text5: str = "Hello, World!! good morning"
print(text5, '**text5.split():', text5.split())
text5 = "Hello,*World!!*good*morning"
print(text5, "**text5.split('*'):", text5.split('*'))
print(text5, "**text5.split():", text5.split())

# Join
print(['H', 'E', 'L', 'L', 'O'])
print("**join(['H', 'E', 'L', 'L', 'O']:", "".join(['H', 'E', 'L', 'L', 'O']))

text6: str = "Hello, World!! good morning"
print(text6, '**text6.startswith("Hello") ?', text6.startswith("Hello"))

text7: str = "Hello, World!! good morning"
print(text7, '**text7.endswith("good morning") ?', text7.endswith("good morning"))

text8: str = "hello, world!! good morning"
print(text8, 'text8.capitalize() ', text8.capitalize())

text9: str = "hello, world!! good morning"
print(text9, 'text9.title() ', text9.title())

print('"1234" text10.isalpha() ', "1234".isalpha())
print('"abcd".isalpha()', "abcd".isalpha())
print('"abcd_".isalpha()', "abcd_".isalpha())
print('"abcd1".isalpha()', "abcd1".isalpha())

print('"1234" text10.isdigit()', "1234".isdigit())
print('"abcd".isdigit()" ', "abcd".isdigit())
print('"abcd1".isdigit()" ', "abcd1".isdigit())

print('"Aab".islower()', "Aab".islower())
print('"aab".islower()', "aab".islower())
print('"Aab".isupper()', "Aab".isupper())
print('"ABC".isupper()', "ABC".isupper())

print('"AasdasBcccC".swapcase()', "AasdasBcccC".swapcase())

print('"42".zfill(5)', "42".zfill(5))

print('123456789012')
print('Hello!'.center(120, '-'))
print('Hello!'.center(12, ' '))

print('"     ".isspace()', "    ".isspace())

print("0123456789012345678")
print("Hello python course")  # ['H', 'e', ... ]
print('   [0]', "Hello python course"[0])
print("  [-1]", "Hello python course"[-1])
print("[::-1]", "Hello python course"[::-1])
print("  [5:]", "Hello python course"[5:])
print("  [:8]", "Hello python course"[:8])
print(" [::2]", "Hello python course"[::2])