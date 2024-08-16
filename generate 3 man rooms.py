from openpyxl.workbook import Workbook
from openpyxl import load_workbook

#load existing spreadsheet
wb = load_workbook("/Users/jamesguan/Desktop/CS A level NEA/NEA-project/NEA testing.xlsx")
#create the actual spreadsheet
ws = wb.active

class Student:

    def __init__(self, name, preferred_one, preferred_two, preferred_three, hated):
        self._name = name
        self._preferred_one = preferred_one
        self._preferred_two = preferred_two
        self._preferred_three = preferred_three
        self._hated = hated

    def name(self):
        return self._name
    
    def preferred_one(self):
        return self._preferred_one
    
    def preferred_two(self):
        return self._preferred_two
    
    def preferred_three(self):
        return self._preferred_three
    
    def hated(self):
        return self._hated

class rooming:

    def __init__(self, student_in_yeargroup:list, unwanted_pairs:list):
        self._student_in_yeargroup = student_in_yeargroup
        self._unwanted_pairs = unwanted_pairs
        self._rooming_combinations = []
        self._rooming_scores = {}
    
    def generate_all_combination(self, max_no_of_people):
        result = []
        def backtrack(start, comb):
            if len(comb) == max_no_of_people:
                result.append(comb.copy())
                return
            for i in range(start, len(self._student_in_yeargroup)):
                comb.append(self._student_in_yeargroup[i])
                backtrack(i+1,comb)
                comb.pop()
        backtrack(0,[])
        return result

    def _check_existed_pupil(self,room_one, room_two):
        for student_one in room_one:
            if student_one in room_two:
                return True
        return False
    
    def pick_rooms(self, rooms:list, no_of_rooms:int):
        result = []
        def backtrack(start, comb):
            if len(comb) == no_of_rooms:
                result.append(comb.copy())
                return
            for i in range(start, len(rooms)):
                have_existed = False
                for existed_room in comb:
                    if self._check_existed_pupil(rooms[i], existed_room):
                        have_existed = True
                        break
                if have_existed == False:
                    comb.append(rooms[i])
                    backtrack(i+1,comb)
                    comb.pop()

        backtrack(0,[])
        return result
    
    def produce_rooming__without_a_type_of_room(self, combs_room_one, combs_room_two):
        for comb_room_one in combs_room_one:
                for comb_room_two in combs_room_two:
                    for room_one in comb_room_one:
                        for room_two in comb_room_two:
                            if self._check_existed_pupil(room_one, room_two):
                                continue
                            self._rooming_combinations.append([comb_room_one, comb_room_two])

    
    def produce_roomings(self, no_of_one_man_room:int,no_of_two_man_room:int,no_of_three_man_room:int):

        one_man_rooms = self.generate_all_combination(1)
        two_man_rooms = self.generate_all_combination(2)
        three_man_rooms = self.generate_all_combination(3)

        combs_one_man_rooms = self.pick_rooms(one_man_rooms,no_of_one_man_room)
        combs_two_man_rooms = self.pick_rooms(two_man_rooms, no_of_two_man_room)
        combs_three_man_rooms = self.pick_rooms(three_man_rooms, no_of_three_man_room)

        if no_of_two_man_room == 0 and no_of_three_man_room == 0 and no_of_one_man_room > 0:
            return combs_one_man_rooms
        
        elif no_of_one_man_room == 0 and no_of_three_man_room == 0 and no_of_two_man_room > 0:
            return combs_two_man_rooms
        
        elif no_of_two_man_room == 0 and no_of_one_man_room == 0 and no_of_three_man_room > 0:
            return combs_three_man_rooms
        
        elif no_of_one_man_room == 0 and no_of_two_man_room > 0 and no_of_three_man_room > 0:
            self.produce_rooming__without_a_type_of_room(combs_two_man_rooms, combs_three_man_rooms)

        elif no_of_one_man_room > 0 and no_of_two_man_room == 0 and no_of_three_man_room > 0:
            self.produce_rooming__without_a_type_of_room(combs_one_man_rooms, combs_three_man_rooms)

        elif no_of_one_man_room > 0 and no_of_two_man_room > 0 and no_of_three_man_room == 0:
            self.produce_rooming__without_a_type_of_room(combs_one_man_rooms, combs_two_man_rooms)

        elif no_of_one_man_room > 0 and no_of_two_man_room > 0 and no_of_three_man_room > 0:
            for comb_one_man_room in combs_one_man_rooms:
                for comb_two_man_room in combs_two_man_rooms:
                    for one_man_room in comb_one_man_room:
                        for two_man_room in comb_two_man_room:
                            if self._check_existed_pupil(one_man_room, two_man_room):
                                continue
                            for comb_three_man_room in combs_three_man_rooms:
                                for three_man_room in comb_three_man_room:
                                    if self._check_existed_pupil(three_man_room, one_man_room) or self._check_existed_pupil(two_man_room, three_man_room):
                                        continue
                                    self._rooming_combinations.append([comb_one_man_room,comb_two_man_room,comb_three_man_room])
    
    def check_if_unwanted(self, room:0):

        is_unwanted = False

        if len(room) == 2:
            for unwanted_pair in self._unwanted_pairs:
                if room[0] in unwanted_pair and room[1] in unwanted_pair:
                    is_unwanted = True
        
        if len(room) == 3:
            for unwanted_pair in self._unwanted_pairs:
                if (room[0] in unwanted_pair and room[1] in unwanted_pair) or (room[0] in unwanted_pair and room[2] in unwanted_pair) or (room[1] in unwanted_pair and room[2] in unwanted_pair):
                    is_unwanted = True

        return is_unwanted

    
    
    def return_rooming(self):
        return self._rooming_combinations
    




student_one = Student(ws["B2"].value, ws["C2"].value, ws["D2"].value, ws["E2"].value, ws["F2"].value)
student_two = Student(ws["B3"].value, ws["C3"].value, ws["D3"].value, ws["E3"].value, ws["F3"].value)
student_three = Student(ws["B4"].value, ws["C4"].value, ws["D4"].value, ws["E4"].value, ws["F4"].value)
student_four = Student(ws["B5"].value, ws["C5"].value, ws["D5"].value, ws["E5"].value, ws["F5"].value)
student_five = Student(ws["B6"].value, ws["C6"].value, ws["D6"].value, ws["E6"].value, ws["F6"].value)
student_six = Student(ws["B7"].value, ws["C7"].value, ws["D7"].value, ws["E7"].value, ws["F7"].value)
student_seven = Student(ws["B8"].value, ws["C8"].value, ws["D8"].value, ws["E8"].value, ws["F8"].value)
student_eight = Student(ws["B9"].value, ws["C9"].value, ws["D9"].value, ws["E9"].value, ws["F9"].value)
student_nine = Student(ws["B10"].value, ws["C10"].value, ws["D10"].value, ws["E10"].value, ws["F10"].value)
student_ten = Student(ws["B11"].value, ws["C11"].value, ws["D11"].value, ws["E11"].value, ws["F11"].value)
student_eleven = Student(ws["B12"].value, ws["C12"].value, ws["D12"].value, ws["E12"].value, ws["F12"].value)
student_twelve= Student(ws["B13"].value, ws["C13"].value, ws["D13"].value, ws["E13"].value, ws["F13"].value)
student_thirteen = Student(ws["B14"].value, ws["C14"].value, ws["D14"].value, ws["E14"].value, ws["F14"].value)

students = [student_one.name(),student_two.name(), student_three.name(), student_four.name(), student_five.name(), student_six.name(), student_seven.name(), student_eight.name(), student_nine.name(), student_ten.name(), student_eleven.name(), student_twelve.name(), student_thirteen.name()]
while students[-1] == None:
    students.pop()
rooming1 = rooming(students)
rooming1.produce_roomings(0,1,1)
print(rooming1.return_rooming())
