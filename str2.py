
a = 'hi, my Name is Hung'
b = a.capitalize() #chi viet hoa chu dau tien trong string
c = a.upper()   #toupper
d = c.lower()   #tolower
e = a.swapcase() #chuyen hoa thanh thuong va nguoc lai
f = a.title()   #chuyen chu bat dau thanh chu hoa}

g = a.center(40, '.')   #allign middle
h = a.rjust(40, '.')    #allign right


enc1 = a.encode()   #encode
i = a.join(('2 ',' 4 ',' 6 '))  #string cong list
j = a.replace(' ', ' _ ', 2)    #co the co count hoac ko
k = a.strip('h')    #xoa cac ki tu, ' ' o 2 dau
k2 = a.lstrip('h')

print(j)
