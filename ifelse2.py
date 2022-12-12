friend = ['Korkai','Khorkai','Khorkwai','Somchai','Somsak']

friend2 = {'Korkai':'คุณ ก.ไก่',
            'Khorkai':'คุณ ข.ไข่',
            'Khorkwai':'คุณ ค.ควาย'}

visitor = 'khorkwai'


if visitor in friend or visitor.title() in friend:
    print('เป็นเพื่อน ขึ้นมาได้เลย')
    if visitor in friend2 or visitor.title() in friend2:
        print('สวัสดี' + friend2[visitor.title()])
    else:
        print('สวัสดีคุณลูกค้า')
else:
    print('เฮ้ย! คุณเป็นไคร ไม่มีชื่อในเมมเบอร์')
