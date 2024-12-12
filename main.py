str_list=["великий","Китай","партия","нефритовый","стержень","Xi"]
strV_count=0
for word in str_list:
    if 'в' in word:
        strV_count+=1
        pass
print(strV_count)
