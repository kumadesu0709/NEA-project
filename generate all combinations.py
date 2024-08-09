def generate_all_combination(people:list, max_no_of_people):
    result = []
    def backtrack(start, comb):
        if len(comb) == max_no_of_people:
            result.append(comb.copy())
            return
        for i in range(start, len(people)):
            comb.append(people[i])
            backtrack(i+1,comb)
            comb.pop()
    backtrack(0,[])
    return result

print(generate_all_combination([],3))