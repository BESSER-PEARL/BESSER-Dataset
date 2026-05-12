from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class BookedTables:

    def __init__(self, TableNo: int, BookingID: int, bookings4: "Bookings" = None, table16: "Table" = None):
        self.TableNo = TableNo
        self.BookingID = BookingID
        self.bookings4 = bookings4
        self.table16 = table16
        
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
    def TableNo(self, TableNo: int):
        self.__TableNo = TableNo

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

    @property
    def table16(self):
        return self.__table16
    @table16.setter
    def table16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookedTables__table16", None)
        self.__table16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookedTables17"):
                opp_val = getattr(old_value, "bookedTables17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookedTables17"):
                opp_val = getattr(value, "bookedTables17", None)
                if opp_val is None:
                    setattr(value, "bookedTables17", set([self]))
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
    def People(self):
        return self.__People
    @People.setter
    def People(self, People: int):
        self.__People = People

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
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: date):
        self.__Time = Time

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
                    



class AdminPanel:

    def __init__(self, UserID: int, UserName: str, UserLevel: int, menu8: "Menu" = None):
        self.UserID = UserID
        self.UserName = UserName
        self.UserLevel = UserLevel
        self.menu8 = menu8
        
        pass
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
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def menu8(self):
        return self.__menu8
    @menu8.setter
    def menu8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AdminPanel__menu8", None)
        self.__menu8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adminPanel9"):
                opp_val = getattr(old_value, "adminPanel9", None)
                if opp_val == self:
                    setattr(old_value, "adminPanel9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adminPanel9"):
                opp_val = getattr(value, "adminPanel9", None)
                setattr(value, "adminPanel9", self)



class Menu:

    def __init__(self, MenuItem: str, Category: str, Price: float, Availability: int, order7: "Order" = None, adminPanel9: "AdminPanel" = None):
        self.MenuItem = MenuItem
        self.Category = Category
        self.Price = Price
        self.Availability = Availability
        self.order7 = order7
        self.adminPanel9 = adminPanel9
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: float):
        self.__Price = Price

    @property
    def Availability(self):
        return self.__Availability
    @Availability.setter
    def Availability(self, Availability: int):
        self.__Availability = Availability

    @property
    def MenuItem(self):
        return self.__MenuItem
    @MenuItem.setter
    def MenuItem(self, MenuItem: str):
        self.__MenuItem = MenuItem

    @property
    def Category(self):
        return self.__Category
    @Category.setter
    def Category(self, Category: str):
        self.__Category = Category

    @property
    def order7(self):
        return self.__order7
    @order7.setter
    def order7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__order7", None)
        self.__order7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu6"):
                opp_val = getattr(old_value, "menu6", None)
                if opp_val == self:
                    setattr(old_value, "menu6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu6"):
                opp_val = getattr(value, "menu6", None)
                setattr(value, "menu6", self)

    @property
    def adminPanel9(self):
        return self.__adminPanel9
    @adminPanel9.setter
    def adminPanel9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__adminPanel9", None)
        self.__adminPanel9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu8"):
                opp_val = getattr(old_value, "menu8", None)
                if opp_val == self:
                    setattr(old_value, "menu8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu8"):
                opp_val = getattr(value, "menu8", None)
                setattr(value, "menu8", self)



class OrderItem:

    def __init__(self, ItemName: str, RemaningTime: date, Completed: int, viewOrder11: "ViewOrder" = None, order12: "Order" = None):
        self.ItemName = ItemName
        self.RemaningTime = RemaningTime
        self.Completed = Completed
        self.viewOrder11 = viewOrder11
        self.order12 = order12
        
        pass
    @property
    def ItemName(self):
        return self.__ItemName
    @ItemName.setter
    def ItemName(self, ItemName: str):
        self.__ItemName = ItemName

    @property
    def Completed(self):
        return self.__Completed
    @Completed.setter
    def Completed(self, Completed: int):
        self.__Completed = Completed

    @property
    def RemaningTime(self):
        return self.__RemaningTime
    @RemaningTime.setter
    def RemaningTime(self, RemaningTime: date):
        self.__RemaningTime = RemaningTime

    @property
    def order12(self):
        return self.__order12
    @order12.setter
    def order12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderItem__order12", None)
        self.__order12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderItem13"):
                opp_val = getattr(old_value, "orderItem13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderItem13"):
                opp_val = getattr(value, "orderItem13", None)
                if opp_val is None:
                    setattr(value, "orderItem13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewOrder11(self):
        return self.__viewOrder11
    @viewOrder11.setter
    def viewOrder11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderItem__viewOrder11", None)
        self.__viewOrder11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderItem10"):
                opp_val = getattr(old_value, "orderItem10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderItem10"):
                opp_val = getattr(value, "orderItem10", None)
                if opp_val is None:
                    setattr(value, "orderItem10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ViewOrder:

    def __init__(self, getUser: int, orderItem10: set["OrderItem"] = None):
        self.getUser = getUser
        self.orderItem10 = orderItem10 if orderItem10 is not None else set()
        
        pass
    @property
    def getUser(self):
        return self.__getUser
    @getUser.setter
    def getUser(self, getUser: int):
        self.__getUser = getUser

    @property
    def orderItem10(self):
        return self.__orderItem10
    @orderItem10.setter
    def orderItem10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ViewOrder__orderItem10", None)
        self.__orderItem10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewOrder11"):
                    opp_val = getattr(item, "viewOrder11", None)
                    
                    if opp_val == self:
                        setattr(item, "viewOrder11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewOrder11"):
                    opp_val = getattr(item, "viewOrder11", None)
                    
                    setattr(item, "viewOrder11", self)
                    



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

    def __init__(self, OrderID: int, Date: date, UserID: int, Total: float, DicountLvl: int, membership_Card1: "Membership_Card" = None, table2: "Table" = None, menu6: "Menu" = None, orderItem13: set["OrderItem"] = None, users14: "Users" = None):
        self.OrderID = OrderID
        self.Date = Date
        self.UserID = UserID
        self.Total = Total
        self.DicountLvl = DicountLvl
        self.membership_Card1 = membership_Card1
        self.table2 = table2
        self.menu6 = menu6
        self.orderItem13 = orderItem13 if orderItem13 is not None else set()
        self.users14 = users14
        
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
    def Total(self):
        return self.__Total
    @Total.setter
    def Total(self, Total: float):
        self.__Total = Total

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def DicountLvl(self):
        return self.__DicountLvl
    @DicountLvl.setter
    def DicountLvl(self, DicountLvl: int):
        self.__DicountLvl = DicountLvl

    @property
    def orderItem13(self):
        return self.__orderItem13
    @orderItem13.setter
    def orderItem13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderItem13", None)
        self.__orderItem13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order12"):
                    opp_val = getattr(item, "order12", None)
                    
                    if opp_val == self:
                        setattr(item, "order12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order12"):
                    opp_val = getattr(item, "order12", None)
                    
                    setattr(item, "order12", self)
                    

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
    def menu6(self):
        return self.__menu6
    @menu6.setter
    def menu6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__menu6", None)
        self.__menu6 = value
        
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
    def users14(self):
        return self.__users14
    @users14.setter
    def users14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__users14", None)
        self.__users14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order15"):
                opp_val = getattr(old_value, "order15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order15"):
                opp_val = getattr(value, "order15", None)
                if opp_val is None:
                    setattr(value, "order15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Table:

    def __init__(self, TableNo: int, Occupied: int, order3: set["Order"] = None, bookedTables17: set["BookedTables"] = None):
        self.TableNo = TableNo
        self.Occupied = Occupied
        self.order3 = order3 if order3 is not None else set()
        self.bookedTables17 = bookedTables17 if bookedTables17 is not None else set()
        
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
    def bookedTables17(self):
        return self.__bookedTables17
    @bookedTables17.setter
    def bookedTables17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__bookedTables17", None)
        self.__bookedTables17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "table16"):
                    opp_val = getattr(item, "table16", None)
                    
                    if opp_val == self:
                        setattr(item, "table16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "table16"):
                    opp_val = getattr(item, "table16", None)
                    
                    setattr(item, "table16", self)
                    



class Users:

    def __init__(self, UserID: int, UserName: str, UserLevel: int, order15: set["Order"] = None):
        self.UserID = UserID
        self.UserName = UserName
        self.UserLevel = UserLevel
        self.order15 = order15 if order15 is not None else set()
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

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
    def order15(self):
        return self.__order15
    @order15.setter
    def order15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users__order15", None)
        self.__order15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "users14"):
                    opp_val = getattr(item, "users14", None)
                    
                    if opp_val == self:
                        setattr(item, "users14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "users14"):
                    opp_val = getattr(item, "users14", None)
                    
                    setattr(item, "users14", self)
                    

