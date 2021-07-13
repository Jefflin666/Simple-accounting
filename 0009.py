commodity=[]
while True:
	c=input('請輸入商品名稱：')
	if c=='q':
		break
	p=input('請輸入價格：')
	commodity.append([c,p])
for a in commodity:
	print(a)