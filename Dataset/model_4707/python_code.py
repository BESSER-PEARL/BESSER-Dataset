from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariableQualification(Enum):
    Select = "Select"
    Optional = "Optional"
    Assert = "Assert"
    Negate = "Negate"
    ExactlyOne = "ExactlyOne"
    ThereExists = "ThereExists"
    All = "All"
class AssertionStrength(Enum):
    Global = "Global"
    Local = "Local"


############################################
# Definition of Classes
############################################

class UniquenessConstraint:

    pass
class ObjectOperationType:

    pass
class Traversal:

    pass
class Facet:

    pass
class smif_facets_Category(Facet):

    pass
class smif_facets_Role(Facet):

    pass
class facets_Facet:

    pass
class Relationship:

    pass
class smif_facets_FacetOfEntity(Relationship):

    pass
class CharacteristicType:

    pass
class smif_properties_AnnotationProperty(CharacteristicType):

    pass
class properties_PropertyBinding:

    pass
class properties_PropertyType:

    pass
class Term:

    pass
class IRIIdentifier:

    pass
class metadata_Metadata:

    pass
class ConditionalRule:

    pass
class smif_mapping_RepresentationRule(ConditionalRule):

    def __init__(self, mapAll: str, Type236: "Type" = None, Type239: set["Type"] = None):
        self.mapAll = mapAll
        self.Type236 = Type236
        self.Type239 = Type239 if Type239 is not None else set()
        
    @property
    def mapAll(self) -> str:
        return self.__mapAll

    @mapAll.setter
    def mapAll(self, mapAll: str):
        self.__mapAll = mapAll

    @property
    def Type239(self):
        return self.__Type239

    @Type239.setter
    def Type239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_RepresentationRule__Type239", None)
        self.__Type239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types240"):
                    opp_val = getattr(item, "types240", None)
                    
                    if opp_val == self:
                        setattr(item, "types240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types240"):
                    opp_val = getattr(item, "types240", None)
                    
                    setattr(item, "types240", self)
                    

    @property
    def Type236(self):
        return self.__Type236

    @Type236.setter
    def Type236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_RepresentationRule__Type236", None)
        self.__Type236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types237"):
                opp_val = getattr(old_value, "types237", None)
                if opp_val == self:
                    setattr(old_value, "types237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types237"):
                opp_val = getattr(value, "types237", None)
                setattr(value, "types237", self)

class PropertyOwnerType:

    pass
class smif_associations_AssociationType(PropertyOwnerType):

    pass
class Prefix:

    pass
class Package:

    pass
class smif_lexicalscope_MappingPackage(Package):

    pass
class smif_lexicalscope_MOFPackage(Package):

    pass
class smif_lexicalscope_PhysicalPackage(Package):

    pass
class smif_lexicalscope_LogicalPackage(Package):

    pass
class smif_lexicalscope_Model(Package):

    pass
class smif_patterns_Computed(ABC):

    pass
class OwnedPropertyBinding:

    pass
class smif_patterns_VariableBinding(OwnedPropertyBinding):

    pass
class Situation:

    pass
class Facade:

    pass
class smif_mapping_ComputedFacade(Facade):

    def __init__(self):
        
    def pull(self) -> str:
        # TODO: Implement pull method
        pass

    def push(self) -> str:
        # TODO: Implement push method
        pass

class patterns_Pattern:

    pass
class MatchRule:

    pass
class Pattern:

    pass
class VariableBinding:

    pass
class ActualSituation:

    pass
class smif_patterns_PatternMatch(ActualSituation):

    pass
class smif_patterns_PatternOfType(Pattern):

    pass
class TypePatternVariable:

    pass
class smif_patterns_FocusVariable(TypePatternVariable):

    pass
class smif_patterns_PartVariable(TypePatternVariable):

    def __init__(self, isBoundaryPart: str):
        self.isBoundaryPart = isBoundaryPart
        
    @property
    def isBoundaryPart(self) -> str:
        return self.__isBoundaryPart

    @isBoundaryPart.setter
    def isBoundaryPart(self, isBoundaryPart: str):
        self.__isBoundaryPart = isBoundaryPart

class patterns_Computed:

    pass
class patterns_PatternVariable:

    pass
class smif_patterns_ExpressionVariable(patterns_Computed, patterns_PatternVariable):

    pass
class Mapping:

    pass
class Equality:

    pass
class properties_OwnedPropertyType:

    pass
class PatternVariable:

    pass
class smif_patterns_PropositionVariable(PatternVariable):

    pass
class smif_patterns_TypePatternVariable(PatternVariable):

    pass
class TemporalEntity:

    pass
class smif_toplevel_ActualEntity(TemporalEntity):

    pass
class PropositionVariable:

    pass
class LexicalReference:

    pass
class smif_lexicalscope_Include(LexicalReference):

    pass
class smif_constraints_Conditional(ABC):

    pass
class ConstantReference:

    pass
class smif_toplevel_Thing(ABC):

    pass
class PropertyBinding:

    pass
class smif_properties_OwnedPropertyBinding(PropertyBinding):

    pass
class InformationSource:

    pass
class Record:

    pass
class smif_metadata_Metadata(Record):

    pass
class Name:

    pass
class Metadata:

    pass
class smif_metadata_Definition(Metadata):

    def __init__(self, textDefinition: str, summaryDescription: str, smif_metadata_Definition: "IRIIdentifier" = None, smif_metadata_Definition277: "Term" = None, IdentifiableEntity279: "IdentifiableEntity" = None, metadata112: "smif_toplevel_IdentifiableEntity"):
        self.textDefinition = textDefinition
        self.summaryDescription = summaryDescription
        self.smif_metadata_Definition = smif_metadata_Definition
        self.smif_metadata_Definition277 = smif_metadata_Definition277
        self.IdentifiableEntity279 = IdentifiableEntity279
        
    @property
    def summaryDescription(self) -> str:
        return self.__summaryDescription

    @summaryDescription.setter
    def summaryDescription(self, summaryDescription: str):
        self.__summaryDescription = summaryDescription

    @property
    def textDefinition(self) -> str:
        return self.__textDefinition

    @textDefinition.setter
    def textDefinition(self, textDefinition: str):
        self.__textDefinition = textDefinition

    @property
    def smif_metadata_Definition277(self):
        return self.__smif_metadata_Definition277

    @smif_metadata_Definition277.setter
    def smif_metadata_Definition277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_metadata_Definition__smif_metadata_Definition277", None)
        self.__smif_metadata_Definition277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Term"):
                opp_val = getattr(old_value, "Term", None)
                if opp_val == self:
                    setattr(old_value, "Term", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Term"):
                opp_val = getattr(value, "Term", None)
                setattr(value, "Term", self)

    @property
    def IdentifiableEntity279(self):
        return self.__IdentifiableEntity279

    @IdentifiableEntity279.setter
    def IdentifiableEntity279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_metadata_Definition__IdentifiableEntity279", None)
        self.__IdentifiableEntity279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toplevel280"):
                opp_val = getattr(old_value, "toplevel280", None)
                if opp_val == self:
                    setattr(old_value, "toplevel280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toplevel280"):
                opp_val = getattr(value, "toplevel280", None)
                setattr(value, "toplevel280", self)

    @property
    def smif_metadata_Definition(self):
        return self.__smif_metadata_Definition

    @smif_metadata_Definition.setter
    def smif_metadata_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_metadata_Definition__smif_metadata_Definition", None)
        self.__smif_metadata_Definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IRIIdentifier"):
                opp_val = getattr(old_value, "IRIIdentifier", None)
                if opp_val == self:
                    setattr(old_value, "IRIIdentifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IRIIdentifier"):
                opp_val = getattr(value, "IRIIdentifier", None)
                setattr(value, "IRIIdentifier", self)

class smif_metadata_Statement(Metadata):

    pass
class Statement:

    pass
class Rule:

    pass
class smif_mapping_MatchRule(Rule):

    def __init__(self, coerce: str, MatchEnd207: "MatchEnd" = None, MatchEnd210: "MatchEnd" = None, Mapping213: "Mapping" = None, constraints119: "smif_toplevel_IdentifiableEntity", constraints75: "smif_constraints_Rule", constraints78: "smif_constraints_Rule"):
        self.coerce = coerce
        self.MatchEnd207 = MatchEnd207
        self.MatchEnd210 = MatchEnd210
        self.Mapping213 = Mapping213
        
    @property
    def coerce(self) -> str:
        return self.__coerce

    @coerce.setter
    def coerce(self, coerce: str):
        self.__coerce = coerce

    @property
    def MatchEnd207(self):
        return self.__MatchEnd207

    @MatchEnd207.setter
    def MatchEnd207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_MatchRule__MatchEnd207", None)
        self.__MatchEnd207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapping208"):
                opp_val = getattr(old_value, "mapping208", None)
                if opp_val == self:
                    setattr(old_value, "mapping208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapping208"):
                opp_val = getattr(value, "mapping208", None)
                setattr(value, "mapping208", self)

    @property
    def MatchEnd210(self):
        return self.__MatchEnd210

    @MatchEnd210.setter
    def MatchEnd210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_MatchRule__MatchEnd210", None)
        self.__MatchEnd210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapping211"):
                opp_val = getattr(old_value, "mapping211", None)
                if opp_val == self:
                    setattr(old_value, "mapping211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapping211"):
                opp_val = getattr(value, "mapping211", None)
                setattr(value, "mapping211", self)

    @property
    def Mapping213(self):
        return self.__Mapping213

    @Mapping213.setter
    def Mapping213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_MatchRule__Mapping213", None)
        self.__Mapping213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapping214"):
                opp_val = getattr(old_value, "mapping214", None)
                if opp_val == self:
                    setattr(old_value, "mapping214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapping214"):
                opp_val = getattr(value, "mapping214", None)
                setattr(value, "mapping214", self)

class Proposition:

    pass
class smif_constraints_Rule(Proposition):

    pass
class situations_SituationType:

    pass
class smif_facets_Phase(situations_SituationType, facets_Facet):

    pass
class smif_properties_CharacteristicType(properties_PropertyType, situations_SituationType):

    pass
class PropertyConstraint:

    pass
class smif_constraints_PropertyTypeConstraint(PropertyConstraint):

    def __init__(self, prerequisiteType: str, Type95: "Type" = None):
        self.prerequisiteType = prerequisiteType
        self.Type95 = Type95
        
    @property
    def prerequisiteType(self) -> str:
        return self.__prerequisiteType

    @prerequisiteType.setter
    def prerequisiteType(self, prerequisiteType: str):
        self.__prerequisiteType = prerequisiteType

    @property
    def Type95(self):
        return self.__Type95

    @Type95.setter
    def Type95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_PropertyTypeConstraint__Type95", None)
        self.__Type95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types96"):
                opp_val = getattr(old_value, "types96", None)
                if opp_val == self:
                    setattr(old_value, "types96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types96"):
                opp_val = getattr(value, "types96", None)
                setattr(value, "types96", self)

class smif_constraints_PropertyTransitivityConstraint(PropertyConstraint):

    pass
class smif_constraints_PropertyConstraint(Rule):

    pass
class smif_constraints_Enumerated(Rule):

    pass
class smif_constraints_Disjoint(Rule):

    pass
class smif_constraints_Equivalent(Rule):

    pass
class smif_constraints_TypeConstraint(Rule):

    pass
class constraints_Conditional:

    pass
class smif_patterns_PatternVariable(properties_OwnedPropertyType, constraints_Conditional):

    def __init__(self, qualification: str, explicit: str, PatternVariable179: set["PatternVariable"] = None, PatternVariable182: set["PatternVariable"] = None, Mapping: "Mapping" = None, Mapping187: "Mapping" = None, Pattern: "Pattern" = None, PatternVariable170: set["PatternVariable"] = None, MatchEnd173: set["MatchEnd"] = None, PatternVariable176: set["PatternVariable"] = None):
        self.qualification = qualification
        self.explicit = explicit
        self.PatternVariable179 = PatternVariable179 if PatternVariable179 is not None else set()
        self.PatternVariable182 = PatternVariable182 if PatternVariable182 is not None else set()
        self.Mapping = Mapping
        self.Mapping187 = Mapping187
        self.Pattern = Pattern
        self.PatternVariable170 = PatternVariable170 if PatternVariable170 is not None else set()
        self.MatchEnd173 = MatchEnd173 if MatchEnd173 is not None else set()
        self.PatternVariable176 = PatternVariable176 if PatternVariable176 is not None else set()
        
    @property
    def qualification(self) -> str:
        return self.__qualification

    @qualification.setter
    def qualification(self, qualification: str):
        self.__qualification = qualification

    @property
    def explicit(self) -> str:
        return self.__explicit

    @explicit.setter
    def explicit(self, explicit: str):
        self.__explicit = explicit

    @property
    def Mapping(self):
        return self.__Mapping

    @Mapping.setter
    def Mapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__Mapping", None)
        self.__Mapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapping185"):
                opp_val = getattr(old_value, "mapping185", None)
                if opp_val == self:
                    setattr(old_value, "mapping185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapping185"):
                opp_val = getattr(value, "mapping185", None)
                setattr(value, "mapping185", self)

    @property
    def Pattern(self):
        return self.__Pattern

    @Pattern.setter
    def Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__Pattern", None)
        self.__Pattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patterns168"):
                opp_val = getattr(old_value, "patterns168", None)
                if opp_val == self:
                    setattr(old_value, "patterns168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patterns168"):
                opp_val = getattr(value, "patterns168", None)
                setattr(value, "patterns168", self)

    @property
    def PatternVariable179(self):
        return self.__PatternVariable179

    @PatternVariable179.setter
    def PatternVariable179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__PatternVariable179", None)
        self.__PatternVariable179 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patterns180"):
                    opp_val = getattr(item, "patterns180", None)
                    
                    if opp_val == self:
                        setattr(item, "patterns180", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patterns180"):
                    opp_val = getattr(item, "patterns180", None)
                    
                    setattr(item, "patterns180", self)
                    

    @property
    def PatternVariable176(self):
        return self.__PatternVariable176

    @PatternVariable176.setter
    def PatternVariable176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__PatternVariable176", None)
        self.__PatternVariable176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patterns177"):
                    opp_val = getattr(item, "patterns177", None)
                    
                    if opp_val == self:
                        setattr(item, "patterns177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patterns177"):
                    opp_val = getattr(item, "patterns177", None)
                    
                    setattr(item, "patterns177", self)
                    

    @property
    def PatternVariable182(self):
        return self.__PatternVariable182

    @PatternVariable182.setter
    def PatternVariable182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__PatternVariable182", None)
        self.__PatternVariable182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patterns183"):
                    opp_val = getattr(item, "patterns183", None)
                    
                    if opp_val == self:
                        setattr(item, "patterns183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patterns183"):
                    opp_val = getattr(item, "patterns183", None)
                    
                    setattr(item, "patterns183", self)
                    

    @property
    def MatchEnd173(self):
        return self.__MatchEnd173

    @MatchEnd173.setter
    def MatchEnd173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__MatchEnd173", None)
        self.__MatchEnd173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mapping174"):
                    opp_val = getattr(item, "mapping174", None)
                    
                    if opp_val == self:
                        setattr(item, "mapping174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mapping174"):
                    opp_val = getattr(item, "mapping174", None)
                    
                    setattr(item, "mapping174", self)
                    

    @property
    def PatternVariable170(self):
        return self.__PatternVariable170

    @PatternVariable170.setter
    def PatternVariable170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__PatternVariable170", None)
        self.__PatternVariable170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patterns171"):
                    opp_val = getattr(item, "patterns171", None)
                    
                    if opp_val == self:
                        setattr(item, "patterns171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patterns171"):
                    opp_val = getattr(item, "patterns171", None)
                    
                    setattr(item, "patterns171", self)
                    

    @property
    def Mapping187(self):
        return self.__Mapping187

    @Mapping187.setter
    def Mapping187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__Mapping187", None)
        self.__Mapping187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapping188"):
                opp_val = getattr(old_value, "mapping188", None)
                if opp_val == self:
                    setattr(old_value, "mapping188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapping188"):
                opp_val = getattr(value, "mapping188", None)
                setattr(value, "mapping188", self)

class smif_mapping_MatchEnd(patterns_Computed, constraints_Conditional):

    pass
class constraints_Rule:

    pass
class smif_mapping_Mapping(constraints_Rule, patterns_Pattern):

    def __init__(self, strength: str, PatternVariable227: "PatternVariable" = None, MatchRule230: set["MatchRule"] = None, PatternVariable233: "PatternVariable" = None):
        self.strength = strength
        self.PatternVariable227 = PatternVariable227
        self.MatchRule230 = MatchRule230 if MatchRule230 is not None else set()
        self.PatternVariable233 = PatternVariable233
        
    @property
    def strength(self) -> str:
        return self.__strength

    @strength.setter
    def strength(self, strength: str):
        self.__strength = strength

    @property
    def PatternVariable227(self):
        return self.__PatternVariable227

    @PatternVariable227.setter
    def PatternVariable227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_Mapping__PatternVariable227", None)
        self.__PatternVariable227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patterns228"):
                opp_val = getattr(old_value, "patterns228", None)
                if opp_val == self:
                    setattr(old_value, "patterns228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patterns228"):
                opp_val = getattr(value, "patterns228", None)
                setattr(value, "patterns228", self)

    @property
    def MatchRule230(self):
        return self.__MatchRule230

    @MatchRule230.setter
    def MatchRule230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_Mapping__MatchRule230", None)
        self.__MatchRule230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mapping231"):
                    opp_val = getattr(item, "mapping231", None)
                    
                    if opp_val == self:
                        setattr(item, "mapping231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mapping231"):
                    opp_val = getattr(item, "mapping231", None)
                    
                    setattr(item, "mapping231", self)
                    

    @property
    def PatternVariable233(self):
        return self.__PatternVariable233

    @PatternVariable233.setter
    def PatternVariable233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_Mapping__PatternVariable233", None)
        self.__PatternVariable233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patterns234"):
                opp_val = getattr(old_value, "patterns234", None)
                if opp_val == self:
                    setattr(old_value, "patterns234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patterns234"):
                opp_val = getattr(value, "patterns234", None)
                setattr(value, "patterns234", self)

class smif_constraints_ConditionalRule(constraints_Rule, constraints_Conditional):

    pass
class TypeConstraint:

    pass
class smif_constraints_UniquenessConstraint(TypeConstraint):

    def __init__(self, isPrimaryIdentity: str, PropertyType86: set["PropertyType"] = None):
        self.isPrimaryIdentity = isPrimaryIdentity
        self.PropertyType86 = PropertyType86 if PropertyType86 is not None else set()
        
    @property
    def isPrimaryIdentity(self) -> str:
        return self.__isPrimaryIdentity

    @isPrimaryIdentity.setter
    def isPrimaryIdentity(self, isPrimaryIdentity: str):
        self.__isPrimaryIdentity = isPrimaryIdentity

    @property
    def PropertyType86(self):
        return self.__PropertyType86

    @PropertyType86.setter
    def PropertyType86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_UniquenessConstraint__PropertyType86", None)
        self.__PropertyType86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties87"):
                    opp_val = getattr(item, "properties87", None)
                    
                    if opp_val == self:
                        setattr(item, "properties87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties87"):
                    opp_val = getattr(item, "properties87", None)
                    
                    setattr(item, "properties87", self)
                    

class smif_constraints_GeneralizationConstraint(TypeConstraint):

    def __init__(self, redefines: str, Type89: "Type" = None, Type92: "Type" = None):
        self.redefines = redefines
        self.Type89 = Type89
        self.Type92 = Type92
        
    @property
    def redefines(self) -> str:
        return self.__redefines

    @redefines.setter
    def redefines(self, redefines: str):
        self.__redefines = redefines

    @property
    def Type92(self):
        return self.__Type92

    @Type92.setter
    def Type92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_GeneralizationConstraint__Type92", None)
        self.__Type92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types93"):
                opp_val = getattr(old_value, "types93", None)
                if opp_val == self:
                    setattr(old_value, "types93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types93"):
                opp_val = getattr(value, "types93", None)
                setattr(value, "types93", self)

    @property
    def Type89(self):
        return self.__Type89

    @Type89.setter
    def Type89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_GeneralizationConstraint__Type89", None)
        self.__Type89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types90"):
                opp_val = getattr(old_value, "types90", None)
                if opp_val == self:
                    setattr(old_value, "types90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types90"):
                opp_val = getattr(value, "types90", None)
                setattr(value, "types90", self)

class smif_constraints_CoveringConstraint(TypeConstraint):

    pass
class smif_constraints_MultiplicityConstraint(TypeConstraint):

    def __init__(self, mininumNumber: str, maximumNumber: str, atOnce: str, isSufficent: str, Type80: set["Type"] = None, Type83: "Type" = None):
        self.mininumNumber = mininumNumber
        self.maximumNumber = maximumNumber
        self.atOnce = atOnce
        self.isSufficent = isSufficent
        self.Type80 = Type80 if Type80 is not None else set()
        self.Type83 = Type83
        
    @property
    def maximumNumber(self) -> str:
        return self.__maximumNumber

    @maximumNumber.setter
    def maximumNumber(self, maximumNumber: str):
        self.__maximumNumber = maximumNumber

    @property
    def mininumNumber(self) -> str:
        return self.__mininumNumber

    @mininumNumber.setter
    def mininumNumber(self, mininumNumber: str):
        self.__mininumNumber = mininumNumber

    @property
    def atOnce(self) -> str:
        return self.__atOnce

    @atOnce.setter
    def atOnce(self, atOnce: str):
        self.__atOnce = atOnce

    @property
    def isSufficent(self) -> str:
        return self.__isSufficent

    @isSufficent.setter
    def isSufficent(self, isSufficent: str):
        self.__isSufficent = isSufficent

    @property
    def Type83(self):
        return self.__Type83

    @Type83.setter
    def Type83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_MultiplicityConstraint__Type83", None)
        self.__Type83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types84"):
                opp_val = getattr(old_value, "types84", None)
                if opp_val == self:
                    setattr(old_value, "types84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types84"):
                opp_val = getattr(value, "types84", None)
                setattr(value, "types84", self)

    @property
    def Type80(self):
        return self.__Type80

    @Type80.setter
    def Type80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_MultiplicityConstraint__Type80", None)
        self.__Type80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types81"):
                    opp_val = getattr(item, "types81", None)
                    
                    if opp_val == self:
                        setattr(item, "types81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types81"):
                    opp_val = getattr(item, "types81", None)
                    
                    setattr(item, "types81", self)
                    

class situations_ActualSituation:

    pass
class smif_properties_CharacteristicBinding(situations_ActualSituation, properties_PropertyBinding):

    pass
class expressions_ExpressionNode:

    pass
class FunctionType:

    pass
class smif_expressions_ObjectOperationType(FunctionType):

    pass
class Evaluation:

    pass
class UnitValue:

    pass
class smif_values_ScalarQuantity(UnitValue):

    def __init__(self, _unnamed_ScalarQuantity: str):
        self._unnamed_ScalarQuantity = _unnamed_ScalarQuantity
        
    @property
    def _unnamed_ScalarQuantity(self) -> str:
        return self.___unnamed_ScalarQuantity

    @_unnamed_ScalarQuantity.setter
    def _unnamed_ScalarQuantity(self, _unnamed_ScalarQuantity: str):
        self.___unnamed_ScalarQuantity = _unnamed_ScalarQuantity

class Value:

    pass
class smif_values_UnitValue(Value):

    def __init__(self, hasValue: str):
        self.hasValue = hasValue
        
    @property
    def hasValue(self) -> str:
        return self.__hasValue

    @hasValue.setter
    def hasValue(self, hasValue: str):
        self.__hasValue = hasValue

class FunctionCall:

    pass
class ExpressionNode:

    pass
class smif_expressions_ConstantReference(ExpressionNode):

    pass
class smif_expressions_Equality(ExpressionNode):

    pass
class expressions_ExpressionContext:

    pass
class UniqueTextIdentifier:

    pass
class smif_lexicalscope_Prefix(UniqueTextIdentifier):

    pass
class smif_identifiers_TechnicalIdentifier(UniqueTextIdentifier):

    pass
class TextIdentifier:

    pass
class smif_identifiers_Name(TextIdentifier):

    pass
class UniqueIdentifier:

    pass
class IdentifiableEntity:

    pass
class smif_toplevel_TemporalEntity(IdentifiableEntity):

    pass
class smif_expressions_ExpressionContext(IdentifiableEntity):

    pass
class smif_toplevel_Context(IdentifiableEntity):

    pass
class smif_toplevel_Proposition(IdentifiableEntity):

    pass
class smif_identifiers_Identifier(Value):

    pass
class identifiers_TextIdentifier:

    pass
class identifiers_UniqueIdentifier:

    pass
class smif_identifiers_UniqueTextIdentifier(identifiers_UniqueIdentifier, identifiers_TextIdentifier):

    pass
class identifiers_UniqueTextIdentifier:

    pass
class identifiers_Name:

    pass
class smif_identifiers_Term(identifiers_UniqueTextIdentifier, identifiers_Name):

    pass
class TechnicalIdentifier:

    pass
class smif_identifiers_IRIIdentifier(TechnicalIdentifier):

    pass
class Namespace:

    pass
class smif_lexicalscope_LexicalScope(Namespace):

    pass
class Identifier:

    pass
class smif_identifiers_TextIdentifier(Identifier):

    def __init__(self, value: str, identifiers104: "smif_toplevel_IdentifiableEntity", identifiers110: "smif_toplevel_IdentifiableEntity"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smif_identifiers_UniqueIdentifier(Identifier):

    pass
class RepresentationRule:

    pass
class MatchEnd:

    pass
class properties_PropertyOwner:

    pass
class smif_relationships_Relationship(situations_ActualSituation, properties_PropertyOwner):

    pass
class smif_expressions_FunctionCall(expressions_ExpressionNode, properties_PropertyOwner):

    pass
class smif_records_Record(situations_ActualSituation, properties_PropertyOwner):

    pass
class smif_expressions_Traversal(expressions_ExpressionNode, properties_PropertyOwner):

    def __init__(self, traverseToRelation: str, inverse: str, PropertyType57: set["PropertyType"] = None):
        self.traverseToRelation = traverseToRelation
        self.inverse = inverse
        self.PropertyType57 = PropertyType57 if PropertyType57 is not None else set()
        
    @property
    def inverse(self) -> str:
        return self.__inverse

    @inverse.setter
    def inverse(self, inverse: str):
        self.__inverse = inverse

    @property
    def traverseToRelation(self) -> str:
        return self.__traverseToRelation

    @traverseToRelation.setter
    def traverseToRelation(self, traverseToRelation: str):
        self.__traverseToRelation = traverseToRelation

    @property
    def PropertyType57(self):
        return self.__PropertyType57

    @PropertyType57.setter
    def PropertyType57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_expressions_Traversal__PropertyType57", None)
        self.__PropertyType57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "properties58"):
                    opp_val = getattr(item, "properties58", None)
                    
                    if opp_val == self:
                        setattr(item, "properties58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "properties58"):
                    opp_val = getattr(item, "properties58", None)
                    
                    setattr(item, "properties58", self)
                    

class values_Value:

    pass
class smif_values_StructuredValue(properties_PropertyOwner, values_Value):

    pass
class properties_PropertyOwnerType:

    pass
class smif_records_RecordType(situations_SituationType, properties_PropertyOwnerType):

    pass
class smif_expressions_FunctionType(expressions_ExpressionContext, properties_PropertyOwnerType):

    pass
class smif_relationships_RelationshipType(situations_SituationType, properties_PropertyOwnerType):

    pass
class values_ValueType:

    pass
class smif_values_StructuredValueType(properties_PropertyOwnerType, values_ValueType):

    pass
class Context:

    pass
class smif_identifiers_Namespace(Context):

    pass
class smif_lexicalscope_LexicalReference(Context):

    pass
class smif_values_SystemOfUnits(Context):

    pass
class UnitType:

    pass
class smif_values_BaseUnitType(UnitType):

    pass
class SystemOfUnits:

    pass
class Definition:

    pass
class ValueType:

    pass
class smif_values_UnitType(ValueType):

    def __init__(self, ratio: str, offset: str, symbol: str, smif_values_UnitType: "Definition" = None, SystemOfUnits: "SystemOfUnits" = None, ValueType262: "smif_metadata_Statement", ValueType: "smif_metadata_Statement", ValueType265: "smif_metadata_Statement"):
        self.ratio = ratio
        self.offset = offset
        self.symbol = symbol
        self.smif_values_UnitType = smif_values_UnitType
        self.SystemOfUnits = SystemOfUnits
        
    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def ratio(self) -> str:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: str):
        self.__ratio = ratio

    @property
    def SystemOfUnits(self):
        return self.__SystemOfUnits

    @SystemOfUnits.setter
    def SystemOfUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_values_UnitType__SystemOfUnits", None)
        self.__SystemOfUnits = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "values"):
                opp_val = getattr(old_value, "values", None)
                if opp_val == self:
                    setattr(old_value, "values", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "values"):
                opp_val = getattr(value, "values", None)
                setattr(value, "values", self)

    @property
    def smif_values_UnitType(self):
        return self.__smif_values_UnitType

    @smif_values_UnitType.setter
    def smif_values_UnitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_values_UnitType__smif_values_UnitType", None)
        self.__smif_values_UnitType = value
        
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

class smif_values_QuantityKind(ValueType):

    pass
class situations_Situation:

    pass
class toplevel_ActualEntity:

    pass
class smif_metadata_InformationSource(metadata_Metadata, toplevel_ActualEntity):

    pass
class smif_situations_ActualSituation(toplevel_ActualEntity, situations_Situation):

    pass
class PatternMatch:

    pass
class toplevel_TemporalEntity:

    pass
class toplevel_Proposition:

    pass
class smif_associations_Association(properties_PropertyOwner, toplevel_Proposition):

    pass
class EntityType:

    pass
class smif_situations_SituationType(EntityType):

    pass
class Type:

    pass
class smif_properties_PropertyType(Type):

    pass
class smif_types_UnionType(Type):

    pass
class smif_facets_Facet(Type):

    pass
class smif_properties_PropertyOwnerType(Type):

    pass
class smif_types_EntityType(Type):

    pass
class smif_values_ValueType(Type):

    pass
class smif_types_IntersectionType(Type):

    pass
class ExpressionContext:

    pass
class smif_expressions_ExpressionNode(ExpressionContext):

    def __init__(self, expressionText: str, expressionTextLanguage: str, Evaluation: set["Evaluation"] = None, FunctionType: "FunctionType" = None, expressions151: "smif_toplevel_Context", expressions: "smif_types_Type"):
        self.expressionText = expressionText
        self.expressionTextLanguage = expressionTextLanguage
        self.Evaluation = Evaluation if Evaluation is not None else set()
        self.FunctionType = FunctionType
        
    @property
    def expressionText(self) -> str:
        return self.__expressionText

    @expressionText.setter
    def expressionText(self, expressionText: str):
        self.__expressionText = expressionText

    @property
    def expressionTextLanguage(self) -> str:
        return self.__expressionTextLanguage

    @expressionTextLanguage.setter
    def expressionTextLanguage(self, expressionTextLanguage: str):
        self.__expressionTextLanguage = expressionTextLanguage

    @property
    def FunctionType(self):
        return self.__FunctionType

    @FunctionType.setter
    def FunctionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_expressions_ExpressionNode__FunctionType", None)
        self.__FunctionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions52"):
                opp_val = getattr(old_value, "expressions52", None)
                if opp_val == self:
                    setattr(old_value, "expressions52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions52"):
                opp_val = getattr(value, "expressions52", None)
                setattr(value, "expressions52", self)

    @property
    def Evaluation(self):
        return self.__Evaluation

    @Evaluation.setter
    def Evaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_expressions_ExpressionNode__Evaluation", None)
        self.__Evaluation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expressions50"):
                    opp_val = getattr(item, "expressions50", None)
                    
                    if opp_val == self:
                        setattr(item, "expressions50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expressions50"):
                    opp_val = getattr(item, "expressions50", None)
                    
                    setattr(item, "expressions50", self)
                    

class smif_expressions_Evaluation(ExpressionContext):

    pass
class RecordType:

    pass
class smif_mapping_Facade(RecordType):

    pass
class PropertyTypeConstraint:

    pass
class MultiplicityConstraint:

    pass
class GeneralizationConstraint:

    pass
class smif_constraints_FacetClassificationConstraint(GeneralizationConstraint):

    pass
class CoveringConstraint:

    pass
class PatternOfType:

    pass
class PropertyType:

    pass
class smif_properties_OwnedPropertyType(PropertyType):

    pass
class Thing:

    pass
class smif_properties_PropertyBinding(Thing):

    pass
class smif_properties_PropertyOwner(Thing):

    pass
class smif_toplevel_IdentifiableEntity(Thing):

    pass
class smif_values_Value(Thing):

    pass
class toplevel_Context:

    pass
class lexicalscope_LexicalScope:

    pass
class smif_situations_Situation(lexicalscope_LexicalScope, toplevel_Context, toplevel_TemporalEntity, toplevel_Proposition):

    pass
class smif_patterns_Pattern(lexicalscope_LexicalScope, situations_SituationType, properties_PropertyOwner, situations_Situation):

    pass
class smif_types_Type(lexicalscope_LexicalScope, toplevel_Context):

    pass
class LexicalScope:

    pass
class smif_lexicalscope_Package(LexicalScope):

    pass
class smif_Repository:

    pass