import sys

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class HexNumber:
    def __init__(self, str):
        self.head = None
        self.lenght = len(str)
        for element in str:
            self.head = Node(element, self.head)


    def __str__(self):
        str = ''
        a = self.head
        while a:
            str += a.val
            a = a.next
        return str[::-1]


    def add(self, second):
        if self.lenght > second.lenght:
            len = self.lenght
        else:
            len = second.lenght
        if_rem = False

        for i in range(len):
            if self.head != None and second.head != None:
                num = from_hex_to_decimal(self.head.val) + from_hex_to_decimal(second.head.val)
                self.head = self.head.next
                second.head = second.head.next

            else:
                if self.head != None and second.head == None:
                    num = from_hex_to_decimal(self.head.val)
                    self.head = self.head.next

                if self.head == None and second.head != None:
                    num = from_hex_to_decimal(second.head.val)
                    second.head = second.head.next

            if if_rem:
                num += 1
                if_rem = False

            if num > 15:
                num = num - 16
                if_rem = True

            if i == 0:
                res = HexNumber(from_decimal_to_hex(num))
                real_head = res.head
            else:
                res.head.next = Node(from_decimal_to_hex(num))
                res.head = res.head.next

        if if_rem:
            res.head.next = Node(from_decimal_to_hex(1))
        res.head = real_head
        return res

def from_hex_to_decimal(num):
    return ord(num) - ord('A') + 10 if num >= 'A' and num <= 'F' else ord(num) - ord('0')


def from_decimal_to_hex(num):
    return chr(ord('A') + num - 10) if num > 9 else chr(ord('0') + num)


def proverka(params):
    k = 0
    for i in params:
            if i.isdigit() == False and (i < 'A' or i > 'F'):
                k += 1
    return k


if __name__ == '__main__':
    params = sys.argv
    params = ['', 'F', '3']
    if proverka(params[1]) == 0 and proverka(params[2]) == 0:
        num1 = HexNumber(params[1])
        num2 = HexNumber(params[2])
        print(str(num1.add(num2)))
    else:
        print('Error')