mark = []
tot = 0
print("Enter Marks Obtained in 5 Subjects: ")
for i in range(5):
mark.insert(i, input())

for i in range(5):
tot = tot + int(mark[i])
avg = tot/5
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
print("Grade: A+")
elif(avg>=80&avg<89):
print("Grade: A")
elif(avg>=70&avg<79):
print("Grade:B ")
elif(avg>=60&avg<69):
print("Grade: C")
elif(avg>=50&avg<59):
print("Grade: D")
elif(avg<50):
print("Grade: Fail")
else:
print("invalid marks")
