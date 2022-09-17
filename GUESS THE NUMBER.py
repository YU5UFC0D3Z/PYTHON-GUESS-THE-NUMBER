import time

perfect_number = 4

print("""
+-------------------------------------+
|  YU5UFC0D3Z                         |
|                                     |
|  PICK A NUMBER BETWEEN 1 and 10     |
|  WILL YOU GET IT CORRECT!           | 
+-------------------------------------+
""")

number = int(input("Enter number: "))

while number != perfect_number:
    if number < perfect_number:
        
        print("Too low.\n")
    else:
        print("Too high.\n")

    number = int(input("Enter number: "))

print("WOW YOU GUESSED THE CORRECT NUMBER\n")
