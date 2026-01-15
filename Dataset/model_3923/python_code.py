from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CellType(Enum):
    default = "default"
    defaultWithDisclosure = "defaultWithDisclosure"
    value2 = "value2"
    double = "double"
    subtitle = "subtitle"


############################################
# Definition of Classes
############################################

class StringFunction:

    pass
class applauseDsl_StringConcat(StringFunction):

    pass
class ViewAction:

    pass
class applauseDsl_ExternalOpen(ViewAction):

    pass
class ProviderConstruction:

    pass
class applauseDsl_SimpleProviderConstruction(ProviderConstruction):

    pass
class applauseDsl_ComplexProviderConstruction(ProviderConstruction):

    pass
class CollectionFunction:

    pass
class applauseDsl_StringSplit(CollectionFunction):

    pass
class applauseDsl_StringUrlConform(StringFunction):

    pass
class applauseDsl_StringReplace(StringFunction):

    pass
class applauseDsl_ViewHeader:

    pass
class applauseDsl_ViewAction:

    pass
class applauseDsl_SectionCell:

    def __init__(self, type: str, applauseDsl_SectionCell: "applauseDsl_ViewSection" = None, applauseDsl_SectionCell67: "applauseDsl_CollectionIterator" = None, applauseDsl_SectionCell69: "applauseDsl_ScalarExpression" = None, applauseDsl_SectionCell72: "applauseDsl_ScalarExpression" = None, applauseDsl_SectionCell75: "applauseDsl_ScalarExpression" = None, applauseDsl_SectionCell78: "applauseDsl_ViewAction" = None):
        self.type = type
        self.applauseDsl_SectionCell = applauseDsl_SectionCell
        self.applauseDsl_SectionCell67 = applauseDsl_SectionCell67
        self.applauseDsl_SectionCell69 = applauseDsl_SectionCell69
        self.applauseDsl_SectionCell72 = applauseDsl_SectionCell72
        self.applauseDsl_SectionCell75 = applauseDsl_SectionCell75
        self.applauseDsl_SectionCell78 = applauseDsl_SectionCell78
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def applauseDsl_SectionCell75(self):
        return self.__applauseDsl_SectionCell75

    @applauseDsl_SectionCell75.setter
    def applauseDsl_SectionCell75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell75", None)
        self.__applauseDsl_SectionCell75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression76"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression76", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression76"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression76", None)
                setattr(value, "applauseDsl_ScalarExpression76", self)

    @property
    def applauseDsl_SectionCell72(self):
        return self.__applauseDsl_SectionCell72

    @applauseDsl_SectionCell72.setter
    def applauseDsl_SectionCell72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell72", None)
        self.__applauseDsl_SectionCell72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression73"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression73", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression73"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression73", None)
                setattr(value, "applauseDsl_ScalarExpression73", self)

    @property
    def applauseDsl_SectionCell69(self):
        return self.__applauseDsl_SectionCell69

    @applauseDsl_SectionCell69.setter
    def applauseDsl_SectionCell69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell69", None)
        self.__applauseDsl_SectionCell69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression70"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression70", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression70"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression70", None)
                setattr(value, "applauseDsl_ScalarExpression70", self)

    @property
    def applauseDsl_SectionCell67(self):
        return self.__applauseDsl_SectionCell67

    @applauseDsl_SectionCell67.setter
    def applauseDsl_SectionCell67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell67", None)
        self.__applauseDsl_SectionCell67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_CollectionIterator"):
                opp_val = getattr(old_value, "applauseDsl_CollectionIterator", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_CollectionIterator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_CollectionIterator"):
                opp_val = getattr(value, "applauseDsl_CollectionIterator", None)
                setattr(value, "applauseDsl_CollectionIterator", self)

    @property
    def applauseDsl_SectionCell78(self):
        return self.__applauseDsl_SectionCell78

    @applauseDsl_SectionCell78.setter
    def applauseDsl_SectionCell78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell78", None)
        self.__applauseDsl_SectionCell78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ViewAction"):
                opp_val = getattr(old_value, "applauseDsl_ViewAction", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ViewAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ViewAction"):
                opp_val = getattr(value, "applauseDsl_ViewAction", None)
                setattr(value, "applauseDsl_ViewAction", self)

    @property
    def applauseDsl_SectionCell(self):
        return self.__applauseDsl_SectionCell

    @applauseDsl_SectionCell.setter
    def applauseDsl_SectionCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell", None)
        self.__applauseDsl_SectionCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ViewSection65"):
                opp_val = getattr(old_value, "applauseDsl_ViewSection65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ViewSection65"):
                opp_val = getattr(value, "applauseDsl_ViewSection65", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_ViewSection65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class applauseDsl_Entity(Type):

    pass
class applauseDsl_SimpleType(Type):

    def __init__(self, platformType: str):
        self.platformType = platformType
        
    @property
    def platformType(self) -> str:
        return self.__platformType

    @platformType.setter
    def platformType(self, platformType: str):
        self.__platformType = platformType

class ModelElement:

    pass
class applauseDsl_ViewCall(ViewAction):

    pass
class SectionedView:

    pass
class applauseDsl_DetailsView(SectionedView):

    pass
class applauseDsl_TableView(SectionedView):

    pass
class applauseDsl_ViewSection:

    pass
class View:

    pass
class applauseDsl_CustomView(View):

    def __init__(self, objclass: str):
        self.objclass = objclass
        
    @property
    def objclass(self) -> str:
        return self.__objclass

    @objclass.setter
    def objclass(self, objclass: str):
        self.__objclass = objclass

class applauseDsl_SectionedView(View):

    pass
class applauseDsl_View(ModelElement):

    pass
class applauseDsl_ProviderConstruction:

    pass
class applauseDsl_ContentProvider(ModelElement):

    def __init__(self, many: bool, applauseDsl_ContentProvider: "applauseDsl_Parameter" = None, applauseDsl_ContentProvider34: "applauseDsl_Type" = None, applauseDsl_ContentProvider37: "applauseDsl_ScalarExpression" = None, applauseDsl_ContentProvider40: "applauseDsl_ScalarExpression" = None, applauseDsl_ContentProvider106: "applauseDsl_ComplexProviderConstruction" = None):
        self.many = many
        self.applauseDsl_ContentProvider = applauseDsl_ContentProvider
        self.applauseDsl_ContentProvider34 = applauseDsl_ContentProvider34
        self.applauseDsl_ContentProvider37 = applauseDsl_ContentProvider37
        self.applauseDsl_ContentProvider40 = applauseDsl_ContentProvider40
        self.applauseDsl_ContentProvider106 = applauseDsl_ContentProvider106
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def applauseDsl_ContentProvider106(self):
        return self.__applauseDsl_ContentProvider106

    @applauseDsl_ContentProvider106.setter
    def applauseDsl_ContentProvider106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider106", None)
        self.__applauseDsl_ContentProvider106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ComplexProviderConstruction"):
                opp_val = getattr(old_value, "applauseDsl_ComplexProviderConstruction", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ComplexProviderConstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ComplexProviderConstruction"):
                opp_val = getattr(value, "applauseDsl_ComplexProviderConstruction", None)
                setattr(value, "applauseDsl_ComplexProviderConstruction", self)

    @property
    def applauseDsl_ContentProvider(self):
        return self.__applauseDsl_ContentProvider

    @applauseDsl_ContentProvider.setter
    def applauseDsl_ContentProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider", None)
        self.__applauseDsl_ContentProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Parameter32"):
                opp_val = getattr(old_value, "applauseDsl_Parameter32", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Parameter32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Parameter32"):
                opp_val = getattr(value, "applauseDsl_Parameter32", None)
                setattr(value, "applauseDsl_Parameter32", self)

    @property
    def applauseDsl_ContentProvider34(self):
        return self.__applauseDsl_ContentProvider34

    @applauseDsl_ContentProvider34.setter
    def applauseDsl_ContentProvider34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider34", None)
        self.__applauseDsl_ContentProvider34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Type35"):
                opp_val = getattr(old_value, "applauseDsl_Type35", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Type35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Type35"):
                opp_val = getattr(value, "applauseDsl_Type35", None)
                setattr(value, "applauseDsl_Type35", self)

    @property
    def applauseDsl_ContentProvider40(self):
        return self.__applauseDsl_ContentProvider40

    @applauseDsl_ContentProvider40.setter
    def applauseDsl_ContentProvider40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider40", None)
        self.__applauseDsl_ContentProvider40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression41"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression41", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression41"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression41", None)
                setattr(value, "applauseDsl_ScalarExpression41", self)

    @property
    def applauseDsl_ContentProvider37(self):
        return self.__applauseDsl_ContentProvider37

    @applauseDsl_ContentProvider37.setter
    def applauseDsl_ContentProvider37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider37", None)
        self.__applauseDsl_ContentProvider37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression38"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression38", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression38"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression38", None)
                setattr(value, "applauseDsl_ScalarExpression38", self)

class CollectionExpression:

    pass
class ScalarExpression:

    pass
class Expression:

    pass
class applauseDsl_ObjectReference(ScalarExpression, Expression, CollectionExpression):

    pass
class VariableDeclaration:

    pass
class applauseDsl_CollectionIterator(VariableDeclaration):

    pass
class applauseDsl_Property(VariableDeclaration):

    def __init__(self, derived: bool, applauseDsl_Property29: "applauseDsl_TypeDescription" = None, applauseDsl_Property: "applauseDsl_Entity" = None):
        self.derived = derived
        self.applauseDsl_Property29 = applauseDsl_Property29
        self.applauseDsl_Property = applauseDsl_Property
        
    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def applauseDsl_Property29(self):
        return self.__applauseDsl_Property29

    @applauseDsl_Property29.setter
    def applauseDsl_Property29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Property__applauseDsl_Property29", None)
        self.__applauseDsl_Property29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_TypeDescription30"):
                opp_val = getattr(old_value, "applauseDsl_TypeDescription30", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_TypeDescription30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_TypeDescription30"):
                opp_val = getattr(value, "applauseDsl_TypeDescription30", None)
                setattr(value, "applauseDsl_TypeDescription30", self)

    @property
    def applauseDsl_Property(self):
        return self.__applauseDsl_Property

    @applauseDsl_Property.setter
    def applauseDsl_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Property__applauseDsl_Property", None)
        self.__applauseDsl_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Entity27"):
                opp_val = getattr(old_value, "applauseDsl_Entity27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Entity27"):
                opp_val = getattr(value, "applauseDsl_Entity27", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Entity27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class applauseDsl_Parameter(VariableDeclaration):

    pass
class applauseDsl_Type(ModelElement):

    pass
class applauseDsl_TypeDescription:

    def __init__(self, many: bool, applauseDsl_TypeDescription: "applauseDsl_Type" = None, applauseDsl_TypeDescription5: "applauseDsl_Parameter" = None, applauseDsl_TypeDescription30: "applauseDsl_Property" = None):
        self.many = many
        self.applauseDsl_TypeDescription = applauseDsl_TypeDescription
        self.applauseDsl_TypeDescription5 = applauseDsl_TypeDescription5
        self.applauseDsl_TypeDescription30 = applauseDsl_TypeDescription30
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def applauseDsl_TypeDescription(self):
        return self.__applauseDsl_TypeDescription

    @applauseDsl_TypeDescription.setter
    def applauseDsl_TypeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TypeDescription__applauseDsl_TypeDescription", None)
        self.__applauseDsl_TypeDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Type"):
                opp_val = getattr(old_value, "applauseDsl_Type", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Type"):
                opp_val = getattr(value, "applauseDsl_Type", None)
                setattr(value, "applauseDsl_Type", self)

    @property
    def applauseDsl_TypeDescription5(self):
        return self.__applauseDsl_TypeDescription5

    @applauseDsl_TypeDescription5.setter
    def applauseDsl_TypeDescription5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TypeDescription__applauseDsl_TypeDescription5", None)
        self.__applauseDsl_TypeDescription5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Parameter"):
                opp_val = getattr(old_value, "applauseDsl_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Parameter"):
                opp_val = getattr(value, "applauseDsl_Parameter", None)
                setattr(value, "applauseDsl_Parameter", self)

    @property
    def applauseDsl_TypeDescription30(self):
        return self.__applauseDsl_TypeDescription30

    @applauseDsl_TypeDescription30.setter
    def applauseDsl_TypeDescription30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TypeDescription__applauseDsl_TypeDescription30", None)
        self.__applauseDsl_TypeDescription30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Property29"):
                opp_val = getattr(old_value, "applauseDsl_Property29", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Property29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Property29"):
                opp_val = getattr(value, "applauseDsl_Property29", None)
                setattr(value, "applauseDsl_Property29", self)

class applauseDsl_VariableDeclaration:

    def __init__(self, name: str, applauseDsl_VariableDeclaration: "applauseDsl_ObjectReference" = None):
        self.name = name
        self.applauseDsl_VariableDeclaration = applauseDsl_VariableDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_VariableDeclaration(self):
        return self.__applauseDsl_VariableDeclaration

    @applauseDsl_VariableDeclaration.setter
    def applauseDsl_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_VariableDeclaration__applauseDsl_VariableDeclaration", None)
        self.__applauseDsl_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ObjectReference"):
                opp_val = getattr(old_value, "applauseDsl_ObjectReference", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ObjectReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ObjectReference"):
                opp_val = getattr(value, "applauseDsl_ObjectReference", None)
                setattr(value, "applauseDsl_ObjectReference", self)

class applauseDsl_TabbarButton:

    pass
class applauseDsl_CollectionFunction(Expression, CollectionExpression):

    pass
class applauseDsl_CollectionLiteral(Expression, CollectionExpression):

    pass
class applauseDsl_StringFunction(ScalarExpression, Expression):

    pass
class applauseDsl_StringLiteral(ScalarExpression, Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class applauseDsl_CollectionExpression:

    pass
class applauseDsl_ScalarExpression:

    pass
class applauseDsl_Expression:

    pass
class applauseDsl_ModelElement:

    def __init__(self, name: str, applauseDsl_ModelElement: "applauseDsl_Model" = None):
        self.name = name
        self.applauseDsl_ModelElement = applauseDsl_ModelElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_ModelElement(self):
        return self.__applauseDsl_ModelElement

    @applauseDsl_ModelElement.setter
    def applauseDsl_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ModelElement__applauseDsl_ModelElement", None)
        self.__applauseDsl_ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Model2"):
                opp_val = getattr(old_value, "applauseDsl_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Model2"):
                opp_val = getattr(value, "applauseDsl_Model2", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class applauseDsl_Application:

    def __init__(self, name: str, applauseDsl_Application: "applauseDsl_Model" = None, applauseDsl_Application12: "applauseDsl_ScalarExpression" = None, applauseDsl_Application15: set["applauseDsl_TabbarButton"] = None):
        self.name = name
        self.applauseDsl_Application = applauseDsl_Application
        self.applauseDsl_Application12 = applauseDsl_Application12
        self.applauseDsl_Application15 = applauseDsl_Application15 if applauseDsl_Application15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_Application(self):
        return self.__applauseDsl_Application

    @applauseDsl_Application.setter
    def applauseDsl_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Application__applauseDsl_Application", None)
        self.__applauseDsl_Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Model"):
                opp_val = getattr(old_value, "applauseDsl_Model", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Model"):
                opp_val = getattr(value, "applauseDsl_Model", None)
                setattr(value, "applauseDsl_Model", self)

    @property
    def applauseDsl_Application12(self):
        return self.__applauseDsl_Application12

    @applauseDsl_Application12.setter
    def applauseDsl_Application12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Application__applauseDsl_Application12", None)
        self.__applauseDsl_Application12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression13"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression13", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression13"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression13", None)
                setattr(value, "applauseDsl_ScalarExpression13", self)

    @property
    def applauseDsl_Application15(self):
        return self.__applauseDsl_Application15

    @applauseDsl_Application15.setter
    def applauseDsl_Application15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Application__applauseDsl_Application15", None)
        self.__applauseDsl_Application15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_TabbarButton"):
                    opp_val = getattr(item, "applauseDsl_TabbarButton", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_TabbarButton", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_TabbarButton"):
                    opp_val = getattr(item, "applauseDsl_TabbarButton", None)
                    
                    setattr(item, "applauseDsl_TabbarButton", self)
                    

class applauseDsl_Model:

    pass