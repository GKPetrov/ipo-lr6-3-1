str_list=["великий","Китай","партия","нефритовый","стержень","Xi"]
strV_count=0
for i in range(len(str_list)):
    if 'в' in str_list[i]:
        strV_count+=1
        pass
print(strV_count)
