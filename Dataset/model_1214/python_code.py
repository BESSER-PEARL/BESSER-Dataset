from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class JavaBody:

    pass
class atlext_OCL_GetAppliedStereotypesBody(JavaBody):

    pass
class OclExpression:

    pass
class atlext_OCL_JavaBody(OclExpression):

    pass
class OutPatternElement:

    pass
class ResolveTempResolution:

    pass
class atlext_OCL_OperationCallExp:

    pass
class ContextHelper:

    pass
class Callable:

    pass
class atlext_OCL_TypedElement(ABC):

    pass
class MatchedRule:

    pass
class atlext_ATL_RuleResolutionInfo:

    pass
class RuleResolutionInfo:

    pass
class atlext_OCL_ResolveTempResolution(RuleResolutionInfo):

    pass
class atlext_ATL_Binding:

    pass
class OCL_atlext_EObject:

    pass
class atlext_OCL_PropertyCallExp:

    def __init__(self, isStaticCall: bool, atlext_OCL_PropertyCallExp: "OCL_atlext_EObject" = None, atlext_OCL_PropertyCallExp36: set["OCL_atlext_EObject"] = None, atlext_OCL_PropertyCallExp39: "OCL_atlext_EObject" = None, atlext_OCL_PropertyCallExp42: "Callable" = None, ContextHelper: set["ContextHelper"] = None):
        self.isStaticCall = isStaticCall
        self.atlext_OCL_PropertyCallExp = atlext_OCL_PropertyCallExp
        self.atlext_OCL_PropertyCallExp36 = atlext_OCL_PropertyCallExp36 if atlext_OCL_PropertyCallExp36 is not None else set()
        self.atlext_OCL_PropertyCallExp39 = atlext_OCL_PropertyCallExp39
        self.atlext_OCL_PropertyCallExp42 = atlext_OCL_PropertyCallExp42
        self.ContextHelper = ContextHelper if ContextHelper is not None else set()
        
    @property
    def isStaticCall(self) -> bool:
        return self.__isStaticCall

    @isStaticCall.setter
    def isStaticCall(self, isStaticCall: bool):
        self.__isStaticCall = isStaticCall

    @property
    def ContextHelper(self):
        return self.__ContextHelper

    @ContextHelper.setter
    def ContextHelper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__ContextHelper", None)
        self.__ContextHelper = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL"):
                    opp_val = getattr(item, "ATL", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL"):
                    opp_val = getattr(item, "ATL", None)
                    
                    setattr(item, "ATL", self)
                    

    @property
    def atlext_OCL_PropertyCallExp39(self):
        return self.__atlext_OCL_PropertyCallExp39

    @atlext_OCL_PropertyCallExp39.setter
    def atlext_OCL_PropertyCallExp39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp39", None)
        self.__atlext_OCL_PropertyCallExp39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL_atlext_EObject40"):
                opp_val = getattr(old_value, "OCL_atlext_EObject40", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_EObject40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_EObject40"):
                opp_val = getattr(value, "OCL_atlext_EObject40", None)
                setattr(value, "OCL_atlext_EObject40", self)

    @property
    def atlext_OCL_PropertyCallExp36(self):
        return self.__atlext_OCL_PropertyCallExp36

    @atlext_OCL_PropertyCallExp36.setter
    def atlext_OCL_PropertyCallExp36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp36", None)
        self.__atlext_OCL_PropertyCallExp36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL_atlext_EObject37"):
                    opp_val = getattr(item, "OCL_atlext_EObject37", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL_atlext_EObject37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL_atlext_EObject37"):
                    opp_val = getattr(item, "OCL_atlext_EObject37", None)
                    
                    setattr(item, "OCL_atlext_EObject37", self)
                    

    @property
    def atlext_OCL_PropertyCallExp42(self):
        return self.__atlext_OCL_PropertyCallExp42

    @atlext_OCL_PropertyCallExp42.setter
    def atlext_OCL_PropertyCallExp42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp42", None)
        self.__atlext_OCL_PropertyCallExp42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Callable"):
                opp_val = getattr(old_value, "Callable", None)
                if opp_val == self:
                    setattr(old_value, "Callable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Callable"):
                opp_val = getattr(value, "Callable", None)
                setattr(value, "Callable", self)

    @property
    def atlext_OCL_PropertyCallExp(self):
        return self.__atlext_OCL_PropertyCallExp

    @atlext_OCL_PropertyCallExp.setter
    def atlext_OCL_PropertyCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_PropertyCallExp__atlext_OCL_PropertyCallExp", None)
        self.__atlext_OCL_PropertyCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL_atlext_EObject"):
                opp_val = getattr(old_value, "OCL_atlext_EObject", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_EObject"):
                opp_val = getattr(value, "OCL_atlext_EObject", None)
                setattr(value, "OCL_atlext_EObject", self)

class TypedElement:

    pass
class atlext_OCL_OclExpression(TypedElement):

    def __init__(self, implicitlyCasted: bool, atlext_OCL_OclExpression: "OCL_atlext_Type" = None):
        self.implicitlyCasted = implicitlyCasted
        self.atlext_OCL_OclExpression = atlext_OCL_OclExpression
        
    @property
    def implicitlyCasted(self) -> bool:
        return self.__implicitlyCasted

    @implicitlyCasted.setter
    def implicitlyCasted(self, implicitlyCasted: bool):
        self.__implicitlyCasted = implicitlyCasted

    @property
    def atlext_OCL_OclExpression(self):
        return self.__atlext_OCL_OclExpression

    @atlext_OCL_OclExpression.setter
    def atlext_OCL_OclExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_OCL_OclExpression__atlext_OCL_OclExpression", None)
        self.__atlext_OCL_OclExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL_atlext_Type33"):
                opp_val = getattr(old_value, "OCL_atlext_Type33", None)
                if opp_val == self:
                    setattr(old_value, "OCL_atlext_Type33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL_atlext_Type33"):
                opp_val = getattr(value, "OCL_atlext_Type33", None)
                setattr(value, "OCL_atlext_Type33", self)

class atlext_OCL_VariableDeclaration(TypedElement):

    pass
class OCL_atlext_Type:

    pass
class PropertyCallExp:

    pass
class atlext_ATL_Callable:

    pass
class atlext_ATL_OutPatternElement:

    pass
class atlext_ATL_MatchedRule:

    pass
class atlext_ATL_StringToStringMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class StringToStringMap:

    pass
class ATL_atlext_EObject:

    pass
class atlext_ATL_LocatedElement:

    def __init__(self, fileLocation: str, fileObject: str, atlext_ATL_LocatedElement: set["ATL_atlext_EObject"] = None, atlext_ATL_LocatedElement2: set["StringToStringMap"] = None):
        self.fileLocation = fileLocation
        self.fileObject = fileObject
        self.atlext_ATL_LocatedElement = atlext_ATL_LocatedElement if atlext_ATL_LocatedElement is not None else set()
        self.atlext_ATL_LocatedElement2 = atlext_ATL_LocatedElement2 if atlext_ATL_LocatedElement2 is not None else set()
        
    @property
    def fileObject(self) -> str:
        return self.__fileObject

    @fileObject.setter
    def fileObject(self, fileObject: str):
        self.__fileObject = fileObject

    @property
    def fileLocation(self) -> str:
        return self.__fileLocation

    @fileLocation.setter
    def fileLocation(self, fileLocation: str):
        self.__fileLocation = fileLocation

    @property
    def atlext_ATL_LocatedElement(self):
        return self.__atlext_ATL_LocatedElement

    @atlext_ATL_LocatedElement.setter
    def atlext_ATL_LocatedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_LocatedElement__atlext_ATL_LocatedElement", None)
        self.__atlext_ATL_LocatedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL_atlext_EObject"):
                    opp_val = getattr(item, "ATL_atlext_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL_atlext_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL_atlext_EObject"):
                    opp_val = getattr(item, "ATL_atlext_EObject", None)
                    
                    setattr(item, "ATL_atlext_EObject", self)
                    

    @property
    def atlext_ATL_LocatedElement2(self):
        return self.__atlext_ATL_LocatedElement2

    @atlext_ATL_LocatedElement2.setter
    def atlext_ATL_LocatedElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_LocatedElement__atlext_ATL_LocatedElement2", None)
        self.__atlext_ATL_LocatedElement2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToStringMap"):
                    opp_val = getattr(item, "StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToStringMap"):
                    opp_val = getattr(item, "StringToStringMap", None)
                    
                    setattr(item, "StringToStringMap", self)
                    

class atlext_ATL_Helper:

    def __init__(self, hasContext: bool, isAttribute: bool, atlext_ATL_Helper: "ATL_atlext_Type" = None, atlext_ATL_Helper16: "ATL_atlext_Type" = None):
        self.hasContext = hasContext
        self.isAttribute = isAttribute
        self.atlext_ATL_Helper = atlext_ATL_Helper
        self.atlext_ATL_Helper16 = atlext_ATL_Helper16
        
    @property
    def isAttribute(self) -> bool:
        return self.__isAttribute

    @isAttribute.setter
    def isAttribute(self, isAttribute: bool):
        self.__isAttribute = isAttribute

    @property
    def hasContext(self) -> bool:
        return self.__hasContext

    @hasContext.setter
    def hasContext(self, hasContext: bool):
        self.__hasContext = hasContext

    @property
    def atlext_ATL_Helper(self):
        return self.__atlext_ATL_Helper

    @atlext_ATL_Helper.setter
    def atlext_ATL_Helper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__atlext_ATL_Helper", None)
        self.__atlext_ATL_Helper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_Type14"):
                opp_val = getattr(old_value, "ATL_atlext_Type14", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type14"):
                opp_val = getattr(value, "ATL_atlext_Type14", None)
                setattr(value, "ATL_atlext_Type14", self)

    @property
    def atlext_ATL_Helper16(self):
        return self.__atlext_ATL_Helper16

    @atlext_ATL_Helper16.setter
    def atlext_ATL_Helper16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_Helper__atlext_ATL_Helper16", None)
        self.__atlext_ATL_Helper16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_Type17"):
                opp_val = getattr(old_value, "ATL_atlext_Type17", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type17"):
                opp_val = getattr(value, "ATL_atlext_Type17", None)
                setattr(value, "ATL_atlext_Type17", self)

class atlext_ATL_ContextHelper:

    pass
class VariableDeclaration:

    pass
class ATL_atlext_Type:

    pass
class atlext_ATL_CallableParameter:

    def __init__(self, name: str, atlext_ATL_CallableParameter: "ATL_atlext_Type" = None, atlext_ATL_CallableParameter8: "VariableDeclaration" = None):
        self.name = name
        self.atlext_ATL_CallableParameter = atlext_ATL_CallableParameter
        self.atlext_ATL_CallableParameter8 = atlext_ATL_CallableParameter8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atlext_ATL_CallableParameter8(self):
        return self.__atlext_ATL_CallableParameter8

    @atlext_ATL_CallableParameter8.setter
    def atlext_ATL_CallableParameter8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_CallableParameter__atlext_ATL_CallableParameter8", None)
        self.__atlext_ATL_CallableParameter8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration"):
                opp_val = getattr(old_value, "VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration"):
                opp_val = getattr(value, "VariableDeclaration", None)
                setattr(value, "VariableDeclaration", self)

    @property
    def atlext_ATL_CallableParameter(self):
        return self.__atlext_ATL_CallableParameter

    @atlext_ATL_CallableParameter.setter
    def atlext_ATL_CallableParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlext_ATL_CallableParameter__atlext_ATL_CallableParameter", None)
        self.__atlext_ATL_CallableParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL_atlext_Type"):
                opp_val = getattr(old_value, "ATL_atlext_Type", None)
                if opp_val == self:
                    setattr(old_value, "ATL_atlext_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL_atlext_Type"):
                opp_val = getattr(value, "ATL_atlext_Type", None)
                setattr(value, "ATL_atlext_Type", self)

class CallableParameter:

    pass