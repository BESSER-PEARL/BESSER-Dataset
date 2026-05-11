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
class UniquenessConstraint:

    pass
class ObjectOperationType:

    pass
class Traversal:

    pass
class Term:

    pass
class IRIIdentifier:

    pass
class metadata_Metadata:

    pass
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
class smif_lexicalscope_LogicalPackage(Package):

    pass
class smif_lexicalscope_PhysicalPackage(Package):

    pass
class smif_lexicalscope_MOFPackage(Package):

    pass
class smif_lexicalscope_Model(Package):

    pass
class ConditionalRule:

    pass
class smif_mapping_RepresentationRule(ConditionalRule):

    def __init__(self, mapAll: str, representsRule: "Type" = None, conceptRule: set["Type"] = None):
        self.mapAll = mapAll
        self.representsRule = representsRule
        self.conceptRule = conceptRule if conceptRule is not None else set()
        
        pass
    @property
    def mapAll(self):
        return self.__mapAll

    @mapAll.setter
    def mapAll(self, mapAll: str):
        self.__mapAll = mapAll


    @property
    def representsRule(self):
        return self.__representsRule

    @representsRule.setter
    def representsRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_RepresentationRule__representsRule", None)
        self.__representsRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type155"):
                opp_val = getattr(old_value, "Type155", None)
                if opp_val == self:
                    setattr(old_value, "Type155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type155"):
                opp_val = getattr(value, "Type155", None)
                setattr(value, "Type155", self)

    @property
    def conceptRule(self):
        return self.__conceptRule

    @conceptRule.setter
    def conceptRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_RepresentationRule__conceptRule", None)
        self.__conceptRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type157"):
                    opp_val = getattr(item, "Type157", None)
                    
                    if opp_val == self:
                        setattr(item, "Type157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type157"):
                    opp_val = getattr(item, "Type157", None)
                    
                    setattr(item, "Type157", self)
                    

class Facade:

    pass
class smif_mapping_ComputedFacade(Facade):

    def __init__(self):
        
        pass
    def push(self) :
        # TODO: Implement push method
        pass

    def pull(self) :
        # TODO: Implement pull method
        pass

class Situation:

    pass
class VariableBinding:

    pass
class patterns_Pattern:

    pass
class MatchRule:

    pass
class smif_patterns_Computed(ABC):

    pass
class OwnedPropertyBinding:

    pass
class smif_patterns_VariableBinding(OwnedPropertyBinding):

    pass
class Pattern:

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
        
        pass
    @property
    def isBoundaryPart(self):
        return self.__isBoundaryPart

    @isBoundaryPart.setter
    def isBoundaryPart(self, isBoundaryPart: str):
        self.__isBoundaryPart = isBoundaryPart


class patterns_Computed:

    pass
class patterns_PatternVariable:

    pass
class smif_patterns_ExpressionVariable(patterns_PatternVariable, patterns_Computed):

    pass
class Mapping:

    pass
class Equality:

    pass
class properties_OwnedPropertyType:

    pass
class PatternVariable:

    pass
class smif_patterns_TypePatternVariable(PatternVariable):

    pass
class smif_patterns_PropositionVariable(PatternVariable):

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
class Statement:

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
class smif_metadata_Statement(Metadata):

    pass
class smif_metadata_Definition(Metadata):

    def __init__(self, textDefinition: str, summaryDescription: str, smif_metadata_Definition: "IRIIdentifier" = None, smif_metadata_Definition185: "Term" = None, definedBy: "IdentifiableEntity" = None, Metadata: "smif_toplevel_IdentifiableEntity" = None):
        self.textDefinition = textDefinition
        self.summaryDescription = summaryDescription
        self.smif_metadata_Definition = smif_metadata_Definition
        self.smif_metadata_Definition185 = smif_metadata_Definition185
        self.definedBy = definedBy
        
        pass
    @property
    def textDefinition(self):
        return self.__textDefinition

    @textDefinition.setter
    def textDefinition(self, textDefinition: str):
        self.__textDefinition = textDefinition


    @property
    def summaryDescription(self):
        return self.__summaryDescription

    @summaryDescription.setter
    def summaryDescription(self, summaryDescription: str):
        self.__summaryDescription = summaryDescription


    @property
    def definedBy(self):
        return self.__definedBy

    @definedBy.setter
    def definedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_metadata_Definition__definedBy", None)
        self.__definedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IdentifiableEntity187"):
                opp_val = getattr(old_value, "IdentifiableEntity187", None)
                if opp_val == self:
                    setattr(old_value, "IdentifiableEntity187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifiableEntity187"):
                opp_val = getattr(value, "IdentifiableEntity187", None)
                setattr(value, "IdentifiableEntity187", self)

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

    @property
    def smif_metadata_Definition185(self):
        return self.__smif_metadata_Definition185

    @smif_metadata_Definition185.setter
    def smif_metadata_Definition185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_metadata_Definition__smif_metadata_Definition185", None)
        self.__smif_metadata_Definition185 = value
        
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

class constraints_Conditional:

    pass
class smif_mapping_MatchEnd(patterns_Computed, constraints_Conditional):

    pass
class smif_patterns_PatternVariable(properties_OwnedPropertyType, constraints_Conditional):

    def __init__(self, qualification: str, explicit: str, mapsVariable: set["MatchEnd"] = None, hasSubset: set["PatternVariable"] = None, excludes: set["PatternVariable"] = None, excludedBy: set["PatternVariable"] = None, referenceFocus: "Mapping" = None, concreteFocus: "Mapping" = None, ownsVariable: "Pattern" = None, subsets: set["PatternVariable"] = None):
        self.qualification = qualification
        self.explicit = explicit
        self.mapsVariable = mapsVariable if mapsVariable is not None else set()
        self.hasSubset = hasSubset if hasSubset is not None else set()
        self.excludes = excludes if excludes is not None else set()
        self.excludedBy = excludedBy if excludedBy is not None else set()
        self.referenceFocus = referenceFocus
        self.concreteFocus = concreteFocus
        self.ownsVariable = ownsVariable
        self.subsets = subsets if subsets is not None else set()
        
        pass
    @property
    def explicit(self):
        return self.__explicit

    @explicit.setter
    def explicit(self, explicit: str):
        self.__explicit = explicit


    @property
    def qualification(self):
        return self.__qualification

    @qualification.setter
    def qualification(self, qualification: str):
        self.__qualification = qualification


    @property
    def ownsVariable(self):
        return self.__ownsVariable

    @ownsVariable.setter
    def ownsVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__ownsVariable", None)
        self.__ownsVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern"):
                opp_val = getattr(old_value, "Pattern", None)
                if opp_val == self:
                    setattr(old_value, "Pattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern"):
                opp_val = getattr(value, "Pattern", None)
                setattr(value, "Pattern", self)

    @property
    def mapsVariable(self):
        return self.__mapsVariable

    @mapsVariable.setter
    def mapsVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__mapsVariable", None)
        self.__mapsVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MatchEnd113"):
                    opp_val = getattr(item, "MatchEnd113", None)
                    
                    if opp_val == self:
                        setattr(item, "MatchEnd113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MatchEnd113"):
                    opp_val = getattr(item, "MatchEnd113", None)
                    
                    setattr(item, "MatchEnd113", self)
                    

    @property
    def subsets(self):
        return self.__subsets

    @subsets.setter
    def subsets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__subsets", None)
        self.__subsets = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PatternVariable111"):
                    opp_val = getattr(item, "PatternVariable111", None)
                    
                    if opp_val == self:
                        setattr(item, "PatternVariable111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PatternVariable111"):
                    opp_val = getattr(item, "PatternVariable111", None)
                    
                    setattr(item, "PatternVariable111", self)
                    

    @property
    def hasSubset(self):
        return self.__hasSubset

    @hasSubset.setter
    def hasSubset(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__hasSubset", None)
        self.__hasSubset = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PatternVariable115"):
                    opp_val = getattr(item, "PatternVariable115", None)
                    
                    if opp_val == self:
                        setattr(item, "PatternVariable115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PatternVariable115"):
                    opp_val = getattr(item, "PatternVariable115", None)
                    
                    setattr(item, "PatternVariable115", self)
                    

    @property
    def excludedBy(self):
        return self.__excludedBy

    @excludedBy.setter
    def excludedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__excludedBy", None)
        self.__excludedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PatternVariable119"):
                    opp_val = getattr(item, "PatternVariable119", None)
                    
                    if opp_val == self:
                        setattr(item, "PatternVariable119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PatternVariable119"):
                    opp_val = getattr(item, "PatternVariable119", None)
                    
                    setattr(item, "PatternVariable119", self)
                    

    @property
    def excludes(self):
        return self.__excludes

    @excludes.setter
    def excludes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__excludes", None)
        self.__excludes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PatternVariable117"):
                    opp_val = getattr(item, "PatternVariable117", None)
                    
                    if opp_val == self:
                        setattr(item, "PatternVariable117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PatternVariable117"):
                    opp_val = getattr(item, "PatternVariable117", None)
                    
                    setattr(item, "PatternVariable117", self)
                    

    @property
    def referenceFocus(self):
        return self.__referenceFocus

    @referenceFocus.setter
    def referenceFocus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__referenceFocus", None)
        self.__referenceFocus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mapping"):
                opp_val = getattr(old_value, "Mapping", None)
                if opp_val == self:
                    setattr(old_value, "Mapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mapping"):
                opp_val = getattr(value, "Mapping", None)
                setattr(value, "Mapping", self)

    @property
    def concreteFocus(self):
        return self.__concreteFocus

    @concreteFocus.setter
    def concreteFocus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_patterns_PatternVariable__concreteFocus", None)
        self.__concreteFocus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mapping122"):
                opp_val = getattr(old_value, "Mapping122", None)
                if opp_val == self:
                    setattr(old_value, "Mapping122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mapping122"):
                opp_val = getattr(value, "Mapping122", None)
                setattr(value, "Mapping122", self)

class constraints_Rule:

    pass
class smif_mapping_Mapping(constraints_Rule, patterns_Pattern):

    def __init__(self, strength: str, referenceMapping: "PatternVariable" = None, concreteMapping: "PatternVariable" = None, mapRuleOf: set["MatchRule"] = None):
        self.strength = strength
        self.referenceMapping = referenceMapping
        self.concreteMapping = concreteMapping
        self.mapRuleOf = mapRuleOf if mapRuleOf is not None else set()
        
        pass
    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength: str):
        self.__strength = strength


    @property
    def concreteMapping(self):
        return self.__concreteMapping

    @concreteMapping.setter
    def concreteMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_Mapping__concreteMapping", None)
        self.__concreteMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PatternVariable149"):
                opp_val = getattr(old_value, "PatternVariable149", None)
                if opp_val == self:
                    setattr(old_value, "PatternVariable149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PatternVariable149"):
                opp_val = getattr(value, "PatternVariable149", None)
                setattr(value, "PatternVariable149", self)

    @property
    def mapRuleOf(self):
        return self.__mapRuleOf

    @mapRuleOf.setter
    def mapRuleOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_Mapping__mapRuleOf", None)
        self.__mapRuleOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MatchRule151"):
                    opp_val = getattr(item, "MatchRule151", None)
                    
                    if opp_val == self:
                        setattr(item, "MatchRule151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MatchRule151"):
                    opp_val = getattr(item, "MatchRule151", None)
                    
                    setattr(item, "MatchRule151", self)
                    

    @property
    def referenceMapping(self):
        return self.__referenceMapping

    @referenceMapping.setter
    def referenceMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_Mapping__referenceMapping", None)
        self.__referenceMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PatternVariable153"):
                opp_val = getattr(old_value, "PatternVariable153", None)
                if opp_val == self:
                    setattr(old_value, "PatternVariable153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PatternVariable153"):
                opp_val = getattr(value, "PatternVariable153", None)
                setattr(value, "PatternVariable153", self)

class smif_constraints_ConditionalRule(constraints_Rule, constraints_Conditional):

    pass
class smif_constraints_Conditional(ABC):

    pass
class PropertyConstraint:

    pass
class smif_constraints_PropertyTypeConstraint(PropertyConstraint):

    def __init__(self, prerequisiteType: str, propertiesOfType: "Type" = None):
        self.prerequisiteType = prerequisiteType
        self.propertiesOfType = propertiesOfType
        
        pass
    @property
    def prerequisiteType(self):
        return self.__prerequisiteType

    @prerequisiteType.setter
    def prerequisiteType(self, prerequisiteType: str):
        self.__prerequisiteType = prerequisiteType


    @property
    def propertiesOfType(self):
        return self.__propertiesOfType

    @propertiesOfType.setter
    def propertiesOfType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_PropertyTypeConstraint__propertiesOfType", None)
        self.__propertiesOfType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type63"):
                opp_val = getattr(old_value, "Type63", None)
                if opp_val == self:
                    setattr(old_value, "Type63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type63"):
                opp_val = getattr(value, "Type63", None)
                setattr(value, "Type63", self)

class smif_constraints_PropertyTransitivityConstraint(PropertyConstraint):

    pass
class TypeConstraint:

    pass
class smif_constraints_CoveringConstraint(TypeConstraint):

    pass
class smif_constraints_UniquenessConstraint(TypeConstraint):

    def __init__(self, isPrimaryIdentity: str, hasUniquenessConstraint: set["PropertyType"] = None):
        self.isPrimaryIdentity = isPrimaryIdentity
        self.hasUniquenessConstraint = hasUniquenessConstraint if hasUniquenessConstraint is not None else set()
        
        pass
    @property
    def isPrimaryIdentity(self):
        return self.__isPrimaryIdentity

    @isPrimaryIdentity.setter
    def isPrimaryIdentity(self, isPrimaryIdentity: str):
        self.__isPrimaryIdentity = isPrimaryIdentity


    @property
    def hasUniquenessConstraint(self):
        return self.__hasUniquenessConstraint

    @hasUniquenessConstraint.setter
    def hasUniquenessConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_UniquenessConstraint__hasUniquenessConstraint", None)
        self.__hasUniquenessConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PropertyType57"):
                    opp_val = getattr(item, "PropertyType57", None)
                    
                    if opp_val == self:
                        setattr(item, "PropertyType57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PropertyType57"):
                    opp_val = getattr(item, "PropertyType57", None)
                    
                    setattr(item, "PropertyType57", self)
                    

class smif_constraints_GeneralizationConstraint(TypeConstraint):

    def __init__(self, redefines: str, hasSpecialization: "Type" = None, hasGeneralization: "Type" = None):
        self.redefines = redefines
        self.hasSpecialization = hasSpecialization
        self.hasGeneralization = hasGeneralization
        
        pass
    @property
    def redefines(self):
        return self.__redefines

    @redefines.setter
    def redefines(self, redefines: str):
        self.__redefines = redefines


    @property
    def hasGeneralization(self):
        return self.__hasGeneralization

    @hasGeneralization.setter
    def hasGeneralization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_GeneralizationConstraint__hasGeneralization", None)
        self.__hasGeneralization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type61"):
                opp_val = getattr(old_value, "Type61", None)
                if opp_val == self:
                    setattr(old_value, "Type61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type61"):
                opp_val = getattr(value, "Type61", None)
                setattr(value, "Type61", self)

    @property
    def hasSpecialization(self):
        return self.__hasSpecialization

    @hasSpecialization.setter
    def hasSpecialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_GeneralizationConstraint__hasSpecialization", None)
        self.__hasSpecialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type59"):
                opp_val = getattr(old_value, "Type59", None)
                if opp_val == self:
                    setattr(old_value, "Type59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type59"):
                opp_val = getattr(value, "Type59", None)
                setattr(value, "Type59", self)

class Type:

    pass
class smif_types_EntityType(Type):

    pass
class smif_types_UnionType(Type):

    pass
class smif_properties_PropertyOwnerType(Type):

    pass
class smif_facets_Facet(Type):

    pass
class smif_properties_PropertyType(Type):

    pass
class smif_types_IntersectionType(Type):

    pass
class RepresentationRule:

    pass
class MatchEnd:

    pass
class ExpressionContext:

    pass
class smif_expressions_Evaluation(ExpressionContext):

    pass
class smif_values_ValueType(Type):

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

    def __init__(self, ratio: str, offset: str, symbol: str, unitOfSystem: "SystemOfUnits" = None, smif_values_UnitType: "Definition" = None, ValueType173: "smif_metadata_Statement" = None, ValueType: "smif_metadata_Statement" = None, ValueType176: "smif_metadata_Statement" = None):
        self.ratio = ratio
        self.offset = offset
        self.symbol = symbol
        self.unitOfSystem = unitOfSystem
        self.smif_values_UnitType = smif_values_UnitType
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset


    @property
    def ratio(self):
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: str):
        self.__ratio = ratio


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

    @property
    def unitOfSystem(self):
        return self.__unitOfSystem

    @unitOfSystem.setter
    def unitOfSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_values_UnitType__unitOfSystem", None)
        self.__unitOfSystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SystemOfUnits"):
                opp_val = getattr(old_value, "SystemOfUnits", None)
                if opp_val == self:
                    setattr(old_value, "SystemOfUnits", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SystemOfUnits"):
                opp_val = getattr(value, "SystemOfUnits", None)
                setattr(value, "SystemOfUnits", self)

class smif_values_QuantityKind(ValueType):

    pass
class situations_Situation:

    pass
class toplevel_ActualEntity:

    pass
class smif_metadata_InformationSource(metadata_Metadata, toplevel_ActualEntity):

    pass
class smif_situations_ActualSituation(situations_Situation, toplevel_ActualEntity):

    pass
class PatternMatch:

    pass
class toplevel_TemporalEntity:

    pass
class toplevel_Proposition:

    pass
class EntityType:

    pass
class smif_situations_SituationType(EntityType):

    pass
class LexicalScope:

    pass
class smif_lexicalscope_Package(LexicalScope):

    pass
class smif_Repository:

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
class toplevel_Context:

    pass
class lexicalscope_LexicalScope:

    pass
class smif_situations_Situation(lexicalscope_LexicalScope, toplevel_TemporalEntity, toplevel_Proposition, toplevel_Context):

    pass
class smif_types_Type(lexicalscope_LexicalScope, toplevel_Context):

    pass
class smif_constraints_MultiplicityConstraint(TypeConstraint):

    def __init__(self, mininumNumber: str, maximumNumber: str, atOnce: str, isSufficent: str, respectOf: set["Type"] = None, hasMultiplicity: "Type" = None):
        self.mininumNumber = mininumNumber
        self.maximumNumber = maximumNumber
        self.atOnce = atOnce
        self.isSufficent = isSufficent
        self.respectOf = respectOf if respectOf is not None else set()
        self.hasMultiplicity = hasMultiplicity
        
        pass
    @property
    def isSufficent(self):
        return self.__isSufficent

    @isSufficent.setter
    def isSufficent(self, isSufficent: str):
        self.__isSufficent = isSufficent


    @property
    def maximumNumber(self):
        return self.__maximumNumber

    @maximumNumber.setter
    def maximumNumber(self, maximumNumber: str):
        self.__maximumNumber = maximumNumber


    @property
    def atOnce(self):
        return self.__atOnce

    @atOnce.setter
    def atOnce(self, atOnce: str):
        self.__atOnce = atOnce


    @property
    def mininumNumber(self):
        return self.__mininumNumber

    @mininumNumber.setter
    def mininumNumber(self, mininumNumber: str):
        self.__mininumNumber = mininumNumber


    @property
    def hasMultiplicity(self):
        return self.__hasMultiplicity

    @hasMultiplicity.setter
    def hasMultiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_MultiplicityConstraint__hasMultiplicity", None)
        self.__hasMultiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type55"):
                opp_val = getattr(old_value, "Type55", None)
                if opp_val == self:
                    setattr(old_value, "Type55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type55"):
                opp_val = getattr(value, "Type55", None)
                setattr(value, "Type55", self)

    @property
    def respectOf(self):
        return self.__respectOf

    @respectOf.setter
    def respectOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_constraints_MultiplicityConstraint__respectOf", None)
        self.__respectOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type53"):
                    opp_val = getattr(item, "Type53", None)
                    
                    if opp_val == self:
                        setattr(item, "Type53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type53"):
                    opp_val = getattr(item, "Type53", None)
                    
                    setattr(item, "Type53", self)
                    

class Rule:

    pass
class smif_constraints_TypeConstraint(Rule):

    pass
class smif_constraints_Disjoint(Rule):

    pass
class smif_constraints_PropertyConstraint(Rule):

    pass
class smif_constraints_Equivalent(Rule):

    pass
class smif_mapping_MatchRule(Rule):

    def __init__(self, coerce: str, matchFrom: "MatchEnd" = None, matchTo: "MatchEnd" = None, hasMapRule: "Mapping" = None, Rule: "smif_constraints_Rule" = None, Rule78: "smif_toplevel_IdentifiableEntity" = None, Rule51: "smif_constraints_Rule" = None):
        self.coerce = coerce
        self.matchFrom = matchFrom
        self.matchTo = matchTo
        self.hasMapRule = hasMapRule
        
        pass
    @property
    def coerce(self):
        return self.__coerce

    @coerce.setter
    def coerce(self, coerce: str):
        self.__coerce = coerce


    @property
    def matchTo(self):
        return self.__matchTo

    @matchTo.setter
    def matchTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_MatchRule__matchTo", None)
        self.__matchTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MatchEnd138"):
                opp_val = getattr(old_value, "MatchEnd138", None)
                if opp_val == self:
                    setattr(old_value, "MatchEnd138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchEnd138"):
                opp_val = getattr(value, "MatchEnd138", None)
                setattr(value, "MatchEnd138", self)

    @property
    def matchFrom(self):
        return self.__matchFrom

    @matchFrom.setter
    def matchFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_MatchRule__matchFrom", None)
        self.__matchFrom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MatchEnd136"):
                opp_val = getattr(old_value, "MatchEnd136", None)
                if opp_val == self:
                    setattr(old_value, "MatchEnd136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchEnd136"):
                opp_val = getattr(value, "MatchEnd136", None)
                setattr(value, "MatchEnd136", self)

    @property
    def hasMapRule(self):
        return self.__hasMapRule

    @hasMapRule.setter
    def hasMapRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_mapping_MatchRule__hasMapRule", None)
        self.__hasMapRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mapping140"):
                opp_val = getattr(old_value, "Mapping140", None)
                if opp_val == self:
                    setattr(old_value, "Mapping140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mapping140"):
                opp_val = getattr(value, "Mapping140", None)
                setattr(value, "Mapping140", self)

class smif_constraints_Enumerated(Rule):

    pass
class Proposition:

    pass
class smif_constraints_Rule(Proposition):

    pass
class situations_SituationType:

    pass
class smif_properties_CharacteristicType(properties_PropertyType, situations_SituationType):

    pass
class smif_facets_Phase(facets_Facet, situations_SituationType):

    pass
class situations_ActualSituation:

    pass
class smif_properties_CharacteristicBinding(properties_PropertyBinding, situations_ActualSituation):

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
class smif_toplevel_Proposition(IdentifiableEntity):

    pass
class smif_toplevel_Context(IdentifiableEntity):

    pass
class smif_expressions_ExpressionContext(IdentifiableEntity):

    pass
class identifiers_TextIdentifier:

    pass
class identifiers_UniqueIdentifier:

    pass
class expressions_ExpressionNode:

    pass
class FunctionType:

    pass
class smif_expressions_ObjectOperationType(FunctionType):

    pass
class Evaluation:

    pass
class smif_expressions_ExpressionNode(ExpressionContext):

    def __init__(self, expressionText: str, expressionTextLanguage: str, evaluates: set["Evaluation"] = None, implementedBy: "FunctionType" = None, ExpressionContext: "smif_types_Type" = None, ExpressionContext99: "smif_toplevel_Context" = None):
        self.expressionText = expressionText
        self.expressionTextLanguage = expressionTextLanguage
        self.evaluates = evaluates if evaluates is not None else set()
        self.implementedBy = implementedBy
        
        pass
    @property
    def expressionText(self):
        return self.__expressionText

    @expressionText.setter
    def expressionText(self, expressionText: str):
        self.__expressionText = expressionText


    @property
    def expressionTextLanguage(self):
        return self.__expressionTextLanguage

    @expressionTextLanguage.setter
    def expressionTextLanguage(self, expressionTextLanguage: str):
        self.__expressionTextLanguage = expressionTextLanguage


    @property
    def implementedBy(self):
        return self.__implementedBy

    @implementedBy.setter
    def implementedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_expressions_ExpressionNode__implementedBy", None)
        self.__implementedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FunctionType"):
                opp_val = getattr(old_value, "FunctionType", None)
                if opp_val == self:
                    setattr(old_value, "FunctionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FunctionType"):
                opp_val = getattr(value, "FunctionType", None)
                setattr(value, "FunctionType", self)

    @property
    def evaluates(self):
        return self.__evaluates

    @evaluates.setter
    def evaluates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_expressions_ExpressionNode__evaluates", None)
        self.__evaluates = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Evaluation"):
                    opp_val = getattr(item, "Evaluation", None)
                    
                    if opp_val == self:
                        setattr(item, "Evaluation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Evaluation"):
                    opp_val = getattr(item, "Evaluation", None)
                    
                    setattr(item, "Evaluation", self)
                    

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
class properties_PropertyOwner:

    pass
class smif_expressions_FunctionCall(expressions_ExpressionNode, properties_PropertyOwner):

    pass
class smif_relationships_Relationship(properties_PropertyOwner, situations_ActualSituation):

    pass
class smif_patterns_Pattern(situations_Situation, lexicalscope_LexicalScope, situations_SituationType, properties_PropertyOwner):

    pass
class smif_associations_Association(toplevel_Proposition, properties_PropertyOwner):

    pass
class smif_records_Record(properties_PropertyOwner, situations_ActualSituation):

    pass
class smif_expressions_Traversal(expressions_ExpressionNode, properties_PropertyOwner):

    def __init__(self, traverseToRelation: str, inverse: str, traversedBy: set["PropertyType"] = None):
        self.traverseToRelation = traverseToRelation
        self.inverse = inverse
        self.traversedBy = traversedBy if traversedBy is not None else set()
        
        pass
    @property
    def traverseToRelation(self):
        return self.__traverseToRelation

    @traverseToRelation.setter
    def traverseToRelation(self, traverseToRelation: str):
        self.__traverseToRelation = traverseToRelation


    @property
    def inverse(self):
        return self.__inverse

    @inverse.setter
    def inverse(self, inverse: str):
        self.__inverse = inverse


    @property
    def traversedBy(self):
        return self.__traversedBy

    @traversedBy.setter
    def traversedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smif_expressions_Traversal__traversedBy", None)
        self.__traversedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PropertyType38"):
                    opp_val = getattr(item, "PropertyType38", None)
                    
                    if opp_val == self:
                        setattr(item, "PropertyType38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PropertyType38"):
                    opp_val = getattr(item, "PropertyType38", None)
                    
                    setattr(item, "PropertyType38", self)
                    

class values_Value:

    pass
class smif_values_StructuredValue(values_Value, properties_PropertyOwner):

    pass
class properties_PropertyOwnerType:

    pass
class smif_relationships_RelationshipType(situations_SituationType, properties_PropertyOwnerType):

    pass
class smif_records_RecordType(situations_SituationType, properties_PropertyOwnerType):

    pass
class smif_expressions_FunctionType(expressions_ExpressionContext, properties_PropertyOwnerType):

    pass
class values_ValueType:

    pass
class smif_values_StructuredValueType(values_ValueType, properties_PropertyOwnerType):

    pass
class Context:

    pass
class smif_lexicalscope_LexicalReference(Context):

    pass
class smif_identifiers_Namespace(Context):

    pass
class smif_values_SystemOfUnits(Context):

    pass
class smif_values_Value(Thing):

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

    def __init__(self, value: str, Identifier73: "smif_toplevel_IdentifiableEntity" = None, Identifier: "smif_toplevel_IdentifiableEntity" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class smif_identifiers_UniqueIdentifier(Identifier):

    pass
class UnitValue:

    pass
class smif_values_ScalarQuantity(UnitValue):

    def __init__(self, _unnamed_ScalarQuantity: str):
        self._unnamed_ScalarQuantity = _unnamed_ScalarQuantity
        
        pass
    @property
    def _unnamed_ScalarQuantity(self):
        return self.___unnamed_ScalarQuantity

    @_unnamed_ScalarQuantity.setter
    def _unnamed_ScalarQuantity(self, _unnamed_ScalarQuantity: str):
        self.___unnamed_ScalarQuantity = _unnamed_ScalarQuantity


class Value:

    pass
class smif_values_UnitValue(Value):

    def __init__(self, hasValue: str):
        self.hasValue = hasValue
        
        pass
    @property
    def hasValue(self):
        return self.__hasValue

    @hasValue.setter
    def hasValue(self, hasValue: str):
        self.__hasValue = hasValue


class smif_identifiers_Identifier(Value):

    pass