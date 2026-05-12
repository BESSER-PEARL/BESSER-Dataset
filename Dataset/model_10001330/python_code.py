from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class RiderStatusUpdate:

    def __init__(self, OrderDate_Time: str, CustomerName: str, ItemList: str):
        self.OrderDate_Time = OrderDate_Time
        self.CustomerName = CustomerName
        self.ItemList = ItemList
        
        pass
    @property
    def OrderDate_Time(self):
        return self.__OrderDate_Time
    @OrderDate_Time.setter
    def OrderDate_Time(self, OrderDate_Time: str):
        self.__OrderDate_Time = OrderDate_Time

    @property
    def ItemList(self):
        return self.__ItemList
    @ItemList.setter
    def ItemList(self, ItemList: str):
        self.__ItemList = ItemList

    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName



class Order:

    def __init__(self, OrderTime_Date: str, OrderStatus: str, OrderReview: str, OrderPrice: str, OrderRider: str):
        self.OrderTime_Date = OrderTime_Date
        self.OrderStatus = OrderStatus
        self.OrderReview = OrderReview
        self.OrderPrice = OrderPrice
        self.OrderRider = OrderRider
        
        pass
    @property
    def OrderReview(self):
        return self.__OrderReview
    @OrderReview.setter
    def OrderReview(self, OrderReview: str):
        self.__OrderReview = OrderReview

    @property
    def OrderStatus(self):
        return self.__OrderStatus
    @OrderStatus.setter
    def OrderStatus(self, OrderStatus: str):
        self.__OrderStatus = OrderStatus

    @property
    def OrderTime_Date(self):
        return self.__OrderTime_Date
    @OrderTime_Date.setter
    def OrderTime_Date(self, OrderTime_Date: str):
        self.__OrderTime_Date = OrderTime_Date

    @property
    def OrderPrice(self):
        return self.__OrderPrice
    @OrderPrice.setter
    def OrderPrice(self, OrderPrice: str):
        self.__OrderPrice = OrderPrice

    @property
    def OrderRider(self):
        return self.__OrderRider
    @OrderRider.setter
    def OrderRider(self, OrderRider: str):
        self.__OrderRider = OrderRider



class CompanyTrackOrder:

    def __init__(self, CustomerName: str, OrderDate_Time: str, OrderRider: str, OrderStatus: str):
        self.CustomerName = CustomerName
        self.OrderDate_Time = OrderDate_Time
        self.OrderRider = OrderRider
        self.OrderStatus = OrderStatus
        
        pass
    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def OrderDate_Time(self):
        return self.__OrderDate_Time
    @OrderDate_Time.setter
    def OrderDate_Time(self, OrderDate_Time: str):
        self.__OrderDate_Time = OrderDate_Time

    @property
    def OrderRider(self):
        return self.__OrderRider
    @OrderRider.setter
    def OrderRider(self, OrderRider: str):
        self.__OrderRider = OrderRider

    @property
    def OrderStatus(self):
        return self.__OrderStatus
    @OrderStatus.setter
    def OrderStatus(self, OrderStatus: str):
        self.__OrderStatus = OrderStatus



class CompanyOrderHistory:

    def __init__(self, CustomerName: str, OrderDate_Time: str, OrderReview: str, OrderRider: str):
        self.CustomerName = CustomerName
        self.OrderDate_Time = OrderDate_Time
        self.OrderReview = OrderReview
        self.OrderRider = OrderRider
        
        pass
    @property
    def OrderReview(self):
        return self.__OrderReview
    @OrderReview.setter
    def OrderReview(self, OrderReview: str):
        self.__OrderReview = OrderReview

    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def OrderRider(self):
        return self.__OrderRider
    @OrderRider.setter
    def OrderRider(self, OrderRider: str):
        self.__OrderRider = OrderRider

    @property
    def OrderDate_Time(self):
        return self.__OrderDate_Time
    @OrderDate_Time.setter
    def OrderDate_Time(self, OrderDate_Time: str):
        self.__OrderDate_Time = OrderDate_Time



class CompanyAssignRider:

    def __init__(self, CustomerName: str, OrderDate_Time: str, OrderRider: str):
        self.CustomerName = CustomerName
        self.OrderDate_Time = OrderDate_Time
        self.OrderRider = OrderRider
        
        pass
    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def OrderRider(self):
        return self.__OrderRider
    @OrderRider.setter
    def OrderRider(self, OrderRider: str):
        self.__OrderRider = OrderRider

    @property
    def OrderDate_Time(self):
        return self.__OrderDate_Time
    @OrderDate_Time.setter
    def OrderDate_Time(self, OrderDate_Time: str):
        self.__OrderDate_Time = OrderDate_Time



class phon:

    pass


class CompanyAddRider:

    def __init__(self, Name: str, UserName: str, Email: str, Password: str, Address: str, Phone: str, CNIC: int):
        self.Name = Name
        self.UserName = UserName
        self.Email = Email
        self.Password = Password
        self.Address = Address
        self.Phone = Phone
        self.CNIC = CNIC
        
        pass
    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def CNIC(self):
        return self.__CNIC
    @CNIC.setter
    def CNIC(self, CNIC: int):
        self.__CNIC = CNIC

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName



class CompanyAddItem:

    def __init__(self, Name: str, Price: str, Description: str, Category: str):
        self.Name = Name
        self.Price = Price
        self.Description = Description
        self.Category = Category
        
        pass
    @property
    def Category(self):
        return self.__Category
    @Category.setter
    def Category(self, Category: str):
        self.__Category = Category

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price



class CartItems:

    def __init__(self, Name: str, Price: str):
        self.Name = Name
        self.Price = Price
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class Login:

    def __init__(self, Email: str, Password: str):
        self.Email = Email
        self.Password = Password
        
        pass
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



class UserRegisteration:

    def __init__(self, FirstName: str, LastName: str, UserName: str, Email: str, Password: str, Address: str, Phone: str):
        self.FirstName = FirstName
        self.LastName = LastName
        self.UserName = UserName
        self.Email = Email
        self.Password = Password
        self.Address = Address
        self.Phone = Phone
        
        pass
    @property
    def FirstName(self):
        return self.__FirstName
    @FirstName.setter
    def FirstName(self, FirstName: str):
        self.__FirstName = FirstName

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, LastName: str):
        self.__LastName = LastName

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

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
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address



class PlaceOrder:

    def __init__(self, Name: str, Price: str):
        self.Name = Name
        self.Price = Price
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class Categories:

    def __init__(self, Categories: str):
        self.Categories = Categories
        
        pass
    @property
    def Categories(self):
        return self.__Categories
    @Categories.setter
    def Categories(self, Categories: str):
        self.__Categories = Categories



class ConfirmOrder:

    def __init__(self, OrderName: str, OrderPrice: str, Quantity: str, StoreName: str):
        self.OrderName = OrderName
        self.OrderPrice = OrderPrice
        self.Quantity = Quantity
        self.StoreName = StoreName
        
        pass
    @property
    def OrderName(self):
        return self.__OrderName
    @OrderName.setter
    def OrderName(self, OrderName: str):
        self.__OrderName = OrderName

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: str):
        self.__Quantity = Quantity

    @property
    def OrderPrice(self):
        return self.__OrderPrice
    @OrderPrice.setter
    def OrderPrice(self, OrderPrice: str):
        self.__OrderPrice = OrderPrice

    @property
    def StoreName(self):
        return self.__StoreName
    @StoreName.setter
    def StoreName(self, StoreName: str):
        self.__StoreName = StoreName



class OrderHistory:

    def __init__(self, OrderReview: str, OrderStatus: str, OrderDate_Time: str, OrderRider: str):
        self.OrderReview = OrderReview
        self.OrderStatus = OrderStatus
        self.OrderDate_Time = OrderDate_Time
        self.OrderRider = OrderRider
        
        pass
    @property
    def OrderReview(self):
        return self.__OrderReview
    @OrderReview.setter
    def OrderReview(self, OrderReview: str):
        self.__OrderReview = OrderReview

    @property
    def OrderDate_Time(self):
        return self.__OrderDate_Time
    @OrderDate_Time.setter
    def OrderDate_Time(self, OrderDate_Time: str):
        self.__OrderDate_Time = OrderDate_Time

    @property
    def OrderRider(self):
        return self.__OrderRider
    @OrderRider.setter
    def OrderRider(self, OrderRider: str):
        self.__OrderRider = OrderRider

    @property
    def OrderStatus(self):
        return self.__OrderStatus
    @OrderStatus.setter
    def OrderStatus(self, OrderStatus: str):
        self.__OrderStatus = OrderStatus



class ReviewOrder:

    def __init__(self, OrderTime_Date: str, RiderName: str, Review: str):
        self.OrderTime_Date = OrderTime_Date
        self.RiderName = RiderName
        self.Review = Review
        
        pass
    @property
    def Review(self):
        return self.__Review
    @Review.setter
    def Review(self, Review: str):
        self.__Review = Review

    @property
    def OrderTime_Date(self):
        return self.__OrderTime_Date
    @OrderTime_Date.setter
    def OrderTime_Date(self, OrderTime_Date: str):
        self.__OrderTime_Date = OrderTime_Date

    @property
    def RiderName(self):
        return self.__RiderName
    @RiderName.setter
    def RiderName(self, RiderName: str):
        self.__RiderName = RiderName



class void_Interface:

    pass


class Store:

    def __init__(self, Name: str):
        self.Name = Name
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class TrackOrder:

    def __init__(self, OrderTime_Date: str, OrderTrack: str):
        self.OrderTime_Date = OrderTime_Date
        self.OrderTrack = OrderTrack
        
        pass
    @property
    def OrderTime_Date(self):
        return self.__OrderTime_Date
    @OrderTime_Date.setter
    def OrderTime_Date(self, OrderTime_Date: str):
        self.__OrderTime_Date = OrderTime_Date

    @property
    def OrderTrack(self):
        return self.__OrderTrack
    @OrderTrack.setter
    def OrderTrack(self, OrderTrack: str):
        self.__OrderTrack = OrderTrack

