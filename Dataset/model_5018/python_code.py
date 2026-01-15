from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ppo_Item:

    def __init__(self, productName: str, quantity: int, USPrice: int, comment: str, shipDate: str, partNum: str, ppo_Item: "ppo_PurchaseOrder" = None):
        self.productName = productName
        self.quantity = quantity
        self.USPrice = USPrice
        self.comment = comment
        self.shipDate = shipDate
        self.partNum = partNum
        self.ppo_Item = ppo_Item
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def partNum(self) -> str:
        return self.__partNum

    @partNum.setter
    def partNum(self, partNum: str):
        self.__partNum = partNum

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

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
    def productName(self) -> str:
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

    @property
    def ppo_Item(self):
        return self.__ppo_Item

    @ppo_Item.setter
    def ppo_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ppo_Item__ppo_Item", None)
        self.__ppo_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ppo_PurchaseOrder5"):
                opp_val = getattr(old_value, "ppo_PurchaseOrder5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ppo_PurchaseOrder5"):
                opp_val = getattr(value, "ppo_PurchaseOrder5", None)
                if opp_val is None:
                    setattr(value, "ppo_PurchaseOrder5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ppo_USAddress:

    def __init__(self, name: str, street: str, city: str, state: str, zip: int, country: str, ppo_USAddress: "ppo_PurchaseOrder" = None, ppo_USAddress3: "ppo_PurchaseOrder" = None):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.ppo_USAddress = ppo_USAddress
        self.ppo_USAddress3 = ppo_USAddress3
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ppo_USAddress3(self):
        return self.__ppo_USAddress3

    @ppo_USAddress3.setter
    def ppo_USAddress3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ppo_USAddress__ppo_USAddress3", None)
        self.__ppo_USAddress3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ppo_PurchaseOrder2"):
                opp_val = getattr(old_value, "ppo_PurchaseOrder2", None)
                if opp_val == self:
                    setattr(old_value, "ppo_PurchaseOrder2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ppo_PurchaseOrder2"):
                opp_val = getattr(value, "ppo_PurchaseOrder2", None)
                setattr(value, "ppo_PurchaseOrder2", self)

    @property
    def ppo_USAddress(self):
        return self.__ppo_USAddress

    @ppo_USAddress.setter
    def ppo_USAddress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ppo_USAddress__ppo_USAddress", None)
        self.__ppo_USAddress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ppo_PurchaseOrder"):
                opp_val = getattr(old_value, "ppo_PurchaseOrder", None)
                if opp_val == self:
                    setattr(old_value, "ppo_PurchaseOrder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ppo_PurchaseOrder"):
                opp_val = getattr(value, "ppo_PurchaseOrder", None)
                setattr(value, "ppo_PurchaseOrder", self)

class ppo_PurchaseOrder:

    def __init__(self, comment: str, orderDate: str, ppo_PurchaseOrder: "ppo_USAddress" = None, ppo_PurchaseOrder2: "ppo_USAddress" = None, ppo_PurchaseOrder5: set["ppo_Item"] = None):
        self.comment = comment
        self.orderDate = orderDate
        self.ppo_PurchaseOrder = ppo_PurchaseOrder
        self.ppo_PurchaseOrder2 = ppo_PurchaseOrder2
        self.ppo_PurchaseOrder5 = ppo_PurchaseOrder5 if ppo_PurchaseOrder5 is not None else set()
        
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
    def ppo_PurchaseOrder(self):
        return self.__ppo_PurchaseOrder

    @ppo_PurchaseOrder.setter
    def ppo_PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ppo_PurchaseOrder__ppo_PurchaseOrder", None)
        self.__ppo_PurchaseOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ppo_USAddress"):
                opp_val = getattr(old_value, "ppo_USAddress", None)
                if opp_val == self:
                    setattr(old_value, "ppo_USAddress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ppo_USAddress"):
                opp_val = getattr(value, "ppo_USAddress", None)
                setattr(value, "ppo_USAddress", self)

    @property
    def ppo_PurchaseOrder2(self):
        return self.__ppo_PurchaseOrder2

    @ppo_PurchaseOrder2.setter
    def ppo_PurchaseOrder2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ppo_PurchaseOrder__ppo_PurchaseOrder2", None)
        self.__ppo_PurchaseOrder2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ppo_USAddress3"):
                opp_val = getattr(old_value, "ppo_USAddress3", None)
                if opp_val == self:
                    setattr(old_value, "ppo_USAddress3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ppo_USAddress3"):
                opp_val = getattr(value, "ppo_USAddress3", None)
                setattr(value, "ppo_USAddress3", self)

    @property
    def ppo_PurchaseOrder5(self):
        return self.__ppo_PurchaseOrder5

    @ppo_PurchaseOrder5.setter
    def ppo_PurchaseOrder5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ppo_PurchaseOrder__ppo_PurchaseOrder5", None)
        self.__ppo_PurchaseOrder5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ppo_Item"):
                    opp_val = getattr(item, "ppo_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "ppo_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ppo_Item"):
                    opp_val = getattr(item, "ppo_Item", None)
                    
                    setattr(item, "ppo_Item", self)
                    
