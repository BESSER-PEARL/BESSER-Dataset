from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Loan:

    def __init__(self, emp_id: int, emp_name: str, loan_purpose: str, loan_interst: int, loan_type: str, amount: str):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.loan_purpose = loan_purpose
        self.loan_interst = loan_interst
        self.loan_type = loan_type
        self.amount = amount
        
        pass
    @property
    def loan_purpose(self):
        return self.__loan_purpose
    @loan_purpose.setter
    def loan_purpose(self, loan_purpose: str):
        self.__loan_purpose = loan_purpose

    @property
    def loan_type(self):
        return self.__loan_type
    @loan_type.setter
    def loan_type(self, loan_type: str):
        self.__loan_type = loan_type

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def loan_interst(self):
        return self.__loan_interst
    @loan_interst.setter
    def loan_interst(self, loan_interst: int):
        self.__loan_interst = loan_interst

    @property
    def emp_name(self):
        return self.__emp_name
    @emp_name.setter
    def emp_name(self, emp_name: str):
        self.__emp_name = emp_name

    @property
    def emp_id(self):
        return self.__emp_id
    @emp_id.setter
    def emp_id(self, emp_id: int):
        self.__emp_id = emp_id



class payslip:

    def __init__(self, emp_id: int, emp_name: str):
        self.emp_id = emp_id
        self.emp_name = emp_name
        
        pass
    @property
    def emp_name(self):
        return self.__emp_name
    @emp_name.setter
    def emp_name(self, emp_name: str):
        self.__emp_name = emp_name

    @property
    def emp_id(self):
        return self.__emp_id
    @emp_id.setter
    def emp_id(self, emp_id: int):
        self.__emp_id = emp_id



class Attendence:

    def __init__(self, emp_id: int, emp_name: str, Basic_salary: int, employee0: "Employee" = None):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.Basic_salary = Basic_salary
        self.employee0 = employee0
        
        pass
    @property
    def emp_id(self):
        return self.__emp_id
    @emp_id.setter
    def emp_id(self, emp_id: int):
        self.__emp_id = emp_id

    @property
    def emp_name(self):
        return self.__emp_name
    @emp_name.setter
    def emp_name(self, emp_name: str):
        self.__emp_name = emp_name

    @property
    def Basic_salary(self):
        return self.__Basic_salary
    @Basic_salary.setter
    def Basic_salary(self, Basic_salary: int):
        self.__Basic_salary = Basic_salary

    @property
    def employee0(self):
        return self.__employee0
    @employee0.setter
    def employee0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendence__employee0", None)
        self.__employee0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendence1"):
                opp_val = getattr(old_value, "attendence1", None)
                if opp_val == self:
                    setattr(old_value, "attendence1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendence1"):
                opp_val = getattr(value, "attendence1", None)
                setattr(value, "attendence1", self)



class EmployeeRequest:

    pass


class Admin:

    def __init__(self, adminEmail: str, password: int):
        self.adminEmail = adminEmail
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password

    @property
    def adminEmail(self):
        return self.__adminEmail
    @adminEmail.setter
    def adminEmail(self, adminEmail: str):
        self.__adminEmail = adminEmail



class Login:

    def __init__(self, username: str, password: int):
        self.username = username
        self.password = password
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: int):
        self.__password = password



class Salary:

    def __init__(self, emp_id: int, emp_name: str, basic_salary: str, employee3: "Employee" = None):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.basic_salary = basic_salary
        self.employee3 = employee3
        
        pass
    @property
    def emp_name(self):
        return self.__emp_name
    @emp_name.setter
    def emp_name(self, emp_name: str):
        self.__emp_name = emp_name

    @property
    def emp_id(self):
        return self.__emp_id
    @emp_id.setter
    def emp_id(self, emp_id: int):
        self.__emp_id = emp_id

    @property
    def basic_salary(self):
        return self.__basic_salary
    @basic_salary.setter
    def basic_salary(self, basic_salary: str):
        self.__basic_salary = basic_salary

    @property
    def employee3(self):
        return self.__employee3
    @employee3.setter
    def employee3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__employee3", None)
        self.__employee3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary2"):
                opp_val = getattr(old_value, "salary2", None)
                if opp_val == self:
                    setattr(old_value, "salary2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary2"):
                opp_val = getattr(value, "salary2", None)
                setattr(value, "salary2", self)



class Employee:

    def __init__(self, emp_id: int, emp_name: str, emp_email: str, attendence1: "Attendence" = None, salary2: "Salary" = None):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_email = emp_email
        self.attendence1 = attendence1
        self.salary2 = salary2
        
        pass
    @property
    def emp_name(self):
        return self.__emp_name
    @emp_name.setter
    def emp_name(self, emp_name: str):
        self.__emp_name = emp_name

    @property
    def emp_email(self):
        return self.__emp_email
    @emp_email.setter
    def emp_email(self, emp_email: str):
        self.__emp_email = emp_email

    @property
    def emp_id(self):
        return self.__emp_id
    @emp_id.setter
    def emp_id(self, emp_id: int):
        self.__emp_id = emp_id

    @property
    def salary2(self):
        return self.__salary2
    @salary2.setter
    def salary2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__salary2", None)
        self.__salary2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee3"):
                opp_val = getattr(old_value, "employee3", None)
                if opp_val == self:
                    setattr(old_value, "employee3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee3"):
                opp_val = getattr(value, "employee3", None)
                setattr(value, "employee3", self)

    @property
    def attendence1(self):
        return self.__attendence1
    @attendence1.setter
    def attendence1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__attendence1", None)
        self.__attendence1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee0"):
                opp_val = getattr(old_value, "employee0", None)
                if opp_val == self:
                    setattr(old_value, "employee0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee0"):
                opp_val = getattr(value, "employee0", None)
                setattr(value, "employee0", self)

