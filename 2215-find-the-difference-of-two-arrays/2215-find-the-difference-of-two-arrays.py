class Solution(object):
    def findDifference(self, nums1, nums2):
        v1=[]
        v2=[]
        for i in nums1:
            if i not in nums2 and i not in v1:
                v1.append(i)
        for i in nums2 :
            if i not in nums1 and i not in v2:
                v2.append(i)
        return [v1,v2]

        