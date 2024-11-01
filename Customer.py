class Customer:

    def __init__(self, email=" ", password=" ", f_name=" ", l_name=" ", date_of_birth=" ", gender=" ", mobile_number=" "
                 , address=" "):
        """
        init method for customer.
        :param email:
        :param password:
        :param f_name:
        :param l_name:
        :param date_of_birth:
        :param gender:
        :param mobile_number:
        :param address:
        """
        self.email = email
        self.password = password
        self.f_name = f_name
        self.l_name = l_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.mobile_number = mobile_number
        self.address = address

    def get_email(self):
        """
        accessor method for  email
        :return:string
        """
        return self.email

    def set_email(self,email):
        """
        mutator method for email
        :param email:
        :return:string
        """
        self.email = email

    def get_password(self):
        """
        accessor method for password
        :return:string
        """
        return self.password

    def set_password(self,password):
        """
        mutator method for password
        :param password:
        :return: string
        """
        self.password = password

    def get_f_name(self):
        """
        accessor method for f_name
        :return: string
        """
        return self.f_name

    def set_f_name(self,f_name):
        """
        mutator method for f_name
        :param f_name:
        :return: string
        """
        self.f_name = f_name

    def get_l_name(self):
        """
        accessor method for l_name
        :return: string
        """
        return self.l_name

    def set_l_name(self,l_name):
        """
        mutator method for l_name
        :param l_name:
        :return: string
        """
        self.l_name = l_name

    def get_date_of_birth(self):
        """
        accessor method for date_of_birth
        :return: string
        """
        return  self.date_of_birth

    def set_date_of_birth(self,date_of_birth):
        """
        mutator method for date_of_birth
        :param date_of_birth:
        :return: string
        """
        self.date_of_birth = date_of_birth

    def get_gender(self):
        """
        accessor method for gender
        :return: string
        """
        return self.gender

    def set_gender(self, gender):
        """
        mutator method for gender
        :param gender:
        :return: string
        """
        self.gender = gender

    def get_address(self):
        """
        accessor method for address
        :return: string
        """
        return self.address

    def set_address(self, address):
        """
        mutator method for address
        :param address:
        :return: string
        """
        self.address = address

    def get_mobile_number(self):
        """
        accessor method for mobile_number
        :return: string
        """
        return self.mobile_number

    def set_mobile_number(self, mobile_number):
        """
        mutator method for mobile_number
        :param mobile_number:
        :return: string
        """
        self.mobile_number = mobile_number
