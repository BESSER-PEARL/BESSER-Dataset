from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Employee_Actor:

    pass


class Administrator_Actor:

    pass


class Salary_Management_UseCase:

    pass


class Authentication_UseCase:

    pass





class Logout_external:

    pass


class Login_external:

    pass


class office:

    pass


class hourlyPay:

    def __init__(self, employee: employee, employee18: "employee" = None):
        self.employee = employee
        self.employee18 = employee18
        
        pass
    @property
    def employee(self):
        return self.__employee
    @employee.setter
    def employee(self, employee: employee):
        self.__employee = employee

    @property
    def employee18(self):
        return self.__employee18
    @employee18.setter
    def employee18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hourlyPay__employee18", None)
        self.__employee18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hourlyPay19"):
                opp_val = getattr(old_value, "hourlyPay19", None)
                if opp_val == self:
                    setattr(old_value, "hourlyPay19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hourlyPay19"):
                opp_val = getattr(value, "hourlyPay19", None)
                setattr(value, "hourlyPay19", self)



class Department:

    def __init__(self, name: str, description: str, employee17: "employee" = None):
        self.name = name
        self.description = description
        self.employee17 = employee17
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def employee17(self):
        return self.__employee17
    @employee17.setter
    def employee17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__employee17", None)
        self.__employee17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department16"):
                opp_val = getattr(old_value, "department16", None)
                if opp_val == self:
                    setattr(old_value, "department16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department16"):
                opp_val = getattr(value, "department16", None)
                setattr(value, "department16", self)



class Role:

    def __init__(self, name: str, description: str, employee15: "employee" = None):
        self.name = name
        self.description = description
        self.employee15 = employee15
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def employee15(self):
        return self.__employee15
    @employee15.setter
    def employee15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Role__employee15", None)
        self.__employee15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "role14"):
                opp_val = getattr(old_value, "role14", None)
                if opp_val == self:
                    setattr(old_value, "role14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "role14"):
                opp_val = getattr(value, "role14", None)
                setattr(value, "role14", self)



class role:

    pass


class Coordinator:

    def __init__(self, office: office, person13: "Person" = None):
        self.office = office
        self.person13 = person13
        
        pass
    @property
    def office(self):
        return self.__office
    @office.setter
    def office(self, office: office):
        self.__office = office

    @property
    def person13(self):
        return self.__person13
    @person13.setter
    def person13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Coordinator__person13", None)
        self.__person13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coordinator12"):
                opp_val = getattr(old_value, "coordinator12", None)
                if opp_val == self:
                    setattr(old_value, "coordinator12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coordinator12"):
                opp_val = getattr(value, "coordinator12", None)
                setattr(value, "coordinator12", self)



class Physician:

    def __init__(self, office: office, person11: "Person" = None):
        self.office = office
        self.person11 = person11
        
        pass
    @property
    def office(self):
        return self.__office
    @office.setter
    def office(self, office: office):
        self.__office = office

    @property
    def person11(self):
        return self.__person11
    @person11.setter
    def person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Physician__person11", None)
        self.__person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "physician10"):
                opp_val = getattr(old_value, "physician10", None)
                if opp_val == self:
                    setattr(old_value, "physician10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "physician10"):
                opp_val = getattr(value, "physician10", None)
                setattr(value, "physician10", self)



class Patient:

    def __init__(self, patientid: str, ICD: str, approvedHours: float, employee: Employee_Actor, account9: "account" = None):
        self.patientid = patientid
        self.ICD = ICD
        self.approvedHours = approvedHours
        self.employee = employee
        self.account9 = account9
        
        pass
    @property
    def ICD(self):
        return self.__ICD
    @ICD.setter
    def ICD(self, ICD: str):
        self.__ICD = ICD

    @property
    def patientid(self):
        return self.__patientid
    @patientid.setter
    def patientid(self, patientid: str):
        self.__patientid = patientid

    @property
    def approvedHours(self):
        return self.__approvedHours
    @approvedHours.setter
    def approvedHours(self, approvedHours: float):
        self.__approvedHours = approvedHours

    @property
    def employee(self):
        return self.__employee
    @employee.setter
    def employee(self, employee: Employee_Actor):
        self.__employee = employee

    @property
    def account9(self):
        return self.__account9
    @account9.setter
    def account9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__account9", None)
        self.__account9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient8"):
                opp_val = getattr(old_value, "patient8", None)
                if opp_val == self:
                    setattr(old_value, "patient8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient8"):
                opp_val = getattr(value, "patient8", None)
                setattr(value, "patient8", self)



class employee:

    def __init__(self, empid: str, ssn: str, Date_Hired: date, Date_Started: date, Date_Ended: date, workingHours: float, Role: role, Department: Department, account6: "account" = None, role14: "Role" = None, department16: "Department" = None, hourlyPay19: "hourlyPay" = None):
        self.empid = empid
        self.ssn = ssn
        self.Date_Hired = Date_Hired
        self.Date_Started = Date_Started
        self.Date_Ended = Date_Ended
        self.workingHours = workingHours
        self.Role = Role
        self.Department = Department
        self.account6 = account6
        self.role14 = role14
        self.department16 = department16
        self.hourlyPay19 = hourlyPay19
        
        pass
    @property
    def Date_Ended(self):
        return self.__Date_Ended
    @Date_Ended.setter
    def Date_Ended(self, Date_Ended: date):
        self.__Date_Ended = Date_Ended

    @property
    def Role(self):
        return self.__Role
    @Role.setter
    def Role(self, Role: role):
        self.__Role = Role

    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self, empid: str):
        self.__empid = empid

    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: Department):
        self.__Department = Department

    @property
    def ssn(self):
        return self.__ssn
    @ssn.setter
    def ssn(self, ssn: str):
        self.__ssn = ssn

    @property
    def workingHours(self):
        return self.__workingHours
    @workingHours.setter
    def workingHours(self, workingHours: float):
        self.__workingHours = workingHours

    @property
    def Date_Hired(self):
        return self.__Date_Hired
    @Date_Hired.setter
    def Date_Hired(self, Date_Hired: date):
        self.__Date_Hired = Date_Hired

    @property
    def Date_Started(self):
        return self.__Date_Started
    @Date_Started.setter
    def Date_Started(self, Date_Started: date):
        self.__Date_Started = Date_Started

    @property
    def account6(self):
        return self.__account6
    @account6.setter
    def account6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee__account6", None)
        self.__account6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee7"):
                opp_val = getattr(old_value, "employee7", None)
                if opp_val == self:
                    setattr(old_value, "employee7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee7"):
                opp_val = getattr(value, "employee7", None)
                setattr(value, "employee7", self)

    @property
    def role14(self):
        return self.__role14
    @role14.setter
    def role14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee__role14", None)
        self.__role14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee15"):
                opp_val = getattr(old_value, "employee15", None)
                if opp_val == self:
                    setattr(old_value, "employee15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee15"):
                opp_val = getattr(value, "employee15", None)
                setattr(value, "employee15", self)

    @property
    def department16(self):
        return self.__department16
    @department16.setter
    def department16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee__department16", None)
        self.__department16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee17"):
                opp_val = getattr(old_value, "employee17", None)
                if opp_val == self:
                    setattr(old_value, "employee17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee17"):
                opp_val = getattr(value, "employee17", None)
                setattr(value, "employee17", self)

    @property
    def hourlyPay19(self):
        return self.__hourlyPay19
    @hourlyPay19.setter
    def hourlyPay19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee__hourlyPay19", None)
        self.__hourlyPay19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee18"):
                opp_val = getattr(old_value, "employee18", None)
                if opp_val == self:
                    setattr(old_value, "employee18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee18"):
                opp_val = getattr(value, "employee18", None)
                setattr(value, "employee18", self)



class account:

    def __init__(self, username: str, password: str, office: str, id: int, person5: "Person" = None, employee7: "employee" = None, patient8: "Patient" = None):
        self.username = username
        self.password = password
        self.office = office
        self.id = id
        self.person5 = person5
        self.employee7 = employee7
        self.patient8 = patient8
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def office(self):
        return self.__office
    @office.setter
    def office(self, office: str):
        self.__office = office

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def patient8(self):
        return self.__patient8
    @patient8.setter
    def patient8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account__patient8", None)
        self.__patient8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account9"):
                opp_val = getattr(old_value, "account9", None)
                if opp_val == self:
                    setattr(old_value, "account9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account9"):
                opp_val = getattr(value, "account9", None)
                setattr(value, "account9", self)

    @property
    def person5(self):
        return self.__person5
    @person5.setter
    def person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account__person5", None)
        self.__person5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account4"):
                opp_val = getattr(old_value, "account4", None)
                if opp_val == self:
                    setattr(old_value, "account4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account4"):
                opp_val = getattr(value, "account4", None)
                setattr(value, "account4", self)

    @property
    def employee7(self):
        return self.__employee7
    @employee7.setter
    def employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account__employee7", None)
        self.__employee7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account6"):
                opp_val = getattr(old_value, "account6", None)
                if opp_val == self:
                    setattr(old_value, "account6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account6"):
                opp_val = getattr(value, "account6", None)
                setattr(value, "account6", self)



class Person:

    def __init__(self, firstName: str, lastName: str, middleName: str, homePhone: str, cellPhone: str, email: str, address: str, city: str, State: str, DoB: date, note: str, account4: "account" = None, physician10: "Physician" = None, coordinator12: "Coordinator" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        self.homePhone = homePhone
        self.cellPhone = cellPhone
        self.email = email
        self.address = address
        self.city = city
        self.State = State
        self.DoB = DoB
        self.note = note
        self.account4 = account4
        self.physician10 = physician10
        self.coordinator12 = coordinator12
        
        pass
    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def middleName(self):
        return self.__middleName
    @middleName.setter
    def middleName(self, middleName: str):
        self.__middleName = middleName

    @property
    def DoB(self):
        return self.__DoB
    @DoB.setter
    def DoB(self, DoB: date):
        self.__DoB = DoB

    @property
    def homePhone(self):
        return self.__homePhone
    @homePhone.setter
    def homePhone(self, homePhone: str):
        self.__homePhone = homePhone

    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def cellPhone(self):
        return self.__cellPhone
    @cellPhone.setter
    def cellPhone(self, cellPhone: str):
        self.__cellPhone = cellPhone

    @property
    def State(self):
        return self.__State
    @State.setter
    def State(self, State: str):
        self.__State = State

    @property
    def coordinator12(self):
        return self.__coordinator12
    @coordinator12.setter
    def coordinator12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__coordinator12", None)
        self.__coordinator12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person13"):
                opp_val = getattr(old_value, "person13", None)
                if opp_val == self:
                    setattr(old_value, "person13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person13"):
                opp_val = getattr(value, "person13", None)
                setattr(value, "person13", self)

    @property
    def account4(self):
        return self.__account4
    @account4.setter
    def account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__account4", None)
        self.__account4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person5"):
                opp_val = getattr(old_value, "person5", None)
                if opp_val == self:
                    setattr(old_value, "person5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person5"):
                opp_val = getattr(value, "person5", None)
                setattr(value, "person5", self)

    @property
    def physician10(self):
        return self.__physician10
    @physician10.setter
    def physician10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__physician10", None)
        self.__physician10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person11"):
                opp_val = getattr(old_value, "person11", None)
                if opp_val == self:
                    setattr(old_value, "person11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person11"):
                opp_val = getattr(value, "person11", None)
                setattr(value, "person11", self)



class Employee_Management_System_Component:

    pass
