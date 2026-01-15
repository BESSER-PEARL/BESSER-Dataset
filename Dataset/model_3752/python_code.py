from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dbmddandroid_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class dbmddandroid_Relation:

    def __init__(self, minSourceMultiplicity: int, maxSourceMultiplicity: int, minTargetMultiplicity: int, maxTargetMultiplicity: int, dbmddandroid_Relation: "dbmddandroid_DBScheme" = None, Relation: "dbmddandroid_Table" = None, Relation7: "dbmddandroid_Table" = None, outRelation: "dbmddandroid_Table" = None, inRelation: "dbmddandroid_Table" = None):
        self.minSourceMultiplicity = minSourceMultiplicity
        self.maxSourceMultiplicity = maxSourceMultiplicity
        self.minTargetMultiplicity = minTargetMultiplicity
        self.maxTargetMultiplicity = maxTargetMultiplicity
        self.dbmddandroid_Relation = dbmddandroid_Relation
        self.Relation = Relation
        self.Relation7 = Relation7
        self.outRelation = outRelation
        self.inRelation = inRelation
        
    @property
    def maxTargetMultiplicity(self) -> int:
        return self.__maxTargetMultiplicity

    @maxTargetMultiplicity.setter
    def maxTargetMultiplicity(self, maxTargetMultiplicity: int):
        self.__maxTargetMultiplicity = maxTargetMultiplicity

    @property
    def minSourceMultiplicity(self) -> int:
        return self.__minSourceMultiplicity

    @minSourceMultiplicity.setter
    def minSourceMultiplicity(self, minSourceMultiplicity: int):
        self.__minSourceMultiplicity = minSourceMultiplicity

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
    def outRelation(self):
        return self.__outRelation

    @outRelation.setter
    def outRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmddandroid_Relation__outRelation", None)
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
    def Relation7(self):
        return self.__Relation7

    @Relation7.setter
    def Relation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmddandroid_Relation__Relation7", None)
        self.__Relation7 = value
        
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

    @property
    def Relation(self):
        return self.__Relation

    @Relation.setter
    def Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmddandroid_Relation__Relation", None)
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
    def dbmddandroid_Relation(self):
        return self.__dbmddandroid_Relation

    @dbmddandroid_Relation.setter
    def dbmddandroid_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmddandroid_Relation__dbmddandroid_Relation", None)
        self.__dbmddandroid_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmddandroid_DBScheme2"):
                opp_val = getattr(old_value, "dbmddandroid_DBScheme2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmddandroid_DBScheme2"):
                opp_val = getattr(value, "dbmddandroid_DBScheme2", None)
                if opp_val is None:
                    setattr(value, "dbmddandroid_DBScheme2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inRelation(self):
        return self.__inRelation

    @inRelation.setter
    def inRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmddandroid_Relation__inRelation", None)
        self.__inRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table10"):
                opp_val = getattr(old_value, "Table10", None)
                if opp_val == self:
                    setattr(old_value, "Table10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table10"):
                opp_val = getattr(value, "Table10", None)
                setattr(value, "Table10", self)

class NamedElement:

    pass
class dbmddandroid_Table(NamedElement):

    pass
class dbmddandroid_Column(NamedElement):

    def __init__(self, type: str, dbmddandroid_Column: "dbmddandroid_Table" = None):
        self.type = type
        self.dbmddandroid_Column = dbmddandroid_Column
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dbmddandroid_Column(self):
        return self.__dbmddandroid_Column

    @dbmddandroid_Column.setter
    def dbmddandroid_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmddandroid_Column__dbmddandroid_Column", None)
        self.__dbmddandroid_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmddandroid_Table4"):
                opp_val = getattr(old_value, "dbmddandroid_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmddandroid_Table4"):
                opp_val = getattr(value, "dbmddandroid_Table4", None)
                if opp_val is None:
                    setattr(value, "dbmddandroid_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbmddandroid_DBScheme(NamedElement):

    pass