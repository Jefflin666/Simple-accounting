import os
commodity=[]
#讀取檔案
if os.path.isfile('test.csv'): 
	print('找到檔案了')
	with open('test.csv','r',encoding='utf-8') as g:
		for line in g:
			name,price = c.strip().split(',')
			commodity.append([name,price])
	print(commodity)
else:
	print('未找到檔案')

#輸入商品f
while True:
	c=input('請輸入商品名稱：')
	if c=='q':
		break
	p=input('請輸入價格：')
	commodity.append([c,p])

#印出商品f
for a in commodity:
	print(a[0],'的價格是',a[1],'元')

#寫入商品f
with open ('test.csv','w', encoding='utf-8')as f:
	f.write('商品，價格\n')
	for a in commodity:
		f.write(a[0]+','+str(a[1])+'\n')



