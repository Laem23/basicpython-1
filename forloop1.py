for i in range(5):
    print('Hello',i)

print('----------Loop in list----------')
friend = ['Korkai','Khorkai','Khorkwai','Somchai','Somsak']

for f in friend:
    print(f)
    if f == 'Korkai':
        print('สวัสดี คุณ ก.ไก่')
    else:
        print('สวัสดีคุณลูกค้า')

print('----------Loop in Dictionary----------')

friend2 = {'Korkai':'คุณ ก.ไก่',
            'Khorkai':'คุณ ข.ไข่',
            'Khorkwai':'คุณ ค.ควาย'}

# show key
for f in friend2:
    print(f)

# show item
for k,v in friend2.items():
    print('Key : ',k)
    print('Value,k')

# show key only
for f in friend2.keys():
    print(f)

# shoe value only
for f in friend2.values():
    print(f)

#ต้องการลำดับ
for i,f in enumerate(friend,start = 1000):
    print(i,f)

#ต้องการลำดับสำหรับ dict
for i,f in enumerate(friend2.items()):
    print(i,f)

#ต้องการลำดับสำหรับ dict แยก keys
for i,(k,v) in enumerate(friend2.items()):
    print(i,k,v)


        
        