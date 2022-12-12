money = 1000
transfer = 10000000

print('Check',money < transfer)

while money < transfer:
    print('กรุณากรอกตัวเลขใหม่')
    transfer = int(input('new transfer : '))
    if transfer >1000000:
        print('เรียกผู้จัดการ ขอเคลียร์ก่อนถึงจะโอนได้')
        break

print('โอนได้ถ้าผู้จัดการอนุญาตสำหรับกรณีเป็น VIP')