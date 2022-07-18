#Pretty straight forward question
# remove max and min salary from the list of salaries
# return the avg of remaining salaries

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        avg = 0
        for i in range(0,len(salary)):
            avg += salary[i]
        return float(avg / len(salary))
