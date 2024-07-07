'''
day la chu thich
'''
str =   '\a\a hung \b minh \" \t'
print(str)

tran = r'toi la \nguoi'
print(tran[2:None:-2])

strA = float("6.4")
print(strA)

strB = "HowToWin"
strB = strB[None:1] + "0" + strB[2:]
print(strB)

s = "abc xyz"
print(s[len(s):])

#string
print('hung is %s' % ('minh'))
s = '%s %s'
result1 = s%('1','2')
print(result1)

#repr


#float
f = '%f' %(2.4124312)
f2 = '%.2f' %(2.4124312)
print(f + '  ' + f2)

# f { abc }  : format
name = 'Hung'
age = '20'
address = 'BD'
info = f'name: {name}\nage: {age}\naddress: {address}'
print(info)

#format
print('a{}b{}c{}'.format(1,2,3))
print('a={1}b={0}c={2}'.format('zero','one','three'))
print('a={num1}, b={num2}'.format(num1=22, num2=33))

#allignment
#{:<10} left  {*:<10}
#{:>10} right
#{:^10} center
print('{:^10}'.format('a'))
print('{:*^10}'.format('a'))
print('{:>10}'.format('a'))


