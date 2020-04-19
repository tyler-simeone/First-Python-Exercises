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