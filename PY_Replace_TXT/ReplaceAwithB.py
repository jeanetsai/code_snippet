import io
#將a.txt內和b.txt重複的東西去除
#使用注意:a.txt和b.txt最後一行要換行
with io.open('a.txt','r',encoding ='UTF-8') as f:
    array_docA=f.readlines()
    #print(array_docA)      
f.close()

with io.open('b.txt','r',encoding ='UTF-8') as f:
    array_docB=f.readlines() 
    #print(array_docB)      
f.close()
    
for n, i in enumerate(array_docA):
    for x, y in enumerate(array_docB):
        if i == y:
            array_docA[n] = ''

#print(array_docA)

with io.open('output.txt','w',encoding ='UTF-8') as txt_file:
    for line in array_docA:
        txt_file.write("".join(line))
        # works with any number of elements in a line
