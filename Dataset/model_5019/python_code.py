from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class purchaseOrder_Item:

    def __init__(self, productName: str, quantity: int, USPrice: int, comment: str, shipDate: str, partNum: str, purchaseOrder_Item: "purchaseOrder_PurchaseOrder" = None):
        self.productName = productName
        self.quantity = quantity
        self.USPrice = USPrice
        self.comment = comment
        self.shipDate = shipDate
        self.partNum = partNum
        self.purchaseOrder_Item = purchaseOrder_Item
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def productName(self) -> str:
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def USPrice(self) -> int:
        return self.__USPrice

    @USPrice.setter
    def USPrice(self, USPrice: int):
        self.__USPrice = USPrice

    @property
    def shipDate(self) -> str:
        return self.__shipDate

    @shipDate.setter
    def shipDate(self, shipDate: str):
        self.__shipDate = shipDate

    @property
    def partNum(self) -> str:
        return self.__partNum

    @partNum.setter
    def partNum(self, partNum: str):
        self.__partNum = partNum

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def purchaseOrder_Item(self):
        return self.__purchaseOrder_Item

    @purchaseOrder_Item.setter
    def purchaseOrder_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_purchaseOrder_Item__purchaseOrder_Item", None)
        self.__purchaseOrder_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "purchaseOrder_PurchaseOrder5"):
                opp_val = getattr(old_value, "purchaseOrder_PurchaseOrder5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "purchaseOrder_PurchaseOrder5"):
                opp_val = getattr(value, "purchaseOrder_PurchaseOrder5", None)
                if opp_val is None:
                    setattr(value, "purchaseOrder_PurchaseOrder5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class purchaseOrder_USAddress:

    def __init__(self, name: str, street: str, city: str, state: str, zip: int, country: str, purchaseOrder_USAddress: "purchaseOrder_PurchaseOrder" = None, purchaseOrder_USAddress3: "purchaseOrder_PurchaseOrder" = None):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.purchaseOrder_USAddress = purchaseOrder_USAddress
        self.purchaseOrder_USAddress3 = purchaseOrder_USAddress3
        
    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def zip(self) -> int:
        return self.__zip

    @zip.setter
    def zip(self, zip: int):
        self.__zip = zip

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

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
    def purchaseOrder_USAddress3(self):
        return self.__purchaseOrder_USAddress3

    @purchaseOrder_USAddress3.setter
    def purchaseOrder_USAddress3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_purchaseOrder_USAddress__purchaseOrder_USAddress3", None)
        self.__purchaseOrder_USAddress3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "purchaseOrder_PurchaseOrder2"):
                opp_val = getattr(old_value, "purchaseOrder_PurchaseOrder2", None)
                if opp_val == self:
                    setattr(old_value, "purchaseOrder_PurchaseOrder2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "purchaseOrder_PurchaseOrder2"):
                opp_val = getattr(value, "purchaseOrder_PurchaseOrder2", None)
                setattr(value, "purchaseOrder_PurchaseOrder2", self)

    @property
    def purchaseOrder_USAddress(self):
        return self.__purchaseOrder_USAddress

    @purchaseOrder_USAddress.setter
    def purchaseOrder_USAddress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_purchaseOrder_USAddress__purchaseOrder_USAddress", None)
        self.__purchaseOrder_USAddress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "purchaseOrder_PurchaseOrder"):
                opp_val = getattr(old_value, "purchaseOrder_PurchaseOrder", None)
                if opp_val == self:
                    setattr(old_value, "purchaseOrder_PurchaseOrder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "purchaseOrder_PurchaseOrder"):
                opp_val = getattr(value, "purchaseOrder_PurchaseOrder", None)
                setattr(value, "purchaseOrder_PurchaseOrder", self)

class purchaseOrder_PurchaseOrder:

    def __init__(self, comment: str, orderDate: str, purchaseOrder_PurchaseOrder: "purchaseOrder_USAddress" = None, purchaseOrder_PurchaseOrder2: "purchaseOrder_USAddress" = None, purchaseOrder_PurchaseOrder5: set["purchaseOrder_Item"] = None):
        self.comment = comment
        self.orderDate = orderDate
        self.purchaseOrder_PurchaseOrder = purchaseOrder_PurchaseOrder
        self.purchaseOrder_PurchaseOrder2 = purchaseOrder_PurchaseOrder2
        self.purchaseOrder_PurchaseOrder5 = purchaseOrder_PurchaseOrder5 if purchaseOrder_PurchaseOrder5 is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def orderDate(self) -> str:
        return self.__orderDate

    @orderDate.setter
    def orderDate(self, orderDate: str):
        self.__orderDate = orderDate

    @property
    def purchaseOrder_PurchaseOrder(self):
        return self.__purchaseOrder_PurchaseOrder

    @purchaseOrder_PurchaseOrder.setter
    def purchaseOrder_PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_purchaseOrder_PurchaseOrder__purchaseOrder_PurchaseOrder", None)
        self.__purchaseOrder_PurchaseOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "purchaseOrder_USAddress"):
                opp_val = getattr(old_value, "purchaseOrder_USAddress", None)
                if opp_val == self:
                    setattr(old_value, "purchaseOrder_USAddress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "purchaseOrder_USAddress"):
                opp_val = getattr(value, "purchaseOrder_USAddress", None)
                setattr(value, "purchaseOrder_USAddress", self)

    @property
    def purchaseOrder_PurchaseOrder2(self):
        return self.__purchaseOrder_PurchaseOrder2

    @purchaseOrder_PurchaseOrder2.setter
    def purchaseOrder_PurchaseOrder2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_purchaseOrder_PurchaseOrder__purchaseOrder_PurchaseOrder2", None)
        self.__purchaseOrder_PurchaseOrder2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "purchaseOrder_USAddress3"):
                opp_val = getattr(old_value, "purchaseOrder_USAddress3", None)
                if opp_val == self:
                    setattr(old_value, "purchaseOrder_USAddress3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "purchaseOrder_USAddress3"):
                opp_val = getattr(value, "purchaseOrder_USAddress3", None)
                setattr(value, "purchaseOrder_USAddress3", self)

    @property
    def purchaseOrder_PurchaseOrder5(self):
        return self.__purchaseOrder_PurchaseOrder5

    @purchaseOrder_PurchaseOrder5.setter
    def purchaseOrder_PurchaseOrder5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_purchaseOrder_PurchaseOrder__purchaseOrder_PurchaseOrder5", None)
        self.__purchaseOrder_PurchaseOrder5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "purchaseOrder_Item"):
                    opp_val = getattr(item, "purchaseOrder_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "purchaseOrder_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "purchaseOrder_Item"):
                    opp_val = getattr(item, "purchaseOrder_Item", None)
                    
                    setattr(item, "purchaseOrder_Item", self)
                    
