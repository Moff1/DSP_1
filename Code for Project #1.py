import csv

data = open(r'C:\Users\Moffatt\Desktop\Project_1\Vaccination_Coverage_among_Health_Care_Personnel.csv')

LSouthWest = ["New Mexico","Arizona","New Mexico","Kansas","California","Oaklahoma"]
def SouthWest():
    count = 0
    for row in data:

        state = str(row.split(',')[2])
        
        if state in LSoutheast:
        
            #print(answer)
        
            count1 = count + 1
    print("The number of vaccines in the SouthWest is "+ count)
    return count1


LSoutheast = ["Georgia","Florida","Texas","Alabama","Mississippi", "South Carolina", "Tennessee", "Arkansas","Kentucky", "Louisana"]
def SouthEast():
    count = 0
    for row in data:
        state = str(row.split(',')[2])
        
        if state in LSoutheast:
        
            #print(answer)
        
            count2 = count + 1
    print("The number of vaccines in the SEC is "+ count)
    return count2



LNorthWest = ["Nevada","Utah","Wyoming","Idaho","Washington","Oregon","Montana","North Dakota","Utah"]

def NorthWest():
    count = 0
    for row in data:

        state = str(row.split(',')[2])
        
        if state in LNorthWest:
        
            #print(answer)
        
            count3 = count + 1
    print("The number of vaccines in the NorthWest is "+ count)
    return count3
    
    
    
LNorthEast = ["Minnesota","Wisconsin","Iowa","Illinois","Michigan","Ohio","Indiana","Virginia","West Virginia","Delware",
"Maine","New Hampshire","New York","New Jersey","Pennsylvania","Rhode Island","Vermont","Massachusetts","Connecticut"]

def NorthEast():
    count = 0
    for row in data:

        state = str(row.split(',')[2])
        
        if state in LNorthEast:
        
            #print(answer)
        
            count4 = count + 1
    print("The number of vaccines in the NOrthEast is "+ count)
    return count4
 
    
