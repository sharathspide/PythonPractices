from Package.TwoSum import Index
from Package.AddTwoNumbers import AddTwoNumbers, AddTwoNumbers_SingleLinkedList
# class PythonPractices(object):
#     def __init__(self) -> None:
print("This is Python Practices Package")
two_sums: Index = Index([2,7,11,15], 9)
result = two_sums.Find_Index()
print ("Index of two numbers adding to target is: ", result)
print("***************************************")

print ("finding index for the two sum by Two Pointer Approach:")
result_two_pointer = two_sums.Find_Index_TwoPointer()
print ("Index of two numbers adding to target is: ", result)
print("***************************************")

add_two_numbers: AddTwoNumbers = AddTwoNumbers([2,4,3], [5,6,4])
result_addition = add_two_numbers.AddTwoNumbers()
print("The result of addition of two numbers represented as list is: ", result_addition)
print("***************************************")

#single linked list approach is still pending
# add_two_numbers_linkedlist: AddTwoNumbers_SingleLinkedList = AddTwoNumbers_SingleLinkedList([2,4,3], [5,6,4])
# result_addition_linkedlist = add_two_numbers_linkedlist.Reverse_List([2,4,3])
