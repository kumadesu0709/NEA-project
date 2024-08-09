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

class Room:
    def __init__(self, max_no_people):
        self._max_no_people = max_no_people
        self._students_in_room = []
    
    def add_pupil(self, student):
        if len(self._students_in_room) < self._max_no_people:
            self._students_in_room.append(student)
    
    def max_no_people(self):
        return self._max_no_people
    
    def students_in_room(self):
        return self._students_in_room

room_one = Room(3)

def generate_all_combination(students:list, max_no_of_people):
    result = []
    def backtrack(start, comb):
        if len(comb) == max_no_of_people:
            result.append(comb.copy())
            return
        for i in range(start, len(students)):
            comb.append(students[i])
            backtrack(i+1,comb)
            comb.pop()
    backtrack(0,[])
    return result

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

print(generate_all_combination(generate_all_combination(students,3), 3))
