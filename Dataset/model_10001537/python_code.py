from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Ticket:

    def __init__(self, no: int, passenger2: "Passenger" = None, checkStaff9: "CheckStaff" = None):
        self.no = no
        self.passenger2 = passenger2
        self.checkStaff9 = checkStaff9
        
        pass
    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def passenger2(self):
        return self.__passenger2
    @passenger2.setter
    def passenger2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__passenger2", None)
        self.__passenger2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket3"):
                opp_val = getattr(old_value, "ticket3", None)
                if opp_val == self:
                    setattr(old_value, "ticket3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket3"):
                opp_val = getattr(value, "ticket3", None)
                setattr(value, "ticket3", self)

    @property
    def checkStaff9(self):
        return self.__checkStaff9
    @checkStaff9.setter
    def checkStaff9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__checkStaff9", None)
        self.__checkStaff9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket8"):
                opp_val = getattr(old_value, "ticket8", None)
                if opp_val == self:
                    setattr(old_value, "ticket8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket8"):
                opp_val = getattr(value, "ticket8", None)
                setattr(value, "ticket8", self)



class Passenger:

    def __init__(self, name: str, ticket3: "Ticket" = None, checkStaff6: "CheckStaff" = None, luggage1: "Luggage" = None):
        self.name = name
        self.ticket3 = ticket3
        self.checkStaff6 = checkStaff6
        self.luggage1 = luggage1
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def checkStaff6(self):
        return self.__checkStaff6
    @checkStaff6.setter
    def checkStaff6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passenger__checkStaff6", None)
        self.__checkStaff6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passenger7"):
                opp_val = getattr(old_value, "passenger7", None)
                if opp_val == self:
                    setattr(old_value, "passenger7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passenger7"):
                opp_val = getattr(value, "passenger7", None)
                setattr(value, "passenger7", self)

    @property
    def ticket3(self):
        return self.__ticket3
    @ticket3.setter
    def ticket3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passenger__ticket3", None)
        self.__ticket3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passenger2"):
                opp_val = getattr(old_value, "passenger2", None)
                if opp_val == self:
                    setattr(old_value, "passenger2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passenger2"):
                opp_val = getattr(value, "passenger2", None)
                setattr(value, "passenger2", self)

    @property
    def luggage1(self):
        return self.__luggage1
    @luggage1.setter
    def luggage1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passenger__luggage1", None)
        self.__luggage1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passenger0"):
                opp_val = getattr(old_value, "passenger0", None)
                if opp_val == self:
                    setattr(old_value, "passenger0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passenger0"):
                opp_val = getattr(value, "passenger0", None)
                setattr(value, "passenger0", self)



class Luggage:

    def __init__(self, weight: int, checkStaff4: "CheckStaff" = None, passenger0: "Passenger" = None):
        self.weight = weight
        self.checkStaff4 = checkStaff4
        self.passenger0 = passenger0
        
        pass
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def passenger0(self):
        return self.__passenger0
    @passenger0.setter
    def passenger0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Luggage__passenger0", None)
        self.__passenger0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "luggage1"):
                opp_val = getattr(old_value, "luggage1", None)
                if opp_val == self:
                    setattr(old_value, "luggage1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "luggage1"):
                opp_val = getattr(value, "luggage1", None)
                setattr(value, "luggage1", self)

    @property
    def checkStaff4(self):
        return self.__checkStaff4
    @checkStaff4.setter
    def checkStaff4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Luggage__checkStaff4", None)
        self.__checkStaff4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "luggage5"):
                opp_val = getattr(old_value, "luggage5", None)
                if opp_val == self:
                    setattr(old_value, "luggage5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "luggage5"):
                opp_val = getattr(value, "luggage5", None)
                setattr(value, "luggage5", self)



class CheckStaff:

    def __init__(self, name: str, luggage5: "Luggage" = None, passenger7: "Passenger" = None, ticket8: "Ticket" = None):
        self.name = name
        self.luggage5 = luggage5
        self.passenger7 = passenger7
        self.ticket8 = ticket8
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def luggage5(self):
        return self.__luggage5
    @luggage5.setter
    def luggage5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CheckStaff__luggage5", None)
        self.__luggage5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkStaff4"):
                opp_val = getattr(old_value, "checkStaff4", None)
                if opp_val == self:
                    setattr(old_value, "checkStaff4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkStaff4"):
                opp_val = getattr(value, "checkStaff4", None)
                setattr(value, "checkStaff4", self)

    @property
    def passenger7(self):
        return self.__passenger7
    @passenger7.setter
    def passenger7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CheckStaff__passenger7", None)
        self.__passenger7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkStaff6"):
                opp_val = getattr(old_value, "checkStaff6", None)
                if opp_val == self:
                    setattr(old_value, "checkStaff6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkStaff6"):
                opp_val = getattr(value, "checkStaff6", None)
                setattr(value, "checkStaff6", self)

    @property
    def ticket8(self):
        return self.__ticket8
    @ticket8.setter
    def ticket8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CheckStaff__ticket8", None)
        self.__ticket8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkStaff9"):
                opp_val = getattr(old_value, "checkStaff9", None)
                if opp_val == self:
                    setattr(old_value, "checkStaff9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkStaff9"):
                opp_val = getattr(value, "checkStaff9", None)
                setattr(value, "checkStaff9", self)

