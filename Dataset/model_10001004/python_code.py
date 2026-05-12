from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MaintenanceState(Enum):
    pass
class FlightState(Enum):
    pass

############################################
# Definition of Classes
############################################










class Captain:

    pass


class Navigator:

    pass


class CoPilot:

    pass


class Company:

    pass


class Aircraft:

    def __init__(self, state: MaintenanceState, flightState: FlightState, owns1: set["Airline"] = None, uses11: set["Flight"] = None, employs12: set["Pilot"] = None, requires14: set["CoPilot"] = None, requires16: set["Captain"] = None):
        self.state = state
        self.flightState = flightState
        self.owns1 = owns1 if owns1 is not None else set()
        self.uses11 = uses11 if uses11 is not None else set()
        self.employs12 = employs12 if employs12 is not None else set()
        self.requires14 = requires14 if requires14 is not None else set()
        self.requires16 = requires16 if requires16 is not None else set()
        
        pass
    @property
    def flightState(self):
        return self.__flightState
    @flightState.setter
    def flightState(self, flightState: FlightState):
        self.__flightState = flightState

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: MaintenanceState):
        self.__state = state

    @property
    def requires16(self):
        return self.__requires16
    @requires16.setter
    def requires16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aircraft__requires16", None)
        self.__requires16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "captains17"):
                    opp_val = getattr(item, "captains17", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "captains17"):
                    opp_val = getattr(item, "captains17", None)
                    
                    if opp_val is None:
                        setattr(item, "captains17", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def employs12(self):
        return self.__employs12
    @employs12.setter
    def employs12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aircraft__employs12", None)
        self.__employs12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pilots13"):
                    opp_val = getattr(item, "pilots13", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pilots13"):
                    opp_val = getattr(item, "pilots13", None)
                    
                    if opp_val is None:
                        setattr(item, "pilots13", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def requires14(self):
        return self.__requires14
    @requires14.setter
    def requires14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aircraft__requires14", None)
        self.__requires14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "copilots15"):
                    opp_val = getattr(item, "copilots15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "copilots15"):
                    opp_val = getattr(item, "copilots15", None)
                    
                    if opp_val is None:
                        setattr(item, "copilots15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def uses11(self):
        return self.__uses11
    @uses11.setter
    def uses11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aircraft__uses11", None)
        self.__uses11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aircraft10"):
                    opp_val = getattr(item, "aircraft10", None)
                    
                    if opp_val == self:
                        setattr(item, "aircraft10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aircraft10"):
                    opp_val = getattr(item, "aircraft10", None)
                    
                    setattr(item, "aircraft10", self)
                    

    @property
    def owns1(self):
        return self.__owns1
    @owns1.setter
    def owns1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aircraft__owns1", None)
        self.__owns1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aircraft0"):
                    opp_val = getattr(item, "aircraft0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aircraft0"):
                    opp_val = getattr(item, "aircraft0", None)
                    
                    if opp_val is None:
                        setattr(item, "aircraft0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Pilot:

    pass


class Airport:

    def __init__(self, id: str, arrives_at5: set["Flight"] = None, departs_from7: set["Flight"] = None):
        self.id = id
        self.arrives_at5 = arrives_at5 if arrives_at5 is not None else set()
        self.departs_from7 = departs_from7 if departs_from7 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def arrives_at5(self):
        return self.__arrives_at5
    @arrives_at5.setter
    def arrives_at5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Airport__arrives_at5", None)
        self.__arrives_at5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "airport4"):
                    opp_val = getattr(item, "airport4", None)
                    
                    if opp_val == self:
                        setattr(item, "airport4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "airport4"):
                    opp_val = getattr(item, "airport4", None)
                    
                    setattr(item, "airport4", self)
                    

    @property
    def departs_from7(self):
        return self.__departs_from7
    @departs_from7.setter
    def departs_from7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Airport__departs_from7", None)
        self.__departs_from7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "airport6"):
                    opp_val = getattr(item, "airport6", None)
                    
                    if opp_val == self:
                        setattr(item, "airport6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "airport6"):
                    opp_val = getattr(item, "airport6", None)
                    
                    setattr(item, "airport6", self)
                    



class Flight:

    def __init__(self, id: int, departureTime: date, arrivalTime: date, airport4: "Airport" = None, airport6: "Airport" = None, operates9: "Airline" = None, aircraft10: "Aircraft" = None):
        self.id = id
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.airport4 = airport4
        self.airport6 = airport6
        self.operates9 = operates9
        self.aircraft10 = aircraft10
        
        pass
    @property
    def departureTime(self):
        return self.__departureTime
    @departureTime.setter
    def departureTime(self, departureTime: date):
        self.__departureTime = departureTime

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def arrivalTime(self):
        return self.__arrivalTime
    @arrivalTime.setter
    def arrivalTime(self, arrivalTime: date):
        self.__arrivalTime = arrivalTime

    @property
    def operates9(self):
        return self.__operates9
    @operates9.setter
    def operates9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__operates9", None)
        self.__operates9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flight8"):
                opp_val = getattr(old_value, "flight8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flight8"):
                opp_val = getattr(value, "flight8", None)
                if opp_val is None:
                    setattr(value, "flight8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def airport6(self):
        return self.__airport6
    @airport6.setter
    def airport6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__airport6", None)
        self.__airport6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "departs_from7"):
                opp_val = getattr(old_value, "departs_from7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "departs_from7"):
                opp_val = getattr(value, "departs_from7", None)
                if opp_val is None:
                    setattr(value, "departs_from7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aircraft10(self):
        return self.__aircraft10
    @aircraft10.setter
    def aircraft10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__aircraft10", None)
        self.__aircraft10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uses11"):
                opp_val = getattr(old_value, "uses11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uses11"):
                opp_val = getattr(value, "uses11", None)
                if opp_val is None:
                    setattr(value, "uses11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def airport4(self):
        return self.__airport4
    @airport4.setter
    def airport4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__airport4", None)
        self.__airport4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arrives_at5"):
                opp_val = getattr(old_value, "arrives_at5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arrives_at5"):
                opp_val = getattr(value, "arrives_at5", None)
                if opp_val is None:
                    setattr(value, "arrives_at5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Airline:

    def __init__(self, id: str, aircraft0: set["Aircraft"] = None, flight8: set["Flight"] = None):
        self.id = id
        self.aircraft0 = aircraft0 if aircraft0 is not None else set()
        self.flight8 = flight8 if flight8 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def flight8(self):
        return self.__flight8
    @flight8.setter
    def flight8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Airline__flight8", None)
        self.__flight8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operates9"):
                    opp_val = getattr(item, "operates9", None)
                    
                    if opp_val == self:
                        setattr(item, "operates9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operates9"):
                    opp_val = getattr(item, "operates9", None)
                    
                    setattr(item, "operates9", self)
                    

    @property
    def aircraft0(self):
        return self.__aircraft0
    @aircraft0.setter
    def aircraft0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Airline__aircraft0", None)
        self.__aircraft0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "owns1"):
                    opp_val = getattr(item, "owns1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "owns1"):
                    opp_val = getattr(item, "owns1", None)
                    
                    if opp_val is None:
                        setattr(item, "owns1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

