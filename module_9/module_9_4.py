s = input()
s_new = ''
for i in range(len(s)):
    if i < s.find('h') or i > s.rfind('h'):
        s_new += s[i]
print(s_new)