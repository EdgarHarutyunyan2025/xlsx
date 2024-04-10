x='heelo good world aoieu137954682.,[!@#$%]'


def sort_str(st):
    dic={}
    for i in st:
        if i == ' ':
             continue
        if i.isalpha():
              dic[i]=st.count(i)
        elif i.isdigit():
            dic[i]=st.count(i)
        else:
            dic[i]=st.count(i)

    return   sorted(dic.items(),key=lambda x: x[0])


lis=sort_str(x)

import xlsxwriter


workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()


expenses = lis
worksheet.write(0, 0,'tarer')
worksheet.write(0, 1, 'tver'    )
worksheet.write(0, 2,  'simvolner'   )
row = 1
ro=1
r=1
n=8
col = 0
vowels='aouie'
for item, cost in (expenses):
    if item.isalpha(): 
        if item in vowels:
            worksheet.write(1, col,  'vowels')
            r+=1
            worksheet.write(r, col,     item+' = '+ str(cost))
        if not item in vowels:
            worksheet.write(8, col,     'consonants')
            n+=1
            worksheet.write(n, col,     item+' = '+ str(cost))
    if item.isdigit():
        worksheet.write( ro,col+1,    item+' = '+ str(cost))
        ro += 1    
    if not item.isalpha() and not item.isdigit():
        worksheet.write(row, col+2,     item+' = '+ str(cost))
        row+=1



workbook.close()


