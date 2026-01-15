from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DbMddAndroid_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class DbMddAndroid_DBScheme(NamedElement):

    pass
class DbMddAndroid_Column(NamedElement):

    def __init__(self, type: str, DbMddAndroid_Column: "DbMddAndroid_Table" = None, DbMddAndroid_Column7: "DbMddAndroid_Table" = None):
        self.type = type
        self.DbMddAndroid_Column = DbMddAndroid_Column
        self.DbMddAndroid_Column7 = DbMddAndroid_Column7
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def DbMddAndroid_Column(self):
        return self.__DbMddAndroid_Column

    @DbMddAndroid_Column.setter
    def DbMddAndroid_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DbMddAndroid_Column__DbMddAndroid_Column", None)
        self.__DbMddAndroid_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DbMddAndroid_Table4"):
                opp_val = getattr(old_value, "DbMddAndroid_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DbMddAndroid_Table4"):
                opp_val = getattr(value, "DbMddAndroid_Table4", None)
                if opp_val is None:
                    setattr(value, "DbMddAndroid_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DbMddAndroid_Column7(self):
        return self.__DbMddAndroid_Column7

    @DbMddAndroid_Column7.setter
    def DbMddAndroid_Column7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DbMddAndroid_Column__DbMddAndroid_Column7", None)
        self.__DbMddAndroid_Column7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DbMddAndroid_Table6"):
                opp_val = getattr(old_value, "DbMddAndroid_Table6", None)
                if opp_val == self:
                    setattr(old_value, "DbMddAndroid_Table6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DbMddAndroid_Table6"):
                opp_val = getattr(value, "DbMddAndroid_Table6", None)
                setattr(value, "DbMddAndroid_Table6", self)

class DbMddAndroid_Relation:

    def __init__(self, minSourceMultiplicity: int, maxSourceMultiplicity: int, minTargetMultiplicity: int, maxTargetMultiplicity: int, DbMddAndroid_Relation: "DbMddAndroid_DBScheme" = None, Relation: "DbMddAndroid_Table" = None, outRelation: "DbMddAndroid_Table" = None, inRelation: "DbMddAndroid_Table" = None, Relation10: "DbMddAndroid_Table" = None):
        self.minSourceMultiplicity = minSourceMultiplicity
        self.maxSourceMultiplicity = maxSourceMultiplicity
        self.minTargetMultiplicity = minTargetMultiplicity
        self.maxTargetMultiplicity = maxTargetMultiplicity
        self.DbMddAndroid_Relation = DbMddAndroid_Relation
        self.Relation = Relation
        self.outRelation = outRelation
        self.inRelation = inRelation
        self.Relation10 = Relation10
        
    @property
    def minSourceMultiplicity(self) -> int:
        return self.__minSourceMultiplicity

    @minSourceMultiplicity.setter
    def minSourceMultiplicity(self, minSourceMultiplicity: int):
        self.__minSourceMultiplicity = minSourceMultiplicity

    @property
    def maxTargetMultiplicity(self) -> int:
        return self.__maxTargetMultiplicity

    @maxTargetMultiplicity.setter
    def maxTargetMultiplicity(self, maxTargetMultiplicity: int):
        self.__maxTargetMultiplicity = maxTargetMultiplicity

    @property
    def minTargetMultiplicity(self) -> int:
        return self.__minTargetMultiplicity

    @minTargetMultiplicity.setter
    def minTargetMultiplicity(self, minTargetMultiplicity: int):
        self.__minTargetMultiplicity = minTargetMultiplicity

    @property
    def maxSourceMultiplicity(self) -> int:
        return self.__maxSourceMultiplicity

    @maxSourceMultiplicity.setter
    def maxSourceMultiplicity(self, maxSourceMultiplicity: int):
        self.__maxSourceMultiplicity = maxSourceMultiplicity

    @property
    def inRelation(self):
        return self.__inRelation

    @inRelation.setter
    def inRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DbMddAndroid_Relation__inRelation", None)
        self.__inRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table13"):
                opp_val = getattr(old_value, "Table13", None)
                if opp_val == self:
                    setattr(old_value, "Table13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table13"):
                opp_val = getattr(value, "Table13", None)
                setattr(value, "Table13", self)

    @property
    def outRelation(self):
        return self.__outRelation

    @outRelation.setter
    def outRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DbMddAndroid_Relation__outRelation", None)
        self.__outRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table"):
                opp_val = getattr(old_value, "Table", None)
                if opp_val == self:
                    setattr(old_value, "Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table"):
                opp_val = getattr(value, "Table", None)
                setattr(value, "Table", self)

    @property
    def DbMddAndroid_Relation(self):
        return self.__DbMddAndroid_Relation

    @DbMddAndroid_Relation.setter
    def DbMddAndroid_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DbMddAndroid_Relation__DbMddAndroid_Relation", None)
        self.__DbMddAndroid_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DbMddAndroid_DBScheme2"):
                opp_val = getattr(old_value, "DbMddAndroid_DBScheme2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DbMddAndroid_DBScheme2"):
                opp_val = getattr(value, "DbMddAndroid_DBScheme2", None)
                if opp_val is None:
                    setattr(value, "DbMddAndroid_DBScheme2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Relation(self):
        return self.__Relation

    @Relation.setter
    def Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DbMddAndroid_Relation__Relation", None)
        self.__Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Relation10(self):
        return self.__Relation10

    @Relation10.setter
    def Relation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DbMddAndroid_Relation__Relation10", None)
        self.__Relation10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DbMddAndroid_Table(NamedElement):

    pass