from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ppo_PurchaseOrder:

    def __init__(self, comment: str, orderDate: str, ppo_PurchaseOrder: set["ppo_Item"] = None, ppo_PurchaseOrder2: "ppo_USAddress" = None, ppo_PurchaseOrder4: "ppo_USAddress" = None):
        self.comment = comment
        self.orderDate = orderDate
        self.ppo_PurchaseOrder = ppo_PurchaseOrder if ppo_PurchaseOrder is not None else set()
        self.ppo_PurchaseOrder2 = ppo_PurchaseOrder2
        self.ppo_PurchaseOrder4 = ppo_PurchaseOrder4
        
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
    def ppo_PurchaseOrder4(self):
        return self.__ppo_PurchaseOrder4

    @ppo_PurchaseOrder4.setter
    def ppo_PurchaseOrder4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ppo_PurchaseOrder__ppo_PurchaseOrder4", None)
        self.__ppo_PurchaseOrder4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ppo_USAddress5"):
                opp_val = getattr(old_value, "ppo_USAddress5", None)
                if opp_val == self:
                    setattr(old_value, "ppo_USAddress5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ppo_USAddress5"):
                opp_val = getattr(value, "ppo_USAddress5", None)
                setattr(value, "ppo_USAddress5", self)

    @property
    def ppo_PurchaseOrder(self):
        return self.__ppo_PurchaseOrder

    @ppo_PurchaseOrder.setter
    def ppo_PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ppo_PurchaseOrder__ppo_PurchaseOrder", None)
        self.__ppo_PurchaseOrder = value if value is not None else set()
        
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
            if hasattr(old_value, "ppo_USAddress"):
                opp_val = getattr(old_value, "ppo_USAddress", None)
                if opp_val == self:
                    setattr(old_value, "ppo_USAddress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ppo_USAddress"):
                opp_val = getattr(value, "ppo_USAddress", None)
                setattr(value, "ppo_USAddress", self)

class ppo_USAddress:

    def __init__(self, name: str, street: str, city: str, state: str, zip: int, country: str, ppo_USAddress: "ppo_PurchaseOrder" = None, ppo_USAddress5: "ppo_PurchaseOrder" = None):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.ppo_USAddress = ppo_USAddress
        self.ppo_USAddress5 = ppo_USAddress5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def zip(self) -> int:
        return self.__zip

    @zip.setter
    def zip(self, zip: int):
        self.__zip = zip

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

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
    def ppo_USAddress5(self):
        return self.__ppo_USAddress5

    @ppo_USAddress5.setter
    def ppo_USAddress5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ppo_USAddress__ppo_USAddress5", None)
        self.__ppo_USAddress5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ppo_PurchaseOrder4"):
                opp_val = getattr(old_value, "ppo_PurchaseOrder4", None)
                if opp_val == self:
                    setattr(old_value, "ppo_PurchaseOrder4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ppo_PurchaseOrder4"):
                opp_val = getattr(value, "ppo_PurchaseOrder4", None)
                setattr(value, "ppo_PurchaseOrder4", self)

    def hasUSState(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasUSState method
        pass

class ppo_Item:

    def __init__(self, quantity: int, USPrice: int, comment: str, shipDate: str, partNum: str, productName: str, ppo_Item: "ppo_PurchaseOrder" = None):
        self.quantity = quantity
        self.USPrice = USPrice
        self.comment = comment
        self.shipDate = shipDate
        self.partNum = partNum
        self.productName = productName
        self.ppo_Item = ppo_Item
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def shipDate(self) -> str:
        return self.__shipDate

    @shipDate.setter
    def shipDate(self, shipDate: str):
        self.__shipDate = shipDate

    @property
    def USPrice(self) -> int:
        return self.__USPrice

    @USPrice.setter
    def USPrice(self, USPrice: int):
        self.__USPrice = USPrice

    @property
    def productName(self) -> str:
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName

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
    def ppo_Item(self):
        return self.__ppo_Item

    @ppo_Item.setter
    def ppo_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ppo_Item__ppo_Item", None)
        self.__ppo_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ppo_PurchaseOrder"):
                opp_val = getattr(old_value, "ppo_PurchaseOrder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ppo_PurchaseOrder"):
                opp_val = getattr(value, "ppo_PurchaseOrder", None)
                if opp_val is None:
                    setattr(value, "ppo_PurchaseOrder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
