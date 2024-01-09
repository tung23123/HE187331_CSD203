#PROMPT LIST:
numb_element = int(input('Enter number of element of the list: '))
list_n = []
for i in range(0,numb_element):
    tmp = input('Enter element NO {}: '.format(i+1))
    list_n.append(int(tmp))
print('Original list: ',list_n)
    
#REMOVE DUPLICATE AND PRINT:
set_list = set(list_n)
for numb in set_list:
    print(numb)