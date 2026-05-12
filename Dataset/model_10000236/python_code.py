from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class BookedTables:

    def __init__(self, TableNo: int, BookingID: int, bookings4: "Bookings" = None, table12: "Table" = None):
        self.TableNo = TableNo
        self.BookingID = BookingID
        self.bookings4 = bookings4
        self.table12 = table12
        
        pass
    @property
    def TableNo(self):
        return self.__TableNo
    @TableNo.setter
    def TableNo(self, TableNo: int):
        self.__TableNo = TableNo

    @property
    def BookingID(self):
        return self.__BookingID
    @BookingID.setter
    def BookingID(self, BookingID: int):
        self.__BookingID = BookingID

    @property
    def table12(self):
        return self.__table12
    @table12.setter
    def table12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookedTables__table12", None)
        self.__table12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookedTables13"):
                opp_val = getattr(old_value, "bookedTables13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookedTables13"):
                opp_val = getattr(value, "bookedTables13", None)
                if opp_val is None:
                    setattr(value, "bookedTables13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bookings4(self):
        return self.__bookings4
    @bookings4.setter
    def bookings4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookedTables__bookings4", None)
        self.__bookings4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table5"):
                opp_val = getattr(old_value, "table5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table5"):
                opp_val = getattr(value, "table5", None)
                if opp_val is None:
                    setattr(value, "table5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Bookings:

    def __init__(self, BookingID: int, CustomerName: str, Phone: str, People: int, TableNo: int, Date: date, Time: date, table5: set["BookedTables"] = None):
        self.BookingID = BookingID
        self.CustomerName = CustomerName
        self.Phone = Phone
        self.People = People
        self.TableNo = TableNo
        self.Date = Date
        self.Time = Time
        self.table5 = table5 if table5 is not None else set()
        
        pass
    @property
    def TableNo(self):
        return self.__TableNo
    @TableNo.setter
    def TableNo(self, TableNo: int):
        self.__TableNo = TableNo

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: date):
        self.__Time = Time

    @property
    def People(self):
        return self.__People
    @People.setter
    def People(self, People: int):
        self.__People = People

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def BookingID(self):
        return self.__BookingID
    @BookingID.setter
    def BookingID(self, BookingID: int):
        self.__BookingID = BookingID

    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def table5(self):
        return self.__table5
    @table5.setter
    def table5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bookings__table5", None)
        self.__table5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookings4"):
                    opp_val = getattr(item, "bookings4", None)
                    
                    if opp_val == self:
                        setattr(item, "bookings4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookings4"):
                    opp_val = getattr(item, "bookings4", None)
                    
                    setattr(item, "bookings4", self)
                    



class OrderItem:

    def __init__(self, ItemName: str, RemaningTime: date, Completed: int, viewOrder7: "ViewOrder" = None, order8: "Order" = None):
        self.ItemName = ItemName
        self.RemaningTime = RemaningTime
        self.Completed = Completed
        self.viewOrder7 = viewOrder7
        self.order8 = order8
        
        pass
    @property
    def Completed(self):
        return self.__Completed
    @Completed.setter
    def Completed(self, Completed: int):
        self.__Completed = Completed

    @property
    def ItemName(self):
        return self.__ItemName
    @ItemName.setter
    def ItemName(self, ItemName: str):
        self.__ItemName = ItemName

    @property
    def RemaningTime(self):
        return self.__RemaningTime
    @RemaningTime.setter
    def RemaningTime(self, RemaningTime: date):
        self.__RemaningTime = RemaningTime

    @property
    def viewOrder7(self):
        return self.__viewOrder7
    @viewOrder7.setter
    def viewOrder7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderItem__viewOrder7", None)
        self.__viewOrder7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderItem6"):
                opp_val = getattr(old_value, "orderItem6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderItem6"):
                opp_val = getattr(value, "orderItem6", None)
                if opp_val is None:
                    setattr(value, "orderItem6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order8(self):
        return self.__order8
    @order8.setter
    def order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderItem__order8", None)
        self.__order8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderItem9"):
                opp_val = getattr(old_value, "orderItem9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderItem9"):
                opp_val = getattr(value, "orderItem9", None)
                if opp_val is None:
                    setattr(value, "orderItem9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ViewOrder:

    def __init__(self, getUser: int, orderItem6: set["OrderItem"] = None):
        self.getUser = getUser
        self.orderItem6 = orderItem6 if orderItem6 is not None else set()
        
        pass
    @property
    def getUser(self):
        return self.__getUser
    @getUser.setter
    def getUser(self, getUser: int):
        self.__getUser = getUser

    @property
    def orderItem6(self):
        return self.__orderItem6
    @orderItem6.setter
    def orderItem6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ViewOrder__orderItem6", None)
        self.__orderItem6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewOrder7"):
                    opp_val = getattr(item, "viewOrder7", None)
                    
                    if opp_val == self:
                        setattr(item, "viewOrder7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewOrder7"):
                    opp_val = getattr(item, "viewOrder7", None)
                    
                    setattr(item, "viewOrder7", self)
                    



class Membership_Card:

    def __init__(self, ID: int, DiscountLVL: int, order0: set["Order"] = None):
        self.ID = ID
        self.DiscountLVL = DiscountLVL
        self.order0 = order0 if order0 is not None else set()
        
        pass
    @property
    def DiscountLVL(self):
        return self.__DiscountLVL
    @DiscountLVL.setter
    def DiscountLVL(self, DiscountLVL: int):
        self.__DiscountLVL = DiscountLVL

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def order0(self):
        return self.__order0
    @order0.setter
    def order0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Membership_Card__order0", None)
        self.__order0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "membership_Card1"):
                    opp_val = getattr(item, "membership_Card1", None)
                    
                    if opp_val == self:
                        setattr(item, "membership_Card1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "membership_Card1"):
                    opp_val = getattr(item, "membership_Card1", None)
                    
                    setattr(item, "membership_Card1", self)
                    



class Order:

    def __init__(self, OrderID: int, Date: date, UserID: int, Total: float, DicountLvl: int, membership_Card1: "Membership_Card" = None, table2: "Table" = None, orderItem9: set["OrderItem"] = None, users10: "Users" = None):
        self.OrderID = OrderID
        self.Date = Date
        self.UserID = UserID
        self.Total = Total
        self.DicountLvl = DicountLvl
        self.membership_Card1 = membership_Card1
        self.table2 = table2
        self.orderItem9 = orderItem9 if orderItem9 is not None else set()
        self.users10 = users10
        
        pass
    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def DicountLvl(self):
        return self.__DicountLvl
    @DicountLvl.setter
    def DicountLvl(self, DicountLvl: int):
        self.__DicountLvl = DicountLvl

    @property
    def Total(self):
        return self.__Total
    @Total.setter
    def Total(self, Total: float):
        self.__Total = Total

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
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def membership_Card1(self):
        return self.__membership_Card1
    @membership_Card1.setter
    def membership_Card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__membership_Card1", None)
        self.__membership_Card1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order0"):
                opp_val = getattr(old_value, "order0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order0"):
                opp_val = getattr(value, "order0", None)
                if opp_val is None:
                    setattr(value, "order0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def users10(self):
        return self.__users10
    @users10.setter
    def users10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__users10", None)
        self.__users10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order11"):
                opp_val = getattr(old_value, "order11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order11"):
                opp_val = getattr(value, "order11", None)
                if opp_val is None:
                    setattr(value, "order11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def table2(self):
        return self.__table2
    @table2.setter
    def table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__table2", None)
        self.__table2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order3"):
                opp_val = getattr(old_value, "order3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order3"):
                opp_val = getattr(value, "order3", None)
                if opp_val is None:
                    setattr(value, "order3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def orderItem9(self):
        return self.__orderItem9
    @orderItem9.setter
    def orderItem9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderItem9", None)
        self.__orderItem9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order8"):
                    opp_val = getattr(item, "order8", None)
                    
                    if opp_val == self:
                        setattr(item, "order8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order8"):
                    opp_val = getattr(item, "order8", None)
                    
                    setattr(item, "order8", self)
                    



class Table:

    def __init__(self, TableNo: int, Occupied: int, order3: set["Order"] = None, bookedTables13: set["BookedTables"] = None):
        self.TableNo = TableNo
        self.Occupied = Occupied
        self.order3 = order3 if order3 is not None else set()
        self.bookedTables13 = bookedTables13 if bookedTables13 is not None else set()
        
        pass
    @property
    def TableNo(self):
        return self.__TableNo
    @TableNo.setter
    def TableNo(self, TableNo: int):
        self.__TableNo = TableNo

    @property
    def Occupied(self):
        return self.__Occupied
    @Occupied.setter
    def Occupied(self, Occupied: int):
        self.__Occupied = Occupied

    @property
    def order3(self):
        return self.__order3
    @order3.setter
    def order3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__order3", None)
        self.__order3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "table2"):
                    opp_val = getattr(item, "table2", None)
                    
                    if opp_val == self:
                        setattr(item, "table2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "table2"):
                    opp_val = getattr(item, "table2", None)
                    
                    setattr(item, "table2", self)
                    

    @property
    def bookedTables13(self):
        return self.__bookedTables13
    @bookedTables13.setter
    def bookedTables13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__bookedTables13", None)
        self.__bookedTables13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "table12"):
                    opp_val = getattr(item, "table12", None)
                    
                    if opp_val == self:
                        setattr(item, "table12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "table12"):
                    opp_val = getattr(item, "table12", None)
                    
                    setattr(item, "table12", self)
                    



class Users:

    def __init__(self, UserID: int, UserName: str, UserLevel: int, order11: set["Order"] = None):
        self.UserID = UserID
        self.UserName = UserName
        self.UserLevel = UserLevel
        self.order11 = order11 if order11 is not None else set()
        
        pass
    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def UserLevel(self):
        return self.__UserLevel
    @UserLevel.setter
    def UserLevel(self, UserLevel: int):
        self.__UserLevel = UserLevel

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def order11(self):
        return self.__order11
    @order11.setter
    def order11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users__order11", None)
        self.__order11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "users10"):
                    opp_val = getattr(item, "users10", None)
                    
                    if opp_val == self:
                        setattr(item, "users10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "users10"):
                    opp_val = getattr(item, "users10", None)
                    
                    setattr(item, "users10", self)
                    

