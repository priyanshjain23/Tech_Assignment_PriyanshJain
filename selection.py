import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="Priyansh@123", database="virtuos"
)


cursor = conn.cursor()


def get_valid_input(prompt, max_length=None):
    while True:
        value = input(prompt)
        if max_length and len(value) > max_length:
            print(f"Input exceeds max length of {max_length}. Try again.")
        elif value.strip() == "":
            print("Input cannot be empty. Try again.")
        else:
            return value


def get_valid_float(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if value < min_value or value > max_value:
                print("Input value should be between", min_value, "and", max_value)
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


student_name = get_valid_input("Enter Name of student :", max_length=30)
college_name = get_valid_input("Enter College name :", max_length=50)

round1marks = get_valid_float("Enter Round  1 marks :", 0, 10)
round2marks = get_valid_float("Enter Round 2 marks :", 0, 10)
round3marks = get_valid_float("Enter Round 3 marks :", 0, 10)
technicalroundmarks = get_valid_float("Enter Technical round marks :", 0, 20)


total_marks = round1marks + round2marks + round3marks + technicalroundmarks
print(total_marks)

result = "Rejected" if total_marks < 35 else "Selected"

insert_query = """Insert into T1 (StudentName,CollegeName,Round1Marks,Round2Marks,Round3Marks,TechnicalRoundMarks,TotalMarks,Result) 
values (%s , %s, %s, %s, %s, %s, %s, %s)  """

cursor.execute(
    insert_query,
    (
        student_name,
        college_name,
        round1marks,
        round2marks,
        round3marks,
        technicalroundmarks,
        total_marks,
        result,
    ),
)
conn.commit()

print("\nStudent Details Entered!")

cursor.execute(
    """SELECT StudentName,
               CollegeName,
               Round1Marks,
               Round2Marks,
               Round3Marks,
               TechnicalRoundMarks,
               TotalMarks,
               Result,
               Rank() over (order by TotalMarks Desc) as Rank_Result
                FROM T1;
               """
)

record = cursor.fetchall()

print("\nAll Student Records:")
print("-" * 90)
print(
    f"StudentName     |CollegeName      |Round1Marks |Round2Marks |Round3Marks |TechnicalRoundMarks|TotalMarks|Result  |Rank_Result"
)
print("-" * 90)

for row in record:
    print(
        f"{row[0]:<15} | {row[1]:<15} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10} | {row[5]:<15} | {row[6]:<10} | {row[7]:<8} | {row[8]}"
    )

cursor.close()
conn.close()
