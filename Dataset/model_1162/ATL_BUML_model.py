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
LibraryRef = Class(name="LibraryRef")
ATL_Library = Class(name="ATL::Library")
Unit = Class(name="Unit")
Helper = Class(name="Helper")
ATL_Query = Class(name="ATL::Query")
OclExpression = Class(name="OclExpression")
ATL_Module = Class(name="ATL::Module")
OclModel = Class(name="OclModel")
ModuleElement = Class(name="ModuleElement")
ATL_ModuleElement = Class(name="ATL::ModuleElement", is_abstract=True)
Module = Class(name="Module")
ATL_Helper = Class(name="ATL::Helper")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
ATL_Rule = Class(name="ATL::Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
ATL_MatchedRule = Class(name="ATL::MatchedRule")
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
MatchedRule = Class(name="MatchedRule")
ATL_LazyMatchedRule = Class(name="ATL::LazyMatchedRule")
ATL_CalledRule = Class(name="ATL::CalledRule")
Parameter_ = Class(name="Parameter")
ATL_InPattern = Class(name="ATL::InPattern")
InPatternElement = Class(name="InPatternElement")
ATL_OutPattern = Class(name="ATL::OutPattern")
OutPatternElement = Class(name="OutPatternElement")
ATL_PatternElement = Class(name="ATL::PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
ATL_InPatternElement = Class(name="ATL::InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
ATL_SimpleInPatternElement = Class(name="ATL::SimpleInPatternElement")
ATL_OutPatternElement = Class(name="ATL::OutPatternElement", is_abstract=True)
Binding = Class(name="Binding")
ATL_SimpleOutPatternElement = Class(name="ATL::SimpleOutPatternElement")
ATL_ForEachOutPatternElement = Class(name="ATL::ForEachOutPatternElement")
Iterator = Class(name="Iterator")
ATL_Binding = Class(name="ATL::Binding")
ATL_RuleVariableDeclaration = Class(name="ATL::RuleVariableDeclaration")
ATL_LibraryRef = Class(name="ATL::LibraryRef")
ATL_ActionBlock = Class(name="ATL::ActionBlock")
Statement = Class(name="Statement")
ATL_Statement = Class(name="ATL::Statement", is_abstract=True)
ATL_ExpressionStat = Class(name="ATL::ExpressionStat")
ATL_BindingStat = Class(name="ATL::BindingStat")
ATL_IfStat = Class(name="ATL::IfStat")
ATL_ForStat = Class(name="ATL::ForStat")
OCL_OclExpression = Class(name="OCL::OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
OCL_VariableExp = Class(name="OCL::VariableExp")
OCL_SuperExp = Class(name="OCL::SuperExp")
OCL_PrimitiveExp = Class(name="OCL::PrimitiveExp", is_abstract=True)
OCL_StringExp = Class(name="OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
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
OCL_TuplePart = Class(name="OCL::TuplePart")
TupleExp = Class(name="TupleExp")
OCL_MapExp = Class(name="OCL::MapExp")
MapElement = Class(name="MapElement")
OCL_MapElement = Class(name="OCL::MapElement")
MapExp = Class(name="MapExp")
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
OclContextDefinition = Class(name="OclContextDefinition")
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
OCL_SetType = Class(name="OCL::SetType")
OCL_Attribute = Class(name="OCL::Attribute")
OCL_Operation = Class(name="OCL::Operation")
OCL_OclModel = Class(name="OCL::OclModel")
OclModelElement = Class(name="OclModelElement")

# ATL_LocatedElement class attributes and methods
ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
ATL_LocatedElement.attributes={ATL_LocatedElement_commentsBefore, ATL_LocatedElement_location, ATL_LocatedElement_commentsAfter}

# ATL_Unit class attributes and methods
ATL_Unit_name: Property = Property(name="name", type=StringType)
ATL_Unit.attributes={ATL_Unit_name}

# LocatedElement class attributes and methods

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

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# ATL_MatchedRule class attributes and methods
ATL_MatchedRule_isRefining: Property = Property(name="isRefining", type=StringType)
ATL_MatchedRule_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
ATL_MatchedRule_isAbstract: Property = Property(name="isAbstract", type=StringType)
ATL_MatchedRule.attributes={ATL_MatchedRule_isRefining, ATL_MatchedRule_isAbstract, ATL_MatchedRule_isNoDefault}

# Rule class attributes and methods

# InPattern class attributes and methods

# MatchedRule class attributes and methods

# ATL_LazyMatchedRule class attributes and methods
ATL_LazyMatchedRule_isUnique: Property = Property(name="isUnique", type=StringType)
ATL_LazyMatchedRule.attributes={ATL_LazyMatchedRule_isUnique}

# ATL_CalledRule class attributes and methods
ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
ATL_CalledRule.attributes={ATL_CalledRule_isEntrypoint, ATL_CalledRule_isEndpoint}

# Parameter class attributes and methods

# ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# ATL_OutPattern class attributes and methods

# OutPatternElement class attributes and methods

# ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# ATL_SimpleInPatternElement class attributes and methods

# ATL_OutPatternElement class attributes and methods

# Binding class attributes and methods

# ATL_SimpleOutPatternElement class attributes and methods

# ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# ATL_Binding class attributes and methods
ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
ATL_Binding.attributes={ATL_Binding_propertyName, ATL_Binding_isAssignment}

# ATL_RuleVariableDeclaration class attributes and methods

# ATL_LibraryRef class attributes and methods
ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
ATL_LibraryRef.attributes={ATL_LibraryRef_name}

# ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# ATL_Statement class attributes and methods

# ATL_ExpressionStat class attributes and methods

# ATL_BindingStat class attributes and methods
ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
ATL_BindingStat.attributes={ATL_BindingStat_isAssignment, ATL_BindingStat_propertyName}

# ATL_IfStat class attributes and methods

# ATL_ForStat class attributes and methods

# OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# OCL_VariableExp class attributes and methods

# OCL_SuperExp class attributes and methods

# OCL_PrimitiveExp class attributes and methods

# OCL_StringExp class attributes and methods
OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
OCL_StringExp.attributes={OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

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

# OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# OCL_MapElement class attributes and methods

# MapExp class attributes and methods

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
OCL_VariableDeclaration.attributes={OCL_VariableDeclaration_varName, OCL_VariableDeclaration_id}

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# OCL_Iterator class attributes and methods

# OCL_Parameter class attributes and methods

# OCL_CollectionType class attributes and methods

# OCL_OclType class attributes and methods
OCL_OclType_name: Property = Property(name="name", type=StringType)
OCL_OclType.attributes={OCL_OclType_name}

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

# OclContextDefinition class attributes and methods

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

# OCL_SetType class attributes and methods

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
        Property(name="Helper", type=ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Library", type=Helper, multiplicity=Multiplicity(0, 9999))
    }
)
body2: BinaryAssociation = BinaryAssociation(
    name="body2",
    ends={
        Property(name="OclExpression", type=ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inModels6: BinaryAssociation = BinaryAssociation(
    name="inModels6",
    ends={
        Property(name="OclModel", type=ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outModels7: BinaryAssociation = BinaryAssociation(
    name="outModels7",
    ends={
        Property(name="OclModel9", type=ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Module8", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements10: BinaryAssociation = BinaryAssociation(
    name="elements10",
    ends={
        Property(name="#12", type=ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="011", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module13: BinaryAssociation = BinaryAssociation(
    name="module13",
    ends={
        Property(name="#15", type=ATL_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="014", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
query16: BinaryAssociation = BinaryAssociation(
    name="query16",
    ends={
        Property(name="#18", type=ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="017", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
library19: BinaryAssociation = BinaryAssociation(
    name="library19",
    ends={
        Property(name="Library", type=ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Helper", type=Library, multiplicity=Multiplicity(1, 1))
    }
)
definition20: BinaryAssociation = BinaryAssociation(
    name="definition20",
    ends={
        Property(name="OclFeatureDefinition", type=ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Helper21", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPattern22: BinaryAssociation = BinaryAssociation(
    name="outPattern22",
    ends={
        Property(name="#24", type=ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="023", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock25: BinaryAssociation = BinaryAssociation(
    name="actionBlock25",
    ends={
        Property(name="#27", type=ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="026", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables28: BinaryAssociation = BinaryAssociation(
    name="variables28",
    ends={
        Property(name="#30", type=ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="029", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern31: BinaryAssociation = BinaryAssociation(
    name="inPattern31",
    ends={
        Property(name="#33", type=ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="032", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children34: BinaryAssociation = BinaryAssociation(
    name="children34",
    ends={
        Property(name="#36", type=ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="035", type=MatchedRule, multiplicity=Multiplicity(0, 9999))
    }
)
superRule37: BinaryAssociation = BinaryAssociation(
    name="superRule37",
    ends={
        Property(name="#39", type=ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="038", type=MatchedRule, multiplicity=Multiplicity(0, 1))
    }
)
helpers3: BinaryAssociation = BinaryAssociation(
    name="helpers3",
    ends={
        Property(name="#5", type=ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="04", type=Helper, multiplicity=Multiplicity(0, 9999))
    }
)
parameters40: BinaryAssociation = BinaryAssociation(
    name="parameters40",
    ends={
        Property(name="Parameter", type=ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
elements41: BinaryAssociation = BinaryAssociation(
    name="elements41",
    ends={
        Property(name="#43", type=ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="042", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rule44: BinaryAssociation = BinaryAssociation(
    name="rule44",
    ends={
        Property(name="#46", type=ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="045", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
filter47: BinaryAssociation = BinaryAssociation(
    name="filter47",
    ends={
        Property(name="OclExpression48", type=ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule49: BinaryAssociation = BinaryAssociation(
    name="rule49",
    ends={
        Property(name="#51", type=ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="050", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
elements52: BinaryAssociation = BinaryAssociation(
    name="elements52",
    ends={
        Property(name="#54", type=ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="053", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
mapsTo55: BinaryAssociation = BinaryAssociation(
    name="mapsTo55",
    ends={
        Property(name="#57", type=ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="056", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
inPattern58: BinaryAssociation = BinaryAssociation(
    name="inPattern58",
    ends={
        Property(name="#60", type=ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="059", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models61: BinaryAssociation = BinaryAssociation(
    name="models61",
    ends={
        Property(name="OclModel62", type=ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern63: BinaryAssociation = BinaryAssociation(
    name="outPattern63",
    ends={
        Property(name="#65", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="064", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
bindings69: BinaryAssociation = BinaryAssociation(
    name="bindings69",
    ends={
        Property(name="#71", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="070", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model72: BinaryAssociation = BinaryAssociation(
    name="model72",
    ends={
        Property(name="OclModel73", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings74: BinaryAssociation = BinaryAssociation(
    name="reverseBindings74",
    ends={
        Property(name="OclExpression75", type=ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection76: BinaryAssociation = BinaryAssociation(
    name="collection76",
    ends={
        Property(name="OclExpression77", type=ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator78: BinaryAssociation = BinaryAssociation(
    name="iterator78",
    ends={
        Property(name="Iterator", type=ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForEachOutPatternElement79", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value80: BinaryAssociation = BinaryAssociation(
    name="value80",
    ends={
        Property(name="OclExpression81", type=ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement82: BinaryAssociation = BinaryAssociation(
    name="outPatternElement82",
    ends={
        Property(name="#84", type=ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="083", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
rule85: BinaryAssociation = BinaryAssociation(
    name="rule85",
    ends={
        Property(name="#87", type=ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="086", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
unit88: BinaryAssociation = BinaryAssociation(
    name="unit88",
    ends={
        Property(name="#90", type=ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="089", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
rule91: BinaryAssociation = BinaryAssociation(
    name="rule91",
    ends={
        Property(name="#93", type=ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="092", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
sourceElement66: BinaryAssociation = BinaryAssociation(
    name="sourceElement66",
    ends={
        Property(name="#68", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="067", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
expression95: BinaryAssociation = BinaryAssociation(
    name="expression95",
    ends={
        Property(name="OclExpression96", type=ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source97: BinaryAssociation = BinaryAssociation(
    name="source97",
    ends={
        Property(name="OclExpression98", type=ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value99: BinaryAssociation = BinaryAssociation(
    name="value99",
    ends={
        Property(name="OclExpression101", type=ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_BindingStat100", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition102: BinaryAssociation = BinaryAssociation(
    name="condition102",
    ends={
        Property(name="OclExpression103", type=ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements104: BinaryAssociation = BinaryAssociation(
    name="thenStatements104",
    ends={
        Property(name="Statement106", type=ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_IfStat105", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements107: BinaryAssociation = BinaryAssociation(
    name="elseStatements107",
    ends={
        Property(name="Statement109", type=ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_IfStat108", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator110: BinaryAssociation = BinaryAssociation(
    name="iterator110",
    ends={
        Property(name="Iterator111", type=ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection112: BinaryAssociation = BinaryAssociation(
    name="collection112",
    ends={
        Property(name="OclExpression114", type=ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForStat113", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements115: BinaryAssociation = BinaryAssociation(
    name="statements115",
    ends={
        Property(name="Statement117", type=ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForStat116", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type118: BinaryAssociation = BinaryAssociation(
    name="type118",
    ends={
        Property(name="#119", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp3120: BinaryAssociation = BinaryAssociation(
    name="ifExp3120",
    ends={
        Property(name="#122", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1121", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
statements94: BinaryAssociation = BinaryAssociation(
    name="statements94",
    ends={
        Property(name="Statement", type=ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection126: BinaryAssociation = BinaryAssociation(
    name="collection126",
    ends={
        Property(name="#128", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1127", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp129: BinaryAssociation = BinaryAssociation(
    name="letExp129",
    ends={
        Property(name="#131", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1130", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp132: BinaryAssociation = BinaryAssociation(
    name="loopExp132",
    ends={
        Property(name="#134", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1133", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation135: BinaryAssociation = BinaryAssociation(
    name="parentOperation135",
    ends={
        Property(name="#137", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1136", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable138: BinaryAssociation = BinaryAssociation(
    name="initializedVariable138",
    ends={
        Property(name="#140", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1139", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2141: BinaryAssociation = BinaryAssociation(
    name="ifExp2141",
    ends={
        Property(name="#143", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1142", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation144: BinaryAssociation = BinaryAssociation(
    name="owningOperation144",
    ends={
        Property(name="#146", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1145", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1147: BinaryAssociation = BinaryAssociation(
    name="ifExp1147",
    ends={
        Property(name="#149", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1148", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute150: BinaryAssociation = BinaryAssociation(
    name="owningAttribute150",
    ends={
        Property(name="#152", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1151", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable153: BinaryAssociation = BinaryAssociation(
    name="referredVariable153",
    ends={
        Property(name="#155", type=OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1154", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
appliedProperty123: BinaryAssociation = BinaryAssociation(
    name="appliedProperty123",
    ends={
        Property(name="#125", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1124", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
elements156: BinaryAssociation = BinaryAssociation(
    name="elements156",
    ends={
        Property(name="#158", type=OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1157", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart159: BinaryAssociation = BinaryAssociation(
    name="tuplePart159",
    ends={
        Property(name="#161", type=OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1160", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple162: BinaryAssociation = BinaryAssociation(
    name="tuple162",
    ends={
        Property(name="#164", type=OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="1163", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements165: BinaryAssociation = BinaryAssociation(
    name="elements165",
    ends={
        Property(name="#167", type=OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1166", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map168: BinaryAssociation = BinaryAssociation(
    name="map168",
    ends={
        Property(name="#170", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="1169", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key171: BinaryAssociation = BinaryAssociation(
    name="key171",
    ends={
        Property(name="OclExpression172", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value173: BinaryAssociation = BinaryAssociation(
    name="value173",
    ends={
        Property(name="OclExpression175", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement174", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments179: BinaryAssociation = BinaryAssociation(
    name="arguments179",
    ends={
        Property(name="#181", type=OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1180", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body182: BinaryAssociation = BinaryAssociation(
    name="body182",
    ends={
        Property(name="#184", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1183", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators185: BinaryAssociation = BinaryAssociation(
    name="iterators185",
    ends={
        Property(name="#187", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1186", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result188: BinaryAssociation = BinaryAssociation(
    name="result188",
    ends={
        Property(name="#190", type=OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1189", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable191: BinaryAssociation = BinaryAssociation(
    name="variable191",
    ends={
        Property(name="#193", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1192", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_194: BinaryAssociation = BinaryAssociation(
    name="in_194",
    ends={
        Property(name="#196", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1195", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source176: BinaryAssociation = BinaryAssociation(
    name="source176",
    ends={
        Property(name="#178", type=OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1177", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition200: BinaryAssociation = BinaryAssociation(
    name="condition200",
    ends={
        Property(name="#202", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1201", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression203: BinaryAssociation = BinaryAssociation(
    name="elseExpression203",
    ends={
        Property(name="#205", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1204", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type206: BinaryAssociation = BinaryAssociation(
    name="type206",
    ends={
        Property(name="#208", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1207", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression209: BinaryAssociation = BinaryAssociation(
    name="initExpression209",
    ends={
        Property(name="#211", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1210", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp212: BinaryAssociation = BinaryAssociation(
    name="letExp212",
    ends={
        Property(name="#214", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1213", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp215: BinaryAssociation = BinaryAssociation(
    name="baseExp215",
    ends={
        Property(name="#217", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1216", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp218: BinaryAssociation = BinaryAssociation(
    name="variableExp218",
    ends={
        Property(name="#220", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="1219", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr221: BinaryAssociation = BinaryAssociation(
    name="loopExpr221",
    ends={
        Property(name="#223", type=OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="1222", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation224: BinaryAssociation = BinaryAssociation(
    name="operation224",
    ends={
        Property(name="#226", type=OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="1225", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
elementType227: BinaryAssociation = BinaryAssociation(
    name="elementType227",
    ends={
        Property(name="#229", type=OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="1228", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression197: BinaryAssociation = BinaryAssociation(
    name="thenExpression197",
    ends={
        Property(name="#199", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="1198", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions230: BinaryAssociation = BinaryAssociation(
    name="definitions230",
    ends={
        Property(name="#232", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1231", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression233: BinaryAssociation = BinaryAssociation(
    name="oclExpression233",
    ends={
        Property(name="#235", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1234", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation236: BinaryAssociation = BinaryAssociation(
    name="operation236",
    ends={
        Property(name="#238", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1237", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2239: BinaryAssociation = BinaryAssociation(
    name="mapType2239",
    ends={
        Property(name="#241", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1240", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute242: BinaryAssociation = BinaryAssociation(
    name="attribute242",
    ends={
        Property(name="#244", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1243", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType245: BinaryAssociation = BinaryAssociation(
    name="mapType245",
    ends={
        Property(name="#247", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1246", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes248: BinaryAssociation = BinaryAssociation(
    name="collectionTypes248",
    ends={
        Property(name="#250", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1249", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute251: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute251",
    ends={
        Property(name="#253", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1252", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration254: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration254",
    ends={
        Property(name="#256", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="1255", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
attributes257: BinaryAssociation = BinaryAssociation(
    name="attributes257",
    ends={
        Property(name="#259", type=OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="1258", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type260: BinaryAssociation = BinaryAssociation(
    name="type260",
    ends={
        Property(name="#262", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1261", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType263: BinaryAssociation = BinaryAssociation(
    name="tupleType263",
    ends={
        Property(name="#265", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1264", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model266: BinaryAssociation = BinaryAssociation(
    name="model266",
    ends={
        Property(name="#268", type=OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="1267", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType269: BinaryAssociation = BinaryAssociation(
    name="valueType269",
    ends={
        Property(name="#271", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="1270", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType272: BinaryAssociation = BinaryAssociation(
    name="keyType272",
    ends={
        Property(name="#274", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="1273", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature275: BinaryAssociation = BinaryAssociation(
    name="feature275",
    ends={
        Property(name="#277", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1276", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_278: BinaryAssociation = BinaryAssociation(
    name="context_278",
    ends={
        Property(name="#280", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1279", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition281: BinaryAssociation = BinaryAssociation(
    name="definition281",
    ends={
        Property(name="#283", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1282", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_284: BinaryAssociation = BinaryAssociation(
    name="context_284",
    ends={
        Property(name="#286", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="1285", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression290: BinaryAssociation = BinaryAssociation(
    name="initExpression290",
    ends={
        Property(name="#292", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1291", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type293: BinaryAssociation = BinaryAssociation(
    name="type293",
    ends={
        Property(name="#295", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1294", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters296: BinaryAssociation = BinaryAssociation(
    name="parameters296",
    ends={
        Property(name="#298", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1297", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType299: BinaryAssociation = BinaryAssociation(
    name="returnType299",
    ends={
        Property(name="#301", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1300", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body302: BinaryAssociation = BinaryAssociation(
    name="body302",
    ends={
        Property(name="#304", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="1303", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel305: BinaryAssociation = BinaryAssociation(
    name="metamodel305",
    ends={
        Property(name="#307", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1306", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements308: BinaryAssociation = BinaryAssociation(
    name="elements308",
    ends={
        Property(name="#310", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1309", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model311: BinaryAssociation = BinaryAssociation(
    name="model311",
    ends={
        Property(name="#313", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="1312", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
definition287: BinaryAssociation = BinaryAssociation(
    name="definition287",
    ends={
        Property(name="#289", type=OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="1288", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=ATL_Unit)
gen_ATL_Library_Unit = Generalization(general=Unit, specific=ATL_Library)
gen_ATL_Query_Unit = Generalization(general=Unit, specific=ATL_Query)
gen_ATL_Module_Unit = Generalization(general=Unit, specific=ATL_Module)
gen_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=ATL_ModuleElement)
gen_ATL_Helper_ModuleElement = Generalization(general=ModuleElement, specific=ATL_Helper)
gen_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=ATL_Rule)
gen_ATL_MatchedRule_Rule = Generalization(general=Rule, specific=ATL_MatchedRule)
gen_ATL_LazyMatchedRule_MatchedRule = Generalization(general=MatchedRule, specific=ATL_LazyMatchedRule)
gen_ATL_CalledRule_Rule = Generalization(general=Rule, specific=ATL_CalledRule)
gen_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=ATL_InPattern)
gen_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=ATL_OutPattern)
gen_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=ATL_PatternElement)
gen_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=ATL_InPatternElement)
gen_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=ATL_SimpleInPatternElement)
gen_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=ATL_OutPatternElement)
gen_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=ATL_SimpleOutPatternElement)
gen_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=ATL_ForEachOutPatternElement)
gen_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=ATL_Binding)
gen_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=ATL_RuleVariableDeclaration)
gen_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=ATL_LibraryRef)
gen_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=ATL_ActionBlock)
gen_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=ATL_Statement)
gen_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=ATL_ExpressionStat)
gen_ATL_BindingStat_Statement = Generalization(general=Statement, specific=ATL_BindingStat)
gen_ATL_IfStat_Statement = Generalization(general=Statement, specific=ATL_IfStat)
gen_ATL_ForStat_Statement = Generalization(general=Statement, specific=ATL_ForStat)
gen_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclExpression)
gen_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=OCL_VariableExp)
gen_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=OCL_SuperExp)
gen_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PrimitiveExp)
gen_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_StringExp)
gen_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_BooleanExp)
gen_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_NumericExp)
gen_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=OCL_RealExp)
gen_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=OCL_CollectionExp)
gen_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_BagExp)
gen_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_OrderedSetExp)
gen_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_SequenceExp)
gen_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=OCL_SetExp)
gen_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=OCL_TupleExp)
gen_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_TuplePart)
gen_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=OCL_MapExp)
gen_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=OCL_MapElement)
gen_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=OCL_EnumLiteralExp)
gen_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=OCL_OclUndefinedExp)
gen_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PropertyCallExp)
gen_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=OCL_IntegerExp)
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
gen_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=OCL_OclAnyType)
gen_OCL_TupleType_OclType = Generalization(general=OclType, specific=OCL_TupleType)
gen_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=OCL_TupleTypeAttribute)
gen_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=OCL_OclModelElement)
gen_OCL_MapType_OclType = Generalization(general=OclType, specific=OCL_MapType)
gen_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeatureDefinition)
gen_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclContextDefinition)
gen_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeature)
gen_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=OCL_SetType)
gen_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=OCL_Attribute)
gen_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=OCL_Operation)
gen_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclModel)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={ATL_LocatedElement, ATL_Unit, LocatedElement, LibraryRef, ATL_Library, Unit, Helper, ATL_Query, OclExpression, ATL_Module, OclModel, ModuleElement, ATL_ModuleElement, Module, ATL_Helper, Query, Library, OclFeatureDefinition, ATL_Rule, OutPattern, ActionBlock, RuleVariableDeclaration, ATL_MatchedRule, Rule, InPattern, MatchedRule, ATL_LazyMatchedRule, ATL_CalledRule, Parameter_, ATL_InPattern, InPatternElement, ATL_OutPattern, OutPatternElement, ATL_PatternElement, VariableDeclaration, ATL_InPatternElement, PatternElement, ATL_SimpleInPatternElement, ATL_OutPatternElement, Binding, ATL_SimpleOutPatternElement, ATL_ForEachOutPatternElement, Iterator, ATL_Binding, ATL_RuleVariableDeclaration, ATL_LibraryRef, ATL_ActionBlock, Statement, ATL_Statement, ATL_ExpressionStat, ATL_BindingStat, ATL_IfStat, ATL_ForStat, OCL_OclExpression, OclType, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, Operation, Attribute, OCL_VariableExp, OCL_SuperExp, OCL_PrimitiveExp, OCL_StringExp, PrimitiveExp, OCL_BooleanExp, OCL_NumericExp, OCL_RealExp, NumericExp, OCL_IntegerExp, OCL_CollectionExp, OCL_BagExp, OCL_OrderedSetExp, OCL_SequenceExp, OCL_SetExp, OCL_TupleExp, TuplePart, OCL_TuplePart, TupleExp, OCL_MapExp, MapElement, OCL_MapElement, MapExp, OCL_EnumLiteralExp, OCL_OclUndefinedExp, OCL_PropertyCallExp, OCL_NavigationOrAttributeCallExp, OCL_OperationCallExp, OCL_OperatorCallExp, OCL_CollectionOperationCallExp, OCL_LoopExp, OCL_IterateExp, OCL_IteratorExp, OCL_LetExp, OCL_IfExp, OCL_VariableDeclaration, IterateExp, VariableExp, OCL_Iterator, OCL_Parameter, OCL_CollectionType, OCL_OclType, MapType, CollectionType, TupleTypeAttribute, OCL_Primitive, OCL_StringType, Primitive, OCL_BooleanType, OCL_NumericType, OCL_IntegerType, NumericType, OCL_RealType, OCL_BagType, OCL_OrderedSetType, OCL_SequenceType, OclContextDefinition, OCL_OclAnyType, OCL_TupleType, OCL_TupleTypeAttribute, TupleType, OCL_OclModelElement, OCL_MapType, OCL_OclFeatureDefinition, OclFeature, OCL_OclContextDefinition, OCL_OclFeature, OCL_SetType, OCL_Attribute, OCL_Operation, OCL_OclModel, OclModelElement},
    associations={libraries0, helpers1, body2, inModels6, outModels7, elements10, module13, query16, library19, definition20, outPattern22, actionBlock25, variables28, inPattern31, children34, superRule37, helpers3, parameters40, elements41, rule44, filter47, rule49, elements52, mapsTo55, inPattern58, models61, outPattern63, bindings69, model72, reverseBindings74, collection76, iterator78, value80, outPatternElement82, rule85, unit88, rule91, sourceElement66, expression95, source97, value99, condition102, thenStatements104, elseStatements107, iterator110, collection112, statements115, type118, ifExp3120, statements94, collection126, letExp129, loopExp132, parentOperation135, initializedVariable138, ifExp2141, owningOperation144, ifExp1147, owningAttribute150, referredVariable153, appliedProperty123, elements156, tuplePart159, tuple162, elements165, map168, key171, value173, arguments179, body182, iterators185, result188, variable191, in_194, source176, condition200, elseExpression203, type206, initExpression209, letExp212, baseExp215, variableExp218, loopExpr221, operation224, elementType227, thenExpression197, definitions230, oclExpression233, operation236, mapType2239, attribute242, mapType245, collectionTypes248, tupleTypeAttribute251, variableDeclaration254, attributes257, type260, tupleType263, model266, valueType269, keyType272, feature275, context_278, definition281, context_284, initExpression290, type293, parameters296, returnType299, body302, metamodel305, elements308, model311, definition287},
    generalizations={gen_ATL_Unit_LocatedElement, gen_ATL_Library_Unit, gen_ATL_Query_Unit, gen_ATL_Module_Unit, gen_ATL_ModuleElement_LocatedElement, gen_ATL_Helper_ModuleElement, gen_ATL_Rule_ModuleElement, gen_ATL_MatchedRule_Rule, gen_ATL_LazyMatchedRule_MatchedRule, gen_ATL_CalledRule_Rule, gen_ATL_InPattern_LocatedElement, gen_ATL_OutPattern_LocatedElement, gen_ATL_PatternElement_VariableDeclaration, gen_ATL_InPatternElement_PatternElement, gen_ATL_SimpleInPatternElement_InPatternElement, gen_ATL_OutPatternElement_PatternElement, gen_ATL_SimpleOutPatternElement_OutPatternElement, gen_ATL_ForEachOutPatternElement_OutPatternElement, gen_ATL_Binding_LocatedElement, gen_ATL_RuleVariableDeclaration_VariableDeclaration, gen_ATL_LibraryRef_LocatedElement, gen_ATL_ActionBlock_LocatedElement, gen_ATL_Statement_LocatedElement, gen_ATL_ExpressionStat_Statement, gen_ATL_BindingStat_Statement, gen_ATL_IfStat_Statement, gen_ATL_ForStat_Statement, gen_OCL_OclExpression_LocatedElement, gen_OCL_VariableExp_OclExpression, gen_OCL_SuperExp_OclExpression, gen_OCL_PrimitiveExp_OclExpression, gen_OCL_StringExp_PrimitiveExp, gen_OCL_BooleanExp_PrimitiveExp, gen_OCL_NumericExp_PrimitiveExp, gen_OCL_RealExp_NumericExp, gen_OCL_CollectionExp_OclExpression, gen_OCL_BagExp_CollectionExp, gen_OCL_OrderedSetExp_CollectionExp, gen_OCL_SequenceExp_CollectionExp, gen_OCL_SetExp_CollectionExp, gen_OCL_TupleExp_OclExpression, gen_OCL_TuplePart_VariableDeclaration, gen_OCL_MapExp_OclExpression, gen_OCL_MapElement_LocatedElement, gen_OCL_EnumLiteralExp_OclExpression, gen_OCL_OclUndefinedExp_OclExpression, gen_OCL_PropertyCallExp_OclExpression, gen_OCL_IntegerExp_NumericExp, gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_OCL_OperationCallExp_PropertyCallExp, gen_OCL_OperatorCallExp_OperationCallExp, gen_OCL_CollectionOperationCallExp_OperationCallExp, gen_OCL_LoopExp_PropertyCallExp, gen_OCL_IterateExp_LoopExp, gen_OCL_IteratorExp_LoopExp, gen_OCL_LetExp_OclExpression, gen_OCL_IfExp_OclExpression, gen_OCL_VariableDeclaration_LocatedElement, gen_OCL_Iterator_VariableDeclaration, gen_OCL_Parameter_VariableDeclaration, gen_OCL_CollectionType_OclType, gen_OCL_OclType_OclExpression, gen_OCL_Primitive_OclType, gen_OCL_StringType_Primitive, gen_OCL_BooleanType_Primitive, gen_OCL_NumericType_Primitive, gen_OCL_IntegerType_NumericType, gen_OCL_RealType_NumericType, gen_OCL_BagType_CollectionType, gen_OCL_OrderedSetType_CollectionType, gen_OCL_SequenceType_CollectionType, gen_OCL_OclAnyType_OclType, gen_OCL_TupleType_OclType, gen_OCL_TupleTypeAttribute_LocatedElement, gen_OCL_OclModelElement_OclType, gen_OCL_MapType_OclType, gen_OCL_OclFeatureDefinition_LocatedElement, gen_OCL_OclContextDefinition_LocatedElement, gen_OCL_OclFeature_LocatedElement, gen_OCL_SetType_CollectionType, gen_OCL_Attribute_OclFeature, gen_OCL_Operation_OclFeature, gen_OCL_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)