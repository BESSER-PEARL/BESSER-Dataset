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
dom_Program = Class(name="dom::Program")
DomElement = Class(name="DomElement")
dom_Import = Class(name="dom::Import")
dom_OperationDefinition = Class(name="dom::OperationDefinition")
dom_DomElement = Class(name="dom::DomElement", is_abstract=True)
dom_AndOperatorExpression = Class(name="dom::AndOperatorExpression")
BinaryOperatorExpression = Class(name="BinaryOperatorExpression")
dom_LiteralExpression = Class(name="dom::LiteralExpression", is_abstract=True)
dom_BooleanExpression = Class(name="dom::BooleanExpression")
PrimitiveExpression = Class(name="PrimitiveExpression")
dom_DivideOperatorExpression = Class(name="dom::DivideOperatorExpression")
dom_EnumerationLiteralExpression = Class(name="dom::EnumerationLiteralExpression")
dom_Block = Class(name="dom::Block")
dom_NameExpression = Class(name="dom::NameExpression")
dom_ModelDeclarationStatement = Class(name="dom::ModelDeclarationStatement")
dom_StringExpression = Class(name="dom::StringExpression")
dom_Statement = Class(name="dom::Statement", is_abstract=True)
dom_Expression = Class(name="dom::Expression", is_abstract=True)
dom_Type = Class(name="dom::Type", is_abstract=True)
dom_OperatorExpression = Class(name="dom::OperatorExpression", is_abstract=True)
Expression = Class(name="Expression")
dom_BinaryOperatorExpression = Class(name="dom::BinaryOperatorExpression", is_abstract=True)
OperatorExpression = Class(name="OperatorExpression")
dom_NegativeOperatorExpression = Class(name="dom::NegativeOperatorExpression")
UnaryOperatorExpression = Class(name="UnaryOperatorExpression")
dom_NotEqualsOperatorExpression = Class(name="dom::NotEqualsOperatorExpression")
dom_NotOperatorExpression = Class(name="dom::NotOperatorExpression")
dom_OrOperatorExpression = Class(name="dom::OrOperatorExpression")
dom_PlusOperatorExpression = Class(name="dom::PlusOperatorExpression")
dom_PropertyCallExpression = Class(name="dom::PropertyCallExpression")
dom_EqualsOperatorExpression = Class(name="dom::EqualsOperatorExpression")
dom_FeatureCallExpression = Class(name="dom::FeatureCallExpression", is_abstract=True)
dom_GreaterThanOperatorExpression = Class(name="dom::GreaterThanOperatorExpression")
dom_GreaterThanOrEqualToOperatorExpression = Class(name="dom::GreaterThanOrEqualToOperatorExpression")
dom_ImpliesOperatorExpression = Class(name="dom::ImpliesOperatorExpression")
dom_IntegerExpression = Class(name="dom::IntegerExpression")
dom_LessThanOperatorExpression = Class(name="dom::LessThanOperatorExpression")
dom_LessThanOrEqualToOperatorExpression = Class(name="dom::LessThanOrEqualToOperatorExpression")
dom_MethodCallExpression = Class(name="dom::MethodCallExpression")
FeatureCallExpression = Class(name="FeatureCallExpression")
dom_MinusOperatorExpression = Class(name="dom::MinusOperatorExpression")
dom_MultiplyOperatorExpression = Class(name="dom::MultiplyOperatorExpression")
dom_UnaryOperatorExpression = Class(name="dom::UnaryOperatorExpression", is_abstract=True)
dom_RealExpression = Class(name="dom::RealExpression")
dom_VariableDeclarationExpression = Class(name="dom::VariableDeclarationExpression")
dom_AnnotationBlock = Class(name="dom::AnnotationBlock")
dom_XorOperatorExpression = Class(name="dom::XorOperatorExpression")
dom_ForStatement = Class(name="dom::ForStatement")
dom_FormalParameterExpression = Class(name="dom::FormalParameterExpression")
dom_AssignmentStatement = Class(name="dom::AssignmentStatement")
Statement = Class(name="Statement")
dom_BreakStatement = Class(name="dom::BreakStatement")
dom_BreakAllStatement = Class(name="dom::BreakAllStatement")
dom_ContinueStatement = Class(name="dom::ContinueStatement")
dom_DeleteStatement = Class(name="dom::DeleteStatement")
dom_SwitchCaseDefaultStatement = Class(name="dom::SwitchCaseDefaultStatement")
dom_SwitchCaseStatement = Class(name="dom::SwitchCaseStatement", is_abstract=True)
dom_WhileStatement = Class(name="dom::WhileStatement")
dom_IfStatement = Class(name="dom::IfStatement")
dom_ReturnStatement = Class(name="dom::ReturnStatement")
dom_SwitchStatement = Class(name="dom::SwitchStatement")
dom_SwitchCaseExpressionStatement = Class(name="dom::SwitchCaseExpressionStatement")
dom_ExpressionStatement = Class(name="dom::ExpressionStatement")
dom_ModelDeclarationParameter = Class(name="dom::ModelDeclarationParameter")
dom_FOLMethodCallExpression = Class(name="dom::FOLMethodCallExpression")
dom_SequenceExpression = Class(name="dom::SequenceExpression")
dom_OrderedSetExpression = Class(name="dom::OrderedSetExpression")
dom_MapExpression = Class(name="dom::MapExpression")
dom_KeyValue = Class(name="dom::KeyValue")
SwitchCaseStatement = Class(name="SwitchCaseStatement")
dom_PrimitiveExpression = Class(name="dom::PrimitiveExpression", is_abstract=True)
LiteralExpression = Class(name="LiteralExpression")
dom_CollectionExpression = Class(name="dom::CollectionExpression", is_abstract=True)
dom_CollectionInitValue = Class(name="dom::CollectionInitValue", is_abstract=True)
dom_SetExpression = Class(name="dom::SetExpression")
CollectionExpression = Class(name="CollectionExpression")
dom_BagExpression = Class(name="dom::BagExpression")
dom_ExecutableAnnotation = Class(name="dom::ExecutableAnnotation")
Annotation = Class(name="Annotation")
dom_SimpleAnnotation = Class(name="dom::SimpleAnnotation")
dom_AnyType = Class(name="dom::AnyType")
Type = Class(name="Type")
dom_CollectionType = Class(name="dom::CollectionType", is_abstract=True)
dom_PrimitiveType = Class(name="dom::PrimitiveType", is_abstract=True)
dom_BooleanType = Class(name="dom::BooleanType")
PrimitiveType = Class(name="PrimitiveType")
dom_IntegerType = Class(name="dom::IntegerType")
dom_RealType = Class(name="dom::RealType")
dom_StringType = Class(name="dom::StringType")
dom_SetType = Class(name="dom::SetType")
CollectionType = Class(name="CollectionType")
dom_BagType = Class(name="dom::BagType")
dom_SequenceType = Class(name="dom::SequenceType")
dom_OrderedSetType = Class(name="dom::OrderedSetType")
dom_MapType = Class(name="dom::MapType")
dom_Annotation = Class(name="dom::Annotation", is_abstract=True)
dom_SpecialNameExpression = Class(name="dom::SpecialNameExpression")
NameExpression = Class(name="NameExpression")
dom_ModelElementType = Class(name="dom::ModelElementType")
dom_ModelElementTypeExpression = Class(name="dom::ModelElementTypeExpression")
dom_ShortModelDeclarationExpression = Class(name="dom::ShortModelDeclarationExpression")
dom_NativeType = Class(name="dom::NativeType")
dom_ModelExpression = Class(name="dom::ModelExpression")
CollectionInitValue = Class(name="CollectionInitValue")
dom_ExpRange = Class(name="dom::ExpRange")
dom_ThrowStatement = Class(name="dom::ThrowStatement")
dom_AbortStatement = Class(name="dom::AbortStatement")
dom_TransactionStatement = Class(name="dom::TransactionStatement")
dom_ExprList = Class(name="dom::ExprList")
dom_NewExpression = Class(name="dom::NewExpression")
dom_SpecialAssignmentStatement = Class(name="dom::SpecialAssignmentStatement")
AssignmentStatement = Class(name="AssignmentStatement")

# dom_Program class attributes and methods

# DomElement class attributes and methods

# dom_Import class attributes and methods

# dom_OperationDefinition class attributes and methods

# dom_DomElement class attributes and methods
dom_DomElement_line: Property = Property(name="line", type=IntegerType)
dom_DomElement_column: Property = Property(name="column", type=IntegerType)
dom_DomElement.attributes={dom_DomElement_column, dom_DomElement_line}

# dom_AndOperatorExpression class attributes and methods

# BinaryOperatorExpression class attributes and methods

# dom_LiteralExpression class attributes and methods

# dom_BooleanExpression class attributes and methods
dom_BooleanExpression_val: Property = Property(name="val", type=BooleanType)
dom_BooleanExpression.attributes={dom_BooleanExpression_val}

# PrimitiveExpression class attributes and methods

# dom_DivideOperatorExpression class attributes and methods

# dom_EnumerationLiteralExpression class attributes and methods

# dom_Block class attributes and methods

# dom_NameExpression class attributes and methods
dom_NameExpression_name: Property = Property(name="name", type=StringType)
dom_NameExpression.attributes={dom_NameExpression_name}

# dom_ModelDeclarationStatement class attributes and methods

# dom_StringExpression class attributes and methods
dom_StringExpression_val: Property = Property(name="val", type=StringType)
dom_StringExpression.attributes={dom_StringExpression_val}

# dom_Statement class attributes and methods

# dom_Expression class attributes and methods

# dom_Type class attributes and methods

# dom_OperatorExpression class attributes and methods

# Expression class attributes and methods

# dom_BinaryOperatorExpression class attributes and methods

# OperatorExpression class attributes and methods

# dom_NegativeOperatorExpression class attributes and methods

# UnaryOperatorExpression class attributes and methods

# dom_NotEqualsOperatorExpression class attributes and methods

# dom_NotOperatorExpression class attributes and methods

# dom_OrOperatorExpression class attributes and methods

# dom_PlusOperatorExpression class attributes and methods

# dom_PropertyCallExpression class attributes and methods

# dom_EqualsOperatorExpression class attributes and methods

# dom_FeatureCallExpression class attributes and methods

# dom_GreaterThanOperatorExpression class attributes and methods

# dom_GreaterThanOrEqualToOperatorExpression class attributes and methods

# dom_ImpliesOperatorExpression class attributes and methods

# dom_IntegerExpression class attributes and methods
dom_IntegerExpression_val: Property = Property(name="val", type=IntegerType)
dom_IntegerExpression.attributes={dom_IntegerExpression_val}

# dom_LessThanOperatorExpression class attributes and methods

# dom_LessThanOrEqualToOperatorExpression class attributes and methods

# dom_MethodCallExpression class attributes and methods

# FeatureCallExpression class attributes and methods

# dom_MinusOperatorExpression class attributes and methods

# dom_MultiplyOperatorExpression class attributes and methods

# dom_UnaryOperatorExpression class attributes and methods

# dom_RealExpression class attributes and methods
dom_RealExpression_val: Property = Property(name="val", type=FloatType)
dom_RealExpression.attributes={dom_RealExpression_val}

# dom_VariableDeclarationExpression class attributes and methods

# dom_AnnotationBlock class attributes and methods

# dom_XorOperatorExpression class attributes and methods

# dom_ForStatement class attributes and methods

# dom_FormalParameterExpression class attributes and methods

# dom_AssignmentStatement class attributes and methods

# Statement class attributes and methods

# dom_BreakStatement class attributes and methods

# dom_BreakAllStatement class attributes and methods

# dom_ContinueStatement class attributes and methods

# dom_DeleteStatement class attributes and methods

# dom_SwitchCaseDefaultStatement class attributes and methods

# dom_SwitchCaseStatement class attributes and methods

# dom_WhileStatement class attributes and methods

# dom_IfStatement class attributes and methods

# dom_ReturnStatement class attributes and methods

# dom_SwitchStatement class attributes and methods

# dom_SwitchCaseExpressionStatement class attributes and methods

# dom_ExpressionStatement class attributes and methods

# dom_ModelDeclarationParameter class attributes and methods

# dom_FOLMethodCallExpression class attributes and methods

# dom_SequenceExpression class attributes and methods

# dom_OrderedSetExpression class attributes and methods

# dom_MapExpression class attributes and methods

# dom_KeyValue class attributes and methods

# SwitchCaseStatement class attributes and methods

# dom_PrimitiveExpression class attributes and methods

# LiteralExpression class attributes and methods

# dom_CollectionExpression class attributes and methods

# dom_CollectionInitValue class attributes and methods

# dom_SetExpression class attributes and methods

# CollectionExpression class attributes and methods

# dom_BagExpression class attributes and methods

# dom_ExecutableAnnotation class attributes and methods

# Annotation class attributes and methods

# dom_SimpleAnnotation class attributes and methods

# dom_AnyType class attributes and methods

# Type class attributes and methods

# dom_CollectionType class attributes and methods

# dom_PrimitiveType class attributes and methods

# dom_BooleanType class attributes and methods

# PrimitiveType class attributes and methods

# dom_IntegerType class attributes and methods

# dom_RealType class attributes and methods

# dom_StringType class attributes and methods

# dom_SetType class attributes and methods

# CollectionType class attributes and methods

# dom_BagType class attributes and methods

# dom_SequenceType class attributes and methods

# dom_OrderedSetType class attributes and methods

# dom_MapType class attributes and methods

# dom_Annotation class attributes and methods

# dom_SpecialNameExpression class attributes and methods

# NameExpression class attributes and methods

# dom_ModelElementType class attributes and methods

# dom_ModelElementTypeExpression class attributes and methods

# dom_ShortModelDeclarationExpression class attributes and methods

# dom_NativeType class attributes and methods

# dom_ModelExpression class attributes and methods

# CollectionInitValue class attributes and methods

# dom_ExpRange class attributes and methods

# dom_ThrowStatement class attributes and methods

# dom_AbortStatement class attributes and methods

# dom_TransactionStatement class attributes and methods

# dom_ExprList class attributes and methods

# dom_NewExpression class attributes and methods

# dom_SpecialAssignmentStatement class attributes and methods

# AssignmentStatement class attributes and methods

# Relationships
container1: BinaryAssociation = BinaryAssociation(
    name="container1",
    ends={
        Property(name="dom_DomElement", type=dom_DomElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DomElement0", type=dom_DomElement, multiplicity=Multiplicity(0, 1))
    }
)
imports2: BinaryAssociation = BinaryAssociation(
    name="imports2",
    ends={
        Property(name="dom_Import", type=dom_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Program", type=dom_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations3: BinaryAssociation = BinaryAssociation(
    name="operations3",
    ends={
        Property(name="dom_OperationDefinition", type=dom_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Program4", type=dom_OperationDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs16: BinaryAssociation = BinaryAssociation(
    name="lhs16",
    ends={
        Property(name="dom_BinaryOperatorExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="dom_Expression17", type=dom_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1))
    }
)
rhs18: BinaryAssociation = BinaryAssociation(
    name="rhs18",
    ends={
        Property(name="dom_Expression20", type=dom_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_BinaryOperatorExpression19", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumeration21: BinaryAssociation = BinaryAssociation(
    name="enumeration21",
    ends={
        Property(name="dom_NameExpression22", type=dom_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_EnumerationLiteralExpression", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block5: BinaryAssociation = BinaryAssociation(
    name="block5",
    ends={
        Property(name="dom_Block", type=dom_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Program6", type=dom_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name7: BinaryAssociation = BinaryAssociation(
    name="name7",
    ends={
        Property(name="dom_NameExpression", type=dom_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Program8", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelDeclarations9: BinaryAssociation = BinaryAssociation(
    name="modelDeclarations9",
    ends={
        Property(name="dom_ModelDeclarationStatement", type=dom_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Program10", type=dom_ModelDeclarationStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imported11: BinaryAssociation = BinaryAssociation(
    name="imported11",
    ends={
        Property(name="dom_StringExpression", type=dom_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Import12", type=dom_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedType13: BinaryAssociation = BinaryAssociation(
    name="resolvedType13",
    ends={
        Property(name="dom_Type", type=dom_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Expression", type=dom_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements14: BinaryAssociation = BinaryAssociation(
    name="statements14",
    ends={
        Property(name="dom_Statement", type=dom_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Block15", type=dom_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr38: BinaryAssociation = BinaryAssociation(
    name="expr38",
    ends={
        Property(name="dom_UnaryOperatorExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="dom_Expression39", type=dom_UnaryOperatorExpression, multiplicity=Multiplicity(1, 1))
    }
)
property40: BinaryAssociation = BinaryAssociation(
    name="property40",
    ends={
        Property(name="dom_NameExpression41", type=dom_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_PropertyCallExpression", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extended42: BinaryAssociation = BinaryAssociation(
    name="extended42",
    ends={
        Property(name="dom_BooleanExpression44", type=dom_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_PropertyCallExpression43", type=dom_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literal23: BinaryAssociation = BinaryAssociation(
    name="literal23",
    ends={
        Property(name="dom_NameExpression25", type=dom_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_EnumerationLiteralExpression24", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model26: BinaryAssociation = BinaryAssociation(
    name="model26",
    ends={
        Property(name="dom_NameExpression28", type=dom_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_EnumerationLiteralExpression27", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target29: BinaryAssociation = BinaryAssociation(
    name="target29",
    ends={
        Property(name="dom_Expression30", type=dom_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FeatureCallExpression", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isArrow31: BinaryAssociation = BinaryAssociation(
    name="isArrow31",
    ends={
        Property(name="dom_BooleanExpression", type=dom_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FeatureCallExpression32", type=dom_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments33: BinaryAssociation = BinaryAssociation(
    name="arguments33",
    ends={
        Property(name="dom_Expression34", type=dom_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_MethodCallExpression", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method35: BinaryAssociation = BinaryAssociation(
    name="method35",
    ends={
        Property(name="dom_NameExpression37", type=dom_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_MethodCallExpression36", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType56: BinaryAssociation = BinaryAssociation(
    name="returnType56",
    ends={
        Property(name="dom_OperationDefinition57", type=dom_Type, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="dom_Type58", type=dom_OperationDefinition, multiplicity=Multiplicity(1, 1))
    }
)
annotationBlock59: BinaryAssociation = BinaryAssociation(
    name="annotationBlock59",
    ends={
        Property(name="dom_AnnotationBlock", type=dom_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_OperationDefinition60", type=dom_AnnotationBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body61: BinaryAssociation = BinaryAssociation(
    name="body61",
    ends={
        Property(name="dom_Block63", type=dom_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_OperationDefinition62", type=dom_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name64: BinaryAssociation = BinaryAssociation(
    name="name64",
    ends={
        Property(name="dom_NameExpression66", type=dom_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_OperationDefinition65", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name45: BinaryAssociation = BinaryAssociation(
    name="name45",
    ends={
        Property(name="dom_NameExpression46", type=dom_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_VariableDeclarationExpression", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
create47: BinaryAssociation = BinaryAssociation(
    name="create47",
    ends={
        Property(name="dom_BooleanExpression49", type=dom_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_VariableDeclarationExpression48", type=dom_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters50: BinaryAssociation = BinaryAssociation(
    name="parameters50",
    ends={
        Property(name="dom_Expression52", type=dom_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_VariableDeclarationExpression51", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextType53: BinaryAssociation = BinaryAssociation(
    name="contextType53",
    ends={
        Property(name="dom_Type55", type=dom_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_OperationDefinition54", type=dom_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterator76: BinaryAssociation = BinaryAssociation(
    name="iterator76",
    ends={
        Property(name="dom_FormalParameterExpression77", type=dom_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ForStatement", type=dom_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterated78: BinaryAssociation = BinaryAssociation(
    name="iterated78",
    ends={
        Property(name="dom_Expression80", type=dom_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ForStatement79", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body81: BinaryAssociation = BinaryAssociation(
    name="body81",
    ends={
        Property(name="dom_Block83", type=dom_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ForStatement82", type=dom_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters67: BinaryAssociation = BinaryAssociation(
    name="parameters67",
    ends={
        Property(name="dom_FormalParameterExpression", type=dom_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_OperationDefinition68", type=dom_FormalParameterExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs69: BinaryAssociation = BinaryAssociation(
    name="lhs69",
    ends={
        Property(name="dom_Expression70", type=dom_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AssignmentStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs71: BinaryAssociation = BinaryAssociation(
    name="rhs71",
    ends={
        Property(name="dom_Expression73", type=dom_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AssignmentStatement72", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
deleted74: BinaryAssociation = BinaryAssociation(
    name="deleted74",
    ends={
        Property(name="dom_Expression75", type=dom_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DeleteStatement", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default98: BinaryAssociation = BinaryAssociation(
    name="default98",
    ends={
        Property(name="dom_SwitchCaseDefaultStatement", type=dom_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SwitchStatement99", type=dom_SwitchCaseDefaultStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body100: BinaryAssociation = BinaryAssociation(
    name="body100",
    ends={
        Property(name="dom_Block101", type=dom_SwitchCaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SwitchCaseStatement", type=dom_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition84: BinaryAssociation = BinaryAssociation(
    name="condition84",
    ends={
        Property(name="dom_Expression85", type=dom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_IfStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifBody86: BinaryAssociation = BinaryAssociation(
    name="ifBody86",
    ends={
        Property(name="dom_Block88", type=dom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_IfStatement87", type=dom_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBody89: BinaryAssociation = BinaryAssociation(
    name="elseBody89",
    ends={
        Property(name="dom_Block91", type=dom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_IfStatement90", type=dom_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returned92: BinaryAssociation = BinaryAssociation(
    name="returned92",
    ends={
        Property(name="dom_Expression93", type=dom_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ReturnStatement", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression94: BinaryAssociation = BinaryAssociation(
    name="expression94",
    ends={
        Property(name="dom_Expression95", type=dom_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SwitchStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases96: BinaryAssociation = BinaryAssociation(
    name="cases96",
    ends={
        Property(name="dom_SwitchCaseExpressionStatement", type=dom_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SwitchStatement97", type=dom_SwitchCaseExpressionStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterators118: BinaryAssociation = BinaryAssociation(
    name="iterators118",
    ends={
        Property(name="dom_FormalParameterExpression119", type=dom_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FOLMethodCallExpression", type=dom_FormalParameterExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
conditions120: BinaryAssociation = BinaryAssociation(
    name="conditions120",
    ends={
        Property(name="dom_Expression122", type=dom_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FOLMethodCallExpression121", type=dom_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
method123: BinaryAssociation = BinaryAssociation(
    name="method123",
    ends={
        Property(name="dom_NameExpression125", type=dom_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FOLMethodCallExpression124", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition102: BinaryAssociation = BinaryAssociation(
    name="condition102",
    ends={
        Property(name="dom_Expression103", type=dom_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_WhileStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body104: BinaryAssociation = BinaryAssociation(
    name="body104",
    ends={
        Property(name="dom_Block106", type=dom_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_WhileStatement105", type=dom_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name107: BinaryAssociation = BinaryAssociation(
    name="name107",
    ends={
        Property(name="dom_NameExpression109", type=dom_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ModelDeclarationStatement108", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alias110: BinaryAssociation = BinaryAssociation(
    name="alias110",
    ends={
        Property(name="dom_NameExpression112", type=dom_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ModelDeclarationStatement111", type=dom_NameExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
driver113: BinaryAssociation = BinaryAssociation(
    name="driver113",
    ends={
        Property(name="dom_NameExpression115", type=dom_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ModelDeclarationStatement114", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters116: BinaryAssociation = BinaryAssociation(
    name="parameters116",
    ends={
        Property(name="dom_ModelDeclarationParameter", type=dom_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ModelDeclarationStatement117", type=dom_ModelDeclarationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyValues135: BinaryAssociation = BinaryAssociation(
    name="keyValues135",
    ends={
        Property(name="dom_KeyValue", type=dom_MapExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_MapExpression", type=dom_KeyValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="dom_Expression127", type=dom_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ExpressionStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression128: BinaryAssociation = BinaryAssociation(
    name="expression128",
    ends={
        Property(name="dom_Expression130", type=dom_SwitchCaseExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SwitchCaseExpressionStatement129", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterList131: BinaryAssociation = BinaryAssociation(
    name="parameterList131",
    ends={
        Property(name="dom_CollectionInitValue", type=dom_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CollectionExpression", type=dom_CollectionInitValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contentType132: BinaryAssociation = BinaryAssociation(
    name="contentType132",
    ends={
        Property(name="dom_Type134", type=dom_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CollectionExpression133", type=dom_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression138: BinaryAssociation = BinaryAssociation(
    name="expression138",
    ends={
        Property(name="dom_Expression139", type=dom_ExecutableAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ExecutableAnnotation", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values140: BinaryAssociation = BinaryAssociation(
    name="values140",
    ends={
        Property(name="dom_StringExpression141", type=dom_SimpleAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SimpleAnnotation", type=dom_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name136: BinaryAssociation = BinaryAssociation(
    name="name136",
    ends={
        Property(name="dom_NameExpression137", type=dom_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Annotation", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simpleAnnotations151: BinaryAssociation = BinaryAssociation(
    name="simpleAnnotations151",
    ends={
        Property(name="dom_SimpleAnnotation153", type=dom_AnnotationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AnnotationBlock152", type=dom_SimpleAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executableAnnotations154: BinaryAssociation = BinaryAssociation(
    name="executableAnnotations154",
    ends={
        Property(name="dom_ExecutableAnnotation156", type=dom_AnnotationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AnnotationBlock155", type=dom_ExecutableAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name157: BinaryAssociation = BinaryAssociation(
    name="name157",
    ends={
        Property(name="dom_NameExpression159", type=dom_ModelDeclarationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ModelDeclarationParameter158", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
key142: BinaryAssociation = BinaryAssociation(
    name="key142",
    ends={
        Property(name="dom_Expression144", type=dom_KeyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_KeyValue143", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value145: BinaryAssociation = BinaryAssociation(
    name="value145",
    ends={
        Property(name="dom_Expression147", type=dom_KeyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_KeyValue146", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression148: BinaryAssociation = BinaryAssociation(
    name="expression148",
    ends={
        Property(name="dom_ModelElementTypeExpression", type=dom_ModelElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ModelElementType", type=dom_ModelElementTypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nativeExpression149: BinaryAssociation = BinaryAssociation(
    name="nativeExpression149",
    ends={
        Property(name="dom_StringExpression150", type=dom_NativeType, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_NativeType", type=dom_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions173: BinaryAssociation = BinaryAssociation(
    name="expressions173",
    ends={
        Property(name="dom_Expression174", type=dom_ExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ExprList", type=dom_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
start175: BinaryAssociation = BinaryAssociation(
    name="start175",
    ends={
        Property(name="dom_Expression176", type=dom_ExpRange, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ExpRange", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value160: BinaryAssociation = BinaryAssociation(
    name="value160",
    ends={
        Property(name="dom_StringExpression162", type=dom_ModelDeclarationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ModelDeclarationParameter161", type=dom_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thrown163: BinaryAssociation = BinaryAssociation(
    name="thrown163",
    ends={
        Property(name="dom_Expression164", type=dom_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ThrowStatement", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body165: BinaryAssociation = BinaryAssociation(
    name="body165",
    ends={
        Property(name="dom_Block166", type=dom_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_TransactionStatement", type=dom_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
names167: BinaryAssociation = BinaryAssociation(
    name="names167",
    ends={
        Property(name="dom_NameExpression169", type=dom_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_TransactionStatement168", type=dom_NameExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name170: BinaryAssociation = BinaryAssociation(
    name="name170",
    ends={
        Property(name="dom_NameExpression172", type=dom_FormalParameterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FormalParameterExpression171", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end177: BinaryAssociation = BinaryAssociation(
    name="end177",
    ends={
        Property(name="dom_Expression179", type=dom_ExpRange, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ExpRange178", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters180: BinaryAssociation = BinaryAssociation(
    name="parameters180",
    ends={
        Property(name="dom_Expression181", type=dom_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_NewExpression", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model182: BinaryAssociation = BinaryAssociation(
    name="model182",
    ends={
        Property(name="dom_NameExpression184", type=dom_ModelElementTypeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ModelElementTypeExpression183", type=dom_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element185: BinaryAssociation = BinaryAssociation(
    name="element185",
    ends={
        Property(name="dom_NameExpression187", type=dom_ModelElementTypeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ModelElementTypeExpression186", type=dom_NameExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resolvedModelDeclaration188: BinaryAssociation = BinaryAssociation(
    name="resolvedModelDeclaration188",
    ends={
        Property(name="dom_ModelDeclarationStatement190", type=dom_ModelElementTypeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ModelElementTypeExpression189", type=dom_ModelDeclarationStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dom_Program_DomElement = Generalization(general=DomElement, specific=dom_Program)
gen_dom_AndOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_AndOperatorExpression)
gen_dom_LiteralExpression_Expression = Generalization(general=Expression, specific=dom_LiteralExpression)
gen_dom_BooleanExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=dom_BooleanExpression)
gen_dom_DivideOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_DivideOperatorExpression)
gen_dom_EnumerationLiteralExpression_Expression = Generalization(general=Expression, specific=dom_EnumerationLiteralExpression)
gen_dom_Import_DomElement = Generalization(general=DomElement, specific=dom_Import)
gen_dom_Statement_DomElement = Generalization(general=DomElement, specific=dom_Statement)
gen_dom_Expression_DomElement = Generalization(general=DomElement, specific=dom_Expression)
gen_dom_Block_DomElement = Generalization(general=DomElement, specific=dom_Block)
gen_dom_OperatorExpression_Expression = Generalization(general=Expression, specific=dom_OperatorExpression)
gen_dom_BinaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=dom_BinaryOperatorExpression)
gen_dom_NegativeOperatorExpression_UnaryOperatorExpression = Generalization(general=UnaryOperatorExpression, specific=dom_NegativeOperatorExpression)
gen_dom_NotEqualsOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_NotEqualsOperatorExpression)
gen_dom_NotOperatorExpression_UnaryOperatorExpression = Generalization(general=UnaryOperatorExpression, specific=dom_NotOperatorExpression)
gen_dom_OrOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_OrOperatorExpression)
gen_dom_PlusOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_PlusOperatorExpression)
gen_dom_PropertyCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=dom_PropertyCallExpression)
gen_dom_EqualsOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_EqualsOperatorExpression)
gen_dom_FeatureCallExpression_Expression = Generalization(general=Expression, specific=dom_FeatureCallExpression)
gen_dom_GreaterThanOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_GreaterThanOperatorExpression)
gen_dom_GreaterThanOrEqualToOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_GreaterThanOrEqualToOperatorExpression)
gen_dom_ImpliesOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_ImpliesOperatorExpression)
gen_dom_IntegerExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=dom_IntegerExpression)
gen_dom_LessThanOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_LessThanOperatorExpression)
gen_dom_LessThanOrEqualToOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_LessThanOrEqualToOperatorExpression)
gen_dom_MethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=dom_MethodCallExpression)
gen_dom_MinusOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_MinusOperatorExpression)
gen_dom_MultiplyOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_MultiplyOperatorExpression)
gen_dom_NameExpression_Expression = Generalization(general=Expression, specific=dom_NameExpression)
gen_dom_UnaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=dom_UnaryOperatorExpression)
gen_dom_RealExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=dom_RealExpression)
gen_dom_StringExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=dom_StringExpression)
gen_dom_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=dom_VariableDeclarationExpression)
gen_dom_XorOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=dom_XorOperatorExpression)
gen_dom_OperationDefinition_DomElement = Generalization(general=DomElement, specific=dom_OperationDefinition)
gen_dom_ForStatement_Statement = Generalization(general=Statement, specific=dom_ForStatement)
gen_dom_AssignmentStatement_Statement = Generalization(general=Statement, specific=dom_AssignmentStatement)
gen_dom_BreakStatement_Statement = Generalization(general=Statement, specific=dom_BreakStatement)
gen_dom_BreakAllStatement_Statement = Generalization(general=Statement, specific=dom_BreakAllStatement)
gen_dom_ContinueStatement_Statement = Generalization(general=Statement, specific=dom_ContinueStatement)
gen_dom_DeleteStatement_Statement = Generalization(general=Statement, specific=dom_DeleteStatement)
gen_dom_SwitchCaseStatement_Statement = Generalization(general=Statement, specific=dom_SwitchCaseStatement)
gen_dom_WhileStatement_Statement = Generalization(general=Statement, specific=dom_WhileStatement)
gen_dom_IfStatement_Statement = Generalization(general=Statement, specific=dom_IfStatement)
gen_dom_ReturnStatement_Statement = Generalization(general=Statement, specific=dom_ReturnStatement)
gen_dom_SwitchStatement_Statement = Generalization(general=Statement, specific=dom_SwitchStatement)
gen_dom_ModelDeclarationStatement_Statement = Generalization(general=Statement, specific=dom_ModelDeclarationStatement)
gen_dom_FOLMethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=dom_FOLMethodCallExpression)
gen_dom_SequenceExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=dom_SequenceExpression)
gen_dom_OrderedSetExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=dom_OrderedSetExpression)
gen_dom_MapExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=dom_MapExpression)
gen_dom_Type_DomElement = Generalization(general=DomElement, specific=dom_Type)
gen_dom_ExpressionStatement_Statement = Generalization(general=Statement, specific=dom_ExpressionStatement)
gen_dom_SwitchCaseDefaultStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=dom_SwitchCaseDefaultStatement)
gen_dom_SwitchCaseExpressionStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=dom_SwitchCaseExpressionStatement)
gen_dom_PrimitiveExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=dom_PrimitiveExpression)
gen_dom_CollectionExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=dom_CollectionExpression)
gen_dom_SetExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=dom_SetExpression)
gen_dom_BagExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=dom_BagExpression)
gen_dom_ExecutableAnnotation_Annotation = Generalization(general=Annotation, specific=dom_ExecutableAnnotation)
gen_dom_SimpleAnnotation_Annotation = Generalization(general=Annotation, specific=dom_SimpleAnnotation)
gen_dom_AnyType_Type = Generalization(general=Type, specific=dom_AnyType)
gen_dom_CollectionType_Type = Generalization(general=Type, specific=dom_CollectionType)
gen_dom_PrimitiveType_Type = Generalization(general=Type, specific=dom_PrimitiveType)
gen_dom_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=dom_BooleanType)
gen_dom_IntegerType_PrimitiveType = Generalization(general=PrimitiveType, specific=dom_IntegerType)
gen_dom_RealType_PrimitiveType = Generalization(general=PrimitiveType, specific=dom_RealType)
gen_dom_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=dom_StringType)
gen_dom_SetType_CollectionType = Generalization(general=CollectionType, specific=dom_SetType)
gen_dom_BagType_CollectionType = Generalization(general=CollectionType, specific=dom_BagType)
gen_dom_SequenceType_CollectionType = Generalization(general=CollectionType, specific=dom_SequenceType)
gen_dom_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=dom_OrderedSetType)
gen_dom_MapType_Type = Generalization(general=Type, specific=dom_MapType)
gen_dom_Annotation_DomElement = Generalization(general=DomElement, specific=dom_Annotation)
gen_dom_ModelDeclarationParameter_DomElement = Generalization(general=DomElement, specific=dom_ModelDeclarationParameter)
gen_dom_KeyValue_DomElement = Generalization(general=DomElement, specific=dom_KeyValue)
gen_dom_SpecialNameExpression_NameExpression = Generalization(general=NameExpression, specific=dom_SpecialNameExpression)
gen_dom_ModelElementType_Type = Generalization(general=Type, specific=dom_ModelElementType)
gen_dom_NativeType_Type = Generalization(general=Type, specific=dom_NativeType)
gen_dom_ModelExpression_NameExpression = Generalization(general=NameExpression, specific=dom_ModelExpression)
gen_dom_AnnotationBlock_DomElement = Generalization(general=DomElement, specific=dom_AnnotationBlock)
gen_dom_ExprList_CollectionInitValue = Generalization(general=CollectionInitValue, specific=dom_ExprList)
gen_dom_ExpRange_CollectionInitValue = Generalization(general=CollectionInitValue, specific=dom_ExpRange)
gen_dom_ThrowStatement_Statement = Generalization(general=Statement, specific=dom_ThrowStatement)
gen_dom_AbortStatement_Statement = Generalization(general=Statement, specific=dom_AbortStatement)
gen_dom_TransactionStatement_Statement = Generalization(general=Statement, specific=dom_TransactionStatement)
gen_dom_FormalParameterExpression_Expression = Generalization(general=Expression, specific=dom_FormalParameterExpression)
gen_dom_CollectionInitValue_DomElement = Generalization(general=DomElement, specific=dom_CollectionInitValue)
gen_dom_NewExpression_Expression = Generalization(general=Expression, specific=dom_NewExpression)
gen_dom_ModelElementTypeExpression_Expression = Generalization(general=Expression, specific=dom_ModelElementTypeExpression)
gen_dom_SpecialAssignmentStatement_AssignmentStatement = Generalization(general=AssignmentStatement, specific=dom_SpecialAssignmentStatement)

# Domain Model
domain_model = DomainModel(
    name="dom",
    types={dom_Program, DomElement, dom_Import, dom_OperationDefinition, dom_DomElement, dom_AndOperatorExpression, BinaryOperatorExpression, dom_LiteralExpression, dom_BooleanExpression, PrimitiveExpression, dom_DivideOperatorExpression, dom_EnumerationLiteralExpression, dom_Block, dom_NameExpression, dom_ModelDeclarationStatement, dom_StringExpression, dom_Statement, dom_Expression, dom_Type, dom_OperatorExpression, Expression, dom_BinaryOperatorExpression, OperatorExpression, dom_NegativeOperatorExpression, UnaryOperatorExpression, dom_NotEqualsOperatorExpression, dom_NotOperatorExpression, dom_OrOperatorExpression, dom_PlusOperatorExpression, dom_PropertyCallExpression, dom_EqualsOperatorExpression, dom_FeatureCallExpression, dom_GreaterThanOperatorExpression, dom_GreaterThanOrEqualToOperatorExpression, dom_ImpliesOperatorExpression, dom_IntegerExpression, dom_LessThanOperatorExpression, dom_LessThanOrEqualToOperatorExpression, dom_MethodCallExpression, FeatureCallExpression, dom_MinusOperatorExpression, dom_MultiplyOperatorExpression, dom_UnaryOperatorExpression, dom_RealExpression, dom_VariableDeclarationExpression, dom_AnnotationBlock, dom_XorOperatorExpression, dom_ForStatement, dom_FormalParameterExpression, dom_AssignmentStatement, Statement, dom_BreakStatement, dom_BreakAllStatement, dom_ContinueStatement, dom_DeleteStatement, dom_SwitchCaseDefaultStatement, dom_SwitchCaseStatement, dom_WhileStatement, dom_IfStatement, dom_ReturnStatement, dom_SwitchStatement, dom_SwitchCaseExpressionStatement, dom_ExpressionStatement, dom_ModelDeclarationParameter, dom_FOLMethodCallExpression, dom_SequenceExpression, dom_OrderedSetExpression, dom_MapExpression, dom_KeyValue, SwitchCaseStatement, dom_PrimitiveExpression, LiteralExpression, dom_CollectionExpression, dom_CollectionInitValue, dom_SetExpression, CollectionExpression, dom_BagExpression, dom_ExecutableAnnotation, Annotation, dom_SimpleAnnotation, dom_AnyType, Type, dom_CollectionType, dom_PrimitiveType, dom_BooleanType, PrimitiveType, dom_IntegerType, dom_RealType, dom_StringType, dom_SetType, CollectionType, dom_BagType, dom_SequenceType, dom_OrderedSetType, dom_MapType, dom_Annotation, dom_SpecialNameExpression, NameExpression, dom_ModelElementType, dom_ModelElementTypeExpression, dom_ShortModelDeclarationExpression, dom_NativeType, dom_ModelExpression, CollectionInitValue, dom_ExpRange, dom_ThrowStatement, dom_AbortStatement, dom_TransactionStatement, dom_ExprList, dom_NewExpression, dom_SpecialAssignmentStatement, AssignmentStatement},
    associations={container1, imports2, operations3, lhs16, rhs18, enumeration21, block5, name7, modelDeclarations9, imported11, resolvedType13, statements14, expr38, property40, extended42, literal23, model26, target29, isArrow31, arguments33, method35, returnType56, annotationBlock59, body61, name64, name45, create47, parameters50, contextType53, iterator76, iterated78, body81, parameters67, lhs69, rhs71, deleted74, default98, body100, condition84, ifBody86, elseBody89, returned92, expression94, cases96, iterators118, conditions120, method123, condition102, body104, name107, alias110, driver113, parameters116, keyValues135, expression126, expression128, parameterList131, contentType132, expression138, values140, name136, simpleAnnotations151, executableAnnotations154, name157, key142, value145, expression148, nativeExpression149, expressions173, start175, value160, thrown163, body165, names167, name170, end177, parameters180, model182, element185, resolvedModelDeclaration188},
    generalizations={gen_dom_Program_DomElement, gen_dom_AndOperatorExpression_BinaryOperatorExpression, gen_dom_LiteralExpression_Expression, gen_dom_BooleanExpression_PrimitiveExpression, gen_dom_DivideOperatorExpression_BinaryOperatorExpression, gen_dom_EnumerationLiteralExpression_Expression, gen_dom_Import_DomElement, gen_dom_Statement_DomElement, gen_dom_Expression_DomElement, gen_dom_Block_DomElement, gen_dom_OperatorExpression_Expression, gen_dom_BinaryOperatorExpression_OperatorExpression, gen_dom_NegativeOperatorExpression_UnaryOperatorExpression, gen_dom_NotEqualsOperatorExpression_BinaryOperatorExpression, gen_dom_NotOperatorExpression_UnaryOperatorExpression, gen_dom_OrOperatorExpression_BinaryOperatorExpression, gen_dom_PlusOperatorExpression_BinaryOperatorExpression, gen_dom_PropertyCallExpression_FeatureCallExpression, gen_dom_EqualsOperatorExpression_BinaryOperatorExpression, gen_dom_FeatureCallExpression_Expression, gen_dom_GreaterThanOperatorExpression_BinaryOperatorExpression, gen_dom_GreaterThanOrEqualToOperatorExpression_BinaryOperatorExpression, gen_dom_ImpliesOperatorExpression_BinaryOperatorExpression, gen_dom_IntegerExpression_PrimitiveExpression, gen_dom_LessThanOperatorExpression_BinaryOperatorExpression, gen_dom_LessThanOrEqualToOperatorExpression_BinaryOperatorExpression, gen_dom_MethodCallExpression_FeatureCallExpression, gen_dom_MinusOperatorExpression_BinaryOperatorExpression, gen_dom_MultiplyOperatorExpression_BinaryOperatorExpression, gen_dom_NameExpression_Expression, gen_dom_UnaryOperatorExpression_OperatorExpression, gen_dom_RealExpression_PrimitiveExpression, gen_dom_StringExpression_PrimitiveExpression, gen_dom_VariableDeclarationExpression_Expression, gen_dom_XorOperatorExpression_BinaryOperatorExpression, gen_dom_OperationDefinition_DomElement, gen_dom_ForStatement_Statement, gen_dom_AssignmentStatement_Statement, gen_dom_BreakStatement_Statement, gen_dom_BreakAllStatement_Statement, gen_dom_ContinueStatement_Statement, gen_dom_DeleteStatement_Statement, gen_dom_SwitchCaseStatement_Statement, gen_dom_WhileStatement_Statement, gen_dom_IfStatement_Statement, gen_dom_ReturnStatement_Statement, gen_dom_SwitchStatement_Statement, gen_dom_ModelDeclarationStatement_Statement, gen_dom_FOLMethodCallExpression_FeatureCallExpression, gen_dom_SequenceExpression_CollectionExpression, gen_dom_OrderedSetExpression_CollectionExpression, gen_dom_MapExpression_LiteralExpression, gen_dom_Type_DomElement, gen_dom_ExpressionStatement_Statement, gen_dom_SwitchCaseDefaultStatement_SwitchCaseStatement, gen_dom_SwitchCaseExpressionStatement_SwitchCaseStatement, gen_dom_PrimitiveExpression_LiteralExpression, gen_dom_CollectionExpression_LiteralExpression, gen_dom_SetExpression_CollectionExpression, gen_dom_BagExpression_CollectionExpression, gen_dom_ExecutableAnnotation_Annotation, gen_dom_SimpleAnnotation_Annotation, gen_dom_AnyType_Type, gen_dom_CollectionType_Type, gen_dom_PrimitiveType_Type, gen_dom_BooleanType_PrimitiveType, gen_dom_IntegerType_PrimitiveType, gen_dom_RealType_PrimitiveType, gen_dom_StringType_PrimitiveType, gen_dom_SetType_CollectionType, gen_dom_BagType_CollectionType, gen_dom_SequenceType_CollectionType, gen_dom_OrderedSetType_CollectionType, gen_dom_MapType_Type, gen_dom_Annotation_DomElement, gen_dom_ModelDeclarationParameter_DomElement, gen_dom_KeyValue_DomElement, gen_dom_SpecialNameExpression_NameExpression, gen_dom_ModelElementType_Type, gen_dom_NativeType_Type, gen_dom_ModelExpression_NameExpression, gen_dom_AnnotationBlock_DomElement, gen_dom_ExprList_CollectionInitValue, gen_dom_ExpRange_CollectionInitValue, gen_dom_ThrowStatement_Statement, gen_dom_AbortStatement_Statement, gen_dom_TransactionStatement_Statement, gen_dom_FormalParameterExpression_Expression, gen_dom_CollectionInitValue_DomElement, gen_dom_NewExpression_Expression, gen_dom_ModelElementTypeExpression_Expression, gen_dom_SpecialAssignmentStatement_AssignmentStatement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)