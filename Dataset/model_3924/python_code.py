from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Position(Enum):
    default = "default"
    center = "center"
    right = "right"
class CellType(Enum):
    default = "default"
    defaultWithDisclosure = "defaultWithDisclosure"
    value2 = "value2"
    double = "double"
    subtitle = "subtitle"
    maps = "maps"


############################################
# Definition of Classes
############################################

class CollectionFunction:

    pass
class applauseDsl_StringSplit(CollectionFunction):

    pass
class ViewAction:

    pass
class applauseDsl_ExternalOpen(ViewAction):

    pass
class applauseDsl_ActionDelegate(ViewAction):

    pass
class applauseDsl_ViewAction:

    pass
class StringFunction:

    pass
class applauseDsl_StringUrlConform(StringFunction):

    pass
class applauseDsl_StringReplace(StringFunction):

    pass
class applauseDsl_StringConcat(StringFunction):

    pass
class applauseDsl_SectionCell:

    def __init__(self, type: str, applauseDsl_SectionCell112: "applauseDsl_ViewForAllSections" = None, applauseDsl_SectionCell114: "applauseDsl_CollectionIterator" = None, applauseDsl_SectionCell116: "applauseDsl_ScalarExpression" = None, applauseDsl_SectionCell119: "applauseDsl_ScalarExpression" = None, applauseDsl_SectionCell: "applauseDsl_ViewSection" = None, applauseDsl_SectionCell122: "applauseDsl_ScalarExpression" = None, applauseDsl_SectionCell125: "applauseDsl_ScalarExpression" = None, applauseDsl_SectionCell128: "applauseDsl_ViewAction" = None, applauseDsl_SectionCell130: "applauseDsl_ViewAction" = None):
        self.type = type
        self.applauseDsl_SectionCell112 = applauseDsl_SectionCell112
        self.applauseDsl_SectionCell114 = applauseDsl_SectionCell114
        self.applauseDsl_SectionCell116 = applauseDsl_SectionCell116
        self.applauseDsl_SectionCell119 = applauseDsl_SectionCell119
        self.applauseDsl_SectionCell = applauseDsl_SectionCell
        self.applauseDsl_SectionCell122 = applauseDsl_SectionCell122
        self.applauseDsl_SectionCell125 = applauseDsl_SectionCell125
        self.applauseDsl_SectionCell128 = applauseDsl_SectionCell128
        self.applauseDsl_SectionCell130 = applauseDsl_SectionCell130
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def applauseDsl_SectionCell116(self):
        return self.__applauseDsl_SectionCell116

    @applauseDsl_SectionCell116.setter
    def applauseDsl_SectionCell116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell116", None)
        self.__applauseDsl_SectionCell116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression117"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression117", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression117"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression117", None)
                setattr(value, "applauseDsl_ScalarExpression117", self)

    @property
    def applauseDsl_SectionCell114(self):
        return self.__applauseDsl_SectionCell114

    @applauseDsl_SectionCell114.setter
    def applauseDsl_SectionCell114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell114", None)
        self.__applauseDsl_SectionCell114 = value
        
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
    def applauseDsl_SectionCell125(self):
        return self.__applauseDsl_SectionCell125

    @applauseDsl_SectionCell125.setter
    def applauseDsl_SectionCell125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell125", None)
        self.__applauseDsl_SectionCell125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression126"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression126", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression126"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression126", None)
                setattr(value, "applauseDsl_ScalarExpression126", self)

    @property
    def applauseDsl_SectionCell130(self):
        return self.__applauseDsl_SectionCell130

    @applauseDsl_SectionCell130.setter
    def applauseDsl_SectionCell130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell130", None)
        self.__applauseDsl_SectionCell130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ViewAction131"):
                opp_val = getattr(old_value, "applauseDsl_ViewAction131", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ViewAction131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ViewAction131"):
                opp_val = getattr(value, "applauseDsl_ViewAction131", None)
                setattr(value, "applauseDsl_ViewAction131", self)

    @property
    def applauseDsl_SectionCell119(self):
        return self.__applauseDsl_SectionCell119

    @applauseDsl_SectionCell119.setter
    def applauseDsl_SectionCell119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell119", None)
        self.__applauseDsl_SectionCell119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression120"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression120", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression120"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression120", None)
                setattr(value, "applauseDsl_ScalarExpression120", self)

    @property
    def applauseDsl_SectionCell128(self):
        return self.__applauseDsl_SectionCell128

    @applauseDsl_SectionCell128.setter
    def applauseDsl_SectionCell128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell128", None)
        self.__applauseDsl_SectionCell128 = value
        
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
    def applauseDsl_SectionCell112(self):
        return self.__applauseDsl_SectionCell112

    @applauseDsl_SectionCell112.setter
    def applauseDsl_SectionCell112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell112", None)
        self.__applauseDsl_SectionCell112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ViewForAllSections111"):
                opp_val = getattr(old_value, "applauseDsl_ViewForAllSections111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ViewForAllSections111"):
                opp_val = getattr(value, "applauseDsl_ViewForAllSections111", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_ViewForAllSections111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "applauseDsl_ViewSection103"):
                opp_val = getattr(old_value, "applauseDsl_ViewSection103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ViewSection103"):
                opp_val = getattr(value, "applauseDsl_ViewSection103", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_ViewSection103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_SectionCell122(self):
        return self.__applauseDsl_SectionCell122

    @applauseDsl_SectionCell122.setter
    def applauseDsl_SectionCell122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_SectionCell__applauseDsl_SectionCell122", None)
        self.__applauseDsl_SectionCell122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression123"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression123", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression123"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression123", None)
                setattr(value, "applauseDsl_ScalarExpression123", self)

class View:

    pass
class applauseDsl_CustomView(View):

    def __init__(self, objclass: str, applauseDsl_CustomView: "applauseDsl_Parameter" = None):
        self.objclass = objclass
        self.applauseDsl_CustomView = applauseDsl_CustomView
        
    @property
    def objclass(self) -> str:
        return self.__objclass

    @objclass.setter
    def objclass(self, objclass: str):
        self.__objclass = objclass

    @property
    def applauseDsl_CustomView(self):
        return self.__applauseDsl_CustomView

    @applauseDsl_CustomView.setter
    def applauseDsl_CustomView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_CustomView__applauseDsl_CustomView", None)
        self.__applauseDsl_CustomView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Parameter86"):
                opp_val = getattr(old_value, "applauseDsl_Parameter86", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Parameter86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Parameter86"):
                opp_val = getattr(value, "applauseDsl_Parameter86", None)
                setattr(value, "applauseDsl_Parameter86", self)

class applauseDsl_SectionedView(View):

    pass
class applauseDsl_ProviderConstruction:

    pass
class applauseDsl_WebView(View):

    pass
class applauseDsl_ViewHeader:

    pass
class SectionedView:

    pass
class applauseDsl_DetailsView(SectionedView):

    pass
class applauseDsl_TableView(SectionedView):

    pass
class applauseDsl_ViewSection:

    pass
class applauseDsl_ViewForAllSections:

    pass
class Type:

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

class applauseDsl_Button:

    def __init__(self, handler: str, applauseDsl_Button: "applauseDsl_Application" = None, applauseDsl_Button27: "applauseDsl_ScalarExpression" = None, applauseDsl_Button30: "applauseDsl_ScalarExpression" = None, applauseDsl_Button33: "applauseDsl_ViewCall" = None, applauseDsl_Button63: "applauseDsl_View" = None):
        self.handler = handler
        self.applauseDsl_Button = applauseDsl_Button
        self.applauseDsl_Button27 = applauseDsl_Button27
        self.applauseDsl_Button30 = applauseDsl_Button30
        self.applauseDsl_Button33 = applauseDsl_Button33
        self.applauseDsl_Button63 = applauseDsl_Button63
        
    @property
    def handler(self) -> str:
        return self.__handler

    @handler.setter
    def handler(self, handler: str):
        self.__handler = handler

    @property
    def applauseDsl_Button63(self):
        return self.__applauseDsl_Button63

    @applauseDsl_Button63.setter
    def applauseDsl_Button63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Button__applauseDsl_Button63", None)
        self.__applauseDsl_Button63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_View62"):
                opp_val = getattr(old_value, "applauseDsl_View62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_View62"):
                opp_val = getattr(value, "applauseDsl_View62", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_View62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_Button27(self):
        return self.__applauseDsl_Button27

    @applauseDsl_Button27.setter
    def applauseDsl_Button27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Button__applauseDsl_Button27", None)
        self.__applauseDsl_Button27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression28"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression28", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression28"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression28", None)
                setattr(value, "applauseDsl_ScalarExpression28", self)

    @property
    def applauseDsl_Button33(self):
        return self.__applauseDsl_Button33

    @applauseDsl_Button33.setter
    def applauseDsl_Button33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Button__applauseDsl_Button33", None)
        self.__applauseDsl_Button33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ViewCall34"):
                opp_val = getattr(old_value, "applauseDsl_ViewCall34", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ViewCall34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ViewCall34"):
                opp_val = getattr(value, "applauseDsl_ViewCall34", None)
                setattr(value, "applauseDsl_ViewCall34", self)

    @property
    def applauseDsl_Button(self):
        return self.__applauseDsl_Button

    @applauseDsl_Button.setter
    def applauseDsl_Button(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Button__applauseDsl_Button", None)
        self.__applauseDsl_Button = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Application25"):
                opp_val = getattr(old_value, "applauseDsl_Application25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Application25"):
                opp_val = getattr(value, "applauseDsl_Application25", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Application25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_Button30(self):
        return self.__applauseDsl_Button30

    @applauseDsl_Button30.setter
    def applauseDsl_Button30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Button__applauseDsl_Button30", None)
        self.__applauseDsl_Button30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression31"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression31", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression31"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression31", None)
                setattr(value, "applauseDsl_ScalarExpression31", self)

class applauseDsl_ViewCall(ViewAction):

    pass
class applauseDsl_Entity(Type):

    pass
class CollectionExpression:

    pass
class ScalarExpression:

    pass
class Expression:

    pass
class applauseDsl_CollectionFunction(CollectionExpression, Expression):

    pass
class applauseDsl_ObjectReference(CollectionExpression, Expression, ScalarExpression):

    pass
class VariableDeclaration:

    pass
class applauseDsl_Constant(VariableDeclaration):

    def __init__(self, language: str, applauseDsl_Constant: set["applauseDsl_ScalarExpression"] = None):
        self.language = language
        self.applauseDsl_Constant = applauseDsl_Constant if applauseDsl_Constant is not None else set()
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def applauseDsl_Constant(self):
        return self.__applauseDsl_Constant

    @applauseDsl_Constant.setter
    def applauseDsl_Constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Constant__applauseDsl_Constant", None)
        self.__applauseDsl_Constant = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_ScalarExpression163"):
                    opp_val = getattr(item, "applauseDsl_ScalarExpression163", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_ScalarExpression163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_ScalarExpression163"):
                    opp_val = getattr(item, "applauseDsl_ScalarExpression163", None)
                    
                    setattr(item, "applauseDsl_ScalarExpression163", self)
                    

class applauseDsl_CollectionIterator(VariableDeclaration):

    pass
class applauseDsl_Property(VariableDeclaration):

    def __init__(self, derived: bool, applauseDsl_Property: "applauseDsl_Entity" = None, applauseDsl_Property40: "applauseDsl_TypeDescription" = None):
        self.derived = derived
        self.applauseDsl_Property = applauseDsl_Property
        self.applauseDsl_Property40 = applauseDsl_Property40
        
    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

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
            if hasattr(old_value, "applauseDsl_Entity38"):
                opp_val = getattr(old_value, "applauseDsl_Entity38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Entity38"):
                opp_val = getattr(value, "applauseDsl_Entity38", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_Entity38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def applauseDsl_Property40(self):
        return self.__applauseDsl_Property40

    @applauseDsl_Property40.setter
    def applauseDsl_Property40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Property__applauseDsl_Property40", None)
        self.__applauseDsl_Property40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_TypeDescription41"):
                opp_val = getattr(old_value, "applauseDsl_TypeDescription41", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_TypeDescription41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_TypeDescription41"):
                opp_val = getattr(value, "applauseDsl_TypeDescription41", None)
                setattr(value, "applauseDsl_TypeDescription41", self)

class applauseDsl_Parameter(VariableDeclaration):

    pass
class applauseDsl_TypeDescription:

    def __init__(self, many: bool, applauseDsl_TypeDescription: "applauseDsl_Type" = None, applauseDsl_TypeDescription9: "applauseDsl_Parameter" = None, applauseDsl_TypeDescription41: "applauseDsl_Property" = None):
        self.many = many
        self.applauseDsl_TypeDescription = applauseDsl_TypeDescription
        self.applauseDsl_TypeDescription9 = applauseDsl_TypeDescription9
        self.applauseDsl_TypeDescription41 = applauseDsl_TypeDescription41
        
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
    def applauseDsl_TypeDescription9(self):
        return self.__applauseDsl_TypeDescription9

    @applauseDsl_TypeDescription9.setter
    def applauseDsl_TypeDescription9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TypeDescription__applauseDsl_TypeDescription9", None)
        self.__applauseDsl_TypeDescription9 = value
        
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
    def applauseDsl_TypeDescription41(self):
        return self.__applauseDsl_TypeDescription41

    @applauseDsl_TypeDescription41.setter
    def applauseDsl_TypeDescription41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_TypeDescription__applauseDsl_TypeDescription41", None)
        self.__applauseDsl_TypeDescription41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Property40"):
                opp_val = getattr(old_value, "applauseDsl_Property40", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Property40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Property40"):
                opp_val = getattr(value, "applauseDsl_Property40", None)
                setattr(value, "applauseDsl_Property40", self)

class applauseDsl_ScalarExpression:

    pass
class ModelElement:

    pass
class applauseDsl_Type(ModelElement):

    def __init__(self, name: str, applauseDsl_Type: "applauseDsl_TypeDescription" = None, applauseDsl_Type46: "applauseDsl_ContentProvider" = None):
        self.name = name
        self.applauseDsl_Type = applauseDsl_Type
        self.applauseDsl_Type46 = applauseDsl_Type46
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_Type(self):
        return self.__applauseDsl_Type

    @applauseDsl_Type.setter
    def applauseDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Type__applauseDsl_Type", None)
        self.__applauseDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_TypeDescription"):
                opp_val = getattr(old_value, "applauseDsl_TypeDescription", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_TypeDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_TypeDescription"):
                opp_val = getattr(value, "applauseDsl_TypeDescription", None)
                setattr(value, "applauseDsl_TypeDescription", self)

    @property
    def applauseDsl_Type46(self):
        return self.__applauseDsl_Type46

    @applauseDsl_Type46.setter
    def applauseDsl_Type46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Type__applauseDsl_Type46", None)
        self.__applauseDsl_Type46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ContentProvider45"):
                opp_val = getattr(old_value, "applauseDsl_ContentProvider45", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ContentProvider45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ContentProvider45"):
                opp_val = getattr(value, "applauseDsl_ContentProvider45", None)
                setattr(value, "applauseDsl_ContentProvider45", self)

class applauseDsl_ContentProvider(ModelElement):

    def __init__(self, name: str, resolver: bool, many: bool, xml: bool, html: bool, applauseDsl_ContentProvider: "applauseDsl_Parameter" = None, applauseDsl_ContentProvider45: "applauseDsl_Type" = None, applauseDsl_ContentProvider48: "applauseDsl_ScalarExpression" = None, applauseDsl_ContentProvider51: "applauseDsl_ScalarExpression" = None, applauseDsl_ContentProvider54: "applauseDsl_ProviderConstruction" = None):
        self.name = name
        self.resolver = resolver
        self.many = many
        self.xml = xml
        self.html = html
        self.applauseDsl_ContentProvider = applauseDsl_ContentProvider
        self.applauseDsl_ContentProvider45 = applauseDsl_ContentProvider45
        self.applauseDsl_ContentProvider48 = applauseDsl_ContentProvider48
        self.applauseDsl_ContentProvider51 = applauseDsl_ContentProvider51
        self.applauseDsl_ContentProvider54 = applauseDsl_ContentProvider54
        
    @property
    def resolver(self) -> bool:
        return self.__resolver

    @resolver.setter
    def resolver(self, resolver: bool):
        self.__resolver = resolver

    @property
    def xml(self) -> bool:
        return self.__xml

    @xml.setter
    def xml(self, xml: bool):
        self.__xml = xml

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def html(self) -> bool:
        return self.__html

    @html.setter
    def html(self, html: bool):
        self.__html = html

    @property
    def applauseDsl_ContentProvider54(self):
        return self.__applauseDsl_ContentProvider54

    @applauseDsl_ContentProvider54.setter
    def applauseDsl_ContentProvider54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider54", None)
        self.__applauseDsl_ContentProvider54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ProviderConstruction"):
                opp_val = getattr(old_value, "applauseDsl_ProviderConstruction", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ProviderConstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ProviderConstruction"):
                opp_val = getattr(value, "applauseDsl_ProviderConstruction", None)
                setattr(value, "applauseDsl_ProviderConstruction", self)

    @property
    def applauseDsl_ContentProvider51(self):
        return self.__applauseDsl_ContentProvider51

    @applauseDsl_ContentProvider51.setter
    def applauseDsl_ContentProvider51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider51", None)
        self.__applauseDsl_ContentProvider51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression52"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression52", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression52"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression52", None)
                setattr(value, "applauseDsl_ScalarExpression52", self)

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
            if hasattr(old_value, "applauseDsl_Parameter43"):
                opp_val = getattr(old_value, "applauseDsl_Parameter43", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Parameter43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Parameter43"):
                opp_val = getattr(value, "applauseDsl_Parameter43", None)
                setattr(value, "applauseDsl_Parameter43", self)

    @property
    def applauseDsl_ContentProvider45(self):
        return self.__applauseDsl_ContentProvider45

    @applauseDsl_ContentProvider45.setter
    def applauseDsl_ContentProvider45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider45", None)
        self.__applauseDsl_ContentProvider45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_Type46"):
                opp_val = getattr(old_value, "applauseDsl_Type46", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_Type46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_Type46"):
                opp_val = getattr(value, "applauseDsl_Type46", None)
                setattr(value, "applauseDsl_Type46", self)

    @property
    def applauseDsl_ContentProvider48(self):
        return self.__applauseDsl_ContentProvider48

    @applauseDsl_ContentProvider48.setter
    def applauseDsl_ContentProvider48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_ContentProvider__applauseDsl_ContentProvider48", None)
        self.__applauseDsl_ContentProvider48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression49"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression49", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression49"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression49", None)
                setattr(value, "applauseDsl_ScalarExpression49", self)

class applauseDsl_VariableDeclaration(ModelElement):

    def __init__(self, name: str, applauseDsl_VariableDeclaration: "applauseDsl_ObjectReference" = None, applauseDsl_VariableDeclaration66: "applauseDsl_View" = None):
        self.name = name
        self.applauseDsl_VariableDeclaration = applauseDsl_VariableDeclaration
        self.applauseDsl_VariableDeclaration66 = applauseDsl_VariableDeclaration66
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_VariableDeclaration66(self):
        return self.__applauseDsl_VariableDeclaration66

    @applauseDsl_VariableDeclaration66.setter
    def applauseDsl_VariableDeclaration66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_VariableDeclaration__applauseDsl_VariableDeclaration66", None)
        self.__applauseDsl_VariableDeclaration66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_View65"):
                opp_val = getattr(old_value, "applauseDsl_View65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_View65"):
                opp_val = getattr(value, "applauseDsl_View65", None)
                if opp_val is None:
                    setattr(value, "applauseDsl_View65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class applauseDsl_View(ModelElement):

    def __init__(self, name: str, applauseDsl_View: "applauseDsl_ScalarExpression" = None, applauseDsl_View62: set["applauseDsl_Button"] = None, applauseDsl_View65: set["applauseDsl_VariableDeclaration"] = None, applauseDsl_View138: "applauseDsl_ViewCall" = None):
        self.name = name
        self.applauseDsl_View = applauseDsl_View
        self.applauseDsl_View62 = applauseDsl_View62 if applauseDsl_View62 is not None else set()
        self.applauseDsl_View65 = applauseDsl_View65 if applauseDsl_View65 is not None else set()
        self.applauseDsl_View138 = applauseDsl_View138
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def applauseDsl_View138(self):
        return self.__applauseDsl_View138

    @applauseDsl_View138.setter
    def applauseDsl_View138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_View__applauseDsl_View138", None)
        self.__applauseDsl_View138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ViewCall137"):
                opp_val = getattr(old_value, "applauseDsl_ViewCall137", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ViewCall137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ViewCall137"):
                opp_val = getattr(value, "applauseDsl_ViewCall137", None)
                setattr(value, "applauseDsl_ViewCall137", self)

    @property
    def applauseDsl_View62(self):
        return self.__applauseDsl_View62

    @applauseDsl_View62.setter
    def applauseDsl_View62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_View__applauseDsl_View62", None)
        self.__applauseDsl_View62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_Button63"):
                    opp_val = getattr(item, "applauseDsl_Button63", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_Button63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_Button63"):
                    opp_val = getattr(item, "applauseDsl_Button63", None)
                    
                    setattr(item, "applauseDsl_Button63", self)
                    

    @property
    def applauseDsl_View(self):
        return self.__applauseDsl_View

    @applauseDsl_View.setter
    def applauseDsl_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_View__applauseDsl_View", None)
        self.__applauseDsl_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression60"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression60", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression60"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression60", None)
                setattr(value, "applauseDsl_ScalarExpression60", self)

    @property
    def applauseDsl_View65(self):
        return self.__applauseDsl_View65

    @applauseDsl_View65.setter
    def applauseDsl_View65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_View__applauseDsl_View65", None)
        self.__applauseDsl_View65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_VariableDeclaration66"):
                    opp_val = getattr(item, "applauseDsl_VariableDeclaration66", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_VariableDeclaration66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_VariableDeclaration66"):
                    opp_val = getattr(item, "applauseDsl_VariableDeclaration66", None)
                    
                    setattr(item, "applauseDsl_VariableDeclaration66", self)
                    

class applauseDsl_NavigationBarItem(ModelElement):

    def __init__(self, position: str, applauseDsl_NavigationBarItem: "applauseDsl_ScalarExpression" = None, applauseDsl_NavigationBarItem5: set["applauseDsl_ScalarExpression"] = None):
        self.position = position
        self.applauseDsl_NavigationBarItem = applauseDsl_NavigationBarItem
        self.applauseDsl_NavigationBarItem5 = applauseDsl_NavigationBarItem5 if applauseDsl_NavigationBarItem5 is not None else set()
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def applauseDsl_NavigationBarItem5(self):
        return self.__applauseDsl_NavigationBarItem5

    @applauseDsl_NavigationBarItem5.setter
    def applauseDsl_NavigationBarItem5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_NavigationBarItem__applauseDsl_NavigationBarItem5", None)
        self.__applauseDsl_NavigationBarItem5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_ScalarExpression6"):
                    opp_val = getattr(item, "applauseDsl_ScalarExpression6", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_ScalarExpression6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_ScalarExpression6"):
                    opp_val = getattr(item, "applauseDsl_ScalarExpression6", None)
                    
                    setattr(item, "applauseDsl_ScalarExpression6", self)
                    

    @property
    def applauseDsl_NavigationBarItem(self):
        return self.__applauseDsl_NavigationBarItem

    @applauseDsl_NavigationBarItem.setter
    def applauseDsl_NavigationBarItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_NavigationBarItem__applauseDsl_NavigationBarItem", None)
        self.__applauseDsl_NavigationBarItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression", None)
                setattr(value, "applauseDsl_ScalarExpression", self)

class applauseDsl_CollectionLiteral(CollectionExpression, Expression):

    pass
class applauseDsl_StringFunction(Expression, ScalarExpression):

    pass
class PredefinedParameter:

    pass
class applauseDsl_SectionId(PredefinedParameter):

    pass
class applauseDsl_PredefinedParameter:

    pass
class applauseDsl_StringLiteral(Expression, ScalarExpression):

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
class applauseDsl_Expression:

    pass
class applauseDsl_ModelElement:

    pass
class applauseDsl_Application:

    def __init__(self, tabbarApplication: bool, name: str, applauseDsl_Application: "applauseDsl_ApplauseModel" = None, applauseDsl_Application17: "applauseDsl_ScalarExpression" = None, applauseDsl_Application20: "applauseDsl_ScalarExpression" = None, applauseDsl_Application23: "applauseDsl_ViewCall" = None, applauseDsl_Application25: set["applauseDsl_Button"] = None):
        self.tabbarApplication = tabbarApplication
        self.name = name
        self.applauseDsl_Application = applauseDsl_Application
        self.applauseDsl_Application17 = applauseDsl_Application17
        self.applauseDsl_Application20 = applauseDsl_Application20
        self.applauseDsl_Application23 = applauseDsl_Application23
        self.applauseDsl_Application25 = applauseDsl_Application25 if applauseDsl_Application25 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tabbarApplication(self) -> bool:
        return self.__tabbarApplication

    @tabbarApplication.setter
    def tabbarApplication(self, tabbarApplication: bool):
        self.__tabbarApplication = tabbarApplication

    @property
    def applauseDsl_Application20(self):
        return self.__applauseDsl_Application20

    @applauseDsl_Application20.setter
    def applauseDsl_Application20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Application__applauseDsl_Application20", None)
        self.__applauseDsl_Application20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression21"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression21", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression21"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression21", None)
                setattr(value, "applauseDsl_ScalarExpression21", self)

    @property
    def applauseDsl_Application17(self):
        return self.__applauseDsl_Application17

    @applauseDsl_Application17.setter
    def applauseDsl_Application17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Application__applauseDsl_Application17", None)
        self.__applauseDsl_Application17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ScalarExpression18"):
                opp_val = getattr(old_value, "applauseDsl_ScalarExpression18", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ScalarExpression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ScalarExpression18"):
                opp_val = getattr(value, "applauseDsl_ScalarExpression18", None)
                setattr(value, "applauseDsl_ScalarExpression18", self)

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
            if hasattr(old_value, "applauseDsl_ApplauseModel"):
                opp_val = getattr(old_value, "applauseDsl_ApplauseModel", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ApplauseModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ApplauseModel"):
                opp_val = getattr(value, "applauseDsl_ApplauseModel", None)
                setattr(value, "applauseDsl_ApplauseModel", self)

    @property
    def applauseDsl_Application25(self):
        return self.__applauseDsl_Application25

    @applauseDsl_Application25.setter
    def applauseDsl_Application25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Application__applauseDsl_Application25", None)
        self.__applauseDsl_Application25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "applauseDsl_Button"):
                    opp_val = getattr(item, "applauseDsl_Button", None)
                    
                    if opp_val == self:
                        setattr(item, "applauseDsl_Button", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "applauseDsl_Button"):
                    opp_val = getattr(item, "applauseDsl_Button", None)
                    
                    setattr(item, "applauseDsl_Button", self)
                    

    @property
    def applauseDsl_Application23(self):
        return self.__applauseDsl_Application23

    @applauseDsl_Application23.setter
    def applauseDsl_Application23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_applauseDsl_Application__applauseDsl_Application23", None)
        self.__applauseDsl_Application23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applauseDsl_ViewCall"):
                opp_val = getattr(old_value, "applauseDsl_ViewCall", None)
                if opp_val == self:
                    setattr(old_value, "applauseDsl_ViewCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applauseDsl_ViewCall"):
                opp_val = getattr(value, "applauseDsl_ViewCall", None)
                setattr(value, "applauseDsl_ViewCall", self)

class applauseDsl_ApplauseModel:

    pass