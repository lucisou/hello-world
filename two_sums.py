List = []

def twoSum(nums, target):
        pos=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i]+nums[j] == target:
                        pos.append(i)
                    else:
                        pass
                else:
                    pass
        return pos

twoSum([1,2,3], 5)
