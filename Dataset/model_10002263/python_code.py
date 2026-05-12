from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class NO_Queue_mobile_application__NOQueue:

    def __init__(self, APP_Details: str):
        self.APP_Details = APP_Details
        
        pass
    @property
    def APP_Details(self):
        return self.__APP_Details
    @APP_Details.setter
    def APP_Details(self, APP_Details: str):
        self.__APP_Details = APP_Details



class NO_Queue_mobile_application__Product:

    def __init__(self, ID: str, Name: str, Supplier: str, line_item15: set["NO_Queue_mobile_application__Line_item"] = None):
        self.ID = ID
        self.Name = Name
        self.Supplier = Supplier
        self.line_item15 = line_item15 if line_item15 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Supplier(self):
        return self.__Supplier
    @Supplier.setter
    def Supplier(self, Supplier: str):
        self.__Supplier = Supplier

    @property
    def line_item15(self):
        return self.__line_item15
    @line_item15.setter
    def line_item15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Product__line_item15", None)
        self.__line_item15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product14"):
                    opp_val = getattr(item, "product14", None)
                    
                    if opp_val == self:
                        setattr(item, "product14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product14"):
                    opp_val = getattr(item, "product14", None)
                    
                    setattr(item, "product14", self)
                    



class NO_Queue_mobile_application__Line_item:

    def __init__(self, quantity: int, price: str, shopping_Cart11: "NO_Queue_mobile_application__Shopping_Cart" = None, _order__unique_13: "NO_Queue_mobile_application__Order" = None, product14: "NO_Queue_mobile_application__Product" = None):
        self.quantity = quantity
        self.price = price
        self.shopping_Cart11 = shopping_Cart11
        self._order__unique_13 = _order__unique_13
        self.product14 = product14
        
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
    def price(self, price: str):
        self.__price = price

    @property
    def shopping_Cart11(self):
        return self.__shopping_Cart11
    @shopping_Cart11.setter
    def shopping_Cart11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Line_item__shopping_Cart11", None)
        self.__shopping_Cart11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordered__unique10"):
                opp_val = getattr(old_value, "ordered__unique10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordered__unique10"):
                opp_val = getattr(value, "ordered__unique10", None)
                if opp_val is None:
                    setattr(value, "ordered__unique10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product14(self):
        return self.__product14
    @product14.setter
    def product14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Line_item__product14", None)
        self.__product14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "line_item15"):
                opp_val = getattr(old_value, "line_item15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "line_item15"):
                opp_val = getattr(value, "line_item15", None)
                if opp_val is None:
                    setattr(value, "line_item15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def _order__unique_13(self):
        return self.___order__unique_13
    @_order__unique_13.setter
    def _order__unique_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Line_item___order__unique_13", None)
        self.___order__unique_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "line_item12"):
                opp_val = getattr(old_value, "line_item12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "line_item12"):
                opp_val = getattr(value, "line_item12", None)
                if opp_val is None:
                    setattr(value, "line_item12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class NO_Queue_mobile_application__Shopping_Cart:

    def __init__(self, created: str, web_User7: "NO_Queue_mobile_application__App_User" = None, ordered__unique10: set["NO_Queue_mobile_application__Line_item"] = None):
        self.created = created
        self.web_User7 = web_User7
        self.ordered__unique10 = ordered__unique10 if ordered__unique10 is not None else set()
        
        pass
    @property
    def created(self):
        return self.__created
    @created.setter
    def created(self, created: str):
        self.__created = created

    @property
    def ordered__unique10(self):
        return self.__ordered__unique10
    @ordered__unique10.setter
    def ordered__unique10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Shopping_Cart__ordered__unique10", None)
        self.__ordered__unique10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shopping_Cart11"):
                    opp_val = getattr(item, "shopping_Cart11", None)
                    
                    if opp_val == self:
                        setattr(item, "shopping_Cart11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shopping_Cart11"):
                    opp_val = getattr(item, "shopping_Cart11", None)
                    
                    setattr(item, "shopping_Cart11", self)
                    

    @property
    def web_User7(self):
        return self.__web_User7
    @web_User7.setter
    def web_User7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Shopping_Cart__web_User7", None)
        self.__web_User7 = value
        
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



class NO_Queue_mobile_application__Order:

    def __init__(self, Number: str, ordered: str, shipped: str, Ship_to: str, status: str, total: str, account9: "NO_Queue_mobile_application__Account" = None, line_item12: set["NO_Queue_mobile_application__Line_item"] = None):
        self.Number = Number
        self.ordered = ordered
        self.shipped = shipped
        self.Ship_to = Ship_to
        self.status = status
        self.total = total
        self.account9 = account9
        self.line_item12 = line_item12 if line_item12 is not None else set()
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: str):
        self.__total = total

    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: str):
        self.__ordered = ordered

    @property
    def Number(self):
        return self.__Number
    @Number.setter
    def Number(self, Number: str):
        self.__Number = Number

    @property
    def Ship_to(self):
        return self.__Ship_to
    @Ship_to.setter
    def Ship_to(self, Ship_to: str):
        self.__Ship_to = Ship_to

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: str):
        self.__shipped = shipped

    @property
    def line_item12(self):
        return self.__line_item12
    @line_item12.setter
    def line_item12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Order__line_item12", None)
        self.__line_item12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_order__unique_13"):
                    opp_val = getattr(item, "_order__unique_13", None)
                    
                    if opp_val == self:
                        setattr(item, "_order__unique_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_order__unique_13"):
                    opp_val = getattr(item, "_order__unique_13", None)
                    
                    setattr(item, "_order__unique_13", self)
                    

    @property
    def account9(self):
        return self.__account9
    @account9.setter
    def account9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Order__account9", None)
        self.__account9 = value
        
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



class NO_Queue_mobile_application__Payment:

    def __init__(self, ID: str, Paid: str, Total: str, Details: str, account4: "NO_Queue_mobile_application__Account" = None):
        self.ID = ID
        self.Paid = Paid
        self.Total = Total
        self.Details = Details
        self.account4 = account4
        
        pass
    @property
    def Paid(self):
        return self.__Paid
    @Paid.setter
    def Paid(self, Paid: str):
        self.__Paid = Paid

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Total(self):
        return self.__Total
    @Total.setter
    def Total(self, Total: str):
        self.__Total = Total

    @property
    def Details(self):
        return self.__Details
    @Details.setter
    def Details(self, Details: str):
        self.__Details = Details

    @property
    def account4(self):
        return self.__account4
    @account4.setter
    def account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Payment__account4", None)
        self.__account4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment5"):
                opp_val = getattr(old_value, "payment5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment5"):
                opp_val = getattr(value, "payment5", None)
                if opp_val is None:
                    setattr(value, "payment5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class NO_Queue_mobile_application__Account:

    def __init__(self, ID: str, billing_address: str, is_closed: bool, Open: str, Closed: str, customer3: "NO_Queue_mobile_application__Customer" = None, payment5: set["NO_Queue_mobile_application__Payment"] = None, order8: set["NO_Queue_mobile_application__Order"] = None):
        self.ID = ID
        self.billing_address = billing_address
        self.is_closed = is_closed
        self.Open = Open
        self.Closed = Closed
        self.customer3 = customer3
        self.payment5 = payment5 if payment5 is not None else set()
        self.order8 = order8 if order8 is not None else set()
        
        pass
    @property
    def is_closed(self):
        return self.__is_closed
    @is_closed.setter
    def is_closed(self, is_closed: bool):
        self.__is_closed = is_closed

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Closed(self):
        return self.__Closed
    @Closed.setter
    def Closed(self, Closed: str):
        self.__Closed = Closed

    @property
    def billing_address(self):
        return self.__billing_address
    @billing_address.setter
    def billing_address(self, billing_address: str):
        self.__billing_address = billing_address

    @property
    def Open(self):
        return self.__Open
    @Open.setter
    def Open(self, Open: str):
        self.__Open = Open

    @property
    def payment5(self):
        return self.__payment5
    @payment5.setter
    def payment5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Account__payment5", None)
        self.__payment5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account4"):
                    opp_val = getattr(item, "account4", None)
                    
                    if opp_val == self:
                        setattr(item, "account4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account4"):
                    opp_val = getattr(item, "account4", None)
                    
                    setattr(item, "account4", self)
                    

    @property
    def order8(self):
        return self.__order8
    @order8.setter
    def order8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Account__order8", None)
        self.__order8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account9"):
                    opp_val = getattr(item, "account9", None)
                    
                    if opp_val == self:
                        setattr(item, "account9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account9"):
                    opp_val = getattr(item, "account9", None)
                    
                    setattr(item, "account9", self)
                    

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Account__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account2"):
                opp_val = getattr(old_value, "account2", None)
                if opp_val == self:
                    setattr(old_value, "account2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account2"):
                opp_val = getattr(value, "account2", None)
                setattr(value, "account2", self)



class NO_Queue_mobile_application__Customer:

    def __init__(self, ID: str, Address: str, Phone: str, Email: str, web_User1: "NO_Queue_mobile_application__App_User" = None, account2: "NO_Queue_mobile_application__Account" = None):
        self.ID = ID
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.web_User1 = web_User1
        self.account2 = account2
        
        pass
    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def web_User1(self):
        return self.__web_User1
    @web_User1.setter
    def web_User1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Customer__web_User1", None)
        self.__web_User1 = value
        
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
    def account2(self):
        return self.__account2
    @account2.setter
    def account2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__Customer__account2", None)
        self.__account2 = value
        
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



class NO_Queue_mobile_application__App_User:

    def __init__(self, login_id: str, passwd: str, customer0: "NO_Queue_mobile_application__Customer" = None, shopping_Cart6: "NO_Queue_mobile_application__Shopping_Cart" = None):
        self.login_id = login_id
        self.passwd = passwd
        self.customer0 = customer0
        self.shopping_Cart6 = shopping_Cart6
        
        pass
    @property
    def passwd(self):
        return self.__passwd
    @passwd.setter
    def passwd(self, passwd: str):
        self.__passwd = passwd

    @property
    def login_id(self):
        return self.__login_id
    @login_id.setter
    def login_id(self, login_id: str):
        self.__login_id = login_id

    @property
    def shopping_Cart6(self):
        return self.__shopping_Cart6
    @shopping_Cart6.setter
    def shopping_Cart6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__App_User__shopping_Cart6", None)
        self.__shopping_Cart6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_User7"):
                opp_val = getattr(old_value, "web_User7", None)
                if opp_val == self:
                    setattr(old_value, "web_User7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_User7"):
                opp_val = getattr(value, "web_User7", None)
                setattr(value, "web_User7", self)

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_NO_Queue_mobile_application__App_User__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_User1"):
                opp_val = getattr(old_value, "web_User1", None)
                if opp_val == self:
                    setattr(old_value, "web_User1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_User1"):
                opp_val = getattr(value, "web_User1", None)
                setattr(value, "web_User1", self)

