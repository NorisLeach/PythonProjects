import domain
from collections import defaultdict
class Department_Patient_Repository():

    def __init__(self):
        self.departments = []
        self.patients = []

    def addDepartment(self, department):
        self.departments.append(department)

    def getAllDepartments(self):
        for i in range(0, len(self.departments)):
            print(self.departments[i])

    def addPatient(self, patient):
        self.patients.append(patient)

    def getAllPatients(self):
        for i in range(0, len(self.patients)):
            print(self.patients[i])

    def sortPatientsInDepartmentByPersonalCode(self):
        for i in range(0, len(self.patients)-1):
            for j in range(i+1, len(self.patients)):
                if self.patients[i].personal_code > self.patients[j].personal_code:
                    aux = self.patients[i]
                    self.patients[i] = self.patients[j]
                    self.patients[j] = aux

    def sortPatientsInDepartmentByPersonalCode(self):
        def is_sorted(partial_list):
            for i in range(len(partial_list) - 1):
                if partial_list[i].personal_code > partial_list[i + 1].personal_code:
                    return False
            return True

        def backtrack(start):
            if start == len(self.patients):
                return True

            for i in range(start, len(self.patients)):
                self.patients[start], self.patients[i] = self.patients[i], self.patients[start]
                if is_sorted(self.patients[:start + 1]):
                    if backtrack(start + 1):
                        return True
                self.patients[start], self.patients[i] = self.patients[i], self.patients[start]

            return False

        backtrack(0)

    def sortDepartmentsByTheNumberOfPatients(self):
        for i in range(0, len(self.departments) - 1):
            for j in range(i + 1, len(self.departments)):
                st1 = self.departments[i].patients_list.split()
                st2 = self.departments[j].patients_list.split()
                if len(st1) > len(st2):
                    aux = self.departments[i]
                    self.departments[i] = self.departments[j]
                    self.departments[j] = aux

    def sortDepartmentsByTheNumberOfPatientsWithAgeAboveLimit(self, limit):
        for i in range(0, len(self.departments) - 1):
            for j in range(i + 1, len(self.departments)):
                st1 = self.departments[i].patients_list.split()
                st1limit = []
                for p in range(0, len(st1)):
                    for k in range(0, len(self.patients)):
                        if str(self.patients[k].personal_code) == st1[p]:
                            if self.patients[k].age > 50:
                                st1limit.append(self.patients[k].personal_code)
                st2 = self.departments[j].patients_list.split()
                st2limit = []
                for pp in range(0, len(st2)):
                    for kk in range(0, len(self.patients)):
                        if str(self.patients[kk].personal_code) == st1[pp]:
                            if self.patients[kk].age > 50:
                                st2limit.append(self.patients[kk].personal_code)
                if len(st1limit) > len(st2limit):
                    aux = self.departments[i]
                    self.departments[i] = self.departments[j]
                    self.departments[j] = aux

    def sortDepartmentsByTheNumberOfPatientsAndPatientsInDepartmentAlphabetically(self):
        for i in range(0, len(self.departments) - 1):
            for j in range(i + 1, len(self.departments)):
                st1 = self.departments[i].patients_list.split()
                st2 = self.departments[j].patients_list.split()
                if len(st1) > len(st2):
                    aux = self.departments[i]
                    self.departments[i] = self.departments[j]
                    self.departments[j] = aux

        for i in range(0, len(self.departments)):
            names = []
            new_patients_list = []
            st1 = self.departments[i].patients_list.split()
            for p in range(0, len(st1)):
                for j in range(0, len(self.patients)):
                    if str(self.patients[j].personal_code) == st1[p]:
                        names.append(self.patients[j].first_name)
            sorted_names = sorted(names)
            for k in range(0, len(sorted_names)):
                for z in range(0, len(self.patients)):
                    if self.patients[z].first_name == names[k]:
                        new_patients_list.append(self.patients[z].personal_code)
            self.patients[i].patients_list = new_patients_list

    def DepartmentsWithPatientsUnderGivenAge(self, age):
        for i in range(0, len(self.departments)):
            st1 = self.departments[i].patients_list.split()
            for p in range(0, len(st1)):
                for j in range(0, len(self.patients)):
                    if (str(self.patients[j].personal_code) == st1[p]) & (self.patients[j].age < age):
                        print(self.departments[i].name)

    def PatientsFromGivenDepartmentWithTheFirstOrLastNameContainingGivenString(self, dep_id, string):
        for i in range(0, len(self.patients)):
            if (self.patients[i].department == dep_id) and ((self.patients[i].first_name.find(string)) or (self.patients[i].last_name.find(string))):
                print(self.patients[i].personal_code)

    def DepartmentsWithPatientsWithGivenFirstName(self):
        for i in range(0, len(self.departments)):
            sem=1
            st1 = self.departments[i].patients_list.split()
            for p in range(0, len(st1)):
                for j in range(0, len(self.patients)):
                    if (str(self.patients[j].personal_code) == st1[p]) and (len(self.patients[j].first_name) == 0):
                        sem=0
            if sem == 1:
                print(self.departments[i].department_id)

    def GroupsOfPatientsFromSameDepartmentAndSameDisease(self, k):
        if k < len(self.patients):
            print("There are not enough patients")
        else:
            groups = []
            for i in range(0, len(self.departments)):
                subgroups = []
                st1 = self.departments[i].patients_list.split()
                for p in range(0, len(st1)):
                    for j in range(0, len(self.patients)-1):
                        for k in range(j+1, len(self.patients)):
                            if self.patients[j].disease == self.patients[k].disease:
                                subgroups.append(self.patients.personal_code)
        if len(groups) <= k:
            groups.append(subgroups)
        print(groups)

    def GroupsOfDepartmentsHavingAtMost_p_PatientsSufferingFromSameDisease(self, k, p):
        """if k < len(self.departments):
            print("There are not enough departments")
        else:
            groups = []
            for i in range(0, len(self.departments)):
                subgroups = []
                st1 = self.departments[i].patients_list.split()
                for p in range(0, len(st1)):
                    for j in range(0, len(self.patients) - 1):"""

        from collections import defaultdict

        def group_departments(data, k, p):
            disease_groups = defaultdict(list)
            for entry in data:
                key = entry['disease']
                disease_groups[key].append(entry)

            result = []
            for disease, entries in disease_groups.items():
                entries.sort(key=lambda x: x['department'])
                current_group = []
                current_patient_count = 0
                for entry in entries:
                    if len(current_group) < k and current_patient_count + entry['patient_count'] <= p:
                        current_group.append(entry['department'])
                        current_patient_count += entry['patient_count']
                    else:
                        result.append((disease, current_group))
                        current_group = [entry['department']]
                        current_patient_count = entry['patient_count']
                if current_group:
                    result.append((disease, current_group))
            return result


""" ~~~~~~~~~~~~~~~~~~   ASSERTS    ~~~~~~~~~~~~~~~~~~"""

import domain

def test_add_department():
    repo = Department_Patient_Repository()
    department = domain.Department("Cardiology", "1", "101 102")
    repo.addDepartment(department)
    assert len(repo.departments) == 1
    assert repo.departments[0].name == "Cardiology"

def test_get_all_departments():
    repo = Department_Patient_Repository()
    department = domain.Department("Cardiology", "1", "101 102")
    repo.addDepartment(department)
    repo.getAllDepartments()  # Check output manually if needed

def test_add_patient():
    repo = Department_Patient_Repository()
    patient = domain.Patient("John", "Doe", 101, 30, "Cardiology")
    repo.addPatient(patient)
    assert len(repo.patients) == 1
    assert repo.patients[0].first_name == "John"

def test_get_all_patients():
    repo = Department_Patient_Repository()
    patient = domain.Patient("John", "Doe", 101, 30, "Cardiology")
    repo.addPatient(patient)
    repo.getAllPatients()  # Check output manually if needed

def test_sort_patients_in_department_by_personal_code():
    repo = Department_Patient_Repository()
    patient1 = domain.Patient("Alice", "Smith", 102, 25, "Cardiology")
    patient2 = domain.Patient("Bob", "Brown", 101, 30, "Cardiology")
    repo.addPatient(patient1)
    repo.addPatient(patient2)
    repo.sortPatientsInDepartmentByPersonalCode()
    assert repo.patients[0].personal_code == 101
    assert repo.patients[1].personal_code == 102

def test_sort_departments_by_number_of_patients():
    repo = Department_Patient_Repository()
    dept1 = domain.Department("Cardiology", "1", "101 102")
    dept2 = domain.Department("Neurology", "2", "201")
    repo.addDepartment(dept1)
    repo.addDepartment(dept2)
    repo.sortDepartmentsByTheNumberOfPatients()
    assert repo.departments[0].name == "Neurology"

def test_sort_departments_by_number_of_patients_with_age_above_limit():
    repo = Department_Patient_Repository()
    dept1 = domain.Department("Cardiology", "1", "101 102")
    dept2 = domain.Department("Neurology", "2", "201")
    patient1 = domain.Patient("Alice", "Smith", 101, 55, "Cardiology")
    patient2 = domain.Patient("Bob", "Brown", 102, 45, "Cardiology")
    patient3 = domain.Patient("Carol", "Jones", 201, 60, "Neurology")
    repo.addDepartment(dept1)
    repo.addDepartment(dept2)
    repo.addPatient(patient1)
    repo.addPatient(patient2)
    repo.addPatient(patient3)
    repo.sortDepartmentsByTheNumberOfPatientsWithAgeAboveLimit(50)
    assert repo.departments[0].name == "Cardiology"

def test_sort_departments_by_patients_and_alphabetically():
    repo = Department_Patient_Repository()
    dept = domain.Department("Cardiology", "1", "101 102")
    patient1 = domain.Patient("Bob", "Brown", 102, 45, "Cardiology")
    patient2 = domain.Patient("Alice", "Smith", 101, 55, "Cardiology")
    repo.addDepartment(dept)
    repo.addPatient(patient1)
    repo.addPatient(patient2)
    repo.sortDepartmentsByTheNumberOfPatientsAndPatientsInDepartmentAlphabetically()
    assert dept.patients_list == [101, 102]

def test_departments_with_patients_under_age():
    repo = Department_Patient_Repository()
    dept = domain.Department("Cardiology", "1", "101 102")
    patient1 = domain.Patient("Alice", "Smith", 101, 20, "Cardiology")
    patient2 = domain.Patient("Bob", "Brown", 102, 30, "Cardiology")
    repo.addDepartment(dept)
    repo.addPatient(patient1)
    repo.addPatient(patient2)
    repo.DepartmentsWithPatientsUnderGivenAge(25)  # Check output manually

def test_patients_from_department_with_name_containing_string():
    repo = Department_Patient_Repository()
    patient = domain.Patient("John", "Doe", 101, 30, "Cardiology")
    repo.addPatient(patient)
    repo.PatientsFromGivenDepartmentWithTheFirstOrLastNameContainingGivenString("Cardiology", "John")  # Check output manually

def test_departments_with_patients_with_given_first_name():
    repo = Department_Patient_Repository()
    dept = domain.Department("Cardiology", "1", "101 102")
    patient = domain.Patient("John", "Doe", 101, 30, "Cardiology")
    repo.addDepartment(dept)
    repo.addPatient(patient)
    repo.DepartmentsWithPatientsWithGivenFirstName()  # Check output manually

def test_groups_of_patients_from_same_department_and_same_disease():
    repo = Department_Patient_Repository()
    patient1 = domain.Patient("Alice", "Smith", 101, 45, "Cardiology", "Flu")
    patient2 = domain.Patient("Bob", "Brown", 102, 55, "Cardiology", "Flu")
    repo.addPatient(patient1)
    repo.addPatient(patient2)
    repo.GroupsOfPatientsFromSameDepartmentAndSameDisease(2)  # Check output manually


    """
    This class serves as a repository for managing departments and patients. 
    It provides functionalities such as adding departments and patients, 
    retrieving data, and performing various sorting operations. Below is 
    the description of the key methods in the class:

    1. addDepartment(department): 
       - Adds a department to the repository.
       - Args: department (object) - The department to be added.

    2. getAllDepartments(): 
       - Retrieves and prints all departments in the repository.

    3. addPatient(patient): 
       - Adds a patient to the repository.
       - Args: patient (object) - The patient to be added.

    4. getAllPatients(): 
       - Retrieves and prints all patients in the repository.

    5. sortPatientsInDepartmentByPersonalCode(): 
       - Sorts all patients in the repository by their personal codes in ascending order.

    6. sortDepartmentsByTheNumberOfPatients(): 
       - Sorts the departments by the number of patients associated with each department in ascending order.

    7. sortDepartmentsByTheNumberOfPatientsWithAgeAboveLimit(limit): 
       - Sorts the departments based on the number of patients above a specified age limit.
       - Args: limit (int) - The age limit.

    8. sortDepartmentsByTheNumberOfPatientsAndPatientsInDepartmentAlphabetically(): 
       - Sorts the departments by the number of patients and also sorts 
         patients within each department alphabetically by their first names.

    9. DepartmentsWithPatientsUnderGivenAge(age): 
       - Finds and prints the departments that have patients below a given age.
       - Args: age (int) - The age threshold.

    10. PatientsFromGivenDepartmentWithTheFirstOrLastNameContainingGivenString(dep_id, string): 
        - Finds and prints patients from a specific department whose first or 
          last names contain a given string.
        - Args: 
            dep_id (int) - The department ID. 
            string (str) - The substring to search for in the patient's name.

    11. DepartmentsWithPatientsWithGivenFirstName(): 
        - Finds and prints departments where all patients have a first name.

    12. GroupsOfPatientsFromSameDepartmentAndSameDisease(k): 
        - Groups patients from the same department who suffer from the same disease.
        - Args: k (int) - The minimum group size.

    13. GroupsOfDepartmentsHavingAtMost_p_PatientsSufferingFromSameDisease(k, p): 
        - Groups departments where the total number of patients suffering 
          from the same disease does not exceed a given limit.
        - Args: 
            k (int) - The maximum number of departments in a group.
            p (int) - The maximum number of patients with the same disease in a group.

    These methods enable efficient management of the department and patient data, 
    allowing operations like sorting, filtering, and grouping based on various criteria.
    """
