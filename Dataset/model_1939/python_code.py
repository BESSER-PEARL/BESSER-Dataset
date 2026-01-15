from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FlightState(Enum):
    planned = "planned"
    inFlight = "inFlight"
    completed = "completed"
class TravelState(Enum):
    unknown = "unknown"
    checkedIn = "checkedIn"
    luggageDroppedOf = "luggageDroppedOf"
    onBoard = "onBoard"


############################################
# Definition of Classes
############################################

class Flights_Airports:

    pass
class Flights_Routes:

    pass
class Flights_Persons:

    pass
class Flights_Bookings:

    pass
class FlightObject:

    pass
class Flights_Gate(FlightObject):

    def __init__(self, position: int, Gate: "Flights_Flight" = None, Gate20: "Flights_Flight" = None, Flights_Gate: "Flights_Airport" = None, src60: set["Flights_Flight"] = None, trg63: set["Flights_Flight"] = None):
        self.position = position
        self.Gate = Gate
        self.Gate20 = Gate20
        self.Flights_Gate = Flights_Gate
        self.src60 = src60 if src60 is not None else set()
        self.trg63 = trg63 if trg63 is not None else set()
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def Gate20(self):
        return self.__Gate20

    @Gate20.setter
    def Gate20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Gate__Gate20", None)
        self.__Gate20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingFlights"):
                opp_val = getattr(old_value, "incomingFlights", None)
                if opp_val == self:
                    setattr(old_value, "incomingFlights", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingFlights"):
                opp_val = getattr(value, "incomingFlights", None)
                setattr(value, "incomingFlights", self)

    @property
    def src60(self):
        return self.__src60

    @src60.setter
    def src60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Gate__src60", None)
        self.__src60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Flight61"):
                    opp_val = getattr(item, "Flight61", None)
                    
                    if opp_val == self:
                        setattr(item, "Flight61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Flight61"):
                    opp_val = getattr(item, "Flight61", None)
                    
                    setattr(item, "Flight61", self)
                    

    @property
    def trg63(self):
        return self.__trg63

    @trg63.setter
    def trg63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Gate__trg63", None)
        self.__trg63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Flight64"):
                    opp_val = getattr(item, "Flight64", None)
                    
                    if opp_val == self:
                        setattr(item, "Flight64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Flight64"):
                    opp_val = getattr(item, "Flight64", None)
                    
                    setattr(item, "Flight64", self)
                    

    @property
    def Gate(self):
        return self.__Gate

    @Gate.setter
    def Gate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Gate__Gate", None)
        self.__Gate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingFlights"):
                opp_val = getattr(old_value, "outgoingFlights", None)
                if opp_val == self:
                    setattr(old_value, "outgoingFlights", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingFlights"):
                opp_val = getattr(value, "outgoingFlights", None)
                setattr(value, "outgoingFlights", self)

    @property
    def Flights_Gate(self):
        return self.__Flights_Gate

    @Flights_Gate.setter
    def Flights_Gate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Gate__Flights_Gate", None)
        self.__Flights_Gate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_Airport50"):
                opp_val = getattr(old_value, "Flights_Airport50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_Airport50"):
                opp_val = getattr(value, "Flights_Airport50", None)
                if opp_val is None:
                    setattr(value, "Flights_Airport50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Flights_Route(FlightObject):

    def __init__(self, duration: int, Flights_Route: "Flights_Routes" = None, Route: "Flights_Flight" = None, incomingRoutes: "Flights_Airport" = None, route: set["Flights_Flight"] = None, outgoingRoutes: "Flights_Airport" = None, Route54: "Flights_Airport" = None, Route52: "Flights_Airport" = None):
        self.duration = duration
        self.Flights_Route = Flights_Route
        self.Route = Route
        self.incomingRoutes = incomingRoutes
        self.route = route if route is not None else set()
        self.outgoingRoutes = outgoingRoutes
        self.Route54 = Route54
        self.Route52 = Route52
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def Route(self):
        return self.__Route

    @Route.setter
    def Route(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Route__Route", None)
        self.__Route = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flights17"):
                opp_val = getattr(old_value, "flights17", None)
                if opp_val == self:
                    setattr(old_value, "flights17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flights17"):
                opp_val = getattr(value, "flights17", None)
                setattr(value, "flights17", self)

    @property
    def route(self):
        return self.__route

    @route.setter
    def route(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Route__route", None)
        self.__route = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Flight"):
                    opp_val = getattr(item, "Flight", None)
                    
                    if opp_val == self:
                        setattr(item, "Flight", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Flight"):
                    opp_val = getattr(item, "Flight", None)
                    
                    setattr(item, "Flight", self)
                    

    @property
    def Flights_Route(self):
        return self.__Flights_Route

    @Flights_Route.setter
    def Flights_Route(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Route__Flights_Route", None)
        self.__Flights_Route = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_Routes34"):
                opp_val = getattr(old_value, "Flights_Routes34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_Routes34"):
                opp_val = getattr(value, "Flights_Routes34", None)
                if opp_val is None:
                    setattr(value, "Flights_Routes34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Route54(self):
        return self.__Route54

    @Route54.setter
    def Route54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Route__Route54", None)
        self.__Route54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trg"):
                opp_val = getattr(old_value, "trg", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trg"):
                opp_val = getattr(value, "trg", None)
                if opp_val is None:
                    setattr(value, "trg", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingRoutes(self):
        return self.__incomingRoutes

    @incomingRoutes.setter
    def incomingRoutes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Route__incomingRoutes", None)
        self.__incomingRoutes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Airport38"):
                opp_val = getattr(old_value, "Airport38", None)
                if opp_val == self:
                    setattr(old_value, "Airport38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Airport38"):
                opp_val = getattr(value, "Airport38", None)
                setattr(value, "Airport38", self)

    @property
    def Route52(self):
        return self.__Route52

    @Route52.setter
    def Route52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Route__Route52", None)
        self.__Route52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "src"):
                opp_val = getattr(old_value, "src", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "src"):
                opp_val = getattr(value, "src", None)
                if opp_val is None:
                    setattr(value, "src", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingRoutes(self):
        return self.__outgoingRoutes

    @outgoingRoutes.setter
    def outgoingRoutes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Route__outgoingRoutes", None)
        self.__outgoingRoutes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Airport"):
                opp_val = getattr(old_value, "Airport", None)
                if opp_val == self:
                    setattr(old_value, "Airport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Airport"):
                opp_val = getattr(value, "Airport", None)
                setattr(value, "Airport", self)

class Flights_Person(FlightObject):

    def __init__(self, travelState: str, Person: "Flights_Travel" = None, Flights_Person: "Flights_Persons" = None, person: set["Flights_Travel"] = None):
        self.travelState = travelState
        self.Person = Person
        self.Flights_Person = Flights_Person
        self.person = person if person is not None else set()
        
    @property
    def travelState(self) -> str:
        return self.__travelState

    @travelState.setter
    def travelState(self, travelState: str):
        self.__travelState = travelState

    @property
    def Flights_Person(self):
        return self.__Flights_Person

    @Flights_Person.setter
    def Flights_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Person__Flights_Person", None)
        self.__Flights_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_Persons44"):
                opp_val = getattr(old_value, "Flights_Persons44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_Persons44"):
                opp_val = getattr(value, "Flights_Persons44", None)
                if opp_val is None:
                    setattr(value, "Flights_Persons44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "travels42"):
                opp_val = getattr(old_value, "travels42", None)
                if opp_val == self:
                    setattr(old_value, "travels42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "travels42"):
                opp_val = getattr(value, "travels42", None)
                setattr(value, "travels42", self)

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Person__person", None)
        self.__person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Travel46"):
                    opp_val = getattr(item, "Travel46", None)
                    
                    if opp_val == self:
                        setattr(item, "Travel46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Travel46"):
                    opp_val = getattr(item, "Travel46", None)
                    
                    setattr(item, "Travel46", self)
                    

class Flights_Plane(FlightObject):

    def __init__(self, capacity: int, Plane: "Flights_Flight" = None, Flights_Plane: "Flights_Planes" = None, plane: set["Flights_Flight"] = None):
        self.capacity = capacity
        self.Plane = Plane
        self.Flights_Plane = Flights_Plane
        self.plane = plane if plane is not None else set()
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def Flights_Plane(self):
        return self.__Flights_Plane

    @Flights_Plane.setter
    def Flights_Plane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Plane__Flights_Plane", None)
        self.__Flights_Plane = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_Planes56"):
                opp_val = getattr(old_value, "Flights_Planes56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_Planes56"):
                opp_val = getattr(value, "Flights_Planes56", None)
                if opp_val is None:
                    setattr(value, "Flights_Planes56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def plane(self):
        return self.__plane

    @plane.setter
    def plane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Plane__plane", None)
        self.__plane = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Flight58"):
                    opp_val = getattr(item, "Flight58", None)
                    
                    if opp_val == self:
                        setattr(item, "Flight58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Flight58"):
                    opp_val = getattr(item, "Flight58", None)
                    
                    setattr(item, "Flight58", self)
                    

    @property
    def Plane(self):
        return self.__Plane

    @Plane.setter
    def Plane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Plane__Plane", None)
        self.__Plane = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flights22"):
                opp_val = getattr(old_value, "flights22", None)
                if opp_val == self:
                    setattr(old_value, "flights22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flights22"):
                opp_val = getattr(value, "flights22", None)
                setattr(value, "flights22", self)

class Flights_Booking(FlightObject):

    pass
class Flights_Travel(FlightObject):

    pass
class Flights_Airport(FlightObject):

    def __init__(self, size: float, Airport38: "Flights_Route" = None, Airport: "Flights_Route" = None, src: set["Flights_Route"] = None, trg: set["Flights_Route"] = None, Flights_Airport: "Flights_Airports" = None, Flights_Airport50: set["Flights_Gate"] = None):
        self.size = size
        self.Airport38 = Airport38
        self.Airport = Airport
        self.src = src if src is not None else set()
        self.trg = trg if trg is not None else set()
        self.Flights_Airport = Flights_Airport
        self.Flights_Airport50 = Flights_Airport50 if Flights_Airport50 is not None else set()
        
    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Airport__src", None)
        self.__src = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Route52"):
                    opp_val = getattr(item, "Route52", None)
                    
                    if opp_val == self:
                        setattr(item, "Route52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Route52"):
                    opp_val = getattr(item, "Route52", None)
                    
                    setattr(item, "Route52", self)
                    

    @property
    def Flights_Airport(self):
        return self.__Flights_Airport

    @Flights_Airport.setter
    def Flights_Airport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Airport__Flights_Airport", None)
        self.__Flights_Airport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_Airports48"):
                opp_val = getattr(old_value, "Flights_Airports48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_Airports48"):
                opp_val = getattr(value, "Flights_Airports48", None)
                if opp_val is None:
                    setattr(value, "Flights_Airports48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Airport38(self):
        return self.__Airport38

    @Airport38.setter
    def Airport38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Airport__Airport38", None)
        self.__Airport38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingRoutes"):
                opp_val = getattr(old_value, "incomingRoutes", None)
                if opp_val == self:
                    setattr(old_value, "incomingRoutes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingRoutes"):
                opp_val = getattr(value, "incomingRoutes", None)
                setattr(value, "incomingRoutes", self)

    @property
    def Flights_Airport50(self):
        return self.__Flights_Airport50

    @Flights_Airport50.setter
    def Flights_Airport50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Airport__Flights_Airport50", None)
        self.__Flights_Airport50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Flights_Gate"):
                    opp_val = getattr(item, "Flights_Gate", None)
                    
                    if opp_val == self:
                        setattr(item, "Flights_Gate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Flights_Gate"):
                    opp_val = getattr(item, "Flights_Gate", None)
                    
                    setattr(item, "Flights_Gate", self)
                    

    @property
    def trg(self):
        return self.__trg

    @trg.setter
    def trg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Airport__trg", None)
        self.__trg = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Route54"):
                    opp_val = getattr(item, "Route54", None)
                    
                    if opp_val == self:
                        setattr(item, "Route54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Route54"):
                    opp_val = getattr(item, "Route54", None)
                    
                    setattr(item, "Route54", self)
                    

    @property
    def Airport(self):
        return self.__Airport

    @Airport.setter
    def Airport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Airport__Airport", None)
        self.__Airport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingRoutes"):
                opp_val = getattr(old_value, "outgoingRoutes", None)
                if opp_val == self:
                    setattr(old_value, "outgoingRoutes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingRoutes"):
                opp_val = getattr(value, "outgoingRoutes", None)
                setattr(value, "outgoingRoutes", self)

class Flights_Flight(FlightObject):

    def __init__(self, newAttribute: str, Flights_Flight: "Flights_FlightContainer" = None, flights: set["Flights_Travel"] = None, Flights_Flight24: "Flights_TimeStamp" = None, Flights_Flight27: "Flights_TimeStamp" = None, flights17: "Flights_Route" = None, outgoingFlights: "Flights_Gate" = None, incomingFlights: "Flights_Gate" = None, flights22: "Flights_Plane" = None, Flight40: "Flights_Travel" = None, Flight: "Flights_Route" = None, Flight58: "Flights_Plane" = None, Flight61: "Flights_Gate" = None, Flight64: "Flights_Gate" = None):
        self.newAttribute = newAttribute
        self.Flights_Flight = Flights_Flight
        self.flights = flights if flights is not None else set()
        self.Flights_Flight24 = Flights_Flight24
        self.Flights_Flight27 = Flights_Flight27
        self.flights17 = flights17
        self.outgoingFlights = outgoingFlights
        self.incomingFlights = incomingFlights
        self.flights22 = flights22
        self.Flight40 = Flight40
        self.Flight = Flight
        self.Flight58 = Flight58
        self.Flight61 = Flight61
        self.Flight64 = Flight64
        
    @property
    def newAttribute(self) -> str:
        return self.__newAttribute

    @newAttribute.setter
    def newAttribute(self, newAttribute: str):
        self.__newAttribute = newAttribute

    @property
    def Flight(self):
        return self.__Flight

    @Flight.setter
    def Flight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__Flight", None)
        self.__Flight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "route"):
                opp_val = getattr(old_value, "route", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "route"):
                opp_val = getattr(value, "route", None)
                if opp_val is None:
                    setattr(value, "route", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingFlights(self):
        return self.__outgoingFlights

    @outgoingFlights.setter
    def outgoingFlights(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__outgoingFlights", None)
        self.__outgoingFlights = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Gate"):
                opp_val = getattr(old_value, "Gate", None)
                if opp_val == self:
                    setattr(old_value, "Gate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Gate"):
                opp_val = getattr(value, "Gate", None)
                setattr(value, "Gate", self)

    @property
    def flights17(self):
        return self.__flights17

    @flights17.setter
    def flights17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__flights17", None)
        self.__flights17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Route"):
                opp_val = getattr(old_value, "Route", None)
                if opp_val == self:
                    setattr(old_value, "Route", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Route"):
                opp_val = getattr(value, "Route", None)
                setattr(value, "Route", self)

    @property
    def flights(self):
        return self.__flights

    @flights.setter
    def flights(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__flights", None)
        self.__flights = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Travel"):
                    opp_val = getattr(item, "Travel", None)
                    
                    if opp_val == self:
                        setattr(item, "Travel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Travel"):
                    opp_val = getattr(item, "Travel", None)
                    
                    setattr(item, "Travel", self)
                    

    @property
    def Flights_Flight27(self):
        return self.__Flights_Flight27

    @Flights_Flight27.setter
    def Flights_Flight27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__Flights_Flight27", None)
        self.__Flights_Flight27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_TimeStamp28"):
                opp_val = getattr(old_value, "Flights_TimeStamp28", None)
                if opp_val == self:
                    setattr(old_value, "Flights_TimeStamp28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_TimeStamp28"):
                opp_val = getattr(value, "Flights_TimeStamp28", None)
                setattr(value, "Flights_TimeStamp28", self)

    @property
    def Flight40(self):
        return self.__Flight40

    @Flight40.setter
    def Flight40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__Flight40", None)
        self.__Flight40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "travels"):
                opp_val = getattr(old_value, "travels", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "travels"):
                opp_val = getattr(value, "travels", None)
                if opp_val is None:
                    setattr(value, "travels", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Flights_Flight24(self):
        return self.__Flights_Flight24

    @Flights_Flight24.setter
    def Flights_Flight24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__Flights_Flight24", None)
        self.__Flights_Flight24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_TimeStamp25"):
                opp_val = getattr(old_value, "Flights_TimeStamp25", None)
                if opp_val == self:
                    setattr(old_value, "Flights_TimeStamp25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_TimeStamp25"):
                opp_val = getattr(value, "Flights_TimeStamp25", None)
                setattr(value, "Flights_TimeStamp25", self)

    @property
    def flights22(self):
        return self.__flights22

    @flights22.setter
    def flights22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__flights22", None)
        self.__flights22 = value
        
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
    def Flights_Flight(self):
        return self.__Flights_Flight

    @Flights_Flight.setter
    def Flights_Flight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__Flights_Flight", None)
        self.__Flights_Flight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_FlightContainer14"):
                opp_val = getattr(old_value, "Flights_FlightContainer14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_FlightContainer14"):
                opp_val = getattr(value, "Flights_FlightContainer14", None)
                if opp_val is None:
                    setattr(value, "Flights_FlightContainer14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Flight58(self):
        return self.__Flight58

    @Flight58.setter
    def Flight58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__Flight58", None)
        self.__Flight58 = value
        
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
    def incomingFlights(self):
        return self.__incomingFlights

    @incomingFlights.setter
    def incomingFlights(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__incomingFlights", None)
        self.__incomingFlights = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Gate20"):
                opp_val = getattr(old_value, "Gate20", None)
                if opp_val == self:
                    setattr(old_value, "Gate20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Gate20"):
                opp_val = getattr(value, "Gate20", None)
                setattr(value, "Gate20", self)

    @property
    def Flight64(self):
        return self.__Flight64

    @Flight64.setter
    def Flight64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__Flight64", None)
        self.__Flight64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trg63"):
                opp_val = getattr(old_value, "trg63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trg63"):
                opp_val = getattr(value, "trg63", None)
                if opp_val is None:
                    setattr(value, "trg63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Flight61(self):
        return self.__Flight61

    @Flight61.setter
    def Flight61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_Flight__Flight61", None)
        self.__Flight61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "src60"):
                opp_val = getattr(old_value, "src60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "src60"):
                opp_val = getattr(value, "src60", None)
                if opp_val is None:
                    setattr(value, "src60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Flights_FlightObject(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class Flights_TimeStamp:

    def __init__(self, time: str, Flights_TimeStamp: "Flights_FlightModel" = None, Flights_TimeStamp25: "Flights_Flight" = None, Flights_TimeStamp28: "Flights_Flight" = None):
        self.time = time
        self.Flights_TimeStamp = Flights_TimeStamp
        self.Flights_TimeStamp25 = Flights_TimeStamp25
        self.Flights_TimeStamp28 = Flights_TimeStamp28
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def Flights_TimeStamp(self):
        return self.__Flights_TimeStamp

    @Flights_TimeStamp.setter
    def Flights_TimeStamp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_TimeStamp__Flights_TimeStamp", None)
        self.__Flights_TimeStamp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_FlightModel12"):
                opp_val = getattr(old_value, "Flights_FlightModel12", None)
                if opp_val == self:
                    setattr(old_value, "Flights_FlightModel12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_FlightModel12"):
                opp_val = getattr(value, "Flights_FlightModel12", None)
                setattr(value, "Flights_FlightModel12", self)

    @property
    def Flights_TimeStamp28(self):
        return self.__Flights_TimeStamp28

    @Flights_TimeStamp28.setter
    def Flights_TimeStamp28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_TimeStamp__Flights_TimeStamp28", None)
        self.__Flights_TimeStamp28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_Flight27"):
                opp_val = getattr(old_value, "Flights_Flight27", None)
                if opp_val == self:
                    setattr(old_value, "Flights_Flight27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_Flight27"):
                opp_val = getattr(value, "Flights_Flight27", None)
                setattr(value, "Flights_Flight27", self)

    @property
    def Flights_TimeStamp25(self):
        return self.__Flights_TimeStamp25

    @Flights_TimeStamp25.setter
    def Flights_TimeStamp25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flights_TimeStamp__Flights_TimeStamp25", None)
        self.__Flights_TimeStamp25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Flights_Flight24"):
                opp_val = getattr(old_value, "Flights_Flight24", None)
                if opp_val == self:
                    setattr(old_value, "Flights_Flight24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Flights_Flight24"):
                opp_val = getattr(value, "Flights_Flight24", None)
                setattr(value, "Flights_Flight24", self)

class Flights_Planes:

    pass
class Flights_FlightContainer:

    pass
class Flights_FlightModel:

    pass