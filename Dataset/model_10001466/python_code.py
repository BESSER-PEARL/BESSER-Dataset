from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Guest:

    def __init__(self, guestID: str):
        self.guestID = guestID
        
        pass
    @property
    def guestID(self):
        return self.__guestID
    @guestID.setter
    def guestID(self, guestID: str):
        self.__guestID = guestID



class Employee:

    def __init__(self, EmployeeID: str, EmpPassword: str, EmpName: str, orders4: "Orders" = None):
        self.EmployeeID = EmployeeID
        self.EmpPassword = EmpPassword
        self.EmpName = EmpName
        self.orders4 = orders4
        
        pass
    @property
    def EmpPassword(self):
        return self.__EmpPassword
    @EmpPassword.setter
    def EmpPassword(self, EmpPassword: str):
        self.__EmpPassword = EmpPassword

    @property
    def EmpName(self):
        return self.__EmpName
    @EmpName.setter
    def EmpName(self, EmpName: str):
        self.__EmpName = EmpName

    @property
    def EmployeeID(self):
        return self.__EmployeeID
    @EmployeeID.setter
    def EmployeeID(self, EmployeeID: str):
        self.__EmployeeID = EmployeeID

    @property
    def orders4(self):
        return self.__orders4
    @orders4.setter
    def orders4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__orders4", None)
        self.__orders4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee5"):
                opp_val = getattr(old_value, "employee5", None)
                if opp_val == self:
                    setattr(old_value, "employee5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee5"):
                opp_val = getattr(value, "employee5", None)
                setattr(value, "employee5", self)



class OrderDetails:

    def __init__(self, totPrice: str, orderTime: str, status: str, OrderID: int, quantity: int, MealID: str, orders7: "Orders" = None, cart10: "Cart" = None):
        self.totPrice = totPrice
        self.orderTime = orderTime
        self.status = status
        self.OrderID = OrderID
        self.quantity = quantity
        self.MealID = MealID
        self.orders7 = orders7
        self.cart10 = cart10
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def totPrice(self):
        return self.__totPrice
    @totPrice.setter
    def totPrice(self, totPrice: str):
        self.__totPrice = totPrice

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def MealID(self):
        return self.__MealID
    @MealID.setter
    def MealID(self, MealID: str):
        self.__MealID = MealID

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def orderTime(self):
        return self.__orderTime
    @orderTime.setter
    def orderTime(self, orderTime: str):
        self.__orderTime = orderTime

    @property
    def orders7(self):
        return self.__orders7
    @orders7.setter
    def orders7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetails__orders7", None)
        self.__orders7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetails6"):
                opp_val = getattr(old_value, "orderDetails6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetails6"):
                opp_val = getattr(value, "orderDetails6", None)
                if opp_val is None:
                    setattr(value, "orderDetails6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cart10(self):
        return self.__cart10
    @cart10.setter
    def cart10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderDetails__cart10", None)
        self.__cart10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderDetails11"):
                opp_val = getattr(old_value, "orderDetails11", None)
                if opp_val == self:
                    setattr(old_value, "orderDetails11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderDetails11"):
                opp_val = getattr(value, "orderDetails11", None)
                setattr(value, "orderDetails11", self)



class Meals:

    def __init__(self, unitPrice: str, Portion: str, supplier: str, MealID: str, MealName: str, MealType: str):
        self.unitPrice = unitPrice
        self.Portion = Portion
        self.supplier = supplier
        self.MealID = MealID
        self.MealName = MealName
        self.MealType = MealType
        
        pass
    @property
    def Portion(self):
        return self.__Portion
    @Portion.setter
    def Portion(self, Portion: str):
        self.__Portion = Portion

    @property
    def unitPrice(self):
        return self.__unitPrice
    @unitPrice.setter
    def unitPrice(self, unitPrice: str):
        self.__unitPrice = unitPrice

    @property
    def MealType(self):
        return self.__MealType
    @MealType.setter
    def MealType(self, MealType: str):
        self.__MealType = MealType

    @property
    def supplier(self):
        return self.__supplier
    @supplier.setter
    def supplier(self, supplier: str):
        self.__supplier = supplier

    @property
    def MealID(self):
        return self.__MealID
    @MealID.setter
    def MealID(self, MealID: str):
        self.__MealID = MealID

    @property
    def MealName(self):
        return self.__MealName
    @MealName.setter
    def MealName(self, MealName: str):
        self.__MealName = MealName



class Payment:

    def __init__(self, paymentID: str, PaymentType: str, PaymentStatus: str, paymentAmount: str, paymentDate: str, customer1: "Customer" = None, orders15: "Orders" = None):
        self.paymentID = paymentID
        self.PaymentType = PaymentType
        self.PaymentStatus = PaymentStatus
        self.paymentAmount = paymentAmount
        self.paymentDate = paymentDate
        self.customer1 = customer1
        self.orders15 = orders15
        
        pass
    @property
    def paymentDate(self):
        return self.__paymentDate
    @paymentDate.setter
    def paymentDate(self, paymentDate: str):
        self.__paymentDate = paymentDate

    @property
    def paymentID(self):
        return self.__paymentID
    @paymentID.setter
    def paymentID(self, paymentID: str):
        self.__paymentID = paymentID

    @property
    def paymentAmount(self):
        return self.__paymentAmount
    @paymentAmount.setter
    def paymentAmount(self, paymentAmount: str):
        self.__paymentAmount = paymentAmount

    @property
    def PaymentType(self):
        return self.__PaymentType
    @PaymentType.setter
    def PaymentType(self, PaymentType: str):
        self.__PaymentType = PaymentType

    @property
    def PaymentStatus(self):
        return self.__PaymentStatus
    @PaymentStatus.setter
    def PaymentStatus(self, PaymentStatus: str):
        self.__PaymentStatus = PaymentStatus

    @property
    def orders15(self):
        return self.__orders15
    @orders15.setter
    def orders15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__orders15", None)
        self.__orders15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment14"):
                opp_val = getattr(old_value, "payment14", None)
                if opp_val == self:
                    setattr(old_value, "payment14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment14"):
                opp_val = getattr(value, "payment14", None)
                setattr(value, "payment14", self)

    @property
    def customer1(self):
        return self.__customer1
    @customer1.setter
    def customer1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__customer1", None)
        self.__customer1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment0"):
                opp_val = getattr(old_value, "payment0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment0"):
                opp_val = getattr(value, "payment0", None)
                if opp_val is None:
                    setattr(value, "payment0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Admin:

    pass


class Transport:

    def __init__(self, TransportID: int, location: str, transportCost: str, orders13: "Orders" = None):
        self.TransportID = TransportID
        self.location = location
        self.transportCost = transportCost
        self.orders13 = orders13
        
        pass
    @property
    def transportCost(self):
        return self.__transportCost
    @transportCost.setter
    def transportCost(self, transportCost: str):
        self.__transportCost = transportCost

    @property
    def TransportID(self):
        return self.__TransportID
    @TransportID.setter
    def TransportID(self, TransportID: int):
        self.__TransportID = TransportID

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def orders13(self):
        return self.__orders13
    @orders13.setter
    def orders13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transport__orders13", None)
        self.__orders13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transport12"):
                opp_val = getattr(old_value, "transport12", None)
                if opp_val == self:
                    setattr(old_value, "transport12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transport12"):
                opp_val = getattr(value, "transport12", None)
                setattr(value, "transport12", self)



class User:

    def __init__(self, userID: str, Password: str, loginStatus: str):
        self.userID = userID
        self.Password = Password
        self.loginStatus = loginStatus
        
        pass
    @property
    def loginStatus(self):
        return self.__loginStatus
    @loginStatus.setter
    def loginStatus(self, loginStatus: str):
        self.__loginStatus = loginStatus

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def userID(self):
        return self.__userID
    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID



class Orders:

    def __init__(self, OrderID: int, dateOrdered: str, status: str, dateFinished: str, customer3: "Customer" = None, employee5: "Employee" = None, orderDetails6: set["OrderDetails"] = None, transport12: "Transport" = None, payment14: "Payment" = None):
        self.OrderID = OrderID
        self.dateOrdered = dateOrdered
        self.status = status
        self.dateFinished = dateFinished
        self.customer3 = customer3
        self.employee5 = employee5
        self.orderDetails6 = orderDetails6 if orderDetails6 is not None else set()
        self.transport12 = transport12
        self.payment14 = payment14
        
        pass
    @property
    def dateFinished(self):
        return self.__dateFinished
    @dateFinished.setter
    def dateFinished(self, dateFinished: str):
        self.__dateFinished = dateFinished

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def dateOrdered(self):
        return self.__dateOrdered
    @dateOrdered.setter
    def dateOrdered(self, dateOrdered: str):
        self.__dateOrdered = dateOrdered

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders2"):
                opp_val = getattr(old_value, "orders2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders2"):
                opp_val = getattr(value, "orders2", None)
                if opp_val is None:
                    setattr(value, "orders2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transport12(self):
        return self.__transport12
    @transport12.setter
    def transport12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__transport12", None)
        self.__transport12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders13"):
                opp_val = getattr(old_value, "orders13", None)
                if opp_val == self:
                    setattr(old_value, "orders13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders13"):
                opp_val = getattr(value, "orders13", None)
                setattr(value, "orders13", self)

    @property
    def payment14(self):
        return self.__payment14
    @payment14.setter
    def payment14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__payment14", None)
        self.__payment14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders15"):
                opp_val = getattr(old_value, "orders15", None)
                if opp_val == self:
                    setattr(old_value, "orders15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders15"):
                opp_val = getattr(value, "orders15", None)
                setattr(value, "orders15", self)

    @property
    def orderDetails6(self):
        return self.__orderDetails6
    @orderDetails6.setter
    def orderDetails6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__orderDetails6", None)
        self.__orderDetails6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orders7"):
                    opp_val = getattr(item, "orders7", None)
                    
                    if opp_val == self:
                        setattr(item, "orders7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orders7"):
                    opp_val = getattr(item, "orders7", None)
                    
                    setattr(item, "orders7", self)
                    

    @property
    def employee5(self):
        return self.__employee5
    @employee5.setter
    def employee5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__employee5", None)
        self.__employee5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders4"):
                opp_val = getattr(old_value, "orders4", None)
                if opp_val == self:
                    setattr(old_value, "orders4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders4"):
                opp_val = getattr(value, "orders4", None)
                setattr(value, "orders4", self)



class Cart:

    def __init__(self, cartID: int, ProductID: str, Quantity: int, date: str, customer9: "Customer" = None, orderDetails11: "OrderDetails" = None):
        self.cartID = cartID
        self.ProductID = ProductID
        self.Quantity = Quantity
        self.date = date
        self.customer9 = customer9
        self.orderDetails11 = orderDetails11
        
        pass
    @property
    def cartID(self):
        return self.__cartID
    @cartID.setter
    def cartID(self, cartID: int):
        self.__cartID = cartID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: str):
        self.__ProductID = ProductID

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def orderDetails11(self):
        return self.__orderDetails11
    @orderDetails11.setter
    def orderDetails11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__orderDetails11", None)
        self.__orderDetails11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart10"):
                opp_val = getattr(old_value, "cart10", None)
                if opp_val == self:
                    setattr(old_value, "cart10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart10"):
                opp_val = getattr(value, "cart10", None)
                setattr(value, "cart10", self)

    @property
    def customer9(self):
        return self.__customer9
    @customer9.setter
    def customer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__customer9", None)
        self.__customer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart8"):
                opp_val = getattr(old_value, "cart8", None)
                if opp_val == self:
                    setattr(old_value, "cart8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart8"):
                opp_val = getattr(value, "cart8", None)
                setattr(value, "cart8", self)



class Customer:

    def __init__(self, CustomerName: str, CutsomerAddress: str, PhoneNumber: int, Email: str, payment0: set["Payment"] = None, orders2: set["Orders"] = None, cart8: "Cart" = None):
        self.CustomerName = CustomerName
        self.CutsomerAddress = CutsomerAddress
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.payment0 = payment0 if payment0 is not None else set()
        self.orders2 = orders2 if orders2 is not None else set()
        self.cart8 = cart8
        
        pass
    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def CutsomerAddress(self):
        return self.__CutsomerAddress
    @CutsomerAddress.setter
    def CutsomerAddress(self, CutsomerAddress: str):
        self.__CutsomerAddress = CutsomerAddress

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def PhoneNumber(self):
        return self.__PhoneNumber
    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber: int):
        self.__PhoneNumber = PhoneNumber

    @property
    def cart8(self):
        return self.__cart8
    @cart8.setter
    def cart8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__cart8", None)
        self.__cart8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer9"):
                opp_val = getattr(old_value, "customer9", None)
                if opp_val == self:
                    setattr(old_value, "customer9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer9"):
                opp_val = getattr(value, "customer9", None)
                setattr(value, "customer9", self)

    @property
    def payment0(self):
        return self.__payment0
    @payment0.setter
    def payment0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__payment0", None)
        self.__payment0 = value if value is not None else set()
        
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
                    

    @property
    def orders2(self):
        return self.__orders2
    @orders2.setter
    def orders2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__orders2", None)
        self.__orders2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer3"):
                    opp_val = getattr(item, "customer3", None)
                    
                    if opp_val == self:
                        setattr(item, "customer3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer3"):
                    opp_val = getattr(item, "customer3", None)
                    
                    setattr(item, "customer3", self)
                    

