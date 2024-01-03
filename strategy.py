from abc import ABC, abstractmethod, abstractproperty
from typing import List

# We will create a program that will sort the numbers in a list in a way that - 
# If numbers in the list are less than or equal to 20 then it will use the bubble sort algorithm
# If numbers in the list are more than 20 then it will use the merge sort algorthm 

class SortAlgorithm(ABC):
    """SortAlgorithm Abstraction
    """
    @abstractmethod
    def sort(self, nums: List[int]) -> List[int]:
        ...


class BubbleSort(SortAlgorithm):
    """BubbleSort Strategy
    """
    def __init__(self) -> None:
        print("Initiating Bubble Sort")
    
    def sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


class MergeSort(SortAlgorithm):
    """MergeSort Strategy
    """
    def __init__(self) -> None:
        print("Initiating Merge Sort")

    def sort(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:

            #  r is the point where the array is divided into two subarrays
            r = len(nums)//2
            L = nums[:r]
            M = nums[r:]

            # Sort the two halves
            self.sort(L)
            self.sort(M)

            i = j = k = 0

            # Until we reach either end of either L or M, pick larger among
            # elements L and M and place them in the correct position at A[p..r]
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = M[j]
                    j += 1
                k += 1

            # When we run out of elements in either L or M,
            # pick up the remaining elements and put in A[p..r]
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                nums[k] = M[j]
                j += 1
                k += 1
        return nums


class SortNumbers:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.sort_strategy: SortAlgorithm

    def sort_nums(self):
        if len(self.nums)<=20:
            self.sort_strategy = BubbleSort()
        else:
            self.sort_strategy = MergeSort()
        
        return self.sort_strategy.sort(nums=self.nums)


if __name__ == "__main__":
    nums1 = [3, 4, 2, 6, 8, 1, 2, 9, 23, 54, 12, 4, 0, 34, 56, 23, 12, 11, 1, 4, 6, 89, 34, 22]
    nums2 = [3, 4, 2, 6, 8, 1, 2, 9, 23, 54]

    sort1 = SortNumbers(nums=nums1)
    sorted_nums1 = sort1.sort_nums()
    print(sorted_nums1)

    sort2 = SortNumbers(nums=nums2)
    sorted_nums2 = sort2.sort_nums()
    print(sorted_nums2)