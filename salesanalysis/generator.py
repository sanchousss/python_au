import random
import math
year = 2020

def open_file(input_file):
    with open(input_file) as d:
        return list(map(lambda x: x.strip().split(','), d.readlines()))

def generator_file_with_staff_id():
    file = open('input1.csv', "w+")
    data = open_file('input.csv')
    file.write('date,resource,staff_id,count \n')
    for i in range(1, len(data)):
        d = 0
        summ = 0
        count_staff_id = int(data[i][2])
        while count_staff_id > summ:
            new_count_staff_id = random.randint(0, 100)
            summ = summ + new_count_staff_id
            if count_staff_id < summ:
                summ = summ - new_count_staff_id
                new_count_staff_id = count_staff_id - summ
                d = 1
            if count_staff_id > summ:
                file.write("{},{},{},{} \n".format(data[i][0],
                                                   data[i][1],
                                                   random.randint(1, 10),
                                                   new_count_staff_id))
            if d == 1:
                break
    file.close()


def generator_file_without_staff_id():
    file = open('input.csv', "w+")
    file.write('date,resource,count \n')
    for i in range(1,11):
        for j in range(1, 13):
            file.write("{}-{},{},{} \n".format(year, j, i, random.randint(0, 100)))
    file.close()


def main():
    generator_file_without_staff_id()
    generator_file_with_staff_id()


if __name__ == '__main__':
    main()