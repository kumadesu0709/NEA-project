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

    
def check_existed_pupil(room_one, room_two):
    for student_one in room_one:
        if student_one in room_two:
            return True
    return False


def pick_rooms(rooms:list, no_of_rooms:int):
    result = []
    def backtrack(start, comb):
        if len(comb) == no_of_rooms:
            result.append(comb.copy())
            return
        for i in range(start, len(rooms)):
            have_existed = False
            for existed_room in comb:
                if check_existed_pupil(rooms[i], existed_room):
                    have_existed = True
                    break
            if have_existed == False:
                comb.append(rooms[i])
                backtrack(i+1,comb)
                comb.pop()

    backtrack(0,[])
    return result

def produce_roomings(no_of_one_man_room:int,no_of_two_man_room:int,no_of_three_man_room:int, pupil_in_yeargroup:list):

    one_man_rooms = generate_all_combination(pupil_in_yeargroup,1)
    two_man_rooms = generate_all_combination(pupil_in_yeargroup,2)
    three_man_rooms = generate_all_combination(pupil_in_yeargroup,3)

    combs_one_man_rooms = pick_rooms(one_man_rooms,no_of_one_man_room)
    combs_two_man_rooms = pick_rooms(two_man_rooms, no_of_two_man_room)
    combs_three_man_rooms = pick_rooms(three_man_rooms, no_of_three_man_room)

    result = []

    if no_of_two_man_room == 0 and no_of_three_man_room == 0 and no_of_one_man_room > 0:
        return [combs_one_man_rooms]
    
    elif no_of_one_man_room == 0 and no_of_three_man_room == 0 and no_of_two_man_room > 0:
        return [combs_two_man_rooms]
    
    elif no_of_two_man_room == 0 and no_of_one_man_room == 0 and no_of_three_man_room > 0:
        return [combs_three_man_rooms]
    
    elif no_of_one_man_room == 0 and no_of_two_man_room > 0 and no_of_three_man_room > 0:
        for comb_two_man_room in combs_two_man_rooms:
            for comb_three_man_room in combs_three_man_rooms:
                for two_man_room in comb_two_man_room:
                    for three_man_room in comb_three_man_room:
                        if check_existed_pupil(three_man_room, two_man_room):
                            continue
                        result.append([comb_two_man_room,comb_three_man_room])

    elif no_of_one_man_room > 0 and no_of_two_man_room == 0 and no_of_three_man_room > 0:
        for comb_one_man_room in combs_one_man_rooms:
            for comb_three_man_room in combs_three_man_rooms:
                for one_man_room in comb_one_man_room:
                    for three_man_room in comb_three_man_room:
                        if check_existed_pupil(three_man_room, one_man_room):
                            continue
                        result.append([comb_one_man_room,comb_three_man_room])

    elif no_of_one_man_room > 0 and no_of_two_man_room > 0 and no_of_three_man_room == 0:
        for comb_two_man_room in combs_two_man_rooms:
            for comb_one_man_room in combs_one_man_rooms:
                for two_man_room in comb_two_man_room:
                    for one_man_room in comb_one_man_room:
                        if check_existed_pupil(one_man_room, two_man_room):
                            continue
                        result.append([comb_one_man_room, comb_two_man_room])

    elif no_of_one_man_room > 0 and no_of_two_man_room > 0 and no_of_three_man_room > 0:
        for comb_one_man_room in combs_one_man_rooms:
            for comb_two_man_room in combs_two_man_rooms:
                for one_man_room in comb_one_man_room:
                    for two_man_room in comb_two_man_room:
                        if check_existed_pupil(one_man_room, two_man_room):
                            continue
                        for comb_three_man_room in combs_three_man_rooms:
                            for three_man_room in comb_three_man_room:
                                if check_existed_pupil(three_man_room, one_man_room) or check_existed_pupil(two_man_room, three_man_room):
                                    continue
                                result.append([comb_one_man_room,comb_two_man_room,comb_three_man_room])

    return result



pupil = [1,2,3,4,5,6,8,9,10]
produce_roomings(0,3,0,pupil)