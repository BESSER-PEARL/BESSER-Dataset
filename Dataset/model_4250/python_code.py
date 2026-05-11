from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class demo_model_Employee:

    def __init__(self, firstname: str, lastname: str, position: str, email: str, phone: str, birthday: date, employees: "demo_model_Company" = None, demo_model_Employee: "demo_model_Address" = None, Employee: "demo_model_Company" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.email = email
        self.phone = phone
        self.birthday = birthday
        self.employees = employees
        self.demo_model_Employee = demo_model_Employee
        self.Employee = Employee
        
        pass
    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname


    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: date):
        self.__birthday = birthday


    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname


    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_demo_model_Employee__employees", None)
        self.__employees = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company"):
                opp_val = getattr(old_value, "Company", None)
                if opp_val == self:
                    setattr(old_value, "Company", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company"):
                opp_val = getattr(value, "Company", None)
                setattr(value, "Company", self)

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_demo_model_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company"):
                opp_val = getattr(old_value, "company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company"):
                opp_val = getattr(value, "company", None)
                if opp_val is None:
                    setattr(value, "company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def demo_model_Employee(self):
        return self.__demo_model_Employee

    @demo_model_Employee.setter
    def demo_model_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_demo_model_Employee__demo_model_Employee", None)
        self.__demo_model_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "demo_model_Address"):
                opp_val = getattr(old_value, "demo_model_Address", None)
                if opp_val == self:
                    setattr(old_value, "demo_model_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "demo_model_Address"):
                opp_val = getattr(value, "demo_model_Address", None)
                setattr(value, "demo_model_Address", self)

class demo_model_Company:

    def __init__(self, name: str, Company: "demo_model_Employee" = None, company: set["demo_model_Employee"] = None):
        self.name = name
        self.Company = Company
        self.company = company if company is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_demo_model_Company__company", None)
        self.__company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    setattr(item, "Employee", self)
                    

    @property
    def Company(self):
        return self.__Company

    @Company.setter
    def Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_demo_model_Company__Company", None)
        self.__Company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employees"):
                opp_val = getattr(old_value, "employees", None)
                if opp_val == self:
                    setattr(old_value, "employees", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employees"):
                opp_val = getattr(value, "employees", None)
                setattr(value, "employees", self)

class demo_model_Address:

    def __init__(self, country: str, city: str, street: str, zipcode: int, state: str, demo_model_Address: "demo_model_Employee" = None):
        self.country = country
        self.city = city
        self.street = street
        self.zipcode = zipcode
        self.state = state
        self.demo_model_Address = demo_model_Address
        
        pass
    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city


    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street


    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state


    @property
    def zipcode(self):
        return self.__zipcode

    @zipcode.setter
    def zipcode(self, zipcode: int):
        self.__zipcode = zipcode


    @property
    def demo_model_Address(self):
        return self.__demo_model_Address

    @demo_model_Address.setter
    def demo_model_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_demo_model_Address__demo_model_Address", None)
        self.__demo_model_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "demo_model_Employee"):
                opp_val = getattr(old_value, "demo_model_Employee", None)
                if opp_val == self:
                    setattr(old_value, "demo_model_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "demo_model_Employee"):
                opp_val = getattr(value, "demo_model_Employee", None)
                setattr(value, "demo_model_Employee", self)
