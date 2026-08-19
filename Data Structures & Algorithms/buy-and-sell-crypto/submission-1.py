class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices, reverse=True):
            return 0
        
        max_prft = 0
        min_price = prices[0] #best price to have bought at, currently the first p in prices

        for p in range(len(prices)): #currently p is second p in prices
            if min_price > prices[p]: # if second p is less than first
                min_price = prices[p]
            elif min_price <= prices[p]: # if current p less than next p
                if prices[p] - min_price > max_prft:
                    max_prft = prices[p] - min_price
                else:
                    max_prft += 0

        
        return max_prft


            

