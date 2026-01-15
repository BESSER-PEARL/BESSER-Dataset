from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class JvmVisibility(Enum):
    DEFAULT = "DEFAULT"
    PRIVATE = "PRIVATE"
    PROTECTED = "PROTECTED"
    PUBLIC = "PUBLIC"


############################################
# Definition of Classes
############################################

class JvmParameterizedTypeReference:

    pass
class types_JvmInnerTypeReference(JvmParameterizedTypeReference):

    pass
class types_EObject:

    pass
class types_JvmAnnotationReference:

    def __init__(self, types_JvmAnnotationReference: "types_JvmAnnotationTarget" = None, types_JvmAnnotationReference36: "types_JvmAnnotationType" = None, types_JvmAnnotationReference38: set["types_JvmAnnotationValue"] = None, types_JvmAnnotationReference46: "types_JvmAnnotationAnnotationValue" = None):
        self.types_JvmAnnotationReference = types_JvmAnnotationReference
        self.types_JvmAnnotationReference36 = types_JvmAnnotationReference36
        self.types_JvmAnnotationReference38 = types_JvmAnnotationReference38 if types_JvmAnnotationReference38 is not None else set()
        self.types_JvmAnnotationReference46 = types_JvmAnnotationReference46
        
    @property
    def types_JvmAnnotationReference36(self):
        return self.__types_JvmAnnotationReference36

    @types_JvmAnnotationReference36.setter
    def types_JvmAnnotationReference36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmAnnotationReference__types_JvmAnnotationReference36", None)
        self.__types_JvmAnnotationReference36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmAnnotationType"):
                opp_val = getattr(old_value, "types_JvmAnnotationType", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmAnnotationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmAnnotationType"):
                opp_val = getattr(value, "types_JvmAnnotationType", None)
                setattr(value, "types_JvmAnnotationType", self)

    @property
    def types_JvmAnnotationReference46(self):
        return self.__types_JvmAnnotationReference46

    @types_JvmAnnotationReference46.setter
    def types_JvmAnnotationReference46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmAnnotationReference__types_JvmAnnotationReference46", None)
        self.__types_JvmAnnotationReference46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmAnnotationAnnotationValue"):
                opp_val = getattr(old_value, "types_JvmAnnotationAnnotationValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmAnnotationAnnotationValue"):
                opp_val = getattr(value, "types_JvmAnnotationAnnotationValue", None)
                if opp_val is None:
                    setattr(value, "types_JvmAnnotationAnnotationValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_JvmAnnotationReference38(self):
        return self.__types_JvmAnnotationReference38

    @types_JvmAnnotationReference38.setter
    def types_JvmAnnotationReference38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmAnnotationReference__types_JvmAnnotationReference38", None)
        self.__types_JvmAnnotationReference38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_JvmAnnotationValue39"):
                    opp_val = getattr(item, "types_JvmAnnotationValue39", None)
                    
                    if opp_val == self:
                        setattr(item, "types_JvmAnnotationValue39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_JvmAnnotationValue39"):
                    opp_val = getattr(item, "types_JvmAnnotationValue39", None)
                    
                    setattr(item, "types_JvmAnnotationValue39", self)
                    

    @property
    def types_JvmAnnotationReference(self):
        return self.__types_JvmAnnotationReference

    @types_JvmAnnotationReference.setter
    def types_JvmAnnotationReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmAnnotationReference__types_JvmAnnotationReference", None)
        self.__types_JvmAnnotationReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmAnnotationTarget"):
                opp_val = getattr(old_value, "types_JvmAnnotationTarget", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmAnnotationTarget"):
                opp_val = getattr(value, "types_JvmAnnotationTarget", None)
                if opp_val is None:
                    setattr(value, "types_JvmAnnotationTarget", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getValues(self) -> str:
        # TODO: Implement getValues method
        pass

class types_JvmAnnotationValue(ABC):

    def __init__(self, types_JvmAnnotationValue41: "types_JvmOperation" = None, types_JvmAnnotationValue: "types_JvmOperation" = None, types_JvmAnnotationValue39: "types_JvmAnnotationReference" = None):
        self.types_JvmAnnotationValue41 = types_JvmAnnotationValue41
        self.types_JvmAnnotationValue = types_JvmAnnotationValue
        self.types_JvmAnnotationValue39 = types_JvmAnnotationValue39
        
    @property
    def types_JvmAnnotationValue(self):
        return self.__types_JvmAnnotationValue

    @types_JvmAnnotationValue.setter
    def types_JvmAnnotationValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmAnnotationValue__types_JvmAnnotationValue", None)
        self.__types_JvmAnnotationValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmOperation30"):
                opp_val = getattr(old_value, "types_JvmOperation30", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmOperation30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmOperation30"):
                opp_val = getattr(value, "types_JvmOperation30", None)
                setattr(value, "types_JvmOperation30", self)

    @property
    def types_JvmAnnotationValue41(self):
        return self.__types_JvmAnnotationValue41

    @types_JvmAnnotationValue41.setter
    def types_JvmAnnotationValue41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmAnnotationValue__types_JvmAnnotationValue41", None)
        self.__types_JvmAnnotationValue41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmOperation42"):
                opp_val = getattr(old_value, "types_JvmOperation42", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmOperation42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmOperation42"):
                opp_val = getattr(value, "types_JvmOperation42", None)
                setattr(value, "types_JvmOperation42", self)

    @property
    def types_JvmAnnotationValue39(self):
        return self.__types_JvmAnnotationValue39

    @types_JvmAnnotationValue39.setter
    def types_JvmAnnotationValue39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmAnnotationValue__types_JvmAnnotationValue39", None)
        self.__types_JvmAnnotationValue39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmAnnotationReference38"):
                opp_val = getattr(old_value, "types_JvmAnnotationReference38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmAnnotationReference38"):
                opp_val = getattr(value, "types_JvmAnnotationReference38", None)
                if opp_val is None:
                    setattr(value, "types_JvmAnnotationReference38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getValueName(self) -> str:
        # TODO: Implement getValueName method
        pass

class JvmAnnotationValue:

    pass
class types_JvmEnumAnnotationValue(JvmAnnotationValue):

    pass
class types_JvmShortAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class types_JvmCustomAnnotationValue(JvmAnnotationValue):

    pass
class types_JvmFloatAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: float):
        self.values = values
        
    @property
    def values(self) -> float:
        return self.__values

    @values.setter
    def values(self, values: float):
        self.__values = values

class types_JvmDoubleAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: float):
        self.values = values
        
    @property
    def values(self) -> float:
        return self.__values

    @values.setter
    def values(self, values: float):
        self.__values = values

class types_JvmTypeAnnotationValue(JvmAnnotationValue):

    pass
class types_JvmCharAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class types_JvmLongAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class types_JvmBooleanAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: bool):
        self.values = values
        
    @property
    def values(self) -> bool:
        return self.__values

    @values.setter
    def values(self, values: bool):
        self.__values = values

class types_JvmStringAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class types_JvmAnnotationAnnotationValue(JvmAnnotationValue):

    pass
class types_JvmByteAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class types_JvmIntAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: int):
        self.values = values
        
    @property
    def values(self) -> int:
        return self.__values

    @values.setter
    def values(self, values: int):
        self.__values = values

class JvmFeature:

    pass
class types_JvmField(JvmFeature):

    def __init__(self, volatile: bool, transient: bool, constant: bool, constantValue: str, static: bool, final: bool, types_JvmField: "types_JvmTypeReference" = None):
        self.volatile = volatile
        self.transient = transient
        self.constant = constant
        self.constantValue = constantValue
        self.static = static
        self.final = final
        self.types_JvmField = types_JvmField
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def constantValue(self) -> str:
        return self.__constantValue

    @constantValue.setter
    def constantValue(self, constantValue: str):
        self.__constantValue = constantValue

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def types_JvmField(self):
        return self.__types_JvmField

    @types_JvmField.setter
    def types_JvmField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmField__types_JvmField", None)
        self.__types_JvmField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmTypeReference22"):
                opp_val = getattr(old_value, "types_JvmTypeReference22", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmTypeReference22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmTypeReference22"):
                opp_val = getattr(value, "types_JvmTypeReference22", None)
                setattr(value, "types_JvmTypeReference22", self)

    def getConstantValueAsByte(self) -> str:
        # TODO: Implement getConstantValueAsByte method
        pass

    def getConstantValueAsString(self) -> str:
        # TODO: Implement getConstantValueAsString method
        pass

    def getConstantValueAsBoolean(self) -> bool:
        # TODO: Implement getConstantValueAsBoolean method
        pass

    def getConstantValueAsLong(self) -> str:
        # TODO: Implement getConstantValueAsLong method
        pass

    def getConstantValueAsDouble(self) -> float:
        # TODO: Implement getConstantValueAsDouble method
        pass

    def getConstantValueAsShort(self) -> str:
        # TODO: Implement getConstantValueAsShort method
        pass

    def getConstantValueAsInt(self) -> int:
        # TODO: Implement getConstantValueAsInt method
        pass

    def getConstantValueAsChar(self) -> str:
        # TODO: Implement getConstantValueAsChar method
        pass

    def getConstantValueAsFloat(self) -> float:
        # TODO: Implement getConstantValueAsFloat method
        pass

class JvmExecutable:

    pass
class types_JvmOperation(JvmExecutable):

    def __init__(self, static: bool, final: bool, abstract: bool, synchronized: bool, default: bool, native: bool, strictFloatingPoint: bool, types_JvmOperation42: "types_JvmAnnotationValue" = None, types_JvmOperation: "types_JvmTypeReference" = None, types_JvmOperation30: "types_JvmAnnotationValue" = None):
        self.static = static
        self.final = final
        self.abstract = abstract
        self.synchronized = synchronized
        self.default = default
        self.native = native
        self.strictFloatingPoint = strictFloatingPoint
        self.types_JvmOperation42 = types_JvmOperation42
        self.types_JvmOperation = types_JvmOperation
        self.types_JvmOperation30 = types_JvmOperation30
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def native(self) -> bool:
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native

    @property
    def strictFloatingPoint(self) -> bool:
        return self.__strictFloatingPoint

    @strictFloatingPoint.setter
    def strictFloatingPoint(self, strictFloatingPoint: bool):
        self.__strictFloatingPoint = strictFloatingPoint

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def types_JvmOperation30(self):
        return self.__types_JvmOperation30

    @types_JvmOperation30.setter
    def types_JvmOperation30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmOperation__types_JvmOperation30", None)
        self.__types_JvmOperation30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmAnnotationValue"):
                opp_val = getattr(old_value, "types_JvmAnnotationValue", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmAnnotationValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmAnnotationValue"):
                opp_val = getattr(value, "types_JvmAnnotationValue", None)
                setattr(value, "types_JvmAnnotationValue", self)

    @property
    def types_JvmOperation42(self):
        return self.__types_JvmOperation42

    @types_JvmOperation42.setter
    def types_JvmOperation42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmOperation__types_JvmOperation42", None)
        self.__types_JvmOperation42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmAnnotationValue41"):
                opp_val = getattr(old_value, "types_JvmAnnotationValue41", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmAnnotationValue41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmAnnotationValue41"):
                opp_val = getattr(value, "types_JvmAnnotationValue41", None)
                setattr(value, "types_JvmAnnotationValue41", self)

    @property
    def types_JvmOperation(self):
        return self.__types_JvmOperation

    @types_JvmOperation.setter
    def types_JvmOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmOperation__types_JvmOperation", None)
        self.__types_JvmOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmTypeReference28"):
                opp_val = getattr(old_value, "types_JvmTypeReference28", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmTypeReference28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmTypeReference28"):
                opp_val = getattr(value, "types_JvmTypeReference28", None)
                setattr(value, "types_JvmTypeReference28", self)

class types_JvmConstructor(JvmExecutable):

    pass
class JvmTypeReference:

    pass
class types_JvmDelegateTypeReference(JvmTypeReference):

    pass
class types_JvmCompoundTypeReference(JvmTypeReference):

    pass
class types_JvmSpecializedTypeReference(JvmTypeReference):

    pass
class types_JvmGenericArrayTypeReference(JvmTypeReference):

    def __init__(self, types_JvmGenericArrayTypeReference: "types_JvmTypeReference" = None):
        self.types_JvmGenericArrayTypeReference = types_JvmGenericArrayTypeReference
        
    @property
    def types_JvmGenericArrayTypeReference(self):
        return self.__types_JvmGenericArrayTypeReference

    @types_JvmGenericArrayTypeReference.setter
    def types_JvmGenericArrayTypeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmGenericArrayTypeReference__types_JvmGenericArrayTypeReference", None)
        self.__types_JvmGenericArrayTypeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmTypeReference16"):
                opp_val = getattr(old_value, "types_JvmTypeReference16", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmTypeReference16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmTypeReference16"):
                opp_val = getattr(value, "types_JvmTypeReference16", None)
                setattr(value, "types_JvmTypeReference16", self)

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

    def getDimensions(self) -> int:
        # TODO: Implement getDimensions method
        pass

class types_JvmUnknownTypeReference(JvmTypeReference):

    def __init__(self, qualifiedName: str):
        self.qualifiedName = qualifiedName
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

class types_JvmParameterizedTypeReference(JvmTypeReference):

    pass
class JvmAnnotationTarget:

    pass
class types_JvmFormalParameter(JvmAnnotationTarget):

    def __init__(self, name: str, types_JvmFormalParameter: "types_JvmExecutable" = None, types_JvmFormalParameter32: "types_JvmTypeReference" = None):
        self.name = name
        self.types_JvmFormalParameter = types_JvmFormalParameter
        self.types_JvmFormalParameter32 = types_JvmFormalParameter32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_JvmFormalParameter32(self):
        return self.__types_JvmFormalParameter32

    @types_JvmFormalParameter32.setter
    def types_JvmFormalParameter32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmFormalParameter__types_JvmFormalParameter32", None)
        self.__types_JvmFormalParameter32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmTypeReference33"):
                opp_val = getattr(old_value, "types_JvmTypeReference33", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmTypeReference33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmTypeReference33"):
                opp_val = getattr(value, "types_JvmTypeReference33", None)
                setattr(value, "types_JvmTypeReference33", self)

    @property
    def types_JvmFormalParameter(self):
        return self.__types_JvmFormalParameter

    @types_JvmFormalParameter.setter
    def types_JvmFormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmFormalParameter__types_JvmFormalParameter", None)
        self.__types_JvmFormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmExecutable"):
                opp_val = getattr(old_value, "types_JvmExecutable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmExecutable"):
                opp_val = getattr(value, "types_JvmExecutable", None)
                if opp_val is None:
                    setattr(value, "types_JvmExecutable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JvmCompoundTypeReference:

    pass
class types_JvmSynonymTypeReference(JvmCompoundTypeReference):

    pass
class types_JvmMultiTypeReference(JvmCompoundTypeReference):

    pass
class types_JvmAnyTypeReference(JvmTypeReference):

    pass
class types_JvmTypeConstraint(ABC):

    def __init__(self, constraints: "types_JvmConstraintOwner" = None, JvmTypeConstraint: "types_JvmConstraintOwner" = None, types_JvmTypeConstraint: "types_JvmTypeReference" = None):
        self.constraints = constraints
        self.JvmTypeConstraint = JvmTypeConstraint
        self.types_JvmTypeConstraint = types_JvmTypeConstraint
        
    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeConstraint__constraints", None)
        self.__constraints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmConstraintOwner"):
                opp_val = getattr(old_value, "JvmConstraintOwner", None)
                if opp_val == self:
                    setattr(old_value, "JvmConstraintOwner", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmConstraintOwner"):
                opp_val = getattr(value, "JvmConstraintOwner", None)
                setattr(value, "JvmConstraintOwner", self)

    @property
    def JvmTypeConstraint(self):
        return self.__JvmTypeConstraint

    @JvmTypeConstraint.setter
    def JvmTypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeConstraint__JvmTypeConstraint", None)
        self.__JvmTypeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_JvmTypeConstraint(self):
        return self.__types_JvmTypeConstraint

    @types_JvmTypeConstraint.setter
    def types_JvmTypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeConstraint__types_JvmTypeConstraint", None)
        self.__types_JvmTypeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmTypeReference8"):
                opp_val = getattr(old_value, "types_JvmTypeReference8", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmTypeReference8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmTypeReference8"):
                opp_val = getattr(value, "types_JvmTypeReference8", None)
                setattr(value, "types_JvmTypeReference8", self)

    def getQualifiedName(self) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def getQualifiedName(self, innerClassDelimiter: str) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def getIdentifier(self) -> str:
        # TODO: Implement getIdentifier method
        pass

    def getSimpleName(self) -> str:
        # TODO: Implement getSimpleName method
        pass

class types_JvmConstraintOwner(ABC):

    pass
class types_JvmTypeParameterDeclarator(ABC):

    pass
class JvmConstraintOwner:

    pass
class types_JvmWildcardTypeReference(JvmTypeReference, JvmConstraintOwner):

    pass
class types_JvmMember(JvmAnnotationTarget):

    def __init__(self, visibility: str, simpleName: str, identifier: str, deprecated: bool, JvmMember: "types_JvmDeclaredType" = None, members: "types_JvmDeclaredType" = None):
        self.visibility = visibility
        self.simpleName = simpleName
        self.identifier = identifier
        self.deprecated = deprecated
        self.JvmMember = JvmMember
        self.members = members
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def simpleName(self) -> str:
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def deprecated(self) -> bool:
        return self.__deprecated

    @deprecated.setter
    def deprecated(self, deprecated: bool):
        self.__deprecated = deprecated

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmMember__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmDeclaredType"):
                opp_val = getattr(old_value, "JvmDeclaredType", None)
                if opp_val == self:
                    setattr(old_value, "JvmDeclaredType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmDeclaredType"):
                opp_val = getattr(value, "JvmDeclaredType", None)
                setattr(value, "JvmDeclaredType", self)

    @property
    def JvmMember(self):
        return self.__JvmMember

    @JvmMember.setter
    def JvmMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmMember__JvmMember", None)
        self.__JvmMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declaringType"):
                opp_val = getattr(old_value, "declaringType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declaringType"):
                opp_val = getattr(value, "declaringType", None)
                if opp_val is None:
                    setattr(value, "declaringType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def internalSetIdentifier(self, identifier: str):
        # TODO: Implement internalSetIdentifier method
        pass

class JvmTypeParameterDeclarator:

    pass
class types_JvmExecutable(JvmFeature, JvmTypeParameterDeclarator):

    def __init__(self, varArgs: bool, types_JvmExecutable: set["types_JvmFormalParameter"] = None, types_JvmExecutable25: set["types_JvmTypeReference"] = None):
        self.varArgs = varArgs
        self.types_JvmExecutable = types_JvmExecutable if types_JvmExecutable is not None else set()
        self.types_JvmExecutable25 = types_JvmExecutable25 if types_JvmExecutable25 is not None else set()
        
    @property
    def varArgs(self) -> bool:
        return self.__varArgs

    @varArgs.setter
    def varArgs(self, varArgs: bool):
        self.__varArgs = varArgs

    @property
    def types_JvmExecutable25(self):
        return self.__types_JvmExecutable25

    @types_JvmExecutable25.setter
    def types_JvmExecutable25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmExecutable__types_JvmExecutable25", None)
        self.__types_JvmExecutable25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_JvmTypeReference26"):
                    opp_val = getattr(item, "types_JvmTypeReference26", None)
                    
                    if opp_val == self:
                        setattr(item, "types_JvmTypeReference26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_JvmTypeReference26"):
                    opp_val = getattr(item, "types_JvmTypeReference26", None)
                    
                    setattr(item, "types_JvmTypeReference26", self)
                    

    @property
    def types_JvmExecutable(self):
        return self.__types_JvmExecutable

    @types_JvmExecutable.setter
    def types_JvmExecutable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmExecutable__types_JvmExecutable", None)
        self.__types_JvmExecutable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_JvmFormalParameter"):
                    opp_val = getattr(item, "types_JvmFormalParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "types_JvmFormalParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_JvmFormalParameter"):
                    opp_val = getattr(item, "types_JvmFormalParameter", None)
                    
                    setattr(item, "types_JvmFormalParameter", self)
                    

class JvmField:

    pass
class types_JvmEnumerationLiteral(JvmField):

    def __init__(self, types_JvmEnumerationLiteral: "types_JvmEnumerationType" = None, types_JvmEnumerationLiteral48: "types_JvmEnumAnnotationValue" = None):
        self.types_JvmEnumerationLiteral = types_JvmEnumerationLiteral
        self.types_JvmEnumerationLiteral48 = types_JvmEnumerationLiteral48
        
    @property
    def types_JvmEnumerationLiteral(self):
        return self.__types_JvmEnumerationLiteral

    @types_JvmEnumerationLiteral.setter
    def types_JvmEnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmEnumerationLiteral__types_JvmEnumerationLiteral", None)
        self.__types_JvmEnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmEnumerationType"):
                opp_val = getattr(old_value, "types_JvmEnumerationType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmEnumerationType"):
                opp_val = getattr(value, "types_JvmEnumerationType", None)
                if opp_val is None:
                    setattr(value, "types_JvmEnumerationType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_JvmEnumerationLiteral48(self):
        return self.__types_JvmEnumerationLiteral48

    @types_JvmEnumerationLiteral48.setter
    def types_JvmEnumerationLiteral48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmEnumerationLiteral__types_JvmEnumerationLiteral48", None)
        self.__types_JvmEnumerationLiteral48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmEnumAnnotationValue"):
                opp_val = getattr(old_value, "types_JvmEnumAnnotationValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmEnumAnnotationValue"):
                opp_val = getattr(value, "types_JvmEnumAnnotationValue", None)
                if opp_val is None:
                    setattr(value, "types_JvmEnumAnnotationValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getEnumType(self) -> str:
        # TODO: Implement getEnumType method
        pass

class JvmDeclaredType:

    pass
class types_JvmEnumerationType(JvmDeclaredType):

    pass
class types_JvmGenericType(JvmTypeParameterDeclarator, JvmDeclaredType):

    def __init__(self, interface: bool, strictFloatingPoint: bool, anonymous: bool, types_JvmGenericType: "types_JvmFeature" = None):
        self.interface = interface
        self.strictFloatingPoint = strictFloatingPoint
        self.anonymous = anonymous
        self.types_JvmGenericType = types_JvmGenericType
        
    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def strictFloatingPoint(self) -> bool:
        return self.__strictFloatingPoint

    @strictFloatingPoint.setter
    def strictFloatingPoint(self, strictFloatingPoint: bool):
        self.__strictFloatingPoint = strictFloatingPoint

    @property
    def anonymous(self) -> bool:
        return self.__anonymous

    @anonymous.setter
    def anonymous(self, anonymous: bool):
        self.__anonymous = anonymous

    @property
    def types_JvmGenericType(self):
        return self.__types_JvmGenericType

    @types_JvmGenericType.setter
    def types_JvmGenericType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmGenericType__types_JvmGenericType", None)
        self.__types_JvmGenericType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmFeature"):
                opp_val = getattr(old_value, "types_JvmFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmFeature"):
                opp_val = getattr(value, "types_JvmFeature", None)
                if opp_val is None:
                    setattr(value, "types_JvmFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class types_JvmAnnotationType(JvmDeclaredType):

    pass
class JvmTypeConstraint:

    pass
class types_JvmLowerBound(JvmTypeConstraint):

    pass
class types_JvmUpperBound(JvmTypeConstraint):

    pass
class JvmMember:

    pass
class types_JvmFeature(JvmMember):

    def __init__(self, types_JvmFeature: set["types_JvmGenericType"] = None):
        self.types_JvmFeature = types_JvmFeature if types_JvmFeature is not None else set()
        
    @property
    def types_JvmFeature(self):
        return self.__types_JvmFeature

    @types_JvmFeature.setter
    def types_JvmFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmFeature__types_JvmFeature", None)
        self.__types_JvmFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_JvmGenericType"):
                    opp_val = getattr(item, "types_JvmGenericType", None)
                    
                    if opp_val == self:
                        setattr(item, "types_JvmGenericType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_JvmGenericType"):
                    opp_val = getattr(item, "types_JvmGenericType", None)
                    
                    setattr(item, "types_JvmGenericType", self)
                    

    def isStatic(self) -> bool:
        # TODO: Implement isStatic method
        pass

class JvmComponentType:

    pass
class types_JvmDeclaredType(JvmMember, JvmComponentType):

    def __init__(self, abstract: bool, static: bool, final: bool, packageName: str, types_JvmDeclaredType: set["types_JvmTypeReference"] = None, declaringType: set["types_JvmMember"] = None, JvmDeclaredType: "types_JvmMember" = None):
        self.abstract = abstract
        self.static = static
        self.final = final
        self.packageName = packageName
        self.types_JvmDeclaredType = types_JvmDeclaredType if types_JvmDeclaredType is not None else set()
        self.declaringType = declaringType if declaringType is not None else set()
        self.JvmDeclaredType = JvmDeclaredType
        
    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

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

    @property
    def types_JvmDeclaredType(self):
        return self.__types_JvmDeclaredType

    @types_JvmDeclaredType.setter
    def types_JvmDeclaredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmDeclaredType__types_JvmDeclaredType", None)
        self.__types_JvmDeclaredType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_JvmTypeReference"):
                    opp_val = getattr(item, "types_JvmTypeReference", None)
                    
                    if opp_val == self:
                        setattr(item, "types_JvmTypeReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_JvmTypeReference"):
                    opp_val = getattr(item, "types_JvmTypeReference", None)
                    
                    setattr(item, "types_JvmTypeReference", self)
                    

    @property
    def JvmDeclaredType(self):
        return self.__JvmDeclaredType

    @JvmDeclaredType.setter
    def JvmDeclaredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmDeclaredType__JvmDeclaredType", None)
        self.__JvmDeclaredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "members"):
                opp_val = getattr(old_value, "members", None)
                if opp_val == self:
                    setattr(old_value, "members", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "members"):
                opp_val = getattr(value, "members", None)
                setattr(value, "members", self)

    @property
    def declaringType(self):
        return self.__declaringType

    @declaringType.setter
    def declaringType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmDeclaredType__declaringType", None)
        self.__declaringType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmMember"):
                    opp_val = getattr(item, "JvmMember", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmMember"):
                    opp_val = getattr(item, "JvmMember", None)
                    
                    setattr(item, "JvmMember", self)
                    

    def isInstantiateable(self) -> bool:
        # TODO: Implement isInstantiateable method
        pass

    def findAllFeaturesByName(self, simpleName: str):
        # TODO: Implement findAllFeaturesByName method
        pass

    def getDeclaredFields(self):
        # TODO: Implement getDeclaredFields method
        pass

    def getDeclaredOperations(self):
        # TODO: Implement getDeclaredOperations method
        pass

    def getDeclaredConstructors(self):
        # TODO: Implement getDeclaredConstructors method
        pass

    def getAllNestedTypes(self):
        # TODO: Implement getAllNestedTypes method
        pass

    def getExtendedInterfaces(self):
        # TODO: Implement getExtendedInterfaces method
        pass

    def getExtendedClass(self) -> str:
        # TODO: Implement getExtendedClass method
        pass

    def findAllNestedTypesByName(self, simpleName: str):
        # TODO: Implement findAllNestedTypesByName method
        pass

    def getAllFeatures(self):
        # TODO: Implement getAllFeatures method
        pass

    def isLocal(self) -> bool:
        # TODO: Implement isLocal method
        pass

class types_JvmTypeParameter(JvmComponentType, JvmConstraintOwner):

    def __init__(self, name: str, typeParameters: "types_JvmTypeParameterDeclarator" = None, JvmTypeParameter: "types_JvmTypeParameterDeclarator" = None):
        self.name = name
        self.typeParameters = typeParameters
        self.JvmTypeParameter = JvmTypeParameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def JvmTypeParameter(self):
        return self.__JvmTypeParameter

    @JvmTypeParameter.setter
    def JvmTypeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeParameter__JvmTypeParameter", None)
        self.__JvmTypeParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declarator"):
                opp_val = getattr(old_value, "declarator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declarator"):
                opp_val = getattr(value, "declarator", None)
                if opp_val is None:
                    setattr(value, "declarator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def typeParameters(self):
        return self.__typeParameters

    @typeParameters.setter
    def typeParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeParameter__typeParameters", None)
        self.__typeParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeParameterDeclarator"):
                opp_val = getattr(old_value, "JvmTypeParameterDeclarator", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeParameterDeclarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeParameterDeclarator"):
                opp_val = getattr(value, "JvmTypeParameterDeclarator", None)
                setattr(value, "JvmTypeParameterDeclarator", self)

class types_JvmPrimitiveType(JvmComponentType):

    def __init__(self, simpleName: str):
        self.simpleName = simpleName
        
    @property
    def simpleName(self) -> str:
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName

class types_JvmTypeReference(ABC):

    def __init__(self, types_JvmTypeReference: "types_JvmDeclaredType" = None, types_JvmTypeReference8: "types_JvmTypeConstraint" = None, types_JvmTypeReference16: "types_JvmGenericArrayTypeReference" = None, types_JvmTypeReference12: "types_JvmParameterizedTypeReference" = None, types_JvmTypeReference26: "types_JvmExecutable" = None, types_JvmTypeReference22: "types_JvmField" = None, types_JvmTypeReference28: "types_JvmOperation" = None, types_JvmTypeReference33: "types_JvmFormalParameter" = None, types_JvmTypeReference50: "types_JvmDelegateTypeReference" = None, types_JvmTypeReference52: "types_JvmSpecializedTypeReference" = None, types_JvmTypeReference44: "types_JvmTypeAnnotationValue" = None, types_JvmTypeReference57: "types_JvmCompoundTypeReference" = None):
        self.types_JvmTypeReference = types_JvmTypeReference
        self.types_JvmTypeReference8 = types_JvmTypeReference8
        self.types_JvmTypeReference16 = types_JvmTypeReference16
        self.types_JvmTypeReference12 = types_JvmTypeReference12
        self.types_JvmTypeReference26 = types_JvmTypeReference26
        self.types_JvmTypeReference22 = types_JvmTypeReference22
        self.types_JvmTypeReference28 = types_JvmTypeReference28
        self.types_JvmTypeReference33 = types_JvmTypeReference33
        self.types_JvmTypeReference50 = types_JvmTypeReference50
        self.types_JvmTypeReference52 = types_JvmTypeReference52
        self.types_JvmTypeReference44 = types_JvmTypeReference44
        self.types_JvmTypeReference57 = types_JvmTypeReference57
        
    @property
    def types_JvmTypeReference44(self):
        return self.__types_JvmTypeReference44

    @types_JvmTypeReference44.setter
    def types_JvmTypeReference44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference44", None)
        self.__types_JvmTypeReference44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmTypeAnnotationValue"):
                opp_val = getattr(old_value, "types_JvmTypeAnnotationValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmTypeAnnotationValue"):
                opp_val = getattr(value, "types_JvmTypeAnnotationValue", None)
                if opp_val is None:
                    setattr(value, "types_JvmTypeAnnotationValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_JvmTypeReference33(self):
        return self.__types_JvmTypeReference33

    @types_JvmTypeReference33.setter
    def types_JvmTypeReference33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference33", None)
        self.__types_JvmTypeReference33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmFormalParameter32"):
                opp_val = getattr(old_value, "types_JvmFormalParameter32", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmFormalParameter32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmFormalParameter32"):
                opp_val = getattr(value, "types_JvmFormalParameter32", None)
                setattr(value, "types_JvmFormalParameter32", self)

    @property
    def types_JvmTypeReference57(self):
        return self.__types_JvmTypeReference57

    @types_JvmTypeReference57.setter
    def types_JvmTypeReference57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference57", None)
        self.__types_JvmTypeReference57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmCompoundTypeReference56"):
                opp_val = getattr(old_value, "types_JvmCompoundTypeReference56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmCompoundTypeReference56"):
                opp_val = getattr(value, "types_JvmCompoundTypeReference56", None)
                if opp_val is None:
                    setattr(value, "types_JvmCompoundTypeReference56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_JvmTypeReference22(self):
        return self.__types_JvmTypeReference22

    @types_JvmTypeReference22.setter
    def types_JvmTypeReference22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference22", None)
        self.__types_JvmTypeReference22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmField"):
                opp_val = getattr(old_value, "types_JvmField", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmField"):
                opp_val = getattr(value, "types_JvmField", None)
                setattr(value, "types_JvmField", self)

    @property
    def types_JvmTypeReference(self):
        return self.__types_JvmTypeReference

    @types_JvmTypeReference.setter
    def types_JvmTypeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference", None)
        self.__types_JvmTypeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmDeclaredType"):
                opp_val = getattr(old_value, "types_JvmDeclaredType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmDeclaredType"):
                opp_val = getattr(value, "types_JvmDeclaredType", None)
                if opp_val is None:
                    setattr(value, "types_JvmDeclaredType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_JvmTypeReference26(self):
        return self.__types_JvmTypeReference26

    @types_JvmTypeReference26.setter
    def types_JvmTypeReference26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference26", None)
        self.__types_JvmTypeReference26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmExecutable25"):
                opp_val = getattr(old_value, "types_JvmExecutable25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmExecutable25"):
                opp_val = getattr(value, "types_JvmExecutable25", None)
                if opp_val is None:
                    setattr(value, "types_JvmExecutable25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_JvmTypeReference12(self):
        return self.__types_JvmTypeReference12

    @types_JvmTypeReference12.setter
    def types_JvmTypeReference12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference12", None)
        self.__types_JvmTypeReference12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmParameterizedTypeReference"):
                opp_val = getattr(old_value, "types_JvmParameterizedTypeReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmParameterizedTypeReference"):
                opp_val = getattr(value, "types_JvmParameterizedTypeReference", None)
                if opp_val is None:
                    setattr(value, "types_JvmParameterizedTypeReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_JvmTypeReference52(self):
        return self.__types_JvmTypeReference52

    @types_JvmTypeReference52.setter
    def types_JvmTypeReference52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference52", None)
        self.__types_JvmTypeReference52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmSpecializedTypeReference"):
                opp_val = getattr(old_value, "types_JvmSpecializedTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmSpecializedTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmSpecializedTypeReference"):
                opp_val = getattr(value, "types_JvmSpecializedTypeReference", None)
                setattr(value, "types_JvmSpecializedTypeReference", self)

    @property
    def types_JvmTypeReference16(self):
        return self.__types_JvmTypeReference16

    @types_JvmTypeReference16.setter
    def types_JvmTypeReference16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference16", None)
        self.__types_JvmTypeReference16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmGenericArrayTypeReference"):
                opp_val = getattr(old_value, "types_JvmGenericArrayTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmGenericArrayTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmGenericArrayTypeReference"):
                opp_val = getattr(value, "types_JvmGenericArrayTypeReference", None)
                setattr(value, "types_JvmGenericArrayTypeReference", self)

    @property
    def types_JvmTypeReference8(self):
        return self.__types_JvmTypeReference8

    @types_JvmTypeReference8.setter
    def types_JvmTypeReference8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference8", None)
        self.__types_JvmTypeReference8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmTypeConstraint"):
                opp_val = getattr(old_value, "types_JvmTypeConstraint", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmTypeConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmTypeConstraint"):
                opp_val = getattr(value, "types_JvmTypeConstraint", None)
                setattr(value, "types_JvmTypeConstraint", self)

    @property
    def types_JvmTypeReference28(self):
        return self.__types_JvmTypeReference28

    @types_JvmTypeReference28.setter
    def types_JvmTypeReference28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference28", None)
        self.__types_JvmTypeReference28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmOperation"):
                opp_val = getattr(old_value, "types_JvmOperation", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmOperation"):
                opp_val = getattr(value, "types_JvmOperation", None)
                setattr(value, "types_JvmOperation", self)

    @property
    def types_JvmTypeReference50(self):
        return self.__types_JvmTypeReference50

    @types_JvmTypeReference50.setter
    def types_JvmTypeReference50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmTypeReference__types_JvmTypeReference50", None)
        self.__types_JvmTypeReference50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_JvmDelegateTypeReference"):
                opp_val = getattr(old_value, "types_JvmDelegateTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "types_JvmDelegateTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_JvmDelegateTypeReference"):
                opp_val = getattr(value, "types_JvmDelegateTypeReference", None)
                setattr(value, "types_JvmDelegateTypeReference", self)

    def getQualifiedName(self, innerClassDelimiter: str) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def getType(self) -> JvmType:
        # TODO: Implement getType method
        pass

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

    def getIdentifier(self) -> str:
        # TODO: Implement getIdentifier method
        pass

    def getQualifiedName(self) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def getSimpleName(self) -> str:
        # TODO: Implement getSimpleName method
        pass

    def accept(self, visitor: str, parameter: str):
        # TODO: Implement accept method
        pass

class types_JvmIdentifiableElement(ABC):

    def __init__(self):
        
    def getSimpleName(self) -> str:
        # TODO: Implement getSimpleName method
        pass

    def getQualifiedName(self, innerClassDelimiter: str) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def getQualifiedName(self) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def getIdentifier(self) -> str:
        # TODO: Implement getIdentifier method
        pass

class types_JvmArrayType(JvmComponentType):

    def __init__(self, JvmArrayType: "types_JvmComponentType" = None, arrayType: "types_JvmComponentType" = None):
        self.JvmArrayType = JvmArrayType
        self.arrayType = arrayType
        
    @property
    def JvmArrayType(self):
        return self.__JvmArrayType

    @JvmArrayType.setter
    def JvmArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmArrayType__JvmArrayType", None)
        self.__JvmArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "componentType"):
                opp_val = getattr(old_value, "componentType", None)
                if opp_val == self:
                    setattr(old_value, "componentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "componentType"):
                opp_val = getattr(value, "componentType", None)
                setattr(value, "componentType", self)

    @property
    def arrayType(self):
        return self.__arrayType

    @arrayType.setter
    def arrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_JvmArrayType__arrayType", None)
        self.__arrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmComponentType"):
                opp_val = getattr(old_value, "JvmComponentType", None)
                if opp_val == self:
                    setattr(old_value, "JvmComponentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmComponentType"):
                opp_val = getattr(value, "JvmComponentType", None)
                setattr(value, "JvmComponentType", self)

    def getDimensions(self) -> int:
        # TODO: Implement getDimensions method
        pass

class JvmType:

    pass
class types_JvmComponentType(JvmType):

    pass
class types_JvmVoid(JvmType):

    pass
class JvmIdentifiableElement:

    pass
class types_JvmAnnotationTarget(JvmIdentifiableElement):

    pass
class types_JvmType(JvmIdentifiableElement):

    pass