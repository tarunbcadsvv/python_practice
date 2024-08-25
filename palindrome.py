#palindrome num => when number and reverse of number both are same, num is called
# palindrome number
n= int(input('enter a number which you want to check palindrome:'))
rev=0
num=n
while n>0:
    digit = n%10
    rev = rev*10+digit
    n=n//10
if num==rev:
    print('palindrome number!')
else:
    print('not a palindrome number!')
