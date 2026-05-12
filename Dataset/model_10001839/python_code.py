from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class AjoutProduit_UseCase:

    pass


class Webuser_Actor:

    pass


class Admin_Actor:

    pass


class MyActor_Actor:

    pass





class Customer_Support:

    def __init__(self, Email: str, Password: str, ID: int, help42: "Customer" = None):
        self.Email = Email
        self.Password = Password
        self.ID = ID
        self.help42 = help42
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

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

    @property
    def help42(self):
        return self.__help42
    @help42.setter
    def help42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Support__help42", None)
        self.__help42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ask_question43"):
                opp_val = getattr(old_value, "Ask_question43", None)
                if opp_val == self:
                    setattr(old_value, "Ask_question43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ask_question43"):
                opp_val = getattr(value, "Ask_question43", None)
                setattr(value, "Ask_question43", self)



class Shop_Owner:

    def __init__(self, Last_name: str, Name: str, Password: str, IDSowner: int, Email: str, Vendors_Administrator_036: "Administrator" = None, add_and_modify38: set["Product"] = None, Advertise44: set["Product"] = None):
        self.Last_name = Last_name
        self.Name = Name
        self.Password = Password
        self.IDSowner = IDSowner
        self.Email = Email
        self.Vendors_Administrator_036 = Vendors_Administrator_036
        self.add_and_modify38 = add_and_modify38 if add_and_modify38 is not None else set()
        self.Advertise44 = Advertise44 if Advertise44 is not None else set()
        
        pass
    @property
    def IDSowner(self):
        return self.__IDSowner
    @IDSowner.setter
    def IDSowner(self, IDSowner: int):
        self.__IDSowner = IDSowner

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
    def Last_name(self):
        return self.__Last_name
    @Last_name.setter
    def Last_name(self, Last_name: str):
        self.__Last_name = Last_name

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Vendors_Administrator_036(self):
        return self.__Vendors_Administrator_036
    @Vendors_Administrator_036.setter
    def Vendors_Administrator_036(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shop_Owner__Vendors_Administrator_036", None)
        self.__Vendors_Administrator_036 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "give_permission37"):
                opp_val = getattr(old_value, "give_permission37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "give_permission37"):
                opp_val = getattr(value, "give_permission37", None)
                if opp_val is None:
                    setattr(value, "give_permission37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def add_and_modify38(self):
        return self.__add_and_modify38
    @add_and_modify38.setter
    def add_and_modify38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shop_Owner__add_and_modify38", None)
        self.__add_and_modify38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vendors39"):
                    opp_val = getattr(item, "vendors39", None)
                    
                    if opp_val == self:
                        setattr(item, "vendors39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vendors39"):
                    opp_val = getattr(item, "vendors39", None)
                    
                    setattr(item, "vendors39", self)
                    

    @property
    def Advertise44(self):
        return self.__Advertise44
    @Advertise44.setter
    def Advertise44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shop_Owner__Advertise44", None)
        self.__Advertise44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Shop_Owner_Product_145"):
                    opp_val = getattr(item, "Shop_Owner_Product_145", None)
                    
                    if opp_val == self:
                        setattr(item, "Shop_Owner_Product_145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Shop_Owner_Product_145"):
                    opp_val = getattr(item, "Shop_Owner_Product_145", None)
                    
                    setattr(item, "Shop_Owner_Product_145", self)
                    



class Administrator:

    def __init__(self, IDAdm: int, Email: str, Password: str, Name: str, Last_name: str, Manage32: set["Customer"] = None, View_and_edit34: set["Product"] = None, give_permission37: set["Shop_Owner"] = None):
        self.IDAdm = IDAdm
        self.Email = Email
        self.Password = Password
        self.Name = Name
        self.Last_name = Last_name
        self.Manage32 = Manage32 if Manage32 is not None else set()
        self.View_and_edit34 = View_and_edit34 if View_and_edit34 is not None else set()
        self.give_permission37 = give_permission37 if give_permission37 is not None else set()
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Last_name(self):
        return self.__Last_name
    @Last_name.setter
    def Last_name(self, Last_name: str):
        self.__Last_name = Last_name

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def IDAdm(self):
        return self.__IDAdm
    @IDAdm.setter
    def IDAdm(self, IDAdm: int):
        self.__IDAdm = IDAdm

    @property
    def give_permission37(self):
        return self.__give_permission37
    @give_permission37.setter
    def give_permission37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__give_permission37", None)
        self.__give_permission37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vendors_Administrator_036"):
                    opp_val = getattr(item, "Vendors_Administrator_036", None)
                    
                    if opp_val == self:
                        setattr(item, "Vendors_Administrator_036", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vendors_Administrator_036"):
                    opp_val = getattr(item, "Vendors_Administrator_036", None)
                    
                    setattr(item, "Vendors_Administrator_036", self)
                    

    @property
    def Manage32(self):
        return self.__Manage32
    @Manage32.setter
    def Manage32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__Manage32", None)
        self.__Manage32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Administrator_Customer_133"):
                    opp_val = getattr(item, "Administrator_Customer_133", None)
                    
                    if opp_val == self:
                        setattr(item, "Administrator_Customer_133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Administrator_Customer_133"):
                    opp_val = getattr(item, "Administrator_Customer_133", None)
                    
                    setattr(item, "Administrator_Customer_133", self)
                    

    @property
    def View_and_edit34(self):
        return self.__View_and_edit34
    @View_and_edit34.setter
    def View_and_edit34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__View_and_edit34", None)
        self.__View_and_edit34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "administrator35"):
                    opp_val = getattr(item, "administrator35", None)
                    
                    if opp_val == self:
                        setattr(item, "administrator35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "administrator35"):
                    opp_val = getattr(item, "administrator35", None)
                    
                    setattr(item, "administrator35", self)
                    



class Product:

    def __init__(self, name: str, description: str, visitor31: "Visitor" = None, administrator35: "Administrator" = None, vendors39: "Shop_Owner" = None, item7: set["LineItem"] = None, Shop_Owner_Product_145: "Shop_Owner" = None, account22: "Account" = None, Add_to_cart24: "ShoppingCart" = None):
        self.name = name
        self.description = description
        self.visitor31 = visitor31
        self.administrator35 = administrator35
        self.vendors39 = vendors39
        self.item7 = item7 if item7 is not None else set()
        self.Shop_Owner_Product_145 = Shop_Owner_Product_145
        self.account22 = account22
        self.Add_to_cart24 = Add_to_cart24
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def item7(self):
        return self.__item7
    @item7.setter
    def item7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__item7", None)
        self.__item7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product6"):
                    opp_val = getattr(item, "product6", None)
                    
                    if opp_val == self:
                        setattr(item, "product6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product6"):
                    opp_val = getattr(item, "product6", None)
                    
                    setattr(item, "product6", self)
                    

    @property
    def visitor31(self):
        return self.__visitor31
    @visitor31.setter
    def visitor31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__visitor31", None)
        self.__visitor31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "view_products30"):
                opp_val = getattr(old_value, "view_products30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "view_products30"):
                opp_val = getattr(value, "view_products30", None)
                if opp_val is None:
                    setattr(value, "view_products30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Shop_Owner_Product_145(self):
        return self.__Shop_Owner_Product_145
    @Shop_Owner_Product_145.setter
    def Shop_Owner_Product_145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__Shop_Owner_Product_145", None)
        self.__Shop_Owner_Product_145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Advertise44"):
                opp_val = getattr(old_value, "Advertise44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Advertise44"):
                opp_val = getattr(value, "Advertise44", None)
                if opp_val is None:
                    setattr(value, "Advertise44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vendors39(self):
        return self.__vendors39
    @vendors39.setter
    def vendors39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__vendors39", None)
        self.__vendors39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "add_and_modify38"):
                opp_val = getattr(old_value, "add_and_modify38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "add_and_modify38"):
                opp_val = getattr(value, "add_and_modify38", None)
                if opp_val is None:
                    setattr(value, "add_and_modify38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Add_to_cart24(self):
        return self.__Add_to_cart24
    @Add_to_cart24.setter
    def Add_to_cart24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__Add_to_cart24", None)
        self.__Add_to_cart24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product25"):
                opp_val = getattr(old_value, "product25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product25"):
                opp_val = getattr(value, "product25", None)
                if opp_val is None:
                    setattr(value, "product25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def account22(self):
        return self.__account22
    @account22.setter
    def account22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__account22", None)
        self.__account22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product23"):
                opp_val = getattr(old_value, "product23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product23"):
                opp_val = getattr(value, "product23", None)
                if opp_val is None:
                    setattr(value, "product23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def administrator35(self):
        return self.__administrator35
    @administrator35.setter
    def administrator35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__administrator35", None)
        self.__administrator35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "View_and_edit34"):
                opp_val = getattr(old_value, "View_and_edit34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "View_and_edit34"):
                opp_val = getattr(value, "View_and_edit34", None)
                if opp_val is None:
                    setattr(value, "View_and_edit34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class LineItem:

    def __init__(self, quantity: int, price: float, shopping_cart3: "ShoppingCart" = None, product6: "Product" = None, order15: "Order" = None):
        self.quantity = quantity
        self.price = price
        self.shopping_cart3 = shopping_cart3
        self.product6 = product6
        self.order15 = order15
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def product6(self):
        return self.__product6
    @product6.setter
    def product6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__product6", None)
        self.__product6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "item7"):
                opp_val = getattr(old_value, "item7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "item7"):
                opp_val = getattr(value, "item7", None)
                if opp_val is None:
                    setattr(value, "item7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shopping_cart3(self):
        return self.__shopping_cart3
    @shopping_cart3.setter
    def shopping_cart3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__shopping_cart3", None)
        self.__shopping_cart3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items2"):
                opp_val = getattr(old_value, "items2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items2"):
                opp_val = getattr(value, "items2", None)
                if opp_val is None:
                    setattr(value, "items2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order15(self):
        return self.__order15
    @order15.setter
    def order15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__order15", None)
        self.__order15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items14"):
                opp_val = getattr(old_value, "items14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items14"):
                opp_val = getattr(value, "items14", None)
                if opp_val is None:
                    setattr(value, "items14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Order:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: str, items14: set["LineItem"] = None, accnt17: "Account" = None, payment21: "Payment" = None, shoppingCart27: "ShoppingCart" = None):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        self.items14 = items14 if items14 is not None else set()
        self.accnt17 = accnt17
        self.payment21 = payment21
        self.shoppingCart27 = shoppingCart27
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def shoppingCart27(self):
        return self.__shoppingCart27
    @shoppingCart27.setter
    def shoppingCart27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__shoppingCart27", None)
        self.__shoppingCart27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order26"):
                opp_val = getattr(old_value, "order26", None)
                if opp_val == self:
                    setattr(old_value, "order26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order26"):
                opp_val = getattr(value, "order26", None)
                setattr(value, "order26", self)

    @property
    def payment21(self):
        return self.__payment21
    @payment21.setter
    def payment21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment21", None)
        self.__payment21 = value
        
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
    def items14(self):
        return self.__items14
    @items14.setter
    def items14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__items14", None)
        self.__items14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order15"):
                    opp_val = getattr(item, "order15", None)
                    
                    if opp_val == self:
                        setattr(item, "order15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order15"):
                    opp_val = getattr(item, "order15", None)
                    
                    setattr(item, "order15", self)
                    

    @property
    def accnt17(self):
        return self.__accnt17
    @accnt17.setter
    def accnt17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__accnt17", None)
        self.__accnt17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order16"):
                opp_val = getattr(old_value, "order16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order16"):
                opp_val = getattr(value, "order16", None)
                if opp_val is None:
                    setattr(value, "order16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Visitor:

    pass


class Account:

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, cart4: "ShoppingCart" = None, Giving_feedback40: "ShoppingCart" = None, customer13: "Customer" = None, order16: set["Order"] = None, payment18: set["Payment"] = None, product23: set["Product"] = None, payment29: "Payment" = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.cart4 = cart4
        self.Giving_feedback40 = Giving_feedback40
        self.customer13 = customer13
        self.order16 = order16 if order16 is not None else set()
        self.payment18 = payment18 if payment18 is not None else set()
        self.product23 = product23 if product23 is not None else set()
        self.payment29 = payment29
        
        pass
    @property
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

    @property
    def isClosed(self):
        return self.__isClosed
    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def billingAddress(self):
        return self.__billingAddress
    @billingAddress.setter
    def billingAddress(self, billingAddress: str):
        self.__billingAddress = billingAddress

    @property
    def open(self):
        return self.__open
    @open.setter
    def open(self, open: date):
        self.__open = open

    @property
    def cart4(self):
        return self.__cart4
    @cart4.setter
    def cart4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__cart4", None)
        self.__cart4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account5"):
                opp_val = getattr(old_value, "account5", None)
                if opp_val == self:
                    setattr(old_value, "account5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account5"):
                opp_val = getattr(value, "account5", None)
                setattr(value, "account5", self)

    @property
    def order16(self):
        return self.__order16
    @order16.setter
    def order16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order16", None)
        self.__order16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accnt17"):
                    opp_val = getattr(item, "accnt17", None)
                    
                    if opp_val == self:
                        setattr(item, "accnt17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accnt17"):
                    opp_val = getattr(item, "accnt17", None)
                    
                    setattr(item, "accnt17", self)
                    

    @property
    def customer13(self):
        return self.__customer13
    @customer13.setter
    def customer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer13", None)
        self.__customer13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has12"):
                opp_val = getattr(old_value, "has12", None)
                if opp_val == self:
                    setattr(old_value, "has12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has12"):
                opp_val = getattr(value, "has12", None)
                setattr(value, "has12", self)

    @property
    def payment18(self):
        return self.__payment18
    @payment18.setter
    def payment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__payment18", None)
        self.__payment18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account19"):
                    opp_val = getattr(item, "account19", None)
                    
                    if opp_val == self:
                        setattr(item, "account19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account19"):
                    opp_val = getattr(item, "account19", None)
                    
                    setattr(item, "account19", self)
                    

    @property
    def payment29(self):
        return self.__payment29
    @payment29.setter
    def payment29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__payment29", None)
        self.__payment29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account28"):
                opp_val = getattr(old_value, "account28", None)
                if opp_val == self:
                    setattr(old_value, "account28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account28"):
                opp_val = getattr(value, "account28", None)
                setattr(value, "account28", self)

    @property
    def Giving_feedback40(self):
        return self.__Giving_feedback40
    @Giving_feedback40.setter
    def Giving_feedback40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__Giving_feedback40", None)
        self.__Giving_feedback40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Account_ShoppingCart2_141"):
                opp_val = getattr(old_value, "Account_ShoppingCart2_141", None)
                if opp_val == self:
                    setattr(old_value, "Account_ShoppingCart2_141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Account_ShoppingCart2_141"):
                opp_val = getattr(value, "Account_ShoppingCart2_141", None)
                setattr(value, "Account_ShoppingCart2_141", self)

    @property
    def product23(self):
        return self.__product23
    @product23.setter
    def product23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__product23", None)
        self.__product23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account22"):
                    opp_val = getattr(item, "account22", None)
                    
                    if opp_val == self:
                        setattr(item, "account22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account22"):
                    opp_val = getattr(item, "account22", None)
                    
                    setattr(item, "account22", self)
                    



class ShoppingCart:

    def __init__(self, creationDate: date, items2: set["LineItem"] = None, account5: "Account" = None, Account_ShoppingCart2_141: "Account" = None, webUser9: "Visitor" = None, product25: set["Product"] = None, order26: "Order" = None):
        self.creationDate = creationDate
        self.items2 = items2 if items2 is not None else set()
        self.account5 = account5
        self.Account_ShoppingCart2_141 = Account_ShoppingCart2_141
        self.webUser9 = webUser9
        self.product25 = product25 if product25 is not None else set()
        self.order26 = order26
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def Account_ShoppingCart2_141(self):
        return self.__Account_ShoppingCart2_141
    @Account_ShoppingCart2_141.setter
    def Account_ShoppingCart2_141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__Account_ShoppingCart2_141", None)
        self.__Account_ShoppingCart2_141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Giving_feedback40"):
                opp_val = getattr(old_value, "Giving_feedback40", None)
                if opp_val == self:
                    setattr(old_value, "Giving_feedback40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Giving_feedback40"):
                opp_val = getattr(value, "Giving_feedback40", None)
                setattr(value, "Giving_feedback40", self)

    @property
    def product25(self):
        return self.__product25
    @product25.setter
    def product25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__product25", None)
        self.__product25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Add_to_cart24"):
                    opp_val = getattr(item, "Add_to_cart24", None)
                    
                    if opp_val == self:
                        setattr(item, "Add_to_cart24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Add_to_cart24"):
                    opp_val = getattr(item, "Add_to_cart24", None)
                    
                    setattr(item, "Add_to_cart24", self)
                    

    @property
    def order26(self):
        return self.__order26
    @order26.setter
    def order26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__order26", None)
        self.__order26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart27"):
                opp_val = getattr(old_value, "shoppingCart27", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart27"):
                opp_val = getattr(value, "shoppingCart27", None)
                setattr(value, "shoppingCart27", self)

    @property
    def webUser9(self):
        return self.__webUser9
    @webUser9.setter
    def webUser9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__webUser9", None)
        self.__webUser9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart8"):
                opp_val = getattr(old_value, "shoppingCart8", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart8"):
                opp_val = getattr(value, "shoppingCart8", None)
                setattr(value, "shoppingCart8", self)

    @property
    def items2(self):
        return self.__items2
    @items2.setter
    def items2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__items2", None)
        self.__items2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shopping_cart3"):
                    opp_val = getattr(item, "shopping_cart3", None)
                    
                    if opp_val == self:
                        setattr(item, "shopping_cart3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shopping_cart3"):
                    opp_val = getattr(item, "shopping_cart3", None)
                    
                    setattr(item, "shopping_cart3", self)
                    

    @property
    def account5(self):
        return self.__account5
    @account5.setter
    def account5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ShoppingCart__account5", None)
        self.__account5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart4"):
                opp_val = getattr(old_value, "cart4", None)
                if opp_val == self:
                    setattr(old_value, "cart4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart4"):
                opp_val = getattr(value, "cart4", None)
                setattr(value, "cart4", self)



class Payment:

    def __init__(self, paidDate: date, total: float, details: str, account19: "Account" = None, order20: "Order" = None, account28: "Account" = None):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        self.account19 = account19
        self.order20 = order20
        self.account28 = account28
        
        pass
    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def paidDate(self):
        return self.__paidDate
    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def account28(self):
        return self.__account28
    @account28.setter
    def account28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__account28", None)
        self.__account28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment29"):
                opp_val = getattr(old_value, "payment29", None)
                if opp_val == self:
                    setattr(old_value, "payment29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment29"):
                opp_val = getattr(value, "payment29", None)
                setattr(value, "payment29", self)

    @property
    def order20(self):
        return self.__order20
    @order20.setter
    def order20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order20", None)
        self.__order20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment21"):
                opp_val = getattr(old_value, "payment21", None)
                if opp_val == self:
                    setattr(old_value, "payment21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment21"):
                opp_val = getattr(value, "payment21", None)
                setattr(value, "payment21", self)

    @property
    def account19(self):
        return self.__account19
    @account19.setter
    def account19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__account19", None)
        self.__account19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment18"):
                opp_val = getattr(old_value, "payment18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment18"):
                opp_val = getattr(value, "payment18", None)
                if opp_val is None:
                    setattr(value, "payment18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Customer:

    def __init__(self, IDCust: int, Last_name: str, Name: str, Password: str, Email: str, Administrator_Customer_133: "Administrator" = None, Ask_question43: "Customer_Support" = None, webUser11: "Visitor" = None, has12: "Account" = None):
        self.IDCust = IDCust
        self.Last_name = Last_name
        self.Name = Name
        self.Password = Password
        self.Email = Email
        self.Administrator_Customer_133 = Administrator_Customer_133
        self.Ask_question43 = Ask_question43
        self.webUser11 = webUser11
        self.has12 = has12
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Last_name(self):
        return self.__Last_name
    @Last_name.setter
    def Last_name(self, Last_name: str):
        self.__Last_name = Last_name

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def IDCust(self):
        return self.__IDCust
    @IDCust.setter
    def IDCust(self, IDCust: int):
        self.__IDCust = IDCust

    @property
    def has12(self):
        return self.__has12
    @has12.setter
    def has12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__has12", None)
        self.__has12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer13"):
                opp_val = getattr(old_value, "customer13", None)
                if opp_val == self:
                    setattr(old_value, "customer13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer13"):
                opp_val = getattr(value, "customer13", None)
                setattr(value, "customer13", self)

    @property
    def Administrator_Customer_133(self):
        return self.__Administrator_Customer_133
    @Administrator_Customer_133.setter
    def Administrator_Customer_133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Administrator_Customer_133", None)
        self.__Administrator_Customer_133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Manage32"):
                opp_val = getattr(old_value, "Manage32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Manage32"):
                opp_val = getattr(value, "Manage32", None)
                if opp_val is None:
                    setattr(value, "Manage32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Ask_question43(self):
        return self.__Ask_question43
    @Ask_question43.setter
    def Ask_question43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Ask_question43", None)
        self.__Ask_question43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "help42"):
                opp_val = getattr(old_value, "help42", None)
                if opp_val == self:
                    setattr(old_value, "help42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "help42"):
                opp_val = getattr(value, "help42", None)
                setattr(value, "help42", self)

    @property
    def webUser11(self):
        return self.__webUser11
    @webUser11.setter
    def webUser11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__webUser11", None)
        self.__webUser11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer10"):
                opp_val = getattr(old_value, "customer10", None)
                if opp_val == self:
                    setattr(old_value, "customer10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer10"):
                opp_val = getattr(value, "customer10", None)
                setattr(value, "customer10", self)

