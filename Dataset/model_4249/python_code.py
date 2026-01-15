from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class demo_model_Address:

    def __init__(self, city: str, street: str, zipcode: int, state: str, country: str, demo_model_Address: "demo_model_Employee" = None):
        self.city = city
        self.street = street
        self.zipcode = zipcode
        self.state = state
        self.country = country
        self.demo_model_Address = demo_model_Address
        
    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def zipcode(self) -> int:
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

class demo_model_Employee:

    def __init__(self, birthday: date, firstname: str, lastname: str, position: str, email: str, phone: str, Employee: "demo_model_Company" = None, employees: "demo_model_Company" = None, demo_model_Employee: "demo_model_Address" = None):
        self.birthday = birthday
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.email = email
        self.phone = phone
        self.Employee = Employee
        self.employees = employees
        self.demo_model_Employee = demo_model_Employee
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def birthday(self) -> date:
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: date):
        self.__birthday = birthday

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

class demo_model_Company:

    def __init__(self, name: str, company: set["demo_model_Employee"] = None, Company: "demo_model_Employee" = None):
        self.name = name
        self.company = company if company is not None else set()
        self.Company = Company
        
    @property
    def name(self) -> str:
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
