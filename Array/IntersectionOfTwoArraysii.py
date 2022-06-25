class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r1 = 0
        r2 = 0 
        l1 = len(nums1)
        l2 = len(nums2)
        nums1.sort()
        nums2.sort()
        res=[]
        while(r1<l1) and (r2<l2):
            if nums1[r1] == nums2[r2]:
                res.append(nums1[r1])
                r1+=1
                r2+=1
            elif nums1[r1]<nums2[r2]:
                r1+=1
            else:
                r2+=1
        return res
        