from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, CustomerID: int, CustomerName: str, Address: str, Phone: str, Email: str, Gender: int, order2: "Order" = None):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.Gender = Gender
        self.order2 = order2
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: int):
        self.__CustomerID = CustomerID

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: int):
        self.__Gender = Gender

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
    def order2(self):
        return self.__order2
    @order2.setter
    def order2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order2", None)
        self.__order2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer3"):
                opp_val = getattr(old_value, "customer3", None)
                if opp_val == self:
                    setattr(old_value, "customer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer3"):
                opp_val = getattr(value, "customer3", None)
                setattr(value, "customer3", self)



class FlashSale:

    def __init__(self, FlashSaleID: int, FlashSaleName: str, OnlineShopID: int, DiscountPercent: int, DiscountAmount: int, Description: str, baseDateInformation17: "BaseDateInformation" = None, onlineShop19: "OnlineShop" = None):
        self.FlashSaleID = FlashSaleID
        self.FlashSaleName = FlashSaleName
        self.OnlineShopID = OnlineShopID
        self.DiscountPercent = DiscountPercent
        self.DiscountAmount = DiscountAmount
        self.Description = Description
        self.baseDateInformation17 = baseDateInformation17
        self.onlineShop19 = onlineShop19
        
        pass
    @property
    def DiscountAmount(self):
        return self.__DiscountAmount
    @DiscountAmount.setter
    def DiscountAmount(self, DiscountAmount: int):
        self.__DiscountAmount = DiscountAmount

    @property
    def FlashSaleName(self):
        return self.__FlashSaleName
    @FlashSaleName.setter
    def FlashSaleName(self, FlashSaleName: str):
        self.__FlashSaleName = FlashSaleName

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def OnlineShopID(self):
        return self.__OnlineShopID
    @OnlineShopID.setter
    def OnlineShopID(self, OnlineShopID: int):
        self.__OnlineShopID = OnlineShopID

    @property
    def FlashSaleID(self):
        return self.__FlashSaleID
    @FlashSaleID.setter
    def FlashSaleID(self, FlashSaleID: int):
        self.__FlashSaleID = FlashSaleID

    @property
    def DiscountPercent(self):
        return self.__DiscountPercent
    @DiscountPercent.setter
    def DiscountPercent(self, DiscountPercent: int):
        self.__DiscountPercent = DiscountPercent

    @property
    def onlineShop19(self):
        return self.__onlineShop19
    @onlineShop19.setter
    def onlineShop19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlashSale__onlineShop19", None)
        self.__onlineShop19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flashSale18"):
                opp_val = getattr(old_value, "flashSale18", None)
                if opp_val == self:
                    setattr(old_value, "flashSale18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flashSale18"):
                opp_val = getattr(value, "flashSale18", None)
                setattr(value, "flashSale18", self)

    @property
    def baseDateInformation17(self):
        return self.__baseDateInformation17
    @baseDateInformation17.setter
    def baseDateInformation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FlashSale__baseDateInformation17", None)
        self.__baseDateInformation17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flashSale16"):
                opp_val = getattr(old_value, "flashSale16", None)
                if opp_val == self:
                    setattr(old_value, "flashSale16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flashSale16"):
                opp_val = getattr(value, "flashSale16", None)
                setattr(value, "flashSale16", self)



class BaseDateInformation:

    def __init__(self, CreatedBy: str, CreateDate: str, LastModifedBy: str, LastModifedDate: str, product10: "Product" = None, flashSale16: "FlashSale" = None, onlineShop22: "OnlineShop" = None, category6: "Category" = None):
        self.CreatedBy = CreatedBy
        self.CreateDate = CreateDate
        self.LastModifedBy = LastModifedBy
        self.LastModifedDate = LastModifedDate
        self.product10 = product10
        self.flashSale16 = flashSale16
        self.onlineShop22 = onlineShop22
        self.category6 = category6
        
        pass
    @property
    def CreateDate(self):
        return self.__CreateDate
    @CreateDate.setter
    def CreateDate(self, CreateDate: str):
        self.__CreateDate = CreateDate

    @property
    def CreatedBy(self):
        return self.__CreatedBy
    @CreatedBy.setter
    def CreatedBy(self, CreatedBy: str):
        self.__CreatedBy = CreatedBy

    @property
    def LastModifedBy(self):
        return self.__LastModifedBy
    @LastModifedBy.setter
    def LastModifedBy(self, LastModifedBy: str):
        self.__LastModifedBy = LastModifedBy

    @property
    def LastModifedDate(self):
        return self.__LastModifedDate
    @LastModifedDate.setter
    def LastModifedDate(self, LastModifedDate: str):
        self.__LastModifedDate = LastModifedDate

    @property
    def flashSale16(self):
        return self.__flashSale16
    @flashSale16.setter
    def flashSale16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BaseDateInformation__flashSale16", None)
        self.__flashSale16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseDateInformation17"):
                opp_val = getattr(old_value, "baseDateInformation17", None)
                if opp_val == self:
                    setattr(old_value, "baseDateInformation17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseDateInformation17"):
                opp_val = getattr(value, "baseDateInformation17", None)
                setattr(value, "baseDateInformation17", self)

    @property
    def category6(self):
        return self.__category6
    @category6.setter
    def category6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BaseDateInformation__category6", None)
        self.__category6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseDateInformation7"):
                opp_val = getattr(old_value, "baseDateInformation7", None)
                if opp_val == self:
                    setattr(old_value, "baseDateInformation7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseDateInformation7"):
                opp_val = getattr(value, "baseDateInformation7", None)
                setattr(value, "baseDateInformation7", self)

    @property
    def onlineShop22(self):
        return self.__onlineShop22
    @onlineShop22.setter
    def onlineShop22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BaseDateInformation__onlineShop22", None)
        self.__onlineShop22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseDateInformation23"):
                opp_val = getattr(old_value, "baseDateInformation23", None)
                if opp_val == self:
                    setattr(old_value, "baseDateInformation23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseDateInformation23"):
                opp_val = getattr(value, "baseDateInformation23", None)
                setattr(value, "baseDateInformation23", self)

    @property
    def product10(self):
        return self.__product10
    @product10.setter
    def product10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BaseDateInformation__product10", None)
        self.__product10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseDateInformation11"):
                opp_val = getattr(old_value, "baseDateInformation11", None)
                if opp_val == self:
                    setattr(old_value, "baseDateInformation11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseDateInformation11"):
                opp_val = getattr(value, "baseDateInformation11", None)
                setattr(value, "baseDateInformation11", self)



class Role:

    def __init__(self, RoleID: int, RoleName: str, Description: str, isActive: bool, user13: "User" = None):
        self.RoleID = RoleID
        self.RoleName = RoleName
        self.Description = Description
        self.isActive = isActive
        self.user13 = user13
        
        pass
    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def RoleID(self):
        return self.__RoleID
    @RoleID.setter
    def RoleID(self, RoleID: int):
        self.__RoleID = RoleID

    @property
    def RoleName(self):
        return self.__RoleName
    @RoleName.setter
    def RoleName(self, RoleName: str):
        self.__RoleName = RoleName

    @property
    def isActive(self):
        return self.__isActive
    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def user13(self):
        return self.__user13
    @user13.setter
    def user13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Role__user13", None)
        self.__user13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "role12"):
                opp_val = getattr(old_value, "role12", None)
                if opp_val == self:
                    setattr(old_value, "role12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "role12"):
                opp_val = getattr(value, "role12", None)
                setattr(value, "role12", self)



class User:

    def __init__(self, UserID: str, Username: str, RoleID: int, Password: str, RegisterDate: str, isActive: bool, role12: "Role" = None, onlineShop15: "OnlineShop" = None):
        self.UserID = UserID
        self.Username = Username
        self.RoleID = RoleID
        self.Password = Password
        self.RegisterDate = RegisterDate
        self.isActive = isActive
        self.role12 = role12
        self.onlineShop15 = onlineShop15
        
        pass
    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: str):
        self.__UserID = UserID

    @property
    def RoleID(self):
        return self.__RoleID
    @RoleID.setter
    def RoleID(self, RoleID: int):
        self.__RoleID = RoleID

    @property
    def isActive(self):
        return self.__isActive
    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def RegisterDate(self):
        return self.__RegisterDate
    @RegisterDate.setter
    def RegisterDate(self, RegisterDate: str):
        self.__RegisterDate = RegisterDate

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def onlineShop15(self):
        return self.__onlineShop15
    @onlineShop15.setter
    def onlineShop15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__onlineShop15", None)
        self.__onlineShop15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user14"):
                opp_val = getattr(old_value, "user14", None)
                if opp_val == self:
                    setattr(old_value, "user14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user14"):
                opp_val = getattr(value, "user14", None)
                setattr(value, "user14", self)

    @property
    def role12(self):
        return self.__role12
    @role12.setter
    def role12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__role12", None)
        self.__role12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user13"):
                opp_val = getattr(old_value, "user13", None)
                if opp_val == self:
                    setattr(old_value, "user13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user13"):
                opp_val = getattr(value, "user13", None)
                setattr(value, "user13", self)



class Product:

    def __init__(self, ProductID: int, ProductName: str, OnlineShopID: int, CategoryID: int, Description: str, Price: str, Image: str, isActive: bool, category1: "Category" = None, onlineShop8: "OnlineShop" = None, baseDateInformation11: "BaseDateInformation" = None):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.OnlineShopID = OnlineShopID
        self.CategoryID = CategoryID
        self.Description = Description
        self.Price = Price
        self.Image = Image
        self.isActive = isActive
        self.category1 = category1
        self.onlineShop8 = onlineShop8
        self.baseDateInformation11 = baseDateInformation11
        
        pass
    @property
    def isActive(self):
        return self.__isActive
    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def CategoryID(self):
        return self.__CategoryID
    @CategoryID.setter
    def CategoryID(self, CategoryID: int):
        self.__CategoryID = CategoryID

    @property
    def ProductName(self):
        return self.__ProductName
    @ProductName.setter
    def ProductName(self, ProductName: str):
        self.__ProductName = ProductName

    @property
    def Image(self):
        return self.__Image
    @Image.setter
    def Image(self, Image: str):
        self.__Image = Image

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def OnlineShopID(self):
        return self.__OnlineShopID
    @OnlineShopID.setter
    def OnlineShopID(self, OnlineShopID: int):
        self.__OnlineShopID = OnlineShopID

    @property
    def baseDateInformation11(self):
        return self.__baseDateInformation11
    @baseDateInformation11.setter
    def baseDateInformation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__baseDateInformation11", None)
        self.__baseDateInformation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product10"):
                opp_val = getattr(old_value, "product10", None)
                if opp_val == self:
                    setattr(old_value, "product10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product10"):
                opp_val = getattr(value, "product10", None)
                setattr(value, "product10", self)

    @property
    def category1(self):
        return self.__category1
    @category1.setter
    def category1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__category1", None)
        self.__category1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product0"):
                opp_val = getattr(old_value, "product0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product0"):
                opp_val = getattr(value, "product0", None)
                if opp_val is None:
                    setattr(value, "product0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def onlineShop8(self):
        return self.__onlineShop8
    @onlineShop8.setter
    def onlineShop8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__onlineShop8", None)
        self.__onlineShop8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product9"):
                opp_val = getattr(old_value, "product9", None)
                if opp_val == self:
                    setattr(old_value, "product9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product9"):
                opp_val = getattr(value, "product9", None)
                setattr(value, "product9", self)



class Order:

    def __init__(self, OrderID: int, ShopOnlineID: int, OrderDate: str, Status: bool, TotalPrice: str, TotalDiscount: str, OrderCustomerID: int, ReceiveCustomerID: int, UserID: int, onlineShop21: "OnlineShop" = None, customer3: "Customer" = None):
        self.OrderID = OrderID
        self.ShopOnlineID = ShopOnlineID
        self.OrderDate = OrderDate
        self.Status = Status
        self.TotalPrice = TotalPrice
        self.TotalDiscount = TotalDiscount
        self.OrderCustomerID = OrderCustomerID
        self.ReceiveCustomerID = ReceiveCustomerID
        self.UserID = UserID
        self.onlineShop21 = onlineShop21
        self.customer3 = customer3
        
        pass
    @property
    def ShopOnlineID(self):
        return self.__ShopOnlineID
    @ShopOnlineID.setter
    def ShopOnlineID(self, ShopOnlineID: int):
        self.__ShopOnlineID = ShopOnlineID

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: bool):
        self.__Status = Status

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def TotalPrice(self):
        return self.__TotalPrice
    @TotalPrice.setter
    def TotalPrice(self, TotalPrice: str):
        self.__TotalPrice = TotalPrice

    @property
    def OrderCustomerID(self):
        return self.__OrderCustomerID
    @OrderCustomerID.setter
    def OrderCustomerID(self, OrderCustomerID: int):
        self.__OrderCustomerID = OrderCustomerID

    @property
    def TotalDiscount(self):
        return self.__TotalDiscount
    @TotalDiscount.setter
    def TotalDiscount(self, TotalDiscount: str):
        self.__TotalDiscount = TotalDiscount

    @property
    def ReceiveCustomerID(self):
        return self.__ReceiveCustomerID
    @ReceiveCustomerID.setter
    def ReceiveCustomerID(self, ReceiveCustomerID: int):
        self.__ReceiveCustomerID = ReceiveCustomerID

    @property
    def OrderDate(self):
        return self.__OrderDate
    @OrderDate.setter
    def OrderDate(self, OrderDate: str):
        self.__OrderDate = OrderDate

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def onlineShop21(self):
        return self.__onlineShop21
    @onlineShop21.setter
    def onlineShop21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__onlineShop21", None)
        self.__onlineShop21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order20"):
                opp_val = getattr(old_value, "order20", None)
                if opp_val == self:
                    setattr(old_value, "order20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order20"):
                opp_val = getattr(value, "order20", None)
                setattr(value, "order20", self)

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order2"):
                opp_val = getattr(old_value, "order2", None)
                if opp_val == self:
                    setattr(old_value, "order2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order2"):
                opp_val = getattr(value, "order2", None)
                setattr(value, "order2", self)



class OnlineShop:

    def __init__(self, OnlineShopID: int, OnlineShopName: str, ShopCategoryID: int, isActive: bool, product9: "Product" = None, user14: "User" = None, flashSale18: "FlashSale" = None, order20: "Order" = None, baseDateInformation23: "BaseDateInformation" = None, category5: "Category" = None):
        self.OnlineShopID = OnlineShopID
        self.OnlineShopName = OnlineShopName
        self.ShopCategoryID = ShopCategoryID
        self.isActive = isActive
        self.product9 = product9
        self.user14 = user14
        self.flashSale18 = flashSale18
        self.order20 = order20
        self.baseDateInformation23 = baseDateInformation23
        self.category5 = category5
        
        pass
    @property
    def OnlineShopName(self):
        return self.__OnlineShopName
    @OnlineShopName.setter
    def OnlineShopName(self, OnlineShopName: str):
        self.__OnlineShopName = OnlineShopName

    @property
    def OnlineShopID(self):
        return self.__OnlineShopID
    @OnlineShopID.setter
    def OnlineShopID(self, OnlineShopID: int):
        self.__OnlineShopID = OnlineShopID

    @property
    def isActive(self):
        return self.__isActive
    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def ShopCategoryID(self):
        return self.__ShopCategoryID
    @ShopCategoryID.setter
    def ShopCategoryID(self, ShopCategoryID: int):
        self.__ShopCategoryID = ShopCategoryID

    @property
    def baseDateInformation23(self):
        return self.__baseDateInformation23
    @baseDateInformation23.setter
    def baseDateInformation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OnlineShop__baseDateInformation23", None)
        self.__baseDateInformation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "onlineShop22"):
                opp_val = getattr(old_value, "onlineShop22", None)
                if opp_val == self:
                    setattr(old_value, "onlineShop22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "onlineShop22"):
                opp_val = getattr(value, "onlineShop22", None)
                setattr(value, "onlineShop22", self)

    @property
    def product9(self):
        return self.__product9
    @product9.setter
    def product9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OnlineShop__product9", None)
        self.__product9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "onlineShop8"):
                opp_val = getattr(old_value, "onlineShop8", None)
                if opp_val == self:
                    setattr(old_value, "onlineShop8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "onlineShop8"):
                opp_val = getattr(value, "onlineShop8", None)
                setattr(value, "onlineShop8", self)

    @property
    def flashSale18(self):
        return self.__flashSale18
    @flashSale18.setter
    def flashSale18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OnlineShop__flashSale18", None)
        self.__flashSale18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "onlineShop19"):
                opp_val = getattr(old_value, "onlineShop19", None)
                if opp_val == self:
                    setattr(old_value, "onlineShop19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "onlineShop19"):
                opp_val = getattr(value, "onlineShop19", None)
                setattr(value, "onlineShop19", self)

    @property
    def category5(self):
        return self.__category5
    @category5.setter
    def category5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OnlineShop__category5", None)
        self.__category5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "onlineShop4"):
                opp_val = getattr(old_value, "onlineShop4", None)
                if opp_val == self:
                    setattr(old_value, "onlineShop4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "onlineShop4"):
                opp_val = getattr(value, "onlineShop4", None)
                setattr(value, "onlineShop4", self)

    @property
    def user14(self):
        return self.__user14
    @user14.setter
    def user14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OnlineShop__user14", None)
        self.__user14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "onlineShop15"):
                opp_val = getattr(old_value, "onlineShop15", None)
                if opp_val == self:
                    setattr(old_value, "onlineShop15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "onlineShop15"):
                opp_val = getattr(value, "onlineShop15", None)
                setattr(value, "onlineShop15", self)

    @property
    def order20(self):
        return self.__order20
    @order20.setter
    def order20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OnlineShop__order20", None)
        self.__order20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "onlineShop21"):
                opp_val = getattr(old_value, "onlineShop21", None)
                if opp_val == self:
                    setattr(old_value, "onlineShop21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "onlineShop21"):
                opp_val = getattr(value, "onlineShop21", None)
                setattr(value, "onlineShop21", self)



class Category:

    def __init__(self, CategoryID: int, CategoryName: str, Description: str, isActive: bool, product0: set["Product"] = None, onlineShop4: "OnlineShop" = None, baseDateInformation7: "BaseDateInformation" = None):
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName
        self.Description = Description
        self.isActive = isActive
        self.product0 = product0 if product0 is not None else set()
        self.onlineShop4 = onlineShop4
        self.baseDateInformation7 = baseDateInformation7
        
        pass
    @property
    def CategoryName(self):
        return self.__CategoryName
    @CategoryName.setter
    def CategoryName(self, CategoryName: str):
        self.__CategoryName = CategoryName

    @property
    def isActive(self):
        return self.__isActive
    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def CategoryID(self):
        return self.__CategoryID
    @CategoryID.setter
    def CategoryID(self, CategoryID: int):
        self.__CategoryID = CategoryID

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def product0(self):
        return self.__product0
    @product0.setter
    def product0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__product0", None)
        self.__product0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "category1"):
                    opp_val = getattr(item, "category1", None)
                    
                    if opp_val == self:
                        setattr(item, "category1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "category1"):
                    opp_val = getattr(item, "category1", None)
                    
                    setattr(item, "category1", self)
                    

    @property
    def baseDateInformation7(self):
        return self.__baseDateInformation7
    @baseDateInformation7.setter
    def baseDateInformation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__baseDateInformation7", None)
        self.__baseDateInformation7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category6"):
                opp_val = getattr(old_value, "category6", None)
                if opp_val == self:
                    setattr(old_value, "category6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category6"):
                opp_val = getattr(value, "category6", None)
                setattr(value, "category6", self)

    @property
    def onlineShop4(self):
        return self.__onlineShop4
    @onlineShop4.setter
    def onlineShop4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Category__onlineShop4", None)
        self.__onlineShop4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category5"):
                opp_val = getattr(old_value, "category5", None)
                if opp_val == self:
                    setattr(old_value, "category5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category5"):
                opp_val = getattr(value, "category5", None)
                setattr(value, "category5", self)

