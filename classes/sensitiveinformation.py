class Patient:
    def __init__(self, social, dob, acctnum, firstname, lastname, address):
        self.social_security_number = social
        self.date_of_birth = dob
        self.health_insurance_acct_num = acctnum
        self.first_name = firstname
        self.last_name = lastname
        self.address = address

    @property
    def social_security_number(self):
        try:
            return self.__social_security_number
        except AttributeError:
            return ""

    @property
    def date_of_birth(self):
        try:
            return self.__date_of_birth
        except AttributeError:
            return ""

    @property
    def health_insurance_acct_num(self):
        try:
            return self.__health_insurance_acct_num
        except AttributeError:
            return ""

    @property
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return ""

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return ""

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Please provide a string value for the address')

# So it doesn't like me trying to set the initial properties when I'm instantiating a new object...
katie = Patient("001-11-0101", "08/21/91", "01010101010101", "Katie", "Debalmaretti", "1200 Main St.")

print(dir(katie))