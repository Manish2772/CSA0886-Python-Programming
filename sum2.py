def combinationSum2(candidates, target):
    def backtrack(start, path, remaining):
        if remaining == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > remaining:
                break
            backtrack(i+1, path + [candidates[i]], remaining - candidates[i])
    candidates.sort()
    res = []
    backtrack(0, [], target)
    return res
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))