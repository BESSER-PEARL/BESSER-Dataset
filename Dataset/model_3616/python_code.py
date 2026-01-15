from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Guidance(Enum):
    FIXED = "FIXED"
    CLOSED = "CLOSED"
    EXTEND = "EXTEND"
    RESTRICT = "RESTRICT"
    OPEN = "OPEN"
class ValueSetType(Enum):
    Extensional = "Extensional"
    Intensional = "Intensional"
class Extensibility(Enum):
    NEA = "NEA"
    CEA = "CEA"
class BindingKind(Enum):
    Static = "Static"
    Dynamic = "Dynamic"
class ValueSetBinding(Enum):
    Direct = "Direct"
    Indirect = "Indirect"
class StatusKind(Enum):
    Active = "Active"
    Inactive = "Inactive"


############################################
# Definition of Classes
############################################

class profile_NullValueSetConstraint:

    def __init__(self, version: str, binding: str, identifier: str, name: str, profile_NullValueSetConstraint58: "profile_Property" = None, profile_NullValueSetConstraint: "profile_ValueSetVersion" = None):
        self.version = version
        self.binding = binding
        self.identifier = identifier
        self.name = name
        self.profile_NullValueSetConstraint58 = profile_NullValueSetConstraint58
        self.profile_NullValueSetConstraint = profile_NullValueSetConstraint
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def binding(self) -> str:
        return self.__binding

    @binding.setter
    def binding(self, binding: str):
        self.__binding = binding

    @property
    def profile_NullValueSetConstraint(self):
        return self.__profile_NullValueSetConstraint

    @profile_NullValueSetConstraint.setter
    def profile_NullValueSetConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_NullValueSetConstraint__profile_NullValueSetConstraint", None)
        self.__profile_NullValueSetConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ValueSetVersion56"):
                opp_val = getattr(old_value, "profile_ValueSetVersion56", None)
                if opp_val == self:
                    setattr(old_value, "profile_ValueSetVersion56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ValueSetVersion56"):
                opp_val = getattr(value, "profile_ValueSetVersion56", None)
                setattr(value, "profile_ValueSetVersion56", self)

    @property
    def profile_NullValueSetConstraint58(self):
        return self.__profile_NullValueSetConstraint58

    @profile_NullValueSetConstraint58.setter
    def profile_NullValueSetConstraint58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_NullValueSetConstraint__profile_NullValueSetConstraint58", None)
        self.__profile_NullValueSetConstraint58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Property59"):
                opp_val = getattr(old_value, "profile_Property59", None)
                if opp_val == self:
                    setattr(old_value, "profile_Property59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Property59"):
                opp_val = getattr(value, "profile_Property59", None)
                setattr(value, "profile_Property59", self)

class profile_Classifier:

    pass
class profile_CodedType:

    pass
class profile_Context:

    pass
class profile_UsageContext:

    def __init__(self, identifier: str, status: str, statusDate: str, profile_UsageContext49: "profile_Class" = None, profile_UsageContext: "profile_ValueSetContextBinding" = None):
        self.identifier = identifier
        self.status = status
        self.statusDate = statusDate
        self.profile_UsageContext49 = profile_UsageContext49
        self.profile_UsageContext = profile_UsageContext
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def statusDate(self) -> str:
        return self.__statusDate

    @statusDate.setter
    def statusDate(self, statusDate: str):
        self.__statusDate = statusDate

    @property
    def profile_UsageContext(self):
        return self.__profile_UsageContext

    @profile_UsageContext.setter
    def profile_UsageContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_UsageContext__profile_UsageContext", None)
        self.__profile_UsageContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ValueSetContextBinding44"):
                opp_val = getattr(old_value, "profile_ValueSetContextBinding44", None)
                if opp_val == self:
                    setattr(old_value, "profile_ValueSetContextBinding44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ValueSetContextBinding44"):
                opp_val = getattr(value, "profile_ValueSetContextBinding44", None)
                setattr(value, "profile_ValueSetContextBinding44", self)

    @property
    def profile_UsageContext49(self):
        return self.__profile_UsageContext49

    @profile_UsageContext49.setter
    def profile_UsageContext49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_UsageContext__profile_UsageContext49", None)
        self.__profile_UsageContext49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Class50"):
                opp_val = getattr(old_value, "profile_Class50", None)
                if opp_val == self:
                    setattr(old_value, "profile_Class50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Class50"):
                opp_val = getattr(value, "profile_Class50", None)
                setattr(value, "profile_Class50", self)

class profile_ValueSetContextBinding:

    def __init__(self, effectiveDate: str, profile_ValueSetContextBinding46: "profile_Class" = None, profile_ValueSetContextBinding: "profile_ConceptDomain" = None, profile_ValueSetContextBinding41: "profile_ValueSetVersion" = None, profile_ValueSetContextBinding44: "profile_UsageContext" = None):
        self.effectiveDate = effectiveDate
        self.profile_ValueSetContextBinding46 = profile_ValueSetContextBinding46
        self.profile_ValueSetContextBinding = profile_ValueSetContextBinding
        self.profile_ValueSetContextBinding41 = profile_ValueSetContextBinding41
        self.profile_ValueSetContextBinding44 = profile_ValueSetContextBinding44
        
    @property
    def effectiveDate(self) -> str:
        return self.__effectiveDate

    @effectiveDate.setter
    def effectiveDate(self, effectiveDate: str):
        self.__effectiveDate = effectiveDate

    @property
    def profile_ValueSetContextBinding46(self):
        return self.__profile_ValueSetContextBinding46

    @profile_ValueSetContextBinding46.setter
    def profile_ValueSetContextBinding46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetContextBinding__profile_ValueSetContextBinding46", None)
        self.__profile_ValueSetContextBinding46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Class47"):
                opp_val = getattr(old_value, "profile_Class47", None)
                if opp_val == self:
                    setattr(old_value, "profile_Class47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Class47"):
                opp_val = getattr(value, "profile_Class47", None)
                setattr(value, "profile_Class47", self)

    @property
    def profile_ValueSetContextBinding44(self):
        return self.__profile_ValueSetContextBinding44

    @profile_ValueSetContextBinding44.setter
    def profile_ValueSetContextBinding44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetContextBinding__profile_ValueSetContextBinding44", None)
        self.__profile_ValueSetContextBinding44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_UsageContext"):
                opp_val = getattr(old_value, "profile_UsageContext", None)
                if opp_val == self:
                    setattr(old_value, "profile_UsageContext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_UsageContext"):
                opp_val = getattr(value, "profile_UsageContext", None)
                setattr(value, "profile_UsageContext", self)

    @property
    def profile_ValueSetContextBinding41(self):
        return self.__profile_ValueSetContextBinding41

    @profile_ValueSetContextBinding41.setter
    def profile_ValueSetContextBinding41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetContextBinding__profile_ValueSetContextBinding41", None)
        self.__profile_ValueSetContextBinding41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ValueSetVersion42"):
                opp_val = getattr(old_value, "profile_ValueSetVersion42", None)
                if opp_val == self:
                    setattr(old_value, "profile_ValueSetVersion42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ValueSetVersion42"):
                opp_val = getattr(value, "profile_ValueSetVersion42", None)
                setattr(value, "profile_ValueSetVersion42", self)

    @property
    def profile_ValueSetContextBinding(self):
        return self.__profile_ValueSetContextBinding

    @profile_ValueSetContextBinding.setter
    def profile_ValueSetContextBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetContextBinding__profile_ValueSetContextBinding", None)
        self.__profile_ValueSetContextBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ConceptDomain39"):
                opp_val = getattr(old_value, "profile_ConceptDomain39", None)
                if opp_val == self:
                    setattr(old_value, "profile_ConceptDomain39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ConceptDomain39"):
                opp_val = getattr(value, "profile_ConceptDomain39", None)
                setattr(value, "profile_ConceptDomain39", self)

class profile_EnumerationLiteral:

    pass
class profile_ContextToValueSet:

    def __init__(self, key: str, value: str, profile_ContextToValueSet: "profile_ValueSetConstraints" = None):
        self.key = key
        self.value = value
        self.profile_ContextToValueSet = profile_ContextToValueSet
        
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

    @property
    def profile_ContextToValueSet(self):
        return self.__profile_ContextToValueSet

    @profile_ContextToValueSet.setter
    def profile_ContextToValueSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ContextToValueSet__profile_ContextToValueSet", None)
        self.__profile_ContextToValueSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ValueSetConstraints54"):
                opp_val = getattr(old_value, "profile_ValueSetConstraints54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ValueSetConstraints54"):
                opp_val = getattr(value, "profile_ValueSetConstraints54", None)
                if opp_val is None:
                    setattr(value, "profile_ValueSetConstraints54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class profile_ValueSetConstraints:

    pass
class profile_ValueSetCode:

    def __init__(self, conceptName: str, usageNote: str, profile_ValueSetCode: "profile_CodeSystemVersion" = None, profile_ValueSetCode37: "profile_EnumerationLiteral" = None):
        self.conceptName = conceptName
        self.usageNote = usageNote
        self.profile_ValueSetCode = profile_ValueSetCode
        self.profile_ValueSetCode37 = profile_ValueSetCode37
        
    @property
    def usageNote(self) -> str:
        return self.__usageNote

    @usageNote.setter
    def usageNote(self, usageNote: str):
        self.__usageNote = usageNote

    @property
    def conceptName(self) -> str:
        return self.__conceptName

    @conceptName.setter
    def conceptName(self, conceptName: str):
        self.__conceptName = conceptName

    @property
    def profile_ValueSetCode37(self):
        return self.__profile_ValueSetCode37

    @profile_ValueSetCode37.setter
    def profile_ValueSetCode37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetCode__profile_ValueSetCode37", None)
        self.__profile_ValueSetCode37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_EnumerationLiteral"):
                opp_val = getattr(old_value, "profile_EnumerationLiteral", None)
                if opp_val == self:
                    setattr(old_value, "profile_EnumerationLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_EnumerationLiteral"):
                opp_val = getattr(value, "profile_EnumerationLiteral", None)
                setattr(value, "profile_EnumerationLiteral", self)

    @property
    def profile_ValueSetCode(self):
        return self.__profile_ValueSetCode

    @profile_ValueSetCode.setter
    def profile_ValueSetCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetCode__profile_ValueSetCode", None)
        self.__profile_ValueSetCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CodeSystemVersion35"):
                opp_val = getattr(old_value, "profile_CodeSystemVersion35", None)
                if opp_val == self:
                    setattr(old_value, "profile_CodeSystemVersion35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CodeSystemVersion35"):
                opp_val = getattr(value, "profile_CodeSystemVersion35", None)
                setattr(value, "profile_CodeSystemVersion35", self)

class profile_ValueSetVersion:

    def __init__(self, identifier: str, version: str, fullName: str, source: str, url: str, definition: str, effectiveDate: str, expirationDate: str, releaseDate: str, revisionDate: str, status: str, statusDate: str, type: str, binding: str, profile_ValueSetVersion: "profile_ValueSetConstraint" = None, profile_ValueSetVersion29: "profile_CodeSystemVersion" = None, profile_ValueSetVersion32: "profile_Enumeration" = None, profile_ValueSetVersion42: "profile_ValueSetContextBinding" = None, profile_ValueSetVersion56: "profile_NullValueSetConstraint" = None):
        self.identifier = identifier
        self.version = version
        self.fullName = fullName
        self.source = source
        self.url = url
        self.definition = definition
        self.effectiveDate = effectiveDate
        self.expirationDate = expirationDate
        self.releaseDate = releaseDate
        self.revisionDate = revisionDate
        self.status = status
        self.statusDate = statusDate
        self.type = type
        self.binding = binding
        self.profile_ValueSetVersion = profile_ValueSetVersion
        self.profile_ValueSetVersion29 = profile_ValueSetVersion29
        self.profile_ValueSetVersion32 = profile_ValueSetVersion32
        self.profile_ValueSetVersion42 = profile_ValueSetVersion42
        self.profile_ValueSetVersion56 = profile_ValueSetVersion56
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def effectiveDate(self) -> str:
        return self.__effectiveDate

    @effectiveDate.setter
    def effectiveDate(self, effectiveDate: str):
        self.__effectiveDate = effectiveDate

    @property
    def binding(self) -> str:
        return self.__binding

    @binding.setter
    def binding(self, binding: str):
        self.__binding = binding

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def releaseDate(self) -> str:
        return self.__releaseDate

    @releaseDate.setter
    def releaseDate(self, releaseDate: str):
        self.__releaseDate = releaseDate

    @property
    def statusDate(self) -> str:
        return self.__statusDate

    @statusDate.setter
    def statusDate(self, statusDate: str):
        self.__statusDate = statusDate

    @property
    def expirationDate(self) -> str:
        return self.__expirationDate

    @expirationDate.setter
    def expirationDate(self, expirationDate: str):
        self.__expirationDate = expirationDate

    @property
    def revisionDate(self) -> str:
        return self.__revisionDate

    @revisionDate.setter
    def revisionDate(self, revisionDate: str):
        self.__revisionDate = revisionDate

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def definition(self) -> str:
        return self.__definition

    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def profile_ValueSetVersion29(self):
        return self.__profile_ValueSetVersion29

    @profile_ValueSetVersion29.setter
    def profile_ValueSetVersion29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetVersion__profile_ValueSetVersion29", None)
        self.__profile_ValueSetVersion29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CodeSystemVersion30"):
                opp_val = getattr(old_value, "profile_CodeSystemVersion30", None)
                if opp_val == self:
                    setattr(old_value, "profile_CodeSystemVersion30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CodeSystemVersion30"):
                opp_val = getattr(value, "profile_CodeSystemVersion30", None)
                setattr(value, "profile_CodeSystemVersion30", self)

    @property
    def profile_ValueSetVersion56(self):
        return self.__profile_ValueSetVersion56

    @profile_ValueSetVersion56.setter
    def profile_ValueSetVersion56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetVersion__profile_ValueSetVersion56", None)
        self.__profile_ValueSetVersion56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_NullValueSetConstraint"):
                opp_val = getattr(old_value, "profile_NullValueSetConstraint", None)
                if opp_val == self:
                    setattr(old_value, "profile_NullValueSetConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_NullValueSetConstraint"):
                opp_val = getattr(value, "profile_NullValueSetConstraint", None)
                setattr(value, "profile_NullValueSetConstraint", self)

    @property
    def profile_ValueSetVersion32(self):
        return self.__profile_ValueSetVersion32

    @profile_ValueSetVersion32.setter
    def profile_ValueSetVersion32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetVersion__profile_ValueSetVersion32", None)
        self.__profile_ValueSetVersion32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Enumeration33"):
                opp_val = getattr(old_value, "profile_Enumeration33", None)
                if opp_val == self:
                    setattr(old_value, "profile_Enumeration33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Enumeration33"):
                opp_val = getattr(value, "profile_Enumeration33", None)
                setattr(value, "profile_Enumeration33", self)

    @property
    def profile_ValueSetVersion42(self):
        return self.__profile_ValueSetVersion42

    @profile_ValueSetVersion42.setter
    def profile_ValueSetVersion42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetVersion__profile_ValueSetVersion42", None)
        self.__profile_ValueSetVersion42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ValueSetContextBinding41"):
                opp_val = getattr(old_value, "profile_ValueSetContextBinding41", None)
                if opp_val == self:
                    setattr(old_value, "profile_ValueSetContextBinding41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ValueSetContextBinding41"):
                opp_val = getattr(value, "profile_ValueSetContextBinding41", None)
                setattr(value, "profile_ValueSetContextBinding41", self)

    @property
    def profile_ValueSetVersion(self):
        return self.__profile_ValueSetVersion

    @profile_ValueSetVersion.setter
    def profile_ValueSetVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetVersion__profile_ValueSetVersion", None)
        self.__profile_ValueSetVersion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ValueSetConstraint"):
                opp_val = getattr(old_value, "profile_ValueSetConstraint", None)
                if opp_val == self:
                    setattr(old_value, "profile_ValueSetConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ValueSetConstraint"):
                opp_val = getattr(value, "profile_ValueSetConstraint", None)
                setattr(value, "profile_ValueSetConstraint", self)

    def getEnumerationQualifiedName(self) -> str:
        # TODO: Implement getEnumerationQualifiedName method
        pass

    def getEnumerationName(self) -> str:
        # TODO: Implement getEnumerationName method
        pass

    def setEnumerationName(self, name: str):
        # TODO: Implement setEnumerationName method
        pass

class profile_ValueSetConstraint:

    def __init__(self, identifier: str, name: str, version: str, binding: str, extensibility: str, guidance: str, uri: str, profile_ValueSetConstraint: "profile_ValueSetVersion" = None, profile_ValueSetConstraint26: "profile_Property" = None):
        self.identifier = identifier
        self.name = name
        self.version = version
        self.binding = binding
        self.extensibility = extensibility
        self.guidance = guidance
        self.uri = uri
        self.profile_ValueSetConstraint = profile_ValueSetConstraint
        self.profile_ValueSetConstraint26 = profile_ValueSetConstraint26
        
    @property
    def extensibility(self) -> str:
        return self.__extensibility

    @extensibility.setter
    def extensibility(self, extensibility: str):
        self.__extensibility = extensibility

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def guidance(self) -> str:
        return self.__guidance

    @guidance.setter
    def guidance(self, guidance: str):
        self.__guidance = guidance

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def binding(self) -> str:
        return self.__binding

    @binding.setter
    def binding(self, binding: str):
        self.__binding = binding

    @property
    def profile_ValueSetConstraint26(self):
        return self.__profile_ValueSetConstraint26

    @profile_ValueSetConstraint26.setter
    def profile_ValueSetConstraint26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetConstraint__profile_ValueSetConstraint26", None)
        self.__profile_ValueSetConstraint26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Property27"):
                opp_val = getattr(old_value, "profile_Property27", None)
                if opp_val == self:
                    setattr(old_value, "profile_Property27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Property27"):
                opp_val = getattr(value, "profile_Property27", None)
                setattr(value, "profile_Property27", self)

    @property
    def profile_ValueSetConstraint(self):
        return self.__profile_ValueSetConstraint

    @profile_ValueSetConstraint.setter
    def profile_ValueSetConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ValueSetConstraint__profile_ValueSetConstraint", None)
        self.__profile_ValueSetConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ValueSetVersion"):
                opp_val = getattr(old_value, "profile_ValueSetVersion", None)
                if opp_val == self:
                    setattr(old_value, "profile_ValueSetVersion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ValueSetVersion"):
                opp_val = getattr(value, "profile_ValueSetVersion", None)
                setattr(value, "profile_ValueSetVersion", self)

class profile_Enumeration:

    pass
class profile_CodeSystemVersion:

    def __init__(self, identifier: str, version: str, fullName: str, source: str, url: str, effectiveDate: str, releaseDate: str, status: str, statusDate: str, profile_CodeSystemVersion: "profile_CodeSystemConstraint" = None, profile_CodeSystemVersion23: "profile_Enumeration" = None, profile_CodeSystemVersion30: "profile_ValueSetVersion" = None, profile_CodeSystemVersion35: "profile_ValueSetCode" = None):
        self.identifier = identifier
        self.version = version
        self.fullName = fullName
        self.source = source
        self.url = url
        self.effectiveDate = effectiveDate
        self.releaseDate = releaseDate
        self.status = status
        self.statusDate = statusDate
        self.profile_CodeSystemVersion = profile_CodeSystemVersion
        self.profile_CodeSystemVersion23 = profile_CodeSystemVersion23
        self.profile_CodeSystemVersion30 = profile_CodeSystemVersion30
        self.profile_CodeSystemVersion35 = profile_CodeSystemVersion35
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def effectiveDate(self) -> str:
        return self.__effectiveDate

    @effectiveDate.setter
    def effectiveDate(self, effectiveDate: str):
        self.__effectiveDate = effectiveDate

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def statusDate(self) -> str:
        return self.__statusDate

    @statusDate.setter
    def statusDate(self, statusDate: str):
        self.__statusDate = statusDate

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def releaseDate(self) -> str:
        return self.__releaseDate

    @releaseDate.setter
    def releaseDate(self, releaseDate: str):
        self.__releaseDate = releaseDate

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def profile_CodeSystemVersion(self):
        return self.__profile_CodeSystemVersion

    @profile_CodeSystemVersion.setter
    def profile_CodeSystemVersion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CodeSystemVersion__profile_CodeSystemVersion", None)
        self.__profile_CodeSystemVersion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CodeSystemConstraint"):
                opp_val = getattr(old_value, "profile_CodeSystemConstraint", None)
                if opp_val == self:
                    setattr(old_value, "profile_CodeSystemConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CodeSystemConstraint"):
                opp_val = getattr(value, "profile_CodeSystemConstraint", None)
                setattr(value, "profile_CodeSystemConstraint", self)

    @property
    def profile_CodeSystemVersion35(self):
        return self.__profile_CodeSystemVersion35

    @profile_CodeSystemVersion35.setter
    def profile_CodeSystemVersion35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CodeSystemVersion__profile_CodeSystemVersion35", None)
        self.__profile_CodeSystemVersion35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ValueSetCode"):
                opp_val = getattr(old_value, "profile_ValueSetCode", None)
                if opp_val == self:
                    setattr(old_value, "profile_ValueSetCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ValueSetCode"):
                opp_val = getattr(value, "profile_ValueSetCode", None)
                setattr(value, "profile_ValueSetCode", self)

    @property
    def profile_CodeSystemVersion23(self):
        return self.__profile_CodeSystemVersion23

    @profile_CodeSystemVersion23.setter
    def profile_CodeSystemVersion23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CodeSystemVersion__profile_CodeSystemVersion23", None)
        self.__profile_CodeSystemVersion23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Enumeration"):
                opp_val = getattr(old_value, "profile_Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "profile_Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Enumeration"):
                opp_val = getattr(value, "profile_Enumeration", None)
                setattr(value, "profile_Enumeration", self)

    @property
    def profile_CodeSystemVersion30(self):
        return self.__profile_CodeSystemVersion30

    @profile_CodeSystemVersion30.setter
    def profile_CodeSystemVersion30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CodeSystemVersion__profile_CodeSystemVersion30", None)
        self.__profile_CodeSystemVersion30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ValueSetVersion29"):
                opp_val = getattr(old_value, "profile_ValueSetVersion29", None)
                if opp_val == self:
                    setattr(old_value, "profile_ValueSetVersion29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ValueSetVersion29"):
                opp_val = getattr(value, "profile_ValueSetVersion29", None)
                setattr(value, "profile_ValueSetVersion29", self)

    def getEnumerationQualifiedName(self) -> str:
        # TODO: Implement getEnumerationQualifiedName method
        pass

    def setEnumerationName(self, name: str):
        # TODO: Implement setEnumerationName method
        pass

    def getEnumerationName(self) -> str:
        # TODO: Implement getEnumerationName method
        pass

class profile_CodeSystemConstraint:

    def __init__(self, identifier: str, name: str, version: str, binding: str, code: str, displayName: str, profile_CodeSystemConstraint: "profile_CodeSystemVersion" = None, profile_CodeSystemConstraint17: set["profile_CR"] = None, profile_CodeSystemConstraint20: "profile_Property" = None):
        self.identifier = identifier
        self.name = name
        self.version = version
        self.binding = binding
        self.code = code
        self.displayName = displayName
        self.profile_CodeSystemConstraint = profile_CodeSystemConstraint
        self.profile_CodeSystemConstraint17 = profile_CodeSystemConstraint17 if profile_CodeSystemConstraint17 is not None else set()
        self.profile_CodeSystemConstraint20 = profile_CodeSystemConstraint20
        
    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def binding(self) -> str:
        return self.__binding

    @binding.setter
    def binding(self, binding: str):
        self.__binding = binding

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def profile_CodeSystemConstraint17(self):
        return self.__profile_CodeSystemConstraint17

    @profile_CodeSystemConstraint17.setter
    def profile_CodeSystemConstraint17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CodeSystemConstraint__profile_CodeSystemConstraint17", None)
        self.__profile_CodeSystemConstraint17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "profile_CR18"):
                    opp_val = getattr(item, "profile_CR18", None)
                    
                    if opp_val == self:
                        setattr(item, "profile_CR18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "profile_CR18"):
                    opp_val = getattr(item, "profile_CR18", None)
                    
                    setattr(item, "profile_CR18", self)
                    

    @property
    def profile_CodeSystemConstraint20(self):
        return self.__profile_CodeSystemConstraint20

    @profile_CodeSystemConstraint20.setter
    def profile_CodeSystemConstraint20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CodeSystemConstraint__profile_CodeSystemConstraint20", None)
        self.__profile_CodeSystemConstraint20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Property21"):
                opp_val = getattr(old_value, "profile_Property21", None)
                if opp_val == self:
                    setattr(old_value, "profile_Property21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Property21"):
                opp_val = getattr(value, "profile_Property21", None)
                setattr(value, "profile_Property21", self)

    @property
    def profile_CodeSystemConstraint(self):
        return self.__profile_CodeSystemConstraint

    @profile_CodeSystemConstraint.setter
    def profile_CodeSystemConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CodeSystemConstraint__profile_CodeSystemConstraint", None)
        self.__profile_CodeSystemConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CodeSystemVersion"):
                opp_val = getattr(old_value, "profile_CodeSystemVersion", None)
                if opp_val == self:
                    setattr(old_value, "profile_CodeSystemVersion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CodeSystemVersion"):
                opp_val = getattr(value, "profile_CodeSystemVersion", None)
                setattr(value, "profile_CodeSystemVersion", self)

class profile_Class:

    pass
class profile_Property:

    pass
class profile_ConceptDomain:

    def __init__(self, identifier: str, fullName: str, status: str, statusDate: str, profile_ConceptDomain: "profile_ConceptDomainConstraint" = None, profile_ConceptDomain14: "profile_Class" = None, profile_ConceptDomain39: "profile_ValueSetContextBinding" = None):
        self.identifier = identifier
        self.fullName = fullName
        self.status = status
        self.statusDate = statusDate
        self.profile_ConceptDomain = profile_ConceptDomain
        self.profile_ConceptDomain14 = profile_ConceptDomain14
        self.profile_ConceptDomain39 = profile_ConceptDomain39
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def statusDate(self) -> str:
        return self.__statusDate

    @statusDate.setter
    def statusDate(self, statusDate: str):
        self.__statusDate = statusDate

    @property
    def profile_ConceptDomain(self):
        return self.__profile_ConceptDomain

    @profile_ConceptDomain.setter
    def profile_ConceptDomain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ConceptDomain__profile_ConceptDomain", None)
        self.__profile_ConceptDomain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ConceptDomainConstraint"):
                opp_val = getattr(old_value, "profile_ConceptDomainConstraint", None)
                if opp_val == self:
                    setattr(old_value, "profile_ConceptDomainConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ConceptDomainConstraint"):
                opp_val = getattr(value, "profile_ConceptDomainConstraint", None)
                setattr(value, "profile_ConceptDomainConstraint", self)

    @property
    def profile_ConceptDomain39(self):
        return self.__profile_ConceptDomain39

    @profile_ConceptDomain39.setter
    def profile_ConceptDomain39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ConceptDomain__profile_ConceptDomain39", None)
        self.__profile_ConceptDomain39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ValueSetContextBinding"):
                opp_val = getattr(old_value, "profile_ValueSetContextBinding", None)
                if opp_val == self:
                    setattr(old_value, "profile_ValueSetContextBinding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ValueSetContextBinding"):
                opp_val = getattr(value, "profile_ValueSetContextBinding", None)
                setattr(value, "profile_ValueSetContextBinding", self)

    @property
    def profile_ConceptDomain14(self):
        return self.__profile_ConceptDomain14

    @profile_ConceptDomain14.setter
    def profile_ConceptDomain14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ConceptDomain__profile_ConceptDomain14", None)
        self.__profile_ConceptDomain14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Class"):
                opp_val = getattr(old_value, "profile_Class", None)
                if opp_val == self:
                    setattr(old_value, "profile_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Class"):
                opp_val = getattr(value, "profile_Class", None)
                setattr(value, "profile_Class", self)

class profile_ConceptDomainConstraint:

    def __init__(self, identifier: str, name: str, profile_ConceptDomainConstraint: "profile_ConceptDomain" = None, profile_ConceptDomainConstraint12: "profile_Property" = None):
        self.identifier = identifier
        self.name = name
        self.profile_ConceptDomainConstraint = profile_ConceptDomainConstraint
        self.profile_ConceptDomainConstraint12 = profile_ConceptDomainConstraint12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def profile_ConceptDomainConstraint12(self):
        return self.__profile_ConceptDomainConstraint12

    @profile_ConceptDomainConstraint12.setter
    def profile_ConceptDomainConstraint12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ConceptDomainConstraint__profile_ConceptDomainConstraint12", None)
        self.__profile_ConceptDomainConstraint12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_Property"):
                opp_val = getattr(old_value, "profile_Property", None)
                if opp_val == self:
                    setattr(old_value, "profile_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_Property"):
                opp_val = getattr(value, "profile_Property", None)
                setattr(value, "profile_Property", self)

    @property
    def profile_ConceptDomainConstraint(self):
        return self.__profile_ConceptDomainConstraint

    @profile_ConceptDomainConstraint.setter
    def profile_ConceptDomainConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_ConceptDomainConstraint__profile_ConceptDomainConstraint", None)
        self.__profile_ConceptDomainConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_ConceptDomain"):
                opp_val = getattr(old_value, "profile_ConceptDomain", None)
                if opp_val == self:
                    setattr(old_value, "profile_ConceptDomain", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_ConceptDomain"):
                opp_val = getattr(value, "profile_ConceptDomain", None)
                setattr(value, "profile_ConceptDomain", self)

class profile_CR:

    def __init__(self, inverted: str, profile_CR: "profile_CD" = None, profile_CR5: "profile_CD" = None, profile_CR8: "profile_CD" = None, profile_CR18: "profile_CodeSystemConstraint" = None):
        self.inverted = inverted
        self.profile_CR = profile_CR
        self.profile_CR5 = profile_CR5
        self.profile_CR8 = profile_CR8
        self.profile_CR18 = profile_CR18
        
    @property
    def inverted(self) -> str:
        return self.__inverted

    @inverted.setter
    def inverted(self, inverted: str):
        self.__inverted = inverted

    @property
    def profile_CR18(self):
        return self.__profile_CR18

    @profile_CR18.setter
    def profile_CR18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CR__profile_CR18", None)
        self.__profile_CR18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CodeSystemConstraint17"):
                opp_val = getattr(old_value, "profile_CodeSystemConstraint17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CodeSystemConstraint17"):
                opp_val = getattr(value, "profile_CodeSystemConstraint17", None)
                if opp_val is None:
                    setattr(value, "profile_CodeSystemConstraint17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def profile_CR5(self):
        return self.__profile_CR5

    @profile_CR5.setter
    def profile_CR5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CR__profile_CR5", None)
        self.__profile_CR5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CD6"):
                opp_val = getattr(old_value, "profile_CD6", None)
                if opp_val == self:
                    setattr(old_value, "profile_CD6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CD6"):
                opp_val = getattr(value, "profile_CD6", None)
                setattr(value, "profile_CD6", self)

    @property
    def profile_CR8(self):
        return self.__profile_CR8

    @profile_CR8.setter
    def profile_CR8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CR__profile_CR8", None)
        self.__profile_CR8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CD9"):
                opp_val = getattr(old_value, "profile_CD9", None)
                if opp_val == self:
                    setattr(old_value, "profile_CD9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CD9"):
                opp_val = getattr(value, "profile_CD9", None)
                setattr(value, "profile_CD9", self)

    @property
    def profile_CR(self):
        return self.__profile_CR

    @profile_CR.setter
    def profile_CR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CR__profile_CR", None)
        self.__profile_CR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CD"):
                opp_val = getattr(old_value, "profile_CD", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CD"):
                opp_val = getattr(value, "profile_CD", None)
                if opp_val is None:
                    setattr(value, "profile_CD", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class profile_CD:

    def __init__(self, code: str, codeSystem: str, codeSystemName: str, codeSystemVersion: str, displayName: str, profile_CD: set["profile_CR"] = None, profile_CD3: "profile_CD" = None, profile_CD1: set["profile_CD"] = None, profile_CD6: "profile_CR" = None, profile_CD9: "profile_CR" = None):
        self.code = code
        self.codeSystem = codeSystem
        self.codeSystemName = codeSystemName
        self.codeSystemVersion = codeSystemVersion
        self.displayName = displayName
        self.profile_CD = profile_CD if profile_CD is not None else set()
        self.profile_CD3 = profile_CD3
        self.profile_CD1 = profile_CD1 if profile_CD1 is not None else set()
        self.profile_CD6 = profile_CD6
        self.profile_CD9 = profile_CD9
        
    @property
    def codeSystemVersion(self) -> str:
        return self.__codeSystemVersion

    @codeSystemVersion.setter
    def codeSystemVersion(self, codeSystemVersion: str):
        self.__codeSystemVersion = codeSystemVersion

    @property
    def codeSystem(self) -> str:
        return self.__codeSystem

    @codeSystem.setter
    def codeSystem(self, codeSystem: str):
        self.__codeSystem = codeSystem

    @property
    def codeSystemName(self) -> str:
        return self.__codeSystemName

    @codeSystemName.setter
    def codeSystemName(self, codeSystemName: str):
        self.__codeSystemName = codeSystemName

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def profile_CD(self):
        return self.__profile_CD

    @profile_CD.setter
    def profile_CD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CD__profile_CD", None)
        self.__profile_CD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "profile_CR"):
                    opp_val = getattr(item, "profile_CR", None)
                    
                    if opp_val == self:
                        setattr(item, "profile_CR", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "profile_CR"):
                    opp_val = getattr(item, "profile_CR", None)
                    
                    setattr(item, "profile_CR", self)
                    

    @property
    def profile_CD1(self):
        return self.__profile_CD1

    @profile_CD1.setter
    def profile_CD1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CD__profile_CD1", None)
        self.__profile_CD1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "profile_CD3"):
                    opp_val = getattr(item, "profile_CD3", None)
                    
                    if opp_val == self:
                        setattr(item, "profile_CD3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "profile_CD3"):
                    opp_val = getattr(item, "profile_CD3", None)
                    
                    setattr(item, "profile_CD3", self)
                    

    @property
    def profile_CD3(self):
        return self.__profile_CD3

    @profile_CD3.setter
    def profile_CD3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CD__profile_CD3", None)
        self.__profile_CD3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CD1"):
                opp_val = getattr(old_value, "profile_CD1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CD1"):
                opp_val = getattr(value, "profile_CD1", None)
                if opp_val is None:
                    setattr(value, "profile_CD1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def profile_CD9(self):
        return self.__profile_CD9

    @profile_CD9.setter
    def profile_CD9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CD__profile_CD9", None)
        self.__profile_CD9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CR8"):
                opp_val = getattr(old_value, "profile_CR8", None)
                if opp_val == self:
                    setattr(old_value, "profile_CR8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CR8"):
                opp_val = getattr(value, "profile_CR8", None)
                setattr(value, "profile_CR8", self)

    @property
    def profile_CD6(self):
        return self.__profile_CD6

    @profile_CD6.setter
    def profile_CD6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_profile_CD__profile_CD6", None)
        self.__profile_CD6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile_CR5"):
                opp_val = getattr(old_value, "profile_CR5", None)
                if opp_val == self:
                    setattr(old_value, "profile_CR5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile_CR5"):
                opp_val = getattr(value, "profile_CR5", None)
                setattr(value, "profile_CR5", self)
