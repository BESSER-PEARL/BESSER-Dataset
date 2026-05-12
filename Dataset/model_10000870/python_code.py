from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class Seats:

    def __init__(self, SeatNumber: int, Availability: bool, plane12: set["Plane"] = None):
        self.SeatNumber = SeatNumber
        self.Availability = Availability
        self.plane12 = plane12 if plane12 is not None else set()
        
        pass
    @property
    def SeatNumber(self):
        return self.__SeatNumber
    @SeatNumber.setter
    def SeatNumber(self, SeatNumber: int):
        self.__SeatNumber = SeatNumber

    @property
    def Availability(self):
        return self.__Availability
    @Availability.setter
    def Availability(self, Availability: bool):
        self.__Availability = Availability

    @property
    def plane12(self):
        return self.__plane12
    @plane12.setter
    def plane12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Seats__plane12", None)
        self.__plane12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seats13"):
                    opp_val = getattr(item, "seats13", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seats13"):
                    opp_val = getattr(item, "seats13", None)
                    
                    if opp_val is None:
                        setattr(item, "seats13", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Reservation:

    pass


class Ticket:

    def __init__(self, TicketID: str, TicketType: str, Price: str, Gate: str, DateTime: str, flight11: set["Flight"] = None):
        self.TicketID = TicketID
        self.TicketType = TicketType
        self.Price = Price
        self.Gate = Gate
        self.DateTime = DateTime
        self.flight11 = flight11 if flight11 is not None else set()
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def Gate(self):
        return self.__Gate
    @Gate.setter
    def Gate(self, Gate: str):
        self.__Gate = Gate

    @property
    def TicketID(self):
        return self.__TicketID
    @TicketID.setter
    def TicketID(self, TicketID: str):
        self.__TicketID = TicketID

    @property
    def TicketType(self):
        return self.__TicketType
    @TicketType.setter
    def TicketType(self, TicketType: str):
        self.__TicketType = TicketType

    @property
    def DateTime(self):
        return self.__DateTime
    @DateTime.setter
    def DateTime(self, DateTime: str):
        self.__DateTime = DateTime

    @property
    def flight11(self):
        return self.__flight11
    @flight11.setter
    def flight11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__flight11", None)
        self.__flight11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ticket10"):
                    opp_val = getattr(item, "ticket10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ticket10"):
                    opp_val = getattr(item, "ticket10", None)
                    
                    if opp_val is None:
                        setattr(item, "ticket10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Airport:

    def __init__(self, AirportID: str, AirportName: str, Address: str, routes7: set["Routes"] = None):
        self.AirportID = AirportID
        self.AirportName = AirportName
        self.Address = Address
        self.routes7 = routes7 if routes7 is not None else set()
        
        pass
    @property
    def AirportName(self):
        return self.__AirportName
    @AirportName.setter
    def AirportName(self, AirportName: str):
        self.__AirportName = AirportName

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def AirportID(self):
        return self.__AirportID
    @AirportID.setter
    def AirportID(self, AirportID: str):
        self.__AirportID = AirportID

    @property
    def routes7(self):
        return self.__routes7
    @routes7.setter
    def routes7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Airport__routes7", None)
        self.__routes7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "airport6"):
                    opp_val = getattr(item, "airport6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "airport6"):
                    opp_val = getattr(item, "airport6", None)
                    
                    if opp_val is None:
                        setattr(item, "airport6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Plane:

    def __init__(self, PlaneId: str, PlaneName: str, Capacity: int, flight4: set["Flight"] = None, seats13: set["Seats"] = None):
        self.PlaneId = PlaneId
        self.PlaneName = PlaneName
        self.Capacity = Capacity
        self.flight4 = flight4 if flight4 is not None else set()
        self.seats13 = seats13 if seats13 is not None else set()
        
        pass
    @property
    def Capacity(self):
        return self.__Capacity
    @Capacity.setter
    def Capacity(self, Capacity: int):
        self.__Capacity = Capacity

    @property
    def PlaneId(self):
        return self.__PlaneId
    @PlaneId.setter
    def PlaneId(self, PlaneId: str):
        self.__PlaneId = PlaneId

    @property
    def PlaneName(self):
        return self.__PlaneName
    @PlaneName.setter
    def PlaneName(self, PlaneName: str):
        self.__PlaneName = PlaneName

    @property
    def seats13(self):
        return self.__seats13
    @seats13.setter
    def seats13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plane__seats13", None)
        self.__seats13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plane12"):
                    opp_val = getattr(item, "plane12", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plane12"):
                    opp_val = getattr(item, "plane12", None)
                    
                    if opp_val is None:
                        setattr(item, "plane12", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def flight4(self):
        return self.__flight4
    @flight4.setter
    def flight4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plane__flight4", None)
        self.__flight4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plane5"):
                    opp_val = getattr(item, "plane5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plane5"):
                    opp_val = getattr(item, "plane5", None)
                    
                    if opp_val is None:
                        setattr(item, "plane5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Routes:

    def __init__(self, RouteID: str, OriginAirport: str, DestinationAirport: str, airport6: set["Airport"] = None, flight9: set["Flight"] = None):
        self.RouteID = RouteID
        self.OriginAirport = OriginAirport
        self.DestinationAirport = DestinationAirport
        self.airport6 = airport6 if airport6 is not None else set()
        self.flight9 = flight9 if flight9 is not None else set()
        
        pass
    @property
    def OriginAirport(self):
        return self.__OriginAirport
    @OriginAirport.setter
    def OriginAirport(self, OriginAirport: str):
        self.__OriginAirport = OriginAirport

    @property
    def RouteID(self):
        return self.__RouteID
    @RouteID.setter
    def RouteID(self, RouteID: str):
        self.__RouteID = RouteID

    @property
    def DestinationAirport(self):
        return self.__DestinationAirport
    @DestinationAirport.setter
    def DestinationAirport(self, DestinationAirport: str):
        self.__DestinationAirport = DestinationAirport

    @property
    def flight9(self):
        return self.__flight9
    @flight9.setter
    def flight9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Routes__flight9", None)
        self.__flight9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "routes8"):
                    opp_val = getattr(item, "routes8", None)
                    
                    if opp_val == self:
                        setattr(item, "routes8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "routes8"):
                    opp_val = getattr(item, "routes8", None)
                    
                    setattr(item, "routes8", self)
                    

    @property
    def airport6(self):
        return self.__airport6
    @airport6.setter
    def airport6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Routes__airport6", None)
        self.__airport6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "routes7"):
                    opp_val = getattr(item, "routes7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "routes7"):
                    opp_val = getattr(item, "routes7", None)
                    
                    if opp_val is None:
                        setattr(item, "routes7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Flight:

    def __init__(self, FlightNumber: str, Date: str, reservation2: set["Reservation"] = None, plane5: set["Plane"] = None, routes8: "Routes" = None, ticket10: set["Ticket"] = None):
        self.FlightNumber = FlightNumber
        self.Date = Date
        self.reservation2 = reservation2 if reservation2 is not None else set()
        self.plane5 = plane5 if plane5 is not None else set()
        self.routes8 = routes8
        self.ticket10 = ticket10 if ticket10 is not None else set()
        
        pass
    @property
    def FlightNumber(self):
        return self.__FlightNumber
    @FlightNumber.setter
    def FlightNumber(self, FlightNumber: str):
        self.__FlightNumber = FlightNumber

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def reservation2(self):
        return self.__reservation2
    @reservation2.setter
    def reservation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__reservation2", None)
        self.__reservation2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flight3"):
                    opp_val = getattr(item, "flight3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flight3"):
                    opp_val = getattr(item, "flight3", None)
                    
                    if opp_val is None:
                        setattr(item, "flight3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def plane5(self):
        return self.__plane5
    @plane5.setter
    def plane5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__plane5", None)
        self.__plane5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flight4"):
                    opp_val = getattr(item, "flight4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flight4"):
                    opp_val = getattr(item, "flight4", None)
                    
                    if opp_val is None:
                        setattr(item, "flight4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ticket10(self):
        return self.__ticket10
    @ticket10.setter
    def ticket10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__ticket10", None)
        self.__ticket10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flight11"):
                    opp_val = getattr(item, "flight11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flight11"):
                    opp_val = getattr(item, "flight11", None)
                    
                    if opp_val is None:
                        setattr(item, "flight11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def routes8(self):
        return self.__routes8
    @routes8.setter
    def routes8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__routes8", None)
        self.__routes8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flight9"):
                opp_val = getattr(old_value, "flight9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flight9"):
                opp_val = getattr(value, "flight9", None)
                if opp_val is None:
                    setattr(value, "flight9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Customers:

    def __init__(self, IdCustomer: str, NameCustomer: str, Email: str, Password: str, reservation0: "Reservation" = None):
        self.IdCustomer = IdCustomer
        self.NameCustomer = NameCustomer
        self.Email = Email
        self.Password = Password
        self.reservation0 = reservation0
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def NameCustomer(self):
        return self.__NameCustomer
    @NameCustomer.setter
    def NameCustomer(self, NameCustomer: str):
        self.__NameCustomer = NameCustomer

    @property
    def IdCustomer(self):
        return self.__IdCustomer
    @IdCustomer.setter
    def IdCustomer(self, IdCustomer: str):
        self.__IdCustomer = IdCustomer

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def reservation0(self):
        return self.__reservation0
    @reservation0.setter
    def reservation0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customers__reservation0", None)
        self.__reservation0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customers1"):
                opp_val = getattr(old_value, "customers1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customers1"):
                opp_val = getattr(value, "customers1", None)
                if opp_val is None:
                    setattr(value, "customers1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

