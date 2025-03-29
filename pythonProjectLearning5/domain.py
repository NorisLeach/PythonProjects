class Patient:
    def __init__(self, first_name, last_name, age, personal_code, disease, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.personal_code = personal_code
        self.disease = disease
        self.department = department

    def __str__(self):
        # Simple string representation
        return f"MyVector(first_name = {self.first_name}, last_name = {self.last_name}, age = {self.age}, personal_code = {self.personal_code}, disease = {self.disease}, department = {self.department})"


class Department:
    def __init__(self, department_id, name, num_beds, patients_list):
        self.department_id = department_id
        self.name = name
        self.num_beds = num_beds
        self.patients_list = patients_list

    def __str__(self):
        # Simple string representation
        return f"MyVector(department_id = {self.department_id}, name = {self.name}, num_beds = {self.num_beds}, patients_list = {self.patients_list})"



