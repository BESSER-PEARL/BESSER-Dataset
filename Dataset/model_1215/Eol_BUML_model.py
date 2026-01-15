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
eol_EolElement = Class(name="eol::EolElement", is_abstract=True)
eol_TextRegion = Class(name="eol::TextRegion")
eol_TextPosition = Class(name="eol::TextPosition")
eol_Program = Class(name="eol::Program")
EolElement = Class(name="EolElement")
eol_Import = Class(name="eol::Import")
eol_StringExpression = Class(name="eol::StringExpression")
eol_Statement = Class(name="eol::Statement", is_abstract=True)
eol_Expression = Class(name="eol::Expression", is_abstract=True)
eol_Type = Class(name="eol::Type")
eol_OperatorExpression = Class(name="eol::OperatorExpression", is_abstract=True)
Expression = Class(name="Expression")
eol_BinaryOperatorExpression = Class(name="eol::BinaryOperatorExpression", is_abstract=True)
OperatorExpression = Class(name="OperatorExpression")
eol_AndOperatorExpression = Class(name="eol::AndOperatorExpression")
BinaryOperatorExpression = Class(name="BinaryOperatorExpression")
eol_LiteralExpression = Class(name="eol::LiteralExpression", is_abstract=True)
eol_BooleanExpression = Class(name="eol::BooleanExpression")
PrimitiveExpression = Class(name="PrimitiveExpression")
eol_DivideOperatorExpression = Class(name="eol::DivideOperatorExpression")
eol_OperationDefinition = Class(name="eol::OperationDefinition")
eol_Block = Class(name="eol::Block")
eol_NameExpression = Class(name="eol::NameExpression")
eol_ModelDeclarationStatement = Class(name="eol::ModelDeclarationStatement")
eol_FeatureCallExpression = Class(name="eol::FeatureCallExpression", is_abstract=True)
eol_GreaterThanOperatorExpression = Class(name="eol::GreaterThanOperatorExpression")
eol_GreaterThanOrEqualToOperatorExpression = Class(name="eol::GreaterThanOrEqualToOperatorExpression")
eol_ImpliesOperatorExpression = Class(name="eol::ImpliesOperatorExpression")
eol_IntegerExpression = Class(name="eol::IntegerExpression")
eol_LessThanOperatorExpression = Class(name="eol::LessThanOperatorExpression")
eol_LessThanOrEqualToOperatorExpression = Class(name="eol::LessThanOrEqualToOperatorExpression")
eol_MethodCallExpression = Class(name="eol::MethodCallExpression")
FeatureCallExpression = Class(name="FeatureCallExpression")
eol_EObject = Class(name="eol::EObject")
eol_MinusOperatorExpression = Class(name="eol::MinusOperatorExpression")
eol_MultiplyOperatorExpression = Class(name="eol::MultiplyOperatorExpression")
eol_EnumerationLiteralExpression = Class(name="eol::EnumerationLiteralExpression")
eol_ModelExpression = Class(name="eol::ModelExpression")
eol_EqualsOperatorExpression = Class(name="eol::EqualsOperatorExpression")
eol_OrOperatorExpression = Class(name="eol::OrOperatorExpression")
eol_PlusOperatorExpression = Class(name="eol::PlusOperatorExpression")
eol_PropertyCallExpression = Class(name="eol::PropertyCallExpression")
eol_RealExpression = Class(name="eol::RealExpression")
eol_VariableDeclarationExpression = Class(name="eol::VariableDeclarationExpression")
eol_XorOperatorExpression = Class(name="eol::XorOperatorExpression")
eol_UnaryOperatorExpression = Class(name="eol::UnaryOperatorExpression", is_abstract=True)
eol_NegativeOperatorExpression = Class(name="eol::NegativeOperatorExpression")
UnaryOperatorExpression = Class(name="UnaryOperatorExpression")
eol_NotEqualsOperatorExpression = Class(name="eol::NotEqualsOperatorExpression")
eol_NotOperatorExpression = Class(name="eol::NotOperatorExpression")
eol_AssignmentStatement = Class(name="eol::AssignmentStatement")
Statement = Class(name="Statement")
eol_BreakStatement = Class(name="eol::BreakStatement")
eol_BreakAllStatement = Class(name="eol::BreakAllStatement")
eol_ContinueStatement = Class(name="eol::ContinueStatement")
eol_DeleteStatement = Class(name="eol::DeleteStatement")
eol_ForStatement = Class(name="eol::ForStatement")
eol_AnnotationBlock = Class(name="eol::AnnotationBlock")
eol_FormalParameterExpression = Class(name="eol::FormalParameterExpression")
eol_ReturnStatement = Class(name="eol::ReturnStatement")
eol_SwitchStatement = Class(name="eol::SwitchStatement")
eol_SwitchCaseExpressionStatement = Class(name="eol::SwitchCaseExpressionStatement")
eol_SwitchCaseDefaultStatement = Class(name="eol::SwitchCaseDefaultStatement")
eol_SwitchCaseStatement = Class(name="eol::SwitchCaseStatement", is_abstract=True)
eol_WhileStatement = Class(name="eol::WhileStatement")
eol_EPackage = Class(name="eol::EPackage")
eol_IfStatement = Class(name="eol::IfStatement")
eol_ModelDeclarationParameter = Class(name="eol::ModelDeclarationParameter")
eol_FOLMethodCallExpression = Class(name="eol::FOLMethodCallExpression")
eol_ExpressionStatement = Class(name="eol::ExpressionStatement")
SwitchCaseStatement = Class(name="SwitchCaseStatement")
eol_SetExpression = Class(name="eol::SetExpression")
CollectionExpression = Class(name="CollectionExpression")
eol_BagExpression = Class(name="eol::BagExpression")
eol_SequenceExpression = Class(name="eol::SequenceExpression")
eol_OrderedSetExpression = Class(name="eol::OrderedSetExpression")
eol_MapExpression = Class(name="eol::MapExpression")
eol_KeyValue = Class(name="eol::KeyValue")
eol_AnyType = Class(name="eol::AnyType")
Type = Class(name="Type")
eol_CollectionType = Class(name="eol::CollectionType")
eol_PrimitiveType = Class(name="eol::PrimitiveType", is_abstract=True)
eol_BooleanType = Class(name="eol::BooleanType")
PrimitiveType = Class(name="PrimitiveType")
eol_IntegerType = Class(name="eol::IntegerType")
eol_RealType = Class(name="eol::RealType")
eol_StringType = Class(name="eol::StringType")
eol_SetType = Class(name="eol::SetType")
UniqueCollectionType = Class(name="UniqueCollectionType")
eol_BagType = Class(name="eol::BagType")
eol_PrimitiveExpression = Class(name="eol::PrimitiveExpression", is_abstract=True)
LiteralExpression = Class(name="LiteralExpression")
eol_CollectionExpression = Class(name="eol::CollectionExpression", is_abstract=True)
eol_CollectionInitValue = Class(name="eol::CollectionInitValue", is_abstract=True)
eol_Annotation = Class(name="eol::Annotation", is_abstract=True)
eol_ExecutableAnnotation = Class(name="eol::ExecutableAnnotation")
Annotation = Class(name="Annotation")
eol_SimpleAnnotation = Class(name="eol::SimpleAnnotation")
eol_SpecialNameExpression = Class(name="eol::SpecialNameExpression")
NameExpression = Class(name="NameExpression")
eol_ModelElementType = Class(name="eol::ModelElementType")
eol_EClassifier = Class(name="eol::EClassifier")
CollectionType = Class(name="CollectionType")
eol_SequenceType = Class(name="eol::SequenceType")
OrderedCollectionType = Class(name="OrderedCollectionType")
eol_OrderedSetType = Class(name="eol::OrderedSetType")
eol_MapType = Class(name="eol::MapType")
eol_ThrowStatement = Class(name="eol::ThrowStatement")
eol_AbortStatement = Class(name="eol::AbortStatement")
eol_TransactionStatement = Class(name="eol::TransactionStatement")
VariableDeclarationExpression = Class(name="VariableDeclarationExpression")
eol_ExprList = Class(name="eol::ExprList")
CollectionInitValue = Class(name="CollectionInitValue")
eol_NativeType = Class(name="eol::NativeType")
eol_SpecialAssignmentStatement = Class(name="eol::SpecialAssignmentStatement")
AssignmentStatement = Class(name="AssignmentStatement")
eol_ModelType = Class(name="eol::ModelType")
eol_NativeExpression = Class(name="eol::NativeExpression")
eol_EType = Class(name="eol::EType")
eol_VoidType = Class(name="eol::VoidType")
eol_PseudoType = Class(name="eol::PseudoType")
eol_SelfType = Class(name="eol::SelfType")
PseudoType = Class(name="PseudoType")
eol_SelfContentType = Class(name="eol::SelfContentType")
eol_OrderedCollectionType = Class(name="eol::OrderedCollectionType")
eol_ExpRange = Class(name="eol::ExpRange")
eol_NewExpression = Class(name="eol::NewExpression")
eol_UniqueCollectionType = Class(name="eol::UniqueCollectionType")
eol_SelfInnermostType = Class(name="eol::SelfInnermostType")
eol_OperationArgType = Class(name="eol::OperationArgType")

# eol_EolElement class attributes and methods
eol_EolElement_line: Property = Property(name="line", type=IntegerType)
eol_EolElement_column: Property = Property(name="column", type=IntegerType)
eol_EolElement_uri: Property = Property(name="uri", type=StringType)
eol_EolElement.attributes={eol_EolElement_column, eol_EolElement_uri, eol_EolElement_line}

# eol_TextRegion class attributes and methods

# eol_TextPosition class attributes and methods
eol_TextPosition_line: Property = Property(name="line", type=IntegerType)
eol_TextPosition_column: Property = Property(name="column", type=IntegerType)
eol_TextPosition.attributes={eol_TextPosition_column, eol_TextPosition_line}

# eol_Program class attributes and methods

# EolElement class attributes and methods

# eol_Import class attributes and methods

# eol_StringExpression class attributes and methods
eol_StringExpression_val: Property = Property(name="val", type=StringType)
eol_StringExpression.attributes={eol_StringExpression_val}

# eol_Statement class attributes and methods

# eol_Expression class attributes and methods

# eol_Type class attributes and methods

# eol_OperatorExpression class attributes and methods

# Expression class attributes and methods

# eol_BinaryOperatorExpression class attributes and methods

# OperatorExpression class attributes and methods

# eol_AndOperatorExpression class attributes and methods

# BinaryOperatorExpression class attributes and methods

# eol_LiteralExpression class attributes and methods

# eol_BooleanExpression class attributes and methods
eol_BooleanExpression_val: Property = Property(name="val", type=BooleanType)
eol_BooleanExpression.attributes={eol_BooleanExpression_val}

# PrimitiveExpression class attributes and methods

# eol_DivideOperatorExpression class attributes and methods

# eol_OperationDefinition class attributes and methods

# eol_Block class attributes and methods

# eol_NameExpression class attributes and methods
eol_NameExpression_name: Property = Property(name="name", type=StringType)
eol_NameExpression_resolvedContent: Property = Property(name="resolvedContent", type=StringType)
eol_NameExpression.attributes={eol_NameExpression_resolvedContent, eol_NameExpression_name}

# eol_ModelDeclarationStatement class attributes and methods

# eol_FeatureCallExpression class attributes and methods

# eol_GreaterThanOperatorExpression class attributes and methods

# eol_GreaterThanOrEqualToOperatorExpression class attributes and methods

# eol_ImpliesOperatorExpression class attributes and methods

# eol_IntegerExpression class attributes and methods
eol_IntegerExpression_val: Property = Property(name="val", type=IntegerType)
eol_IntegerExpression.attributes={eol_IntegerExpression_val}

# eol_LessThanOperatorExpression class attributes and methods

# eol_LessThanOrEqualToOperatorExpression class attributes and methods

# eol_MethodCallExpression class attributes and methods

# FeatureCallExpression class attributes and methods

# eol_EObject class attributes and methods

# eol_MinusOperatorExpression class attributes and methods

# eol_MultiplyOperatorExpression class attributes and methods

# eol_EnumerationLiteralExpression class attributes and methods

# eol_ModelExpression class attributes and methods

# eol_EqualsOperatorExpression class attributes and methods

# eol_OrOperatorExpression class attributes and methods

# eol_PlusOperatorExpression class attributes and methods

# eol_PropertyCallExpression class attributes and methods

# eol_RealExpression class attributes and methods
eol_RealExpression_val: Property = Property(name="val", type=FloatType)
eol_RealExpression.attributes={eol_RealExpression_val}

# eol_VariableDeclarationExpression class attributes and methods
eol_VariableDeclarationExpression_lastDefinitionPoint: Property = Property(name="lastDefinitionPoint", type=StringType)
eol_VariableDeclarationExpression.attributes={eol_VariableDeclarationExpression_lastDefinitionPoint}

# eol_XorOperatorExpression class attributes and methods

# eol_UnaryOperatorExpression class attributes and methods

# eol_NegativeOperatorExpression class attributes and methods

# UnaryOperatorExpression class attributes and methods

# eol_NotEqualsOperatorExpression class attributes and methods

# eol_NotOperatorExpression class attributes and methods

# eol_AssignmentStatement class attributes and methods

# Statement class attributes and methods

# eol_BreakStatement class attributes and methods

# eol_BreakAllStatement class attributes and methods

# eol_ContinueStatement class attributes and methods

# eol_DeleteStatement class attributes and methods

# eol_ForStatement class attributes and methods

# eol_AnnotationBlock class attributes and methods

# eol_FormalParameterExpression class attributes and methods

# eol_ReturnStatement class attributes and methods

# eol_SwitchStatement class attributes and methods

# eol_SwitchCaseExpressionStatement class attributes and methods

# eol_SwitchCaseDefaultStatement class attributes and methods

# eol_SwitchCaseStatement class attributes and methods

# eol_WhileStatement class attributes and methods

# eol_EPackage class attributes and methods

# eol_IfStatement class attributes and methods

# eol_ModelDeclarationParameter class attributes and methods

# eol_FOLMethodCallExpression class attributes and methods

# eol_ExpressionStatement class attributes and methods

# SwitchCaseStatement class attributes and methods

# eol_SetExpression class attributes and methods

# CollectionExpression class attributes and methods

# eol_BagExpression class attributes and methods

# eol_SequenceExpression class attributes and methods

# eol_OrderedSetExpression class attributes and methods

# eol_MapExpression class attributes and methods

# eol_KeyValue class attributes and methods

# eol_AnyType class attributes and methods

# Type class attributes and methods

# eol_CollectionType class attributes and methods

# eol_PrimitiveType class attributes and methods

# eol_BooleanType class attributes and methods

# PrimitiveType class attributes and methods

# eol_IntegerType class attributes and methods

# eol_RealType class attributes and methods

# eol_StringType class attributes and methods

# eol_SetType class attributes and methods

# UniqueCollectionType class attributes and methods

# eol_BagType class attributes and methods

# eol_PrimitiveExpression class attributes and methods

# LiteralExpression class attributes and methods

# eol_CollectionExpression class attributes and methods

# eol_CollectionInitValue class attributes and methods

# eol_Annotation class attributes and methods

# eol_ExecutableAnnotation class attributes and methods

# Annotation class attributes and methods

# eol_SimpleAnnotation class attributes and methods

# eol_SpecialNameExpression class attributes and methods

# NameExpression class attributes and methods

# eol_ModelElementType class attributes and methods
eol_ModelElementType_modelName: Property = Property(name="modelName", type=StringType)
eol_ModelElementType_elementName: Property = Property(name="elementName", type=StringType)
eol_ModelElementType.attributes={eol_ModelElementType_elementName, eol_ModelElementType_modelName}

# eol_EClassifier class attributes and methods

# CollectionType class attributes and methods

# eol_SequenceType class attributes and methods

# OrderedCollectionType class attributes and methods

# eol_OrderedSetType class attributes and methods

# eol_MapType class attributes and methods

# eol_ThrowStatement class attributes and methods

# eol_AbortStatement class attributes and methods

# eol_TransactionStatement class attributes and methods

# VariableDeclarationExpression class attributes and methods

# eol_ExprList class attributes and methods

# CollectionInitValue class attributes and methods

# eol_NativeType class attributes and methods

# eol_SpecialAssignmentStatement class attributes and methods

# AssignmentStatement class attributes and methods

# eol_ModelType class attributes and methods

# eol_NativeExpression class attributes and methods

# eol_EType class attributes and methods

# eol_VoidType class attributes and methods

# eol_PseudoType class attributes and methods

# eol_SelfType class attributes and methods

# PseudoType class attributes and methods

# eol_SelfContentType class attributes and methods

# eol_OrderedCollectionType class attributes and methods

# eol_ExpRange class attributes and methods

# eol_NewExpression class attributes and methods

# eol_UniqueCollectionType class attributes and methods

# eol_SelfInnermostType class attributes and methods

# eol_OperationArgType class attributes and methods

# Relationships
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
end6: BinaryAssociation = BinaryAssociation(
    name="end6",
    ends={
        Property(name="eol_TextPosition8", type=eol_TextRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TextRegion7", type=eol_TextPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports9: BinaryAssociation = BinaryAssociation(
    name="imports9",
    ends={
        Property(name="eol_Import", type=eol_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Program", type=eol_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedModules11: BinaryAssociation = BinaryAssociation(
    name="importedModules11",
    ends={
        Property(name="eol_Program12", type=eol_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Program10", type=eol_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imported21: BinaryAssociation = BinaryAssociation(
    name="imported21",
    ends={
        Property(name="eol_StringExpression", type=eol_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Import22", type=eol_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
importedProgram23: BinaryAssociation = BinaryAssociation(
    name="importedProgram23",
    ends={
        Property(name="eol_Program25", type=eol_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Import24", type=eol_Program, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedType26: BinaryAssociation = BinaryAssociation(
    name="resolvedType26",
    ends={
        Property(name="eol_Type", type=eol_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Expression", type=eol_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements27: BinaryAssociation = BinaryAssociation(
    name="statements27",
    ends={
        Property(name="eol_Statement", type=eol_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Block28", type=eol_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs29: BinaryAssociation = BinaryAssociation(
    name="lhs29",
    ends={
        Property(name="eol_Expression30", type=eol_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_BinaryOperatorExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs31: BinaryAssociation = BinaryAssociation(
    name="rhs31",
    ends={
        Property(name="eol_Expression33", type=eol_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_BinaryOperatorExpression32", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operations13: BinaryAssociation = BinaryAssociation(
    name="operations13",
    ends={
        Property(name="eol_OperationDefinition", type=eol_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Program14", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block15: BinaryAssociation = BinaryAssociation(
    name="block15",
    ends={
        Property(name="eol_Block", type=eol_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Program16", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name17: BinaryAssociation = BinaryAssociation(
    name="name17",
    ends={
        Property(name="eol_NameExpression", type=eol_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Program18", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelDeclarations19: BinaryAssociation = BinaryAssociation(
    name="modelDeclarations19",
    ends={
        Property(name="eol_ModelDeclarationStatement", type=eol_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Program20", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target41: BinaryAssociation = BinaryAssociation(
    name="target41",
    ends={
        Property(name="eol_Expression42", type=eol_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FeatureCallExpression", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isArrow43: BinaryAssociation = BinaryAssociation(
    name="isArrow43",
    ends={
        Property(name="eol_BooleanExpression", type=eol_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FeatureCallExpression44", type=eol_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments45: BinaryAssociation = BinaryAssociation(
    name="arguments45",
    ends={
        Property(name="eol_Expression46", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method47: BinaryAssociation = BinaryAssociation(
    name="method47",
    ends={
        Property(name="eol_NameExpression49", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression48", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedMethods50: BinaryAssociation = BinaryAssociation(
    name="resolvedMethods50",
    ends={
        Property(name="eol_EObject", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression51", type=eol_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
isType52: BinaryAssociation = BinaryAssociation(
    name="isType52",
    ends={
        Property(name="eol_BooleanExpression54", type=eol_NameExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NameExpression53", type=eol_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumeration34: BinaryAssociation = BinaryAssociation(
    name="enumeration34",
    ends={
        Property(name="eol_NameExpression35", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literal36: BinaryAssociation = BinaryAssociation(
    name="literal36",
    ends={
        Property(name="eol_NameExpression38", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression37", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model39: BinaryAssociation = BinaryAssociation(
    name="model39",
    ends={
        Property(name="eol_ModelExpression", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression40", type=eol_ModelExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property57: BinaryAssociation = BinaryAssociation(
    name="property57",
    ends={
        Property(name="eol_NameExpression58", type=eol_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_PropertyCallExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extended59: BinaryAssociation = BinaryAssociation(
    name="extended59",
    ends={
        Property(name="eol_BooleanExpression61", type=eol_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_PropertyCallExpression60", type=eol_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name62: BinaryAssociation = BinaryAssociation(
    name="name62",
    ends={
        Property(name="eol_NameExpression63", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
create64: BinaryAssociation = BinaryAssociation(
    name="create64",
    ends={
        Property(name="eol_BooleanExpression66", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression65", type=eol_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters67: BinaryAssociation = BinaryAssociation(
    name="parameters67",
    ends={
        Property(name="eol_Expression69", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression68", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextType70: BinaryAssociation = BinaryAssociation(
    name="contextType70",
    ends={
        Property(name="eol_Type72", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition71", type=eol_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr55: BinaryAssociation = BinaryAssociation(
    name="expr55",
    ends={
        Property(name="eol_Expression56", type=eol_UnaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_UnaryOperatorExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
self86: BinaryAssociation = BinaryAssociation(
    name="self86",
    ends={
        Property(name="eol_VariableDeclarationExpression88", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition87", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
_result89: BinaryAssociation = BinaryAssociation(
    name="_result89",
    ends={
        Property(name="eol_VariableDeclarationExpression91", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition90", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs92: BinaryAssociation = BinaryAssociation(
    name="lhs92",
    ends={
        Property(name="eol_Expression93", type=eol_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AssignmentStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs94: BinaryAssociation = BinaryAssociation(
    name="rhs94",
    ends={
        Property(name="eol_Expression96", type=eol_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AssignmentStatement95", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
deleted97: BinaryAssociation = BinaryAssociation(
    name="deleted97",
    ends={
        Property(name="eol_Expression98", type=eol_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_DeleteStatement", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterator99: BinaryAssociation = BinaryAssociation(
    name="iterator99",
    ends={
        Property(name="eol_FormalParameterExpression100", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement", type=eol_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterated101: BinaryAssociation = BinaryAssociation(
    name="iterated101",
    ends={
        Property(name="eol_Expression103", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement102", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType73: BinaryAssociation = BinaryAssociation(
    name="returnType73",
    ends={
        Property(name="eol_Type75", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition74", type=eol_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationBlock76: BinaryAssociation = BinaryAssociation(
    name="annotationBlock76",
    ends={
        Property(name="eol_AnnotationBlock", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition77", type=eol_AnnotationBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body78: BinaryAssociation = BinaryAssociation(
    name="body78",
    ends={
        Property(name="eol_Block80", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition79", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name81: BinaryAssociation = BinaryAssociation(
    name="name81",
    ends={
        Property(name="eol_NameExpression83", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition82", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters84: BinaryAssociation = BinaryAssociation(
    name="parameters84",
    ends={
        Property(name="eol_FormalParameterExpression", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition85", type=eol_FormalParameterExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returned115: BinaryAssociation = BinaryAssociation(
    name="returned115",
    ends={
        Property(name="eol_Expression116", type=eol_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ReturnStatement", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression117: BinaryAssociation = BinaryAssociation(
    name="expression117",
    ends={
        Property(name="eol_Expression118", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases119: BinaryAssociation = BinaryAssociation(
    name="cases119",
    ends={
        Property(name="eol_SwitchCaseExpressionStatement", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement120", type=eol_SwitchCaseExpressionStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default121: BinaryAssociation = BinaryAssociation(
    name="default121",
    ends={
        Property(name="eol_SwitchCaseDefaultStatement", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement122", type=eol_SwitchCaseDefaultStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body123: BinaryAssociation = BinaryAssociation(
    name="body123",
    ends={
        Property(name="eol_Block124", type=eol_SwitchCaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchCaseStatement", type=eol_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition125: BinaryAssociation = BinaryAssociation(
    name="condition125",
    ends={
        Property(name="eol_Expression126", type=eol_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_WhileStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body127: BinaryAssociation = BinaryAssociation(
    name="body127",
    ends={
        Property(name="eol_Block129", type=eol_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_WhileStatement128", type=eol_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
packages130: BinaryAssociation = BinaryAssociation(
    name="packages130",
    ends={
        Property(name="eol_EPackage", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement131", type=eol_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name132: BinaryAssociation = BinaryAssociation(
    name="name132",
    ends={
        Property(name="eol_NameExpression134", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement133", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body104: BinaryAssociation = BinaryAssociation(
    name="body104",
    ends={
        Property(name="eol_Block106", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement105", type=eol_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition107: BinaryAssociation = BinaryAssociation(
    name="condition107",
    ends={
        Property(name="eol_Expression108", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifBody109: BinaryAssociation = BinaryAssociation(
    name="ifBody109",
    ends={
        Property(name="eol_Block111", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement110", type=eol_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBody112: BinaryAssociation = BinaryAssociation(
    name="elseBody112",
    ends={
        Property(name="eol_Block114", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement113", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
driver138: BinaryAssociation = BinaryAssociation(
    name="driver138",
    ends={
        Property(name="eol_NameExpression140", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement139", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters141: BinaryAssociation = BinaryAssociation(
    name="parameters141",
    ends={
        Property(name="eol_ModelDeclarationParameter", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement142", type=eol_ModelDeclarationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EReference0144: BinaryAssociation = BinaryAssociation(
    name="EReference0144",
    ends={
        Property(name="eol_ModelDeclarationStatement145", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement143", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(0, 1))
    }
)
iterators146: BinaryAssociation = BinaryAssociation(
    name="iterators146",
    ends={
        Property(name="eol_FormalParameterExpression147", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression", type=eol_FormalParameterExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
conditions148: BinaryAssociation = BinaryAssociation(
    name="conditions148",
    ends={
        Property(name="eol_Expression150", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression149", type=eol_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
method151: BinaryAssociation = BinaryAssociation(
    name="method151",
    ends={
        Property(name="eol_NameExpression153", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression152", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression154: BinaryAssociation = BinaryAssociation(
    name="expression154",
    ends={
        Property(name="eol_Expression155", type=eol_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression156: BinaryAssociation = BinaryAssociation(
    name="expression156",
    ends={
        Property(name="eol_Expression158", type=eol_SwitchCaseExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchCaseExpressionStatement157", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alias135: BinaryAssociation = BinaryAssociation(
    name="alias135",
    ends={
        Property(name="eol_NameExpression137", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement136", type=eol_NameExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents163: BinaryAssociation = BinaryAssociation(
    name="contents163",
    ends={
        Property(name="eol_LiteralExpression", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression164", type=eol_LiteralExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyValues165: BinaryAssociation = BinaryAssociation(
    name="keyValues165",
    ends={
        Property(name="eol_KeyValue", type=eol_MapExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapExpression", type=eol_KeyValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dynamicType166: BinaryAssociation = BinaryAssociation(
    name="dynamicType166",
    ends={
        Property(name="eol_Type167", type=eol_AnyType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnyType", type=eol_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contentType168: BinaryAssociation = BinaryAssociation(
    name="contentType168",
    ends={
        Property(name="eol_Type169", type=eol_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionType", type=eol_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterList159: BinaryAssociation = BinaryAssociation(
    name="parameterList159",
    ends={
        Property(name="eol_CollectionInitValue", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression", type=eol_CollectionInitValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contentType160: BinaryAssociation = BinaryAssociation(
    name="contentType160",
    ends={
        Property(name="eol_Type162", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression161", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name175: BinaryAssociation = BinaryAssociation(
    name="name175",
    ends={
        Property(name="eol_NameExpression176", type=eol_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Annotation", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression177: BinaryAssociation = BinaryAssociation(
    name="expression177",
    ends={
        Property(name="eol_Expression178", type=eol_ExecutableAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExecutableAnnotation", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values179: BinaryAssociation = BinaryAssociation(
    name="values179",
    ends={
        Property(name="eol_StringExpression180", type=eol_SimpleAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SimpleAnnotation", type=eol_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key181: BinaryAssociation = BinaryAssociation(
    name="key181",
    ends={
        Property(name="eol_Expression183", type=eol_KeyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_KeyValue182", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value184: BinaryAssociation = BinaryAssociation(
    name="value184",
    ends={
        Property(name="eol_Expression186", type=eol_KeyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_KeyValue185", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ecoreType187: BinaryAssociation = BinaryAssociation(
    name="ecoreType187",
    ends={
        Property(name="eol_EClassifier", type=eol_ModelElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelElementType", type=eol_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
resolvedModelDeclaration188: BinaryAssociation = BinaryAssociation(
    name="resolvedModelDeclaration188",
    ends={
        Property(name="eol_ModelDeclarationStatement190", type=eol_ModelElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelElementType189", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(0, 1))
    }
)
valueType170: BinaryAssociation = BinaryAssociation(
    name="valueType170",
    ends={
        Property(name="eol_Type171", type=eol_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapType", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType172: BinaryAssociation = BinaryAssociation(
    name="keyType172",
    ends={
        Property(name="eol_Type174", type=eol_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapType173", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
executableAnnotations196: BinaryAssociation = BinaryAssociation(
    name="executableAnnotations196",
    ends={
        Property(name="eol_ExecutableAnnotation198", type=eol_AnnotationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnnotationBlock197", type=eol_ExecutableAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name199: BinaryAssociation = BinaryAssociation(
    name="name199",
    ends={
        Property(name="eol_NameExpression201", type=eol_ModelDeclarationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationParameter200", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value202: BinaryAssociation = BinaryAssociation(
    name="value202",
    ends={
        Property(name="eol_StringExpression204", type=eol_ModelDeclarationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationParameter203", type=eol_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thrown205: BinaryAssociation = BinaryAssociation(
    name="thrown205",
    ends={
        Property(name="eol_Expression206", type=eol_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ThrowStatement", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body207: BinaryAssociation = BinaryAssociation(
    name="body207",
    ends={
        Property(name="eol_Block208", type=eol_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TransactionStatement", type=eol_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
names209: BinaryAssociation = BinaryAssociation(
    name="names209",
    ends={
        Property(name="eol_NameExpression211", type=eol_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TransactionStatement210", type=eol_NameExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions212: BinaryAssociation = BinaryAssociation(
    name="expressions212",
    ends={
        Property(name="eol_Expression213", type=eol_ExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExprList", type=eol_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
nativeExpression191: BinaryAssociation = BinaryAssociation(
    name="nativeExpression191",
    ends={
        Property(name="eol_StringExpression192", type=eol_NativeType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NativeType", type=eol_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simpleAnnotations193: BinaryAssociation = BinaryAssociation(
    name="simpleAnnotations193",
    ends={
        Property(name="eol_SimpleAnnotation195", type=eol_AnnotationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnnotationBlock194", type=eol_SimpleAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters219: BinaryAssociation = BinaryAssociation(
    name="parameters219",
    ends={
        Property(name="eol_Expression220", type=eol_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NewExpression", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelName221: BinaryAssociation = BinaryAssociation(
    name="modelName221",
    ends={
        Property(name="eol_NameExpression222", type=eol_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelType", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model223: BinaryAssociation = BinaryAssociation(
    name="model223",
    ends={
        Property(name="eol_ModelDeclarationStatement225", type=eol_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelType224", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 9999))
    }
)
nativeExpr226: BinaryAssociation = BinaryAssociation(
    name="nativeExpr226",
    ends={
        Property(name="eol_StringExpression227", type=eol_NativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NativeExpression", type=eol_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isType228: BinaryAssociation = BinaryAssociation(
    name="isType228",
    ends={
        Property(name="eol_BooleanExpression230", type=eol_NativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NativeExpression229", type=eol_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ecoreType231: BinaryAssociation = BinaryAssociation(
    name="ecoreType231",
    ends={
        Property(name="eol_EClassifier232", type=eol_EType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EType", type=eol_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
start214: BinaryAssociation = BinaryAssociation(
    name="start214",
    ends={
        Property(name="eol_Expression215", type=eol_ExpRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpRange", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end216: BinaryAssociation = BinaryAssociation(
    name="end216",
    ends={
        Property(name="eol_Expression218", type=eol_ExpRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpRange217", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_eol_Program_EolElement = Generalization(general=EolElement, specific=eol_Program)
gen_eol_Import_EolElement = Generalization(general=EolElement, specific=eol_Import)
gen_eol_Statement_EolElement = Generalization(general=EolElement, specific=eol_Statement)
gen_eol_Expression_EolElement = Generalization(general=EolElement, specific=eol_Expression)
gen_eol_Block_EolElement = Generalization(general=EolElement, specific=eol_Block)
gen_eol_OperatorExpression_Expression = Generalization(general=Expression, specific=eol_OperatorExpression)
gen_eol_BinaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=eol_BinaryOperatorExpression)
gen_eol_AndOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_AndOperatorExpression)
gen_eol_LiteralExpression_Expression = Generalization(general=Expression, specific=eol_LiteralExpression)
gen_eol_BooleanExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_BooleanExpression)
gen_eol_DivideOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_DivideOperatorExpression)
gen_eol_FeatureCallExpression_Expression = Generalization(general=Expression, specific=eol_FeatureCallExpression)
gen_eol_GreaterThanOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_GreaterThanOperatorExpression)
gen_eol_GreaterThanOrEqualToOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_GreaterThanOrEqualToOperatorExpression)
gen_eol_ImpliesOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_ImpliesOperatorExpression)
gen_eol_IntegerExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_IntegerExpression)
gen_eol_LessThanOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_LessThanOperatorExpression)
gen_eol_LessThanOrEqualToOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_LessThanOrEqualToOperatorExpression)
gen_eol_MethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_MethodCallExpression)
gen_eol_MinusOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_MinusOperatorExpression)
gen_eol_MultiplyOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_MultiplyOperatorExpression)
gen_eol_NameExpression_Expression = Generalization(general=Expression, specific=eol_NameExpression)
gen_eol_EnumerationLiteralExpression_Expression = Generalization(general=Expression, specific=eol_EnumerationLiteralExpression)
gen_eol_EqualsOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_EqualsOperatorExpression)
gen_eol_OrOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_OrOperatorExpression)
gen_eol_PlusOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_PlusOperatorExpression)
gen_eol_PropertyCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_PropertyCallExpression)
gen_eol_RealExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_RealExpression)
gen_eol_StringExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_StringExpression)
gen_eol_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=eol_VariableDeclarationExpression)
gen_eol_XorOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_XorOperatorExpression)
gen_eol_OperationDefinition_EolElement = Generalization(general=EolElement, specific=eol_OperationDefinition)
gen_eol_UnaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=eol_UnaryOperatorExpression)
gen_eol_NegativeOperatorExpression_UnaryOperatorExpression = Generalization(general=UnaryOperatorExpression, specific=eol_NegativeOperatorExpression)
gen_eol_NotEqualsOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_NotEqualsOperatorExpression)
gen_eol_NotOperatorExpression_UnaryOperatorExpression = Generalization(general=UnaryOperatorExpression, specific=eol_NotOperatorExpression)
gen_eol_AssignmentStatement_Statement = Generalization(general=Statement, specific=eol_AssignmentStatement)
gen_eol_BreakStatement_Statement = Generalization(general=Statement, specific=eol_BreakStatement)
gen_eol_BreakAllStatement_Statement = Generalization(general=Statement, specific=eol_BreakAllStatement)
gen_eol_ContinueStatement_Statement = Generalization(general=Statement, specific=eol_ContinueStatement)
gen_eol_DeleteStatement_Statement = Generalization(general=Statement, specific=eol_DeleteStatement)
gen_eol_ForStatement_Statement = Generalization(general=Statement, specific=eol_ForStatement)
gen_eol_ReturnStatement_Statement = Generalization(general=Statement, specific=eol_ReturnStatement)
gen_eol_SwitchStatement_Statement = Generalization(general=Statement, specific=eol_SwitchStatement)
gen_eol_SwitchCaseStatement_Statement = Generalization(general=Statement, specific=eol_SwitchCaseStatement)
gen_eol_WhileStatement_Statement = Generalization(general=Statement, specific=eol_WhileStatement)
gen_eol_ModelDeclarationStatement_Statement = Generalization(general=Statement, specific=eol_ModelDeclarationStatement)
gen_eol_IfStatement_Statement = Generalization(general=Statement, specific=eol_IfStatement)
gen_eol_FOLMethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_FOLMethodCallExpression)
gen_eol_ExpressionStatement_Statement = Generalization(general=Statement, specific=eol_ExpressionStatement)
gen_eol_SwitchCaseDefaultStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_SwitchCaseDefaultStatement)
gen_eol_SwitchCaseExpressionStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_SwitchCaseExpressionStatement)
gen_eol_SetExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_SetExpression)
gen_eol_BagExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_BagExpression)
gen_eol_SequenceExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_SequenceExpression)
gen_eol_OrderedSetExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_OrderedSetExpression)
gen_eol_MapExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=eol_MapExpression)
gen_eol_Type_EolElement = Generalization(general=EolElement, specific=eol_Type)
gen_eol_AnyType_Type = Generalization(general=Type, specific=eol_AnyType)
gen_eol_CollectionType_Type = Generalization(general=Type, specific=eol_CollectionType)
gen_eol_PrimitiveType_Type = Generalization(general=Type, specific=eol_PrimitiveType)
gen_eol_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_BooleanType)
gen_eol_IntegerType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_IntegerType)
gen_eol_RealType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_RealType)
gen_eol_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_StringType)
gen_eol_SetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_SetType)
gen_eol_PrimitiveExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=eol_PrimitiveExpression)
gen_eol_CollectionExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=eol_CollectionExpression)
gen_eol_Annotation_EolElement = Generalization(general=EolElement, specific=eol_Annotation)
gen_eol_ExecutableAnnotation_Annotation = Generalization(general=Annotation, specific=eol_ExecutableAnnotation)
gen_eol_SimpleAnnotation_Annotation = Generalization(general=Annotation, specific=eol_SimpleAnnotation)
gen_eol_KeyValue_EolElement = Generalization(general=EolElement, specific=eol_KeyValue)
gen_eol_SpecialNameExpression_NameExpression = Generalization(general=NameExpression, specific=eol_SpecialNameExpression)
gen_eol_ModelElementType_Type = Generalization(general=Type, specific=eol_ModelElementType)
gen_eol_BagType_CollectionType = Generalization(general=CollectionType, specific=eol_BagType)
gen_eol_SequenceType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_SequenceType)
gen_eol_OrderedSetType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_OrderedSetType)
gen_eol_OrderedSetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_OrderedSetType)
gen_eol_MapType_Type = Generalization(general=Type, specific=eol_MapType)
gen_eol_ModelDeclarationParameter_EolElement = Generalization(general=EolElement, specific=eol_ModelDeclarationParameter)
gen_eol_ThrowStatement_Statement = Generalization(general=Statement, specific=eol_ThrowStatement)
gen_eol_AbortStatement_Statement = Generalization(general=Statement, specific=eol_AbortStatement)
gen_eol_TransactionStatement_Statement = Generalization(general=Statement, specific=eol_TransactionStatement)
gen_eol_FormalParameterExpression_VariableDeclarationExpression = Generalization(general=VariableDeclarationExpression, specific=eol_FormalParameterExpression)
gen_eol_CollectionInitValue_EolElement = Generalization(general=EolElement, specific=eol_CollectionInitValue)
gen_eol_ExprList_CollectionInitValue = Generalization(general=CollectionInitValue, specific=eol_ExprList)
gen_eol_NativeType_Type = Generalization(general=Type, specific=eol_NativeType)
gen_eol_ModelExpression_NameExpression = Generalization(general=NameExpression, specific=eol_ModelExpression)
gen_eol_AnnotationBlock_EolElement = Generalization(general=EolElement, specific=eol_AnnotationBlock)
gen_eol_SpecialAssignmentStatement_AssignmentStatement = Generalization(general=AssignmentStatement, specific=eol_SpecialAssignmentStatement)
gen_eol_ModelType_Type = Generalization(general=Type, specific=eol_ModelType)
gen_eol_NativeExpression_LiteralExpression = Generalization(general=LiteralExpression, specific=eol_NativeExpression)
gen_eol_EType_Type = Generalization(general=Type, specific=eol_EType)
gen_eol_VoidType_Type = Generalization(general=Type, specific=eol_VoidType)
gen_eol_PseudoType_Type = Generalization(general=Type, specific=eol_PseudoType)
gen_eol_SelfType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfType)
gen_eol_SelfContentType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfContentType)
gen_eol_OrderedCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_OrderedCollectionType)
gen_eol_ExpRange_CollectionInitValue = Generalization(general=CollectionInitValue, specific=eol_ExpRange)
gen_eol_NewExpression_Expression = Generalization(general=Expression, specific=eol_NewExpression)
gen_eol_UniqueCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_UniqueCollectionType)
gen_eol_SelfInnermostType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfInnermostType)
gen_eol_OperationArgType_PseudoType = Generalization(general=PseudoType, specific=eol_OperationArgType)

# Domain Model
domain_model = DomainModel(
    name="eol",
    types={eol_EolElement, eol_TextRegion, eol_TextPosition, eol_Program, EolElement, eol_Import, eol_StringExpression, eol_Statement, eol_Expression, eol_Type, eol_OperatorExpression, Expression, eol_BinaryOperatorExpression, OperatorExpression, eol_AndOperatorExpression, BinaryOperatorExpression, eol_LiteralExpression, eol_BooleanExpression, PrimitiveExpression, eol_DivideOperatorExpression, eol_OperationDefinition, eol_Block, eol_NameExpression, eol_ModelDeclarationStatement, eol_FeatureCallExpression, eol_GreaterThanOperatorExpression, eol_GreaterThanOrEqualToOperatorExpression, eol_ImpliesOperatorExpression, eol_IntegerExpression, eol_LessThanOperatorExpression, eol_LessThanOrEqualToOperatorExpression, eol_MethodCallExpression, FeatureCallExpression, eol_EObject, eol_MinusOperatorExpression, eol_MultiplyOperatorExpression, eol_EnumerationLiteralExpression, eol_ModelExpression, eol_EqualsOperatorExpression, eol_OrOperatorExpression, eol_PlusOperatorExpression, eol_PropertyCallExpression, eol_RealExpression, eol_VariableDeclarationExpression, eol_XorOperatorExpression, eol_UnaryOperatorExpression, eol_NegativeOperatorExpression, UnaryOperatorExpression, eol_NotEqualsOperatorExpression, eol_NotOperatorExpression, eol_AssignmentStatement, Statement, eol_BreakStatement, eol_BreakAllStatement, eol_ContinueStatement, eol_DeleteStatement, eol_ForStatement, eol_AnnotationBlock, eol_FormalParameterExpression, eol_ReturnStatement, eol_SwitchStatement, eol_SwitchCaseExpressionStatement, eol_SwitchCaseDefaultStatement, eol_SwitchCaseStatement, eol_WhileStatement, eol_EPackage, eol_IfStatement, eol_ModelDeclarationParameter, eol_FOLMethodCallExpression, eol_ExpressionStatement, SwitchCaseStatement, eol_SetExpression, CollectionExpression, eol_BagExpression, eol_SequenceExpression, eol_OrderedSetExpression, eol_MapExpression, eol_KeyValue, eol_AnyType, Type, eol_CollectionType, eol_PrimitiveType, eol_BooleanType, PrimitiveType, eol_IntegerType, eol_RealType, eol_StringType, eol_SetType, UniqueCollectionType, eol_BagType, eol_PrimitiveExpression, LiteralExpression, eol_CollectionExpression, eol_CollectionInitValue, eol_Annotation, eol_ExecutableAnnotation, Annotation, eol_SimpleAnnotation, eol_SpecialNameExpression, NameExpression, eol_ModelElementType, eol_EClassifier, CollectionType, eol_SequenceType, OrderedCollectionType, eol_OrderedSetType, eol_MapType, eol_ThrowStatement, eol_AbortStatement, eol_TransactionStatement, VariableDeclarationExpression, eol_ExprList, CollectionInitValue, eol_NativeType, eol_SpecialAssignmentStatement, AssignmentStatement, eol_ModelType, eol_NativeExpression, eol_EType, eol_VoidType, eol_PseudoType, eol_SelfType, PseudoType, eol_SelfContentType, eol_OrderedCollectionType, eol_ExpRange, eol_NewExpression, eol_UniqueCollectionType, eol_SelfInnermostType, eol_OperationArgType},
    associations={container1, region2, start4, end6, imports9, importedModules11, imported21, importedProgram23, resolvedType26, statements27, lhs29, rhs31, operations13, block15, name17, modelDeclarations19, target41, isArrow43, arguments45, method47, resolvedMethods50, isType52, enumeration34, literal36, model39, property57, extended59, name62, create64, parameters67, contextType70, expr55, self86, _result89, lhs92, rhs94, deleted97, iterator99, iterated101, returnType73, annotationBlock76, body78, name81, parameters84, returned115, expression117, cases119, default121, body123, condition125, body127, packages130, name132, body104, condition107, ifBody109, elseBody112, driver138, parameters141, EReference0144, iterators146, conditions148, method151, expression154, expression156, alias135, contents163, keyValues165, dynamicType166, contentType168, parameterList159, contentType160, name175, expression177, values179, key181, value184, ecoreType187, resolvedModelDeclaration188, valueType170, keyType172, executableAnnotations196, name199, value202, thrown205, body207, names209, expressions212, nativeExpression191, simpleAnnotations193, parameters219, modelName221, model223, nativeExpr226, isType228, ecoreType231, start214, end216},
    generalizations={gen_eol_Program_EolElement, gen_eol_Import_EolElement, gen_eol_Statement_EolElement, gen_eol_Expression_EolElement, gen_eol_Block_EolElement, gen_eol_OperatorExpression_Expression, gen_eol_BinaryOperatorExpression_OperatorExpression, gen_eol_AndOperatorExpression_BinaryOperatorExpression, gen_eol_LiteralExpression_Expression, gen_eol_BooleanExpression_PrimitiveExpression, gen_eol_DivideOperatorExpression_BinaryOperatorExpression, gen_eol_FeatureCallExpression_Expression, gen_eol_GreaterThanOperatorExpression_BinaryOperatorExpression, gen_eol_GreaterThanOrEqualToOperatorExpression_BinaryOperatorExpression, gen_eol_ImpliesOperatorExpression_BinaryOperatorExpression, gen_eol_IntegerExpression_PrimitiveExpression, gen_eol_LessThanOperatorExpression_BinaryOperatorExpression, gen_eol_LessThanOrEqualToOperatorExpression_BinaryOperatorExpression, gen_eol_MethodCallExpression_FeatureCallExpression, gen_eol_MinusOperatorExpression_BinaryOperatorExpression, gen_eol_MultiplyOperatorExpression_BinaryOperatorExpression, gen_eol_NameExpression_Expression, gen_eol_EnumerationLiteralExpression_Expression, gen_eol_EqualsOperatorExpression_BinaryOperatorExpression, gen_eol_OrOperatorExpression_BinaryOperatorExpression, gen_eol_PlusOperatorExpression_BinaryOperatorExpression, gen_eol_PropertyCallExpression_FeatureCallExpression, gen_eol_RealExpression_PrimitiveExpression, gen_eol_StringExpression_PrimitiveExpression, gen_eol_VariableDeclarationExpression_Expression, gen_eol_XorOperatorExpression_BinaryOperatorExpression, gen_eol_OperationDefinition_EolElement, gen_eol_UnaryOperatorExpression_OperatorExpression, gen_eol_NegativeOperatorExpression_UnaryOperatorExpression, gen_eol_NotEqualsOperatorExpression_BinaryOperatorExpression, gen_eol_NotOperatorExpression_UnaryOperatorExpression, gen_eol_AssignmentStatement_Statement, gen_eol_BreakStatement_Statement, gen_eol_BreakAllStatement_Statement, gen_eol_ContinueStatement_Statement, gen_eol_DeleteStatement_Statement, gen_eol_ForStatement_Statement, gen_eol_ReturnStatement_Statement, gen_eol_SwitchStatement_Statement, gen_eol_SwitchCaseStatement_Statement, gen_eol_WhileStatement_Statement, gen_eol_ModelDeclarationStatement_Statement, gen_eol_IfStatement_Statement, gen_eol_FOLMethodCallExpression_FeatureCallExpression, gen_eol_ExpressionStatement_Statement, gen_eol_SwitchCaseDefaultStatement_SwitchCaseStatement, gen_eol_SwitchCaseExpressionStatement_SwitchCaseStatement, gen_eol_SetExpression_CollectionExpression, gen_eol_BagExpression_CollectionExpression, gen_eol_SequenceExpression_CollectionExpression, gen_eol_OrderedSetExpression_CollectionExpression, gen_eol_MapExpression_LiteralExpression, gen_eol_Type_EolElement, gen_eol_AnyType_Type, gen_eol_CollectionType_Type, gen_eol_PrimitiveType_Type, gen_eol_BooleanType_PrimitiveType, gen_eol_IntegerType_PrimitiveType, gen_eol_RealType_PrimitiveType, gen_eol_StringType_PrimitiveType, gen_eol_SetType_UniqueCollectionType, gen_eol_PrimitiveExpression_LiteralExpression, gen_eol_CollectionExpression_LiteralExpression, gen_eol_Annotation_EolElement, gen_eol_ExecutableAnnotation_Annotation, gen_eol_SimpleAnnotation_Annotation, gen_eol_KeyValue_EolElement, gen_eol_SpecialNameExpression_NameExpression, gen_eol_ModelElementType_Type, gen_eol_BagType_CollectionType, gen_eol_SequenceType_OrderedCollectionType, gen_eol_OrderedSetType_OrderedCollectionType, gen_eol_OrderedSetType_UniqueCollectionType, gen_eol_MapType_Type, gen_eol_ModelDeclarationParameter_EolElement, gen_eol_ThrowStatement_Statement, gen_eol_AbortStatement_Statement, gen_eol_TransactionStatement_Statement, gen_eol_FormalParameterExpression_VariableDeclarationExpression, gen_eol_CollectionInitValue_EolElement, gen_eol_ExprList_CollectionInitValue, gen_eol_NativeType_Type, gen_eol_ModelExpression_NameExpression, gen_eol_AnnotationBlock_EolElement, gen_eol_SpecialAssignmentStatement_AssignmentStatement, gen_eol_ModelType_Type, gen_eol_NativeExpression_LiteralExpression, gen_eol_EType_Type, gen_eol_VoidType_Type, gen_eol_PseudoType_Type, gen_eol_SelfType_PseudoType, gen_eol_SelfContentType_PseudoType, gen_eol_OrderedCollectionType_CollectionType, gen_eol_ExpRange_CollectionInitValue, gen_eol_NewExpression_Expression, gen_eol_UniqueCollectionType_CollectionType, gen_eol_SelfInnermostType_PseudoType, gen_eol_OperationArgType_PseudoType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)