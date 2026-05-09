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
ATL_LocatedElement = Class(name="ATL_LocatedElement", is_abstract=True)
ATL_Unit = Class(name="ATL_Unit")
LocatedElement = Class(name="LocatedElement")
ATL_Module = Class(name="ATL_Module")
OclModel = Class(name="OclModel")
ModuleElement = Class(name="ModuleElement")
ATL_ModuleElement = Class(name="ATL_ModuleElement", is_abstract=True)
Module = Class(name="Module")
ATL_Helper = Class(name="ATL_Helper")
Query = Class(name="Query")
Library = Class(name="Library")
OclFeatureDefinition = Class(name="OclFeatureDefinition")
LibraryRef = Class(name="LibraryRef")
ATL_Library = Class(name="ATL_Library")
Unit = Class(name="Unit")
Helper = Class(name="Helper")
ATL_Query = Class(name="ATL_Query")
OclExpression = Class(name="OclExpression")
ATL_LazyMatchedRule = Class(name="ATL_LazyMatchedRule")
ATL_CalledRule = Class(name="ATL_CalledRule")
Parameter_ = Class(name="Parameter")
ATL_InPattern = Class(name="ATL_InPattern")
InPatternElement = Class(name="InPatternElement")
ATL_OutPattern = Class(name="ATL_OutPattern")
ATL_Rule = Class(name="ATL_Rule", is_abstract=True)
OutPattern = Class(name="OutPattern")
ActionBlock = Class(name="ActionBlock")
RuleVariableDeclaration = Class(name="RuleVariableDeclaration")
ATL_MatchedRule = Class(name="ATL_MatchedRule")
Rule = Class(name="Rule")
InPattern = Class(name="InPattern")
MatchedRule = Class(name="MatchedRule")
Binding = Class(name="Binding")
ATL_SimpleOutPatternElement = Class(name="ATL_SimpleOutPatternElement")
ATL_ForEachOutPatternElement = Class(name="ATL_ForEachOutPatternElement")
Iterator = Class(name="Iterator")
ATL_Binding = Class(name="ATL_Binding")
DropPattern = Class(name="DropPattern")
ATL_RuleVariableDeclaration = Class(name="ATL_RuleVariableDeclaration")
OutPatternElement = Class(name="OutPatternElement")
ATL_DropPattern = Class(name="ATL_DropPattern")
ATL_PatternElement = Class(name="ATL_PatternElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
ATL_InPatternElement = Class(name="ATL_InPatternElement", is_abstract=True)
PatternElement = Class(name="PatternElement")
ATL_SimpleInPatternElement = Class(name="ATL_SimpleInPatternElement")
ATL_OutPatternElement = Class(name="ATL_OutPatternElement", is_abstract=True)
ATL_Statement = Class(name="ATL_Statement", is_abstract=True)
ATL_ExpressionStat = Class(name="ATL_ExpressionStat")
ATL_BindingStat = Class(name="ATL_BindingStat")
ATL_IfStat = Class(name="ATL_IfStat")
ATL_ForStat = Class(name="ATL_ForStat")
ATL_LibraryRef = Class(name="ATL_LibraryRef")
ATL_ActionBlock = Class(name="ATL_ActionBlock")
Statement = Class(name="Statement")
CollectionExp = Class(name="CollectionExp")
LetExp = Class(name="LetExp")
LoopExp = Class(name="LoopExp")
OperationCallExp = Class(name="OperationCallExp")
Operation = Class(name="Operation")
Attribute = Class(name="Attribute")
OCL_VariableExp = Class(name="OCL_VariableExp")
OCL_SuperExp = Class(name="OCL_SuperExp")
OCL_PrimitiveExp = Class(name="OCL_PrimitiveExp", is_abstract=True)
OCL_StringExp = Class(name="OCL_StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
OCL_BooleanExp = Class(name="OCL_BooleanExp")
OCL_NumericExp = Class(name="OCL_NumericExp", is_abstract=True)
OCL_RealExp = Class(name="OCL_RealExp")
NumericExp = Class(name="NumericExp")
OCL_OclExpression = Class(name="OCL_OclExpression", is_abstract=True)
OclType = Class(name="OclType")
IfExp = Class(name="IfExp")
PropertyCallExp = Class(name="PropertyCallExp")
OCL_BagExp = Class(name="OCL_BagExp")
OCL_OrderedSetExp = Class(name="OCL_OrderedSetExp")
OCL_SequenceExp = Class(name="OCL_SequenceExp")
OCL_SetExp = Class(name="OCL_SetExp")
OCL_TupleExp = Class(name="OCL_TupleExp")
TuplePart = Class(name="TuplePart")
OCL_TuplePart = Class(name="OCL_TuplePart")
TupleExp = Class(name="TupleExp")
OCL_MapExp = Class(name="OCL_MapExp")
MapElement = Class(name="MapElement")
OCL_MapElement = Class(name="OCL_MapElement")
MapExp = Class(name="MapExp")
OCL_EnumLiteralExp = Class(name="OCL_EnumLiteralExp")
OCL_OclUndefinedExp = Class(name="OCL_OclUndefinedExp")
OCL_PropertyCallExp = Class(name="OCL_PropertyCallExp", is_abstract=True)
OCL_IntegerExp = Class(name="OCL_IntegerExp")
OCL_CollectionExp = Class(name="OCL_CollectionExp", is_abstract=True)
OCL_OperatorCallExp = Class(name="OCL_OperatorCallExp")
OCL_CollectionOperationCallExp = Class(name="OCL_CollectionOperationCallExp")
OCL_LoopExp = Class(name="OCL_LoopExp", is_abstract=True)
OCL_IterateExp = Class(name="OCL_IterateExp")
OCL_IteratorExp = Class(name="OCL_IteratorExp")
OCL_LetExp = Class(name="OCL_LetExp")
OCL_IfExp = Class(name="OCL_IfExp")
OCL_NavigationOrAttributeCallExp = Class(name="OCL_NavigationOrAttributeCallExp")
OCL_OperationCallExp = Class(name="OCL_OperationCallExp")
IterateExp = Class(name="IterateExp")
VariableExp = Class(name="VariableExp")
OCL_Iterator = Class(name="OCL_Iterator")
OCL_Parameter = Class(name="OCL_Parameter")
OCL_CollectionType = Class(name="OCL_CollectionType")
OCL_OclType = Class(name="OCL_OclType")
OclContextDefinition = Class(name="OclContextDefinition")
MapType = Class(name="MapType")
CollectionType = Class(name="CollectionType")
OCL_VariableDeclaration = Class(name="OCL_VariableDeclaration")
OCL_Primitive = Class(name="OCL_Primitive", is_abstract=True)
OCL_StringType = Class(name="OCL_StringType")
Primitive = Class(name="Primitive")
OCL_BooleanType = Class(name="OCL_BooleanType")
OCL_NumericType = Class(name="OCL_NumericType", is_abstract=True)
OCL_IntegerType = Class(name="OCL_IntegerType")
NumericType = Class(name="NumericType")
OCL_RealType = Class(name="OCL_RealType")
OCL_BagType = Class(name="OCL_BagType")
OCL_OrderedSetType = Class(name="OCL_OrderedSetType")
OCL_SequenceType = Class(name="OCL_SequenceType")
OCL_SetType = Class(name="OCL_SetType")
OCL_OclAnyType = Class(name="OCL_OclAnyType")
OCL_TupleType = Class(name="OCL_TupleType")
OCL_TupleTypeAttribute = Class(name="OCL_TupleTypeAttribute")
TupleType = Class(name="TupleType")
OCL_OclModelElement = Class(name="OCL_OclModelElement")
OCL_MapType = Class(name="OCL_MapType")
OCL_OclFeatureDefinition = Class(name="OCL_OclFeatureDefinition")
OclFeature = Class(name="OclFeature")
OCL_OclContextDefinition = Class(name="OCL_OclContextDefinition")
TupleTypeAttribute = Class(name="TupleTypeAttribute")
OCL_Attribute = Class(name="OCL_Attribute")
OCL_Operation = Class(name="OCL_Operation")
OCL_OclModel = Class(name="OCL_OclModel")
OclModelElement = Class(name="OclModelElement")
OCL_OclFeature = Class(name="OCL_OclFeature", is_abstract=True)

# ATL_LocatedElement class attributes and methods
ATL_LocatedElement_location: Property = Property(name="location", type=StringType)
ATL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
ATL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
ATL_LocatedElement.attributes={ATL_LocatedElement_commentsAfter, ATL_LocatedElement_location, ATL_LocatedElement_commentsBefore}

# ATL_Unit class attributes and methods
ATL_Unit_name: Property = Property(name="name", type=StringType)
ATL_Unit.attributes={ATL_Unit_name}

# LocatedElement class attributes and methods

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

# LibraryRef class attributes and methods

# ATL_Library class attributes and methods

# Unit class attributes and methods

# Helper class attributes and methods

# ATL_Query class attributes and methods

# OclExpression class attributes and methods

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

# ATL_Rule class attributes and methods
ATL_Rule_name: Property = Property(name="name", type=StringType)
ATL_Rule.attributes={ATL_Rule_name}

# OutPattern class attributes and methods

# ActionBlock class attributes and methods

# RuleVariableDeclaration class attributes and methods

# ATL_MatchedRule class attributes and methods
ATL_MatchedRule_isAbstract: Property = Property(name="isAbstract", type=StringType)
ATL_MatchedRule_isRefining: Property = Property(name="isRefining", type=StringType)
ATL_MatchedRule_isNoDefault: Property = Property(name="isNoDefault", type=StringType)
ATL_MatchedRule.attributes={ATL_MatchedRule_isNoDefault, ATL_MatchedRule_isAbstract, ATL_MatchedRule_isRefining}

# Rule class attributes and methods

# InPattern class attributes and methods

# MatchedRule class attributes and methods

# Binding class attributes and methods

# ATL_SimpleOutPatternElement class attributes and methods

# ATL_ForEachOutPatternElement class attributes and methods

# Iterator class attributes and methods

# ATL_Binding class attributes and methods
ATL_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
ATL_Binding_isAssignment: Property = Property(name="isAssignment", type=StringType)
ATL_Binding.attributes={ATL_Binding_isAssignment, ATL_Binding_propertyName}

# DropPattern class attributes and methods

# ATL_RuleVariableDeclaration class attributes and methods

# OutPatternElement class attributes and methods

# ATL_DropPattern class attributes and methods

# ATL_PatternElement class attributes and methods

# VariableDeclaration class attributes and methods

# ATL_InPatternElement class attributes and methods

# PatternElement class attributes and methods

# ATL_SimpleInPatternElement class attributes and methods

# ATL_OutPatternElement class attributes and methods

# ATL_Statement class attributes and methods

# ATL_ExpressionStat class attributes and methods

# ATL_BindingStat class attributes and methods
ATL_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
ATL_BindingStat_isAssignment: Property = Property(name="isAssignment", type=StringType)
ATL_BindingStat.attributes={ATL_BindingStat_propertyName, ATL_BindingStat_isAssignment}

# ATL_IfStat class attributes and methods

# ATL_ForStat class attributes and methods

# ATL_LibraryRef class attributes and methods
ATL_LibraryRef_name: Property = Property(name="name", type=StringType)
ATL_LibraryRef.attributes={ATL_LibraryRef_name}

# ATL_ActionBlock class attributes and methods

# Statement class attributes and methods

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

# OCL_OclExpression class attributes and methods

# OclType class attributes and methods

# IfExp class attributes and methods

# PropertyCallExp class attributes and methods

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

# OCL_IntegerExp class attributes and methods
OCL_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
OCL_IntegerExp.attributes={OCL_IntegerExp_integerSymbol}

# OCL_CollectionExp class attributes and methods

# OCL_OperatorCallExp class attributes and methods

# OCL_CollectionOperationCallExp class attributes and methods

# OCL_LoopExp class attributes and methods

# OCL_IterateExp class attributes and methods

# OCL_IteratorExp class attributes and methods
OCL_IteratorExp_name: Property = Property(name="name", type=StringType)
OCL_IteratorExp.attributes={OCL_IteratorExp_name}

# OCL_LetExp class attributes and methods

# OCL_IfExp class attributes and methods

# OCL_NavigationOrAttributeCallExp class attributes and methods
OCL_NavigationOrAttributeCallExp_name: Property = Property(name="name", type=StringType)
OCL_NavigationOrAttributeCallExp.attributes={OCL_NavigationOrAttributeCallExp_name}

# OCL_OperationCallExp class attributes and methods
OCL_OperationCallExp_operationName: Property = Property(name="operationName", type=StringType)
OCL_OperationCallExp.attributes={OCL_OperationCallExp_operationName}

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

# OCL_VariableDeclaration class attributes and methods
OCL_VariableDeclaration_id: Property = Property(name="id", type=StringType)
OCL_VariableDeclaration_varName: Property = Property(name="varName", type=StringType)
OCL_VariableDeclaration.attributes={OCL_VariableDeclaration_varName, OCL_VariableDeclaration_id}

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

# TupleTypeAttribute class attributes and methods

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

# OCL_OclFeature class attributes and methods

# Relationships
inModels5: BinaryAssociation = BinaryAssociation(
    name="inModels5",
    ends={
        Property(name="OclModel", type=ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Module", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outModels6: BinaryAssociation = BinaryAssociation(
    name="outModels6",
    ends={
        Property(name="OclModel8", type=ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Module7", type=OclModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements9: BinaryAssociation = BinaryAssociation(
    name="elements9",
    ends={
        Property(name="ModuleElement", type=ATL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module10: BinaryAssociation = BinaryAssociation(
    name="module10",
    ends={
        Property(name="Module", type=ATL_ModuleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
query11: BinaryAssociation = BinaryAssociation(
    name="query11",
    ends={
        Property(name="Query", type=ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers", type=Query, multiplicity=Multiplicity(0, 1))
    }
)
library12: BinaryAssociation = BinaryAssociation(
    name="library12",
    ends={
        Property(name="Library", type=ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="helpers13", type=Library, multiplicity=Multiplicity(0, 1))
    }
)
definition14: BinaryAssociation = BinaryAssociation(
    name="definition14",
    ends={
        Property(name="OclFeatureDefinition", type=ATL_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Helper", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
libraries0: BinaryAssociation = BinaryAssociation(
    name="libraries0",
    ends={
        Property(name="LibraryRef", type=ATL_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="unit", type=LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
helpers1: BinaryAssociation = BinaryAssociation(
    name="helpers1",
    ends={
        Property(name="Helper", type=ATL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body2: BinaryAssociation = BinaryAssociation(
    name="body2",
    ends={
        Property(name="OclExpression", type=ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Query", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
helpers3: BinaryAssociation = BinaryAssociation(
    name="helpers3",
    ends={
        Property(name="Helper4", type=ATL_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="query", type=Helper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters25: BinaryAssociation = BinaryAssociation(
    name="parameters25",
    ends={
        Property(name="Parameter", type=ATL_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_CalledRule", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements26: BinaryAssociation = BinaryAssociation(
    name="elements26",
    ends={
        Property(name="InPatternElement", type=ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="inPattern", type=InPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rule27: BinaryAssociation = BinaryAssociation(
    name="rule27",
    ends={
        Property(name="MatchedRule29", type=ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="inPattern28", type=MatchedRule, multiplicity=Multiplicity(1, 1))
    }
)
filter30: BinaryAssociation = BinaryAssociation(
    name="filter30",
    ends={
        Property(name="OclExpression31", type=ATL_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_InPattern", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule32: BinaryAssociation = BinaryAssociation(
    name="rule32",
    ends={
        Property(name="Rule", type=ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
outPattern15: BinaryAssociation = BinaryAssociation(
    name="outPattern15",
    ends={
        Property(name="OutPattern", type=ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule", type=OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock16: BinaryAssociation = BinaryAssociation(
    name="actionBlock16",
    ends={
        Property(name="ActionBlock", type=ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule17", type=ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables18: BinaryAssociation = BinaryAssociation(
    name="variables18",
    ends={
        Property(name="RuleVariableDeclaration", type=ATL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule19", type=RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern20: BinaryAssociation = BinaryAssociation(
    name="inPattern20",
    ends={
        Property(name="InPattern", type=ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule21", type=InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children22: BinaryAssociation = BinaryAssociation(
    name="children22",
    ends={
        Property(name="MatchedRule", type=ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="superRule", type=MatchedRule, multiplicity=Multiplicity(0, 9999))
    }
)
superRule23: BinaryAssociation = BinaryAssociation(
    name="superRule23",
    ends={
        Property(name="MatchedRule24", type=ATL_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=MatchedRule, multiplicity=Multiplicity(0, 1))
    }
)
outPattern46: BinaryAssociation = BinaryAssociation(
    name="outPattern46",
    ends={
        Property(name="OutPattern48", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements47", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
sourceElement49: BinaryAssociation = BinaryAssociation(
    name="sourceElement49",
    ends={
        Property(name="InPatternElement50", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsTo", type=InPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
bindings51: BinaryAssociation = BinaryAssociation(
    name="bindings51",
    ends={
        Property(name="Binding", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="outPatternElement", type=Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model52: BinaryAssociation = BinaryAssociation(
    name="model52",
    ends={
        Property(name="OclModel53", type=ATL_OutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_OutPatternElement", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
reverseBindings54: BinaryAssociation = BinaryAssociation(
    name="reverseBindings54",
    ends={
        Property(name="OclExpression55", type=ATL_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_SimpleOutPatternElement", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection56: BinaryAssociation = BinaryAssociation(
    name="collection56",
    ends={
        Property(name="OclExpression57", type=ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForEachOutPatternElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator58: BinaryAssociation = BinaryAssociation(
    name="iterator58",
    ends={
        Property(name="Iterator", type=ATL_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForEachOutPatternElement59", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value60: BinaryAssociation = BinaryAssociation(
    name="value60",
    ends={
        Property(name="OclExpression61", type=ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_Binding", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outPatternElement62: BinaryAssociation = BinaryAssociation(
    name="outPatternElement62",
    ends={
        Property(name="OutPatternElement63", type=ATL_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="bindings", type=OutPatternElement, multiplicity=Multiplicity(1, 1))
    }
)
dropPattern33: BinaryAssociation = BinaryAssociation(
    name="dropPattern33",
    ends={
        Property(name="DropPattern", type=ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern34", type=DropPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements35: BinaryAssociation = BinaryAssociation(
    name="elements35",
    ends={
        Property(name="OutPatternElement", type=ATL_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outPattern36", type=OutPatternElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outPattern37: BinaryAssociation = BinaryAssociation(
    name="outPattern37",
    ends={
        Property(name="OutPattern38", type=ATL_DropPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dropPattern", type=OutPattern, multiplicity=Multiplicity(1, 1))
    }
)
mapsTo39: BinaryAssociation = BinaryAssociation(
    name="mapsTo39",
    ends={
        Property(name="OutPatternElement40", type=ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceElement", type=OutPatternElement, multiplicity=Multiplicity(0, 1))
    }
)
inPattern41: BinaryAssociation = BinaryAssociation(
    name="inPattern41",
    ends={
        Property(name="InPattern43", type=ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements42", type=InPattern, multiplicity=Multiplicity(1, 1))
    }
)
models44: BinaryAssociation = BinaryAssociation(
    name="models44",
    ends={
        Property(name="OclModel45", type=ATL_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_InPatternElement", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
expression70: BinaryAssociation = BinaryAssociation(
    name="expression70",
    ends={
        Property(name="OclExpression71", type=ATL_ExpressionStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ExpressionStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source72: BinaryAssociation = BinaryAssociation(
    name="source72",
    ends={
        Property(name="OclExpression73", type=ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_BindingStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value74: BinaryAssociation = BinaryAssociation(
    name="value74",
    ends={
        Property(name="OclExpression76", type=ATL_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_BindingStat75", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition77: BinaryAssociation = BinaryAssociation(
    name="condition77",
    ends={
        Property(name="OclExpression78", type=ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_IfStat", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements79: BinaryAssociation = BinaryAssociation(
    name="thenStatements79",
    ends={
        Property(name="Statement81", type=ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_IfStat80", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements82: BinaryAssociation = BinaryAssociation(
    name="elseStatements82",
    ends={
        Property(name="Statement84", type=ATL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_IfStat83", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule64: BinaryAssociation = BinaryAssociation(
    name="rule64",
    ends={
        Property(name="Rule65", type=ATL_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
iterator85: BinaryAssociation = BinaryAssociation(
    name="iterator85",
    ends={
        Property(name="Iterator86", type=ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForStat", type=Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection87: BinaryAssociation = BinaryAssociation(
    name="collection87",
    ends={
        Property(name="OclExpression89", type=ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForStat88", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unit66: BinaryAssociation = BinaryAssociation(
    name="unit66",
    ends={
        Property(name="Unit", type=ATL_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="libraries", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
statements90: BinaryAssociation = BinaryAssociation(
    name="statements90",
    ends={
        Property(name="Statement92", type=ATL_ForStat, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ForStat91", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule67: BinaryAssociation = BinaryAssociation(
    name="rule67",
    ends={
        Property(name="Rule68", type=ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="actionBlock", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
statements69: BinaryAssociation = BinaryAssociation(
    name="statements69",
    ends={
        Property(name="Statement", type=ATL_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ATL_ActionBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection96: BinaryAssociation = BinaryAssociation(
    name="collection96",
    ends={
        Property(name="CollectionExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elements97", type=CollectionExp, multiplicity=Multiplicity(0, 1))
    }
)
letExp98: BinaryAssociation = BinaryAssociation(
    name="letExp98",
    ends={
        Property(name="LetExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
loopExp99: BinaryAssociation = BinaryAssociation(
    name="loopExp99",
    ends={
        Property(name="LoopExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
parentOperation100: BinaryAssociation = BinaryAssociation(
    name="parentOperation100",
    ends={
        Property(name="OperationCallExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arguments", type=OperationCallExp, multiplicity=Multiplicity(0, 1))
    }
)
initializedVariable101: BinaryAssociation = BinaryAssociation(
    name="initializedVariable101",
    ends={
        Property(name="VariableDeclaration", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ifExp2102: BinaryAssociation = BinaryAssociation(
    name="ifExp2102",
    ends={
        Property(name="IfExp103", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thenExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation104: BinaryAssociation = BinaryAssociation(
    name="owningOperation104",
    ends={
        Property(name="Operation", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="body105", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
ifExp1106: BinaryAssociation = BinaryAssociation(
    name="ifExp1106",
    ends={
        Property(name="IfExp107", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
owningAttribute108: BinaryAssociation = BinaryAssociation(
    name="owningAttribute108",
    ends={
        Property(name="Attribute", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="initExpression109", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable110: BinaryAssociation = BinaryAssociation(
    name="referredVariable110",
    ends={
        Property(name="VariableDeclaration111", type=OCL_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="variableExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
type93: BinaryAssociation = BinaryAssociation(
    name="type93",
    ends={
        Property(name="OclType", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="oclExpression", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExp394: BinaryAssociation = BinaryAssociation(
    name="ifExp394",
    ends={
        Property(name="IfExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="elseExpression", type=IfExp, multiplicity=Multiplicity(0, 1))
    }
)
appliedProperty95: BinaryAssociation = BinaryAssociation(
    name="appliedProperty95",
    ends={
        Property(name="PropertyCallExp", type=OCL_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PropertyCallExp, multiplicity=Multiplicity(0, 1))
    }
)
elements112: BinaryAssociation = BinaryAssociation(
    name="elements112",
    ends={
        Property(name="OclExpression113", type=OCL_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuplePart114: BinaryAssociation = BinaryAssociation(
    name="tuplePart114",
    ends={
        Property(name="TuplePart", type=OCL_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TuplePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple115: BinaryAssociation = BinaryAssociation(
    name="tuple115",
    ends={
        Property(name="TupleExp", type=OCL_TuplePart, multiplicity=Multiplicity(1, 1)),
        Property(name="tuplePart", type=TupleExp, multiplicity=Multiplicity(1, 1))
    }
)
elements116: BinaryAssociation = BinaryAssociation(
    name="elements116",
    ends={
        Property(name="MapElement", type=OCL_MapExp, multiplicity=Multiplicity(1, 1)),
        Property(name="map", type=MapElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map117: BinaryAssociation = BinaryAssociation(
    name="map117",
    ends={
        Property(name="MapExp", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements118", type=MapExp, multiplicity=Multiplicity(1, 1))
    }
)
key119: BinaryAssociation = BinaryAssociation(
    name="key119",
    ends={
        Property(name="OclExpression120", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value121: BinaryAssociation = BinaryAssociation(
    name="value121",
    ends={
        Property(name="OclExpression123", type=OCL_MapElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OCL_MapElement122", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments126: BinaryAssociation = BinaryAssociation(
    name="arguments126",
    ends={
        Property(name="OclExpression127", type=OCL_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOperation", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body128: BinaryAssociation = BinaryAssociation(
    name="body128",
    ends={
        Property(name="OclExpression129", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterators130: BinaryAssociation = BinaryAssociation(
    name="iterators130",
    ends={
        Property(name="Iterator131", type=OCL_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="loopExpr", type=Iterator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result132: BinaryAssociation = BinaryAssociation(
    name="result132",
    ends={
        Property(name="VariableDeclaration133", type=OCL_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="baseExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable134: BinaryAssociation = BinaryAssociation(
    name="variable134",
    ends={
        Property(name="VariableDeclaration135", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp", type=VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_136: BinaryAssociation = BinaryAssociation(
    name="in_136",
    ends={
        Property(name="OclExpression138", type=OCL_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="letExp137", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression139: BinaryAssociation = BinaryAssociation(
    name="thenExpression139",
    ends={
        Property(name="OclExpression140", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition141: BinaryAssociation = BinaryAssociation(
    name="condition141",
    ends={
        Property(name="OclExpression142", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp1", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression143: BinaryAssociation = BinaryAssociation(
    name="elseExpression143",
    ends={
        Property(name="OclExpression144", type=OCL_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ifExp3", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source124: BinaryAssociation = BinaryAssociation(
    name="source124",
    ends={
        Property(name="OclExpression125", type=OCL_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProperty", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression147: BinaryAssociation = BinaryAssociation(
    name="initExpression147",
    ends={
        Property(name="OclExpression148", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="initializedVariable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp149: BinaryAssociation = BinaryAssociation(
    name="letExp149",
    ends={
        Property(name="LetExp150", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
baseExp151: BinaryAssociation = BinaryAssociation(
    name="baseExp151",
    ends={
        Property(name="IterateExp", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=IterateExp, multiplicity=Multiplicity(0, 1))
    }
)
variableExp152: BinaryAssociation = BinaryAssociation(
    name="variableExp152",
    ends={
        Property(name="VariableExp", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="referredVariable", type=VariableExp, multiplicity=Multiplicity(0, 9999))
    }
)
loopExpr153: BinaryAssociation = BinaryAssociation(
    name="loopExpr153",
    ends={
        Property(name="LoopExp154", type=OCL_Iterator, multiplicity=Multiplicity(1, 1)),
        Property(name="iterators", type=LoopExp, multiplicity=Multiplicity(0, 1))
    }
)
operation155: BinaryAssociation = BinaryAssociation(
    name="operation155",
    ends={
        Property(name="Operation156", type=OCL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
elementType157: BinaryAssociation = BinaryAssociation(
    name="elementType157",
    ends={
        Property(name="OclType158", type=OCL_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="collectionTypes", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions159: BinaryAssociation = BinaryAssociation(
    name="definitions159",
    ends={
        Property(name="OclContextDefinition", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="context_", type=OclContextDefinition, multiplicity=Multiplicity(0, 1))
    }
)
oclExpression160: BinaryAssociation = BinaryAssociation(
    name="oclExpression160",
    ends={
        Property(name="OclExpression161", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
operation162: BinaryAssociation = BinaryAssociation(
    name="operation162",
    ends={
        Property(name="Operation163", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
mapType2164: BinaryAssociation = BinaryAssociation(
    name="mapType2164",
    ends={
        Property(name="MapType", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="valueType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
attribute165: BinaryAssociation = BinaryAssociation(
    name="attribute165",
    ends={
        Property(name="Attribute167", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type166", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
mapType168: BinaryAssociation = BinaryAssociation(
    name="mapType168",
    ends={
        Property(name="MapType169", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="keyType", type=MapType, multiplicity=Multiplicity(0, 1))
    }
)
type145: BinaryAssociation = BinaryAssociation(
    name="type145",
    ends={
        Property(name="OclType146", type=OCL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclaration", type=OclType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes176: BinaryAssociation = BinaryAssociation(
    name="attributes176",
    ends={
        Property(name="TupleTypeAttribute177", type=OCL_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleType", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type178: BinaryAssociation = BinaryAssociation(
    name="type178",
    ends={
        Property(name="OclType179", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="tupleTypeAttribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tupleType180: BinaryAssociation = BinaryAssociation(
    name="tupleType180",
    ends={
        Property(name="TupleType", type=OCL_TupleTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=TupleType, multiplicity=Multiplicity(1, 1))
    }
)
model181: BinaryAssociation = BinaryAssociation(
    name="model181",
    ends={
        Property(name="OclModel183", type=OCL_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements182", type=OclModel, multiplicity=Multiplicity(1, 1))
    }
)
valueType184: BinaryAssociation = BinaryAssociation(
    name="valueType184",
    ends={
        Property(name="OclType185", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType2", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType186: BinaryAssociation = BinaryAssociation(
    name="keyType186",
    ends={
        Property(name="OclType187", type=OCL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="mapType", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature188: BinaryAssociation = BinaryAssociation(
    name="feature188",
    ends={
        Property(name="OclFeature", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition", type=OclFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_189: BinaryAssociation = BinaryAssociation(
    name="context_189",
    ends={
        Property(name="OclContextDefinition191", type=OCL_OclFeatureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definition190", type=OclContextDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionTypes170: BinaryAssociation = BinaryAssociation(
    name="collectionTypes170",
    ends={
        Property(name="CollectionType", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="elementType", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
tupleTypeAttribute171: BinaryAssociation = BinaryAssociation(
    name="tupleTypeAttribute171",
    ends={
        Property(name="TupleTypeAttribute", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type172", type=TupleTypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclaration173: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration173",
    ends={
        Property(name="VariableDeclaration175", type=OCL_OclType, multiplicity=Multiplicity(1, 1)),
        Property(name="type174", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
initExpression199: BinaryAssociation = BinaryAssociation(
    name="initExpression199",
    ends={
        Property(name="OclExpression200", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAttribute", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type201: BinaryAssociation = BinaryAssociation(
    name="type201",
    ends={
        Property(name="OclType202", type=OCL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters203: BinaryAssociation = BinaryAssociation(
    name="parameters203",
    ends={
        Property(name="Parameter204", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType205: BinaryAssociation = BinaryAssociation(
    name="returnType205",
    ends={
        Property(name="OclType207", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation206", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body208: BinaryAssociation = BinaryAssociation(
    name="body208",
    ends={
        Property(name="OclExpression209", type=OCL_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metamodel210: BinaryAssociation = BinaryAssociation(
    name="metamodel210",
    ends={
        Property(name="OclModel211", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=OclModel, multiplicity=Multiplicity(0, 1))
    }
)
elements212: BinaryAssociation = BinaryAssociation(
    name="elements212",
    ends={
        Property(name="OclModelElement", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model213", type=OclModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
model214: BinaryAssociation = BinaryAssociation(
    name="model214",
    ends={
        Property(name="OclModel215", type=OCL_OclModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=OclModel, multiplicity=Multiplicity(0, 9999))
    }
)
definition192: BinaryAssociation = BinaryAssociation(
    name="definition192",
    ends={
        Property(name="OclFeatureDefinition194", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="context_193", type=OclFeatureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
context_195: BinaryAssociation = BinaryAssociation(
    name="context_195",
    ends={
        Property(name="OclType196", type=OCL_OclContextDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=OclType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition197: BinaryAssociation = BinaryAssociation(
    name="definition197",
    ends={
        Property(name="OclFeatureDefinition198", type=OCL_OclFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=OclFeatureDefinition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ATL_Unit_LocatedElement = Generalization(general=LocatedElement, specific=ATL_Unit)
gen_ATL_Module_Unit = Generalization(general=Unit, specific=ATL_Module)
gen_ATL_ModuleElement_LocatedElement = Generalization(general=LocatedElement, specific=ATL_ModuleElement)
gen_ATL_Helper_ModuleElement = Generalization(general=ModuleElement, specific=ATL_Helper)
gen_ATL_Library_Unit = Generalization(general=Unit, specific=ATL_Library)
gen_ATL_Query_Unit = Generalization(general=Unit, specific=ATL_Query)
gen_ATL_LazyMatchedRule_MatchedRule = Generalization(general=MatchedRule, specific=ATL_LazyMatchedRule)
gen_ATL_CalledRule_Rule = Generalization(general=Rule, specific=ATL_CalledRule)
gen_ATL_InPattern_LocatedElement = Generalization(general=LocatedElement, specific=ATL_InPattern)
gen_ATL_OutPattern_LocatedElement = Generalization(general=LocatedElement, specific=ATL_OutPattern)
gen_ATL_Rule_ModuleElement = Generalization(general=ModuleElement, specific=ATL_Rule)
gen_ATL_MatchedRule_Rule = Generalization(general=Rule, specific=ATL_MatchedRule)
gen_ATL_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=ATL_SimpleOutPatternElement)
gen_ATL_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=ATL_ForEachOutPatternElement)
gen_ATL_Binding_LocatedElement = Generalization(general=LocatedElement, specific=ATL_Binding)
gen_ATL_RuleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=ATL_RuleVariableDeclaration)
gen_ATL_DropPattern_LocatedElement = Generalization(general=LocatedElement, specific=ATL_DropPattern)
gen_ATL_PatternElement_VariableDeclaration = Generalization(general=VariableDeclaration, specific=ATL_PatternElement)
gen_ATL_InPatternElement_PatternElement = Generalization(general=PatternElement, specific=ATL_InPatternElement)
gen_ATL_SimpleInPatternElement_InPatternElement = Generalization(general=InPatternElement, specific=ATL_SimpleInPatternElement)
gen_ATL_OutPatternElement_PatternElement = Generalization(general=PatternElement, specific=ATL_OutPatternElement)
gen_ATL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=ATL_Statement)
gen_ATL_ExpressionStat_Statement = Generalization(general=Statement, specific=ATL_ExpressionStat)
gen_ATL_BindingStat_Statement = Generalization(general=Statement, specific=ATL_BindingStat)
gen_ATL_IfStat_Statement = Generalization(general=Statement, specific=ATL_IfStat)
gen_ATL_ForStat_Statement = Generalization(general=Statement, specific=ATL_ForStat)
gen_ATL_LibraryRef_LocatedElement = Generalization(general=LocatedElement, specific=ATL_LibraryRef)
gen_ATL_ActionBlock_LocatedElement = Generalization(general=LocatedElement, specific=ATL_ActionBlock)
gen_OCL_VariableExp_OclExpression = Generalization(general=OclExpression, specific=OCL_VariableExp)
gen_OCL_SuperExp_OclExpression = Generalization(general=OclExpression, specific=OCL_SuperExp)
gen_OCL_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=OCL_PrimitiveExp)
gen_OCL_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_StringExp)
gen_OCL_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_BooleanExp)
gen_OCL_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=OCL_NumericExp)
gen_OCL_RealExp_NumericExp = Generalization(general=NumericExp, specific=OCL_RealExp)
gen_OCL_OclExpression_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclExpression)
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
gen_OCL_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=OCL_CollectionExp)
gen_OCL_OperatorCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_OperatorCallExp)
gen_OCL_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=OCL_CollectionOperationCallExp)
gen_OCL_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_LoopExp)
gen_OCL_IterateExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IterateExp)
gen_OCL_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=OCL_IteratorExp)
gen_OCL_LetExp_OclExpression = Generalization(general=OclExpression, specific=OCL_LetExp)
gen_OCL_IfExp_OclExpression = Generalization(general=OclExpression, specific=OCL_IfExp)
gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_NavigationOrAttributeCallExp)
gen_OCL_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=OCL_OperationCallExp)
gen_OCL_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Iterator)
gen_OCL_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=OCL_Parameter)
gen_OCL_CollectionType_OclType = Generalization(general=OclType, specific=OCL_CollectionType)
gen_OCL_OclType_OclExpression = Generalization(general=OclExpression, specific=OCL_OclType)
gen_OCL_VariableDeclaration_LocatedElement = Generalization(general=LocatedElement, specific=OCL_VariableDeclaration)
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
gen_OCL_Attribute_OclFeature = Generalization(general=OclFeature, specific=OCL_Attribute)
gen_OCL_Operation_OclFeature = Generalization(general=OclFeature, specific=OCL_Operation)
gen_OCL_OclModel_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclModel)
gen_OCL_OclFeature_LocatedElement = Generalization(general=LocatedElement, specific=OCL_OclFeature)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={ATL_LocatedElement, ATL_Unit, LocatedElement, ATL_Module, OclModel, ModuleElement, ATL_ModuleElement, Module, ATL_Helper, Query, Library, OclFeatureDefinition, LibraryRef, ATL_Library, Unit, Helper, ATL_Query, OclExpression, ATL_LazyMatchedRule, ATL_CalledRule, Parameter_, ATL_InPattern, InPatternElement, ATL_OutPattern, ATL_Rule, OutPattern, ActionBlock, RuleVariableDeclaration, ATL_MatchedRule, Rule, InPattern, MatchedRule, Binding, ATL_SimpleOutPatternElement, ATL_ForEachOutPatternElement, Iterator, ATL_Binding, DropPattern, ATL_RuleVariableDeclaration, OutPatternElement, ATL_DropPattern, ATL_PatternElement, VariableDeclaration, ATL_InPatternElement, PatternElement, ATL_SimpleInPatternElement, ATL_OutPatternElement, ATL_Statement, ATL_ExpressionStat, ATL_BindingStat, ATL_IfStat, ATL_ForStat, ATL_LibraryRef, ATL_ActionBlock, Statement, CollectionExp, LetExp, LoopExp, OperationCallExp, Operation, Attribute, OCL_VariableExp, OCL_SuperExp, OCL_PrimitiveExp, OCL_StringExp, PrimitiveExp, OCL_BooleanExp, OCL_NumericExp, OCL_RealExp, NumericExp, OCL_OclExpression, OclType, IfExp, PropertyCallExp, OCL_BagExp, OCL_OrderedSetExp, OCL_SequenceExp, OCL_SetExp, OCL_TupleExp, TuplePart, OCL_TuplePart, TupleExp, OCL_MapExp, MapElement, OCL_MapElement, MapExp, OCL_EnumLiteralExp, OCL_OclUndefinedExp, OCL_PropertyCallExp, OCL_IntegerExp, OCL_CollectionExp, OCL_OperatorCallExp, OCL_CollectionOperationCallExp, OCL_LoopExp, OCL_IterateExp, OCL_IteratorExp, OCL_LetExp, OCL_IfExp, OCL_NavigationOrAttributeCallExp, OCL_OperationCallExp, IterateExp, VariableExp, OCL_Iterator, OCL_Parameter, OCL_CollectionType, OCL_OclType, OclContextDefinition, MapType, CollectionType, OCL_VariableDeclaration, OCL_Primitive, OCL_StringType, Primitive, OCL_BooleanType, OCL_NumericType, OCL_IntegerType, NumericType, OCL_RealType, OCL_BagType, OCL_OrderedSetType, OCL_SequenceType, OCL_SetType, OCL_OclAnyType, OCL_TupleType, OCL_TupleTypeAttribute, TupleType, OCL_OclModelElement, OCL_MapType, OCL_OclFeatureDefinition, OclFeature, OCL_OclContextDefinition, TupleTypeAttribute, OCL_Attribute, OCL_Operation, OCL_OclModel, OclModelElement, OCL_OclFeature},
    associations={inModels5, outModels6, elements9, module10, query11, library12, definition14, libraries0, helpers1, body2, helpers3, parameters25, elements26, rule27, filter30, rule32, outPattern15, actionBlock16, variables18, inPattern20, children22, superRule23, outPattern46, sourceElement49, bindings51, model52, reverseBindings54, collection56, iterator58, value60, outPatternElement62, dropPattern33, elements35, outPattern37, mapsTo39, inPattern41, models44, expression70, source72, value74, condition77, thenStatements79, elseStatements82, rule64, iterator85, collection87, unit66, statements90, rule67, statements69, collection96, letExp98, loopExp99, parentOperation100, initializedVariable101, ifExp2102, owningOperation104, ifExp1106, owningAttribute108, referredVariable110, type93, ifExp394, appliedProperty95, elements112, tuplePart114, tuple115, elements116, map117, key119, value121, arguments126, body128, iterators130, result132, variable134, in_136, thenExpression139, condition141, elseExpression143, source124, initExpression147, letExp149, baseExp151, variableExp152, loopExpr153, operation155, elementType157, definitions159, oclExpression160, operation162, mapType2164, attribute165, mapType168, type145, attributes176, type178, tupleType180, model181, valueType184, keyType186, feature188, context_189, collectionTypes170, tupleTypeAttribute171, variableDeclaration173, initExpression199, type201, parameters203, returnType205, body208, metamodel210, elements212, model214, definition192, context_195, definition197},
    generalizations={gen_ATL_Unit_LocatedElement, gen_ATL_Module_Unit, gen_ATL_ModuleElement_LocatedElement, gen_ATL_Helper_ModuleElement, gen_ATL_Library_Unit, gen_ATL_Query_Unit, gen_ATL_LazyMatchedRule_MatchedRule, gen_ATL_CalledRule_Rule, gen_ATL_InPattern_LocatedElement, gen_ATL_OutPattern_LocatedElement, gen_ATL_Rule_ModuleElement, gen_ATL_MatchedRule_Rule, gen_ATL_SimpleOutPatternElement_OutPatternElement, gen_ATL_ForEachOutPatternElement_OutPatternElement, gen_ATL_Binding_LocatedElement, gen_ATL_RuleVariableDeclaration_VariableDeclaration, gen_ATL_DropPattern_LocatedElement, gen_ATL_PatternElement_VariableDeclaration, gen_ATL_InPatternElement_PatternElement, gen_ATL_SimpleInPatternElement_InPatternElement, gen_ATL_OutPatternElement_PatternElement, gen_ATL_Statement_LocatedElement, gen_ATL_ExpressionStat_Statement, gen_ATL_BindingStat_Statement, gen_ATL_IfStat_Statement, gen_ATL_ForStat_Statement, gen_ATL_LibraryRef_LocatedElement, gen_ATL_ActionBlock_LocatedElement, gen_OCL_VariableExp_OclExpression, gen_OCL_SuperExp_OclExpression, gen_OCL_PrimitiveExp_OclExpression, gen_OCL_StringExp_PrimitiveExp, gen_OCL_BooleanExp_PrimitiveExp, gen_OCL_NumericExp_PrimitiveExp, gen_OCL_RealExp_NumericExp, gen_OCL_OclExpression_LocatedElement, gen_OCL_BagExp_CollectionExp, gen_OCL_OrderedSetExp_CollectionExp, gen_OCL_SequenceExp_CollectionExp, gen_OCL_SetExp_CollectionExp, gen_OCL_TupleExp_OclExpression, gen_OCL_TuplePart_VariableDeclaration, gen_OCL_MapExp_OclExpression, gen_OCL_MapElement_LocatedElement, gen_OCL_EnumLiteralExp_OclExpression, gen_OCL_OclUndefinedExp_OclExpression, gen_OCL_PropertyCallExp_OclExpression, gen_OCL_IntegerExp_NumericExp, gen_OCL_CollectionExp_OclExpression, gen_OCL_OperatorCallExp_OperationCallExp, gen_OCL_CollectionOperationCallExp_OperationCallExp, gen_OCL_LoopExp_PropertyCallExp, gen_OCL_IterateExp_LoopExp, gen_OCL_IteratorExp_LoopExp, gen_OCL_LetExp_OclExpression, gen_OCL_IfExp_OclExpression, gen_OCL_NavigationOrAttributeCallExp_PropertyCallExp, gen_OCL_OperationCallExp_PropertyCallExp, gen_OCL_Iterator_VariableDeclaration, gen_OCL_Parameter_VariableDeclaration, gen_OCL_CollectionType_OclType, gen_OCL_OclType_OclExpression, gen_OCL_VariableDeclaration_LocatedElement, gen_OCL_Primitive_OclType, gen_OCL_StringType_Primitive, gen_OCL_BooleanType_Primitive, gen_OCL_NumericType_Primitive, gen_OCL_IntegerType_NumericType, gen_OCL_RealType_NumericType, gen_OCL_BagType_CollectionType, gen_OCL_OrderedSetType_CollectionType, gen_OCL_SequenceType_CollectionType, gen_OCL_SetType_CollectionType, gen_OCL_OclAnyType_OclType, gen_OCL_TupleType_OclType, gen_OCL_TupleTypeAttribute_LocatedElement, gen_OCL_OclModelElement_OclType, gen_OCL_MapType_OclType, gen_OCL_OclFeatureDefinition_LocatedElement, gen_OCL_OclContextDefinition_LocatedElement, gen_OCL_Attribute_OclFeature, gen_OCL_Operation_OclFeature, gen_OCL_OclModel_LocatedElement, gen_OCL_OclFeature_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)