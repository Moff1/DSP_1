import csv

data = open(r'C:\Users\Moffatt\Desktop\Project_2_Python\2006_-_2011_NYS_Math_Test_Results_by_Grade_-_Citywide_-_by_Race-Ethnicity.csv')

for row in data:
    print(str(row.split(',')[3]))
    
'''  
def combo_one(year,race):
    for row in data:
        if str(row.split(',')[1]) == year:
            print(row)
            
combo_one("2007","black")


def combo_two(grade):
    for row in data:
        if str(row.split(',')[0]) == grade:
            print(row)
combo_two(grade)


def total():
    total = 0
    for row in data:
        number = str(row.split(',')[3])
        total = total + number
    return total
        
print("The total total number of students tested from 2006-2011 is "+ total())
'''