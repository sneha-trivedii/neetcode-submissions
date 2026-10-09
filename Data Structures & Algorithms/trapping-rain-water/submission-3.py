class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach: Use prefix max and suffix max arrays.
        pref=[0]*len(height)
        suff=[0]*len(height)
        res=0
        if len(height)<1:
            return res
        
        # Prefix array
        pref[0]=height[0]
        for i in range(1,len(height)):
            pref[i]=max(pref[i-1],height[i])

        #Suffix array
        suff[len(height)-1]=height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            suff[i]=max(suff[i+1],height[i])

        for i in range(len(height)):
            res=res+(min(pref[i],suff[i])-height[i])
        
        return res
