#     1
#    121
#   12321
#  1234321
for i in range(1,5,1):
    print(" "*(4-i), end=" ")
    for j in range(1,i+1,1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
