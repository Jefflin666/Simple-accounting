commodity=[]
while True:
	c=input('請輸入商品名稱：')
	if c=='q':
		break
	p=input('請輸入價格：')
	commodity.append([c,p])
for a in commodity:
	print(a[0],'的價格是',a[1],'元')
with open ('test.csv','w')as f:
	f.write('商品，價格\n')
	for a in commodity:
		f.write(a[0]+','+str(a[1])+'\n')
