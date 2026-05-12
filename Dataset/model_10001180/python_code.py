from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Membership:

    def __init__(self, loyaltyID: int, discount: float, checkout16: "Checkout" = None):
        self.loyaltyID = loyaltyID
        self.discount = discount
        self.checkout16 = checkout16
        
        pass
    @property
    def loyaltyID(self):
        return self.__loyaltyID
    @loyaltyID.setter
    def loyaltyID(self, loyaltyID: int):
        self.__loyaltyID = loyaltyID

    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, discount: float):
        self.__discount = discount

    @property
    def checkout16(self):
        return self.__checkout16
    @checkout16.setter
    def checkout16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Membership__checkout16", None)
        self.__checkout16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "membership17"):
                opp_val = getattr(old_value, "membership17", None)
                if opp_val == self:
                    setattr(old_value, "membership17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "membership17"):
                opp_val = getattr(value, "membership17", None)
                setattr(value, "membership17", self)



class Checkout:

    def __init__(self, checkoutID: int, checkoutAmount: float, order15: "Order" = None, membership17: "Membership" = None):
        self.checkoutID = checkoutID
        self.checkoutAmount = checkoutAmount
        self.order15 = order15
        self.membership17 = membership17
        
        pass
    @property
    def checkoutID(self):
        return self.__checkoutID
    @checkoutID.setter
    def checkoutID(self, checkoutID: int):
        self.__checkoutID = checkoutID

    @property
    def checkoutAmount(self):
        return self.__checkoutAmount
    @checkoutAmount.setter
    def checkoutAmount(self, checkoutAmount: float):
        self.__checkoutAmount = checkoutAmount

    @property
    def order15(self):
        return self.__order15
    @order15.setter
    def order15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Checkout__order15", None)
        self.__order15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkout14"):
                opp_val = getattr(old_value, "checkout14", None)
                if opp_val == self:
                    setattr(old_value, "checkout14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkout14"):
                opp_val = getattr(value, "checkout14", None)
                setattr(value, "checkout14", self)

    @property
    def membership17(self):
        return self.__membership17
    @membership17.setter
    def membership17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Checkout__membership17", None)
        self.__membership17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkout16"):
                opp_val = getattr(old_value, "checkout16", None)
                if opp_val == self:
                    setattr(old_value, "checkout16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkout16"):
                opp_val = getattr(value, "checkout16", None)
                setattr(value, "checkout16", self)



class BookedTables:

    def __init__(self, TableNo: int, BookingID: int, table12: "Table" = None, bookings2: "Bookings" = None):
        self.TableNo = TableNo
        self.BookingID = BookingID
        self.table12 = table12
        self.bookings2 = bookings2
        
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
    def bookings2(self):
        return self.__bookings2
    @bookings2.setter
    def bookings2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BookedTables__bookings2", None)
        self.__bookings2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table3"):
                opp_val = getattr(old_value, "table3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table3"):
                opp_val = getattr(value, "table3", None)
                if opp_val is None:
                    setattr(value, "table3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Bookings:

    def __init__(self, BookingID: int, CustomerName: str, Phone: str, People: int, Date: date, Time: date, table3: set["BookedTables"] = None):
        self.BookingID = BookingID
        self.CustomerName = CustomerName
        self.Phone = Phone
        self.People = People
        self.Date = Date
        self.Time = Time
        self.table3 = table3 if table3 is not None else set()
        
        pass
    @property
    def BookingID(self):
        return self.__BookingID
    @BookingID.setter
    def BookingID(self, BookingID: int):
        self.__BookingID = BookingID

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: date):
        self.__Time = Time

    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def People(self):
        return self.__People
    @People.setter
    def People(self, People: int):
        self.__People = People

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
    def table3(self):
        return self.__table3
    @table3.setter
    def table3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bookings__table3", None)
        self.__table3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookings2"):
                    opp_val = getattr(item, "bookings2", None)
                    
                    if opp_val == self:
                        setattr(item, "bookings2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookings2"):
                    opp_val = getattr(item, "bookings2", None)
                    
                    setattr(item, "bookings2", self)
                    



class Menu:

    def __init__(self, MenuItem: str, Category: str, Price: float, Availability: int, orderItem5: set["OrderList"] = None):
        self.MenuItem = MenuItem
        self.Category = Category
        self.Price = Price
        self.Availability = Availability
        self.orderItem5 = orderItem5 if orderItem5 is not None else set()
        
        pass
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
    def orderItem5(self):
        return self.__orderItem5
    @orderItem5.setter
    def orderItem5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu__orderItem5", None)
        self.__orderItem5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "menu4"):
                    opp_val = getattr(item, "menu4", None)
                    
                    if opp_val == self:
                        setattr(item, "menu4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "menu4"):
                    opp_val = getattr(item, "menu4", None)
                    
                    setattr(item, "menu4", self)
                    



class OrderList:

    def __init__(self, OrderItemID: int, OrderID: int, ItemName: str, RemaningTime: date, menu4: "Menu" = None, viewOrder7: "ViewOrder" = None, order8: "Order" = None):
        self.OrderItemID = OrderItemID
        self.OrderID = OrderID
        self.ItemName = ItemName
        self.RemaningTime = RemaningTime
        self.menu4 = menu4
        self.viewOrder7 = viewOrder7
        self.order8 = order8
        
        pass
    @property
    def OrderItemID(self):
        return self.__OrderItemID
    @OrderItemID.setter
    def OrderItemID(self, OrderItemID: int):
        self.__OrderItemID = OrderItemID

    @property
    def RemaningTime(self):
        return self.__RemaningTime
    @RemaningTime.setter
    def RemaningTime(self, RemaningTime: date):
        self.__RemaningTime = RemaningTime

    @property
    def ItemName(self):
        return self.__ItemName
    @ItemName.setter
    def ItemName(self, ItemName: str):
        self.__ItemName = ItemName

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def menu4(self):
        return self.__menu4
    @menu4.setter
    def menu4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderList__menu4", None)
        self.__menu4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderItem5"):
                opp_val = getattr(old_value, "orderItem5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderItem5"):
                opp_val = getattr(value, "orderItem5", None)
                if opp_val is None:
                    setattr(value, "orderItem5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order8(self):
        return self.__order8
    @order8.setter
    def order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderList__order8", None)
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

    @property
    def viewOrder7(self):
        return self.__viewOrder7
    @viewOrder7.setter
    def viewOrder7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderList__viewOrder7", None)
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



class ViewOrder:

    def __init__(self, getOrderList: int, orderItem6: set["OrderList"] = None):
        self.getOrderList = getOrderList
        self.orderItem6 = orderItem6 if orderItem6 is not None else set()
        
        pass
    @property
    def getOrderList(self):
        return self.__getOrderList
    @getOrderList.setter
    def getOrderList(self, getOrderList: int):
        self.__getOrderList = getOrderList

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
                    



class Order:

    def __init__(self, OrderID: int, UserID: int, Date: str, Completed: int, table0: "Table" = None, orderItem9: set["OrderList"] = None, users10: "Users" = None, checkout14: "Checkout" = None):
        self.OrderID = OrderID
        self.UserID = UserID
        self.Date = Date
        self.Completed = Completed
        self.table0 = table0
        self.orderItem9 = orderItem9 if orderItem9 is not None else set()
        self.users10 = users10
        self.checkout14 = checkout14
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def Completed(self):
        return self.__Completed
    @Completed.setter
    def Completed(self, Completed: int):
        self.__Completed = Completed

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def table0(self):
        return self.__table0
    @table0.setter
    def table0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__table0", None)
        self.__table0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order1"):
                opp_val = getattr(old_value, "order1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order1"):
                opp_val = getattr(value, "order1", None)
                if opp_val is None:
                    setattr(value, "order1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def checkout14(self):
        return self.__checkout14
    @checkout14.setter
    def checkout14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__checkout14", None)
        self.__checkout14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order15"):
                opp_val = getattr(old_value, "order15", None)
                if opp_val == self:
                    setattr(old_value, "order15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order15"):
                opp_val = getattr(value, "order15", None)
                setattr(value, "order15", self)

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

    def __init__(self, TableNo: int, Occupied: int, order1: set["Order"] = None, bookedTables13: set["BookedTables"] = None):
        self.TableNo = TableNo
        self.Occupied = Occupied
        self.order1 = order1 if order1 is not None else set()
        self.bookedTables13 = bookedTables13 if bookedTables13 is not None else set()
        
        pass
    @property
    def Occupied(self):
        return self.__Occupied
    @Occupied.setter
    def Occupied(self, Occupied: int):
        self.__Occupied = Occupied

    @property
    def TableNo(self):
        return self.__TableNo
    @TableNo.setter
    def TableNo(self, TableNo: int):
        self.__TableNo = TableNo

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
                    

    @property
    def order1(self):
        return self.__order1
    @order1.setter
    def order1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__order1", None)
        self.__order1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "table0"):
                    opp_val = getattr(item, "table0", None)
                    
                    if opp_val == self:
                        setattr(item, "table0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "table0"):
                    opp_val = getattr(item, "table0", None)
                    
                    setattr(item, "table0", self)
                    



class Users:

    def __init__(self, UserID: int, UserName: str, UserLevel: int, UserBday: date, order11: set["Order"] = None):
        self.UserID = UserID
        self.UserName = UserName
        self.UserLevel = UserLevel
        self.UserBday = UserBday
        self.order11 = order11 if order11 is not None else set()
        
        pass
    @property
    def UserBday(self):
        return self.__UserBday
    @UserBday.setter
    def UserBday(self, UserBday: date):
        self.__UserBday = UserBday

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
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

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
                    

