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
ModuleElement = Class(name="ModuleElement")
atlstatic_ATL_ModuleElement = Class(name="atlstatic_ATL_ModuleElement", is_abstract=True)
atlstatic_ATL_Helper = Class(name="atlstatic_ATL_Helper")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
atlstatic_ATL_Rule = Class(name="atlstatic_ATL_Rule", is_abstract=True)
atlstatic_ATL_LocatedElement = Class(name="atlstatic_ATL_LocatedElement", is_abstract=True)
atlstatic_ATL_Unit = Class(name="atlstatic_ATL_Unit")
LocatedElement = Class(name="LocatedElement")
LibraryRef = Class(name="LibraryRef")
atlstatic_ATL_Library = Class(name="atlstatic_ATL_Library")
Unit = Class(name="Unit")
Helper = Class(name="Helper")
atlstatic_ATL_Query = Class(name="atlstatic_ATL_Query")
OclExpression = Class(name="OclExpression")
atlstatic_ATL_Module = Class(name="atlstatic_ATL_Module")
OclModel = Class(name="OclModel")
atlstatic_ATL_OutPattern = Class(name="atlstatic_ATL_OutPattern")
DropPattern = Class(name="DropPattern")
OutPatternElement = Class(name="OutPatternElement")
atlstatic_ATL_DropPattern = Class(name="atlstatic_ATL_DropPattern")
atlstatic_ATL_PatternElement = Class(name="atlstatic_ATL_PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
atlstatic_ATL_InPatternElement = Class(name="atlstatic_ATL_InPatternElement", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
atlstatic_ATL_MatchedRule = Class(name="atlstatic_ATL_MatchedRule")
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
MatchedRule = Class(name="MatchedRule")
atlstatic_ATL_LazyMatchedRule = Class(name="atlstatic_ATL_LazyMatchedRule")
atlstatic_ATL_CalledRule = Class(name="atlstatic_ATL_CalledRule")
Parameter_ = Class(name="Parameter")
atlstatic_ATL_InPattern = Class(name="atlstatic_ATL_InPattern")
InPatternElement = Class(name="InPatternElement")
atlstatic_ATL_RuleVariableDeclaration = Class(name="atlstatic_ATL_RuleVariableDeclaration")
atlstatic_ATL_LibraryRef = Class(name="atlstatic_ATL_LibraryRef")
atlstatic_ATL_ActionBlock = Class(name="atlstatic_ATL_ActionBlock")
Statement = Class(name="Statement")
PatternElement = Class(name="PatternElement")
atlstatic_ATL_SimpleInPatternElement = Class(name="atlstatic_ATL_SimpleInPatternElement")
atlstatic_ATL_OutPatternElement = Class(name="atlstatic_ATL_OutPatternElement", is_abstract=True)
Binding = Class(name="Binding")
atlstatic_ATL_SimpleOutPatternElement = Class(name="atlstatic_ATL_SimpleOutPatternElement")
atlstatic_ATL_ForEachOutPatternElement = Class(name="atlstatic_ATL_ForEachOutPatternElement")
Iterator = Class(name="Iterator")
atlstatic_ATL_Binding = Class(name="atlstatic_ATL_Binding")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
atlstatic_ATL_Statement = Class(name="atlstatic_ATL_Statement", is_abstract=True)
atlstatic_ATL_ExpressionStat = Class(name="atlstatic_ATL_ExpressionStat")
atlstatic_ATL_BindingStat = Class(name="atlstatic_ATL_BindingStat")
atlstatic_ATL_IfStat = Class(name="atlstatic_ATL_IfStat")
atlstatic_ATL_ForStat = Class(name="atlstatic_ATL_ForStat")
atlstatic_OCL_OclExpression = Class(name="atlstatic_OCL_OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
TuplePart = Class(name="TuplePart")
atlstatic_OCL_TuplePart = Class(name="atlstatic_OCL_TuplePart")
TupleExp = Class(name="TupleExp")
atlstatic_OCL_MapExp = Class(name="atlstatic_OCL_MapExp")
MapElement = Class(name="MapElement")
atlstatic_OCL_MapElement = Class(name="atlstatic_OCL_MapElement")
MapExp = Class(name="MapExp")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
atlstatic_OCL_VariableExp = Class(name="atlstatic_OCL_VariableExp")
atlstatic_OCL_SuperExp = Class(name="atlstatic_OCL_SuperExp")
atlstatic_OCL_PrimitiveExp = Class(name="atlstatic_OCL_PrimitiveExp", is_abstract=True)
atlstatic_OCL_StringExp = Class(name="atlstatic_OCL_StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
atlstatic_OCL_BooleanExp = Class(name="atlstatic_OCL_BooleanExp")
atlstatic_OCL_NumericExp = Class(name="atlstatic_OCL_NumericExp", is_abstract=True)
atlstatic_OCL_RealExp = Class(name="atlstatic_OCL_RealExp")
NumericExp = Class(name="NumericExp")
atlstatic_OCL_IntegerExp = Class(name="atlstatic_OCL_IntegerExp")
atlstatic_OCL_CollectionExp = Class(name="atlstatic_OCL_CollectionExp", is_abstract=True)
atlstatic_OCL_BagExp = Class(name="atlstatic_OCL_BagExp")
atlstatic_OCL_OrderedSetExp = Class(name="atlstatic_OCL_OrderedSetExp")
atlstatic_OCL_SequenceExp = Class(name="atlstatic_OCL_SequenceExp")
atlstatic_OCL_SetExp = Class(name="atlstatic_OCL_SetExp")
atlstatic_OCL_TupleExp = Class(name="atlstatic_OCL_TupleExp")
atlstatic_OCL_NavigationOrAttributeCallExp = Class(name="atlstatic_OCL_NavigationOrAttributeCallExp")
atlstatic_OCL_OperationCallExp = Class(name="atlstatic_OCL_OperationCallExp")
atlstatic_OCL_OperatorCallExp = Class(name="atlstatic_OCL_OperatorCallExp")
atlstatic_OCL_CollectionOperationCallExp = Class(name="atlstatic_OCL_CollectionOperationCallExp")
atlstatic_OCL_LoopExp = Class(name="atlstatic_OCL_LoopExp", is_abstract=True)
atlstatic_OCL_EnumLiteralExp = Class(name="atlstatic_OCL_EnumLiteralExp")
atlstatic_OCL_OclUndefinedExp = Class(name="atlstatic_OCL_OclUndefinedExp")
atlstatic_OCL_PropertyCallExp = Class(name="atlstatic_OCL_PropertyCallExp", is_abstract=True)
atlstatic_OCL_VariableDeclaration = Class(name="atlstatic_OCL_VariableDeclaration")
atlstatic_OCL_IterateExp = Class(name="atlstatic_OCL_IterateExp")
atlstatic_OCL_IteratorExp = Class(name="atlstatic_OCL_IteratorExp")
atlstatic_OCL_LetExp = Class(name="atlstatic_OCL_LetExp")
atlstatic_OCL_IfExp = Class(name="atlstatic_OCL_IfExp")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
atlstatic_OCL_Primitive = Class(name="atlstatic_OCL_Primitive", is_abstract=True)
atlstatic_OCL_StringType = Class(name="atlstatic_OCL_StringType")
Primitive = Class(name="Primitive")
atlstatic_OCL_BooleanType = Class(name="atlstatic_OCL_BooleanType")
atlstatic_OCL_NumericType = Class(name="atlstatic_OCL_NumericType", is_abstract=True)
atlstatic_OCL_IntegerType = Class(name="atlstatic_OCL_IntegerType")
NumericType = Class(name="NumericType")
atlstatic_OCL_RealType = Class(name="atlstatic_OCL_RealType")
atlstatic_OCL_BagType = Class(name="atlstatic_OCL_BagType")
atlstatic_OCL_OrderedSetType = Class(name="atlstatic_OCL_OrderedSetType")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
atlstatic_OCL_Iterator = Class(name="atlstatic_OCL_Iterator")
atlstatic_OCL_Parameter = Class(name="atlstatic_OCL_Parameter")
atlstatic_OCL_CollectionType = Class(name="atlstatic_OCL_CollectionType")
atlstatic_OCL_OclType = Class(name="atlstatic_OCL_OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
atlstatic_OCL_OclFeature = Class(name="atlstatic_OCL_OclFeature", is_abstract=True)
atlstatic_OCL_Attribute = Class(name="atlstatic_OCL_Attribute")
atlstatic_OCL_Operation = Class(name="atlstatic_OCL_Operation")
atlstatic_OCL_SequenceType = Class(name="atlstatic_OCL_SequenceType")
atlstatic_OCL_SetType = Class(name="atlstatic_OCL_SetType")
atlstatic_OCL_OclAnyType = Class(name="atlstatic_OCL_OclAnyType")
atlstatic_OCL_TupleType = Class(name="atlstatic_OCL_TupleType")
atlstatic_OCL_TupleTypeAttribute = Class(name="atlstatic_OCL_TupleTypeAttribute")
TupleType = Class(name="TupleType")
atlstatic_OCL_OclModelElement = Class(name="atlstatic_OCL_OclModelElement")
atlstatic_OCL_MapType = Class(name="atlstatic_OCL_MapType")
atlstatic_OCL_OclFeatureDefinition = Class(name="atlstatic_OCL_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
atlstatic_OCL_OclContextDefinition = Class(name="atlstatic_OCL_OclContextDefinition")
atlstatic_OCL_OclModel = Class(name="atlstatic_OCL_OclModel")
OclModelElement = Class(name="OclModelElement")

# ModuleElement class attributes and methods

# atlstatic_ATL_ModuleElement class attributes and methods

# atlstatic_ATL_Helper class attributes and methods

# Query class attributes and methods

# Library class attributes and methods

# OclFeatureDefinition class attributes and methods

# atlstatic_ATL_Rule class attributes and methods
atlstatic_ATL_Rule_name: Property = Property(name="name", type=StringType)
atlstatic_ATL_Rule.attributes={atlstatic_ATL_Rule_name}

# atlstatic_ATL_LocatedElement class attributes and methods
atlstatic_ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
atlstatic_ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
atlstatic_ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
atlstatic_ATL_LocatedElement.attributes={atlstatic_ATL_LocatedElement_commentsBefore, atlstatic_ATL_LocatedElement_commentsAfter, atlstatic_ATL_LocatedElement_location}

# atlstatic_ATL_Unit class attributes and methods
atlstatic_ATL_Unit_name: Property = Property(name="name", type=StringType)
atlstatic_ATL_Unit.attributes={atlstatic_ATL_Unit_name}

# LocatedElement class attributes and methods

# LibraryRef class attributes and methods

# atlstatic_ATL_Library class attributes and methods

# Unit class attributes and methods

# Helper class attributes and methods

# atlstatic_ATL_Query class attributes and methods

# OclExpression class attributes and methods

# atlstatic_ATL_Module class attributes and methods
atlstatic_ATL_Module_isRefining: Property = Property(name="isRefining", type=StringType)
atlstatic_ATL_Module.attributes={atlstatic_ATL_Module_isRefining}

# OclModel class attributes and methods

# atlstatic_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# OutPatternElement class attributes and methods

# atlstatic_ATL_DropPattern class attributes and methods

# atlstatic_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# atlstatic_ATL_InPatternElement class attributes and methods

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# atlstatic_ATL_MatchedRule class attributes and methods
atlstatic_ATL_MatchedRule_isAbstract: Property = Property(name="isAbstract", type=StringType)
atlstatic_ATL_MatchedRule_isRefining: Property = Property(name="isRefining", type=StringType)
atlstatic_ATL_MatchedRule_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
atlstatic_ATL_MatchedRule.attributes={atlstatic_ATL_MatchedRule_isRefining, atlstatic_ATL_MatchedRule_isNoDefault, atlstatic_ATL_MatchedRule_isAbstract}

# Rule class attributes and methods

# InPattern class attributes and methods

# MatchedRule class attributes and methods

# atlstatic_ATL_LazyMatchedRule class attributes and methods
atlstatic_ATL_LazyMatchedRule_isUnique: Property = Property(name="isUnique", type=StringType)
atlstatic_ATL_LazyMatchedRule.attributes={atlstatic_ATL_LazyMatchedRule_isUnique}

# atlstatic_ATL_CalledRule class attributes and methods
atlstatic_ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
atlstatic_ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
atlstatic_ATL_CalledRule.attributes={atlstatic_ATL_CalledRule_isEndpoint, atlstatic_ATL_CalledRule_isEntrypoint}

# Parameter class attributes and methods

# atlstatic_ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# atlstatic_ATL_RuleVariableDeclaration class attributes and methods

# atlstatic_ATL_LibraryRef class attributes and methods
atlstatic_ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
atlstatic_ATL_LibraryRef.attributes={atlstatic_ATL_LibraryRef_name}

# atlstatic_ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# PatternElement class attributes and methods

# atlstatic_ATL_SimpleInPatternElement class attributes and methods

# atlstatic_ATL_OutPatternElement class attributes and methods

# Binding class attributes and methods

# atlstatic_ATL_SimpleOutPatternElement class attributes and methods

# atlstatic_ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# atlstatic_ATL_Binding class attributes and methods
atlstatic_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlstatic_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
atlstatic_ATL_Binding.attributes={atlstatic_ATL_Binding_propertyName, atlstatic_ATL_Binding_isAssignment}

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# atlstatic_ATL_Statement class attributes and methods

# atlstatic_ATL_ExpressionStat class attributes and methods

# atlstatic_ATL_BindingStat class attributes and methods
atlstatic_ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
atlstatic_ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlstatic_ATL_BindingStat.attributes={atlstatic_ATL_BindingStat_propertyName, atlstatic_ATL_BindingStat_isAssignment}

# atlstatic_ATL_IfStat class attributes and methods

# atlstatic_ATL_ForStat class attributes and methods

# atlstatic_OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# TuplePart class attributes and methods

# atlstatic_OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# atlstatic_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# atlstatic_OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# Operation class attributes and methods

# Attribute class attributes and methods

# atlstatic_OCL_VariableExp class attributes and methods

# atlstatic_OCL_SuperExp class attributes and methods

# atlstatic_OCL_PrimitiveExp class attributes and methods

# atlstatic_OCL_StringExp class attributes and methods
atlstatic_OCL_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
atlstatic_OCL_StringExp.attributes={atlstatic_OCL_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# atlstatic_OCL_BooleanExp class attributes and methods
atlstatic_OCL_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
atlstatic_OCL_BooleanExp.attributes={atlstatic_OCL_BooleanExp_booleanSymbol}

# atlstatic_OCL_NumericExp class attributes and methods

# atlstatic_OCL_RealExp class attributes and methods
atlstatic_OCL_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
atlstatic_OCL_RealExp.attributes={atlstatic_OCL_RealExp_realSymbol}

# NumericExp class attributes and methods

# atlstatic_OCL_IntegerExp class attributes and methods
atlstatic_OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
atlstatic_OCL_IntegerExp.attributes={atlstatic_OCL_IntegerExp_integerSymbol}

# atlstatic_OCL_CollectionExp class attributes and methods

# atlstatic_OCL_BagExp class attributes and methods

# atlstatic_OCL_OrderedSetExp class attributes and methods

# atlstatic_OCL_SequenceExp class attributes and methods

# atlstatic_OCL_SetExp class attributes and methods

# atlstatic_OCL_TupleExp class attributes and methods

# atlstatic_OCL_NavigationOrAttributeCallExp class attributes and methods
atlstatic_OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_NavigationOrAttributeCallExp.attributes={atlstatic_OCL_NavigationOrAttributeCallExp_name}

# atlstatic_OCL_OperationCallExp class attributes and methods
atlstatic_OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
atlstatic_OCL_OperationCallExp.attributes={atlstatic_OCL_OperationCallExp_operationName}

# atlstatic_OCL_OperatorCallExp class attributes and methods

# atlstatic_OCL_CollectionOperationCallExp class attributes and methods

# atlstatic_OCL_LoopExp class attributes and methods

# atlstatic_OCL_EnumLiteralExp class attributes and methods
atlstatic_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_EnumLiteralExp.attributes={atlstatic_OCL_EnumLiteralExp_name}

# atlstatic_OCL_OclUndefinedExp class attributes and methods

# atlstatic_OCL_PropertyCallExp class attributes and methods

# atlstatic_OCL_VariableDeclaration class attributes and methods
atlstatic_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
atlstatic_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
atlstatic_OCL_VariableDeclaration.attributes={atlstatic_OCL_VariableDeclaration_id, atlstatic_OCL_VariableDeclaration_varName}

# atlstatic_OCL_IterateExp class attributes and methods

# atlstatic_OCL_IteratorExp class attributes and methods
atlstatic_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_IteratorExp.attributes={atlstatic_OCL_IteratorExp_name}

# atlstatic_OCL_LetExp class attributes and methods

# atlstatic_OCL_IfExp class attributes and methods

# TupleTypeAttribute class attributes and methods

# atlstatic_OCL_Primitive class attributes and methods

# atlstatic_OCL_StringType class attributes and methods

# Primitive class attributes and methods

# atlstatic_OCL_BooleanType class attributes and methods

# atlstatic_OCL_NumericType class attributes and methods

# atlstatic_OCL_IntegerType class attributes and methods

# NumericType class attributes and methods

# atlstatic_OCL_RealType class attributes and methods

# atlstatic_OCL_BagType class attributes and methods

# atlstatic_OCL_OrderedSetType class attributes and methods

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# atlstatic_OCL_Iterator class attributes and methods

# atlstatic_OCL_Parameter class attributes and methods

# atlstatic_OCL_CollectionType class attributes and methods

# atlstatic_OCL_OclType class attributes and methods
atlstatic_OCL_OclType_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_OclType.attributes={atlstatic_OCL_OclType_name}

# OclContextDefinition class attributes and methods

# MapType class attributes and methods

# CollectionType class attributes and methods

# atlstatic_OCL_OclFeature class attributes and methods

# atlstatic_OCL_Attribute class attributes and methods
atlstatic_OCL_Attribute_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_Attribute.attributes={atlstatic_OCL_Attribute_name}

# atlstatic_OCL_Operation class attributes and methods
atlstatic_OCL_Operation_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_Operation.attributes={atlstatic_OCL_Operation_name}

# atlstatic_OCL_SequenceType class attributes and methods

# atlstatic_OCL_SetType class attributes and methods

# atlstatic_OCL_OclAnyType class attributes and methods

# atlstatic_OCL_TupleType class attributes and methods

# atlstatic_OCL_TupleTypeAttribute class attributes and methods
atlstatic_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_TupleTypeAttribute.attributes={atlstatic_OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# atlstatic_OCL_OclModelElement class attributes and methods

# atlstatic_OCL_MapType class attributes and methods

# atlstatic_OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# atlstatic_OCL_OclContextDefinition class attributes and methods

# atlstatic_OCL_OclModel class attributes and methods
atlstatic_OCL_OclModel_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_OclModel.attributes={atlstatic_OCL_OclModel_name}

# OclModelElement class attributes and methods

# Relationships
outModels6: BinaryAssociation = BinaryAssociation(
    name="outModels6",
    ends={
        Property(name="OclModel8", type=atlstatic_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Module7", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements9: BinaryAssociation = BinaryAssociation(
    name="elements9",
    ends={
        Property(name="ModuleElement", type=atlstatic_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Module10", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query11: BinaryAssociation = BinaryAssociation(
    name="query11",
    ends={
        Property(name="Query", type=atlstatic_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
library12: BinaryAssociation = BinaryAssociation(
    name="library12",
    ends={
        Property(name="Library", type=atlstatic_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers13", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
definition14: BinaryAssociation = BinaryAssociation(
    name="definition14",
    ends={
        Property(name="OclFeatureDefinition", type=atlstatic_ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
libraries0: BinaryAssociation = BinaryAssociation(
    name="libraries0",
    ends={
        Property(name="LibraryRef", type=atlstatic_ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="unit", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers1: BinaryAssociation = BinaryAssociation(
    name="helpers1",
    ends={
        Property(name="Helper", type=atlstatic_ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body2: BinaryAssociation = BinaryAssociation(
    name="body2",
    ends={
        Property(name="OclExpression", type=atlstatic_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
helpers3: BinaryAssociation = BinaryAssociation(
    name="helpers3",
    ends={
        Property(name="Helper4", type=atlstatic_ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="query", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inModels5: BinaryAssociation = BinaryAssociation(
    name="inModels5",
    ends={
        Property(name="OclModel", type=atlstatic_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
filter30: BinaryAssociation = BinaryAssociation(
    name="filter30",
    ends={
        Property(name="OclExpression31", type=atlstatic_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule32: BinaryAssociation = BinaryAssociation(
    name="rule32",
    ends={
        Property(name="Rule", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern33: BinaryAssociation = BinaryAssociation(
    name="dropPattern33",
    ends={
        Property(name="DropPattern", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern34", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements35: BinaryAssociation = BinaryAssociation(
    name="elements35",
    ends={
        Property(name="OutPatternElement", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern36", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern37: BinaryAssociation = BinaryAssociation(
    name="outPattern37",
    ends={
        Property(name="OutPattern38", type=atlstatic_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dropPattern", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
outPattern15: BinaryAssociation = BinaryAssociation(
    name="outPattern15",
    ends={
        Property(name="OutPattern", type=atlstatic_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock16: BinaryAssociation = BinaryAssociation(
    name="actionBlock16",
    ends={
        Property(name="ActionBlock", type=atlstatic_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule17", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables18: BinaryAssociation = BinaryAssociation(
    name="variables18",
    ends={
        Property(name="RuleVariableDeclaration", type=atlstatic_ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule19", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern20: BinaryAssociation = BinaryAssociation(
    name="inPattern20",
    ends={
        Property(name="InPattern", type=atlstatic_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule21", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children22: BinaryAssociation = BinaryAssociation(
    name="children22",
    ends={
        Property(name="MatchedRule", type=atlstatic_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="superRule", type=MatchedRule, multiplicity=Multiplicity(0, 9999))
    }
)
superRule23: BinaryAssociation = BinaryAssociation(
    name="superRule23",
    ends={
        Property(name="MatchedRule24", type=atlstatic_ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=MatchedRule, multiplicity=Multiplicity(0, 1))
    }
)
parameters25: BinaryAssociation = BinaryAssociation(
    name="parameters25",
    ends={
        Property(name="Parameter", type=atlstatic_ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements26: BinaryAssociation = BinaryAssociation(
    name="elements26",
    ends={
        Property(name="InPatternElement", type=atlstatic_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="inPattern", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rule27: BinaryAssociation = BinaryAssociation(
    name="rule27",
    ends={
        Property(name="MatchedRule29", type=atlstatic_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="inPattern28", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
rule63: BinaryAssociation = BinaryAssociation(
    name="rule63",
    ends={
        Property(name="Rule64", type=atlstatic_ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
unit65: BinaryAssociation = BinaryAssociation(
    name="unit65",
    ends={
        Property(name="Unit", type=atlstatic_ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="libraries", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
rule66: BinaryAssociation = BinaryAssociation(
    name="rule66",
    ends={
        Property(name="Rule67", type=atlstatic_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="actionBlock", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements68: BinaryAssociation = BinaryAssociation(
    name="statements68",
    ends={
        Property(name="Statement", type=atlstatic_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapsTo39: BinaryAssociation = BinaryAssociation(
    name="mapsTo39",
    ends={
        Property(name="OutPatternElement40", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceElement", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
inPattern41: BinaryAssociation = BinaryAssociation(
    name="inPattern41",
    ends={
        Property(name="InPattern42", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models43: BinaryAssociation = BinaryAssociation(
    name="models43",
    ends={
        Property(name="OclModel44", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern45: BinaryAssociation = BinaryAssociation(
    name="outPattern45",
    ends={
        Property(name="OutPattern47", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements46", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
sourceElement48: BinaryAssociation = BinaryAssociation(
    name="sourceElement48",
    ends={
        Property(name="InPatternElement49", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsTo", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings50: BinaryAssociation = BinaryAssociation(
    name="bindings50",
    ends={
        Property(name="Binding", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="outPatternElement", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model51: BinaryAssociation = BinaryAssociation(
    name="model51",
    ends={
        Property(name="OclModel52", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings53: BinaryAssociation = BinaryAssociation(
    name="reverseBindings53",
    ends={
        Property(name="OclExpression54", type=atlstatic_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection55: BinaryAssociation = BinaryAssociation(
    name="collection55",
    ends={
        Property(name="OclExpression56", type=atlstatic_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator57: BinaryAssociation = BinaryAssociation(
    name="iterator57",
    ends={
        Property(name="Iterator", type=atlstatic_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForEachOutPatternElement58", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value59: BinaryAssociation = BinaryAssociation(
    name="value59",
    ends={
        Property(name="OclExpression60", type=atlstatic_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement61: BinaryAssociation = BinaryAssociation(
    name="outPatternElement61",
    ends={
        Property(name="OutPatternElement62", type=atlstatic_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="bindings", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
appliedProperty94: BinaryAssociation = BinaryAssociation(
    name="appliedProperty94",
    ends={
        Property(name="PropertyCallExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection95: BinaryAssociation = BinaryAssociation(
    name="collection95",
    ends={
        Property(name="CollectionExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements96", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp97: BinaryAssociation = BinaryAssociation(
    name="letExp97",
    ends={
        Property(name="LetExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp98: BinaryAssociation = BinaryAssociation(
    name="loopExp98",
    ends={
        Property(name="LoopExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation99: BinaryAssociation = BinaryAssociation(
    name="parentOperation99",
    ends={
        Property(name="OperationCallExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable100: BinaryAssociation = BinaryAssociation(
    name="initializedVariable100",
    ends={
        Property(name="VariableDeclaration", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2101: BinaryAssociation = BinaryAssociation(
    name="ifExp2101",
    ends={
        Property(name="IfExp102", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
expression69: BinaryAssociation = BinaryAssociation(
    name="expression69",
    ends={
        Property(name="OclExpression70", type=atlstatic_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source71: BinaryAssociation = BinaryAssociation(
    name="source71",
    ends={
        Property(name="OclExpression72", type=atlstatic_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value73: BinaryAssociation = BinaryAssociation(
    name="value73",
    ends={
        Property(name="OclExpression75", type=atlstatic_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_BindingStat74", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition76: BinaryAssociation = BinaryAssociation(
    name="condition76",
    ends={
        Property(name="OclExpression77", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements78: BinaryAssociation = BinaryAssociation(
    name="thenStatements78",
    ends={
        Property(name="Statement80", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat79", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements81: BinaryAssociation = BinaryAssociation(
    name="elseStatements81",
    ends={
        Property(name="Statement83", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat82", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator84: BinaryAssociation = BinaryAssociation(
    name="iterator84",
    ends={
        Property(name="Iterator85", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection86: BinaryAssociation = BinaryAssociation(
    name="collection86",
    ends={
        Property(name="OclExpression88", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat87", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements89: BinaryAssociation = BinaryAssociation(
    name="statements89",
    ends={
        Property(name="Statement91", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat90", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type92: BinaryAssociation = BinaryAssociation(
    name="type92",
    ends={
        Property(name="OclType", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp393: BinaryAssociation = BinaryAssociation(
    name="ifExp393",
    ends={
        Property(name="IfExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
tuplePart113: BinaryAssociation = BinaryAssociation(
    name="tuplePart113",
    ends={
        Property(name="TuplePart", type=atlstatic_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple114: BinaryAssociation = BinaryAssociation(
    name="tuple114",
    ends={
        Property(name="TupleExp", type=atlstatic_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements115: BinaryAssociation = BinaryAssociation(
    name="elements115",
    ends={
        Property(name="MapElement", type=atlstatic_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map116: BinaryAssociation = BinaryAssociation(
    name="map116",
    ends={
        Property(name="MapExp", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements117", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
owningOperation103: BinaryAssociation = BinaryAssociation(
    name="owningOperation103",
    ends={
        Property(name="Operation", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body104", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1105: BinaryAssociation = BinaryAssociation(
    name="ifExp1105",
    ends={
        Property(name="IfExp106", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute107: BinaryAssociation = BinaryAssociation(
    name="owningAttribute107",
    ends={
        Property(name="Attribute", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression108", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable109: BinaryAssociation = BinaryAssociation(
    name="referredVariable109",
    ends={
        Property(name="VariableDeclaration110", type=atlstatic_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
elements111: BinaryAssociation = BinaryAssociation(
    name="elements111",
    ends={
        Property(name="OclExpression112", type=atlstatic_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments125: BinaryAssociation = BinaryAssociation(
    name="arguments125",
    ends={
        Property(name="OclExpression126", type=atlstatic_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key118: BinaryAssociation = BinaryAssociation(
    name="key118",
    ends={
        Property(name="OclExpression119", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value120: BinaryAssociation = BinaryAssociation(
    name="value120",
    ends={
        Property(name="OclExpression122", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_MapElement121", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source123: BinaryAssociation = BinaryAssociation(
    name="source123",
    ends={
        Property(name="OclExpression124", type=atlstatic_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression142: BinaryAssociation = BinaryAssociation(
    name="elseExpression142",
    ends={
        Property(name="OclExpression143", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type144: BinaryAssociation = BinaryAssociation(
    name="type144",
    ends={
        Property(name="OclType145", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression146: BinaryAssociation = BinaryAssociation(
    name="initExpression146",
    ends={
        Property(name="OclExpression147", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body127: BinaryAssociation = BinaryAssociation(
    name="body127",
    ends={
        Property(name="OclExpression128", type=atlstatic_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators129: BinaryAssociation = BinaryAssociation(
    name="iterators129",
    ends={
        Property(name="Iterator130", type=atlstatic_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result131: BinaryAssociation = BinaryAssociation(
    name="result131",
    ends={
        Property(name="VariableDeclaration132", type=atlstatic_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable133: BinaryAssociation = BinaryAssociation(
    name="variable133",
    ends={
        Property(name="VariableDeclaration134", type=atlstatic_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_135: BinaryAssociation = BinaryAssociation(
    name="in_135",
    ends={
        Property(name="OclExpression137", type=atlstatic_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp136", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression138: BinaryAssociation = BinaryAssociation(
    name="thenExpression138",
    ends={
        Property(name="OclExpression139", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition140: BinaryAssociation = BinaryAssociation(
    name="condition140",
    ends={
        Property(name="OclExpression141", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleTypeAttribute168: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute168",
    ends={
        Property(name="TupleTypeAttribute", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type169", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration170: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration170",
    ends={
        Property(name="VariableDeclaration172", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type171", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
letExp148: BinaryAssociation = BinaryAssociation(
    name="letExp148",
    ends={
        Property(name="LetExp149", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp150: BinaryAssociation = BinaryAssociation(
    name="baseExp150",
    ends={
        Property(name="IterateExp", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp151: BinaryAssociation = BinaryAssociation(
    name="variableExp151",
    ends={
        Property(name="VariableExp", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr152: BinaryAssociation = BinaryAssociation(
    name="loopExpr152",
    ends={
        Property(name="LoopExp153", type=atlstatic_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
elementType154: BinaryAssociation = BinaryAssociation(
    name="elementType154",
    ends={
        Property(name="OclType155", type=atlstatic_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions156: BinaryAssociation = BinaryAssociation(
    name="definitions156",
    ends={
        Property(name="OclContextDefinition", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression157: BinaryAssociation = BinaryAssociation(
    name="oclExpression157",
    ends={
        Property(name="OclExpression158", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation159: BinaryAssociation = BinaryAssociation(
    name="operation159",
    ends={
        Property(name="Operation160", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2161: BinaryAssociation = BinaryAssociation(
    name="mapType2161",
    ends={
        Property(name="MapType", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute162: BinaryAssociation = BinaryAssociation(
    name="attribute162",
    ends={
        Property(name="Attribute164", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type163", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType165: BinaryAssociation = BinaryAssociation(
    name="mapType165",
    ends={
        Property(name="MapType166", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes167: BinaryAssociation = BinaryAssociation(
    name="collectionTypes167",
    ends={
        Property(name="CollectionType", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
context_192: BinaryAssociation = BinaryAssociation(
    name="context_192",
    ends={
        Property(name="OclType193", type=atlstatic_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition194: BinaryAssociation = BinaryAssociation(
    name="definition194",
    ends={
        Property(name="OclFeatureDefinition195", type=atlstatic_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression196: BinaryAssociation = BinaryAssociation(
    name="initExpression196",
    ends={
        Property(name="OclExpression197", type=atlstatic_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type198: BinaryAssociation = BinaryAssociation(
    name="type198",
    ends={
        Property(name="OclType199", type=atlstatic_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes173: BinaryAssociation = BinaryAssociation(
    name="attributes173",
    ends={
        Property(name="TupleTypeAttribute174", type=atlstatic_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type175: BinaryAssociation = BinaryAssociation(
    name="type175",
    ends={
        Property(name="OclType176", type=atlstatic_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType177: BinaryAssociation = BinaryAssociation(
    name="tupleType177",
    ends={
        Property(name="TupleType", type=atlstatic_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model178: BinaryAssociation = BinaryAssociation(
    name="model178",
    ends={
        Property(name="OclModel180", type=atlstatic_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements179", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType181: BinaryAssociation = BinaryAssociation(
    name="valueType181",
    ends={
        Property(name="OclType182", type=atlstatic_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType183: BinaryAssociation = BinaryAssociation(
    name="keyType183",
    ends={
        Property(name="OclType184", type=atlstatic_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature185: BinaryAssociation = BinaryAssociation(
    name="feature185",
    ends={
        Property(name="OclFeature", type=atlstatic_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_186: BinaryAssociation = BinaryAssociation(
    name="context_186",
    ends={
        Property(name="OclContextDefinition188", type=atlstatic_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition187", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition189: BinaryAssociation = BinaryAssociation(
    name="definition189",
    ends={
        Property(name="OclFeatureDefinition191", type=atlstatic_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_190", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
parameters200: BinaryAssociation = BinaryAssociation(
    name="parameters200",
    ends={
        Property(name="Parameter201", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType202: BinaryAssociation = BinaryAssociation(
    name="returnType202",
    ends={
        Property(name="OclType203", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body204: BinaryAssociation = BinaryAssociation(
    name="body204",
    ends={
        Property(name="OclExpression205", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel206: BinaryAssociation = BinaryAssociation(
    name="metamodel206",
    ends={
        Property(name="OclModel207", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements208: BinaryAssociation = BinaryAssociation(
    name="elements208",
    ends={
        Property(name="OclModelElement", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model209", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model210: BinaryAssociation = BinaryAssociation(
    name="model210",
    ends={
        Property(name="OclModel211", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_atlstatic_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_ModuleElement)
gen_atlstatic_ATL_Helper_ModuleElement = Generalization(general=ModuleElement, specific=atlstatic_ATL_Helper)
gen_atlstatic_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=atlstatic_ATL_Rule)
gen_atlstatic_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Unit)
gen_atlstatic_ATL_Library_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Library)
gen_atlstatic_ATL_Query_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Query)
gen_atlstatic_ATL_Module_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Module)
gen_atlstatic_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_OutPattern)
gen_atlstatic_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_DropPattern)
gen_atlstatic_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_ATL_PatternElement)
gen_atlstatic_ATL_MatchedRule_Rule = Generalization(general=Rule, specific=atlstatic_ATL_MatchedRule)
gen_atlstatic_ATL_LazyMatchedRule_MatchedRule = Generalization(general=MatchedRule, specific=atlstatic_ATL_LazyMatchedRule)
gen_atlstatic_ATL_CalledRule_Rule = Generalization(general=Rule, specific=atlstatic_ATL_CalledRule)
gen_atlstatic_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_InPattern)
gen_atlstatic_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_ATL_RuleVariableDeclaration)
gen_atlstatic_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_LibraryRef)
gen_atlstatic_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_ActionBlock)
gen_atlstatic_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlstatic_ATL_InPatternElement)
gen_atlstatic_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=atlstatic_ATL_SimpleInPatternElement)
gen_atlstatic_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlstatic_ATL_OutPatternElement)
gen_atlstatic_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlstatic_ATL_SimpleOutPatternElement)
gen_atlstatic_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlstatic_ATL_ForEachOutPatternElement)
gen_atlstatic_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Binding)
gen_atlstatic_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Statement)
gen_atlstatic_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_ExpressionStat)
gen_atlstatic_ATL_BindingStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_BindingStat)
gen_atlstatic_ATL_IfStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_IfStat)
gen_atlstatic_ATL_ForStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_ForStat)
gen_atlstatic_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclExpression)
gen_atlstatic_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_TuplePart)
gen_atlstatic_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_MapExp)
gen_atlstatic_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_MapElement)
gen_atlstatic_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_VariableExp)
gen_atlstatic_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_SuperExp)
gen_atlstatic_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_PrimitiveExp)
gen_atlstatic_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_StringExp)
gen_atlstatic_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_BooleanExp)
gen_atlstatic_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_NumericExp)
gen_atlstatic_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=atlstatic_OCL_RealExp)
gen_atlstatic_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=atlstatic_OCL_IntegerExp)
gen_atlstatic_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_CollectionExp)
gen_atlstatic_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_BagExp)
gen_atlstatic_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_OrderedSetExp)
gen_atlstatic_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_SequenceExp)
gen_atlstatic_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_SetExp)
gen_atlstatic_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_TupleExp)
gen_atlstatic_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_NavigationOrAttributeCallExp)
gen_atlstatic_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_OperationCallExp)
gen_atlstatic_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlstatic_OCL_OperatorCallExp)
gen_atlstatic_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlstatic_OCL_CollectionOperationCallExp)
gen_atlstatic_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_LoopExp)
gen_atlstatic_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_EnumLiteralExp)
gen_atlstatic_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_OclUndefinedExp)
gen_atlstatic_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_PropertyCallExp)
gen_atlstatic_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_VariableDeclaration)
gen_atlstatic_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=atlstatic_OCL_IterateExp)
gen_atlstatic_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=atlstatic_OCL_IteratorExp)
gen_atlstatic_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_LetExp)
gen_atlstatic_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_IfExp)
gen_atlstatic_OCL_Primitive_OclType = Generalization(general=OclType, specific=atlstatic_OCL_Primitive)
gen_atlstatic_OCL_StringType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_StringType)
gen_atlstatic_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_BooleanType)
gen_atlstatic_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_NumericType)
gen_atlstatic_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=atlstatic_OCL_IntegerType)
gen_atlstatic_OCL_RealType_NumericType = Generalization(general=NumericType, specific=atlstatic_OCL_RealType)
gen_atlstatic_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_BagType)
gen_atlstatic_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_OrderedSetType)
gen_atlstatic_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_Iterator)
gen_atlstatic_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_Parameter)
gen_atlstatic_OCL_CollectionType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_CollectionType)
gen_atlstatic_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_OclType)
gen_atlstatic_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclFeature)
gen_atlstatic_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=atlstatic_OCL_Attribute)
gen_atlstatic_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=atlstatic_OCL_Operation)
gen_atlstatic_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_SequenceType)
gen_atlstatic_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_SetType)
gen_atlstatic_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_OclAnyType)
gen_atlstatic_OCL_TupleType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_TupleType)
gen_atlstatic_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_TupleTypeAttribute)
gen_atlstatic_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=atlstatic_OCL_OclModelElement)
gen_atlstatic_OCL_MapType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_MapType)
gen_atlstatic_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclFeatureDefinition)
gen_atlstatic_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclContextDefinition)
gen_atlstatic_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclModel)

# Domain Model
domain_model = DomainModel(
    name="atlstatic",
    types={ModuleElement, atlstatic_ATL_ModuleElement, atlstatic_ATL_Helper, Query, Library, OclFeatureDefinition, atlstatic_ATL_Rule, atlstatic_ATL_LocatedElement, atlstatic_ATL_Unit, LocatedElement, LibraryRef, atlstatic_ATL_Library, Unit, Helper, atlstatic_ATL_Query, OclExpression, atlstatic_ATL_Module, OclModel, atlstatic_ATL_OutPattern, DropPattern, OutPatternElement, atlstatic_ATL_DropPattern, atlstatic_ATL_PatternElement, VariableDeclaration, atlstatic_ATL_InPatternElement, OutPattern, ActionBlock, RuleVariableDeclaration, atlstatic_ATL_MatchedRule, Rule, InPattern, MatchedRule, atlstatic_ATL_LazyMatchedRule, atlstatic_ATL_CalledRule, Parameter_, atlstatic_ATL_InPattern, InPatternElement, atlstatic_ATL_RuleVariableDeclaration, atlstatic_ATL_LibraryRef, atlstatic_ATL_ActionBlock, Statement, PatternElement, atlstatic_ATL_SimpleInPatternElement, atlstatic_ATL_OutPatternElement, Binding, atlstatic_ATL_SimpleOutPatternElement, atlstatic_ATL_ForEachOutPatternElement, Iterator, atlstatic_ATL_Binding, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, atlstatic_ATL_Statement, atlstatic_ATL_ExpressionStat, atlstatic_ATL_BindingStat, atlstatic_ATL_IfStat, atlstatic_ATL_ForStat, atlstatic_OCL_OclExpression, OclType, IfExp, TuplePart, atlstatic_OCL_TuplePart, TupleExp, atlstatic_OCL_MapExp, MapElement, atlstatic_OCL_MapElement, MapExp, Operation, Attribute, atlstatic_OCL_VariableExp, atlstatic_OCL_SuperExp, atlstatic_OCL_PrimitiveExp, atlstatic_OCL_StringExp, PrimitiveExp, atlstatic_OCL_BooleanExp, atlstatic_OCL_NumericExp, atlstatic_OCL_RealExp, NumericExp, atlstatic_OCL_IntegerExp, atlstatic_OCL_CollectionExp, atlstatic_OCL_BagExp, atlstatic_OCL_OrderedSetExp, atlstatic_OCL_SequenceExp, atlstatic_OCL_SetExp, atlstatic_OCL_TupleExp, atlstatic_OCL_NavigationOrAttributeCallExp, atlstatic_OCL_OperationCallExp, atlstatic_OCL_OperatorCallExp, atlstatic_OCL_CollectionOperationCallExp, atlstatic_OCL_LoopExp, atlstatic_OCL_EnumLiteralExp, atlstatic_OCL_OclUndefinedExp, atlstatic_OCL_PropertyCallExp, atlstatic_OCL_VariableDeclaration, atlstatic_OCL_IterateExp, atlstatic_OCL_IteratorExp, atlstatic_OCL_LetExp, atlstatic_OCL_IfExp, TupleTypeAttribute, atlstatic_OCL_Primitive, atlstatic_OCL_StringType, Primitive, atlstatic_OCL_BooleanType, atlstatic_OCL_NumericType, atlstatic_OCL_IntegerType, NumericType, atlstatic_OCL_RealType, atlstatic_OCL_BagType, atlstatic_OCL_OrderedSetType, IterateExp, VariableExp, atlstatic_OCL_Iterator, atlstatic_OCL_Parameter, atlstatic_OCL_CollectionType, atlstatic_OCL_OclType, OclContextDefinition, MapType, CollectionType, atlstatic_OCL_OclFeature, atlstatic_OCL_Attribute, atlstatic_OCL_Operation, atlstatic_OCL_SequenceType, atlstatic_OCL_SetType, atlstatic_OCL_OclAnyType, atlstatic_OCL_TupleType, atlstatic_OCL_TupleTypeAttribute, TupleType, atlstatic_OCL_OclModelElement, atlstatic_OCL_MapType, atlstatic_OCL_OclFeatureDefinition, OclFeature, atlstatic_OCL_OclContextDefinition, atlstatic_OCL_OclModel, OclModelElement},
    associations={outModels6, elements9, query11, library12, definition14, libraries0, helpers1, body2, helpers3, inModels5, filter30, rule32, dropPattern33, elements35, outPattern37, outPattern15, actionBlock16, variables18, inPattern20, children22, superRule23, parameters25, elements26, rule27, rule63, unit65, rule66, statements68, mapsTo39, inPattern41, models43, outPattern45, sourceElement48, bindings50, model51, reverseBindings53, collection55, iterator57, value59, outPatternElement61, appliedProperty94, collection95, letExp97, loopExp98, parentOperation99, initializedVariable100, ifExp2101, expression69, source71, value73, condition76, thenStatements78, elseStatements81, iterator84, collection86, statements89, type92, ifExp393, tuplePart113, tuple114, elements115, map116, owningOperation103, ifExp1105, owningAttribute107, referredVariable109, elements111, arguments125, key118, value120, source123, elseExpression142, type144, initExpression146, body127, iterators129, result131, variable133, in_135, thenExpression138, condition140, tupleTypeAttribute168, variableDeclaration170, letExp148, baseExp150, variableExp151, loopExpr152, elementType154, definitions156, oclExpression157, operation159, mapType2161, attribute162, mapType165, collectionTypes167, context_192, definition194, initExpression196, type198, attributes173, type175, tupleType177, model178, valueType181, keyType183, feature185, context_186, definition189, parameters200, returnType202, body204, metamodel206, elements208, model210},
    generalizations={gen_atlstatic_ATL_ModuleElement_LocatedElement, gen_atlstatic_ATL_Helper_ModuleElement, gen_atlstatic_ATL_Rule_ModuleElement, gen_atlstatic_ATL_Unit_LocatedElement, gen_atlstatic_ATL_Library_Unit, gen_atlstatic_ATL_Query_Unit, gen_atlstatic_ATL_Module_Unit, gen_atlstatic_ATL_OutPattern_LocatedElement, gen_atlstatic_ATL_DropPattern_LocatedElement, gen_atlstatic_ATL_PatternElement_VariableDeclaration, gen_atlstatic_ATL_MatchedRule_Rule, gen_atlstatic_ATL_LazyMatchedRule_MatchedRule, gen_atlstatic_ATL_CalledRule_Rule, gen_atlstatic_ATL_InPattern_LocatedElement, gen_atlstatic_ATL_RuleVariableDeclaration_VariableDeclaration, gen_atlstatic_ATL_LibraryRef_LocatedElement, gen_atlstatic_ATL_ActionBlock_LocatedElement, gen_atlstatic_ATL_InPatternElement_PatternElement, gen_atlstatic_ATL_SimpleInPatternElement_InPatternElement, gen_atlstatic_ATL_OutPatternElement_PatternElement, gen_atlstatic_ATL_SimpleOutPatternElement_OutPatternElement, gen_atlstatic_ATL_ForEachOutPatternElement_OutPatternElement, gen_atlstatic_ATL_Binding_LocatedElement, gen_atlstatic_ATL_Statement_LocatedElement, gen_atlstatic_ATL_ExpressionStat_Statement, gen_atlstatic_ATL_BindingStat_Statement, gen_atlstatic_ATL_IfStat_Statement, gen_atlstatic_ATL_ForStat_Statement, gen_atlstatic_OCL_OclExpression_LocatedElement, gen_atlstatic_OCL_TuplePart_VariableDeclaration, gen_atlstatic_OCL_MapExp_OclExpression, gen_atlstatic_OCL_MapElement_LocatedElement, gen_atlstatic_OCL_VariableExp_OclExpression, gen_atlstatic_OCL_SuperExp_OclExpression, gen_atlstatic_OCL_PrimitiveExp_OclExpression, gen_atlstatic_OCL_StringExp_PrimitiveExp, gen_atlstatic_OCL_BooleanExp_PrimitiveExp, gen_atlstatic_OCL_NumericExp_PrimitiveExp, gen_atlstatic_OCL_RealExp_NumericExp, gen_atlstatic_OCL_IntegerExp_NumericExp, gen_atlstatic_OCL_CollectionExp_OclExpression, gen_atlstatic_OCL_BagExp_CollectionExp, gen_atlstatic_OCL_OrderedSetExp_CollectionExp, gen_atlstatic_OCL_SequenceExp_CollectionExp, gen_atlstatic_OCL_SetExp_CollectionExp, gen_atlstatic_OCL_TupleExp_OclExpression, gen_atlstatic_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_atlstatic_OCL_OperationCallExp_PropertyCallExp, gen_atlstatic_OCL_OperatorCallExp_OperationCallExp, gen_atlstatic_OCL_CollectionOperationCallExp_OperationCallExp, gen_atlstatic_OCL_LoopExp_PropertyCallExp, gen_atlstatic_OCL_EnumLiteralExp_OclExpression, gen_atlstatic_OCL_OclUndefinedExp_OclExpression, gen_atlstatic_OCL_PropertyCallExp_OclExpression, gen_atlstatic_OCL_VariableDeclaration_LocatedElement, gen_atlstatic_OCL_IterateExp_LoopExp, gen_atlstatic_OCL_IteratorExp_LoopExp, gen_atlstatic_OCL_LetExp_OclExpression, gen_atlstatic_OCL_IfExp_OclExpression, gen_atlstatic_OCL_Primitive_OclType, gen_atlstatic_OCL_StringType_Primitive, gen_atlstatic_OCL_BooleanType_Primitive, gen_atlstatic_OCL_NumericType_Primitive, gen_atlstatic_OCL_IntegerType_NumericType, gen_atlstatic_OCL_RealType_NumericType, gen_atlstatic_OCL_BagType_CollectionType, gen_atlstatic_OCL_OrderedSetType_CollectionType, gen_atlstatic_OCL_Iterator_VariableDeclaration, gen_atlstatic_OCL_Parameter_VariableDeclaration, gen_atlstatic_OCL_CollectionType_OclType, gen_atlstatic_OCL_OclType_OclExpression, gen_atlstatic_OCL_OclFeature_LocatedElement, gen_atlstatic_OCL_Attribute_OclFeature, gen_atlstatic_OCL_Operation_OclFeature, gen_atlstatic_OCL_SequenceType_CollectionType, gen_atlstatic_OCL_SetType_CollectionType, gen_atlstatic_OCL_OclAnyType_OclType, gen_atlstatic_OCL_TupleType_OclType, gen_atlstatic_OCL_TupleTypeAttribute_LocatedElement, gen_atlstatic_OCL_OclModelElement_OclType, gen_atlstatic_OCL_MapType_OclType, gen_atlstatic_OCL_OclFeatureDefinition_LocatedElement, gen_atlstatic_OCL_OclContextDefinition_LocatedElement, gen_atlstatic_OCL_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)