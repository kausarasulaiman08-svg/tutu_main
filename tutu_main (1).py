# --- Variable Declaration ---
full_name = "Emmanuel Adebayo"
reg_number = "23/55EE104"
current_age = 20
current_cgpa = 4.45
status_active = True
enrolled_courses = ["EE301", "EE302", "GSE301", "MTH301"]
exam_grades = {'EE301': 'A', 'EE302': 'B', 'GSE301': 'A', 'MTH301': 'C'}

# storing info in a dictionary
profile = {
    "name": full_name,
    "reg_no": reg_number,
    "age": current_age,
    "cgpa": current_cgpa,
    "active": status_active,
    "courses": enrolled_courses,
    "scores": exam_grades
}

# Class list to hold multiple students
class_list = []
class_list.append(profile)

# Save to a generic text file
with open("class_data.txt", "w") as f:
    for p in class_list:
        f.write(str(p) + "\n")


# --- Data Processing Functions ---

# 1. Register a new subject
def register_subject(student_dict, code):
    # Check if course is already there
    if code in student_dict["courses"]:
        print(code + " is already in the list.")
    else:
        student_dict["courses"].append(code)
        student_dict["scores"][code] = None # No grade yet
        print(f"Successfully added {code}.")


# 2. Modify a student's score
def change_grade(student_dict, code, letter_grade):
    if code in student_dict["scores"]:
        student_dict["scores"][code] = letter_grade
        print(f"Updated {code} to {letter_grade}")
    else:
        print("Error: Course not found.")

# 3. GPA Calculation logic
point_system = {
    'A': 5.0,
    'B': 4.0,
    'C': 3.0,
    'D': 2.0,
    'E': 1.0,
    'F': 0.0
}

def get_gpa(grades_dictionary):
    sum_points = 0
    count = 0
    for key in grades_dictionary:
        grade_letter = grades_dictionary[key]
        if grade_letter in point_system: # simple check
            sum_points += point_system[grade_letter]
            count += 1
    
    if count == 0: return 0.0
    return sum_points / count

my_gpa = get_gpa(exam_grades)
print("Computed GPA:", my_gpa)

def show_summary():
    print("\n--- INDIVIDUAL REPORT ---")
    print("Student:", full_name)
    print("Matric:", reg_number)
    print("Age / CGPA:", current_age, "/", current_cgpa)
    print("Status:", "Active" if status_active else "Inactive")
    print("Courses Taken:", enrolled_courses)
    print("Semester GPA:", get_gpa(exam_grades))
    print("-------------------------\n")

show_summary()


# --- Task 1.2: Batch Storage ---

# New list of names
names_list = ["Chidinma Obi", "Emmanuel Adebayo", "Tola Adegoke", "Musa Ibrahim", "Sarah Johnson"]

# Dictionary list for 5 students
dept_students = [
    {
        "name": "Chidinma Obi", "reg_no": "23/55EE001", "age": 19, "cgpa": 4.80,
        "active": True, "courses": ["EE101", "EE102"], "scores": {'EE101': 'A', 'EE102': 'A'}
    },
    {
        "name": "Emmanuel Adebayo", "reg_no": "23/55EE002", "age": 20, "cgpa": 4.45,
        "active": True, "courses": ["EE201", "EE202"], "scores": {'EE201': 'B', 'EE202': 'C'}
    },
    {
        "name": "Tola Adegoke", "reg_no": "23/55EE003", "age": 21, "cgpa": 3.50,
        "active": False, "courses": ["EE301", "EE302"], "scores": {'EE301': 'C', 'EE302': 'D'}
    },
    {
        "name": "Musa Ibrahim", "reg_no": "23/55EE004", "age": 22, "cgpa": 2.10,
        "active": True, "courses": ["EE401", "EE402"], "scores": {'EE401': 'D', 'EE402': 'E'}
    },
    {
        "name": "Sarah Johnson", "reg_no": "23/55EE005", "age": 18, "cgpa": 4.90,
        "active": True, "courses": ["EE101", "EE102"], "scores": {'EE101': 'A', 'EE102': 'A'}
    }
]

# Set for unique subjects
all_courses_set = set()

for s in dept_students:
    for c in s["courses"]:
        all_courses_set.add(c)

print("Names:", names_list)
print("Available Dept Courses:", all_courses_set)


# --- Task 2: Grading Logic ---

def get_letter_grade(mark):
    # Validation check
    if mark < 0 or mark > 100:
        return "Error"
    
    if mark >= 70: return 'A'
    elif mark >= 60: return 'B'
    elif mark >= 50: return 'C'
    elif mark >= 45: return 'D'
    elif mark >= 40: return 'E'
    else: return 'F'

def print_remark(letter):
    match letter:
        case "A": print("Outstanding!")
        case "B": print("Good job.")
        case "C": print("You tried, but aim higher.")
        case "D": print("Fair.")
        case "E": print("Just passed.")
        case "F": print("Failed. See advisor.")
        case _: print("Invalid input.")

# Input section
try:
    user_score = int(input("\nEnter marks (0-100): "))
    res = get_letter_grade(user_score)
    print(f"Grade: {res}")
    print_remark(res)
except ValueError:
    print("Please type a number.")


# --- Task 2.2: Input Validation ---

def check_details():
    try:
        s_age = input("Age: ")
        s_cgpa = input("Current CGPA: ")

        # Converting
        val_age = int(s_age)
        val_cgpa = float(s_cgpa)

        # Logic check
        if not (16 <= val_age <= 35):
            print("Age out of range for this program.")
            return
        
        if not (0.0 <= val_cgpa <= 5.0):
            print("CGPA is impossible.")
            return

        print("Data Accepted.")
        print(f"Age: {val_age}, CGPA: {val_cgpa}")

    except:
        print("Error: Make sure you entered numbers correctly.")

check_details()


# --- Task 3: List Slicing ---

# 10 random scores
test_results = [55, 92, 48, 79, 88, 60, 95, 70, 81, 66]

# Top 3
test_results.sort(reverse=True)
print("Top 3 Results:", test_results[:3])

# Last 5 (from original list assumption, but we sorted it above, so let's reload or just slice current)
# NOTE: The previous sort affects the list. Let's use the sorted one.
print("Bottom 5 (from sorted):", test_results[-5:])

# Every second item
print("Skipping one:", test_results[::2])


# --- Task 3.2: Sets ---

passed_java = {"Emmanuel", "Sarah", "Musa", "Tola"}
dean_list = {"Emmanuel", "Sarah", "Chidinma"}

# Intersection (Passed AND Dean's list)
smart_passers = passed_java & dean_list 
print("Passed Java & on Dean's List:", smart_passers)

# Union (Everyone unique)
everyone = passed_java | dean_list
print("All unique students:", everyone)

# Difference (Passed Java but NOT on Dean's list)
just_passed = passed_java - dean_list
print("Passed Java only:", just_passed)


# --- Task 4: Console Menu ---

db_students = [
    {"n": "Emmanuel Adebayo", "p": 4.45},
    {"n": "Chidinma Obi", "p": 4.80},
    {"n": "Tola Adegoke", "p": 3.50},
    {"n": "Musa Ibrahim", "p": 2.10},
    {"n": "Sarah Johnson", "p": 4.90}
]

loop_switch = True

while loop_switch:
    print("\n--- CLASS MANAGER ---")
    print("[1] Show List")
    print("[2] Add Student")
    print("[3] Check Grad Status")
    print("[4] Best Student")
    print("[5] Quit")

    opt = input("Choice: ")

    match opt:
        case "1":
            print("\nList:")
            for x in db_students:
                print(f"{x['n']} (CGPA: {x['p']})")
        
        case "2":
            nm = input("Name: ")
            gp = float(input("CGPA: "))
            db_students.append({"n": nm, "p": gp})
            print("Saved.")

        case "3":
            check_name = input("Who to check? ")
            found = False
            for x in db_students:
                if x["n"] == check_name:
                    found = True
                    if x["p"] >= 2.5: 
                        print("Eligible.")
                    else: 
                        print("Not eligible.")
            if not found: print("Who is that?")

        case "4":
            # Finding max manually just to be different or using max()
            best = max(db_students, key=lambda z: z["p"])
            print(f"Highest: {best['n']} with {best['p']}")

        case "5":
            print("Bye!")
            loop_switch = False
        
        case _:
            print("Wrong number.")


# --- Task 4.2: Graduation Function ---

def can_graduate(s_rec):
    # Criteria: 2.5 GPA, Active, No Fs
    
    gpa_check = s_rec["cgpa"] >= 2.5
    active_check = s_rec["active"]
    
    # check for Fs
    no_carryovers = True
    for g in s_rec["scores"].values():
        if g == 'F' or g is None:
            no_carryovers = False
            break
            
    if gpa_check and active_check and no_carryovers:
        return True, "Verified: Can Graduate."
    else:
        return False, "Denied: Requirements not met."

# Test
dummy = {
    "name": "Musa Ibrahim",
    "cgpa": 2.10,
    "active": True,
    "scores": {"EE401": "D", "EE402": "E"} 
} # Note: GPA is low here

is_ok, status_msg = can_graduate(dummy)
print(status_msg)


# --- Task 5: Nested Dicts ---

results_matrix = {
    "Emmanuel": {"MTH": 70, "ENG": 80, "PHY": 65},
    "Sarah": {"MTH": 90, "ENG": 95, "PHY": 92},
    "Musa": {"MTH": 45, "ENG": 50, "PHY": 40},
    "Chidinma": {"MTH": 88, "ENG": 85, "PHY": 90},
    "Tola": {"MTH": 60, "ENG": 55, "PHY": 72}
}

avgs = {}
stars = []

for std, subs in results_matrix.items():
    # Calculate average
    marks = list(subs.values())
    curr_avg = sum(marks) / len(marks)
    avgs[std] = curr_avg
    
    # Check if all > 70
    clean_sweep = True
    for m in marks:
        if m <= 70:
            clean_sweep = False
    
    if clean_sweep:
        stars.append(std)

print("\nAverages:", avgs)
print("Star Students (>70 in all):", stars)


# --- Task 5.2: Type Checker ---

def check_type(variable):
    match variable:
        case int():
            print(f"It's an Integer: {variable}")
        case float():
            print(f"It's a Float: {variable}")
        case list():
            print(f"It's a List with size {len(variable)}")
        case dict():
            print("It's a Dictionary.")
        case str():
            print(f"It's a String saying: '{variable}'")
        case _:
            print("Unknown type.")

check_type([10, 20])
check_type("Python")
check_type(404)