

s1 = "Hello123World45"
sum=0
count=0
for letter in s1:
    if letter.isdigit():
        sum+=int(letter)
        count+=1
ave=sum/count
print("sum= ", sum, "average= ", ave)


