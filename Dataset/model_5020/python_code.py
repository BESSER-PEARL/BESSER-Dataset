from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class esof_homework4_q2_USAddress:

    def __init__(self, name: str, street: str, city: str, zip: int, state: str, country: str, esof_homework4_q2_USAddress: "esof_homework4_q2_PurchaseOrder" = None, esof_homework4_q2_USAddress5: "esof_homework4_q2_PurchaseOrder" = None):
        self.name = name
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        self.country = country
        self.esof_homework4_q2_USAddress = esof_homework4_q2_USAddress
        self.esof_homework4_q2_USAddress5 = esof_homework4_q2_USAddress5
        
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
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

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
    def esof_homework4_q2_USAddress(self):
        return self.__esof_homework4_q2_USAddress

    @esof_homework4_q2_USAddress.setter
    def esof_homework4_q2_USAddress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esof_homework4_q2_USAddress__esof_homework4_q2_USAddress", None)
        self.__esof_homework4_q2_USAddress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esof_homework4_q2_PurchaseOrder2"):
                opp_val = getattr(old_value, "esof_homework4_q2_PurchaseOrder2", None)
                if opp_val == self:
                    setattr(old_value, "esof_homework4_q2_PurchaseOrder2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esof_homework4_q2_PurchaseOrder2"):
                opp_val = getattr(value, "esof_homework4_q2_PurchaseOrder2", None)
                setattr(value, "esof_homework4_q2_PurchaseOrder2", self)

    @property
    def esof_homework4_q2_USAddress5(self):
        return self.__esof_homework4_q2_USAddress5

    @esof_homework4_q2_USAddress5.setter
    def esof_homework4_q2_USAddress5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esof_homework4_q2_USAddress__esof_homework4_q2_USAddress5", None)
        self.__esof_homework4_q2_USAddress5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esof_homework4_q2_PurchaseOrder4"):
                opp_val = getattr(old_value, "esof_homework4_q2_PurchaseOrder4", None)
                if opp_val == self:
                    setattr(old_value, "esof_homework4_q2_PurchaseOrder4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esof_homework4_q2_PurchaseOrder4"):
                opp_val = getattr(value, "esof_homework4_q2_PurchaseOrder4", None)
                setattr(value, "esof_homework4_q2_PurchaseOrder4", self)

class esof_homework4_q2_Item:

    def __init__(self, productName: str, quantity: int, USPrice: int, comment: str, shipDate: str, partNum: str, esof_homework4_q2_Item: "esof_homework4_q2_PurchaseOrder" = None):
        self.productName = productName
        self.quantity = quantity
        self.USPrice = USPrice
        self.comment = comment
        self.shipDate = shipDate
        self.partNum = partNum
        self.esof_homework4_q2_Item = esof_homework4_q2_Item
        
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
    def esof_homework4_q2_Item(self):
        return self.__esof_homework4_q2_Item

    @esof_homework4_q2_Item.setter
    def esof_homework4_q2_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esof_homework4_q2_Item__esof_homework4_q2_Item", None)
        self.__esof_homework4_q2_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esof_homework4_q2_PurchaseOrder"):
                opp_val = getattr(old_value, "esof_homework4_q2_PurchaseOrder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esof_homework4_q2_PurchaseOrder"):
                opp_val = getattr(value, "esof_homework4_q2_PurchaseOrder", None)
                if opp_val is None:
                    setattr(value, "esof_homework4_q2_PurchaseOrder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class esof_homework4_q2_PurchaseOrder:

    def __init__(self, comment: str, orderDate: str, esof_homework4_q2_PurchaseOrder: set["esof_homework4_q2_Item"] = None, esof_homework4_q2_PurchaseOrder2: "esof_homework4_q2_USAddress" = None, esof_homework4_q2_PurchaseOrder4: "esof_homework4_q2_USAddress" = None):
        self.comment = comment
        self.orderDate = orderDate
        self.esof_homework4_q2_PurchaseOrder = esof_homework4_q2_PurchaseOrder if esof_homework4_q2_PurchaseOrder is not None else set()
        self.esof_homework4_q2_PurchaseOrder2 = esof_homework4_q2_PurchaseOrder2
        self.esof_homework4_q2_PurchaseOrder4 = esof_homework4_q2_PurchaseOrder4
        
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
    def esof_homework4_q2_PurchaseOrder4(self):
        return self.__esof_homework4_q2_PurchaseOrder4

    @esof_homework4_q2_PurchaseOrder4.setter
    def esof_homework4_q2_PurchaseOrder4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esof_homework4_q2_PurchaseOrder__esof_homework4_q2_PurchaseOrder4", None)
        self.__esof_homework4_q2_PurchaseOrder4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esof_homework4_q2_USAddress5"):
                opp_val = getattr(old_value, "esof_homework4_q2_USAddress5", None)
                if opp_val == self:
                    setattr(old_value, "esof_homework4_q2_USAddress5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esof_homework4_q2_USAddress5"):
                opp_val = getattr(value, "esof_homework4_q2_USAddress5", None)
                setattr(value, "esof_homework4_q2_USAddress5", self)

    @property
    def esof_homework4_q2_PurchaseOrder2(self):
        return self.__esof_homework4_q2_PurchaseOrder2

    @esof_homework4_q2_PurchaseOrder2.setter
    def esof_homework4_q2_PurchaseOrder2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esof_homework4_q2_PurchaseOrder__esof_homework4_q2_PurchaseOrder2", None)
        self.__esof_homework4_q2_PurchaseOrder2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esof_homework4_q2_USAddress"):
                opp_val = getattr(old_value, "esof_homework4_q2_USAddress", None)
                if opp_val == self:
                    setattr(old_value, "esof_homework4_q2_USAddress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esof_homework4_q2_USAddress"):
                opp_val = getattr(value, "esof_homework4_q2_USAddress", None)
                setattr(value, "esof_homework4_q2_USAddress", self)

    @property
    def esof_homework4_q2_PurchaseOrder(self):
        return self.__esof_homework4_q2_PurchaseOrder

    @esof_homework4_q2_PurchaseOrder.setter
    def esof_homework4_q2_PurchaseOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esof_homework4_q2_PurchaseOrder__esof_homework4_q2_PurchaseOrder", None)
        self.__esof_homework4_q2_PurchaseOrder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "esof_homework4_q2_Item"):
                    opp_val = getattr(item, "esof_homework4_q2_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "esof_homework4_q2_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "esof_homework4_q2_Item"):
                    opp_val = getattr(item, "esof_homework4_q2_Item", None)
                    
                    setattr(item, "esof_homework4_q2_Item", self)
                    
