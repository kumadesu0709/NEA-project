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

def pick_rooms(rooms:list, no_of_rooms):
    result = []
    def check_existed_pupil(room1, room2):
        have_existed = False
        for student1 in room1:
            for student2 in room2:
                if student1 == student2:
                    have_existed = True
        return have_existed
    def backtrack(start, comb):
        if len(comb) == no_of_rooms:
            result.append(comb.copy())
            return
        for i in range(start, len(rooms)):
            have_existed = False
            for existed_room in comb:
                if check_existed_pupil(rooms[i], existed_room):
                    have_existed = True
            if have_existed == False:
                comb.append(rooms[i])
                backtrack(i+1,comb)
                comb.pop()
    backtrack(0,[])
    return result

rooms = generate_all_combination(["a","b","c","d","e","f","g"],3)
print(pick_rooms(rooms,2))