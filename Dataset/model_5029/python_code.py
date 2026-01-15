from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ShipmentStatus(Enum):
    NEW = "NEW"
    ASSIGNED = "ASSIGNED"
    UNDERWAY = "UNDERWAY"
    DELIVERED = "DELIVERED"


############################################
# Definition of Classes
############################################

class pickupnet_Shipment:

    def __init__(self, id: str, status: str, orders: "pickupnet_Customer" = None, pickupnet_Shipment11: "pickupnet_Address" = None, pickupnet_Shipment13: "pickupnet_Address" = None, pickupnet_Shipment: "pickupnet_Station" = None, Shipment: "pickupnet_Driver" = None, Shipment7: "pickupnet_Customer" = None, assignments: "pickupnet_Driver" = None):
        self.id = id
        self.status = status
        self.orders = orders
        self.pickupnet_Shipment11 = pickupnet_Shipment11
        self.pickupnet_Shipment13 = pickupnet_Shipment13
        self.pickupnet_Shipment = pickupnet_Shipment
        self.Shipment = Shipment
        self.Shipment7 = Shipment7
        self.assignments = assignments
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def Shipment(self):
        return self.__Shipment

    @Shipment.setter
    def Shipment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Shipment__Shipment", None)
        self.__Shipment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver"):
                opp_val = getattr(old_value, "driver", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver"):
                opp_val = getattr(value, "driver", None)
                if opp_val is None:
                    setattr(value, "driver", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assignments(self):
        return self.__assignments

    @assignments.setter
    def assignments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Shipment__assignments", None)
        self.__assignments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Driver"):
                opp_val = getattr(old_value, "Driver", None)
                if opp_val == self:
                    setattr(old_value, "Driver", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Driver"):
                opp_val = getattr(value, "Driver", None)
                setattr(value, "Driver", self)

    @property
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Shipment__orders", None)
        self.__orders = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer"):
                opp_val = getattr(old_value, "Customer", None)
                if opp_val == self:
                    setattr(old_value, "Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer"):
                opp_val = getattr(value, "Customer", None)
                setattr(value, "Customer", self)

    @property
    def pickupnet_Shipment11(self):
        return self.__pickupnet_Shipment11

    @pickupnet_Shipment11.setter
    def pickupnet_Shipment11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Shipment__pickupnet_Shipment11", None)
        self.__pickupnet_Shipment11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pickupnet_Address"):
                opp_val = getattr(old_value, "pickupnet_Address", None)
                if opp_val == self:
                    setattr(old_value, "pickupnet_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pickupnet_Address"):
                opp_val = getattr(value, "pickupnet_Address", None)
                setattr(value, "pickupnet_Address", self)

    @property
    def Shipment7(self):
        return self.__Shipment7

    @Shipment7.setter
    def Shipment7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Shipment__Shipment7", None)
        self.__Shipment7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderer"):
                opp_val = getattr(old_value, "orderer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderer"):
                opp_val = getattr(value, "orderer", None)
                if opp_val is None:
                    setattr(value, "orderer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pickupnet_Shipment(self):
        return self.__pickupnet_Shipment

    @pickupnet_Shipment.setter
    def pickupnet_Shipment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Shipment__pickupnet_Shipment", None)
        self.__pickupnet_Shipment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pickupnet_Station4"):
                opp_val = getattr(old_value, "pickupnet_Station4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pickupnet_Station4"):
                opp_val = getattr(value, "pickupnet_Station4", None)
                if opp_val is None:
                    setattr(value, "pickupnet_Station4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pickupnet_Shipment13(self):
        return self.__pickupnet_Shipment13

    @pickupnet_Shipment13.setter
    def pickupnet_Shipment13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Shipment__pickupnet_Shipment13", None)
        self.__pickupnet_Shipment13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pickupnet_Address14"):
                opp_val = getattr(old_value, "pickupnet_Address14", None)
                if opp_val == self:
                    setattr(old_value, "pickupnet_Address14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pickupnet_Address14"):
                opp_val = getattr(value, "pickupnet_Address14", None)
                setattr(value, "pickupnet_Address14", self)

class pickupnet_Driver:

    def __init__(self, id: str, name: str, pickupnet_Driver: "pickupnet_Station" = None, driver: set["pickupnet_Shipment"] = None, Driver: "pickupnet_Shipment" = None):
        self.id = id
        self.name = name
        self.pickupnet_Driver = pickupnet_Driver
        self.driver = driver if driver is not None else set()
        self.Driver = Driver
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Driver__driver", None)
        self.__driver = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Shipment"):
                    opp_val = getattr(item, "Shipment", None)
                    
                    if opp_val == self:
                        setattr(item, "Shipment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Shipment"):
                    opp_val = getattr(item, "Shipment", None)
                    
                    setattr(item, "Shipment", self)
                    

    @property
    def pickupnet_Driver(self):
        return self.__pickupnet_Driver

    @pickupnet_Driver.setter
    def pickupnet_Driver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Driver__pickupnet_Driver", None)
        self.__pickupnet_Driver = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pickupnet_Station2"):
                opp_val = getattr(old_value, "pickupnet_Station2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pickupnet_Station2"):
                opp_val = getattr(value, "pickupnet_Station2", None)
                if opp_val is None:
                    setattr(value, "pickupnet_Station2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Driver(self):
        return self.__Driver

    @Driver.setter
    def Driver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Driver__Driver", None)
        self.__Driver = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignments"):
                opp_val = getattr(old_value, "assignments", None)
                if opp_val == self:
                    setattr(old_value, "assignments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignments"):
                opp_val = getattr(value, "assignments", None)
                setattr(value, "assignments", self)

class pickupnet_Customer:

    def __init__(self, id: str, name: str, twitterUserName: str, Customer: "pickupnet_Shipment" = None, pickupnet_Customer: "pickupnet_Station" = None, orderer: set["pickupnet_Shipment"] = None):
        self.id = id
        self.name = name
        self.twitterUserName = twitterUserName
        self.Customer = Customer
        self.pickupnet_Customer = pickupnet_Customer
        self.orderer = orderer if orderer is not None else set()
        
    @property
    def twitterUserName(self) -> str:
        return self.__twitterUserName

    @twitterUserName.setter
    def twitterUserName(self, twitterUserName: str):
        self.__twitterUserName = twitterUserName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pickupnet_Customer(self):
        return self.__pickupnet_Customer

    @pickupnet_Customer.setter
    def pickupnet_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Customer__pickupnet_Customer", None)
        self.__pickupnet_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pickupnet_Station"):
                opp_val = getattr(old_value, "pickupnet_Station", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pickupnet_Station"):
                opp_val = getattr(value, "pickupnet_Station", None)
                if opp_val is None:
                    setattr(value, "pickupnet_Station", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def orderer(self):
        return self.__orderer

    @orderer.setter
    def orderer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Customer__orderer", None)
        self.__orderer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Shipment7"):
                    opp_val = getattr(item, "Shipment7", None)
                    
                    if opp_val == self:
                        setattr(item, "Shipment7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Shipment7"):
                    opp_val = getattr(item, "Shipment7", None)
                    
                    setattr(item, "Shipment7", self)
                    

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders"):
                opp_val = getattr(old_value, "orders", None)
                if opp_val == self:
                    setattr(old_value, "orders", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders"):
                opp_val = getattr(value, "orders", None)
                setattr(value, "orders", self)

class pickupnet_GeoLocation:

    def __init__(self, lat: float, lon: float, pickupnet_GeoLocation: "pickupnet_Address" = None):
        self.lat = lat
        self.lon = lon
        self.pickupnet_GeoLocation = pickupnet_GeoLocation
        
    @property
    def lat(self) -> float:
        return self.__lat

    @lat.setter
    def lat(self, lat: float):
        self.__lat = lat

    @property
    def lon(self) -> float:
        return self.__lon

    @lon.setter
    def lon(self, lon: float):
        self.__lon = lon

    @property
    def pickupnet_GeoLocation(self):
        return self.__pickupnet_GeoLocation

    @pickupnet_GeoLocation.setter
    def pickupnet_GeoLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_GeoLocation__pickupnet_GeoLocation", None)
        self.__pickupnet_GeoLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pickupnet_Address16"):
                opp_val = getattr(old_value, "pickupnet_Address16", None)
                if opp_val == self:
                    setattr(old_value, "pickupnet_Address16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pickupnet_Address16"):
                opp_val = getattr(value, "pickupnet_Address16", None)
                setattr(value, "pickupnet_Address16", self)

class pickupnet_Address:

    def __init__(self, text: str, pickupnet_Address: "pickupnet_Shipment" = None, pickupnet_Address14: "pickupnet_Shipment" = None, pickupnet_Address16: "pickupnet_GeoLocation" = None):
        self.text = text
        self.pickupnet_Address = pickupnet_Address
        self.pickupnet_Address14 = pickupnet_Address14
        self.pickupnet_Address16 = pickupnet_Address16
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def pickupnet_Address16(self):
        return self.__pickupnet_Address16

    @pickupnet_Address16.setter
    def pickupnet_Address16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Address__pickupnet_Address16", None)
        self.__pickupnet_Address16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pickupnet_GeoLocation"):
                opp_val = getattr(old_value, "pickupnet_GeoLocation", None)
                if opp_val == self:
                    setattr(old_value, "pickupnet_GeoLocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pickupnet_GeoLocation"):
                opp_val = getattr(value, "pickupnet_GeoLocation", None)
                setattr(value, "pickupnet_GeoLocation", self)

    @property
    def pickupnet_Address(self):
        return self.__pickupnet_Address

    @pickupnet_Address.setter
    def pickupnet_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Address__pickupnet_Address", None)
        self.__pickupnet_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pickupnet_Shipment11"):
                opp_val = getattr(old_value, "pickupnet_Shipment11", None)
                if opp_val == self:
                    setattr(old_value, "pickupnet_Shipment11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pickupnet_Shipment11"):
                opp_val = getattr(value, "pickupnet_Shipment11", None)
                setattr(value, "pickupnet_Shipment11", self)

    @property
    def pickupnet_Address14(self):
        return self.__pickupnet_Address14

    @pickupnet_Address14.setter
    def pickupnet_Address14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Address__pickupnet_Address14", None)
        self.__pickupnet_Address14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pickupnet_Shipment13"):
                opp_val = getattr(old_value, "pickupnet_Shipment13", None)
                if opp_val == self:
                    setattr(old_value, "pickupnet_Shipment13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pickupnet_Shipment13"):
                opp_val = getattr(value, "pickupnet_Shipment13", None)
                setattr(value, "pickupnet_Shipment13", self)

class pickupnet_Station:

    def __init__(self, pickupnet_Station: set["pickupnet_Customer"] = None, pickupnet_Station2: set["pickupnet_Driver"] = None, pickupnet_Station4: set["pickupnet_Shipment"] = None):
        self.pickupnet_Station = pickupnet_Station if pickupnet_Station is not None else set()
        self.pickupnet_Station2 = pickupnet_Station2 if pickupnet_Station2 is not None else set()
        self.pickupnet_Station4 = pickupnet_Station4 if pickupnet_Station4 is not None else set()
        
    @property
    def pickupnet_Station4(self):
        return self.__pickupnet_Station4

    @pickupnet_Station4.setter
    def pickupnet_Station4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Station__pickupnet_Station4", None)
        self.__pickupnet_Station4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pickupnet_Shipment"):
                    opp_val = getattr(item, "pickupnet_Shipment", None)
                    
                    if opp_val == self:
                        setattr(item, "pickupnet_Shipment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pickupnet_Shipment"):
                    opp_val = getattr(item, "pickupnet_Shipment", None)
                    
                    setattr(item, "pickupnet_Shipment", self)
                    

    @property
    def pickupnet_Station2(self):
        return self.__pickupnet_Station2

    @pickupnet_Station2.setter
    def pickupnet_Station2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Station__pickupnet_Station2", None)
        self.__pickupnet_Station2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pickupnet_Driver"):
                    opp_val = getattr(item, "pickupnet_Driver", None)
                    
                    if opp_val == self:
                        setattr(item, "pickupnet_Driver", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pickupnet_Driver"):
                    opp_val = getattr(item, "pickupnet_Driver", None)
                    
                    setattr(item, "pickupnet_Driver", self)
                    

    @property
    def pickupnet_Station(self):
        return self.__pickupnet_Station

    @pickupnet_Station.setter
    def pickupnet_Station(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pickupnet_Station__pickupnet_Station", None)
        self.__pickupnet_Station = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pickupnet_Customer"):
                    opp_val = getattr(item, "pickupnet_Customer", None)
                    
                    if opp_val == self:
                        setattr(item, "pickupnet_Customer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pickupnet_Customer"):
                    opp_val = getattr(item, "pickupnet_Customer", None)
                    
                    setattr(item, "pickupnet_Customer", self)
                    

    def registerCustomer(self, customer: str):
        # TODO: Implement registerCustomer method
        pass

    def acceptShipment(self, shipment: str):
        # TODO: Implement acceptShipment method
        pass

    def registerDriver(self, driver: str):
        # TODO: Implement registerDriver method
        pass
