from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributeType(Enum):
    Simple = "Simple"
    Derivate = "Derivate"


############################################
# Definition of Classes
############################################

class Relational_EnumeratedLiteral:

    def __init__(self, name: str, Relational_EnumeratedLiteral: "Relational_EnumerationType" = None):
        self.name = name
        self.Relational_EnumeratedLiteral = Relational_EnumeratedLiteral
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Relational_EnumeratedLiteral(self):
        return self.__Relational_EnumeratedLiteral

    @Relational_EnumeratedLiteral.setter
    def Relational_EnumeratedLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_EnumeratedLiteral__Relational_EnumeratedLiteral", None)
        self.__Relational_EnumeratedLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_EnumerationType"):
                opp_val = getattr(old_value, "Relational_EnumerationType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_EnumerationType"):
                opp_val = getattr(value, "Relational_EnumerationType", None)
                if opp_val is None:
                    setattr(value, "Relational_EnumerationType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Domain:

    pass
class Relational_EnumerationType(Domain):

    pass
class Relational_PrimitiveType(Domain):

    pass
class CandidateKey:

    pass
class Relational_Schema:

    def __init__(self, name: str, Relational_Schema: set["Relational_Table"] = None, Relational_Schema2: set["Relational_Domain"] = None, Relational_Schema4: set["Relational_Constraint"] = None):
        self.name = name
        self.Relational_Schema = Relational_Schema if Relational_Schema is not None else set()
        self.Relational_Schema2 = Relational_Schema2 if Relational_Schema2 is not None else set()
        self.Relational_Schema4 = Relational_Schema4 if Relational_Schema4 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Relational_Schema2(self):
        return self.__Relational_Schema2

    @Relational_Schema2.setter
    def Relational_Schema2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Schema__Relational_Schema2", None)
        self.__Relational_Schema2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relational_Domain"):
                    opp_val = getattr(item, "Relational_Domain", None)
                    
                    if opp_val == self:
                        setattr(item, "Relational_Domain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relational_Domain"):
                    opp_val = getattr(item, "Relational_Domain", None)
                    
                    setattr(item, "Relational_Domain", self)
                    

    @property
    def Relational_Schema4(self):
        return self.__Relational_Schema4

    @Relational_Schema4.setter
    def Relational_Schema4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Schema__Relational_Schema4", None)
        self.__Relational_Schema4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relational_Constraint"):
                    opp_val = getattr(item, "Relational_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Relational_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relational_Constraint"):
                    opp_val = getattr(item, "Relational_Constraint", None)
                    
                    setattr(item, "Relational_Constraint", self)
                    

    @property
    def Relational_Schema(self):
        return self.__Relational_Schema

    @Relational_Schema.setter
    def Relational_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Schema__Relational_Schema", None)
        self.__Relational_Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relational_Table"):
                    opp_val = getattr(item, "Relational_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "Relational_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relational_Table"):
                    opp_val = getattr(item, "Relational_Table", None)
                    
                    setattr(item, "Relational_Table", self)
                    

class Relational_ForeignKey(CandidateKey):

    pass
class Relational_Attribute:

    def __init__(self, name: str, type: str, nullable: bool, multiplicity: int, Relational_Attribute15: "Relational_Domain" = None, Relational_Attribute: "Relational_Table" = None, Relational_Attribute22: "Relational_CandidateKey" = None):
        self.name = name
        self.type = type
        self.nullable = nullable
        self.multiplicity = multiplicity
        self.Relational_Attribute15 = Relational_Attribute15
        self.Relational_Attribute = Relational_Attribute
        self.Relational_Attribute22 = Relational_Attribute22
        
        pass
    @property
    def multiplicity(self):
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: int):
        self.__multiplicity = multiplicity


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def Relational_Attribute15(self):
        return self.__Relational_Attribute15

    @Relational_Attribute15.setter
    def Relational_Attribute15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Attribute__Relational_Attribute15", None)
        self.__Relational_Attribute15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_Domain16"):
                opp_val = getattr(old_value, "Relational_Domain16", None)
                if opp_val == self:
                    setattr(old_value, "Relational_Domain16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_Domain16"):
                opp_val = getattr(value, "Relational_Domain16", None)
                setattr(value, "Relational_Domain16", self)

    @property
    def Relational_Attribute(self):
        return self.__Relational_Attribute

    @Relational_Attribute.setter
    def Relational_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Attribute__Relational_Attribute", None)
        self.__Relational_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_Table11"):
                opp_val = getattr(old_value, "Relational_Table11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_Table11"):
                opp_val = getattr(value, "Relational_Table11", None)
                if opp_val is None:
                    setattr(value, "Relational_Table11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Relational_Attribute22(self):
        return self.__Relational_Attribute22

    @Relational_Attribute22.setter
    def Relational_Attribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Attribute__Relational_Attribute22", None)
        self.__Relational_Attribute22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_CandidateKey21"):
                opp_val = getattr(old_value, "Relational_CandidateKey21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_CandidateKey21"):
                opp_val = getattr(value, "Relational_CandidateKey21", None)
                if opp_val is None:
                    setattr(value, "Relational_CandidateKey21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Relational_CandidateKey:

    def __init__(self, name: str, Relational_CandidateKey: "Relational_Table" = None, Relational_CandidateKey9: "Relational_Table" = None, Relational_CandidateKey21: set["Relational_Attribute"] = None):
        self.name = name
        self.Relational_CandidateKey = Relational_CandidateKey
        self.Relational_CandidateKey9 = Relational_CandidateKey9
        self.Relational_CandidateKey21 = Relational_CandidateKey21 if Relational_CandidateKey21 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Relational_CandidateKey9(self):
        return self.__Relational_CandidateKey9

    @Relational_CandidateKey9.setter
    def Relational_CandidateKey9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_CandidateKey__Relational_CandidateKey9", None)
        self.__Relational_CandidateKey9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_Table8"):
                opp_val = getattr(old_value, "Relational_Table8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_Table8"):
                opp_val = getattr(value, "Relational_Table8", None)
                if opp_val is None:
                    setattr(value, "Relational_Table8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Relational_CandidateKey(self):
        return self.__Relational_CandidateKey

    @Relational_CandidateKey.setter
    def Relational_CandidateKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_CandidateKey__Relational_CandidateKey", None)
        self.__Relational_CandidateKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_Table6"):
                opp_val = getattr(old_value, "Relational_Table6", None)
                if opp_val == self:
                    setattr(old_value, "Relational_Table6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_Table6"):
                opp_val = getattr(value, "Relational_Table6", None)
                setattr(value, "Relational_Table6", self)

    @property
    def Relational_CandidateKey21(self):
        return self.__Relational_CandidateKey21

    @Relational_CandidateKey21.setter
    def Relational_CandidateKey21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_CandidateKey__Relational_CandidateKey21", None)
        self.__Relational_CandidateKey21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relational_Attribute22"):
                    opp_val = getattr(item, "Relational_Attribute22", None)
                    
                    if opp_val == self:
                        setattr(item, "Relational_Attribute22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relational_Attribute22"):
                    opp_val = getattr(item, "Relational_Attribute22", None)
                    
                    setattr(item, "Relational_Attribute22", self)
                    

class Relational_Constraint:

    def __init__(self, name: str, description: str, Relational_Constraint19: "Relational_Domain" = None, Relational_Constraint: "Relational_Schema" = None):
        self.name = name
        self.description = description
        self.Relational_Constraint19 = Relational_Constraint19
        self.Relational_Constraint = Relational_Constraint
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def Relational_Constraint(self):
        return self.__Relational_Constraint

    @Relational_Constraint.setter
    def Relational_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Constraint__Relational_Constraint", None)
        self.__Relational_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_Schema4"):
                opp_val = getattr(old_value, "Relational_Schema4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_Schema4"):
                opp_val = getattr(value, "Relational_Schema4", None)
                if opp_val is None:
                    setattr(value, "Relational_Schema4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Relational_Constraint19(self):
        return self.__Relational_Constraint19

    @Relational_Constraint19.setter
    def Relational_Constraint19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Constraint__Relational_Constraint19", None)
        self.__Relational_Constraint19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_Domain18"):
                opp_val = getattr(old_value, "Relational_Domain18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_Domain18"):
                opp_val = getattr(value, "Relational_Domain18", None)
                if opp_val is None:
                    setattr(value, "Relational_Domain18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Relational_Domain:

    def __init__(self, name: str, Relational_Domain16: "Relational_Attribute" = None, Relational_Domain18: set["Relational_Constraint"] = None, Relational_Domain: "Relational_Schema" = None):
        self.name = name
        self.Relational_Domain16 = Relational_Domain16
        self.Relational_Domain18 = Relational_Domain18 if Relational_Domain18 is not None else set()
        self.Relational_Domain = Relational_Domain
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Relational_Domain(self):
        return self.__Relational_Domain

    @Relational_Domain.setter
    def Relational_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Domain__Relational_Domain", None)
        self.__Relational_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_Schema2"):
                opp_val = getattr(old_value, "Relational_Schema2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_Schema2"):
                opp_val = getattr(value, "Relational_Schema2", None)
                if opp_val is None:
                    setattr(value, "Relational_Schema2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Relational_Domain16(self):
        return self.__Relational_Domain16

    @Relational_Domain16.setter
    def Relational_Domain16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Domain__Relational_Domain16", None)
        self.__Relational_Domain16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_Attribute15"):
                opp_val = getattr(old_value, "Relational_Attribute15", None)
                if opp_val == self:
                    setattr(old_value, "Relational_Attribute15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_Attribute15"):
                opp_val = getattr(value, "Relational_Attribute15", None)
                setattr(value, "Relational_Attribute15", self)

    @property
    def Relational_Domain18(self):
        return self.__Relational_Domain18

    @Relational_Domain18.setter
    def Relational_Domain18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Domain__Relational_Domain18", None)
        self.__Relational_Domain18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relational_Constraint19"):
                    opp_val = getattr(item, "Relational_Constraint19", None)
                    
                    if opp_val == self:
                        setattr(item, "Relational_Constraint19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relational_Constraint19"):
                    opp_val = getattr(item, "Relational_Constraint19", None)
                    
                    setattr(item, "Relational_Constraint19", self)
                    

class Relational_Table:

    def __init__(self, name: str, Relational_Table25: "Relational_ForeignKey" = None, Relational_Table: "Relational_Schema" = None, Relational_Table6: "Relational_CandidateKey" = None, Relational_Table8: set["Relational_CandidateKey"] = None, Relational_Table11: set["Relational_Attribute"] = None, Relational_Table13: set["Relational_ForeignKey"] = None):
        self.name = name
        self.Relational_Table25 = Relational_Table25
        self.Relational_Table = Relational_Table
        self.Relational_Table6 = Relational_Table6
        self.Relational_Table8 = Relational_Table8 if Relational_Table8 is not None else set()
        self.Relational_Table11 = Relational_Table11 if Relational_Table11 is not None else set()
        self.Relational_Table13 = Relational_Table13 if Relational_Table13 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Relational_Table8(self):
        return self.__Relational_Table8

    @Relational_Table8.setter
    def Relational_Table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Table__Relational_Table8", None)
        self.__Relational_Table8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relational_CandidateKey9"):
                    opp_val = getattr(item, "Relational_CandidateKey9", None)
                    
                    if opp_val == self:
                        setattr(item, "Relational_CandidateKey9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relational_CandidateKey9"):
                    opp_val = getattr(item, "Relational_CandidateKey9", None)
                    
                    setattr(item, "Relational_CandidateKey9", self)
                    

    @property
    def Relational_Table13(self):
        return self.__Relational_Table13

    @Relational_Table13.setter
    def Relational_Table13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Table__Relational_Table13", None)
        self.__Relational_Table13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relational_ForeignKey"):
                    opp_val = getattr(item, "Relational_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "Relational_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relational_ForeignKey"):
                    opp_val = getattr(item, "Relational_ForeignKey", None)
                    
                    setattr(item, "Relational_ForeignKey", self)
                    

    @property
    def Relational_Table(self):
        return self.__Relational_Table

    @Relational_Table.setter
    def Relational_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Table__Relational_Table", None)
        self.__Relational_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_Schema"):
                opp_val = getattr(old_value, "Relational_Schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_Schema"):
                opp_val = getattr(value, "Relational_Schema", None)
                if opp_val is None:
                    setattr(value, "Relational_Schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Relational_Table25(self):
        return self.__Relational_Table25

    @Relational_Table25.setter
    def Relational_Table25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Table__Relational_Table25", None)
        self.__Relational_Table25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_ForeignKey24"):
                opp_val = getattr(old_value, "Relational_ForeignKey24", None)
                if opp_val == self:
                    setattr(old_value, "Relational_ForeignKey24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_ForeignKey24"):
                opp_val = getattr(value, "Relational_ForeignKey24", None)
                setattr(value, "Relational_ForeignKey24", self)

    @property
    def Relational_Table11(self):
        return self.__Relational_Table11

    @Relational_Table11.setter
    def Relational_Table11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Table__Relational_Table11", None)
        self.__Relational_Table11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relational_Attribute"):
                    opp_val = getattr(item, "Relational_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Relational_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relational_Attribute"):
                    opp_val = getattr(item, "Relational_Attribute", None)
                    
                    setattr(item, "Relational_Attribute", self)
                    

    @property
    def Relational_Table6(self):
        return self.__Relational_Table6

    @Relational_Table6.setter
    def Relational_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Relational_Table__Relational_Table6", None)
        self.__Relational_Table6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relational_CandidateKey"):
                opp_val = getattr(old_value, "Relational_CandidateKey", None)
                if opp_val == self:
                    setattr(old_value, "Relational_CandidateKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relational_CandidateKey"):
                opp_val = getattr(value, "Relational_CandidateKey", None)
                setattr(value, "Relational_CandidateKey", self)
