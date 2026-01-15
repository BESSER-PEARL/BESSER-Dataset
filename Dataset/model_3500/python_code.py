from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Statement:

    pass
class sourcecode_Decision(Statement):

    pass
class sourcecode_Assignment(Statement):

    pass
class sourcecode_Program:

    pass
class sourcecode_While(Statement):

    pass
class sourcecode_Statement(ABC):

    def __init__(self, id: str, sourcecode_Statement: "sourcecode_Statement" = None, sourcecode_Statement0: "sourcecode_Statement" = None, sourcecode_Statement8: "sourcecode_While" = None, sourcecode_Statement11: "sourcecode_While" = None, sourcecode_Statement13: "sourcecode_Program" = None, sourcecode_Statement3: "sourcecode_Decision" = None, sourcecode_Statement6: "sourcecode_Decision" = None):
        self.id = id
        self.sourcecode_Statement = sourcecode_Statement
        self.sourcecode_Statement0 = sourcecode_Statement0
        self.sourcecode_Statement8 = sourcecode_Statement8
        self.sourcecode_Statement11 = sourcecode_Statement11
        self.sourcecode_Statement13 = sourcecode_Statement13
        self.sourcecode_Statement3 = sourcecode_Statement3
        self.sourcecode_Statement6 = sourcecode_Statement6
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def sourcecode_Statement3(self):
        return self.__sourcecode_Statement3

    @sourcecode_Statement3.setter
    def sourcecode_Statement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecode_Statement__sourcecode_Statement3", None)
        self.__sourcecode_Statement3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecode_Decision"):
                opp_val = getattr(old_value, "sourcecode_Decision", None)
                if opp_val == self:
                    setattr(old_value, "sourcecode_Decision", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecode_Decision"):
                opp_val = getattr(value, "sourcecode_Decision", None)
                setattr(value, "sourcecode_Decision", self)

    @property
    def sourcecode_Statement13(self):
        return self.__sourcecode_Statement13

    @sourcecode_Statement13.setter
    def sourcecode_Statement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecode_Statement__sourcecode_Statement13", None)
        self.__sourcecode_Statement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecode_Program"):
                opp_val = getattr(old_value, "sourcecode_Program", None)
                if opp_val == self:
                    setattr(old_value, "sourcecode_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecode_Program"):
                opp_val = getattr(value, "sourcecode_Program", None)
                setattr(value, "sourcecode_Program", self)

    @property
    def sourcecode_Statement11(self):
        return self.__sourcecode_Statement11

    @sourcecode_Statement11.setter
    def sourcecode_Statement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecode_Statement__sourcecode_Statement11", None)
        self.__sourcecode_Statement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecode_While10"):
                opp_val = getattr(old_value, "sourcecode_While10", None)
                if opp_val == self:
                    setattr(old_value, "sourcecode_While10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecode_While10"):
                opp_val = getattr(value, "sourcecode_While10", None)
                setattr(value, "sourcecode_While10", self)

    @property
    def sourcecode_Statement(self):
        return self.__sourcecode_Statement

    @sourcecode_Statement.setter
    def sourcecode_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecode_Statement__sourcecode_Statement", None)
        self.__sourcecode_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecode_Statement0"):
                opp_val = getattr(old_value, "sourcecode_Statement0", None)
                if opp_val == self:
                    setattr(old_value, "sourcecode_Statement0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecode_Statement0"):
                opp_val = getattr(value, "sourcecode_Statement0", None)
                setattr(value, "sourcecode_Statement0", self)

    @property
    def sourcecode_Statement6(self):
        return self.__sourcecode_Statement6

    @sourcecode_Statement6.setter
    def sourcecode_Statement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecode_Statement__sourcecode_Statement6", None)
        self.__sourcecode_Statement6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecode_Decision5"):
                opp_val = getattr(old_value, "sourcecode_Decision5", None)
                if opp_val == self:
                    setattr(old_value, "sourcecode_Decision5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecode_Decision5"):
                opp_val = getattr(value, "sourcecode_Decision5", None)
                setattr(value, "sourcecode_Decision5", self)

    @property
    def sourcecode_Statement0(self):
        return self.__sourcecode_Statement0

    @sourcecode_Statement0.setter
    def sourcecode_Statement0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecode_Statement__sourcecode_Statement0", None)
        self.__sourcecode_Statement0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecode_Statement"):
                opp_val = getattr(old_value, "sourcecode_Statement", None)
                if opp_val == self:
                    setattr(old_value, "sourcecode_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecode_Statement"):
                opp_val = getattr(value, "sourcecode_Statement", None)
                setattr(value, "sourcecode_Statement", self)

    @property
    def sourcecode_Statement8(self):
        return self.__sourcecode_Statement8

    @sourcecode_Statement8.setter
    def sourcecode_Statement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecode_Statement__sourcecode_Statement8", None)
        self.__sourcecode_Statement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecode_While"):
                opp_val = getattr(old_value, "sourcecode_While", None)
                if opp_val == self:
                    setattr(old_value, "sourcecode_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecode_While"):
                opp_val = getattr(value, "sourcecode_While", None)
                setattr(value, "sourcecode_While", self)
