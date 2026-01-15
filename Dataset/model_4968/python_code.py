from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    public = "public"
    private = "private"
    protected = "protected"


############################################
# Definition of Classes
############################################

class Association:

    pass
class dcmddandroid_Agregation(Association):

    pass
class dcmddandroid_EVisibility:

    def __init__(self, visibility: str):
        self.visibility = visibility
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class dcmddandroid_Composition(Association):

    pass
class AbstractClass:

    pass
class dcmddandroid_CycleClass(AbstractClass):

    pass
class dcmddandroid_Class(AbstractClass):

    pass
class ClassElement:

    pass
class NamedElement:

    pass
class dcmddandroid_EnumValue(NamedElement):

    def __init__(self, intValue: int, dcmddandroid_EnumValue: "dcmddandroid_Enum" = None):
        self.intValue = intValue
        self.dcmddandroid_EnumValue = dcmddandroid_EnumValue
        
    @property
    def intValue(self) -> int:
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: int):
        self.__intValue = intValue

    @property
    def dcmddandroid_EnumValue(self):
        return self.__dcmddandroid_EnumValue

    @dcmddandroid_EnumValue.setter
    def dcmddandroid_EnumValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_EnumValue__dcmddandroid_EnumValue", None)
        self.__dcmddandroid_EnumValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcmddandroid_Enum"):
                opp_val = getattr(old_value, "dcmddandroid_Enum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcmddandroid_Enum"):
                opp_val = getattr(value, "dcmddandroid_Enum", None)
                if opp_val is None:
                    setattr(value, "dcmddandroid_Enum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dcmddandroid_Parameter(NamedElement):

    def __init__(self, type: str, dcmddandroid_Parameter: "dcmddandroid_Method" = None):
        self.type = type
        self.dcmddandroid_Parameter = dcmddandroid_Parameter
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dcmddandroid_Parameter(self):
        return self.__dcmddandroid_Parameter

    @dcmddandroid_Parameter.setter
    def dcmddandroid_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_Parameter__dcmddandroid_Parameter", None)
        self.__dcmddandroid_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcmddandroid_Method13"):
                opp_val = getattr(old_value, "dcmddandroid_Method13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcmddandroid_Method13"):
                opp_val = getattr(value, "dcmddandroid_Method13", None)
                if opp_val is None:
                    setattr(value, "dcmddandroid_Method13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dcmddandroid_Diagram(NamedElement):

    pass
class dcmddandroid_ModelElement(NamedElement):

    pass
class dcmddandroid_PersistentClass(AbstractClass):

    pass
class dcmddandroid_Method(ClassElement):

    def __init__(self, isAbstract: bool, returns: str, dcmddandroid_Method: "dcmddandroid_AbstractClass" = None, dcmddandroid_Method11: "dcmddandroid_Interface" = None, dcmddandroid_Method13: set["dcmddandroid_Parameter"] = None):
        self.isAbstract = isAbstract
        self.returns = returns
        self.dcmddandroid_Method = dcmddandroid_Method
        self.dcmddandroid_Method11 = dcmddandroid_Method11
        self.dcmddandroid_Method13 = dcmddandroid_Method13 if dcmddandroid_Method13 is not None else set()
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def returns(self) -> str:
        return self.__returns

    @returns.setter
    def returns(self, returns: str):
        self.__returns = returns

    @property
    def dcmddandroid_Method13(self):
        return self.__dcmddandroid_Method13

    @dcmddandroid_Method13.setter
    def dcmddandroid_Method13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_Method__dcmddandroid_Method13", None)
        self.__dcmddandroid_Method13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dcmddandroid_Parameter"):
                    opp_val = getattr(item, "dcmddandroid_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "dcmddandroid_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dcmddandroid_Parameter"):
                    opp_val = getattr(item, "dcmddandroid_Parameter", None)
                    
                    setattr(item, "dcmddandroid_Parameter", self)
                    

    @property
    def dcmddandroid_Method11(self):
        return self.__dcmddandroid_Method11

    @dcmddandroid_Method11.setter
    def dcmddandroid_Method11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_Method__dcmddandroid_Method11", None)
        self.__dcmddandroid_Method11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcmddandroid_Interface10"):
                opp_val = getattr(old_value, "dcmddandroid_Interface10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcmddandroid_Interface10"):
                opp_val = getattr(value, "dcmddandroid_Interface10", None)
                if opp_val is None:
                    setattr(value, "dcmddandroid_Interface10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dcmddandroid_Method(self):
        return self.__dcmddandroid_Method

    @dcmddandroid_Method.setter
    def dcmddandroid_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_Method__dcmddandroid_Method", None)
        self.__dcmddandroid_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcmddandroid_AbstractClass3"):
                opp_val = getattr(old_value, "dcmddandroid_AbstractClass3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcmddandroid_AbstractClass3"):
                opp_val = getattr(value, "dcmddandroid_AbstractClass3", None)
                if opp_val is None:
                    setattr(value, "dcmddandroid_AbstractClass3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dcmddandroid_Attribute(ClassElement):

    def __init__(self, defaultValue: str, type: str, secured: str, dcmddandroid_Attribute: "dcmddandroid_AbstractClass" = None):
        self.defaultValue = defaultValue
        self.type = type
        self.secured = secured
        self.dcmddandroid_Attribute = dcmddandroid_Attribute
        
    @property
    def secured(self) -> str:
        return self.__secured

    @secured.setter
    def secured(self, secured: str):
        self.__secured = secured

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dcmddandroid_Attribute(self):
        return self.__dcmddandroid_Attribute

    @dcmddandroid_Attribute.setter
    def dcmddandroid_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_Attribute__dcmddandroid_Attribute", None)
        self.__dcmddandroid_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dcmddandroid_AbstractClass"):
                opp_val = getattr(old_value, "dcmddandroid_AbstractClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dcmddandroid_AbstractClass"):
                opp_val = getattr(value, "dcmddandroid_AbstractClass", None)
                if opp_val is None:
                    setattr(value, "dcmddandroid_AbstractClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EVisibility:

    pass
class dcmddandroid_ClassElement(EVisibility, NamedElement):

    def __init__(self, final: bool, static: bool):
        self.final = final
        self.static = static
        
    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

class ModelElement:

    pass
class dcmddandroid_Association(ModelElement):

    def __init__(self, rolSource: str, rolTarget: str, minMultiplicitySource: int, maxMultiplicitySource: int, minMultiplicityTarget: int, maxMultiplicityTarget: int, Association: "dcmddandroid_AbstractClass" = None, Association6: "dcmddandroid_AbstractClass" = None, associationAsSource: "dcmddandroid_AbstractClass" = None, associationAsTarget: "dcmddandroid_AbstractClass" = None):
        self.rolSource = rolSource
        self.rolTarget = rolTarget
        self.minMultiplicitySource = minMultiplicitySource
        self.maxMultiplicitySource = maxMultiplicitySource
        self.minMultiplicityTarget = minMultiplicityTarget
        self.maxMultiplicityTarget = maxMultiplicityTarget
        self.Association = Association
        self.Association6 = Association6
        self.associationAsSource = associationAsSource
        self.associationAsTarget = associationAsTarget
        
    @property
    def minMultiplicitySource(self) -> int:
        return self.__minMultiplicitySource

    @minMultiplicitySource.setter
    def minMultiplicitySource(self, minMultiplicitySource: int):
        self.__minMultiplicitySource = minMultiplicitySource

    @property
    def maxMultiplicitySource(self) -> int:
        return self.__maxMultiplicitySource

    @maxMultiplicitySource.setter
    def maxMultiplicitySource(self, maxMultiplicitySource: int):
        self.__maxMultiplicitySource = maxMultiplicitySource

    @property
    def minMultiplicityTarget(self) -> int:
        return self.__minMultiplicityTarget

    @minMultiplicityTarget.setter
    def minMultiplicityTarget(self, minMultiplicityTarget: int):
        self.__minMultiplicityTarget = minMultiplicityTarget

    @property
    def rolSource(self) -> str:
        return self.__rolSource

    @rolSource.setter
    def rolSource(self, rolSource: str):
        self.__rolSource = rolSource

    @property
    def maxMultiplicityTarget(self) -> int:
        return self.__maxMultiplicityTarget

    @maxMultiplicityTarget.setter
    def maxMultiplicityTarget(self, maxMultiplicityTarget: int):
        self.__maxMultiplicityTarget = maxMultiplicityTarget

    @property
    def rolTarget(self) -> str:
        return self.__rolTarget

    @rolTarget.setter
    def rolTarget(self, rolTarget: str):
        self.__rolTarget = rolTarget

    @property
    def associationAsSource(self):
        return self.__associationAsSource

    @associationAsSource.setter
    def associationAsSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_Association__associationAsSource", None)
        self.__associationAsSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractClass"):
                opp_val = getattr(old_value, "AbstractClass", None)
                if opp_val == self:
                    setattr(old_value, "AbstractClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractClass"):
                opp_val = getattr(value, "AbstractClass", None)
                setattr(value, "AbstractClass", self)

    @property
    def associationAsTarget(self):
        return self.__associationAsTarget

    @associationAsTarget.setter
    def associationAsTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_Association__associationAsTarget", None)
        self.__associationAsTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractClass18"):
                opp_val = getattr(old_value, "AbstractClass18", None)
                if opp_val == self:
                    setattr(old_value, "AbstractClass18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractClass18"):
                opp_val = getattr(value, "AbstractClass18", None)
                setattr(value, "AbstractClass18", self)

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_Association__Association", None)
        self.__Association = value
        
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
    def Association6(self):
        return self.__Association6

    @Association6.setter
    def Association6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_Association__Association6", None)
        self.__Association6 = value
        
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

class dcmddandroid_Enum(ModelElement):

    pass
class dcmddandroid_Interface(EVisibility, ModelElement):

    pass
class dcmddandroid_Implements(ModelElement):

    pass
class dcmddandroid_AbstractClass(EVisibility, ModelElement):

    def __init__(self, isAbstract: bool, implements: set["dcmddandroid_Implements"] = None, dcmddandroid_AbstractClass: set["dcmddandroid_Attribute"] = None, dcmddandroid_AbstractClass3: set["dcmddandroid_Method"] = None, source: set["dcmddandroid_Association"] = None, target: set["dcmddandroid_Association"] = None, AbstractClass23: "dcmddandroid_Implements" = None, AbstractClass: "dcmddandroid_Association" = None, AbstractClass18: "dcmddandroid_Association" = None):
        self.isAbstract = isAbstract
        self.implements = implements if implements is not None else set()
        self.dcmddandroid_AbstractClass = dcmddandroid_AbstractClass if dcmddandroid_AbstractClass is not None else set()
        self.dcmddandroid_AbstractClass3 = dcmddandroid_AbstractClass3 if dcmddandroid_AbstractClass3 is not None else set()
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.AbstractClass23 = AbstractClass23
        self.AbstractClass = AbstractClass
        self.AbstractClass18 = AbstractClass18
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def AbstractClass18(self):
        return self.__AbstractClass18

    @AbstractClass18.setter
    def AbstractClass18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_AbstractClass__AbstractClass18", None)
        self.__AbstractClass18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationAsTarget"):
                opp_val = getattr(old_value, "associationAsTarget", None)
                if opp_val == self:
                    setattr(old_value, "associationAsTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationAsTarget"):
                opp_val = getattr(value, "associationAsTarget", None)
                setattr(value, "associationAsTarget", self)

    @property
    def AbstractClass23(self):
        return self.__AbstractClass23

    @AbstractClass23.setter
    def AbstractClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_AbstractClass__AbstractClass23", None)
        self.__AbstractClass23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "implements22"):
                opp_val = getattr(old_value, "implements22", None)
                if opp_val == self:
                    setattr(old_value, "implements22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "implements22"):
                opp_val = getattr(value, "implements22", None)
                setattr(value, "implements22", self)

    @property
    def dcmddandroid_AbstractClass(self):
        return self.__dcmddandroid_AbstractClass

    @dcmddandroid_AbstractClass.setter
    def dcmddandroid_AbstractClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_AbstractClass__dcmddandroid_AbstractClass", None)
        self.__dcmddandroid_AbstractClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dcmddandroid_Attribute"):
                    opp_val = getattr(item, "dcmddandroid_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "dcmddandroid_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dcmddandroid_Attribute"):
                    opp_val = getattr(item, "dcmddandroid_Attribute", None)
                    
                    setattr(item, "dcmddandroid_Attribute", self)
                    

    @property
    def AbstractClass(self):
        return self.__AbstractClass

    @AbstractClass.setter
    def AbstractClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_AbstractClass__AbstractClass", None)
        self.__AbstractClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationAsSource"):
                opp_val = getattr(old_value, "associationAsSource", None)
                if opp_val == self:
                    setattr(old_value, "associationAsSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationAsSource"):
                opp_val = getattr(value, "associationAsSource", None)
                setattr(value, "associationAsSource", self)

    @property
    def implements(self):
        return self.__implements

    @implements.setter
    def implements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_AbstractClass__implements", None)
        self.__implements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Implements"):
                    opp_val = getattr(item, "Implements", None)
                    
                    if opp_val == self:
                        setattr(item, "Implements", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Implements"):
                    opp_val = getattr(item, "Implements", None)
                    
                    setattr(item, "Implements", self)
                    

    @property
    def dcmddandroid_AbstractClass3(self):
        return self.__dcmddandroid_AbstractClass3

    @dcmddandroid_AbstractClass3.setter
    def dcmddandroid_AbstractClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_AbstractClass__dcmddandroid_AbstractClass3", None)
        self.__dcmddandroid_AbstractClass3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dcmddandroid_Method"):
                    opp_val = getattr(item, "dcmddandroid_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "dcmddandroid_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dcmddandroid_Method"):
                    opp_val = getattr(item, "dcmddandroid_Method", None)
                    
                    setattr(item, "dcmddandroid_Method", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_AbstractClass__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Association"):
                    opp_val = getattr(item, "Association", None)
                    
                    if opp_val == self:
                        setattr(item, "Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Association"):
                    opp_val = getattr(item, "Association", None)
                    
                    setattr(item, "Association", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dcmddandroid_AbstractClass__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Association6"):
                    opp_val = getattr(item, "Association6", None)
                    
                    if opp_val == self:
                        setattr(item, "Association6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Association6"):
                    opp_val = getattr(item, "Association6", None)
                    
                    setattr(item, "Association6", self)
                    

class dcmddandroid_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
