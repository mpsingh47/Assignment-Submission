#Que.1 Create 2 list with some brand names

list1=['APPLE','MICROSOFT','SAMSUNG','IBM','BMW','ROLEX','NIKE']
list2=['NIKE','ADIDAS','ROLEX','APPLE','INTEL','AUDI','GUCCI']

#Que.2 List of overlapping brand names in both lists
#method1 by using for loop
overlap_list=[]
for brand in list1:
    if brand in list2:
        overlap_list.append(brand)
print('List of overlapping Brand names is ',overlap_list)

#method2 by using set operation
overlap_l=list( set(list1) & set(list2) )
print('List of overlapping Brand names is ',overlap_l)


#Que.3 Print even numbers starting with 20 and ending with 40
list_num=[2030,12456,2040,20340,2055540,20330,34540,55640,20140]
print('\nPrint even numbers starting with 20 and ending with 40:')
for num in list_num:
    num=str(num)
    if (num[:2]+ num[len(num)-2:]) =='2040':
        print(int(num),end='  ')





