print("\n====================================")
print("          REPORT CARD")
print("====================================")

name = input("Enter the name: ")
roll_no = input("Enter the roll_no.: ")

print("\n--- Enter Marks (out of 100) ---")

maths = float(input("Maths: "))
science = float(input("Science: "))
social_science = float(input("Social Science: "))
english = float(input("English: "))
hindi = float(input("Hindi: "))

Total = (maths + science + social_science + hindi + english)
Percentage = (Total/500)*100

if Percentage >= 90:
    grade = "A+"
elif 90 > Percentage >= 80:
    grade = "A"
elif 80 > Percentage >= 70:
    grade = "B"
elif 70 > Percentage >= 60:
    grade = "C"
elif 60 > Percentage >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

if(Percentage>=50):
    Result =  "PASS"
elif(Percentage<50):
    Result = "FAIL"

print("------------------------------------")

print("Total Marks Obtained: ", Total)
print("Percentage:  %", Percentage)
print("Grade: ", grade)
print("Result: ", Result)

print("====================================\n")
print("✨ Thank you for using the Marksheet Program ✨")
