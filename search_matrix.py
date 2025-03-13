class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        answer = False 

        for row in matrix:
            if answer == True:
                break

            if row[-1] == target:
                answer = True
                break

            if row[-1] > target:
                for element in row:
                    if element == target:
                        answer = True
                        break
            

        return answer
