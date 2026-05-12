from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Person:

    def __init__(self, Name: str, Surname: str, Email: str, Address: str, order1: set["Order"] = None, user9: "User" = None):
        self.Name = Name
        self.Surname = Surname
        self.Email = Email
        self.Address = Address
        self.order1 = order1 if order1 is not None else set()
        self.user9 = user9
        
        pass
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
    def Surname(self):
        return self.__Surname
    @Surname.setter
    def Surname(self, Surname: str):
        self.__Surname = Surname

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def order1(self):
        return self.__order1
    @order1.setter
    def order1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__order1", None)
        self.__order1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "person0"):
                    opp_val = getattr(item, "person0", None)
                    
                    if opp_val == self:
                        setattr(item, "person0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "person0"):
                    opp_val = getattr(item, "person0", None)
                    
                    setattr(item, "person0", self)
                    

    @property
    def user9(self):
        return self.__user9
    @user9.setter
    def user9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__user9", None)
        self.__user9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person8"):
                opp_val = getattr(old_value, "person8", None)
                if opp_val == self:
                    setattr(old_value, "person8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person8"):
                opp_val = getattr(value, "person8", None)
                setattr(value, "person8", self)



class User:

    def __init__(self, UserID: int, UserName: str, Password: str, person8: "Person" = None):
        self.UserID = UserID
        self.UserName = UserName
        self.Password = Password
        self.person8 = person8
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

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
    def person8(self):
        return self.__person8
    @person8.setter
    def person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__person8", None)
        self.__person8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user9"):
                opp_val = getattr(old_value, "user9", None)
                if opp_val == self:
                    setattr(old_value, "user9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user9"):
                opp_val = getattr(value, "user9", None)
                setattr(value, "user9", self)



class Order:

    def __init__(self, OrderID: int, Date: str, Customer: Person, items: Shopping_cart, person0: "Person" = None, shopping_cart2: "Shopping_cart" = None):
        self.OrderID = OrderID
        self.Date = Date
        self.Customer = Customer
        self.items = items
        self.person0 = person0
        self.shopping_cart2 = shopping_cart2
        
        pass
    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self, items: Shopping_cart):
        self.__items = items

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def Customer(self):
        return self.__Customer
    @Customer.setter
    def Customer(self, Customer: Person):
        self.__Customer = Customer

    @property
    def shopping_cart2(self):
        return self.__shopping_cart2
    @shopping_cart2.setter
    def shopping_cart2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__shopping_cart2", None)
        self.__shopping_cart2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order3"):
                opp_val = getattr(old_value, "order3", None)
                if opp_val == self:
                    setattr(old_value, "order3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order3"):
                opp_val = getattr(value, "order3", None)
                setattr(value, "order3", self)

    @property
    def person0(self):
        return self.__person0
    @person0.setter
    def person0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__person0", None)
        self.__person0 = value
        
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



class Stock:

    def __init__(self, Items: str, product4: set["Product"] = None):
        self.Items = Items
        self.product4 = product4 if product4 is not None else set()
        
        pass
    @property
    def Items(self):
        return self.__Items
    @Items.setter
    def Items(self, Items: str):
        self.__Items = Items

    @property
    def product4(self):
        return self.__product4
    @product4.setter
    def product4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stock__product4", None)
        self.__product4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stock5"):
                    opp_val = getattr(item, "stock5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stock5"):
                    opp_val = getattr(item, "stock5", None)
                    
                    if opp_val is None:
                        setattr(item, "stock5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Shopping_cart:

    def __init__(self, Products: str, order3: "Order" = None, product6: set["Product"] = None):
        self.Products = Products
        self.order3 = order3
        self.product6 = product6 if product6 is not None else set()
        
        pass
    @property
    def Products(self):
        return self.__Products
    @Products.setter
    def Products(self, Products: str):
        self.__Products = Products

    @property
    def product6(self):
        return self.__product6
    @product6.setter
    def product6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_cart__product6", None)
        self.__product6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shopping_cart7"):
                    opp_val = getattr(item, "shopping_cart7", None)
                    
                    if opp_val == self:
                        setattr(item, "shopping_cart7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shopping_cart7"):
                    opp_val = getattr(item, "shopping_cart7", None)
                    
                    setattr(item, "shopping_cart7", self)
                    

    @property
    def order3(self):
        return self.__order3
    @order3.setter
    def order3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_cart__order3", None)
        self.__order3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_cart2"):
                opp_val = getattr(old_value, "shopping_cart2", None)
                if opp_val == self:
                    setattr(old_value, "shopping_cart2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_cart2"):
                opp_val = getattr(value, "shopping_cart2", None)
                setattr(value, "shopping_cart2", self)



class Product:

    def __init__(self, ProductID: int, name: str, description: str, price: int, quantity: int, stock5: set["Stock"] = None, shopping_cart7: "Shopping_cart" = None):
        self.ProductID = ProductID
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.stock5 = stock5 if stock5 is not None else set()
        self.shopping_cart7 = shopping_cart7
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, ProductID: int):
        self.__ProductID = ProductID

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def shopping_cart7(self):
        return self.__shopping_cart7
    @shopping_cart7.setter
    def shopping_cart7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__shopping_cart7", None)
        self.__shopping_cart7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product6"):
                opp_val = getattr(old_value, "product6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product6"):
                opp_val = getattr(value, "product6", None)
                if opp_val is None:
                    setattr(value, "product6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stock5(self):
        return self.__stock5
    @stock5.setter
    def stock5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__stock5", None)
        self.__stock5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product4"):
                    opp_val = getattr(item, "product4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product4"):
                    opp_val = getattr(item, "product4", None)
                    
                    if opp_val is None:
                        setattr(item, "product4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

