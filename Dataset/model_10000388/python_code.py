from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Actor:

    def __init__(self, name: str, username: str, password: str, listing0: set["Listing"] = None):
        self.name = name
        self.username = username
        self.password = password
        self.listing0 = listing0 if listing0 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def listing0(self):
        return self.__listing0
    @listing0.setter
    def listing0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Actor__listing0", None)
        self.__listing0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actor1"):
                    opp_val = getattr(item, "actor1", None)
                    
                    if opp_val == self:
                        setattr(item, "actor1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actor1"):
                    opp_val = getattr(item, "actor1", None)
                    
                    setattr(item, "actor1", self)
                    






class Administrator:

    pass


class RegisteredUser:

    pass


class RealEstateAgent:

    def __init__(self, listings: str):
        self.listings = listings
        
        pass
    @property
    def listings(self):
        return self.__listings
    @listings.setter
    def listings(self, listings: str):
        self.__listings = listings



class House:

    def __init__(self, numberOfFloors: int, sizeOfProperty: int, price: int, fees: int):
        self.numberOfFloors = numberOfFloors
        self.sizeOfProperty = sizeOfProperty
        self.price = price
        self.fees = fees
        
        pass
    @property
    def sizeOfProperty(self):
        return self.__sizeOfProperty
    @sizeOfProperty.setter
    def sizeOfProperty(self, sizeOfProperty: int):
        self.__sizeOfProperty = sizeOfProperty

    @property
    def numberOfFloors(self):
        return self.__numberOfFloors
    @numberOfFloors.setter
    def numberOfFloors(self, numberOfFloors: int):
        self.__numberOfFloors = numberOfFloors

    @property
    def fees(self):
        return self.__fees
    @fees.setter
    def fees(self, fees: int):
        self.__fees = fees

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price



class Apartment:

    def __init__(self, size: int, lease: int, securityDeposit: int, monthlyRent: int):
        self.size = size
        self.lease = lease
        self.securityDeposit = securityDeposit
        self.monthlyRent = monthlyRent
        
        pass
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def lease(self):
        return self.__lease
    @lease.setter
    def lease(self, lease: int):
        self.__lease = lease

    @property
    def securityDeposit(self):
        return self.__securityDeposit
    @securityDeposit.setter
    def securityDeposit(self, securityDeposit: int):
        self.__securityDeposit = securityDeposit

    @property
    def monthlyRent(self):
        return self.__monthlyRent
    @monthlyRent.setter
    def monthlyRent(self, monthlyRent: int):
        self.__monthlyRent = monthlyRent



class Listing:

    def __init__(self, address: str, numberOfBedroms: int, numberOfBathrooms: int, kitchen: int, livingRooom: int, furnished: bool, parkingPossibilities: int, image: str, video: str, actor1: "Actor" = None):
        self.address = address
        self.numberOfBedroms = numberOfBedroms
        self.numberOfBathrooms = numberOfBathrooms
        self.kitchen = kitchen
        self.livingRooom = livingRooom
        self.furnished = furnished
        self.parkingPossibilities = parkingPossibilities
        self.image = image
        self.video = video
        self.actor1 = actor1
        
        pass
    @property
    def numberOfBathrooms(self):
        return self.__numberOfBathrooms
    @numberOfBathrooms.setter
    def numberOfBathrooms(self, numberOfBathrooms: int):
        self.__numberOfBathrooms = numberOfBathrooms

    @property
    def kitchen(self):
        return self.__kitchen
    @kitchen.setter
    def kitchen(self, kitchen: int):
        self.__kitchen = kitchen

    @property
    def video(self):
        return self.__video
    @video.setter
    def video(self, video: str):
        self.__video = video

    @property
    def livingRooom(self):
        return self.__livingRooom
    @livingRooom.setter
    def livingRooom(self, livingRooom: int):
        self.__livingRooom = livingRooom

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def furnished(self):
        return self.__furnished
    @furnished.setter
    def furnished(self, furnished: bool):
        self.__furnished = furnished

    @property
    def numberOfBedroms(self):
        return self.__numberOfBedroms
    @numberOfBedroms.setter
    def numberOfBedroms(self, numberOfBedroms: int):
        self.__numberOfBedroms = numberOfBedroms

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def parkingPossibilities(self):
        return self.__parkingPossibilities
    @parkingPossibilities.setter
    def parkingPossibilities(self, parkingPossibilities: int):
        self.__parkingPossibilities = parkingPossibilities

    @property
    def actor1(self):
        return self.__actor1
    @actor1.setter
    def actor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Listing__actor1", None)
        self.__actor1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "listing0"):
                opp_val = getattr(old_value, "listing0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "listing0"):
                opp_val = getattr(value, "listing0", None)
                if opp_val is None:
                    setattr(value, "listing0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

