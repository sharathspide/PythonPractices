from optparse import Option
from typing import Optional


class AddTwoNumbers(object):
    def __init__(self, l1: list[int], l2:list[int])->None:
        self.l1 = l1
        self.l2 = l2

    def Reverse_List(l1: list[int]) -> list[int]:
        return l1[::-1]

    def AddTwoNumbers(self) -> list[int]:
        l1_reversed = AddTwoNumbers.Reverse_List(self.l1)
        l2_reversed = AddTwoNumbers.Reverse_List(self.l2)
        num1 = int(''.join(map(str, l1_reversed)))
        num2 = int(''.join(map(str, l2_reversed))) #join is performed only for string
        total = list(str(num1 + num2))
        return AddTwoNumbers.Reverse_List(total)

class AddTwoNumbers_SingleLinkedList(object):
    def __init__(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.l1 = l1
        self.l2 = l2

    def Reverse_List(l1: list[int]) -> list[int]:
        return l1[::-1]