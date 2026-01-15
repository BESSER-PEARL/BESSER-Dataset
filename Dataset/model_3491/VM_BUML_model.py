####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
vM_PackageDeclaration = Class(name="vM::PackageDeclaration")
VmBlock = Class(name="VmBlock")
vM_ImportDeclaration = Class(name="vM::ImportDeclaration")
vM_MetaDataDeclaration = Class(name="vM::MetaDataDeclaration")
vM_Version = Class(name="vM::Version")
vM_Email = Class(name="vM::Email")
vM_Relationships = Class(name="vM::Relationships")
vM_FeatureHierarchy = Class(name="vM::FeatureHierarchy")
FeatureDefinition = Class(name="FeatureDefinition")
vM_Model = Class(name="vM::Model")
vM_VmBlock = Class(name="vM::VmBlock")
vM_FeaturesGroup = Class(name="vM::FeaturesGroup")
vM_Xorgroup = Class(name="vM::Xorgroup")
FeaturesGroup = Class(name="FeaturesGroup")
vM_Orgroup = Class(name="vM::Orgroup")
vM_CardinalityBased = Class(name="vM::CardinalityBased")
vM_Attributes = Class(name="vM::Attributes")
vM_AttrDef = Class(name="vM::AttrDef")
vM_BasicAttrValuation = Class(name="vM::BasicAttrValuation")
vM_BasicAttrDef = Class(name="vM::BasicAttrDef")
vM_EnumAttrDef = Class(name="vM::EnumAttrDef")
vM_BooleanAttrDef = Class(name="vM::BooleanAttrDef")
BasicAttrDef = Class(name="BasicAttrDef")
vM_Boolean_ATT_ID = Class(name="vM::Boolean::ATT::ID")
vM_BoolDefaultDef = Class(name="vM::BoolDefaultDef")
vM_StringAttrDef = Class(name="vM::StringAttrDef")
vM_Feature = Class(name="vM::Feature")
vM_String_ATT_ID = Class(name="vM::String::ATT::ID")
vM_FeatureDefinition = Class(name="vM::FeatureDefinition")
vM_StringDefaultDef = Class(name="vM::StringDefaultDef")
vM_IntegerAttrDefBounded = Class(name="vM::IntegerAttrDefBounded")
IntegerAttrDef = Class(name="IntegerAttrDef")
vM_IntegerAttrDefComplement = Class(name="vM::IntegerAttrDefComplement")
vM_IntegerDeltaDef = Class(name="vM::IntegerDeltaDef")
vM_IntegerAttrDefUnbounded = Class(name="vM::IntegerAttrDefUnbounded")
vM_RealAttrDef = Class(name="vM::RealAttrDef")
vM_Real_ATT_ID = Class(name="vM::Real::ATT::ID")
vM_RealDefaultDef = Class(name="vM::RealDefaultDef")
vM_RealAttrDefBounded = Class(name="vM::RealAttrDefBounded")
RealAttrDef = Class(name="RealAttrDef")
vM_RealAttrDefComplement = Class(name="vM::RealAttrDefComplement")
vM_RealDeltaDef = Class(name="vM::RealDeltaDef")
vM_IntegerAttrDef = Class(name="vM::IntegerAttrDef")
vM_Integer_ATT_ID = Class(name="vM::Integer::ATT::ID")
vM_IntegerDefaultDef = Class(name="vM::IntegerDefaultDef")
EnumAttrDef = Class(name="EnumAttrDef")
vM_Enum_String_ATT_ID = Class(name="vM::Enum::String::ATT::ID")
vM_EnumIntegerDef = Class(name="vM::EnumIntegerDef")
vM_Enum_Integer_ATT_ID = Class(name="vM::Enum::Integer::ATT::ID")
vM_EnumRealDef = Class(name="vM::EnumRealDef")
vM_Enum_Real_ATT_ID = Class(name="vM::Enum::Real::ATT::ID")
vM_RealAttrDefUnbounded = Class(name="vM::RealAttrDefUnbounded")
vM_Descriptions = Class(name="vM::Descriptions")
vM_EnumStringDef = Class(name="vM::EnumStringDef")
vM_FeatureDescription = Class(name="vM::FeatureDescription")
vM_AttributeDescription = Class(name="vM::AttributeDescription")
vM_Abstract_ATT_ID = Class(name="vM::Abstract::ATT::ID")
vM_Constraints = Class(name="vM::Constraints")
vM_Constraint = Class(name="vM::Constraint")
vM_ComplexExpression = Class(name="vM::ComplexExpression")
vM_Expression = Class(name="vM::Expression")
ComplexExpression = Class(name="ComplexExpression")
vM_SpecialExpression = Class(name="vM::SpecialExpression")
Expression = Class(name="Expression")
vM_PrimitiveExpression = Class(name="vM::PrimitiveExpression")
vM_AttHead = Class(name="vM::AttHead")
vM_BooleanExpression = Class(name="vM::BooleanExpression")
vM_BooleanExpression_List = Class(name="vM::BooleanExpression::List")
vM_BrackedExpression = Class(name="vM::BrackedExpression")
vM_NumericExpression = Class(name="vM::NumericExpression")
vM_Objectives = Class(name="vM::Objectives")
vM_StringExpression = Class(name="vM::StringExpression")
vM_Objective = Class(name="vM::Objective")
vM_ObjectiveExpression = Class(name="vM::ObjectiveExpression")
vM_NumericExpression_List = Class(name="vM::NumericExpression::List")
vM_BooleanValuation = Class(name="vM::BooleanValuation")
vM_ExtendedValuation = Class(name="vM::ExtendedValuation")
ExtendedValuation = Class(name="ExtendedValuation")
vM_Configurations = Class(name="vM::Configurations")
vM_Configuration = Class(name="vM::Configuration")
vM_IntegerAttrValuation = Class(name="vM::IntegerAttrValuation")
vM_BooleanAttrValuation = Class(name="vM::BooleanAttrValuation")
vM_StringAttrValuation = Class(name="vM::StringAttrValuation")
vM_AdvancedAttrValuation = Class(name="vM::AdvancedAttrValuation")
vM_RealAttrValuation = Class(name="vM::RealAttrValuation")
vM_TableBasedValuationByFeatureAndClone = Class(name="vM::TableBasedValuationByFeatureAndClone")
BasicAttrValuation = Class(name="BasicAttrValuation")
vM_PairAttributeValue = Class(name="vM::PairAttributeValue")
vM_TableBasedValuationByFeature = Class(name="vM::TableBasedValuationByFeature")
vM_TableBasedValuationByAttribute = Class(name="vM::TableBasedValuationByAttribute")
vM_TableBasedValuationByAttributeForInteger = Class(name="vM::TableBasedValuationByAttributeForInteger")
TableBasedValuationByAttribute = Class(name="TableBasedValuationByAttribute")
vM_PairFeatureInteger = Class(name="vM::PairFeatureInteger")
vM_TableBasedValuationByAttributeForReal = Class(name="vM::TableBasedValuationByAttributeForReal")
Abstract_ATT_ID = Class(name="Abstract::ATT::ID")
vM_PairFeatureReal = Class(name="vM::PairFeatureReal")
vM_If = Class(name="vM::If")
vM_LeftImplication = Class(name="vM::LeftImplication")
vM_RightImplication = Class(name="vM::RightImplication")
vM_BiImplication = Class(name="vM::BiImplication")
vM_Or = Class(name="vM::Or")
vM_And = Class(name="vM::And")
vM_Equality = Class(name="vM::Equality")
vM_Inequality = Class(name="vM::Inequality")
vM_Less = Class(name="vM::Less")
vM_Lessequal = Class(name="vM::Lessequal")
vM_Plus = Class(name="vM::Plus")
vM_Minus = Class(name="vM::Minus")
vM_Multiplication = Class(name="vM::Multiplication")
vM_Division = Class(name="vM::Division")
vM_Excludes = Class(name="vM::Excludes")
vM_Greater = Class(name="vM::Greater")
vM_Greaterequal = Class(name="vM::Greaterequal")
vM_Requires = Class(name="vM::Requires")

# vM_PackageDeclaration class attributes and methods
vM_PackageDeclaration_name: Property = Property(name="name", type=StringType)
vM_PackageDeclaration.attributes={vM_PackageDeclaration_name}

# VmBlock class attributes and methods

# vM_ImportDeclaration class attributes and methods
vM_ImportDeclaration_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
vM_ImportDeclaration.attributes={vM_ImportDeclaration_importedNamespace}

# vM_MetaDataDeclaration class attributes and methods
vM_MetaDataDeclaration_name: Property = Property(name="name", type=StringType)
vM_MetaDataDeclaration_description: Property = Property(name="description", type=StringType)
vM_MetaDataDeclaration_author: Property = Property(name="author", type=StringType)
vM_MetaDataDeclaration_organization: Property = Property(name="organization", type=StringType)
vM_MetaDataDeclaration_publication: Property = Property(name="publication", type=StringType)
vM_MetaDataDeclaration_date: Property = Property(name="date", type=StringType)
vM_MetaDataDeclaration.attributes={vM_MetaDataDeclaration_date, vM_MetaDataDeclaration_name, vM_MetaDataDeclaration_organization, vM_MetaDataDeclaration_author, vM_MetaDataDeclaration_publication, vM_MetaDataDeclaration_description}

# vM_Version class attributes and methods
vM_Version_main: Property = Property(name="main", type=IntegerType)
vM_Version_tail: Property = Property(name="tail", type=IntegerType)
vM_Version.attributes={vM_Version_main, vM_Version_tail}

# vM_Email class attributes and methods
vM_Email_username: Property = Property(name="username", type=StringType)
vM_Email_domain: Property = Property(name="domain", type=StringType)
vM_Email.attributes={vM_Email_username, vM_Email_domain}

# vM_Relationships class attributes and methods

# vM_FeatureHierarchy class attributes and methods

# FeatureDefinition class attributes and methods

# vM_Model class attributes and methods

# vM_VmBlock class attributes and methods

# vM_FeaturesGroup class attributes and methods

# vM_Xorgroup class attributes and methods

# FeaturesGroup class attributes and methods

# vM_Orgroup class attributes and methods

# vM_CardinalityBased class attributes and methods
vM_CardinalityBased_min: Property = Property(name="min", type=StringType)
vM_CardinalityBased_max: Property = Property(name="max", type=StringType)
vM_CardinalityBased_all: Property = Property(name="all", type=BooleanType)
vM_CardinalityBased.attributes={vM_CardinalityBased_max, vM_CardinalityBased_all, vM_CardinalityBased_min}

# vM_Attributes class attributes and methods

# vM_AttrDef class attributes and methods
vM_AttrDef_notTranslatable: Property = Property(name="notTranslatable", type=BooleanType)
vM_AttrDef_runTime: Property = Property(name="runTime", type=BooleanType)
vM_AttrDef_notDecidable: Property = Property(name="notDecidable", type=BooleanType)
vM_AttrDef.attributes={vM_AttrDef_notDecidable, vM_AttrDef_notTranslatable, vM_AttrDef_runTime}

# vM_BasicAttrValuation class attributes and methods
vM_BasicAttrValuation_value: Property = Property(name="value", type=StringType)
vM_BasicAttrValuation.attributes={vM_BasicAttrValuation_value}

# vM_BasicAttrDef class attributes and methods

# vM_EnumAttrDef class attributes and methods
vM_EnumAttrDef_value: Property = Property(name="value", type=StringType)
vM_EnumAttrDef.attributes={vM_EnumAttrDef_value}

# vM_BooleanAttrDef class attributes and methods
vM_BooleanAttrDef_value: Property = Property(name="value", type=StringType)
vM_BooleanAttrDef.attributes={vM_BooleanAttrDef_value}

# BasicAttrDef class attributes and methods

# vM_Boolean_ATT_ID class attributes and methods

# vM_BoolDefaultDef class attributes and methods
vM_BoolDefaultDef_value: Property = Property(name="value", type=StringType)
vM_BoolDefaultDef.attributes={vM_BoolDefaultDef_value}

# vM_StringAttrDef class attributes and methods
vM_StringAttrDef_value: Property = Property(name="value", type=StringType)
vM_StringAttrDef.attributes={vM_StringAttrDef_value}

# vM_Feature class attributes and methods
vM_Feature_min: Property = Property(name="min", type=StringType)
vM_Feature_max: Property = Property(name="max", type=StringType)
vM_Feature_name: Property = Property(name="name", type=StringType)
vM_Feature_notTranslatable: Property = Property(name="notTranslatable", type=BooleanType)
vM_Feature_runTime: Property = Property(name="runTime", type=BooleanType)
vM_Feature_notDecidable: Property = Property(name="notDecidable", type=BooleanType)
vM_Feature_optional: Property = Property(name="optional", type=BooleanType)
vM_Feature.attributes={vM_Feature_max, vM_Feature_notDecidable, vM_Feature_min, vM_Feature_notTranslatable, vM_Feature_optional, vM_Feature_runTime, vM_Feature_name}

# vM_String_ATT_ID class attributes and methods

# vM_FeatureDefinition class attributes and methods

# vM_StringDefaultDef class attributes and methods
vM_StringDefaultDef_value: Property = Property(name="value", type=StringType)
vM_StringDefaultDef.attributes={vM_StringDefaultDef_value}

# vM_IntegerAttrDefBounded class attributes and methods

# IntegerAttrDef class attributes and methods

# vM_IntegerAttrDefComplement class attributes and methods
vM_IntegerAttrDefComplement_min: Property = Property(name="min", type=StringType)
vM_IntegerAttrDefComplement_max: Property = Property(name="max", type=StringType)
vM_IntegerAttrDefComplement.attributes={vM_IntegerAttrDefComplement_min, vM_IntegerAttrDefComplement_max}

# vM_IntegerDeltaDef class attributes and methods
vM_IntegerDeltaDef_value: Property = Property(name="value", type=IntegerType)
vM_IntegerDeltaDef.attributes={vM_IntegerDeltaDef_value}

# vM_IntegerAttrDefUnbounded class attributes and methods
vM_IntegerAttrDefUnbounded_value: Property = Property(name="value", type=StringType)
vM_IntegerAttrDefUnbounded.attributes={vM_IntegerAttrDefUnbounded_value}

# vM_RealAttrDef class attributes and methods

# vM_Real_ATT_ID class attributes and methods

# vM_RealDefaultDef class attributes and methods
vM_RealDefaultDef_value: Property = Property(name="value", type=StringType)
vM_RealDefaultDef.attributes={vM_RealDefaultDef_value}

# vM_RealAttrDefBounded class attributes and methods

# RealAttrDef class attributes and methods

# vM_RealAttrDefComplement class attributes and methods
vM_RealAttrDefComplement_min: Property = Property(name="min", type=StringType)
vM_RealAttrDefComplement_max: Property = Property(name="max", type=StringType)
vM_RealAttrDefComplement.attributes={vM_RealAttrDefComplement_max, vM_RealAttrDefComplement_min}

# vM_RealDeltaDef class attributes and methods
vM_RealDeltaDef_value: Property = Property(name="value", type=StringType)
vM_RealDeltaDef.attributes={vM_RealDeltaDef_value}

# vM_IntegerAttrDef class attributes and methods

# vM_Integer_ATT_ID class attributes and methods

# vM_IntegerDefaultDef class attributes and methods
vM_IntegerDefaultDef_value: Property = Property(name="value", type=IntegerType)
vM_IntegerDefaultDef.attributes={vM_IntegerDefaultDef_value}

# EnumAttrDef class attributes and methods

# vM_Enum_String_ATT_ID class attributes and methods

# vM_EnumIntegerDef class attributes and methods

# vM_Enum_Integer_ATT_ID class attributes and methods

# vM_EnumRealDef class attributes and methods

# vM_Enum_Real_ATT_ID class attributes and methods

# vM_RealAttrDefUnbounded class attributes and methods
vM_RealAttrDefUnbounded_value: Property = Property(name="value", type=StringType)
vM_RealAttrDefUnbounded.attributes={vM_RealAttrDefUnbounded_value}

# vM_Descriptions class attributes and methods

# vM_EnumStringDef class attributes and methods

# vM_FeatureDescription class attributes and methods
vM_FeatureDescription_description: Property = Property(name="description", type=StringType)
vM_FeatureDescription.attributes={vM_FeatureDescription_description}

# vM_AttributeDescription class attributes and methods
vM_AttributeDescription_description: Property = Property(name="description", type=StringType)
vM_AttributeDescription.attributes={vM_AttributeDescription_description}

# vM_Abstract_ATT_ID class attributes and methods
vM_Abstract_ATT_ID_name: Property = Property(name="name", type=StringType)
vM_Abstract_ATT_ID.attributes={vM_Abstract_ATT_ID_name}

# vM_Constraints class attributes and methods

# vM_Constraint class attributes and methods
vM_Constraint_name: Property = Property(name="name", type=StringType)
vM_Constraint_not: Property = Property(name="not", type=BooleanType)
vM_Constraint.attributes={vM_Constraint_not, vM_Constraint_name}

# vM_ComplexExpression class attributes and methods

# vM_Expression class attributes and methods

# ComplexExpression class attributes and methods

# vM_SpecialExpression class attributes and methods
vM_SpecialExpression_op: Property = Property(name="op", type=StringType)
vM_SpecialExpression.attributes={vM_SpecialExpression_op}

# Expression class attributes and methods

# vM_PrimitiveExpression class attributes and methods

# vM_AttHead class attributes and methods
vM_AttHead_forAllFeatures: Property = Property(name="forAllFeatures", type=BooleanType)
vM_AttHead.attributes={vM_AttHead_forAllFeatures}

# vM_BooleanExpression class attributes and methods
vM_BooleanExpression_value: Property = Property(name="value", type=StringType)
vM_BooleanExpression_op: Property = Property(name="op", type=StringType)
vM_BooleanExpression.attributes={vM_BooleanExpression_op, vM_BooleanExpression_value}

# vM_BooleanExpression_List class attributes and methods

# vM_BrackedExpression class attributes and methods

# vM_NumericExpression class attributes and methods
vM_NumericExpression_value: Property = Property(name="value", type=StringType)
vM_NumericExpression_op: Property = Property(name="op", type=StringType)
vM_NumericExpression.attributes={vM_NumericExpression_op, vM_NumericExpression_value}

# vM_Objectives class attributes and methods

# vM_StringExpression class attributes and methods
vM_StringExpression_value: Property = Property(name="value", type=StringType)
vM_StringExpression.attributes={vM_StringExpression_value}

# vM_Objective class attributes and methods
vM_Objective_name: Property = Property(name="name", type=StringType)
vM_Objective_op: Property = Property(name="op", type=StringType)
vM_Objective.attributes={vM_Objective_name, vM_Objective_op}

# vM_ObjectiveExpression class attributes and methods
vM_ObjectiveExpression_op: Property = Property(name="op", type=StringType)
vM_ObjectiveExpression.attributes={vM_ObjectiveExpression_op}

# vM_NumericExpression_List class attributes and methods

# vM_BooleanValuation class attributes and methods
vM_BooleanValuation_notSelected: Property = Property(name="notSelected", type=BooleanType)
vM_BooleanValuation.attributes={vM_BooleanValuation_notSelected}

# vM_ExtendedValuation class attributes and methods

# ExtendedValuation class attributes and methods

# vM_Configurations class attributes and methods

# vM_Configuration class attributes and methods
vM_Configuration_name: Property = Property(name="name", type=StringType)
vM_Configuration.attributes={vM_Configuration_name}

# vM_IntegerAttrValuation class attributes and methods

# vM_BooleanAttrValuation class attributes and methods

# vM_StringAttrValuation class attributes and methods

# vM_AdvancedAttrValuation class attributes and methods

# vM_RealAttrValuation class attributes and methods

# vM_TableBasedValuationByFeatureAndClone class attributes and methods
vM_TableBasedValuationByFeatureAndClone_name: Property = Property(name="name", type=StringType)
vM_TableBasedValuationByFeatureAndClone.attributes={vM_TableBasedValuationByFeatureAndClone_name}

# BasicAttrValuation class attributes and methods

# vM_PairAttributeValue class attributes and methods
vM_PairAttributeValue_value: Property = Property(name="value", type=StringType)
vM_PairAttributeValue.attributes={vM_PairAttributeValue_value}

# vM_TableBasedValuationByFeature class attributes and methods

# vM_TableBasedValuationByAttribute class attributes and methods

# vM_TableBasedValuationByAttributeForInteger class attributes and methods

# TableBasedValuationByAttribute class attributes and methods

# vM_PairFeatureInteger class attributes and methods
vM_PairFeatureInteger_value: Property = Property(name="value", type=StringType)
vM_PairFeatureInteger.attributes={vM_PairFeatureInteger_value}

# vM_TableBasedValuationByAttributeForReal class attributes and methods

# Abstract_ATT_ID class attributes and methods

# vM_PairFeatureReal class attributes and methods
vM_PairFeatureReal_value: Property = Property(name="value", type=StringType)
vM_PairFeatureReal.attributes={vM_PairFeatureReal_value}

# vM_If class attributes and methods

# vM_LeftImplication class attributes and methods

# vM_RightImplication class attributes and methods

# vM_BiImplication class attributes and methods

# vM_Or class attributes and methods

# vM_And class attributes and methods

# vM_Equality class attributes and methods

# vM_Inequality class attributes and methods

# vM_Less class attributes and methods

# vM_Lessequal class attributes and methods

# vM_Plus class attributes and methods

# vM_Minus class attributes and methods

# vM_Multiplication class attributes and methods

# vM_Division class attributes and methods

# vM_Excludes class attributes and methods

# vM_Greater class attributes and methods

# vM_Greaterequal class attributes and methods

# vM_Requires class attributes and methods

# Relationships
blocks1: BinaryAssociation = BinaryAssociation(
    name="blocks1",
    ends={
        Property(name="vM_VmBlock2", type=vM_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_PackageDeclaration", type=vM_VmBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
version3: BinaryAssociation = BinaryAssociation(
    name="version3",
    ends={
        Property(name="vM_Version", type=vM_MetaDataDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_MetaDataDeclaration", type=vM_Version, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
email4: BinaryAssociation = BinaryAssociation(
    name="email4",
    ends={
        Property(name="vM_Email", type=vM_MetaDataDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_MetaDataDeclaration5", type=vM_Email, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
root6: BinaryAssociation = BinaryAssociation(
    name="root6",
    ends={
        Property(name="vM_FeatureHierarchy", type=vM_Relationships, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Relationships", type=vM_FeatureHierarchy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocks0: BinaryAssociation = BinaryAssociation(
    name="blocks0",
    ends={
        Property(name="vM_VmBlock", type=vM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Model", type=vM_VmBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupedFeatures11: BinaryAssociation = BinaryAssociation(
    name="groupedFeatures11",
    ends={
        Property(name="vM_FeatureDefinition12", type=vM_FeaturesGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_FeaturesGroup", type=vM_FeatureDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrDefs13: BinaryAssociation = BinaryAssociation(
    name="attrDefs13",
    ends={
        Property(name="vM_AttrDef", type=vM_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Attributes", type=vM_AttrDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrValuations14: BinaryAssociation = BinaryAssociation(
    name="attrValuations14",
    ends={
        Property(name="vM_BasicAttrValuation", type=vM_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Attributes15", type=vM_BasicAttrValuation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicAttrDef16: BinaryAssociation = BinaryAssociation(
    name="basicAttrDef16",
    ends={
        Property(name="vM_BasicAttrDef", type=vM_AttrDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_AttrDef17", type=vM_BasicAttrDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumAttrDef18: BinaryAssociation = BinaryAssociation(
    name="enumAttrDef18",
    ends={
        Property(name="vM_EnumAttrDef", type=vM_AttrDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_AttrDef19", type=vM_EnumAttrDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name20: BinaryAssociation = BinaryAssociation(
    name="name20",
    ends={
        Property(name="vM_Boolean_ATT_ID", type=vM_BooleanAttrDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BooleanAttrDef", type=vM_Boolean_ATT_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default21: BinaryAssociation = BinaryAssociation(
    name="default21",
    ends={
        Property(name="vM_BoolDefaultDef", type=vM_BooleanAttrDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BooleanAttrDef22", type=vM_BoolDefaultDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="vM_Feature", type=vM_FeatureHierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_FeatureHierarchy8", type=vM_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name23: BinaryAssociation = BinaryAssociation(
    name="name23",
    ends={
        Property(name="vM_String_ATT_ID", type=vM_StringAttrDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_StringAttrDef", type=vM_String_ATT_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children9: BinaryAssociation = BinaryAssociation(
    name="children9",
    ends={
        Property(name="vM_FeatureDefinition", type=vM_FeatureHierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_FeatureHierarchy10", type=vM_FeatureDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complements29: BinaryAssociation = BinaryAssociation(
    name="complements29",
    ends={
        Property(name="vM_IntegerAttrDefComplement", type=vM_IntegerAttrDefBounded, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_IntegerAttrDefBounded", type=vM_IntegerAttrDefComplement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complement30: BinaryAssociation = BinaryAssociation(
    name="complement30",
    ends={
        Property(name="vM_IntegerAttrDefComplement32", type=vM_IntegerAttrDefBounded, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_IntegerAttrDefBounded31", type=vM_IntegerAttrDefComplement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delta33: BinaryAssociation = BinaryAssociation(
    name="delta33",
    ends={
        Property(name="vM_IntegerDeltaDef", type=vM_IntegerAttrDefComplement, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_IntegerAttrDefComplement34", type=vM_IntegerDeltaDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name35: BinaryAssociation = BinaryAssociation(
    name="name35",
    ends={
        Property(name="vM_Real_ATT_ID", type=vM_RealAttrDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_RealAttrDef", type=vM_Real_ATT_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default36: BinaryAssociation = BinaryAssociation(
    name="default36",
    ends={
        Property(name="vM_RealDefaultDef", type=vM_RealAttrDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_RealAttrDef37", type=vM_RealDefaultDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
complement38: BinaryAssociation = BinaryAssociation(
    name="complement38",
    ends={
        Property(name="vM_RealAttrDefComplement", type=vM_RealAttrDefBounded, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_RealAttrDefBounded", type=vM_RealAttrDefComplement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delta39: BinaryAssociation = BinaryAssociation(
    name="delta39",
    ends={
        Property(name="vM_RealDeltaDef", type=vM_RealAttrDefComplement, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_RealAttrDefComplement40", type=vM_RealDeltaDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default24: BinaryAssociation = BinaryAssociation(
    name="default24",
    ends={
        Property(name="vM_StringDefaultDef", type=vM_StringAttrDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_StringAttrDef25", type=vM_StringDefaultDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name26: BinaryAssociation = BinaryAssociation(
    name="name26",
    ends={
        Property(name="vM_Integer_ATT_ID", type=vM_IntegerAttrDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_IntegerAttrDef", type=vM_Integer_ATT_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default27: BinaryAssociation = BinaryAssociation(
    name="default27",
    ends={
        Property(name="vM_IntegerDefaultDef", type=vM_IntegerAttrDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_IntegerAttrDef28", type=vM_IntegerDefaultDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name41: BinaryAssociation = BinaryAssociation(
    name="name41",
    ends={
        Property(name="vM_Enum_String_ATT_ID", type=vM_EnumStringDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_EnumStringDef", type=vM_Enum_String_ATT_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default42: BinaryAssociation = BinaryAssociation(
    name="default42",
    ends={
        Property(name="vM_StringDefaultDef44", type=vM_EnumStringDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_EnumStringDef43", type=vM_StringDefaultDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name45: BinaryAssociation = BinaryAssociation(
    name="name45",
    ends={
        Property(name="vM_Enum_Integer_ATT_ID", type=vM_EnumIntegerDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_EnumIntegerDef", type=vM_Enum_Integer_ATT_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default46: BinaryAssociation = BinaryAssociation(
    name="default46",
    ends={
        Property(name="vM_IntegerDefaultDef48", type=vM_EnumIntegerDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_EnumIntegerDef47", type=vM_IntegerDefaultDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name49: BinaryAssociation = BinaryAssociation(
    name="name49",
    ends={
        Property(name="vM_Enum_Real_ATT_ID", type=vM_EnumRealDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_EnumRealDef", type=vM_Enum_Real_ATT_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default50: BinaryAssociation = BinaryAssociation(
    name="default50",
    ends={
        Property(name="vM_RealDefaultDef52", type=vM_EnumRealDef, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_EnumRealDef51", type=vM_RealDefaultDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featuresDescriptions53: BinaryAssociation = BinaryAssociation(
    name="featuresDescriptions53",
    ends={
        Property(name="vM_FeatureDescription", type=vM_Descriptions, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Descriptions", type=vM_FeatureDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributesDescriptions54: BinaryAssociation = BinaryAssociation(
    name="attributesDescriptions54",
    ends={
        Property(name="vM_AttributeDescription", type=vM_Descriptions, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Descriptions55", type=vM_AttributeDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refFeat56: BinaryAssociation = BinaryAssociation(
    name="refFeat56",
    ends={
        Property(name="vM_Feature58", type=vM_FeatureDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_FeatureDescription57", type=vM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
refFeat59: BinaryAssociation = BinaryAssociation(
    name="refFeat59",
    ends={
        Property(name="vM_Feature61", type=vM_AttributeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_AttributeDescription60", type=vM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
refAtt62: BinaryAssociation = BinaryAssociation(
    name="refAtt62",
    ends={
        Property(name="vM_Abstract_ATT_ID", type=vM_AttributeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_AttributeDescription63", type=vM_Abstract_ATT_ID, multiplicity=Multiplicity(0, 1))
    }
)
constraints64: BinaryAssociation = BinaryAssociation(
    name="constraints64",
    ends={
        Property(name="vM_Constraint", type=vM_Constraints, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Constraints", type=vM_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression65: BinaryAssociation = BinaryAssociation(
    name="expression65",
    ends={
        Property(name="vM_ComplexExpression", type=vM_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Constraint66", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureID69: BinaryAssociation = BinaryAssociation(
    name="featureID69",
    ends={
        Property(name="vM_Feature70", type=vM_PrimitiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_PrimitiveExpression", type=vM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
head71: BinaryAssociation = BinaryAssociation(
    name="head71",
    ends={
        Property(name="vM_AttHead", type=vM_PrimitiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_PrimitiveExpression72", type=vM_AttHead, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refAtt73: BinaryAssociation = BinaryAssociation(
    name="refAtt73",
    ends={
        Property(name="vM_Abstract_ATT_ID75", type=vM_PrimitiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_PrimitiveExpression74", type=vM_Abstract_ATT_ID, multiplicity=Multiplicity(0, 1))
    }
)
expression77: BinaryAssociation = BinaryAssociation(
    name="expression77",
    ends={
        Property(name="vM_BooleanExpression", type=vM_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BooleanExpression76", type=vM_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_list78: BinaryAssociation = BinaryAssociation(
    name="expression_list78",
    ends={
        Property(name="vM_BooleanExpression_List", type=vM_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BooleanExpression79", type=vM_BooleanExpression_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression80: BinaryAssociation = BinaryAssociation(
    name="expression80",
    ends={
        Property(name="vM_ComplexExpression81", type=vM_BrackedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BrackedExpression", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex89: BinaryAssociation = BinaryAssociation(
    name="ex89",
    ends={
        Property(name="vM_BooleanExpression91", type=vM_BooleanExpression_List, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BooleanExpression_List90", type=vM_BooleanExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression67: BinaryAssociation = BinaryAssociation(
    name="expression67",
    ends={
        Property(name="vM_Feature68", type=vM_SpecialExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_SpecialExpression", type=vM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
objectives92: BinaryAssociation = BinaryAssociation(
    name="objectives92",
    ends={
        Property(name="vM_Objective", type=vM_Objectives, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Objectives", type=vM_Objective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression93: BinaryAssociation = BinaryAssociation(
    name="expression93",
    ends={
        Property(name="vM_ObjectiveExpression", type=vM_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Objective94", type=vM_ObjectiveExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression95: BinaryAssociation = BinaryAssociation(
    name="expression95",
    ends={
        Property(name="vM_PrimitiveExpression97", type=vM_ObjectiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_ObjectiveExpression96", type=vM_PrimitiveExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression83: BinaryAssociation = BinaryAssociation(
    name="expression83",
    ends={
        Property(name="vM_NumericExpression", type=vM_NumericExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_NumericExpression82", type=vM_NumericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_list84: BinaryAssociation = BinaryAssociation(
    name="expression_list84",
    ends={
        Property(name="vM_NumericExpression_List", type=vM_NumericExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_NumericExpression85", type=vM_NumericExpression_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ex86: BinaryAssociation = BinaryAssociation(
    name="ex86",
    ends={
        Property(name="vM_NumericExpression88", type=vM_NumericExpression_List, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_NumericExpression_List87", type=vM_NumericExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booleanValuation99: BinaryAssociation = BinaryAssociation(
    name="booleanValuation99",
    ends={
        Property(name="vM_BooleanValuation", type=vM_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Configuration100", type=vM_BooleanValuation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedValuation101: BinaryAssociation = BinaryAssociation(
    name="extendedValuation101",
    ends={
        Property(name="vM_ExtendedValuation", type=vM_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Configuration102", type=vM_ExtendedValuation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature103: BinaryAssociation = BinaryAssociation(
    name="feature103",
    ends={
        Property(name="vM_Feature105", type=vM_BooleanValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BooleanValuation104", type=vM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
head106: BinaryAssociation = BinaryAssociation(
    name="head106",
    ends={
        Property(name="vM_AttHead108", type=vM_BasicAttrValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BasicAttrValuation107", type=vM_AttHead, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configurations98: BinaryAssociation = BinaryAssociation(
    name="configurations98",
    ends={
        Property(name="vM_Configuration", type=vM_Configurations, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Configurations", type=vM_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refAtt109: BinaryAssociation = BinaryAssociation(
    name="refAtt109",
    ends={
        Property(name="vM_Real_ATT_ID110", type=vM_RealAttrValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_RealAttrValuation", type=vM_Real_ATT_ID, multiplicity=Multiplicity(0, 1))
    }
)
refAtt111: BinaryAssociation = BinaryAssociation(
    name="refAtt111",
    ends={
        Property(name="vM_Integer_ATT_ID112", type=vM_IntegerAttrValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_IntegerAttrValuation", type=vM_Integer_ATT_ID, multiplicity=Multiplicity(0, 1))
    }
)
refAtt113: BinaryAssociation = BinaryAssociation(
    name="refAtt113",
    ends={
        Property(name="vM_Boolean_ATT_ID114", type=vM_BooleanAttrValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BooleanAttrValuation", type=vM_Boolean_ATT_ID, multiplicity=Multiplicity(0, 1))
    }
)
refAtt115: BinaryAssociation = BinaryAssociation(
    name="refAtt115",
    ends={
        Property(name="vM_String_ATT_ID116", type=vM_StringAttrValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_StringAttrValuation", type=vM_String_ATT_ID, multiplicity=Multiplicity(0, 1))
    }
)
attVsValForMultiFeature120: BinaryAssociation = BinaryAssociation(
    name="attVsValForMultiFeature120",
    ends={
        Property(name="vM_TableBasedValuationByFeatureAndClone", type=vM_AdvancedAttrValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_AdvancedAttrValuation121", type=vM_TableBasedValuationByFeatureAndClone, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refFeature122: BinaryAssociation = BinaryAssociation(
    name="refFeature122",
    ends={
        Property(name="vM_Feature124", type=vM_TableBasedValuationByFeatureAndClone, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_TableBasedValuationByFeatureAndClone123", type=vM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
pairs125: BinaryAssociation = BinaryAssociation(
    name="pairs125",
    ends={
        Property(name="vM_PairAttributeValue", type=vM_TableBasedValuationByFeatureAndClone, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_TableBasedValuationByFeatureAndClone126", type=vM_PairAttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refFeature127: BinaryAssociation = BinaryAssociation(
    name="refFeature127",
    ends={
        Property(name="vM_Feature129", type=vM_TableBasedValuationByFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_TableBasedValuationByFeature128", type=vM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
attVsVal117: BinaryAssociation = BinaryAssociation(
    name="attVsVal117",
    ends={
        Property(name="vM_TableBasedValuationByFeature", type=vM_AdvancedAttrValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_AdvancedAttrValuation", type=vM_TableBasedValuationByFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featVsVal118: BinaryAssociation = BinaryAssociation(
    name="featVsVal118",
    ends={
        Property(name="vM_TableBasedValuationByAttribute", type=vM_AdvancedAttrValuation, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_AdvancedAttrValuation119", type=vM_TableBasedValuationByAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refAtt136: BinaryAssociation = BinaryAssociation(
    name="refAtt136",
    ends={
        Property(name="vM_Integer_ATT_ID137", type=vM_TableBasedValuationByAttributeForInteger, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_TableBasedValuationByAttributeForInteger", type=vM_Integer_ATT_ID, multiplicity=Multiplicity(0, 1))
    }
)
pairs138: BinaryAssociation = BinaryAssociation(
    name="pairs138",
    ends={
        Property(name="vM_PairFeatureInteger", type=vM_TableBasedValuationByAttributeForInteger, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_TableBasedValuationByAttributeForInteger139", type=vM_PairFeatureInteger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refFeat140: BinaryAssociation = BinaryAssociation(
    name="refFeat140",
    ends={
        Property(name="vM_Feature142", type=vM_PairFeatureInteger, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_PairFeatureInteger141", type=vM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
pairs130: BinaryAssociation = BinaryAssociation(
    name="pairs130",
    ends={
        Property(name="vM_PairAttributeValue132", type=vM_TableBasedValuationByFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_TableBasedValuationByFeature131", type=vM_PairAttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refAtt133: BinaryAssociation = BinaryAssociation(
    name="refAtt133",
    ends={
        Property(name="vM_Abstract_ATT_ID135", type=vM_PairAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_PairAttributeValue134", type=vM_Abstract_ATT_ID, multiplicity=Multiplicity(0, 1))
    }
)
refFeat147: BinaryAssociation = BinaryAssociation(
    name="refFeat147",
    ends={
        Property(name="vM_PairFeatureReal148", type=vM_Feature, multiplicity=Multiplicity(0, 1)),
        Property(name="vM_Feature149", type=vM_PairFeatureReal, multiplicity=Multiplicity(1, 1))
    }
)
refAtt143: BinaryAssociation = BinaryAssociation(
    name="refAtt143",
    ends={
        Property(name="vM_Real_ATT_ID144", type=vM_TableBasedValuationByAttributeForReal, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_TableBasedValuationByAttributeForReal", type=vM_Real_ATT_ID, multiplicity=Multiplicity(0, 1))
    }
)
pairs145: BinaryAssociation = BinaryAssociation(
    name="pairs145",
    ends={
        Property(name="vM_PairFeatureReal", type=vM_TableBasedValuationByAttributeForReal, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_TableBasedValuationByAttributeForReal146", type=vM_PairFeatureReal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left156: BinaryAssociation = BinaryAssociation(
    name="left156",
    ends={
        Property(name="vM_ComplexExpression157", type=vM_If, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_If", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right158: BinaryAssociation = BinaryAssociation(
    name="right158",
    ends={
        Property(name="vM_ComplexExpression160", type=vM_If, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_If159", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left161: BinaryAssociation = BinaryAssociation(
    name="left161",
    ends={
        Property(name="vM_ComplexExpression162", type=vM_LeftImplication, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_LeftImplication", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right163: BinaryAssociation = BinaryAssociation(
    name="right163",
    ends={
        Property(name="vM_ComplexExpression165", type=vM_LeftImplication, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_LeftImplication164", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedFeature150: BinaryAssociation = BinaryAssociation(
    name="ownedFeature150",
    ends={
        Property(name="vM_Feature152", type=vM_AttHead, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_AttHead151", type=vM_Feature, multiplicity=Multiplicity(0, 1))
    }
)
head153: BinaryAssociation = BinaryAssociation(
    name="head153",
    ends={
        Property(name="vM_AttHead155", type=vM_Abstract_ATT_ID, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Abstract_ATT_ID154", type=vM_AttHead, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left171: BinaryAssociation = BinaryAssociation(
    name="left171",
    ends={
        Property(name="vM_ComplexExpression172", type=vM_BiImplication, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BiImplication", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right173: BinaryAssociation = BinaryAssociation(
    name="right173",
    ends={
        Property(name="vM_ComplexExpression175", type=vM_BiImplication, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_BiImplication174", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left176: BinaryAssociation = BinaryAssociation(
    name="left176",
    ends={
        Property(name="vM_ComplexExpression177", type=vM_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Or", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right178: BinaryAssociation = BinaryAssociation(
    name="right178",
    ends={
        Property(name="vM_ComplexExpression180", type=vM_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Or179", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left166: BinaryAssociation = BinaryAssociation(
    name="left166",
    ends={
        Property(name="vM_ComplexExpression167", type=vM_RightImplication, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_RightImplication", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right168: BinaryAssociation = BinaryAssociation(
    name="right168",
    ends={
        Property(name="vM_ComplexExpression170", type=vM_RightImplication, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_RightImplication169", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right183: BinaryAssociation = BinaryAssociation(
    name="right183",
    ends={
        Property(name="vM_ComplexExpression185", type=vM_And, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_And184", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left186: BinaryAssociation = BinaryAssociation(
    name="left186",
    ends={
        Property(name="vM_ComplexExpression187", type=vM_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Equality", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right188: BinaryAssociation = BinaryAssociation(
    name="right188",
    ends={
        Property(name="vM_ComplexExpression190", type=vM_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Equality189", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left191: BinaryAssociation = BinaryAssociation(
    name="left191",
    ends={
        Property(name="vM_ComplexExpression192", type=vM_Inequality, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Inequality", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right193: BinaryAssociation = BinaryAssociation(
    name="right193",
    ends={
        Property(name="vM_ComplexExpression195", type=vM_Inequality, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Inequality194", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left196: BinaryAssociation = BinaryAssociation(
    name="left196",
    ends={
        Property(name="vM_ComplexExpression197", type=vM_Less, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Less", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right198: BinaryAssociation = BinaryAssociation(
    name="right198",
    ends={
        Property(name="vM_ComplexExpression200", type=vM_Less, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Less199", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left201: BinaryAssociation = BinaryAssociation(
    name="left201",
    ends={
        Property(name="vM_Less202", type=vM_Lessequal, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Lessequal", type=vM_Less, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left181: BinaryAssociation = BinaryAssociation(
    name="left181",
    ends={
        Property(name="vM_ComplexExpression182", type=vM_And, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_And", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right213: BinaryAssociation = BinaryAssociation(
    name="right213",
    ends={
        Property(name="vM_ComplexExpression215", type=vM_Greaterequal, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Greaterequal214", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left216: BinaryAssociation = BinaryAssociation(
    name="left216",
    ends={
        Property(name="vM_ComplexExpression217", type=vM_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Plus", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right218: BinaryAssociation = BinaryAssociation(
    name="right218",
    ends={
        Property(name="vM_ComplexExpression220", type=vM_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Plus219", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left221: BinaryAssociation = BinaryAssociation(
    name="left221",
    ends={
        Property(name="vM_ComplexExpression222", type=vM_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Minus", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right223: BinaryAssociation = BinaryAssociation(
    name="right223",
    ends={
        Property(name="vM_ComplexExpression225", type=vM_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Minus224", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left226: BinaryAssociation = BinaryAssociation(
    name="left226",
    ends={
        Property(name="vM_ComplexExpression227", type=vM_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Multiplication", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right228: BinaryAssociation = BinaryAssociation(
    name="right228",
    ends={
        Property(name="vM_ComplexExpression230", type=vM_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Multiplication229", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left231: BinaryAssociation = BinaryAssociation(
    name="left231",
    ends={
        Property(name="vM_ComplexExpression232", type=vM_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Division", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right233: BinaryAssociation = BinaryAssociation(
    name="right233",
    ends={
        Property(name="vM_ComplexExpression235", type=vM_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Division234", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left236: BinaryAssociation = BinaryAssociation(
    name="left236",
    ends={
        Property(name="vM_ComplexExpression237", type=vM_Excludes, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Excludes", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right203: BinaryAssociation = BinaryAssociation(
    name="right203",
    ends={
        Property(name="vM_ComplexExpression205", type=vM_Lessequal, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Lessequal204", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left206: BinaryAssociation = BinaryAssociation(
    name="left206",
    ends={
        Property(name="vM_ComplexExpression207", type=vM_Greater, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Greater", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right208: BinaryAssociation = BinaryAssociation(
    name="right208",
    ends={
        Property(name="vM_ComplexExpression210", type=vM_Greater, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Greater209", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left211: BinaryAssociation = BinaryAssociation(
    name="left211",
    ends={
        Property(name="vM_Greater212", type=vM_Greaterequal, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Greaterequal", type=vM_Greater, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right238: BinaryAssociation = BinaryAssociation(
    name="right238",
    ends={
        Property(name="vM_Expression", type=vM_Excludes, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Excludes239", type=vM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left240: BinaryAssociation = BinaryAssociation(
    name="left240",
    ends={
        Property(name="vM_ComplexExpression241", type=vM_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Requires", type=vM_ComplexExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right242: BinaryAssociation = BinaryAssociation(
    name="right242",
    ends={
        Property(name="vM_Expression244", type=vM_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="vM_Requires243", type=vM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_vM_PackageDeclaration_VmBlock = Generalization(general=VmBlock, specific=vM_PackageDeclaration)
gen_vM_ImportDeclaration_VmBlock = Generalization(general=VmBlock, specific=vM_ImportDeclaration)
gen_vM_MetaDataDeclaration_VmBlock = Generalization(general=VmBlock, specific=vM_MetaDataDeclaration)
gen_vM_Relationships_VmBlock = Generalization(general=VmBlock, specific=vM_Relationships)
gen_vM_FeatureHierarchy_FeatureDefinition = Generalization(general=FeatureDefinition, specific=vM_FeatureHierarchy)
gen_vM_FeaturesGroup_FeatureDefinition = Generalization(general=FeatureDefinition, specific=vM_FeaturesGroup)
gen_vM_Xorgroup_FeaturesGroup = Generalization(general=FeaturesGroup, specific=vM_Xorgroup)
gen_vM_Orgroup_FeaturesGroup = Generalization(general=FeaturesGroup, specific=vM_Orgroup)
gen_vM_CardinalityBased_FeaturesGroup = Generalization(general=FeaturesGroup, specific=vM_CardinalityBased)
gen_vM_Attributes_VmBlock = Generalization(general=VmBlock, specific=vM_Attributes)
gen_vM_BooleanAttrDef_BasicAttrDef = Generalization(general=BasicAttrDef, specific=vM_BooleanAttrDef)
gen_vM_StringAttrDef_BasicAttrDef = Generalization(general=BasicAttrDef, specific=vM_StringAttrDef)
gen_vM_Feature_FeatureDefinition = Generalization(general=FeatureDefinition, specific=vM_Feature)
gen_vM_IntegerAttrDefBounded_IntegerAttrDef = Generalization(general=IntegerAttrDef, specific=vM_IntegerAttrDefBounded)
gen_vM_IntegerAttrDefUnbounded_IntegerAttrDef = Generalization(general=IntegerAttrDef, specific=vM_IntegerAttrDefUnbounded)
gen_vM_RealAttrDef_BasicAttrDef = Generalization(general=BasicAttrDef, specific=vM_RealAttrDef)
gen_vM_RealAttrDefBounded_RealAttrDef = Generalization(general=RealAttrDef, specific=vM_RealAttrDefBounded)
gen_vM_IntegerAttrDef_BasicAttrDef = Generalization(general=BasicAttrDef, specific=vM_IntegerAttrDef)
gen_vM_EnumStringDef_EnumAttrDef = Generalization(general=EnumAttrDef, specific=vM_EnumStringDef)
gen_vM_EnumIntegerDef_EnumAttrDef = Generalization(general=EnumAttrDef, specific=vM_EnumIntegerDef)
gen_vM_EnumRealDef_EnumAttrDef = Generalization(general=EnumAttrDef, specific=vM_EnumRealDef)
gen_vM_RealAttrDefUnbounded_RealAttrDef = Generalization(general=RealAttrDef, specific=vM_RealAttrDefUnbounded)
gen_vM_Descriptions_VmBlock = Generalization(general=VmBlock, specific=vM_Descriptions)
gen_vM_Constraints_VmBlock = Generalization(general=VmBlock, specific=vM_Constraints)
gen_vM_Expression_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Expression)
gen_vM_SpecialExpression_Expression = Generalization(general=Expression, specific=vM_SpecialExpression)
gen_vM_PrimitiveExpression_Expression = Generalization(general=Expression, specific=vM_PrimitiveExpression)
gen_vM_BooleanExpression_Expression = Generalization(general=Expression, specific=vM_BooleanExpression)
gen_vM_BrackedExpression_Expression = Generalization(general=Expression, specific=vM_BrackedExpression)
gen_vM_NumericExpression_Expression = Generalization(general=Expression, specific=vM_NumericExpression)
gen_vM_Objectives_VmBlock = Generalization(general=VmBlock, specific=vM_Objectives)
gen_vM_StringExpression_Expression = Generalization(general=Expression, specific=vM_StringExpression)
gen_vM_BasicAttrValuation_ExtendedValuation = Generalization(general=ExtendedValuation, specific=vM_BasicAttrValuation)
gen_vM_Configurations_VmBlock = Generalization(general=VmBlock, specific=vM_Configurations)
gen_vM_IntegerAttrValuation_BasicAttrValuation = Generalization(general=BasicAttrValuation, specific=vM_IntegerAttrValuation)
gen_vM_BooleanAttrValuation_BasicAttrValuation = Generalization(general=BasicAttrValuation, specific=vM_BooleanAttrValuation)
gen_vM_StringAttrValuation_BasicAttrValuation = Generalization(general=BasicAttrValuation, specific=vM_StringAttrValuation)
gen_vM_RealAttrValuation_BasicAttrValuation = Generalization(general=BasicAttrValuation, specific=vM_RealAttrValuation)
gen_vM_AdvancedAttrValuation_ExtendedValuation = Generalization(general=ExtendedValuation, specific=vM_AdvancedAttrValuation)
gen_vM_TableBasedValuationByAttributeForInteger_TableBasedValuationByAttribute = Generalization(general=TableBasedValuationByAttribute, specific=vM_TableBasedValuationByAttributeForInteger)
gen_vM_TableBasedValuationByAttributeForReal_TableBasedValuationByAttribute = Generalization(general=TableBasedValuationByAttribute, specific=vM_TableBasedValuationByAttributeForReal)
gen_vM_Boolean_ATT_ID_Abstract_ATT_ID = Generalization(general=Abstract_ATT_ID, specific=vM_Boolean_ATT_ID)
gen_vM_String_ATT_ID_Abstract_ATT_ID = Generalization(general=Abstract_ATT_ID, specific=vM_String_ATT_ID)
gen_vM_Integer_ATT_ID_Abstract_ATT_ID = Generalization(general=Abstract_ATT_ID, specific=vM_Integer_ATT_ID)
gen_vM_Real_ATT_ID_Abstract_ATT_ID = Generalization(general=Abstract_ATT_ID, specific=vM_Real_ATT_ID)
gen_vM_Enum_String_ATT_ID_Abstract_ATT_ID = Generalization(general=Abstract_ATT_ID, specific=vM_Enum_String_ATT_ID)
gen_vM_Enum_Integer_ATT_ID_Abstract_ATT_ID = Generalization(general=Abstract_ATT_ID, specific=vM_Enum_Integer_ATT_ID)
gen_vM_Enum_Real_ATT_ID_Abstract_ATT_ID = Generalization(general=Abstract_ATT_ID, specific=vM_Enum_Real_ATT_ID)
gen_vM_If_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_If)
gen_vM_LeftImplication_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_LeftImplication)
gen_vM_RightImplication_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_RightImplication)
gen_vM_BiImplication_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_BiImplication)
gen_vM_Or_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Or)
gen_vM_And_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_And)
gen_vM_Equality_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Equality)
gen_vM_Inequality_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Inequality)
gen_vM_Less_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Less)
gen_vM_Lessequal_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Lessequal)
gen_vM_Plus_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Plus)
gen_vM_Minus_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Minus)
gen_vM_Multiplication_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Multiplication)
gen_vM_Division_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Division)
gen_vM_Excludes_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Excludes)
gen_vM_Greater_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Greater)
gen_vM_Greaterequal_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Greaterequal)
gen_vM_Requires_ComplexExpression = Generalization(general=ComplexExpression, specific=vM_Requires)

# Domain Model
domain_model = DomainModel(
    name="vM",
    types={vM_PackageDeclaration, VmBlock, vM_ImportDeclaration, vM_MetaDataDeclaration, vM_Version, vM_Email, vM_Relationships, vM_FeatureHierarchy, FeatureDefinition, vM_Model, vM_VmBlock, vM_FeaturesGroup, vM_Xorgroup, FeaturesGroup, vM_Orgroup, vM_CardinalityBased, vM_Attributes, vM_AttrDef, vM_BasicAttrValuation, vM_BasicAttrDef, vM_EnumAttrDef, vM_BooleanAttrDef, BasicAttrDef, vM_Boolean_ATT_ID, vM_BoolDefaultDef, vM_StringAttrDef, vM_Feature, vM_String_ATT_ID, vM_FeatureDefinition, vM_StringDefaultDef, vM_IntegerAttrDefBounded, IntegerAttrDef, vM_IntegerAttrDefComplement, vM_IntegerDeltaDef, vM_IntegerAttrDefUnbounded, vM_RealAttrDef, vM_Real_ATT_ID, vM_RealDefaultDef, vM_RealAttrDefBounded, RealAttrDef, vM_RealAttrDefComplement, vM_RealDeltaDef, vM_IntegerAttrDef, vM_Integer_ATT_ID, vM_IntegerDefaultDef, EnumAttrDef, vM_Enum_String_ATT_ID, vM_EnumIntegerDef, vM_Enum_Integer_ATT_ID, vM_EnumRealDef, vM_Enum_Real_ATT_ID, vM_RealAttrDefUnbounded, vM_Descriptions, vM_EnumStringDef, vM_FeatureDescription, vM_AttributeDescription, vM_Abstract_ATT_ID, vM_Constraints, vM_Constraint, vM_ComplexExpression, vM_Expression, ComplexExpression, vM_SpecialExpression, Expression, vM_PrimitiveExpression, vM_AttHead, vM_BooleanExpression, vM_BooleanExpression_List, vM_BrackedExpression, vM_NumericExpression, vM_Objectives, vM_StringExpression, vM_Objective, vM_ObjectiveExpression, vM_NumericExpression_List, vM_BooleanValuation, vM_ExtendedValuation, ExtendedValuation, vM_Configurations, vM_Configuration, vM_IntegerAttrValuation, vM_BooleanAttrValuation, vM_StringAttrValuation, vM_AdvancedAttrValuation, vM_RealAttrValuation, vM_TableBasedValuationByFeatureAndClone, BasicAttrValuation, vM_PairAttributeValue, vM_TableBasedValuationByFeature, vM_TableBasedValuationByAttribute, vM_TableBasedValuationByAttributeForInteger, TableBasedValuationByAttribute, vM_PairFeatureInteger, vM_TableBasedValuationByAttributeForReal, Abstract_ATT_ID, vM_PairFeatureReal, vM_If, vM_LeftImplication, vM_RightImplication, vM_BiImplication, vM_Or, vM_And, vM_Equality, vM_Inequality, vM_Less, vM_Lessequal, vM_Plus, vM_Minus, vM_Multiplication, vM_Division, vM_Excludes, vM_Greater, vM_Greaterequal, vM_Requires},
    associations={blocks1, version3, email4, root6, blocks0, groupedFeatures11, attrDefs13, attrValuations14, basicAttrDef16, enumAttrDef18, name20, default21, parent7, name23, children9, complements29, complement30, delta33, name35, default36, complement38, delta39, default24, name26, default27, name41, default42, name45, default46, name49, default50, featuresDescriptions53, attributesDescriptions54, refFeat56, refFeat59, refAtt62, constraints64, expression65, featureID69, head71, refAtt73, expression77, expression_list78, expression80, ex89, expression67, objectives92, expression93, expression95, expression83, expression_list84, ex86, booleanValuation99, extendedValuation101, feature103, head106, configurations98, refAtt109, refAtt111, refAtt113, refAtt115, attVsValForMultiFeature120, refFeature122, pairs125, refFeature127, attVsVal117, featVsVal118, refAtt136, pairs138, refFeat140, pairs130, refAtt133, refFeat147, refAtt143, pairs145, left156, right158, left161, right163, ownedFeature150, head153, left171, right173, left176, right178, left166, right168, right183, left186, right188, left191, right193, left196, right198, left201, left181, right213, left216, right218, left221, right223, left226, right228, left231, right233, left236, right203, left206, right208, left211, right238, left240, right242},
    generalizations={gen_vM_PackageDeclaration_VmBlock, gen_vM_ImportDeclaration_VmBlock, gen_vM_MetaDataDeclaration_VmBlock, gen_vM_Relationships_VmBlock, gen_vM_FeatureHierarchy_FeatureDefinition, gen_vM_FeaturesGroup_FeatureDefinition, gen_vM_Xorgroup_FeaturesGroup, gen_vM_Orgroup_FeaturesGroup, gen_vM_CardinalityBased_FeaturesGroup, gen_vM_Attributes_VmBlock, gen_vM_BooleanAttrDef_BasicAttrDef, gen_vM_StringAttrDef_BasicAttrDef, gen_vM_Feature_FeatureDefinition, gen_vM_IntegerAttrDefBounded_IntegerAttrDef, gen_vM_IntegerAttrDefUnbounded_IntegerAttrDef, gen_vM_RealAttrDef_BasicAttrDef, gen_vM_RealAttrDefBounded_RealAttrDef, gen_vM_IntegerAttrDef_BasicAttrDef, gen_vM_EnumStringDef_EnumAttrDef, gen_vM_EnumIntegerDef_EnumAttrDef, gen_vM_EnumRealDef_EnumAttrDef, gen_vM_RealAttrDefUnbounded_RealAttrDef, gen_vM_Descriptions_VmBlock, gen_vM_Constraints_VmBlock, gen_vM_Expression_ComplexExpression, gen_vM_SpecialExpression_Expression, gen_vM_PrimitiveExpression_Expression, gen_vM_BooleanExpression_Expression, gen_vM_BrackedExpression_Expression, gen_vM_NumericExpression_Expression, gen_vM_Objectives_VmBlock, gen_vM_StringExpression_Expression, gen_vM_BasicAttrValuation_ExtendedValuation, gen_vM_Configurations_VmBlock, gen_vM_IntegerAttrValuation_BasicAttrValuation, gen_vM_BooleanAttrValuation_BasicAttrValuation, gen_vM_StringAttrValuation_BasicAttrValuation, gen_vM_RealAttrValuation_BasicAttrValuation, gen_vM_AdvancedAttrValuation_ExtendedValuation, gen_vM_TableBasedValuationByAttributeForInteger_TableBasedValuationByAttribute, gen_vM_TableBasedValuationByAttributeForReal_TableBasedValuationByAttribute, gen_vM_Boolean_ATT_ID_Abstract_ATT_ID, gen_vM_String_ATT_ID_Abstract_ATT_ID, gen_vM_Integer_ATT_ID_Abstract_ATT_ID, gen_vM_Real_ATT_ID_Abstract_ATT_ID, gen_vM_Enum_String_ATT_ID_Abstract_ATT_ID, gen_vM_Enum_Integer_ATT_ID_Abstract_ATT_ID, gen_vM_Enum_Real_ATT_ID_Abstract_ATT_ID, gen_vM_If_ComplexExpression, gen_vM_LeftImplication_ComplexExpression, gen_vM_RightImplication_ComplexExpression, gen_vM_BiImplication_ComplexExpression, gen_vM_Or_ComplexExpression, gen_vM_And_ComplexExpression, gen_vM_Equality_ComplexExpression, gen_vM_Inequality_ComplexExpression, gen_vM_Less_ComplexExpression, gen_vM_Lessequal_ComplexExpression, gen_vM_Plus_ComplexExpression, gen_vM_Minus_ComplexExpression, gen_vM_Multiplication_ComplexExpression, gen_vM_Division_ComplexExpression, gen_vM_Excludes_ComplexExpression, gen_vM_Greater_ComplexExpression, gen_vM_Greaterequal_ComplexExpression, gen_vM_Requires_ComplexExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)