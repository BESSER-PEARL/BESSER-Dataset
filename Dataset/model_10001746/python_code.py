from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Shopping_Cart:

    def __init__(self, ProductPurchased: str, ClientAccount_Shopping_Cart_11: "ClientAccount" = None, product4: "Product" = None, order7: "Order" = None):
        self.ProductPurchased = ProductPurchased
        self.ClientAccount_Shopping_Cart_11 = ClientAccount_Shopping_Cart_11
        self.product4 = product4
        self.order7 = order7
        
        pass
    @property
    def ProductPurchased(self):
        return self.__ProductPurchased
    @ProductPurchased.setter
    def ProductPurchased(self, ProductPurchased: str):
        self.__ProductPurchased = ProductPurchased

    @property
    def order7(self):
        return self.__order7
    @order7.setter
    def order7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__order7", None)
        self.__order7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Cart6"):
                opp_val = getattr(old_value, "shopping_Cart6", None)
                if opp_val == self:
                    setattr(old_value, "shopping_Cart6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Cart6"):
                opp_val = getattr(value, "shopping_Cart6", None)
                setattr(value, "shopping_Cart6", self)

    @property
    def ClientAccount_Shopping_Cart_11(self):
        return self.__ClientAccount_Shopping_Cart_11
    @ClientAccount_Shopping_Cart_11.setter
    def ClientAccount_Shopping_Cart_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__ClientAccount_Shopping_Cart_11", None)
        self.__ClientAccount_Shopping_Cart_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClientAccount_Shopping_Cart_00"):
                opp_val = getattr(old_value, "ClientAccount_Shopping_Cart_00", None)
                if opp_val == self:
                    setattr(old_value, "ClientAccount_Shopping_Cart_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClientAccount_Shopping_Cart_00"):
                opp_val = getattr(value, "ClientAccount_Shopping_Cart_00", None)
                setattr(value, "ClientAccount_Shopping_Cart_00", self)

    @property
    def product4(self):
        return self.__product4
    @product4.setter
    def product4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_Cart__product4", None)
        self.__product4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_Cart5"):
                opp_val = getattr(old_value, "shopping_Cart5", None)
                if opp_val == self:
                    setattr(old_value, "shopping_Cart5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_Cart5"):
                opp_val = getattr(value, "shopping_Cart5", None)
                setattr(value, "shopping_Cart5", self)



class Order:

    def __init__(self, OrderNumber: int, Date: str, CustomerName: User, Products: Shopping_Cart, PaymentMethod: str, HomeAddress: User, clientAccount2: set["ClientAccount"] = None, shopping_Cart6: "Shopping_Cart" = None):
        self.OrderNumber = OrderNumber
        self.Date = Date
        self.CustomerName = CustomerName
        self.Products = Products
        self.PaymentMethod = PaymentMethod
        self.HomeAddress = HomeAddress
        self.clientAccount2 = clientAccount2 if clientAccount2 is not None else set()
        self.shopping_Cart6 = shopping_Cart6
        
        pass
    @property
    def PaymentMethod(self):
        return self.__PaymentMethod
    @PaymentMethod.setter
    def PaymentMethod(self, PaymentMethod: str):
        self.__PaymentMethod = PaymentMethod

    @property
    def OrderNumber(self):
        return self.__OrderNumber
    @OrderNumber.setter
    def OrderNumber(self, OrderNumber: int):
        self.__OrderNumber = OrderNumber

    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: User):
        self.__CustomerName = CustomerName

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def HomeAddress(self):
        return self.__HomeAddress
    @HomeAddress.setter
    def HomeAddress(self, HomeAddress: User):
        self.__HomeAddress = HomeAddress

    @property
    def Products(self):
        return self.__Products
    @Products.setter
    def Products(self, Products: Shopping_Cart):
        self.__Products = Products

    @property
    def clientAccount2(self):
        return self.__clientAccount2
    @clientAccount2.setter
    def clientAccount2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__clientAccount2", None)
        self.__clientAccount2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order3"):
                    opp_val = getattr(item, "order3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order3"):
                    opp_val = getattr(item, "order3", None)
                    
                    if opp_val is None:
                        setattr(item, "order3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def shopping_Cart6(self):
        return self.__shopping_Cart6
    @shopping_Cart6.setter
    def shopping_Cart6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__shopping_Cart6", None)
        self.__shopping_Cart6 = value
        
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



class Double_Interface:

    pass


class ClientAccount:

    def __init__(self, Password: str, ClientAccount_Shopping_Cart_00: "Shopping_Cart" = None, order3: set["Order"] = None):
        self.Password = Password
        self.ClientAccount_Shopping_Cart_00 = ClientAccount_Shopping_Cart_00
        self.order3 = order3 if order3 is not None else set()
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def ClientAccount_Shopping_Cart_00(self):
        return self.__ClientAccount_Shopping_Cart_00
    @ClientAccount_Shopping_Cart_00.setter
    def ClientAccount_Shopping_Cart_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClientAccount__ClientAccount_Shopping_Cart_00", None)
        self.__ClientAccount_Shopping_Cart_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClientAccount_Shopping_Cart_11"):
                opp_val = getattr(old_value, "ClientAccount_Shopping_Cart_11", None)
                if opp_val == self:
                    setattr(old_value, "ClientAccount_Shopping_Cart_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClientAccount_Shopping_Cart_11"):
                opp_val = getattr(value, "ClientAccount_Shopping_Cart_11", None)
                setattr(value, "ClientAccount_Shopping_Cart_11", self)

    @property
    def order3(self):
        return self.__order3
    @order3.setter
    def order3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClientAccount__order3", None)
        self.__order3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "clientAccount2"):
                    opp_val = getattr(item, "clientAccount2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "clientAccount2"):
                    opp_val = getattr(item, "clientAccount2", None)
                    
                    if opp_val is None:
                        setattr(item, "clientAccount2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class User:

    def __init__(self, Name: str, Surname: str, Age: int, Email: str, HomeAddress: str):
        self.Name = Name
        self.Surname = Surname
        self.Age = Age
        self.Email = Email
        self.HomeAddress = HomeAddress
        
        pass
    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def Surname(self):
        return self.__Surname
    @Surname.setter
    def Surname(self, Surname: str):
        self.__Surname = Surname

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
    def HomeAddress(self):
        return self.__HomeAddress
    @HomeAddress.setter
    def HomeAddress(self, HomeAddress: str):
        self.__HomeAddress = HomeAddress



class Product:

    def __init__(self, ProductID: int, ProductName: str, ProductType: str, ProductPrice: float, ProductDescription: str, ProductImage: str, shopping_Cart5: "Shopping_Cart" = None):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.ProductType = ProductType
        self.ProductPrice = ProductPrice
        self.ProductDescription = ProductDescription
        self.ProductImage = ProductImage
        self.shopping_Cart5 = shopping_Cart5
        
        pass
    @property
    def ProductPrice(self):
        return self.__ProductPrice
    @ProductPrice.setter
    def ProductPrice(self, ProductPrice: float):
        self.__ProductPrice = ProductPrice

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def ProductDescription(self):
        return self.__ProductDescription
    @ProductDescription.setter
    def ProductDescription(self, ProductDescription: str):
        self.__ProductDescription = ProductDescription

    @property
    def ProductType(self):
        return self.__ProductType
    @ProductType.setter
    def ProductType(self, ProductType: str):
        self.__ProductType = ProductType

    @property
    def ProductImage(self):
        return self.__ProductImage
    @ProductImage.setter
    def ProductImage(self, ProductImage: str):
        self.__ProductImage = ProductImage

    @property
    def ProductName(self):
        return self.__ProductName
    @ProductName.setter
    def ProductName(self, ProductName: str):
        self.__ProductName = ProductName

    @property
    def shopping_Cart5(self):
        return self.__shopping_Cart5
    @shopping_Cart5.setter
    def shopping_Cart5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__shopping_Cart5", None)
        self.__shopping_Cart5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product4"):
                opp_val = getattr(old_value, "product4", None)
                if opp_val == self:
                    setattr(old_value, "product4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product4"):
                opp_val = getattr(value, "product4", None)
                setattr(value, "product4", self)

