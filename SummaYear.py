year = int(input("Введите год: "))
january = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0+3+1)
march = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0+3+1)
april = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0)
may = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0+3+1)
june = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0)
july = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0+3+1)
august = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0+3+1)
september = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0)
october = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0+3+1)
november = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0)
december = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9+3+0+3+1)
if (year % 4 == 0):
    february  = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9)
    summa = january + february + march + april + may + june + july + august + september + october + november + december
    print("Год - високосный")
    print(summa)
else:
    february  = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8)
    summa = january + february + march + april + may + june + july + august + september + october + november + december
    print("Год - не високосный")
    print(summa)