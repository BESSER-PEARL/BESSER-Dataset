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


class Manager2:

    def __init__(self, id: int, password: str, name: str, employee15: set["Employee1"] = None):
        self.id = id
        self.password = password
        self.name = name
        self.employee15 = employee15 if employee15 is not None else set()
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def employee15(self):
        return self.__employee15
    @employee15.setter
    def employee15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager2__employee15", None)
        self.__employee15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "manager14"):
                    opp_val = getattr(item, "manager14", None)
                    
                    if opp_val == self:
                        setattr(item, "manager14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "manager14"):
                    opp_val = getattr(item, "manager14", None)
                    
                    setattr(item, "manager14", self)
                    



class Customer1:

    def __init__(self, Customer_Name: str, S: str):
        self.Customer_Name = Customer_Name
        self.S = S
        
        pass
    @property
    def Customer_Name(self):
        return self.__Customer_Name
    @Customer_Name.setter
    def Customer_Name(self, Customer_Name: str):
        self.__Customer_Name = Customer_Name

    @property
    def S(self):
        return self.__S
    @S.setter
    def S(self, S: str):
        self.__S = S



class Manager1:

    def __init__(self, Manager_id: int, Password: str, Name: str):
        self.Manager_id = Manager_id
        self.Password = Password
        self.Name = Name
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Manager_id(self):
        return self.__Manager_id
    @Manager_id.setter
    def Manager_id(self, Manager_id: int):
        self.__Manager_id = Manager_id



class Order:

    def __init__(self, id: int, name: str, customer9: "Customer" = None, admin13: "Admin1" = None):
        self.id = id
        self.name = name
        self.customer9 = customer9
        self.admin13 = admin13
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def customer9(self):
        return self.__customer9
    @customer9.setter
    def customer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer9", None)
        self.__customer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order8"):
                opp_val = getattr(old_value, "order8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order8"):
                opp_val = getattr(value, "order8", None)
                if opp_val is None:
                    setattr(value, "order8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def admin13(self):
        return self.__admin13
    @admin13.setter
    def admin13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__admin13", None)
        self.__admin13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order12"):
                opp_val = getattr(old_value, "order12", None)
                if opp_val == self:
                    setattr(old_value, "order12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order12"):
                opp_val = getattr(value, "order12", None)
                setattr(value, "order12", self)



class Manager:

    def __init__(self, UserName: str, password: str):
        self.UserName = UserName
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName



class Customer:

    def __init__(self, UserName: str, password: str, address: str, postal_code: int, country: str, order8: set["Order"] = None):
        self.UserName = UserName
        self.password = password
        self.address = address
        self.postal_code = postal_code
        self.country = country
        self.order8 = order8 if order8 is not None else set()
        
        pass
    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def postal_code(self):
        return self.__postal_code
    @postal_code.setter
    def postal_code(self, postal_code: int):
        self.__postal_code = postal_code

    @property
    def order8(self):
        return self.__order8
    @order8.setter
    def order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order8", None)
        self.__order8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer9"):
                    opp_val = getattr(item, "customer9", None)
                    
                    if opp_val == self:
                        setattr(item, "customer9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer9"):
                    opp_val = getattr(item, "customer9", None)
                    
                    setattr(item, "customer9", self)
                    



class Employee1:

    def __init__(self, UserName: str, password: str, name: str, contact_no: int, Email: str, attribute: str, Emp_Address: str, Emp_Dep: str, Salary: int, admin11: "Admin1" = None, manager14: "Manager2" = None):
        self.UserName = UserName
        self.password = password
        self.name = name
        self.contact_no = contact_no
        self.Email = Email
        self.attribute = attribute
        self.Emp_Address = Emp_Address
        self.Emp_Dep = Emp_Dep
        self.Salary = Salary
        self.admin11 = admin11
        self.manager14 = manager14
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def contact_no(self):
        return self.__contact_no
    @contact_no.setter
    def contact_no(self, contact_no: int):
        self.__contact_no = contact_no

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: int):
        self.__Salary = Salary

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Emp_Dep(self):
        return self.__Emp_Dep
    @Emp_Dep.setter
    def Emp_Dep(self, Emp_Dep: str):
        self.__Emp_Dep = Emp_Dep

    @property
    def Emp_Address(self):
        return self.__Emp_Address
    @Emp_Address.setter
    def Emp_Address(self, Emp_Address: str):
        self.__Emp_Address = Emp_Address

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def admin11(self):
        return self.__admin11
    @admin11.setter
    def admin11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee1__admin11", None)
        self.__admin11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee10"):
                opp_val = getattr(old_value, "employee10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee10"):
                opp_val = getattr(value, "employee10", None)
                if opp_val is None:
                    setattr(value, "employee10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def manager14(self):
        return self.__manager14
    @manager14.setter
    def manager14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee1__manager14", None)
        self.__manager14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee15"):
                opp_val = getattr(old_value, "employee15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee15"):
                opp_val = getattr(value, "employee15", None)
                if opp_val is None:
                    setattr(value, "employee15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Admin1:

    def __init__(self, UserName: str, password: str, employee10: set["Employee1"] = None, order12: "Order" = None):
        self.UserName = UserName
        self.password = password
        self.employee10 = employee10 if employee10 is not None else set()
        self.order12 = order12
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def employee10(self):
        return self.__employee10
    @employee10.setter
    def employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin1__employee10", None)
        self.__employee10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin11"):
                    opp_val = getattr(item, "admin11", None)
                    
                    if opp_val == self:
                        setattr(item, "admin11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin11"):
                    opp_val = getattr(item, "admin11", None)
                    
                    setattr(item, "admin11", self)
                    

    @property
    def order12(self):
        return self.__order12
    @order12.setter
    def order12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin1__order12", None)
        self.__order12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin13"):
                opp_val = getattr(old_value, "admin13", None)
                if opp_val == self:
                    setattr(old_value, "admin13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin13"):
                opp_val = getattr(value, "admin13", None)
                setattr(value, "admin13", self)



class Users1:

    def __init__(self, id: str, password: str):
        self.id = id
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id



class Admin:

    def __init__(self, UserName: str, Password: str):
        self.UserName = UserName
        self.Password = Password
        
        pass
    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password



class Employee_Management_System_Component:

    pass


class Users:

    def __init__(self, UserName: str, Password: str):
        self.UserName = UserName
        self.Password = Password
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName



class Leave:

    def __init__(self, leave_id: int, Emp_Id: int, Leave_Title: str, Leave_detail: str, Leave_EndDate: date, Leave_Status: str, employee1: "Employee" = None):
        self.leave_id = leave_id
        self.Emp_Id = Emp_Id
        self.Leave_Title = Leave_Title
        self.Leave_detail = Leave_detail
        self.Leave_EndDate = Leave_EndDate
        self.Leave_Status = Leave_Status
        self.employee1 = employee1
        
        pass
    @property
    def Leave_EndDate(self):
        return self.__Leave_EndDate
    @Leave_EndDate.setter
    def Leave_EndDate(self, Leave_EndDate: date):
        self.__Leave_EndDate = Leave_EndDate

    @property
    def Leave_Status(self):
        return self.__Leave_Status
    @Leave_Status.setter
    def Leave_Status(self, Leave_Status: str):
        self.__Leave_Status = Leave_Status

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def Leave_detail(self):
        return self.__Leave_detail
    @Leave_detail.setter
    def Leave_detail(self, Leave_detail: str):
        self.__Leave_detail = Leave_detail

    @property
    def Leave_Title(self):
        return self.__Leave_Title
    @Leave_Title.setter
    def Leave_Title(self, Leave_Title: str):
        self.__Leave_Title = Leave_Title

    @property
    def leave_id(self):
        return self.__leave_id
    @leave_id.setter
    def leave_id(self, leave_id: int):
        self.__leave_id = leave_id

    @property
    def employee1(self):
        return self.__employee1
    @employee1.setter
    def employee1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Leave__employee1", None)
        self.__employee1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leave0"):
                opp_val = getattr(old_value, "leave0", None)
                if opp_val == self:
                    setattr(old_value, "leave0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leave0"):
                opp_val = getattr(value, "leave0", None)
                setattr(value, "leave0", self)



class Salary:

    def __init__(self, Emp_Id: int, Sly_Basic: float, Sly_Increment: float, Sly_Decrement: float, Sly_Netgross: float, OverTime: str, employee3: "Employee" = None):
        self.Emp_Id = Emp_Id
        self.Sly_Basic = Sly_Basic
        self.Sly_Increment = Sly_Increment
        self.Sly_Decrement = Sly_Decrement
        self.Sly_Netgross = Sly_Netgross
        self.OverTime = OverTime
        self.employee3 = employee3
        
        pass
    @property
    def Sly_Netgross(self):
        return self.__Sly_Netgross
    @Sly_Netgross.setter
    def Sly_Netgross(self, Sly_Netgross: float):
        self.__Sly_Netgross = Sly_Netgross

    @property
    def Sly_Increment(self):
        return self.__Sly_Increment
    @Sly_Increment.setter
    def Sly_Increment(self, Sly_Increment: float):
        self.__Sly_Increment = Sly_Increment

    @property
    def Sly_Basic(self):
        return self.__Sly_Basic
    @Sly_Basic.setter
    def Sly_Basic(self, Sly_Basic: float):
        self.__Sly_Basic = Sly_Basic

    @property
    def Sly_Decrement(self):
        return self.__Sly_Decrement
    @Sly_Decrement.setter
    def Sly_Decrement(self, Sly_Decrement: float):
        self.__Sly_Decrement = Sly_Decrement

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def OverTime(self):
        return self.__OverTime
    @OverTime.setter
    def OverTime(self, OverTime: str):
        self.__OverTime = OverTime

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

    def __init__(self, Emp_Id: int, Password: str, Emp_Name: str, Emp_ContactNo: str, Emp_Email: str, Emp_Address: str, Emp_Department: str, Emp_Salary: float, leave0: "Leave" = None, salary2: "Salary" = None):
        self.Emp_Id = Emp_Id
        self.Password = Password
        self.Emp_Name = Emp_Name
        self.Emp_ContactNo = Emp_ContactNo
        self.Emp_Email = Emp_Email
        self.Emp_Address = Emp_Address
        self.Emp_Department = Emp_Department
        self.Emp_Salary = Emp_Salary
        self.leave0 = leave0
        self.salary2 = salary2
        
        pass
    @property
    def Emp_Address(self):
        return self.__Emp_Address
    @Emp_Address.setter
    def Emp_Address(self, Emp_Address: str):
        self.__Emp_Address = Emp_Address

    @property
    def Emp_ContactNo(self):
        return self.__Emp_ContactNo
    @Emp_ContactNo.setter
    def Emp_ContactNo(self, Emp_ContactNo: str):
        self.__Emp_ContactNo = Emp_ContactNo

    @property
    def Emp_Name(self):
        return self.__Emp_Name
    @Emp_Name.setter
    def Emp_Name(self, Emp_Name: str):
        self.__Emp_Name = Emp_Name

    @property
    def Emp_Id(self):
        return self.__Emp_Id
    @Emp_Id.setter
    def Emp_Id(self, Emp_Id: int):
        self.__Emp_Id = Emp_Id

    @property
    def Emp_Email(self):
        return self.__Emp_Email
    @Emp_Email.setter
    def Emp_Email(self, Emp_Email: str):
        self.__Emp_Email = Emp_Email

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Emp_Salary(self):
        return self.__Emp_Salary
    @Emp_Salary.setter
    def Emp_Salary(self, Emp_Salary: float):
        self.__Emp_Salary = Emp_Salary

    @property
    def Emp_Department(self):
        return self.__Emp_Department
    @Emp_Department.setter
    def Emp_Department(self, Emp_Department: str):
        self.__Emp_Department = Emp_Department

    @property
    def leave0(self):
        return self.__leave0
    @leave0.setter
    def leave0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__leave0", None)
        self.__leave0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee1"):
                opp_val = getattr(old_value, "employee1", None)
                if opp_val == self:
                    setattr(old_value, "employee1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee1"):
                opp_val = getattr(value, "employee1", None)
                setattr(value, "employee1", self)

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

