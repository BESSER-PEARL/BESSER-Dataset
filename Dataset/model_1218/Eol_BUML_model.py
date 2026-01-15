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
eol_EolProgram = Class(name="eol::EolProgram")
EolLibraryModule = Class(name="EolLibraryModule")
eol_Block = Class(name="eol::Block")
eol_Import = Class(name="eol::Import")
EolElement = Class(name="EolElement")
eol_StringExpression = Class(name="eol::StringExpression")
eol_EolElement = Class(name="eol::EolElement", is_abstract=True)
eol_TextRegion = Class(name="eol::TextRegion")
eol_TextPosition = Class(name="eol::TextPosition")
eol_OperatorExpression = Class(name="eol::OperatorExpression", is_abstract=True)
Expression = Class(name="Expression")
eol_BinaryOperatorExpression = Class(name="eol::BinaryOperatorExpression", is_abstract=True)
OperatorExpression = Class(name="OperatorExpression")
eol_EolLibraryModule = Class(name="eol::EolLibraryModule")
eol_AndOperatorExpression = Class(name="eol::AndOperatorExpression")
LogicalOperatorExpression = Class(name="LogicalOperatorExpression")
eol_LiteralExpression = Class(name="eol::LiteralExpression", is_abstract=True)
eol_BooleanExpression = Class(name="eol::BooleanExpression")
PrimitiveExpression = Class(name="PrimitiveExpression")
eol_Statement = Class(name="eol::Statement", is_abstract=True)
eol_Expression = Class(name="eol::Expression", is_abstract=True)
eol_Type = Class(name="eol::Type")
eol_ModelExpression = Class(name="eol::ModelExpression")
eol_EqualsOperatorExpression = Class(name="eol::EqualsOperatorExpression")
ComparisonOperatorExpression = Class(name="ComparisonOperatorExpression")
eol_FeatureCallExpression = Class(name="eol::FeatureCallExpression", is_abstract=True)
eol_GreaterThanOperatorExpression = Class(name="eol::GreaterThanOperatorExpression")
eol_GreaterThanOrEqualToOperatorExpression = Class(name="eol::GreaterThanOrEqualToOperatorExpression")
eol_ImpliesOperatorExpression = Class(name="eol::ImpliesOperatorExpression")
eol_DivideOperatorExpression = Class(name="eol::DivideOperatorExpression")
ArithmeticOperatorExpression = Class(name="ArithmeticOperatorExpression")
eol_EnumerationLiteralExpression = Class(name="eol::EnumerationLiteralExpression")
eol_NameExpression = Class(name="eol::NameExpression")
eol_EObject = Class(name="eol::EObject")
eol_MinusOperatorExpression = Class(name="eol::MinusOperatorExpression")
eol_MultiplyOperatorExpression = Class(name="eol::MultiplyOperatorExpression")
eol_UnaryOperatorExpression = Class(name="eol::UnaryOperatorExpression", is_abstract=True)
eol_IntegerExpression = Class(name="eol::IntegerExpression")
eol_LessThanOperatorExpression = Class(name="eol::LessThanOperatorExpression")
eol_LessThanOrEqualToOperatorExpression = Class(name="eol::LessThanOrEqualToOperatorExpression")
eol_MethodCallExpression = Class(name="eol::MethodCallExpression")
FeatureCallExpression = Class(name="FeatureCallExpression")
eol_PropertyCallExpression = Class(name="eol::PropertyCallExpression")
eol_RealExpression = Class(name="eol::RealExpression")
eol_VariableDeclarationExpression = Class(name="eol::VariableDeclarationExpression")
eol_NegativeOperatorExpression = Class(name="eol::NegativeOperatorExpression")
UnaryOperatorExpression = Class(name="UnaryOperatorExpression")
eol_NotEqualsOperatorExpression = Class(name="eol::NotEqualsOperatorExpression")
eol_NotOperatorExpression = Class(name="eol::NotOperatorExpression")
eol_OrOperatorExpression = Class(name="eol::OrOperatorExpression")
eol_PlusOperatorExpression = Class(name="eol::PlusOperatorExpression")
eol_OperationDefinition = Class(name="eol::OperationDefinition")
eol_AnnotationBlock = Class(name="eol::AnnotationBlock")
eol_FormalParameterExpression = Class(name="eol::FormalParameterExpression")
eol_XorOperatorExpression = Class(name="eol::XorOperatorExpression")
eol_BreakStatement = Class(name="eol::BreakStatement")
eol_BreakAllStatement = Class(name="eol::BreakAllStatement")
eol_ContinueStatement = Class(name="eol::ContinueStatement")
eol_DeleteStatement = Class(name="eol::DeleteStatement")
eol_ForStatement = Class(name="eol::ForStatement")
eol_AssignmentStatement = Class(name="eol::AssignmentStatement")
Statement = Class(name="Statement")
eol_ReturnStatement = Class(name="eol::ReturnStatement")
eol_SwitchStatement = Class(name="eol::SwitchStatement")
eol_ExpressionOrStatementBlock = Class(name="eol::ExpressionOrStatementBlock")
eol_IfStatement = Class(name="eol::IfStatement")
eol_WhileStatement = Class(name="eol::WhileStatement")
eol_ModelDeclarationStatement = Class(name="eol::ModelDeclarationStatement")
eol_EPackage = Class(name="eol::EPackage")
eol_SwitchCaseExpressionStatement = Class(name="eol::SwitchCaseExpressionStatement")
eol_SwitchCaseDefaultStatement = Class(name="eol::SwitchCaseDefaultStatement")
eol_SwitchCaseStatement = Class(name="eol::SwitchCaseStatement", is_abstract=True)
eol_FOLMethodCallExpression = Class(name="eol::FOLMethodCallExpression")
eol_ExpressionStatement = Class(name="eol::ExpressionStatement")
SwitchCaseStatement = Class(name="SwitchCaseStatement")
eol_ModelDeclarationParameter = Class(name="eol::ModelDeclarationParameter")
eol_SetExpression = Class(name="eol::SetExpression")
CollectionExpression = Class(name="CollectionExpression")
eol_BagExpression = Class(name="eol::BagExpression")
eol_SequenceExpression = Class(name="eol::SequenceExpression")
eol_OrderedSetExpression = Class(name="eol::OrderedSetExpression")
eol_MapExpression = Class(name="eol::MapExpression")
eol_KeyValue = Class(name="eol::KeyValue")
eol_PrimitiveExpression = Class(name="eol::PrimitiveExpression", is_abstract=True)
LiteralExpression = Class(name="LiteralExpression")
eol_CollectionExpression = Class(name="eol::CollectionExpression", is_abstract=True)
eol_CollectionInitValue = Class(name="eol::CollectionInitValue", is_abstract=True)
eol_PrimitiveType = Class(name="eol::PrimitiveType", is_abstract=True)
eol_BooleanType = Class(name="eol::BooleanType")
PrimitiveType = Class(name="PrimitiveType")
eol_IntegerType = Class(name="eol::IntegerType")
eol_RealType = Class(name="eol::RealType")
eol_StringType = Class(name="eol::StringType")
eol_SetType = Class(name="eol::SetType")
UniqueCollectionType = Class(name="UniqueCollectionType")
eol_BagType = Class(name="eol::BagType")
CollectionType = Class(name="CollectionType")
eol_SequenceType = Class(name="eol::SequenceType")
OrderedCollectionType = Class(name="OrderedCollectionType")
eol_OrderedSetType = Class(name="eol::OrderedSetType")
eol_MapType = Class(name="eol::MapType")
eol_AnyType = Class(name="eol::AnyType")
Type = Class(name="Type")
eol_CollectionType = Class(name="eol::CollectionType")
eol_SimpleAnnotation = Class(name="eol::SimpleAnnotation")
eol_Annotation = Class(name="eol::Annotation", is_abstract=True)
eol_ExecutableAnnotation = Class(name="eol::ExecutableAnnotation")
Annotation = Class(name="Annotation")
eol_SpecialNameExpression = Class(name="eol::SpecialNameExpression")
NameExpression = Class(name="NameExpression")
eol_ModelElementType = Class(name="eol::ModelElementType")
eol_EClassifier = Class(name="eol::EClassifier")
eol_NativeType = Class(name="eol::NativeType")
eol_SpecialAssignmentStatement = Class(name="eol::SpecialAssignmentStatement")
VariableDeclarationExpression = Class(name="VariableDeclarationExpression")
eol_ExprList = Class(name="eol::ExprList")
CollectionInitValue = Class(name="CollectionInitValue")
eol_ExpRange = Class(name="eol::ExpRange")
eol_ThrowStatement = Class(name="eol::ThrowStatement")
eol_NewExpression = Class(name="eol::NewExpression")
eol_AbortStatement = Class(name="eol::AbortStatement")
eol_TransactionStatement = Class(name="eol::TransactionStatement")
eol_OrderedCollectionType = Class(name="eol::OrderedCollectionType")
eol_UniqueCollectionType = Class(name="eol::UniqueCollectionType")
eol_SelfInnermostType = Class(name="eol::SelfInnermostType")
AssignmentStatement = Class(name="AssignmentStatement")
eol_OperationArgType = Class(name="eol::OperationArgType")
eol_ModelType = Class(name="eol::ModelType")
eol_NativeExpression = Class(name="eol::NativeExpression")
eol_EType = Class(name="eol::EType")
eol_VoidType = Class(name="eol::VoidType")
eol_PseudoType = Class(name="eol::PseudoType")
eol_SelfType = Class(name="eol::SelfType")
PseudoType = Class(name="PseudoType")
eol_SelfContentType = Class(name="eol::SelfContentType")
eol_LogicalOperatorExpression = Class(name="eol::LogicalOperatorExpression")
BinaryOperatorExpression = Class(name="BinaryOperatorExpression")
eol_ComparisonOperatorExpression = Class(name="eol::ComparisonOperatorExpression")
eol_ArithmeticOperatorExpression = Class(name="eol::ArithmeticOperatorExpression")

# eol_EolProgram class attributes and methods

# EolLibraryModule class attributes and methods

# eol_Block class attributes and methods

# eol_Import class attributes and methods

# EolElement class attributes and methods

# eol_StringExpression class attributes and methods
eol_StringExpression_val: Property = Property(name="val", type=StringType)
eol_StringExpression.attributes={eol_StringExpression_val}

# eol_EolElement class attributes and methods
eol_EolElement_line: Property = Property(name="line", type=IntegerType)
eol_EolElement_column: Property = Property(name="column", type=IntegerType)
eol_EolElement_uri: Property = Property(name="uri", type=StringType)
eol_EolElement.attributes={eol_EolElement_column, eol_EolElement_line, eol_EolElement_uri}

# eol_TextRegion class attributes and methods

# eol_TextPosition class attributes and methods
eol_TextPosition_line: Property = Property(name="line", type=IntegerType)
eol_TextPosition_column: Property = Property(name="column", type=IntegerType)
eol_TextPosition.attributes={eol_TextPosition_column, eol_TextPosition_line}

# eol_OperatorExpression class attributes and methods

# Expression class attributes and methods

# eol_BinaryOperatorExpression class attributes and methods

# OperatorExpression class attributes and methods

# eol_EolLibraryModule class attributes and methods

# eol_AndOperatorExpression class attributes and methods

# LogicalOperatorExpression class attributes and methods

# eol_LiteralExpression class attributes and methods

# eol_BooleanExpression class attributes and methods
eol_BooleanExpression_val: Property = Property(name="val", type=BooleanType)
eol_BooleanExpression.attributes={eol_BooleanExpression_val}

# PrimitiveExpression class attributes and methods

# eol_Statement class attributes and methods

# eol_Expression class attributes and methods

# eol_Type class attributes and methods

# eol_ModelExpression class attributes and methods

# eol_EqualsOperatorExpression class attributes and methods

# ComparisonOperatorExpression class attributes and methods

# eol_FeatureCallExpression class attributes and methods

# eol_GreaterThanOperatorExpression class attributes and methods

# eol_GreaterThanOrEqualToOperatorExpression class attributes and methods

# eol_ImpliesOperatorExpression class attributes and methods

# eol_DivideOperatorExpression class attributes and methods

# ArithmeticOperatorExpression class attributes and methods

# eol_EnumerationLiteralExpression class attributes and methods

# eol_NameExpression class attributes and methods
eol_NameExpression_name: Property = Property(name="name", type=StringType)
eol_NameExpression_resolvedContent: Property = Property(name="resolvedContent", type=StringType)
eol_NameExpression.attributes={eol_NameExpression_name, eol_NameExpression_resolvedContent}

# eol_EObject class attributes and methods

# eol_MinusOperatorExpression class attributes and methods

# eol_MultiplyOperatorExpression class attributes and methods

# eol_UnaryOperatorExpression class attributes and methods

# eol_IntegerExpression class attributes and methods
eol_IntegerExpression_val: Property = Property(name="val", type=IntegerType)
eol_IntegerExpression.attributes={eol_IntegerExpression_val}

# eol_LessThanOperatorExpression class attributes and methods

# eol_LessThanOrEqualToOperatorExpression class attributes and methods

# eol_MethodCallExpression class attributes and methods

# FeatureCallExpression class attributes and methods

# eol_PropertyCallExpression class attributes and methods

# eol_RealExpression class attributes and methods
eol_RealExpression_val: Property = Property(name="val", type=FloatType)
eol_RealExpression.attributes={eol_RealExpression_val}

# eol_VariableDeclarationExpression class attributes and methods
eol_VariableDeclarationExpression_definitionPoints: Property = Property(name="definitionPoints", type=StringType)
eol_VariableDeclarationExpression.attributes={eol_VariableDeclarationExpression_definitionPoints}

# eol_NegativeOperatorExpression class attributes and methods

# UnaryOperatorExpression class attributes and methods

# eol_NotEqualsOperatorExpression class attributes and methods

# eol_NotOperatorExpression class attributes and methods

# eol_OrOperatorExpression class attributes and methods

# eol_PlusOperatorExpression class attributes and methods

# eol_OperationDefinition class attributes and methods

# eol_AnnotationBlock class attributes and methods

# eol_FormalParameterExpression class attributes and methods

# eol_XorOperatorExpression class attributes and methods

# eol_BreakStatement class attributes and methods

# eol_BreakAllStatement class attributes and methods

# eol_ContinueStatement class attributes and methods

# eol_DeleteStatement class attributes and methods

# eol_ForStatement class attributes and methods

# eol_AssignmentStatement class attributes and methods

# Statement class attributes and methods

# eol_ReturnStatement class attributes and methods

# eol_SwitchStatement class attributes and methods

# eol_ExpressionOrStatementBlock class attributes and methods

# eol_IfStatement class attributes and methods

# eol_WhileStatement class attributes and methods

# eol_ModelDeclarationStatement class attributes and methods

# eol_EPackage class attributes and methods

# eol_SwitchCaseExpressionStatement class attributes and methods

# eol_SwitchCaseDefaultStatement class attributes and methods

# eol_SwitchCaseStatement class attributes and methods

# eol_FOLMethodCallExpression class attributes and methods

# eol_ExpressionStatement class attributes and methods

# SwitchCaseStatement class attributes and methods

# eol_ModelDeclarationParameter class attributes and methods

# eol_SetExpression class attributes and methods

# CollectionExpression class attributes and methods

# eol_BagExpression class attributes and methods

# eol_SequenceExpression class attributes and methods

# eol_OrderedSetExpression class attributes and methods

# eol_MapExpression class attributes and methods

# eol_KeyValue class attributes and methods

# eol_PrimitiveExpression class attributes and methods

# LiteralExpression class attributes and methods

# eol_CollectionExpression class attributes and methods

# eol_CollectionInitValue class attributes and methods

# eol_PrimitiveType class attributes and methods

# eol_BooleanType class attributes and methods

# PrimitiveType class attributes and methods

# eol_IntegerType class attributes and methods

# eol_RealType class attributes and methods

# eol_StringType class attributes and methods

# eol_SetType class attributes and methods

# UniqueCollectionType class attributes and methods

# eol_BagType class attributes and methods

# CollectionType class attributes and methods

# eol_SequenceType class attributes and methods

# OrderedCollectionType class attributes and methods

# eol_OrderedSetType class attributes and methods

# eol_MapType class attributes and methods

# eol_AnyType class attributes and methods
eol_AnyType_declared: Property = Property(name="declared", type=BooleanType)
eol_AnyType.attributes={eol_AnyType_declared}

# Type class attributes and methods

# eol_CollectionType class attributes and methods

# eol_SimpleAnnotation class attributes and methods

# eol_Annotation class attributes and methods

# eol_ExecutableAnnotation class attributes and methods

# Annotation class attributes and methods

# eol_SpecialNameExpression class attributes and methods

# NameExpression class attributes and methods

# eol_ModelElementType class attributes and methods
eol_ModelElementType_modelName: Property = Property(name="modelName", type=StringType)
eol_ModelElementType_elementName: Property = Property(name="elementName", type=StringType)
eol_ModelElementType.attributes={eol_ModelElementType_modelName, eol_ModelElementType_elementName}

# eol_EClassifier class attributes and methods

# eol_NativeType class attributes and methods

# eol_SpecialAssignmentStatement class attributes and methods

# VariableDeclarationExpression class attributes and methods

# eol_ExprList class attributes and methods

# CollectionInitValue class attributes and methods

# eol_ExpRange class attributes and methods

# eol_ThrowStatement class attributes and methods

# eol_NewExpression class attributes and methods

# eol_AbortStatement class attributes and methods

# eol_TransactionStatement class attributes and methods

# eol_OrderedCollectionType class attributes and methods

# eol_UniqueCollectionType class attributes and methods

# eol_SelfInnermostType class attributes and methods

# AssignmentStatement class attributes and methods

# eol_OperationArgType class attributes and methods

# eol_ModelType class attributes and methods

# eol_NativeExpression class attributes and methods

# eol_EType class attributes and methods

# eol_VoidType class attributes and methods

# eol_PseudoType class attributes and methods

# eol_SelfType class attributes and methods

# PseudoType class attributes and methods

# eol_SelfContentType class attributes and methods

# eol_LogicalOperatorExpression class attributes and methods

# BinaryOperatorExpression class attributes and methods

# eol_ComparisonOperatorExpression class attributes and methods

# eol_ArithmeticOperatorExpression class attributes and methods

# Relationships
end6: BinaryAssociation = BinaryAssociation(
    name="end6",
    ends={
        Property(name="eol_TextRegion7", type=eol_TextPosition, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="eol_TextPosition8", type=eol_TextRegion, multiplicity=Multiplicity(1, 1))
    }
)
importedModules10: BinaryAssociation = BinaryAssociation(
    name="importedModules10",
    ends={
        Property(name="eol_EolProgram", type=eol_EolProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EolProgram9", type=eol_EolProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block11: BinaryAssociation = BinaryAssociation(
    name="block11",
    ends={
        Property(name="eol_Block", type=eol_EolProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EolProgram12", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container1: BinaryAssociation = BinaryAssociation(
    name="container1",
    ends={
        Property(name="eol_EolElement", type=eol_EolElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EolElement0", type=eol_EolElement, multiplicity=Multiplicity(0, 1))
    }
)
region2: BinaryAssociation = BinaryAssociation(
    name="region2",
    ends={
        Property(name="eol_TextRegion", type=eol_EolElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EolElement3", type=eol_TextRegion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start4: BinaryAssociation = BinaryAssociation(
    name="start4",
    ends={
        Property(name="eol_TextPosition", type=eol_TextRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TextRegion5", type=eol_TextPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements17: BinaryAssociation = BinaryAssociation(
    name="statements17",
    ends={
        Property(name="eol_Block18", type=eol_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="eol_Statement", type=eol_Block, multiplicity=Multiplicity(1, 1))
    }
)
lhs19: BinaryAssociation = BinaryAssociation(
    name="lhs19",
    ends={
        Property(name="eol_Expression20", type=eol_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_BinaryOperatorExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs21: BinaryAssociation = BinaryAssociation(
    name="rhs21",
    ends={
        Property(name="eol_Expression23", type=eol_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_BinaryOperatorExpression22", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imported13: BinaryAssociation = BinaryAssociation(
    name="imported13",
    ends={
        Property(name="eol_StringExpression", type=eol_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Import", type=eol_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
importedProgram14: BinaryAssociation = BinaryAssociation(
    name="importedProgram14",
    ends={
        Property(name="eol_EolLibraryModule", type=eol_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Import15", type=eol_EolLibraryModule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedType16: BinaryAssociation = BinaryAssociation(
    name="resolvedType16",
    ends={
        Property(name="eol_Type", type=eol_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Expression", type=eol_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model28: BinaryAssociation = BinaryAssociation(
    name="model28",
    ends={
        Property(name="eol_ModelExpression", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression29", type=eol_ModelExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target30: BinaryAssociation = BinaryAssociation(
    name="target30",
    ends={
        Property(name="eol_Expression31", type=eol_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FeatureCallExpression", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isArrow32: BinaryAssociation = BinaryAssociation(
    name="isArrow32",
    ends={
        Property(name="eol_BooleanExpression", type=eol_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FeatureCallExpression33", type=eol_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumeration24: BinaryAssociation = BinaryAssociation(
    name="enumeration24",
    ends={
        Property(name="eol_NameExpression", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literal25: BinaryAssociation = BinaryAssociation(
    name="literal25",
    ends={
        Property(name="eol_NameExpression27", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression26", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
method36: BinaryAssociation = BinaryAssociation(
    name="method36",
    ends={
        Property(name="eol_NameExpression38", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression37", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedMethods39: BinaryAssociation = BinaryAssociation(
    name="resolvedMethods39",
    ends={
        Property(name="eol_EObject", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression40", type=eol_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
isType41: BinaryAssociation = BinaryAssociation(
    name="isType41",
    ends={
        Property(name="eol_BooleanExpression43", type=eol_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NameExpression42", type=eol_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments34: BinaryAssociation = BinaryAssociation(
    name="arguments34",
    ends={
        Property(name="eol_Expression35", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property46: BinaryAssociation = BinaryAssociation(
    name="property46",
    ends={
        Property(name="eol_NameExpression47", type=eol_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_PropertyCallExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extended48: BinaryAssociation = BinaryAssociation(
    name="extended48",
    ends={
        Property(name="eol_BooleanExpression50", type=eol_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_PropertyCallExpression49", type=eol_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr44: BinaryAssociation = BinaryAssociation(
    name="expr44",
    ends={
        Property(name="eol_Expression45", type=eol_UnaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_UnaryOperatorExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextType59: BinaryAssociation = BinaryAssociation(
    name="contextType59",
    ends={
        Property(name="eol_Type60", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition", type=eol_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType61: BinaryAssociation = BinaryAssociation(
    name="returnType61",
    ends={
        Property(name="eol_Type63", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition62", type=eol_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationBlock64: BinaryAssociation = BinaryAssociation(
    name="annotationBlock64",
    ends={
        Property(name="eol_AnnotationBlock", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition65", type=eol_AnnotationBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body66: BinaryAssociation = BinaryAssociation(
    name="body66",
    ends={
        Property(name="eol_Block68", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition67", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name69: BinaryAssociation = BinaryAssociation(
    name="name69",
    ends={
        Property(name="eol_NameExpression71", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition70", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters72: BinaryAssociation = BinaryAssociation(
    name="parameters72",
    ends={
        Property(name="eol_FormalParameterExpression", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition73", type=eol_FormalParameterExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name51: BinaryAssociation = BinaryAssociation(
    name="name51",
    ends={
        Property(name="eol_NameExpression52", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
create53: BinaryAssociation = BinaryAssociation(
    name="create53",
    ends={
        Property(name="eol_BooleanExpression55", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression54", type=eol_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters56: BinaryAssociation = BinaryAssociation(
    name="parameters56",
    ends={
        Property(name="eol_Expression58", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression57", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs83: BinaryAssociation = BinaryAssociation(
    name="lhs83",
    ends={
        Property(name="eol_Expression84", type=eol_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AssignmentStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs85: BinaryAssociation = BinaryAssociation(
    name="rhs85",
    ends={
        Property(name="eol_Expression87", type=eol_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AssignmentStatement86", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
deleted88: BinaryAssociation = BinaryAssociation(
    name="deleted88",
    ends={
        Property(name="eol_Expression89", type=eol_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_DeleteStatement", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
self74: BinaryAssociation = BinaryAssociation(
    name="self74",
    ends={
        Property(name="eol_VariableDeclarationExpression76", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition75", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
_result77: BinaryAssociation = BinaryAssociation(
    name="_result77",
    ends={
        Property(name="eol_VariableDeclarationExpression79", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition78", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependingOperationDefinitions81: BinaryAssociation = BinaryAssociation(
    name="dependingOperationDefinitions81",
    ends={
        Property(name="eol_OperationDefinition82", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition80", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
condition97: BinaryAssociation = BinaryAssociation(
    name="condition97",
    ends={
        Property(name="eol_IfStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="eol_Expression98", type=eol_IfStatement, multiplicity=Multiplicity(1, 1))
    }
)
ifBody99: BinaryAssociation = BinaryAssociation(
    name="ifBody99",
    ends={
        Property(name="eol_ExpressionOrStatementBlock101", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement100", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBody102: BinaryAssociation = BinaryAssociation(
    name="elseBody102",
    ends={
        Property(name="eol_ExpressionOrStatementBlock104", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement103", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returned105: BinaryAssociation = BinaryAssociation(
    name="returned105",
    ends={
        Property(name="eol_Expression106", type=eol_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ReturnStatement", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression107: BinaryAssociation = BinaryAssociation(
    name="expression107",
    ends={
        Property(name="eol_Expression108", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator90: BinaryAssociation = BinaryAssociation(
    name="iterator90",
    ends={
        Property(name="eol_FormalParameterExpression91", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement", type=eol_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterated92: BinaryAssociation = BinaryAssociation(
    name="iterated92",
    ends={
        Property(name="eol_Expression94", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement93", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body95: BinaryAssociation = BinaryAssociation(
    name="body95",
    ends={
        Property(name="eol_ExpressionOrStatementBlock", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement96", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition115: BinaryAssociation = BinaryAssociation(
    name="condition115",
    ends={
        Property(name="eol_Expression116", type=eol_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_WhileStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body117: BinaryAssociation = BinaryAssociation(
    name="body117",
    ends={
        Property(name="eol_ExpressionOrStatementBlock119", type=eol_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_WhileStatement118", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packages120: BinaryAssociation = BinaryAssociation(
    name="packages120",
    ends={
        Property(name="eol_EPackage", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement", type=eol_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name121: BinaryAssociation = BinaryAssociation(
    name="name121",
    ends={
        Property(name="eol_VariableDeclarationExpression123", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement122", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases109: BinaryAssociation = BinaryAssociation(
    name="cases109",
    ends={
        Property(name="eol_SwitchCaseExpressionStatement", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement110", type=eol_SwitchCaseExpressionStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default111: BinaryAssociation = BinaryAssociation(
    name="default111",
    ends={
        Property(name="eol_SwitchCaseDefaultStatement", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement112", type=eol_SwitchCaseDefaultStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body113: BinaryAssociation = BinaryAssociation(
    name="body113",
    ends={
        Property(name="eol_ExpressionOrStatementBlock114", type=eol_SwitchCaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchCaseStatement", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterator135: BinaryAssociation = BinaryAssociation(
    name="iterator135",
    ends={
        Property(name="eol_FormalParameterExpression136", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression", type=eol_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition137: BinaryAssociation = BinaryAssociation(
    name="condition137",
    ends={
        Property(name="eol_Expression139", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression138", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
method140: BinaryAssociation = BinaryAssociation(
    name="method140",
    ends={
        Property(name="eol_NameExpression142", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression141", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression143: BinaryAssociation = BinaryAssociation(
    name="expression143",
    ends={
        Property(name="eol_Expression144", type=eol_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alias124: BinaryAssociation = BinaryAssociation(
    name="alias124",
    ends={
        Property(name="eol_VariableDeclarationExpression126", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement125", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
driver127: BinaryAssociation = BinaryAssociation(
    name="driver127",
    ends={
        Property(name="eol_VariableDeclarationExpression129", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement128", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters130: BinaryAssociation = BinaryAssociation(
    name="parameters130",
    ends={
        Property(name="eol_ModelDeclarationParameter", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement131", type=eol_ModelDeclarationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EReference0133: BinaryAssociation = BinaryAssociation(
    name="EReference0133",
    ends={
        Property(name="eol_ModelDeclarationStatement134", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement132", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(0, 1))
    }
)
contentType149: BinaryAssociation = BinaryAssociation(
    name="contentType149",
    ends={
        Property(name="eol_Type151", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression150", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contents152: BinaryAssociation = BinaryAssociation(
    name="contents152",
    ends={
        Property(name="eol_LiteralExpression", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression153", type=eol_LiteralExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyValues154: BinaryAssociation = BinaryAssociation(
    name="keyValues154",
    ends={
        Property(name="eol_KeyValue", type=eol_MapExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapExpression", type=eol_KeyValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression145: BinaryAssociation = BinaryAssociation(
    name="expression145",
    ends={
        Property(name="eol_Expression147", type=eol_SwitchCaseExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchCaseExpressionStatement146", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterList148: BinaryAssociation = BinaryAssociation(
    name="parameterList148",
    ends={
        Property(name="eol_CollectionInitValue", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression", type=eol_CollectionInitValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dynamicTypes155: BinaryAssociation = BinaryAssociation(
    name="dynamicTypes155",
    ends={
        Property(name="eol_Type156", type=eol_AnyType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnyType", type=eol_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentType157: BinaryAssociation = BinaryAssociation(
    name="contentType157",
    ends={
        Property(name="eol_Type158", type=eol_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionType", type=eol_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression166: BinaryAssociation = BinaryAssociation(
    name="expression166",
    ends={
        Property(name="eol_Expression167", type=eol_ExecutableAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExecutableAnnotation", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values168: BinaryAssociation = BinaryAssociation(
    name="values168",
    ends={
        Property(name="eol_StringExpression169", type=eol_SimpleAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SimpleAnnotation", type=eol_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key170: BinaryAssociation = BinaryAssociation(
    name="key170",
    ends={
        Property(name="eol_Expression172", type=eol_KeyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_KeyValue171", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value173: BinaryAssociation = BinaryAssociation(
    name="value173",
    ends={
        Property(name="eol_Expression175", type=eol_KeyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_KeyValue174", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueType159: BinaryAssociation = BinaryAssociation(
    name="valueType159",
    ends={
        Property(name="eol_Type160", type=eol_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapType", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType161: BinaryAssociation = BinaryAssociation(
    name="keyType161",
    ends={
        Property(name="eol_Type163", type=eol_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapType162", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name164: BinaryAssociation = BinaryAssociation(
    name="name164",
    ends={
        Property(name="eol_NameExpression165", type=eol_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Annotation", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nativeExpression180: BinaryAssociation = BinaryAssociation(
    name="nativeExpression180",
    ends={
        Property(name="eol_StringExpression181", type=eol_NativeType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NativeType", type=eol_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simpleAnnotations182: BinaryAssociation = BinaryAssociation(
    name="simpleAnnotations182",
    ends={
        Property(name="eol_SimpleAnnotation184", type=eol_AnnotationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnnotationBlock183", type=eol_SimpleAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executableAnnotations185: BinaryAssociation = BinaryAssociation(
    name="executableAnnotations185",
    ends={
        Property(name="eol_ExecutableAnnotation187", type=eol_AnnotationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnnotationBlock186", type=eol_ExecutableAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name188: BinaryAssociation = BinaryAssociation(
    name="name188",
    ends={
        Property(name="eol_NameExpression190", type=eol_ModelDeclarationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationParameter189", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ecoreType176: BinaryAssociation = BinaryAssociation(
    name="ecoreType176",
    ends={
        Property(name="eol_EClassifier", type=eol_ModelElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelElementType", type=eol_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
resolvedModelDeclaration177: BinaryAssociation = BinaryAssociation(
    name="resolvedModelDeclaration177",
    ends={
        Property(name="eol_ModelDeclarationStatement179", type=eol_ModelElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelElementType178", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(0, 9999))
    }
)
names196: BinaryAssociation = BinaryAssociation(
    name="names196",
    ends={
        Property(name="eol_TransactionStatement", type=eol_NameExpression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="eol_NameExpression197", type=eol_TransactionStatement, multiplicity=Multiplicity(1, 1))
    }
)
expression210: BinaryAssociation = BinaryAssociation(
    name="expression210",
    ends={
        Property(name="eol_Expression212", type=eol_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NewExpression211", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body198: BinaryAssociation = BinaryAssociation(
    name="body198",
    ends={
        Property(name="eol_ExpressionOrStatementBlock200", type=eol_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TransactionStatement199", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions201: BinaryAssociation = BinaryAssociation(
    name="expressions201",
    ends={
        Property(name="eol_Expression202", type=eol_ExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExprList", type=eol_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
start203: BinaryAssociation = BinaryAssociation(
    name="start203",
    ends={
        Property(name="eol_Expression204", type=eol_ExpRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpRange", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value191: BinaryAssociation = BinaryAssociation(
    name="value191",
    ends={
        Property(name="eol_StringExpression193", type=eol_ModelDeclarationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationParameter192", type=eol_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end205: BinaryAssociation = BinaryAssociation(
    name="end205",
    ends={
        Property(name="eol_Expression207", type=eol_ExpRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpRange206", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thrown194: BinaryAssociation = BinaryAssociation(
    name="thrown194",
    ends={
        Property(name="eol_Expression195", type=eol_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ThrowStatement", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters208: BinaryAssociation = BinaryAssociation(
    name="parameters208",
    ends={
        Property(name="eol_Expression209", type=eol_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NewExpression", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
models213: BinaryAssociation = BinaryAssociation(
    name="models213",
    ends={
        Property(name="eol_ModelDeclarationStatement214", type=eol_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelType", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 9999))
    }
)
nativeExpr215: BinaryAssociation = BinaryAssociation(
    name="nativeExpr215",
    ends={
        Property(name="eol_StringExpression216", type=eol_NativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NativeExpression", type=eol_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isType217: BinaryAssociation = BinaryAssociation(
    name="isType217",
    ends={
        Property(name="eol_BooleanExpression219", type=eol_NativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NativeExpression218", type=eol_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ecoreType220: BinaryAssociation = BinaryAssociation(
    name="ecoreType220",
    ends={
        Property(name="eol_EClassifier221", type=eol_EType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EType", type=eol_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
block222: BinaryAssociation = BinaryAssociation(
    name="block222",
    ends={
        Property(name="eol_Block224", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionOrStatementBlock223", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression225: BinaryAssociation = BinaryAssociation(
    name="expression225",
    ends={
        Property(name="eol_Expression227", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionOrStatementBlock226", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelDeclarations228: BinaryAssociation = BinaryAssociation(
    name="modelDeclarations228",
    ends={
        Property(name="eol_ModelDeclarationStatement230", type=eol_EolLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EolLibraryModule229", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports231: BinaryAssociation = BinaryAssociation(
    name="imports231",
    ends={
        Property(name="eol_Import233", type=eol_EolLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EolLibraryModule232", type=eol_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations234: BinaryAssociation = BinaryAssociation(
    name="operations234",
    ends={
        Property(name="eol_OperationDefinition236", type=eol_EolLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EolLibraryModule235", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name237: BinaryAssociation = BinaryAssociation(
    name="name237",
    ends={
        Property(name="eol_NameExpression239", type=eol_EolLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EolLibraryModule238", type=eol_NameExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_eol_EolProgram_EolLibraryModule = Generalization(general=EolLibraryModule, specific=eol_EolProgram)
gen_eol_Import_EolElement = Generalization(general=EolElement, specific=eol_Import)
gen_eol_OperatorExpression_Expression = Generalization(general=Expression, specific=eol_OperatorExpression)
gen_eol_BinaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=eol_BinaryOperatorExpression)
gen_eol_AndOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_AndOperatorExpression)
gen_eol_LiteralExpression_Expression = Generalization(general=Expression, specific=eol_LiteralExpression)
gen_eol_Statement_EolElement = Generalization(general=EolElement, specific=eol_Statement)
gen_eol_Expression_EolElement = Generalization(general=EolElement, specific=eol_Expression)
gen_eol_Block_EolElement = Generalization(general=EolElement, specific=eol_Block)
gen_eol_EqualsOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_EqualsOperatorExpression)
gen_eol_FeatureCallExpression_Expression = Generalization(general=Expression, specific=eol_FeatureCallExpression)
gen_eol_GreaterThanOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_GreaterThanOperatorExpression)
gen_eol_GreaterThanOrEqualToOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_GreaterThanOrEqualToOperatorExpression)
gen_eol_ImpliesOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_ImpliesOperatorExpression)
gen_eol_BooleanExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_BooleanExpression)
gen_eol_DivideOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_DivideOperatorExpression)
gen_eol_EnumerationLiteralExpression_Expression = Generalization(general=Expression, specific=eol_EnumerationLiteralExpression)
gen_eol_MinusOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_MinusOperatorExpression)
gen_eol_MultiplyOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_MultiplyOperatorExpression)
gen_eol_NameExpression_Expression = Generalization(general=Expression, specific=eol_NameExpression)
gen_eol_IntegerExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_IntegerExpression)
gen_eol_LessThanOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_LessThanOperatorExpression)
gen_eol_LessThanOrEqualToOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_LessThanOrEqualToOperatorExpression)
gen_eol_MethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_MethodCallExpression)
gen_eol_PlusOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_PlusOperatorExpression)
gen_eol_PropertyCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_PropertyCallExpression)
gen_eol_RealExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_RealExpression)
gen_eol_StringExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_StringExpression)
gen_eol_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=eol_VariableDeclarationExpression)
gen_eol_UnaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=eol_UnaryOperatorExpression)
gen_eol_NegativeOperatorExpression_UnaryOperatorExpression = Generalization(general=UnaryOperatorExpression, specific=eol_NegativeOperatorExpression)
gen_eol_NotEqualsOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_NotEqualsOperatorExpression)
gen_eol_NotOperatorExpression_UnaryOperatorExpression = Generalization(general=UnaryOperatorExpression, specific=eol_NotOperatorExpression)
gen_eol_OrOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_OrOperatorExpression)
gen_eol_OperationDefinition_EolElement = Generalization(general=EolElement, specific=eol_OperationDefinition)
gen_eol_XorOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_XorOperatorExpression)
gen_eol_BreakStatement_Statement = Generalization(general=Statement, specific=eol_BreakStatement)
gen_eol_BreakAllStatement_Statement = Generalization(general=Statement, specific=eol_BreakAllStatement)
gen_eol_ContinueStatement_Statement = Generalization(general=Statement, specific=eol_ContinueStatement)
gen_eol_DeleteStatement_Statement = Generalization(general=Statement, specific=eol_DeleteStatement)
gen_eol_ForStatement_Statement = Generalization(general=Statement, specific=eol_ForStatement)
gen_eol_AssignmentStatement_Statement = Generalization(general=Statement, specific=eol_AssignmentStatement)
gen_eol_ReturnStatement_Statement = Generalization(general=Statement, specific=eol_ReturnStatement)
gen_eol_SwitchStatement_Statement = Generalization(general=Statement, specific=eol_SwitchStatement)
gen_eol_IfStatement_Statement = Generalization(general=Statement, specific=eol_IfStatement)
gen_eol_WhileStatement_Statement = Generalization(general=Statement, specific=eol_WhileStatement)
gen_eol_ModelDeclarationStatement_Statement = Generalization(general=Statement, specific=eol_ModelDeclarationStatement)
gen_eol_SwitchCaseStatement_Statement = Generalization(general=Statement, specific=eol_SwitchCaseStatement)
gen_eol_FOLMethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_FOLMethodCallExpression)
gen_eol_ExpressionStatement_Statement = Generalization(general=Statement, specific=eol_ExpressionStatement)
gen_eol_SwitchCaseDefaultStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_SwitchCaseDefaultStatement)
gen_eol_SetExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_SetExpression)
gen_eol_BagExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_BagExpression)
gen_eol_SequenceExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_SequenceExpression)
gen_eol_OrderedSetExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_OrderedSetExpression)
gen_eol_MapExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=eol_MapExpression)
gen_eol_Type_EolElement = Generalization(general=EolElement, specific=eol_Type)
gen_eol_SwitchCaseExpressionStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_SwitchCaseExpressionStatement)
gen_eol_PrimitiveExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=eol_PrimitiveExpression)
gen_eol_CollectionExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=eol_CollectionExpression)
gen_eol_PrimitiveType_Type = Generalization(general=Type, specific=eol_PrimitiveType)
gen_eol_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_BooleanType)
gen_eol_IntegerType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_IntegerType)
gen_eol_RealType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_RealType)
gen_eol_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_StringType)
gen_eol_SetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_SetType)
gen_eol_BagType_CollectionType = Generalization(general=CollectionType, specific=eol_BagType)
gen_eol_SequenceType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_SequenceType)
gen_eol_OrderedSetType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_OrderedSetType)
gen_eol_OrderedSetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_OrderedSetType)
gen_eol_MapType_Type = Generalization(general=Type, specific=eol_MapType)
gen_eol_AnyType_Type = Generalization(general=Type, specific=eol_AnyType)
gen_eol_CollectionType_Type = Generalization(general=Type, specific=eol_CollectionType)
gen_eol_SimpleAnnotation_Annotation = Generalization(general=Annotation, specific=eol_SimpleAnnotation)
gen_eol_KeyValue_Expression = Generalization(general=Expression, specific=eol_KeyValue)
gen_eol_Annotation_EolElement = Generalization(general=EolElement, specific=eol_Annotation)
gen_eol_ExecutableAnnotation_Annotation = Generalization(general=Annotation, specific=eol_ExecutableAnnotation)
gen_eol_ModelExpression_NameExpression = Generalization(general=NameExpression, specific=eol_ModelExpression)
gen_eol_AnnotationBlock_EolElement = Generalization(general=EolElement, specific=eol_AnnotationBlock)
gen_eol_ModelDeclarationParameter_Expression = Generalization(general=Expression, specific=eol_ModelDeclarationParameter)
gen_eol_SpecialNameExpression_NameExpression = Generalization(general=NameExpression, specific=eol_SpecialNameExpression)
gen_eol_ModelElementType_Type = Generalization(general=Type, specific=eol_ModelElementType)
gen_eol_NativeType_Type = Generalization(general=Type, specific=eol_NativeType)
gen_eol_FormalParameterExpression_VariableDeclarationExpression = Generalization(general=VariableDeclarationExpression, specific=eol_FormalParameterExpression)
gen_eol_CollectionInitValue_Expression = Generalization(general=Expression, specific=eol_CollectionInitValue)
gen_eol_ExprList_CollectionInitValue = Generalization(general=CollectionInitValue, specific=eol_ExprList)
gen_eol_ExpRange_CollectionInitValue = Generalization(general=CollectionInitValue, specific=eol_ExpRange)
gen_eol_ThrowStatement_Statement = Generalization(general=Statement, specific=eol_ThrowStatement)
gen_eol_NewExpression_Expression = Generalization(general=Expression, specific=eol_NewExpression)
gen_eol_AbortStatement_Statement = Generalization(general=Statement, specific=eol_AbortStatement)
gen_eol_TransactionStatement_Statement = Generalization(general=Statement, specific=eol_TransactionStatement)
gen_eol_OrderedCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_OrderedCollectionType)
gen_eol_UniqueCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_UniqueCollectionType)
gen_eol_SelfInnermostType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfInnermostType)
gen_eol_SpecialAssignmentStatement_AssignmentStatement = Generalization(general=AssignmentStatement, specific=eol_SpecialAssignmentStatement)
gen_eol_OperationArgType_PseudoType = Generalization(general=PseudoType, specific=eol_OperationArgType)
gen_eol_ModelType_Type = Generalization(general=Type, specific=eol_ModelType)
gen_eol_NativeExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=eol_NativeExpression)
gen_eol_EType_Type = Generalization(general=Type, specific=eol_EType)
gen_eol_VoidType_Type = Generalization(general=Type, specific=eol_VoidType)
gen_eol_PseudoType_Type = Generalization(general=Type, specific=eol_PseudoType)
gen_eol_SelfType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfType)
gen_eol_SelfContentType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfContentType)
gen_eol_LogicalOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_LogicalOperatorExpression)
gen_eol_ComparisonOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_ComparisonOperatorExpression)
gen_eol_ArithmeticOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_ArithmeticOperatorExpression)
gen_eol_ExpressionOrStatementBlock_EolElement = Generalization(general=EolElement, specific=eol_ExpressionOrStatementBlock)
gen_eol_EolLibraryModule_EolElement = Generalization(general=EolElement, specific=eol_EolLibraryModule)

# Domain Model
domain_model = DomainModel(
    name="eol",
    types={eol_EolProgram, EolLibraryModule, eol_Block, eol_Import, EolElement, eol_StringExpression, eol_EolElement, eol_TextRegion, eol_TextPosition, eol_OperatorExpression, Expression, eol_BinaryOperatorExpression, OperatorExpression, eol_EolLibraryModule, eol_AndOperatorExpression, LogicalOperatorExpression, eol_LiteralExpression, eol_BooleanExpression, PrimitiveExpression, eol_Statement, eol_Expression, eol_Type, eol_ModelExpression, eol_EqualsOperatorExpression, ComparisonOperatorExpression, eol_FeatureCallExpression, eol_GreaterThanOperatorExpression, eol_GreaterThanOrEqualToOperatorExpression, eol_ImpliesOperatorExpression, eol_DivideOperatorExpression, ArithmeticOperatorExpression, eol_EnumerationLiteralExpression, eol_NameExpression, eol_EObject, eol_MinusOperatorExpression, eol_MultiplyOperatorExpression, eol_UnaryOperatorExpression, eol_IntegerExpression, eol_LessThanOperatorExpression, eol_LessThanOrEqualToOperatorExpression, eol_MethodCallExpression, FeatureCallExpression, eol_PropertyCallExpression, eol_RealExpression, eol_VariableDeclarationExpression, eol_NegativeOperatorExpression, UnaryOperatorExpression, eol_NotEqualsOperatorExpression, eol_NotOperatorExpression, eol_OrOperatorExpression, eol_PlusOperatorExpression, eol_OperationDefinition, eol_AnnotationBlock, eol_FormalParameterExpression, eol_XorOperatorExpression, eol_BreakStatement, eol_BreakAllStatement, eol_ContinueStatement, eol_DeleteStatement, eol_ForStatement, eol_AssignmentStatement, Statement, eol_ReturnStatement, eol_SwitchStatement, eol_ExpressionOrStatementBlock, eol_IfStatement, eol_WhileStatement, eol_ModelDeclarationStatement, eol_EPackage, eol_SwitchCaseExpressionStatement, eol_SwitchCaseDefaultStatement, eol_SwitchCaseStatement, eol_FOLMethodCallExpression, eol_ExpressionStatement, SwitchCaseStatement, eol_ModelDeclarationParameter, eol_SetExpression, CollectionExpression, eol_BagExpression, eol_SequenceExpression, eol_OrderedSetExpression, eol_MapExpression, eol_KeyValue, eol_PrimitiveExpression, LiteralExpression, eol_CollectionExpression, eol_CollectionInitValue, eol_PrimitiveType, eol_BooleanType, PrimitiveType, eol_IntegerType, eol_RealType, eol_StringType, eol_SetType, UniqueCollectionType, eol_BagType, CollectionType, eol_SequenceType, OrderedCollectionType, eol_OrderedSetType, eol_MapType, eol_AnyType, Type, eol_CollectionType, eol_SimpleAnnotation, eol_Annotation, eol_ExecutableAnnotation, Annotation, eol_SpecialNameExpression, NameExpression, eol_ModelElementType, eol_EClassifier, eol_NativeType, eol_SpecialAssignmentStatement, VariableDeclarationExpression, eol_ExprList, CollectionInitValue, eol_ExpRange, eol_ThrowStatement, eol_NewExpression, eol_AbortStatement, eol_TransactionStatement, eol_OrderedCollectionType, eol_UniqueCollectionType, eol_SelfInnermostType, AssignmentStatement, eol_OperationArgType, eol_ModelType, eol_NativeExpression, eol_EType, eol_VoidType, eol_PseudoType, eol_SelfType, PseudoType, eol_SelfContentType, eol_LogicalOperatorExpression, BinaryOperatorExpression, eol_ComparisonOperatorExpression, eol_ArithmeticOperatorExpression},
    associations={end6, importedModules10, block11, container1, region2, start4, statements17, lhs19, rhs21, imported13, importedProgram14, resolvedType16, model28, target30, isArrow32, enumeration24, literal25, method36, resolvedMethods39, isType41, arguments34, property46, extended48, expr44, contextType59, returnType61, annotationBlock64, body66, name69, parameters72, name51, create53, parameters56, lhs83, rhs85, deleted88, self74, _result77, dependingOperationDefinitions81, condition97, ifBody99, elseBody102, returned105, expression107, iterator90, iterated92, body95, condition115, body117, packages120, name121, cases109, default111, body113, iterator135, condition137, method140, expression143, alias124, driver127, parameters130, EReference0133, contentType149, contents152, keyValues154, expression145, parameterList148, dynamicTypes155, contentType157, expression166, values168, key170, value173, valueType159, keyType161, name164, nativeExpression180, simpleAnnotations182, executableAnnotations185, name188, ecoreType176, resolvedModelDeclaration177, names196, expression210, body198, expressions201, start203, value191, end205, thrown194, parameters208, models213, nativeExpr215, isType217, ecoreType220, block222, expression225, modelDeclarations228, imports231, operations234, name237},
    generalizations={gen_eol_EolProgram_EolLibraryModule, gen_eol_Import_EolElement, gen_eol_OperatorExpression_Expression, gen_eol_BinaryOperatorExpression_OperatorExpression, gen_eol_AndOperatorExpression_LogicalOperatorExpression, gen_eol_LiteralExpression_Expression, gen_eol_Statement_EolElement, gen_eol_Expression_EolElement, gen_eol_Block_EolElement, gen_eol_EqualsOperatorExpression_ComparisonOperatorExpression, gen_eol_FeatureCallExpression_Expression, gen_eol_GreaterThanOperatorExpression_ComparisonOperatorExpression, gen_eol_GreaterThanOrEqualToOperatorExpression_ComparisonOperatorExpression, gen_eol_ImpliesOperatorExpression_LogicalOperatorExpression, gen_eol_BooleanExpression_PrimitiveExpression, gen_eol_DivideOperatorExpression_ArithmeticOperatorExpression, gen_eol_EnumerationLiteralExpression_Expression, gen_eol_MinusOperatorExpression_ArithmeticOperatorExpression, gen_eol_MultiplyOperatorExpression_ArithmeticOperatorExpression, gen_eol_NameExpression_Expression, gen_eol_IntegerExpression_PrimitiveExpression, gen_eol_LessThanOperatorExpression_ComparisonOperatorExpression, gen_eol_LessThanOrEqualToOperatorExpression_ComparisonOperatorExpression, gen_eol_MethodCallExpression_FeatureCallExpression, gen_eol_PlusOperatorExpression_ArithmeticOperatorExpression, gen_eol_PropertyCallExpression_FeatureCallExpression, gen_eol_RealExpression_PrimitiveExpression, gen_eol_StringExpression_PrimitiveExpression, gen_eol_VariableDeclarationExpression_Expression, gen_eol_UnaryOperatorExpression_OperatorExpression, gen_eol_NegativeOperatorExpression_UnaryOperatorExpression, gen_eol_NotEqualsOperatorExpression_ComparisonOperatorExpression, gen_eol_NotOperatorExpression_UnaryOperatorExpression, gen_eol_OrOperatorExpression_LogicalOperatorExpression, gen_eol_OperationDefinition_EolElement, gen_eol_XorOperatorExpression_LogicalOperatorExpression, gen_eol_BreakStatement_Statement, gen_eol_BreakAllStatement_Statement, gen_eol_ContinueStatement_Statement, gen_eol_DeleteStatement_Statement, gen_eol_ForStatement_Statement, gen_eol_AssignmentStatement_Statement, gen_eol_ReturnStatement_Statement, gen_eol_SwitchStatement_Statement, gen_eol_IfStatement_Statement, gen_eol_WhileStatement_Statement, gen_eol_ModelDeclarationStatement_Statement, gen_eol_SwitchCaseStatement_Statement, gen_eol_FOLMethodCallExpression_FeatureCallExpression, gen_eol_ExpressionStatement_Statement, gen_eol_SwitchCaseDefaultStatement_SwitchCaseStatement, gen_eol_SetExpression_CollectionExpression, gen_eol_BagExpression_CollectionExpression, gen_eol_SequenceExpression_CollectionExpression, gen_eol_OrderedSetExpression_CollectionExpression, gen_eol_MapExpression_LiteralExpression, gen_eol_Type_EolElement, gen_eol_SwitchCaseExpressionStatement_SwitchCaseStatement, gen_eol_PrimitiveExpression_LiteralExpression, gen_eol_CollectionExpression_LiteralExpression, gen_eol_PrimitiveType_Type, gen_eol_BooleanType_PrimitiveType, gen_eol_IntegerType_PrimitiveType, gen_eol_RealType_PrimitiveType, gen_eol_StringType_PrimitiveType, gen_eol_SetType_UniqueCollectionType, gen_eol_BagType_CollectionType, gen_eol_SequenceType_OrderedCollectionType, gen_eol_OrderedSetType_OrderedCollectionType, gen_eol_OrderedSetType_UniqueCollectionType, gen_eol_MapType_Type, gen_eol_AnyType_Type, gen_eol_CollectionType_Type, gen_eol_SimpleAnnotation_Annotation, gen_eol_KeyValue_Expression, gen_eol_Annotation_EolElement, gen_eol_ExecutableAnnotation_Annotation, gen_eol_ModelExpression_NameExpression, gen_eol_AnnotationBlock_EolElement, gen_eol_ModelDeclarationParameter_Expression, gen_eol_SpecialNameExpression_NameExpression, gen_eol_ModelElementType_Type, gen_eol_NativeType_Type, gen_eol_FormalParameterExpression_VariableDeclarationExpression, gen_eol_CollectionInitValue_Expression, gen_eol_ExprList_CollectionInitValue, gen_eol_ExpRange_CollectionInitValue, gen_eol_ThrowStatement_Statement, gen_eol_NewExpression_Expression, gen_eol_AbortStatement_Statement, gen_eol_TransactionStatement_Statement, gen_eol_OrderedCollectionType_CollectionType, gen_eol_UniqueCollectionType_CollectionType, gen_eol_SelfInnermostType_PseudoType, gen_eol_SpecialAssignmentStatement_AssignmentStatement, gen_eol_OperationArgType_PseudoType, gen_eol_ModelType_Type, gen_eol_NativeExpression_LiteralExpression, gen_eol_EType_Type, gen_eol_VoidType_Type, gen_eol_PseudoType_Type, gen_eol_SelfType_PseudoType, gen_eol_SelfContentType_PseudoType, gen_eol_LogicalOperatorExpression_BinaryOperatorExpression, gen_eol_ComparisonOperatorExpression_BinaryOperatorExpression, gen_eol_ArithmeticOperatorExpression_BinaryOperatorExpression, gen_eol_ExpressionOrStatementBlock_EolElement, gen_eol_EolLibraryModule_EolElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)