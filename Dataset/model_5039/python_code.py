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

class rental_RentalObject:

    def __init__(self, ID: str, name: str, picture: str, objectsToRent: "rental_RentalAgency" = None, RentalObject: "rental_RentalAgency" = None, rental_RentalObject: "rental_Rental" = None):
        self.ID = ID
        self.name = name
        self.picture = picture
        self.objectsToRent = objectsToRent
        self.RentalObject = RentalObject
        self.rental_RentalObject = rental_RentalObject
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def picture(self) -> str:
        return self.__picture

    @picture.setter
    def picture(self, picture: str):
        self.__picture = picture

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "RentalAgency11"):
                opp_val = getattr(old_value, "RentalAgency11", None)
                if opp_val == self:
                    setattr(old_value, "RentalAgency11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RentalAgency11"):
                opp_val = getattr(value, "RentalAgency11", None)
                setattr(value, "RentalAgency11", self)

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
            if hasattr(old_value, "rental_Rental18"):
                opp_val = getattr(old_value, "rental_Rental18", None)
                if opp_val == self:
                    setattr(old_value, "rental_Rental18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Rental18"):
                opp_val = getattr(value, "rental_Rental18", None)
                setattr(value, "rental_Rental18", self)

    def rent(self, customer: str) -> str:
        # TODO: Implement rent method
        pass

    def isAvailable(self) -> bool:
        # TODO: Implement isAvailable method
        pass

class rental_RentalAgency:

    def __init__(self, name: str, parentAgency7: set["rental_Customer"] = None, rental_RentalAgency9: set["rental_Rental"] = None, RentalAgency11: "rental_RentalObject" = None, RentalAgency: "rental_Customer" = None, rental_RentalAgency: "rental_Address" = None, parentAgency: set["rental_RentalObject"] = None, rental_RentalAgency21: "rental_Rental" = None):
        self.name = name
        self.parentAgency7 = parentAgency7 if parentAgency7 is not None else set()
        self.rental_RentalAgency9 = rental_RentalAgency9 if rental_RentalAgency9 is not None else set()
        self.RentalAgency11 = RentalAgency11
        self.RentalAgency = RentalAgency
        self.rental_RentalAgency = rental_RentalAgency
        self.parentAgency = parentAgency if parentAgency is not None else set()
        self.rental_RentalAgency21 = rental_RentalAgency21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def parentAgency7(self):
        return self.__parentAgency7

    @parentAgency7.setter
    def parentAgency7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__parentAgency7", None)
        self.__parentAgency7 = value if value is not None else set()
        
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
    def rental_RentalAgency(self):
        return self.__rental_RentalAgency

    @rental_RentalAgency.setter
    def rental_RentalAgency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__rental_RentalAgency", None)
        self.__rental_RentalAgency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_Address4"):
                opp_val = getattr(old_value, "rental_Address4", None)
                if opp_val == self:
                    setattr(old_value, "rental_Address4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Address4"):
                opp_val = getattr(value, "rental_Address4", None)
                setattr(value, "rental_Address4", self)

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
    def rental_RentalAgency9(self):
        return self.__rental_RentalAgency9

    @rental_RentalAgency9.setter
    def rental_RentalAgency9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__rental_RentalAgency9", None)
        self.__rental_RentalAgency9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rental_Rental"):
                    opp_val = getattr(item, "rental_Rental", None)
                    
                    if opp_val == self:
                        setattr(item, "rental_Rental", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rental_Rental"):
                    opp_val = getattr(item, "rental_Rental", None)
                    
                    setattr(item, "rental_Rental", self)
                    

    @property
    def rental_RentalAgency21(self):
        return self.__rental_RentalAgency21

    @rental_RentalAgency21.setter
    def rental_RentalAgency21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__rental_RentalAgency21", None)
        self.__rental_RentalAgency21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_Rental20"):
                opp_val = getattr(old_value, "rental_Rental20", None)
                if opp_val == self:
                    setattr(old_value, "rental_Rental20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Rental20"):
                opp_val = getattr(value, "rental_Rental20", None)
                setattr(value, "rental_Rental20", self)

    @property
    def RentalAgency11(self):
        return self.__RentalAgency11

    @RentalAgency11.setter
    def RentalAgency11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__RentalAgency11", None)
        self.__RentalAgency11 = value
        
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

    def addCustomer(self, customer: str):
        # TODO: Implement addCustomer method
        pass

    def book(self, to: date, rentedObject: str, customer: str, from: date) -> str:
        # TODO: Implement book method
        pass

    def addObject(self, object: str):
        # TODO: Implement addObject method
        pass

class rental_License:

    def __init__(self, number: int, validityDate: date, License: "rental_Customer" = None, licenses: "rental_Customer" = None):
        self.number = number
        self.validityDate = validityDate
        self.License = License
        self.licenses = licenses
        
    @property
    def validityDate(self) -> date:
        return self.__validityDate

    @validityDate.setter
    def validityDate(self, validityDate: date):
        self.__validityDate = validityDate

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def License(self):
        return self.__License

    @License.setter
    def License(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_License__License", None)
        self.__License = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def licenses(self):
        return self.__licenses

    @licenses.setter
    def licenses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_License__licenses", None)
        self.__licenses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer13"):
                opp_val = getattr(old_value, "Customer13", None)
                if opp_val == self:
                    setattr(old_value, "Customer13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer13"):
                opp_val = getattr(value, "Customer13", None)
                setattr(value, "Customer13", self)

class rental_Address:

    def __init__(self, streetType: str, number: int, zipCode: str, city: str, streetName: str, rental_Address: "rental_Customer" = None, rental_Address4: "rental_RentalAgency" = None):
        self.streetType = streetType
        self.number = number
        self.zipCode = zipCode
        self.city = city
        self.streetName = streetName
        self.rental_Address = rental_Address
        self.rental_Address4 = rental_Address4
        
    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def streetType(self) -> str:
        return self.__streetType

    @streetType.setter
    def streetType(self, streetType: str):
        self.__streetType = streetType

    @property
    def streetName(self) -> str:
        return self.__streetName

    @streetName.setter
    def streetName(self, streetName: str):
        self.__streetName = streetName

    @property
    def zipCode(self) -> str:
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode

    @property
    def rental_Address4(self):
        return self.__rental_Address4

    @rental_Address4.setter
    def rental_Address4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Address__rental_Address4", None)
        self.__rental_Address4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_RentalAgency"):
                opp_val = getattr(old_value, "rental_RentalAgency", None)
                if opp_val == self:
                    setattr(old_value, "rental_RentalAgency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_RentalAgency"):
                opp_val = getattr(value, "rental_RentalAgency", None)
                setattr(value, "rental_RentalAgency", self)

    @property
    def rental_Address(self):
        return self.__rental_Address

    @rental_Address.setter
    def rental_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Address__rental_Address", None)
        self.__rental_Address = value
        
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

class rental_Rental:

    def __init__(self, startDate: date, endDate: date, rental_Rental: "rental_RentalAgency" = None, rental_Rental15: "rental_Customer" = None, rental_Rental18: "rental_RentalObject" = None, rental_Rental20: "rental_RentalAgency" = None):
        self.startDate = startDate
        self.endDate = endDate
        self.rental_Rental = rental_Rental
        self.rental_Rental15 = rental_Rental15
        self.rental_Rental18 = rental_Rental18
        self.rental_Rental20 = rental_Rental20
        
    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

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
            if hasattr(old_value, "rental_RentalAgency9"):
                opp_val = getattr(old_value, "rental_RentalAgency9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_RentalAgency9"):
                opp_val = getattr(value, "rental_RentalAgency9", None)
                if opp_val is None:
                    setattr(value, "rental_RentalAgency9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rental_Rental15(self):
        return self.__rental_Rental15

    @rental_Rental15.setter
    def rental_Rental15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Rental__rental_Rental15", None)
        self.__rental_Rental15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_Customer16"):
                opp_val = getattr(old_value, "rental_Customer16", None)
                if opp_val == self:
                    setattr(old_value, "rental_Customer16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Customer16"):
                opp_val = getattr(value, "rental_Customer16", None)
                setattr(value, "rental_Customer16", self)

    @property
    def rental_Rental20(self):
        return self.__rental_Rental20

    @rental_Rental20.setter
    def rental_Rental20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Rental__rental_Rental20", None)
        self.__rental_Rental20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_RentalAgency21"):
                opp_val = getattr(old_value, "rental_RentalAgency21", None)
                if opp_val == self:
                    setattr(old_value, "rental_RentalAgency21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_RentalAgency21"):
                opp_val = getattr(value, "rental_RentalAgency21", None)
                setattr(value, "rental_RentalAgency21", self)

    @property
    def rental_Rental18(self):
        return self.__rental_Rental18

    @rental_Rental18.setter
    def rental_Rental18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Rental__rental_Rental18", None)
        self.__rental_Rental18 = value
        
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

    def nbDaysRented(self) -> int:
        # TODO: Implement nbDaysRented method
        pass

    def nbDaysBooked(self) -> int:
        # TODO: Implement nbDaysBooked method
        pass

    def end(self) -> int:
        # TODO: Implement end method
        pass

    def start(self) -> int:
        # TODO: Implement start method
        pass

class rental_Customer:

    def __init__(self, firstName: str, lastName: str, Customer: "rental_RentalAgency" = None, rental_Customer: "rental_Address" = None, owner: set["rental_License"] = None, customers: "rental_RentalAgency" = None, Customer13: "rental_License" = None, rental_Customer16: "rental_Rental" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.Customer = Customer
        self.rental_Customer = rental_Customer
        self.owner = owner if owner is not None else set()
        self.customers = customers
        self.Customer13 = Customer13
        self.rental_Customer16 = rental_Customer16
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def Customer13(self):
        return self.__Customer13

    @Customer13.setter
    def Customer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Customer__Customer13", None)
        self.__Customer13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "licenses"):
                opp_val = getattr(old_value, "licenses", None)
                if opp_val == self:
                    setattr(old_value, "licenses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "licenses"):
                opp_val = getattr(value, "licenses", None)
                setattr(value, "licenses", self)

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
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Customer__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "License"):
                    opp_val = getattr(item, "License", None)
                    
                    if opp_val == self:
                        setattr(item, "License", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "License"):
                    opp_val = getattr(item, "License", None)
                    
                    setattr(item, "License", self)
                    

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
            if hasattr(old_value, "parentAgency7"):
                opp_val = getattr(old_value, "parentAgency7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentAgency7"):
                opp_val = getattr(value, "parentAgency7", None)
                if opp_val is None:
                    setattr(value, "parentAgency7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "rental_Address"):
                opp_val = getattr(old_value, "rental_Address", None)
                if opp_val == self:
                    setattr(old_value, "rental_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Address"):
                opp_val = getattr(value, "rental_Address", None)
                setattr(value, "rental_Address", self)

    @property
    def rental_Customer16(self):
        return self.__rental_Customer16

    @rental_Customer16.setter
    def rental_Customer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Customer__rental_Customer16", None)
        self.__rental_Customer16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_Rental15"):
                opp_val = getattr(old_value, "rental_Rental15", None)
                if opp_val == self:
                    setattr(old_value, "rental_Rental15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Rental15"):
                opp_val = getattr(value, "rental_Rental15", None)
                setattr(value, "rental_Rental15", self)

    def getDisplayName(self) -> str:
        # TODO: Implement getDisplayName method
        pass
