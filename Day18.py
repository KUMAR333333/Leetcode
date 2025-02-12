s = "I speak Goat Latin"
#Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
s=s.split()
for i in range(len(s)):
    if s[i][0] in "aeiouAEIOU":
        s[i]=s[i]+"ma"+"a"*(i+1)
    if s[i][0] not in "AEIOUaeiou":
        s[i] = s[i][1:]+s[i][0]+"ma"+"a"*(i+1)
print(s)
        
