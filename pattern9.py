#    1
#   222
#  33333
# 4444444
for i in range(1,5,1):
    print(" "*(4-i), end="")
    for j in range(2 * i - 1):
        print(i, end="")
    print()