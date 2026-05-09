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
top_ATL_Unit = Class(name="top_ATL_Unit")
LocatedElement = Class(name="LocatedElement")
top_ATL_LocatedElement = Class(name="top_ATL_LocatedElement", is_abstract=True)
LibraryRef = Class(name="LibraryRef")
top_ATL_Library = Class(name="top_ATL_Library")
Unit = Class(name="Unit")
Helper = Class(name="Helper")
top_ATL_Query = Class(name="top_ATL_Query")
OclExpression = Class(name="OclExpression")
top_ATL_Module = Class(name="top_ATL_Module")
OclModel = Class(name="OclModel")
ModuleElement = Class(name="ModuleElement")
top_ATL_ModuleElement = Class(name="top_ATL_ModuleElement", is_abstract=True)
Module = Class(name="Module")
top_ATL_Helper = Class(name="top_ATL_Helper")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
top_ATL_Rule = Class(name="top_ATL_Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
top_ATL_MatchedRule = Class(name="top_ATL_MatchedRule")
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
MatchedRule = Class(name="MatchedRule")
top_ATL_LazyMatchedRule = Class(name="top_ATL_LazyMatchedRule")
top_ATL_CalledRule = Class(name="top_ATL_CalledRule")
Parameter_ = Class(name="Parameter")
top_ATL_InPattern = Class(name="top_ATL_InPattern")
InPatternElement = Class(name="InPatternElement")
top_ATL_OutPattern = Class(name="top_ATL_OutPattern")
DropPattern = Class(name="DropPattern")
OutPatternElement = Class(name="OutPatternElement")
top_ATL_DropPattern = Class(name="top_ATL_DropPattern")
top_ATL_PatternElement = Class(name="top_ATL_PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
top_ATL_InPatternElement = Class(name="top_ATL_InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
top_ATL_LibraryRef = Class(name="top_ATL_LibraryRef")
top_ATL_SimpleInPatternElement = Class(name="top_ATL_SimpleInPatternElement")
top_ATL_OutPatternElement = Class(name="top_ATL_OutPatternElement", is_abstract=True)
Binding = Class(name="Binding")
top_ATL_SimpleOutPatternElement = Class(name="top_ATL_SimpleOutPatternElement")
top_ATL_ForEachOutPatternElement = Class(name="top_ATL_ForEachOutPatternElement")
Iterator = Class(name="Iterator")
top_ATL_Binding = Class(name="top_ATL_Binding")
top_ATL_RuleVariableDeclaration = Class(name="top_ATL_RuleVariableDeclaration")
top_ATL_ForStat = Class(name="top_ATL_ForStat")
top_ATL_ActionBlock = Class(name="top_ATL_ActionBlock")
Statement = Class(name="Statement")
top_ATL_Statement = Class(name="top_ATL_Statement", is_abstract=True)
top_ATL_ExpressionStat = Class(name="top_ATL_ExpressionStat")
top_ATL_BindingStat = Class(name="top_ATL_BindingStat")
top_ATL_IfStat = Class(name="top_ATL_IfStat")
top_OCL_VariableExp = Class(name="top_OCL_VariableExp")
top_OCL_OclExpression = Class(name="top_OCL_OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
TupleExp = Class(name="TupleExp")
top_OCL_MapExp = Class(name="top_OCL_MapExp")
top_OCL_SuperExp = Class(name="top_OCL_SuperExp")
top_OCL_PrimitiveExp = Class(name="top_OCL_PrimitiveExp", is_abstract=True)
top_OCL_StringExp = Class(name="top_OCL_StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
top_OCL_BooleanExp = Class(name="top_OCL_BooleanExp")
top_OCL_NumericExp = Class(name="top_OCL_NumericExp", is_abstract=True)
top_OCL_RealExp = Class(name="top_OCL_RealExp")
NumericExp = Class(name="NumericExp")
top_OCL_IntegerExp = Class(name="top_OCL_IntegerExp")
top_OCL_CollectionExp = Class(name="top_OCL_CollectionExp", is_abstract=True)
top_OCL_BagExp = Class(name="top_OCL_BagExp")
top_OCL_OrderedSetExp = Class(name="top_OCL_OrderedSetExp")
top_OCL_SequenceExp = Class(name="top_OCL_SequenceExp")
top_OCL_SetExp = Class(name="top_OCL_SetExp")
top_OCL_TupleExp = Class(name="top_OCL_TupleExp")
TuplePart = Class(name="TuplePart")
top_OCL_TuplePart = Class(name="top_OCL_TuplePart")
MapElement = Class(name="MapElement")
top_OCL_MapElement = Class(name="top_OCL_MapElement")
MapExp = Class(name="MapExp")
top_OCL_EnumLiteralExp = Class(name="top_OCL_EnumLiteralExp")
top_OCL_OclUndefinedExp = Class(name="top_OCL_OclUndefinedExp")
top_OCL_PropertyCallExp = Class(name="top_OCL_PropertyCallExp", is_abstract=True)
top_OCL_NavigationOrAttributeCallExp = Class(name="top_OCL_NavigationOrAttributeCallExp")
top_OCL_OperationCallExp = Class(name="top_OCL_OperationCallExp")
top_OCL_OperatorCallExp = Class(name="top_OCL_OperatorCallExp")
top_OCL_CollectionOperationCallExp = Class(name="top_OCL_CollectionOperationCallExp")
top_OCL_LoopExp = Class(name="top_OCL_LoopExp", is_abstract=True)
top_OCL_IterateExp = Class(name="top_OCL_IterateExp")
top_OCL_IteratorExp = Class(name="top_OCL_IteratorExp")
top_OCL_LetExp = Class(name="top_OCL_LetExp")
top_OCL_IfExp = Class(name="top_OCL_IfExp")
top_OCL_VariableDeclaration = Class(name="top_OCL_VariableDeclaration")
top_OCL_Primitive = Class(name="top_OCL_Primitive", is_abstract=True)
top_OCL_StringType = Class(name="top_OCL_StringType")
Primitive = Class(name="Primitive")
top_OCL_BooleanType = Class(name="top_OCL_BooleanType")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
top_OCL_Iterator = Class(name="top_OCL_Iterator")
top_OCL_Parameter = Class(name="top_OCL_Parameter")
top_OCL_CollectionType = Class(name="top_OCL_CollectionType")
top_OCL_OclType = Class(name="top_OCL_OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
top_OCL_OclFeature = Class(name="top_OCL_OclFeature", is_abstract=True)
top_OCL_NumericType = Class(name="top_OCL_NumericType", is_abstract=True)
top_OCL_IntegerType = Class(name="top_OCL_IntegerType")
NumericType = Class(name="NumericType")
top_OCL_RealType = Class(name="top_OCL_RealType")
top_OCL_BagType = Class(name="top_OCL_BagType")
top_OCL_OrderedSetType = Class(name="top_OCL_OrderedSetType")
top_OCL_SequenceType = Class(name="top_OCL_SequenceType")
top_OCL_SetType = Class(name="top_OCL_SetType")
top_OCL_OclAnyType = Class(name="top_OCL_OclAnyType")
top_OCL_TupleType = Class(name="top_OCL_TupleType")
top_OCL_TupleTypeAttribute = Class(name="top_OCL_TupleTypeAttribute")
TupleType = Class(name="TupleType")
top_OCL_OclModelElement = Class(name="top_OCL_OclModelElement")
top_OCL_MapType = Class(name="top_OCL_MapType")
top_OCL_OclFeatureDefinition = Class(name="top_OCL_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
top_OCL_OclContextDefinition = Class(name="top_OCL_OclContextDefinition")
top_OCL_Attribute = Class(name="top_OCL_Attribute")
top_OCL_Operation = Class(name="top_OCL_Operation")
top_OCL_OclModel = Class(name="top_OCL_OclModel")
OclModelElement = Class(name="OclModelElement")

# top_ATL_Unit class attributes and methods
top_ATL_Unit_name: Property = Property(name="name", type=StringType)
top_ATL_Unit.attributes={top_ATL_Unit_name}

# LocatedElement class attributes and methods

# top_ATL_LocatedElement class attributes and methods
top_ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
top_ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
top_ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
top_ATL_LocatedElement.attributes={top_ATL_LocatedElement_commentsAfter, top_ATL_LocatedElement_location, top_ATL_LocatedElement_commentsBefore}

# LibraryRef class attributes and methods

# top_ATL_Library class attributes and methods

# Unit class attributes and methods

# Helper class attributes and methods

# top_ATL_Query class attributes and methods

# OclExpression class attributes and methods

# top_ATL_Module class attributes and methods
top_ATL_Module_isRefining: Property = Property(name="isRefining", type=StringType)
top_ATL_Module.attributes={top_ATL_Module_isRefining}

# OclModel class attributes and methods

# ModuleElement class attributes and methods

# top_ATL_ModuleElement class attributes and methods

# Module class attributes and methods

# top_ATL_Helper class attributes and methods

# Query class attributes and methods

# Library class attributes and methods

# OclFeatureDefinition class attributes and methods

# top_ATL_Rule class attributes and methods
top_ATL_Rule_name: Property = Property(name="name", type=StringType)
top_ATL_Rule.attributes={top_ATL_Rule_name}

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# top_ATL_MatchedRule class attributes and methods
top_ATL_MatchedRule_isAbstract: Property = Property(name="isAbstract", type=StringType)
top_ATL_MatchedRule_isRefining: Property = Property(name="isRefining", type=StringType)
top_ATL_MatchedRule_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
top_ATL_MatchedRule.attributes={top_ATL_MatchedRule_isAbstract, top_ATL_MatchedRule_isRefining, top_ATL_MatchedRule_isNoDefault}

# Rule class attributes and methods

# InPattern class attributes and methods

# MatchedRule class attributes and methods

# top_ATL_LazyMatchedRule class attributes and methods
top_ATL_LazyMatchedRule_isUnique: Property = Property(name="isUnique", type=StringType)
top_ATL_LazyMatchedRule.attributes={top_ATL_LazyMatchedRule_isUnique}

# top_ATL_CalledRule class attributes and methods
top_ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
top_ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
top_ATL_CalledRule.attributes={top_ATL_CalledRule_isEntrypoint, top_ATL_CalledRule_isEndpoint}

# Parameter class attributes and methods

# top_ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# top_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# OutPatternElement class attributes and methods

# top_ATL_DropPattern class attributes and methods

# top_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# top_ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# top_ATL_LibraryRef class attributes and methods
top_ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
top_ATL_LibraryRef.attributes={top_ATL_LibraryRef_name}

# top_ATL_SimpleInPatternElement class attributes and methods

# top_ATL_OutPatternElement class attributes and methods

# Binding class attributes and methods

# top_ATL_SimpleOutPatternElement class attributes and methods

# top_ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# top_ATL_Binding class attributes and methods
top_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
top_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
top_ATL_Binding.attributes={top_ATL_Binding_isAssignment, top_ATL_Binding_propertyName}

# top_ATL_RuleVariableDeclaration class attributes and methods

# top_ATL_ForStat class attributes and methods

# top_ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# top_ATL_Statement class attributes and methods

# top_ATL_ExpressionStat class attributes and methods

# top_ATL_BindingStat class attributes and methods
top_ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
top_ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
top_ATL_BindingStat.attributes={top_ATL_BindingStat_isAssignment, top_ATL_BindingStat_propertyName}

# top_ATL_IfStat class attributes and methods

# top_OCL_VariableExp class attributes and methods

# top_OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# TupleExp class attributes and methods

# top_OCL_MapExp class attributes and methods

# top_OCL_SuperExp class attributes and methods

# top_OCL_PrimitiveExp class attributes and methods

# top_OCL_StringExp class attributes and methods
top_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
top_OCL_StringExp.attributes={top_OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# top_OCL_BooleanExp class attributes and methods
top_OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
top_OCL_BooleanExp.attributes={top_OCL_BooleanExp_booleanSymbol}

# top_OCL_NumericExp class attributes and methods

# top_OCL_RealExp class attributes and methods
top_OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
top_OCL_RealExp.attributes={top_OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# top_OCL_IntegerExp class attributes and methods
top_OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
top_OCL_IntegerExp.attributes={top_OCL_IntegerExp_integerSymbol}

# top_OCL_CollectionExp class attributes and methods

# top_OCL_BagExp class attributes and methods

# top_OCL_OrderedSetExp class attributes and methods

# top_OCL_SequenceExp class attributes and methods

# top_OCL_SetExp class attributes and methods

# top_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# top_OCL_TuplePart class attributes and methods

# MapElement class attributes and methods

# top_OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# top_OCL_EnumLiteralExp class attributes and methods
top_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
top_OCL_EnumLiteralExp.attributes={top_OCL_EnumLiteralExp_name}

# top_OCL_OclUndefinedExp class attributes and methods

# top_OCL_PropertyCallExp class attributes and methods

# top_OCL_NavigationOrAttributeCallExp class attributes and methods
top_OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
top_OCL_NavigationOrAttributeCallExp.attributes={top_OCL_NavigationOrAttributeCallExp_name}

# top_OCL_OperationCallExp class attributes and methods
top_OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
top_OCL_OperationCallExp.attributes={top_OCL_OperationCallExp_operationName}

# top_OCL_OperatorCallExp class attributes and methods

# top_OCL_CollectionOperationCallExp class attributes and methods

# top_OCL_LoopExp class attributes and methods

# top_OCL_IterateExp class attributes and methods

# top_OCL_IteratorExp class attributes and methods
top_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
top_OCL_IteratorExp.attributes={top_OCL_IteratorExp_name}

# top_OCL_LetExp class attributes and methods

# top_OCL_IfExp class attributes and methods

# top_OCL_VariableDeclaration class attributes and methods
top_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
top_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
top_OCL_VariableDeclaration.attributes={top_OCL_VariableDeclaration_id, top_OCL_VariableDeclaration_varName}

# top_OCL_Primitive class attributes and methods

# top_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# top_OCL_BooleanType class attributes and methods

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# top_OCL_Iterator class attributes and methods

# top_OCL_Parameter class attributes and methods

# top_OCL_CollectionType class attributes and methods

# top_OCL_OclType class attributes and methods
top_OCL_OclType_name: Property = Property(name="name", type=StringType)
top_OCL_OclType.attributes={top_OCL_OclType_name}

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# TupleTypeAttribute class attributes and methods

# top_OCL_OclFeature class attributes and methods

# top_OCL_NumericType class attributes and methods

# top_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# top_OCL_RealType class attributes and methods

# top_OCL_BagType class attributes and methods

# top_OCL_OrderedSetType class attributes and methods

# top_OCL_SequenceType class attributes and methods

# top_OCL_SetType class attributes and methods

# top_OCL_OclAnyType class attributes and methods

# top_OCL_TupleType class attributes and methods

# top_OCL_TupleTypeAttribute class attributes and methods
top_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
top_OCL_TupleTypeAttribute.attributes={top_OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# top_OCL_OclModelElement class attributes and methods

# top_OCL_MapType class attributes and methods

# top_OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# top_OCL_OclContextDefinition class attributes and methods

# top_OCL_Attribute class attributes and methods
top_OCL_Attribute_name: Property = Property(name="name", type=StringType)
top_OCL_Attribute.attributes={top_OCL_Attribute_name}

# top_OCL_Operation class attributes and methods
top_OCL_Operation_name: Property = Property(name="name", type=StringType)
top_OCL_Operation.attributes={top_OCL_Operation_name}

# top_OCL_OclModel class attributes and methods
top_OCL_OclModel_name: Property = Property(name="name", type=StringType)
top_OCL_OclModel.attributes={top_OCL_OclModel_name}

# OclModelElement class attributes and methods

# Relationships
libraries0: BinaryAssociation = BinaryAssociation(
    name="libraries0",
    ends={
        Property(name="LibraryRef", type=top_ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="unit", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers1: BinaryAssociation = BinaryAssociation(
    name="helpers1",
    ends={
        Property(name="Helper", type=top_ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body2: BinaryAssociation = BinaryAssociation(
    name="body2",
    ends={
        Property(name="OclExpression", type=top_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
helpers3: BinaryAssociation = BinaryAssociation(
    name="helpers3",
    ends={
        Property(name="Helper4", type=top_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="query", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inModels5: BinaryAssociation = BinaryAssociation(
    name="inModels5",
    ends={
        Property(name="OclModel", type=top_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outModels6: BinaryAssociation = BinaryAssociation(
    name="outModels6",
    ends={
        Property(name="OclModel8", type=top_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_Module7", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements9: BinaryAssociation = BinaryAssociation(
    name="elements9",
    ends={
        Property(name="ModuleElement", type=top_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module10: BinaryAssociation = BinaryAssociation(
    name="module10",
    ends={
        Property(name="Module", type=top_ATL_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
superRule23: BinaryAssociation = BinaryAssociation(
    name="superRule23",
    ends={
        Property(name="MatchedRule24", type=top_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=MatchedRule, multiplicity=Multiplicity(0, 1))
    }
)
query11: BinaryAssociation = BinaryAssociation(
    name="query11",
    ends={
        Property(name="Query", type=top_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
library12: BinaryAssociation = BinaryAssociation(
    name="library12",
    ends={
        Property(name="Library", type=top_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers13", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
definition14: BinaryAssociation = BinaryAssociation(
    name="definition14",
    ends={
        Property(name="OclFeatureDefinition", type=top_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPattern15: BinaryAssociation = BinaryAssociation(
    name="outPattern15",
    ends={
        Property(name="OutPattern", type=top_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock16: BinaryAssociation = BinaryAssociation(
    name="actionBlock16",
    ends={
        Property(name="ActionBlock", type=top_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule17", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables18: BinaryAssociation = BinaryAssociation(
    name="variables18",
    ends={
        Property(name="RuleVariableDeclaration", type=top_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule19", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern20: BinaryAssociation = BinaryAssociation(
    name="inPattern20",
    ends={
        Property(name="InPattern", type=top_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule21", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children22: BinaryAssociation = BinaryAssociation(
    name="children22",
    ends={
        Property(name="MatchedRule", type=top_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="superRule", type=MatchedRule, multiplicity=Multiplicity(0, 9999))
    }
)
mapsTo39: BinaryAssociation = BinaryAssociation(
    name="mapsTo39",
    ends={
        Property(name="OutPatternElement40", type=top_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceElement", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
inPattern41: BinaryAssociation = BinaryAssociation(
    name="inPattern41",
    ends={
        Property(name="InPattern43", type=top_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements42", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
parameters25: BinaryAssociation = BinaryAssociation(
    name="parameters25",
    ends={
        Property(name="Parameter", type=top_ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements26: BinaryAssociation = BinaryAssociation(
    name="elements26",
    ends={
        Property(name="InPatternElement", type=top_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="inPattern", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rule27: BinaryAssociation = BinaryAssociation(
    name="rule27",
    ends={
        Property(name="MatchedRule29", type=top_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="inPattern28", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
filter30: BinaryAssociation = BinaryAssociation(
    name="filter30",
    ends={
        Property(name="OclExpression31", type=top_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule32: BinaryAssociation = BinaryAssociation(
    name="rule32",
    ends={
        Property(name="Rule", type=top_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern33: BinaryAssociation = BinaryAssociation(
    name="dropPattern33",
    ends={
        Property(name="DropPattern", type=top_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern34", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements35: BinaryAssociation = BinaryAssociation(
    name="elements35",
    ends={
        Property(name="OutPatternElement", type=top_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern36", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern37: BinaryAssociation = BinaryAssociation(
    name="outPattern37",
    ends={
        Property(name="OutPattern38", type=top_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dropPattern", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
rule64: BinaryAssociation = BinaryAssociation(
    name="rule64",
    ends={
        Property(name="Rule65", type=top_ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
models44: BinaryAssociation = BinaryAssociation(
    name="models44",
    ends={
        Property(name="OclModel45", type=top_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern46: BinaryAssociation = BinaryAssociation(
    name="outPattern46",
    ends={
        Property(name="OutPattern48", type=top_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements47", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
sourceElement49: BinaryAssociation = BinaryAssociation(
    name="sourceElement49",
    ends={
        Property(name="InPatternElement50", type=top_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsTo", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings51: BinaryAssociation = BinaryAssociation(
    name="bindings51",
    ends={
        Property(name="Binding", type=top_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="outPatternElement", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model52: BinaryAssociation = BinaryAssociation(
    name="model52",
    ends={
        Property(name="OclModel53", type=top_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings54: BinaryAssociation = BinaryAssociation(
    name="reverseBindings54",
    ends={
        Property(name="OclExpression55", type=top_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection56: BinaryAssociation = BinaryAssociation(
    name="collection56",
    ends={
        Property(name="OclExpression57", type=top_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator58: BinaryAssociation = BinaryAssociation(
    name="iterator58",
    ends={
        Property(name="Iterator", type=top_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ForEachOutPatternElement59", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value60: BinaryAssociation = BinaryAssociation(
    name="value60",
    ends={
        Property(name="OclExpression61", type=top_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement62: BinaryAssociation = BinaryAssociation(
    name="outPatternElement62",
    ends={
        Property(name="OutPatternElement63", type=top_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="bindings", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
elseStatements82: BinaryAssociation = BinaryAssociation(
    name="elseStatements82",
    ends={
        Property(name="Statement84", type=top_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_IfStat83", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit66: BinaryAssociation = BinaryAssociation(
    name="unit66",
    ends={
        Property(name="Unit", type=top_ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="libraries", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
rule67: BinaryAssociation = BinaryAssociation(
    name="rule67",
    ends={
        Property(name="Rule68", type=top_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="actionBlock", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements69: BinaryAssociation = BinaryAssociation(
    name="statements69",
    ends={
        Property(name="Statement", type=top_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression70: BinaryAssociation = BinaryAssociation(
    name="expression70",
    ends={
        Property(name="OclExpression71", type=top_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source72: BinaryAssociation = BinaryAssociation(
    name="source72",
    ends={
        Property(name="OclExpression73", type=top_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value74: BinaryAssociation = BinaryAssociation(
    name="value74",
    ends={
        Property(name="OclExpression76", type=top_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_BindingStat75", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition77: BinaryAssociation = BinaryAssociation(
    name="condition77",
    ends={
        Property(name="OclExpression78", type=top_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements79: BinaryAssociation = BinaryAssociation(
    name="thenStatements79",
    ends={
        Property(name="Statement81", type=top_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_IfStat80", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningAttribute108: BinaryAssociation = BinaryAssociation(
    name="owningAttribute108",
    ends={
        Property(name="initExpression109", type=Attribute, multiplicity=Multiplicity(0, 1)),
        Property(name="Attribute", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1))
    }
)
iterator85: BinaryAssociation = BinaryAssociation(
    name="iterator85",
    ends={
        Property(name="Iterator86", type=top_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection87: BinaryAssociation = BinaryAssociation(
    name="collection87",
    ends={
        Property(name="OclExpression89", type=top_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ForStat88", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements90: BinaryAssociation = BinaryAssociation(
    name="statements90",
    ends={
        Property(name="Statement92", type=top_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="top_ATL_ForStat91", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type93: BinaryAssociation = BinaryAssociation(
    name="type93",
    ends={
        Property(name="OclType", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp394: BinaryAssociation = BinaryAssociation(
    name="ifExp394",
    ends={
        Property(name="IfExp", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty95: BinaryAssociation = BinaryAssociation(
    name="appliedProperty95",
    ends={
        Property(name="PropertyCallExp", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection96: BinaryAssociation = BinaryAssociation(
    name="collection96",
    ends={
        Property(name="CollectionExp", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements97", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp98: BinaryAssociation = BinaryAssociation(
    name="letExp98",
    ends={
        Property(name="LetExp", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp99: BinaryAssociation = BinaryAssociation(
    name="loopExp99",
    ends={
        Property(name="LoopExp", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation100: BinaryAssociation = BinaryAssociation(
    name="parentOperation100",
    ends={
        Property(name="OperationCallExp", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable101: BinaryAssociation = BinaryAssociation(
    name="initializedVariable101",
    ends={
        Property(name="VariableDeclaration", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2102: BinaryAssociation = BinaryAssociation(
    name="ifExp2102",
    ends={
        Property(name="IfExp103", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation104: BinaryAssociation = BinaryAssociation(
    name="owningOperation104",
    ends={
        Property(name="Operation", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body105", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1106: BinaryAssociation = BinaryAssociation(
    name="ifExp1106",
    ends={
        Property(name="IfExp107", type=top_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
tuple115: BinaryAssociation = BinaryAssociation(
    name="tuple115",
    ends={
        Property(name="TupleExp", type=top_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
referredVariable110: BinaryAssociation = BinaryAssociation(
    name="referredVariable110",
    ends={
        Property(name="VariableDeclaration111", type=top_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elements112: BinaryAssociation = BinaryAssociation(
    name="elements112",
    ends={
        Property(name="OclExpression113", type=top_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart114: BinaryAssociation = BinaryAssociation(
    name="tuplePart114",
    ends={
        Property(name="TuplePart", type=top_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable134: BinaryAssociation = BinaryAssociation(
    name="variable134",
    ends={
        Property(name="VariableDeclaration135", type=top_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements116: BinaryAssociation = BinaryAssociation(
    name="elements116",
    ends={
        Property(name="MapElement", type=top_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map117: BinaryAssociation = BinaryAssociation(
    name="map117",
    ends={
        Property(name="MapExp", type=top_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements118", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key119: BinaryAssociation = BinaryAssociation(
    name="key119",
    ends={
        Property(name="OclExpression120", type=top_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value121: BinaryAssociation = BinaryAssociation(
    name="value121",
    ends={
        Property(name="OclExpression123", type=top_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="top_OCL_MapElement122", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source124: BinaryAssociation = BinaryAssociation(
    name="source124",
    ends={
        Property(name="OclExpression125", type=top_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments126: BinaryAssociation = BinaryAssociation(
    name="arguments126",
    ends={
        Property(name="OclExpression127", type=top_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body128: BinaryAssociation = BinaryAssociation(
    name="body128",
    ends={
        Property(name="OclExpression129", type=top_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators130: BinaryAssociation = BinaryAssociation(
    name="iterators130",
    ends={
        Property(name="Iterator131", type=top_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result132: BinaryAssociation = BinaryAssociation(
    name="result132",
    ends={
        Property(name="VariableDeclaration133", type=top_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression147: BinaryAssociation = BinaryAssociation(
    name="initExpression147",
    ends={
        Property(name="OclExpression148", type=top_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in_136: BinaryAssociation = BinaryAssociation(
    name="in_136",
    ends={
        Property(name="OclExpression138", type=top_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp137", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression139: BinaryAssociation = BinaryAssociation(
    name="thenExpression139",
    ends={
        Property(name="OclExpression140", type=top_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition141: BinaryAssociation = BinaryAssociation(
    name="condition141",
    ends={
        Property(name="OclExpression142", type=top_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression143: BinaryAssociation = BinaryAssociation(
    name="elseExpression143",
    ends={
        Property(name="OclExpression144", type=top_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type145: BinaryAssociation = BinaryAssociation(
    name="type145",
    ends={
        Property(name="OclType146", type=top_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp149: BinaryAssociation = BinaryAssociation(
    name="letExp149",
    ends={
        Property(name="LetExp150", type=top_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp151: BinaryAssociation = BinaryAssociation(
    name="baseExp151",
    ends={
        Property(name="IterateExp", type=top_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp152: BinaryAssociation = BinaryAssociation(
    name="variableExp152",
    ends={
        Property(name="VariableExp", type=top_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr153: BinaryAssociation = BinaryAssociation(
    name="loopExpr153",
    ends={
        Property(name="LoopExp154", type=top_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation155: BinaryAssociation = BinaryAssociation(
    name="operation155",
    ends={
        Property(name="Operation156", type=top_OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
elementType157: BinaryAssociation = BinaryAssociation(
    name="elementType157",
    ends={
        Property(name="OclType158", type=top_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions159: BinaryAssociation = BinaryAssociation(
    name="definitions159",
    ends={
        Property(name="OclContextDefinition", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression160: BinaryAssociation = BinaryAssociation(
    name="oclExpression160",
    ends={
        Property(name="OclExpression161", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation162: BinaryAssociation = BinaryAssociation(
    name="operation162",
    ends={
        Property(name="Operation163", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2164: BinaryAssociation = BinaryAssociation(
    name="mapType2164",
    ends={
        Property(name="MapType", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute165: BinaryAssociation = BinaryAssociation(
    name="attribute165",
    ends={
        Property(name="Attribute167", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type166", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType168: BinaryAssociation = BinaryAssociation(
    name="mapType168",
    ends={
        Property(name="MapType169", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes170: BinaryAssociation = BinaryAssociation(
    name="collectionTypes170",
    ends={
        Property(name="CollectionType", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute171: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute171",
    ends={
        Property(name="TupleTypeAttribute", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type172", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration173: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration173",
    ends={
        Property(name="VariableDeclaration175", type=top_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type174", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
context_195: BinaryAssociation = BinaryAssociation(
    name="context_195",
    ends={
        Property(name="OclType196", type=top_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes176: BinaryAssociation = BinaryAssociation(
    name="attributes176",
    ends={
        Property(name="TupleTypeAttribute177", type=top_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type178: BinaryAssociation = BinaryAssociation(
    name="type178",
    ends={
        Property(name="OclType179", type=top_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType180: BinaryAssociation = BinaryAssociation(
    name="tupleType180",
    ends={
        Property(name="TupleType", type=top_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model181: BinaryAssociation = BinaryAssociation(
    name="model181",
    ends={
        Property(name="OclModel183", type=top_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements182", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType184: BinaryAssociation = BinaryAssociation(
    name="valueType184",
    ends={
        Property(name="OclType185", type=top_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType186: BinaryAssociation = BinaryAssociation(
    name="keyType186",
    ends={
        Property(name="OclType187", type=top_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature188: BinaryAssociation = BinaryAssociation(
    name="feature188",
    ends={
        Property(name="OclFeature", type=top_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_189: BinaryAssociation = BinaryAssociation(
    name="context_189",
    ends={
        Property(name="OclContextDefinition191", type=top_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition190", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition192: BinaryAssociation = BinaryAssociation(
    name="definition192",
    ends={
        Property(name="OclFeatureDefinition194", type=top_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_193", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
definition197: BinaryAssociation = BinaryAssociation(
    name="definition197",
    ends={
        Property(name="OclFeatureDefinition198", type=top_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression199: BinaryAssociation = BinaryAssociation(
    name="initExpression199",
    ends={
        Property(name="OclExpression200", type=top_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type201: BinaryAssociation = BinaryAssociation(
    name="type201",
    ends={
        Property(name="OclType202", type=top_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters203: BinaryAssociation = BinaryAssociation(
    name="parameters203",
    ends={
        Property(name="Parameter204", type=top_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType205: BinaryAssociation = BinaryAssociation(
    name="returnType205",
    ends={
        Property(name="OclType207", type=top_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation206", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body208: BinaryAssociation = BinaryAssociation(
    name="body208",
    ends={
        Property(name="OclExpression209", type=top_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel210: BinaryAssociation = BinaryAssociation(
    name="metamodel210",
    ends={
        Property(name="OclModel211", type=top_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements212: BinaryAssociation = BinaryAssociation(
    name="elements212",
    ends={
        Property(name="OclModelElement", type=top_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model213", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model214: BinaryAssociation = BinaryAssociation(
    name="model214",
    ends={
        Property(name="OclModel215", type=top_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_top_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_Unit)
gen_top_ATL_Library_Unit = Generalization(general=Unit, specific=top_ATL_Library)
gen_top_ATL_Query_Unit = Generalization(general=Unit, specific=top_ATL_Query)
gen_top_ATL_Module_Unit = Generalization(general=Unit, specific=top_ATL_Module)
gen_top_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_ModuleElement)
gen_top_ATL_Helper_ModuleElement = Generalization(general=ModuleElement, specific=top_ATL_Helper)
gen_top_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=top_ATL_Rule)
gen_top_ATL_MatchedRule_Rule = Generalization(general=Rule, specific=top_ATL_MatchedRule)
gen_top_ATL_LazyMatchedRule_MatchedRule = Generalization(general=MatchedRule, specific=top_ATL_LazyMatchedRule)
gen_top_ATL_CalledRule_Rule = Generalization(general=Rule, specific=top_ATL_CalledRule)
gen_top_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_InPattern)
gen_top_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_OutPattern)
gen_top_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_DropPattern)
gen_top_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=top_ATL_PatternElement)
gen_top_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=top_ATL_InPatternElement)
gen_top_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_LibraryRef)
gen_top_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=top_ATL_SimpleInPatternElement)
gen_top_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=top_ATL_OutPatternElement)
gen_top_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=top_ATL_SimpleOutPatternElement)
gen_top_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=top_ATL_ForEachOutPatternElement)
gen_top_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_Binding)
gen_top_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=top_ATL_RuleVariableDeclaration)
gen_top_ATL_ForStat_Statement = Generalization(general=Statement, specific=top_ATL_ForStat)
gen_top_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_ActionBlock)
gen_top_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=top_ATL_Statement)
gen_top_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=top_ATL_ExpressionStat)
gen_top_ATL_BindingStat_Statement = Generalization(general=Statement, specific=top_ATL_BindingStat)
gen_top_ATL_IfStat_Statement = Generalization(general=Statement, specific=top_ATL_IfStat)
gen_top_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_VariableExp)
gen_top_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_OclExpression)
gen_top_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_MapExp)
gen_top_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_SuperExp)
gen_top_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_PrimitiveExp)
gen_top_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=top_OCL_StringExp)
gen_top_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=top_OCL_BooleanExp)
gen_top_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=top_OCL_NumericExp)
gen_top_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=top_OCL_RealExp)
gen_top_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=top_OCL_IntegerExp)
gen_top_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_CollectionExp)
gen_top_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=top_OCL_BagExp)
gen_top_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=top_OCL_OrderedSetExp)
gen_top_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=top_OCL_SequenceExp)
gen_top_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=top_OCL_SetExp)
gen_top_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_TupleExp)
gen_top_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=top_OCL_TuplePart)
gen_top_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_MapElement)
gen_top_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_EnumLiteralExp)
gen_top_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_OclUndefinedExp)
gen_top_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_PropertyCallExp)
gen_top_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=top_OCL_NavigationOrAttributeCallExp)
gen_top_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=top_OCL_OperationCallExp)
gen_top_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=top_OCL_OperatorCallExp)
gen_top_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=top_OCL_CollectionOperationCallExp)
gen_top_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=top_OCL_LoopExp)
gen_top_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=top_OCL_IterateExp)
gen_top_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=top_OCL_IteratorExp)
gen_top_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_LetExp)
gen_top_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=top_OCL_IfExp)
gen_top_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_VariableDeclaration)
gen_top_OCL_Primitive_OclType = Generalization(general=OclType, specific=top_OCL_Primitive)
gen_top_OCL_StringType_Primitive = Generalization(general=Primitive, specific=top_OCL_StringType)
gen_top_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=top_OCL_Iterator)
gen_top_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=top_OCL_Parameter)
gen_top_OCL_CollectionType_OclType = Generalization(general=OclType, specific=top_OCL_CollectionType)
gen_top_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=top_OCL_OclType)
gen_top_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_OclFeature)
gen_top_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=top_OCL_BooleanType)
gen_top_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=top_OCL_NumericType)
gen_top_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=top_OCL_IntegerType)
gen_top_OCL_RealType_NumericType = Generalization(general=NumericType, specific=top_OCL_RealType)
gen_top_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=top_OCL_BagType)
gen_top_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=top_OCL_OrderedSetType)
gen_top_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=top_OCL_SequenceType)
gen_top_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=top_OCL_SetType)
gen_top_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=top_OCL_OclAnyType)
gen_top_OCL_TupleType_OclType = Generalization(general=OclType, specific=top_OCL_TupleType)
gen_top_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_TupleTypeAttribute)
gen_top_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=top_OCL_OclModelElement)
gen_top_OCL_MapType_OclType = Generalization(general=OclType, specific=top_OCL_MapType)
gen_top_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_OclFeatureDefinition)
gen_top_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_OclContextDefinition)
gen_top_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=top_OCL_Attribute)
gen_top_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=top_OCL_Operation)
gen_top_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=top_OCL_OclModel)

# Domain Model
domain_model = DomainModel(
    name="top",
    types={top_ATL_Unit, LocatedElement, top_ATL_LocatedElement, LibraryRef, top_ATL_Library, Unit, Helper, top_ATL_Query, OclExpression, top_ATL_Module, OclModel, ModuleElement, top_ATL_ModuleElement, Module, top_ATL_Helper, Query, Library, OclFeatureDefinition, top_ATL_Rule, OutPattern, ActionBlock, RuleVariableDeclaration, top_ATL_MatchedRule, Rule, InPattern, MatchedRule, top_ATL_LazyMatchedRule, top_ATL_CalledRule, Parameter_, top_ATL_InPattern, InPatternElement, top_ATL_OutPattern, DropPattern, OutPatternElement, top_ATL_DropPattern, top_ATL_PatternElement, VariableDeclaration, top_ATL_InPatternElement, PatternElement, top_ATL_LibraryRef, top_ATL_SimpleInPatternElement, top_ATL_OutPatternElement, Binding, top_ATL_SimpleOutPatternElement, top_ATL_ForEachOutPatternElement, Iterator, top_ATL_Binding, top_ATL_RuleVariableDeclaration, top_ATL_ForStat, top_ATL_ActionBlock, Statement, top_ATL_Statement, top_ATL_ExpressionStat, top_ATL_BindingStat, top_ATL_IfStat, top_OCL_VariableExp, top_OCL_OclExpression, OclType, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, Operation, Attribute, TupleExp, top_OCL_MapExp, top_OCL_SuperExp, top_OCL_PrimitiveExp, top_OCL_StringExp, PrimitiveExp, top_OCL_BooleanExp, top_OCL_NumericExp, top_OCL_RealExp, NumericExp, top_OCL_IntegerExp, top_OCL_CollectionExp, top_OCL_BagExp, top_OCL_OrderedSetExp, top_OCL_SequenceExp, top_OCL_SetExp, top_OCL_TupleExp, TuplePart, top_OCL_TuplePart, MapElement, top_OCL_MapElement, MapExp, top_OCL_EnumLiteralExp, top_OCL_OclUndefinedExp, top_OCL_PropertyCallExp, top_OCL_NavigationOrAttributeCallExp, top_OCL_OperationCallExp, top_OCL_OperatorCallExp, top_OCL_CollectionOperationCallExp, top_OCL_LoopExp, top_OCL_IterateExp, top_OCL_IteratorExp, top_OCL_LetExp, top_OCL_IfExp, top_OCL_VariableDeclaration, top_OCL_Primitive, top_OCL_StringType, Primitive, top_OCL_BooleanType, IterateExp, VariableExp, top_OCL_Iterator, top_OCL_Parameter, top_OCL_CollectionType, top_OCL_OclType, OclContextDefinition, MapType, CollectionType, TupleTypeAttribute, top_OCL_OclFeature, top_OCL_NumericType, top_OCL_IntegerType, NumericType, top_OCL_RealType, top_OCL_BagType, top_OCL_OrderedSetType, top_OCL_SequenceType, top_OCL_SetType, top_OCL_OclAnyType, top_OCL_TupleType, top_OCL_TupleTypeAttribute, TupleType, top_OCL_OclModelElement, top_OCL_MapType, top_OCL_OclFeatureDefinition, OclFeature, top_OCL_OclContextDefinition, top_OCL_Attribute, top_OCL_Operation, top_OCL_OclModel, OclModelElement},
    associations={libraries0, helpers1, body2, helpers3, inModels5, outModels6, elements9, module10, superRule23, query11, library12, definition14, outPattern15, actionBlock16, variables18, inPattern20, children22, mapsTo39, inPattern41, parameters25, elements26, rule27, filter30, rule32, dropPattern33, elements35, outPattern37, rule64, models44, outPattern46, sourceElement49, bindings51, model52, reverseBindings54, collection56, iterator58, value60, outPatternElement62, elseStatements82, unit66, rule67, statements69, expression70, source72, value74, condition77, thenStatements79, owningAttribute108, iterator85, collection87, statements90, type93, ifExp394, appliedProperty95, collection96, letExp98, loopExp99, parentOperation100, initializedVariable101, ifExp2102, owningOperation104, ifExp1106, tuple115, referredVariable110, elements112, tuplePart114, variable134, elements116, map117, key119, value121, source124, arguments126, body128, iterators130, result132, initExpression147, in_136, thenExpression139, condition141, elseExpression143, type145, letExp149, baseExp151, variableExp152, loopExpr153, operation155, elementType157, definitions159, oclExpression160, operation162, mapType2164, attribute165, mapType168, collectionTypes170, tupleTypeAttribute171, variableDeclaration173, context_195, attributes176, type178, tupleType180, model181, valueType184, keyType186, feature188, context_189, definition192, definition197, initExpression199, type201, parameters203, returnType205, body208, metamodel210, elements212, model214},
    generalizations={gen_top_ATL_Unit_LocatedElement, gen_top_ATL_Library_Unit, gen_top_ATL_Query_Unit, gen_top_ATL_Module_Unit, gen_top_ATL_ModuleElement_LocatedElement, gen_top_ATL_Helper_ModuleElement, gen_top_ATL_Rule_ModuleElement, gen_top_ATL_MatchedRule_Rule, gen_top_ATL_LazyMatchedRule_MatchedRule, gen_top_ATL_CalledRule_Rule, gen_top_ATL_InPattern_LocatedElement, gen_top_ATL_OutPattern_LocatedElement, gen_top_ATL_DropPattern_LocatedElement, gen_top_ATL_PatternElement_VariableDeclaration, gen_top_ATL_InPatternElement_PatternElement, gen_top_ATL_LibraryRef_LocatedElement, gen_top_ATL_SimpleInPatternElement_InPatternElement, gen_top_ATL_OutPatternElement_PatternElement, gen_top_ATL_SimpleOutPatternElement_OutPatternElement, gen_top_ATL_ForEachOutPatternElement_OutPatternElement, gen_top_ATL_Binding_LocatedElement, gen_top_ATL_RuleVariableDeclaration_VariableDeclaration, gen_top_ATL_ForStat_Statement, gen_top_ATL_ActionBlock_LocatedElement, gen_top_ATL_Statement_LocatedElement, gen_top_ATL_ExpressionStat_Statement, gen_top_ATL_BindingStat_Statement, gen_top_ATL_IfStat_Statement, gen_top_OCL_VariableExp_OclExpression, gen_top_OCL_OclExpression_LocatedElement, gen_top_OCL_MapExp_OclExpression, gen_top_OCL_SuperExp_OclExpression, gen_top_OCL_PrimitiveExp_OclExpression, gen_top_OCL_StringExp_PrimitiveExp, gen_top_OCL_BooleanExp_PrimitiveExp, gen_top_OCL_NumericExp_PrimitiveExp, gen_top_OCL_RealExp_NumericExp, gen_top_OCL_IntegerExp_NumericExp, gen_top_OCL_CollectionExp_OclExpression, gen_top_OCL_BagExp_CollectionExp, gen_top_OCL_OrderedSetExp_CollectionExp, gen_top_OCL_SequenceExp_CollectionExp, gen_top_OCL_SetExp_CollectionExp, gen_top_OCL_TupleExp_OclExpression, gen_top_OCL_TuplePart_VariableDeclaration, gen_top_OCL_MapElement_LocatedElement, gen_top_OCL_EnumLiteralExp_OclExpression, gen_top_OCL_OclUndefinedExp_OclExpression, gen_top_OCL_PropertyCallExp_OclExpression, gen_top_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_top_OCL_OperationCallExp_PropertyCallExp, gen_top_OCL_OperatorCallExp_OperationCallExp, gen_top_OCL_CollectionOperationCallExp_OperationCallExp, gen_top_OCL_LoopExp_PropertyCallExp, gen_top_OCL_IterateExp_LoopExp, gen_top_OCL_IteratorExp_LoopExp, gen_top_OCL_LetExp_OclExpression, gen_top_OCL_IfExp_OclExpression, gen_top_OCL_VariableDeclaration_LocatedElement, gen_top_OCL_Primitive_OclType, gen_top_OCL_StringType_Primitive, gen_top_OCL_Iterator_VariableDeclaration, gen_top_OCL_Parameter_VariableDeclaration, gen_top_OCL_CollectionType_OclType, gen_top_OCL_OclType_OclExpression, gen_top_OCL_OclFeature_LocatedElement, gen_top_OCL_BooleanType_Primitive, gen_top_OCL_NumericType_Primitive, gen_top_OCL_IntegerType_NumericType, gen_top_OCL_RealType_NumericType, gen_top_OCL_BagType_CollectionType, gen_top_OCL_OrderedSetType_CollectionType, gen_top_OCL_SequenceType_CollectionType, gen_top_OCL_SetType_CollectionType, gen_top_OCL_OclAnyType_OclType, gen_top_OCL_TupleType_OclType, gen_top_OCL_TupleTypeAttribute_LocatedElement, gen_top_OCL_OclModelElement_OclType, gen_top_OCL_MapType_OclType, gen_top_OCL_OclFeatureDefinition_LocatedElement, gen_top_OCL_OclContextDefinition_LocatedElement, gen_top_OCL_Attribute_OclFeature, gen_top_OCL_Operation_OclFeature, gen_top_OCL_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)