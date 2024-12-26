from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
     min_buy=prices[0]
     max_profit=0
     for i in range(len(prices)):
      if  min_buy > prices[i]:
         min_buy= prices[i]

      current_prof=prices[i]-min_buy

      max_profit=max(max_profit,current_prof)
      




     return max_profit   







sol=Solution()
print(sol.maxProfit([10,1,5,6,7,1]))


