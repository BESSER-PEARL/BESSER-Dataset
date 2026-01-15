from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Type:

    pass
class smalluml_IntegerType(Type):

    pass
class smalluml_RealType(Type):

    pass
class smalluml_BooleanType(Type):

    pass
class smalluml_Cardinalities:

    def __init__(self, lowerbound: int, upperbound: int, smalluml_Cardinalities: "smalluml_Association" = None):
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.smalluml_Cardinalities = smalluml_Cardinalities
        
    @property
    def upperbound(self) -> int:
        return self.__upperbound

    @upperbound.setter
    def upperbound(self, upperbound: int):
        self.__upperbound = upperbound

    @property
    def lowerbound(self) -> int:
        return self.__lowerbound

    @lowerbound.setter
    def lowerbound(self, lowerbound: int):
        self.__lowerbound = lowerbound

    @property
    def smalluml_Cardinalities(self):
        return self.__smalluml_Cardinalities

    @smalluml_Cardinalities.setter
    def smalluml_Cardinalities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Cardinalities__smalluml_Cardinalities", None)
        self.__smalluml_Cardinalities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association"):
                opp_val = getattr(old_value, "smalluml_Association", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association"):
                opp_val = getattr(value, "smalluml_Association", None)
                setattr(value, "smalluml_Association", self)

class smalluml_Parameter:

    def __init__(self, name: str, smalluml_Parameter: "smalluml_Operation" = None, smalluml_Parameter15: "smalluml_Type" = None):
        self.name = name
        self.smalluml_Parameter = smalluml_Parameter
        self.smalluml_Parameter15 = smalluml_Parameter15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smalluml_Parameter15(self):
        return self.__smalluml_Parameter15

    @smalluml_Parameter15.setter
    def smalluml_Parameter15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Parameter__smalluml_Parameter15", None)
        self.__smalluml_Parameter15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Type16"):
                opp_val = getattr(old_value, "smalluml_Type16", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Type16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Type16"):
                opp_val = getattr(value, "smalluml_Type16", None)
                setattr(value, "smalluml_Type16", self)

    @property
    def smalluml_Parameter(self):
        return self.__smalluml_Parameter

    @smalluml_Parameter.setter
    def smalluml_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Parameter__smalluml_Parameter", None)
        self.__smalluml_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Operation10"):
                opp_val = getattr(old_value, "smalluml_Operation10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Operation10"):
                opp_val = getattr(value, "smalluml_Operation10", None)
                if opp_val is None:
                    setattr(value, "smalluml_Operation10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smalluml_Type:

    pass
class smalluml_Entity:

    def __init__(self, name: str, smalluml_Entity: "smalluml_ClassDiagram" = None):
        self.name = name
        self.smalluml_Entity = smalluml_Entity
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smalluml_Entity(self):
        return self.__smalluml_Entity

    @smalluml_Entity.setter
    def smalluml_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Entity__smalluml_Entity", None)
        self.__smalluml_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_ClassDiagram"):
                opp_val = getattr(old_value, "smalluml_ClassDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_ClassDiagram"):
                opp_val = getattr(value, "smalluml_ClassDiagram", None)
                if opp_val is None:
                    setattr(value, "smalluml_ClassDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smalluml_ClassDiagram:

    def __init__(self, name: str, smalluml_ClassDiagram: set["smalluml_Entity"] = None):
        self.name = name
        self.smalluml_ClassDiagram = smalluml_ClassDiagram if smalluml_ClassDiagram is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smalluml_ClassDiagram(self):
        return self.__smalluml_ClassDiagram

    @smalluml_ClassDiagram.setter
    def smalluml_ClassDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_ClassDiagram__smalluml_ClassDiagram", None)
        self.__smalluml_ClassDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Entity"):
                    opp_val = getattr(item, "smalluml_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Entity"):
                    opp_val = getattr(item, "smalluml_Entity", None)
                    
                    setattr(item, "smalluml_Entity", self)
                    

class smalluml_Operation:

    def __init__(self, name: str, smalluml_Operation: "smalluml_Class" = None, smalluml_Operation8: "smalluml_Type" = None, smalluml_Operation10: set["smalluml_Parameter"] = None):
        self.name = name
        self.smalluml_Operation = smalluml_Operation
        self.smalluml_Operation8 = smalluml_Operation8
        self.smalluml_Operation10 = smalluml_Operation10 if smalluml_Operation10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smalluml_Operation10(self):
        return self.__smalluml_Operation10

    @smalluml_Operation10.setter
    def smalluml_Operation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Operation__smalluml_Operation10", None)
        self.__smalluml_Operation10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Parameter"):
                    opp_val = getattr(item, "smalluml_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Parameter"):
                    opp_val = getattr(item, "smalluml_Parameter", None)
                    
                    setattr(item, "smalluml_Parameter", self)
                    

    @property
    def smalluml_Operation(self):
        return self.__smalluml_Operation

    @smalluml_Operation.setter
    def smalluml_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Operation__smalluml_Operation", None)
        self.__smalluml_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class5"):
                opp_val = getattr(old_value, "smalluml_Class5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class5"):
                opp_val = getattr(value, "smalluml_Class5", None)
                if opp_val is None:
                    setattr(value, "smalluml_Class5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Operation8(self):
        return self.__smalluml_Operation8

    @smalluml_Operation8.setter
    def smalluml_Operation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Operation__smalluml_Operation8", None)
        self.__smalluml_Operation8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Type"):
                opp_val = getattr(old_value, "smalluml_Type", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Type"):
                opp_val = getattr(value, "smalluml_Type", None)
                setattr(value, "smalluml_Type", self)

class smalluml_Enumeration(Type):

    def __init__(self, variable: str, name: str):
        self.variable = variable
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

class smalluml_Attribute:

    def __init__(self, name: str, smalluml_Attribute: "smalluml_Class" = None, smalluml_Attribute12: "smalluml_Type" = None):
        self.name = name
        self.smalluml_Attribute = smalluml_Attribute
        self.smalluml_Attribute12 = smalluml_Attribute12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smalluml_Attribute12(self):
        return self.__smalluml_Attribute12

    @smalluml_Attribute12.setter
    def smalluml_Attribute12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Attribute__smalluml_Attribute12", None)
        self.__smalluml_Attribute12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Type13"):
                opp_val = getattr(old_value, "smalluml_Type13", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Type13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Type13"):
                opp_val = getattr(value, "smalluml_Type13", None)
                setattr(value, "smalluml_Type13", self)

    @property
    def smalluml_Attribute(self):
        return self.__smalluml_Attribute

    @smalluml_Attribute.setter
    def smalluml_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Attribute__smalluml_Attribute", None)
        self.__smalluml_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class"):
                opp_val = getattr(old_value, "smalluml_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class"):
                opp_val = getattr(value, "smalluml_Class", None)
                if opp_val is None:
                    setattr(value, "smalluml_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Entity:

    pass
class smalluml_Class(Entity):

    def __init__(self, abstract: bool, smalluml_Class: set["smalluml_Attribute"] = None, smalluml_Class3: "smalluml_Class" = None, smalluml_Class1: "smalluml_Class" = None, smalluml_Class5: set["smalluml_Operation"] = None, smalluml_Class20: "smalluml_Association" = None, smalluml_Class23: "smalluml_Association" = None):
        self.abstract = abstract
        self.smalluml_Class = smalluml_Class if smalluml_Class is not None else set()
        self.smalluml_Class3 = smalluml_Class3
        self.smalluml_Class1 = smalluml_Class1
        self.smalluml_Class5 = smalluml_Class5 if smalluml_Class5 is not None else set()
        self.smalluml_Class20 = smalluml_Class20
        self.smalluml_Class23 = smalluml_Class23
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def smalluml_Class(self):
        return self.__smalluml_Class

    @smalluml_Class.setter
    def smalluml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class", None)
        self.__smalluml_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Attribute"):
                    opp_val = getattr(item, "smalluml_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Attribute"):
                    opp_val = getattr(item, "smalluml_Attribute", None)
                    
                    setattr(item, "smalluml_Attribute", self)
                    

    @property
    def smalluml_Class3(self):
        return self.__smalluml_Class3

    @smalluml_Class3.setter
    def smalluml_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class3", None)
        self.__smalluml_Class3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class1"):
                opp_val = getattr(old_value, "smalluml_Class1", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Class1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class1"):
                opp_val = getattr(value, "smalluml_Class1", None)
                setattr(value, "smalluml_Class1", self)

    @property
    def smalluml_Class20(self):
        return self.__smalluml_Class20

    @smalluml_Class20.setter
    def smalluml_Class20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class20", None)
        self.__smalluml_Class20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association19"):
                opp_val = getattr(old_value, "smalluml_Association19", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Association19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association19"):
                opp_val = getattr(value, "smalluml_Association19", None)
                setattr(value, "smalluml_Association19", self)

    @property
    def smalluml_Class5(self):
        return self.__smalluml_Class5

    @smalluml_Class5.setter
    def smalluml_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class5", None)
        self.__smalluml_Class5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Operation"):
                    opp_val = getattr(item, "smalluml_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Operation"):
                    opp_val = getattr(item, "smalluml_Operation", None)
                    
                    setattr(item, "smalluml_Operation", self)
                    

    @property
    def smalluml_Class1(self):
        return self.__smalluml_Class1

    @smalluml_Class1.setter
    def smalluml_Class1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class1", None)
        self.__smalluml_Class1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class3"):
                opp_val = getattr(old_value, "smalluml_Class3", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Class3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class3"):
                opp_val = getattr(value, "smalluml_Class3", None)
                setattr(value, "smalluml_Class3", self)

    @property
    def smalluml_Class23(self):
        return self.__smalluml_Class23

    @smalluml_Class23.setter
    def smalluml_Class23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class23", None)
        self.__smalluml_Class23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association22"):
                opp_val = getattr(old_value, "smalluml_Association22", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Association22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association22"):
                opp_val = getattr(value, "smalluml_Association22", None)
                setattr(value, "smalluml_Association22", self)

class smalluml_Association(Entity):

    pass