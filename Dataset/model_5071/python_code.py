from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StreetType(Enum):
    Street = "Street"
    Road = "Road"


############################################
# Definition of Classes
############################################

class rental_Rental:

    def __init__(self, startDate: date, endDate: date, Rental: "rental_RentalAgency" = None, rental_Rental: "rental_Customer" = None, rental_Rental10: "rental_RentalObject" = None, rentals: "rental_RentalAgency" = None):
        self.startDate = startDate
        self.endDate = endDate
        self.Rental = Rental
        self.rental_Rental = rental_Rental
        self.rental_Rental10 = rental_Rental10
        self.rentals = rentals
        
    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def rentals(self):
        return self.__rentals

    @rentals.setter
    def rentals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Rental__rentals", None)
        self.__rentals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RentalAgency12"):
                opp_val = getattr(old_value, "RentalAgency12", None)
                if opp_val == self:
                    setattr(old_value, "RentalAgency12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RentalAgency12"):
                opp_val = getattr(value, "RentalAgency12", None)
                setattr(value, "RentalAgency12", self)

    @property
    def rental_Rental(self):
        return self.__rental_Rental

    @rental_Rental.setter
    def rental_Rental(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Rental__rental_Rental", None)
        self.__rental_Rental = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_Customer"):
                opp_val = getattr(old_value, "rental_Customer", None)
                if opp_val == self:
                    setattr(old_value, "rental_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Customer"):
                opp_val = getattr(value, "rental_Customer", None)
                setattr(value, "rental_Customer", self)

    @property
    def rental_Rental10(self):
        return self.__rental_Rental10

    @rental_Rental10.setter
    def rental_Rental10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Rental__rental_Rental10", None)
        self.__rental_Rental10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_RentalObject"):
                opp_val = getattr(old_value, "rental_RentalObject", None)
                if opp_val == self:
                    setattr(old_value, "rental_RentalObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_RentalObject"):
                opp_val = getattr(value, "rental_RentalObject", None)
                setattr(value, "rental_RentalObject", self)

    @property
    def Rental(self):
        return self.__Rental

    @Rental.setter
    def Rental(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Rental__Rental", None)
        self.__Rental = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentAgency4"):
                opp_val = getattr(old_value, "parentAgency4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentAgency4"):
                opp_val = getattr(value, "parentAgency4", None)
                if opp_val is None:
                    setattr(value, "parentAgency4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def nbDaysBooked(self) -> int:
        # TODO: Implement nbDaysBooked method
        pass

class rental_Customer:

    def __init__(self, firstName: str, lastName: str, customers: "rental_RentalAgency" = None, Customer: "rental_RentalAgency" = None, rental_Customer: "rental_Rental" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.customers = customers
        self.Customer = Customer
        self.rental_Customer = rental_Customer
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def customers(self):
        return self.__customers

    @customers.setter
    def customers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Customer__customers", None)
        self.__customers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RentalAgency"):
                opp_val = getattr(old_value, "RentalAgency", None)
                if opp_val == self:
                    setattr(old_value, "RentalAgency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RentalAgency"):
                opp_val = getattr(value, "RentalAgency", None)
                setattr(value, "RentalAgency", self)

    @property
    def rental_Customer(self):
        return self.__rental_Customer

    @rental_Customer.setter
    def rental_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Customer__rental_Customer", None)
        self.__rental_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_Rental"):
                opp_val = getattr(old_value, "rental_Rental", None)
                if opp_val == self:
                    setattr(old_value, "rental_Rental", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Rental"):
                opp_val = getattr(value, "rental_Rental", None)
                setattr(value, "rental_Rental", self)

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentAgency2"):
                opp_val = getattr(old_value, "parentAgency2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentAgency2"):
                opp_val = getattr(value, "parentAgency2", None)
                if opp_val is None:
                    setattr(value, "parentAgency2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getDisplayName(self) -> str:
        # TODO: Implement getDisplayName method
        pass

class rental_RentalObject:

    def __init__(self, ID: str, name: str, picture: str, objectsToRent: "rental_RentalAgency" = None, RentalObject: "rental_RentalAgency" = None, rental_RentalObject: "rental_Rental" = None):
        self.ID = ID
        self.name = name
        self.picture = picture
        self.objectsToRent = objectsToRent
        self.RentalObject = RentalObject
        self.rental_RentalObject = rental_RentalObject
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def picture(self) -> str:
        return self.__picture

    @picture.setter
    def picture(self, picture: str):
        self.__picture = picture

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def objectsToRent(self):
        return self.__objectsToRent

    @objectsToRent.setter
    def objectsToRent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalObject__objectsToRent", None)
        self.__objectsToRent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RentalAgency7"):
                opp_val = getattr(old_value, "RentalAgency7", None)
                if opp_val == self:
                    setattr(old_value, "RentalAgency7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RentalAgency7"):
                opp_val = getattr(value, "RentalAgency7", None)
                setattr(value, "RentalAgency7", self)

    @property
    def RentalObject(self):
        return self.__RentalObject

    @RentalObject.setter
    def RentalObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalObject__RentalObject", None)
        self.__RentalObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentAgency"):
                opp_val = getattr(old_value, "parentAgency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentAgency"):
                opp_val = getattr(value, "parentAgency", None)
                if opp_val is None:
                    setattr(value, "parentAgency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rental_RentalObject(self):
        return self.__rental_RentalObject

    @rental_RentalObject.setter
    def rental_RentalObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalObject__rental_RentalObject", None)
        self.__rental_RentalObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_Rental10"):
                opp_val = getattr(old_value, "rental_Rental10", None)
                if opp_val == self:
                    setattr(old_value, "rental_Rental10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Rental10"):
                opp_val = getattr(value, "rental_Rental10", None)
                setattr(value, "rental_Rental10", self)

    def rent(self, customer: str) -> str:
        # TODO: Implement rent method
        pass

class rental_RentalAgency:

    def __init__(self, name: str, parentAgency4: set["rental_Rental"] = None, RentalAgency: "rental_Customer" = None, RentalAgency7: "rental_RentalObject" = None, parentAgency: set["rental_RentalObject"] = None, parentAgency2: set["rental_Customer"] = None, RentalAgency12: "rental_Rental" = None):
        self.name = name
        self.parentAgency4 = parentAgency4 if parentAgency4 is not None else set()
        self.RentalAgency = RentalAgency
        self.RentalAgency7 = RentalAgency7
        self.parentAgency = parentAgency if parentAgency is not None else set()
        self.parentAgency2 = parentAgency2 if parentAgency2 is not None else set()
        self.RentalAgency12 = RentalAgency12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parentAgency4(self):
        return self.__parentAgency4

    @parentAgency4.setter
    def parentAgency4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__parentAgency4", None)
        self.__parentAgency4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rental"):
                    opp_val = getattr(item, "Rental", None)
                    
                    if opp_val == self:
                        setattr(item, "Rental", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rental"):
                    opp_val = getattr(item, "Rental", None)
                    
                    setattr(item, "Rental", self)
                    

    @property
    def RentalAgency7(self):
        return self.__RentalAgency7

    @RentalAgency7.setter
    def RentalAgency7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__RentalAgency7", None)
        self.__RentalAgency7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "objectsToRent"):
                opp_val = getattr(old_value, "objectsToRent", None)
                if opp_val == self:
                    setattr(old_value, "objectsToRent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "objectsToRent"):
                opp_val = getattr(value, "objectsToRent", None)
                setattr(value, "objectsToRent", self)

    @property
    def parentAgency(self):
        return self.__parentAgency

    @parentAgency.setter
    def parentAgency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__parentAgency", None)
        self.__parentAgency = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RentalObject"):
                    opp_val = getattr(item, "RentalObject", None)
                    
                    if opp_val == self:
                        setattr(item, "RentalObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RentalObject"):
                    opp_val = getattr(item, "RentalObject", None)
                    
                    setattr(item, "RentalObject", self)
                    

    @property
    def parentAgency2(self):
        return self.__parentAgency2

    @parentAgency2.setter
    def parentAgency2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__parentAgency2", None)
        self.__parentAgency2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer"):
                    opp_val = getattr(item, "Customer", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer"):
                    opp_val = getattr(item, "Customer", None)
                    
                    setattr(item, "Customer", self)
                    

    @property
    def RentalAgency12(self):
        return self.__RentalAgency12

    @RentalAgency12.setter
    def RentalAgency12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__RentalAgency12", None)
        self.__RentalAgency12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rentals"):
                opp_val = getattr(old_value, "rentals", None)
                if opp_val == self:
                    setattr(old_value, "rentals", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rentals"):
                opp_val = getattr(value, "rentals", None)
                setattr(value, "rentals", self)

    @property
    def RentalAgency(self):
        return self.__RentalAgency

    @RentalAgency.setter
    def RentalAgency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__RentalAgency", None)
        self.__RentalAgency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customers"):
                opp_val = getattr(old_value, "customers", None)
                if opp_val == self:
                    setattr(old_value, "customers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customers"):
                opp_val = getattr(value, "customers", None)
                setattr(value, "customers", self)

    def addObject(self, object: str):
        # TODO: Implement addObject method
        pass

    def removeCustomer(self, customer: str):
        # TODO: Implement removeCustomer method
        pass

    def addCustomer(self, customer: str):
        # TODO: Implement addCustomer method
        pass

    def removeObject(self, object: str):
        # TODO: Implement removeObject method
        pass

    def isAvailable(self, rentedObject: str, from: date, to: date) -> bool:
        # TODO: Implement isAvailable method
        pass

    def book(self, to: date, rentedObject: str, customer: str, from: date) -> str:
        # TODO: Implement book method
        pass
