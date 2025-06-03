class Solution:


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target<= 0 or len(candidates)==0:
            return []
        answers = []
        currentCandidate = candidates[0]
        for number_times_to_add in range(0,target+1):
            if number_times_to_add * currentCandidate > target:
                break
            if target-currentCandidate*number_times_to_add==0:
                answers.append([currentCandidate for _ in range(number_times_to_add)])
                break
            other_candidates_answers = self.combinationSum(candidates[1:],target-currentCandidate*number_times_to_add)
            if len(other_candidates_answers)>0:
                other_candidates_answers = [[currentCandidate for _ in range(number_times_to_add)]+ans for ans in other_candidates_answers]
                for ans in other_candidates_answers:
                    answers.append(ans)
        return answers

            

        
            
        