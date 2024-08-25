#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E 
ascii= 65
for i in range(5):
    print(" " * (5-i), end=" ")
    for j in range(i+1):
        print(chr(ascii), end=" ")
        ascii= ascii+1
    ascii = 65
    print()