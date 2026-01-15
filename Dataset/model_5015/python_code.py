from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class schemaprimerpo_USAddress:

    def __init__(self, name: str, street: str, city: str, state: str, zip: str, country: str, schemaprimerpo_USAddress: "schemaprimerpo_PurchaseOrder" = None, schemaprimerpo_USAddress10: "schemaprimerpo_PurchaseOrder" = None):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.schemaprimerpo_USAddress = schemaprimerpo_USAddress
        self.schemaprimerpo_USAddress10 = schemaprimerpo_USAddress10
        
    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, zip: str):
        self.__zip = zip

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def schemaprimerpo_USAddress(self):
        return self.__schemaprimerpo_USAddress

    @schemaprimerpo_USAddress.setter
    def schemaprimerpo_USAddress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schemaprimerpo_USAddress__schemaprimerpo_USAddress", None)
        self.__schemaprimerpo_USAddress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schemaprimerpo_PurchaseOrder7"):
                opp_val = getattr(old_value, "schemaprimerpo_PurchaseOrder7", None)
                if opp_val == self:
                    setattr(old_value, "schemaprimerpo_PurchaseOrder7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schemaprimerpo_PurchaseOrder7"):
                opp_val = getattr(value, "schemaprimerpo_PurchaseOrder7", None)
                setattr(value, "schemaprimerpo_PurchaseOrder7", self)

    @property
    def schemaprimerpo_USAddress10(self):
        return self.__schemaprimerpo_USAddress10

    @schemaprimerpo_USAddress10.setter
    def schemaprimerpo_USAddress10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schemaprimerpo_USAddress__schemaprimerpo_USAddress10", None)
        self.__schemaprimerpo_USAddress10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schemaprimerpo_PurchaseOrder9"):
                opp_val = getattr(old_value, "schemaprimerpo_PurchaseOrder9", None)
                if opp_val == self:
                    setattr(old_value, "schemaprimerpo_PurchaseOrder9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schemaprimerpo_PurchaseOrder9"):
                opp_val = getattr(value, "schemaprimerpo_PurchaseOrder9", None)
                setattr(value, "schemaprimerpo_PurchaseOrder9", self)

class schemaprimerpo_Item:

    def __init__(self, productName: str, quantity: str, partNum: str, uSPrice: str, comment: str, shipDate: str, schemaprimerpo_Item: "schemaprimerpo_PurchaseOrder" = None):
        self.productName = productName
        self.quantity = quantity
        self.partNum = partNum
        self.uSPrice = uSPrice
        self.comment = comment
        self.shipDate = shipDate
        self.schemaprimerpo_Item = schemaprimerpo_Item
        
    @property
    def partNum(self) -> str:
        return self.__partNum

    @partNum.setter
    def partNum(self, partNum: str):
        self.__partNum = partNum

    @property
    def productName(self) -> str:
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def shipDate(self) -> str:
        return self.__shipDate

    @shipDate.setter
    def shipDate(self, shipDate: str):
        self.__shipDate = shipDate

    @property
    def uSPrice(self) -> str:
        return self.__uSPrice

    @uSPrice.setter
    def uSPrice(self, uSPrice: str):
        self.__uSPrice = uSPrice

    @property
    def quantity(self) -> str:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def schemaprimerpo_Item(self):
        return self.__schemaprimerpo_Item

    @schemaprimerpo_Item.setter
    def schemaprimerpo_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schemaprimerpo_Item__schemaprimerpo_Item", None)
        self.__schemaprimerpo_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schemaprimerpo_PurchaseOrder12"):
                opp_val = getattr(old_value, "schemaprimerpo_PurchaseOrder12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schemaprimerpo_PurchaseOrder12"):
                opp_val = getattr(value, "schemaprimerpo_PurchaseOrder12", None)
                if opp_val is None:
                    setattr(value, "schemaprimerpo_PurchaseOrder12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class schemaprimerpo_PurchaseOrder:

    def __init__(self, comment: str, orderDate: str, schemaprimerpo_PurchaseOrder: "schemaprimerpo_DocumentRoot" = None, schemaprimerpo_PurchaseOrder7: "schemaprimerpo_USAddress" = None, schemaprimerpo_PurchaseOrder9: "schemaprimerpo_USAddress" = None, schemaprimerpo_PurchaseOrder12: set["schemaprimerpo_Item"] = None):
        self.comment = comment
        self.orderDate = orderDate
        self.schemaprimerpo_PurchaseOrder = schemaprimerpo_PurchaseOrder
        self.schemaprimerpo_PurchaseOrder7 = schemaprimerpo_PurchaseOrder7
        self.schemaprimerpo_PurchaseOrder9 = schemaprimerpo_PurchaseOrder9
        self.schemaprimerpo_PurchaseOrder12 = schemaprimerpo_PurchaseOrder12 if schemaprimerpo_PurchaseOrder12 is not None else set()
        
    @property
    def orderDate(self) -> str:
        return self.__orderDate

    @orderDate.setter
    def orderDate(self, orderDate: str):
        self.__orderDate = orderDate

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def schemaprimerpo_PurchaseOrder9(self):
        return self.__schemaprimerpo_PurchaseOrder9

    @schemaprimerpo_PurchaseOrder9.setter
    def schemaprimerpo_PurchaseOrder9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schemaprimerpo_PurchaseOrder__schemaprimerpo_PurchaseOrder9", None)
        self.__schemaprimerpo_PurchaseOrder9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schemaprimerpo_USAddress10"):
                opp_val = getattr(old_value, "schemaprimerpo_USAddress10", None)
                if opp_val == self:
                    setattr(old_value, "schemaprimerpo_USAddress10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schemaprimerpo_USAddress10"):
                opp_val = getattr(value, "schemaprimerpo_USAddress10", None)
                setattr(value, "schemaprimerpo_USAddress10", self)

    @property
    def schemaprimerpo_PurchaseOrder7(self):
        return self.__schemaprimerpo_PurchaseOrder7

    @schemaprimerpo_PurchaseOrder7.setter
    def schemaprimerpo_PurchaseOrder7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schemaprimerpo_PurchaseOrder__schemaprimerpo_PurchaseOrder7", None)
        self.__schemaprimerpo_PurchaseOrder7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schemaprimerpo_USAddress"):
                opp_val = getattr(old_value, "schemaprimerpo_USAddress", None)
                if opp_val == self:
                    setattr(old_value, "schemaprimerpo_USAddress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schemaprimerpo_USAddress"):
                opp_val = getattr(value, "schemaprimerpo_USAddress", None)
                setattr(value, "schemaprimerpo_USAddress", self)

    @property
    def schemaprimerpo_PurchaseOrder12(self):
        return self.__schemaprimerpo_PurchaseOrder12

    @schemaprimerpo_PurchaseOrder12.setter
    def schemaprimerpo_PurchaseOrder12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schemaprimerpo_PurchaseOrder__schemaprimerpo_PurchaseOrder12", None)
        self.__schemaprimerpo_PurchaseOrder12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schemaprimerpo_Item"):
                    opp_val = getattr(item, "schemaprimerpo_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "schemaprimerpo_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schemaprimerpo_Item"):
                    opp_val = getattr(item, "schemaprimerpo_Item", None)
                    
                    setattr(item, "schemaprimerpo_Item", self)
                    

    @property
    def schemaprimerpo_PurchaseOrder(self):
        return self.__schemaprimerpo_PurchaseOrder

    @schemaprimerpo_PurchaseOrder.setter
    def schemaprimerpo_PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schemaprimerpo_PurchaseOrder__schemaprimerpo_PurchaseOrder", None)
        self.__schemaprimerpo_PurchaseOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schemaprimerpo_DocumentRoot5"):
                opp_val = getattr(old_value, "schemaprimerpo_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schemaprimerpo_DocumentRoot5"):
                opp_val = getattr(value, "schemaprimerpo_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "schemaprimerpo_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class schemaprimerpo_EStringToStringMapEntry:

    pass
class schemaprimerpo_DocumentRoot:

    def __init__(self, mixed: str, comment: str, schemaprimerpo_DocumentRoot: set["schemaprimerpo_EStringToStringMapEntry"] = None, schemaprimerpo_DocumentRoot2: set["schemaprimerpo_EStringToStringMapEntry"] = None, schemaprimerpo_DocumentRoot5: set["schemaprimerpo_PurchaseOrder"] = None):
        self.mixed = mixed
        self.comment = comment
        self.schemaprimerpo_DocumentRoot = schemaprimerpo_DocumentRoot if schemaprimerpo_DocumentRoot is not None else set()
        self.schemaprimerpo_DocumentRoot2 = schemaprimerpo_DocumentRoot2 if schemaprimerpo_DocumentRoot2 is not None else set()
        self.schemaprimerpo_DocumentRoot5 = schemaprimerpo_DocumentRoot5 if schemaprimerpo_DocumentRoot5 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def schemaprimerpo_DocumentRoot2(self):
        return self.__schemaprimerpo_DocumentRoot2

    @schemaprimerpo_DocumentRoot2.setter
    def schemaprimerpo_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schemaprimerpo_DocumentRoot__schemaprimerpo_DocumentRoot2", None)
        self.__schemaprimerpo_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schemaprimerpo_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "schemaprimerpo_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "schemaprimerpo_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schemaprimerpo_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "schemaprimerpo_EStringToStringMapEntry3", None)
                    
                    setattr(item, "schemaprimerpo_EStringToStringMapEntry3", self)
                    

    @property
    def schemaprimerpo_DocumentRoot(self):
        return self.__schemaprimerpo_DocumentRoot

    @schemaprimerpo_DocumentRoot.setter
    def schemaprimerpo_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schemaprimerpo_DocumentRoot__schemaprimerpo_DocumentRoot", None)
        self.__schemaprimerpo_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schemaprimerpo_EStringToStringMapEntry"):
                    opp_val = getattr(item, "schemaprimerpo_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "schemaprimerpo_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schemaprimerpo_EStringToStringMapEntry"):
                    opp_val = getattr(item, "schemaprimerpo_EStringToStringMapEntry", None)
                    
                    setattr(item, "schemaprimerpo_EStringToStringMapEntry", self)
                    

    @property
    def schemaprimerpo_DocumentRoot5(self):
        return self.__schemaprimerpo_DocumentRoot5

    @schemaprimerpo_DocumentRoot5.setter
    def schemaprimerpo_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schemaprimerpo_DocumentRoot__schemaprimerpo_DocumentRoot5", None)
        self.__schemaprimerpo_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schemaprimerpo_PurchaseOrder"):
                    opp_val = getattr(item, "schemaprimerpo_PurchaseOrder", None)
                    
                    if opp_val == self:
                        setattr(item, "schemaprimerpo_PurchaseOrder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schemaprimerpo_PurchaseOrder"):
                    opp_val = getattr(item, "schemaprimerpo_PurchaseOrder", None)
                    
                    setattr(item, "schemaprimerpo_PurchaseOrder", self)
                    
