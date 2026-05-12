from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Login:

    def __init__(self, LoyaltyID: int, Discount: int, processQuery12: "processQuery" = None):
        self.LoyaltyID = LoyaltyID
        self.Discount = Discount
        self.processQuery12 = processQuery12
        
        pass
    @property
    def LoyaltyID(self):
        return self.__LoyaltyID
    @LoyaltyID.setter
    def LoyaltyID(self, LoyaltyID: int):
        self.__LoyaltyID = LoyaltyID

    @property
    def Discount(self):
        return self.__Discount
    @Discount.setter
    def Discount(self, Discount: int):
        self.__Discount = Discount

    @property
    def processQuery12(self):
        return self.__processQuery12
    @processQuery12.setter
    def processQuery12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__processQuery12", None)
        self.__processQuery12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login13"):
                opp_val = getattr(old_value, "login13", None)
                if opp_val == self:
                    setattr(old_value, "login13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login13"):
                opp_val = getattr(value, "login13", None)
                setattr(value, "login13", self)



class processQuery:

    pass


class AdminController:

    def __init__(self, UserID: int, UserName: str, UserLevel: int, processQuery7: "processQuery" = None):
        self.UserID = UserID
        self.UserName = UserName
        self.UserLevel = UserLevel
        self.processQuery7 = processQuery7
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def UserLevel(self):
        return self.__UserLevel
    @UserLevel.setter
    def UserLevel(self, UserLevel: int):
        self.__UserLevel = UserLevel

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def processQuery7(self):
        return self.__processQuery7
    @processQuery7.setter
    def processQuery7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AdminController__processQuery7", None)
        self.__processQuery7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adminPanel6"):
                opp_val = getattr(old_value, "adminPanel6", None)
                if opp_val == self:
                    setattr(old_value, "adminPanel6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adminPanel6"):
                opp_val = getattr(value, "adminPanel6", None)
                setattr(value, "adminPanel6", self)



class Membership_Card:

    def __init__(self, LoyaltyID: int, Discount: int, order5: set["OrderController"] = None):
        self.LoyaltyID = LoyaltyID
        self.Discount = Discount
        self.order5 = order5 if order5 is not None else set()
        
        pass
    @property
    def LoyaltyID(self):
        return self.__LoyaltyID
    @LoyaltyID.setter
    def LoyaltyID(self, LoyaltyID: int):
        self.__LoyaltyID = LoyaltyID

    @property
    def Discount(self):
        return self.__Discount
    @Discount.setter
    def Discount(self, Discount: int):
        self.__Discount = Discount

    @property
    def order5(self):
        return self.__order5
    @order5.setter
    def order5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Membership_Card__order5", None)
        self.__order5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "membership_Card4"):
                    opp_val = getattr(item, "membership_Card4", None)
                    
                    if opp_val == self:
                        setattr(item, "membership_Card4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "membership_Card4"):
                    opp_val = getattr(item, "membership_Card4", None)
                    
                    setattr(item, "membership_Card4", self)
                    



class OrderController:

    def __init__(self, OrderID: int, Date: str, UserID: int, OrderTotal: str, membership_Card4: "Membership_Card" = None, processQuery11: "processQuery" = None, is_ordered_by0: "Table" = None):
        self.OrderID = OrderID
        self.Date = Date
        self.UserID = UserID
        self.OrderTotal = OrderTotal
        self.membership_Card4 = membership_Card4
        self.processQuery11 = processQuery11
        self.is_ordered_by0 = is_ordered_by0
        
        pass
    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def OrderTotal(self):
        return self.__OrderTotal
    @OrderTotal.setter
    def OrderTotal(self, OrderTotal: str):
        self.__OrderTotal = OrderTotal

    @property
    def processQuery11(self):
        return self.__processQuery11
    @processQuery11.setter
    def processQuery11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderController__processQuery11", None)
        self.__processQuery11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order10"):
                opp_val = getattr(old_value, "order10", None)
                if opp_val == self:
                    setattr(old_value, "order10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order10"):
                opp_val = getattr(value, "order10", None)
                setattr(value, "order10", self)

    @property
    def membership_Card4(self):
        return self.__membership_Card4
    @membership_Card4.setter
    def membership_Card4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderController__membership_Card4", None)
        self.__membership_Card4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order5"):
                opp_val = getattr(old_value, "order5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order5"):
                opp_val = getattr(value, "order5", None)
                if opp_val is None:
                    setattr(value, "order5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def is_ordered_by0(self):
        return self.__is_ordered_by0
    @is_ordered_by0.setter
    def is_ordered_by0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderController__is_ordered_by0", None)
        self.__is_ordered_by0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has1"):
                opp_val = getattr(old_value, "has1", None)
                if opp_val == self:
                    setattr(old_value, "has1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has1"):
                opp_val = getattr(value, "has1", None)
                setattr(value, "has1", self)



class Table:

    def __init__(self, TableNo: str, Occupied: bool, processQuery15: "processQuery" = None, has1: "OrderController" = None, reserved2: "BookingController" = None):
        self.TableNo = TableNo
        self.Occupied = Occupied
        self.processQuery15 = processQuery15
        self.has1 = has1
        self.reserved2 = reserved2
        
        pass
    @property
    def TableNo(self):
        return self.__TableNo
    @TableNo.setter
    def TableNo(self, TableNo: str):
        self.__TableNo = TableNo

    @property
    def Occupied(self):
        return self.__Occupied
    @Occupied.setter
    def Occupied(self, Occupied: bool):
        self.__Occupied = Occupied

    @property
    def reserved2(self):
        return self.__reserved2
    @reserved2.setter
    def reserved2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__reserved2", None)
        self.__reserved2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "is_reserved_by3"):
                opp_val = getattr(old_value, "is_reserved_by3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "is_reserved_by3"):
                opp_val = getattr(value, "is_reserved_by3", None)
                if opp_val is None:
                    setattr(value, "is_reserved_by3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def has1(self):
        return self.__has1
    @has1.setter
    def has1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__has1", None)
        self.__has1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "is_ordered_by0"):
                opp_val = getattr(old_value, "is_ordered_by0", None)
                if opp_val == self:
                    setattr(old_value, "is_ordered_by0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "is_ordered_by0"):
                opp_val = getattr(value, "is_ordered_by0", None)
                setattr(value, "is_ordered_by0", self)

    @property
    def processQuery15(self):
        return self.__processQuery15
    @processQuery15.setter
    def processQuery15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__processQuery15", None)
        self.__processQuery15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table14"):
                opp_val = getattr(old_value, "table14", None)
                if opp_val == self:
                    setattr(old_value, "table14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table14"):
                opp_val = getattr(value, "table14", None)
                setattr(value, "table14", self)



class BookingController:

    def __init__(self, BookingID: int, CustomerName: str, Phone: str, TableNo: str, Date: str, Time: str, processQuery9: "processQuery" = None, is_reserved_by3: set["Table"] = None):
        self.BookingID = BookingID
        self.CustomerName = CustomerName
        self.Phone = Phone
        self.TableNo = TableNo
        self.Date = Date
        self.Time = Time
        self.processQuery9 = processQuery9
        self.is_reserved_by3 = is_reserved_by3 if is_reserved_by3 is not None else set()
        
        pass
    @property
    def BookingID(self):
        return self.__BookingID
    @BookingID.setter
    def BookingID(self, BookingID: int):
        self.__BookingID = BookingID

    @property
    def TableNo(self):
        return self.__TableNo
    @TableNo.setter
    def TableNo(self, TableNo: str):
        self.__TableNo = TableNo

    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: str):
        self.__Time = Time

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def is_reserved_by3(self):
        return self.__is_reserved_by3
    @is_reserved_by3.setter
    def is_reserved_by3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookingController__is_reserved_by3", None)
        self.__is_reserved_by3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reserved2"):
                    opp_val = getattr(item, "reserved2", None)
                    
                    if opp_val == self:
                        setattr(item, "reserved2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reserved2"):
                    opp_val = getattr(item, "reserved2", None)
                    
                    setattr(item, "reserved2", self)
                    

    @property
    def processQuery9(self):
        return self.__processQuery9
    @processQuery9.setter
    def processQuery9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookingController__processQuery9", None)
        self.__processQuery9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking8"):
                opp_val = getattr(old_value, "booking8", None)
                if opp_val == self:
                    setattr(old_value, "booking8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking8"):
                opp_val = getattr(value, "booking8", None)
                setattr(value, "booking8", self)

