str1=raw_input("enter the string:")
j=0;
str2 = ''
for i in range(len(str1)-1,-1,-1):
    str2 += str1[i]
if str1==str2:
    print "string is palindrome"
else:
    print "not palindrome"
# print str2
# print str1
