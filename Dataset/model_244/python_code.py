from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ecore_EGenericType:

    def __init__(self, ecore_EGenericType: "EGenericType" = None, ecore_EGenericType106: set["EGenericType"] = None, ecore_EGenericType109: "EClassifier" = None, ecore_EGenericType112: "EGenericType" = None, ecore_EGenericType115: "ETypeParameter" = None, ecore_EGenericType118: "EClassifier" = None):
        self.ecore_EGenericType = ecore_EGenericType
        self.ecore_EGenericType106 = ecore_EGenericType106 if ecore_EGenericType106 is not None else set()
        self.ecore_EGenericType109 = ecore_EGenericType109
        self.ecore_EGenericType112 = ecore_EGenericType112
        self.ecore_EGenericType115 = ecore_EGenericType115
        self.ecore_EGenericType118 = ecore_EGenericType118
        
    @property
    def ecore_EGenericType115(self):
        return self.__ecore_EGenericType115

    @ecore_EGenericType115.setter
    def ecore_EGenericType115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType115", None)
        self.__ecore_EGenericType115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ETypeParameter116"):
                opp_val = getattr(old_value, "ETypeParameter116", None)
                if opp_val == self:
                    setattr(old_value, "ETypeParameter116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ETypeParameter116"):
                opp_val = getattr(value, "ETypeParameter116", None)
                setattr(value, "ETypeParameter116", self)

    @property
    def ecore_EGenericType109(self):
        return self.__ecore_EGenericType109

    @ecore_EGenericType109.setter
    def ecore_EGenericType109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType109", None)
        self.__ecore_EGenericType109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClassifier110"):
                opp_val = getattr(old_value, "EClassifier110", None)
                if opp_val == self:
                    setattr(old_value, "EClassifier110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClassifier110"):
                opp_val = getattr(value, "EClassifier110", None)
                setattr(value, "EClassifier110", self)

    @property
    def ecore_EGenericType118(self):
        return self.__ecore_EGenericType118

    @ecore_EGenericType118.setter
    def ecore_EGenericType118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType118", None)
        self.__ecore_EGenericType118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClassifier119"):
                opp_val = getattr(old_value, "EClassifier119", None)
                if opp_val == self:
                    setattr(old_value, "EClassifier119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClassifier119"):
                opp_val = getattr(value, "EClassifier119", None)
                setattr(value, "EClassifier119", self)

    @property
    def ecore_EGenericType112(self):
        return self.__ecore_EGenericType112

    @ecore_EGenericType112.setter
    def ecore_EGenericType112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType112", None)
        self.__ecore_EGenericType112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EGenericType113"):
                opp_val = getattr(old_value, "EGenericType113", None)
                if opp_val == self:
                    setattr(old_value, "EGenericType113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EGenericType113"):
                opp_val = getattr(value, "EGenericType113", None)
                setattr(value, "EGenericType113", self)

    @property
    def ecore_EGenericType(self):
        return self.__ecore_EGenericType

    @ecore_EGenericType.setter
    def ecore_EGenericType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType", None)
        self.__ecore_EGenericType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EGenericType104"):
                opp_val = getattr(old_value, "EGenericType104", None)
                if opp_val == self:
                    setattr(old_value, "EGenericType104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EGenericType104"):
                opp_val = getattr(value, "EGenericType104", None)
                setattr(value, "EGenericType104", self)

    @property
    def ecore_EGenericType106(self):
        return self.__ecore_EGenericType106

    @ecore_EGenericType106.setter
    def ecore_EGenericType106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EGenericType__ecore_EGenericType106", None)
        self.__ecore_EGenericType106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EGenericType107"):
                    opp_val = getattr(item, "EGenericType107", None)
                    
                    if opp_val == self:
                        setattr(item, "EGenericType107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EGenericType107"):
                    opp_val = getattr(item, "EGenericType107", None)
                    
                    setattr(item, "EGenericType107", self)
                    

    def isInstance(self, object: str) -> str:
        # TODO: Implement isInstance method
        pass

class ecore_EStringToStringMapEntry:

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

class EFactory:

    pass
class EParameter:

    pass
class ecore_EObject:

    def __init__(self):
        
    def eIsProxy(self) -> str:
        # TODO: Implement eIsProxy method
        pass

    def eContainer(self) -> str:
        # TODO: Implement eContainer method
        pass

    def eIsSet(self, feature: str) -> str:
        # TODO: Implement eIsSet method
        pass

    def eContainingFeature(self) -> str:
        # TODO: Implement eContainingFeature method
        pass

    def eAllContents(self) -> str:
        # TODO: Implement eAllContents method
        pass

    def eUnset(self, feature: str):
        # TODO: Implement eUnset method
        pass

    def eContents(self) -> str:
        # TODO: Implement eContents method
        pass

    def eResource(self) -> str:
        # TODO: Implement eResource method
        pass

    def eCrossReferences(self) -> str:
        # TODO: Implement eCrossReferences method
        pass

    def eSet(self, newValue: str, feature: str):
        # TODO: Implement eSet method
        pass

    def eInvoke(self, operation: str, arguments: str) -> str:
        # TODO: Implement eInvoke method
        pass

    def eGet(self, feature: str, resolve: str) -> str:
        # TODO: Implement eGet method
        pass

    def eClass(self) -> str:
        # TODO: Implement eClass method
        pass

    def op_eGet(self, feature: str) -> str:
        # TODO: Implement op_eGet method
        pass

    def eContainmentFeature(self) -> str:
        # TODO: Implement eContainmentFeature method
        pass

class ETypedElement:

    pass
class ecore_EParameter(ETypedElement):

    pass
class ecore_EStructuralFeature(ETypedElement):

    def __init__(self, changeable: str, volatile: str, transient: str, defaultValueLiteral: str, defaultValue: str, unsettable: str, derived: str, 196: "EClass" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.defaultValue = defaultValue
        self.unsettable = unsettable
        self.derived = derived
        self.196 = 196
        
    @property
    def transient(self) -> str:
        return self.__transient

    @transient.setter
    def transient(self, transient: str):
        self.__transient = transient

    @property
    def changeable(self) -> str:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: str):
        self.__changeable = changeable

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

    @property
    def derived(self) -> str:
        return self.__derived

    @derived.setter
    def derived(self, derived: str):
        self.__derived = derived

    @property
    def unsettable(self) -> str:
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: str):
        self.__unsettable = unsettable

    @property
    def volatile(self) -> str:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: str):
        self.__volatile = volatile

    @property
    def 196(self):
        return self.__196

    @196.setter
    def 196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EStructuralFeature__196", None)
        self.__196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#97"):
                opp_val = getattr(old_value, "#97", None)
                if opp_val == self:
                    setattr(old_value, "#97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#97"):
                opp_val = getattr(value, "#97", None)
                setattr(value, "#97", self)

    def getContainerClass(self) -> str:
        # TODO: Implement getContainerClass method
        pass

    def getFeatureID(self) -> str:
        # TODO: Implement getFeatureID method
        pass

class ecore_EOperation(ETypedElement):

    def __init__(self, 165: set["EParameter"] = None, ecore_EOperation68: set["EClassifier"] = None, ecore_EOperation70: set["EGenericType"] = None, 160: "EClass" = None, ecore_EOperation: set["ETypeParameter"] = None):
        self.165 = 165 if 165 is not None else set()
        self.ecore_EOperation68 = ecore_EOperation68 if ecore_EOperation68 is not None else set()
        self.ecore_EOperation70 = ecore_EOperation70 if ecore_EOperation70 is not None else set()
        self.160 = 160
        self.ecore_EOperation = ecore_EOperation if ecore_EOperation is not None else set()
        
    @property
    def 165(self):
        return self.__165

    @165.setter
    def 165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__165", None)
        self.__165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#66"):
                    opp_val = getattr(item, "#66", None)
                    
                    if opp_val == self:
                        setattr(item, "#66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#66"):
                    opp_val = getattr(item, "#66", None)
                    
                    setattr(item, "#66", self)
                    

    @property
    def 160(self):
        return self.__160

    @160.setter
    def 160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__160", None)
        self.__160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#61"):
                opp_val = getattr(old_value, "#61", None)
                if opp_val == self:
                    setattr(old_value, "#61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#61"):
                opp_val = getattr(value, "#61", None)
                setattr(value, "#61", self)

    @property
    def ecore_EOperation68(self):
        return self.__ecore_EOperation68

    @ecore_EOperation68.setter
    def ecore_EOperation68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__ecore_EOperation68", None)
        self.__ecore_EOperation68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EClassifier"):
                    opp_val = getattr(item, "EClassifier", None)
                    
                    if opp_val == self:
                        setattr(item, "EClassifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EClassifier"):
                    opp_val = getattr(item, "EClassifier", None)
                    
                    setattr(item, "EClassifier", self)
                    

    @property
    def ecore_EOperation70(self):
        return self.__ecore_EOperation70

    @ecore_EOperation70.setter
    def ecore_EOperation70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__ecore_EOperation70", None)
        self.__ecore_EOperation70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EGenericType71"):
                    opp_val = getattr(item, "EGenericType71", None)
                    
                    if opp_val == self:
                        setattr(item, "EGenericType71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EGenericType71"):
                    opp_val = getattr(item, "EGenericType71", None)
                    
                    setattr(item, "EGenericType71", self)
                    

    @property
    def ecore_EOperation(self):
        return self.__ecore_EOperation

    @ecore_EOperation.setter
    def ecore_EOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EOperation__ecore_EOperation", None)
        self.__ecore_EOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ETypeParameter63"):
                    opp_val = getattr(item, "ETypeParameter63", None)
                    
                    if opp_val == self:
                        setattr(item, "ETypeParameter63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ETypeParameter63"):
                    opp_val = getattr(item, "ETypeParameter63", None)
                    
                    setattr(item, "ETypeParameter63", self)
                    

    def isOverrideOf(self, someOperation: str) -> str:
        # TODO: Implement isOverrideOf method
        pass

    def getOperationID(self) -> str:
        # TODO: Implement getOperationID method
        pass

class EAnnotation:

    pass
class ecore_EModelElement(ABC):

    def __init__(self, 157: set["EAnnotation"] = None):
        self.157 = 157 if 157 is not None else set()
        
    @property
    def 157(self):
        return self.__157

    @157.setter
    def 157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EModelElement__157", None)
        self.__157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#58"):
                    opp_val = getattr(item, "#58", None)
                    
                    if opp_val == self:
                        setattr(item, "#58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#58"):
                    opp_val = getattr(item, "#58", None)
                    
                    setattr(item, "#58", self)
                    

    def getEAnnotation(self, source: str) -> str:
        # TODO: Implement getEAnnotation method
        pass

class EEnum:

    pass
class EEnumLiteral:

    pass
class ETypeParameter:

    pass
class EPackage:

    pass
class ENamedElement:

    pass
class ecore_ETypedElement(ENamedElement):

    def __init__(self, ordered: str, lowerBound: str, upperBound: str, many: str, required: str, unique: str, ecore_ETypedElement: "EClassifier" = None, ecore_ETypedElement101: "EGenericType" = None):
        self.ordered = ordered
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.unique = unique
        self.ecore_ETypedElement = ecore_ETypedElement
        self.ecore_ETypedElement101 = ecore_ETypedElement101
        
    @property
    def unique(self) -> str:
        return self.__unique

    @unique.setter
    def unique(self, unique: str):
        self.__unique = unique

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def ordered(self) -> str:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: str):
        self.__ordered = ordered

    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

    @property
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def ecore_ETypedElement(self):
        return self.__ecore_ETypedElement

    @ecore_ETypedElement.setter
    def ecore_ETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ETypedElement__ecore_ETypedElement", None)
        self.__ecore_ETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClassifier99"):
                opp_val = getattr(old_value, "EClassifier99", None)
                if opp_val == self:
                    setattr(old_value, "EClassifier99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClassifier99"):
                opp_val = getattr(value, "EClassifier99", None)
                setattr(value, "EClassifier99", self)

    @property
    def ecore_ETypedElement101(self):
        return self.__ecore_ETypedElement101

    @ecore_ETypedElement101.setter
    def ecore_ETypedElement101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_ETypedElement__ecore_ETypedElement101", None)
        self.__ecore_ETypedElement101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EGenericType102"):
                opp_val = getattr(old_value, "EGenericType102", None)
                if opp_val == self:
                    setattr(old_value, "EGenericType102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EGenericType102"):
                opp_val = getattr(value, "EGenericType102", None)
                setattr(value, "EGenericType102", self)

class ecore_EEnumLiteral(ENamedElement):

    def __init__(self, value: str, instance: str, literal: str, 151: "EEnum" = None):
        self.value = value
        self.instance = instance
        self.literal = literal
        self.151 = 151
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def instance(self) -> str:
        return self.__instance

    @instance.setter
    def instance(self, instance: str):
        self.__instance = instance

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def 151(self):
        return self.__151

    @151.setter
    def 151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EEnumLiteral__151", None)
        self.__151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#52"):
                opp_val = getattr(old_value, "#52", None)
                if opp_val == self:
                    setattr(old_value, "#52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#52"):
                opp_val = getattr(value, "#52", None)
                setattr(value, "#52", self)

class ecore_ETypeParameter(ENamedElement):

    pass
class ecore_EPackage(ENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, 173: "EFactory" = None, 176: set["EClassifier"] = None, 179: set["EPackage"] = None, 182: "EPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.173 = 173
        self.176 = 176 if 176 is not None else set()
        self.179 = 179 if 179 is not None else set()
        self.182 = 182
        
    @property
    def nsURI(self) -> str:
        return self.__nsURI

    @nsURI.setter
    def nsURI(self, nsURI: str):
        self.__nsURI = nsURI

    @property
    def nsPrefix(self) -> str:
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix

    @property
    def 176(self):
        return self.__176

    @176.setter
    def 176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__176", None)
        self.__176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#77"):
                    opp_val = getattr(item, "#77", None)
                    
                    if opp_val == self:
                        setattr(item, "#77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#77"):
                    opp_val = getattr(item, "#77", None)
                    
                    setattr(item, "#77", self)
                    

    @property
    def 179(self):
        return self.__179

    @179.setter
    def 179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__179", None)
        self.__179 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#80"):
                    opp_val = getattr(item, "#80", None)
                    
                    if opp_val == self:
                        setattr(item, "#80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#80"):
                    opp_val = getattr(item, "#80", None)
                    
                    setattr(item, "#80", self)
                    

    @property
    def 182(self):
        return self.__182

    @182.setter
    def 182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__182", None)
        self.__182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#83"):
                opp_val = getattr(old_value, "#83", None)
                if opp_val == self:
                    setattr(old_value, "#83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#83"):
                opp_val = getattr(value, "#83", None)
                setattr(value, "#83", self)

    @property
    def 173(self):
        return self.__173

    @173.setter
    def 173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EPackage__173", None)
        self.__173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#74"):
                opp_val = getattr(old_value, "#74", None)
                if opp_val == self:
                    setattr(old_value, "#74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#74"):
                opp_val = getattr(value, "#74", None)
                setattr(value, "#74", self)

    def getEClassifier(self, name: str) -> str:
        # TODO: Implement getEClassifier method
        pass

class ecore_EClassifier(ENamedElement):

    def __init__(self, instanceClassName: str, defaultValue: str, instanceTypeName: str, instanceClass: str, 144: "EPackage" = None, ecore_EClassifier: set["ETypeParameter"] = None):
        self.instanceClassName = instanceClassName
        self.defaultValue = defaultValue
        self.instanceTypeName = instanceTypeName
        self.instanceClass = instanceClass
        self.144 = 144
        self.ecore_EClassifier = ecore_EClassifier if ecore_EClassifier is not None else set()
        
    @property
    def instanceTypeName(self) -> str:
        return self.__instanceTypeName

    @instanceTypeName.setter
    def instanceTypeName(self, instanceTypeName: str):
        self.__instanceTypeName = instanceTypeName

    @property
    def instanceClass(self) -> str:
        return self.__instanceClass

    @instanceClass.setter
    def instanceClass(self, instanceClass: str):
        self.__instanceClass = instanceClass

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def 144(self):
        return self.__144

    @144.setter
    def 144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__144", None)
        self.__144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#45"):
                opp_val = getattr(old_value, "#45", None)
                if opp_val == self:
                    setattr(old_value, "#45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#45"):
                opp_val = getattr(value, "#45", None)
                setattr(value, "#45", self)

    @property
    def ecore_EClassifier(self):
        return self.__ecore_EClassifier

    @ecore_EClassifier.setter
    def ecore_EClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClassifier__ecore_EClassifier", None)
        self.__ecore_EClassifier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ETypeParameter"):
                    opp_val = getattr(item, "ETypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ETypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ETypeParameter"):
                    opp_val = getattr(item, "ETypeParameter", None)
                    
                    setattr(item, "ETypeParameter", self)
                    

    def isInstance(self, object: str) -> str:
        # TODO: Implement isInstance method
        pass

    def getClassifierID(self) -> str:
        # TODO: Implement getClassifierID method
        pass

class EGenericType:

    pass
class EReference:

    pass
class EAttribute:

    pass
class EOperation:

    pass
class EClass:

    pass
class EObject:

    pass
class EStringToStringMapEntry:

    pass
class EModelElement:

    pass
class ecore_ENamedElement(EModelElement):

    def __init__(self, name: str, #: "ecore_EAnnotation"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ecore_EFactory(EModelElement):

    def __init__(self, 154: "EPackage" = None, #: "ecore_EAnnotation"):
        self.154 = 154
        
    @property
    def 154(self):
        return self.__154

    @154.setter
    def 154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EFactory__154", None)
        self.__154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#55"):
                opp_val = getattr(old_value, "#55", None)
                if opp_val == self:
                    setattr(old_value, "#55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#55"):
                opp_val = getattr(value, "#55", None)
                setattr(value, "#55", self)

    def convertToString(self, eDataType: str, instanceValue: str) -> str:
        # TODO: Implement convertToString method
        pass

    def createFromString(self, eDataType: str, literalValue: str) -> str:
        # TODO: Implement createFromString method
        pass

    def create(self, eClass: str) -> str:
        # TODO: Implement create method
        pass

class ecore_EAnnotation(EModelElement):

    def __init__(self, source: str, ecore_EAnnotation: set["EStringToStringMapEntry"] = None, 1: "EModelElement" = None, ecore_EAnnotation4: set["EObject"] = None, ecore_EAnnotation6: set["EObject"] = None, #: "ecore_EAnnotation"):
        self.source = source
        self.ecore_EAnnotation = ecore_EAnnotation if ecore_EAnnotation is not None else set()
        self.1 = 1
        self.ecore_EAnnotation4 = ecore_EAnnotation4 if ecore_EAnnotation4 is not None else set()
        self.ecore_EAnnotation6 = ecore_EAnnotation6 if ecore_EAnnotation6 is not None else set()
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def ecore_EAnnotation6(self):
        return self.__ecore_EAnnotation6

    @ecore_EAnnotation6.setter
    def ecore_EAnnotation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation6", None)
        self.__ecore_EAnnotation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EObject7"):
                    opp_val = getattr(item, "EObject7", None)
                    
                    if opp_val == self:
                        setattr(item, "EObject7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EObject7"):
                    opp_val = getattr(item, "EObject7", None)
                    
                    setattr(item, "EObject7", self)
                    

    @property
    def ecore_EAnnotation(self):
        return self.__ecore_EAnnotation

    @ecore_EAnnotation.setter
    def ecore_EAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation", None)
        self.__ecore_EAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EStringToStringMapEntry"):
                    opp_val = getattr(item, "EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EStringToStringMapEntry"):
                    opp_val = getattr(item, "EStringToStringMapEntry", None)
                    
                    setattr(item, "EStringToStringMapEntry", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#"):
                opp_val = getattr(old_value, "#", None)
                if opp_val == self:
                    setattr(old_value, "#", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#"):
                opp_val = getattr(value, "#", None)
                setattr(value, "#", self)

    @property
    def ecore_EAnnotation4(self):
        return self.__ecore_EAnnotation4

    @ecore_EAnnotation4.setter
    def ecore_EAnnotation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAnnotation__ecore_EAnnotation4", None)
        self.__ecore_EAnnotation4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EObject"):
                    opp_val = getattr(item, "EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EObject"):
                    opp_val = getattr(item, "EObject", None)
                    
                    setattr(item, "EObject", self)
                    

class EDataType:

    pass
class ecore_EEnum(EDataType):

    def __init__(self, 148: set["EEnumLiteral"] = None, EDataType: "ecore_EAttribute"):
        self.148 = 148 if 148 is not None else set()
        
    @property
    def 148(self):
        return self.__148

    @148.setter
    def 148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EEnum__148", None)
        self.__148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#49"):
                    opp_val = getattr(item, "#49", None)
                    
                    if opp_val == self:
                        setattr(item, "#49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#49"):
                    opp_val = getattr(item, "#49", None)
                    
                    setattr(item, "#49", self)
                    

    def op_getEEnumLiteral(self, name: str) -> str:
        # TODO: Implement op_getEEnumLiteral method
        pass

    def getEEnumLiteralByLiteral(self, literal: str) -> str:
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

    def getEEnumLiteral(self, value: str) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

class EStructuralFeature:

    pass
class ecore_EReference(EStructuralFeature):

    def __init__(self, containment: str, container: str, resolveProxies: str, ecore_EReference: "EReference" = None, ecore_EReference90: "EClass" = None, ecore_EReference93: set["EAttribute"] = None, EStructuralFeature: "ecore_EClass", #37: "ecore_EClass"):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.ecore_EReference = ecore_EReference
        self.ecore_EReference90 = ecore_EReference90
        self.ecore_EReference93 = ecore_EReference93 if ecore_EReference93 is not None else set()
        
    @property
    def containment(self) -> str:
        return self.__containment

    @containment.setter
    def containment(self, containment: str):
        self.__containment = containment

    @property
    def container(self) -> str:
        return self.__container

    @container.setter
    def container(self, container: str):
        self.__container = container

    @property
    def resolveProxies(self) -> str:
        return self.__resolveProxies

    @resolveProxies.setter
    def resolveProxies(self, resolveProxies: str):
        self.__resolveProxies = resolveProxies

    @property
    def ecore_EReference93(self):
        return self.__ecore_EReference93

    @ecore_EReference93.setter
    def ecore_EReference93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference93", None)
        self.__ecore_EReference93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EAttribute94"):
                    opp_val = getattr(item, "EAttribute94", None)
                    
                    if opp_val == self:
                        setattr(item, "EAttribute94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAttribute94"):
                    opp_val = getattr(item, "EAttribute94", None)
                    
                    setattr(item, "EAttribute94", self)
                    

    @property
    def ecore_EReference90(self):
        return self.__ecore_EReference90

    @ecore_EReference90.setter
    def ecore_EReference90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference90", None)
        self.__ecore_EReference90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EClass91"):
                opp_val = getattr(old_value, "EClass91", None)
                if opp_val == self:
                    setattr(old_value, "EClass91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EClass91"):
                opp_val = getattr(value, "EClass91", None)
                setattr(value, "EClass91", self)

    @property
    def ecore_EReference(self):
        return self.__ecore_EReference

    @ecore_EReference.setter
    def ecore_EReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EReference__ecore_EReference", None)
        self.__ecore_EReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EReference88"):
                opp_val = getattr(old_value, "EReference88", None)
                if opp_val == self:
                    setattr(old_value, "EReference88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EReference88"):
                opp_val = getattr(value, "EReference88", None)
                setattr(value, "EReference88", self)

class EClassifier:

    pass
class ecore_EDataType(EClassifier):

    def __init__(self, serializable: str, EClassifier99: "ecore_ETypedElement", EClassifier: "ecore_EOperation", EClassifier119: "ecore_EGenericType", EClassifier110: "ecore_EGenericType", #77: "ecore_EPackage"):
        self.serializable = serializable
        
    @property
    def serializable(self) -> str:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: str):
        self.__serializable = serializable

class ecore_EClass(EClassifier):

    def __init__(self, abstract: str, interface: str, ecore_EClass: set["EClass"] = None, ecore_EClass20: set["EAttribute"] = None, ecore_EClass23: set["EReference"] = None, 110: set["EOperation"] = None, ecore_EClass13: set["EAttribute"] = None, ecore_EClass15: set["EReference"] = None, ecore_EClass17: set["EReference"] = None, ecore_EClass33: "EAttribute" = None, 136: set["EStructuralFeature"] = None, ecore_EClass39: set["EGenericType"] = None, ecore_EClass41: set["EGenericType"] = None, ecore_EClass26: set["EOperation"] = None, ecore_EClass28: set["EStructuralFeature"] = None, ecore_EClass30: set["EClass"] = None, EClassifier99: "ecore_ETypedElement", EClassifier: "ecore_EOperation", EClassifier119: "ecore_EGenericType", EClassifier110: "ecore_EGenericType", #77: "ecore_EPackage"):
        self.abstract = abstract
        self.interface = interface
        self.ecore_EClass = ecore_EClass if ecore_EClass is not None else set()
        self.ecore_EClass20 = ecore_EClass20 if ecore_EClass20 is not None else set()
        self.ecore_EClass23 = ecore_EClass23 if ecore_EClass23 is not None else set()
        self.110 = 110 if 110 is not None else set()
        self.ecore_EClass13 = ecore_EClass13 if ecore_EClass13 is not None else set()
        self.ecore_EClass15 = ecore_EClass15 if ecore_EClass15 is not None else set()
        self.ecore_EClass17 = ecore_EClass17 if ecore_EClass17 is not None else set()
        self.ecore_EClass33 = ecore_EClass33
        self.136 = 136 if 136 is not None else set()
        self.ecore_EClass39 = ecore_EClass39 if ecore_EClass39 is not None else set()
        self.ecore_EClass41 = ecore_EClass41 if ecore_EClass41 is not None else set()
        self.ecore_EClass26 = ecore_EClass26 if ecore_EClass26 is not None else set()
        self.ecore_EClass28 = ecore_EClass28 if ecore_EClass28 is not None else set()
        self.ecore_EClass30 = ecore_EClass30 if ecore_EClass30 is not None else set()
        
    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def interface(self) -> str:
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface

    @property
    def ecore_EClass39(self):
        return self.__ecore_EClass39

    @ecore_EClass39.setter
    def ecore_EClass39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass39", None)
        self.__ecore_EClass39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EGenericType"):
                    opp_val = getattr(item, "EGenericType", None)
                    
                    if opp_val == self:
                        setattr(item, "EGenericType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EGenericType"):
                    opp_val = getattr(item, "EGenericType", None)
                    
                    setattr(item, "EGenericType", self)
                    

    @property
    def ecore_EClass28(self):
        return self.__ecore_EClass28

    @ecore_EClass28.setter
    def ecore_EClass28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass28", None)
        self.__ecore_EClass28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EStructuralFeature"):
                    opp_val = getattr(item, "EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EStructuralFeature"):
                    opp_val = getattr(item, "EStructuralFeature", None)
                    
                    setattr(item, "EStructuralFeature", self)
                    

    @property
    def ecore_EClass13(self):
        return self.__ecore_EClass13

    @ecore_EClass13.setter
    def ecore_EClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass13", None)
        self.__ecore_EClass13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EAttribute"):
                    opp_val = getattr(item, "EAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "EAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAttribute"):
                    opp_val = getattr(item, "EAttribute", None)
                    
                    setattr(item, "EAttribute", self)
                    

    @property
    def ecore_EClass30(self):
        return self.__ecore_EClass30

    @ecore_EClass30.setter
    def ecore_EClass30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass30", None)
        self.__ecore_EClass30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EClass31"):
                    opp_val = getattr(item, "EClass31", None)
                    
                    if opp_val == self:
                        setattr(item, "EClass31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EClass31"):
                    opp_val = getattr(item, "EClass31", None)
                    
                    setattr(item, "EClass31", self)
                    

    @property
    def ecore_EClass41(self):
        return self.__ecore_EClass41

    @ecore_EClass41.setter
    def ecore_EClass41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass41", None)
        self.__ecore_EClass41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EGenericType42"):
                    opp_val = getattr(item, "EGenericType42", None)
                    
                    if opp_val == self:
                        setattr(item, "EGenericType42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EGenericType42"):
                    opp_val = getattr(item, "EGenericType42", None)
                    
                    setattr(item, "EGenericType42", self)
                    

    @property
    def ecore_EClass23(self):
        return self.__ecore_EClass23

    @ecore_EClass23.setter
    def ecore_EClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass23", None)
        self.__ecore_EClass23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EReference24"):
                    opp_val = getattr(item, "EReference24", None)
                    
                    if opp_val == self:
                        setattr(item, "EReference24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EReference24"):
                    opp_val = getattr(item, "EReference24", None)
                    
                    setattr(item, "EReference24", self)
                    

    @property
    def ecore_EClass26(self):
        return self.__ecore_EClass26

    @ecore_EClass26.setter
    def ecore_EClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass26", None)
        self.__ecore_EClass26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EOperation"):
                    opp_val = getattr(item, "EOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "EOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EOperation"):
                    opp_val = getattr(item, "EOperation", None)
                    
                    setattr(item, "EOperation", self)
                    

    @property
    def ecore_EClass(self):
        return self.__ecore_EClass

    @ecore_EClass.setter
    def ecore_EClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass", None)
        self.__ecore_EClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EClass"):
                    opp_val = getattr(item, "EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EClass"):
                    opp_val = getattr(item, "EClass", None)
                    
                    setattr(item, "EClass", self)
                    

    @property
    def ecore_EClass20(self):
        return self.__ecore_EClass20

    @ecore_EClass20.setter
    def ecore_EClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass20", None)
        self.__ecore_EClass20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EAttribute21"):
                    opp_val = getattr(item, "EAttribute21", None)
                    
                    if opp_val == self:
                        setattr(item, "EAttribute21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EAttribute21"):
                    opp_val = getattr(item, "EAttribute21", None)
                    
                    setattr(item, "EAttribute21", self)
                    

    @property
    def 136(self):
        return self.__136

    @136.setter
    def 136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__136", None)
        self.__136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#37"):
                    opp_val = getattr(item, "#37", None)
                    
                    if opp_val == self:
                        setattr(item, "#37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#37"):
                    opp_val = getattr(item, "#37", None)
                    
                    setattr(item, "#37", self)
                    

    @property
    def 110(self):
        return self.__110

    @110.setter
    def 110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__110", None)
        self.__110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#11"):
                    opp_val = getattr(item, "#11", None)
                    
                    if opp_val == self:
                        setattr(item, "#11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#11"):
                    opp_val = getattr(item, "#11", None)
                    
                    setattr(item, "#11", self)
                    

    @property
    def ecore_EClass15(self):
        return self.__ecore_EClass15

    @ecore_EClass15.setter
    def ecore_EClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass15", None)
        self.__ecore_EClass15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EReference"):
                    opp_val = getattr(item, "EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EReference"):
                    opp_val = getattr(item, "EReference", None)
                    
                    setattr(item, "EReference", self)
                    

    @property
    def ecore_EClass33(self):
        return self.__ecore_EClass33

    @ecore_EClass33.setter
    def ecore_EClass33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass33", None)
        self.__ecore_EClass33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EAttribute34"):
                opp_val = getattr(old_value, "EAttribute34", None)
                if opp_val == self:
                    setattr(old_value, "EAttribute34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EAttribute34"):
                opp_val = getattr(value, "EAttribute34", None)
                setattr(value, "EAttribute34", self)

    @property
    def ecore_EClass17(self):
        return self.__ecore_EClass17

    @ecore_EClass17.setter
    def ecore_EClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EClass__ecore_EClass17", None)
        self.__ecore_EClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EReference18"):
                    opp_val = getattr(item, "EReference18", None)
                    
                    if opp_val == self:
                        setattr(item, "EReference18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EReference18"):
                    opp_val = getattr(item, "EReference18", None)
                    
                    setattr(item, "EReference18", self)
                    

    def getOperationCount(self) -> str:
        # TODO: Implement getOperationCount method
        pass

    def isSuperTypeOf(self, someClass: str) -> str:
        # TODO: Implement isSuperTypeOf method
        pass

    def getOperationID(self, operation: str) -> str:
        # TODO: Implement getOperationID method
        pass

    def getEStructuralFeature(self, featureName: str) -> str:
        # TODO: Implement getEStructuralFeature method
        pass

    def getOverride(self, operation: str) -> str:
        # TODO: Implement getOverride method
        pass

    def getFeatureType(self, feature: str) -> str:
        # TODO: Implement getFeatureType method
        pass

    def getFeatureID(self, feature: str) -> str:
        # TODO: Implement getFeatureID method
        pass

    def getEOperation(self, operationID: str) -> str:
        # TODO: Implement getEOperation method
        pass

    def getFeatureCount(self) -> str:
        # TODO: Implement getFeatureCount method
        pass

    def op_getEStructuralFeature(self, featureID: str) -> str:
        # TODO: Implement op_getEStructuralFeature method
        pass

class ecore_EAttribute(EStructuralFeature):

    def __init__(self, iD: str, ecore_EAttribute: "EDataType" = None, EStructuralFeature: "ecore_EClass", #37: "ecore_EClass"):
        self.iD = iD
        self.ecore_EAttribute = ecore_EAttribute
        
    @property
    def iD(self) -> str:
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD

    @property
    def ecore_EAttribute(self):
        return self.__ecore_EAttribute

    @ecore_EAttribute.setter
    def ecore_EAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_EAttribute__ecore_EAttribute", None)
        self.__ecore_EAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EDataType"):
                opp_val = getattr(old_value, "EDataType", None)
                if opp_val == self:
                    setattr(old_value, "EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EDataType"):
                opp_val = getattr(value, "EDataType", None)
                setattr(value, "EDataType", self)
