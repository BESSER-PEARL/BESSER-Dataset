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
atlstatic_ATL_LocatedElement = Class(name="atlstatic_ATL_LocatedElement", is_abstract=True)
atlstatic_ATL_StaticRule = Class(name="atlstatic_ATL_StaticRule", is_abstract=True)
ATL_Rule = Class(name="ATL_Rule")
atlstatic_ATL_ModuleCallable = Class(name="atlstatic_ATL_ModuleCallable", is_abstract=True)
Callable = Class(name="Callable")
atlstatic_ATL_Callable = Class(name="atlstatic_ATL_Callable", is_abstract=True)
atlstatic_ATL_RuleWithPattern = Class(name="atlstatic_ATL_RuleWithPattern", is_abstract=True)
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
RuleWithPattern = Class(name="RuleWithPattern")
atlstatic_ATL_MatchedRule = Class(name="atlstatic_ATL_MatchedRule")
atlstatic_ATL_LazyRule = Class(name="atlstatic_ATL_LazyRule")
ATL_RuleWithPattern = Class(name="ATL_RuleWithPattern")
ATL_StaticRule = Class(name="ATL_StaticRule")
atlstatic_ATL_CalledRule = Class(name="atlstatic_ATL_CalledRule")
StaticRule = Class(name="StaticRule")
Parameter_ = Class(name="Parameter")
ModuleElement = Class(name="ModuleElement")
atlstatic_ATL_ModuleElement = Class(name="atlstatic_ATL_ModuleElement", is_abstract=True)
atlstatic_ATL_Helper = Class(name="atlstatic_ATL_Helper", is_abstract=True)
ATL_ModuleElement = Class(name="ATL_ModuleElement")
ATL_Callable = Class(name="ATL_Callable")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
atlstatic_ATL_StaticHelper = Class(name="atlstatic_ATL_StaticHelper")
ATL_Helper = Class(name="ATL_Helper")
ATL_ModuleCallable = Class(name="ATL_ModuleCallable")
atlstatic_ATL_ContextHelper = Class(name="atlstatic_ATL_ContextHelper")
atlstatic_ATL_Rule = Class(name="atlstatic_ATL_Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
atlstatic_ATL_SimpleInPatternElement = Class(name="atlstatic_ATL_SimpleInPatternElement")
atlstatic_ATL_OutPatternElement = Class(name="atlstatic_ATL_OutPatternElement", is_abstract=True)
Binding = Class(name="Binding")
atlstatic_ATL_SimpleOutPatternElement = Class(name="atlstatic_ATL_SimpleOutPatternElement")
atlstatic_ATL_ForEachOutPatternElement = Class(name="atlstatic_ATL_ForEachOutPatternElement")
Iterator = Class(name="Iterator")
atlstatic_ATL_Binding = Class(name="atlstatic_ATL_Binding")
atlstatic_ATL_InPattern = Class(name="atlstatic_ATL_InPattern")
InPatternElement = Class(name="InPatternElement")
atlstatic_ATL_OutPattern = Class(name="atlstatic_ATL_OutPattern")
DropPattern = Class(name="DropPattern")
OutPatternElement = Class(name="OutPatternElement")
atlstatic_ATL_DropPattern = Class(name="atlstatic_ATL_DropPattern")
atlstatic_ATL_PatternElement = Class(name="atlstatic_ATL_PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
atlstatic_ATL_InPatternElement = Class(name="atlstatic_ATL_InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
atlstatic_ATL_ExpressionStat = Class(name="atlstatic_ATL_ExpressionStat")
atlstatic_ATL_BindingStat = Class(name="atlstatic_ATL_BindingStat")
atlstatic_ATL_IfStat = Class(name="atlstatic_ATL_IfStat")
atlstatic_ATL_ForStat = Class(name="atlstatic_ATL_ForStat")
atlstatic_ATL_RuleVariableDeclaration = Class(name="atlstatic_ATL_RuleVariableDeclaration")
atlstatic_ATL_LibraryRef = Class(name="atlstatic_ATL_LibraryRef")
atlstatic_ATL_ActionBlock = Class(name="atlstatic_ATL_ActionBlock")
Statement = Class(name="Statement")
atlstatic_ATL_Statement = Class(name="atlstatic_ATL_Statement", is_abstract=True)
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
atlstatic_OCL_OclExpression = Class(name="atlstatic_OCL_OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
atlstatic_OCL_MapExp = Class(name="atlstatic_OCL_MapExp")
MapElement = Class(name="MapElement")
atlstatic_OCL_MapElement = Class(name="atlstatic_OCL_MapElement")
MapExp = Class(name="MapExp")
atlstatic_OCL_EnumLiteralExp = Class(name="atlstatic_OCL_EnumLiteralExp")
atlstatic_OCL_OclUndefinedExp = Class(name="atlstatic_OCL_OclUndefinedExp")
atlstatic_OCL_PropertyCallExp = Class(name="atlstatic_OCL_PropertyCallExp", is_abstract=True)
atlstatic_OCL_NavigationOrAttributeCallExp = Class(name="atlstatic_OCL_NavigationOrAttributeCallExp")
atlstatic_OCL_OperationCallExp = Class(name="atlstatic_OCL_OperationCallExp")
atlstatic_OCL_IntegerExp = Class(name="atlstatic_OCL_IntegerExp")
atlstatic_OCL_CollectionExp = Class(name="atlstatic_OCL_CollectionExp", is_abstract=True)
atlstatic_OCL_BagExp = Class(name="atlstatic_OCL_BagExp")
atlstatic_OCL_OrderedSetExp = Class(name="atlstatic_OCL_OrderedSetExp")
atlstatic_OCL_SequenceExp = Class(name="atlstatic_OCL_SequenceExp")
atlstatic_OCL_SetExp = Class(name="atlstatic_OCL_SetExp")
atlstatic_OCL_TupleExp = Class(name="atlstatic_OCL_TupleExp")
TuplePart = Class(name="TuplePart")
atlstatic_OCL_TuplePart = Class(name="atlstatic_OCL_TuplePart")
TupleExp = Class(name="TupleExp")
atlstatic_OCL_IfExp = Class(name="atlstatic_OCL_IfExp")
atlstatic_OCL_VariableDeclaration = Class(name="atlstatic_OCL_VariableDeclaration")
atlstatic_OCL_OperatorCallExp = Class(name="atlstatic_OCL_OperatorCallExp")
atlstatic_OCL_CollectionOperationCallExp = Class(name="atlstatic_OCL_CollectionOperationCallExp")
atlstatic_OCL_LoopExp = Class(name="atlstatic_OCL_LoopExp", is_abstract=True)
atlstatic_OCL_IterateExp = Class(name="atlstatic_OCL_IterateExp")
atlstatic_OCL_IteratorExp = Class(name="atlstatic_OCL_IteratorExp")
atlstatic_OCL_LetExp = Class(name="atlstatic_OCL_LetExp")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
atlstatic_OCL_Iterator = Class(name="atlstatic_OCL_Iterator")
atlstatic_OCL_Parameter = Class(name="atlstatic_OCL_Parameter")
atlstatic_OCL_CollectionType = Class(name="atlstatic_OCL_CollectionType")
atlstatic_OCL_OclType = Class(name="atlstatic_OCL_OclType")
OclContextDefinition = Class(name="OclContextDefinition")
CollectionType = Class(name="CollectionType")
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
atlstatic_OCL_SequenceType = Class(name="atlstatic_OCL_SequenceType")
atlstatic_OCL_SetType = Class(name="atlstatic_OCL_SetType")
atlstatic_OCL_OclAnyType = Class(name="atlstatic_OCL_OclAnyType")
atlstatic_OCL_TupleType = Class(name="atlstatic_OCL_TupleType")
atlstatic_OCL_TupleTypeAttribute = Class(name="atlstatic_OCL_TupleTypeAttribute")
TupleType = Class(name="TupleType")
MapType = Class(name="MapType")
atlstatic_OCL_OclFeatureDefinition = Class(name="atlstatic_OCL_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
atlstatic_OCL_OclContextDefinition = Class(name="atlstatic_OCL_OclContextDefinition")
atlstatic_OCL_OclFeature = Class(name="atlstatic_OCL_OclFeature", is_abstract=True)
atlstatic_OCL_Attribute = Class(name="atlstatic_OCL_Attribute")
atlstatic_OCL_Operation = Class(name="atlstatic_OCL_Operation")
atlstatic_OCL_OclModelElement = Class(name="atlstatic_OCL_OclModelElement")
atlstatic_OCL_MapType = Class(name="atlstatic_OCL_MapType")
atlstatic_OCL_OclModel = Class(name="atlstatic_OCL_OclModel")
OclModelElement = Class(name="OclModelElement")

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

# atlstatic_ATL_LocatedElement class attributes and methods
atlstatic_ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
atlstatic_ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
atlstatic_ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
atlstatic_ATL_LocatedElement.attributes={atlstatic_ATL_LocatedElement_commentsAfter, atlstatic_ATL_LocatedElement_commentsBefore, atlstatic_ATL_LocatedElement_location}

# atlstatic_ATL_StaticRule class attributes and methods

# ATL_Rule class attributes and methods

# atlstatic_ATL_ModuleCallable class attributes and methods

# Callable class attributes and methods

# atlstatic_ATL_Callable class attributes and methods

# atlstatic_ATL_RuleWithPattern class attributes and methods
atlstatic_ATL_RuleWithPattern_isAbstract: Property = Property(name="isAbstract", type=StringType)
atlstatic_ATL_RuleWithPattern_isRefining: Property = Property(name="isRefining", type=StringType)
atlstatic_ATL_RuleWithPattern_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
atlstatic_ATL_RuleWithPattern.attributes={atlstatic_ATL_RuleWithPattern_isNoDefault, atlstatic_ATL_RuleWithPattern_isRefining, atlstatic_ATL_RuleWithPattern_isAbstract}

# Rule class attributes and methods

# InPattern class attributes and methods

# RuleWithPattern class attributes and methods

# atlstatic_ATL_MatchedRule class attributes and methods

# atlstatic_ATL_LazyRule class attributes and methods
atlstatic_ATL_LazyRule_isUnique: Property = Property(name="isUnique", type=StringType)
atlstatic_ATL_LazyRule.attributes={atlstatic_ATL_LazyRule_isUnique}

# ATL_RuleWithPattern class attributes and methods

# ATL_StaticRule class attributes and methods

# atlstatic_ATL_CalledRule class attributes and methods
atlstatic_ATL_CalledRule_isEntrypoint: Property = Property(name="isEntrypoint", type=StringType)
atlstatic_ATL_CalledRule_isEndpoint: Property = Property(name="isEndpoint", type=StringType)
atlstatic_ATL_CalledRule.attributes={atlstatic_ATL_CalledRule_isEndpoint, atlstatic_ATL_CalledRule_isEntrypoint}

# StaticRule class attributes and methods

# Parameter class attributes and methods

# ModuleElement class attributes and methods

# atlstatic_ATL_ModuleElement class attributes and methods

# atlstatic_ATL_Helper class attributes and methods

# ATL_ModuleElement class attributes and methods

# ATL_Callable class attributes and methods

# Query class attributes and methods

# Library class attributes and methods

# OclFeatureDefinition class attributes and methods

# atlstatic_ATL_StaticHelper class attributes and methods

# ATL_Helper class attributes and methods

# ATL_ModuleCallable class attributes and methods

# atlstatic_ATL_ContextHelper class attributes and methods

# atlstatic_ATL_Rule class attributes and methods
atlstatic_ATL_Rule_name: Property = Property(name="name", type=StringType)
atlstatic_ATL_Rule.attributes={atlstatic_ATL_Rule_name}

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# atlstatic_ATL_SimpleInPatternElement class attributes and methods

# atlstatic_ATL_OutPatternElement class attributes and methods

# Binding class attributes and methods

# atlstatic_ATL_SimpleOutPatternElement class attributes and methods

# atlstatic_ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# atlstatic_ATL_Binding class attributes and methods
atlstatic_ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
atlstatic_ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlstatic_ATL_Binding.attributes={atlstatic_ATL_Binding_isAssignment, atlstatic_ATL_Binding_propertyName}

# atlstatic_ATL_InPattern class attributes and methods

# InPatternElement class attributes and methods

# atlstatic_ATL_OutPattern class attributes and methods

# DropPattern class attributes and methods

# OutPatternElement class attributes and methods

# atlstatic_ATL_DropPattern class attributes and methods

# atlstatic_ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# atlstatic_ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# atlstatic_ATL_ExpressionStat class attributes and methods

# atlstatic_ATL_BindingStat class attributes and methods
atlstatic_ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
atlstatic_ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
atlstatic_ATL_BindingStat.attributes={atlstatic_ATL_BindingStat_isAssignment, atlstatic_ATL_BindingStat_propertyName}

# atlstatic_ATL_IfStat class attributes and methods

# atlstatic_ATL_ForStat class attributes and methods

# atlstatic_ATL_RuleVariableDeclaration class attributes and methods

# atlstatic_ATL_LibraryRef class attributes and methods
atlstatic_ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
atlstatic_ATL_LibraryRef.attributes={atlstatic_ATL_LibraryRef_name}

# atlstatic_ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

# atlstatic_ATL_Statement class attributes and methods

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

# atlstatic_OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

# CollectionExp class attributes and methods

# LetExp class attributes and methods

# LoopExp class attributes and methods

# OperationCallExp class attributes and methods

# atlstatic_OCL_MapExp class attributes and methods

# MapElement class attributes and methods

# atlstatic_OCL_MapElement class attributes and methods

# MapExp class attributes and methods

# atlstatic_OCL_EnumLiteralExp class attributes and methods
atlstatic_OCL_EnumLiteralExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_EnumLiteralExp.attributes={atlstatic_OCL_EnumLiteralExp_name}

# atlstatic_OCL_OclUndefinedExp class attributes and methods

# atlstatic_OCL_PropertyCallExp class attributes and methods

# atlstatic_OCL_NavigationOrAttributeCallExp class attributes and methods
atlstatic_OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_NavigationOrAttributeCallExp.attributes={atlstatic_OCL_NavigationOrAttributeCallExp_name}

# atlstatic_OCL_OperationCallExp class attributes and methods
atlstatic_OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
atlstatic_OCL_OperationCallExp.attributes={atlstatic_OCL_OperationCallExp_operationName}

# atlstatic_OCL_IntegerExp class attributes and methods
atlstatic_OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
atlstatic_OCL_IntegerExp.attributes={atlstatic_OCL_IntegerExp_integerSymbol}

# atlstatic_OCL_CollectionExp class attributes and methods

# atlstatic_OCL_BagExp class attributes and methods

# atlstatic_OCL_OrderedSetExp class attributes and methods

# atlstatic_OCL_SequenceExp class attributes and methods

# atlstatic_OCL_SetExp class attributes and methods

# atlstatic_OCL_TupleExp class attributes and methods

# TuplePart class attributes and methods

# atlstatic_OCL_TuplePart class attributes and methods

# TupleExp class attributes and methods

# atlstatic_OCL_IfExp class attributes and methods

# atlstatic_OCL_VariableDeclaration class attributes and methods
atlstatic_OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
atlstatic_OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
atlstatic_OCL_VariableDeclaration.attributes={atlstatic_OCL_VariableDeclaration_id, atlstatic_OCL_VariableDeclaration_varName}

# atlstatic_OCL_OperatorCallExp class attributes and methods

# atlstatic_OCL_CollectionOperationCallExp class attributes and methods

# atlstatic_OCL_LoopExp class attributes and methods

# atlstatic_OCL_IterateExp class attributes and methods

# atlstatic_OCL_IteratorExp class attributes and methods
atlstatic_OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_IteratorExp.attributes={atlstatic_OCL_IteratorExp_name}

# atlstatic_OCL_LetExp class attributes and methods

# IterateExp class attributes and methods

# VariableExp class attributes and methods

# atlstatic_OCL_Iterator class attributes and methods

# atlstatic_OCL_Parameter class attributes and methods

# atlstatic_OCL_CollectionType class attributes and methods

# atlstatic_OCL_OclType class attributes and methods
atlstatic_OCL_OclType_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_OclType.attributes={atlstatic_OCL_OclType_name}

# OclContextDefinition class attributes and methods

# CollectionType class attributes and methods

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

# atlstatic_OCL_SequenceType class attributes and methods

# atlstatic_OCL_SetType class attributes and methods

# atlstatic_OCL_OclAnyType class attributes and methods

# atlstatic_OCL_TupleType class attributes and methods

# atlstatic_OCL_TupleTypeAttribute class attributes and methods
atlstatic_OCL_TupleTypeAttribute_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_TupleTypeAttribute.attributes={atlstatic_OCL_TupleTypeAttribute_name}

# TupleType class attributes and methods

# MapType class attributes and methods

# atlstatic_OCL_OclFeatureDefinition class attributes and methods

# OclFeature class attributes and methods

# atlstatic_OCL_OclContextDefinition class attributes and methods

# atlstatic_OCL_OclFeature class attributes and methods

# atlstatic_OCL_Attribute class attributes and methods
atlstatic_OCL_Attribute_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_Attribute.attributes={atlstatic_OCL_Attribute_name}

# atlstatic_OCL_Operation class attributes and methods
atlstatic_OCL_Operation_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_Operation.attributes={atlstatic_OCL_Operation_name}

# atlstatic_OCL_OclModelElement class attributes and methods

# atlstatic_OCL_MapType class attributes and methods

# atlstatic_OCL_OclModel class attributes and methods
atlstatic_OCL_OclModel_name: Property = Property(name="name", type=StringType)
atlstatic_OCL_OclModel.attributes={atlstatic_OCL_OclModel_name}

# OclModelElement class attributes and methods

# Relationships
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
outModels6: BinaryAssociation = BinaryAssociation(
    name="outModels6",
    ends={
        Property(name="OclModel8", type=atlstatic_ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Module7", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inPattern20: BinaryAssociation = BinaryAssociation(
    name="inPattern20",
    ends={
        Property(name="InPattern", type=atlstatic_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_RuleWithPattern", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children21: BinaryAssociation = BinaryAssociation(
    name="children21",
    ends={
        Property(name="RuleWithPattern", type=atlstatic_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="superRule", type=RuleWithPattern, multiplicity=Multiplicity(0, 9999))
    }
)
superRule22: BinaryAssociation = BinaryAssociation(
    name="superRule22",
    ends={
        Property(name="RuleWithPattern23", type=atlstatic_ATL_RuleWithPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=RuleWithPattern, multiplicity=Multiplicity(0, 1))
    }
)
parameters24: BinaryAssociation = BinaryAssociation(
    name="parameters24",
    ends={
        Property(name="Parameter", type=atlstatic_ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
inPattern37: BinaryAssociation = BinaryAssociation(
    name="inPattern37",
    ends={
        Property(name="InPattern38", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models39: BinaryAssociation = BinaryAssociation(
    name="models39",
    ends={
        Property(name="OclModel40", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
outPattern41: BinaryAssociation = BinaryAssociation(
    name="outPattern41",
    ends={
        Property(name="OutPattern43", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements42", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
sourceElement44: BinaryAssociation = BinaryAssociation(
    name="sourceElement44",
    ends={
        Property(name="InPatternElement45", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsTo", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings46: BinaryAssociation = BinaryAssociation(
    name="bindings46",
    ends={
        Property(name="Binding", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="outPatternElement", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model47: BinaryAssociation = BinaryAssociation(
    name="model47",
    ends={
        Property(name="OclModel48", type=atlstatic_ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings49: BinaryAssociation = BinaryAssociation(
    name="reverseBindings49",
    ends={
        Property(name="OclExpression50", type=atlstatic_ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection51: BinaryAssociation = BinaryAssociation(
    name="collection51",
    ends={
        Property(name="OclExpression52", type=atlstatic_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator53: BinaryAssociation = BinaryAssociation(
    name="iterator53",
    ends={
        Property(name="Iterator", type=atlstatic_ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForEachOutPatternElement54", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value55: BinaryAssociation = BinaryAssociation(
    name="value55",
    ends={
        Property(name="OclExpression56", type=atlstatic_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements25: BinaryAssociation = BinaryAssociation(
    name="elements25",
    ends={
        Property(name="InPatternElement", type=atlstatic_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="inPattern", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
filter26: BinaryAssociation = BinaryAssociation(
    name="filter26",
    ends={
        Property(name="OclExpression27", type=atlstatic_ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule28: BinaryAssociation = BinaryAssociation(
    name="rule28",
    ends={
        Property(name="Rule", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern29: BinaryAssociation = BinaryAssociation(
    name="dropPattern29",
    ends={
        Property(name="DropPattern", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern30", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements31: BinaryAssociation = BinaryAssociation(
    name="elements31",
    ends={
        Property(name="OutPatternElement", type=atlstatic_ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern32", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern33: BinaryAssociation = BinaryAssociation(
    name="outPattern33",
    ends={
        Property(name="OutPattern34", type=atlstatic_ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dropPattern", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
mapsTo35: BinaryAssociation = BinaryAssociation(
    name="mapsTo35",
    ends={
        Property(name="OutPatternElement36", type=atlstatic_ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceElement", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
expression65: BinaryAssociation = BinaryAssociation(
    name="expression65",
    ends={
        Property(name="OclExpression66", type=atlstatic_ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source67: BinaryAssociation = BinaryAssociation(
    name="source67",
    ends={
        Property(name="OclExpression68", type=atlstatic_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value69: BinaryAssociation = BinaryAssociation(
    name="value69",
    ends={
        Property(name="OclExpression71", type=atlstatic_ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_BindingStat70", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition72: BinaryAssociation = BinaryAssociation(
    name="condition72",
    ends={
        Property(name="OclExpression73", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements74: BinaryAssociation = BinaryAssociation(
    name="thenStatements74",
    ends={
        Property(name="Statement76", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat75", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements77: BinaryAssociation = BinaryAssociation(
    name="elseStatements77",
    ends={
        Property(name="Statement79", type=atlstatic_ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_IfStat78", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterator80: BinaryAssociation = BinaryAssociation(
    name="iterator80",
    ends={
        Property(name="Iterator81", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection82: BinaryAssociation = BinaryAssociation(
    name="collection82",
    ends={
        Property(name="OclExpression84", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat83", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements85: BinaryAssociation = BinaryAssociation(
    name="statements85",
    ends={
        Property(name="Statement87", type=atlstatic_ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ForStat86", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outPatternElement57: BinaryAssociation = BinaryAssociation(
    name="outPatternElement57",
    ends={
        Property(name="OutPatternElement58", type=atlstatic_ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="bindings", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
rule59: BinaryAssociation = BinaryAssociation(
    name="rule59",
    ends={
        Property(name="Rule60", type=atlstatic_ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
unit61: BinaryAssociation = BinaryAssociation(
    name="unit61",
    ends={
        Property(name="Unit", type=atlstatic_ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="libraries", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
rule62: BinaryAssociation = BinaryAssociation(
    name="rule62",
    ends={
        Property(name="Rule63", type=atlstatic_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="actionBlock", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements64: BinaryAssociation = BinaryAssociation(
    name="statements64",
    ends={
        Property(name="Statement", type=atlstatic_ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializedVariable96: BinaryAssociation = BinaryAssociation(
    name="initializedVariable96",
    ends={
        Property(name="VariableDeclaration", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp297: BinaryAssociation = BinaryAssociation(
    name="ifExp297",
    ends={
        Property(name="IfExp98", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation99: BinaryAssociation = BinaryAssociation(
    name="owningOperation99",
    ends={
        Property(name="Operation", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body100", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1101: BinaryAssociation = BinaryAssociation(
    name="ifExp1101",
    ends={
        Property(name="IfExp102", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute103: BinaryAssociation = BinaryAssociation(
    name="owningAttribute103",
    ends={
        Property(name="Attribute", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression104", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable105: BinaryAssociation = BinaryAssociation(
    name="referredVariable105",
    ends={
        Property(name="VariableDeclaration106", type=atlstatic_OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
type88: BinaryAssociation = BinaryAssociation(
    name="type88",
    ends={
        Property(name="OclType", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp389: BinaryAssociation = BinaryAssociation(
    name="ifExp389",
    ends={
        Property(name="IfExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty90: BinaryAssociation = BinaryAssociation(
    name="appliedProperty90",
    ends={
        Property(name="PropertyCallExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
collection91: BinaryAssociation = BinaryAssociation(
    name="collection91",
    ends={
        Property(name="CollectionExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements92", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp93: BinaryAssociation = BinaryAssociation(
    name="letExp93",
    ends={
        Property(name="LetExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp94: BinaryAssociation = BinaryAssociation(
    name="loopExp94",
    ends={
        Property(name="LoopExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation95: BinaryAssociation = BinaryAssociation(
    name="parentOperation95",
    ends={
        Property(name="OperationCallExp", type=atlstatic_OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
elements111: BinaryAssociation = BinaryAssociation(
    name="elements111",
    ends={
        Property(name="MapElement", type=atlstatic_OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map112: BinaryAssociation = BinaryAssociation(
    name="map112",
    ends={
        Property(name="MapExp", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements113", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key114: BinaryAssociation = BinaryAssociation(
    name="key114",
    ends={
        Property(name="OclExpression115", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value116: BinaryAssociation = BinaryAssociation(
    name="value116",
    ends={
        Property(name="OclExpression118", type=atlstatic_OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_MapElement117", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source119: BinaryAssociation = BinaryAssociation(
    name="source119",
    ends={
        Property(name="OclExpression120", type=atlstatic_OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements107: BinaryAssociation = BinaryAssociation(
    name="elements107",
    ends={
        Property(name="OclExpression108", type=atlstatic_OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart109: BinaryAssociation = BinaryAssociation(
    name="tuplePart109",
    ends={
        Property(name="TuplePart", type=atlstatic_OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple110: BinaryAssociation = BinaryAssociation(
    name="tuple110",
    ends={
        Property(name="TupleExp", type=atlstatic_OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
in_131: BinaryAssociation = BinaryAssociation(
    name="in_131",
    ends={
        Property(name="OclExpression133", type=atlstatic_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp132", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression134: BinaryAssociation = BinaryAssociation(
    name="thenExpression134",
    ends={
        Property(name="OclExpression135", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition136: BinaryAssociation = BinaryAssociation(
    name="condition136",
    ends={
        Property(name="OclExpression137", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression138: BinaryAssociation = BinaryAssociation(
    name="elseExpression138",
    ends={
        Property(name="OclExpression139", type=atlstatic_OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type140: BinaryAssociation = BinaryAssociation(
    name="type140",
    ends={
        Property(name="OclType141", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression142: BinaryAssociation = BinaryAssociation(
    name="initExpression142",
    ends={
        Property(name="OclExpression143", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments121: BinaryAssociation = BinaryAssociation(
    name="arguments121",
    ends={
        Property(name="OclExpression122", type=atlstatic_OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body123: BinaryAssociation = BinaryAssociation(
    name="body123",
    ends={
        Property(name="OclExpression124", type=atlstatic_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators125: BinaryAssociation = BinaryAssociation(
    name="iterators125",
    ends={
        Property(name="Iterator126", type=atlstatic_OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result127: BinaryAssociation = BinaryAssociation(
    name="result127",
    ends={
        Property(name="VariableDeclaration128", type=atlstatic_OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable129: BinaryAssociation = BinaryAssociation(
    name="variable129",
    ends={
        Property(name="VariableDeclaration130", type=atlstatic_OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
baseExp146: BinaryAssociation = BinaryAssociation(
    name="baseExp146",
    ends={
        Property(name="IterateExp", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp147: BinaryAssociation = BinaryAssociation(
    name="variableExp147",
    ends={
        Property(name="VariableExp", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr148: BinaryAssociation = BinaryAssociation(
    name="loopExpr148",
    ends={
        Property(name="LoopExp149", type=atlstatic_OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
elementType150: BinaryAssociation = BinaryAssociation(
    name="elementType150",
    ends={
        Property(name="OclType151", type=atlstatic_OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions152: BinaryAssociation = BinaryAssociation(
    name="definitions152",
    ends={
        Property(name="OclContextDefinition", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression153: BinaryAssociation = BinaryAssociation(
    name="oclExpression153",
    ends={
        Property(name="OclExpression154", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation155: BinaryAssociation = BinaryAssociation(
    name="operation155",
    ends={
        Property(name="Operation156", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
letExp144: BinaryAssociation = BinaryAssociation(
    name="letExp144",
    ends={
        Property(name="LetExp145", type=atlstatic_OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
collectionTypes163: BinaryAssociation = BinaryAssociation(
    name="collectionTypes163",
    ends={
        Property(name="CollectionType", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute164: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute164",
    ends={
        Property(name="TupleTypeAttribute", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type165", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration166: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration166",
    ends={
        Property(name="VariableDeclaration168", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type167", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
attributes169: BinaryAssociation = BinaryAssociation(
    name="attributes169",
    ends={
        Property(name="TupleTypeAttribute170", type=atlstatic_OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type171: BinaryAssociation = BinaryAssociation(
    name="type171",
    ends={
        Property(name="OclType172", type=atlstatic_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType173: BinaryAssociation = BinaryAssociation(
    name="tupleType173",
    ends={
        Property(name="TupleType", type=atlstatic_OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
mapType2157: BinaryAssociation = BinaryAssociation(
    name="mapType2157",
    ends={
        Property(name="MapType", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute158: BinaryAssociation = BinaryAssociation(
    name="attribute158",
    ends={
        Property(name="Attribute160", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type159", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType161: BinaryAssociation = BinaryAssociation(
    name="mapType161",
    ends={
        Property(name="MapType162", type=atlstatic_OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
keyType179: BinaryAssociation = BinaryAssociation(
    name="keyType179",
    ends={
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="OclType180", type=atlstatic_OCL_MapType, multiplicity=Multiplicity(1, 1))
    }
)
feature181: BinaryAssociation = BinaryAssociation(
    name="feature181",
    ends={
        Property(name="OclFeature", type=atlstatic_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_182: BinaryAssociation = BinaryAssociation(
    name="context_182",
    ends={
        Property(name="OclContextDefinition184", type=atlstatic_OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition183", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition185: BinaryAssociation = BinaryAssociation(
    name="definition185",
    ends={
        Property(name="OclFeatureDefinition187", type=atlstatic_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_186", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_188: BinaryAssociation = BinaryAssociation(
    name="context_188",
    ends={
        Property(name="OclType189", type=atlstatic_OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition190: BinaryAssociation = BinaryAssociation(
    name="definition190",
    ends={
        Property(name="OclFeatureDefinition191", type=atlstatic_OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)
initExpression192: BinaryAssociation = BinaryAssociation(
    name="initExpression192",
    ends={
        Property(name="OclExpression193", type=atlstatic_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type194: BinaryAssociation = BinaryAssociation(
    name="type194",
    ends={
        Property(name="OclType195", type=atlstatic_OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters196: BinaryAssociation = BinaryAssociation(
    name="parameters196",
    ends={
        Property(name="Parameter197", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="atlstatic_OCL_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType198: BinaryAssociation = BinaryAssociation(
    name="returnType198",
    ends={
        Property(name="OclType199", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body200: BinaryAssociation = BinaryAssociation(
    name="body200",
    ends={
        Property(name="OclExpression201", type=atlstatic_OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model174: BinaryAssociation = BinaryAssociation(
    name="model174",
    ends={
        Property(name="OclModel176", type=atlstatic_OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements175", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType177: BinaryAssociation = BinaryAssociation(
    name="valueType177",
    ends={
        Property(name="OclType178", type=atlstatic_OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel202: BinaryAssociation = BinaryAssociation(
    name="metamodel202",
    ends={
        Property(name="OclModel203", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements204: BinaryAssociation = BinaryAssociation(
    name="elements204",
    ends={
        Property(name="OclModelElement", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model205", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model206: BinaryAssociation = BinaryAssociation(
    name="model206",
    ends={
        Property(name="OclModel207", type=atlstatic_OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_atlstatic_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Unit)
gen_atlstatic_ATL_Library_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Library)
gen_atlstatic_ATL_Query_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Query)
gen_atlstatic_ATL_Module_Unit = Generalization(general=Unit, specific=atlstatic_ATL_Module)
gen_atlstatic_ATL_StaticRule_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlstatic_ATL_StaticRule)
gen_atlstatic_ATL_StaticRule_ATL_Rule = Generalization(general=ATL_Rule, specific=atlstatic_ATL_StaticRule)
gen_atlstatic_ATL_ModuleCallable_Callable = Generalization(general=Callable, specific=atlstatic_ATL_ModuleCallable)
gen_atlstatic_ATL_RuleWithPattern_Rule = Generalization(general=Rule, specific=atlstatic_ATL_RuleWithPattern)
gen_atlstatic_ATL_MatchedRule_RuleWithPattern = Generalization(general=RuleWithPattern, specific=atlstatic_ATL_MatchedRule)
gen_atlstatic_ATL_LazyRule_ATL_RuleWithPattern = Generalization(general=ATL_RuleWithPattern, specific=atlstatic_ATL_LazyRule)
gen_atlstatic_ATL_LazyRule_ATL_StaticRule = Generalization(general=ATL_StaticRule, specific=atlstatic_ATL_LazyRule)
gen_atlstatic_ATL_CalledRule_StaticRule = Generalization(general=StaticRule, specific=atlstatic_ATL_CalledRule)
gen_atlstatic_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_ModuleElement)
gen_atlstatic_ATL_Helper_ATL_ModuleElement = Generalization(general=ATL_ModuleElement, specific=atlstatic_ATL_Helper)
gen_atlstatic_ATL_Helper_ATL_Callable = Generalization(general=ATL_Callable, specific=atlstatic_ATL_Helper)
gen_atlstatic_ATL_StaticHelper_ATL_Helper = Generalization(general=ATL_Helper, specific=atlstatic_ATL_StaticHelper)
gen_atlstatic_ATL_StaticHelper_ATL_ModuleCallable = Generalization(general=ATL_ModuleCallable, specific=atlstatic_ATL_StaticHelper)
gen_atlstatic_ATL_ContextHelper_Helper = Generalization(general=Helper, specific=atlstatic_ATL_ContextHelper)
gen_atlstatic_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=atlstatic_ATL_Rule)
gen_atlstatic_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=atlstatic_ATL_SimpleInPatternElement)
gen_atlstatic_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlstatic_ATL_OutPatternElement)
gen_atlstatic_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlstatic_ATL_SimpleOutPatternElement)
gen_atlstatic_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=atlstatic_ATL_ForEachOutPatternElement)
gen_atlstatic_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Binding)
gen_atlstatic_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_InPattern)
gen_atlstatic_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_OutPattern)
gen_atlstatic_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_DropPattern)
gen_atlstatic_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_ATL_PatternElement)
gen_atlstatic_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=atlstatic_ATL_InPatternElement)
gen_atlstatic_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_ExpressionStat)
gen_atlstatic_ATL_BindingStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_BindingStat)
gen_atlstatic_ATL_IfStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_IfStat)
gen_atlstatic_ATL_ForStat_Statement = Generalization(general=Statement, specific=atlstatic_ATL_ForStat)
gen_atlstatic_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_ATL_RuleVariableDeclaration)
gen_atlstatic_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_LibraryRef)
gen_atlstatic_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_ActionBlock)
gen_atlstatic_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_ATL_Statement)
gen_atlstatic_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_VariableExp)
gen_atlstatic_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_SuperExp)
gen_atlstatic_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_PrimitiveExp)
gen_atlstatic_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_StringExp)
gen_atlstatic_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_BooleanExp)
gen_atlstatic_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=atlstatic_OCL_NumericExp)
gen_atlstatic_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=atlstatic_OCL_RealExp)
gen_atlstatic_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclExpression)
gen_atlstatic_OCL_MapExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_MapExp)
gen_atlstatic_OCL_MapElement_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_MapElement)
gen_atlstatic_OCL_EnumLiteralExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_EnumLiteralExp)
gen_atlstatic_OCL_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_OclUndefinedExp)
gen_atlstatic_OCL_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_PropertyCallExp)
gen_atlstatic_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_NavigationOrAttributeCallExp)
gen_atlstatic_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_OperationCallExp)
gen_atlstatic_OCL_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=atlstatic_OCL_IntegerExp)
gen_atlstatic_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_CollectionExp)
gen_atlstatic_OCL_BagExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_BagExp)
gen_atlstatic_OCL_OrderedSetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_OrderedSetExp)
gen_atlstatic_OCL_SequenceExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_SequenceExp)
gen_atlstatic_OCL_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=atlstatic_OCL_SetExp)
gen_atlstatic_OCL_TupleExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_TupleExp)
gen_atlstatic_OCL_TuplePart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_TuplePart)
gen_atlstatic_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_IfExp)
gen_atlstatic_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_VariableDeclaration)
gen_atlstatic_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlstatic_OCL_OperatorCallExp)
gen_atlstatic_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=atlstatic_OCL_CollectionOperationCallExp)
gen_atlstatic_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=atlstatic_OCL_LoopExp)
gen_atlstatic_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=atlstatic_OCL_IterateExp)
gen_atlstatic_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=atlstatic_OCL_IteratorExp)
gen_atlstatic_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_LetExp)
gen_atlstatic_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_Iterator)
gen_atlstatic_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=atlstatic_OCL_Parameter)
gen_atlstatic_OCL_CollectionType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_CollectionType)
gen_atlstatic_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=atlstatic_OCL_OclType)
gen_atlstatic_OCL_Primitive_OclType = Generalization(general=OclType, specific=atlstatic_OCL_Primitive)
gen_atlstatic_OCL_StringType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_StringType)
gen_atlstatic_OCL_BooleanType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_BooleanType)
gen_atlstatic_OCL_NumericType_Primitive = Generalization(general=Primitive, specific=atlstatic_OCL_NumericType)
gen_atlstatic_OCL_IntegerType_NumericType = Generalization(general=NumericType, specific=atlstatic_OCL_IntegerType)
gen_atlstatic_OCL_RealType_NumericType = Generalization(general=NumericType, specific=atlstatic_OCL_RealType)
gen_atlstatic_OCL_BagType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_BagType)
gen_atlstatic_OCL_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_OrderedSetType)
gen_atlstatic_OCL_SequenceType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_SequenceType)
gen_atlstatic_OCL_SetType_CollectionType = Generalization(general=CollectionType, specific=atlstatic_OCL_SetType)
gen_atlstatic_OCL_OclAnyType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_OclAnyType)
gen_atlstatic_OCL_TupleType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_TupleType)
gen_atlstatic_OCL_TupleTypeAttribute_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_TupleTypeAttribute)
gen_atlstatic_OCL_OclFeatureDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclFeatureDefinition)
gen_atlstatic_OCL_OclContextDefinition_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclContextDefinition)
gen_atlstatic_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclFeature)
gen_atlstatic_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=atlstatic_OCL_Attribute)
gen_atlstatic_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=atlstatic_OCL_Operation)
gen_atlstatic_OCL_OclModelElement_OclType = Generalization(general=OclType, specific=atlstatic_OCL_OclModelElement)
gen_atlstatic_OCL_MapType_OclType = Generalization(general=OclType, specific=atlstatic_OCL_MapType)
gen_atlstatic_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=atlstatic_OCL_OclModel)

# Domain Model
domain_model = DomainModel(
    name="atlstatic",
    types={atlstatic_ATL_Unit, LocatedElement, LibraryRef, atlstatic_ATL_Library, Unit, Helper, atlstatic_ATL_Query, OclExpression, atlstatic_ATL_Module, OclModel, atlstatic_ATL_LocatedElement, atlstatic_ATL_StaticRule, ATL_Rule, atlstatic_ATL_ModuleCallable, Callable, atlstatic_ATL_Callable, atlstatic_ATL_RuleWithPattern, Rule, InPattern, RuleWithPattern, atlstatic_ATL_MatchedRule, atlstatic_ATL_LazyRule, ATL_RuleWithPattern, ATL_StaticRule, atlstatic_ATL_CalledRule, StaticRule, Parameter_, ModuleElement, atlstatic_ATL_ModuleElement, atlstatic_ATL_Helper, ATL_ModuleElement, ATL_Callable, Query, Library, OclFeatureDefinition, atlstatic_ATL_StaticHelper, ATL_Helper, ATL_ModuleCallable, atlstatic_ATL_ContextHelper, atlstatic_ATL_Rule, OutPattern, ActionBlock, RuleVariableDeclaration, atlstatic_ATL_SimpleInPatternElement, atlstatic_ATL_OutPatternElement, Binding, atlstatic_ATL_SimpleOutPatternElement, atlstatic_ATL_ForEachOutPatternElement, Iterator, atlstatic_ATL_Binding, atlstatic_ATL_InPattern, InPatternElement, atlstatic_ATL_OutPattern, DropPattern, OutPatternElement, atlstatic_ATL_DropPattern, atlstatic_ATL_PatternElement, VariableDeclaration, atlstatic_ATL_InPatternElement, PatternElement, atlstatic_ATL_ExpressionStat, atlstatic_ATL_BindingStat, atlstatic_ATL_IfStat, atlstatic_ATL_ForStat, atlstatic_ATL_RuleVariableDeclaration, atlstatic_ATL_LibraryRef, atlstatic_ATL_ActionBlock, Statement, atlstatic_ATL_Statement, Operation, Attribute, atlstatic_OCL_VariableExp, atlstatic_OCL_SuperExp, atlstatic_OCL_PrimitiveExp, atlstatic_OCL_StringExp, PrimitiveExp, atlstatic_OCL_BooleanExp, atlstatic_OCL_NumericExp, atlstatic_OCL_RealExp, NumericExp, atlstatic_OCL_OclExpression, OclType, IfExp, PropertyCallExp, CollectionExp, LetExp, LoopExp, OperationCallExp, atlstatic_OCL_MapExp, MapElement, atlstatic_OCL_MapElement, MapExp, atlstatic_OCL_EnumLiteralExp, atlstatic_OCL_OclUndefinedExp, atlstatic_OCL_PropertyCallExp, atlstatic_OCL_NavigationOrAttributeCallExp, atlstatic_OCL_OperationCallExp, atlstatic_OCL_IntegerExp, atlstatic_OCL_CollectionExp, atlstatic_OCL_BagExp, atlstatic_OCL_OrderedSetExp, atlstatic_OCL_SequenceExp, atlstatic_OCL_SetExp, atlstatic_OCL_TupleExp, TuplePart, atlstatic_OCL_TuplePart, TupleExp, atlstatic_OCL_IfExp, atlstatic_OCL_VariableDeclaration, atlstatic_OCL_OperatorCallExp, atlstatic_OCL_CollectionOperationCallExp, atlstatic_OCL_LoopExp, atlstatic_OCL_IterateExp, atlstatic_OCL_IteratorExp, atlstatic_OCL_LetExp, IterateExp, VariableExp, atlstatic_OCL_Iterator, atlstatic_OCL_Parameter, atlstatic_OCL_CollectionType, atlstatic_OCL_OclType, OclContextDefinition, CollectionType, TupleTypeAttribute, atlstatic_OCL_Primitive, atlstatic_OCL_StringType, Primitive, atlstatic_OCL_BooleanType, atlstatic_OCL_NumericType, atlstatic_OCL_IntegerType, NumericType, atlstatic_OCL_RealType, atlstatic_OCL_BagType, atlstatic_OCL_OrderedSetType, atlstatic_OCL_SequenceType, atlstatic_OCL_SetType, atlstatic_OCL_OclAnyType, atlstatic_OCL_TupleType, atlstatic_OCL_TupleTypeAttribute, TupleType, MapType, atlstatic_OCL_OclFeatureDefinition, OclFeature, atlstatic_OCL_OclContextDefinition, atlstatic_OCL_OclFeature, atlstatic_OCL_Attribute, atlstatic_OCL_Operation, atlstatic_OCL_OclModelElement, atlstatic_OCL_MapType, atlstatic_OCL_OclModel, OclModelElement},
    associations={libraries0, helpers1, body2, helpers3, inModels5, outModels6, inPattern20, children21, superRule22, parameters24, elements9, query11, library12, definition14, outPattern15, actionBlock16, variables18, inPattern37, models39, outPattern41, sourceElement44, bindings46, model47, reverseBindings49, collection51, iterator53, value55, elements25, filter26, rule28, dropPattern29, elements31, outPattern33, mapsTo35, expression65, source67, value69, condition72, thenStatements74, elseStatements77, iterator80, collection82, statements85, outPatternElement57, rule59, unit61, rule62, statements64, initializedVariable96, ifExp297, owningOperation99, ifExp1101, owningAttribute103, referredVariable105, type88, ifExp389, appliedProperty90, collection91, letExp93, loopExp94, parentOperation95, elements111, map112, key114, value116, source119, elements107, tuplePart109, tuple110, in_131, thenExpression134, condition136, elseExpression138, type140, initExpression142, arguments121, body123, iterators125, result127, variable129, baseExp146, variableExp147, loopExpr148, elementType150, definitions152, oclExpression153, operation155, letExp144, collectionTypes163, tupleTypeAttribute164, variableDeclaration166, attributes169, type171, tupleType173, mapType2157, attribute158, mapType161, keyType179, feature181, context_182, definition185, context_188, definition190, initExpression192, type194, parameters196, returnType198, body200, model174, valueType177, metamodel202, elements204, model206},
    generalizations={gen_atlstatic_ATL_Unit_LocatedElement, gen_atlstatic_ATL_Library_Unit, gen_atlstatic_ATL_Query_Unit, gen_atlstatic_ATL_Module_Unit, gen_atlstatic_ATL_StaticRule_ATL_ModuleCallable, gen_atlstatic_ATL_StaticRule_ATL_Rule, gen_atlstatic_ATL_ModuleCallable_Callable, gen_atlstatic_ATL_RuleWithPattern_Rule, gen_atlstatic_ATL_MatchedRule_RuleWithPattern, gen_atlstatic_ATL_LazyRule_ATL_RuleWithPattern, gen_atlstatic_ATL_LazyRule_ATL_StaticRule, gen_atlstatic_ATL_CalledRule_StaticRule, gen_atlstatic_ATL_ModuleElement_LocatedElement, gen_atlstatic_ATL_Helper_ATL_ModuleElement, gen_atlstatic_ATL_Helper_ATL_Callable, gen_atlstatic_ATL_StaticHelper_ATL_Helper, gen_atlstatic_ATL_StaticHelper_ATL_ModuleCallable, gen_atlstatic_ATL_ContextHelper_Helper, gen_atlstatic_ATL_Rule_ModuleElement, gen_atlstatic_ATL_SimpleInPatternElement_InPatternElement, gen_atlstatic_ATL_OutPatternElement_PatternElement, gen_atlstatic_ATL_SimpleOutPatternElement_OutPatternElement, gen_atlstatic_ATL_ForEachOutPatternElement_OutPatternElement, gen_atlstatic_ATL_Binding_LocatedElement, gen_atlstatic_ATL_InPattern_LocatedElement, gen_atlstatic_ATL_OutPattern_LocatedElement, gen_atlstatic_ATL_DropPattern_LocatedElement, gen_atlstatic_ATL_PatternElement_VariableDeclaration, gen_atlstatic_ATL_InPatternElement_PatternElement, gen_atlstatic_ATL_ExpressionStat_Statement, gen_atlstatic_ATL_BindingStat_Statement, gen_atlstatic_ATL_IfStat_Statement, gen_atlstatic_ATL_ForStat_Statement, gen_atlstatic_ATL_RuleVariableDeclaration_VariableDeclaration, gen_atlstatic_ATL_LibraryRef_LocatedElement, gen_atlstatic_ATL_ActionBlock_LocatedElement, gen_atlstatic_ATL_Statement_LocatedElement, gen_atlstatic_OCL_VariableExp_OclExpression, gen_atlstatic_OCL_SuperExp_OclExpression, gen_atlstatic_OCL_PrimitiveExp_OclExpression, gen_atlstatic_OCL_StringExp_PrimitiveExp, gen_atlstatic_OCL_BooleanExp_PrimitiveExp, gen_atlstatic_OCL_NumericExp_PrimitiveExp, gen_atlstatic_OCL_RealExp_NumericExp, gen_atlstatic_OCL_OclExpression_LocatedElement, gen_atlstatic_OCL_MapExp_OclExpression, gen_atlstatic_OCL_MapElement_LocatedElement, gen_atlstatic_OCL_EnumLiteralExp_OclExpression, gen_atlstatic_OCL_OclUndefinedExp_OclExpression, gen_atlstatic_OCL_PropertyCallExp_OclExpression, gen_atlstatic_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_atlstatic_OCL_OperationCallExp_PropertyCallExp, gen_atlstatic_OCL_IntegerExp_NumericExp, gen_atlstatic_OCL_CollectionExp_OclExpression, gen_atlstatic_OCL_BagExp_CollectionExp, gen_atlstatic_OCL_OrderedSetExp_CollectionExp, gen_atlstatic_OCL_SequenceExp_CollectionExp, gen_atlstatic_OCL_SetExp_CollectionExp, gen_atlstatic_OCL_TupleExp_OclExpression, gen_atlstatic_OCL_TuplePart_VariableDeclaration, gen_atlstatic_OCL_IfExp_OclExpression, gen_atlstatic_OCL_VariableDeclaration_LocatedElement, gen_atlstatic_OCL_OperatorCallExp_OperationCallExp, gen_atlstatic_OCL_CollectionOperationCallExp_OperationCallExp, gen_atlstatic_OCL_LoopExp_PropertyCallExp, gen_atlstatic_OCL_IterateExp_LoopExp, gen_atlstatic_OCL_IteratorExp_LoopExp, gen_atlstatic_OCL_LetExp_OclExpression, gen_atlstatic_OCL_Iterator_VariableDeclaration, gen_atlstatic_OCL_Parameter_VariableDeclaration, gen_atlstatic_OCL_CollectionType_OclType, gen_atlstatic_OCL_OclType_OclExpression, gen_atlstatic_OCL_Primitive_OclType, gen_atlstatic_OCL_StringType_Primitive, gen_atlstatic_OCL_BooleanType_Primitive, gen_atlstatic_OCL_NumericType_Primitive, gen_atlstatic_OCL_IntegerType_NumericType, gen_atlstatic_OCL_RealType_NumericType, gen_atlstatic_OCL_BagType_CollectionType, gen_atlstatic_OCL_OrderedSetType_CollectionType, gen_atlstatic_OCL_SequenceType_CollectionType, gen_atlstatic_OCL_SetType_CollectionType, gen_atlstatic_OCL_OclAnyType_OclType, gen_atlstatic_OCL_TupleType_OclType, gen_atlstatic_OCL_TupleTypeAttribute_LocatedElement, gen_atlstatic_OCL_OclFeatureDefinition_LocatedElement, gen_atlstatic_OCL_OclContextDefinition_LocatedElement, gen_atlstatic_OCL_OclFeature_LocatedElement, gen_atlstatic_OCL_Attribute_OclFeature, gen_atlstatic_OCL_Operation_OclFeature, gen_atlstatic_OCL_OclModelElement_OclType, gen_atlstatic_OCL_MapType_OclType, gen_atlstatic_OCL_OclModel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)