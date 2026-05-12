from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class search_UseCase:

    pass


class registered_client_Actor:

    pass


class online_client_Actor:

    pass


class admin_Actor:

    pass





class Order:

    def __init__(self, OrderID: int, customerID: str, shippingID: str, dateCreated: str, dateShipped: str, status: str, customer9: "Customer" = None):
        self.OrderID = OrderID
        self.customerID = customerID
        self.shippingID = shippingID
        self.dateCreated = dateCreated
        self.dateShipped = dateShipped
        self.status = status
        self.customer9 = customer9
        
        pass
    @property
    def dateCreated(self):
        return self.__dateCreated
    @dateCreated.setter
    def dateCreated(self, dateCreated: str):
        self.__dateCreated = dateCreated

    @property
    def dateShipped(self):
        return self.__dateShipped
    @dateShipped.setter
    def dateShipped(self, dateShipped: str):
        self.__dateShipped = dateShipped

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def customerID(self):
        return self.__customerID
    @customerID.setter
    def customerID(self, customerID: str):
        self.__customerID = customerID

    @property
    def shippingID(self):
        return self.__shippingID
    @shippingID.setter
    def shippingID(self, shippingID: str):
        self.__shippingID = shippingID

    @property
    def customer9(self):
        return self.__customer9
    @customer9.setter
    def customer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer9", None)
        self.__customer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order8"):
                opp_val = getattr(old_value, "order8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order8"):
                opp_val = getattr(value, "order8", None)
                if opp_val is None:
                    setattr(value, "order8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class keyWord:

    def __init__(self, keyword: str, product6: "Product" = None):
        self.keyword = keyword
        self.product6 = product6
        
        pass
    @property
    def keyword(self):
        return self.__keyword
    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def product6(self):
        return self.__product6
    @product6.setter
    def product6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_keyWord__product6", None)
        self.__product6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keyWord7"):
                opp_val = getattr(old_value, "keyWord7", None)
                if opp_val == self:
                    setattr(old_value, "keyWord7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keyWord7"):
                opp_val = getattr(value, "keyWord7", None)
                setattr(value, "keyWord7", self)



class CartItem:

    def __init__(self, cartID: int, Name: str, ProductID: int, quantity: int, Price: str, fileName: str, subtotal: str, shoppingCart3: "ShoppingCart" = None, product5: set["Product"] = None):
        self.cartID = cartID
        self.Name = Name
        self.ProductID = ProductID
        self.quantity = quantity
        self.Price = Price
        self.fileName = fileName
        self.subtotal = subtotal
        self.shoppingCart3 = shoppingCart3
        self.product5 = product5 if product5 is not None else set()
        
        pass
    @property
    def subtotal(self):
        return self.__subtotal
    @subtotal.setter
    def subtotal(self, subtotal: str):
        self.__subtotal = subtotal

    @property
    def cartID(self):
        return self.__cartID
    @cartID.setter
    def cartID(self, cartID: int):
        self.__cartID = cartID

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def fileName(self):
        return self.__fileName
    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def shoppingCart3(self):
        return self.__shoppingCart3
    @shoppingCart3.setter
    def shoppingCart3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CartItem__shoppingCart3", None)
        self.__shoppingCart3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cartItem2"):
                opp_val = getattr(old_value, "cartItem2", None)
                if opp_val == self:
                    setattr(old_value, "cartItem2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cartItem2"):
                opp_val = getattr(value, "cartItem2", None)
                setattr(value, "cartItem2", self)

    @property
    def product5(self):
        return self.__product5
    @product5.setter
    def product5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CartItem__product5", None)
        self.__product5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cartItem4"):
                    opp_val = getattr(item, "cartItem4", None)
                    
                    if opp_val == self:
                        setattr(item, "cartItem4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cartItem4"):
                    opp_val = getattr(item, "cartItem4", None)
                    
                    setattr(item, "cartItem4", self)
                    



class Product:

    def __init__(self, ProductID: int, Name: str, Price: str, fileName: str, cardId: int, description: str, cartItem4: "CartItem" = None, keyWord7: "keyWord" = None):
        self.ProductID = ProductID
        self.Name = Name
        self.Price = Price
        self.fileName = fileName
        self.cardId = cardId
        self.description = description
        self.cartItem4 = cartItem4
        self.keyWord7 = keyWord7
        
        pass
    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def cardId(self):
        return self.__cardId
    @cardId.setter
    def cardId(self, cardId: int):
        self.__cardId = cardId

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def fileName(self):
        return self.__fileName
    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def cartItem4(self):
        return self.__cartItem4
    @cartItem4.setter
    def cartItem4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__cartItem4", None)
        self.__cartItem4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product5"):
                opp_val = getattr(old_value, "product5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product5"):
                opp_val = getattr(value, "product5", None)
                if opp_val is None:
                    setattr(value, "product5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def keyWord7(self):
        return self.__keyWord7
    @keyWord7.setter
    def keyWord7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__keyWord7", None)
        self.__keyWord7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product6"):
                opp_val = getattr(old_value, "product6", None)
                if opp_val == self:
                    setattr(old_value, "product6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product6"):
                opp_val = getattr(value, "product6", None)
                setattr(value, "product6", self)



class ShoppingCart:

    def __init__(self, cartID: int, productID: int, quantity: int, dateAdded: str, customer0: "Customer" = None, cartItem2: "CartItem" = None):
        self.cartID = cartID
        self.productID = productID
        self.quantity = quantity
        self.dateAdded = dateAdded
        self.customer0 = customer0
        self.cartItem2 = cartItem2
        
        pass
    @property
    def dateAdded(self):
        return self.__dateAdded
    @dateAdded.setter
    def dateAdded(self, dateAdded: str):
        self.__dateAdded = dateAdded

    @property
    def productID(self):
        return self.__productID
    @productID.setter
    def productID(self, productID: int):
        self.__productID = productID

    @property
    def cartID(self):
        return self.__cartID
    @cartID.setter
    def cartID(self, cartID: int):
        self.__cartID = cartID

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def cartItem2(self):
        return self.__cartItem2
    @cartItem2.setter
    def cartItem2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__cartItem2", None)
        self.__cartItem2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart3"):
                opp_val = getattr(old_value, "shoppingCart3", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart3"):
                opp_val = getattr(value, "shoppingCart3", None)
                setattr(value, "shoppingCart3", self)

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShoppingCart_Customer_11"):
                opp_val = getattr(old_value, "ShoppingCart_Customer_11", None)
                if opp_val == self:
                    setattr(old_value, "ShoppingCart_Customer_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShoppingCart_Customer_11"):
                opp_val = getattr(value, "ShoppingCart_Customer_11", None)
                setattr(value, "ShoppingCart_Customer_11", self)



class Customer:

    def __init__(self, Name: str, adress: str, email: str, phone: str, cardId: int, ShoppingCart_Customer_11: "ShoppingCart" = None, order8: set["Order"] = None):
        self.Name = Name
        self.adress = adress
        self.email = email
        self.phone = phone
        self.cardId = cardId
        self.ShoppingCart_Customer_11 = ShoppingCart_Customer_11
        self.order8 = order8 if order8 is not None else set()
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def adress(self):
        return self.__adress
    @adress.setter
    def adress(self, adress: str):
        self.__adress = adress

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def cardId(self):
        return self.__cardId
    @cardId.setter
    def cardId(self, cardId: int):
        self.__cardId = cardId

    @property
    def ShoppingCart_Customer_11(self):
        return self.__ShoppingCart_Customer_11
    @ShoppingCart_Customer_11.setter
    def ShoppingCart_Customer_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__ShoppingCart_Customer_11", None)
        self.__ShoppingCart_Customer_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer0"):
                opp_val = getattr(old_value, "customer0", None)
                if opp_val == self:
                    setattr(old_value, "customer0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer0"):
                opp_val = getattr(value, "customer0", None)
                setattr(value, "customer0", self)

    @property
    def order8(self):
        return self.__order8
    @order8.setter
    def order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order8", None)
        self.__order8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer9"):
                    opp_val = getattr(item, "customer9", None)
                    
                    if opp_val == self:
                        setattr(item, "customer9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer9"):
                    opp_val = getattr(item, "customer9", None)
                    
                    setattr(item, "customer9", self)
                    



class Product_catalog_Component:

    pass


class online_shopping_portal_Component:

    pass


class admin_portal_Component:

    pass


class online_shopping_chart_system_Component:

    pass
