value_1=["Bob","Alice","Charlie","Delilah","Joe","Esperanza"]
value_2=["EE", "CpE", "ChemE", "Journalism", "Stalking", "MechE"]
value_3=[1.5,2.5,3.8,2.1,4.0,3.0]

students= {
"Name" : value_1,
"Major" : value_2,
"GPA" : value_3
}

print("Students record are shown below:\n", students)

students["Num of absences"]=[1298,5,3,1,0,2]
print("\nNum of absences is now included in the students record:\n", students)

def GPA_av(GPA):

    return int(sum(GPA)/len(GPA))

average=GPA_av(students["GPA"])
print("\nThe average GPA of all the students is:", average)

def Highest_absent(MAX):
    Maximum=max(MAX)
    return Maximum

Hig_absent=Highest_absent(students["Num of absences"])
print("\nHighest number absences of all the students is:", Hig_absent)



Reset_absences=students["Num of absences"]
length=len(Reset_absences)
for i in range(0,length):
    Reset_absences[i]=0
students["Num of absences"]=Reset_absences
print("\nSemester ended, absences = 0 for all students:", students["Num of absences"])


New_name="Fernando"
Major="EE"
GPA=3.2
Attendance=0
students.get("Name").append(New_name)
students.get("Major").append(Major)
students.get("GPA").append(GPA)
students.get("Num of absences").append(Attendance)

print("\nNew student joined the school, his record are now included in the system:\n",students)
