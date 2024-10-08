from numbers_parser import Document
"""doc = Document("testing.numbers")
sheets = doc.sheets
tables = sheets[0].tables
table = tables[0]
table.write(11, 1, "This is new text")
table.write("B7", "hiiiii")
doc.save("testing.numbers")"""

list = [[1,2,3],[4,5,6],[7,8,9]]
doc = Document("sheet.numbers")
doc.add_sheet("test3", "New Table")
sheet = doc.sheets["test3"]
table = sheet.tables["New Table"]
row = 1
column = 0
for room in list:
    column = 0
    for label in room:
        table.write(row, column, label)
        column += 1
    row+= 1
doc.save("sheet.numbers")