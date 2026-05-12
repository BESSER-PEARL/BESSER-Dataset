from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class EventsProductGroup:

    def __init__(self, id: int, Event: Events, ProductGroup: ProductGroup, productGroup4: "ProductGroup" = None, events6: "Events" = None):
        self.id = id
        self.Event = Event
        self.ProductGroup = ProductGroup
        self.productGroup4 = productGroup4
        self.events6 = events6
        
        pass
    @property
    def ProductGroup(self):
        return self.__ProductGroup
    @ProductGroup.setter
    def ProductGroup(self, ProductGroup: ProductGroup):
        self.__ProductGroup = ProductGroup

    @property
    def Event(self):
        return self.__Event
    @Event.setter
    def Event(self, Event: Events):
        self.__Event = Event

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def events6(self):
        return self.__events6
    @events6.setter
    def events6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventsProductGroup__events6", None)
        self.__events6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventsProductGroup7"):
                opp_val = getattr(old_value, "eventsProductGroup7", None)
                if opp_val == self:
                    setattr(old_value, "eventsProductGroup7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventsProductGroup7"):
                opp_val = getattr(value, "eventsProductGroup7", None)
                setattr(value, "eventsProductGroup7", self)

    @property
    def productGroup4(self):
        return self.__productGroup4
    @productGroup4.setter
    def productGroup4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventsProductGroup__productGroup4", None)
        self.__productGroup4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventsProductGroup5"):
                opp_val = getattr(old_value, "eventsProductGroup5", None)
                if opp_val == self:
                    setattr(old_value, "eventsProductGroup5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventsProductGroup5"):
                opp_val = getattr(value, "eventsProductGroup5", None)
                setattr(value, "eventsProductGroup5", self)



class Events:

    def __init__(self, id: int, datetime: int, user: str, name: str, eventsProductGroup7: "EventsProductGroup" = None):
        self.id = id
        self.datetime = datetime
        self.user = user
        self.name = name
        self.eventsProductGroup7 = eventsProductGroup7
        
        pass
    @property
    def datetime(self):
        return self.__datetime
    @datetime.setter
    def datetime(self, datetime: int):
        self.__datetime = datetime

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def eventsProductGroup7(self):
        return self.__eventsProductGroup7
    @eventsProductGroup7.setter
    def eventsProductGroup7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Events__eventsProductGroup7", None)
        self.__eventsProductGroup7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events6"):
                opp_val = getattr(old_value, "events6", None)
                if opp_val == self:
                    setattr(old_value, "events6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events6"):
                opp_val = getattr(value, "events6", None)
                setattr(value, "events6", self)



class ProductGroupProduct:

    def __init__(self, id: int, ProductGroup: ProductGroup, Product: Product, weight: int, product0: "Product" = None, productGroup2: "ProductGroup" = None):
        self.id = id
        self.ProductGroup = ProductGroup
        self.Product = Product
        self.weight = weight
        self.product0 = product0
        self.productGroup2 = productGroup2
        
        pass
    @property
    def Product(self):
        return self.__Product
    @Product.setter
    def Product(self, Product: Product):
        self.__Product = Product

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def ProductGroup(self):
        return self.__ProductGroup
    @ProductGroup.setter
    def ProductGroup(self, ProductGroup: ProductGroup):
        self.__ProductGroup = ProductGroup

    @property
    def product0(self):
        return self.__product0
    @product0.setter
    def product0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductGroupProduct__product0", None)
        self.__product0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "productGroupProduct1"):
                opp_val = getattr(old_value, "productGroupProduct1", None)
                if opp_val == self:
                    setattr(old_value, "productGroupProduct1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "productGroupProduct1"):
                opp_val = getattr(value, "productGroupProduct1", None)
                setattr(value, "productGroupProduct1", self)

    @property
    def productGroup2(self):
        return self.__productGroup2
    @productGroup2.setter
    def productGroup2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductGroupProduct__productGroup2", None)
        self.__productGroup2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "productGroupProduct3"):
                opp_val = getattr(old_value, "productGroupProduct3", None)
                if opp_val == self:
                    setattr(old_value, "productGroupProduct3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "productGroupProduct3"):
                opp_val = getattr(value, "productGroupProduct3", None)
                setattr(value, "productGroupProduct3", self)



class ProductGroup:

    def __init__(self, id: int, name: str, productGroupProduct3: "ProductGroupProduct" = None, eventsProductGroup5: "EventsProductGroup" = None):
        self.id = id
        self.name = name
        self.productGroupProduct3 = productGroupProduct3
        self.eventsProductGroup5 = eventsProductGroup5
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def productGroupProduct3(self):
        return self.__productGroupProduct3
    @productGroupProduct3.setter
    def productGroupProduct3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductGroup__productGroupProduct3", None)
        self.__productGroupProduct3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "productGroup2"):
                opp_val = getattr(old_value, "productGroup2", None)
                if opp_val == self:
                    setattr(old_value, "productGroup2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "productGroup2"):
                opp_val = getattr(value, "productGroup2", None)
                setattr(value, "productGroup2", self)

    @property
    def eventsProductGroup5(self):
        return self.__eventsProductGroup5
    @eventsProductGroup5.setter
    def eventsProductGroup5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ProductGroup__eventsProductGroup5", None)
        self.__eventsProductGroup5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "productGroup4"):
                opp_val = getattr(old_value, "productGroup4", None)
                if opp_val == self:
                    setattr(old_value, "productGroup4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "productGroup4"):
                opp_val = getattr(value, "productGroup4", None)
                setattr(value, "productGroup4", self)



class Product:

    def __init__(self, name: str, id: int, productGroupProduct1: "ProductGroupProduct" = None):
        self.name = name
        self.id = id
        self.productGroupProduct1 = productGroupProduct1
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def productGroupProduct1(self):
        return self.__productGroupProduct1
    @productGroupProduct1.setter
    def productGroupProduct1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__productGroupProduct1", None)
        self.__productGroupProduct1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product0"):
                opp_val = getattr(old_value, "product0", None)
                if opp_val == self:
                    setattr(old_value, "product0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product0"):
                opp_val = getattr(value, "product0", None)
                setattr(value, "product0", self)

