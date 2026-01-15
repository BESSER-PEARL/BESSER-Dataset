from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MultiplicityKind(Enum):
    Optional = "Optional"
    One = "One"
    OneOrMore = "OneOrMore"
    ZeroOrMore = "ZeroOrMore"
class ConstraintKind(Enum):
    invariant = "invariant"
    abie = "abie"
    bdt = "bdt"
    dependency = "dependency"
    facet = "facet"
    payload = "payload"
    document = "document"


############################################
# Definition of Classes
############################################

class OclBooleanLiteral:

    pass
class umm_OclBooleanTrue(OclBooleanLiteral):

    pass
class umm_OclBooleanFalse(OclBooleanLiteral):

    pass
class OclLiteral:

    pass
class umm_OclIntegerLiteral(OclLiteral):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class umm_OclBooleanLiteral(OclLiteral):

    pass
class umm_OclStringLiteral(OclLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class umm_OclEnumerationLiteral(OclLiteral):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class OclFunctionCall:

    pass
class umm_OclIsEmpty(OclFunctionCall):

    pass
class umm_OclForAll(OclFunctionCall):

    pass
class umm_OclFunctionCall:

    pass
class umm_OclRef:

    def __init__(self, name: str, multiplicity: str, umm_OclRef: "umm_OclPathFeatureHead" = None, umm_OclRef78: "umm_OclPathTail" = None):
        self.name = name
        self.multiplicity = multiplicity
        self.umm_OclRef = umm_OclRef
        self.umm_OclRef78 = umm_OclRef78
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def multiplicity(self) -> str:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: str):
        self.__multiplicity = multiplicity

    @property
    def umm_OclRef78(self):
        return self.__umm_OclRef78

    @umm_OclRef78.setter
    def umm_OclRef78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_OclRef__umm_OclRef78", None)
        self.__umm_OclRef78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_OclPathTail77"):
                opp_val = getattr(old_value, "umm_OclPathTail77", None)
                if opp_val == self:
                    setattr(old_value, "umm_OclPathTail77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_OclPathTail77"):
                opp_val = getattr(value, "umm_OclPathTail77", None)
                setattr(value, "umm_OclPathTail77", self)

    @property
    def umm_OclRef(self):
        return self.__umm_OclRef

    @umm_OclRef.setter
    def umm_OclRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_OclRef__umm_OclRef", None)
        self.__umm_OclRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_OclPathFeatureHead"):
                opp_val = getattr(old_value, "umm_OclPathFeatureHead", None)
                if opp_val == self:
                    setattr(old_value, "umm_OclPathFeatureHead", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_OclPathFeatureHead"):
                opp_val = getattr(value, "umm_OclPathFeatureHead", None)
                setattr(value, "umm_OclPathFeatureHead", self)

class umm_OclSize(OclFunctionCall):

    pass
class umm_OclNotEmpty(OclFunctionCall):

    pass
class OclValue:

    pass
class umm_OclLiteral(OclValue):

    pass
class umm_OclReference(OclValue):

    pass
class OclExpression:

    pass
class umm_OclMoreOrEqual(OclExpression):

    pass
class umm_OclMore(OclExpression):

    pass
class umm_OclXor(OclExpression):

    pass
class umm_OclEqual(OclExpression):

    pass
class umm_OclAnd(OclExpression):

    pass
class umm_OclImplies(OclExpression):

    pass
class umm_OclLess(OclExpression):

    pass
class umm_OclArrow(OclExpression):

    pass
class umm_OclLessOrEqual(OclExpression):

    pass
class umm_OclOr(OclExpression):

    pass
class umm_OclValue(OclExpression):

    pass
class umm_OclExpression:

    pass
class CDTProperty:

    pass
class umm_CDT_Supplement(CDTProperty):

    def __init__(self, defaultValue: str, restriction: str, fixedValue: str):
        self.defaultValue = defaultValue
        self.restriction = restriction
        self.fixedValue = fixedValue
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def restriction(self) -> str:
        return self.__restriction

    @restriction.setter
    def restriction(self, restriction: str):
        self.__restriction = restriction

    @property
    def fixedValue(self) -> str:
        return self.__fixedValue

    @fixedValue.setter
    def fixedValue(self, fixedValue: str):
        self.__fixedValue = fixedValue

class umm_CDT_Content(CDTProperty):

    pass
class umm_OclPathTail:

    pass
class OclReference:

    pass
class umm_OclPathFeatureHead(OclReference):

    pass
class umm_OclPathSelfHead(OclReference):

    pass
class umm_CDTProperty:

    def __init__(self, definition: str, dictionary: str, uniqueIdentifier: str, versionIdentifier: str, multiplicity: str, name: str, businessTerm: str, umm_CDTProperty: "umm_CDT" = None, umm_CDTProperty66: "umm_Primitive" = None):
        self.definition = definition
        self.dictionary = dictionary
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.multiplicity = multiplicity
        self.name = name
        self.businessTerm = businessTerm
        self.umm_CDTProperty = umm_CDTProperty
        self.umm_CDTProperty66 = umm_CDTProperty66
        
    @property
    def dictionary(self) -> str:
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary: str):
        self.__dictionary = dictionary

    @property
    def multiplicity(self) -> str:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: str):
        self.__multiplicity = multiplicity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def umm_CDTProperty66(self):
        return self.__umm_CDTProperty66

    @umm_CDTProperty66.setter
    def umm_CDTProperty66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_CDTProperty__umm_CDTProperty66", None)
        self.__umm_CDTProperty66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_Primitive"):
                opp_val = getattr(old_value, "umm_Primitive", None)
                if opp_val == self:
                    setattr(old_value, "umm_Primitive", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_Primitive"):
                opp_val = getattr(value, "umm_Primitive", None)
                setattr(value, "umm_Primitive", self)

    @property
    def umm_CDTProperty(self):
        return self.__umm_CDTProperty

    @umm_CDTProperty.setter
    def umm_CDTProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_CDTProperty__umm_CDTProperty", None)
        self.__umm_CDTProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_CDT64"):
                opp_val = getattr(old_value, "umm_CDT64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_CDT64"):
                opp_val = getattr(value, "umm_CDT64", None)
                if opp_val is None:
                    setattr(value, "umm_CDT64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umm_CDT:

    def __init__(self, name: str, businessTerm: str, definition: str, dictionary: str, uniqueIdentifier: str, versionIdentifier: str, umm_CDT: "umm_BCC" = None, umm_CDT62: "umm_CDTLibrary" = None, umm_CDT64: set["umm_CDTProperty"] = None):
        self.name = name
        self.businessTerm = businessTerm
        self.definition = definition
        self.dictionary = dictionary
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.umm_CDT = umm_CDT
        self.umm_CDT62 = umm_CDT62
        self.umm_CDT64 = umm_CDT64 if umm_CDT64 is not None else set()
        
    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def dictionary(self) -> str:
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary: str):
        self.__dictionary = dictionary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def umm_CDT64(self):
        return self.__umm_CDT64

    @umm_CDT64.setter
    def umm_CDT64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_CDT__umm_CDT64", None)
        self.__umm_CDT64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_CDTProperty"):
                    opp_val = getattr(item, "umm_CDTProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_CDTProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_CDTProperty"):
                    opp_val = getattr(item, "umm_CDTProperty", None)
                    
                    setattr(item, "umm_CDTProperty", self)
                    

    @property
    def umm_CDT(self):
        return self.__umm_CDT

    @umm_CDT.setter
    def umm_CDT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_CDT__umm_CDT", None)
        self.__umm_CDT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_BCC"):
                opp_val = getattr(old_value, "umm_BCC", None)
                if opp_val == self:
                    setattr(old_value, "umm_BCC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_BCC"):
                opp_val = getattr(value, "umm_BCC", None)
                setattr(value, "umm_BCC", self)

    @property
    def umm_CDT62(self):
        return self.__umm_CDT62

    @umm_CDT62.setter
    def umm_CDT62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_CDT__umm_CDT62", None)
        self.__umm_CDT62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_CDTLibrary"):
                opp_val = getattr(old_value, "umm_CDTLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_CDTLibrary"):
                opp_val = getattr(value, "umm_CDTLibrary", None)
                if opp_val is None:
                    setattr(value, "umm_CDTLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ACCProperty:

    pass
class umm_BCC(ACCProperty):

    def __init__(self, restriction: str, fixedValue: str, umm_BCC: "umm_CDT" = None):
        self.restriction = restriction
        self.fixedValue = fixedValue
        self.umm_BCC = umm_BCC
        
    @property
    def fixedValue(self) -> str:
        return self.__fixedValue

    @fixedValue.setter
    def fixedValue(self, fixedValue: str):
        self.__fixedValue = fixedValue

    @property
    def restriction(self) -> str:
        return self.__restriction

    @restriction.setter
    def restriction(self, restriction: str):
        self.__restriction = restriction

    @property
    def umm_BCC(self):
        return self.__umm_BCC

    @umm_BCC.setter
    def umm_BCC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BCC__umm_BCC", None)
        self.__umm_BCC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_CDT"):
                opp_val = getattr(old_value, "umm_CDT", None)
                if opp_val == self:
                    setattr(old_value, "umm_CDT", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_CDT"):
                opp_val = getattr(value, "umm_CDT", None)
                setattr(value, "umm_CDT", self)

class umm_ASCC(ACCProperty):

    pass
class umm_ACCProperty:

    def __init__(self, multiplicity: str, name: str, businessTerm: str, definition: str, dictionary: str, uniqueIdentifier: str, versionIdentifier: str, sequencingKey: str, umm_ACCProperty: "umm_ACC" = None):
        self.multiplicity = multiplicity
        self.name = name
        self.businessTerm = businessTerm
        self.definition = definition
        self.dictionary = dictionary
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.sequencingKey = sequencingKey
        self.umm_ACCProperty = umm_ACCProperty
        
    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def multiplicity(self) -> str:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: str):
        self.__multiplicity = multiplicity

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def dictionary(self) -> str:
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary: str):
        self.__dictionary = dictionary

    @property
    def sequencingKey(self) -> str:
        return self.__sequencingKey

    @sequencingKey.setter
    def sequencingKey(self, sequencingKey: str):
        self.__sequencingKey = sequencingKey

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umm_ACCProperty(self):
        return self.__umm_ACCProperty

    @umm_ACCProperty.setter
    def umm_ACCProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ACCProperty__umm_ACCProperty", None)
        self.__umm_ACCProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_ACC54"):
                opp_val = getattr(old_value, "umm_ACC54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_ACC54"):
                opp_val = getattr(value, "umm_ACC54", None)
                if opp_val is None:
                    setattr(value, "umm_ACC54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umm_ACC:

    def __init__(self, name: str, businessTerm: str, definition: str, dictionary: str, uniqueIdentifier: str, versionIdentifier: str, umm_ACC: "umm_CCLibrary" = None, umm_ACC54: set["umm_ACCProperty"] = None, umm_ACC56: set["umm_Constraint"] = None, umm_ACC59: "umm_ASCC" = None):
        self.name = name
        self.businessTerm = businessTerm
        self.definition = definition
        self.dictionary = dictionary
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.umm_ACC = umm_ACC
        self.umm_ACC54 = umm_ACC54 if umm_ACC54 is not None else set()
        self.umm_ACC56 = umm_ACC56 if umm_ACC56 is not None else set()
        self.umm_ACC59 = umm_ACC59
        
    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def dictionary(self) -> str:
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary: str):
        self.__dictionary = dictionary

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def umm_ACC56(self):
        return self.__umm_ACC56

    @umm_ACC56.setter
    def umm_ACC56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ACC__umm_ACC56", None)
        self.__umm_ACC56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_Constraint57"):
                    opp_val = getattr(item, "umm_Constraint57", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_Constraint57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_Constraint57"):
                    opp_val = getattr(item, "umm_Constraint57", None)
                    
                    setattr(item, "umm_Constraint57", self)
                    

    @property
    def umm_ACC59(self):
        return self.__umm_ACC59

    @umm_ACC59.setter
    def umm_ACC59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ACC__umm_ACC59", None)
        self.__umm_ACC59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_ASCC"):
                opp_val = getattr(old_value, "umm_ASCC", None)
                if opp_val == self:
                    setattr(old_value, "umm_ASCC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_ASCC"):
                opp_val = getattr(value, "umm_ASCC", None)
                setattr(value, "umm_ASCC", self)

    @property
    def umm_ACC(self):
        return self.__umm_ACC

    @umm_ACC.setter
    def umm_ACC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ACC__umm_ACC", None)
        self.__umm_ACC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_CCLibrary"):
                opp_val = getattr(old_value, "umm_CCLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_CCLibrary"):
                opp_val = getattr(value, "umm_CCLibrary", None)
                if opp_val is None:
                    setattr(value, "umm_CCLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umm_ACC54(self):
        return self.__umm_ACC54

    @umm_ACC54.setter
    def umm_ACC54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ACC__umm_ACC54", None)
        self.__umm_ACC54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_ACCProperty"):
                    opp_val = getattr(item, "umm_ACCProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_ACCProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_ACCProperty"):
                    opp_val = getattr(item, "umm_ACCProperty", None)
                    
                    setattr(item, "umm_ACCProperty", self)
                    

class umm_CodelistEntry:

    def __init__(self, name: str, description: str, umm_CodelistEntry: "umm_Original" = None, umm_CodelistEntry51: "umm_Subset" = None):
        self.name = name
        self.description = description
        self.umm_CodelistEntry = umm_CodelistEntry
        self.umm_CodelistEntry51 = umm_CodelistEntry51
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umm_CodelistEntry51(self):
        return self.__umm_CodelistEntry51

    @umm_CodelistEntry51.setter
    def umm_CodelistEntry51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_CodelistEntry__umm_CodelistEntry51", None)
        self.__umm_CodelistEntry51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_Subset50"):
                opp_val = getattr(old_value, "umm_Subset50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_Subset50"):
                opp_val = getattr(value, "umm_Subset50", None)
                if opp_val is None:
                    setattr(value, "umm_Subset50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umm_CodelistEntry(self):
        return self.__umm_CodelistEntry

    @umm_CodelistEntry.setter
    def umm_CodelistEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_CodelistEntry__umm_CodelistEntry", None)
        self.__umm_CodelistEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_Original48"):
                opp_val = getattr(old_value, "umm_Original48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_Original48"):
                opp_val = getattr(value, "umm_Original48", None)
                if opp_val is None:
                    setattr(value, "umm_Original48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ENUM:

    pass
class umm_Subset(ENUM):

    pass
class umm_ENUM:

    def __init__(self, name: str, businessTerm: str, definition: str, codeListAgencyIdentifier: str, codeListName: str, codeListIdentifier: str, dictionary: str, uniqueIdentifier: str, versionIdentifier: str, umm_ENUM: "umm_ENUMLibrary" = None):
        self.name = name
        self.businessTerm = businessTerm
        self.definition = definition
        self.codeListAgencyIdentifier = codeListAgencyIdentifier
        self.codeListName = codeListName
        self.codeListIdentifier = codeListIdentifier
        self.dictionary = dictionary
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.umm_ENUM = umm_ENUM
        
    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def dictionary(self) -> str:
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary: str):
        self.__dictionary = dictionary

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def codeListIdentifier(self) -> str:
        return self.__codeListIdentifier

    @codeListIdentifier.setter
    def codeListIdentifier(self, codeListIdentifier: str):
        self.__codeListIdentifier = codeListIdentifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def codeListName(self) -> str:
        return self.__codeListName

    @codeListName.setter
    def codeListName(self, codeListName: str):
        self.__codeListName = codeListName

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def codeListAgencyIdentifier(self) -> str:
        return self.__codeListAgencyIdentifier

    @codeListAgencyIdentifier.setter
    def codeListAgencyIdentifier(self, codeListAgencyIdentifier: str):
        self.__codeListAgencyIdentifier = codeListAgencyIdentifier

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def umm_ENUM(self):
        return self.__umm_ENUM

    @umm_ENUM.setter
    def umm_ENUM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ENUM__umm_ENUM", None)
        self.__umm_ENUM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_ENUMLibrary"):
                opp_val = getattr(old_value, "umm_ENUMLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_ENUMLibrary"):
                opp_val = getattr(value, "umm_ENUMLibrary", None)
                if opp_val is None:
                    setattr(value, "umm_ENUMLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umm_Original(ENUM):

    pass
class AssembledBase:

    pass
class umm_Assembled(AssembledBase):

    pass
class umm_Primitive(AssembledBase):

    pass
class BDTProperty:

    pass
class umm_Supplement(BDTProperty):

    def __init__(self, fixedValue: str, defaultValue: str, restriction: str):
        self.fixedValue = fixedValue
        self.defaultValue = defaultValue
        self.restriction = restriction
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def restriction(self) -> str:
        return self.__restriction

    @restriction.setter
    def restriction(self, restriction: str):
        self.__restriction = restriction

    @property
    def fixedValue(self) -> str:
        return self.__fixedValue

    @fixedValue.setter
    def fixedValue(self, fixedValue: str):
        self.__fixedValue = fixedValue

class umm_Content(BDTProperty):

    def __init__(self, maxInclusive: int, maxExclusive: int, minInclusive: int, minExclusive: int, fractionalDigits: int, totalDigits: int):
        self.maxInclusive = maxInclusive
        self.maxExclusive = maxExclusive
        self.minInclusive = minInclusive
        self.minExclusive = minExclusive
        self.fractionalDigits = fractionalDigits
        self.totalDigits = totalDigits
        
    @property
    def maxExclusive(self) -> int:
        return self.__maxExclusive

    @maxExclusive.setter
    def maxExclusive(self, maxExclusive: int):
        self.__maxExclusive = maxExclusive

    @property
    def minInclusive(self) -> int:
        return self.__minInclusive

    @minInclusive.setter
    def minInclusive(self, minInclusive: int):
        self.__minInclusive = minInclusive

    @property
    def fractionalDigits(self) -> int:
        return self.__fractionalDigits

    @fractionalDigits.setter
    def fractionalDigits(self, fractionalDigits: int):
        self.__fractionalDigits = fractionalDigits

    @property
    def maxInclusive(self) -> int:
        return self.__maxInclusive

    @maxInclusive.setter
    def maxInclusive(self, maxInclusive: int):
        self.__maxInclusive = maxInclusive

    @property
    def minExclusive(self) -> int:
        return self.__minExclusive

    @minExclusive.setter
    def minExclusive(self, minExclusive: int):
        self.__minExclusive = minExclusive

    @property
    def totalDigits(self) -> int:
        return self.__totalDigits

    @totalDigits.setter
    def totalDigits(self, totalDigits: int):
        self.__totalDigits = totalDigits

class umm_AssembledBase(ENUM):

    pass
class ABIEProperty:

    pass
class umm_BBIE(ABIEProperty):

    def __init__(self, restriction: str, fixedValue: str, umm_BBIE: "umm_BDT" = None):
        self.restriction = restriction
        self.fixedValue = fixedValue
        self.umm_BBIE = umm_BBIE
        
    @property
    def restriction(self) -> str:
        return self.__restriction

    @restriction.setter
    def restriction(self, restriction: str):
        self.__restriction = restriction

    @property
    def fixedValue(self) -> str:
        return self.__fixedValue

    @fixedValue.setter
    def fixedValue(self, fixedValue: str):
        self.__fixedValue = fixedValue

    @property
    def umm_BBIE(self):
        return self.__umm_BBIE

    @umm_BBIE.setter
    def umm_BBIE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BBIE__umm_BBIE", None)
        self.__umm_BBIE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_BDT"):
                opp_val = getattr(old_value, "umm_BDT", None)
                if opp_val == self:
                    setattr(old_value, "umm_BDT", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_BDT"):
                opp_val = getattr(value, "umm_BDT", None)
                setattr(value, "umm_BDT", self)

class umm_ASBIE(ABIEProperty):

    pass
class umm_OclInvariant:

    pass
class umm_TC_Constraint:

    def __init__(self, listIdentifier: str, responsibleAgency: str, kind: str, umm_TC_Constraint: "umm_Constraint" = None):
        self.listIdentifier = listIdentifier
        self.responsibleAgency = responsibleAgency
        self.kind = kind
        self.umm_TC_Constraint = umm_TC_Constraint
        
    @property
    def listIdentifier(self) -> str:
        return self.__listIdentifier

    @listIdentifier.setter
    def listIdentifier(self, listIdentifier: str):
        self.__listIdentifier = listIdentifier

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def responsibleAgency(self) -> str:
        return self.__responsibleAgency

    @responsibleAgency.setter
    def responsibleAgency(self, responsibleAgency: str):
        self.__responsibleAgency = responsibleAgency

    @property
    def umm_TC_Constraint(self):
        return self.__umm_TC_Constraint

    @umm_TC_Constraint.setter
    def umm_TC_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_TC_Constraint__umm_TC_Constraint", None)
        self.__umm_TC_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_Constraint16"):
                opp_val = getattr(old_value, "umm_Constraint16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_Constraint16"):
                opp_val = getattr(value, "umm_Constraint16", None)
                if opp_val is None:
                    setattr(value, "umm_Constraint16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umm_ContextRef:

    def __init__(self, name: str, umm_ContextRef: "umm_Constraint" = None):
        self.name = name
        self.umm_ContextRef = umm_ContextRef
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umm_ContextRef(self):
        return self.__umm_ContextRef

    @umm_ContextRef.setter
    def umm_ContextRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ContextRef__umm_ContextRef", None)
        self.__umm_ContextRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_Constraint14"):
                opp_val = getattr(old_value, "umm_Constraint14", None)
                if opp_val == self:
                    setattr(old_value, "umm_Constraint14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_Constraint14"):
                opp_val = getattr(value, "umm_Constraint14", None)
                setattr(value, "umm_Constraint14", self)

class MAProperty:

    pass
class umm_ASNONE(MAProperty):

    pass
class umm_ASMA(MAProperty):

    pass
class OclRef:

    pass
class umm_BDTProperty(OclRef):

    def __init__(self, pattern: str, minLength: int, maxLength: int, length: int, businessTerm: str, definition: str, dictionary: str, uniqueIdentifier: str, versionIdentifier: str, umm_BDTProperty42: "umm_AssembledBase" = None, umm_BDTProperty: "umm_BDT" = None):
        self.pattern = pattern
        self.minLength = minLength
        self.maxLength = maxLength
        self.length = length
        self.businessTerm = businessTerm
        self.definition = definition
        self.dictionary = dictionary
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.umm_BDTProperty42 = umm_BDTProperty42
        self.umm_BDTProperty = umm_BDTProperty
        
    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def maxLength(self) -> int:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def minLength(self) -> int:
        return self.__minLength

    @minLength.setter
    def minLength(self, minLength: int):
        self.__minLength = minLength

    @property
    def dictionary(self) -> str:
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary: str):
        self.__dictionary = dictionary

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def umm_BDTProperty42(self):
        return self.__umm_BDTProperty42

    @umm_BDTProperty42.setter
    def umm_BDTProperty42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BDTProperty__umm_BDTProperty42", None)
        self.__umm_BDTProperty42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_AssembledBase"):
                opp_val = getattr(old_value, "umm_AssembledBase", None)
                if opp_val == self:
                    setattr(old_value, "umm_AssembledBase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_AssembledBase"):
                opp_val = getattr(value, "umm_AssembledBase", None)
                setattr(value, "umm_AssembledBase", self)

    @property
    def umm_BDTProperty(self):
        return self.__umm_BDTProperty

    @umm_BDTProperty.setter
    def umm_BDTProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BDTProperty__umm_BDTProperty", None)
        self.__umm_BDTProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_BDT40"):
                opp_val = getattr(old_value, "umm_BDT40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_BDT40"):
                opp_val = getattr(value, "umm_BDT40", None)
                if opp_val is None:
                    setattr(value, "umm_BDT40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umm_ABIEProperty(OclRef):

    def __init__(self, businessTerm: str, definition: str, dictionary: str, uniqueIdentifier: str, versionIdentifier: str, sequencingKey: str, umm_ABIEProperty: "umm_ABIE" = None, umm_ABIEProperty32: "umm_ABIEProperty" = None, umm_ABIEProperty30: set["umm_ABIEProperty"] = None):
        self.businessTerm = businessTerm
        self.definition = definition
        self.dictionary = dictionary
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.sequencingKey = sequencingKey
        self.umm_ABIEProperty = umm_ABIEProperty
        self.umm_ABIEProperty32 = umm_ABIEProperty32
        self.umm_ABIEProperty30 = umm_ABIEProperty30 if umm_ABIEProperty30 is not None else set()
        
    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def sequencingKey(self) -> str:
        return self.__sequencingKey

    @sequencingKey.setter
    def sequencingKey(self, sequencingKey: str):
        self.__sequencingKey = sequencingKey

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def dictionary(self) -> str:
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary: str):
        self.__dictionary = dictionary

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def umm_ABIEProperty30(self):
        return self.__umm_ABIEProperty30

    @umm_ABIEProperty30.setter
    def umm_ABIEProperty30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ABIEProperty__umm_ABIEProperty30", None)
        self.__umm_ABIEProperty30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_ABIEProperty32"):
                    opp_val = getattr(item, "umm_ABIEProperty32", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_ABIEProperty32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_ABIEProperty32"):
                    opp_val = getattr(item, "umm_ABIEProperty32", None)
                    
                    setattr(item, "umm_ABIEProperty32", self)
                    

    @property
    def umm_ABIEProperty(self):
        return self.__umm_ABIEProperty

    @umm_ABIEProperty.setter
    def umm_ABIEProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ABIEProperty__umm_ABIEProperty", None)
        self.__umm_ABIEProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_ABIE26"):
                opp_val = getattr(old_value, "umm_ABIE26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_ABIE26"):
                opp_val = getattr(value, "umm_ABIE26", None)
                if opp_val is None:
                    setattr(value, "umm_ABIE26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umm_ABIEProperty32(self):
        return self.__umm_ABIEProperty32

    @umm_ABIEProperty32.setter
    def umm_ABIEProperty32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ABIEProperty__umm_ABIEProperty32", None)
        self.__umm_ABIEProperty32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_ABIEProperty30"):
                opp_val = getattr(old_value, "umm_ABIEProperty30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_ABIEProperty30"):
                opp_val = getattr(value, "umm_ABIEProperty30", None)
                if opp_val is None:
                    setattr(value, "umm_ABIEProperty30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umm_MAProperty(OclRef):

    pass
class ContextRef:

    pass
class umm_BDT(ContextRef):

    def __init__(self, businessTerm: str, definition: str, dictionary: str, uniqueIdentifier: str, versionIdentifier: str, umm_BDT: "umm_BBIE" = None, umm_BDT40: set["umm_BDTProperty"] = None, umm_BDT38: "umm_BDTLibrary" = None):
        self.businessTerm = businessTerm
        self.definition = definition
        self.dictionary = dictionary
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.umm_BDT = umm_BDT
        self.umm_BDT40 = umm_BDT40 if umm_BDT40 is not None else set()
        self.umm_BDT38 = umm_BDT38
        
    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def dictionary(self) -> str:
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary: str):
        self.__dictionary = dictionary

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def umm_BDT40(self):
        return self.__umm_BDT40

    @umm_BDT40.setter
    def umm_BDT40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BDT__umm_BDT40", None)
        self.__umm_BDT40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_BDTProperty"):
                    opp_val = getattr(item, "umm_BDTProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_BDTProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_BDTProperty"):
                    opp_val = getattr(item, "umm_BDTProperty", None)
                    
                    setattr(item, "umm_BDTProperty", self)
                    

    @property
    def umm_BDT(self):
        return self.__umm_BDT

    @umm_BDT.setter
    def umm_BDT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BDT__umm_BDT", None)
        self.__umm_BDT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_BBIE"):
                opp_val = getattr(old_value, "umm_BBIE", None)
                if opp_val == self:
                    setattr(old_value, "umm_BBIE", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_BBIE"):
                opp_val = getattr(value, "umm_BBIE", None)
                setattr(value, "umm_BBIE", self)

    @property
    def umm_BDT38(self):
        return self.__umm_BDT38

    @umm_BDT38.setter
    def umm_BDT38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BDT__umm_BDT38", None)
        self.__umm_BDT38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_BDTLibrary37"):
                opp_val = getattr(old_value, "umm_BDTLibrary37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_BDTLibrary37"):
                opp_val = getattr(value, "umm_BDTLibrary37", None)
                if opp_val is None:
                    setattr(value, "umm_BDTLibrary37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umm_ABIE(ContextRef):

    def __init__(self, businessTerm: str, definition: str, dictionary: str, uniqueIdentifier: str, versionIdentifier: str, umm_ABIE: "umm_MAProperty" = None, umm_ABIE24: "umm_BIELibrary" = None, umm_ABIE26: set["umm_ABIEProperty"] = None, umm_ABIE28: set["umm_Constraint"] = None, umm_ABIE34: "umm_ASBIE" = None):
        self.businessTerm = businessTerm
        self.definition = definition
        self.dictionary = dictionary
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.umm_ABIE = umm_ABIE
        self.umm_ABIE24 = umm_ABIE24
        self.umm_ABIE26 = umm_ABIE26 if umm_ABIE26 is not None else set()
        self.umm_ABIE28 = umm_ABIE28 if umm_ABIE28 is not None else set()
        self.umm_ABIE34 = umm_ABIE34
        
    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def dictionary(self) -> str:
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, dictionary: str):
        self.__dictionary = dictionary

    @property
    def umm_ABIE(self):
        return self.__umm_ABIE

    @umm_ABIE.setter
    def umm_ABIE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ABIE__umm_ABIE", None)
        self.__umm_ABIE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_MAProperty12"):
                opp_val = getattr(old_value, "umm_MAProperty12", None)
                if opp_val == self:
                    setattr(old_value, "umm_MAProperty12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_MAProperty12"):
                opp_val = getattr(value, "umm_MAProperty12", None)
                setattr(value, "umm_MAProperty12", self)

    @property
    def umm_ABIE34(self):
        return self.__umm_ABIE34

    @umm_ABIE34.setter
    def umm_ABIE34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ABIE__umm_ABIE34", None)
        self.__umm_ABIE34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_ASBIE"):
                opp_val = getattr(old_value, "umm_ASBIE", None)
                if opp_val == self:
                    setattr(old_value, "umm_ASBIE", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_ASBIE"):
                opp_val = getattr(value, "umm_ASBIE", None)
                setattr(value, "umm_ASBIE", self)

    @property
    def umm_ABIE24(self):
        return self.__umm_ABIE24

    @umm_ABIE24.setter
    def umm_ABIE24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ABIE__umm_ABIE24", None)
        self.__umm_ABIE24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_BIELibrary23"):
                opp_val = getattr(old_value, "umm_BIELibrary23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_BIELibrary23"):
                opp_val = getattr(value, "umm_BIELibrary23", None)
                if opp_val is None:
                    setattr(value, "umm_BIELibrary23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umm_ABIE26(self):
        return self.__umm_ABIE26

    @umm_ABIE26.setter
    def umm_ABIE26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ABIE__umm_ABIE26", None)
        self.__umm_ABIE26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_ABIEProperty"):
                    opp_val = getattr(item, "umm_ABIEProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_ABIEProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_ABIEProperty"):
                    opp_val = getattr(item, "umm_ABIEProperty", None)
                    
                    setattr(item, "umm_ABIEProperty", self)
                    

    @property
    def umm_ABIE28(self):
        return self.__umm_ABIE28

    @umm_ABIE28.setter
    def umm_ABIE28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ABIE__umm_ABIE28", None)
        self.__umm_ABIE28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_Constraint29"):
                    opp_val = getattr(item, "umm_Constraint29", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_Constraint29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_Constraint29"):
                    opp_val = getattr(item, "umm_Constraint29", None)
                    
                    setattr(item, "umm_Constraint29", self)
                    

class umm_MA(ContextRef):

    pass
class umm_InfEnvelope:

    def __init__(self, name: str, umm_InfEnvelope: "umm_DocLibrary" = None, umm_InfEnvelope6: set["umm_MA"] = None):
        self.name = name
        self.umm_InfEnvelope = umm_InfEnvelope
        self.umm_InfEnvelope6 = umm_InfEnvelope6 if umm_InfEnvelope6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umm_InfEnvelope6(self):
        return self.__umm_InfEnvelope6

    @umm_InfEnvelope6.setter
    def umm_InfEnvelope6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_InfEnvelope__umm_InfEnvelope6", None)
        self.__umm_InfEnvelope6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_MA"):
                    opp_val = getattr(item, "umm_MA", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_MA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_MA"):
                    opp_val = getattr(item, "umm_MA", None)
                    
                    setattr(item, "umm_MA", self)
                    

    @property
    def umm_InfEnvelope(self):
        return self.__umm_InfEnvelope

    @umm_InfEnvelope.setter
    def umm_InfEnvelope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_InfEnvelope__umm_InfEnvelope", None)
        self.__umm_InfEnvelope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_DocLibrary4"):
                opp_val = getattr(old_value, "umm_DocLibrary4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_DocLibrary4"):
                opp_val = getattr(value, "umm_DocLibrary4", None)
                if opp_val is None:
                    setattr(value, "umm_DocLibrary4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umm_Constraint:

    pass
class Library:

    pass
class umm_CCLibrary(Library):

    def __init__(self, uniqueIdentifier: str, versionIdentifier: str, baseURN: str, businessTerm: str, copyright: str, owner: str, reference: str, namespacePrefix: str, umm_CCLibrary: set["umm_ACC"] = None):
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.baseURN = baseURN
        self.businessTerm = businessTerm
        self.copyright = copyright
        self.owner = owner
        self.reference = reference
        self.namespacePrefix = namespacePrefix
        self.umm_CCLibrary = umm_CCLibrary if umm_CCLibrary is not None else set()
        
    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def baseURN(self) -> str:
        return self.__baseURN

    @baseURN.setter
    def baseURN(self, baseURN: str):
        self.__baseURN = baseURN

    @property
    def namespacePrefix(self) -> str:
        return self.__namespacePrefix

    @namespacePrefix.setter
    def namespacePrefix(self, namespacePrefix: str):
        self.__namespacePrefix = namespacePrefix

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def umm_CCLibrary(self):
        return self.__umm_CCLibrary

    @umm_CCLibrary.setter
    def umm_CCLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_CCLibrary__umm_CCLibrary", None)
        self.__umm_CCLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_ACC"):
                    opp_val = getattr(item, "umm_ACC", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_ACC", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_ACC"):
                    opp_val = getattr(item, "umm_ACC", None)
                    
                    setattr(item, "umm_ACC", self)
                    

class umm_CDTLibrary(Library):

    def __init__(self, copyright: str, owner: str, reference: str, uniqueIdentifier: str, versionIdentifier: str, businessTerm: str, baseURN: str, namespacePrefix: str, umm_CDTLibrary: set["umm_CDT"] = None):
        self.copyright = copyright
        self.owner = owner
        self.reference = reference
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.businessTerm = businessTerm
        self.baseURN = baseURN
        self.namespacePrefix = namespacePrefix
        self.umm_CDTLibrary = umm_CDTLibrary if umm_CDTLibrary is not None else set()
        
    @property
    def namespacePrefix(self) -> str:
        return self.__namespacePrefix

    @namespacePrefix.setter
    def namespacePrefix(self, namespacePrefix: str):
        self.__namespacePrefix = namespacePrefix

    @property
    def baseURN(self) -> str:
        return self.__baseURN

    @baseURN.setter
    def baseURN(self, baseURN: str):
        self.__baseURN = baseURN

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def umm_CDTLibrary(self):
        return self.__umm_CDTLibrary

    @umm_CDTLibrary.setter
    def umm_CDTLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_CDTLibrary__umm_CDTLibrary", None)
        self.__umm_CDTLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_CDT62"):
                    opp_val = getattr(item, "umm_CDT62", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_CDT62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_CDT62"):
                    opp_val = getattr(item, "umm_CDT62", None)
                    
                    setattr(item, "umm_CDT62", self)
                    

class umm_BDTLibrary(Library):

    def __init__(self, businessTerm: str, copyright: str, owner: str, reference: str, uniqueIdentifier: str, versionIdentifier: str, baseURN: str, namespacePrefix: str, umm_BDTLibrary: "umm_DocLibrary" = None, umm_BDTLibrary21: "umm_BIELibrary" = None, umm_BDTLibrary37: set["umm_BDT"] = None):
        self.businessTerm = businessTerm
        self.copyright = copyright
        self.owner = owner
        self.reference = reference
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.baseURN = baseURN
        self.namespacePrefix = namespacePrefix
        self.umm_BDTLibrary = umm_BDTLibrary
        self.umm_BDTLibrary21 = umm_BDTLibrary21
        self.umm_BDTLibrary37 = umm_BDTLibrary37 if umm_BDTLibrary37 is not None else set()
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def baseURN(self) -> str:
        return self.__baseURN

    @baseURN.setter
    def baseURN(self, baseURN: str):
        self.__baseURN = baseURN

    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def namespacePrefix(self) -> str:
        return self.__namespacePrefix

    @namespacePrefix.setter
    def namespacePrefix(self, namespacePrefix: str):
        self.__namespacePrefix = namespacePrefix

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def umm_BDTLibrary(self):
        return self.__umm_BDTLibrary

    @umm_BDTLibrary.setter
    def umm_BDTLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BDTLibrary__umm_BDTLibrary", None)
        self.__umm_BDTLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_DocLibrary2"):
                opp_val = getattr(old_value, "umm_DocLibrary2", None)
                if opp_val == self:
                    setattr(old_value, "umm_DocLibrary2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_DocLibrary2"):
                opp_val = getattr(value, "umm_DocLibrary2", None)
                setattr(value, "umm_DocLibrary2", self)

    @property
    def umm_BDTLibrary37(self):
        return self.__umm_BDTLibrary37

    @umm_BDTLibrary37.setter
    def umm_BDTLibrary37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BDTLibrary__umm_BDTLibrary37", None)
        self.__umm_BDTLibrary37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_BDT38"):
                    opp_val = getattr(item, "umm_BDT38", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_BDT38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_BDT38"):
                    opp_val = getattr(item, "umm_BDT38", None)
                    
                    setattr(item, "umm_BDT38", self)
                    

    @property
    def umm_BDTLibrary21(self):
        return self.__umm_BDTLibrary21

    @umm_BDTLibrary21.setter
    def umm_BDTLibrary21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BDTLibrary__umm_BDTLibrary21", None)
        self.__umm_BDTLibrary21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_BIELibrary20"):
                opp_val = getattr(old_value, "umm_BIELibrary20", None)
                if opp_val == self:
                    setattr(old_value, "umm_BIELibrary20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_BIELibrary20"):
                opp_val = getattr(value, "umm_BIELibrary20", None)
                setattr(value, "umm_BIELibrary20", self)

class umm_PrimitiveLibrary(Library):

    pass
class umm_BIELibrary(Library):

    def __init__(self, businessTerm: str, copyright: str, owner: str, reference: str, uniqueIdentifier: str, versionIdentifier: str, baseURN: str, namespacePrefix: str, umm_BIELibrary: "umm_DocLibrary" = None, umm_BIELibrary20: "umm_BDTLibrary" = None, umm_BIELibrary23: set["umm_ABIE"] = None):
        self.businessTerm = businessTerm
        self.copyright = copyright
        self.owner = owner
        self.reference = reference
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.baseURN = baseURN
        self.namespacePrefix = namespacePrefix
        self.umm_BIELibrary = umm_BIELibrary
        self.umm_BIELibrary20 = umm_BIELibrary20
        self.umm_BIELibrary23 = umm_BIELibrary23 if umm_BIELibrary23 is not None else set()
        
    @property
    def namespacePrefix(self) -> str:
        return self.__namespacePrefix

    @namespacePrefix.setter
    def namespacePrefix(self, namespacePrefix: str):
        self.__namespacePrefix = namespacePrefix

    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def baseURN(self) -> str:
        return self.__baseURN

    @baseURN.setter
    def baseURN(self, baseURN: str):
        self.__baseURN = baseURN

    @property
    def umm_BIELibrary20(self):
        return self.__umm_BIELibrary20

    @umm_BIELibrary20.setter
    def umm_BIELibrary20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BIELibrary__umm_BIELibrary20", None)
        self.__umm_BIELibrary20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_BDTLibrary21"):
                opp_val = getattr(old_value, "umm_BDTLibrary21", None)
                if opp_val == self:
                    setattr(old_value, "umm_BDTLibrary21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_BDTLibrary21"):
                opp_val = getattr(value, "umm_BDTLibrary21", None)
                setattr(value, "umm_BDTLibrary21", self)

    @property
    def umm_BIELibrary23(self):
        return self.__umm_BIELibrary23

    @umm_BIELibrary23.setter
    def umm_BIELibrary23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BIELibrary__umm_BIELibrary23", None)
        self.__umm_BIELibrary23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_ABIE24"):
                    opp_val = getattr(item, "umm_ABIE24", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_ABIE24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_ABIE24"):
                    opp_val = getattr(item, "umm_ABIE24", None)
                    
                    setattr(item, "umm_ABIE24", self)
                    

    @property
    def umm_BIELibrary(self):
        return self.__umm_BIELibrary

    @umm_BIELibrary.setter
    def umm_BIELibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_BIELibrary__umm_BIELibrary", None)
        self.__umm_BIELibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_DocLibrary"):
                opp_val = getattr(old_value, "umm_DocLibrary", None)
                if opp_val == self:
                    setattr(old_value, "umm_DocLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_DocLibrary"):
                opp_val = getattr(value, "umm_DocLibrary", None)
                setattr(value, "umm_DocLibrary", self)

class umm_ENUMLibrary(Library):

    def __init__(self, businessTerm: str, copyright: str, owner: str, reference: str, uniqueIdentifier: str, versionIdentifier: str, baseURN: str, namespacePrefix: str, umm_ENUMLibrary: set["umm_ENUM"] = None):
        self.businessTerm = businessTerm
        self.copyright = copyright
        self.owner = owner
        self.reference = reference
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.baseURN = baseURN
        self.namespacePrefix = namespacePrefix
        self.umm_ENUMLibrary = umm_ENUMLibrary if umm_ENUMLibrary is not None else set()
        
    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def namespacePrefix(self) -> str:
        return self.__namespacePrefix

    @namespacePrefix.setter
    def namespacePrefix(self, namespacePrefix: str):
        self.__namespacePrefix = namespacePrefix

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def baseURN(self) -> str:
        return self.__baseURN

    @baseURN.setter
    def baseURN(self, baseURN: str):
        self.__baseURN = baseURN

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def umm_ENUMLibrary(self):
        return self.__umm_ENUMLibrary

    @umm_ENUMLibrary.setter
    def umm_ENUMLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_ENUMLibrary__umm_ENUMLibrary", None)
        self.__umm_ENUMLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_ENUM"):
                    opp_val = getattr(item, "umm_ENUM", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_ENUM", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_ENUM"):
                    opp_val = getattr(item, "umm_ENUM", None)
                    
                    setattr(item, "umm_ENUM", self)
                    

class umm_DocLibrary(Library):

    def __init__(self, reference: str, uniqueIdentifier: str, versionIdentifier: str, businessTerm: str, copyright: str, owner: str, baseURN: str, namespacePrefix: str, umm_DocLibrary: "umm_BIELibrary" = None, umm_DocLibrary2: "umm_BDTLibrary" = None, umm_DocLibrary4: set["umm_InfEnvelope"] = None):
        self.reference = reference
        self.uniqueIdentifier = uniqueIdentifier
        self.versionIdentifier = versionIdentifier
        self.businessTerm = businessTerm
        self.copyright = copyright
        self.owner = owner
        self.baseURN = baseURN
        self.namespacePrefix = namespacePrefix
        self.umm_DocLibrary = umm_DocLibrary
        self.umm_DocLibrary2 = umm_DocLibrary2
        self.umm_DocLibrary4 = umm_DocLibrary4 if umm_DocLibrary4 is not None else set()
        
    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def baseURN(self) -> str:
        return self.__baseURN

    @baseURN.setter
    def baseURN(self, baseURN: str):
        self.__baseURN = baseURN

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def versionIdentifier(self) -> str:
        return self.__versionIdentifier

    @versionIdentifier.setter
    def versionIdentifier(self, versionIdentifier: str):
        self.__versionIdentifier = versionIdentifier

    @property
    def businessTerm(self) -> str:
        return self.__businessTerm

    @businessTerm.setter
    def businessTerm(self, businessTerm: str):
        self.__businessTerm = businessTerm

    @property
    def uniqueIdentifier(self) -> str:
        return self.__uniqueIdentifier

    @uniqueIdentifier.setter
    def uniqueIdentifier(self, uniqueIdentifier: str):
        self.__uniqueIdentifier = uniqueIdentifier

    @property
    def namespacePrefix(self) -> str:
        return self.__namespacePrefix

    @namespacePrefix.setter
    def namespacePrefix(self, namespacePrefix: str):
        self.__namespacePrefix = namespacePrefix

    @property
    def umm_DocLibrary(self):
        return self.__umm_DocLibrary

    @umm_DocLibrary.setter
    def umm_DocLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_DocLibrary__umm_DocLibrary", None)
        self.__umm_DocLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_BIELibrary"):
                opp_val = getattr(old_value, "umm_BIELibrary", None)
                if opp_val == self:
                    setattr(old_value, "umm_BIELibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_BIELibrary"):
                opp_val = getattr(value, "umm_BIELibrary", None)
                setattr(value, "umm_BIELibrary", self)

    @property
    def umm_DocLibrary2(self):
        return self.__umm_DocLibrary2

    @umm_DocLibrary2.setter
    def umm_DocLibrary2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_DocLibrary__umm_DocLibrary2", None)
        self.__umm_DocLibrary2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umm_BDTLibrary"):
                opp_val = getattr(old_value, "umm_BDTLibrary", None)
                if opp_val == self:
                    setattr(old_value, "umm_BDTLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umm_BDTLibrary"):
                opp_val = getattr(value, "umm_BDTLibrary", None)
                setattr(value, "umm_BDTLibrary", self)

    @property
    def umm_DocLibrary4(self):
        return self.__umm_DocLibrary4

    @umm_DocLibrary4.setter
    def umm_DocLibrary4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umm_DocLibrary__umm_DocLibrary4", None)
        self.__umm_DocLibrary4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umm_InfEnvelope"):
                    opp_val = getattr(item, "umm_InfEnvelope", None)
                    
                    if opp_val == self:
                        setattr(item, "umm_InfEnvelope", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umm_InfEnvelope"):
                    opp_val = getattr(item, "umm_InfEnvelope", None)
                    
                    setattr(item, "umm_InfEnvelope", self)
                    

class umm_Library:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
