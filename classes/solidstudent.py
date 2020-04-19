class Student():
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort_number = 0

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}"

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return ""

    @first_name.setter
    def first_name(self, new_firstname):
        if type(new_firstname) is str:
            self.__first_name = new_firstname
        else:
            raise TypeError('Please provide a string for the first name')

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return ""

    @last_name.setter
    def last_name(self, new_lastname):
        if type(new_lastname) is str:
            self.__last_name = new_lastname
        else:
            raise TypeError('Please provide a string for the last name')

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @age.setter
    def age(self, newage):
        if type(newage) is int:
            self.__age = newage
        else:
            raise TypeError('Please provide an integer for the age')

    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0

    @cohort_number.setter
    def cohort_number(self, newnumber):
        if type(newnumber) is int:
            self.__cohort_number = newnumber
        else:
            raise TypeError('Please provide an integer for the Cohort number')

    # Read-only property, so not defined in __init__ constructor method.
    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return ""

rachel = Student()
rachel.first_name = "Rachel"
rachel.last_name = "McCreary"
rachel.age = 27
rachel.cohort_number = 38
print(rachel)
