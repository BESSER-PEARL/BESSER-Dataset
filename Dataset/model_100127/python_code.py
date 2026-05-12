from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class relationaldatabase_Taggable:

    pass
class relationaldatabase_Configuration:

    pass
class relationaldatabase_Tag:

    def __init__(self, name: str, documentation: str, relationaldatabase_Tag: "relationaldatabase_DatabaseModel" = None, relationaldatabase_Tag24: "relationaldatabase_Taggable" = None):
        self.name = name
        self.documentation = documentation
        self.relationaldatabase_Tag = relationaldatabase_Tag
        self.relationaldatabase_Tag24 = relationaldatabase_Tag24
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


    @property
    def relationaldatabase_Tag24(self):
        return self.__relationaldatabase_Tag24

    @relationaldatabase_Tag24.setter
    def relationaldatabase_Tag24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldatabase_Tag__relationaldatabase_Tag24", None)
        self.__relationaldatabase_Tag24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationaldatabase_Taggable"):
                opp_val = getattr(old_value, "relationaldatabase_Taggable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationaldatabase_Taggable"):
                opp_val = getattr(value, "relationaldatabase_Taggable", None)
                if opp_val is None:
                    setattr(value, "relationaldatabase_Taggable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationaldatabase_Tag(self):
        return self.__relationaldatabase_Tag

    @relationaldatabase_Tag.setter
    def relationaldatabase_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldatabase_Tag__relationaldatabase_Tag", None)
        self.__relationaldatabase_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationaldatabase_DatabaseModel4"):
                opp_val = getattr(old_value, "relationaldatabase_DatabaseModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationaldatabase_DatabaseModel4"):
                opp_val = getattr(value, "relationaldatabase_DatabaseModel4", None)
                if opp_val is None:
                    setattr(value, "relationaldatabase_DatabaseModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class relationaldatabase_DataType(NamedElement):

    pass
class relationaldatabase_ForeignKey(NamedElement):

    def __init__(self, sourceLowerBoundary: str, sourceUpperBoundary: str, targetLowerBoundary: str, targetUpperBoundary: str, relationaldatabase_ForeignKey: "relationaldatabase_Table" = None, relationaldatabase_ForeignKey15: set["relationaldatabase_Column"] = None, relationaldatabase_ForeignKey18: set["relationaldatabase_Column"] = None, relationaldatabase_ForeignKey21: "relationaldatabase_Table" = None):
        self.sourceLowerBoundary = sourceLowerBoundary
        self.sourceUpperBoundary = sourceUpperBoundary
        self.targetLowerBoundary = targetLowerBoundary
        self.targetUpperBoundary = targetUpperBoundary
        self.relationaldatabase_ForeignKey = relationaldatabase_ForeignKey
        self.relationaldatabase_ForeignKey15 = relationaldatabase_ForeignKey15 if relationaldatabase_ForeignKey15 is not None else set()
        self.relationaldatabase_ForeignKey18 = relationaldatabase_ForeignKey18 if relationaldatabase_ForeignKey18 is not None else set()
        self.relationaldatabase_ForeignKey21 = relationaldatabase_ForeignKey21
        
        pass
    @property
    def targetLowerBoundary(self):
        return self.__targetLowerBoundary

    @targetLowerBoundary.setter
    def targetLowerBoundary(self, targetLowerBoundary: str):
        self.__targetLowerBoundary = targetLowerBoundary


    @property
    def targetUpperBoundary(self):
        return self.__targetUpperBoundary

    @targetUpperBoundary.setter
    def targetUpperBoundary(self, targetUpperBoundary: str):
        self.__targetUpperBoundary = targetUpperBoundary


    @property
    def sourceLowerBoundary(self):
        return self.__sourceLowerBoundary

    @sourceLowerBoundary.setter
    def sourceLowerBoundary(self, sourceLowerBoundary: str):
        self.__sourceLowerBoundary = sourceLowerBoundary


    @property
    def sourceUpperBoundary(self):
        return self.__sourceUpperBoundary

    @sourceUpperBoundary.setter
    def sourceUpperBoundary(self, sourceUpperBoundary: str):
        self.__sourceUpperBoundary = sourceUpperBoundary


    @property
    def relationaldatabase_ForeignKey21(self):
        return self.__relationaldatabase_ForeignKey21

    @relationaldatabase_ForeignKey21.setter
    def relationaldatabase_ForeignKey21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldatabase_ForeignKey__relationaldatabase_ForeignKey21", None)
        self.__relationaldatabase_ForeignKey21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationaldatabase_Table22"):
                opp_val = getattr(old_value, "relationaldatabase_Table22", None)
                if opp_val == self:
                    setattr(old_value, "relationaldatabase_Table22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationaldatabase_Table22"):
                opp_val = getattr(value, "relationaldatabase_Table22", None)
                setattr(value, "relationaldatabase_Table22", self)

    @property
    def relationaldatabase_ForeignKey18(self):
        return self.__relationaldatabase_ForeignKey18

    @relationaldatabase_ForeignKey18.setter
    def relationaldatabase_ForeignKey18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldatabase_ForeignKey__relationaldatabase_ForeignKey18", None)
        self.__relationaldatabase_ForeignKey18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationaldatabase_Column19"):
                    opp_val = getattr(item, "relationaldatabase_Column19", None)
                    
                    if opp_val == self:
                        setattr(item, "relationaldatabase_Column19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationaldatabase_Column19"):
                    opp_val = getattr(item, "relationaldatabase_Column19", None)
                    
                    setattr(item, "relationaldatabase_Column19", self)
                    

    @property
    def relationaldatabase_ForeignKey(self):
        return self.__relationaldatabase_ForeignKey

    @relationaldatabase_ForeignKey.setter
    def relationaldatabase_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldatabase_ForeignKey__relationaldatabase_ForeignKey", None)
        self.__relationaldatabase_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationaldatabase_Table10"):
                opp_val = getattr(old_value, "relationaldatabase_Table10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationaldatabase_Table10"):
                opp_val = getattr(value, "relationaldatabase_Table10", None)
                if opp_val is None:
                    setattr(value, "relationaldatabase_Table10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationaldatabase_ForeignKey15(self):
        return self.__relationaldatabase_ForeignKey15

    @relationaldatabase_ForeignKey15.setter
    def relationaldatabase_ForeignKey15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldatabase_ForeignKey__relationaldatabase_ForeignKey15", None)
        self.__relationaldatabase_ForeignKey15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationaldatabase_Column16"):
                    opp_val = getattr(item, "relationaldatabase_Column16", None)
                    
                    if opp_val == self:
                        setattr(item, "relationaldatabase_Column16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationaldatabase_Column16"):
                    opp_val = getattr(item, "relationaldatabase_Column16", None)
                    
                    setattr(item, "relationaldatabase_Column16", self)
                    

class relationaldatabase_Table(NamedElement):

    pass
class relationaldatabase_Column(NamedElement):

    def __init__(self, nullable: bool, primaryKey: bool, size: str, scale: str, arrayDimensions: int, unique: bool, relationaldatabase_Column: "relationaldatabase_Table" = None, relationaldatabase_Column12: "relationaldatabase_DataType" = None, relationaldatabase_Column16: "relationaldatabase_ForeignKey" = None, relationaldatabase_Column19: "relationaldatabase_ForeignKey" = None):
        self.nullable = nullable
        self.primaryKey = primaryKey
        self.size = size
        self.scale = scale
        self.arrayDimensions = arrayDimensions
        self.unique = unique
        self.relationaldatabase_Column = relationaldatabase_Column
        self.relationaldatabase_Column12 = relationaldatabase_Column12
        self.relationaldatabase_Column16 = relationaldatabase_Column16
        self.relationaldatabase_Column19 = relationaldatabase_Column19
        
        pass
    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale


    @property
    def primaryKey(self):
        return self.__primaryKey

    @primaryKey.setter
    def primaryKey(self, primaryKey: bool):
        self.__primaryKey = primaryKey


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def arrayDimensions(self):
        return self.__arrayDimensions

    @arrayDimensions.setter
    def arrayDimensions(self, arrayDimensions: int):
        self.__arrayDimensions = arrayDimensions


    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


    @property
    def relationaldatabase_Column19(self):
        return self.__relationaldatabase_Column19

    @relationaldatabase_Column19.setter
    def relationaldatabase_Column19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldatabase_Column__relationaldatabase_Column19", None)
        self.__relationaldatabase_Column19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationaldatabase_ForeignKey18"):
                opp_val = getattr(old_value, "relationaldatabase_ForeignKey18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationaldatabase_ForeignKey18"):
                opp_val = getattr(value, "relationaldatabase_ForeignKey18", None)
                if opp_val is None:
                    setattr(value, "relationaldatabase_ForeignKey18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationaldatabase_Column12(self):
        return self.__relationaldatabase_Column12

    @relationaldatabase_Column12.setter
    def relationaldatabase_Column12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldatabase_Column__relationaldatabase_Column12", None)
        self.__relationaldatabase_Column12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationaldatabase_DataType13"):
                opp_val = getattr(old_value, "relationaldatabase_DataType13", None)
                if opp_val == self:
                    setattr(old_value, "relationaldatabase_DataType13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationaldatabase_DataType13"):
                opp_val = getattr(value, "relationaldatabase_DataType13", None)
                setattr(value, "relationaldatabase_DataType13", self)

    @property
    def relationaldatabase_Column16(self):
        return self.__relationaldatabase_Column16

    @relationaldatabase_Column16.setter
    def relationaldatabase_Column16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldatabase_Column__relationaldatabase_Column16", None)
        self.__relationaldatabase_Column16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationaldatabase_ForeignKey15"):
                opp_val = getattr(old_value, "relationaldatabase_ForeignKey15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationaldatabase_ForeignKey15"):
                opp_val = getattr(value, "relationaldatabase_ForeignKey15", None)
                if opp_val is None:
                    setattr(value, "relationaldatabase_ForeignKey15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationaldatabase_Column(self):
        return self.__relationaldatabase_Column

    @relationaldatabase_Column.setter
    def relationaldatabase_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationaldatabase_Column__relationaldatabase_Column", None)
        self.__relationaldatabase_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationaldatabase_Table8"):
                opp_val = getattr(old_value, "relationaldatabase_Table8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationaldatabase_Table8"):
                opp_val = getattr(value, "relationaldatabase_Table8", None)
                if opp_val is None:
                    setattr(value, "relationaldatabase_Table8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class relationaldatabase_DatabaseModel(NamedElement):

    pass
class Taggable:

    pass
class relationaldatabase_NamedElement(Taggable):

    def __init__(self, name: str, documentation: str):
        self.name = name
        self.documentation = documentation
        
        pass
    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

