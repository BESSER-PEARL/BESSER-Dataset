from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class PaymentMethod:

    def __init__(self, paymentType: str, online: str, cashOnDelievery: str, cart9: "Cart" = None):
        self.paymentType = paymentType
        self.online = online
        self.cashOnDelievery = cashOnDelievery
        self.cart9 = cart9
        
        pass
    @property
    def cashOnDelievery(self):
        return self.__cashOnDelievery
    @cashOnDelievery.setter
    def cashOnDelievery(self, cashOnDelievery: str):
        self.__cashOnDelievery = cashOnDelievery

    @property
    def paymentType(self):
        return self.__paymentType
    @paymentType.setter
    def paymentType(self, paymentType: str):
        self.__paymentType = paymentType

    @property
    def online(self):
        return self.__online
    @online.setter
    def online(self, online: str):
        self.__online = online

    @property
    def cart9(self):
        return self.__cart9
    @cart9.setter
    def cart9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PaymentMethod__cart9", None)
        self.__cart9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paymentMethod8"):
                opp_val = getattr(old_value, "paymentMethod8", None)
                if opp_val == self:
                    setattr(old_value, "paymentMethod8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paymentMethod8"):
                opp_val = getattr(value, "paymentMethod8", None)
                setattr(value, "paymentMethod8", self)



class ExerciseMachine:

    def __init__(self, id: int, name: str, type: str, size: int, product5: "Product" = None):
        self.id = id
        self.name = name
        self.type = type
        self.size = size
        self.product5 = product5
        
        pass
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

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
    def product5(self):
        return self.__product5
    @product5.setter
    def product5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ExerciseMachine__product5", None)
        self.__product5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exerciseMachine4"):
                opp_val = getattr(old_value, "exerciseMachine4", None)
                if opp_val == self:
                    setattr(old_value, "exerciseMachine4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exerciseMachine4"):
                opp_val = getattr(value, "exerciseMachine4", None)
                setattr(value, "exerciseMachine4", self)



class MediDevices:

    def __init__(self, id: str, name: str, type: str, product3: "Product" = None):
        self.id = id
        self.name = name
        self.type = type
        self.product3 = product3
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def product3(self):
        return self.__product3
    @product3.setter
    def product3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MediDevices__product3", None)
        self.__product3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mediDevices2"):
                opp_val = getattr(old_value, "mediDevices2", None)
                if opp_val == self:
                    setattr(old_value, "mediDevices2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mediDevices2"):
                opp_val = getattr(value, "mediDevices2", None)
                setattr(value, "mediDevices2", self)



class Cart:

    def __init__(self, id: int, TotalBill: int, order7: "Order" = None, paymentMethod8: "PaymentMethod" = None):
        self.id = id
        self.TotalBill = TotalBill
        self.order7 = order7
        self.paymentMethod8 = paymentMethod8
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def TotalBill(self):
        return self.__TotalBill
    @TotalBill.setter
    def TotalBill(self, TotalBill: int):
        self.__TotalBill = TotalBill

    @property
    def paymentMethod8(self):
        return self.__paymentMethod8
    @paymentMethod8.setter
    def paymentMethod8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__paymentMethod8", None)
        self.__paymentMethod8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart9"):
                opp_val = getattr(old_value, "cart9", None)
                if opp_val == self:
                    setattr(old_value, "cart9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart9"):
                opp_val = getattr(value, "cart9", None)
                setattr(value, "cart9", self)

    @property
    def order7(self):
        return self.__order7
    @order7.setter
    def order7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__order7", None)
        self.__order7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart6"):
                opp_val = getattr(old_value, "cart6", None)
                if opp_val == self:
                    setattr(old_value, "cart6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart6"):
                opp_val = getattr(value, "cart6", None)
                setattr(value, "cart6", self)



class Medicine:

    def __init__(self, id: int, name: str, formula: str, potency: str, product1: "Product" = None):
        self.id = id
        self.name = name
        self.formula = formula
        self.potency = potency
        self.product1 = product1
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def potency(self):
        return self.__potency
    @potency.setter
    def potency(self, potency: str):
        self.__potency = potency

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def formula(self):
        return self.__formula
    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula

    @property
    def product1(self):
        return self.__product1
    @product1.setter
    def product1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medicine__product1", None)
        self.__product1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medicine0"):
                opp_val = getattr(old_value, "medicine0", None)
                if opp_val == self:
                    setattr(old_value, "medicine0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medicine0"):
                opp_val = getattr(value, "medicine0", None)
                setattr(value, "medicine0", self)



class Customer:

    def __init__(self, id: int, userName: str, password: str):
        self.id = id
        self.userName = userName
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
    def id(self, id: int):
        self.__id = id

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName



class Admin:

    def __init__(self, id: int, userName: str, password: str, registration10: "Registration" = None, product14: "Product" = None):
        self.id = id
        self.userName = userName
        self.password = password
        self.registration10 = registration10
        self.product14 = product14
        
        pass
    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def registration10(self):
        return self.__registration10
    @registration10.setter
    def registration10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__registration10", None)
        self.__registration10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin11"):
                opp_val = getattr(old_value, "admin11", None)
                if opp_val == self:
                    setattr(old_value, "admin11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin11"):
                opp_val = getattr(value, "admin11", None)
                setattr(value, "admin11", self)

    @property
    def product14(self):
        return self.__product14
    @product14.setter
    def product14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__product14", None)
        self.__product14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin15"):
                opp_val = getattr(old_value, "admin15", None)
                if opp_val == self:
                    setattr(old_value, "admin15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin15"):
                opp_val = getattr(value, "admin15", None)
                setattr(value, "admin15", self)



class Order:

    def __init__(self, id: int, orderDate: str, quantity: int, orderStatus: str, cart6: "Cart" = None, product17: "Product" = None):
        self.id = id
        self.orderDate = orderDate
        self.quantity = quantity
        self.orderStatus = orderStatus
        self.cart6 = cart6
        self.product17 = product17
        
        pass
    @property
    def orderStatus(self):
        return self.__orderStatus
    @orderStatus.setter
    def orderStatus(self, orderStatus: str):
        self.__orderStatus = orderStatus

    @property
    def orderDate(self):
        return self.__orderDate
    @orderDate.setter
    def orderDate(self, orderDate: str):
        self.__orderDate = orderDate

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def cart6(self):
        return self.__cart6
    @cart6.setter
    def cart6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__cart6", None)
        self.__cart6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order7"):
                opp_val = getattr(old_value, "order7", None)
                if opp_val == self:
                    setattr(old_value, "order7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order7"):
                opp_val = getattr(value, "order7", None)
                setattr(value, "order7", self)

    @property
    def product17(self):
        return self.__product17
    @product17.setter
    def product17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__product17", None)
        self.__product17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order16"):
                opp_val = getattr(old_value, "order16", None)
                if opp_val == self:
                    setattr(old_value, "order16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order16"):
                opp_val = getattr(value, "order16", None)
                setattr(value, "order16", self)



class Product:

    def __init__(self, pID: str, name: str, price: int, manufecturer: str, manufecturedDate: str, expiry: str, color: str, medicine0: "Medicine" = None, mediDevices2: "MediDevices" = None, exerciseMachine4: "ExerciseMachine" = None, person13: "Person" = None, admin15: "Admin" = None, order16: "Order" = None):
        self.pID = pID
        self.name = name
        self.price = price
        self.manufecturer = manufecturer
        self.manufecturedDate = manufecturedDate
        self.expiry = expiry
        self.color = color
        self.medicine0 = medicine0
        self.mediDevices2 = mediDevices2
        self.exerciseMachine4 = exerciseMachine4
        self.person13 = person13
        self.admin15 = admin15
        self.order16 = order16
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def manufecturer(self):
        return self.__manufecturer
    @manufecturer.setter
    def manufecturer(self, manufecturer: str):
        self.__manufecturer = manufecturer

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def manufecturedDate(self):
        return self.__manufecturedDate
    @manufecturedDate.setter
    def manufecturedDate(self, manufecturedDate: str):
        self.__manufecturedDate = manufecturedDate

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def pID(self):
        return self.__pID
    @pID.setter
    def pID(self, pID: str):
        self.__pID = pID

    @property
    def expiry(self):
        return self.__expiry
    @expiry.setter
    def expiry(self, expiry: str):
        self.__expiry = expiry

    @property
    def exerciseMachine4(self):
        return self.__exerciseMachine4
    @exerciseMachine4.setter
    def exerciseMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__exerciseMachine4", None)
        self.__exerciseMachine4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product5"):
                opp_val = getattr(old_value, "product5", None)
                if opp_val == self:
                    setattr(old_value, "product5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product5"):
                opp_val = getattr(value, "product5", None)
                setattr(value, "product5", self)

    @property
    def medicine0(self):
        return self.__medicine0
    @medicine0.setter
    def medicine0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__medicine0", None)
        self.__medicine0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product1"):
                opp_val = getattr(old_value, "product1", None)
                if opp_val == self:
                    setattr(old_value, "product1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product1"):
                opp_val = getattr(value, "product1", None)
                setattr(value, "product1", self)

    @property
    def admin15(self):
        return self.__admin15
    @admin15.setter
    def admin15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__admin15", None)
        self.__admin15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product14"):
                opp_val = getattr(old_value, "product14", None)
                if opp_val == self:
                    setattr(old_value, "product14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product14"):
                opp_val = getattr(value, "product14", None)
                setattr(value, "product14", self)

    @property
    def order16(self):
        return self.__order16
    @order16.setter
    def order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__order16", None)
        self.__order16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product17"):
                opp_val = getattr(old_value, "product17", None)
                if opp_val == self:
                    setattr(old_value, "product17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product17"):
                opp_val = getattr(value, "product17", None)
                setattr(value, "product17", self)

    @property
    def mediDevices2(self):
        return self.__mediDevices2
    @mediDevices2.setter
    def mediDevices2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__mediDevices2", None)
        self.__mediDevices2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product3"):
                opp_val = getattr(old_value, "product3", None)
                if opp_val == self:
                    setattr(old_value, "product3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product3"):
                opp_val = getattr(value, "product3", None)
                setattr(value, "product3", self)

    @property
    def person13(self):
        return self.__person13
    @person13.setter
    def person13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__person13", None)
        self.__person13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product12"):
                opp_val = getattr(old_value, "product12", None)
                if opp_val == self:
                    setattr(old_value, "product12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product12"):
                opp_val = getattr(value, "product12", None)
                setattr(value, "product12", self)



class Person:

    def __init__(self, Name: str, LastName: str, DOB: str, Address: str, Phone: int, Email: str, registration18: "Registration" = None, product12: "Product" = None):
        self.Name = Name
        self.LastName = LastName
        self.DOB = DOB
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.registration18 = registration18
        self.product12 = product12
        
        pass
    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: int):
        self.__Phone = Phone

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def DOB(self):
        return self.__DOB
    @DOB.setter
    def DOB(self, DOB: str):
        self.__DOB = DOB

    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, LastName: str):
        self.__LastName = LastName

    @property
    def product12(self):
        return self.__product12
    @product12.setter
    def product12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__product12", None)
        self.__product12 = value
        
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
    def registration18(self):
        return self.__registration18
    @registration18.setter
    def registration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__registration18", None)
        self.__registration18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person19"):
                opp_val = getattr(old_value, "person19", None)
                if opp_val == self:
                    setattr(old_value, "person19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person19"):
                opp_val = getattr(value, "person19", None)
                setattr(value, "person19", self)



class Registration:

    def __init__(self, name: str, LastName: str, DOB: str, UserName: str, Password: str, Address: str, Phone: int, Email: str, person19: "Person" = None, admin11: "Admin" = None):
        self.name = name
        self.LastName = LastName
        self.DOB = DOB
        self.UserName = UserName
        self.Password = Password
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.person19 = person19
        self.admin11 = admin11
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, LastName: str):
        self.__LastName = LastName

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: int):
        self.__Phone = Phone

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def DOB(self):
        return self.__DOB
    @DOB.setter
    def DOB(self, DOB: str):
        self.__DOB = DOB

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def person19(self):
        return self.__person19
    @person19.setter
    def person19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registration__person19", None)
        self.__person19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registration18"):
                opp_val = getattr(old_value, "registration18", None)
                if opp_val == self:
                    setattr(old_value, "registration18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registration18"):
                opp_val = getattr(value, "registration18", None)
                setattr(value, "registration18", self)

    @property
    def admin11(self):
        return self.__admin11
    @admin11.setter
    def admin11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registration__admin11", None)
        self.__admin11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registration10"):
                opp_val = getattr(old_value, "registration10", None)
                if opp_val == self:
                    setattr(old_value, "registration10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registration10"):
                opp_val = getattr(value, "registration10", None)
                setattr(value, "registration10", self)

