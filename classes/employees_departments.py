# This practice is to start implementing relationships between 
# classes/types.

class Employee:
    def __init__(self, fullname, jobtitle, startdate):
        self.name = fullname
        self.job_title = jobtitle
        self.start_date = startdate

class Company:
    def __init__(self, bizname, address, industry):
        self.business_name = bizname
        self.address = address
        self.industry_type = industry
        self.employees = list()

    def list_employees(self):
        for employee in self.employees:
            print(f"{employee.name} is an employee of {self.business_name}")

global_financial = Company("Global Financial", "132 Capital Way", "Banking")
highpoint_medical = Company("Highpoint Medical", "400 Freedom Blvd", "Healthcare")

jack = Employee("Jack Ma", "CEO", "11/01/01")
global_financial.employees.append(jack)


brady = Employee("Brady Green", "Banker", "10/20/19")
global_financial.employees.append(brady)

samantha = Employee("Samantha Sue", "Nurse", "05/14/15")
highpoint_medical.employees.append(samantha)

andrea = Employee("Andrea Barlowe", "Nurse", "07/17/17")
highpoint_medical.employees.append(andrea)

scott = Employee("Scott Branford", "Doctor", "01/20/18")
highpoint_medical.employees.append(scott)

# Ideally they want me to print a list of employees to terminal from an f-string... 
global_financial.list_employees()
highpoint_medical.list_employees()