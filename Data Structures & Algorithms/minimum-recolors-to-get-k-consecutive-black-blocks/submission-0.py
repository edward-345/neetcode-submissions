class Solution:
    """
    You are given a 0-indexed string blocks of length n, where blocks[i] is 
    either 'W' or 'B', representing the color of the ith block. The characters 
    'W' and 'B' denote the colors white and black, respectively. 
    
    You are also given an integer k, which is the desired number of consecutive 
    black blocks.
    
    In one operation, you can recolor a white block such that it becomes a black 
    block.
    
    Return the minimum number of operations needed such that there is at least 
    one occurrence of k consecutive black blocks.
    """
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = []
        end = len(blocks) - k

        if end == 0:
            return blocks.count('W')
        else:
            for i in range(end):
                window = blocks[i:k]
                w_count = window.count('W')
                count.append(w_count)
                k += 1
            return min(count)