from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CorrelationPattern(Enum):
    request = "request"
    response = "response"
    requestresponse = "requestresponse"
class XSDSubstitutionGroupExclusions(Enum):
    extension = "extension"
    restriction = "restriction"
class XSDProhibitedSubstitutions(Enum):
    extension = "extension"
    restriction = "restriction"
    all = "all"
class XSDConstraint(Enum):
    default = "default"
    fixed = "fixed"
class XSDVariety(Enum):
    atomic = "atomic"
    list = "list"
    union = "union"
class XSDDerivationMethod(Enum):
    extension = "extension"
    restriction = "restriction"
class XSDOrdered(Enum):
    false = "false"
    partial = "partial"
    total = "total"
class XSDDisallowedSubstitutions(Enum):
    substitution = "substitution"
    extension = "extension"
    restriction = "restriction"
    all = "all"
class XSDIdentityConstraintCategory(Enum):
    key = "key"
    keyref = "keyref"
    unique = "unique"
class XSDSimpleFinal(Enum):
    list = "list"
    restriction = "restriction"
    union = "union"
    all = "all"
class XSDContentTypeCategory(Enum):
    empty = "empty"
    simple = "simple"
    mixed = "mixed"
    elementOnly = "elementOnly"
class XSDDiagnosticSeverity(Enum):
    fatal = "fatal"
    error = "error"
    warning = "warning"
    information = "information"
class XSDProcessContents(Enum):
    strict = "strict"
    lax = "lax"
    skip = "skip"
class XSDNamespaceConstraintCategory(Enum):
    any = "any"
    not = "not"
    set = "set"
class XSDWhiteSpace(Enum):
    replace = "replace"
    collapse = "collapse"
    preserve = "preserve"
class XSDCardinality(Enum):
    finite = "finite"
    countablyInfinite = "countablyInfinite"
class XSDAttributeUseCategory(Enum):
    optional = "optional"
    prohibited = "prohibited"
    required = "required"
class XSDCompositor(Enum):
    sequence = "sequence"
    all = "all"
    choice = "choice"
class XSDXPathVariety(Enum):
    selector = "selector"
    field = "field"
class EndpointReferenceRole(Enum):
    myRole = "myRole"
    partnerRole = "partnerRole"
class XSDComplexFinal(Enum):
    extension = "extension"
    restriction = "restriction"
    all = "all"
class XSDForm(Enum):
    qualified = "qualified"
    unqualified = "unqualified"


############################################
# Definition of Classes
############################################

class Query:

    pass
class XSDBoundedFacet:

    pass
class XSDOrderedFacet:

    pass
class XSDFractionDigitsFacet:

    pass
class XSDTotalDigitsFacet:

    pass
class XSDMinLengthFacet:

    pass
class XSDMaxLengthFacet:

    pass
class XSDNumericFacet:

    pass
class XSDEnumerationFacet:

    pass
class XSDWhiteSpaceFacet:

    pass
class XSDLengthFacet:

    pass
class XSDMaxExclusiveFacet:

    pass
class XSDMinExclusiveFacet:

    pass
class XSDMinInclusiveFacet:

    pass
class XSDMaxInclusiveFacet:

    pass
class XSDCardinalityFacet:

    pass
class XSDPatternFacet:

    pass
class xsd_XSDComplexTypeContent:

    pass
class XSDNotationDeclaration:

    pass
class XSDRedefineContent:

    pass
class XSDSchemaContent:

    pass
class model_xsd_XSDSchemaDirective(XSDSchemaContent):

    def __init__(self, schemaLocation: str, model_xsd_XSDSchemaDirective: "XSDSchema" = None, XSDSchemaContent: "model_xsd_XSDSchema"):
        self.schemaLocation = schemaLocation
        self.model_xsd_XSDSchemaDirective = model_xsd_XSDSchemaDirective
        
    @property
    def schemaLocation(self) -> str:
        return self.__schemaLocation

    @schemaLocation.setter
    def schemaLocation(self, schemaLocation: str):
        self.__schemaLocation = schemaLocation

    @property
    def model_xsd_XSDSchemaDirective(self):
        return self.__model_xsd_XSDSchemaDirective

    @model_xsd_XSDSchemaDirective.setter
    def model_xsd_XSDSchemaDirective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchemaDirective__model_xsd_XSDSchemaDirective", None)
        self.__model_xsd_XSDSchemaDirective = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSchema598"):
                opp_val = getattr(old_value, "XSDSchema598", None)
                if opp_val == self:
                    setattr(old_value, "XSDSchema598", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSchema598"):
                opp_val = getattr(value, "XSDSchema598", None)
                setattr(value, "XSDSchema598", self)

class model_xsd_XSDRedefineContent(XSDSchemaContent):

    pass
class XSDParticleContent:

    pass
class XSDModelGroupDefinition:

    pass
class XSDModelGroup:

    pass
class xsd_XSDParticleContent:

    pass
class XSDTerm:

    pass
class model_xsd_XSDWildcard(XSDTerm):

    def __init__(self, namespaceConstraintCategory: str, namespaceConstraint: str, processContents: str, lexicalNamespaceConstraint: str, model_xsd_XSDWildcard: "XSDAnnotation" = None, model_xsd_XSDWildcard714: set["XSDAnnotation"] = None, XSDTerm: "model_xsd_XSDParticle"):
        self.namespaceConstraintCategory = namespaceConstraintCategory
        self.namespaceConstraint = namespaceConstraint
        self.processContents = processContents
        self.lexicalNamespaceConstraint = lexicalNamespaceConstraint
        self.model_xsd_XSDWildcard = model_xsd_XSDWildcard
        self.model_xsd_XSDWildcard714 = model_xsd_XSDWildcard714 if model_xsd_XSDWildcard714 is not None else set()
        
    @property
    def lexicalNamespaceConstraint(self) -> str:
        return self.__lexicalNamespaceConstraint

    @lexicalNamespaceConstraint.setter
    def lexicalNamespaceConstraint(self, lexicalNamespaceConstraint: str):
        self.__lexicalNamespaceConstraint = lexicalNamespaceConstraint

    @property
    def namespaceConstraintCategory(self) -> str:
        return self.__namespaceConstraintCategory

    @namespaceConstraintCategory.setter
    def namespaceConstraintCategory(self, namespaceConstraintCategory: str):
        self.__namespaceConstraintCategory = namespaceConstraintCategory

    @property
    def processContents(self) -> str:
        return self.__processContents

    @processContents.setter
    def processContents(self, processContents: str):
        self.__processContents = processContents

    @property
    def namespaceConstraint(self) -> str:
        return self.__namespaceConstraint

    @namespaceConstraint.setter
    def namespaceConstraint(self, namespaceConstraint: str):
        self.__namespaceConstraint = namespaceConstraint

    @property
    def model_xsd_XSDWildcard(self):
        return self.__model_xsd_XSDWildcard

    @model_xsd_XSDWildcard.setter
    def model_xsd_XSDWildcard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDWildcard__model_xsd_XSDWildcard", None)
        self.__model_xsd_XSDWildcard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation712"):
                opp_val = getattr(old_value, "XSDAnnotation712", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation712", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation712"):
                opp_val = getattr(value, "XSDAnnotation712", None)
                setattr(value, "XSDAnnotation712", self)

    @property
    def model_xsd_XSDWildcard714(self):
        return self.__model_xsd_XSDWildcard714

    @model_xsd_XSDWildcard714.setter
    def model_xsd_XSDWildcard714(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDWildcard__model_xsd_XSDWildcard714", None)
        self.__model_xsd_XSDWildcard714 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDAnnotation715"):
                    opp_val = getattr(item, "XSDAnnotation715", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDAnnotation715", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDAnnotation715"):
                    opp_val = getattr(item, "XSDAnnotation715", None)
                    
                    setattr(item, "XSDAnnotation715", self)
                    

class model_xsd_XSDModelGroup(XSDTerm):

    def __init__(self, compositor: str, model_xsd_XSDModelGroup: "XSDAnnotation" = None, model_xsd_XSDModelGroup532: set["XSDParticle"] = None, model_xsd_XSDModelGroup535: set["XSDParticle"] = None, XSDTerm: "model_xsd_XSDParticle"):
        self.compositor = compositor
        self.model_xsd_XSDModelGroup = model_xsd_XSDModelGroup
        self.model_xsd_XSDModelGroup532 = model_xsd_XSDModelGroup532 if model_xsd_XSDModelGroup532 is not None else set()
        self.model_xsd_XSDModelGroup535 = model_xsd_XSDModelGroup535 if model_xsd_XSDModelGroup535 is not None else set()
        
    @property
    def compositor(self) -> str:
        return self.__compositor

    @compositor.setter
    def compositor(self, compositor: str):
        self.__compositor = compositor

    @property
    def model_xsd_XSDModelGroup535(self):
        return self.__model_xsd_XSDModelGroup535

    @model_xsd_XSDModelGroup535.setter
    def model_xsd_XSDModelGroup535(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDModelGroup__model_xsd_XSDModelGroup535", None)
        self.__model_xsd_XSDModelGroup535 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDParticle536"):
                    opp_val = getattr(item, "XSDParticle536", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDParticle536", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDParticle536"):
                    opp_val = getattr(item, "XSDParticle536", None)
                    
                    setattr(item, "XSDParticle536", self)
                    

    @property
    def model_xsd_XSDModelGroup532(self):
        return self.__model_xsd_XSDModelGroup532

    @model_xsd_XSDModelGroup532.setter
    def model_xsd_XSDModelGroup532(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDModelGroup__model_xsd_XSDModelGroup532", None)
        self.__model_xsd_XSDModelGroup532 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDParticle533"):
                    opp_val = getattr(item, "XSDParticle533", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDParticle533", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDParticle533"):
                    opp_val = getattr(item, "XSDParticle533", None)
                    
                    setattr(item, "XSDParticle533", self)
                    

    @property
    def model_xsd_XSDModelGroup(self):
        return self.__model_xsd_XSDModelGroup

    @model_xsd_XSDModelGroup.setter
    def model_xsd_XSDModelGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDModelGroup__model_xsd_XSDModelGroup", None)
        self.__model_xsd_XSDModelGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation530"):
                opp_val = getattr(old_value, "XSDAnnotation530", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation530", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation530"):
                opp_val = getattr(value, "XSDAnnotation530", None)
                setattr(value, "XSDAnnotation530", self)

class XSDMinFacet:

    pass
class model_xsd_XSDMinInclusiveFacet(XSDMinFacet):

    pass
class model_xsd_XSDMinExclusiveFacet(XSDMinFacet):

    pass
class xsd_XSDNamedComponent:

    pass
class XSDSchemaCompositor:

    pass
class model_xsd_XSDRedefine(XSDSchemaCompositor):

    pass
class model_xsd_XSDInclude(XSDSchemaCompositor):

    pass
class XSDSchemaDirective:

    pass
class model_xsd_XSDSchemaCompositor(XSDSchemaDirective):

    pass
class model_xsd_XSDImport(XSDSchemaDirective):

    def __init__(self, namespace: str, model_xsd_XSDImport: "XSDAnnotation" = None, XSDSchemaDirective: "model_xsd_XSDSchema"):
        self.namespace = namespace
        self.model_xsd_XSDImport = model_xsd_XSDImport
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def model_xsd_XSDImport(self):
        return self.__model_xsd_XSDImport

    @model_xsd_XSDImport.setter
    def model_xsd_XSDImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDImport__model_xsd_XSDImport", None)
        self.__model_xsd_XSDImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation526"):
                opp_val = getattr(old_value, "XSDAnnotation526", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation526", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation526"):
                opp_val = getattr(value, "XSDAnnotation526", None)
                setattr(value, "XSDAnnotation526", self)

class XSDXPathDefinition:

    pass
class XSDFixedFacet:

    pass
class model_xsd_XSDLengthFacet(XSDFixedFacet):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class model_xsd_XSDMinFacet(XSDFixedFacet):

    def __init__(self, value: str, inclusive: bool, exclusive: bool):
        self.value = value
        self.inclusive = inclusive
        self.exclusive = exclusive
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def inclusive(self) -> bool:
        return self.__inclusive

    @inclusive.setter
    def inclusive(self, inclusive: bool):
        self.__inclusive = inclusive

    @property
    def exclusive(self) -> bool:
        return self.__exclusive

    @exclusive.setter
    def exclusive(self, exclusive: bool):
        self.__exclusive = exclusive

class model_xsd_XSDWhiteSpaceFacet(XSDFixedFacet):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_xsd_XSDMinLengthFacet(XSDFixedFacet):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class model_xsd_XSDTotalDigitsFacet(XSDFixedFacet):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class model_xsd_XSDMaxLengthFacet(XSDFixedFacet):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class model_xsd_XSDFractionDigitsFacet(XSDFixedFacet):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class XSDConstrainingFacet:

    pass
class model_xsd_XSDRepeatableFacet(XSDConstrainingFacet):

    pass
class model_xsd_XSDFixedFacet(XSDConstrainingFacet):

    def __init__(self, fixed: bool, XSDConstrainingFacet605: "model_xsd_XSDSimpleTypeDefinition", XSDConstrainingFacet: "model_xsd_XSDSimpleTypeDefinition"):
        self.fixed = fixed
        
    @property
    def fixed(self) -> bool:
        return self.__fixed

    @fixed.setter
    def fixed(self, fixed: bool):
        self.__fixed = fixed

class XSDFeature:

    pass
class XSDScope:

    pass
class model_xsd_XSDSchema(XSDScope):

    def __init__(self, document: str, schemaLocation: str, targetNamespace: str, attributeFormDefault: str, elementFormDefault: str, finalDefault: str, blockDefault: str, version: str, model_xsd_XSDSchema587: "XSDSchema" = None, model_xsd_XSDSchema: set["XSDSchemaContent"] = None, model_xsd_XSDSchema556: set["XSDElementDeclaration"] = None, model_xsd_XSDSchema559: set["XSDAttributeDeclaration"] = None, model_xsd_XSDSchema562: set["XSDAttributeGroupDefinition"] = None, model_xsd_XSDSchema565: set["XSDTypeDefinition"] = None, model_xsd_XSDSchema568: set["XSDModelGroupDefinition"] = None, model_xsd_XSDSchema571: set["XSDIdentityConstraintDefinition"] = None, model_xsd_XSDSchema574: set["XSDNotationDeclaration"] = None, model_xsd_XSDSchema576: set["XSDAnnotation"] = None, model_xsd_XSDSchema579: set["XSDDiagnostic"] = None, model_xsd_XSDSchema582: set["XSDSchemaDirective"] = None, model_xsd_XSDSchema584: "XSDSchema" = None, model_xsd_XSDSchema590: set["XSDSchema"] = None, model_xsd_XSDSchema593: "XSDSchema" = None, XSDScope: "model_xsd_XSDFeature"):
        self.document = document
        self.schemaLocation = schemaLocation
        self.targetNamespace = targetNamespace
        self.attributeFormDefault = attributeFormDefault
        self.elementFormDefault = elementFormDefault
        self.finalDefault = finalDefault
        self.blockDefault = blockDefault
        self.version = version
        self.model_xsd_XSDSchema587 = model_xsd_XSDSchema587
        self.model_xsd_XSDSchema = model_xsd_XSDSchema if model_xsd_XSDSchema is not None else set()
        self.model_xsd_XSDSchema556 = model_xsd_XSDSchema556 if model_xsd_XSDSchema556 is not None else set()
        self.model_xsd_XSDSchema559 = model_xsd_XSDSchema559 if model_xsd_XSDSchema559 is not None else set()
        self.model_xsd_XSDSchema562 = model_xsd_XSDSchema562 if model_xsd_XSDSchema562 is not None else set()
        self.model_xsd_XSDSchema565 = model_xsd_XSDSchema565 if model_xsd_XSDSchema565 is not None else set()
        self.model_xsd_XSDSchema568 = model_xsd_XSDSchema568 if model_xsd_XSDSchema568 is not None else set()
        self.model_xsd_XSDSchema571 = model_xsd_XSDSchema571 if model_xsd_XSDSchema571 is not None else set()
        self.model_xsd_XSDSchema574 = model_xsd_XSDSchema574 if model_xsd_XSDSchema574 is not None else set()
        self.model_xsd_XSDSchema576 = model_xsd_XSDSchema576 if model_xsd_XSDSchema576 is not None else set()
        self.model_xsd_XSDSchema579 = model_xsd_XSDSchema579 if model_xsd_XSDSchema579 is not None else set()
        self.model_xsd_XSDSchema582 = model_xsd_XSDSchema582 if model_xsd_XSDSchema582 is not None else set()
        self.model_xsd_XSDSchema584 = model_xsd_XSDSchema584
        self.model_xsd_XSDSchema590 = model_xsd_XSDSchema590 if model_xsd_XSDSchema590 is not None else set()
        self.model_xsd_XSDSchema593 = model_xsd_XSDSchema593
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def blockDefault(self) -> str:
        return self.__blockDefault

    @blockDefault.setter
    def blockDefault(self, blockDefault: str):
        self.__blockDefault = blockDefault

    @property
    def targetNamespace(self) -> str:
        return self.__targetNamespace

    @targetNamespace.setter
    def targetNamespace(self, targetNamespace: str):
        self.__targetNamespace = targetNamespace

    @property
    def finalDefault(self) -> str:
        return self.__finalDefault

    @finalDefault.setter
    def finalDefault(self, finalDefault: str):
        self.__finalDefault = finalDefault

    @property
    def elementFormDefault(self) -> str:
        return self.__elementFormDefault

    @elementFormDefault.setter
    def elementFormDefault(self, elementFormDefault: str):
        self.__elementFormDefault = elementFormDefault

    @property
    def document(self) -> str:
        return self.__document

    @document.setter
    def document(self, document: str):
        self.__document = document

    @property
    def attributeFormDefault(self) -> str:
        return self.__attributeFormDefault

    @attributeFormDefault.setter
    def attributeFormDefault(self, attributeFormDefault: str):
        self.__attributeFormDefault = attributeFormDefault

    @property
    def schemaLocation(self) -> str:
        return self.__schemaLocation

    @schemaLocation.setter
    def schemaLocation(self, schemaLocation: str):
        self.__schemaLocation = schemaLocation

    @property
    def model_xsd_XSDSchema556(self):
        return self.__model_xsd_XSDSchema556

    @model_xsd_XSDSchema556.setter
    def model_xsd_XSDSchema556(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema556", None)
        self.__model_xsd_XSDSchema556 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDElementDeclaration557"):
                    opp_val = getattr(item, "XSDElementDeclaration557", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDElementDeclaration557", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDElementDeclaration557"):
                    opp_val = getattr(item, "XSDElementDeclaration557", None)
                    
                    setattr(item, "XSDElementDeclaration557", self)
                    

    @property
    def model_xsd_XSDSchema574(self):
        return self.__model_xsd_XSDSchema574

    @model_xsd_XSDSchema574.setter
    def model_xsd_XSDSchema574(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema574", None)
        self.__model_xsd_XSDSchema574 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDNotationDeclaration"):
                    opp_val = getattr(item, "XSDNotationDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDNotationDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDNotationDeclaration"):
                    opp_val = getattr(item, "XSDNotationDeclaration", None)
                    
                    setattr(item, "XSDNotationDeclaration", self)
                    

    @property
    def model_xsd_XSDSchema571(self):
        return self.__model_xsd_XSDSchema571

    @model_xsd_XSDSchema571.setter
    def model_xsd_XSDSchema571(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema571", None)
        self.__model_xsd_XSDSchema571 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDIdentityConstraintDefinition572"):
                    opp_val = getattr(item, "XSDIdentityConstraintDefinition572", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDIdentityConstraintDefinition572", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDIdentityConstraintDefinition572"):
                    opp_val = getattr(item, "XSDIdentityConstraintDefinition572", None)
                    
                    setattr(item, "XSDIdentityConstraintDefinition572", self)
                    

    @property
    def model_xsd_XSDSchema593(self):
        return self.__model_xsd_XSDSchema593

    @model_xsd_XSDSchema593.setter
    def model_xsd_XSDSchema593(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema593", None)
        self.__model_xsd_XSDSchema593 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSchema594"):
                opp_val = getattr(old_value, "XSDSchema594", None)
                if opp_val == self:
                    setattr(old_value, "XSDSchema594", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSchema594"):
                opp_val = getattr(value, "XSDSchema594", None)
                setattr(value, "XSDSchema594", self)

    @property
    def model_xsd_XSDSchema(self):
        return self.__model_xsd_XSDSchema

    @model_xsd_XSDSchema.setter
    def model_xsd_XSDSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema", None)
        self.__model_xsd_XSDSchema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDSchemaContent"):
                    opp_val = getattr(item, "XSDSchemaContent", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDSchemaContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDSchemaContent"):
                    opp_val = getattr(item, "XSDSchemaContent", None)
                    
                    setattr(item, "XSDSchemaContent", self)
                    

    @property
    def model_xsd_XSDSchema559(self):
        return self.__model_xsd_XSDSchema559

    @model_xsd_XSDSchema559.setter
    def model_xsd_XSDSchema559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema559", None)
        self.__model_xsd_XSDSchema559 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDAttributeDeclaration560"):
                    opp_val = getattr(item, "XSDAttributeDeclaration560", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDAttributeDeclaration560", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDAttributeDeclaration560"):
                    opp_val = getattr(item, "XSDAttributeDeclaration560", None)
                    
                    setattr(item, "XSDAttributeDeclaration560", self)
                    

    @property
    def model_xsd_XSDSchema562(self):
        return self.__model_xsd_XSDSchema562

    @model_xsd_XSDSchema562.setter
    def model_xsd_XSDSchema562(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema562", None)
        self.__model_xsd_XSDSchema562 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDAttributeGroupDefinition563"):
                    opp_val = getattr(item, "XSDAttributeGroupDefinition563", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDAttributeGroupDefinition563", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDAttributeGroupDefinition563"):
                    opp_val = getattr(item, "XSDAttributeGroupDefinition563", None)
                    
                    setattr(item, "XSDAttributeGroupDefinition563", self)
                    

    @property
    def model_xsd_XSDSchema590(self):
        return self.__model_xsd_XSDSchema590

    @model_xsd_XSDSchema590.setter
    def model_xsd_XSDSchema590(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema590", None)
        self.__model_xsd_XSDSchema590 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDSchema591"):
                    opp_val = getattr(item, "XSDSchema591", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDSchema591", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDSchema591"):
                    opp_val = getattr(item, "XSDSchema591", None)
                    
                    setattr(item, "XSDSchema591", self)
                    

    @property
    def model_xsd_XSDSchema587(self):
        return self.__model_xsd_XSDSchema587

    @model_xsd_XSDSchema587.setter
    def model_xsd_XSDSchema587(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema587", None)
        self.__model_xsd_XSDSchema587 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSchema588"):
                opp_val = getattr(old_value, "XSDSchema588", None)
                if opp_val == self:
                    setattr(old_value, "XSDSchema588", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSchema588"):
                opp_val = getattr(value, "XSDSchema588", None)
                setattr(value, "XSDSchema588", self)

    @property
    def model_xsd_XSDSchema584(self):
        return self.__model_xsd_XSDSchema584

    @model_xsd_XSDSchema584.setter
    def model_xsd_XSDSchema584(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema584", None)
        self.__model_xsd_XSDSchema584 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSchema585"):
                opp_val = getattr(old_value, "XSDSchema585", None)
                if opp_val == self:
                    setattr(old_value, "XSDSchema585", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSchema585"):
                opp_val = getattr(value, "XSDSchema585", None)
                setattr(value, "XSDSchema585", self)

    @property
    def model_xsd_XSDSchema576(self):
        return self.__model_xsd_XSDSchema576

    @model_xsd_XSDSchema576.setter
    def model_xsd_XSDSchema576(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema576", None)
        self.__model_xsd_XSDSchema576 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDAnnotation577"):
                    opp_val = getattr(item, "XSDAnnotation577", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDAnnotation577", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDAnnotation577"):
                    opp_val = getattr(item, "XSDAnnotation577", None)
                    
                    setattr(item, "XSDAnnotation577", self)
                    

    @property
    def model_xsd_XSDSchema579(self):
        return self.__model_xsd_XSDSchema579

    @model_xsd_XSDSchema579.setter
    def model_xsd_XSDSchema579(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema579", None)
        self.__model_xsd_XSDSchema579 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDDiagnostic580"):
                    opp_val = getattr(item, "XSDDiagnostic580", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDDiagnostic580", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDDiagnostic580"):
                    opp_val = getattr(item, "XSDDiagnostic580", None)
                    
                    setattr(item, "XSDDiagnostic580", self)
                    

    @property
    def model_xsd_XSDSchema582(self):
        return self.__model_xsd_XSDSchema582

    @model_xsd_XSDSchema582.setter
    def model_xsd_XSDSchema582(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema582", None)
        self.__model_xsd_XSDSchema582 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDSchemaDirective"):
                    opp_val = getattr(item, "XSDSchemaDirective", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDSchemaDirective", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDSchemaDirective"):
                    opp_val = getattr(item, "XSDSchemaDirective", None)
                    
                    setattr(item, "XSDSchemaDirective", self)
                    

    @property
    def model_xsd_XSDSchema565(self):
        return self.__model_xsd_XSDSchema565

    @model_xsd_XSDSchema565.setter
    def model_xsd_XSDSchema565(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema565", None)
        self.__model_xsd_XSDSchema565 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDTypeDefinition566"):
                    opp_val = getattr(item, "XSDTypeDefinition566", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDTypeDefinition566", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDTypeDefinition566"):
                    opp_val = getattr(item, "XSDTypeDefinition566", None)
                    
                    setattr(item, "XSDTypeDefinition566", self)
                    

    @property
    def model_xsd_XSDSchema568(self):
        return self.__model_xsd_XSDSchema568

    @model_xsd_XSDSchema568.setter
    def model_xsd_XSDSchema568(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSchema__model_xsd_XSDSchema568", None)
        self.__model_xsd_XSDSchema568 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDModelGroupDefinition569"):
                    opp_val = getattr(item, "XSDModelGroupDefinition569", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDModelGroupDefinition569", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDModelGroupDefinition569"):
                    opp_val = getattr(item, "XSDModelGroupDefinition569", None)
                    
                    setattr(item, "XSDModelGroupDefinition569", self)
                    

class model_xsd_XSDMaxFacet(XSDFixedFacet):

    def __init__(self, value: str, inclusive: bool, exclusive: bool):
        self.value = value
        self.inclusive = inclusive
        self.exclusive = exclusive
        
    @property
    def exclusive(self) -> bool:
        return self.__exclusive

    @exclusive.setter
    def exclusive(self, exclusive: bool):
        self.__exclusive = exclusive

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def inclusive(self) -> bool:
        return self.__inclusive

    @inclusive.setter
    def inclusive(self, inclusive: bool):
        self.__inclusive = inclusive

class XSDMaxFacet:

    pass
class model_xsd_XSDMaxInclusiveFacet(XSDMaxFacet):

    pass
class model_xsd_XSDMaxExclusiveFacet(XSDMaxFacet):

    pass
class XSDNamedComponent:

    pass
class model_xsd_XSDIdentityConstraintDefinition(XSDNamedComponent):

    def __init__(self, identityConstraintCategory: str, model_xsd_XSDIdentityConstraintDefinition: "XSDAnnotation" = None, model_xsd_XSDIdentityConstraintDefinition518: "XSDIdentityConstraintDefinition" = None, model_xsd_XSDIdentityConstraintDefinition521: "XSDXPathDefinition" = None, model_xsd_XSDIdentityConstraintDefinition523: set["XSDXPathDefinition"] = None):
        self.identityConstraintCategory = identityConstraintCategory
        self.model_xsd_XSDIdentityConstraintDefinition = model_xsd_XSDIdentityConstraintDefinition
        self.model_xsd_XSDIdentityConstraintDefinition518 = model_xsd_XSDIdentityConstraintDefinition518
        self.model_xsd_XSDIdentityConstraintDefinition521 = model_xsd_XSDIdentityConstraintDefinition521
        self.model_xsd_XSDIdentityConstraintDefinition523 = model_xsd_XSDIdentityConstraintDefinition523 if model_xsd_XSDIdentityConstraintDefinition523 is not None else set()
        
    @property
    def identityConstraintCategory(self) -> str:
        return self.__identityConstraintCategory

    @identityConstraintCategory.setter
    def identityConstraintCategory(self, identityConstraintCategory: str):
        self.__identityConstraintCategory = identityConstraintCategory

    @property
    def model_xsd_XSDIdentityConstraintDefinition521(self):
        return self.__model_xsd_XSDIdentityConstraintDefinition521

    @model_xsd_XSDIdentityConstraintDefinition521.setter
    def model_xsd_XSDIdentityConstraintDefinition521(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDIdentityConstraintDefinition__model_xsd_XSDIdentityConstraintDefinition521", None)
        self.__model_xsd_XSDIdentityConstraintDefinition521 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDXPathDefinition"):
                opp_val = getattr(old_value, "XSDXPathDefinition", None)
                if opp_val == self:
                    setattr(old_value, "XSDXPathDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDXPathDefinition"):
                opp_val = getattr(value, "XSDXPathDefinition", None)
                setattr(value, "XSDXPathDefinition", self)

    @property
    def model_xsd_XSDIdentityConstraintDefinition518(self):
        return self.__model_xsd_XSDIdentityConstraintDefinition518

    @model_xsd_XSDIdentityConstraintDefinition518.setter
    def model_xsd_XSDIdentityConstraintDefinition518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDIdentityConstraintDefinition__model_xsd_XSDIdentityConstraintDefinition518", None)
        self.__model_xsd_XSDIdentityConstraintDefinition518 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDIdentityConstraintDefinition519"):
                opp_val = getattr(old_value, "XSDIdentityConstraintDefinition519", None)
                if opp_val == self:
                    setattr(old_value, "XSDIdentityConstraintDefinition519", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDIdentityConstraintDefinition519"):
                opp_val = getattr(value, "XSDIdentityConstraintDefinition519", None)
                setattr(value, "XSDIdentityConstraintDefinition519", self)

    @property
    def model_xsd_XSDIdentityConstraintDefinition(self):
        return self.__model_xsd_XSDIdentityConstraintDefinition

    @model_xsd_XSDIdentityConstraintDefinition.setter
    def model_xsd_XSDIdentityConstraintDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDIdentityConstraintDefinition__model_xsd_XSDIdentityConstraintDefinition", None)
        self.__model_xsd_XSDIdentityConstraintDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation516"):
                opp_val = getattr(old_value, "XSDAnnotation516", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation516", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation516"):
                opp_val = getattr(value, "XSDAnnotation516", None)
                setattr(value, "XSDAnnotation516", self)

    @property
    def model_xsd_XSDIdentityConstraintDefinition523(self):
        return self.__model_xsd_XSDIdentityConstraintDefinition523

    @model_xsd_XSDIdentityConstraintDefinition523.setter
    def model_xsd_XSDIdentityConstraintDefinition523(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDIdentityConstraintDefinition__model_xsd_XSDIdentityConstraintDefinition523", None)
        self.__model_xsd_XSDIdentityConstraintDefinition523 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDXPathDefinition524"):
                    opp_val = getattr(item, "XSDXPathDefinition524", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDXPathDefinition524", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDXPathDefinition524"):
                    opp_val = getattr(item, "XSDXPathDefinition524", None)
                    
                    setattr(item, "XSDXPathDefinition524", self)
                    

class model_xsd_XSDFeature(XSDNamedComponent):

    def __init__(self, value: str, constraint: str, form: str, lexicalValue: str, global: bool, featureReference: bool, model_xsd_XSDFeature: "XSDScope" = None, model_xsd_XSDFeature511: "XSDFeature" = None, model_xsd_XSDFeature513: "XSDTypeDefinition" = None):
        self.value = value
        self.constraint = constraint
        self.form = form
        self.lexicalValue = lexicalValue
        self.global = global
        self.featureReference = featureReference
        self.model_xsd_XSDFeature = model_xsd_XSDFeature
        self.model_xsd_XSDFeature511 = model_xsd_XSDFeature511
        self.model_xsd_XSDFeature513 = model_xsd_XSDFeature513
        
    @property
    def form(self) -> str:
        return self.__form

    @form.setter
    def form(self, form: str):
        self.__form = form

    @property
    def featureReference(self) -> bool:
        return self.__featureReference

    @featureReference.setter
    def featureReference(self, featureReference: bool):
        self.__featureReference = featureReference

    @property
    def global(self) -> bool:
        return self.__global

    @global.setter
    def global(self, global: bool):
        self.__global = global

    @property
    def constraint(self) -> str:
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: str):
        self.__constraint = constraint

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def lexicalValue(self) -> str:
        return self.__lexicalValue

    @lexicalValue.setter
    def lexicalValue(self, lexicalValue: str):
        self.__lexicalValue = lexicalValue

    @property
    def model_xsd_XSDFeature511(self):
        return self.__model_xsd_XSDFeature511

    @model_xsd_XSDFeature511.setter
    def model_xsd_XSDFeature511(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDFeature__model_xsd_XSDFeature511", None)
        self.__model_xsd_XSDFeature511 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDFeature"):
                opp_val = getattr(old_value, "XSDFeature", None)
                if opp_val == self:
                    setattr(old_value, "XSDFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDFeature"):
                opp_val = getattr(value, "XSDFeature", None)
                setattr(value, "XSDFeature", self)

    @property
    def model_xsd_XSDFeature513(self):
        return self.__model_xsd_XSDFeature513

    @model_xsd_XSDFeature513.setter
    def model_xsd_XSDFeature513(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDFeature__model_xsd_XSDFeature513", None)
        self.__model_xsd_XSDFeature513 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTypeDefinition514"):
                opp_val = getattr(old_value, "XSDTypeDefinition514", None)
                if opp_val == self:
                    setattr(old_value, "XSDTypeDefinition514", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTypeDefinition514"):
                opp_val = getattr(value, "XSDTypeDefinition514", None)
                setattr(value, "XSDTypeDefinition514", self)

    @property
    def model_xsd_XSDFeature(self):
        return self.__model_xsd_XSDFeature

    @model_xsd_XSDFeature.setter
    def model_xsd_XSDFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDFeature__model_xsd_XSDFeature", None)
        self.__model_xsd_XSDFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDScope"):
                opp_val = getattr(old_value, "XSDScope", None)
                if opp_val == self:
                    setattr(old_value, "XSDScope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDScope"):
                opp_val = getattr(value, "XSDScope", None)
                setattr(value, "XSDScope", self)

class XSDRepeatableFacet:

    pass
class model_xsd_XSDPatternFacet(XSDRepeatableFacet):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_xsd_XSDEnumerationFacet(XSDRepeatableFacet):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class XSDIdentityConstraintDefinition:

    pass
class XSDFacet:

    pass
class model_xsd_XSDFundamentalFacet(XSDFacet):

    pass
class model_xsd_XSDConstrainingFacet(XSDFacet):

    pass
class XSDDiagnostic:

    pass
class model_xsd_XSDConcreteComponent(ABC):

    def __init__(self, element: str, model_xsd_XSDConcreteComponent: "XSDConcreteComponent" = None, model_xsd_XSDConcreteComponent473: "XSDConcreteComponent" = None, model_xsd_XSDConcreteComponent476: "XSDSchema" = None, model_xsd_XSDConcreteComponent479: set["XSDDiagnostic"] = None):
        self.element = element
        self.model_xsd_XSDConcreteComponent = model_xsd_XSDConcreteComponent
        self.model_xsd_XSDConcreteComponent473 = model_xsd_XSDConcreteComponent473
        self.model_xsd_XSDConcreteComponent476 = model_xsd_XSDConcreteComponent476
        self.model_xsd_XSDConcreteComponent479 = model_xsd_XSDConcreteComponent479 if model_xsd_XSDConcreteComponent479 is not None else set()
        
    @property
    def element(self) -> str:
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element

    @property
    def model_xsd_XSDConcreteComponent479(self):
        return self.__model_xsd_XSDConcreteComponent479

    @model_xsd_XSDConcreteComponent479.setter
    def model_xsd_XSDConcreteComponent479(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDConcreteComponent__model_xsd_XSDConcreteComponent479", None)
        self.__model_xsd_XSDConcreteComponent479 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDDiagnostic"):
                    opp_val = getattr(item, "XSDDiagnostic", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDDiagnostic", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDDiagnostic"):
                    opp_val = getattr(item, "XSDDiagnostic", None)
                    
                    setattr(item, "XSDDiagnostic", self)
                    

    @property
    def model_xsd_XSDConcreteComponent(self):
        return self.__model_xsd_XSDConcreteComponent

    @model_xsd_XSDConcreteComponent.setter
    def model_xsd_XSDConcreteComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDConcreteComponent__model_xsd_XSDConcreteComponent", None)
        self.__model_xsd_XSDConcreteComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDConcreteComponent"):
                opp_val = getattr(old_value, "XSDConcreteComponent", None)
                if opp_val == self:
                    setattr(old_value, "XSDConcreteComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDConcreteComponent"):
                opp_val = getattr(value, "XSDConcreteComponent", None)
                setattr(value, "XSDConcreteComponent", self)

    @property
    def model_xsd_XSDConcreteComponent476(self):
        return self.__model_xsd_XSDConcreteComponent476

    @model_xsd_XSDConcreteComponent476.setter
    def model_xsd_XSDConcreteComponent476(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDConcreteComponent__model_xsd_XSDConcreteComponent476", None)
        self.__model_xsd_XSDConcreteComponent476 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSchema477"):
                opp_val = getattr(old_value, "XSDSchema477", None)
                if opp_val == self:
                    setattr(old_value, "XSDSchema477", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSchema477"):
                opp_val = getattr(value, "XSDSchema477", None)
                setattr(value, "XSDSchema477", self)

    @property
    def model_xsd_XSDConcreteComponent473(self):
        return self.__model_xsd_XSDConcreteComponent473

    @model_xsd_XSDConcreteComponent473.setter
    def model_xsd_XSDConcreteComponent473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDConcreteComponent__model_xsd_XSDConcreteComponent473", None)
        self.__model_xsd_XSDConcreteComponent473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDConcreteComponent474"):
                opp_val = getattr(old_value, "XSDConcreteComponent474", None)
                if opp_val == self:
                    setattr(old_value, "XSDConcreteComponent474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDConcreteComponent474"):
                opp_val = getattr(value, "XSDConcreteComponent474", None)
                setattr(value, "XSDConcreteComponent474", self)

class xsd_XSDTerm:

    pass
class XSDComplexTypeContent:

    pass
class model_xsd_XSDParticle(XSDComplexTypeContent):

    def __init__(self, minOccurs: int, maxOccurs: int, model_xsd_XSDParticle: "XSDParticleContent" = None, model_xsd_XSDParticle547: "XSDTerm" = None, XSDComplexTypeContent: "model_xsd_XSDComplexTypeDefinition", XSDComplexTypeContent450: "model_xsd_XSDComplexTypeDefinition"):
        self.minOccurs = minOccurs
        self.maxOccurs = maxOccurs
        self.model_xsd_XSDParticle = model_xsd_XSDParticle
        self.model_xsd_XSDParticle547 = model_xsd_XSDParticle547
        
    @property
    def maxOccurs(self) -> int:
        return self.__maxOccurs

    @maxOccurs.setter
    def maxOccurs(self, maxOccurs: int):
        self.__maxOccurs = maxOccurs

    @property
    def minOccurs(self) -> int:
        return self.__minOccurs

    @minOccurs.setter
    def minOccurs(self, minOccurs: int):
        self.__minOccurs = minOccurs

    @property
    def model_xsd_XSDParticle547(self):
        return self.__model_xsd_XSDParticle547

    @model_xsd_XSDParticle547.setter
    def model_xsd_XSDParticle547(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDParticle__model_xsd_XSDParticle547", None)
        self.__model_xsd_XSDParticle547 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTerm"):
                opp_val = getattr(old_value, "XSDTerm", None)
                if opp_val == self:
                    setattr(old_value, "XSDTerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTerm"):
                opp_val = getattr(value, "XSDTerm", None)
                setattr(value, "XSDTerm", self)

    @property
    def model_xsd_XSDParticle(self):
        return self.__model_xsd_XSDParticle

    @model_xsd_XSDParticle.setter
    def model_xsd_XSDParticle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDParticle__model_xsd_XSDParticle", None)
        self.__model_xsd_XSDParticle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDParticleContent"):
                opp_val = getattr(old_value, "XSDParticleContent", None)
                if opp_val == self:
                    setattr(old_value, "XSDParticleContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDParticleContent"):
                opp_val = getattr(value, "XSDParticleContent", None)
                setattr(value, "XSDParticleContent", self)

class xsd_XSDScope:

    pass
class XSDParticle:

    pass
class XSDAttributeGroupDefinition:

    pass
class XSDWildcard:

    pass
class XSDAttributeUse:

    pass
class XSDAttributeGroupContent:

    pass
class xsd_XSDAttributeGroupContent:

    pass
class xsd_XSDRedefinableComponent:

    pass
class XSDConcreteComponent:

    pass
class model_xsd_XSDDiagnostic(XSDConcreteComponent):

    def __init__(self, severity: str, message: str, locationURI: str, line: int, column: int, node: str, annotationURI: str, key: str, substitutions: str, model_xsd_XSDDiagnostic: set["XSDConcreteComponent"] = None, model_xsd_XSDDiagnostic483: "XSDConcreteComponent" = None, XSDConcreteComponent474: "model_xsd_XSDConcreteComponent", XSDConcreteComponent: "model_xsd_XSDConcreteComponent", XSDConcreteComponent481: "model_xsd_XSDDiagnostic", XSDConcreteComponent484: "model_xsd_XSDDiagnostic"):
        self.severity = severity
        self.message = message
        self.locationURI = locationURI
        self.line = line
        self.column = column
        self.node = node
        self.annotationURI = annotationURI
        self.key = key
        self.substitutions = substitutions
        self.model_xsd_XSDDiagnostic = model_xsd_XSDDiagnostic if model_xsd_XSDDiagnostic is not None else set()
        self.model_xsd_XSDDiagnostic483 = model_xsd_XSDDiagnostic483
        
    @property
    def line(self) -> int:
        return self.__line

    @line.setter
    def line(self, line: int):
        self.__line = line

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def column(self) -> int:
        return self.__column

    @column.setter
    def column(self, column: int):
        self.__column = column

    @property
    def annotationURI(self) -> str:
        return self.__annotationURI

    @annotationURI.setter
    def annotationURI(self, annotationURI: str):
        self.__annotationURI = annotationURI

    @property
    def locationURI(self) -> str:
        return self.__locationURI

    @locationURI.setter
    def locationURI(self, locationURI: str):
        self.__locationURI = locationURI

    @property
    def substitutions(self) -> str:
        return self.__substitutions

    @substitutions.setter
    def substitutions(self, substitutions: str):
        self.__substitutions = substitutions

    @property
    def node(self) -> str:
        return self.__node

    @node.setter
    def node(self, node: str):
        self.__node = node

    @property
    def model_xsd_XSDDiagnostic(self):
        return self.__model_xsd_XSDDiagnostic

    @model_xsd_XSDDiagnostic.setter
    def model_xsd_XSDDiagnostic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDDiagnostic__model_xsd_XSDDiagnostic", None)
        self.__model_xsd_XSDDiagnostic = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDConcreteComponent481"):
                    opp_val = getattr(item, "XSDConcreteComponent481", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDConcreteComponent481", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDConcreteComponent481"):
                    opp_val = getattr(item, "XSDConcreteComponent481", None)
                    
                    setattr(item, "XSDConcreteComponent481", self)
                    

    @property
    def model_xsd_XSDDiagnostic483(self):
        return self.__model_xsd_XSDDiagnostic483

    @model_xsd_XSDDiagnostic483.setter
    def model_xsd_XSDDiagnostic483(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDDiagnostic__model_xsd_XSDDiagnostic483", None)
        self.__model_xsd_XSDDiagnostic483 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDConcreteComponent484"):
                opp_val = getattr(old_value, "XSDConcreteComponent484", None)
                if opp_val == self:
                    setattr(old_value, "XSDConcreteComponent484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDConcreteComponent484"):
                opp_val = getattr(value, "XSDConcreteComponent484", None)
                setattr(value, "XSDConcreteComponent484", self)

class model_xsd_XSDParticleContent(XSDConcreteComponent):

    pass
class model_xsd_XSDComponent(XSDConcreteComponent):

    pass
class model_xsd_XSDSchemaContent(XSDConcreteComponent):

    pass
class model_xsd_XSDAttributeGroupContent(XSDConcreteComponent):

    pass
class xsd_XSDTypeDefinition:

    pass
class model_xsd_XSDSimpleTypeDefinition(xsd_XSDTypeDefinition, xsd_XSDComplexTypeContent):

    def __init__(self, variety: str, final: str, lexicalFinal: str, validFacets: str, model_xsd_XSDSimpleTypeDefinition610: set["XSDFundamentalFacet"] = None, model_xsd_XSDSimpleTypeDefinition612: "XSDSimpleTypeDefinition" = None, model_xsd_XSDSimpleTypeDefinition615: "XSDSimpleTypeDefinition" = None, model_xsd_XSDSimpleTypeDefinition: set["XSDSimpleTypeDefinition"] = None, model_xsd_XSDSimpleTypeDefinition602: set["XSDConstrainingFacet"] = None, model_xsd_XSDSimpleTypeDefinition604: set["XSDConstrainingFacet"] = None, model_xsd_XSDSimpleTypeDefinition607: set["XSDSimpleTypeDefinition"] = None, model_xsd_XSDSimpleTypeDefinition642: set["XSDPatternFacet"] = None, model_xsd_XSDSimpleTypeDefinition644: "XSDCardinalityFacet" = None, model_xsd_XSDSimpleTypeDefinition618: "XSDSimpleTypeDefinition" = None, model_xsd_XSDSimpleTypeDefinition621: "XSDSimpleTypeDefinition" = None, model_xsd_XSDSimpleTypeDefinition624: "XSDMinFacet" = None, model_xsd_XSDSimpleTypeDefinition626: "XSDMaxFacet" = None, model_xsd_XSDSimpleTypeDefinition628: "XSDMaxInclusiveFacet" = None, model_xsd_XSDSimpleTypeDefinition630: "XSDMinInclusiveFacet" = None, model_xsd_XSDSimpleTypeDefinition632: "XSDMinExclusiveFacet" = None, model_xsd_XSDSimpleTypeDefinition634: "XSDMaxExclusiveFacet" = None, model_xsd_XSDSimpleTypeDefinition636: "XSDLengthFacet" = None, model_xsd_XSDSimpleTypeDefinition638: "XSDWhiteSpaceFacet" = None, model_xsd_XSDSimpleTypeDefinition640: set["XSDEnumerationFacet"] = None, model_xsd_XSDSimpleTypeDefinition672: "XSDPatternFacet" = None, model_xsd_XSDSimpleTypeDefinition675: "XSDEnumerationFacet" = None, model_xsd_XSDSimpleTypeDefinition646: "XSDNumericFacet" = None, model_xsd_XSDSimpleTypeDefinition648: "XSDMaxLengthFacet" = None, model_xsd_XSDSimpleTypeDefinition650: "XSDMinLengthFacet" = None, model_xsd_XSDSimpleTypeDefinition652: "XSDTotalDigitsFacet" = None, model_xsd_XSDSimpleTypeDefinition654: "XSDFractionDigitsFacet" = None, model_xsd_XSDSimpleTypeDefinition656: "XSDOrderedFacet" = None, model_xsd_XSDSimpleTypeDefinition658: "XSDBoundedFacet" = None, model_xsd_XSDSimpleTypeDefinition660: "XSDMaxFacet" = None, model_xsd_XSDSimpleTypeDefinition663: "XSDWhiteSpaceFacet" = None, model_xsd_XSDSimpleTypeDefinition666: "XSDMaxLengthFacet" = None, model_xsd_XSDSimpleTypeDefinition669: "XSDFractionDigitsFacet" = None, model_xsd_XSDSimpleTypeDefinition678: "XSDTotalDigitsFacet" = None, model_xsd_XSDSimpleTypeDefinition681: "XSDMinLengthFacet" = None, model_xsd_XSDSimpleTypeDefinition684: "XSDLengthFacet" = None, model_xsd_XSDSimpleTypeDefinition687: "XSDMinFacet" = None, model_xsd_XSDSimpleTypeDefinition690: set["XSDFacet"] = None):
        self.variety = variety
        self.final = final
        self.lexicalFinal = lexicalFinal
        self.validFacets = validFacets
        self.model_xsd_XSDSimpleTypeDefinition610 = model_xsd_XSDSimpleTypeDefinition610 if model_xsd_XSDSimpleTypeDefinition610 is not None else set()
        self.model_xsd_XSDSimpleTypeDefinition612 = model_xsd_XSDSimpleTypeDefinition612
        self.model_xsd_XSDSimpleTypeDefinition615 = model_xsd_XSDSimpleTypeDefinition615
        self.model_xsd_XSDSimpleTypeDefinition = model_xsd_XSDSimpleTypeDefinition if model_xsd_XSDSimpleTypeDefinition is not None else set()
        self.model_xsd_XSDSimpleTypeDefinition602 = model_xsd_XSDSimpleTypeDefinition602 if model_xsd_XSDSimpleTypeDefinition602 is not None else set()
        self.model_xsd_XSDSimpleTypeDefinition604 = model_xsd_XSDSimpleTypeDefinition604 if model_xsd_XSDSimpleTypeDefinition604 is not None else set()
        self.model_xsd_XSDSimpleTypeDefinition607 = model_xsd_XSDSimpleTypeDefinition607 if model_xsd_XSDSimpleTypeDefinition607 is not None else set()
        self.model_xsd_XSDSimpleTypeDefinition642 = model_xsd_XSDSimpleTypeDefinition642 if model_xsd_XSDSimpleTypeDefinition642 is not None else set()
        self.model_xsd_XSDSimpleTypeDefinition644 = model_xsd_XSDSimpleTypeDefinition644
        self.model_xsd_XSDSimpleTypeDefinition618 = model_xsd_XSDSimpleTypeDefinition618
        self.model_xsd_XSDSimpleTypeDefinition621 = model_xsd_XSDSimpleTypeDefinition621
        self.model_xsd_XSDSimpleTypeDefinition624 = model_xsd_XSDSimpleTypeDefinition624
        self.model_xsd_XSDSimpleTypeDefinition626 = model_xsd_XSDSimpleTypeDefinition626
        self.model_xsd_XSDSimpleTypeDefinition628 = model_xsd_XSDSimpleTypeDefinition628
        self.model_xsd_XSDSimpleTypeDefinition630 = model_xsd_XSDSimpleTypeDefinition630
        self.model_xsd_XSDSimpleTypeDefinition632 = model_xsd_XSDSimpleTypeDefinition632
        self.model_xsd_XSDSimpleTypeDefinition634 = model_xsd_XSDSimpleTypeDefinition634
        self.model_xsd_XSDSimpleTypeDefinition636 = model_xsd_XSDSimpleTypeDefinition636
        self.model_xsd_XSDSimpleTypeDefinition638 = model_xsd_XSDSimpleTypeDefinition638
        self.model_xsd_XSDSimpleTypeDefinition640 = model_xsd_XSDSimpleTypeDefinition640 if model_xsd_XSDSimpleTypeDefinition640 is not None else set()
        self.model_xsd_XSDSimpleTypeDefinition672 = model_xsd_XSDSimpleTypeDefinition672
        self.model_xsd_XSDSimpleTypeDefinition675 = model_xsd_XSDSimpleTypeDefinition675
        self.model_xsd_XSDSimpleTypeDefinition646 = model_xsd_XSDSimpleTypeDefinition646
        self.model_xsd_XSDSimpleTypeDefinition648 = model_xsd_XSDSimpleTypeDefinition648
        self.model_xsd_XSDSimpleTypeDefinition650 = model_xsd_XSDSimpleTypeDefinition650
        self.model_xsd_XSDSimpleTypeDefinition652 = model_xsd_XSDSimpleTypeDefinition652
        self.model_xsd_XSDSimpleTypeDefinition654 = model_xsd_XSDSimpleTypeDefinition654
        self.model_xsd_XSDSimpleTypeDefinition656 = model_xsd_XSDSimpleTypeDefinition656
        self.model_xsd_XSDSimpleTypeDefinition658 = model_xsd_XSDSimpleTypeDefinition658
        self.model_xsd_XSDSimpleTypeDefinition660 = model_xsd_XSDSimpleTypeDefinition660
        self.model_xsd_XSDSimpleTypeDefinition663 = model_xsd_XSDSimpleTypeDefinition663
        self.model_xsd_XSDSimpleTypeDefinition666 = model_xsd_XSDSimpleTypeDefinition666
        self.model_xsd_XSDSimpleTypeDefinition669 = model_xsd_XSDSimpleTypeDefinition669
        self.model_xsd_XSDSimpleTypeDefinition678 = model_xsd_XSDSimpleTypeDefinition678
        self.model_xsd_XSDSimpleTypeDefinition681 = model_xsd_XSDSimpleTypeDefinition681
        self.model_xsd_XSDSimpleTypeDefinition684 = model_xsd_XSDSimpleTypeDefinition684
        self.model_xsd_XSDSimpleTypeDefinition687 = model_xsd_XSDSimpleTypeDefinition687
        self.model_xsd_XSDSimpleTypeDefinition690 = model_xsd_XSDSimpleTypeDefinition690 if model_xsd_XSDSimpleTypeDefinition690 is not None else set()
        
    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def variety(self) -> str:
        return self.__variety

    @variety.setter
    def variety(self, variety: str):
        self.__variety = variety

    @property
    def validFacets(self) -> str:
        return self.__validFacets

    @validFacets.setter
    def validFacets(self, validFacets: str):
        self.__validFacets = validFacets

    @property
    def lexicalFinal(self) -> str:
        return self.__lexicalFinal

    @lexicalFinal.setter
    def lexicalFinal(self, lexicalFinal: str):
        self.__lexicalFinal = lexicalFinal

    @property
    def model_xsd_XSDSimpleTypeDefinition630(self):
        return self.__model_xsd_XSDSimpleTypeDefinition630

    @model_xsd_XSDSimpleTypeDefinition630.setter
    def model_xsd_XSDSimpleTypeDefinition630(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition630", None)
        self.__model_xsd_XSDSimpleTypeDefinition630 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMinInclusiveFacet"):
                opp_val = getattr(old_value, "XSDMinInclusiveFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDMinInclusiveFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMinInclusiveFacet"):
                opp_val = getattr(value, "XSDMinInclusiveFacet", None)
                setattr(value, "XSDMinInclusiveFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition607(self):
        return self.__model_xsd_XSDSimpleTypeDefinition607

    @model_xsd_XSDSimpleTypeDefinition607.setter
    def model_xsd_XSDSimpleTypeDefinition607(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition607", None)
        self.__model_xsd_XSDSimpleTypeDefinition607 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDSimpleTypeDefinition608"):
                    opp_val = getattr(item, "XSDSimpleTypeDefinition608", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDSimpleTypeDefinition608", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDSimpleTypeDefinition608"):
                    opp_val = getattr(item, "XSDSimpleTypeDefinition608", None)
                    
                    setattr(item, "XSDSimpleTypeDefinition608", self)
                    

    @property
    def model_xsd_XSDSimpleTypeDefinition675(self):
        return self.__model_xsd_XSDSimpleTypeDefinition675

    @model_xsd_XSDSimpleTypeDefinition675.setter
    def model_xsd_XSDSimpleTypeDefinition675(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition675", None)
        self.__model_xsd_XSDSimpleTypeDefinition675 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDEnumerationFacet676"):
                opp_val = getattr(old_value, "XSDEnumerationFacet676", None)
                if opp_val == self:
                    setattr(old_value, "XSDEnumerationFacet676", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDEnumerationFacet676"):
                opp_val = getattr(value, "XSDEnumerationFacet676", None)
                setattr(value, "XSDEnumerationFacet676", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition658(self):
        return self.__model_xsd_XSDSimpleTypeDefinition658

    @model_xsd_XSDSimpleTypeDefinition658.setter
    def model_xsd_XSDSimpleTypeDefinition658(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition658", None)
        self.__model_xsd_XSDSimpleTypeDefinition658 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDBoundedFacet"):
                opp_val = getattr(old_value, "XSDBoundedFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDBoundedFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDBoundedFacet"):
                opp_val = getattr(value, "XSDBoundedFacet", None)
                setattr(value, "XSDBoundedFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition666(self):
        return self.__model_xsd_XSDSimpleTypeDefinition666

    @model_xsd_XSDSimpleTypeDefinition666.setter
    def model_xsd_XSDSimpleTypeDefinition666(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition666", None)
        self.__model_xsd_XSDSimpleTypeDefinition666 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMaxLengthFacet667"):
                opp_val = getattr(old_value, "XSDMaxLengthFacet667", None)
                if opp_val == self:
                    setattr(old_value, "XSDMaxLengthFacet667", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMaxLengthFacet667"):
                opp_val = getattr(value, "XSDMaxLengthFacet667", None)
                setattr(value, "XSDMaxLengthFacet667", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition648(self):
        return self.__model_xsd_XSDSimpleTypeDefinition648

    @model_xsd_XSDSimpleTypeDefinition648.setter
    def model_xsd_XSDSimpleTypeDefinition648(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition648", None)
        self.__model_xsd_XSDSimpleTypeDefinition648 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMaxLengthFacet"):
                opp_val = getattr(old_value, "XSDMaxLengthFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDMaxLengthFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMaxLengthFacet"):
                opp_val = getattr(value, "XSDMaxLengthFacet", None)
                setattr(value, "XSDMaxLengthFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition602(self):
        return self.__model_xsd_XSDSimpleTypeDefinition602

    @model_xsd_XSDSimpleTypeDefinition602.setter
    def model_xsd_XSDSimpleTypeDefinition602(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition602", None)
        self.__model_xsd_XSDSimpleTypeDefinition602 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDConstrainingFacet"):
                    opp_val = getattr(item, "XSDConstrainingFacet", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDConstrainingFacet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDConstrainingFacet"):
                    opp_val = getattr(item, "XSDConstrainingFacet", None)
                    
                    setattr(item, "XSDConstrainingFacet", self)
                    

    @property
    def model_xsd_XSDSimpleTypeDefinition604(self):
        return self.__model_xsd_XSDSimpleTypeDefinition604

    @model_xsd_XSDSimpleTypeDefinition604.setter
    def model_xsd_XSDSimpleTypeDefinition604(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition604", None)
        self.__model_xsd_XSDSimpleTypeDefinition604 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDConstrainingFacet605"):
                    opp_val = getattr(item, "XSDConstrainingFacet605", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDConstrainingFacet605", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDConstrainingFacet605"):
                    opp_val = getattr(item, "XSDConstrainingFacet605", None)
                    
                    setattr(item, "XSDConstrainingFacet605", self)
                    

    @property
    def model_xsd_XSDSimpleTypeDefinition656(self):
        return self.__model_xsd_XSDSimpleTypeDefinition656

    @model_xsd_XSDSimpleTypeDefinition656.setter
    def model_xsd_XSDSimpleTypeDefinition656(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition656", None)
        self.__model_xsd_XSDSimpleTypeDefinition656 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDOrderedFacet"):
                opp_val = getattr(old_value, "XSDOrderedFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDOrderedFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDOrderedFacet"):
                opp_val = getattr(value, "XSDOrderedFacet", None)
                setattr(value, "XSDOrderedFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition678(self):
        return self.__model_xsd_XSDSimpleTypeDefinition678

    @model_xsd_XSDSimpleTypeDefinition678.setter
    def model_xsd_XSDSimpleTypeDefinition678(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition678", None)
        self.__model_xsd_XSDSimpleTypeDefinition678 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTotalDigitsFacet679"):
                opp_val = getattr(old_value, "XSDTotalDigitsFacet679", None)
                if opp_val == self:
                    setattr(old_value, "XSDTotalDigitsFacet679", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTotalDigitsFacet679"):
                opp_val = getattr(value, "XSDTotalDigitsFacet679", None)
                setattr(value, "XSDTotalDigitsFacet679", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition650(self):
        return self.__model_xsd_XSDSimpleTypeDefinition650

    @model_xsd_XSDSimpleTypeDefinition650.setter
    def model_xsd_XSDSimpleTypeDefinition650(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition650", None)
        self.__model_xsd_XSDSimpleTypeDefinition650 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMinLengthFacet"):
                opp_val = getattr(old_value, "XSDMinLengthFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDMinLengthFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMinLengthFacet"):
                opp_val = getattr(value, "XSDMinLengthFacet", None)
                setattr(value, "XSDMinLengthFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition636(self):
        return self.__model_xsd_XSDSimpleTypeDefinition636

    @model_xsd_XSDSimpleTypeDefinition636.setter
    def model_xsd_XSDSimpleTypeDefinition636(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition636", None)
        self.__model_xsd_XSDSimpleTypeDefinition636 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDLengthFacet"):
                opp_val = getattr(old_value, "XSDLengthFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDLengthFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDLengthFacet"):
                opp_val = getattr(value, "XSDLengthFacet", None)
                setattr(value, "XSDLengthFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition669(self):
        return self.__model_xsd_XSDSimpleTypeDefinition669

    @model_xsd_XSDSimpleTypeDefinition669.setter
    def model_xsd_XSDSimpleTypeDefinition669(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition669", None)
        self.__model_xsd_XSDSimpleTypeDefinition669 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDFractionDigitsFacet670"):
                opp_val = getattr(old_value, "XSDFractionDigitsFacet670", None)
                if opp_val == self:
                    setattr(old_value, "XSDFractionDigitsFacet670", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDFractionDigitsFacet670"):
                opp_val = getattr(value, "XSDFractionDigitsFacet670", None)
                setattr(value, "XSDFractionDigitsFacet670", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition660(self):
        return self.__model_xsd_XSDSimpleTypeDefinition660

    @model_xsd_XSDSimpleTypeDefinition660.setter
    def model_xsd_XSDSimpleTypeDefinition660(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition660", None)
        self.__model_xsd_XSDSimpleTypeDefinition660 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMaxFacet661"):
                opp_val = getattr(old_value, "XSDMaxFacet661", None)
                if opp_val == self:
                    setattr(old_value, "XSDMaxFacet661", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMaxFacet661"):
                opp_val = getattr(value, "XSDMaxFacet661", None)
                setattr(value, "XSDMaxFacet661", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition612(self):
        return self.__model_xsd_XSDSimpleTypeDefinition612

    @model_xsd_XSDSimpleTypeDefinition612.setter
    def model_xsd_XSDSimpleTypeDefinition612(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition612", None)
        self.__model_xsd_XSDSimpleTypeDefinition612 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSimpleTypeDefinition613"):
                opp_val = getattr(old_value, "XSDSimpleTypeDefinition613", None)
                if opp_val == self:
                    setattr(old_value, "XSDSimpleTypeDefinition613", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSimpleTypeDefinition613"):
                opp_val = getattr(value, "XSDSimpleTypeDefinition613", None)
                setattr(value, "XSDSimpleTypeDefinition613", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition618(self):
        return self.__model_xsd_XSDSimpleTypeDefinition618

    @model_xsd_XSDSimpleTypeDefinition618.setter
    def model_xsd_XSDSimpleTypeDefinition618(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition618", None)
        self.__model_xsd_XSDSimpleTypeDefinition618 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSimpleTypeDefinition619"):
                opp_val = getattr(old_value, "XSDSimpleTypeDefinition619", None)
                if opp_val == self:
                    setattr(old_value, "XSDSimpleTypeDefinition619", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSimpleTypeDefinition619"):
                opp_val = getattr(value, "XSDSimpleTypeDefinition619", None)
                setattr(value, "XSDSimpleTypeDefinition619", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition684(self):
        return self.__model_xsd_XSDSimpleTypeDefinition684

    @model_xsd_XSDSimpleTypeDefinition684.setter
    def model_xsd_XSDSimpleTypeDefinition684(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition684", None)
        self.__model_xsd_XSDSimpleTypeDefinition684 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDLengthFacet685"):
                opp_val = getattr(old_value, "XSDLengthFacet685", None)
                if opp_val == self:
                    setattr(old_value, "XSDLengthFacet685", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDLengthFacet685"):
                opp_val = getattr(value, "XSDLengthFacet685", None)
                setattr(value, "XSDLengthFacet685", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition640(self):
        return self.__model_xsd_XSDSimpleTypeDefinition640

    @model_xsd_XSDSimpleTypeDefinition640.setter
    def model_xsd_XSDSimpleTypeDefinition640(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition640", None)
        self.__model_xsd_XSDSimpleTypeDefinition640 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDEnumerationFacet"):
                    opp_val = getattr(item, "XSDEnumerationFacet", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDEnumerationFacet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDEnumerationFacet"):
                    opp_val = getattr(item, "XSDEnumerationFacet", None)
                    
                    setattr(item, "XSDEnumerationFacet", self)
                    

    @property
    def model_xsd_XSDSimpleTypeDefinition632(self):
        return self.__model_xsd_XSDSimpleTypeDefinition632

    @model_xsd_XSDSimpleTypeDefinition632.setter
    def model_xsd_XSDSimpleTypeDefinition632(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition632", None)
        self.__model_xsd_XSDSimpleTypeDefinition632 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMinExclusiveFacet"):
                opp_val = getattr(old_value, "XSDMinExclusiveFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDMinExclusiveFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMinExclusiveFacet"):
                opp_val = getattr(value, "XSDMinExclusiveFacet", None)
                setattr(value, "XSDMinExclusiveFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition610(self):
        return self.__model_xsd_XSDSimpleTypeDefinition610

    @model_xsd_XSDSimpleTypeDefinition610.setter
    def model_xsd_XSDSimpleTypeDefinition610(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition610", None)
        self.__model_xsd_XSDSimpleTypeDefinition610 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDFundamentalFacet"):
                    opp_val = getattr(item, "XSDFundamentalFacet", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDFundamentalFacet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDFundamentalFacet"):
                    opp_val = getattr(item, "XSDFundamentalFacet", None)
                    
                    setattr(item, "XSDFundamentalFacet", self)
                    

    @property
    def model_xsd_XSDSimpleTypeDefinition642(self):
        return self.__model_xsd_XSDSimpleTypeDefinition642

    @model_xsd_XSDSimpleTypeDefinition642.setter
    def model_xsd_XSDSimpleTypeDefinition642(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition642", None)
        self.__model_xsd_XSDSimpleTypeDefinition642 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDPatternFacet"):
                    opp_val = getattr(item, "XSDPatternFacet", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDPatternFacet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDPatternFacet"):
                    opp_val = getattr(item, "XSDPatternFacet", None)
                    
                    setattr(item, "XSDPatternFacet", self)
                    

    @property
    def model_xsd_XSDSimpleTypeDefinition621(self):
        return self.__model_xsd_XSDSimpleTypeDefinition621

    @model_xsd_XSDSimpleTypeDefinition621.setter
    def model_xsd_XSDSimpleTypeDefinition621(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition621", None)
        self.__model_xsd_XSDSimpleTypeDefinition621 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSimpleTypeDefinition622"):
                opp_val = getattr(old_value, "XSDSimpleTypeDefinition622", None)
                if opp_val == self:
                    setattr(old_value, "XSDSimpleTypeDefinition622", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSimpleTypeDefinition622"):
                opp_val = getattr(value, "XSDSimpleTypeDefinition622", None)
                setattr(value, "XSDSimpleTypeDefinition622", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition(self):
        return self.__model_xsd_XSDSimpleTypeDefinition

    @model_xsd_XSDSimpleTypeDefinition.setter
    def model_xsd_XSDSimpleTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition", None)
        self.__model_xsd_XSDSimpleTypeDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDSimpleTypeDefinition600"):
                    opp_val = getattr(item, "XSDSimpleTypeDefinition600", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDSimpleTypeDefinition600", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDSimpleTypeDefinition600"):
                    opp_val = getattr(item, "XSDSimpleTypeDefinition600", None)
                    
                    setattr(item, "XSDSimpleTypeDefinition600", self)
                    

    @property
    def model_xsd_XSDSimpleTypeDefinition634(self):
        return self.__model_xsd_XSDSimpleTypeDefinition634

    @model_xsd_XSDSimpleTypeDefinition634.setter
    def model_xsd_XSDSimpleTypeDefinition634(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition634", None)
        self.__model_xsd_XSDSimpleTypeDefinition634 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMaxExclusiveFacet"):
                opp_val = getattr(old_value, "XSDMaxExclusiveFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDMaxExclusiveFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMaxExclusiveFacet"):
                opp_val = getattr(value, "XSDMaxExclusiveFacet", None)
                setattr(value, "XSDMaxExclusiveFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition638(self):
        return self.__model_xsd_XSDSimpleTypeDefinition638

    @model_xsd_XSDSimpleTypeDefinition638.setter
    def model_xsd_XSDSimpleTypeDefinition638(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition638", None)
        self.__model_xsd_XSDSimpleTypeDefinition638 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDWhiteSpaceFacet"):
                opp_val = getattr(old_value, "XSDWhiteSpaceFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDWhiteSpaceFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDWhiteSpaceFacet"):
                opp_val = getattr(value, "XSDWhiteSpaceFacet", None)
                setattr(value, "XSDWhiteSpaceFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition663(self):
        return self.__model_xsd_XSDSimpleTypeDefinition663

    @model_xsd_XSDSimpleTypeDefinition663.setter
    def model_xsd_XSDSimpleTypeDefinition663(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition663", None)
        self.__model_xsd_XSDSimpleTypeDefinition663 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDWhiteSpaceFacet664"):
                opp_val = getattr(old_value, "XSDWhiteSpaceFacet664", None)
                if opp_val == self:
                    setattr(old_value, "XSDWhiteSpaceFacet664", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDWhiteSpaceFacet664"):
                opp_val = getattr(value, "XSDWhiteSpaceFacet664", None)
                setattr(value, "XSDWhiteSpaceFacet664", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition624(self):
        return self.__model_xsd_XSDSimpleTypeDefinition624

    @model_xsd_XSDSimpleTypeDefinition624.setter
    def model_xsd_XSDSimpleTypeDefinition624(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition624", None)
        self.__model_xsd_XSDSimpleTypeDefinition624 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMinFacet"):
                opp_val = getattr(old_value, "XSDMinFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDMinFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMinFacet"):
                opp_val = getattr(value, "XSDMinFacet", None)
                setattr(value, "XSDMinFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition628(self):
        return self.__model_xsd_XSDSimpleTypeDefinition628

    @model_xsd_XSDSimpleTypeDefinition628.setter
    def model_xsd_XSDSimpleTypeDefinition628(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition628", None)
        self.__model_xsd_XSDSimpleTypeDefinition628 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMaxInclusiveFacet"):
                opp_val = getattr(old_value, "XSDMaxInclusiveFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDMaxInclusiveFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMaxInclusiveFacet"):
                opp_val = getattr(value, "XSDMaxInclusiveFacet", None)
                setattr(value, "XSDMaxInclusiveFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition646(self):
        return self.__model_xsd_XSDSimpleTypeDefinition646

    @model_xsd_XSDSimpleTypeDefinition646.setter
    def model_xsd_XSDSimpleTypeDefinition646(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition646", None)
        self.__model_xsd_XSDSimpleTypeDefinition646 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDNumericFacet"):
                opp_val = getattr(old_value, "XSDNumericFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDNumericFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDNumericFacet"):
                opp_val = getattr(value, "XSDNumericFacet", None)
                setattr(value, "XSDNumericFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition690(self):
        return self.__model_xsd_XSDSimpleTypeDefinition690

    @model_xsd_XSDSimpleTypeDefinition690.setter
    def model_xsd_XSDSimpleTypeDefinition690(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition690", None)
        self.__model_xsd_XSDSimpleTypeDefinition690 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDFacet"):
                    opp_val = getattr(item, "XSDFacet", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDFacet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDFacet"):
                    opp_val = getattr(item, "XSDFacet", None)
                    
                    setattr(item, "XSDFacet", self)
                    

    @property
    def model_xsd_XSDSimpleTypeDefinition687(self):
        return self.__model_xsd_XSDSimpleTypeDefinition687

    @model_xsd_XSDSimpleTypeDefinition687.setter
    def model_xsd_XSDSimpleTypeDefinition687(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition687", None)
        self.__model_xsd_XSDSimpleTypeDefinition687 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMinFacet688"):
                opp_val = getattr(old_value, "XSDMinFacet688", None)
                if opp_val == self:
                    setattr(old_value, "XSDMinFacet688", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMinFacet688"):
                opp_val = getattr(value, "XSDMinFacet688", None)
                setattr(value, "XSDMinFacet688", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition626(self):
        return self.__model_xsd_XSDSimpleTypeDefinition626

    @model_xsd_XSDSimpleTypeDefinition626.setter
    def model_xsd_XSDSimpleTypeDefinition626(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition626", None)
        self.__model_xsd_XSDSimpleTypeDefinition626 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMaxFacet"):
                opp_val = getattr(old_value, "XSDMaxFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDMaxFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMaxFacet"):
                opp_val = getattr(value, "XSDMaxFacet", None)
                setattr(value, "XSDMaxFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition644(self):
        return self.__model_xsd_XSDSimpleTypeDefinition644

    @model_xsd_XSDSimpleTypeDefinition644.setter
    def model_xsd_XSDSimpleTypeDefinition644(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition644", None)
        self.__model_xsd_XSDSimpleTypeDefinition644 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDCardinalityFacet"):
                opp_val = getattr(old_value, "XSDCardinalityFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDCardinalityFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDCardinalityFacet"):
                opp_val = getattr(value, "XSDCardinalityFacet", None)
                setattr(value, "XSDCardinalityFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition654(self):
        return self.__model_xsd_XSDSimpleTypeDefinition654

    @model_xsd_XSDSimpleTypeDefinition654.setter
    def model_xsd_XSDSimpleTypeDefinition654(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition654", None)
        self.__model_xsd_XSDSimpleTypeDefinition654 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDFractionDigitsFacet"):
                opp_val = getattr(old_value, "XSDFractionDigitsFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDFractionDigitsFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDFractionDigitsFacet"):
                opp_val = getattr(value, "XSDFractionDigitsFacet", None)
                setattr(value, "XSDFractionDigitsFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition652(self):
        return self.__model_xsd_XSDSimpleTypeDefinition652

    @model_xsd_XSDSimpleTypeDefinition652.setter
    def model_xsd_XSDSimpleTypeDefinition652(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition652", None)
        self.__model_xsd_XSDSimpleTypeDefinition652 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTotalDigitsFacet"):
                opp_val = getattr(old_value, "XSDTotalDigitsFacet", None)
                if opp_val == self:
                    setattr(old_value, "XSDTotalDigitsFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTotalDigitsFacet"):
                opp_val = getattr(value, "XSDTotalDigitsFacet", None)
                setattr(value, "XSDTotalDigitsFacet", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition672(self):
        return self.__model_xsd_XSDSimpleTypeDefinition672

    @model_xsd_XSDSimpleTypeDefinition672.setter
    def model_xsd_XSDSimpleTypeDefinition672(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition672", None)
        self.__model_xsd_XSDSimpleTypeDefinition672 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDPatternFacet673"):
                opp_val = getattr(old_value, "XSDPatternFacet673", None)
                if opp_val == self:
                    setattr(old_value, "XSDPatternFacet673", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDPatternFacet673"):
                opp_val = getattr(value, "XSDPatternFacet673", None)
                setattr(value, "XSDPatternFacet673", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition681(self):
        return self.__model_xsd_XSDSimpleTypeDefinition681

    @model_xsd_XSDSimpleTypeDefinition681.setter
    def model_xsd_XSDSimpleTypeDefinition681(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition681", None)
        self.__model_xsd_XSDSimpleTypeDefinition681 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDMinLengthFacet682"):
                opp_val = getattr(old_value, "XSDMinLengthFacet682", None)
                if opp_val == self:
                    setattr(old_value, "XSDMinLengthFacet682", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDMinLengthFacet682"):
                opp_val = getattr(value, "XSDMinLengthFacet682", None)
                setattr(value, "XSDMinLengthFacet682", self)

    @property
    def model_xsd_XSDSimpleTypeDefinition615(self):
        return self.__model_xsd_XSDSimpleTypeDefinition615

    @model_xsd_XSDSimpleTypeDefinition615.setter
    def model_xsd_XSDSimpleTypeDefinition615(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDSimpleTypeDefinition__model_xsd_XSDSimpleTypeDefinition615", None)
        self.__model_xsd_XSDSimpleTypeDefinition615 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSimpleTypeDefinition616"):
                opp_val = getattr(old_value, "XSDSimpleTypeDefinition616", None)
                if opp_val == self:
                    setattr(old_value, "XSDSimpleTypeDefinition616", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSimpleTypeDefinition616"):
                opp_val = getattr(value, "XSDSimpleTypeDefinition616", None)
                setattr(value, "XSDSimpleTypeDefinition616", self)

class model_xsd_XSDComplexTypeDefinition(xsd_XSDTypeDefinition, xsd_XSDScope):

    def __init__(self, derivationMethod: str, final: str, abstract: bool, contentTypeCategory: str, prohibitedSubstitutions: str, lexicalFinal: str, block: str, mixed: bool, model_xsd_XSDComplexTypeDefinition464: "XSDTypeDefinition" = None, model_xsd_XSDComplexTypeDefinition467: "XSDParticle" = None, model_xsd_XSDComplexTypeDefinition: "XSDAnnotation" = None, model_xsd_XSDComplexTypeDefinition444: "XSDTypeDefinition" = None, model_xsd_XSDComplexTypeDefinition447: "XSDComplexTypeContent" = None, model_xsd_XSDComplexTypeDefinition449: "XSDComplexTypeContent" = None, model_xsd_XSDComplexTypeDefinition452: set["XSDAttributeUse"] = None, model_xsd_XSDComplexTypeDefinition455: set["XSDAttributeGroupContent"] = None, model_xsd_XSDComplexTypeDefinition458: "XSDWildcard" = None, model_xsd_XSDComplexTypeDefinition461: "XSDWildcard" = None, model_xsd_XSDComplexTypeDefinition469: "XSDWildcard" = None):
        self.derivationMethod = derivationMethod
        self.final = final
        self.abstract = abstract
        self.contentTypeCategory = contentTypeCategory
        self.prohibitedSubstitutions = prohibitedSubstitutions
        self.lexicalFinal = lexicalFinal
        self.block = block
        self.mixed = mixed
        self.model_xsd_XSDComplexTypeDefinition464 = model_xsd_XSDComplexTypeDefinition464
        self.model_xsd_XSDComplexTypeDefinition467 = model_xsd_XSDComplexTypeDefinition467
        self.model_xsd_XSDComplexTypeDefinition = model_xsd_XSDComplexTypeDefinition
        self.model_xsd_XSDComplexTypeDefinition444 = model_xsd_XSDComplexTypeDefinition444
        self.model_xsd_XSDComplexTypeDefinition447 = model_xsd_XSDComplexTypeDefinition447
        self.model_xsd_XSDComplexTypeDefinition449 = model_xsd_XSDComplexTypeDefinition449
        self.model_xsd_XSDComplexTypeDefinition452 = model_xsd_XSDComplexTypeDefinition452 if model_xsd_XSDComplexTypeDefinition452 is not None else set()
        self.model_xsd_XSDComplexTypeDefinition455 = model_xsd_XSDComplexTypeDefinition455 if model_xsd_XSDComplexTypeDefinition455 is not None else set()
        self.model_xsd_XSDComplexTypeDefinition458 = model_xsd_XSDComplexTypeDefinition458
        self.model_xsd_XSDComplexTypeDefinition461 = model_xsd_XSDComplexTypeDefinition461
        self.model_xsd_XSDComplexTypeDefinition469 = model_xsd_XSDComplexTypeDefinition469
        
    @property
    def derivationMethod(self) -> str:
        return self.__derivationMethod

    @derivationMethod.setter
    def derivationMethod(self, derivationMethod: str):
        self.__derivationMethod = derivationMethod

    @property
    def contentTypeCategory(self) -> str:
        return self.__contentTypeCategory

    @contentTypeCategory.setter
    def contentTypeCategory(self, contentTypeCategory: str):
        self.__contentTypeCategory = contentTypeCategory

    @property
    def prohibitedSubstitutions(self) -> str:
        return self.__prohibitedSubstitutions

    @prohibitedSubstitutions.setter
    def prohibitedSubstitutions(self, prohibitedSubstitutions: str):
        self.__prohibitedSubstitutions = prohibitedSubstitutions

    @property
    def lexicalFinal(self) -> str:
        return self.__lexicalFinal

    @lexicalFinal.setter
    def lexicalFinal(self, lexicalFinal: str):
        self.__lexicalFinal = lexicalFinal

    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def mixed(self) -> bool:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: bool):
        self.__mixed = mixed

    @property
    def block(self) -> str:
        return self.__block

    @block.setter
    def block(self, block: str):
        self.__block = block

    @property
    def model_xsd_XSDComplexTypeDefinition452(self):
        return self.__model_xsd_XSDComplexTypeDefinition452

    @model_xsd_XSDComplexTypeDefinition452.setter
    def model_xsd_XSDComplexTypeDefinition452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition452", None)
        self.__model_xsd_XSDComplexTypeDefinition452 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDAttributeUse453"):
                    opp_val = getattr(item, "XSDAttributeUse453", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDAttributeUse453", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDAttributeUse453"):
                    opp_val = getattr(item, "XSDAttributeUse453", None)
                    
                    setattr(item, "XSDAttributeUse453", self)
                    

    @property
    def model_xsd_XSDComplexTypeDefinition(self):
        return self.__model_xsd_XSDComplexTypeDefinition

    @model_xsd_XSDComplexTypeDefinition.setter
    def model_xsd_XSDComplexTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition", None)
        self.__model_xsd_XSDComplexTypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation442"):
                opp_val = getattr(old_value, "XSDAnnotation442", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation442"):
                opp_val = getattr(value, "XSDAnnotation442", None)
                setattr(value, "XSDAnnotation442", self)

    @property
    def model_xsd_XSDComplexTypeDefinition469(self):
        return self.__model_xsd_XSDComplexTypeDefinition469

    @model_xsd_XSDComplexTypeDefinition469.setter
    def model_xsd_XSDComplexTypeDefinition469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition469", None)
        self.__model_xsd_XSDComplexTypeDefinition469 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDWildcard470"):
                opp_val = getattr(old_value, "XSDWildcard470", None)
                if opp_val == self:
                    setattr(old_value, "XSDWildcard470", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDWildcard470"):
                opp_val = getattr(value, "XSDWildcard470", None)
                setattr(value, "XSDWildcard470", self)

    @property
    def model_xsd_XSDComplexTypeDefinition455(self):
        return self.__model_xsd_XSDComplexTypeDefinition455

    @model_xsd_XSDComplexTypeDefinition455.setter
    def model_xsd_XSDComplexTypeDefinition455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition455", None)
        self.__model_xsd_XSDComplexTypeDefinition455 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDAttributeGroupContent456"):
                    opp_val = getattr(item, "XSDAttributeGroupContent456", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDAttributeGroupContent456", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDAttributeGroupContent456"):
                    opp_val = getattr(item, "XSDAttributeGroupContent456", None)
                    
                    setattr(item, "XSDAttributeGroupContent456", self)
                    

    @property
    def model_xsd_XSDComplexTypeDefinition461(self):
        return self.__model_xsd_XSDComplexTypeDefinition461

    @model_xsd_XSDComplexTypeDefinition461.setter
    def model_xsd_XSDComplexTypeDefinition461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition461", None)
        self.__model_xsd_XSDComplexTypeDefinition461 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDWildcard462"):
                opp_val = getattr(old_value, "XSDWildcard462", None)
                if opp_val == self:
                    setattr(old_value, "XSDWildcard462", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDWildcard462"):
                opp_val = getattr(value, "XSDWildcard462", None)
                setattr(value, "XSDWildcard462", self)

    @property
    def model_xsd_XSDComplexTypeDefinition444(self):
        return self.__model_xsd_XSDComplexTypeDefinition444

    @model_xsd_XSDComplexTypeDefinition444.setter
    def model_xsd_XSDComplexTypeDefinition444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition444", None)
        self.__model_xsd_XSDComplexTypeDefinition444 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTypeDefinition445"):
                opp_val = getattr(old_value, "XSDTypeDefinition445", None)
                if opp_val == self:
                    setattr(old_value, "XSDTypeDefinition445", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTypeDefinition445"):
                opp_val = getattr(value, "XSDTypeDefinition445", None)
                setattr(value, "XSDTypeDefinition445", self)

    @property
    def model_xsd_XSDComplexTypeDefinition447(self):
        return self.__model_xsd_XSDComplexTypeDefinition447

    @model_xsd_XSDComplexTypeDefinition447.setter
    def model_xsd_XSDComplexTypeDefinition447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition447", None)
        self.__model_xsd_XSDComplexTypeDefinition447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDComplexTypeContent"):
                opp_val = getattr(old_value, "XSDComplexTypeContent", None)
                if opp_val == self:
                    setattr(old_value, "XSDComplexTypeContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDComplexTypeContent"):
                opp_val = getattr(value, "XSDComplexTypeContent", None)
                setattr(value, "XSDComplexTypeContent", self)

    @property
    def model_xsd_XSDComplexTypeDefinition458(self):
        return self.__model_xsd_XSDComplexTypeDefinition458

    @model_xsd_XSDComplexTypeDefinition458.setter
    def model_xsd_XSDComplexTypeDefinition458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition458", None)
        self.__model_xsd_XSDComplexTypeDefinition458 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDWildcard459"):
                opp_val = getattr(old_value, "XSDWildcard459", None)
                if opp_val == self:
                    setattr(old_value, "XSDWildcard459", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDWildcard459"):
                opp_val = getattr(value, "XSDWildcard459", None)
                setattr(value, "XSDWildcard459", self)

    @property
    def model_xsd_XSDComplexTypeDefinition464(self):
        return self.__model_xsd_XSDComplexTypeDefinition464

    @model_xsd_XSDComplexTypeDefinition464.setter
    def model_xsd_XSDComplexTypeDefinition464(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition464", None)
        self.__model_xsd_XSDComplexTypeDefinition464 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTypeDefinition465"):
                opp_val = getattr(old_value, "XSDTypeDefinition465", None)
                if opp_val == self:
                    setattr(old_value, "XSDTypeDefinition465", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTypeDefinition465"):
                opp_val = getattr(value, "XSDTypeDefinition465", None)
                setattr(value, "XSDTypeDefinition465", self)

    @property
    def model_xsd_XSDComplexTypeDefinition449(self):
        return self.__model_xsd_XSDComplexTypeDefinition449

    @model_xsd_XSDComplexTypeDefinition449.setter
    def model_xsd_XSDComplexTypeDefinition449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition449", None)
        self.__model_xsd_XSDComplexTypeDefinition449 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDComplexTypeContent450"):
                opp_val = getattr(old_value, "XSDComplexTypeContent450", None)
                if opp_val == self:
                    setattr(old_value, "XSDComplexTypeContent450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDComplexTypeContent450"):
                opp_val = getattr(value, "XSDComplexTypeContent450", None)
                setattr(value, "XSDComplexTypeContent450", self)

    @property
    def model_xsd_XSDComplexTypeDefinition467(self):
        return self.__model_xsd_XSDComplexTypeDefinition467

    @model_xsd_XSDComplexTypeDefinition467.setter
    def model_xsd_XSDComplexTypeDefinition467(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDComplexTypeDefinition__model_xsd_XSDComplexTypeDefinition467", None)
        self.__model_xsd_XSDComplexTypeDefinition467 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDParticle"):
                opp_val = getattr(old_value, "XSDParticle", None)
                if opp_val == self:
                    setattr(old_value, "XSDParticle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDParticle"):
                opp_val = getattr(value, "XSDParticle", None)
                setattr(value, "XSDParticle", self)

class XSDComponent:

    pass
class model_xsd_XSDFacet(XSDComponent):

    def __init__(self, lexicalValue: str, facetName: str, effectiveValue: str, model_xsd_XSDFacet: "XSDAnnotation" = None, model_xsd_XSDFacet507: "XSDSimpleTypeDefinition" = None):
        self.lexicalValue = lexicalValue
        self.facetName = facetName
        self.effectiveValue = effectiveValue
        self.model_xsd_XSDFacet = model_xsd_XSDFacet
        self.model_xsd_XSDFacet507 = model_xsd_XSDFacet507
        
    @property
    def facetName(self) -> str:
        return self.__facetName

    @facetName.setter
    def facetName(self, facetName: str):
        self.__facetName = facetName

    @property
    def effectiveValue(self) -> str:
        return self.__effectiveValue

    @effectiveValue.setter
    def effectiveValue(self, effectiveValue: str):
        self.__effectiveValue = effectiveValue

    @property
    def lexicalValue(self) -> str:
        return self.__lexicalValue

    @lexicalValue.setter
    def lexicalValue(self, lexicalValue: str):
        self.__lexicalValue = lexicalValue

    @property
    def model_xsd_XSDFacet507(self):
        return self.__model_xsd_XSDFacet507

    @model_xsd_XSDFacet507.setter
    def model_xsd_XSDFacet507(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDFacet__model_xsd_XSDFacet507", None)
        self.__model_xsd_XSDFacet507 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSimpleTypeDefinition508"):
                opp_val = getattr(old_value, "XSDSimpleTypeDefinition508", None)
                if opp_val == self:
                    setattr(old_value, "XSDSimpleTypeDefinition508", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSimpleTypeDefinition508"):
                opp_val = getattr(value, "XSDSimpleTypeDefinition508", None)
                setattr(value, "XSDSimpleTypeDefinition508", self)

    @property
    def model_xsd_XSDFacet(self):
        return self.__model_xsd_XSDFacet

    @model_xsd_XSDFacet.setter
    def model_xsd_XSDFacet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDFacet__model_xsd_XSDFacet", None)
        self.__model_xsd_XSDFacet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation505"):
                opp_val = getattr(old_value, "XSDAnnotation505", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation505", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation505"):
                opp_val = getattr(value, "XSDAnnotation505", None)
                setattr(value, "XSDAnnotation505", self)

class model_xsd_XSDNamedComponent(XSDComponent):

    def __init__(self, targetNamespace: str, aliasName: str, uRI: str, aliasURI: str, qName: str, name: str):
        self.targetNamespace = targetNamespace
        self.aliasName = aliasName
        self.uRI = uRI
        self.aliasURI = aliasURI
        self.qName = qName
        self.name = name
        
    @property
    def aliasURI(self) -> str:
        return self.__aliasURI

    @aliasURI.setter
    def aliasURI(self, aliasURI: str):
        self.__aliasURI = aliasURI

    @property
    def targetNamespace(self) -> str:
        return self.__targetNamespace

    @targetNamespace.setter
    def targetNamespace(self, targetNamespace: str):
        self.__targetNamespace = targetNamespace

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def aliasName(self) -> str:
        return self.__aliasName

    @aliasName.setter
    def aliasName(self, aliasName: str):
        self.__aliasName = aliasName

    @property
    def uRI(self) -> str:
        return self.__uRI

    @uRI.setter
    def uRI(self, uRI: str):
        self.__uRI = uRI

    @property
    def qName(self) -> str:
        return self.__qName

    @qName.setter
    def qName(self, qName: str):
        self.__qName = qName

class model_xsd_XSDScope(XSDComponent):

    pass
class model_xsd_XSDXPathDefinition(XSDComponent):

    def __init__(self, variety: str, value: str, model_xsd_XSDXPathDefinition: "XSDAnnotation" = None):
        self.variety = variety
        self.value = value
        self.model_xsd_XSDXPathDefinition = model_xsd_XSDXPathDefinition
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def variety(self) -> str:
        return self.__variety

    @variety.setter
    def variety(self, variety: str):
        self.__variety = variety

    @property
    def model_xsd_XSDXPathDefinition(self):
        return self.__model_xsd_XSDXPathDefinition

    @model_xsd_XSDXPathDefinition.setter
    def model_xsd_XSDXPathDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDXPathDefinition__model_xsd_XSDXPathDefinition", None)
        self.__model_xsd_XSDXPathDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation717"):
                opp_val = getattr(old_value, "XSDAnnotation717", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation717", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation717"):
                opp_val = getattr(value, "XSDAnnotation717", None)
                setattr(value, "XSDAnnotation717", self)

class model_xsd_XSDComplexTypeContent(XSDComponent):

    pass
class XSDFundamentalFacet:

    pass
class model_xsd_XSDCardinalityFacet(XSDFundamentalFacet):

    def __init__(self, value: str, XSDFundamentalFacet: "model_xsd_XSDSimpleTypeDefinition"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_xsd_XSDOrderedFacet(XSDFundamentalFacet):

    def __init__(self, value: str, XSDFundamentalFacet: "model_xsd_XSDSimpleTypeDefinition"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_xsd_XSDNumericFacet(XSDFundamentalFacet):

    def __init__(self, value: bool, XSDFundamentalFacet: "model_xsd_XSDSimpleTypeDefinition"):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class model_xsd_XSDBoundedFacet(XSDFundamentalFacet):

    def __init__(self, value: bool, XSDFundamentalFacet: "model_xsd_XSDSimpleTypeDefinition"):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class XSDAnnotation:

    pass
class xsd_XSDSchemaContent:

    pass
class model_xsd_XSDNotationDeclaration(xsd_XSDNamedComponent, xsd_XSDSchemaContent):

    def __init__(self, systemIdentifier: str, publicIdentifier: str, model_xsd_XSDNotationDeclaration: "XSDAnnotation" = None):
        self.systemIdentifier = systemIdentifier
        self.publicIdentifier = publicIdentifier
        self.model_xsd_XSDNotationDeclaration = model_xsd_XSDNotationDeclaration
        
    @property
    def publicIdentifier(self) -> str:
        return self.__publicIdentifier

    @publicIdentifier.setter
    def publicIdentifier(self, publicIdentifier: str):
        self.__publicIdentifier = publicIdentifier

    @property
    def systemIdentifier(self) -> str:
        return self.__systemIdentifier

    @systemIdentifier.setter
    def systemIdentifier(self, systemIdentifier: str):
        self.__systemIdentifier = systemIdentifier

    @property
    def model_xsd_XSDNotationDeclaration(self):
        return self.__model_xsd_XSDNotationDeclaration

    @model_xsd_XSDNotationDeclaration.setter
    def model_xsd_XSDNotationDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDNotationDeclaration__model_xsd_XSDNotationDeclaration", None)
        self.__model_xsd_XSDNotationDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation544"):
                opp_val = getattr(old_value, "XSDAnnotation544", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation544", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation544"):
                opp_val = getattr(value, "XSDAnnotation544", None)
                setattr(value, "XSDAnnotation544", self)

class xsd_XSDFeature:

    pass
class model_xsd_XSDElementDeclaration(xsd_XSDTerm, xsd_XSDSchemaContent, xsd_XSDFeature):

    def __init__(self, nillable: bool, disallowedSubstitutions: str, substitutionGroupExclusions: str, abstract: bool, lexicalFinal: str, block: str, elementDeclarationReference: bool, circular: bool, model_xsd_XSDElementDeclaration: "XSDAnnotation" = None, model_xsd_XSDElementDeclaration488: "XSDTypeDefinition" = None, model_xsd_XSDElementDeclaration491: "XSDTypeDefinition" = None, model_xsd_XSDElementDeclaration494: set["XSDIdentityConstraintDefinition"] = None, model_xsd_XSDElementDeclaration496: "XSDElementDeclaration" = None, model_xsd_XSDElementDeclaration499: "XSDElementDeclaration" = None, model_xsd_XSDElementDeclaration502: set["XSDElementDeclaration"] = None):
        self.nillable = nillable
        self.disallowedSubstitutions = disallowedSubstitutions
        self.substitutionGroupExclusions = substitutionGroupExclusions
        self.abstract = abstract
        self.lexicalFinal = lexicalFinal
        self.block = block
        self.elementDeclarationReference = elementDeclarationReference
        self.circular = circular
        self.model_xsd_XSDElementDeclaration = model_xsd_XSDElementDeclaration
        self.model_xsd_XSDElementDeclaration488 = model_xsd_XSDElementDeclaration488
        self.model_xsd_XSDElementDeclaration491 = model_xsd_XSDElementDeclaration491
        self.model_xsd_XSDElementDeclaration494 = model_xsd_XSDElementDeclaration494 if model_xsd_XSDElementDeclaration494 is not None else set()
        self.model_xsd_XSDElementDeclaration496 = model_xsd_XSDElementDeclaration496
        self.model_xsd_XSDElementDeclaration499 = model_xsd_XSDElementDeclaration499
        self.model_xsd_XSDElementDeclaration502 = model_xsd_XSDElementDeclaration502 if model_xsd_XSDElementDeclaration502 is not None else set()
        
    @property
    def lexicalFinal(self) -> str:
        return self.__lexicalFinal

    @lexicalFinal.setter
    def lexicalFinal(self, lexicalFinal: str):
        self.__lexicalFinal = lexicalFinal

    @property
    def block(self) -> str:
        return self.__block

    @block.setter
    def block(self, block: str):
        self.__block = block

    @property
    def substitutionGroupExclusions(self) -> str:
        return self.__substitutionGroupExclusions

    @substitutionGroupExclusions.setter
    def substitutionGroupExclusions(self, substitutionGroupExclusions: str):
        self.__substitutionGroupExclusions = substitutionGroupExclusions

    @property
    def nillable(self) -> bool:
        return self.__nillable

    @nillable.setter
    def nillable(self, nillable: bool):
        self.__nillable = nillable

    @property
    def elementDeclarationReference(self) -> bool:
        return self.__elementDeclarationReference

    @elementDeclarationReference.setter
    def elementDeclarationReference(self, elementDeclarationReference: bool):
        self.__elementDeclarationReference = elementDeclarationReference

    @property
    def circular(self) -> bool:
        return self.__circular

    @circular.setter
    def circular(self, circular: bool):
        self.__circular = circular

    @property
    def disallowedSubstitutions(self) -> str:
        return self.__disallowedSubstitutions

    @disallowedSubstitutions.setter
    def disallowedSubstitutions(self, disallowedSubstitutions: str):
        self.__disallowedSubstitutions = disallowedSubstitutions

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def model_xsd_XSDElementDeclaration(self):
        return self.__model_xsd_XSDElementDeclaration

    @model_xsd_XSDElementDeclaration.setter
    def model_xsd_XSDElementDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDElementDeclaration__model_xsd_XSDElementDeclaration", None)
        self.__model_xsd_XSDElementDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation486"):
                opp_val = getattr(old_value, "XSDAnnotation486", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation486", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation486"):
                opp_val = getattr(value, "XSDAnnotation486", None)
                setattr(value, "XSDAnnotation486", self)

    @property
    def model_xsd_XSDElementDeclaration496(self):
        return self.__model_xsd_XSDElementDeclaration496

    @model_xsd_XSDElementDeclaration496.setter
    def model_xsd_XSDElementDeclaration496(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDElementDeclaration__model_xsd_XSDElementDeclaration496", None)
        self.__model_xsd_XSDElementDeclaration496 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDElementDeclaration497"):
                opp_val = getattr(old_value, "XSDElementDeclaration497", None)
                if opp_val == self:
                    setattr(old_value, "XSDElementDeclaration497", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDElementDeclaration497"):
                opp_val = getattr(value, "XSDElementDeclaration497", None)
                setattr(value, "XSDElementDeclaration497", self)

    @property
    def model_xsd_XSDElementDeclaration499(self):
        return self.__model_xsd_XSDElementDeclaration499

    @model_xsd_XSDElementDeclaration499.setter
    def model_xsd_XSDElementDeclaration499(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDElementDeclaration__model_xsd_XSDElementDeclaration499", None)
        self.__model_xsd_XSDElementDeclaration499 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDElementDeclaration500"):
                opp_val = getattr(old_value, "XSDElementDeclaration500", None)
                if opp_val == self:
                    setattr(old_value, "XSDElementDeclaration500", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDElementDeclaration500"):
                opp_val = getattr(value, "XSDElementDeclaration500", None)
                setattr(value, "XSDElementDeclaration500", self)

    @property
    def model_xsd_XSDElementDeclaration488(self):
        return self.__model_xsd_XSDElementDeclaration488

    @model_xsd_XSDElementDeclaration488.setter
    def model_xsd_XSDElementDeclaration488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDElementDeclaration__model_xsd_XSDElementDeclaration488", None)
        self.__model_xsd_XSDElementDeclaration488 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTypeDefinition489"):
                opp_val = getattr(old_value, "XSDTypeDefinition489", None)
                if opp_val == self:
                    setattr(old_value, "XSDTypeDefinition489", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTypeDefinition489"):
                opp_val = getattr(value, "XSDTypeDefinition489", None)
                setattr(value, "XSDTypeDefinition489", self)

    @property
    def model_xsd_XSDElementDeclaration502(self):
        return self.__model_xsd_XSDElementDeclaration502

    @model_xsd_XSDElementDeclaration502.setter
    def model_xsd_XSDElementDeclaration502(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDElementDeclaration__model_xsd_XSDElementDeclaration502", None)
        self.__model_xsd_XSDElementDeclaration502 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDElementDeclaration503"):
                    opp_val = getattr(item, "XSDElementDeclaration503", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDElementDeclaration503", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDElementDeclaration503"):
                    opp_val = getattr(item, "XSDElementDeclaration503", None)
                    
                    setattr(item, "XSDElementDeclaration503", self)
                    

    @property
    def model_xsd_XSDElementDeclaration494(self):
        return self.__model_xsd_XSDElementDeclaration494

    @model_xsd_XSDElementDeclaration494.setter
    def model_xsd_XSDElementDeclaration494(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDElementDeclaration__model_xsd_XSDElementDeclaration494", None)
        self.__model_xsd_XSDElementDeclaration494 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDIdentityConstraintDefinition"):
                    opp_val = getattr(item, "XSDIdentityConstraintDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDIdentityConstraintDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDIdentityConstraintDefinition"):
                    opp_val = getattr(item, "XSDIdentityConstraintDefinition", None)
                    
                    setattr(item, "XSDIdentityConstraintDefinition", self)
                    

    @property
    def model_xsd_XSDElementDeclaration491(self):
        return self.__model_xsd_XSDElementDeclaration491

    @model_xsd_XSDElementDeclaration491.setter
    def model_xsd_XSDElementDeclaration491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDElementDeclaration__model_xsd_XSDElementDeclaration491", None)
        self.__model_xsd_XSDElementDeclaration491 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTypeDefinition492"):
                opp_val = getattr(old_value, "XSDTypeDefinition492", None)
                if opp_val == self:
                    setattr(old_value, "XSDTypeDefinition492", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTypeDefinition492"):
                opp_val = getattr(value, "XSDTypeDefinition492", None)
                setattr(value, "XSDTypeDefinition492", self)

class model_xsd_XSDAttributeDeclaration(xsd_XSDSchemaContent, xsd_XSDFeature):

    def __init__(self, attributeDeclarationReference: bool, model_xsd_XSDAttributeDeclaration414: "XSDSimpleTypeDefinition" = None, model_xsd_XSDAttributeDeclaration416: "XSDSimpleTypeDefinition" = None, model_xsd_XSDAttributeDeclaration: "XSDAnnotation" = None, model_xsd_XSDAttributeDeclaration419: "XSDAttributeDeclaration" = None):
        self.attributeDeclarationReference = attributeDeclarationReference
        self.model_xsd_XSDAttributeDeclaration414 = model_xsd_XSDAttributeDeclaration414
        self.model_xsd_XSDAttributeDeclaration416 = model_xsd_XSDAttributeDeclaration416
        self.model_xsd_XSDAttributeDeclaration = model_xsd_XSDAttributeDeclaration
        self.model_xsd_XSDAttributeDeclaration419 = model_xsd_XSDAttributeDeclaration419
        
    @property
    def attributeDeclarationReference(self) -> bool:
        return self.__attributeDeclarationReference

    @attributeDeclarationReference.setter
    def attributeDeclarationReference(self, attributeDeclarationReference: bool):
        self.__attributeDeclarationReference = attributeDeclarationReference

    @property
    def model_xsd_XSDAttributeDeclaration416(self):
        return self.__model_xsd_XSDAttributeDeclaration416

    @model_xsd_XSDAttributeDeclaration416.setter
    def model_xsd_XSDAttributeDeclaration416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeDeclaration__model_xsd_XSDAttributeDeclaration416", None)
        self.__model_xsd_XSDAttributeDeclaration416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSimpleTypeDefinition417"):
                opp_val = getattr(old_value, "XSDSimpleTypeDefinition417", None)
                if opp_val == self:
                    setattr(old_value, "XSDSimpleTypeDefinition417", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSimpleTypeDefinition417"):
                opp_val = getattr(value, "XSDSimpleTypeDefinition417", None)
                setattr(value, "XSDSimpleTypeDefinition417", self)

    @property
    def model_xsd_XSDAttributeDeclaration414(self):
        return self.__model_xsd_XSDAttributeDeclaration414

    @model_xsd_XSDAttributeDeclaration414.setter
    def model_xsd_XSDAttributeDeclaration414(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeDeclaration__model_xsd_XSDAttributeDeclaration414", None)
        self.__model_xsd_XSDAttributeDeclaration414 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSimpleTypeDefinition"):
                opp_val = getattr(old_value, "XSDSimpleTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "XSDSimpleTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSimpleTypeDefinition"):
                opp_val = getattr(value, "XSDSimpleTypeDefinition", None)
                setattr(value, "XSDSimpleTypeDefinition", self)

    @property
    def model_xsd_XSDAttributeDeclaration(self):
        return self.__model_xsd_XSDAttributeDeclaration

    @model_xsd_XSDAttributeDeclaration.setter
    def model_xsd_XSDAttributeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeDeclaration__model_xsd_XSDAttributeDeclaration", None)
        self.__model_xsd_XSDAttributeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation"):
                opp_val = getattr(old_value, "XSDAnnotation", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation"):
                opp_val = getattr(value, "XSDAnnotation", None)
                setattr(value, "XSDAnnotation", self)

    @property
    def model_xsd_XSDAttributeDeclaration419(self):
        return self.__model_xsd_XSDAttributeDeclaration419

    @model_xsd_XSDAttributeDeclaration419.setter
    def model_xsd_XSDAttributeDeclaration419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeDeclaration__model_xsd_XSDAttributeDeclaration419", None)
        self.__model_xsd_XSDAttributeDeclaration419 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAttributeDeclaration"):
                opp_val = getattr(old_value, "XSDAttributeDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "XSDAttributeDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAttributeDeclaration"):
                opp_val = getattr(value, "XSDAttributeDeclaration", None)
                setattr(value, "XSDAttributeDeclaration", self)

class xsd_XSDRedefineContent:

    pass
class model_xsd_XSDRedefinableComponent(xsd_XSDNamedComponent, xsd_XSDRedefineContent):

    def __init__(self, circular: bool):
        self.circular = circular
        
    @property
    def circular(self) -> bool:
        return self.__circular

    @circular.setter
    def circular(self, circular: bool):
        self.__circular = circular

class model_xsd_XSDModelGroupDefinition(xsd_XSDRedefinableComponent, xsd_XSDParticleContent, xsd_XSDRedefineContent):

    def __init__(self, modelGroupDefinitionReference: bool, model_xsd_XSDModelGroupDefinition: "XSDAnnotation" = None, model_xsd_XSDModelGroupDefinition540: "XSDModelGroup" = None, model_xsd_XSDModelGroupDefinition542: "XSDModelGroupDefinition" = None):
        self.modelGroupDefinitionReference = modelGroupDefinitionReference
        self.model_xsd_XSDModelGroupDefinition = model_xsd_XSDModelGroupDefinition
        self.model_xsd_XSDModelGroupDefinition540 = model_xsd_XSDModelGroupDefinition540
        self.model_xsd_XSDModelGroupDefinition542 = model_xsd_XSDModelGroupDefinition542
        
    @property
    def modelGroupDefinitionReference(self) -> bool:
        return self.__modelGroupDefinitionReference

    @modelGroupDefinitionReference.setter
    def modelGroupDefinitionReference(self, modelGroupDefinitionReference: bool):
        self.__modelGroupDefinitionReference = modelGroupDefinitionReference

    @property
    def model_xsd_XSDModelGroupDefinition542(self):
        return self.__model_xsd_XSDModelGroupDefinition542

    @model_xsd_XSDModelGroupDefinition542.setter
    def model_xsd_XSDModelGroupDefinition542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDModelGroupDefinition__model_xsd_XSDModelGroupDefinition542", None)
        self.__model_xsd_XSDModelGroupDefinition542 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDModelGroupDefinition"):
                opp_val = getattr(old_value, "XSDModelGroupDefinition", None)
                if opp_val == self:
                    setattr(old_value, "XSDModelGroupDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDModelGroupDefinition"):
                opp_val = getattr(value, "XSDModelGroupDefinition", None)
                setattr(value, "XSDModelGroupDefinition", self)

    @property
    def model_xsd_XSDModelGroupDefinition540(self):
        return self.__model_xsd_XSDModelGroupDefinition540

    @model_xsd_XSDModelGroupDefinition540.setter
    def model_xsd_XSDModelGroupDefinition540(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDModelGroupDefinition__model_xsd_XSDModelGroupDefinition540", None)
        self.__model_xsd_XSDModelGroupDefinition540 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDModelGroup"):
                opp_val = getattr(old_value, "XSDModelGroup", None)
                if opp_val == self:
                    setattr(old_value, "XSDModelGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDModelGroup"):
                opp_val = getattr(value, "XSDModelGroup", None)
                setattr(value, "XSDModelGroup", self)

    @property
    def model_xsd_XSDModelGroupDefinition(self):
        return self.__model_xsd_XSDModelGroupDefinition

    @model_xsd_XSDModelGroupDefinition.setter
    def model_xsd_XSDModelGroupDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDModelGroupDefinition__model_xsd_XSDModelGroupDefinition", None)
        self.__model_xsd_XSDModelGroupDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation538"):
                opp_val = getattr(old_value, "XSDAnnotation538", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation538", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation538"):
                opp_val = getattr(value, "XSDAnnotation538", None)
                setattr(value, "XSDAnnotation538", self)

class model_xsd_XSDAttributeGroupDefinition(xsd_XSDRedefineContent, xsd_XSDAttributeGroupContent, xsd_XSDRedefinableComponent):

    def __init__(self, attributeGroupDefinitionReference: bool, model_xsd_XSDAttributeGroupDefinition: "XSDAnnotation" = None, model_xsd_XSDAttributeGroupDefinition423: set["XSDAttributeGroupContent"] = None, model_xsd_XSDAttributeGroupDefinition425: set["XSDAttributeUse"] = None, model_xsd_XSDAttributeGroupDefinition427: "XSDWildcard" = None, model_xsd_XSDAttributeGroupDefinition429: "XSDWildcard" = None, model_xsd_XSDAttributeGroupDefinition432: "XSDAttributeGroupDefinition" = None, model_xsd_XSDAttributeGroupDefinition434: "XSDWildcard" = None):
        self.attributeGroupDefinitionReference = attributeGroupDefinitionReference
        self.model_xsd_XSDAttributeGroupDefinition = model_xsd_XSDAttributeGroupDefinition
        self.model_xsd_XSDAttributeGroupDefinition423 = model_xsd_XSDAttributeGroupDefinition423 if model_xsd_XSDAttributeGroupDefinition423 is not None else set()
        self.model_xsd_XSDAttributeGroupDefinition425 = model_xsd_XSDAttributeGroupDefinition425 if model_xsd_XSDAttributeGroupDefinition425 is not None else set()
        self.model_xsd_XSDAttributeGroupDefinition427 = model_xsd_XSDAttributeGroupDefinition427
        self.model_xsd_XSDAttributeGroupDefinition429 = model_xsd_XSDAttributeGroupDefinition429
        self.model_xsd_XSDAttributeGroupDefinition432 = model_xsd_XSDAttributeGroupDefinition432
        self.model_xsd_XSDAttributeGroupDefinition434 = model_xsd_XSDAttributeGroupDefinition434
        
    @property
    def attributeGroupDefinitionReference(self) -> bool:
        return self.__attributeGroupDefinitionReference

    @attributeGroupDefinitionReference.setter
    def attributeGroupDefinitionReference(self, attributeGroupDefinitionReference: bool):
        self.__attributeGroupDefinitionReference = attributeGroupDefinitionReference

    @property
    def model_xsd_XSDAttributeGroupDefinition429(self):
        return self.__model_xsd_XSDAttributeGroupDefinition429

    @model_xsd_XSDAttributeGroupDefinition429.setter
    def model_xsd_XSDAttributeGroupDefinition429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeGroupDefinition__model_xsd_XSDAttributeGroupDefinition429", None)
        self.__model_xsd_XSDAttributeGroupDefinition429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDWildcard430"):
                opp_val = getattr(old_value, "XSDWildcard430", None)
                if opp_val == self:
                    setattr(old_value, "XSDWildcard430", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDWildcard430"):
                opp_val = getattr(value, "XSDWildcard430", None)
                setattr(value, "XSDWildcard430", self)

    @property
    def model_xsd_XSDAttributeGroupDefinition427(self):
        return self.__model_xsd_XSDAttributeGroupDefinition427

    @model_xsd_XSDAttributeGroupDefinition427.setter
    def model_xsd_XSDAttributeGroupDefinition427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeGroupDefinition__model_xsd_XSDAttributeGroupDefinition427", None)
        self.__model_xsd_XSDAttributeGroupDefinition427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDWildcard"):
                opp_val = getattr(old_value, "XSDWildcard", None)
                if opp_val == self:
                    setattr(old_value, "XSDWildcard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDWildcard"):
                opp_val = getattr(value, "XSDWildcard", None)
                setattr(value, "XSDWildcard", self)

    @property
    def model_xsd_XSDAttributeGroupDefinition425(self):
        return self.__model_xsd_XSDAttributeGroupDefinition425

    @model_xsd_XSDAttributeGroupDefinition425.setter
    def model_xsd_XSDAttributeGroupDefinition425(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeGroupDefinition__model_xsd_XSDAttributeGroupDefinition425", None)
        self.__model_xsd_XSDAttributeGroupDefinition425 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDAttributeUse"):
                    opp_val = getattr(item, "XSDAttributeUse", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDAttributeUse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDAttributeUse"):
                    opp_val = getattr(item, "XSDAttributeUse", None)
                    
                    setattr(item, "XSDAttributeUse", self)
                    

    @property
    def model_xsd_XSDAttributeGroupDefinition(self):
        return self.__model_xsd_XSDAttributeGroupDefinition

    @model_xsd_XSDAttributeGroupDefinition.setter
    def model_xsd_XSDAttributeGroupDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeGroupDefinition__model_xsd_XSDAttributeGroupDefinition", None)
        self.__model_xsd_XSDAttributeGroupDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAnnotation421"):
                opp_val = getattr(old_value, "XSDAnnotation421", None)
                if opp_val == self:
                    setattr(old_value, "XSDAnnotation421", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAnnotation421"):
                opp_val = getattr(value, "XSDAnnotation421", None)
                setattr(value, "XSDAnnotation421", self)

    @property
    def model_xsd_XSDAttributeGroupDefinition423(self):
        return self.__model_xsd_XSDAttributeGroupDefinition423

    @model_xsd_XSDAttributeGroupDefinition423.setter
    def model_xsd_XSDAttributeGroupDefinition423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeGroupDefinition__model_xsd_XSDAttributeGroupDefinition423", None)
        self.__model_xsd_XSDAttributeGroupDefinition423 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XSDAttributeGroupContent"):
                    opp_val = getattr(item, "XSDAttributeGroupContent", None)
                    
                    if opp_val == self:
                        setattr(item, "XSDAttributeGroupContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XSDAttributeGroupContent"):
                    opp_val = getattr(item, "XSDAttributeGroupContent", None)
                    
                    setattr(item, "XSDAttributeGroupContent", self)
                    

    @property
    def model_xsd_XSDAttributeGroupDefinition434(self):
        return self.__model_xsd_XSDAttributeGroupDefinition434

    @model_xsd_XSDAttributeGroupDefinition434.setter
    def model_xsd_XSDAttributeGroupDefinition434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeGroupDefinition__model_xsd_XSDAttributeGroupDefinition434", None)
        self.__model_xsd_XSDAttributeGroupDefinition434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDWildcard435"):
                opp_val = getattr(old_value, "XSDWildcard435", None)
                if opp_val == self:
                    setattr(old_value, "XSDWildcard435", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDWildcard435"):
                opp_val = getattr(value, "XSDWildcard435", None)
                setattr(value, "XSDWildcard435", self)

    @property
    def model_xsd_XSDAttributeGroupDefinition432(self):
        return self.__model_xsd_XSDAttributeGroupDefinition432

    @model_xsd_XSDAttributeGroupDefinition432.setter
    def model_xsd_XSDAttributeGroupDefinition432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeGroupDefinition__model_xsd_XSDAttributeGroupDefinition432", None)
        self.__model_xsd_XSDAttributeGroupDefinition432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAttributeGroupDefinition"):
                opp_val = getattr(old_value, "XSDAttributeGroupDefinition", None)
                if opp_val == self:
                    setattr(old_value, "XSDAttributeGroupDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAttributeGroupDefinition"):
                opp_val = getattr(value, "XSDAttributeGroupDefinition", None)
                setattr(value, "XSDAttributeGroupDefinition", self)

class model_xsd_XSDTypeDefinition(xsd_XSDRedefinableComponent, xsd_XSDRedefineContent):

    pass
class xsd_XSDComponent:

    pass
class model_xsd_XSDTerm(xsd_XSDComponent, xsd_XSDParticleContent):

    pass
class model_xsd_XSDAttributeUse(xsd_XSDComponent, xsd_XSDAttributeGroupContent):

    def __init__(self, required: bool, value: str, constraint: str, use: str, lexicalValue: str, model_xsd_XSDAttributeUse: "XSDAttributeDeclaration" = None, model_xsd_XSDAttributeUse439: "XSDAttributeDeclaration" = None):
        self.required = required
        self.value = value
        self.constraint = constraint
        self.use = use
        self.lexicalValue = lexicalValue
        self.model_xsd_XSDAttributeUse = model_xsd_XSDAttributeUse
        self.model_xsd_XSDAttributeUse439 = model_xsd_XSDAttributeUse439
        
    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def use(self) -> str:
        return self.__use

    @use.setter
    def use(self, use: str):
        self.__use = use

    @property
    def constraint(self) -> str:
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: str):
        self.__constraint = constraint

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def lexicalValue(self) -> str:
        return self.__lexicalValue

    @lexicalValue.setter
    def lexicalValue(self, lexicalValue: str):
        self.__lexicalValue = lexicalValue

    @property
    def model_xsd_XSDAttributeUse(self):
        return self.__model_xsd_XSDAttributeUse

    @model_xsd_XSDAttributeUse.setter
    def model_xsd_XSDAttributeUse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeUse__model_xsd_XSDAttributeUse", None)
        self.__model_xsd_XSDAttributeUse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAttributeDeclaration437"):
                opp_val = getattr(old_value, "XSDAttributeDeclaration437", None)
                if opp_val == self:
                    setattr(old_value, "XSDAttributeDeclaration437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAttributeDeclaration437"):
                opp_val = getattr(value, "XSDAttributeDeclaration437", None)
                setattr(value, "XSDAttributeDeclaration437", self)

    @property
    def model_xsd_XSDAttributeUse439(self):
        return self.__model_xsd_XSDAttributeUse439

    @model_xsd_XSDAttributeUse439.setter
    def model_xsd_XSDAttributeUse439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xsd_XSDAttributeUse__model_xsd_XSDAttributeUse439", None)
        self.__model_xsd_XSDAttributeUse439 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDAttributeDeclaration440"):
                opp_val = getattr(old_value, "XSDAttributeDeclaration440", None)
                if opp_val == self:
                    setattr(old_value, "XSDAttributeDeclaration440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDAttributeDeclaration440"):
                opp_val = getattr(value, "XSDAttributeDeclaration440", None)
                setattr(value, "XSDAttributeDeclaration440", self)

class model_xsd_XSDAnnotation(xsd_XSDComponent, xsd_XSDRedefineContent):

    def __init__(self, applicationInformation: str, userInformation: str, attributes: str):
        self.applicationInformation = applicationInformation
        self.userInformation = userInformation
        self.attributes = attributes
        
    @property
    def userInformation(self) -> str:
        return self.__userInformation

    @userInformation.setter
    def userInformation(self, userInformation: str):
        self.__userInformation = userInformation

    @property
    def attributes(self) -> str:
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes: str):
        self.__attributes = attributes

    @property
    def applicationInformation(self) -> str:
        return self.__applicationInformation

    @applicationInformation.setter
    def applicationInformation(self, applicationInformation: str):
        self.__applicationInformation = applicationInformation

class IExtensibilityElement:

    pass
class model_wsdl_ISchema(IExtensibilityElement):

    pass
class model_wsdl_IObject(ABC):

    pass
class model_wsdl_IAttributeExtensible(ABC):

    def __init__(self):
        
    def getNativeAttributeNames(self) -> str:
        # TODO: Implement getNativeAttributeNames method
        pass

    def getExtensionAttribute(self, name: str) -> str:
        # TODO: Implement getExtensionAttribute method
        pass

    def setExtensionAttribute(self, name: str, value: str):
        # TODO: Implement setExtensionAttribute method
        pass

    def getExtensionAttributes(self) -> str:
        # TODO: Implement getExtensionAttributes method
        pass

class model_wsdl_IElementExtensible(ABC):

    def __init__(self):
        
    def addExtensibilityElement(self, extElement: str):
        # TODO: Implement addExtensibilityElement method
        pass

    def getExtensibilityElements(self) -> str:
        # TODO: Implement getExtensibilityElements method
        pass

class XSDAttributeDeclaration:

    pass
class XSDSimpleTypeDefinition:

    pass
class model_wsdl_ITypes(ABC):

    pass
class model_wsdl_IIterator(ABC):

    pass
class wsdl_ITypes:

    pass
class model_wsdl_IExtensionRegistry(ABC):

    pass
class model_wsdl_IURL(ABC):

    pass
class model_wsdl_IMap(ABC):

    pass
class model_wsdl_IList(ABC):

    pass
class wsdl_ISchema:

    pass
class wsdl_ExtensibilityElement:

    pass
class model_wsdl_XSDSchemaExtensibilityElement(wsdl_ISchema, wsdl_ExtensibilityElement):

    def __init__(self, documentBaseURI: str, model_wsdl_XSDSchemaExtensibilityElement: "XSDSchema" = None):
        self.documentBaseURI = documentBaseURI
        self.model_wsdl_XSDSchemaExtensibilityElement = model_wsdl_XSDSchemaExtensibilityElement
        
    @property
    def documentBaseURI(self) -> str:
        return self.__documentBaseURI

    @documentBaseURI.setter
    def documentBaseURI(self, documentBaseURI: str):
        self.__documentBaseURI = documentBaseURI

    @property
    def model_wsdl_XSDSchemaExtensibilityElement(self):
        return self.__model_wsdl_XSDSchemaExtensibilityElement

    @model_wsdl_XSDSchemaExtensibilityElement.setter
    def model_wsdl_XSDSchemaExtensibilityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_XSDSchemaExtensibilityElement__model_wsdl_XSDSchemaExtensibilityElement", None)
        self.__model_wsdl_XSDSchemaExtensibilityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSchema409"):
                opp_val = getattr(old_value, "XSDSchema409", None)
                if opp_val == self:
                    setattr(old_value, "XSDSchema409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSchema409"):
                opp_val = getattr(value, "XSDSchema409", None)
                setattr(value, "XSDSchema409", self)

class model_wsdl_IExtensibilityElement(ABC):

    pass
class IElementExtensible:

    pass
class model_wsdl_IBindingOperation(IElementExtensible):

    def __init__(self):
        
    def getBindingOutput(self) -> str:
        # TODO: Implement getBindingOutput method
        pass

    def setBindingInput(self, bindingInput: str):
        # TODO: Implement setBindingInput method
        pass

    def getBindingFault(self, name: str) -> str:
        # TODO: Implement getBindingFault method
        pass

    def setOperation(self, operation: str):
        # TODO: Implement setOperation method
        pass

    def getBindingInput(self) -> str:
        # TODO: Implement getBindingInput method
        pass

    def getOperation(self) -> str:
        # TODO: Implement getOperation method
        pass

    def addBindingFault(self, bindingFault: str):
        # TODO: Implement addBindingFault method
        pass

    def setBindingOutput(self, bindingOutput: str):
        # TODO: Implement setBindingOutput method
        pass

    def getBindingFaults(self) -> str:
        # TODO: Implement getBindingFaults method
        pass

class model_wsdl_IPort(IElementExtensible):

    def __init__(self):
        
    def setBinding(self, binding: str):
        # TODO: Implement setBinding method
        pass

    def getBinding(self) -> str:
        # TODO: Implement getBinding method
        pass

class model_wsdl_IBindingInput(IElementExtensible):

    pass
class model_wsdl_IBinding(IElementExtensible):

    def __init__(self):
        
    def getBindingOperations(self) -> str:
        # TODO: Implement getBindingOperations method
        pass

    def getPortType(self) -> str:
        # TODO: Implement getPortType method
        pass

    def setPortType(self, portType: str):
        # TODO: Implement setPortType method
        pass

    def getBindingOperation(self, name: str, outputName: str, inputName: str) -> str:
        # TODO: Implement getBindingOperation method
        pass

    def addBindingOperation(self, bindingOperation: str):
        # TODO: Implement addBindingOperation method
        pass

class model_wsdl_IBindingFault(IElementExtensible):

    pass
class model_wsdl_IBindingOutput(IElementExtensible):

    pass
class model_wsdl_IService(IElementExtensible):

    def __init__(self):
        
    def addPort(self, port: str):
        # TODO: Implement addPort method
        pass

    def getPort(self, name: str) -> str:
        # TODO: Implement getPort method
        pass

    def getPorts(self) -> str:
        # TODO: Implement getPorts method
        pass

class model_wsdl_IDefinition(IElementExtensible):

    def __init__(self):
        
    def removePortType(self, name: str) -> str:
        # TODO: Implement removePortType method
        pass

    def addBinding(self, binding: str):
        # TODO: Implement addBinding method
        pass

    def getImports(self, namespaceURI: str) -> str:
        # TODO: Implement getImports method
        pass

    def getBindings(self) -> str:
        # TODO: Implement getBindings method
        pass

    def addImport(self, importDef: str):
        # TODO: Implement addImport method
        pass

    def createBindingOutput(self) -> str:
        # TODO: Implement createBindingOutput method
        pass

    def removeMessage(self, name: str) -> str:
        # TODO: Implement removeMessage method
        pass

    def addService(self, service: str):
        # TODO: Implement addService method
        pass

    def createOperation(self) -> str:
        # TODO: Implement createOperation method
        pass

    def removeBinding(self, name: str) -> str:
        # TODO: Implement removeBinding method
        pass

    def getNamespaces(self) -> str:
        # TODO: Implement getNamespaces method
        pass

    def addNamespace(self, prefix: str, namespaceURI: str):
        # TODO: Implement addNamespace method
        pass

    def createPortType(self) -> str:
        # TODO: Implement createPortType method
        pass

    def createImport(self) -> str:
        # TODO: Implement createImport method
        pass

    def createTypes(self) -> str:
        # TODO: Implement createTypes method
        pass

    def getPrefix(self, namespaceURI: str) -> str:
        # TODO: Implement getPrefix method
        pass

    def getDocumentBaseURI(self) -> str:
        # TODO: Implement getDocumentBaseURI method
        pass

    def addMessage(self, message: str):
        # TODO: Implement addMessage method
        pass

    def createPort(self) -> str:
        # TODO: Implement createPort method
        pass

    def getNamespace(self, prefix: str) -> str:
        # TODO: Implement getNamespace method
        pass

    def getMessages(self) -> str:
        # TODO: Implement getMessages method
        pass

    def addPortType(self, portType: str):
        # TODO: Implement addPortType method
        pass

    def getPortTypes(self) -> str:
        # TODO: Implement getPortTypes method
        pass

    def createService(self) -> str:
        # TODO: Implement createService method
        pass

    def createMessage(self) -> str:
        # TODO: Implement createMessage method
        pass

    def getMessage(self, name: str) -> str:
        # TODO: Implement getMessage method
        pass

    def createBindingInput(self) -> str:
        # TODO: Implement createBindingInput method
        pass

    def getImports(self) -> str:
        # TODO: Implement getImports method
        pass

    def getTypes(self) -> str:
        # TODO: Implement getTypes method
        pass

    def createBinding(self) -> str:
        # TODO: Implement createBinding method
        pass

    def createInput(self) -> str:
        # TODO: Implement createInput method
        pass

    def setExtensionRegistry(self, extensionRegistry: str):
        # TODO: Implement setExtensionRegistry method
        pass

    def createBindingFault(self) -> str:
        # TODO: Implement createBindingFault method
        pass

    def getPortType(self, name: str) -> str:
        # TODO: Implement getPortType method
        pass

    def createPart(self) -> str:
        # TODO: Implement createPart method
        pass

    def removeService(self, name: str) -> str:
        # TODO: Implement removeService method
        pass

    def setDocumentBaseURI(self, documentBase: str):
        # TODO: Implement setDocumentBaseURI method
        pass

    def getService(self, name: str) -> str:
        # TODO: Implement getService method
        pass

    def createFault(self) -> str:
        # TODO: Implement createFault method
        pass

    def createBindingOperation(self) -> str:
        # TODO: Implement createBindingOperation method
        pass

    def setTypes(self, types: str):
        # TODO: Implement setTypes method
        pass

    def getBinding(self, name: str) -> str:
        # TODO: Implement getBinding method
        pass

    def createOutput(self) -> str:
        # TODO: Implement createOutput method
        pass

    def getExtensionRegistry(self) -> str:
        # TODO: Implement getExtensionRegistry method
        pass

    def getServices(self) -> str:
        # TODO: Implement getServices method
        pass

class model_wsdl_IOperation(IElementExtensible):

    def __init__(self):
        
    def getInput(self) -> str:
        # TODO: Implement getInput method
        pass

    def getFault(self, name: str) -> str:
        # TODO: Implement getFault method
        pass

    def addFault(self, fault: str):
        # TODO: Implement addFault method
        pass

    def setInput(self, input: str):
        # TODO: Implement setInput method
        pass

    def getOutput(self) -> str:
        # TODO: Implement getOutput method
        pass

    def getFaults(self) -> str:
        # TODO: Implement getFaults method
        pass

    def setOutput(self, output: str):
        # TODO: Implement setOutput method
        pass

    def getParameterOrdering(self) -> str:
        # TODO: Implement getParameterOrdering method
        pass

    def setParameterOrdering(self, parameterOrder: str):
        # TODO: Implement setParameterOrdering method
        pass

class IAttributeExtensible:

    pass
class model_wsdl_IPart(IAttributeExtensible):

    pass
class model_wsdl_IImport(IAttributeExtensible):

    pass
class model_wsdl_IFault(IAttributeExtensible):

    def __init__(self):
        
    def setMessage(self, message: str):
        # TODO: Implement setMessage method
        pass

    def getMessage(self) -> str:
        # TODO: Implement getMessage method
        pass

class model_wsdl_IOutput(IAttributeExtensible):

    def __init__(self):
        
    def setMessage(self, message: str):
        # TODO: Implement setMessage method
        pass

    def getMessage(self) -> str:
        # TODO: Implement getMessage method
        pass

class model_wsdl_IInput(IAttributeExtensible):

    def __init__(self):
        
    def getMessage(self) -> str:
        # TODO: Implement getMessage method
        pass

    def setMessage(self, message: str):
        # TODO: Implement setMessage method
        pass

class model_wsdl_IPortType(IAttributeExtensible):

    def __init__(self):
        
    def addOperation(self, operation: str):
        # TODO: Implement addOperation method
        pass

    def getOperations(self) -> str:
        # TODO: Implement getOperations method
        pass

    def getOperation(self, outputName: str, inputName: str, name: str) -> str:
        # TODO: Implement getOperation method
        pass

class model_wsdl_IMessage(IElementExtensible):

    def __init__(self):
        
    def getPart(self, name: str) -> str:
        # TODO: Implement getPart method
        pass

    def getOrderedParts(self, partOrder: str) -> str:
        # TODO: Implement getOrderedParts method
        pass

    def getParts(self) -> str:
        # TODO: Implement getParts method
        pass

    def addPart(self, part: str):
        # TODO: Implement addPart method
        pass

class wsdl_IBindingFault:

    pass
class wsdl_IBindingOutput:

    pass
class wsdl_IBindingInput:

    pass
class wsdl_IFault:

    pass
class wsdl_IOutput:

    pass
class model_wsdl_Namespace:

    def __init__(self, URI: str, prefix: str):
        self.URI = URI
        self.prefix = prefix
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

class XSDSchema:

    pass
class Definition:

    pass
class wsdl_IImport:

    pass
class Namespace:

    pass
class Service:

    pass
class Types:

    pass
class Import:

    pass
class wsdl_IInput:

    pass
class wsdl_MessageReference:

    pass
class model_wsdl_Output(wsdl_MessageReference, wsdl_IOutput):

    pass
class model_wsdl_Fault(wsdl_MessageReference, wsdl_IFault):

    pass
class model_wsdl_Input(wsdl_MessageReference, wsdl_IInput):

    pass
class wsdl_IDefinition:

    pass
class wsdl_IAttributeExtensible:

    pass
class wsdl_IElementExtensible:

    pass
class wsdl_IExtensibilityElement:

    pass
class wsdl_WSDLElement:

    pass
class model_wsdl_ExtensibleElement(wsdl_IAttributeExtensible, wsdl_WSDLElement, wsdl_IElementExtensible):

    pass
class model_wsdl_ExtensibilityElement(wsdl_IExtensibilityElement, wsdl_WSDLElement):

    def __init__(self, required: bool, elementType: str):
        self.required = required
        self.elementType = elementType
        
    @property
    def elementType(self) -> str:
        return self.__elementType

    @elementType.setter
    def elementType(self, elementType: str):
        self.__elementType = elementType

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

class Binding:

    pass
class wsdl_IPort:

    pass
class Port:

    pass
class wsdl_IService:

    pass
class BindingFault:

    pass
class BindingOutput:

    pass
class BindingInput:

    pass
class wsdl_IBindingOperation:

    pass
class BindingOperation:

    pass
class wsdl_IBinding:

    pass
class wsdl_IPart:

    pass
class wsdl_IMessage:

    pass
class Fault:

    pass
class Output:

    pass
class Input:

    pass
class wsdl_IOperation:

    pass
class wsdl_IPortType:

    pass
class wsdl_ExtensibleElement:

    pass
class model_wsdl_BindingOutput(wsdl_IBindingOutput, wsdl_ExtensibleElement):

    def __init__(self, name: str, model_wsdl_BindingOutput: "Output" = None):
        self.name = name
        self.model_wsdl_BindingOutput = model_wsdl_BindingOutput
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_wsdl_BindingOutput(self):
        return self.__model_wsdl_BindingOutput

    @model_wsdl_BindingOutput.setter
    def model_wsdl_BindingOutput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_BindingOutput__model_wsdl_BindingOutput", None)
        self.__model_wsdl_BindingOutput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Output404"):
                opp_val = getattr(old_value, "Output404", None)
                if opp_val == self:
                    setattr(old_value, "Output404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Output404"):
                opp_val = getattr(value, "Output404", None)
                setattr(value, "Output404", self)

    def getOutput(self) -> str:
        # TODO: Implement getOutput method
        pass

    def setOutput(self, output: str):
        # TODO: Implement setOutput method
        pass

class model_wsdl_BindingOperation(wsdl_IBindingOperation, wsdl_ExtensibleElement):

    def __init__(self, name: str, model_wsdl_BindingOperation: "Operation" = None, model_wsdl_BindingOperation374: "BindingInput" = None, model_wsdl_BindingOperation376: "BindingOutput" = None, model_wsdl_BindingOperation378: set["BindingFault"] = None):
        self.name = name
        self.model_wsdl_BindingOperation = model_wsdl_BindingOperation
        self.model_wsdl_BindingOperation374 = model_wsdl_BindingOperation374
        self.model_wsdl_BindingOperation376 = model_wsdl_BindingOperation376
        self.model_wsdl_BindingOperation378 = model_wsdl_BindingOperation378 if model_wsdl_BindingOperation378 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_wsdl_BindingOperation(self):
        return self.__model_wsdl_BindingOperation

    @model_wsdl_BindingOperation.setter
    def model_wsdl_BindingOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_BindingOperation__model_wsdl_BindingOperation", None)
        self.__model_wsdl_BindingOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation372"):
                opp_val = getattr(old_value, "Operation372", None)
                if opp_val == self:
                    setattr(old_value, "Operation372", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation372"):
                opp_val = getattr(value, "Operation372", None)
                setattr(value, "Operation372", self)

    @property
    def model_wsdl_BindingOperation378(self):
        return self.__model_wsdl_BindingOperation378

    @model_wsdl_BindingOperation378.setter
    def model_wsdl_BindingOperation378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_BindingOperation__model_wsdl_BindingOperation378", None)
        self.__model_wsdl_BindingOperation378 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BindingFault"):
                    opp_val = getattr(item, "BindingFault", None)
                    
                    if opp_val == self:
                        setattr(item, "BindingFault", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BindingFault"):
                    opp_val = getattr(item, "BindingFault", None)
                    
                    setattr(item, "BindingFault", self)
                    

    @property
    def model_wsdl_BindingOperation374(self):
        return self.__model_wsdl_BindingOperation374

    @model_wsdl_BindingOperation374.setter
    def model_wsdl_BindingOperation374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_BindingOperation__model_wsdl_BindingOperation374", None)
        self.__model_wsdl_BindingOperation374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BindingInput"):
                opp_val = getattr(old_value, "BindingInput", None)
                if opp_val == self:
                    setattr(old_value, "BindingInput", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BindingInput"):
                opp_val = getattr(value, "BindingInput", None)
                setattr(value, "BindingInput", self)

    @property
    def model_wsdl_BindingOperation376(self):
        return self.__model_wsdl_BindingOperation376

    @model_wsdl_BindingOperation376.setter
    def model_wsdl_BindingOperation376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_BindingOperation__model_wsdl_BindingOperation376", None)
        self.__model_wsdl_BindingOperation376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BindingOutput"):
                opp_val = getattr(old_value, "BindingOutput", None)
                if opp_val == self:
                    setattr(old_value, "BindingOutput", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BindingOutput"):
                opp_val = getattr(value, "BindingOutput", None)
                setattr(value, "BindingOutput", self)

class model_wsdl_Operation(wsdl_IOperation, wsdl_ExtensibleElement):

    def __init__(self, style: str, name: str, undefined: bool, model_wsdl_Operation: "Input" = None, model_wsdl_Operation351: "Output" = None, model_wsdl_Operation353: set["Fault"] = None, model_wsdl_Operation355: set["Part"] = None):
        self.style = style
        self.name = name
        self.undefined = undefined
        self.model_wsdl_Operation = model_wsdl_Operation
        self.model_wsdl_Operation351 = model_wsdl_Operation351
        self.model_wsdl_Operation353 = model_wsdl_Operation353 if model_wsdl_Operation353 is not None else set()
        self.model_wsdl_Operation355 = model_wsdl_Operation355 if model_wsdl_Operation355 is not None else set()
        
    @property
    def undefined(self) -> bool:
        return self.__undefined

    @undefined.setter
    def undefined(self, undefined: bool):
        self.__undefined = undefined

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_wsdl_Operation(self):
        return self.__model_wsdl_Operation

    @model_wsdl_Operation.setter
    def model_wsdl_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Operation__model_wsdl_Operation", None)
        self.__model_wsdl_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Input"):
                opp_val = getattr(old_value, "Input", None)
                if opp_val == self:
                    setattr(old_value, "Input", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Input"):
                opp_val = getattr(value, "Input", None)
                setattr(value, "Input", self)

    @property
    def model_wsdl_Operation353(self):
        return self.__model_wsdl_Operation353

    @model_wsdl_Operation353.setter
    def model_wsdl_Operation353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Operation__model_wsdl_Operation353", None)
        self.__model_wsdl_Operation353 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Fault"):
                    opp_val = getattr(item, "Fault", None)
                    
                    if opp_val == self:
                        setattr(item, "Fault", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Fault"):
                    opp_val = getattr(item, "Fault", None)
                    
                    setattr(item, "Fault", self)
                    

    @property
    def model_wsdl_Operation351(self):
        return self.__model_wsdl_Operation351

    @model_wsdl_Operation351.setter
    def model_wsdl_Operation351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Operation__model_wsdl_Operation351", None)
        self.__model_wsdl_Operation351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Output"):
                opp_val = getattr(old_value, "Output", None)
                if opp_val == self:
                    setattr(old_value, "Output", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Output"):
                opp_val = getattr(value, "Output", None)
                setattr(value, "Output", self)

    @property
    def model_wsdl_Operation355(self):
        return self.__model_wsdl_Operation355

    @model_wsdl_Operation355.setter
    def model_wsdl_Operation355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Operation__model_wsdl_Operation355", None)
        self.__model_wsdl_Operation355 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Part356"):
                    opp_val = getattr(item, "Part356", None)
                    
                    if opp_val == self:
                        setattr(item, "Part356", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Part356"):
                    opp_val = getattr(item, "Part356", None)
                    
                    setattr(item, "Part356", self)
                    

class model_wsdl_Types(wsdl_ITypes, wsdl_ExtensibleElement):

    def __init__(self):
        
    def getSchemas(self) -> str:
        # TODO: Implement getSchemas method
        pass

    def getSchemas(self, namespaceURI: str) -> str:
        # TODO: Implement getSchemas method
        pass

class model_wsdl_Binding(wsdl_IBinding, wsdl_ExtensibleElement):

    def __init__(self, qName: str, undefined: bool, model_wsdl_Binding: "PortType" = None, model_wsdl_Binding370: set["BindingOperation"] = None):
        self.qName = qName
        self.undefined = undefined
        self.model_wsdl_Binding = model_wsdl_Binding
        self.model_wsdl_Binding370 = model_wsdl_Binding370 if model_wsdl_Binding370 is not None else set()
        
    @property
    def undefined(self) -> bool:
        return self.__undefined

    @undefined.setter
    def undefined(self, undefined: bool):
        self.__undefined = undefined

    @property
    def qName(self) -> str:
        return self.__qName

    @qName.setter
    def qName(self, qName: str):
        self.__qName = qName

    @property
    def model_wsdl_Binding(self):
        return self.__model_wsdl_Binding

    @model_wsdl_Binding.setter
    def model_wsdl_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Binding__model_wsdl_Binding", None)
        self.__model_wsdl_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PortType368"):
                opp_val = getattr(old_value, "PortType368", None)
                if opp_val == self:
                    setattr(old_value, "PortType368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PortType368"):
                opp_val = getattr(value, "PortType368", None)
                setattr(value, "PortType368", self)

    @property
    def model_wsdl_Binding370(self):
        return self.__model_wsdl_Binding370

    @model_wsdl_Binding370.setter
    def model_wsdl_Binding370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Binding__model_wsdl_Binding370", None)
        self.__model_wsdl_Binding370 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BindingOperation"):
                    opp_val = getattr(item, "BindingOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "BindingOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BindingOperation"):
                    opp_val = getattr(item, "BindingOperation", None)
                    
                    setattr(item, "BindingOperation", self)
                    

class model_wsdl_BindingFault(wsdl_IBindingFault, wsdl_ExtensibleElement):

    def __init__(self, name: str, model_wsdl_BindingFault: "Fault" = None):
        self.name = name
        self.model_wsdl_BindingFault = model_wsdl_BindingFault
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_wsdl_BindingFault(self):
        return self.__model_wsdl_BindingFault

    @model_wsdl_BindingFault.setter
    def model_wsdl_BindingFault(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_BindingFault__model_wsdl_BindingFault", None)
        self.__model_wsdl_BindingFault = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fault406"):
                opp_val = getattr(old_value, "Fault406", None)
                if opp_val == self:
                    setattr(old_value, "Fault406", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fault406"):
                opp_val = getattr(value, "Fault406", None)
                setattr(value, "Fault406", self)

    def setFault(self, fault: str):
        # TODO: Implement setFault method
        pass

    def getFault(self) -> str:
        # TODO: Implement getFault method
        pass

class model_wsdl_Port(wsdl_IPort, wsdl_ExtensibleElement):

    def __init__(self, name: str, model_wsdl_Port: "Binding" = None):
        self.name = name
        self.model_wsdl_Port = model_wsdl_Port
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_wsdl_Port(self):
        return self.__model_wsdl_Port

    @model_wsdl_Port.setter
    def model_wsdl_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Port__model_wsdl_Port", None)
        self.__model_wsdl_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Binding"):
                opp_val = getattr(old_value, "Binding", None)
                if opp_val == self:
                    setattr(old_value, "Binding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Binding"):
                opp_val = getattr(value, "Binding", None)
                setattr(value, "Binding", self)

class model_wsdl_Definition(wsdl_IDefinition, wsdl_ExtensibleElement):

    def __init__(self, targetNamespace: str, location: str, qName: str, encoding: str, model_wsdl_Definition: set["Import"] = None, model_wsdl_Definition383: "Types" = None, model_wsdl_Definition385: set["Message"] = None, model_wsdl_Definition388: set["PortType"] = None, model_wsdl_Definition391: set["Binding"] = None, model_wsdl_Definition394: set["Service"] = None, model_wsdl_Definition396: set["Namespace"] = None):
        self.targetNamespace = targetNamespace
        self.location = location
        self.qName = qName
        self.encoding = encoding
        self.model_wsdl_Definition = model_wsdl_Definition if model_wsdl_Definition is not None else set()
        self.model_wsdl_Definition383 = model_wsdl_Definition383
        self.model_wsdl_Definition385 = model_wsdl_Definition385 if model_wsdl_Definition385 is not None else set()
        self.model_wsdl_Definition388 = model_wsdl_Definition388 if model_wsdl_Definition388 is not None else set()
        self.model_wsdl_Definition391 = model_wsdl_Definition391 if model_wsdl_Definition391 is not None else set()
        self.model_wsdl_Definition394 = model_wsdl_Definition394 if model_wsdl_Definition394 is not None else set()
        self.model_wsdl_Definition396 = model_wsdl_Definition396 if model_wsdl_Definition396 is not None else set()
        
    @property
    def encoding(self) -> str:
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding: str):
        self.__encoding = encoding

    @property
    def qName(self) -> str:
        return self.__qName

    @qName.setter
    def qName(self, qName: str):
        self.__qName = qName

    @property
    def targetNamespace(self) -> str:
        return self.__targetNamespace

    @targetNamespace.setter
    def targetNamespace(self, targetNamespace: str):
        self.__targetNamespace = targetNamespace

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def model_wsdl_Definition391(self):
        return self.__model_wsdl_Definition391

    @model_wsdl_Definition391.setter
    def model_wsdl_Definition391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Definition__model_wsdl_Definition391", None)
        self.__model_wsdl_Definition391 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Binding392"):
                    opp_val = getattr(item, "Binding392", None)
                    
                    if opp_val == self:
                        setattr(item, "Binding392", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Binding392"):
                    opp_val = getattr(item, "Binding392", None)
                    
                    setattr(item, "Binding392", self)
                    

    @property
    def model_wsdl_Definition394(self):
        return self.__model_wsdl_Definition394

    @model_wsdl_Definition394.setter
    def model_wsdl_Definition394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Definition__model_wsdl_Definition394", None)
        self.__model_wsdl_Definition394 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    if opp_val == self:
                        setattr(item, "Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    setattr(item, "Service", self)
                    

    @property
    def model_wsdl_Definition388(self):
        return self.__model_wsdl_Definition388

    @model_wsdl_Definition388.setter
    def model_wsdl_Definition388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Definition__model_wsdl_Definition388", None)
        self.__model_wsdl_Definition388 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PortType389"):
                    opp_val = getattr(item, "PortType389", None)
                    
                    if opp_val == self:
                        setattr(item, "PortType389", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PortType389"):
                    opp_val = getattr(item, "PortType389", None)
                    
                    setattr(item, "PortType389", self)
                    

    @property
    def model_wsdl_Definition385(self):
        return self.__model_wsdl_Definition385

    @model_wsdl_Definition385.setter
    def model_wsdl_Definition385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Definition__model_wsdl_Definition385", None)
        self.__model_wsdl_Definition385 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Message386"):
                    opp_val = getattr(item, "Message386", None)
                    
                    if opp_val == self:
                        setattr(item, "Message386", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Message386"):
                    opp_val = getattr(item, "Message386", None)
                    
                    setattr(item, "Message386", self)
                    

    @property
    def model_wsdl_Definition(self):
        return self.__model_wsdl_Definition

    @model_wsdl_Definition.setter
    def model_wsdl_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Definition__model_wsdl_Definition", None)
        self.__model_wsdl_Definition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Import"):
                    opp_val = getattr(item, "Import", None)
                    
                    if opp_val == self:
                        setattr(item, "Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Import"):
                    opp_val = getattr(item, "Import", None)
                    
                    setattr(item, "Import", self)
                    

    @property
    def model_wsdl_Definition383(self):
        return self.__model_wsdl_Definition383

    @model_wsdl_Definition383.setter
    def model_wsdl_Definition383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Definition__model_wsdl_Definition383", None)
        self.__model_wsdl_Definition383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Types"):
                opp_val = getattr(old_value, "Types", None)
                if opp_val == self:
                    setattr(old_value, "Types", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Types"):
                opp_val = getattr(value, "Types", None)
                setattr(value, "Types", self)

    @property
    def model_wsdl_Definition396(self):
        return self.__model_wsdl_Definition396

    @model_wsdl_Definition396.setter
    def model_wsdl_Definition396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Definition__model_wsdl_Definition396", None)
        self.__model_wsdl_Definition396 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Namespace"):
                    opp_val = getattr(item, "Namespace", None)
                    
                    if opp_val == self:
                        setattr(item, "Namespace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Namespace"):
                    opp_val = getattr(item, "Namespace", None)
                    
                    setattr(item, "Namespace", self)
                    

    def setDocument(self, document: str):
        # TODO: Implement setDocument method
        pass

    def getDocument(self) -> str:
        # TODO: Implement getDocument method
        pass

class model_wsdl_BindingInput(wsdl_IBindingInput, wsdl_ExtensibleElement):

    def __init__(self, name: str, model_wsdl_BindingInput: "Input" = None):
        self.name = name
        self.model_wsdl_BindingInput = model_wsdl_BindingInput
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_wsdl_BindingInput(self):
        return self.__model_wsdl_BindingInput

    @model_wsdl_BindingInput.setter
    def model_wsdl_BindingInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_BindingInput__model_wsdl_BindingInput", None)
        self.__model_wsdl_BindingInput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Input402"):
                opp_val = getattr(old_value, "Input402", None)
                if opp_val == self:
                    setattr(old_value, "Input402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Input402"):
                opp_val = getattr(value, "Input402", None)
                setattr(value, "Input402", self)

    def setInput(self, input: str):
        # TODO: Implement setInput method
        pass

    def getInput(self) -> str:
        # TODO: Implement getInput method
        pass

class model_wsdl_Part(wsdl_IPart, wsdl_ExtensibleElement):

    def __init__(self, name: str, elementName: str, typeName: str, model_wsdl_Part: "XSDTypeDefinition" = None, model_wsdl_Part362: "XSDElementDeclaration" = None, model_wsdl_Part365: "Message" = None):
        self.name = name
        self.elementName = elementName
        self.typeName = typeName
        self.model_wsdl_Part = model_wsdl_Part
        self.model_wsdl_Part362 = model_wsdl_Part362
        self.model_wsdl_Part365 = model_wsdl_Part365
        
    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_wsdl_Part362(self):
        return self.__model_wsdl_Part362

    @model_wsdl_Part362.setter
    def model_wsdl_Part362(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Part__model_wsdl_Part362", None)
        self.__model_wsdl_Part362 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDElementDeclaration363"):
                opp_val = getattr(old_value, "XSDElementDeclaration363", None)
                if opp_val == self:
                    setattr(old_value, "XSDElementDeclaration363", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDElementDeclaration363"):
                opp_val = getattr(value, "XSDElementDeclaration363", None)
                setattr(value, "XSDElementDeclaration363", self)

    @property
    def model_wsdl_Part365(self):
        return self.__model_wsdl_Part365

    @model_wsdl_Part365.setter
    def model_wsdl_Part365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Part__model_wsdl_Part365", None)
        self.__model_wsdl_Part365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Message366"):
                opp_val = getattr(old_value, "Message366", None)
                if opp_val == self:
                    setattr(old_value, "Message366", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Message366"):
                opp_val = getattr(value, "Message366", None)
                setattr(value, "Message366", self)

    @property
    def model_wsdl_Part(self):
        return self.__model_wsdl_Part

    @model_wsdl_Part.setter
    def model_wsdl_Part(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Part__model_wsdl_Part", None)
        self.__model_wsdl_Part = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTypeDefinition360"):
                opp_val = getattr(old_value, "XSDTypeDefinition360", None)
                if opp_val == self:
                    setattr(old_value, "XSDTypeDefinition360", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTypeDefinition360"):
                opp_val = getattr(value, "XSDTypeDefinition360", None)
                setattr(value, "XSDTypeDefinition360", self)

class model_wsdl_Message(wsdl_IMessage, wsdl_ExtensibleElement):

    def __init__(self, qName: str, undefined: bool, model_wsdl_Message: set["Part"] = None):
        self.qName = qName
        self.undefined = undefined
        self.model_wsdl_Message = model_wsdl_Message if model_wsdl_Message is not None else set()
        
    @property
    def qName(self) -> str:
        return self.__qName

    @qName.setter
    def qName(self, qName: str):
        self.__qName = qName

    @property
    def undefined(self) -> bool:
        return self.__undefined

    @undefined.setter
    def undefined(self, undefined: bool):
        self.__undefined = undefined

    @property
    def model_wsdl_Message(self):
        return self.__model_wsdl_Message

    @model_wsdl_Message.setter
    def model_wsdl_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Message__model_wsdl_Message", None)
        self.__model_wsdl_Message = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Part358"):
                    opp_val = getattr(item, "Part358", None)
                    
                    if opp_val == self:
                        setattr(item, "Part358", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Part358"):
                    opp_val = getattr(item, "Part358", None)
                    
                    setattr(item, "Part358", self)
                    

class model_wsdl_Import(wsdl_IImport, wsdl_ExtensibleElement):

    def __init__(self, namespaceURI: str, locationURI: str, model_wsdl_Import: "Definition" = None, model_wsdl_Import399: "XSDSchema" = None):
        self.namespaceURI = namespaceURI
        self.locationURI = locationURI
        self.model_wsdl_Import = model_wsdl_Import
        self.model_wsdl_Import399 = model_wsdl_Import399
        
    @property
    def namespaceURI(self) -> str:
        return self.__namespaceURI

    @namespaceURI.setter
    def namespaceURI(self, namespaceURI: str):
        self.__namespaceURI = namespaceURI

    @property
    def locationURI(self) -> str:
        return self.__locationURI

    @locationURI.setter
    def locationURI(self, locationURI: str):
        self.__locationURI = locationURI

    @property
    def model_wsdl_Import(self):
        return self.__model_wsdl_Import

    @model_wsdl_Import.setter
    def model_wsdl_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Import__model_wsdl_Import", None)
        self.__model_wsdl_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Definition"):
                opp_val = getattr(old_value, "Definition", None)
                if opp_val == self:
                    setattr(old_value, "Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Definition"):
                opp_val = getattr(value, "Definition", None)
                setattr(value, "Definition", self)

    @property
    def model_wsdl_Import399(self):
        return self.__model_wsdl_Import399

    @model_wsdl_Import399.setter
    def model_wsdl_Import399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Import__model_wsdl_Import399", None)
        self.__model_wsdl_Import399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDSchema"):
                opp_val = getattr(old_value, "XSDSchema", None)
                if opp_val == self:
                    setattr(old_value, "XSDSchema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDSchema"):
                opp_val = getattr(value, "XSDSchema", None)
                setattr(value, "XSDSchema", self)

    def setSchema(self, schema: str):
        # TODO: Implement setSchema method
        pass

    def getSchema(self) -> str:
        # TODO: Implement getSchema method
        pass

class model_wsdl_Service(wsdl_IService, wsdl_ExtensibleElement):

    def __init__(self, qName: str, undefined: bool, model_wsdl_Service: set["Port"] = None):
        self.qName = qName
        self.undefined = undefined
        self.model_wsdl_Service = model_wsdl_Service if model_wsdl_Service is not None else set()
        
    @property
    def qName(self) -> str:
        return self.__qName

    @qName.setter
    def qName(self, qName: str):
        self.__qName = qName

    @property
    def undefined(self) -> bool:
        return self.__undefined

    @undefined.setter
    def undefined(self, undefined: bool):
        self.__undefined = undefined

    @property
    def model_wsdl_Service(self):
        return self.__model_wsdl_Service

    @model_wsdl_Service.setter
    def model_wsdl_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_Service__model_wsdl_Service", None)
        self.__model_wsdl_Service = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Port"):
                    opp_val = getattr(item, "Port", None)
                    
                    if opp_val == self:
                        setattr(item, "Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Port"):
                    opp_val = getattr(item, "Port", None)
                    
                    setattr(item, "Port", self)
                    

class model_wsdl_PortType(wsdl_IPortType, wsdl_ExtensibleElement):

    def __init__(self, qName: str, undefined: bool, model_wsdl_PortType: set["Operation"] = None):
        self.qName = qName
        self.undefined = undefined
        self.model_wsdl_PortType = model_wsdl_PortType if model_wsdl_PortType is not None else set()
        
    @property
    def undefined(self) -> bool:
        return self.__undefined

    @undefined.setter
    def undefined(self, undefined: bool):
        self.__undefined = undefined

    @property
    def qName(self) -> str:
        return self.__qName

    @qName.setter
    def qName(self, qName: str):
        self.__qName = qName

    @property
    def model_wsdl_PortType(self):
        return self.__model_wsdl_PortType

    @model_wsdl_PortType.setter
    def model_wsdl_PortType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_PortType__model_wsdl_PortType", None)
        self.__model_wsdl_PortType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation348"):
                    opp_val = getattr(item, "Operation348", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation348", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation348"):
                    opp_val = getattr(item, "Operation348", None)
                    
                    setattr(item, "Operation348", self)
                    

class model_wsdl_WSDLElement(ABC):

    def __init__(self, documentationElement: str, element: str):
        self.documentationElement = documentationElement
        self.element = element
        
    @property
    def element(self) -> str:
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element

    @property
    def documentationElement(self) -> str:
        return self.__documentationElement

    @documentationElement.setter
    def documentationElement(self, documentationElement: str):
        self.__documentationElement = documentationElement

    def getEnclosingDefinition(self) -> str:
        # TODO: Implement getEnclosingDefinition method
        pass

    def setEnclosingDefinition(self, definition: str):
        # TODO: Implement setEnclosingDefinition method
        pass

class ExtensibleElement:

    pass
class model_BPELExtensibleElement(ExtensibleElement):

    pass
class model_wsdl_MessageReference(ExtensibleElement):

    def __init__(self, name: str, model_wsdl_MessageReference: "Message" = None):
        self.name = name
        self.model_wsdl_MessageReference = model_wsdl_MessageReference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_wsdl_MessageReference(self):
        return self.__model_wsdl_MessageReference

    @model_wsdl_MessageReference.setter
    def model_wsdl_MessageReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_wsdl_MessageReference__model_wsdl_MessageReference", None)
        self.__model_wsdl_MessageReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Message411"):
                opp_val = getattr(old_value, "Message411", None)
                if opp_val == self:
                    setattr(old_value, "Message411", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Message411"):
                opp_val = getattr(value, "Message411", None)
                setattr(value, "Message411", self)

class WSDLElement:

    pass
class UnknownExtensibilityElement:

    pass
class model_UnknownExtensibilityAttribute(UnknownExtensibilityElement):

    pass
class Expression:

    pass
class model_Branches(Expression):

    def __init__(self, countCompletedBranchesOnly: str, model_Branches: "model_CompletionCondition" = None):
        self.countCompletedBranchesOnly = countCompletedBranchesOnly
        self.model_Branches = model_Branches
        
    @property
    def countCompletedBranchesOnly(self) -> str:
        return self.__countCompletedBranchesOnly

    @countCompletedBranchesOnly.setter
    def countCompletedBranchesOnly(self, countCompletedBranchesOnly: str):
        self.__countCompletedBranchesOnly = countCompletedBranchesOnly

    @property
    def model_Branches(self):
        return self.__model_Branches

    @model_Branches.setter
    def model_Branches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Branches__model_Branches", None)
        self.__model_Branches = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CompletionCondition339"):
                opp_val = getattr(old_value, "model_CompletionCondition339", None)
                if opp_val == self:
                    setattr(old_value, "model_CompletionCondition339", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CompletionCondition339"):
                opp_val = getattr(value, "model_CompletionCondition339", None)
                setattr(value, "model_CompletionCondition339", self)

class model_BooleanExpression(Expression):

    pass
class ExtensibilityElement:

    pass
class model_partnerlinktype_PartnerLinkType(ExtensibilityElement):

    def __init__(self, name: str, ID: str, model_partnerlinktype_PartnerLinkType: set["Role"] = None, ExtensibilityElement: "model_wsdl_ExtensibleElement"):
        self.name = name
        self.ID = ID
        self.model_partnerlinktype_PartnerLinkType = model_partnerlinktype_PartnerLinkType if model_partnerlinktype_PartnerLinkType is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def model_partnerlinktype_PartnerLinkType(self):
        return self.__model_partnerlinktype_PartnerLinkType

    @model_partnerlinktype_PartnerLinkType.setter
    def model_partnerlinktype_PartnerLinkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_partnerlinktype_PartnerLinkType__model_partnerlinktype_PartnerLinkType", None)
        self.__model_partnerlinktype_PartnerLinkType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role723"):
                    opp_val = getattr(item, "Role723", None)
                    
                    if opp_val == self:
                        setattr(item, "Role723", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role723"):
                    opp_val = getattr(item, "Role723", None)
                    
                    setattr(item, "Role723", self)
                    

class model_messageproperties_PropertyAlias(ExtensibilityElement):

    def __init__(self, messageType: str, part: str, propertyName: str, ID: str, type: str, XSDElement: str, model_messageproperties_PropertyAlias: "Part" = None, model_messageproperties_PropertyAlias721: "Query" = None, ExtensibilityElement: "model_wsdl_ExtensibleElement"):
        self.messageType = messageType
        self.part = part
        self.propertyName = propertyName
        self.ID = ID
        self.type = type
        self.XSDElement = XSDElement
        self.model_messageproperties_PropertyAlias = model_messageproperties_PropertyAlias
        self.model_messageproperties_PropertyAlias721 = model_messageproperties_PropertyAlias721
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def messageType(self) -> str:
        return self.__messageType

    @messageType.setter
    def messageType(self, messageType: str):
        self.__messageType = messageType

    @property
    def part(self) -> str:
        return self.__part

    @part.setter
    def part(self, part: str):
        self.__part = part

    @property
    def XSDElement(self) -> str:
        return self.__XSDElement

    @XSDElement.setter
    def XSDElement(self, XSDElement: str):
        self.__XSDElement = XSDElement

    @property
    def model_messageproperties_PropertyAlias721(self):
        return self.__model_messageproperties_PropertyAlias721

    @model_messageproperties_PropertyAlias721.setter
    def model_messageproperties_PropertyAlias721(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_messageproperties_PropertyAlias__model_messageproperties_PropertyAlias721", None)
        self.__model_messageproperties_PropertyAlias721 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Query"):
                opp_val = getattr(old_value, "Query", None)
                if opp_val == self:
                    setattr(old_value, "Query", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Query"):
                opp_val = getattr(value, "Query", None)
                setattr(value, "Query", self)

    @property
    def model_messageproperties_PropertyAlias(self):
        return self.__model_messageproperties_PropertyAlias

    @model_messageproperties_PropertyAlias.setter
    def model_messageproperties_PropertyAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_messageproperties_PropertyAlias__model_messageproperties_PropertyAlias", None)
        self.__model_messageproperties_PropertyAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Part719"):
                opp_val = getattr(old_value, "Part719", None)
                if opp_val == self:
                    setattr(old_value, "Part719", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Part719"):
                opp_val = getattr(value, "Part719", None)
                setattr(value, "Part719", self)

class model_messageproperties_Property(ExtensibilityElement):

    def __init__(self, qName: str, name: str, type: str, ID: str, ExtensibilityElement: "model_wsdl_ExtensibleElement"):
        self.qName = qName
        self.name = name
        self.type = type
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def qName(self) -> str:
        return self.__qName

    @qName.setter
    def qName(self, qName: str):
        self.__qName = qName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class model_messageproperties_Query(ExtensibilityElement):

    def __init__(self, queryLanguage: str, value: str, ExtensibilityElement: "model_wsdl_ExtensibleElement"):
        self.queryLanguage = queryLanguage
        self.value = value
        
    @property
    def queryLanguage(self) -> str:
        return self.__queryLanguage

    @queryLanguage.setter
    def queryLanguage(self, queryLanguage: str):
        self.__queryLanguage = queryLanguage

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_partnerlinktype_Role(ExtensibilityElement):

    def __init__(self, ID: str, name: str, portType: str, ExtensibilityElement: "model_wsdl_ExtensibleElement"):
        self.ID = ID
        self.name = name
        self.portType = portType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def portType(self) -> str:
        return self.__portType

    @portType.setter
    def portType(self, portType: str):
        self.__portType = portType

class model_wsdl_UnknownExtensibilityElement(ExtensibilityElement):

    pass
class XSDTypeDefinition:

    pass
class model_ServiceRef(ExtensibleElement):

    def __init__(self, referenceScheme: str, value: str, model_ServiceRef: "model_From" = None):
        self.referenceScheme = referenceScheme
        self.value = value
        self.model_ServiceRef = model_ServiceRef
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def referenceScheme(self) -> str:
        return self.__referenceScheme

    @referenceScheme.setter
    def referenceScheme(self, referenceScheme: str):
        self.__referenceScheme = referenceScheme

    @property
    def model_ServiceRef(self):
        return self.__model_ServiceRef

    @model_ServiceRef.setter
    def model_ServiceRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ServiceRef__model_ServiceRef", None)
        self.__model_ServiceRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_From165"):
                opp_val = getattr(old_value, "model_From165", None)
                if opp_val == self:
                    setattr(old_value, "model_From165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_From165"):
                opp_val = getattr(value, "model_From165", None)
                setattr(value, "model_From165", self)

class AbstractAssignBound:

    pass
class model_Query(WSDLElement):

    def __init__(self, value: str, queryLanguage: str, model_Query: "model_AbstractAssignBound" = None):
        self.value = value
        self.queryLanguage = queryLanguage
        self.model_Query = model_Query
        
    @property
    def queryLanguage(self) -> str:
        return self.__queryLanguage

    @queryLanguage.setter
    def queryLanguage(self, queryLanguage: str):
        self.__queryLanguage = queryLanguage

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def model_Query(self):
        return self.__model_Query

    @model_Query.setter
    def model_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Query__model_Query", None)
        self.__model_Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractAssignBound160"):
                opp_val = getattr(old_value, "model_AbstractAssignBound160", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractAssignBound160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractAssignBound160"):
                opp_val = getattr(value, "model_AbstractAssignBound160", None)
                setattr(value, "model_AbstractAssignBound160", self)

class model_AbstractAssignBound(ABC):

    pass
class Part:

    pass
class model_Condition(Expression):

    pass
class model_Expression(ExtensibilityElement):

    def __init__(self, body: str, expressionLanguage: str, opaque: str, model_Expression: "model_Wait" = None, model_Expression86: "model_Wait" = None, model_Expression107: "model_OnAlarm" = None, model_Expression110: "model_OnAlarm" = None, model_Expression113: "model_OnAlarm" = None, model_Expression163: "model_AbstractAssignBound" = None, model_Expression297: "model_ForEach" = None, model_Expression300: "model_ForEach" = None, ExtensibilityElement: "model_wsdl_ExtensibleElement"):
        self.body = body
        self.expressionLanguage = expressionLanguage
        self.opaque = opaque
        self.model_Expression = model_Expression
        self.model_Expression86 = model_Expression86
        self.model_Expression107 = model_Expression107
        self.model_Expression110 = model_Expression110
        self.model_Expression113 = model_Expression113
        self.model_Expression163 = model_Expression163
        self.model_Expression297 = model_Expression297
        self.model_Expression300 = model_Expression300
        
    @property
    def opaque(self) -> str:
        return self.__opaque

    @opaque.setter
    def opaque(self, opaque: str):
        self.__opaque = opaque

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

    @property
    def model_Expression300(self):
        return self.__model_Expression300

    @model_Expression300.setter
    def model_Expression300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Expression__model_Expression300", None)
        self.__model_Expression300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ForEach299"):
                opp_val = getattr(old_value, "model_ForEach299", None)
                if opp_val == self:
                    setattr(old_value, "model_ForEach299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ForEach299"):
                opp_val = getattr(value, "model_ForEach299", None)
                setattr(value, "model_ForEach299", self)

    @property
    def model_Expression163(self):
        return self.__model_Expression163

    @model_Expression163.setter
    def model_Expression163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Expression__model_Expression163", None)
        self.__model_Expression163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractAssignBound162"):
                opp_val = getattr(old_value, "model_AbstractAssignBound162", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractAssignBound162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractAssignBound162"):
                opp_val = getattr(value, "model_AbstractAssignBound162", None)
                setattr(value, "model_AbstractAssignBound162", self)

    @property
    def model_Expression(self):
        return self.__model_Expression

    @model_Expression.setter
    def model_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Expression__model_Expression", None)
        self.__model_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Wait"):
                opp_val = getattr(old_value, "model_Wait", None)
                if opp_val == self:
                    setattr(old_value, "model_Wait", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Wait"):
                opp_val = getattr(value, "model_Wait", None)
                setattr(value, "model_Wait", self)

    @property
    def model_Expression110(self):
        return self.__model_Expression110

    @model_Expression110.setter
    def model_Expression110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Expression__model_Expression110", None)
        self.__model_Expression110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnAlarm109"):
                opp_val = getattr(old_value, "model_OnAlarm109", None)
                if opp_val == self:
                    setattr(old_value, "model_OnAlarm109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnAlarm109"):
                opp_val = getattr(value, "model_OnAlarm109", None)
                setattr(value, "model_OnAlarm109", self)

    @property
    def model_Expression297(self):
        return self.__model_Expression297

    @model_Expression297.setter
    def model_Expression297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Expression__model_Expression297", None)
        self.__model_Expression297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ForEach"):
                opp_val = getattr(old_value, "model_ForEach", None)
                if opp_val == self:
                    setattr(old_value, "model_ForEach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ForEach"):
                opp_val = getattr(value, "model_ForEach", None)
                setattr(value, "model_ForEach", self)

    @property
    def model_Expression107(self):
        return self.__model_Expression107

    @model_Expression107.setter
    def model_Expression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Expression__model_Expression107", None)
        self.__model_Expression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnAlarm106"):
                opp_val = getattr(old_value, "model_OnAlarm106", None)
                if opp_val == self:
                    setattr(old_value, "model_OnAlarm106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnAlarm106"):
                opp_val = getattr(value, "model_OnAlarm106", None)
                setattr(value, "model_OnAlarm106", self)

    @property
    def model_Expression86(self):
        return self.__model_Expression86

    @model_Expression86.setter
    def model_Expression86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Expression__model_Expression86", None)
        self.__model_Expression86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Wait85"):
                opp_val = getattr(old_value, "model_Wait85", None)
                if opp_val == self:
                    setattr(old_value, "model_Wait85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Wait85"):
                opp_val = getattr(value, "model_Wait85", None)
                setattr(value, "model_Wait85", self)

    @property
    def model_Expression113(self):
        return self.__model_Expression113

    @model_Expression113.setter
    def model_Expression113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Expression__model_Expression113", None)
        self.__model_Expression113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnAlarm112"):
                opp_val = getattr(old_value, "model_OnAlarm112", None)
                if opp_val == self:
                    setattr(old_value, "model_OnAlarm112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnAlarm112"):
                opp_val = getattr(value, "model_OnAlarm112", None)
                setattr(value, "model_OnAlarm112", self)

class Operation:

    pass
class Activity:

    pass
class model_Compensate(Activity):

    pass
class model_Assign(Activity):

    def __init__(self, validate: str, model_Assign: set["model_Copy"] = None):
        self.validate = validate
        self.model_Assign = model_Assign if model_Assign is not None else set()
        
    @property
    def validate(self) -> str:
        return self.__validate

    @validate.setter
    def validate(self, validate: str):
        self.__validate = validate

    @property
    def model_Assign(self):
        return self.__model_Assign

    @model_Assign.setter
    def model_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Assign__model_Assign", None)
        self.__model_Assign = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Copy"):
                    opp_val = getattr(item, "model_Copy", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Copy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Copy"):
                    opp_val = getattr(item, "model_Copy", None)
                    
                    setattr(item, "model_Copy", self)
                    

class model_PartnerActivity(Activity):

    pass
class model_Wait(Activity):

    pass
class model_If(Activity):

    pass
class model_RepeatUntil(Activity):

    pass
class model_ExtensionActivity(Activity):

    pass
class model_Rethrow(Activity):

    pass
class model_Exit(Activity):

    pass
class model_OpaqueActivity(Activity):

    pass
class model_ForEach(Activity):

    def __init__(self, parallel: str, model_ForEach302: "model_Variable" = None, model_ForEach: "model_Expression" = None, model_ForEach299: "model_Expression" = None, model_ForEach305: "model_CompletionCondition" = None, model_ForEach308: "model_Activity" = None):
        self.parallel = parallel
        self.model_ForEach302 = model_ForEach302
        self.model_ForEach = model_ForEach
        self.model_ForEach299 = model_ForEach299
        self.model_ForEach305 = model_ForEach305
        self.model_ForEach308 = model_ForEach308
        
    @property
    def parallel(self) -> str:
        return self.__parallel

    @parallel.setter
    def parallel(self, parallel: str):
        self.__parallel = parallel

    @property
    def model_ForEach308(self):
        return self.__model_ForEach308

    @model_ForEach308.setter
    def model_ForEach308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ForEach__model_ForEach308", None)
        self.__model_ForEach308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Activity309"):
                opp_val = getattr(old_value, "model_Activity309", None)
                if opp_val == self:
                    setattr(old_value, "model_Activity309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Activity309"):
                opp_val = getattr(value, "model_Activity309", None)
                setattr(value, "model_Activity309", self)

    @property
    def model_ForEach302(self):
        return self.__model_ForEach302

    @model_ForEach302.setter
    def model_ForEach302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ForEach__model_ForEach302", None)
        self.__model_ForEach302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Variable303"):
                opp_val = getattr(old_value, "model_Variable303", None)
                if opp_val == self:
                    setattr(old_value, "model_Variable303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Variable303"):
                opp_val = getattr(value, "model_Variable303", None)
                setattr(value, "model_Variable303", self)

    @property
    def model_ForEach(self):
        return self.__model_ForEach

    @model_ForEach.setter
    def model_ForEach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ForEach__model_ForEach", None)
        self.__model_ForEach = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Expression297"):
                opp_val = getattr(old_value, "model_Expression297", None)
                if opp_val == self:
                    setattr(old_value, "model_Expression297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Expression297"):
                opp_val = getattr(value, "model_Expression297", None)
                setattr(value, "model_Expression297", self)

    @property
    def model_ForEach299(self):
        return self.__model_ForEach299

    @model_ForEach299.setter
    def model_ForEach299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ForEach__model_ForEach299", None)
        self.__model_ForEach299 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Expression300"):
                opp_val = getattr(old_value, "model_Expression300", None)
                if opp_val == self:
                    setattr(old_value, "model_Expression300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Expression300"):
                opp_val = getattr(value, "model_Expression300", None)
                setattr(value, "model_Expression300", self)

    @property
    def model_ForEach305(self):
        return self.__model_ForEach305

    @model_ForEach305.setter
    def model_ForEach305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ForEach__model_ForEach305", None)
        self.__model_ForEach305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CompletionCondition306"):
                opp_val = getattr(old_value, "model_CompletionCondition306", None)
                if opp_val == self:
                    setattr(old_value, "model_CompletionCondition306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CompletionCondition306"):
                opp_val = getattr(value, "model_CompletionCondition306", None)
                setattr(value, "model_CompletionCondition306", self)

class model_CompensateScope(Activity):

    pass
class model_Scope(Activity):

    def __init__(self, isolated: str, exitOnStandardFault: str, model_Scope: "model_FaultHandler" = None, model_Scope122: "model_CompensationHandler" = None, model_Scope125: "model_Activity" = None, model_Scope128: "model_Variables" = None, model_Scope131: "model_CorrelationSets" = None, model_Scope134: "model_EventHandler" = None, model_Scope137: "model_PartnerLinks" = None, model_Scope140: "model_TerminationHandler" = None, model_Scope142: "model_MessageExchanges" = None):
        self.isolated = isolated
        self.exitOnStandardFault = exitOnStandardFault
        self.model_Scope = model_Scope
        self.model_Scope122 = model_Scope122
        self.model_Scope125 = model_Scope125
        self.model_Scope128 = model_Scope128
        self.model_Scope131 = model_Scope131
        self.model_Scope134 = model_Scope134
        self.model_Scope137 = model_Scope137
        self.model_Scope140 = model_Scope140
        self.model_Scope142 = model_Scope142
        
    @property
    def exitOnStandardFault(self) -> str:
        return self.__exitOnStandardFault

    @exitOnStandardFault.setter
    def exitOnStandardFault(self, exitOnStandardFault: str):
        self.__exitOnStandardFault = exitOnStandardFault

    @property
    def isolated(self) -> str:
        return self.__isolated

    @isolated.setter
    def isolated(self, isolated: str):
        self.__isolated = isolated

    @property
    def model_Scope125(self):
        return self.__model_Scope125

    @model_Scope125.setter
    def model_Scope125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Scope__model_Scope125", None)
        self.__model_Scope125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Activity126"):
                opp_val = getattr(old_value, "model_Activity126", None)
                if opp_val == self:
                    setattr(old_value, "model_Activity126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Activity126"):
                opp_val = getattr(value, "model_Activity126", None)
                setattr(value, "model_Activity126", self)

    @property
    def model_Scope(self):
        return self.__model_Scope

    @model_Scope.setter
    def model_Scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Scope__model_Scope", None)
        self.__model_Scope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FaultHandler120"):
                opp_val = getattr(old_value, "model_FaultHandler120", None)
                if opp_val == self:
                    setattr(old_value, "model_FaultHandler120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FaultHandler120"):
                opp_val = getattr(value, "model_FaultHandler120", None)
                setattr(value, "model_FaultHandler120", self)

    @property
    def model_Scope142(self):
        return self.__model_Scope142

    @model_Scope142.setter
    def model_Scope142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Scope__model_Scope142", None)
        self.__model_Scope142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MessageExchanges143"):
                opp_val = getattr(old_value, "model_MessageExchanges143", None)
                if opp_val == self:
                    setattr(old_value, "model_MessageExchanges143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MessageExchanges143"):
                opp_val = getattr(value, "model_MessageExchanges143", None)
                setattr(value, "model_MessageExchanges143", self)

    @property
    def model_Scope134(self):
        return self.__model_Scope134

    @model_Scope134.setter
    def model_Scope134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Scope__model_Scope134", None)
        self.__model_Scope134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_EventHandler135"):
                opp_val = getattr(old_value, "model_EventHandler135", None)
                if opp_val == self:
                    setattr(old_value, "model_EventHandler135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_EventHandler135"):
                opp_val = getattr(value, "model_EventHandler135", None)
                setattr(value, "model_EventHandler135", self)

    @property
    def model_Scope128(self):
        return self.__model_Scope128

    @model_Scope128.setter
    def model_Scope128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Scope__model_Scope128", None)
        self.__model_Scope128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Variables129"):
                opp_val = getattr(old_value, "model_Variables129", None)
                if opp_val == self:
                    setattr(old_value, "model_Variables129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Variables129"):
                opp_val = getattr(value, "model_Variables129", None)
                setattr(value, "model_Variables129", self)

    @property
    def model_Scope140(self):
        return self.__model_Scope140

    @model_Scope140.setter
    def model_Scope140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Scope__model_Scope140", None)
        self.__model_Scope140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TerminationHandler"):
                opp_val = getattr(old_value, "model_TerminationHandler", None)
                if opp_val == self:
                    setattr(old_value, "model_TerminationHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TerminationHandler"):
                opp_val = getattr(value, "model_TerminationHandler", None)
                setattr(value, "model_TerminationHandler", self)

    @property
    def model_Scope122(self):
        return self.__model_Scope122

    @model_Scope122.setter
    def model_Scope122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Scope__model_Scope122", None)
        self.__model_Scope122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CompensationHandler123"):
                opp_val = getattr(old_value, "model_CompensationHandler123", None)
                if opp_val == self:
                    setattr(old_value, "model_CompensationHandler123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CompensationHandler123"):
                opp_val = getattr(value, "model_CompensationHandler123", None)
                setattr(value, "model_CompensationHandler123", self)

    @property
    def model_Scope131(self):
        return self.__model_Scope131

    @model_Scope131.setter
    def model_Scope131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Scope__model_Scope131", None)
        self.__model_Scope131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CorrelationSets132"):
                opp_val = getattr(old_value, "model_CorrelationSets132", None)
                if opp_val == self:
                    setattr(old_value, "model_CorrelationSets132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CorrelationSets132"):
                opp_val = getattr(value, "model_CorrelationSets132", None)
                setattr(value, "model_CorrelationSets132", self)

    @property
    def model_Scope137(self):
        return self.__model_Scope137

    @model_Scope137.setter
    def model_Scope137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Scope__model_Scope137", None)
        self.__model_Scope137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PartnerLinks138"):
                opp_val = getattr(old_value, "model_PartnerLinks138", None)
                if opp_val == self:
                    setattr(old_value, "model_PartnerLinks138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PartnerLinks138"):
                opp_val = getattr(value, "model_PartnerLinks138", None)
                setattr(value, "model_PartnerLinks138", self)

class model_Validate(Activity):

    pass
class model_Throw(Activity):

    def __init__(self, faultName: str, model_Throw: "model_Variable" = None):
        self.faultName = faultName
        self.model_Throw = model_Throw
        
    @property
    def faultName(self) -> str:
        return self.__faultName

    @faultName.setter
    def faultName(self, faultName: str):
        self.__faultName = faultName

    @property
    def model_Throw(self):
        return self.__model_Throw

    @model_Throw.setter
    def model_Throw(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Throw__model_Throw", None)
        self.__model_Throw = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Variable82"):
                opp_val = getattr(old_value, "model_Variable82", None)
                if opp_val == self:
                    setattr(old_value, "model_Variable82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Variable82"):
                opp_val = getattr(value, "model_Variable82", None)
                setattr(value, "model_Variable82", self)

class model_Sequence(Activity):

    pass
class model_Pick(Activity):

    def __init__(self, createInstance: str, model_Pick: set["model_OnMessage"] = None, model_Pick95: set["model_OnAlarm"] = None):
        self.createInstance = createInstance
        self.model_Pick = model_Pick if model_Pick is not None else set()
        self.model_Pick95 = model_Pick95 if model_Pick95 is not None else set()
        
    @property
    def createInstance(self) -> str:
        return self.__createInstance

    @createInstance.setter
    def createInstance(self, createInstance: str):
        self.__createInstance = createInstance

    @property
    def model_Pick(self):
        return self.__model_Pick

    @model_Pick.setter
    def model_Pick(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Pick__model_Pick", None)
        self.__model_Pick = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_OnMessage"):
                    opp_val = getattr(item, "model_OnMessage", None)
                    
                    if opp_val == self:
                        setattr(item, "model_OnMessage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_OnMessage"):
                    opp_val = getattr(item, "model_OnMessage", None)
                    
                    setattr(item, "model_OnMessage", self)
                    

    @property
    def model_Pick95(self):
        return self.__model_Pick95

    @model_Pick95.setter
    def model_Pick95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Pick__model_Pick95", None)
        self.__model_Pick95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_OnAlarm"):
                    opp_val = getattr(item, "model_OnAlarm", None)
                    
                    if opp_val == self:
                        setattr(item, "model_OnAlarm", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_OnAlarm"):
                    opp_val = getattr(item, "model_OnAlarm", None)
                    
                    setattr(item, "model_OnAlarm", self)
                    

class model_Empty(Activity):

    pass
class model_While(Activity):

    pass
class model_Flow(Activity):

    pass
class XSDElementDeclaration:

    pass
class Message:

    pass
class PortType:

    pass
class PartnerActivity:

    pass
class model_Receive(PartnerActivity):

    def __init__(self, createInstance: str, model_Receive: "model_Variable" = None, model_Receive76: "model_FromParts" = None, model_Receive79: "model_MessageExchange" = None):
        self.createInstance = createInstance
        self.model_Receive = model_Receive
        self.model_Receive76 = model_Receive76
        self.model_Receive79 = model_Receive79
        
    @property
    def createInstance(self) -> str:
        return self.__createInstance

    @createInstance.setter
    def createInstance(self, createInstance: str):
        self.__createInstance = createInstance

    @property
    def model_Receive79(self):
        return self.__model_Receive79

    @model_Receive79.setter
    def model_Receive79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Receive__model_Receive79", None)
        self.__model_Receive79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MessageExchange80"):
                opp_val = getattr(old_value, "model_MessageExchange80", None)
                if opp_val == self:
                    setattr(old_value, "model_MessageExchange80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MessageExchange80"):
                opp_val = getattr(value, "model_MessageExchange80", None)
                setattr(value, "model_MessageExchange80", self)

    @property
    def model_Receive(self):
        return self.__model_Receive

    @model_Receive.setter
    def model_Receive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Receive__model_Receive", None)
        self.__model_Receive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Variable74"):
                opp_val = getattr(old_value, "model_Variable74", None)
                if opp_val == self:
                    setattr(old_value, "model_Variable74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Variable74"):
                opp_val = getattr(value, "model_Variable74", None)
                setattr(value, "model_Variable74", self)

    @property
    def model_Receive76(self):
        return self.__model_Receive76

    @model_Receive76.setter
    def model_Receive76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Receive__model_Receive76", None)
        self.__model_Receive76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FromParts77"):
                opp_val = getattr(old_value, "model_FromParts77", None)
                if opp_val == self:
                    setattr(old_value, "model_FromParts77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FromParts77"):
                opp_val = getattr(value, "model_FromParts77", None)
                setattr(value, "model_FromParts77", self)

class model_Reply(PartnerActivity, Activity):

    def __init__(self, faultName: str, model_Reply: "model_Variable" = None, model_Reply61: "model_ToParts" = None, model_Reply64: "model_MessageExchange" = None):
        self.faultName = faultName
        self.model_Reply = model_Reply
        self.model_Reply61 = model_Reply61
        self.model_Reply64 = model_Reply64
        
    @property
    def faultName(self) -> str:
        return self.__faultName

    @faultName.setter
    def faultName(self, faultName: str):
        self.__faultName = faultName

    @property
    def model_Reply64(self):
        return self.__model_Reply64

    @model_Reply64.setter
    def model_Reply64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Reply__model_Reply64", None)
        self.__model_Reply64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MessageExchange"):
                opp_val = getattr(old_value, "model_MessageExchange", None)
                if opp_val == self:
                    setattr(old_value, "model_MessageExchange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MessageExchange"):
                opp_val = getattr(value, "model_MessageExchange", None)
                setattr(value, "model_MessageExchange", self)

    @property
    def model_Reply(self):
        return self.__model_Reply

    @model_Reply.setter
    def model_Reply(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Reply__model_Reply", None)
        self.__model_Reply = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Variable59"):
                opp_val = getattr(old_value, "model_Variable59", None)
                if opp_val == self:
                    setattr(old_value, "model_Variable59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Variable59"):
                opp_val = getattr(value, "model_Variable59", None)
                setattr(value, "model_Variable59", self)

    @property
    def model_Reply61(self):
        return self.__model_Reply61

    @model_Reply61.setter
    def model_Reply61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Reply__model_Reply61", None)
        self.__model_Reply61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ToParts62"):
                opp_val = getattr(old_value, "model_ToParts62", None)
                if opp_val == self:
                    setattr(old_value, "model_ToParts62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ToParts62"):
                opp_val = getattr(value, "model_ToParts62", None)
                setattr(value, "model_ToParts62", self)

class model_Invoke(PartnerActivity):

    pass
class Property:

    pass
class PartnerLinkType:

    pass
class Role:

    pass
class BPELExtensibleElement:

    pass
class model_Activity(BPELExtensibleElement):

    def __init__(self, name: str, suppressJoinFailure: str, model_Activity: "model_Process" = None, model_Activity28: "model_Targets" = None, model_Activity30: "model_Sources" = None, model_Activity53: "model_Catch" = None, model_Activity88: "model_Sequence" = None, model_Activity90: "model_While" = None, model_Activity97: "model_Flow" = None, model_Activity104: "model_OnAlarm" = None, model_Activity126: "model_Scope" = None, model_Activity145: "model_CompensateScope" = None, model_Activity148: "model_CompensationHandler" = None, model_Activity173: "model_OnMessage" = None, model_Activity202: "model_Source" = None, model_Activity209: "model_Target" = None, model_Activity226: "model_CatchAll" = None, model_Activity244: "model_OnEvent" = None, model_Activity337: "model_Else" = None, model_Activity309: "model_ForEach" = None, model_Activity311: "model_RepeatUntil" = None, model_Activity317: "model_TerminationHandler" = None, model_Activity328: "model_If" = None, model_Activity334: "model_ElseIf" = None):
        self.name = name
        self.suppressJoinFailure = suppressJoinFailure
        self.model_Activity = model_Activity
        self.model_Activity28 = model_Activity28
        self.model_Activity30 = model_Activity30
        self.model_Activity53 = model_Activity53
        self.model_Activity88 = model_Activity88
        self.model_Activity90 = model_Activity90
        self.model_Activity97 = model_Activity97
        self.model_Activity104 = model_Activity104
        self.model_Activity126 = model_Activity126
        self.model_Activity145 = model_Activity145
        self.model_Activity148 = model_Activity148
        self.model_Activity173 = model_Activity173
        self.model_Activity202 = model_Activity202
        self.model_Activity209 = model_Activity209
        self.model_Activity226 = model_Activity226
        self.model_Activity244 = model_Activity244
        self.model_Activity337 = model_Activity337
        self.model_Activity309 = model_Activity309
        self.model_Activity311 = model_Activity311
        self.model_Activity317 = model_Activity317
        self.model_Activity328 = model_Activity328
        self.model_Activity334 = model_Activity334
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def suppressJoinFailure(self) -> str:
        return self.__suppressJoinFailure

    @suppressJoinFailure.setter
    def suppressJoinFailure(self, suppressJoinFailure: str):
        self.__suppressJoinFailure = suppressJoinFailure

    @property
    def model_Activity337(self):
        return self.__model_Activity337

    @model_Activity337.setter
    def model_Activity337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity337", None)
        self.__model_Activity337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Else336"):
                opp_val = getattr(old_value, "model_Else336", None)
                if opp_val == self:
                    setattr(old_value, "model_Else336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Else336"):
                opp_val = getattr(value, "model_Else336", None)
                setattr(value, "model_Else336", self)

    @property
    def model_Activity104(self):
        return self.__model_Activity104

    @model_Activity104.setter
    def model_Activity104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity104", None)
        self.__model_Activity104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnAlarm103"):
                opp_val = getattr(old_value, "model_OnAlarm103", None)
                if opp_val == self:
                    setattr(old_value, "model_OnAlarm103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnAlarm103"):
                opp_val = getattr(value, "model_OnAlarm103", None)
                setattr(value, "model_OnAlarm103", self)

    @property
    def model_Activity126(self):
        return self.__model_Activity126

    @model_Activity126.setter
    def model_Activity126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity126", None)
        self.__model_Activity126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Scope125"):
                opp_val = getattr(old_value, "model_Scope125", None)
                if opp_val == self:
                    setattr(old_value, "model_Scope125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Scope125"):
                opp_val = getattr(value, "model_Scope125", None)
                setattr(value, "model_Scope125", self)

    @property
    def model_Activity209(self):
        return self.__model_Activity209

    @model_Activity209.setter
    def model_Activity209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity209", None)
        self.__model_Activity209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Target"):
                opp_val = getattr(old_value, "model_Target", None)
                if opp_val == self:
                    setattr(old_value, "model_Target", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Target"):
                opp_val = getattr(value, "model_Target", None)
                setattr(value, "model_Target", self)

    @property
    def model_Activity97(self):
        return self.__model_Activity97

    @model_Activity97.setter
    def model_Activity97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity97", None)
        self.__model_Activity97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Flow"):
                opp_val = getattr(old_value, "model_Flow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Flow"):
                opp_val = getattr(value, "model_Flow", None)
                if opp_val is None:
                    setattr(value, "model_Flow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Activity317(self):
        return self.__model_Activity317

    @model_Activity317.setter
    def model_Activity317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity317", None)
        self.__model_Activity317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TerminationHandler316"):
                opp_val = getattr(old_value, "model_TerminationHandler316", None)
                if opp_val == self:
                    setattr(old_value, "model_TerminationHandler316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TerminationHandler316"):
                opp_val = getattr(value, "model_TerminationHandler316", None)
                setattr(value, "model_TerminationHandler316", self)

    @property
    def model_Activity309(self):
        return self.__model_Activity309

    @model_Activity309.setter
    def model_Activity309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity309", None)
        self.__model_Activity309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ForEach308"):
                opp_val = getattr(old_value, "model_ForEach308", None)
                if opp_val == self:
                    setattr(old_value, "model_ForEach308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ForEach308"):
                opp_val = getattr(value, "model_ForEach308", None)
                setattr(value, "model_ForEach308", self)

    @property
    def model_Activity88(self):
        return self.__model_Activity88

    @model_Activity88.setter
    def model_Activity88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity88", None)
        self.__model_Activity88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Sequence"):
                opp_val = getattr(old_value, "model_Sequence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Sequence"):
                opp_val = getattr(value, "model_Sequence", None)
                if opp_val is None:
                    setattr(value, "model_Sequence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Activity(self):
        return self.__model_Activity

    @model_Activity.setter
    def model_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity", None)
        self.__model_Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Process4"):
                opp_val = getattr(old_value, "model_Process4", None)
                if opp_val == self:
                    setattr(old_value, "model_Process4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Process4"):
                opp_val = getattr(value, "model_Process4", None)
                setattr(value, "model_Process4", self)

    @property
    def model_Activity145(self):
        return self.__model_Activity145

    @model_Activity145.setter
    def model_Activity145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity145", None)
        self.__model_Activity145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CompensateScope"):
                opp_val = getattr(old_value, "model_CompensateScope", None)
                if opp_val == self:
                    setattr(old_value, "model_CompensateScope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CompensateScope"):
                opp_val = getattr(value, "model_CompensateScope", None)
                setattr(value, "model_CompensateScope", self)

    @property
    def model_Activity90(self):
        return self.__model_Activity90

    @model_Activity90.setter
    def model_Activity90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity90", None)
        self.__model_Activity90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_While"):
                opp_val = getattr(old_value, "model_While", None)
                if opp_val == self:
                    setattr(old_value, "model_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_While"):
                opp_val = getattr(value, "model_While", None)
                setattr(value, "model_While", self)

    @property
    def model_Activity173(self):
        return self.__model_Activity173

    @model_Activity173.setter
    def model_Activity173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity173", None)
        self.__model_Activity173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnMessage172"):
                opp_val = getattr(old_value, "model_OnMessage172", None)
                if opp_val == self:
                    setattr(old_value, "model_OnMessage172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnMessage172"):
                opp_val = getattr(value, "model_OnMessage172", None)
                setattr(value, "model_OnMessage172", self)

    @property
    def model_Activity328(self):
        return self.__model_Activity328

    @model_Activity328.setter
    def model_Activity328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity328", None)
        self.__model_Activity328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_If327"):
                opp_val = getattr(old_value, "model_If327", None)
                if opp_val == self:
                    setattr(old_value, "model_If327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_If327"):
                opp_val = getattr(value, "model_If327", None)
                setattr(value, "model_If327", self)

    @property
    def model_Activity334(self):
        return self.__model_Activity334

    @model_Activity334.setter
    def model_Activity334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity334", None)
        self.__model_Activity334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ElseIf333"):
                opp_val = getattr(old_value, "model_ElseIf333", None)
                if opp_val == self:
                    setattr(old_value, "model_ElseIf333", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ElseIf333"):
                opp_val = getattr(value, "model_ElseIf333", None)
                setattr(value, "model_ElseIf333", self)

    @property
    def model_Activity311(self):
        return self.__model_Activity311

    @model_Activity311.setter
    def model_Activity311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity311", None)
        self.__model_Activity311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RepeatUntil"):
                opp_val = getattr(old_value, "model_RepeatUntil", None)
                if opp_val == self:
                    setattr(old_value, "model_RepeatUntil", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RepeatUntil"):
                opp_val = getattr(value, "model_RepeatUntil", None)
                setattr(value, "model_RepeatUntil", self)

    @property
    def model_Activity30(self):
        return self.__model_Activity30

    @model_Activity30.setter
    def model_Activity30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity30", None)
        self.__model_Activity30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Sources"):
                opp_val = getattr(old_value, "model_Sources", None)
                if opp_val == self:
                    setattr(old_value, "model_Sources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Sources"):
                opp_val = getattr(value, "model_Sources", None)
                setattr(value, "model_Sources", self)

    @property
    def model_Activity53(self):
        return self.__model_Activity53

    @model_Activity53.setter
    def model_Activity53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity53", None)
        self.__model_Activity53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Catch52"):
                opp_val = getattr(old_value, "model_Catch52", None)
                if opp_val == self:
                    setattr(old_value, "model_Catch52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Catch52"):
                opp_val = getattr(value, "model_Catch52", None)
                setattr(value, "model_Catch52", self)

    @property
    def model_Activity28(self):
        return self.__model_Activity28

    @model_Activity28.setter
    def model_Activity28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity28", None)
        self.__model_Activity28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Targets"):
                opp_val = getattr(old_value, "model_Targets", None)
                if opp_val == self:
                    setattr(old_value, "model_Targets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Targets"):
                opp_val = getattr(value, "model_Targets", None)
                setattr(value, "model_Targets", self)

    @property
    def model_Activity226(self):
        return self.__model_Activity226

    @model_Activity226.setter
    def model_Activity226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity226", None)
        self.__model_Activity226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CatchAll225"):
                opp_val = getattr(old_value, "model_CatchAll225", None)
                if opp_val == self:
                    setattr(old_value, "model_CatchAll225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CatchAll225"):
                opp_val = getattr(value, "model_CatchAll225", None)
                setattr(value, "model_CatchAll225", self)

    @property
    def model_Activity202(self):
        return self.__model_Activity202

    @model_Activity202.setter
    def model_Activity202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity202", None)
        self.__model_Activity202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Source"):
                opp_val = getattr(old_value, "model_Source", None)
                if opp_val == self:
                    setattr(old_value, "model_Source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Source"):
                opp_val = getattr(value, "model_Source", None)
                setattr(value, "model_Source", self)

    @property
    def model_Activity148(self):
        return self.__model_Activity148

    @model_Activity148.setter
    def model_Activity148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity148", None)
        self.__model_Activity148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CompensationHandler147"):
                opp_val = getattr(old_value, "model_CompensationHandler147", None)
                if opp_val == self:
                    setattr(old_value, "model_CompensationHandler147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CompensationHandler147"):
                opp_val = getattr(value, "model_CompensationHandler147", None)
                setattr(value, "model_CompensationHandler147", self)

    @property
    def model_Activity244(self):
        return self.__model_Activity244

    @model_Activity244.setter
    def model_Activity244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Activity__model_Activity244", None)
        self.__model_Activity244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnEvent243"):
                opp_val = getattr(old_value, "model_OnEvent243", None)
                if opp_val == self:
                    setattr(old_value, "model_OnEvent243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnEvent243"):
                opp_val = getattr(value, "model_OnEvent243", None)
                setattr(value, "model_OnEvent243", self)

class model_TerminationHandler(BPELExtensibleElement):

    pass
class model_Correlation(BPELExtensibleElement):

    def __init__(self, initiate: str, pattern: str, model_Correlation: "model_CorrelationSet" = None, model_Correlation229: "model_Correlations" = None):
        self.initiate = initiate
        self.pattern = pattern
        self.model_Correlation = model_Correlation
        self.model_Correlation229 = model_Correlation229
        
    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def initiate(self) -> str:
        return self.__initiate

    @initiate.setter
    def initiate(self, initiate: str):
        self.__initiate = initiate

    @property
    def model_Correlation(self):
        return self.__model_Correlation

    @model_Correlation.setter
    def model_Correlation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Correlation__model_Correlation", None)
        self.__model_Correlation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CorrelationSet193"):
                opp_val = getattr(old_value, "model_CorrelationSet193", None)
                if opp_val == self:
                    setattr(old_value, "model_CorrelationSet193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CorrelationSet193"):
                opp_val = getattr(value, "model_CorrelationSet193", None)
                setattr(value, "model_CorrelationSet193", self)

    @property
    def model_Correlation229(self):
        return self.__model_Correlation229

    @model_Correlation229.setter
    def model_Correlation229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Correlation__model_Correlation229", None)
        self.__model_Correlation229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Correlations228"):
                opp_val = getattr(old_value, "model_Correlations228", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Correlations228"):
                opp_val = getattr(value, "model_Correlations228", None)
                if opp_val is None:
                    setattr(value, "model_Correlations228", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_MessageExchange(BPELExtensibleElement):

    def __init__(self, name: str, model_MessageExchange: "model_Reply" = None, model_MessageExchange80: "model_Receive" = None, model_MessageExchange191: "model_OnMessage" = None, model_MessageExchange215: "model_MessageExchanges" = None, model_MessageExchange274: "model_OnEvent" = None):
        self.name = name
        self.model_MessageExchange = model_MessageExchange
        self.model_MessageExchange80 = model_MessageExchange80
        self.model_MessageExchange191 = model_MessageExchange191
        self.model_MessageExchange215 = model_MessageExchange215
        self.model_MessageExchange274 = model_MessageExchange274
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_MessageExchange(self):
        return self.__model_MessageExchange

    @model_MessageExchange.setter
    def model_MessageExchange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MessageExchange__model_MessageExchange", None)
        self.__model_MessageExchange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Reply64"):
                opp_val = getattr(old_value, "model_Reply64", None)
                if opp_val == self:
                    setattr(old_value, "model_Reply64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Reply64"):
                opp_val = getattr(value, "model_Reply64", None)
                setattr(value, "model_Reply64", self)

    @property
    def model_MessageExchange274(self):
        return self.__model_MessageExchange274

    @model_MessageExchange274.setter
    def model_MessageExchange274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MessageExchange__model_MessageExchange274", None)
        self.__model_MessageExchange274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnEvent273"):
                opp_val = getattr(old_value, "model_OnEvent273", None)
                if opp_val == self:
                    setattr(old_value, "model_OnEvent273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnEvent273"):
                opp_val = getattr(value, "model_OnEvent273", None)
                setattr(value, "model_OnEvent273", self)

    @property
    def model_MessageExchange80(self):
        return self.__model_MessageExchange80

    @model_MessageExchange80.setter
    def model_MessageExchange80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MessageExchange__model_MessageExchange80", None)
        self.__model_MessageExchange80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Receive79"):
                opp_val = getattr(old_value, "model_Receive79", None)
                if opp_val == self:
                    setattr(old_value, "model_Receive79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Receive79"):
                opp_val = getattr(value, "model_Receive79", None)
                setattr(value, "model_Receive79", self)

    @property
    def model_MessageExchange215(self):
        return self.__model_MessageExchange215

    @model_MessageExchange215.setter
    def model_MessageExchange215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MessageExchange__model_MessageExchange215", None)
        self.__model_MessageExchange215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MessageExchanges214"):
                opp_val = getattr(old_value, "model_MessageExchanges214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MessageExchanges214"):
                opp_val = getattr(value, "model_MessageExchanges214", None)
                if opp_val is None:
                    setattr(value, "model_MessageExchanges214", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_MessageExchange191(self):
        return self.__model_MessageExchange191

    @model_MessageExchange191.setter
    def model_MessageExchange191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MessageExchange__model_MessageExchange191", None)
        self.__model_MessageExchange191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnMessage190"):
                opp_val = getattr(old_value, "model_OnMessage190", None)
                if opp_val == self:
                    setattr(old_value, "model_OnMessage190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnMessage190"):
                opp_val = getattr(value, "model_OnMessage190", None)
                setattr(value, "model_OnMessage190", self)

class model_Links(BPELExtensibleElement):

    pass
class model_Import(BPELExtensibleElement):

    def __init__(self, namespace: str, location: str, importType: str, model_Import: "model_Process" = None):
        self.namespace = namespace
        self.location = location
        self.importType = importType
        self.model_Import = model_Import
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def importType(self) -> str:
        return self.__importType

    @importType.setter
    def importType(self, importType: str):
        self.__importType = importType

    @property
    def model_Import(self):
        return self.__model_Import

    @model_Import.setter
    def model_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Import__model_Import", None)
        self.__model_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Process12"):
                opp_val = getattr(old_value, "model_Process12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Process12"):
                opp_val = getattr(value, "model_Process12", None)
                if opp_val is None:
                    setattr(value, "model_Process12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_CorrelationSets(BPELExtensibleElement):

    pass
class model_OnEvent(BPELExtensibleElement):

    pass
class model_EventHandler(BPELExtensibleElement):

    pass
class model_Else(BPELExtensibleElement):

    pass
class model_Variables(BPELExtensibleElement):

    pass
class model_Target(BPELExtensibleElement):

    pass
class model_CorrelationSet(BPELExtensibleElement):

    def __init__(self, name: str, model_CorrelationSet: set["Property"] = None, model_CorrelationSet193: "model_Correlation" = None, model_CorrelationSet221: "model_CorrelationSets" = None):
        self.name = name
        self.model_CorrelationSet = model_CorrelationSet if model_CorrelationSet is not None else set()
        self.model_CorrelationSet193 = model_CorrelationSet193
        self.model_CorrelationSet221 = model_CorrelationSet221
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_CorrelationSet(self):
        return self.__model_CorrelationSet

    @model_CorrelationSet.setter
    def model_CorrelationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CorrelationSet__model_CorrelationSet", None)
        self.__model_CorrelationSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def model_CorrelationSet221(self):
        return self.__model_CorrelationSet221

    @model_CorrelationSet221.setter
    def model_CorrelationSet221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CorrelationSet__model_CorrelationSet221", None)
        self.__model_CorrelationSet221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CorrelationSets220"):
                opp_val = getattr(old_value, "model_CorrelationSets220", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CorrelationSets220"):
                opp_val = getattr(value, "model_CorrelationSets220", None)
                if opp_val is None:
                    setattr(value, "model_CorrelationSets220", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_CorrelationSet193(self):
        return self.__model_CorrelationSet193

    @model_CorrelationSet193.setter
    def model_CorrelationSet193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CorrelationSet__model_CorrelationSet193", None)
        self.__model_CorrelationSet193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Correlation"):
                opp_val = getattr(old_value, "model_Correlation", None)
                if opp_val == self:
                    setattr(old_value, "model_Correlation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Correlation"):
                opp_val = getattr(value, "model_Correlation", None)
                setattr(value, "model_Correlation", self)

class model_Targets(BPELExtensibleElement):

    pass
class model_FromPart(BPELExtensibleElement):

    pass
class model_Catch(BPELExtensibleElement):

    def __init__(self, faultName: str, model_Catch: "model_FaultHandler" = None, model_Catch49: "model_Variable" = None, model_Catch52: "model_Activity" = None, model_Catch55: "Message" = None, model_Catch57: "XSDElementDeclaration" = None):
        self.faultName = faultName
        self.model_Catch = model_Catch
        self.model_Catch49 = model_Catch49
        self.model_Catch52 = model_Catch52
        self.model_Catch55 = model_Catch55
        self.model_Catch57 = model_Catch57
        
    @property
    def faultName(self) -> str:
        return self.__faultName

    @faultName.setter
    def faultName(self, faultName: str):
        self.__faultName = faultName

    @property
    def model_Catch49(self):
        return self.__model_Catch49

    @model_Catch49.setter
    def model_Catch49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Catch__model_Catch49", None)
        self.__model_Catch49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Variable50"):
                opp_val = getattr(old_value, "model_Variable50", None)
                if opp_val == self:
                    setattr(old_value, "model_Variable50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Variable50"):
                opp_val = getattr(value, "model_Variable50", None)
                setattr(value, "model_Variable50", self)

    @property
    def model_Catch55(self):
        return self.__model_Catch55

    @model_Catch55.setter
    def model_Catch55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Catch__model_Catch55", None)
        self.__model_Catch55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Message"):
                opp_val = getattr(old_value, "Message", None)
                if opp_val == self:
                    setattr(old_value, "Message", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Message"):
                opp_val = getattr(value, "Message", None)
                setattr(value, "Message", self)

    @property
    def model_Catch57(self):
        return self.__model_Catch57

    @model_Catch57.setter
    def model_Catch57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Catch__model_Catch57", None)
        self.__model_Catch57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDElementDeclaration"):
                opp_val = getattr(old_value, "XSDElementDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "XSDElementDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDElementDeclaration"):
                opp_val = getattr(value, "XSDElementDeclaration", None)
                setattr(value, "XSDElementDeclaration", self)

    @property
    def model_Catch52(self):
        return self.__model_Catch52

    @model_Catch52.setter
    def model_Catch52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Catch__model_Catch52", None)
        self.__model_Catch52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Activity53"):
                opp_val = getattr(old_value, "model_Activity53", None)
                if opp_val == self:
                    setattr(old_value, "model_Activity53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Activity53"):
                opp_val = getattr(value, "model_Activity53", None)
                setattr(value, "model_Activity53", self)

    @property
    def model_Catch(self):
        return self.__model_Catch

    @model_Catch.setter
    def model_Catch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Catch__model_Catch", None)
        self.__model_Catch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FaultHandler24"):
                opp_val = getattr(old_value, "model_FaultHandler24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FaultHandler24"):
                opp_val = getattr(value, "model_FaultHandler24", None)
                if opp_val is None:
                    setattr(value, "model_FaultHandler24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_CompletionCondition(BPELExtensibleElement):

    pass
class model_ToParts(BPELExtensibleElement):

    pass
class model_Sources(BPELExtensibleElement):

    pass
class model_Correlations(BPELExtensibleElement):

    pass
class model_CompensationHandler(BPELExtensibleElement):

    pass
class model_OnAlarm(BPELExtensibleElement):

    pass
class model_Source(BPELExtensibleElement):

    pass
class model_Extensions(BPELExtensibleElement):

    pass
class model_PartnerLink(BPELExtensibleElement):

    def __init__(self, name: str, initializePartnerRole: str, model_PartnerLink: "Role" = None, model_PartnerLink19: "Role" = None, model_PartnerLink22: "PartnerLinkType" = None, model_PartnerLink66: "model_PartnerActivity" = None, model_PartnerLink155: "model_AbstractAssignBound" = None, model_PartnerLink179: "model_OnMessage" = None, model_PartnerLink212: "model_PartnerLinks" = None, model_PartnerLink250: "model_OnEvent" = None):
        self.name = name
        self.initializePartnerRole = initializePartnerRole
        self.model_PartnerLink = model_PartnerLink
        self.model_PartnerLink19 = model_PartnerLink19
        self.model_PartnerLink22 = model_PartnerLink22
        self.model_PartnerLink66 = model_PartnerLink66
        self.model_PartnerLink155 = model_PartnerLink155
        self.model_PartnerLink179 = model_PartnerLink179
        self.model_PartnerLink212 = model_PartnerLink212
        self.model_PartnerLink250 = model_PartnerLink250
        
    @property
    def initializePartnerRole(self) -> str:
        return self.__initializePartnerRole

    @initializePartnerRole.setter
    def initializePartnerRole(self, initializePartnerRole: str):
        self.__initializePartnerRole = initializePartnerRole

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_PartnerLink66(self):
        return self.__model_PartnerLink66

    @model_PartnerLink66.setter
    def model_PartnerLink66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PartnerLink__model_PartnerLink66", None)
        self.__model_PartnerLink66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PartnerActivity"):
                opp_val = getattr(old_value, "model_PartnerActivity", None)
                if opp_val == self:
                    setattr(old_value, "model_PartnerActivity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PartnerActivity"):
                opp_val = getattr(value, "model_PartnerActivity", None)
                setattr(value, "model_PartnerActivity", self)

    @property
    def model_PartnerLink22(self):
        return self.__model_PartnerLink22

    @model_PartnerLink22.setter
    def model_PartnerLink22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PartnerLink__model_PartnerLink22", None)
        self.__model_PartnerLink22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PartnerLinkType"):
                opp_val = getattr(old_value, "PartnerLinkType", None)
                if opp_val == self:
                    setattr(old_value, "PartnerLinkType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PartnerLinkType"):
                opp_val = getattr(value, "PartnerLinkType", None)
                setattr(value, "PartnerLinkType", self)

    @property
    def model_PartnerLink19(self):
        return self.__model_PartnerLink19

    @model_PartnerLink19.setter
    def model_PartnerLink19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PartnerLink__model_PartnerLink19", None)
        self.__model_PartnerLink19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role20"):
                opp_val = getattr(old_value, "Role20", None)
                if opp_val == self:
                    setattr(old_value, "Role20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role20"):
                opp_val = getattr(value, "Role20", None)
                setattr(value, "Role20", self)

    @property
    def model_PartnerLink179(self):
        return self.__model_PartnerLink179

    @model_PartnerLink179.setter
    def model_PartnerLink179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PartnerLink__model_PartnerLink179", None)
        self.__model_PartnerLink179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnMessage178"):
                opp_val = getattr(old_value, "model_OnMessage178", None)
                if opp_val == self:
                    setattr(old_value, "model_OnMessage178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnMessage178"):
                opp_val = getattr(value, "model_OnMessage178", None)
                setattr(value, "model_OnMessage178", self)

    @property
    def model_PartnerLink(self):
        return self.__model_PartnerLink

    @model_PartnerLink.setter
    def model_PartnerLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PartnerLink__model_PartnerLink", None)
        self.__model_PartnerLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role"):
                opp_val = getattr(old_value, "Role", None)
                if opp_val == self:
                    setattr(old_value, "Role", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role"):
                opp_val = getattr(value, "Role", None)
                setattr(value, "Role", self)

    @property
    def model_PartnerLink212(self):
        return self.__model_PartnerLink212

    @model_PartnerLink212.setter
    def model_PartnerLink212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PartnerLink__model_PartnerLink212", None)
        self.__model_PartnerLink212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PartnerLinks211"):
                opp_val = getattr(old_value, "model_PartnerLinks211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PartnerLinks211"):
                opp_val = getattr(value, "model_PartnerLinks211", None)
                if opp_val is None:
                    setattr(value, "model_PartnerLinks211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_PartnerLink250(self):
        return self.__model_PartnerLink250

    @model_PartnerLink250.setter
    def model_PartnerLink250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PartnerLink__model_PartnerLink250", None)
        self.__model_PartnerLink250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnEvent249"):
                opp_val = getattr(old_value, "model_OnEvent249", None)
                if opp_val == self:
                    setattr(old_value, "model_OnEvent249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnEvent249"):
                opp_val = getattr(value, "model_OnEvent249", None)
                setattr(value, "model_OnEvent249", self)

    @property
    def model_PartnerLink155(self):
        return self.__model_PartnerLink155

    @model_PartnerLink155.setter
    def model_PartnerLink155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PartnerLink__model_PartnerLink155", None)
        self.__model_PartnerLink155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractAssignBound154"):
                opp_val = getattr(old_value, "model_AbstractAssignBound154", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractAssignBound154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractAssignBound154"):
                opp_val = getattr(value, "model_AbstractAssignBound154", None)
                setattr(value, "model_AbstractAssignBound154", self)

class model_FaultHandler(BPELExtensibleElement):

    pass
class model_Copy(BPELExtensibleElement):

    def __init__(self, keepSrcElementName: str, ignoreMissingFromData: str, model_Copy: "model_Assign" = None, model_Copy116: "model_To" = None, model_Copy118: "model_From" = None):
        self.keepSrcElementName = keepSrcElementName
        self.ignoreMissingFromData = ignoreMissingFromData
        self.model_Copy = model_Copy
        self.model_Copy116 = model_Copy116
        self.model_Copy118 = model_Copy118
        
    @property
    def keepSrcElementName(self) -> str:
        return self.__keepSrcElementName

    @keepSrcElementName.setter
    def keepSrcElementName(self, keepSrcElementName: str):
        self.__keepSrcElementName = keepSrcElementName

    @property
    def ignoreMissingFromData(self) -> str:
        return self.__ignoreMissingFromData

    @ignoreMissingFromData.setter
    def ignoreMissingFromData(self, ignoreMissingFromData: str):
        self.__ignoreMissingFromData = ignoreMissingFromData

    @property
    def model_Copy(self):
        return self.__model_Copy

    @model_Copy.setter
    def model_Copy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Copy__model_Copy", None)
        self.__model_Copy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Assign"):
                opp_val = getattr(old_value, "model_Assign", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Assign"):
                opp_val = getattr(value, "model_Assign", None)
                if opp_val is None:
                    setattr(value, "model_Assign", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Copy116(self):
        return self.__model_Copy116

    @model_Copy116.setter
    def model_Copy116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Copy__model_Copy116", None)
        self.__model_Copy116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_To"):
                opp_val = getattr(old_value, "model_To", None)
                if opp_val == self:
                    setattr(old_value, "model_To", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_To"):
                opp_val = getattr(value, "model_To", None)
                setattr(value, "model_To", self)

    @property
    def model_Copy118(self):
        return self.__model_Copy118

    @model_Copy118.setter
    def model_Copy118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Copy__model_Copy118", None)
        self.__model_Copy118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_From"):
                opp_val = getattr(old_value, "model_From", None)
                if opp_val == self:
                    setattr(old_value, "model_From", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_From"):
                opp_val = getattr(value, "model_From", None)
                setattr(value, "model_From", self)

class model_From(BPELExtensibleElement, AbstractAssignBound):

    def __init__(self, opaque: str, endpointReference: str, literal: str, unsafeLiteral: str, model_From: "model_Copy" = None, model_From165: "model_ServiceRef" = None, model_From167: "XSDTypeDefinition" = None, model_From241: "model_Variable" = None):
        self.opaque = opaque
        self.endpointReference = endpointReference
        self.literal = literal
        self.unsafeLiteral = unsafeLiteral
        self.model_From = model_From
        self.model_From165 = model_From165
        self.model_From167 = model_From167
        self.model_From241 = model_From241
        
    @property
    def opaque(self) -> str:
        return self.__opaque

    @opaque.setter
    def opaque(self, opaque: str):
        self.__opaque = opaque

    @property
    def endpointReference(self) -> str:
        return self.__endpointReference

    @endpointReference.setter
    def endpointReference(self, endpointReference: str):
        self.__endpointReference = endpointReference

    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def unsafeLiteral(self) -> str:
        return self.__unsafeLiteral

    @unsafeLiteral.setter
    def unsafeLiteral(self, unsafeLiteral: str):
        self.__unsafeLiteral = unsafeLiteral

    @property
    def model_From(self):
        return self.__model_From

    @model_From.setter
    def model_From(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_From__model_From", None)
        self.__model_From = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Copy118"):
                opp_val = getattr(old_value, "model_Copy118", None)
                if opp_val == self:
                    setattr(old_value, "model_Copy118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Copy118"):
                opp_val = getattr(value, "model_Copy118", None)
                setattr(value, "model_Copy118", self)

    @property
    def model_From241(self):
        return self.__model_From241

    @model_From241.setter
    def model_From241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_From__model_From241", None)
        self.__model_From241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Variable240"):
                opp_val = getattr(old_value, "model_Variable240", None)
                if opp_val == self:
                    setattr(old_value, "model_Variable240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Variable240"):
                opp_val = getattr(value, "model_Variable240", None)
                setattr(value, "model_Variable240", self)

    @property
    def model_From167(self):
        return self.__model_From167

    @model_From167.setter
    def model_From167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_From__model_From167", None)
        self.__model_From167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTypeDefinition"):
                opp_val = getattr(old_value, "XSDTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "XSDTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTypeDefinition"):
                opp_val = getattr(value, "XSDTypeDefinition", None)
                setattr(value, "XSDTypeDefinition", self)

    @property
    def model_From165(self):
        return self.__model_From165

    @model_From165.setter
    def model_From165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_From__model_From165", None)
        self.__model_From165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ServiceRef"):
                opp_val = getattr(old_value, "model_ServiceRef", None)
                if opp_val == self:
                    setattr(old_value, "model_ServiceRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ServiceRef"):
                opp_val = getattr(value, "model_ServiceRef", None)
                setattr(value, "model_ServiceRef", self)

class model_To(BPELExtensibleElement, AbstractAssignBound):

    pass
class model_PartnerLinks(BPELExtensibleElement):

    pass
class model_MessageExchanges(BPELExtensibleElement):

    pass
class model_ElseIf(BPELExtensibleElement):

    pass
class model_OnMessage(BPELExtensibleElement):

    pass
class model_Documentation(BPELExtensibleElement):

    def __init__(self, lang: str, source: str, value: str, model_Documentation: "model_BPELExtensibleElement" = None):
        self.lang = lang
        self.source = source
        self.value = value
        self.model_Documentation = model_Documentation
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def model_Documentation(self):
        return self.__model_Documentation

    @model_Documentation.setter
    def model_Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Documentation__model_Documentation", None)
        self.__model_Documentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BPELExtensibleElement"):
                opp_val = getattr(old_value, "model_BPELExtensibleElement", None)
                if opp_val == self:
                    setattr(old_value, "model_BPELExtensibleElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BPELExtensibleElement"):
                opp_val = getattr(value, "model_BPELExtensibleElement", None)
                setattr(value, "model_BPELExtensibleElement", self)

class model_ToPart(BPELExtensibleElement):

    pass
class model_Extension(BPELExtensibleElement):

    def __init__(self, namespace: str, mustUnderstand: str, model_Extension: "model_Extensions" = None):
        self.namespace = namespace
        self.mustUnderstand = mustUnderstand
        self.model_Extension = model_Extension
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def mustUnderstand(self) -> str:
        return self.__mustUnderstand

    @mustUnderstand.setter
    def mustUnderstand(self, mustUnderstand: str):
        self.__mustUnderstand = mustUnderstand

    @property
    def model_Extension(self):
        return self.__model_Extension

    @model_Extension.setter
    def model_Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Extension__model_Extension", None)
        self.__model_Extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Extensions285"):
                opp_val = getattr(old_value, "model_Extensions285", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Extensions285"):
                opp_val = getattr(value, "model_Extensions285", None)
                if opp_val is None:
                    setattr(value, "model_Extensions285", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_CatchAll(BPELExtensibleElement):

    pass
class model_Link(BPELExtensibleElement):

    def __init__(self, name: str, Link: set["model_Source"] = None, Link47: set["model_Target"] = None, Link200: "model_Source" = None, Link207: "model_Target" = None, model_Link: "model_Links" = None):
        self.name = name
        self.Link = Link if Link is not None else set()
        self.Link47 = Link47 if Link47 is not None else set()
        self.Link200 = Link200
        self.Link207 = Link207
        self.model_Link = model_Link
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Link(self):
        return self.__Link

    @Link.setter
    def Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Link__Link", None)
        self.__Link = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Source"):
                    opp_val = getattr(item, "Source", None)
                    
                    if opp_val == self:
                        setattr(item, "Source", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Source"):
                    opp_val = getattr(item, "Source", None)
                    
                    setattr(item, "Source", self)
                    

    @property
    def model_Link(self):
        return self.__model_Link

    @model_Link.setter
    def model_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Link__model_Link", None)
        self.__model_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Links223"):
                opp_val = getattr(old_value, "model_Links223", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Links223"):
                opp_val = getattr(value, "model_Links223", None)
                if opp_val is None:
                    setattr(value, "model_Links223", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Link207(self):
        return self.__Link207

    @Link207.setter
    def Link207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Link__Link207", None)
        self.__Link207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targets"):
                opp_val = getattr(old_value, "targets", None)
                if opp_val == self:
                    setattr(old_value, "targets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targets"):
                opp_val = getattr(value, "targets", None)
                setattr(value, "targets", self)

    @property
    def Link47(self):
        return self.__Link47

    @Link47.setter
    def Link47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Link__Link47", None)
        self.__Link47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Target"):
                    opp_val = getattr(item, "Target", None)
                    
                    if opp_val == self:
                        setattr(item, "Target", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Target"):
                    opp_val = getattr(item, "Target", None)
                    
                    setattr(item, "Target", self)
                    

    @property
    def Link200(self):
        return self.__Link200

    @Link200.setter
    def Link200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Link__Link200", None)
        self.__Link200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sources"):
                opp_val = getattr(old_value, "sources", None)
                if opp_val == self:
                    setattr(old_value, "sources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sources"):
                opp_val = getattr(value, "sources", None)
                setattr(value, "sources", self)

class model_Variable(BPELExtensibleElement):

    def __init__(self, name: str, model_Variable: "model_Invoke" = None, model_Variable35: "model_Invoke" = None, model_Variable50: "model_Catch" = None, model_Variable59: "model_Reply" = None, model_Variable74: "model_Receive" = None, model_Variable82: "model_Throw" = None, model_Variable150: "model_AbstractAssignBound" = None, model_Variable170: "model_OnMessage" = None, model_Variable234: "XSDElementDeclaration" = None, model_Variable218: "model_Variables" = None, model_Variable231: "Message" = None, model_Variable237: "XSDTypeDefinition" = None, model_Variable240: "model_From" = None, model_Variable247: "model_OnEvent" = None, model_Variable303: "model_ForEach" = None, model_Variable287: "model_FromPart" = None, model_Variable292: "model_ToPart" = None, model_Variable319: "model_Validate" = None):
        self.name = name
        self.model_Variable = model_Variable
        self.model_Variable35 = model_Variable35
        self.model_Variable50 = model_Variable50
        self.model_Variable59 = model_Variable59
        self.model_Variable74 = model_Variable74
        self.model_Variable82 = model_Variable82
        self.model_Variable150 = model_Variable150
        self.model_Variable170 = model_Variable170
        self.model_Variable234 = model_Variable234
        self.model_Variable218 = model_Variable218
        self.model_Variable231 = model_Variable231
        self.model_Variable237 = model_Variable237
        self.model_Variable240 = model_Variable240
        self.model_Variable247 = model_Variable247
        self.model_Variable303 = model_Variable303
        self.model_Variable287 = model_Variable287
        self.model_Variable292 = model_Variable292
        self.model_Variable319 = model_Variable319
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Variable35(self):
        return self.__model_Variable35

    @model_Variable35.setter
    def model_Variable35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable35", None)
        self.__model_Variable35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Invoke34"):
                opp_val = getattr(old_value, "model_Invoke34", None)
                if opp_val == self:
                    setattr(old_value, "model_Invoke34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Invoke34"):
                opp_val = getattr(value, "model_Invoke34", None)
                setattr(value, "model_Invoke34", self)

    @property
    def model_Variable292(self):
        return self.__model_Variable292

    @model_Variable292.setter
    def model_Variable292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable292", None)
        self.__model_Variable292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ToPart"):
                opp_val = getattr(old_value, "model_ToPart", None)
                if opp_val == self:
                    setattr(old_value, "model_ToPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ToPart"):
                opp_val = getattr(value, "model_ToPart", None)
                setattr(value, "model_ToPart", self)

    @property
    def model_Variable234(self):
        return self.__model_Variable234

    @model_Variable234.setter
    def model_Variable234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable234", None)
        self.__model_Variable234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDElementDeclaration235"):
                opp_val = getattr(old_value, "XSDElementDeclaration235", None)
                if opp_val == self:
                    setattr(old_value, "XSDElementDeclaration235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDElementDeclaration235"):
                opp_val = getattr(value, "XSDElementDeclaration235", None)
                setattr(value, "XSDElementDeclaration235", self)

    @property
    def model_Variable170(self):
        return self.__model_Variable170

    @model_Variable170.setter
    def model_Variable170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable170", None)
        self.__model_Variable170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnMessage169"):
                opp_val = getattr(old_value, "model_OnMessage169", None)
                if opp_val == self:
                    setattr(old_value, "model_OnMessage169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnMessage169"):
                opp_val = getattr(value, "model_OnMessage169", None)
                setattr(value, "model_OnMessage169", self)

    @property
    def model_Variable240(self):
        return self.__model_Variable240

    @model_Variable240.setter
    def model_Variable240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable240", None)
        self.__model_Variable240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_From241"):
                opp_val = getattr(old_value, "model_From241", None)
                if opp_val == self:
                    setattr(old_value, "model_From241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_From241"):
                opp_val = getattr(value, "model_From241", None)
                setattr(value, "model_From241", self)

    @property
    def model_Variable231(self):
        return self.__model_Variable231

    @model_Variable231.setter
    def model_Variable231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable231", None)
        self.__model_Variable231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Message232"):
                opp_val = getattr(old_value, "Message232", None)
                if opp_val == self:
                    setattr(old_value, "Message232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Message232"):
                opp_val = getattr(value, "Message232", None)
                setattr(value, "Message232", self)

    @property
    def model_Variable150(self):
        return self.__model_Variable150

    @model_Variable150.setter
    def model_Variable150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable150", None)
        self.__model_Variable150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractAssignBound"):
                opp_val = getattr(old_value, "model_AbstractAssignBound", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractAssignBound", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractAssignBound"):
                opp_val = getattr(value, "model_AbstractAssignBound", None)
                setattr(value, "model_AbstractAssignBound", self)

    @property
    def model_Variable82(self):
        return self.__model_Variable82

    @model_Variable82.setter
    def model_Variable82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable82", None)
        self.__model_Variable82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Throw"):
                opp_val = getattr(old_value, "model_Throw", None)
                if opp_val == self:
                    setattr(old_value, "model_Throw", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Throw"):
                opp_val = getattr(value, "model_Throw", None)
                setattr(value, "model_Throw", self)

    @property
    def model_Variable303(self):
        return self.__model_Variable303

    @model_Variable303.setter
    def model_Variable303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable303", None)
        self.__model_Variable303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ForEach302"):
                opp_val = getattr(old_value, "model_ForEach302", None)
                if opp_val == self:
                    setattr(old_value, "model_ForEach302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ForEach302"):
                opp_val = getattr(value, "model_ForEach302", None)
                setattr(value, "model_ForEach302", self)

    @property
    def model_Variable247(self):
        return self.__model_Variable247

    @model_Variable247.setter
    def model_Variable247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable247", None)
        self.__model_Variable247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OnEvent246"):
                opp_val = getattr(old_value, "model_OnEvent246", None)
                if opp_val == self:
                    setattr(old_value, "model_OnEvent246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OnEvent246"):
                opp_val = getattr(value, "model_OnEvent246", None)
                setattr(value, "model_OnEvent246", self)

    @property
    def model_Variable(self):
        return self.__model_Variable

    @model_Variable.setter
    def model_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable", None)
        self.__model_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Invoke"):
                opp_val = getattr(old_value, "model_Invoke", None)
                if opp_val == self:
                    setattr(old_value, "model_Invoke", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Invoke"):
                opp_val = getattr(value, "model_Invoke", None)
                setattr(value, "model_Invoke", self)

    @property
    def model_Variable287(self):
        return self.__model_Variable287

    @model_Variable287.setter
    def model_Variable287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable287", None)
        self.__model_Variable287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FromPart"):
                opp_val = getattr(old_value, "model_FromPart", None)
                if opp_val == self:
                    setattr(old_value, "model_FromPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FromPart"):
                opp_val = getattr(value, "model_FromPart", None)
                setattr(value, "model_FromPart", self)

    @property
    def model_Variable237(self):
        return self.__model_Variable237

    @model_Variable237.setter
    def model_Variable237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable237", None)
        self.__model_Variable237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XSDTypeDefinition238"):
                opp_val = getattr(old_value, "XSDTypeDefinition238", None)
                if opp_val == self:
                    setattr(old_value, "XSDTypeDefinition238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XSDTypeDefinition238"):
                opp_val = getattr(value, "XSDTypeDefinition238", None)
                setattr(value, "XSDTypeDefinition238", self)

    @property
    def model_Variable319(self):
        return self.__model_Variable319

    @model_Variable319.setter
    def model_Variable319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable319", None)
        self.__model_Variable319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Validate"):
                opp_val = getattr(old_value, "model_Validate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Validate"):
                opp_val = getattr(value, "model_Validate", None)
                if opp_val is None:
                    setattr(value, "model_Validate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Variable218(self):
        return self.__model_Variable218

    @model_Variable218.setter
    def model_Variable218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable218", None)
        self.__model_Variable218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Variables217"):
                opp_val = getattr(old_value, "model_Variables217", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Variables217"):
                opp_val = getattr(value, "model_Variables217", None)
                if opp_val is None:
                    setattr(value, "model_Variables217", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Variable59(self):
        return self.__model_Variable59

    @model_Variable59.setter
    def model_Variable59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable59", None)
        self.__model_Variable59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Reply"):
                opp_val = getattr(old_value, "model_Reply", None)
                if opp_val == self:
                    setattr(old_value, "model_Reply", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Reply"):
                opp_val = getattr(value, "model_Reply", None)
                setattr(value, "model_Reply", self)

    @property
    def model_Variable50(self):
        return self.__model_Variable50

    @model_Variable50.setter
    def model_Variable50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable50", None)
        self.__model_Variable50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Catch49"):
                opp_val = getattr(old_value, "model_Catch49", None)
                if opp_val == self:
                    setattr(old_value, "model_Catch49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Catch49"):
                opp_val = getattr(value, "model_Catch49", None)
                setattr(value, "model_Catch49", self)

    @property
    def model_Variable74(self):
        return self.__model_Variable74

    @model_Variable74.setter
    def model_Variable74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Variable__model_Variable74", None)
        self.__model_Variable74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Receive"):
                opp_val = getattr(old_value, "model_Receive", None)
                if opp_val == self:
                    setattr(old_value, "model_Receive", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Receive"):
                opp_val = getattr(value, "model_Receive", None)
                setattr(value, "model_Receive", self)

class model_FromParts(BPELExtensibleElement):

    pass
class model_Process(BPELExtensibleElement):

    def __init__(self, name: str, targetNamespace: str, queryLanguage: str, exitOnStandardFault: str, expressionLanguage: str, suppressJoinFailure: str, variableAccessSerializable: str, abstractProcessProfile: str, model_Process16: "model_MessageExchanges" = None, model_Process: "model_PartnerLinks" = None, model_Process2: "model_Variables" = None, model_Process4: "model_Activity" = None, model_Process6: "model_FaultHandler" = None, model_Process8: "model_EventHandler" = None, model_Process10: "model_CorrelationSets" = None, model_Process12: set["model_Import"] = None, model_Process14: "model_Extensions" = None):
        self.name = name
        self.targetNamespace = targetNamespace
        self.queryLanguage = queryLanguage
        self.exitOnStandardFault = exitOnStandardFault
        self.expressionLanguage = expressionLanguage
        self.suppressJoinFailure = suppressJoinFailure
        self.variableAccessSerializable = variableAccessSerializable
        self.abstractProcessProfile = abstractProcessProfile
        self.model_Process16 = model_Process16
        self.model_Process = model_Process
        self.model_Process2 = model_Process2
        self.model_Process4 = model_Process4
        self.model_Process6 = model_Process6
        self.model_Process8 = model_Process8
        self.model_Process10 = model_Process10
        self.model_Process12 = model_Process12 if model_Process12 is not None else set()
        self.model_Process14 = model_Process14
        
    @property
    def targetNamespace(self) -> str:
        return self.__targetNamespace

    @targetNamespace.setter
    def targetNamespace(self, targetNamespace: str):
        self.__targetNamespace = targetNamespace

    @property
    def expressionLanguage(self) -> str:
        return self.__expressionLanguage

    @expressionLanguage.setter
    def expressionLanguage(self, expressionLanguage: str):
        self.__expressionLanguage = expressionLanguage

    @property
    def queryLanguage(self) -> str:
        return self.__queryLanguage

    @queryLanguage.setter
    def queryLanguage(self, queryLanguage: str):
        self.__queryLanguage = queryLanguage

    @property
    def abstractProcessProfile(self) -> str:
        return self.__abstractProcessProfile

    @abstractProcessProfile.setter
    def abstractProcessProfile(self, abstractProcessProfile: str):
        self.__abstractProcessProfile = abstractProcessProfile

    @property
    def suppressJoinFailure(self) -> str:
        return self.__suppressJoinFailure

    @suppressJoinFailure.setter
    def suppressJoinFailure(self, suppressJoinFailure: str):
        self.__suppressJoinFailure = suppressJoinFailure

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def exitOnStandardFault(self) -> str:
        return self.__exitOnStandardFault

    @exitOnStandardFault.setter
    def exitOnStandardFault(self, exitOnStandardFault: str):
        self.__exitOnStandardFault = exitOnStandardFault

    @property
    def variableAccessSerializable(self) -> str:
        return self.__variableAccessSerializable

    @variableAccessSerializable.setter
    def variableAccessSerializable(self, variableAccessSerializable: str):
        self.__variableAccessSerializable = variableAccessSerializable

    @property
    def model_Process14(self):
        return self.__model_Process14

    @model_Process14.setter
    def model_Process14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Process__model_Process14", None)
        self.__model_Process14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Extensions"):
                opp_val = getattr(old_value, "model_Extensions", None)
                if opp_val == self:
                    setattr(old_value, "model_Extensions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Extensions"):
                opp_val = getattr(value, "model_Extensions", None)
                setattr(value, "model_Extensions", self)

    @property
    def model_Process8(self):
        return self.__model_Process8

    @model_Process8.setter
    def model_Process8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Process__model_Process8", None)
        self.__model_Process8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_EventHandler"):
                opp_val = getattr(old_value, "model_EventHandler", None)
                if opp_val == self:
                    setattr(old_value, "model_EventHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_EventHandler"):
                opp_val = getattr(value, "model_EventHandler", None)
                setattr(value, "model_EventHandler", self)

    @property
    def model_Process2(self):
        return self.__model_Process2

    @model_Process2.setter
    def model_Process2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Process__model_Process2", None)
        self.__model_Process2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Variables"):
                opp_val = getattr(old_value, "model_Variables", None)
                if opp_val == self:
                    setattr(old_value, "model_Variables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Variables"):
                opp_val = getattr(value, "model_Variables", None)
                setattr(value, "model_Variables", self)

    @property
    def model_Process(self):
        return self.__model_Process

    @model_Process.setter
    def model_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Process__model_Process", None)
        self.__model_Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PartnerLinks"):
                opp_val = getattr(old_value, "model_PartnerLinks", None)
                if opp_val == self:
                    setattr(old_value, "model_PartnerLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PartnerLinks"):
                opp_val = getattr(value, "model_PartnerLinks", None)
                setattr(value, "model_PartnerLinks", self)

    @property
    def model_Process10(self):
        return self.__model_Process10

    @model_Process10.setter
    def model_Process10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Process__model_Process10", None)
        self.__model_Process10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CorrelationSets"):
                opp_val = getattr(old_value, "model_CorrelationSets", None)
                if opp_val == self:
                    setattr(old_value, "model_CorrelationSets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CorrelationSets"):
                opp_val = getattr(value, "model_CorrelationSets", None)
                setattr(value, "model_CorrelationSets", self)

    @property
    def model_Process12(self):
        return self.__model_Process12

    @model_Process12.setter
    def model_Process12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Process__model_Process12", None)
        self.__model_Process12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Import"):
                    opp_val = getattr(item, "model_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Import"):
                    opp_val = getattr(item, "model_Import", None)
                    
                    setattr(item, "model_Import", self)
                    

    @property
    def model_Process16(self):
        return self.__model_Process16

    @model_Process16.setter
    def model_Process16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Process__model_Process16", None)
        self.__model_Process16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MessageExchanges"):
                opp_val = getattr(old_value, "model_MessageExchanges", None)
                if opp_val == self:
                    setattr(old_value, "model_MessageExchanges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MessageExchanges"):
                opp_val = getattr(value, "model_MessageExchanges", None)
                setattr(value, "model_MessageExchanges", self)

    @property
    def model_Process4(self):
        return self.__model_Process4

    @model_Process4.setter
    def model_Process4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Process__model_Process4", None)
        self.__model_Process4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Activity"):
                opp_val = getattr(old_value, "model_Activity", None)
                if opp_val == self:
                    setattr(old_value, "model_Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Activity"):
                opp_val = getattr(value, "model_Activity", None)
                setattr(value, "model_Activity", self)

    @property
    def model_Process6(self):
        return self.__model_Process6

    @model_Process6.setter
    def model_Process6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Process__model_Process6", None)
        self.__model_Process6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FaultHandler"):
                opp_val = getattr(old_value, "model_FaultHandler", None)
                if opp_val == self:
                    setattr(old_value, "model_FaultHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FaultHandler"):
                opp_val = getattr(value, "model_FaultHandler", None)
                setattr(value, "model_FaultHandler", self)
