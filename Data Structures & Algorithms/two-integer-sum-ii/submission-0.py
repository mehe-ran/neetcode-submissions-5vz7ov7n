class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstPointer, secondPointer = 0, len(numbers) - 1
        
        while firstPointer < secondPointer:
            curSum = numbers[firstPointer] + numbers[secondPointer]

            if curSum > target:
                secondPointer -= 1
            elif curSum < target:
                firstPointer += 1
            else:
                return [firstPointer+ 1, secondPointer+1]
        return []