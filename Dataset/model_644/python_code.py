from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Booking:

    pass
class reservationsystem_City:

    def __init__(self, id: int, name: str, abbr: str, City: "reservationsystem_Airport" = None, city: set["reservationsystem_Airport"] = None):
        self.id = id
        self.name = name
        self.abbr = abbr
        self.City = City
        self.city = city if city is not None else set()
        
    @property
    def abbr(self) -> str:
        return self.__abbr

    @abbr.setter
    def abbr(self, abbr: str):
        self.__abbr = abbr

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def City(self):
        return self.__City

    @City.setter
    def City(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_City__City", None)
        self.__City = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "airport"):
                opp_val = getattr(old_value, "airport", None)
                if opp_val == self:
                    setattr(old_value, "airport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "airport"):
                opp_val = getattr(value, "airport", None)
                setattr(value, "airport", self)

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_City__city", None)
        self.__city = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Airport"):
                    opp_val = getattr(item, "Airport", None)
                    
                    if opp_val == self:
                        setattr(item, "Airport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Airport"):
                    opp_val = getattr(item, "Airport", None)
                    
                    setattr(item, "Airport", self)
                    

class reservationsystem_Plane:

    def __init__(self, id: str, model: str, crewNum: int, capacity: int, Plane: "reservationsystem_SpecificFlight" = None, plane: set["reservationsystem_SpecificFlight"] = None, plane30: set["reservationsystem_Seat"] = None, Plane35: "reservationsystem_Seat" = None):
        self.id = id
        self.model = model
        self.crewNum = crewNum
        self.capacity = capacity
        self.Plane = Plane
        self.plane = plane if plane is not None else set()
        self.plane30 = plane30 if plane30 is not None else set()
        self.Plane35 = Plane35
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def crewNum(self) -> int:
        return self.__crewNum

    @crewNum.setter
    def crewNum(self, crewNum: int):
        self.__crewNum = crewNum

    @property
    def plane(self):
        return self.__plane

    @plane.setter
    def plane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Plane__plane", None)
        self.__plane = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecificFlight28"):
                    opp_val = getattr(item, "SpecificFlight28", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecificFlight28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecificFlight28"):
                    opp_val = getattr(item, "SpecificFlight28", None)
                    
                    setattr(item, "SpecificFlight28", self)
                    

    @property
    def Plane35(self):
        return self.__Plane35

    @Plane35.setter
    def Plane35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Plane__Plane35", None)
        self.__Plane35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seats"):
                opp_val = getattr(old_value, "seats", None)
                if opp_val == self:
                    setattr(old_value, "seats", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seats"):
                opp_val = getattr(value, "seats", None)
                setattr(value, "seats", self)

    @property
    def Plane(self):
        return self.__Plane

    @Plane.setter
    def Plane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Plane__Plane", None)
        self.__Plane = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specificFlight21"):
                opp_val = getattr(old_value, "specificFlight21", None)
                if opp_val == self:
                    setattr(old_value, "specificFlight21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specificFlight21"):
                opp_val = getattr(value, "specificFlight21", None)
                setattr(value, "specificFlight21", self)

    @property
    def plane30(self):
        return self.__plane30

    @plane30.setter
    def plane30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Plane__plane30", None)
        self.__plane30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Seat31"):
                    opp_val = getattr(item, "Seat31", None)
                    
                    if opp_val == self:
                        setattr(item, "Seat31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Seat31"):
                    opp_val = getattr(item, "Seat31", None)
                    
                    setattr(item, "Seat31", self)
                    

class reservationsystem_PaymentInfo(Booking):

    def __init__(self, id: str, createTime: date, status: int, payTime: date, type: int, cardNo: str, cardOwner: str, cardAddr: str, reservationsystem_PaymentInfo: "reservationsystem_Booking" = None):
        self.id = id
        self.createTime = createTime
        self.status = status
        self.payTime = payTime
        self.type = type
        self.cardNo = cardNo
        self.cardOwner = cardOwner
        self.cardAddr = cardAddr
        self.reservationsystem_PaymentInfo = reservationsystem_PaymentInfo
        
    @property
    def payTime(self) -> date:
        return self.__payTime

    @payTime.setter
    def payTime(self, payTime: date):
        self.__payTime = payTime

    @property
    def status(self) -> int:
        return self.__status

    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def cardNo(self) -> str:
        return self.__cardNo

    @cardNo.setter
    def cardNo(self, cardNo: str):
        self.__cardNo = cardNo

    @property
    def createTime(self) -> date:
        return self.__createTime

    @createTime.setter
    def createTime(self, createTime: date):
        self.__createTime = createTime

    @property
    def cardOwner(self) -> str:
        return self.__cardOwner

    @cardOwner.setter
    def cardOwner(self, cardOwner: str):
        self.__cardOwner = cardOwner

    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def cardAddr(self) -> str:
        return self.__cardAddr

    @cardAddr.setter
    def cardAddr(self, cardAddr: str):
        self.__cardAddr = cardAddr

    @property
    def reservationsystem_PaymentInfo(self):
        return self.__reservationsystem_PaymentInfo

    @reservationsystem_PaymentInfo.setter
    def reservationsystem_PaymentInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_PaymentInfo__reservationsystem_PaymentInfo", None)
        self.__reservationsystem_PaymentInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_Booking7"):
                opp_val = getattr(old_value, "reservationsystem_Booking7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_Booking7"):
                opp_val = getattr(value, "reservationsystem_Booking7", None)
                if opp_val is None:
                    setattr(value, "reservationsystem_Booking7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class reservationsystem_Airport:

    def __init__(self, id: int, name: str, abbr: str, reservationsystem_Airport: "reservationsystem_GeneralFlight" = None, reservationsystem_Airport18: "reservationsystem_GeneralFlight" = None, airport: "reservationsystem_City" = None, Airport: "reservationsystem_City" = None):
        self.id = id
        self.name = name
        self.abbr = abbr
        self.reservationsystem_Airport = reservationsystem_Airport
        self.reservationsystem_Airport18 = reservationsystem_Airport18
        self.airport = airport
        self.Airport = Airport
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def abbr(self) -> str:
        return self.__abbr

    @abbr.setter
    def abbr(self, abbr: str):
        self.__abbr = abbr

    @property
    def reservationsystem_Airport(self):
        return self.__reservationsystem_Airport

    @reservationsystem_Airport.setter
    def reservationsystem_Airport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Airport__reservationsystem_Airport", None)
        self.__reservationsystem_Airport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_GeneralFlight"):
                opp_val = getattr(old_value, "reservationsystem_GeneralFlight", None)
                if opp_val == self:
                    setattr(old_value, "reservationsystem_GeneralFlight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_GeneralFlight"):
                opp_val = getattr(value, "reservationsystem_GeneralFlight", None)
                setattr(value, "reservationsystem_GeneralFlight", self)

    @property
    def reservationsystem_Airport18(self):
        return self.__reservationsystem_Airport18

    @reservationsystem_Airport18.setter
    def reservationsystem_Airport18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Airport__reservationsystem_Airport18", None)
        self.__reservationsystem_Airport18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_GeneralFlight17"):
                opp_val = getattr(old_value, "reservationsystem_GeneralFlight17", None)
                if opp_val == self:
                    setattr(old_value, "reservationsystem_GeneralFlight17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_GeneralFlight17"):
                opp_val = getattr(value, "reservationsystem_GeneralFlight17", None)
                setattr(value, "reservationsystem_GeneralFlight17", self)

    @property
    def airport(self):
        return self.__airport

    @airport.setter
    def airport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Airport__airport", None)
        self.__airport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "City"):
                opp_val = getattr(old_value, "City", None)
                if opp_val == self:
                    setattr(old_value, "City", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "City"):
                opp_val = getattr(value, "City", None)
                setattr(value, "City", self)

    @property
    def Airport(self):
        return self.__Airport

    @Airport.setter
    def Airport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Airport__Airport", None)
        self.__Airport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "city"):
                opp_val = getattr(old_value, "city", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "city"):
                opp_val = getattr(value, "city", None)
                if opp_val is None:
                    setattr(value, "city", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class reservationsystem_GeneralFlight:

    def __init__(self, flightNo: str, departureTime: str, arrivalTime: str, generalFlight: set["reservationsystem_SpecificFlight"] = None, reservationsystem_GeneralFlight: "reservationsystem_Airport" = None, reservationsystem_GeneralFlight17: "reservationsystem_Airport" = None, GeneralFlight: "reservationsystem_SpecificFlight" = None):
        self.flightNo = flightNo
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.generalFlight = generalFlight if generalFlight is not None else set()
        self.reservationsystem_GeneralFlight = reservationsystem_GeneralFlight
        self.reservationsystem_GeneralFlight17 = reservationsystem_GeneralFlight17
        self.GeneralFlight = GeneralFlight
        
    @property
    def arrivalTime(self) -> str:
        return self.__arrivalTime

    @arrivalTime.setter
    def arrivalTime(self, arrivalTime: str):
        self.__arrivalTime = arrivalTime

    @property
    def flightNo(self) -> str:
        return self.__flightNo

    @flightNo.setter
    def flightNo(self, flightNo: str):
        self.__flightNo = flightNo

    @property
    def departureTime(self) -> str:
        return self.__departureTime

    @departureTime.setter
    def departureTime(self, departureTime: str):
        self.__departureTime = departureTime

    @property
    def reservationsystem_GeneralFlight(self):
        return self.__reservationsystem_GeneralFlight

    @reservationsystem_GeneralFlight.setter
    def reservationsystem_GeneralFlight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_GeneralFlight__reservationsystem_GeneralFlight", None)
        self.__reservationsystem_GeneralFlight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_Airport"):
                opp_val = getattr(old_value, "reservationsystem_Airport", None)
                if opp_val == self:
                    setattr(old_value, "reservationsystem_Airport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_Airport"):
                opp_val = getattr(value, "reservationsystem_Airport", None)
                setattr(value, "reservationsystem_Airport", self)

    @property
    def reservationsystem_GeneralFlight17(self):
        return self.__reservationsystem_GeneralFlight17

    @reservationsystem_GeneralFlight17.setter
    def reservationsystem_GeneralFlight17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_GeneralFlight__reservationsystem_GeneralFlight17", None)
        self.__reservationsystem_GeneralFlight17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_Airport18"):
                opp_val = getattr(old_value, "reservationsystem_Airport18", None)
                if opp_val == self:
                    setattr(old_value, "reservationsystem_Airport18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_Airport18"):
                opp_val = getattr(value, "reservationsystem_Airport18", None)
                setattr(value, "reservationsystem_Airport18", self)

    @property
    def GeneralFlight(self):
        return self.__GeneralFlight

    @GeneralFlight.setter
    def GeneralFlight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_GeneralFlight__GeneralFlight", None)
        self.__GeneralFlight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specificFlight"):
                opp_val = getattr(old_value, "specificFlight", None)
                if opp_val == self:
                    setattr(old_value, "specificFlight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specificFlight"):
                opp_val = getattr(value, "specificFlight", None)
                setattr(value, "specificFlight", self)

    @property
    def generalFlight(self):
        return self.__generalFlight

    @generalFlight.setter
    def generalFlight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_GeneralFlight__generalFlight", None)
        self.__generalFlight = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecificFlight14"):
                    opp_val = getattr(item, "SpecificFlight14", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecificFlight14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecificFlight14"):
                    opp_val = getattr(item, "SpecificFlight14", None)
                    
                    setattr(item, "SpecificFlight14", self)
                    

class reservationsystem_Seat:

    def __init__(self, no: str, type: int, isExit: bool, Seat: "reservationsystem_Booking" = None, Seat31: "reservationsystem_Plane" = None, seats: "reservationsystem_Plane" = None, seats37: "reservationsystem_Booking" = None):
        self.no = no
        self.type = type
        self.isExit = isExit
        self.Seat = Seat
        self.Seat31 = Seat31
        self.seats = seats
        self.seats37 = seats37
        
    @property
    def no(self) -> str:
        return self.__no

    @no.setter
    def no(self, no: str):
        self.__no = no

    @property
    def isExit(self) -> bool:
        return self.__isExit

    @isExit.setter
    def isExit(self, isExit: bool):
        self.__isExit = isExit

    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def Seat(self):
        return self.__Seat

    @Seat.setter
    def Seat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Seat__Seat", None)
        self.__Seat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book"):
                opp_val = getattr(old_value, "book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book"):
                opp_val = getattr(value, "book", None)
                if opp_val is None:
                    setattr(value, "book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Seat31(self):
        return self.__Seat31

    @Seat31.setter
    def Seat31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Seat__Seat31", None)
        self.__Seat31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plane30"):
                opp_val = getattr(old_value, "plane30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plane30"):
                opp_val = getattr(value, "plane30", None)
                if opp_val is None:
                    setattr(value, "plane30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def seats37(self):
        return self.__seats37

    @seats37.setter
    def seats37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Seat__seats37", None)
        self.__seats37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Booking38"):
                opp_val = getattr(old_value, "Booking38", None)
                if opp_val == self:
                    setattr(old_value, "Booking38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Booking38"):
                opp_val = getattr(value, "Booking38", None)
                setattr(value, "Booking38", self)

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Seat__seats", None)
        self.__seats = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Plane35"):
                opp_val = getattr(old_value, "Plane35", None)
                if opp_val == self:
                    setattr(old_value, "Plane35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Plane35"):
                opp_val = getattr(value, "Plane35", None)
                setattr(value, "Plane35", self)

class Person:

    pass
class Crew:

    pass
class reservationsystem_Attendant(Crew):

    pass
class reservationsystem_Pilot(Crew):

    def __init__(self, certificationId: str, experience: int):
        self.certificationId = certificationId
        self.experience = experience
        
    @property
    def experience(self) -> int:
        return self.__experience

    @experience.setter
    def experience(self, experience: int):
        self.__experience = experience

    @property
    def certificationId(self) -> str:
        return self.__certificationId

    @certificationId.setter
    def certificationId(self, certificationId: str):
        self.__certificationId = certificationId

class reservationsystem_Booking:

    def __init__(self, bookNo: str, bookingStatus: int, baggageInfo: str, reservationsystem_Booking: "reservationsystem_Passenger" = None, Booking: "reservationsystem_Passenger" = None, booking: set["reservationsystem_Passenger"] = None, booking10: set["reservationsystem_SpecificFlight"] = None, book: set["reservationsystem_Seat"] = None, reservationsystem_Booking7: set["reservationsystem_PaymentInfo"] = None, Booking26: "reservationsystem_SpecificFlight" = None, Booking38: "reservationsystem_Seat" = None):
        self.bookNo = bookNo
        self.bookingStatus = bookingStatus
        self.baggageInfo = baggageInfo
        self.reservationsystem_Booking = reservationsystem_Booking
        self.Booking = Booking
        self.booking = booking if booking is not None else set()
        self.booking10 = booking10 if booking10 is not None else set()
        self.book = book if book is not None else set()
        self.reservationsystem_Booking7 = reservationsystem_Booking7 if reservationsystem_Booking7 is not None else set()
        self.Booking26 = Booking26
        self.Booking38 = Booking38
        
    @property
    def baggageInfo(self) -> str:
        return self.__baggageInfo

    @baggageInfo.setter
    def baggageInfo(self, baggageInfo: str):
        self.__baggageInfo = baggageInfo

    @property
    def bookNo(self) -> str:
        return self.__bookNo

    @bookNo.setter
    def bookNo(self, bookNo: str):
        self.__bookNo = bookNo

    @property
    def bookingStatus(self) -> int:
        return self.__bookingStatus

    @bookingStatus.setter
    def bookingStatus(self, bookingStatus: int):
        self.__bookingStatus = bookingStatus

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Booking__book", None)
        self.__book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Seat"):
                    opp_val = getattr(item, "Seat", None)
                    
                    if opp_val == self:
                        setattr(item, "Seat", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Seat"):
                    opp_val = getattr(item, "Seat", None)
                    
                    setattr(item, "Seat", self)
                    

    @property
    def booking(self):
        return self.__booking

    @booking.setter
    def booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Booking__booking", None)
        self.__booking = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Passenger"):
                    opp_val = getattr(item, "Passenger", None)
                    
                    if opp_val == self:
                        setattr(item, "Passenger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Passenger"):
                    opp_val = getattr(item, "Passenger", None)
                    
                    setattr(item, "Passenger", self)
                    

    @property
    def Booking(self):
        return self.__Booking

    @Booking.setter
    def Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Booking__Booking", None)
        self.__Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passenger"):
                opp_val = getattr(old_value, "passenger", None)
                if opp_val == self:
                    setattr(old_value, "passenger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passenger"):
                opp_val = getattr(value, "passenger", None)
                setattr(value, "passenger", self)

    @property
    def Booking38(self):
        return self.__Booking38

    @Booking38.setter
    def Booking38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Booking__Booking38", None)
        self.__Booking38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seats37"):
                opp_val = getattr(old_value, "seats37", None)
                if opp_val == self:
                    setattr(old_value, "seats37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seats37"):
                opp_val = getattr(value, "seats37", None)
                setattr(value, "seats37", self)

    @property
    def booking10(self):
        return self.__booking10

    @booking10.setter
    def booking10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Booking__booking10", None)
        self.__booking10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecificFlight11"):
                    opp_val = getattr(item, "SpecificFlight11", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecificFlight11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecificFlight11"):
                    opp_val = getattr(item, "SpecificFlight11", None)
                    
                    setattr(item, "SpecificFlight11", self)
                    

    @property
    def Booking26(self):
        return self.__Booking26

    @Booking26.setter
    def Booking26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Booking__Booking26", None)
        self.__Booking26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specificFlight25"):
                opp_val = getattr(old_value, "specificFlight25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specificFlight25"):
                opp_val = getattr(value, "specificFlight25", None)
                if opp_val is None:
                    setattr(value, "specificFlight25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reservationsystem_Booking7(self):
        return self.__reservationsystem_Booking7

    @reservationsystem_Booking7.setter
    def reservationsystem_Booking7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Booking__reservationsystem_Booking7", None)
        self.__reservationsystem_Booking7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reservationsystem_PaymentInfo"):
                    opp_val = getattr(item, "reservationsystem_PaymentInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "reservationsystem_PaymentInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reservationsystem_PaymentInfo"):
                    opp_val = getattr(item, "reservationsystem_PaymentInfo", None)
                    
                    setattr(item, "reservationsystem_PaymentInfo", self)
                    

    @property
    def reservationsystem_Booking(self):
        return self.__reservationsystem_Booking

    @reservationsystem_Booking.setter
    def reservationsystem_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Booking__reservationsystem_Booking", None)
        self.__reservationsystem_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_Passenger"):
                opp_val = getattr(old_value, "reservationsystem_Passenger", None)
                if opp_val == self:
                    setattr(old_value, "reservationsystem_Passenger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_Passenger"):
                opp_val = getattr(value, "reservationsystem_Passenger", None)
                setattr(value, "reservationsystem_Passenger", self)

class reservationsystem_Passenger(Person):

    def __init__(self, specialNeeds: str, foodPref: str, reservationsystem_Passenger: "reservationsystem_Booking" = None, passenger: "reservationsystem_Booking" = None, Passenger: "reservationsystem_Booking" = None):
        self.specialNeeds = specialNeeds
        self.foodPref = foodPref
        self.reservationsystem_Passenger = reservationsystem_Passenger
        self.passenger = passenger
        self.Passenger = Passenger
        
    @property
    def specialNeeds(self) -> str:
        return self.__specialNeeds

    @specialNeeds.setter
    def specialNeeds(self, specialNeeds: str):
        self.__specialNeeds = specialNeeds

    @property
    def foodPref(self) -> str:
        return self.__foodPref

    @foodPref.setter
    def foodPref(self, foodPref: str):
        self.__foodPref = foodPref

    @property
    def reservationsystem_Passenger(self):
        return self.__reservationsystem_Passenger

    @reservationsystem_Passenger.setter
    def reservationsystem_Passenger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Passenger__reservationsystem_Passenger", None)
        self.__reservationsystem_Passenger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_Booking"):
                opp_val = getattr(old_value, "reservationsystem_Booking", None)
                if opp_val == self:
                    setattr(old_value, "reservationsystem_Booking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_Booking"):
                opp_val = getattr(value, "reservationsystem_Booking", None)
                setattr(value, "reservationsystem_Booking", self)

    @property
    def Passenger(self):
        return self.__Passenger

    @Passenger.setter
    def Passenger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Passenger__Passenger", None)
        self.__Passenger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking"):
                opp_val = getattr(old_value, "booking", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking"):
                opp_val = getattr(value, "booking", None)
                if opp_val is None:
                    setattr(value, "booking", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def passenger(self):
        return self.__passenger

    @passenger.setter
    def passenger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Passenger__passenger", None)
        self.__passenger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Booking"):
                opp_val = getattr(old_value, "Booking", None)
                if opp_val == self:
                    setattr(old_value, "Booking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Booking"):
                opp_val = getattr(value, "Booking", None)
                setattr(value, "Booking", self)

class reservationsystem_SpecificFlight:

    def __init__(self, id: int, date: date, realDepTime: date, realArriTime: date, status: int, SpecificFlight: "reservationsystem_Crew" = None, SpecificFlight11: "reservationsystem_Booking" = None, SpecificFlight14: "reservationsystem_GeneralFlight" = None, specificFlight: "reservationsystem_GeneralFlight" = None, specificFlight21: "reservationsystem_Plane" = None, specificFlight23: set["reservationsystem_Crew"] = None, specificFlight25: set["reservationsystem_Booking"] = None, SpecificFlight28: "reservationsystem_Plane" = None):
        self.id = id
        self.date = date
        self.realDepTime = realDepTime
        self.realArriTime = realArriTime
        self.status = status
        self.SpecificFlight = SpecificFlight
        self.SpecificFlight11 = SpecificFlight11
        self.SpecificFlight14 = SpecificFlight14
        self.specificFlight = specificFlight
        self.specificFlight21 = specificFlight21
        self.specificFlight23 = specificFlight23 if specificFlight23 is not None else set()
        self.specificFlight25 = specificFlight25 if specificFlight25 is not None else set()
        self.SpecificFlight28 = SpecificFlight28
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def realDepTime(self) -> date:
        return self.__realDepTime

    @realDepTime.setter
    def realDepTime(self, realDepTime: date):
        self.__realDepTime = realDepTime

    @property
    def realArriTime(self) -> date:
        return self.__realArriTime

    @realArriTime.setter
    def realArriTime(self, realArriTime: date):
        self.__realArriTime = realArriTime

    @property
    def status(self) -> int:
        return self.__status

    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def SpecificFlight14(self):
        return self.__SpecificFlight14

    @SpecificFlight14.setter
    def SpecificFlight14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_SpecificFlight__SpecificFlight14", None)
        self.__SpecificFlight14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalFlight"):
                opp_val = getattr(old_value, "generalFlight", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalFlight"):
                opp_val = getattr(value, "generalFlight", None)
                if opp_val is None:
                    setattr(value, "generalFlight", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SpecificFlight(self):
        return self.__SpecificFlight

    @SpecificFlight.setter
    def SpecificFlight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_SpecificFlight__SpecificFlight", None)
        self.__SpecificFlight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crew"):
                opp_val = getattr(old_value, "crew", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crew"):
                opp_val = getattr(value, "crew", None)
                if opp_val is None:
                    setattr(value, "crew", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SpecificFlight28(self):
        return self.__SpecificFlight28

    @SpecificFlight28.setter
    def SpecificFlight28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_SpecificFlight__SpecificFlight28", None)
        self.__SpecificFlight28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plane"):
                opp_val = getattr(old_value, "plane", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plane"):
                opp_val = getattr(value, "plane", None)
                if opp_val is None:
                    setattr(value, "plane", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SpecificFlight11(self):
        return self.__SpecificFlight11

    @SpecificFlight11.setter
    def SpecificFlight11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_SpecificFlight__SpecificFlight11", None)
        self.__SpecificFlight11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking10"):
                opp_val = getattr(old_value, "booking10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking10"):
                opp_val = getattr(value, "booking10", None)
                if opp_val is None:
                    setattr(value, "booking10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specificFlight23(self):
        return self.__specificFlight23

    @specificFlight23.setter
    def specificFlight23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_SpecificFlight__specificFlight23", None)
        self.__specificFlight23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Crew"):
                    opp_val = getattr(item, "Crew", None)
                    
                    if opp_val == self:
                        setattr(item, "Crew", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Crew"):
                    opp_val = getattr(item, "Crew", None)
                    
                    setattr(item, "Crew", self)
                    

    @property
    def specificFlight21(self):
        return self.__specificFlight21

    @specificFlight21.setter
    def specificFlight21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_SpecificFlight__specificFlight21", None)
        self.__specificFlight21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Plane"):
                opp_val = getattr(old_value, "Plane", None)
                if opp_val == self:
                    setattr(old_value, "Plane", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Plane"):
                opp_val = getattr(value, "Plane", None)
                setattr(value, "Plane", self)

    @property
    def specificFlight(self):
        return self.__specificFlight

    @specificFlight.setter
    def specificFlight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_SpecificFlight__specificFlight", None)
        self.__specificFlight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GeneralFlight"):
                opp_val = getattr(old_value, "GeneralFlight", None)
                if opp_val == self:
                    setattr(old_value, "GeneralFlight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GeneralFlight"):
                opp_val = getattr(value, "GeneralFlight", None)
                setattr(value, "GeneralFlight", self)

    @property
    def specificFlight25(self):
        return self.__specificFlight25

    @specificFlight25.setter
    def specificFlight25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_SpecificFlight__specificFlight25", None)
        self.__specificFlight25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Booking26"):
                    opp_val = getattr(item, "Booking26", None)
                    
                    if opp_val == self:
                        setattr(item, "Booking26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Booking26"):
                    opp_val = getattr(item, "Booking26", None)
                    
                    setattr(item, "Booking26", self)
                    

    def assignPilot(self, personId: int):
        # TODO: Implement assignPilot method
        pass

    def assignAttd(self, personId: int):
        # TODO: Implement assignAttd method
        pass

class reservationsystem_Person(ABC):

    def __init__(self, name: str, addr: str, phone: str, citizenship: str, residence: str, middleName: str, FamilyName: str, birthDate: date, id: int, passportId: str, email: str, gender: int, reservationsystem_Person: "reservationsystem_User" = None):
        self.name = name
        self.addr = addr
        self.phone = phone
        self.citizenship = citizenship
        self.residence = residence
        self.middleName = middleName
        self.FamilyName = FamilyName
        self.birthDate = birthDate
        self.id = id
        self.passportId = passportId
        self.email = email
        self.gender = gender
        self.reservationsystem_Person = reservationsystem_Person
        
    @property
    def birthDate(self) -> date:
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: date):
        self.__birthDate = birthDate

    @property
    def FamilyName(self) -> str:
        return self.__FamilyName

    @FamilyName.setter
    def FamilyName(self, FamilyName: str):
        self.__FamilyName = FamilyName

    @property
    def citizenship(self) -> str:
        return self.__citizenship

    @citizenship.setter
    def citizenship(self, citizenship: str):
        self.__citizenship = citizenship

    @property
    def residence(self) -> str:
        return self.__residence

    @residence.setter
    def residence(self, residence: str):
        self.__residence = residence

    @property
    def passportId(self) -> str:
        return self.__passportId

    @passportId.setter
    def passportId(self, passportId: str):
        self.__passportId = passportId

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def middleName(self) -> str:
        return self.__middleName

    @middleName.setter
    def middleName(self, middleName: str):
        self.__middleName = middleName

    @property
    def gender(self) -> int:
        return self.__gender

    @gender.setter
    def gender(self, gender: int):
        self.__gender = gender

    @property
    def addr(self) -> str:
        return self.__addr

    @addr.setter
    def addr(self, addr: str):
        self.__addr = addr

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def reservationsystem_Person(self):
        return self.__reservationsystem_Person

    @reservationsystem_Person.setter
    def reservationsystem_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Person__reservationsystem_Person", None)
        self.__reservationsystem_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_User"):
                opp_val = getattr(old_value, "reservationsystem_User", None)
                if opp_val == self:
                    setattr(old_value, "reservationsystem_User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_User"):
                opp_val = getattr(value, "reservationsystem_User", None)
                setattr(value, "reservationsystem_User", self)

class reservationsystem_Crew(Person):

    def __init__(self, employeeId: str, reservationsystem_Crew: "reservationsystem_Crew" = None, reservationsystem_Crew1: "reservationsystem_Crew" = None, crew: set["reservationsystem_SpecificFlight"] = None, Crew: "reservationsystem_SpecificFlight" = None):
        self.employeeId = employeeId
        self.reservationsystem_Crew = reservationsystem_Crew
        self.reservationsystem_Crew1 = reservationsystem_Crew1
        self.crew = crew if crew is not None else set()
        self.Crew = Crew
        
    @property
    def employeeId(self) -> str:
        return self.__employeeId

    @employeeId.setter
    def employeeId(self, employeeId: str):
        self.__employeeId = employeeId

    @property
    def crew(self):
        return self.__crew

    @crew.setter
    def crew(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Crew__crew", None)
        self.__crew = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecificFlight"):
                    opp_val = getattr(item, "SpecificFlight", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecificFlight", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecificFlight"):
                    opp_val = getattr(item, "SpecificFlight", None)
                    
                    setattr(item, "SpecificFlight", self)
                    

    @property
    def Crew(self):
        return self.__Crew

    @Crew.setter
    def Crew(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Crew__Crew", None)
        self.__Crew = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specificFlight23"):
                opp_val = getattr(old_value, "specificFlight23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specificFlight23"):
                opp_val = getattr(value, "specificFlight23", None)
                if opp_val is None:
                    setattr(value, "specificFlight23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reservationsystem_Crew(self):
        return self.__reservationsystem_Crew

    @reservationsystem_Crew.setter
    def reservationsystem_Crew(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Crew__reservationsystem_Crew", None)
        self.__reservationsystem_Crew = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_Crew1"):
                opp_val = getattr(old_value, "reservationsystem_Crew1", None)
                if opp_val == self:
                    setattr(old_value, "reservationsystem_Crew1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_Crew1"):
                opp_val = getattr(value, "reservationsystem_Crew1", None)
                setattr(value, "reservationsystem_Crew1", self)

    @property
    def reservationsystem_Crew1(self):
        return self.__reservationsystem_Crew1

    @reservationsystem_Crew1.setter
    def reservationsystem_Crew1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_Crew__reservationsystem_Crew1", None)
        self.__reservationsystem_Crew1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_Crew"):
                opp_val = getattr(old_value, "reservationsystem_Crew", None)
                if opp_val == self:
                    setattr(old_value, "reservationsystem_Crew", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_Crew"):
                opp_val = getattr(value, "reservationsystem_Crew", None)
                setattr(value, "reservationsystem_Crew", self)

    def setLeader(self):
        # TODO: Implement setLeader method
        pass

class reservationsystem_User:

    def __init__(self, userType: str, userName: str, md5Pwd: str, reservationsystem_User: "reservationsystem_Person" = None):
        self.userType = userType
        self.userName = userName
        self.md5Pwd = md5Pwd
        self.reservationsystem_User = reservationsystem_User
        
    @property
    def md5Pwd(self) -> str:
        return self.__md5Pwd

    @md5Pwd.setter
    def md5Pwd(self, md5Pwd: str):
        self.__md5Pwd = md5Pwd

    @property
    def userType(self) -> str:
        return self.__userType

    @userType.setter
    def userType(self, userType: str):
        self.__userType = userType

    @property
    def userName(self) -> str:
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def reservationsystem_User(self):
        return self.__reservationsystem_User

    @reservationsystem_User.setter
    def reservationsystem_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservationsystem_User__reservationsystem_User", None)
        self.__reservationsystem_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservationsystem_Person"):
                opp_val = getattr(old_value, "reservationsystem_Person", None)
                if opp_val == self:
                    setattr(old_value, "reservationsystem_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservationsystem_Person"):
                opp_val = getattr(value, "reservationsystem_Person", None)
                setattr(value, "reservationsystem_Person", self)
