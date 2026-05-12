from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Vendor:

    def __init__(self, VendorID: int, Name: str, Address: str, Contact_Number: int, Email: str, Product_Vendor_115: set["Product"] = None):
        self.VendorID = VendorID
        self.Name = Name
        self.Address = Address
        self.Contact_Number = Contact_Number
        self.Email = Email
        self.Product_Vendor_115 = Product_Vendor_115 if Product_Vendor_115 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Contact_Number(self):
        return self.__Contact_Number
    @Contact_Number.setter
    def Contact_Number(self, Contact_Number: int):
        self.__Contact_Number = Contact_Number

    @property
    def VendorID(self):
        return self.__VendorID
    @VendorID.setter
    def VendorID(self, VendorID: int):
        self.__VendorID = VendorID

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Product_Vendor_115(self):
        return self.__Product_Vendor_115
    @Product_Vendor_115.setter
    def Product_Vendor_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vendor__Product_Vendor_115", None)
        self.__Product_Vendor_115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Product_Vendor_014"):
                    opp_val = getattr(item, "Product_Vendor_014", None)
                    
                    if opp_val == self:
                        setattr(item, "Product_Vendor_014", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Product_Vendor_014"):
                    opp_val = getattr(item, "Product_Vendor_014", None)
                    
                    setattr(item, "Product_Vendor_014", self)
                    



class UserAddress:

    def __init__(self, City: str, StreetNum: int, StreetName: str, PostCode: str, user_Account11: "User_Account" = None):
        self.City = City
        self.StreetNum = StreetNum
        self.StreetName = StreetName
        self.PostCode = PostCode
        self.user_Account11 = user_Account11
        
        pass
    @property
    def PostCode(self):
        return self.__PostCode
    @PostCode.setter
    def PostCode(self, PostCode: str):
        self.__PostCode = PostCode

    @property
    def City(self):
        return self.__City
    @City.setter
    def City(self, City: str):
        self.__City = City

    @property
    def StreetNum(self):
        return self.__StreetNum
    @StreetNum.setter
    def StreetNum(self, StreetNum: int):
        self.__StreetNum = StreetNum

    @property
    def StreetName(self):
        return self.__StreetName
    @StreetName.setter
    def StreetName(self, StreetName: str):
        self.__StreetName = StreetName

    @property
    def user_Account11(self):
        return self.__user_Account11
    @user_Account11.setter
    def user_Account11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UserAddress__user_Account11", None)
        self.__user_Account11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "userAddress10"):
                opp_val = getattr(old_value, "userAddress10", None)
                if opp_val == self:
                    setattr(old_value, "userAddress10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "userAddress10"):
                opp_val = getattr(value, "userAddress10", None)
                setattr(value, "userAddress10", self)



class Promos:

    def __init__(self, PromoCode: str, Name: str, Discount: str, StartDate: str, EndDate: str, shoppingCart8: set["ShoppingCart"] = None, Premium_Members_Promos_113: "Premium_Members" = None):
        self.PromoCode = PromoCode
        self.Name = Name
        self.Discount = Discount
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.shoppingCart8 = shoppingCart8 if shoppingCart8 is not None else set()
        self.Premium_Members_Promos_113 = Premium_Members_Promos_113
        
        pass
    @property
    def Discount(self):
        return self.__Discount
    @Discount.setter
    def Discount(self, Discount: str):
        self.__Discount = Discount

    @property
    def StartDate(self):
        return self.__StartDate
    @StartDate.setter
    def StartDate(self, StartDate: str):
        self.__StartDate = StartDate

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def EndDate(self):
        return self.__EndDate
    @EndDate.setter
    def EndDate(self, EndDate: str):
        self.__EndDate = EndDate

    @property
    def PromoCode(self):
        return self.__PromoCode
    @PromoCode.setter
    def PromoCode(self, PromoCode: str):
        self.__PromoCode = PromoCode

    @property
    def shoppingCart8(self):
        return self.__shoppingCart8
    @shoppingCart8.setter
    def shoppingCart8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Promos__shoppingCart8", None)
        self.__shoppingCart8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "promos9"):
                    opp_val = getattr(item, "promos9", None)
                    
                    if opp_val == self:
                        setattr(item, "promos9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "promos9"):
                    opp_val = getattr(item, "promos9", None)
                    
                    setattr(item, "promos9", self)
                    

    @property
    def Premium_Members_Promos_113(self):
        return self.__Premium_Members_Promos_113
    @Premium_Members_Promos_113.setter
    def Premium_Members_Promos_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Promos__Premium_Members_Promos_113", None)
        self.__Premium_Members_Promos_113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Premium_Members_Promos_012"):
                opp_val = getattr(old_value, "Premium_Members_Promos_012", None)
                if opp_val == self:
                    setattr(old_value, "Premium_Members_Promos_012", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Premium_Members_Promos_012"):
                opp_val = getattr(value, "Premium_Members_Promos_012", None)
                setattr(value, "Premium_Members_Promos_012", self)



class Product:

    def __init__(self, ProductID: int, Description: str, InventoryQuantity: int, InventoryMinQuantity: int, VendorID: int, Product_Vendor_014: "Vendor" = None):
        self.ProductID = ProductID
        self.Description = Description
        self.InventoryQuantity = InventoryQuantity
        self.InventoryMinQuantity = InventoryMinQuantity
        self.VendorID = VendorID
        self.Product_Vendor_014 = Product_Vendor_014
        
        pass
    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def InventoryQuantity(self):
        return self.__InventoryQuantity
    @InventoryQuantity.setter
    def InventoryQuantity(self, InventoryQuantity: int):
        self.__InventoryQuantity = InventoryQuantity

    @property
    def VendorID(self):
        return self.__VendorID
    @VendorID.setter
    def VendorID(self, VendorID: int):
        self.__VendorID = VendorID

    @property
    def InventoryMinQuantity(self):
        return self.__InventoryMinQuantity
    @InventoryMinQuantity.setter
    def InventoryMinQuantity(self, InventoryMinQuantity: int):
        self.__InventoryMinQuantity = InventoryMinQuantity

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Product_Vendor_014(self):
        return self.__Product_Vendor_014
    @Product_Vendor_014.setter
    def Product_Vendor_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__Product_Vendor_014", None)
        self.__Product_Vendor_014 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Product_Vendor_115"):
                opp_val = getattr(old_value, "Product_Vendor_115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Product_Vendor_115"):
                opp_val = getattr(value, "Product_Vendor_115", None)
                if opp_val is None:
                    setattr(value, "Product_Vendor_115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class OrderProcess:

    def __init__(self, OrderID: int, UserID: int, MemberShipPayment: int, PromoCode: str, Total: str, IsMember: int, OrderPickUp: int, ShoppingCart_Order_13: "ShoppingCart" = None, user_Account7: "User_Account" = None):
        self.OrderID = OrderID
        self.UserID = UserID
        self.MemberShipPayment = MemberShipPayment
        self.PromoCode = PromoCode
        self.Total = Total
        self.IsMember = IsMember
        self.OrderPickUp = OrderPickUp
        self.ShoppingCart_Order_13 = ShoppingCart_Order_13
        self.user_Account7 = user_Account7
        
        pass
    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def Total(self):
        return self.__Total
    @Total.setter
    def Total(self, Total: str):
        self.__Total = Total

    @property
    def PromoCode(self):
        return self.__PromoCode
    @PromoCode.setter
    def PromoCode(self, PromoCode: str):
        self.__PromoCode = PromoCode

    @property
    def OrderPickUp(self):
        return self.__OrderPickUp
    @OrderPickUp.setter
    def OrderPickUp(self, OrderPickUp: int):
        self.__OrderPickUp = OrderPickUp

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def MemberShipPayment(self):
        return self.__MemberShipPayment
    @MemberShipPayment.setter
    def MemberShipPayment(self, MemberShipPayment: int):
        self.__MemberShipPayment = MemberShipPayment

    @property
    def IsMember(self):
        return self.__IsMember
    @IsMember.setter
    def IsMember(self, IsMember: int):
        self.__IsMember = IsMember

    @property
    def user_Account7(self):
        return self.__user_Account7
    @user_Account7.setter
    def user_Account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderProcess__user_Account7", None)
        self.__user_Account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderProcess6"):
                opp_val = getattr(old_value, "orderProcess6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderProcess6"):
                opp_val = getattr(value, "orderProcess6", None)
                if opp_val is None:
                    setattr(value, "orderProcess6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ShoppingCart_Order_13(self):
        return self.__ShoppingCart_Order_13
    @ShoppingCart_Order_13.setter
    def ShoppingCart_Order_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OrderProcess__ShoppingCart_Order_13", None)
        self.__ShoppingCart_Order_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_Order_02"):
                opp_val = getattr(old_value, "ShoppingCart_Order_02", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_Order_02", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_Order_02"):
                opp_val = getattr(value, "ShoppingCart_Order_02", None)
                setattr(value, "ShoppingCart_Order_02", self)



class ShoppingCart:

    def __init__(self, ShoppingCartID: int, OrderID: int, UserID: str, Total: str, ProductID: int, Quantity: int, Promo: Promos, ShoppingCart_Order_02: "OrderProcess" = None, Order_Regular_Members_04: "User_Account" = None, promos9: "Promos" = None):
        self.ShoppingCartID = ShoppingCartID
        self.OrderID = OrderID
        self.UserID = UserID
        self.Total = Total
        self.ProductID = ProductID
        self.Quantity = Quantity
        self.Promo = Promo
        self.ShoppingCart_Order_02 = ShoppingCart_Order_02
        self.Order_Regular_Members_04 = Order_Regular_Members_04
        self.promos9 = promos9
        
        pass
    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def ShoppingCartID(self):
        return self.__ShoppingCartID
    @ShoppingCartID.setter
    def ShoppingCartID(self, ShoppingCartID: int):
        self.__ShoppingCartID = ShoppingCartID

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def Total(self):
        return self.__Total
    @Total.setter
    def Total(self, Total: str):
        self.__Total = Total

    @property
    def Promo(self):
        return self.__Promo
    @Promo.setter
    def Promo(self, Promo: Promos):
        self.__Promo = Promo

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: str):
        self.__UserID = UserID

    @property
    def Order_Regular_Members_04(self):
        return self.__Order_Regular_Members_04
    @Order_Regular_Members_04.setter
    def Order_Regular_Members_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__Order_Regular_Members_04", None)
        self.__Order_Regular_Members_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Order_Regular_Members_15"):
                opp_val = getattr(old_value, "Order_Regular_Members_15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Order_Regular_Members_15"):
                opp_val = getattr(value, "Order_Regular_Members_15", None)
                if opp_val is None:
                    setattr(value, "Order_Regular_Members_15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ShoppingCart_Order_02(self):
        return self.__ShoppingCart_Order_02
    @ShoppingCart_Order_02.setter
    def ShoppingCart_Order_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__ShoppingCart_Order_02", None)
        self.__ShoppingCart_Order_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_Order_13"):
                opp_val = getattr(old_value, "ShoppingCart_Order_13", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_Order_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_Order_13"):
                opp_val = getattr(value, "ShoppingCart_Order_13", None)
                setattr(value, "ShoppingCart_Order_13", self)

    @property
    def promos9(self):
        return self.__promos9
    @promos9.setter
    def promos9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__promos9", None)
        self.__promos9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart8"):
                opp_val = getattr(old_value, "shoppingCart8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart8"):
                opp_val = getattr(value, "shoppingCart8", None)
                if opp_val is None:
                    setattr(value, "shoppingCart8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Regular_Members:

    def __init__(self, TriedPremium: int, TrialStartDate: str):
        self.TriedPremium = TriedPremium
        self.TrialStartDate = TrialStartDate
        
        pass
    @property
    def TriedPremium(self):
        return self.__TriedPremium
    @TriedPremium.setter
    def TriedPremium(self, TriedPremium: int):
        self.__TriedPremium = TriedPremium

    @property
    def TrialStartDate(self):
        return self.__TrialStartDate
    @TrialStartDate.setter
    def TrialStartDate(self, TrialStartDate: str):
        self.__TrialStartDate = TrialStartDate



class Premium_Members:

    def __init__(self, MembershipStartDate: str, MembershipEndDate: str, PromoCode: str, Premium_Members_Promos_012: "Promos" = None):
        self.MembershipStartDate = MembershipStartDate
        self.MembershipEndDate = MembershipEndDate
        self.PromoCode = PromoCode
        self.Premium_Members_Promos_012 = Premium_Members_Promos_012
        
        pass
    @property
    def MembershipEndDate(self):
        return self.__MembershipEndDate
    @MembershipEndDate.setter
    def MembershipEndDate(self, MembershipEndDate: str):
        self.__MembershipEndDate = MembershipEndDate

    @property
    def PromoCode(self):
        return self.__PromoCode
    @PromoCode.setter
    def PromoCode(self, PromoCode: str):
        self.__PromoCode = PromoCode

    @property
    def MembershipStartDate(self):
        return self.__MembershipStartDate
    @MembershipStartDate.setter
    def MembershipStartDate(self, MembershipStartDate: str):
        self.__MembershipStartDate = MembershipStartDate

    @property
    def Premium_Members_Promos_012(self):
        return self.__Premium_Members_Promos_012
    @Premium_Members_Promos_012.setter
    def Premium_Members_Promos_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Premium_Members__Premium_Members_Promos_012", None)
        self.__Premium_Members_Promos_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Premium_Members_Promos_113"):
                opp_val = getattr(old_value, "Premium_Members_Promos_113", None)
                if opp_val == self:
                    setattr(old_value, "Premium_Members_Promos_113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Premium_Members_Promos_113"):
                opp_val = getattr(value, "Premium_Members_Promos_113", None)
                setattr(value, "Premium_Members_Promos_113", self)



class UserName:

    def __init__(self, FirstName: str, LastName: str, Customer_ShoppingCart_11: "User_Account" = None):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Customer_ShoppingCart_11 = Customer_ShoppingCart_11
        
        pass
    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, LastName: str):
        self.__LastName = LastName

    @property
    def FirstName(self):
        return self.__FirstName
    @FirstName.setter
    def FirstName(self, FirstName: str):
        self.__FirstName = FirstName

    @property
    def Customer_ShoppingCart_11(self):
        return self.__Customer_ShoppingCart_11
    @Customer_ShoppingCart_11.setter
    def Customer_ShoppingCart_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UserName__Customer_ShoppingCart_11", None)
        self.__Customer_ShoppingCart_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_ShoppingCart_00"):
                opp_val = getattr(old_value, "Customer_ShoppingCart_00", None)
                if opp_val == self:
                    setattr(old_value, "Customer_ShoppingCart_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_ShoppingCart_00"):
                opp_val = getattr(value, "Customer_ShoppingCart_00", None)
                setattr(value, "Customer_ShoppingCart_00", self)



class User_Account:

    def __init__(self, UserID: str, FullName: str, Email: str, DateOfBirth: str, RegDate: str, UserAddress: str, Customer_ShoppingCart_00: "UserName" = None, Order_Regular_Members_15: set["ShoppingCart"] = None, orderProcess6: set["OrderProcess"] = None, userAddress10: "UserAddress" = None):
        self.UserID = UserID
        self.FullName = FullName
        self.Email = Email
        self.DateOfBirth = DateOfBirth
        self.RegDate = RegDate
        self.UserAddress = UserAddress
        self.Customer_ShoppingCart_00 = Customer_ShoppingCart_00
        self.Order_Regular_Members_15 = Order_Regular_Members_15 if Order_Regular_Members_15 is not None else set()
        self.orderProcess6 = orderProcess6 if orderProcess6 is not None else set()
        self.userAddress10 = userAddress10
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def FullName(self):
        return self.__FullName
    @FullName.setter
    def FullName(self, FullName: str):
        self.__FullName = FullName

    @property
    def DateOfBirth(self):
        return self.__DateOfBirth
    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth: str):
        self.__DateOfBirth = DateOfBirth

    @property
    def UserAddress(self):
        return self.__UserAddress
    @UserAddress.setter
    def UserAddress(self, UserAddress: str):
        self.__UserAddress = UserAddress

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: str):
        self.__UserID = UserID

    @property
    def RegDate(self):
        return self.__RegDate
    @RegDate.setter
    def RegDate(self, RegDate: str):
        self.__RegDate = RegDate

    @property
    def Order_Regular_Members_15(self):
        return self.__Order_Regular_Members_15
    @Order_Regular_Members_15.setter
    def Order_Regular_Members_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Account__Order_Regular_Members_15", None)
        self.__Order_Regular_Members_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order_Regular_Members_04"):
                    opp_val = getattr(item, "Order_Regular_Members_04", None)
                    
                    if opp_val == self:
                        setattr(item, "Order_Regular_Members_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order_Regular_Members_04"):
                    opp_val = getattr(item, "Order_Regular_Members_04", None)
                    
                    setattr(item, "Order_Regular_Members_04", self)
                    

    @property
    def userAddress10(self):
        return self.__userAddress10
    @userAddress10.setter
    def userAddress10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Account__userAddress10", None)
        self.__userAddress10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user_Account11"):
                opp_val = getattr(old_value, "user_Account11", None)
                if opp_val == self:
                    setattr(old_value, "user_Account11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user_Account11"):
                opp_val = getattr(value, "user_Account11", None)
                setattr(value, "user_Account11", self)

    @property
    def Customer_ShoppingCart_00(self):
        return self.__Customer_ShoppingCart_00
    @Customer_ShoppingCart_00.setter
    def Customer_ShoppingCart_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Account__Customer_ShoppingCart_00", None)
        self.__Customer_ShoppingCart_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_ShoppingCart_11"):
                opp_val = getattr(old_value, "Customer_ShoppingCart_11", None)
                if opp_val == self:
                    setattr(old_value, "Customer_ShoppingCart_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_ShoppingCart_11"):
                opp_val = getattr(value, "Customer_ShoppingCart_11", None)
                setattr(value, "Customer_ShoppingCart_11", self)

    @property
    def orderProcess6(self):
        return self.__orderProcess6
    @orderProcess6.setter
    def orderProcess6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Account__orderProcess6", None)
        self.__orderProcess6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user_Account7"):
                    opp_val = getattr(item, "user_Account7", None)
                    
                    if opp_val == self:
                        setattr(item, "user_Account7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user_Account7"):
                    opp_val = getattr(item, "user_Account7", None)
                    
                    setattr(item, "user_Account7", self)
                    

