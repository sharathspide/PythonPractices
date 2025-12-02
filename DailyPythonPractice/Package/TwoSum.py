class Index (object):
    def __init__(self, nums: list[int], target: int) -> None:
        self.nums = nums
        self.target = target

    def Find_Index(self) -> list[int]:
        for i in range (len(self.nums)):
            if(i+1<=len(self.nums)):
                sum = self.nums[i] + self.nums[i+1]
                if (sum == self.target):
                    return [i, i+1]
        return [0,0]
    
    def Find_Index_TwoPointer(self) -> list[int]:
        for i in range (len(self.nums)):
            if (i+1>=len(self.nums)):
               break
            for j in range (i+1, len(self.nums)):
                sum = self.nums[i] + self.nums[j]
                if (sum == self.target):
                    return [i, j]
        return [0,0]




