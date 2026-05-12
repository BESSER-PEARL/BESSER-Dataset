from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class BookedTables:

    def __init__(self, TableNo: int, BookingID: int, bookings4: "Bookings" = None, table14: "Table" = None):
        self.TableNo = TableNo
        self.BookingID = BookingID
        self.bookings4 = bookings4
        self.table14 = table14
        
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
    def table14(self):
        return self.__table14
    @table14.setter
    def table14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookedTables__table14", None)
        self.__table14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookedTables15"):
                opp_val = getattr(old_value, "bookedTables15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookedTables15"):
                opp_val = getattr(value, "bookedTables15", None)
                if opp_val is None:
                    setattr(value, "bookedTables15", set([self]))
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

    def __init__(self, BookingID: int, CustomerName: str, Phone: str, People: int, Date: date, Time: date, table5: set["BookedTables"] = None):
        self.BookingID = BookingID
        self.CustomerName = CustomerName
        self.Phone = Phone
        self.People = People
        self.Date = Date
        self.Time = Time
        self.table5 = table5 if table5 is not None else set()
        
        pass
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
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def BookingID(self):
        return self.__BookingID
    @BookingID.setter
    def BookingID(self, BookingID: int):
        self.__BookingID = BookingID

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
                    



class Menu:

    def __init__(self, MenuItem: str, Category: str, Price: float, Availability: int, orderItem7: set["OrderItem"] = None):
        self.MenuItem = MenuItem
        self.Category = Category
        self.Price = Price
        self.Availability = Availability
        self.orderItem7 = orderItem7 if orderItem7 is not None else set()
        
        pass
    @property
    def MenuItem(self):
        return self.__MenuItem
    @MenuItem.setter
    def MenuItem(self, MenuItem: str):
        self.__MenuItem = MenuItem

    @property
    def Availability(self):
        return self.__Availability
    @Availability.setter
    def Availability(self, Availability: int):
        self.__Availability = Availability

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: float):
        self.__Price = Price

    @property
    def Category(self):
        return self.__Category
    @Category.setter
    def Category(self, Category: str):
        self.__Category = Category

    @property
    def orderItem7(self):
        return self.__orderItem7
    @orderItem7.setter
    def orderItem7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__orderItem7", None)
        self.__orderItem7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "menu6"):
                    opp_val = getattr(item, "menu6", None)
                    
                    if opp_val == self:
                        setattr(item, "menu6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "menu6"):
                    opp_val = getattr(item, "menu6", None)
                    
                    setattr(item, "menu6", self)
                    



class OrderItem:

    def __init__(self, OrderItemID: int, OrderID: int, ItemName: str, RemaningTime: date, Completed: int, menu6: "Menu" = None, viewOrder9: "ViewOrder" = None, order10: "Order" = None):
        self.OrderItemID = OrderItemID
        self.OrderID = OrderID
        self.ItemName = ItemName
        self.RemaningTime = RemaningTime
        self.Completed = Completed
        self.menu6 = menu6
        self.viewOrder9 = viewOrder9
        self.order10 = order10
        
        pass
    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def Completed(self):
        return self.__Completed
    @Completed.setter
    def Completed(self, Completed: int):
        self.__Completed = Completed

    @property
    def OrderItemID(self):
        return self.__OrderItemID
    @OrderItemID.setter
    def OrderItemID(self, OrderItemID: int):
        self.__OrderItemID = OrderItemID

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
    def viewOrder9(self):
        return self.__viewOrder9
    @viewOrder9.setter
    def viewOrder9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderItem__viewOrder9", None)
        self.__viewOrder9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderItem8"):
                opp_val = getattr(old_value, "orderItem8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderItem8"):
                opp_val = getattr(value, "orderItem8", None)
                if opp_val is None:
                    setattr(value, "orderItem8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def menu6(self):
        return self.__menu6
    @menu6.setter
    def menu6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderItem__menu6", None)
        self.__menu6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderItem7"):
                opp_val = getattr(old_value, "orderItem7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderItem7"):
                opp_val = getattr(value, "orderItem7", None)
                if opp_val is None:
                    setattr(value, "orderItem7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order10(self):
        return self.__order10
    @order10.setter
    def order10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderItem__order10", None)
        self.__order10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderItem11"):
                opp_val = getattr(old_value, "orderItem11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderItem11"):
                opp_val = getattr(value, "orderItem11", None)
                if opp_val is None:
                    setattr(value, "orderItem11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ViewOrder:

    def __init__(self, getUser: int, orderItem8: set["OrderItem"] = None):
        self.getUser = getUser
        self.orderItem8 = orderItem8 if orderItem8 is not None else set()
        
        pass
    @property
    def getUser(self):
        return self.__getUser
    @getUser.setter
    def getUser(self, getUser: int):
        self.__getUser = getUser

    @property
    def orderItem8(self):
        return self.__orderItem8
    @orderItem8.setter
    def orderItem8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ViewOrder__orderItem8", None)
        self.__orderItem8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewOrder9"):
                    opp_val = getattr(item, "viewOrder9", None)
                    
                    if opp_val == self:
                        setattr(item, "viewOrder9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewOrder9"):
                    opp_val = getattr(item, "viewOrder9", None)
                    
                    setattr(item, "viewOrder9", self)
                    



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

    def __init__(self, OrderID: int, Date: date, UserID: int, Total: float, DicountLvl: int, orderItem11: set["OrderItem"] = None, users12: "Users" = None, membership_Card1: "Membership_Card" = None, table2: "Table" = None):
        self.OrderID = OrderID
        self.Date = Date
        self.UserID = UserID
        self.Total = Total
        self.DicountLvl = DicountLvl
        self.orderItem11 = orderItem11 if orderItem11 is not None else set()
        self.users12 = users12
        self.membership_Card1 = membership_Card1
        self.table2 = table2
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

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
    def orderItem11(self):
        return self.__orderItem11
    @orderItem11.setter
    def orderItem11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__orderItem11", None)
        self.__orderItem11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order10"):
                    opp_val = getattr(item, "order10", None)
                    
                    if opp_val == self:
                        setattr(item, "order10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order10"):
                    opp_val = getattr(item, "order10", None)
                    
                    setattr(item, "order10", self)
                    

    @property
    def users12(self):
        return self.__users12
    @users12.setter
    def users12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__users12", None)
        self.__users12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order13"):
                opp_val = getattr(old_value, "order13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order13"):
                opp_val = getattr(value, "order13", None)
                if opp_val is None:
                    setattr(value, "order13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Table:

    def __init__(self, TableNo: int, Occupied: int, order3: set["Order"] = None, bookedTables15: set["BookedTables"] = None):
        self.TableNo = TableNo
        self.Occupied = Occupied
        self.order3 = order3 if order3 is not None else set()
        self.bookedTables15 = bookedTables15 if bookedTables15 is not None else set()
        
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
    def bookedTables15(self):
        return self.__bookedTables15
    @bookedTables15.setter
    def bookedTables15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__bookedTables15", None)
        self.__bookedTables15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "table14"):
                    opp_val = getattr(item, "table14", None)
                    
                    if opp_val == self:
                        setattr(item, "table14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "table14"):
                    opp_val = getattr(item, "table14", None)
                    
                    setattr(item, "table14", self)
                    

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
                    



class Users:

    def __init__(self, UserID: int, UserName: str, UserLevel: int, order13: set["Order"] = None):
        self.UserID = UserID
        self.UserName = UserName
        self.UserLevel = UserLevel
        self.order13 = order13 if order13 is not None else set()
        
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
    def order13(self):
        return self.__order13
    @order13.setter
    def order13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users__order13", None)
        self.__order13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "users12"):
                    opp_val = getattr(item, "users12", None)
                    
                    if opp_val == self:
                        setattr(item, "users12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "users12"):
                    opp_val = getattr(item, "users12", None)
                    
                    setattr(item, "users12", self)
                    

