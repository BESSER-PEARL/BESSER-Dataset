from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Doctor:

    def __init__(self, DoctorID: int, Name: str, ContactNo: str, Email: str):
        self.DoctorID = DoctorID
        self.Name = Name
        self.ContactNo = ContactNo
        self.Email = Email
        
        pass
    @property
    def DoctorID(self):
        return self.__DoctorID
    @DoctorID.setter
    def DoctorID(self, DoctorID: int):
        self.__DoctorID = DoctorID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ContactNo(self):
        return self.__ContactNo
    @ContactNo.setter
    def ContactNo(self, ContactNo: str):
        self.__ContactNo = ContactNo

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email



class Shopping_Cart:

    def __init__(self, CartID: int, OrderID: int, Quantity: int, order5: "Order" = None):
        self.CartID = CartID
        self.OrderID = OrderID
        self.Quantity = Quantity
        self.order5 = order5
        
        pass
    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def CartID(self):
        return self.__CartID
    @CartID.setter
    def CartID(self, CartID: int):
        self.__CartID = CartID

    @property
    def order5(self):
        return self.__order5
    @order5.setter
    def order5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__order5", None)
        self.__order5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_0__4"):
                opp_val = getattr(old_value, "_0__4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_0__4"):
                opp_val = getattr(value, "_0__4", None)
                if opp_val is None:
                    setattr(value, "_0__4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Payment:

    def __init__(self, PaymentID: int, Method: str, OrderID: int, order3: "Order" = None):
        self.PaymentID = PaymentID
        self.Method = Method
        self.OrderID = OrderID
        self.order3 = order3
        
        pass
    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def PaymentID(self):
        return self.__PaymentID
    @PaymentID.setter
    def PaymentID(self, PaymentID: int):
        self.__PaymentID = PaymentID

    @property
    def Method(self):
        return self.__Method
    @Method.setter
    def Method(self, Method: str):
        self.__Method = Method

    @property
    def order3(self):
        return self.__order3
    @order3.setter
    def order3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order3", None)
        self.__order3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment2"):
                opp_val = getattr(old_value, "payment2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment2"):
                opp_val = getattr(value, "payment2", None)
                if opp_val is None:
                    setattr(value, "payment2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Manager:

    def __init__(self, ManagerID: int, Name: str, ContatctNo: str, Email: str):
        self.ManagerID = ManagerID
        self.Name = Name
        self.ContatctNo = ContatctNo
        self.Email = Email
        
        pass
    @property
    def ContatctNo(self):
        return self.__ContatctNo
    @ContatctNo.setter
    def ContatctNo(self, ContatctNo: str):
        self.__ContatctNo = ContatctNo

    @property
    def ManagerID(self):
        return self.__ManagerID
    @ManagerID.setter
    def ManagerID(self, ManagerID: int):
        self.__ManagerID = ManagerID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email



class Employee:

    def __init__(self, EmpID: int, Name: str, ContactNo: str, Department: str):
        self.EmpID = EmpID
        self.Name = Name
        self.ContactNo = ContactNo
        self.Department = Department
        
        pass
    @property
    def ContactNo(self):
        return self.__ContactNo
    @ContactNo.setter
    def ContactNo(self, ContactNo: str):
        self.__ContactNo = ContactNo

    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: str):
        self.__Department = Department

    @property
    def EmpID(self):
        return self.__EmpID
    @EmpID.setter
    def EmpID(self, EmpID: int):
        self.__EmpID = EmpID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class Pets:

    def __init__(self, PetID: int, PetType: str, PetName: str, Age: int):
        self.PetID = PetID
        self.PetType = PetType
        self.PetName = PetName
        self.Age = Age
        
        pass
    @property
    def PetID(self):
        return self.__PetID
    @PetID.setter
    def PetID(self, PetID: int):
        self.__PetID = PetID

    @property
    def PetName(self):
        return self.__PetName
    @PetName.setter
    def PetName(self, PetName: str):
        self.__PetName = PetName

    @property
    def PetType(self):
        return self.__PetType
    @PetType.setter
    def PetType(self, PetType: str):
        self.__PetType = PetType

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age



class Order:

    def __init__(self, OrderID: int, DateCreated: str, CusID: int, customer1: "Customer" = None, payment2: set["Payment"] = None, _0__4: set["Shopping_Cart"] = None):
        self.OrderID = OrderID
        self.DateCreated = DateCreated
        self.CusID = CusID
        self.customer1 = customer1
        self.payment2 = payment2 if payment2 is not None else set()
        self._0__4 = _0__4 if _0__4 is not None else set()
        
        pass
    @property
    def DateCreated(self):
        return self.__DateCreated
    @DateCreated.setter
    def DateCreated(self, DateCreated: str):
        self.__DateCreated = DateCreated

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def CusID(self):
        return self.__CusID
    @CusID.setter
    def CusID(self, CusID: int):
        self.__CusID = CusID

    @property
    def payment2(self):
        return self.__payment2
    @payment2.setter
    def payment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment2", None)
        self.__payment2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order3"):
                    opp_val = getattr(item, "order3", None)
                    
                    if opp_val == self:
                        setattr(item, "order3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order3"):
                    opp_val = getattr(item, "order3", None)
                    
                    setattr(item, "order3", self)
                    

    @property
    def _0__4(self):
        return self.___0__4
    @_0__4.setter
    def _0__4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order___0__4", None)
        self.___0__4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order5"):
                    opp_val = getattr(item, "order5", None)
                    
                    if opp_val == self:
                        setattr(item, "order5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order5"):
                    opp_val = getattr(item, "order5", None)
                    
                    setattr(item, "order5", self)
                    

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer1", None)
        self.__customer1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_0__0"):
                opp_val = getattr(old_value, "_0__0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_0__0"):
                opp_val = getattr(value, "_0__0", None)
                if opp_val is None:
                    setattr(value, "_0__0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Administrator:

    def __init__(self, adminID: str, Name: str):
        self.adminID = adminID
        self.Name = Name
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def adminID(self):
        return self.__adminID
    @adminID.setter
    def adminID(self, adminID: str):
        self.__adminID = adminID



class User:

    def __init__(self, UserID: str, Password: str):
        self.UserID = UserID
        self.Password = Password
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: str):
        self.__UserID = UserID

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password



class Customer:

    def __init__(self, ContactNo: str, Address: str, Email: str, CusID: int, Name: str, _0__0: set["Order"] = None):
        self.ContactNo = ContactNo
        self.Address = Address
        self.Email = Email
        self.CusID = CusID
        self.Name = Name
        self._0__0 = _0__0 if _0__0 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def CusID(self):
        return self.__CusID
    @CusID.setter
    def CusID(self, CusID: int):
        self.__CusID = CusID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def ContactNo(self):
        return self.__ContactNo
    @ContactNo.setter
    def ContactNo(self, ContactNo: str):
        self.__ContactNo = ContactNo

    @property
    def _0__0(self):
        return self.___0__0
    @_0__0.setter
    def _0__0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer___0__0", None)
        self.___0__0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer1"):
                    opp_val = getattr(item, "customer1", None)
                    
                    if opp_val == self:
                        setattr(item, "customer1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer1"):
                    opp_val = getattr(item, "customer1", None)
                    
                    setattr(item, "customer1", self)
                    

