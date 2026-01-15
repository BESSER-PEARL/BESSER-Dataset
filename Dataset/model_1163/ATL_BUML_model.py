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
ATL_LocatedElement = Class(name="ATL::LocatedElement", is_abstract=True)
ATL_Unit = Class(name="ATL::Unit")
LocatedElement = Class(name="LocatedElement")
ModuleElement = Class(name="ModuleElement")
ATL_ModuleElement = Class(name="ATL::ModuleElement", is_abstract=True)
Module = Class(name="Module")
ATL_Helper = Class(name="ATL::Helper")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
ATL_Rule = Class(name="ATL::Rule", is_abstract=True)
LibraryRef = Class(name="LibraryRef")
ATL_Library = Class(name="ATL::Library")
Unit = Class(name="Unit")
Helper = Class(name="Helper")
ATL_Query = Class(name="ATL::Query")
OclExpression = Class(name="OclExpression")
ATL_Module = Class(name="ATL::Module")
OclModel = Class(name="OclModel")
ATL_CalledRule = Class(name="ATL::CalledRule")
Parameter_ = Class(name="Parameter")
ATL_InPattern = Class(name="ATL::InPattern")
InPatternElement = Class(name="InPatternElement")
ATL_OutPattern = Class(name="ATL::OutPattern")
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
ATL_MatchedRule = Class(name="ATL::MatchedRule")
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
MatchedRule = Class(name="MatchedRule")
ATL_LazyMatchedRule = Class(name="ATL::LazyMatchedRule")
ATL_SimpleInPatternElement = Class(name="ATL::SimpleInPatternElement")
ATL_OutPatternElement = Class(name="ATL::OutPatternElement", is_abstract=True)
Binding = Class(name="Binding")
ATL_SimpleOutPatternElement = Class(name="ATL::SimpleOutPatternElement")
ATL_ForEachOutPatternElement = Class(name="ATL::ForEachOutPatternElement")
DropPattern = Class(name="DropPattern")
OutPatternElement = Class(name="OutPatternElement")
ATL_DropPattern = Class(name="ATL::DropPattern")
ATL_PatternElement = Class(name="ATL::PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
ATL_InPatternElement = Class(name="ATL::InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
ATL_ActionBlock = Class(name="ATL::ActionBlock")
Statement = Class(name="Statement")
ATL_Statement = Class(name="ATL::Statement", is_abstract=True)
ATL_ExpressionStat = Class(name="ATL::ExpressionStat")
ATL_BindingStat = Class(name="ATL::BindingStat")
Iterator = Class(name="Iterator")
ATL_Binding = Class(name="ATL::Binding")
ATL_RuleVariableDeclaration = Class(name="ATL::RuleVariableDeclaration")
ATL_LibraryRef = Class(name="ATL::LibraryRef")
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
ATL_IfStat = Class(name="ATL::IfStat")
ATL_ForStat = Class(name="ATL::ForStat")
OCL_OclExpression = Class(name="OCL::OclExpression", is_abstract=True)
OCL_BooleanExp = Class(name="OCL::BooleanExp")
OCL_NumericExp = Class(name="OCL::NumericExp", is_abstract=True)
OCL_RealExp = Class(name="OCL::RealExp")
NumericExp = Class(name="NumericExp")
OCL_IntegerExp = Class(name="OCL::IntegerExp")
OCL_CollectionExp = Class(name="OCL::CollectionExp", is_abstract=True)
OCL_BagExp = Class(name="OCL::BagExp")
OCL_OrderedSetExp = Class(name="OCL::OrderedSetExp")
OCL_SequenceExp = Class(name="OCL::SequenceExp")
OCL_SetExp = Class(name="OCL::SetExp")
OCL_TupleExp = Class(name="OCL::TupleExp")
TuplePart = Class(name="TuplePart")
Operation = Class(name="Operation")
OCL_TuplePart = Class(name="OCL::TuplePart")
TupleExp = Class(name="TupleExp")
Attribute = Class(name="Attribute")
OCL_MapExp = Class(name="OCL::MapExp")
MapElement = Class(name="MapElement")
OCL_VariableExp = Class(name="OCL::VariableExp")
OCL_MapElement = Class(name="OCL::MapElement")
MapExp = Class(name="MapExp")
OCL_SuperExp = Class(name="OCL::SuperExp")
OCL_PrimitiveExp = Class(name="OCL::PrimitiveExp", is_abstract=True)
OCL_StringExp = Class(name="OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
OCL_EnumLiteralExp = Class(name="OCL::EnumLiteralExp")
OCL_OclUndefinedExp = Class(name="OCL::OclUndefinedExp")
OCL_PropertyCallExp = Class(name="OCL::PropertyCallExp", is_abstract=True)
OCL_NavigationOrAttributeCallExp = Class(name="OCL::NavigationOrAttributeCallExp")
OCL_OperationCallExp = Class(name="OCL::OperationCallExp")
OCL_OperatorCallExp = Class(name="OCL::OperatorCallExp")
OCL_CollectionOperationCallExp = Class(name="OCL::CollectionOperationCallExp")
OCL_LoopExp = Class(name="OCL::LoopExp", is_abstract=True)
OCL_IterateExp = Class(name="OCL::IterateExp")
OCL_IteratorExp = Class(name="OCL::IteratorExp")
OCL_LetExp = Class(name="OCL::LetExp")
OCL_IfExp = Class(name="OCL::IfExp")
OCL_VariableDeclaration = Class(name="OCL::VariableDeclaration")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
OCL_Iterator = Class(name="OCL::Iterator")
OCL_Parameter = Class(name="OCL::Parameter")
OCL_CollectionType = Class(name="OCL::CollectionType")
OCL_OclType = Class(name="OCL::OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
OCL_Primitive = Class(name="OCL::Primitive", is_abstract=True)
OCL_StringType = Class(name="OCL::StringType")
Primitive = Class(name="Primitive")
OCL_BooleanType = Class(name="OCL::BooleanType")
OCL_NumericType = Class(name="OCL::NumericType", is_abstract=True)
OCL_IntegerType = Class(name="OCL::IntegerType")
NumericType = Class(name="NumericType")
OCL_RealType = Class(name="OCL::RealType")
OCL_BagType = Class(name="OCL::BagType")
OCL_OrderedSetType = Class(name="OCL::OrderedSetType")
OCL_SequenceType = Class(name="OCL::SequenceType")
OCL_SetType = Class(name="OCL::SetType")
OCL_OclAnyType = Class(name="OCL::OclAnyType")
OCL_TupleType = Class(name="OCL::TupleType")
OCL_TupleTypeAttribute = Class(name="OCL::TupleTypeAttribute")
TupleType = Class(name="TupleType")
OCL_OclModelElement = Class(name="OCL::OclModelElement")
OCL_MapType = Class(name="OCL::MapType")
OCL_OclFeatureDefinition = Class(name="OCL::OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
OCL_OclContextDefinition = Class(name="OCL::OclContextDefinition")
OCL_OclFeature = Class(name="OCL::OclFeature", is_abstract=True)
OCL_Attribute = Class(name="OCL::Attribute")
OCL_Operation = Class(name="OCL::Operation")
OCL_OclModel = Class(name="OCL::OclModel")
OclModelElement = Class(name="OclModelElement")

# ATL_LocatedElement class attributes and methods
ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
ATL_LocatedElement.attributes={ATL_LocatedElement_commentsAfter, ATL_LocatedElement_commentsBefore, ATL_LocatedElement_location}

# ATL_Unit class attributes and methods
ATL_Unit_name: Property = Property(name="name", type=StringType)
ATL_Unit.attributes={ATL_Unit_name}

# LocatedElement class attributes and methods

# ModuleElement class attributes and methods

# ATL_ModuleElement class attributes and methods

# Module class attributes and methods

# ATL_Helper class attributes and methods

# Query class attributes and methods

# Library class attributes and methods

# OclFeatureDefinition class attributes and methods

# ATL_Rule class attributes and methods
ATL_Rule_name: Property = Property(name="name", type=StringType)
ATL_Rule.attributes={ATL_Rule_name}

# LibraryRef class attributes and methods

# ATL_Library class attributes and methods

# Unit class attributes and methods

# Helper class attributes and methods

# ATL_Query class attributes and methods

# OclExpression class attributes and methods

# ATL_Module class attributes and methods
ATL_Module_isRefining: Property = Property(name="isRefining", type=StringType)
ATL_Module.attributes={ATL_Module_isRefining}

# OclModel class attributes and methods

# ATL_CalledRule class attributes and methods
ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
ATL_CalledRule.attributes={ATL_CalledRule_isEndpoint, ATL_CalledRule_isEntrypoint}

# Parameter class attributes and methods

# ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# ATL_OutPattern class attributes and methods

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# ATL_MatchedRule class attributes and methods
ATL_MatchedRule_isAbstract: Property = Property(name="isAbstract", type=StringType)
ATL_MatchedRule_isRefining: Property = Property(name="isRefining", type=StringType)
ATL_MatchedRule_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
ATL_MatchedRule.attributes={ATL_MatchedRule_isAbstract, ATL_MatchedRule_isNoDefault, ATL_MatchedRule_isRefining}

# Rule class attributes and methods

# InPattern class attributes and methods

# MatchedRule class attributes and methods

# ATL_LazyMatchedRule class attributes and methods
ATL_LazyMatchedRule_isUnique: Property = Property(name="isUnique", type=StringType)
ATL_LazyMatchedRule.attributes={ATL_LazyMatchedRule_isUnique}

# ATL_SimpleInPatternElement class attributes and methods

# ATL_OutPatternElement class attributes and methods

# Binding class attributes and methods

# ATL_SimpleOutPatternElement class attributes and methods

# ATL_ForEachOutPatternElement class attributes and methods

# DropPattern class attributes and methods

# OutPatternElement class attributes and methods

# ATL_DropPattern class attributes and methods

# ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# ATL_Statement class attributes and methods

# ATL_ExpressionStat class attributes and methods

# ATL_BindingStat class attributes and methods
ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
ATL_BindingStat.attributes={ATL_BindingStat_propertyName, ATL_BindingStat_isAssignment}

# Iterator class attributes and methods

# ATL_Binding class attributes and methods
ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
ATL_Binding.attributes={ATL_Binding_propertyName, ATL_Binding_isAssignment}

# ATL_RuleVariableDeclaration class attributes and methods

# ATL_LibraryRef class attributes and methods
ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
ATL_LibraryRef.attributes={ATL_LibraryRef_name}

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# ATL_IfStat class attributes and methods

# ATL_ForStat class attributes and methods

# OCL_OclExpression class attributes and methods

# OCL_BooleanExp class attributes and methods
OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
OCL_BooleanExp.attributes={OCL_BooleanExp_booleanSymbol}

# OCL_NumericExp class attributes and methods

# OCL_RealExp class attributes and methods
OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
OCL_RealExp.attributes={OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# OCL_IntegerExp class attributes and methods
OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
OCL_IntegerExp.attributes={OCL_IntegerExp_integerSymbol}

# OCL_CollectionExp class attributes and methods

# OCL_BagExp class attributes and methods

# OCL_OrderedSetExp class attributes and methods

# OCL_SequenceExp class attributes and methods

# OCL_SetExp class attributes and methods

# OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# Operation class attributes and methods

# OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# Attribute class attributes and methods

# OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# OCL_VariableExp class attributes and methods

# OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# OCL_SuperExp class attributes and methods

# OCL_PrimitiveExp class attributes and methods

# OCL_StringExp class attributes and methods
OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
OCL_StringExp.attributes={OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# OCL_EnumLiteralExp class attributes and methods
OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
OCL_EnumLiteralExp.attributes={OCL_EnumLiteralExp_name}

# OCL_OclUndefinedExp class attributes and methods

# OCL_PropertyCallExp class attributes and methods

# OCL_NavigationOrAttributeCallExp class attributes and methods
OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
OCL_NavigationOrAttributeCallExp.attributes={OCL_NavigationOrAttributeCallExp_name}

# OCL_OperationCallExp class attributes and methods
OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
OCL_OperationCallExp.attributes={OCL_OperationCallExp_operationName}

# OCL_OperatorCallExp class attributes and methods

# OCL_CollectionOperationCallExp class attributes and methods

# OCL_LoopExp class attributes and methods

# OCL_IterateExp class attributes and methods

# OCL_IteratorExp class attributes and methods
OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
OCL_IteratorExp.attributes={OCL_IteratorExp_name}

# OCL_LetExp class attributes and methods

# OCL_IfExp class attributes and methods

# OCL_VariableDeclaration class attributes and methods
OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
OCL_VariableDeclaration.attributes={OCL_VariableDeclaration_id, OCL_VariableDeclaration_varName}

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# OCL_Iterator class attributes and methods

# OCL_Parameter class attributes and methods

# OCL_CollectionType class attributes and methods

# OCL_OclType class attributes and methods
OCL_OclType_name: Property = Property(name="name", type=StringType)
OCL_OclType.attributes={OCL_OclType_name}

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# OCL_Primitive class attributes and methods

# OCL_StringType class attributes and methods

# Primitive class attributes and methods

# OCL_BooleanType class attributes and methods

# OCL_NumericType class attributes and methods

# OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# OCL_RealType class attributes and methods

# OCL_BagType class attributes and methods

# OCL_OrderedSetType class attributes and methods

# OCL_SequenceType class attributes and methods

# OCL_SetType class attributes and methods

# OCL_OclAnyType class attributes and methods

# OCL_TupleType class attributes and methods

# OCL_TupleTypeAttribute class attributes and methods
OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
OCL_TupleTypeAttribute.attributes={OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# OCL_OclModelElement class attributes and methods

# OCL_MapType class attributes and methods

# OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# OCL_OclContextDefinition class attributes and methods

# OCL_OclFeature class attributes and methods

# OCL_Attribute class attributes and methods
OCL_Attribute_name: Property = Property(name="name", type=StringType)
OCL_Attribute.attributes={OCL_Attribute_name}

# OCL_Operation class attributes and methods
OCL_Operation_name: Property = Property(name="name", type=StringType)
OCL_Operation.attributes={OCL_Operation_name}

# OCL_OclModel class attributes and methods
OCL_OclModel_name: Property = Property(name="name", type=StringType)
OCL_OclModel.attributes={OCL_OclModel_name}

# OclModelElement class attributes and methods

# Relationships
elements12: BinaryAssociation = BinaryAssociation(
    name="elements12",
    ends={
        Property(name="#14", type=ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="013", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module15: BinaryAssociation = BinaryAssociation(
    name="module15",
    ends={
        Property(name="#17", type=ATL_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="016", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
query18: BinaryAssociation = BinaryAssociation(
    name="query18",
    ends={
        Property(name="#20", type=ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="019", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
library21: BinaryAssociation = BinaryAssociation(
    name="library21",
    ends={
        Property(name="#23", type=ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="022", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
definition24: BinaryAssociation = BinaryAssociation(
    name="definition24",
    ends={
        Property(name="OclFeatureDefinition", type=ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
libraries0: BinaryAssociation = BinaryAssociation(
    name="libraries0",
    ends={
        Property(name="#", type=ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers1: BinaryAssociation = BinaryAssociation(
    name="helpers1",
    ends={
        Property(name="#3", type=ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Helper, multiplicity=Multiplicity(0, 9999))
    }
)
body4: BinaryAssociation = BinaryAssociation(
    name="body4",
    ends={
        Property(name="OclExpression", type=ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
helpers5: BinaryAssociation = BinaryAssociation(
    name="helpers5",
    ends={
        Property(name="#7", type=ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="06", type=Helper, multiplicity=Multiplicity(0, 9999))
    }
)
inModels8: BinaryAssociation = BinaryAssociation(
    name="inModels8",
    ends={
        Property(name="OclModel", type=ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outModels9: BinaryAssociation = BinaryAssociation(
    name="outModels9",
    ends={
        Property(name="OclModel11", type=ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Module10", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameters43: BinaryAssociation = BinaryAssociation(
    name="parameters43",
    ends={
        Property(name="Parameter", type=ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
elements44: BinaryAssociation = BinaryAssociation(
    name="elements44",
    ends={
        Property(name="#46", type=ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="045", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rule47: BinaryAssociation = BinaryAssociation(
    name="rule47",
    ends={
        Property(name="#49", type=ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="048", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
filter50: BinaryAssociation = BinaryAssociation(
    name="filter50",
    ends={
        Property(name="OclExpression51", type=ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outPattern25: BinaryAssociation = BinaryAssociation(
    name="outPattern25",
    ends={
        Property(name="#27", type=ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="026", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock28: BinaryAssociation = BinaryAssociation(
    name="actionBlock28",
    ends={
        Property(name="#30", type=ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="029", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables31: BinaryAssociation = BinaryAssociation(
    name="variables31",
    ends={
        Property(name="#33", type=ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="032", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern34: BinaryAssociation = BinaryAssociation(
    name="inPattern34",
    ends={
        Property(name="#36", type=ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="035", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children37: BinaryAssociation = BinaryAssociation(
    name="children37",
    ends={
        Property(name="#39", type=ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="038", type=MatchedRule, multiplicity=Multiplicity(0, 9999))
    }
)
superRule40: BinaryAssociation = BinaryAssociation(
    name="superRule40",
    ends={
        Property(name="#42", type=ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="041", type=MatchedRule, multiplicity=Multiplicity(0, 1))
    }
)
outPattern72: BinaryAssociation = BinaryAssociation(
    name="outPattern72",
    ends={
        Property(name="#74", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="073", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
sourceElement75: BinaryAssociation = BinaryAssociation(
    name="sourceElement75",
    ends={
        Property(name="#77", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="076", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings78: BinaryAssociation = BinaryAssociation(
    name="bindings78",
    ends={
        Property(name="#80", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="079", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model81: BinaryAssociation = BinaryAssociation(
    name="model81",
    ends={
        Property(name="OclModel82", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings83: BinaryAssociation = BinaryAssociation(
    name="reverseBindings83",
    ends={
        Property(name="OclExpression84", type=ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule52: BinaryAssociation = BinaryAssociation(
    name="rule52",
    ends={
        Property(name="#54", type=ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="053", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern55: BinaryAssociation = BinaryAssociation(
    name="dropPattern55",
    ends={
        Property(name="#57", type=ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="056", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements58: BinaryAssociation = BinaryAssociation(
    name="elements58",
    ends={
        Property(name="#60", type=ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="059", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern61: BinaryAssociation = BinaryAssociation(
    name="outPattern61",
    ends={
        Property(name="#63", type=ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="062", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
mapsTo64: BinaryAssociation = BinaryAssociation(
    name="mapsTo64",
    ends={
        Property(name="#66", type=ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="065", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
inPattern67: BinaryAssociation = BinaryAssociation(
    name="inPattern67",
    ends={
        Property(name="#69", type=ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="068", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models70: BinaryAssociation = BinaryAssociation(
    name="models70",
    ends={
        Property(name="OclModel71", type=ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
rule100: BinaryAssociation = BinaryAssociation(
    name="rule100",
    ends={
        Property(name="#102", type=ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="0101", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements103: BinaryAssociation = BinaryAssociation(
    name="statements103",
    ends={
        Property(name="Statement", type=ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression104: BinaryAssociation = BinaryAssociation(
    name="expression104",
    ends={
        Property(name="OclExpression105", type=ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source106: BinaryAssociation = BinaryAssociation(
    name="source106",
    ends={
        Property(name="OclExpression107", type=ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection85: BinaryAssociation = BinaryAssociation(
    name="collection85",
    ends={
        Property(name="OclExpression86", type=ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator87: BinaryAssociation = BinaryAssociation(
    name="iterator87",
    ends={
        Property(name="Iterator", type=ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForEachOutPatternElement88", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value89: BinaryAssociation = BinaryAssociation(
    name="value89",
    ends={
        Property(name="OclExpression90", type=ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement91: BinaryAssociation = BinaryAssociation(
    name="outPatternElement91",
    ends={
        Property(name="#93", type=ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="092", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
rule94: BinaryAssociation = BinaryAssociation(
    name="rule94",
    ends={
        Property(name="#96", type=ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="095", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
unit97: BinaryAssociation = BinaryAssociation(
    name="unit97",
    ends={
        Property(name="#99", type=ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="098", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
type127: BinaryAssociation = BinaryAssociation(
    name="type127",
    ends={
        Property(name="#128", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp3129: BinaryAssociation = BinaryAssociation(
    name="ifExp3129",
    ends={
        Property(name="#131", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1130", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty132: BinaryAssociation = BinaryAssociation(
    name="appliedProperty132",
    ends={
        Property(name="#134", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1133", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection135: BinaryAssociation = BinaryAssociation(
    name="collection135",
    ends={
        Property(name="#137", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1136", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp138: BinaryAssociation = BinaryAssociation(
    name="letExp138",
    ends={
        Property(name="#140", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1139", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp141: BinaryAssociation = BinaryAssociation(
    name="loopExp141",
    ends={
        Property(name="#143", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1142", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation144: BinaryAssociation = BinaryAssociation(
    name="parentOperation144",
    ends={
        Property(name="#146", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1145", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
value108: BinaryAssociation = BinaryAssociation(
    name="value108",
    ends={
        Property(name="OclExpression110", type=ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_BindingStat109", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition111: BinaryAssociation = BinaryAssociation(
    name="condition111",
    ends={
        Property(name="OclExpression112", type=ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements113: BinaryAssociation = BinaryAssociation(
    name="thenStatements113",
    ends={
        Property(name="Statement115", type=ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_IfStat114", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements116: BinaryAssociation = BinaryAssociation(
    name="elseStatements116",
    ends={
        Property(name="Statement118", type=ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_IfStat117", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator119: BinaryAssociation = BinaryAssociation(
    name="iterator119",
    ends={
        Property(name="Iterator120", type=ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection121: BinaryAssociation = BinaryAssociation(
    name="collection121",
    ends={
        Property(name="OclExpression123", type=ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForStat122", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements124: BinaryAssociation = BinaryAssociation(
    name="statements124",
    ends={
        Property(name="Statement126", type=ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForStat125", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements165: BinaryAssociation = BinaryAssociation(
    name="elements165",
    ends={
        Property(name="#167", type=OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1166", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializedVariable147: BinaryAssociation = BinaryAssociation(
    name="initializedVariable147",
    ends={
        Property(name="#149", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1148", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2150: BinaryAssociation = BinaryAssociation(
    name="ifExp2150",
    ends={
        Property(name="#152", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1151", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
tuplePart168: BinaryAssociation = BinaryAssociation(
    name="tuplePart168",
    ends={
        Property(name="#170", type=OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1169", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningOperation153: BinaryAssociation = BinaryAssociation(
    name="owningOperation153",
    ends={
        Property(name="#155", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1154", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1156: BinaryAssociation = BinaryAssociation(
    name="ifExp1156",
    ends={
        Property(name="#158", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1157", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
tuple171: BinaryAssociation = BinaryAssociation(
    name="tuple171",
    ends={
        Property(name="#173", type=OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="1172", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
owningAttribute159: BinaryAssociation = BinaryAssociation(
    name="owningAttribute159",
    ends={
        Property(name="#161", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1160", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
elements174: BinaryAssociation = BinaryAssociation(
    name="elements174",
    ends={
        Property(name="#176", type=OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1175", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredVariable162: BinaryAssociation = BinaryAssociation(
    name="referredVariable162",
    ends={
        Property(name="#164", type=OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1163", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
map177: BinaryAssociation = BinaryAssociation(
    name="map177",
    ends={
        Property(name="#179", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="1178", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key180: BinaryAssociation = BinaryAssociation(
    name="key180",
    ends={
        Property(name="OclExpression181", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source185: BinaryAssociation = BinaryAssociation(
    name="source185",
    ends={
        Property(name="#187", type=OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1186", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments188: BinaryAssociation = BinaryAssociation(
    name="arguments188",
    ends={
        Property(name="#190", type=OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1189", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body191: BinaryAssociation = BinaryAssociation(
    name="body191",
    ends={
        Property(name="#193", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1192", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators194: BinaryAssociation = BinaryAssociation(
    name="iterators194",
    ends={
        Property(name="#196", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1195", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result197: BinaryAssociation = BinaryAssociation(
    name="result197",
    ends={
        Property(name="#199", type=OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1198", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value182: BinaryAssociation = BinaryAssociation(
    name="value182",
    ends={
        Property(name="OclExpression184", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement183", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable200: BinaryAssociation = BinaryAssociation(
    name="variable200",
    ends={
        Property(name="#202", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1201", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_203: BinaryAssociation = BinaryAssociation(
    name="in_203",
    ends={
        Property(name="#205", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1204", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression206: BinaryAssociation = BinaryAssociation(
    name="thenExpression206",
    ends={
        Property(name="#208", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1207", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition209: BinaryAssociation = BinaryAssociation(
    name="condition209",
    ends={
        Property(name="#211", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1210", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression212: BinaryAssociation = BinaryAssociation(
    name="elseExpression212",
    ends={
        Property(name="#214", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1213", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type215: BinaryAssociation = BinaryAssociation(
    name="type215",
    ends={
        Property(name="#217", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1216", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression218: BinaryAssociation = BinaryAssociation(
    name="initExpression218",
    ends={
        Property(name="#220", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1219", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp221: BinaryAssociation = BinaryAssociation(
    name="letExp221",
    ends={
        Property(name="#223", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1222", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp224: BinaryAssociation = BinaryAssociation(
    name="baseExp224",
    ends={
        Property(name="#226", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1225", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp227: BinaryAssociation = BinaryAssociation(
    name="variableExp227",
    ends={
        Property(name="#229", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1228", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr230: BinaryAssociation = BinaryAssociation(
    name="loopExpr230",
    ends={
        Property(name="#232", type=OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="1231", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation233: BinaryAssociation = BinaryAssociation(
    name="operation233",
    ends={
        Property(name="#235", type=OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="1234", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType236: BinaryAssociation = BinaryAssociation(
    name="elementType236",
    ends={
        Property(name="#238", type=OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="1237", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions239: BinaryAssociation = BinaryAssociation(
    name="definitions239",
    ends={
        Property(name="#241", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1240", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression242: BinaryAssociation = BinaryAssociation(
    name="oclExpression242",
    ends={
        Property(name="#244", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1243", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation245: BinaryAssociation = BinaryAssociation(
    name="operation245",
    ends={
        Property(name="#247", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1246", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2248: BinaryAssociation = BinaryAssociation(
    name="mapType2248",
    ends={
        Property(name="#250", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1249", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute251: BinaryAssociation = BinaryAssociation(
    name="attribute251",
    ends={
        Property(name="#253", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1252", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType254: BinaryAssociation = BinaryAssociation(
    name="mapType254",
    ends={
        Property(name="#256", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1255", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes257: BinaryAssociation = BinaryAssociation(
    name="collectionTypes257",
    ends={
        Property(name="#259", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1258", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute260: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute260",
    ends={
        Property(name="#262", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1261", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration263: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration263",
    ends={
        Property(name="#265", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1264", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
attributes266: BinaryAssociation = BinaryAssociation(
    name="attributes266",
    ends={
        Property(name="#268", type=OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="1267", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type269: BinaryAssociation = BinaryAssociation(
    name="type269",
    ends={
        Property(name="#271", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1270", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType272: BinaryAssociation = BinaryAssociation(
    name="tupleType272",
    ends={
        Property(name="#274", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1273", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model275: BinaryAssociation = BinaryAssociation(
    name="model275",
    ends={
        Property(name="#277", type=OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="1276", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType278: BinaryAssociation = BinaryAssociation(
    name="valueType278",
    ends={
        Property(name="#280", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="1279", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType281: BinaryAssociation = BinaryAssociation(
    name="keyType281",
    ends={
        Property(name="#283", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="1282", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature284: BinaryAssociation = BinaryAssociation(
    name="feature284",
    ends={
        Property(name="#286", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1285", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_287: BinaryAssociation = BinaryAssociation(
    name="context_287",
    ends={
        Property(name="#289", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1288", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition290: BinaryAssociation = BinaryAssociation(
    name="definition290",
    ends={
        Property(name="#292", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1291", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_293: BinaryAssociation = BinaryAssociation(
    name="context_293",
    ends={
        Property(name="#295", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1294", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition296: BinaryAssociation = BinaryAssociation(
    name="definition296",
    ends={
        Property(name="#298", type=OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="1297", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression299: BinaryAssociation = BinaryAssociation(
    name="initExpression299",
    ends={
        Property(name="#301", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1300", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type302: BinaryAssociation = BinaryAssociation(
    name="type302",
    ends={
        Property(name="#304", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1303", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters305: BinaryAssociation = BinaryAssociation(
    name="parameters305",
    ends={
        Property(name="#307", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1306", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType308: BinaryAssociation = BinaryAssociation(
    name="returnType308",
    ends={
        Property(name="#310", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1309", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body311: BinaryAssociation = BinaryAssociation(
    name="body311",
    ends={
        Property(name="#313", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1312", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel314: BinaryAssociation = BinaryAssociation(
    name="metamodel314",
    ends={
        Property(name="#316", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1315", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements317: BinaryAssociation = BinaryAssociation(
    name="elements317",
    ends={
        Property(name="#319", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1318", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model320: BinaryAssociation = BinaryAssociation(
    name="model320",
    ends={
        Property(name="#322", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1321", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=ATL_Unit)
gen_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=ATL_ModuleElement)
gen_ATL_Helper_ModuleElement = Generalization(general=ModuleElement, specific=ATL_Helper)
gen_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=ATL_Rule)
gen_ATL_Library_Unit = Generalization(general=Unit, specific=ATL_Library)
gen_ATL_Query_Unit = Generalization(general=Unit, specific=ATL_Query)
gen_ATL_Module_Unit = Generalization(general=Unit, specific=ATL_Module)
gen_ATL_CalledRule_Rule = Generalization(general=Rule, specific=ATL_CalledRule)
gen_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=ATL_InPattern)
gen_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=ATL_OutPattern)
gen_ATL_MatchedRule_Rule = Generalization(general=Rule, specific=ATL_MatchedRule)
gen_ATL_LazyMatchedRule_MatchedRule = Generalization(general=MatchedRule, specific=ATL_LazyMatchedRule)
gen_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=ATL_SimpleInPatternElement)
gen_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=ATL_OutPatternElement)
gen_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=ATL_SimpleOutPatternElement)
gen_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=ATL_ForEachOutPatternElement)
gen_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=ATL_DropPattern)
gen_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=ATL_PatternElement)
gen_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=ATL_InPatternElement)
gen_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=ATL_ActionBlock)
gen_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=ATL_Statement)
gen_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=ATL_ExpressionStat)
gen_ATL_BindingStat_Statement = Generalization(general=Statement, specific=ATL_BindingStat)
gen_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=ATL_Binding)
gen_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=ATL_RuleVariableDeclaration)
gen_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=ATL_LibraryRef)
gen_ATL_IfStat_Statement = Generalization(general=Statement, specific=ATL_IfStat)
gen_ATL_ForStat_Statement = Generalization(general=Statement, specific=ATL_ForStat)
gen_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclExpression)
gen_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_BooleanExp)
gen_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_NumericExp)
gen_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=OCL_RealExp)
gen_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=OCL_IntegerExp)
gen_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=OCL_CollectionExp)
gen_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_BagExp)
gen_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_OrderedSetExp)
gen_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_SequenceExp)
gen_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_SetExp)
gen_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=OCL_TupleExp)
gen_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_TuplePart)
gen_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=OCL_MapExp)
gen_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=OCL_VariableExp)
gen_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=OCL_MapElement)
gen_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=OCL_SuperExp)
gen_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PrimitiveExp)
gen_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_StringExp)
gen_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=OCL_EnumLiteralExp)
gen_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=OCL_OclUndefinedExp)
gen_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PropertyCallExp)
gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_NavigationOrAttributeCallExp)
gen_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_OperationCallExp)
gen_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_OperatorCallExp)
gen_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_CollectionOperationCallExp)
gen_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_LoopExp)
gen_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IterateExp)
gen_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IteratorExp)
gen_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=OCL_LetExp)
gen_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=OCL_IfExp)
gen_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=OCL_VariableDeclaration)
gen_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Iterator)
gen_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Parameter)
gen_OCL_CollectionType_OclType = Generalization(general=OclType, specific=OCL_CollectionType)
gen_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=OCL_OclType)
gen_OCL_Primitive_OclType = Generalization(general=OclType, specific=OCL_Primitive)
gen_OCL_StringType_Primitive = Generalization(general=Primitive, specific=OCL_StringType)
gen_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=OCL_BooleanType)
gen_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=OCL_NumericType)
gen_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=OCL_IntegerType)
gen_OCL_RealType_NumericType = Generalization(general=NumericType, specific=OCL_RealType)
gen_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=OCL_BagType)
gen_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=OCL_OrderedSetType)
gen_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=OCL_SequenceType)
gen_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=OCL_SetType)
gen_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=OCL_OclAnyType)
gen_OCL_TupleType_OclType = Generalization(general=OclType, specific=OCL_TupleType)
gen_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=OCL_TupleTypeAttribute)
gen_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=OCL_OclModelElement)
gen_OCL_MapType_OclType = Generalization(general=OclType, specific=OCL_MapType)
gen_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeatureDefinition)
gen_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclContextDefinition)
gen_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeature)
gen_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=OCL_Attribute)
gen_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=OCL_Operation)
gen_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclModel)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={ATL_LocatedElement, ATL_Unit, LocatedElement, ModuleElement, ATL_ModuleElement, Module, ATL_Helper, Query, Library, OclFeatureDefinition, ATL_Rule, LibraryRef, ATL_Library, Unit, Helper, ATL_Query, OclExpression, ATL_Module, OclModel, ATL_CalledRule, Parameter_, ATL_InPattern, InPatternElement, ATL_OutPattern, OutPattern, ActionBlock, RuleVariableDeclaration, ATL_MatchedRule, Rule, InPattern, MatchedRule, ATL_LazyMatchedRule, ATL_SimpleInPatternElement, ATL_OutPatternElement, Binding, ATL_SimpleOutPatternElement, ATL_ForEachOutPatternElement, DropPattern, OutPatternElement, ATL_DropPattern, ATL_PatternElement, VariableDeclaration, ATL_InPatternElement, PatternElement, ATL_ActionBlock, Statement, ATL_Statement, ATL_ExpressionStat, ATL_BindingStat, Iterator, ATL_Binding, ATL_RuleVariableDeclaration, ATL_LibraryRef, OclType, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, ATL_IfStat, ATL_ForStat, OCL_OclExpression, OCL_BooleanExp, OCL_NumericExp, OCL_RealExp, NumericExp, OCL_IntegerExp, OCL_CollectionExp, OCL_BagExp, OCL_OrderedSetExp, OCL_SequenceExp, OCL_SetExp, OCL_TupleExp, TuplePart, Operation, OCL_TuplePart, TupleExp, Attribute, OCL_MapExp, MapElement, OCL_VariableExp, OCL_MapElement, MapExp, OCL_SuperExp, OCL_PrimitiveExp, OCL_StringExp, PrimitiveExp, OCL_EnumLiteralExp, OCL_OclUndefinedExp, OCL_PropertyCallExp, OCL_NavigationOrAttributeCallExp, OCL_OperationCallExp, OCL_OperatorCallExp, OCL_CollectionOperationCallExp, OCL_LoopExp, OCL_IterateExp, OCL_IteratorExp, OCL_LetExp, OCL_IfExp, OCL_VariableDeclaration, IterateExp, VariableExp, OCL_Iterator, OCL_Parameter, OCL_CollectionType, OCL_OclType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, OCL_Primitive, OCL_StringType, Primitive, OCL_BooleanType, OCL_NumericType, OCL_IntegerType, NumericType, OCL_RealType, OCL_BagType, OCL_OrderedSetType, OCL_SequenceType, OCL_SetType, OCL_OclAnyType, OCL_TupleType, OCL_TupleTypeAttribute, TupleType, OCL_OclModelElement, OCL_MapType, OCL_OclFeatureDefinition, OclFeature, OCL_OclContextDefinition, OCL_OclFeature, OCL_Attribute, OCL_Operation, OCL_OclModel, OclModelElement},
    associations={elements12, module15, query18, library21, definition24, libraries0, helpers1, body4, helpers5, inModels8, outModels9, parameters43, elements44, rule47, filter50, outPattern25, actionBlock28, variables31, inPattern34, children37, superRule40, outPattern72, sourceElement75, bindings78, model81, reverseBindings83, rule52, dropPattern55, elements58, outPattern61, mapsTo64, inPattern67, models70, rule100, statements103, expression104, source106, collection85, iterator87, value89, outPatternElement91, rule94, unit97, type127, ifExp3129, appliedProperty132, collection135, letExp138, loopExp141, parentOperation144, value108, condition111, thenStatements113, elseStatements116, iterator119, collection121, statements124, elements165, initializedVariable147, ifExp2150, tuplePart168, owningOperation153, ifExp1156, tuple171, owningAttribute159, elements174, referredVariable162, map177, key180, source185, arguments188, body191, iterators194, result197, value182, variable200, in_203, thenExpression206, condition209, elseExpression212, type215, initExpression218, letExp221, baseExp224, variableExp227, loopExpr230, operation233, elementType236, definitions239, oclExpression242, operation245, mapType2248, attribute251, mapType254, collectionTypes257, tupleTypeAttribute260, variableDeclaration263, attributes266, type269, tupleType272, model275, valueType278, keyType281, feature284, context_287, definition290, context_293, definition296, initExpression299, type302, parameters305, returnType308, body311, metamodel314, elements317, model320},
    generalizations={gen_ATL_Unit_LocatedElement, gen_ATL_ModuleElement_LocatedElement, gen_ATL_Helper_ModuleElement, gen_ATL_Rule_ModuleElement, gen_ATL_Library_Unit, gen_ATL_Query_Unit, gen_ATL_Module_Unit, gen_ATL_CalledRule_Rule, gen_ATL_InPattern_LocatedElement, gen_ATL_OutPattern_LocatedElement, gen_ATL_MatchedRule_Rule, gen_ATL_LazyMatchedRule_MatchedRule, gen_ATL_SimpleInPatternElement_InPatternElement, gen_ATL_OutPatternElement_PatternElement, gen_ATL_SimpleOutPatternElement_OutPatternElement, gen_ATL_ForEachOutPatternElement_OutPatternElement, gen_ATL_DropPattern_LocatedElement, gen_ATL_PatternElement_VariableDeclaration, gen_ATL_InPatternElement_PatternElement, gen_ATL_ActionBlock_LocatedElement, gen_ATL_Statement_LocatedElement, gen_ATL_ExpressionStat_Statement, gen_ATL_BindingStat_Statement, gen_ATL_Binding_LocatedElement, gen_ATL_RuleVariableDeclaration_VariableDeclaration, gen_ATL_LibraryRef_LocatedElement, gen_ATL_IfStat_Statement, gen_ATL_ForStat_Statement, gen_OCL_OclExpression_LocatedElement, gen_OCL_BooleanExp_PrimitiveExp, gen_OCL_NumericExp_PrimitiveExp, gen_OCL_RealExp_NumericExp, gen_OCL_IntegerExp_NumericExp, gen_OCL_CollectionExp_OclExpression, gen_OCL_BagExp_CollectionExp, gen_OCL_OrderedSetExp_CollectionExp, gen_OCL_SequenceExp_CollectionExp, gen_OCL_SetExp_CollectionExp, gen_OCL_TupleExp_OclExpression, gen_OCL_TuplePart_VariableDeclaration, gen_OCL_MapExp_OclExpression, gen_OCL_VariableExp_OclExpression, gen_OCL_MapElement_LocatedElement, gen_OCL_SuperExp_OclExpression, gen_OCL_PrimitiveExp_OclExpression, gen_OCL_StringExp_PrimitiveExp, gen_OCL_EnumLiteralExp_OclExpression, gen_OCL_OclUndefinedExp_OclExpression, gen_OCL_PropertyCallExp_OclExpression, gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_OCL_OperationCallExp_PropertyCallExp, gen_OCL_OperatorCallExp_OperationCallExp, gen_OCL_CollectionOperationCallExp_OperationCallExp, gen_OCL_LoopExp_PropertyCallExp, gen_OCL_IterateExp_LoopExp, gen_OCL_IteratorExp_LoopExp, gen_OCL_LetExp_OclExpression, gen_OCL_IfExp_OclExpression, gen_OCL_VariableDeclaration_LocatedElement, gen_OCL_Iterator_VariableDeclaration, gen_OCL_Parameter_VariableDeclaration, gen_OCL_CollectionType_OclType, gen_OCL_OclType_OclExpression, gen_OCL_Primitive_OclType, gen_OCL_StringType_Primitive, gen_OCL_BooleanType_Primitive, gen_OCL_NumericType_Primitive, gen_OCL_IntegerType_NumericType, gen_OCL_RealType_NumericType, gen_OCL_BagType_CollectionType, gen_OCL_OrderedSetType_CollectionType, gen_OCL_SequenceType_CollectionType, gen_OCL_SetType_CollectionType, gen_OCL_OclAnyType_OclType, gen_OCL_TupleType_OclType, gen_OCL_TupleTypeAttribute_LocatedElement, gen_OCL_OclModelElement_OclType, gen_OCL_MapType_OclType, gen_OCL_OclFeatureDefinition_LocatedElement, gen_OCL_OclContextDefinition_LocatedElement, gen_OCL_OclFeature_LocatedElement, gen_OCL_Attribute_OclFeature, gen_OCL_Operation_OclFeature, gen_OCL_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)