from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Craft:

    pass
class CarRentalModel_Automobile(Craft):

    def __init__(self, isCabrio: bool):
        self.isCabrio = isCabrio
        
    @property
    def isCabrio(self) -> bool:
        return self.__isCabrio

    @isCabrio.setter
    def isCabrio(self, isCabrio: bool):
        self.__isCabrio = isCabrio

class CarRentalModel_Motorcycle(Craft):

    def __init__(self, cm3: int):
        self.cm3 = cm3
        
    @property
    def cm3(self) -> int:
        return self.__cm3

    @cm3.setter
    def cm3(self, cm3: int):
        self.__cm3 = cm3

class Customer:

    pass
class CarRentalModel_VipCustomer(Customer):

    def __init__(self, discount: float):
        self.discount = discount
        
    @property
    def discount(self) -> float:
        return self.__discount

    @discount.setter
    def discount(self, discount: float):
        self.__discount = discount

class CarRentalModel_Order:

    def __init__(self, orderDate: date, price: float, Order: "CarRentalModel_Customer" = None, rentBy: "CarRentalModel_Craft" = None, bestellungen: "CarRentalModel_Customer" = None, Order12: "CarRentalModel_Craft" = None):
        self.orderDate = orderDate
        self.price = price
        self.Order = Order
        self.rentBy = rentBy
        self.bestellungen = bestellungen
        self.Order12 = Order12
        
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def orderDate(self) -> date:
        return self.__orderDate

    @orderDate.setter
    def orderDate(self, orderDate: date):
        self.__orderDate = orderDate

    @property
    def rentBy(self):
        return self.__rentBy

    @rentBy.setter
    def rentBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Order__rentBy", None)
        self.__rentBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Craft"):
                opp_val = getattr(old_value, "Craft", None)
                if opp_val == self:
                    setattr(old_value, "Craft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Craft"):
                opp_val = getattr(value, "Craft", None)
                setattr(value, "Craft", self)

    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Order__Order", None)
        self.__Order = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer"):
                opp_val = getattr(old_value, "customer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer"):
                opp_val = getattr(value, "customer", None)
                if opp_val is None:
                    setattr(value, "customer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bestellungen(self):
        return self.__bestellungen

    @bestellungen.setter
    def bestellungen(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Order__bestellungen", None)
        self.__bestellungen = value
        
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
    def Order12(self):
        return self.__Order12

    @Order12.setter
    def Order12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Order__Order12", None)
        self.__Order12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "craft"):
                opp_val = getattr(old_value, "craft", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "craft"):
                opp_val = getattr(value, "craft", None)
                if opp_val is None:
                    setattr(value, "craft", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CarRentalModel_Customer:

    def __init__(self, identifier: str, lastname: str, surname: str, CarRentalModel_Customer: "CarRentalModel_CarRental" = None, customer: set["CarRentalModel_Order"] = None, Customer: "CarRentalModel_Order" = None):
        self.identifier = identifier
        self.lastname = lastname
        self.surname = surname
        self.CarRentalModel_Customer = CarRentalModel_Customer
        self.customer = customer if customer is not None else set()
        self.Customer = Customer
        
    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def CarRentalModel_Customer(self):
        return self.__CarRentalModel_Customer

    @CarRentalModel_Customer.setter
    def CarRentalModel_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Customer__CarRentalModel_Customer", None)
        self.__CarRentalModel_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRentalModel_CarRental"):
                opp_val = getattr(old_value, "CarRentalModel_CarRental", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRentalModel_CarRental"):
                opp_val = getattr(value, "CarRentalModel_CarRental", None)
                if opp_val is None:
                    setattr(value, "CarRentalModel_CarRental", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Customer__customer", None)
        self.__customer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order"):
                    opp_val = getattr(item, "Order", None)
                    
                    if opp_val == self:
                        setattr(item, "Order", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order"):
                    opp_val = getattr(item, "Order", None)
                    
                    setattr(item, "Order", self)
                    

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bestellungen"):
                opp_val = getattr(old_value, "bestellungen", None)
                if opp_val == self:
                    setattr(old_value, "bestellungen", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bestellungen"):
                opp_val = getattr(value, "bestellungen", None)
                setattr(value, "bestellungen", self)

class CarRentalModel_CarRental:

    pass
class CarRentalModel_Craft(ABC):

    def __init__(self, vin: int, charge: float, licenseNo: str, CarRentalModel_Craft: "CarRentalModel_CarRental" = None, Craft: "CarRentalModel_Order" = None, craft: set["CarRentalModel_Order"] = None):
        self.vin = vin
        self.charge = charge
        self.licenseNo = licenseNo
        self.CarRentalModel_Craft = CarRentalModel_Craft
        self.Craft = Craft
        self.craft = craft if craft is not None else set()
        
    @property
    def charge(self) -> float:
        return self.__charge

    @charge.setter
    def charge(self, charge: float):
        self.__charge = charge

    @property
    def vin(self) -> int:
        return self.__vin

    @vin.setter
    def vin(self, vin: int):
        self.__vin = vin

    @property
    def licenseNo(self) -> str:
        return self.__licenseNo

    @licenseNo.setter
    def licenseNo(self, licenseNo: str):
        self.__licenseNo = licenseNo

    @property
    def craft(self):
        return self.__craft

    @craft.setter
    def craft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Craft__craft", None)
        self.__craft = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Order12"):
                    opp_val = getattr(item, "Order12", None)
                    
                    if opp_val == self:
                        setattr(item, "Order12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Order12"):
                    opp_val = getattr(item, "Order12", None)
                    
                    setattr(item, "Order12", self)
                    

    @property
    def CarRentalModel_Craft(self):
        return self.__CarRentalModel_Craft

    @CarRentalModel_Craft.setter
    def CarRentalModel_Craft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Craft__CarRentalModel_Craft", None)
        self.__CarRentalModel_Craft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRentalModel_CarRental4"):
                opp_val = getattr(old_value, "CarRentalModel_CarRental4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRentalModel_CarRental4"):
                opp_val = getattr(value, "CarRentalModel_CarRental4", None)
                if opp_val is None:
                    setattr(value, "CarRentalModel_CarRental4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Craft(self):
        return self.__Craft

    @Craft.setter
    def Craft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Craft__Craft", None)
        self.__Craft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rentBy"):
                opp_val = getattr(old_value, "rentBy", None)
                if opp_val == self:
                    setattr(old_value, "rentBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rentBy"):
                opp_val = getattr(value, "rentBy", None)
                setattr(value, "rentBy", self)

class CarRentalModel_Agency:

    def __init__(self, street: str, place: str, zip: int, CarRentalModel_Agency: "CarRentalModel_CarRental" = None, CarRentalModel_Agency7: "CarRentalModel_CarRental" = None):
        self.street = street
        self.place = place
        self.zip = zip
        self.CarRentalModel_Agency = CarRentalModel_Agency
        self.CarRentalModel_Agency7 = CarRentalModel_Agency7
        
    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def place(self) -> str:
        return self.__place

    @place.setter
    def place(self, place: str):
        self.__place = place

    @property
    def zip(self) -> int:
        return self.__zip

    @zip.setter
    def zip(self, zip: int):
        self.__zip = zip

    @property
    def CarRentalModel_Agency(self):
        return self.__CarRentalModel_Agency

    @CarRentalModel_Agency.setter
    def CarRentalModel_Agency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Agency__CarRentalModel_Agency", None)
        self.__CarRentalModel_Agency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRentalModel_CarRental2"):
                opp_val = getattr(old_value, "CarRentalModel_CarRental2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRentalModel_CarRental2"):
                opp_val = getattr(value, "CarRentalModel_CarRental2", None)
                if opp_val is None:
                    setattr(value, "CarRentalModel_CarRental2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CarRentalModel_Agency7(self):
        return self.__CarRentalModel_Agency7

    @CarRentalModel_Agency7.setter
    def CarRentalModel_Agency7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRentalModel_Agency__CarRentalModel_Agency7", None)
        self.__CarRentalModel_Agency7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRentalModel_CarRental6"):
                opp_val = getattr(old_value, "CarRentalModel_CarRental6", None)
                if opp_val == self:
                    setattr(old_value, "CarRentalModel_CarRental6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRentalModel_CarRental6"):
                opp_val = getattr(value, "CarRentalModel_CarRental6", None)
                setattr(value, "CarRentalModel_CarRental6", self)
