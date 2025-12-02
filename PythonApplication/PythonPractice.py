from Package.TwoSum import Index
from Package.AddTwoNumbers import AddTwoNumbers, AddTwoNumbers_SingleLinkedList

print("********************************")
print("Find 2 Indexes of that adds to the SUM")
print("********************************")
FindIndex: Index = Index([3,2,3],6)
print(FindIndex.Find_Index())
print(FindIndex.Find_Index_TwoPointer())

print("********************************")
print("Add Two Numbers - Normal Approach")
print("********************************")

AddTwoNums: AddTwoNumbers = AddTwoNumbers([2,4,3],[5,6,4])
print(AddTwoNums.AddTwoNumbers())
print("********************************")
AddTwoNums: AddTwoNumbers = AddTwoNumbers([0],[0])
print(AddTwoNums.AddTwoNumbers())
print("********************************")
AddTwoNums: AddTwoNumbers = AddTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])
print(AddTwoNums.AddTwoNumbers())

print("********************************")
print("Add Two Numbers - Single Linked List Approach")
print("********************************")

AddTwoNums_SLL: AddTwoNumbers_SingleLinkedList = AddTwoNumbers_SingleLinkedList([2,4,3],[5,6,4])
print(AddTwoNums_SLL.AddTwoNumbers())
print("********************************")
AddTwoNums_SLL: AddTwoNumbers_SingleLinkedList = AddTwoNumbers_SingleLinkedList([0],[0])
print(AddTwoNums_SLL.AddTwoNumbers())
print("********************************")
AddTwoNums_SLL: AddTwoNumbers_SingleLinkedList = AddTwoNumbers_SingleLinkedList([9,9,9,9,9,9,9],[9,9,9,9])
print(AddTwoNums_SLL.AddTwoNumbers())