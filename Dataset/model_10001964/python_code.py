from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class MAINTAINS_THE_PRODUCTS_SERVICES_UseCase:

    pass


class ADMINISTRATOR_Actor:

    pass


class WEB_DEVELOPER_Actor:

    pass


class SUPPORT_AND_FEEDBACK_UseCase:

    pass


class DELIVERS_THE_PRODUCT_UseCase:

    pass


class PAYS_THE_BILL_UseCase:

    pass


class SELECTS_THE_MODE_OF_PAYMENT_UseCase:

    pass


class ADDS_ITEMS_SERVICE_TO_CART_UseCase:

    pass


class SELECTS_THE_ITEMS_SERVICE_UseCase:

    pass


class CREATES_THE_WEBSITE_UseCase:

    pass


class VISITS_THE_WEBSITE_UseCase:

    pass


class CUSTOMER_Actor:

    pass





class Feedback:

    def __init__(self, customername: str, id: int, phoneno: int):
        self.customername = customername
        self.id = id
        self.phoneno = phoneno
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def customername(self):
        return self.__customername
    @customername.setter
    def customername(self, customername: str):
        self.__customername = customername

    @property
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno



class Customercare:

    def __init__(self, no: int, address: str, customer25: set["Customer"] = None):
        self.no = no
        self.address = address
        self.customer25 = customer25 if customer25 is not None else set()
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def customer25(self):
        return self.__customer25
    @customer25.setter
    def customer25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customercare__customer25", None)
        self.__customer25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customercare24"):
                    opp_val = getattr(item, "customercare24", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customercare24"):
                    opp_val = getattr(item, "customercare24", None)
                    
                    if opp_val is None:
                        setattr(item, "customercare24", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class services:

    def __init__(self, database: str, location: str, product27: set["company"] = None):
        self.database = database
        self.location = location
        self.product27 = product27 if product27 is not None else set()
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def database(self):
        return self.__database
    @database.setter
    def database(self, database: str):
        self.__database = database

    @property
    def product27(self):
        return self.__product27
    @product27.setter
    def product27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_services__product27", None)
        self.__product27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "warehouse26"):
                    opp_val = getattr(item, "warehouse26", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "warehouse26"):
                    opp_val = getattr(item, "warehouse26", None)
                    
                    if opp_val is None:
                        setattr(item, "warehouse26", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class company:

    def __init__(self, name: str, id: int, type: str, warehouse26: set["services"] = None, customer29: set["Customer"] = None):
        self.name = name
        self.id = id
        self.type = type
        self.warehouse26 = warehouse26 if warehouse26 is not None else set()
        self.customer29 = customer29 if customer29 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def customer29(self):
        return self.__customer29
    @customer29.setter
    def customer29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company__customer29", None)
        self.__customer29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company28"):
                    opp_val = getattr(item, "company28", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company28"):
                    opp_val = getattr(item, "company28", None)
                    
                    if opp_val is None:
                        setattr(item, "company28", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def warehouse26(self):
        return self.__warehouse26
    @warehouse26.setter
    def warehouse26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company__warehouse26", None)
        self.__warehouse26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product27"):
                    opp_val = getattr(item, "product27", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product27"):
                    opp_val = getattr(item, "product27", None)
                    
                    if opp_val is None:
                        setattr(item, "product27", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Customer:

    def __init__(self, name: str, id: int, mailid: str, address: str, phoneno: int, customercare24: set["Customercare"] = None, company28: set["company"] = None):
        self.name = name
        self.id = id
        self.mailid = mailid
        self.address = address
        self.phoneno = phoneno
        self.customercare24 = customercare24 if customercare24 is not None else set()
        self.company28 = company28 if company28 is not None else set()
        
        pass
    @property
    def phoneno(self):
        return self.__phoneno
    @phoneno.setter
    def phoneno(self, phoneno: int):
        self.__phoneno = phoneno

    @property
    def mailid(self):
        return self.__mailid
    @mailid.setter
    def mailid(self, mailid: str):
        self.__mailid = mailid

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def company28(self):
        return self.__company28
    @company28.setter
    def company28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__company28", None)
        self.__company28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer29"):
                    opp_val = getattr(item, "customer29", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer29"):
                    opp_val = getattr(item, "customer29", None)
                    
                    if opp_val is None:
                        setattr(item, "customer29", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def customercare24(self):
        return self.__customercare24
    @customercare24.setter
    def customercare24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__customercare24", None)
        self.__customercare24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer25"):
                    opp_val = getattr(item, "customer25", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer25"):
                    opp_val = getattr(item, "customer25", None)
                    
                    if opp_val is None:
                        setattr(item, "customer25", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

