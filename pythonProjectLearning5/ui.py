from domain import Patient
from domain import Department
import domain
from DepartmentsRepository import Department_Patient_Repository

print("For addDepartment function type 1")
print("For getAllDepartments function type 2")
print("For addPatient function type 3")
print("For getAllPatients function type 4")
print("For sortPatientsInDepartmentByPersonalCode function type 5")
print("For sortDepartmentsByTheNumberOfPatients function type 6")
print("For sortDepartmentsByTheNumberOfPatientsWithAgeAboveLimit function type 7")
print("For sortDepartmentsByTheNumberOfPatientsAndPatientsInDepartmentAlphabetically function type 8")
print("For DepartmentsWithPatientsUnderGivenAge function type 9")
print("For PatientsFromGivenDepartmentWithTheFirstOrLastNameContainingGivenString function type 10")
print("For DepartmentsWithPatientsWithGivenFirstName function type 11")
print("For GroupsOfPatientsFromSameDepartmentAndSameDisease function type 12")
print("For GroupsOfDepartmentsHavingAtMost_p_PatientsSufferingFromSameDisease function type 13")

repo = Department_Patient_Repository()

repo.addDepartment(domain.Department(1, "medias", 2, "193 200"))
repo.addDepartment(domain.Department(2, "copsa", 4, "178"))
repo.addDepartment(domain.Department(3, "sighisoara", 3, "150 160 170"))
repo.addDepartment(domain.Department(4, "targu mures", 5, "200 210 220 230"))
repo.addDepartment(domain.Department(5, "reghin", 1, "300"))
repo.addDepartment(domain.Department(6, "ludus", 2, "310 320"))
repo.addDepartment(domain.Department(7, "iernut", 4, "330 340 350 360"))
repo.addDepartment(domain.Department(8, "santana", 3, "400 410 420"))
repo.addDepartment(domain.Department(9, "toplita", 2, "500 510"))
repo.addDepartment(domain.Department(10, "blaj", 6, "600 610 620 630 640 650"))


repo.addPatient(domain.Patient("noris", "leach", 18, 193, "raceala acuta", 1))
repo.addPatient(domain.Patient("stefi", "chitu", 18, 200, "somnolenta", 1))
repo.addPatient(domain.Patient("veali", "cretu", 25,  178, "intindere", 2))
repo.addPatient(domain.Patient("alex", "pop", 30, 150, "fractura", 3))
repo.addPatient(domain.Patient("maria", "ionescu", 22, 160, "migrena", 3))
repo.addPatient(domain.Patient("george", "vasile", 40, 170, "gripa", 3))
repo.addPatient(domain.Patient("ioana", "morar", 35, 210, "varicela", 4))
repo.addPatient(domain.Patient("david", "ilies", 28, 220, "insomnie", 4))
repo.addPatient(domain.Patient("cristina", "dragomir", 45, 300, "anxietate", 5))
repo.addPatient(domain.Patient("paul", "stan", 50, 330, "carie", 7))
repo.addPatient(domain.Patient("ana", "marin", 29, 410, "intoxicatie alimentara", 8))

def main():
    while True:
        x = int(input("   Enter a number between 1 and 13   "))
        if x == 1:
            department = input("Enter department name: ")
            repo.addDepartment(department)
        elif x == 2:
            repo.getAllDepartments()
        elif x == 3:
            patient = {
                "first_name": input("Enter first name: "),
                "last_name": input("Enter last name: "),
                "personal_code": int(input("Enter personal code: ")),
                "age": int(input("Enter age: ")),
                "disease": input("Enter disease: "),
                "department": input("Enter department: ")
            }
            repo.addPatient(patient)
        elif x == 4:
            repo.getAllPatients()
        elif x == 5:
            repo.sortPatientsInDepartmentByPersonalCode()
        elif x == 6:
            repo.sortDepartmentsByTheNumberOfPatients()
        elif x == 7:
            age_limit = int(input("Enter age limit: "))
            repo.sortDepartmentsByTheNumberOfPatientsWithAgeAboveLimit(age_limit)
        elif x == 8:
            repo.sortDepartmentsByTheNumberOfPatientsAndPatientsInDepartmentAlphabetically()
        elif x == 9:
            age = int(input("Enter age: "))
            repo.DepartmentsWithPatientsUnderGivenAge(age)
        elif x == 10:
            dep_id = input("Enter department ID: ")
            string = input("Enter string to search in names: ")
            repo.PatientsFromGivenDepartmentWithTheFirstOrLastNameContainingGivenString(dep_id, string)
        elif x == 11:
            repo.DepartmentsWithPatientsWithGivenFirstName()
        elif x == 12:
            k = int(input("Enter group size: "))
            repo.GroupsOfPatientsFromSameDepartmentAndSameDisease(k)
        elif x == 13:
            k = int(input("Enter maximum departments per group: "))
            p = int(input("Enter maximum patients per group: "))
            data = []
            num_entries = int(input("Enter number of data entries: "))
            for _ in range(num_entries):
                entry = {
                    "disease": input("Enter disease: "),
                    "department": input("Enter department: "),
                    "patient_count": int(input("Enter patient count: "))
                }
                data.append(entry)
            result = repo.group_departments(data, k, p)
            print("Groups:", result)
        elif x == 0:
            print("Exiting...")
            break
        else:
            print("Invalid value!")
            raise ValueError("the number must be from 1 to 13")


if __name__ == '__main__':
    try:
        main()
    except ValueError as er:
        print("exceptional case: ", er)
