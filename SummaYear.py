year = int(input("Введите год: "))
def program(year):
    january = 31
    march = 31
    april = 30
    may = 31
    june = 30
    july = 31
    august = 31
    september = 30 
    october = 31
    november = 30
    december = 31
    if (year % 4 == 0):
        february = 29
        print("Год - високосный")
    else: 
        february = 28
        print("Год - не високосный")
    months = [january, february, march, april, may, june, july, august, september, october, november, december]
    i = 0
    result = 0
    for i in range(len(months)):
        result += sumMonth(months[i])
    return result

def sumMonth(month):
    i = 1
    month += 1
    sum = 0
    for i in range(month):
        if (month < 10):
            sum += i
        else: divmod(sum)
    return sum
print(program(year))

#if (calendar.isleap(year) == True)
# year1 = array([cal.datetime.date.day])
# divmod(year1)
# sum(year1)
# if (year % 4 == 0):
#     february  = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8+2+9)
#     summa = january + february + march + april + may + june + july + august + september + october + november + december
#     
#     print(summa)
# else:
#     february  = int(1+2+3+4+5+6+7+8+9+1+0+1+1+1+2+1+3+1+4+1+5+1+6+1+7+1+8+1+9+2+0+2+1+2+2+2+3+2+4+2+5+2+6+2+7+2+8)
#     summa = january + february + march + april + may + june + july + august + september + october + november + december
#     
#     print(summa)