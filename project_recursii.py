def tower(num, kernel_from, kernel_to, kernel_time):
    if num > 0:
        tower(num-1, kernel_from, kernel_time, kernel_to)
        print("Переложить кольцо со стержня", kernel_from, "на стержень", kernel_to)
        tower(num-1, kernel_time, kernel_to, kernel_from)


def main():
    num = int(input("Введите колличество дисков расположенных на первоначальной пирамиде: "))
    kernel_from = int(input("Выберите стержень котором изначально лежать все кольца: "))
    kernel_to = int(input("Выберети стержень на который хотите переместить все кольца: "))
    kernel_time = int(input("Выберите стержень который послужит в качестве временного хранилища колец: "))
    tower(num, kernel_from, kernel_to, kernel_time)
    print("Задача решена!")


main()
