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

class RentalObject:

    pass
class rental_Device(RentalObject):

    def __init__(self, serialNumber: str, width: int, height: int, length: int):
        self.serialNumber = serialNumber
        self.width = width
        self.height = height
        self.length = length
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def serialNumber(self) -> str:
        return self.__serialNumber

    @serialNumber.setter
    def serialNumber(self, serialNumber: str):
        self.__serialNumber = serialNumber

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class rental_Car(RentalObject):

    def __init__(self, licensePlate: str):
        self.licensePlate = licensePlate
        
    @property
    def licensePlate(self) -> str:
        return self.__licensePlate

    @licensePlate.setter
    def licensePlate(self, licensePlate: str):
        self.__licensePlate = licensePlate

class rental_License:

    def __init__(self, number: int, validityDate: date, licenses: "rental_Customer" = None, rental_License: "rental_Customer" = None, License: "rental_Customer" = None):
        self.number = number
        self.validityDate = validityDate
        self.licenses = licenses
        self.rental_License = rental_License
        self.License = License
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def validityDate(self) -> date:
        return self.__validityDate

    @validityDate.setter
    def validityDate(self, validityDate: date):
        self.__validityDate = validityDate

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

    @property
    def rental_License(self):
        return self.__rental_License

    @rental_License.setter
    def rental_License(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_License__rental_License", None)
        self.__rental_License = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_Customer15"):
                opp_val = getattr(old_value, "rental_Customer15", None)
                if opp_val == self:
                    setattr(old_value, "rental_Customer15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Customer15"):
                opp_val = getattr(value, "rental_Customer15", None)
                setattr(value, "rental_Customer15", self)

    def isValid(self) -> bool:
        # TODO: Implement isValid method
        pass

class rental_Address:

    def __init__(self, streetType: str, number: int, zipCode: str, city: str, streetName: str, rental_Address: "rental_RentalAgency" = None, rental_Address7: "rental_Customer" = None):
        self.streetType = streetType
        self.number = number
        self.zipCode = zipCode
        self.city = city
        self.streetName = streetName
        self.rental_Address = rental_Address
        self.rental_Address7 = rental_Address7
        
    @property
    def streetType(self) -> str:
        return self.__streetType

    @streetType.setter
    def streetType(self, streetType: str):
        self.__streetType = streetType

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def zipCode(self) -> str:
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def streetName(self) -> str:
        return self.__streetName

    @streetName.setter
    def streetName(self, streetName: str):
        self.__streetName = streetName

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
    def rental_Address7(self):
        return self.__rental_Address7

    @rental_Address7.setter
    def rental_Address7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Address__rental_Address7", None)
        self.__rental_Address7 = value
        
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

class rental_RentalAgency:

    def __init__(self, name: str, parentAgency: set["rental_RentalObject"] = None, parentAgency3: set["rental_Customer"] = None, parentAgency5: set["rental_Rental"] = None, rental_RentalAgency: "rental_Address" = None, RentalAgency: "rental_Customer" = None, RentalAgency11: "rental_RentalObject" = None, RentalAgency21: "rental_Rental" = None):
        self.name = name
        self.parentAgency = parentAgency if parentAgency is not None else set()
        self.parentAgency3 = parentAgency3 if parentAgency3 is not None else set()
        self.parentAgency5 = parentAgency5 if parentAgency5 is not None else set()
        self.rental_RentalAgency = rental_RentalAgency
        self.RentalAgency = RentalAgency
        self.RentalAgency11 = RentalAgency11
        self.RentalAgency21 = RentalAgency21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parentAgency3(self):
        return self.__parentAgency3

    @parentAgency3.setter
    def parentAgency3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__parentAgency3", None)
        self.__parentAgency3 = value if value is not None else set()
        
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
    def rental_RentalAgency(self):
        return self.__rental_RentalAgency

    @rental_RentalAgency.setter
    def rental_RentalAgency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__rental_RentalAgency", None)
        self.__rental_RentalAgency = value
        
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
    def RentalAgency21(self):
        return self.__RentalAgency21

    @RentalAgency21.setter
    def RentalAgency21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__RentalAgency21", None)
        self.__RentalAgency21 = value
        
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
    def parentAgency5(self):
        return self.__parentAgency5

    @parentAgency5.setter
    def parentAgency5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_RentalAgency__parentAgency5", None)
        self.__parentAgency5 = value if value is not None else set()
        
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
                    

    def isAvailable(self, to: date, rentedObject: str, from: date) -> bool:
        # TODO: Implement isAvailable method
        pass

    def book(self, customer: str, rentedObject: str, from: date, to: date) -> str:
        # TODO: Implement book method
        pass

class rental_Rental:

    def __init__(self, startDate: date, endDate: date, Rental: "rental_RentalAgency" = None, rental_Rental: "rental_Customer" = None, rental_Rental19: "rental_RentalObject" = None, rentals: "rental_RentalAgency" = None):
        self.startDate = startDate
        self.endDate = endDate
        self.Rental = Rental
        self.rental_Rental = rental_Rental
        self.rental_Rental19 = rental_Rental19
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
            if hasattr(old_value, "RentalAgency21"):
                opp_val = getattr(old_value, "RentalAgency21", None)
                if opp_val == self:
                    setattr(old_value, "RentalAgency21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RentalAgency21"):
                opp_val = getattr(value, "RentalAgency21", None)
                setattr(value, "RentalAgency21", self)

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
            if hasattr(old_value, "parentAgency5"):
                opp_val = getattr(old_value, "parentAgency5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentAgency5"):
                opp_val = getattr(value, "parentAgency5", None)
                if opp_val is None:
                    setattr(value, "parentAgency5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rental_Rental19(self):
        return self.__rental_Rental19

    @rental_Rental19.setter
    def rental_Rental19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Rental__rental_Rental19", None)
        self.__rental_Rental19 = value
        
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
    def rental_Rental(self):
        return self.__rental_Rental

    @rental_Rental.setter
    def rental_Rental(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Rental__rental_Rental", None)
        self.__rental_Rental = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_Customer17"):
                opp_val = getattr(old_value, "rental_Customer17", None)
                if opp_val == self:
                    setattr(old_value, "rental_Customer17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Customer17"):
                opp_val = getattr(value, "rental_Customer17", None)
                setattr(value, "rental_Customer17", self)

    def nbDaysBooked(self) -> int:
        # TODO: Implement nbDaysBooked method
        pass

class rental_Customer:

    def __init__(self, firstName: str, lastName: str, Customer: "rental_RentalAgency" = None, Customer13: "rental_License" = None, rental_Customer15: "rental_License" = None, rental_Customer17: "rental_Rental" = None, rental_Customer: "rental_Address" = None, owner: set["rental_License"] = None, customers: "rental_RentalAgency" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.Customer = Customer
        self.Customer13 = Customer13
        self.rental_Customer15 = rental_Customer15
        self.rental_Customer17 = rental_Customer17
        self.rental_Customer = rental_Customer
        self.owner = owner if owner is not None else set()
        self.customers = customers
        
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
    def rental_Customer(self):
        return self.__rental_Customer

    @rental_Customer.setter
    def rental_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Customer__rental_Customer", None)
        self.__rental_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_Address7"):
                opp_val = getattr(old_value, "rental_Address7", None)
                if opp_val == self:
                    setattr(old_value, "rental_Address7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Address7"):
                opp_val = getattr(value, "rental_Address7", None)
                setattr(value, "rental_Address7", self)

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
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentAgency3"):
                opp_val = getattr(old_value, "parentAgency3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentAgency3"):
                opp_val = getattr(value, "parentAgency3", None)
                if opp_val is None:
                    setattr(value, "parentAgency3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rental_Customer15(self):
        return self.__rental_Customer15

    @rental_Customer15.setter
    def rental_Customer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Customer__rental_Customer15", None)
        self.__rental_Customer15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental_License"):
                opp_val = getattr(old_value, "rental_License", None)
                if opp_val == self:
                    setattr(old_value, "rental_License", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_License"):
                opp_val = getattr(value, "rental_License", None)
                setattr(value, "rental_License", self)

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
    def rental_Customer17(self):
        return self.__rental_Customer17

    @rental_Customer17.setter
    def rental_Customer17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rental_Customer__rental_Customer17", None)
        self.__rental_Customer17 = value
        
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

    def addLicense(self, license: str):
        # TODO: Implement addLicense method
        pass

    def getDisplayName(self) -> str:
        # TODO: Implement getDisplayName method
        pass

class rental_RentalObject:

    def __init__(self, ID: str, name: str, available: bool, RentalObject: "rental_RentalAgency" = None, objectsToRent: "rental_RentalAgency" = None, rental_RentalObject: "rental_Rental" = None):
        self.ID = ID
        self.name = name
        self.available = available
        self.RentalObject = RentalObject
        self.objectsToRent = objectsToRent
        self.rental_RentalObject = rental_RentalObject
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def available(self) -> bool:
        return self.__available

    @available.setter
    def available(self, available: bool):
        self.__available = available

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "rental_Rental19"):
                opp_val = getattr(old_value, "rental_Rental19", None)
                if opp_val == self:
                    setattr(old_value, "rental_Rental19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental_Rental19"):
                opp_val = getattr(value, "rental_Rental19", None)
                setattr(value, "rental_Rental19", self)

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

    def rent(self, customer: str) -> str:
        # TODO: Implement rent method
        pass
