a=["великий","Китай","партия","нефритовый","стержень","Xi"]
str_count=0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]=='в':
            str_count+=1
            break
print(str_count)