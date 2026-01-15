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
atl_n_ocl_ATL_Query = Class(name="atl::n::ocl::ATL::Query")
OclExpression = Class(name="OclExpression")
Helper = Class(name="Helper")
atl_n_ocl_ATL_MatchedRule = Class(name="atl::n::ocl::ATL::MatchedRule")
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
MatchedRule = Class(name="MatchedRule")
atl_n_ocl_ATL_LazyMatchedRule = Class(name="atl::n::ocl::ATL::LazyMatchedRule")
atl_n_ocl_ATL_Module = Class(name="atl::n::ocl::ATL::Module")
OclModel = Class(name="OclModel")
ModuleElement = Class(name="ModuleElement")
atl_n_ocl_ATL_ModuleElement = Class(name="atl::n::ocl::ATL::ModuleElement", is_abstract=True)
atl_n_ocl_ATL_Helper = Class(name="atl::n::ocl::ATL::Helper")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
atl_n_ocl_ATL_Rule = Class(name="atl::n::ocl::ATL::Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
atl_n_ocl_ATL_OutPatternElement = Class(name="atl::n::ocl::ATL::OutPatternElement", is_abstract=True)
Binding = Class(name="Binding")
atl_n_ocl_ATL_SimpleOutPatternElement = Class(name="atl::n::ocl::ATL::SimpleOutPatternElement")
atl_n_ocl_ATL_CalledRule = Class(name="atl::n::ocl::ATL::CalledRule")
Parameter_ = Class(name="Parameter")
atl_n_ocl_ATL_InPattern = Class(name="atl::n::ocl::ATL::InPattern")
InPatternElement = Class(name="InPatternElement")
atl_n_ocl_ATL_OutPattern = Class(name="atl::n::ocl::ATL::OutPattern")
DropPattern = Class(name="DropPattern")
OutPatternElement = Class(name="OutPatternElement")
atl_n_ocl_ATL_DropPattern = Class(name="atl::n::ocl::ATL::DropPattern")
atl_n_ocl_ATL_PatternElement = Class(name="atl::n::ocl::ATL::PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
atl_n_ocl_ATL_InPatternElement = Class(name="atl::n::ocl::ATL::InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
atl_n_ocl_ATL_SimpleInPatternElement = Class(name="atl::n::ocl::ATL::SimpleInPatternElement")
atl_n_ocl_ATL_IfStat = Class(name="atl::n::ocl::ATL::IfStat")
atl_n_ocl_ATL_ForEachOutPatternElement = Class(name="atl::n::ocl::ATL::ForEachOutPatternElement")
Iterator = Class(name="Iterator")
atl_n_ocl_ATL_Binding = Class(name="atl::n::ocl::ATL::Binding")
atl_n_ocl_ATL_RuleVariableDeclaration = Class(name="atl::n::ocl::ATL::RuleVariableDeclaration")
atl_n_ocl_ATL_ActionBlock = Class(name="atl::n::ocl::ATL::ActionBlock")
Statement = Class(name="Statement")
atl_n_ocl_ATL_Statement = Class(name="atl::n::ocl::ATL::Statement", is_abstract=True)
atl_n_ocl_ATL_ExpressionStat = Class(name="atl::n::ocl::ATL::ExpressionStat")
atl_n_ocl_ATL_BindingStat = Class(name="atl::n::ocl::ATL::BindingStat")
atl_n_ocl_OCL_VariableExp = Class(name="atl::n::ocl::OCL::VariableExp")
atl_n_ocl_ATL_ForStat = Class(name="atl::n::ocl::ATL::ForStat")
atl_n_ocl_OCL_OclExpression = Class(name="atl::n::ocl::OCL::OclExpression", is_abstract=True)
OclType = Class(name="OclType")
atl_n_ocl_OCL_SuperExp = Class(name="atl::n::ocl::OCL::SuperExp")
atl_n_ocl_OCL_PrimitiveExp = Class(name="atl::n::ocl::OCL::PrimitiveExp", is_abstract=True)
atl_n_ocl_OCL_StringExp = Class(name="atl::n::ocl::OCL::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
atl_n_ocl_OCL_NumericExp = Class(name="atl::n::ocl::OCL::NumericExp", is_abstract=True)
atl_n_ocl_OCL_RealExp = Class(name="atl::n::ocl::OCL::RealExp")
NumericExp = Class(name="NumericExp")
atl_n_ocl_OCL_IntegerExp = Class(name="atl::n::ocl::OCL::IntegerExp")
atl_n_ocl_OCL_CollectionExp = Class(name="atl::n::ocl::OCL::CollectionExp", is_abstract=True)
atl_n_ocl_OCL_BooleanExp = Class(name="atl::n::ocl::OCL::BooleanExp")
atl_n_ocl_OCL_OclUndefinedExp = Class(name="atl::n::ocl::OCL::OclUndefinedExp")
atl_n_ocl_OCL_PropertyCallExp = Class(name="atl::n::ocl::OCL::PropertyCallExp", is_abstract=True)
atl_n_ocl_OCL_NavigationOrAttributeCallExp = Class(name="atl::n::ocl::OCL::NavigationOrAttributeCallExp")
PropertyCallExp = Class(name="PropertyCallExp")
atl_n_ocl_OCL_OperationCallExp = Class(name="atl::n::ocl::OCL::OperationCallExp")
atl_n_ocl_OCL_BagExp = Class(name="atl::n::ocl::OCL::BagExp")
CollectionExp = Class(name="CollectionExp")
atl_n_ocl_OCL_OrderedSetExp = Class(name="atl::n::ocl::OCL::OrderedSetExp")
atl_n_ocl_OCL_SequenceExp = Class(name="atl::n::ocl::OCL::SequenceExp")
atl_n_ocl_OCL_SetExp = Class(name="atl::n::ocl::OCL::SetExp")
atl_n_ocl_OCL_TupleExp = Class(name="atl::n::ocl::OCL::TupleExp")
TuplePart = Class(name="TuplePart")
atl_n_ocl_OCL_TuplePart = Class(name="atl::n::ocl::OCL::TuplePart")
TupleExp = Class(name="TupleExp")
atl_n_ocl_OCL_MapExp = Class(name="atl::n::ocl::OCL::MapExp")
MapElement = Class(name="MapElement")
atl_n_ocl_OCL_MapElement = Class(name="atl::n::ocl::OCL::MapElement")
atl_n_ocl_OCL_EnumLiteralExp = Class(name="atl::n::ocl::OCL::EnumLiteralExp")
atl_n_ocl_OCL_IfExp = Class(name="atl::n::ocl::OCL::IfExp")
atl_n_ocl_OCL_OperatorCallExp = Class(name="atl::n::ocl::OCL::OperatorCallExp")
OperationCallExp = Class(name="OperationCallExp")
atl_n_ocl_OCL_CollectionOperationCallExp = Class(name="atl::n::ocl::OCL::CollectionOperationCallExp")
atl_n_ocl_OCL_LoopExp = Class(name="atl::n::ocl::OCL::LoopExp", is_abstract=True)
atl_n_ocl_OCL_IterateExp = Class(name="atl::n::ocl::OCL::IterateExp")
LoopExp = Class(name="LoopExp")
atl_n_ocl_OCL_IteratorExp = Class(name="atl::n::ocl::OCL::IteratorExp")
atl_n_ocl_OCL_LetExp = Class(name="atl::n::ocl::OCL::LetExp")
atl_n_ocl_OCL_BooleanType = Class(name="atl::n::ocl::OCL::BooleanType")
atl_n_ocl_OCL_NumericType = Class(name="atl::n::ocl::OCL::NumericType", is_abstract=True)
atl_n_ocl_OCL_IntegerType = Class(name="atl::n::ocl::OCL::IntegerType")
NumericType = Class(name="NumericType")
atl_n_ocl_OCL_RealType = Class(name="atl::n::ocl::OCL::RealType")
atl_n_ocl_OCL_BagType = Class(name="atl::n::ocl::OCL::BagType")
CollectionType = Class(name="CollectionType")
atl_n_ocl_OCL_OrderedSetType = Class(name="atl::n::ocl::OCL::OrderedSetType")
atl_n_ocl_OCL_SequenceType = Class(name="atl::n::ocl::OCL::SequenceType")
atl_n_ocl_OCL_SetType = Class(name="atl::n::ocl::OCL::SetType")
atl_n_ocl_OCL_OclAnyType = Class(name="atl::n::ocl::OCL::OclAnyType")
atl_n_ocl_OCL_TupleType = Class(name="atl::n::ocl::OCL::TupleType")
atl_n_ocl_OCL_VariableDeclaration = Class(name="atl::n::ocl::OCL::VariableDeclaration")
atl_n_ocl_OCL_Iterator = Class(name="atl::n::ocl::OCL::Iterator")
atl_n_ocl_OCL_Parameter = Class(name="atl::n::ocl::OCL::Parameter")
atl_n_ocl_OCL_CollectionType = Class(name="atl::n::ocl::OCL::CollectionType")
atl_n_ocl_OCL_OclType = Class(name="atl::n::ocl::OCL::OclType")
atl_n_ocl_OCL_Primitive = Class(name="atl::n::ocl::OCL::Primitive", is_abstract=True)
atl_n_ocl_OCL_StringType = Class(name="atl::n::ocl::OCL::StringType")
Primitive = Class(name="Primitive")
atl_n_ocl_OCL_Attribute = Class(name="atl::n::ocl::OCL::Attribute")
atl_n_ocl_OCL_Operation = Class(name="atl::n::ocl::OCL::Operation")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
atl_n_ocl_OCL_TupleTypeAttribute = Class(name="atl::n::ocl::OCL::TupleTypeAttribute")
atl_n_ocl_OCL_OclModelElement = Class(name="atl::n::ocl::OCL::OclModelElement")
atl_n_ocl_OCL_MapType = Class(name="atl::n::ocl::OCL::MapType")
atl_n_ocl_OCL_OclFeatureDefinition = Class(name="atl::n::ocl::OCL::OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
OclContextDefinition = Class(name="OclContextDefinition")
atl_n_ocl_OCL_OclContextDefinition = Class(name="atl::n::ocl::OCL::OclContextDefinition")
atl_n_ocl_OCL_OclFeature = Class(name="atl::n::ocl::OCL::OclFeature", is_abstract=True)
atl_n_ocl_OCL_OclModel = Class(name="atl::n::ocl::OCL::OclModel")
OclModelElement = Class(name="OclModelElement")

# atl_n_ocl_ATL_Query class attributes and methods

# OclExpression class attributes and methods

# Helper class attributes and methods

# atl_n_ocl_ATL_MatchedRule class attributes and methods
atl_n_ocl_ATL_MatchedRule_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
atl_n_ocl_ATL_MatchedRule_isRefining: Property = Property(name="isRefining", type=BooleanType)
atl_n_ocl_ATL_MatchedRule_isNoDefault: Property = Property(name="isNoDefault", type=BooleanType)
atl_n_ocl_ATL_MatchedRule.attributes={atl_n_ocl_ATL_MatchedRule_isNoDefault, atl_n_ocl_ATL_MatchedRule_isRefining, atl_n_ocl_ATL_MatchedRule_isAbstract}

# Rule class attributes and methods

# InPattern class attributes and methods

# MatchedRule class attributes and methods

# atl_n_ocl_ATL_LazyMatchedRule class attributes and methods
atl_n_ocl_ATL_LazyMatchedRule_isUnique: Property = Property(name="isUnique", type=BooleanType)
atl_n_ocl_ATL_LazyMatchedRule.attributes={atl_n_ocl_ATL_LazyMatchedRule_isUnique}

# atl_n_ocl_ATL_Module class attributes and methods
atl_n_ocl_ATL_Module_isRefining: Property = Property(name="isRefining", type=BooleanType)
atl_n_ocl_ATL_Module.attributes={atl_n_ocl_ATL_Module_isRefining}

# OclModel class attributes and methods

# ModuleElement class attributes and methods

# atl_n_ocl_ATL_ModuleElement class attributes and methods

# atl_n_ocl_ATL_Helper class attributes and methods

# OclFeatureDefinition class attributes and methods

# atl_n_ocl_ATL_Rule class attributes and methods
atl_n_ocl_ATL_Rule_name: Property = Property(name="name", type=StringType)
atl_n_ocl_ATL_Rule.attributes={atl_n_ocl_ATL_Rule_name}

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# atl_n_ocl_ATL_OutPatternElement class attributes and methods

# Binding class attributes and methods

# atl_n_ocl_ATL_SimpleOutPatternElement class attributes and methods

# atl_n_ocl_ATL_CalledRule class attributes and methods
atl_n_ocl_ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=BooleanType)
atl_n_ocl_ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=BooleanType)
atl_n_ocl_ATL_CalledRule.attributes={atl_n_ocl_ATL_CalledRule_isEndpoint, atl_n_ocl_ATL_CalledRule_isEntrypoint}

# Parameter class attributes and methods

# atl_n_ocl_ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# atl_n_ocl_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# OutPatternElement class attributes and methods

# atl_n_ocl_ATL_DropPattern class attributes and methods

# atl_n_ocl_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# atl_n_ocl_ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# atl_n_ocl_ATL_SimpleInPatternElement class attributes and methods

# atl_n_ocl_ATL_IfStat class attributes and methods

# atl_n_ocl_ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# atl_n_ocl_ATL_Binding class attributes and methods
atl_n_ocl_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
atl_n_ocl_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=BooleanType)
atl_n_ocl_ATL_Binding.attributes={atl_n_ocl_ATL_Binding_isAssignment, atl_n_ocl_ATL_Binding_propertyName}

# atl_n_ocl_ATL_RuleVariableDeclaration class attributes and methods

# atl_n_ocl_ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# atl_n_ocl_ATL_Statement class attributes and methods

# atl_n_ocl_ATL_ExpressionStat class attributes and methods

# atl_n_ocl_ATL_BindingStat class attributes and methods
atl_n_ocl_ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=BooleanType)
atl_n_ocl_ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
atl_n_ocl_ATL_BindingStat.attributes={atl_n_ocl_ATL_BindingStat_isAssignment, atl_n_ocl_ATL_BindingStat_propertyName}

# atl_n_ocl_OCL_VariableExp class attributes and methods

# atl_n_ocl_ATL_ForStat class attributes and methods

# atl_n_ocl_OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# atl_n_ocl_OCL_SuperExp class attributes and methods

# atl_n_ocl_OCL_PrimitiveExp class attributes and methods

# atl_n_ocl_OCL_StringExp class attributes and methods
atl_n_ocl_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
atl_n_ocl_OCL_StringExp.attributes={atl_n_ocl_OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# atl_n_ocl_OCL_NumericExp class attributes and methods

# atl_n_ocl_OCL_RealExp class attributes and methods
atl_n_ocl_OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=FloatType)
atl_n_ocl_OCL_RealExp.attributes={atl_n_ocl_OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# atl_n_ocl_OCL_IntegerExp class attributes and methods
atl_n_ocl_OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=IntegerType)
atl_n_ocl_OCL_IntegerExp.attributes={atl_n_ocl_OCL_IntegerExp_integerSymbol}

# atl_n_ocl_OCL_CollectionExp class attributes and methods

# atl_n_ocl_OCL_BooleanExp class attributes and methods
atl_n_ocl_OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=BooleanType)
atl_n_ocl_OCL_BooleanExp.attributes={atl_n_ocl_OCL_BooleanExp_booleanSymbol}

# atl_n_ocl_OCL_OclUndefinedExp class attributes and methods

# atl_n_ocl_OCL_PropertyCallExp class attributes and methods

# atl_n_ocl_OCL_NavigationOrAttributeCallExp class attributes and methods
atl_n_ocl_OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
atl_n_ocl_OCL_NavigationOrAttributeCallExp.attributes={atl_n_ocl_OCL_NavigationOrAttributeCallExp_name}

# PropertyCallExp class attributes and methods

# atl_n_ocl_OCL_OperationCallExp class attributes and methods
atl_n_ocl_OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
atl_n_ocl_OCL_OperationCallExp.attributes={atl_n_ocl_OCL_OperationCallExp_operationName}

# atl_n_ocl_OCL_BagExp class attributes and methods

# CollectionExp class attributes and methods

# atl_n_ocl_OCL_OrderedSetExp class attributes and methods

# atl_n_ocl_OCL_SequenceExp class attributes and methods

# atl_n_ocl_OCL_SetExp class attributes and methods

# atl_n_ocl_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# atl_n_ocl_OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# atl_n_ocl_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# atl_n_ocl_OCL_MapElement class attributes and methods

# atl_n_ocl_OCL_EnumLiteralExp class attributes and methods
atl_n_ocl_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
atl_n_ocl_OCL_EnumLiteralExp.attributes={atl_n_ocl_OCL_EnumLiteralExp_name}

# atl_n_ocl_OCL_IfExp class attributes and methods

# atl_n_ocl_OCL_OperatorCallExp class attributes and methods

# OperationCallExp class attributes and methods

# atl_n_ocl_OCL_CollectionOperationCallExp class attributes and methods

# atl_n_ocl_OCL_LoopExp class attributes and methods

# atl_n_ocl_OCL_IterateExp class attributes and methods

# LoopExp class attributes and methods

# atl_n_ocl_OCL_IteratorExp class attributes and methods
atl_n_ocl_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
atl_n_ocl_OCL_IteratorExp.attributes={atl_n_ocl_OCL_IteratorExp_name}

# atl_n_ocl_OCL_LetExp class attributes and methods

# atl_n_ocl_OCL_BooleanType class attributes and methods

# atl_n_ocl_OCL_NumericType class attributes and methods

# atl_n_ocl_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# atl_n_ocl_OCL_RealType class attributes and methods

# atl_n_ocl_OCL_BagType class attributes and methods

# CollectionType class attributes and methods

# atl_n_ocl_OCL_OrderedSetType class attributes and methods

# atl_n_ocl_OCL_SequenceType class attributes and methods

# atl_n_ocl_OCL_SetType class attributes and methods

# atl_n_ocl_OCL_OclAnyType class attributes and methods

# atl_n_ocl_OCL_TupleType class attributes and methods

# atl_n_ocl_OCL_VariableDeclaration class attributes and methods
atl_n_ocl_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
atl_n_ocl_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
atl_n_ocl_OCL_VariableDeclaration.attributes={atl_n_ocl_OCL_VariableDeclaration_id, atl_n_ocl_OCL_VariableDeclaration_varName}

# atl_n_ocl_OCL_Iterator class attributes and methods

# atl_n_ocl_OCL_Parameter class attributes and methods

# atl_n_ocl_OCL_CollectionType class attributes and methods

# atl_n_ocl_OCL_OclType class attributes and methods
atl_n_ocl_OCL_OclType_name: Property = Property(name="name", type=StringType)
atl_n_ocl_OCL_OclType.attributes={atl_n_ocl_OCL_OclType_name}

# atl_n_ocl_OCL_Primitive class attributes and methods

# atl_n_ocl_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# atl_n_ocl_OCL_Attribute class attributes and methods
atl_n_ocl_OCL_Attribute_name: Property = Property(name="name", type=StringType)
atl_n_ocl_OCL_Attribute.attributes={atl_n_ocl_OCL_Attribute_name}

# atl_n_ocl_OCL_Operation class attributes and methods
atl_n_ocl_OCL_Operation_name: Property = Property(name="name", type=StringType)
atl_n_ocl_OCL_Operation.attributes={atl_n_ocl_OCL_Operation_name}

# TupleTypeAttribute class attributes and methods

# atl_n_ocl_OCL_TupleTypeAttribute class attributes and methods
atl_n_ocl_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
atl_n_ocl_OCL_TupleTypeAttribute.attributes={atl_n_ocl_OCL_TupleTypeAttribute_name}

# atl_n_ocl_OCL_OclModelElement class attributes and methods

# atl_n_ocl_OCL_MapType class attributes and methods

# atl_n_ocl_OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# OclContextDefinition class attributes and methods

# atl_n_ocl_OCL_OclContextDefinition class attributes and methods

# atl_n_ocl_OCL_OclFeature class attributes and methods

# atl_n_ocl_OCL_OclModel class attributes and methods
atl_n_ocl_OCL_OclModel_name: Property = Property(name="name", type=StringType)
atl_n_ocl_OCL_OclModel.attributes={atl_n_ocl_OCL_OclModel_name}

# OclModelElement class attributes and methods

# Relationships
body0: BinaryAssociation = BinaryAssociation(
    name="body0",
    ends={
        Property(name="OclExpression", type=atl_n_ocl_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPattern15: BinaryAssociation = BinaryAssociation(
    name="inPattern15",
    ends={
        Property(name="InPattern", type=atl_n_ocl_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_MatchedRule", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children16: BinaryAssociation = BinaryAssociation(
    name="children16",
    ends={
        Property(name="MatchedRule", type=atl_n_ocl_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_MatchedRule17", type=MatchedRule, multiplicity=Multiplicity(0, 9999))
    }
)
helpers1: BinaryAssociation = BinaryAssociation(
    name="helpers1",
    ends={
        Property(name="Helper", type=atl_n_ocl_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_Query2", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inModels3: BinaryAssociation = BinaryAssociation(
    name="inModels3",
    ends={
        Property(name="OclModel", type=atl_n_ocl_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outModels4: BinaryAssociation = BinaryAssociation(
    name="outModels4",
    ends={
        Property(name="OclModel6", type=atl_n_ocl_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_Module5", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements7: BinaryAssociation = BinaryAssociation(
    name="elements7",
    ends={
        Property(name="ModuleElement", type=atl_n_ocl_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_Module8", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition9: BinaryAssociation = BinaryAssociation(
    name="definition9",
    ends={
        Property(name="OclFeatureDefinition", type=atl_n_ocl_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPattern10: BinaryAssociation = BinaryAssociation(
    name="outPattern10",
    ends={
        Property(name="OutPattern", type=atl_n_ocl_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_Rule", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock11: BinaryAssociation = BinaryAssociation(
    name="actionBlock11",
    ends={
        Property(name="ActionBlock", type=atl_n_ocl_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_Rule12", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables13: BinaryAssociation = BinaryAssociation(
    name="variables13",
    ends={
        Property(name="RuleVariableDeclaration", type=atl_n_ocl_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_Rule14", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceElement30: BinaryAssociation = BinaryAssociation(
    name="sourceElement30",
    ends={
        Property(name="InPatternElement31", type=atl_n_ocl_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_OutPatternElement", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings32: BinaryAssociation = BinaryAssociation(
    name="bindings32",
    ends={
        Property(name="Binding", type=atl_n_ocl_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_OutPatternElement33", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model34: BinaryAssociation = BinaryAssociation(
    name="model34",
    ends={
        Property(name="OclModel36", type=atl_n_ocl_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_OutPatternElement35", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings37: BinaryAssociation = BinaryAssociation(
    name="reverseBindings37",
    ends={
        Property(name="OclExpression38", type=atl_n_ocl_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters18: BinaryAssociation = BinaryAssociation(
    name="parameters18",
    ends={
        Property(name="Parameter", type=atl_n_ocl_ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements19: BinaryAssociation = BinaryAssociation(
    name="elements19",
    ends={
        Property(name="InPatternElement", type=atl_n_ocl_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_InPattern", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
filter20: BinaryAssociation = BinaryAssociation(
    name="filter20",
    ends={
        Property(name="OclExpression22", type=atl_n_ocl_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_InPattern21", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dropPattern23: BinaryAssociation = BinaryAssociation(
    name="dropPattern23",
    ends={
        Property(name="DropPattern", type=atl_n_ocl_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_OutPattern", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements24: BinaryAssociation = BinaryAssociation(
    name="elements24",
    ends={
        Property(name="OutPatternElement", type=atl_n_ocl_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_OutPattern25", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern26: BinaryAssociation = BinaryAssociation(
    name="outPattern26",
    ends={
        Property(name="OutPattern27", type=atl_n_ocl_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_DropPattern", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
models28: BinaryAssociation = BinaryAssociation(
    name="models28",
    ends={
        Property(name="OclModel29", type=atl_n_ocl_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
value50: BinaryAssociation = BinaryAssociation(
    name="value50",
    ends={
        Property(name="OclExpression52", type=atl_n_ocl_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_BindingStat51", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition53: BinaryAssociation = BinaryAssociation(
    name="condition53",
    ends={
        Property(name="OclExpression54", type=atl_n_ocl_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements55: BinaryAssociation = BinaryAssociation(
    name="thenStatements55",
    ends={
        Property(name="Statement57", type=atl_n_ocl_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_IfStat56", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements58: BinaryAssociation = BinaryAssociation(
    name="elseStatements58",
    ends={
        Property(name="Statement60", type=atl_n_ocl_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_IfStat59", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection39: BinaryAssociation = BinaryAssociation(
    name="collection39",
    ends={
        Property(name="OclExpression40", type=atl_n_ocl_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator41: BinaryAssociation = BinaryAssociation(
    name="iterator41",
    ends={
        Property(name="Iterator", type=atl_n_ocl_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_ForEachOutPatternElement42", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value43: BinaryAssociation = BinaryAssociation(
    name="value43",
    ends={
        Property(name="OclExpression44", type=atl_n_ocl_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements45: BinaryAssociation = BinaryAssociation(
    name="statements45",
    ends={
        Property(name="Statement", type=atl_n_ocl_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression46: BinaryAssociation = BinaryAssociation(
    name="expression46",
    ends={
        Property(name="OclExpression47", type=atl_n_ocl_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source48: BinaryAssociation = BinaryAssociation(
    name="source48",
    ends={
        Property(name="OclExpression49", type=atl_n_ocl_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredVariable70: BinaryAssociation = BinaryAssociation(
    name="referredVariable70",
    ends={
        Property(name="VariableDeclaration", type=atl_n_ocl_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_VariableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
iterator61: BinaryAssociation = BinaryAssociation(
    name="iterator61",
    ends={
        Property(name="Iterator62", type=atl_n_ocl_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection63: BinaryAssociation = BinaryAssociation(
    name="collection63",
    ends={
        Property(name="OclExpression65", type=atl_n_ocl_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_ForStat64", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements66: BinaryAssociation = BinaryAssociation(
    name="statements66",
    ends={
        Property(name="Statement68", type=atl_n_ocl_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_ATL_ForStat67", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type69: BinaryAssociation = BinaryAssociation(
    name="type69",
    ends={
        Property(name="OclType", type=atl_n_ocl_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_OclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements71: BinaryAssociation = BinaryAssociation(
    name="elements71",
    ends={
        Property(name="OclExpression72", type=atl_n_ocl_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_CollectionExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source81: BinaryAssociation = BinaryAssociation(
    name="source81",
    ends={
        Property(name="OclExpression82", type=atl_n_ocl_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_PropertyCallExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tuplePart73: BinaryAssociation = BinaryAssociation(
    name="tuplePart73",
    ends={
        Property(name="TuplePart", type=atl_n_ocl_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_TupleExp", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple74: BinaryAssociation = BinaryAssociation(
    name="tuple74",
    ends={
        Property(name="TupleExp", type=atl_n_ocl_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_TuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements75: BinaryAssociation = BinaryAssociation(
    name="elements75",
    ends={
        Property(name="MapElement", type=atl_n_ocl_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_MapExp", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key76: BinaryAssociation = BinaryAssociation(
    name="key76",
    ends={
        Property(name="OclExpression77", type=atl_n_ocl_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value78: BinaryAssociation = BinaryAssociation(
    name="value78",
    ends={
        Property(name="OclExpression80", type=atl_n_ocl_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_MapElement79", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_94: BinaryAssociation = BinaryAssociation(
    name="in_94",
    ends={
        Property(name="OclExpression96", type=atl_n_ocl_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_LetExp95", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression97: BinaryAssociation = BinaryAssociation(
    name="thenExpression97",
    ends={
        Property(name="OclExpression98", type=atl_n_ocl_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition99: BinaryAssociation = BinaryAssociation(
    name="condition99",
    ends={
        Property(name="OclExpression101", type=atl_n_ocl_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_IfExp100", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments83: BinaryAssociation = BinaryAssociation(
    name="arguments83",
    ends={
        Property(name="OclExpression84", type=atl_n_ocl_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body85: BinaryAssociation = BinaryAssociation(
    name="body85",
    ends={
        Property(name="OclExpression86", type=atl_n_ocl_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators87: BinaryAssociation = BinaryAssociation(
    name="iterators87",
    ends={
        Property(name="Iterator89", type=atl_n_ocl_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_LoopExp88", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result90: BinaryAssociation = BinaryAssociation(
    name="result90",
    ends={
        Property(name="VariableDeclaration91", type=atl_n_ocl_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_IterateExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable92: BinaryAssociation = BinaryAssociation(
    name="variable92",
    ends={
        Property(name="VariableDeclaration93", type=atl_n_ocl_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_LetExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression102: BinaryAssociation = BinaryAssociation(
    name="elseExpression102",
    ends={
        Property(name="OclExpression104", type=atl_n_ocl_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_IfExp103", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type105: BinaryAssociation = BinaryAssociation(
    name="type105",
    ends={
        Property(name="OclType106", type=atl_n_ocl_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_VariableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression107: BinaryAssociation = BinaryAssociation(
    name="initExpression107",
    ends={
        Property(name="OclExpression109", type=atl_n_ocl_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_VariableDeclaration108", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType110: BinaryAssociation = BinaryAssociation(
    name="elementType110",
    ends={
        Property(name="OclType111", type=atl_n_ocl_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_CollectionType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression125: BinaryAssociation = BinaryAssociation(
    name="initExpression125",
    ends={
        Property(name="OclExpression126", type=atl_n_ocl_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_Attribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type127: BinaryAssociation = BinaryAssociation(
    name="type127",
    ends={
        Property(name="OclType129", type=atl_n_ocl_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_Attribute128", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes112: BinaryAssociation = BinaryAssociation(
    name="attributes112",
    ends={
        Property(name="TupleTypeAttribute", type=atl_n_ocl_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_TupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type113: BinaryAssociation = BinaryAssociation(
    name="type113",
    ends={
        Property(name="OclType114", type=atl_n_ocl_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_TupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueType115: BinaryAssociation = BinaryAssociation(
    name="valueType115",
    ends={
        Property(name="OclType116", type=atl_n_ocl_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_MapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType117: BinaryAssociation = BinaryAssociation(
    name="keyType117",
    ends={
        Property(name="OclType119", type=atl_n_ocl_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_MapType118", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature120: BinaryAssociation = BinaryAssociation(
    name="feature120",
    ends={
        Property(name="OclFeature", type=atl_n_ocl_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_OclFeatureDefinition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_121: BinaryAssociation = BinaryAssociation(
    name="context_121",
    ends={
        Property(name="OclContextDefinition", type=atl_n_ocl_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_OclFeatureDefinition122", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context_123: BinaryAssociation = BinaryAssociation(
    name="context_123",
    ends={
        Property(name="OclType124", type=atl_n_ocl_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_OclContextDefinition", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters130: BinaryAssociation = BinaryAssociation(
    name="parameters130",
    ends={
        Property(name="Parameter131", type=atl_n_ocl_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType132: BinaryAssociation = BinaryAssociation(
    name="returnType132",
    ends={
        Property(name="OclType134", type=atl_n_ocl_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_Operation133", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body135: BinaryAssociation = BinaryAssociation(
    name="body135",
    ends={
        Property(name="OclExpression137", type=atl_n_ocl_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_Operation136", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel138: BinaryAssociation = BinaryAssociation(
    name="metamodel138",
    ends={
        Property(name="OclModel139", type=atl_n_ocl_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_OclModel", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements140: BinaryAssociation = BinaryAssociation(
    name="elements140",
    ends={
        Property(name="OclModelElement", type=atl_n_ocl_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_OclModel141", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model142: BinaryAssociation = BinaryAssociation(
    name="model142",
    ends={
        Property(name="OclModel144", type=atl_n_ocl_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="atl_n_ocl_OCL_OclModel143", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_atl_n_ocl_ATL_MatchedRule_Rule = Generalization(general=Rule, specific=atl_n_ocl_ATL_MatchedRule)
gen_atl_n_ocl_ATL_LazyMatchedRule_MatchedRule = Generalization(general=MatchedRule, specific=atl_n_ocl_ATL_LazyMatchedRule)
gen_atl_n_ocl_ATL_Helper_ModuleElement = Generalization(general=ModuleElement, specific=atl_n_ocl_ATL_Helper)
gen_atl_n_ocl_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=atl_n_ocl_ATL_Rule)
gen_atl_n_ocl_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=atl_n_ocl_ATL_SimpleInPatternElement)
gen_atl_n_ocl_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=atl_n_ocl_ATL_OutPatternElement)
gen_atl_n_ocl_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atl_n_ocl_ATL_SimpleOutPatternElement)
gen_atl_n_ocl_ATL_CalledRule_Rule = Generalization(general=Rule, specific=atl_n_ocl_ATL_CalledRule)
gen_atl_n_ocl_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atl_n_ocl_ATL_PatternElement)
gen_atl_n_ocl_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=atl_n_ocl_ATL_InPatternElement)
gen_atl_n_ocl_ATL_IfStat_Statement = Generalization(general=Statement, specific=atl_n_ocl_ATL_IfStat)
gen_atl_n_ocl_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atl_n_ocl_ATL_ForEachOutPatternElement)
gen_atl_n_ocl_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atl_n_ocl_ATL_RuleVariableDeclaration)
gen_atl_n_ocl_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=atl_n_ocl_ATL_ExpressionStat)
gen_atl_n_ocl_ATL_BindingStat_Statement = Generalization(general=Statement, specific=atl_n_ocl_ATL_BindingStat)
gen_atl_n_ocl_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_VariableExp)
gen_atl_n_ocl_ATL_ForStat_Statement = Generalization(general=Statement, specific=atl_n_ocl_ATL_ForStat)
gen_atl_n_ocl_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_SuperExp)
gen_atl_n_ocl_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_PrimitiveExp)
gen_atl_n_ocl_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atl_n_ocl_OCL_StringExp)
gen_atl_n_ocl_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atl_n_ocl_OCL_NumericExp)
gen_atl_n_ocl_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=atl_n_ocl_OCL_RealExp)
gen_atl_n_ocl_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=atl_n_ocl_OCL_IntegerExp)
gen_atl_n_ocl_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_CollectionExp)
gen_atl_n_ocl_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atl_n_ocl_OCL_BooleanExp)
gen_atl_n_ocl_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_OclUndefinedExp)
gen_atl_n_ocl_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_PropertyCallExp)
gen_atl_n_ocl_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atl_n_ocl_OCL_NavigationOrAttributeCallExp)
gen_atl_n_ocl_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atl_n_ocl_OCL_OperationCallExp)
gen_atl_n_ocl_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=atl_n_ocl_OCL_BagExp)
gen_atl_n_ocl_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=atl_n_ocl_OCL_OrderedSetExp)
gen_atl_n_ocl_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=atl_n_ocl_OCL_SequenceExp)
gen_atl_n_ocl_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=atl_n_ocl_OCL_SetExp)
gen_atl_n_ocl_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_TupleExp)
gen_atl_n_ocl_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atl_n_ocl_OCL_TuplePart)
gen_atl_n_ocl_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_MapExp)
gen_atl_n_ocl_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_EnumLiteralExp)
gen_atl_n_ocl_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_IfExp)
gen_atl_n_ocl_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atl_n_ocl_OCL_OperatorCallExp)
gen_atl_n_ocl_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atl_n_ocl_OCL_CollectionOperationCallExp)
gen_atl_n_ocl_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atl_n_ocl_OCL_LoopExp)
gen_atl_n_ocl_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=atl_n_ocl_OCL_IterateExp)
gen_atl_n_ocl_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=atl_n_ocl_OCL_IteratorExp)
gen_atl_n_ocl_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_LetExp)
gen_atl_n_ocl_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=atl_n_ocl_OCL_BooleanType)
gen_atl_n_ocl_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=atl_n_ocl_OCL_NumericType)
gen_atl_n_ocl_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=atl_n_ocl_OCL_IntegerType)
gen_atl_n_ocl_OCL_RealType_NumericType = Generalization(general=NumericType, specific=atl_n_ocl_OCL_RealType)
gen_atl_n_ocl_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=atl_n_ocl_OCL_BagType)
gen_atl_n_ocl_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=atl_n_ocl_OCL_OrderedSetType)
gen_atl_n_ocl_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=atl_n_ocl_OCL_SequenceType)
gen_atl_n_ocl_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=atl_n_ocl_OCL_SetType)
gen_atl_n_ocl_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=atl_n_ocl_OCL_OclAnyType)
gen_atl_n_ocl_OCL_TupleType_OclType = Generalization(general=OclType, specific=atl_n_ocl_OCL_TupleType)
gen_atl_n_ocl_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atl_n_ocl_OCL_Iterator)
gen_atl_n_ocl_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atl_n_ocl_OCL_Parameter)
gen_atl_n_ocl_OCL_CollectionType_OclType = Generalization(general=OclType, specific=atl_n_ocl_OCL_CollectionType)
gen_atl_n_ocl_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=atl_n_ocl_OCL_OclType)
gen_atl_n_ocl_OCL_Primitive_OclType = Generalization(general=OclType, specific=atl_n_ocl_OCL_Primitive)
gen_atl_n_ocl_OCL_StringType_Primitive = Generalization(general=Primitive, specific=atl_n_ocl_OCL_StringType)
gen_atl_n_ocl_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=atl_n_ocl_OCL_Attribute)
gen_atl_n_ocl_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=atl_n_ocl_OCL_Operation)
gen_atl_n_ocl_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=atl_n_ocl_OCL_OclModelElement)
gen_atl_n_ocl_OCL_MapType_OclType = Generalization(general=OclType, specific=atl_n_ocl_OCL_MapType)

# Domain Model
domain_model = DomainModel(
    name="atl_n_ocl",
    types={atl_n_ocl_ATL_Query, OclExpression, Helper, atl_n_ocl_ATL_MatchedRule, Rule, InPattern, MatchedRule, atl_n_ocl_ATL_LazyMatchedRule, atl_n_ocl_ATL_Module, OclModel, ModuleElement, atl_n_ocl_ATL_ModuleElement, atl_n_ocl_ATL_Helper, OclFeatureDefinition, atl_n_ocl_ATL_Rule, OutPattern, ActionBlock, RuleVariableDeclaration, atl_n_ocl_ATL_OutPatternElement, Binding, atl_n_ocl_ATL_SimpleOutPatternElement, atl_n_ocl_ATL_CalledRule, Parameter_, atl_n_ocl_ATL_InPattern, InPatternElement, atl_n_ocl_ATL_OutPattern, DropPattern, OutPatternElement, atl_n_ocl_ATL_DropPattern, atl_n_ocl_ATL_PatternElement, VariableDeclaration, atl_n_ocl_ATL_InPatternElement, PatternElement, atl_n_ocl_ATL_SimpleInPatternElement, atl_n_ocl_ATL_IfStat, atl_n_ocl_ATL_ForEachOutPatternElement, Iterator, atl_n_ocl_ATL_Binding, atl_n_ocl_ATL_RuleVariableDeclaration, atl_n_ocl_ATL_ActionBlock, Statement, atl_n_ocl_ATL_Statement, atl_n_ocl_ATL_ExpressionStat, atl_n_ocl_ATL_BindingStat, atl_n_ocl_OCL_VariableExp, atl_n_ocl_ATL_ForStat, atl_n_ocl_OCL_OclExpression, OclType, atl_n_ocl_OCL_SuperExp, atl_n_ocl_OCL_PrimitiveExp, atl_n_ocl_OCL_StringExp, PrimitiveExp, atl_n_ocl_OCL_NumericExp, atl_n_ocl_OCL_RealExp, NumericExp, atl_n_ocl_OCL_IntegerExp, atl_n_ocl_OCL_CollectionExp, atl_n_ocl_OCL_BooleanExp, atl_n_ocl_OCL_OclUndefinedExp, atl_n_ocl_OCL_PropertyCallExp, atl_n_ocl_OCL_NavigationOrAttributeCallExp, PropertyCallExp, atl_n_ocl_OCL_OperationCallExp, atl_n_ocl_OCL_BagExp, CollectionExp, atl_n_ocl_OCL_OrderedSetExp, atl_n_ocl_OCL_SequenceExp, atl_n_ocl_OCL_SetExp, atl_n_ocl_OCL_TupleExp, TuplePart, atl_n_ocl_OCL_TuplePart, TupleExp, atl_n_ocl_OCL_MapExp, MapElement, atl_n_ocl_OCL_MapElement, atl_n_ocl_OCL_EnumLiteralExp, atl_n_ocl_OCL_IfExp, atl_n_ocl_OCL_OperatorCallExp, OperationCallExp, atl_n_ocl_OCL_CollectionOperationCallExp, atl_n_ocl_OCL_LoopExp, atl_n_ocl_OCL_IterateExp, LoopExp, atl_n_ocl_OCL_IteratorExp, atl_n_ocl_OCL_LetExp, atl_n_ocl_OCL_BooleanType, atl_n_ocl_OCL_NumericType, atl_n_ocl_OCL_IntegerType, NumericType, atl_n_ocl_OCL_RealType, atl_n_ocl_OCL_BagType, CollectionType, atl_n_ocl_OCL_OrderedSetType, atl_n_ocl_OCL_SequenceType, atl_n_ocl_OCL_SetType, atl_n_ocl_OCL_OclAnyType, atl_n_ocl_OCL_TupleType, atl_n_ocl_OCL_VariableDeclaration, atl_n_ocl_OCL_Iterator, atl_n_ocl_OCL_Parameter, atl_n_ocl_OCL_CollectionType, atl_n_ocl_OCL_OclType, atl_n_ocl_OCL_Primitive, atl_n_ocl_OCL_StringType, Primitive, atl_n_ocl_OCL_Attribute, atl_n_ocl_OCL_Operation, TupleTypeAttribute, atl_n_ocl_OCL_TupleTypeAttribute, atl_n_ocl_OCL_OclModelElement, atl_n_ocl_OCL_MapType, atl_n_ocl_OCL_OclFeatureDefinition, OclFeature, OclContextDefinition, atl_n_ocl_OCL_OclContextDefinition, atl_n_ocl_OCL_OclFeature, atl_n_ocl_OCL_OclModel, OclModelElement},
    associations={body0, inPattern15, children16, helpers1, inModels3, outModels4, elements7, definition9, outPattern10, actionBlock11, variables13, sourceElement30, bindings32, model34, reverseBindings37, parameters18, elements19, filter20, dropPattern23, elements24, outPattern26, models28, value50, condition53, thenStatements55, elseStatements58, collection39, iterator41, value43, statements45, expression46, source48, referredVariable70, iterator61, collection63, statements66, type69, elements71, source81, tuplePart73, tuple74, elements75, key76, value78, in_94, thenExpression97, condition99, arguments83, body85, iterators87, result90, variable92, elseExpression102, type105, initExpression107, elementType110, initExpression125, type127, attributes112, type113, valueType115, keyType117, feature120, context_121, context_123, parameters130, returnType132, body135, metamodel138, elements140, model142},
    generalizations={gen_atl_n_ocl_ATL_MatchedRule_Rule, gen_atl_n_ocl_ATL_LazyMatchedRule_MatchedRule, gen_atl_n_ocl_ATL_Helper_ModuleElement, gen_atl_n_ocl_ATL_Rule_ModuleElement, gen_atl_n_ocl_ATL_SimpleInPatternElement_InPatternElement, gen_atl_n_ocl_ATL_OutPatternElement_PatternElement, gen_atl_n_ocl_ATL_SimpleOutPatternElement_OutPatternElement, gen_atl_n_ocl_ATL_CalledRule_Rule, gen_atl_n_ocl_ATL_PatternElement_VariableDeclaration, gen_atl_n_ocl_ATL_InPatternElement_PatternElement, gen_atl_n_ocl_ATL_IfStat_Statement, gen_atl_n_ocl_ATL_ForEachOutPatternElement_OutPatternElement, gen_atl_n_ocl_ATL_RuleVariableDeclaration_VariableDeclaration, gen_atl_n_ocl_ATL_ExpressionStat_Statement, gen_atl_n_ocl_ATL_BindingStat_Statement, gen_atl_n_ocl_OCL_VariableExp_OclExpression, gen_atl_n_ocl_ATL_ForStat_Statement, gen_atl_n_ocl_OCL_SuperExp_OclExpression, gen_atl_n_ocl_OCL_PrimitiveExp_OclExpression, gen_atl_n_ocl_OCL_StringExp_PrimitiveExp, gen_atl_n_ocl_OCL_NumericExp_PrimitiveExp, gen_atl_n_ocl_OCL_RealExp_NumericExp, gen_atl_n_ocl_OCL_IntegerExp_NumericExp, gen_atl_n_ocl_OCL_CollectionExp_OclExpression, gen_atl_n_ocl_OCL_BooleanExp_PrimitiveExp, gen_atl_n_ocl_OCL_OclUndefinedExp_OclExpression, gen_atl_n_ocl_OCL_PropertyCallExp_OclExpression, gen_atl_n_ocl_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_atl_n_ocl_OCL_OperationCallExp_PropertyCallExp, gen_atl_n_ocl_OCL_BagExp_CollectionExp, gen_atl_n_ocl_OCL_OrderedSetExp_CollectionExp, gen_atl_n_ocl_OCL_SequenceExp_CollectionExp, gen_atl_n_ocl_OCL_SetExp_CollectionExp, gen_atl_n_ocl_OCL_TupleExp_OclExpression, gen_atl_n_ocl_OCL_TuplePart_VariableDeclaration, gen_atl_n_ocl_OCL_MapExp_OclExpression, gen_atl_n_ocl_OCL_EnumLiteralExp_OclExpression, gen_atl_n_ocl_OCL_IfExp_OclExpression, gen_atl_n_ocl_OCL_OperatorCallExp_OperationCallExp, gen_atl_n_ocl_OCL_CollectionOperationCallExp_OperationCallExp, gen_atl_n_ocl_OCL_LoopExp_PropertyCallExp, gen_atl_n_ocl_OCL_IterateExp_LoopExp, gen_atl_n_ocl_OCL_IteratorExp_LoopExp, gen_atl_n_ocl_OCL_LetExp_OclExpression, gen_atl_n_ocl_OCL_BooleanType_Primitive, gen_atl_n_ocl_OCL_NumericType_Primitive, gen_atl_n_ocl_OCL_IntegerType_NumericType, gen_atl_n_ocl_OCL_RealType_NumericType, gen_atl_n_ocl_OCL_BagType_CollectionType, gen_atl_n_ocl_OCL_OrderedSetType_CollectionType, gen_atl_n_ocl_OCL_SequenceType_CollectionType, gen_atl_n_ocl_OCL_SetType_CollectionType, gen_atl_n_ocl_OCL_OclAnyType_OclType, gen_atl_n_ocl_OCL_TupleType_OclType, gen_atl_n_ocl_OCL_Iterator_VariableDeclaration, gen_atl_n_ocl_OCL_Parameter_VariableDeclaration, gen_atl_n_ocl_OCL_CollectionType_OclType, gen_atl_n_ocl_OCL_OclType_OclExpression, gen_atl_n_ocl_OCL_Primitive_OclType, gen_atl_n_ocl_OCL_StringType_Primitive, gen_atl_n_ocl_OCL_Attribute_OclFeature, gen_atl_n_ocl_OCL_Operation_OclFeature, gen_atl_n_ocl_OCL_OclModelElement_OclType, gen_atl_n_ocl_OCL_MapType_OclType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)