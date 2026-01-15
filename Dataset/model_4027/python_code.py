from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Class:

    pass
class UML_Enumeration(Class):

    pass
class UML_Interface(Class):

    pass
class UML_Element(ABC):

    def __init__(self, visibility: str, name: str):
        self.visibility = visibility
        self.name = name
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Attribute:

    pass
class UML_Property(Attribute):

    def __init__(self, isStatic: bool, UML_Property: "UML_Association" = None, UML_Property10: "UML_Property" = None, UML_Property8: set["UML_Property"] = None, UML_Property12: "UML_Association" = None, UML_Property15: "UML_Association" = None, UML_Property18: "UML_Interface" = None, UML_Property52: "UML_Association" = None, UML_Property55: "UML_Association" = None):
        self.isStatic = isStatic
        self.UML_Property = UML_Property
        self.UML_Property10 = UML_Property10
        self.UML_Property8 = UML_Property8 if UML_Property8 is not None else set()
        self.UML_Property12 = UML_Property12
        self.UML_Property15 = UML_Property15
        self.UML_Property18 = UML_Property18
        self.UML_Property52 = UML_Property52
        self.UML_Property55 = UML_Property55
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def UML_Property52(self):
        return self.__UML_Property52

    @UML_Property52.setter
    def UML_Property52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Property__UML_Property52", None)
        self.__UML_Property52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Association51"):
                opp_val = getattr(old_value, "UML_Association51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Association51"):
                opp_val = getattr(value, "UML_Association51", None)
                if opp_val is None:
                    setattr(value, "UML_Association51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_Property(self):
        return self.__UML_Property

    @UML_Property.setter
    def UML_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Property__UML_Property", None)
        self.__UML_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Association"):
                opp_val = getattr(old_value, "UML_Association", None)
                if opp_val == self:
                    setattr(old_value, "UML_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Association"):
                opp_val = getattr(value, "UML_Association", None)
                setattr(value, "UML_Association", self)

    @property
    def UML_Property12(self):
        return self.__UML_Property12

    @UML_Property12.setter
    def UML_Property12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Property__UML_Property12", None)
        self.__UML_Property12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Association13"):
                opp_val = getattr(old_value, "UML_Association13", None)
                if opp_val == self:
                    setattr(old_value, "UML_Association13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Association13"):
                opp_val = getattr(value, "UML_Association13", None)
                setattr(value, "UML_Association13", self)

    @property
    def UML_Property10(self):
        return self.__UML_Property10

    @UML_Property10.setter
    def UML_Property10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Property__UML_Property10", None)
        self.__UML_Property10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Property8"):
                opp_val = getattr(old_value, "UML_Property8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Property8"):
                opp_val = getattr(value, "UML_Property8", None)
                if opp_val is None:
                    setattr(value, "UML_Property8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_Property18(self):
        return self.__UML_Property18

    @UML_Property18.setter
    def UML_Property18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Property__UML_Property18", None)
        self.__UML_Property18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Interface"):
                opp_val = getattr(old_value, "UML_Interface", None)
                if opp_val == self:
                    setattr(old_value, "UML_Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Interface"):
                opp_val = getattr(value, "UML_Interface", None)
                setattr(value, "UML_Interface", self)

    @property
    def UML_Property15(self):
        return self.__UML_Property15

    @UML_Property15.setter
    def UML_Property15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Property__UML_Property15", None)
        self.__UML_Property15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Association16"):
                opp_val = getattr(old_value, "UML_Association16", None)
                if opp_val == self:
                    setattr(old_value, "UML_Association16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Association16"):
                opp_val = getattr(value, "UML_Association16", None)
                setattr(value, "UML_Association16", self)

    @property
    def UML_Property55(self):
        return self.__UML_Property55

    @UML_Property55.setter
    def UML_Property55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Property__UML_Property55", None)
        self.__UML_Property55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Association54"):
                opp_val = getattr(old_value, "UML_Association54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Association54"):
                opp_val = getattr(value, "UML_Association54", None)
                if opp_val is None:
                    setattr(value, "UML_Association54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_Property8(self):
        return self.__UML_Property8

    @UML_Property8.setter
    def UML_Property8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Property__UML_Property8", None)
        self.__UML_Property8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_Property10"):
                    opp_val = getattr(item, "UML_Property10", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_Property10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_Property10"):
                    opp_val = getattr(item, "UML_Property10", None)
                    
                    setattr(item, "UML_Property10", self)
                    

class TypedElement:

    pass
class UML_Parameter(TypedElement):

    def __init__(self, direction: str, UML_Parameter: "UML_Operation" = None):
        self.direction = direction
        self.UML_Parameter = UML_Parameter
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def UML_Parameter(self):
        return self.__UML_Parameter

    @UML_Parameter.setter
    def UML_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Parameter__UML_Parameter", None)
        self.__UML_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Operation"):
                opp_val = getattr(old_value, "UML_Operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Operation"):
                opp_val = getattr(value, "UML_Operation", None)
                if opp_val is None:
                    setattr(value, "UML_Operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_Attribute(TypedElement):

    pass
class Package:

    pass
class UML_Operation(Package):

    pass
class UML_LiteralInteger(Package):

    pass
class UML_LiteralUnlimitedNatural(Package):

    def __init__(self, value: int, UML_LiteralUnlimitedNatural: "UML_TypedElement" = None):
        self.value = value
        self.UML_LiteralUnlimitedNatural = UML_LiteralUnlimitedNatural
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def UML_LiteralUnlimitedNatural(self):
        return self.__UML_LiteralUnlimitedNatural

    @UML_LiteralUnlimitedNatural.setter
    def UML_LiteralUnlimitedNatural(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_LiteralUnlimitedNatural__UML_LiteralUnlimitedNatural", None)
        self.__UML_LiteralUnlimitedNatural = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_TypedElement6"):
                opp_val = getattr(old_value, "UML_TypedElement6", None)
                if opp_val == self:
                    setattr(old_value, "UML_TypedElement6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_TypedElement6"):
                opp_val = getattr(value, "UML_TypedElement6", None)
                setattr(value, "UML_TypedElement6", self)

class UML_PrimitiveType(Package):

    pass
class UML_EnumerationLiteral(Package):

    pass
class UML_Class(Package):

    pass
class UML_Association(Package):

    pass
class UML_Model(Package):

    pass
class PackageableElement:

    pass
class UML_Package(PackageableElement):

    pass
class Element:

    pass
class UML_Generalization(Element):

    pass
class UML_TemplateParameterSubstitution(Element):

    pass
class UML_TypedElement(Element):

    pass
class UML_TemplateBinding(Element):

    pass
class UML_PackageableElement(Element):

    pass