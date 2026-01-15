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
eol_EOLElement = Class(name="eol::EOLElement")
eol_Statement = Class(name="eol::Statement", is_abstract=True)
eol_TextRegion = Class(name="eol::TextRegion")
eol_TextPosition = Class(name="eol::TextPosition")
eol_EOLLibraryModule = Class(name="eol::EOLLibraryModule")
EOLElement = Class(name="EOLElement")
eol_Import = Class(name="eol::Import")
eol_ModelDeclarationStatement = Class(name="eol::ModelDeclarationStatement")
eol_OperationDefinition = Class(name="eol::OperationDefinition")
eol_EOLModule = Class(name="eol::EOLModule")
EOLLibraryModule = Class(name="EOLLibraryModule")
eol_Block = Class(name="eol::Block")
eol_AnnotationBlock = Class(name="eol::AnnotationBlock")
Block = Class(name="Block")
eol_ExpressionOrStatementBlock = Class(name="eol::ExpressionOrStatementBlock")
eol_Expression = Class(name="eol::Expression", is_abstract=True)
eol_Type = Class(name="eol::Type")
eol_NameExpression = Class(name="eol::NameExpression")
eol_FormalParameterExpression = Class(name="eol::FormalParameterExpression")
eol_VariableDeclarationExpression = Class(name="eol::VariableDeclarationExpression")
eol_MultiplyOperatorExpression = Class(name="eol::MultiplyOperatorExpression")
eol_MinusOperatorExpression = Class(name="eol::MinusOperatorExpression")
eol_PlusOperatorExpression = Class(name="eol::PlusOperatorExpression")
eol_ComparisonOperatorExpression = Class(name="eol::ComparisonOperatorExpression", is_abstract=True)
eol_GreaterThanOrEqualToOperatorExpression = Class(name="eol::GreaterThanOrEqualToOperatorExpression")
ComparisonOperatorExpression = Class(name="ComparisonOperatorExpression")
eol_OperatorExpression = Class(name="eol::OperatorExpression", is_abstract=True)
Expression = Class(name="Expression")
eol_UnaryOperatorExpression = Class(name="eol::UnaryOperatorExpression", is_abstract=True)
OperatorExpression = Class(name="OperatorExpression")
eol_NotOperatorExpression = Class(name="eol::NotOperatorExpression")
UnaryOperatorExpression = Class(name="UnaryOperatorExpression")
eol_NegativeOperatorExpression = Class(name="eol::NegativeOperatorExpression")
eol_BinaryOperatorExpression = Class(name="eol::BinaryOperatorExpression", is_abstract=True)
eol_LogicalOperatorExpression = Class(name="eol::LogicalOperatorExpression", is_abstract=True)
BinaryOperatorExpression = Class(name="BinaryOperatorExpression")
eol_AndOperatorExpression = Class(name="eol::AndOperatorExpression")
LogicalOperatorExpression = Class(name="LogicalOperatorExpression")
eol_XorOperatorExpression = Class(name="eol::XorOperatorExpression")
eol_OrOperatorExpression = Class(name="eol::OrOperatorExpression")
eol_ImpliesOperatorExpression = Class(name="eol::ImpliesOperatorExpression")
eol_ArithmeticOperatorExpression = Class(name="eol::ArithmeticOperatorExpression", is_abstract=True)
eol_DivideOperatorExpression = Class(name="eol::DivideOperatorExpression")
ArithmeticOperatorExpression = Class(name="ArithmeticOperatorExpression")
eol_PropertyCallExpression = Class(name="eol::PropertyCallExpression")
eol_GreaterThanOperatorExpression = Class(name="eol::GreaterThanOperatorExpression")
eol_LessThanOrEqualToOperatorExpression = Class(name="eol::LessThanOrEqualToOperatorExpression")
eol_LessThanOperatorExpression = Class(name="eol::LessThanOperatorExpression")
eol_NotEqualsOperatorExpression = Class(name="eol::NotEqualsOperatorExpression")
eol_EqualsOperatorExpression = Class(name="eol::EqualsOperatorExpression")
VariableDeclarationExpression = Class(name="VariableDeclarationExpression")
eol_FeatureCallExpression = Class(name="eol::FeatureCallExpression", is_abstract=True)
eol_MethodCallExpression = Class(name="eol::MethodCallExpression")
FeatureCallExpression = Class(name="FeatureCallExpression")
eol_CollectionExpression = Class(name="eol::CollectionExpression", is_abstract=True)
eol_FOLMethodCallExpression = Class(name="eol::FOLMethodCallExpression")
eol_KeyValueExpression = Class(name="eol::KeyValueExpression")
eol_ModelDeclarationParameter = Class(name="eol::ModelDeclarationParameter")
KeyValueExpression = Class(name="KeyValueExpression")
eol_NewExpression = Class(name="eol::NewExpression")
eol_MapExpression = Class(name="eol::MapExpression")
eol_CollectionInitialisationExpression = Class(name="eol::CollectionInitialisationExpression", is_abstract=True)
eol_PrimitiveExpression = Class(name="eol::PrimitiveExpression", is_abstract=True)
eol_ComparableExpression = Class(name="eol::ComparableExpression", is_abstract=True)
PrimitiveExpression = Class(name="PrimitiveExpression")
eol_SummableExpression = Class(name="eol::SummableExpression", is_abstract=True)
eol_StringExpression = Class(name="eol::StringExpression")
ComparableExpression = Class(name="ComparableExpression")
SummableExpression = Class(name="SummableExpression")
eol_BooleanExpression = Class(name="eol::BooleanExpression")
eol_RealExpression = Class(name="eol::RealExpression")
eol_IntegerExpression = Class(name="eol::IntegerExpression")
eol_BagExpression = Class(name="eol::BagExpression")
CollectionExpression = Class(name="CollectionExpression")
eol_SetExpression = Class(name="eol::SetExpression")
UniqueCollection = Class(name="UniqueCollection")
eol_OrderedSetExpression = Class(name="eol::OrderedSetExpression")
OrderedCollection = Class(name="OrderedCollection")
eol_SequenceExpression = Class(name="eol::SequenceExpression")
eol_OrderedCollection = Class(name="eol::OrderedCollection", is_abstract=True)
eol_UniqueCollection = Class(name="eol::UniqueCollection", is_abstract=True)
eol_EnumerationLiteralExpression = Class(name="eol::EnumerationLiteralExpression")
eol_SwitchCaseExpressionStatement = Class(name="eol::SwitchCaseExpressionStatement")
eol_SwitchCaseDefaultStatement = Class(name="eol::SwitchCaseDefaultStatement")
eol_ExpressionRange = Class(name="eol::ExpressionRange")
CollectionInitialisationExpression = Class(name="CollectionInitialisationExpression")
eol_ExpressionList = Class(name="eol::ExpressionList")
eol_TransactionStatement = Class(name="eol::TransactionStatement")
Statement = Class(name="Statement")
eol_ExpressionStatement = Class(name="eol::ExpressionStatement")
eol_SwitchStatement = Class(name="eol::SwitchStatement")
eol_SwitchCaseStatement = Class(name="eol::SwitchCaseStatement", is_abstract=True)
SwitchCaseStatement = Class(name="SwitchCaseStatement")
eol_IfStatement = Class(name="eol::IfStatement")
eol_ForStatement = Class(name="eol::ForStatement")
eol_DeleteStatement = Class(name="eol::DeleteStatement")
eol_WhileStatement = Class(name="eol::WhileStatement")
eol_ReturnStatement = Class(name="eol::ReturnStatement")
eol_ThrowStatement = Class(name="eol::ThrowStatement")
eol_SimpleAnnotationStatement = Class(name="eol::SimpleAnnotationStatement")
AnnotationStatement = Class(name="AnnotationStatement")
eol_AssignmentStatement = Class(name="eol::AssignmentStatement")
eol_SpecialAssignmentStatement = Class(name="eol::SpecialAssignmentStatement")
AssignmentStatement = Class(name="AssignmentStatement")
eol_ContinueStatement = Class(name="eol::ContinueStatement")
eol_AbortStatement = Class(name="eol::AbortStatement")
eol_BreakStatement = Class(name="eol::BreakStatement")
eol_BreakAllStatement = Class(name="eol::BreakAllStatement")
eol_AnnotationStatement = Class(name="eol::AnnotationStatement", is_abstract=True)
eol_ModelType = Class(name="eol::ModelType")
AnyType = Class(name="AnyType")
eol_ModelElementType = Class(name="eol::ModelElementType")
eol_ExecutableAnnotationStatement = Class(name="eol::ExecutableAnnotationStatement")
eol_AnyType = Class(name="eol::AnyType")
Type = Class(name="Type")
eol_BagType = Class(name="eol::BagType")
CollectionType = Class(name="CollectionType")
eol_OrderedCollectionType = Class(name="eol::OrderedCollectionType", is_abstract=True)
eol_UniqueCollectionType = Class(name="eol::UniqueCollectionType", is_abstract=True)
eol_SetType = Class(name="eol::SetType")
UniqueCollectionType = Class(name="UniqueCollectionType")
eol_OrderedSetType = Class(name="eol::OrderedSetType")
OrderedCollectionType = Class(name="OrderedCollectionType")
eol_SequenceType = Class(name="eol::SequenceType")
eol_PrimitiveType = Class(name="eol::PrimitiveType", is_abstract=True)
eol_ComparablePrimitiveType = Class(name="eol::ComparablePrimitiveType", is_abstract=True)
PrimitiveType = Class(name="PrimitiveType")
eol_SummablePrimitiveType = Class(name="eol::SummablePrimitiveType", is_abstract=True)
eol_PseudoType = Class(name="eol::PseudoType", is_abstract=True)
eol_SelfType = Class(name="eol::SelfType")
PseudoType = Class(name="PseudoType")
eol_SelfContentType = Class(name="eol::SelfContentType")
eol_MapType = Class(name="eol::MapType")
eol_NativeType = Class(name="eol::NativeType")
eol_VoidType = Class(name="eol::VoidType")
eol_InvalidType = Class(name="eol::InvalidType")
eol_CollectionType = Class(name="eol::CollectionType")
eol_BooleanType = Class(name="eol::BooleanType")
eol_RealType = Class(name="eol::RealType")
ComparablePrimitiveType = Class(name="ComparablePrimitiveType")
SummablePrimitiveType = Class(name="SummablePrimitiveType")
eol_IntegerType = Class(name="eol::IntegerType")
RealType = Class(name="RealType")
eol_StringType = Class(name="eol::StringType")

# eol_EOLElement class attributes and methods
eol_EOLElement_uri: Property = Property(name="uri", type=StringType)
eol_EOLElement.attributes={eol_EOLElement_uri}

# eol_Statement class attributes and methods

# eol_TextRegion class attributes and methods

# eol_TextPosition class attributes and methods
eol_TextPosition_line: Property = Property(name="line", type=IntegerType)
eol_TextPosition_column: Property = Property(name="column", type=IntegerType)
eol_TextPosition.attributes={eol_TextPosition_line, eol_TextPosition_column}

# eol_EOLLibraryModule class attributes and methods
eol_EOLLibraryModule_name: Property = Property(name="name", type=StringType)
eol_EOLLibraryModule.attributes={eol_EOLLibraryModule_name}

# EOLElement class attributes and methods

# eol_Import class attributes and methods
eol_Import_imported: Property = Property(name="imported", type=StringType)
eol_Import.attributes={eol_Import_imported}

# eol_ModelDeclarationStatement class attributes and methods
eol_ModelDeclarationStatement_resolvedIMetamodel: Property = Property(name="resolvedIMetamodel", type=StringType)
eol_ModelDeclarationStatement.attributes={eol_ModelDeclarationStatement_resolvedIMetamodel}

# eol_OperationDefinition class attributes and methods

# eol_EOLModule class attributes and methods

# EOLLibraryModule class attributes and methods

# eol_Block class attributes and methods

# eol_AnnotationBlock class attributes and methods

# Block class attributes and methods

# eol_ExpressionOrStatementBlock class attributes and methods

# eol_Expression class attributes and methods
eol_Expression_inBrackets: Property = Property(name="inBrackets", type=BooleanType)
eol_Expression.attributes={eol_Expression_inBrackets}

# eol_Type class attributes and methods

# eol_NameExpression class attributes and methods
eol_NameExpression_name: Property = Property(name="name", type=StringType)
eol_NameExpression_resolvedContent: Property = Property(name="resolvedContent", type=StringType)
eol_NameExpression_isType: Property = Property(name="isType", type=BooleanType)
eol_NameExpression.attributes={eol_NameExpression_name, eol_NameExpression_isType, eol_NameExpression_resolvedContent}

# eol_FormalParameterExpression class attributes and methods

# eol_VariableDeclarationExpression class attributes and methods
eol_VariableDeclarationExpression_create: Property = Property(name="create", type=BooleanType)
eol_VariableDeclarationExpression.attributes={eol_VariableDeclarationExpression_create}

# eol_MultiplyOperatorExpression class attributes and methods

# eol_MinusOperatorExpression class attributes and methods

# eol_PlusOperatorExpression class attributes and methods

# eol_ComparisonOperatorExpression class attributes and methods

# eol_GreaterThanOrEqualToOperatorExpression class attributes and methods

# ComparisonOperatorExpression class attributes and methods

# eol_OperatorExpression class attributes and methods

# Expression class attributes and methods

# eol_UnaryOperatorExpression class attributes and methods

# OperatorExpression class attributes and methods

# eol_NotOperatorExpression class attributes and methods

# UnaryOperatorExpression class attributes and methods

# eol_NegativeOperatorExpression class attributes and methods

# eol_BinaryOperatorExpression class attributes and methods

# eol_LogicalOperatorExpression class attributes and methods

# BinaryOperatorExpression class attributes and methods

# eol_AndOperatorExpression class attributes and methods

# LogicalOperatorExpression class attributes and methods

# eol_XorOperatorExpression class attributes and methods

# eol_OrOperatorExpression class attributes and methods

# eol_ImpliesOperatorExpression class attributes and methods

# eol_ArithmeticOperatorExpression class attributes and methods

# eol_DivideOperatorExpression class attributes and methods

# ArithmeticOperatorExpression class attributes and methods

# eol_PropertyCallExpression class attributes and methods
eol_PropertyCallExpression_extended: Property = Property(name="extended", type=BooleanType)
eol_PropertyCallExpression.attributes={eol_PropertyCallExpression_extended}

# eol_GreaterThanOperatorExpression class attributes and methods

# eol_LessThanOrEqualToOperatorExpression class attributes and methods

# eol_LessThanOperatorExpression class attributes and methods

# eol_NotEqualsOperatorExpression class attributes and methods

# eol_EqualsOperatorExpression class attributes and methods

# VariableDeclarationExpression class attributes and methods

# eol_FeatureCallExpression class attributes and methods
eol_FeatureCallExpression_arrow: Property = Property(name="arrow", type=BooleanType)
eol_FeatureCallExpression.attributes={eol_FeatureCallExpression_arrow}

# eol_MethodCallExpression class attributes and methods

# FeatureCallExpression class attributes and methods

# eol_CollectionExpression class attributes and methods

# eol_FOLMethodCallExpression class attributes and methods

# eol_KeyValueExpression class attributes and methods

# eol_ModelDeclarationParameter class attributes and methods

# KeyValueExpression class attributes and methods

# eol_NewExpression class attributes and methods

# eol_MapExpression class attributes and methods

# eol_CollectionInitialisationExpression class attributes and methods

# eol_PrimitiveExpression class attributes and methods

# eol_ComparableExpression class attributes and methods

# PrimitiveExpression class attributes and methods

# eol_SummableExpression class attributes and methods

# eol_StringExpression class attributes and methods
eol_StringExpression_value: Property = Property(name="value", type=StringType)
eol_StringExpression.attributes={eol_StringExpression_value}

# ComparableExpression class attributes and methods

# SummableExpression class attributes and methods

# eol_BooleanExpression class attributes and methods
eol_BooleanExpression_value: Property = Property(name="value", type=BooleanType)
eol_BooleanExpression.attributes={eol_BooleanExpression_value}

# eol_RealExpression class attributes and methods
eol_RealExpression_value: Property = Property(name="value", type=FloatType)
eol_RealExpression.attributes={eol_RealExpression_value}

# eol_IntegerExpression class attributes and methods
eol_IntegerExpression_value: Property = Property(name="value", type=IntegerType)
eol_IntegerExpression.attributes={eol_IntegerExpression_value}

# eol_BagExpression class attributes and methods

# CollectionExpression class attributes and methods

# eol_SetExpression class attributes and methods

# UniqueCollection class attributes and methods

# eol_OrderedSetExpression class attributes and methods

# OrderedCollection class attributes and methods

# eol_SequenceExpression class attributes and methods

# eol_OrderedCollection class attributes and methods

# eol_UniqueCollection class attributes and methods

# eol_EnumerationLiteralExpression class attributes and methods

# eol_SwitchCaseExpressionStatement class attributes and methods

# eol_SwitchCaseDefaultStatement class attributes and methods

# eol_ExpressionRange class attributes and methods

# CollectionInitialisationExpression class attributes and methods

# eol_ExpressionList class attributes and methods

# eol_TransactionStatement class attributes and methods

# Statement class attributes and methods

# eol_ExpressionStatement class attributes and methods

# eol_SwitchStatement class attributes and methods

# eol_SwitchCaseStatement class attributes and methods

# SwitchCaseStatement class attributes and methods

# eol_IfStatement class attributes and methods

# eol_ForStatement class attributes and methods

# eol_DeleteStatement class attributes and methods

# eol_WhileStatement class attributes and methods

# eol_ReturnStatement class attributes and methods

# eol_ThrowStatement class attributes and methods

# eol_SimpleAnnotationStatement class attributes and methods

# AnnotationStatement class attributes and methods

# eol_AssignmentStatement class attributes and methods

# eol_SpecialAssignmentStatement class attributes and methods

# AssignmentStatement class attributes and methods

# eol_ContinueStatement class attributes and methods

# eol_AbortStatement class attributes and methods

# eol_BreakStatement class attributes and methods

# eol_BreakAllStatement class attributes and methods

# eol_AnnotationStatement class attributes and methods

# eol_ModelType class attributes and methods
eol_ModelType_resolvedIMetamodel: Property = Property(name="resolvedIMetamodel", type=StringType)
eol_ModelType_modelName: Property = Property(name="modelName", type=StringType)
eol_ModelType.attributes={eol_ModelType_modelName, eol_ModelType_resolvedIMetamodel}

# AnyType class attributes and methods

# eol_ModelElementType class attributes and methods
eol_ModelElementType_modelName: Property = Property(name="modelName", type=StringType)
eol_ModelElementType_elementName: Property = Property(name="elementName", type=StringType)
eol_ModelElementType_resolvedIMetamodel: Property = Property(name="resolvedIMetamodel", type=StringType)
eol_ModelElementType_resolvedIPackage: Property = Property(name="resolvedIPackage", type=StringType)
eol_ModelElementType_modelElementType: Property = Property(name="modelElementType", type=StringType)
eol_ModelElementType.attributes={eol_ModelElementType_modelElementType, eol_ModelElementType_resolvedIPackage, eol_ModelElementType_resolvedIMetamodel, eol_ModelElementType_elementName, eol_ModelElementType_modelName}

# eol_ExecutableAnnotationStatement class attributes and methods

# eol_AnyType class attributes and methods
eol_AnyType_declared: Property = Property(name="declared", type=BooleanType)
eol_AnyType.attributes={eol_AnyType_declared}

# Type class attributes and methods

# eol_BagType class attributes and methods

# CollectionType class attributes and methods

# eol_OrderedCollectionType class attributes and methods

# eol_UniqueCollectionType class attributes and methods

# eol_SetType class attributes and methods

# UniqueCollectionType class attributes and methods

# eol_OrderedSetType class attributes and methods

# OrderedCollectionType class attributes and methods

# eol_SequenceType class attributes and methods

# eol_PrimitiveType class attributes and methods

# eol_ComparablePrimitiveType class attributes and methods

# PrimitiveType class attributes and methods

# eol_SummablePrimitiveType class attributes and methods

# eol_PseudoType class attributes and methods

# eol_SelfType class attributes and methods

# PseudoType class attributes and methods

# eol_SelfContentType class attributes and methods

# eol_MapType class attributes and methods

# eol_NativeType class attributes and methods

# eol_VoidType class attributes and methods

# eol_InvalidType class attributes and methods

# eol_CollectionType class attributes and methods

# eol_BooleanType class attributes and methods

# eol_RealType class attributes and methods

# ComparablePrimitiveType class attributes and methods

# SummablePrimitiveType class attributes and methods

# eol_IntegerType class attributes and methods

# RealType class attributes and methods

# eol_StringType class attributes and methods

# Relationships
importedModule15: BinaryAssociation = BinaryAssociation(
    name="importedModule15",
    ends={
        Property(name="eol_EOLLibraryModule17", type=eol_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Import16", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container1: BinaryAssociation = BinaryAssociation(
    name="container1",
    ends={
        Property(name="eol_EOLElement", type=eol_EOLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLElement0", type=eol_EOLElement, multiplicity=Multiplicity(0, 1))
    }
)
region2: BinaryAssociation = BinaryAssociation(
    name="region2",
    ends={
        Property(name="eol_TextRegion", type=eol_EOLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLElement3", type=eol_TextRegion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start4: BinaryAssociation = BinaryAssociation(
    name="start4",
    ends={
        Property(name="eol_TextPosition", type=eol_TextRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TextRegion5", type=eol_TextPosition, multiplicity=Multiplicity(1, 1), is_composite=True)
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
        Property(name="eol_Import", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLLibraryModule", type=eol_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelDeclarations10: BinaryAssociation = BinaryAssociation(
    name="modelDeclarations10",
    ends={
        Property(name="eol_ModelDeclarationStatement", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLLibraryModule11", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations12: BinaryAssociation = BinaryAssociation(
    name="operations12",
    ends={
        Property(name="eol_OperationDefinition", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLLibraryModule13", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block14: BinaryAssociation = BinaryAssociation(
    name="block14",
    ends={
        Property(name="eol_Block", type=eol_EOLModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLModule", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
self41: BinaryAssociation = BinaryAssociation(
    name="self41",
    ends={
        Property(name="eol_OperationDefinition42", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="eol_VariableDeclarationExpression", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1))
    }
)
_result43: BinaryAssociation = BinaryAssociation(
    name="_result43",
    ends={
        Property(name="eol_VariableDeclarationExpression45", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition44", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependingOperationDefinitions47: BinaryAssociation = BinaryAssociation(
    name="dependingOperationDefinitions47",
    ends={
        Property(name="eol_OperationDefinition48", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition46", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
statements18: BinaryAssociation = BinaryAssociation(
    name="statements18",
    ends={
        Property(name="eol_Statement", type=eol_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Block19", type=eol_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block20: BinaryAssociation = BinaryAssociation(
    name="block20",
    ends={
        Property(name="eol_Block21", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionOrStatementBlock", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression22: BinaryAssociation = BinaryAssociation(
    name="expression22",
    ends={
        Property(name="eol_Expression", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionOrStatementBlock23", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition24: BinaryAssociation = BinaryAssociation(
    name="condition24",
    ends={
        Property(name="eol_Expression26", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionOrStatementBlock25", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contextType27: BinaryAssociation = BinaryAssociation(
    name="contextType27",
    ends={
        Property(name="eol_Type", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition28", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType29: BinaryAssociation = BinaryAssociation(
    name="returnType29",
    ends={
        Property(name="eol_Type31", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition30", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotationBlock32: BinaryAssociation = BinaryAssociation(
    name="annotationBlock32",
    ends={
        Property(name="eol_AnnotationBlock", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition33", type=eol_AnnotationBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body34: BinaryAssociation = BinaryAssociation(
    name="body34",
    ends={
        Property(name="eol_Block36", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition35", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name37: BinaryAssociation = BinaryAssociation(
    name="name37",
    ends={
        Property(name="eol_NameExpression", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition38", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters39: BinaryAssociation = BinaryAssociation(
    name="parameters39",
    ends={
        Property(name="eol_FormalParameterExpression", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition40", type=eol_FormalParameterExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolvedType49: BinaryAssociation = BinaryAssociation(
    name="resolvedType49",
    ends={
        Property(name="eol_Type51", type=eol_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Expression50", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression52: BinaryAssociation = BinaryAssociation(
    name="expression52",
    ends={
        Property(name="eol_Expression53", type=eol_UnaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_UnaryOperatorExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs54: BinaryAssociation = BinaryAssociation(
    name="lhs54",
    ends={
        Property(name="eol_Expression55", type=eol_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_BinaryOperatorExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs56: BinaryAssociation = BinaryAssociation(
    name="rhs56",
    ends={
        Property(name="eol_Expression58", type=eol_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_BinaryOperatorExpression57", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
method69: BinaryAssociation = BinaryAssociation(
    name="method69",
    ends={
        Property(name="eol_NameExpression71", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression70", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedOperationDefinition72: BinaryAssociation = BinaryAssociation(
    name="resolvedOperationDefinition72",
    ends={
        Property(name="eol_OperationDefinition74", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression73", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 1))
    }
)
name59: BinaryAssociation = BinaryAssociation(
    name="name59",
    ends={
        Property(name="eol_NameExpression61", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression60", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
references62: BinaryAssociation = BinaryAssociation(
    name="references62",
    ends={
        Property(name="eol_NameExpression64", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression63", type=eol_NameExpression, multiplicity=Multiplicity(0, 9999))
    }
)
target65: BinaryAssociation = BinaryAssociation(
    name="target65",
    ends={
        Property(name="eol_Expression66", type=eol_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FeatureCallExpression", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments67: BinaryAssociation = BinaryAssociation(
    name="arguments67",
    ends={
        Property(name="eol_Expression68", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyValues98: BinaryAssociation = BinaryAssociation(
    name="keyValues98",
    ends={
        Property(name="eol_MapExpression", type=eol_KeyValueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="eol_KeyValueExpression99", type=eol_MapExpression, multiplicity=Multiplicity(1, 1))
    }
)
contents100: BinaryAssociation = BinaryAssociation(
    name="contents100",
    ends={
        Property(name="eol_Expression101", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property75: BinaryAssociation = BinaryAssociation(
    name="property75",
    ends={
        Property(name="eol_NameExpression76", type=eol_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_PropertyCallExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator77: BinaryAssociation = BinaryAssociation(
    name="iterator77",
    ends={
        Property(name="eol_FormalParameterExpression78", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression", type=eol_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditions79: BinaryAssociation = BinaryAssociation(
    name="conditions79",
    ends={
        Property(name="eol_Expression81", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression80", type=eol_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
method82: BinaryAssociation = BinaryAssociation(
    name="method82",
    ends={
        Property(name="eol_NameExpression84", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression83", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedFOLDefinition85: BinaryAssociation = BinaryAssociation(
    name="resolvedFOLDefinition85",
    ends={
        Property(name="eol_OperationDefinition87", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression86", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 1))
    }
)
key88: BinaryAssociation = BinaryAssociation(
    name="key88",
    ends={
        Property(name="eol_Expression89", type=eol_KeyValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_KeyValueExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value90: BinaryAssociation = BinaryAssociation(
    name="value90",
    ends={
        Property(name="eol_Expression92", type=eol_KeyValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_KeyValueExpression91", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeName93: BinaryAssociation = BinaryAssociation(
    name="typeName93",
    ends={
        Property(name="eol_NameExpression94", type=eol_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NewExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters95: BinaryAssociation = BinaryAssociation(
    name="parameters95",
    ends={
        Property(name="eol_Expression97", type=eol_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NewExpression96", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration106: BinaryAssociation = BinaryAssociation(
    name="enumeration106",
    ends={
        Property(name="eol_NameExpression108", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression107", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterList102: BinaryAssociation = BinaryAssociation(
    name="parameterList102",
    ends={
        Property(name="eol_CollectionInitialisationExpression", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression103", type=eol_CollectionInitialisationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal104: BinaryAssociation = BinaryAssociation(
    name="literal104",
    ends={
        Property(name="eol_NameExpression105", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="eol_Expression127", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases128: BinaryAssociation = BinaryAssociation(
    name="cases128",
    ends={
        Property(name="eol_SwitchCaseExpressionStatement", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement129", type=eol_SwitchCaseExpressionStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model109: BinaryAssociation = BinaryAssociation(
    name="model109",
    ends={
        Property(name="eol_NameExpression111", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression110", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
start112: BinaryAssociation = BinaryAssociation(
    name="start112",
    ends={
        Property(name="eol_Expression113", type=eol_ExpressionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionRange", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end114: BinaryAssociation = BinaryAssociation(
    name="end114",
    ends={
        Property(name="eol_Expression116", type=eol_ExpressionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionRange115", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions117: BinaryAssociation = BinaryAssociation(
    name="expressions117",
    ends={
        Property(name="eol_Expression118", type=eol_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionList", type=eol_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
names119: BinaryAssociation = BinaryAssociation(
    name="names119",
    ends={
        Property(name="eol_NameExpression120", type=eol_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TransactionStatement", type=eol_NameExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body121: BinaryAssociation = BinaryAssociation(
    name="body121",
    ends={
        Property(name="eol_ExpressionOrStatementBlock123", type=eol_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TransactionStatement122", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression124: BinaryAssociation = BinaryAssociation(
    name="expression124",
    ends={
        Property(name="eol_Expression125", type=eol_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition150: BinaryAssociation = BinaryAssociation(
    name="condition150",
    ends={
        Property(name="eol_Expression152", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement151", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body153: BinaryAssociation = BinaryAssociation(
    name="body153",
    ends={
        Property(name="eol_ExpressionOrStatementBlock155", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement154", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
default130: BinaryAssociation = BinaryAssociation(
    name="default130",
    ends={
        Property(name="eol_SwitchCaseDefaultStatement", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement131", type=eol_SwitchCaseDefaultStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body132: BinaryAssociation = BinaryAssociation(
    name="body132",
    ends={
        Property(name="eol_ExpressionOrStatementBlock133", type=eol_SwitchCaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchCaseStatement", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression134: BinaryAssociation = BinaryAssociation(
    name="expression134",
    ends={
        Property(name="eol_Expression136", type=eol_SwitchCaseExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchCaseExpressionStatement135", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition137: BinaryAssociation = BinaryAssociation(
    name="condition137",
    ends={
        Property(name="eol_Expression138", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifBody139: BinaryAssociation = BinaryAssociation(
    name="ifBody139",
    ends={
        Property(name="eol_ExpressionOrStatementBlock141", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement140", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseIfBodies142: BinaryAssociation = BinaryAssociation(
    name="elseIfBodies142",
    ends={
        Property(name="eol_ExpressionOrStatementBlock144", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement143", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseBody145: BinaryAssociation = BinaryAssociation(
    name="elseBody145",
    ends={
        Property(name="eol_ExpressionOrStatementBlock147", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement146", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterator148: BinaryAssociation = BinaryAssociation(
    name="iterator148",
    ends={
        Property(name="eol_FormalParameterExpression149", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement", type=eol_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression163: BinaryAssociation = BinaryAssociation(
    name="expression163",
    ends={
        Property(name="eol_Expression164", type=eol_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ThrowStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition156: BinaryAssociation = BinaryAssociation(
    name="condition156",
    ends={
        Property(name="eol_Expression157", type=eol_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_WhileStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body158: BinaryAssociation = BinaryAssociation(
    name="body158",
    ends={
        Property(name="eol_ExpressionOrStatementBlock160", type=eol_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_WhileStatement159", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression161: BinaryAssociation = BinaryAssociation(
    name="expression161",
    ends={
        Property(name="eol_Expression162", type=eol_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ReturnStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name172: BinaryAssociation = BinaryAssociation(
    name="name172",
    ends={
        Property(name="eol_NameExpression173", type=eol_AnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnnotationStatement", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression165: BinaryAssociation = BinaryAssociation(
    name="expression165",
    ends={
        Property(name="eol_Expression166", type=eol_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_DeleteStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs167: BinaryAssociation = BinaryAssociation(
    name="lhs167",
    ends={
        Property(name="eol_Expression168", type=eol_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AssignmentStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs169: BinaryAssociation = BinaryAssociation(
    name="rhs169",
    ends={
        Property(name="eol_Expression171", type=eol_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AssignmentStatement170", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values174: BinaryAssociation = BinaryAssociation(
    name="values174",
    ends={
        Property(name="eol_StringExpression", type=eol_SimpleAnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SimpleAnnotationStatement", type=eol_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression175: BinaryAssociation = BinaryAssociation(
    name="expression175",
    ends={
        Property(name="eol_Expression176", type=eol_ExecutableAnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExecutableAnnotationStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name177: BinaryAssociation = BinaryAssociation(
    name="name177",
    ends={
        Property(name="eol_VariableDeclarationExpression179", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement178", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
driver180: BinaryAssociation = BinaryAssociation(
    name="driver180",
    ends={
        Property(name="eol_NameExpression182", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement181", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
aliases183: BinaryAssociation = BinaryAssociation(
    name="aliases183",
    ends={
        Property(name="eol_VariableDeclarationExpression185", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement184", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters186: BinaryAssociation = BinaryAssociation(
    name="parameters186",
    ends={
        Property(name="eol_ModelDeclarationParameter", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement187", type=eol_ModelDeclarationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dynamicTypes188: BinaryAssociation = BinaryAssociation(
    name="dynamicTypes188",
    ends={
        Property(name="eol_Type189", type=eol_AnyType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnyType", type=eol_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentType199: BinaryAssociation = BinaryAssociation(
    name="contentType199",
    ends={
        Property(name="eol_Type200", type=eol_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionType", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedModelDeclaration190: BinaryAssociation = BinaryAssociation(
    name="resolvedModelDeclaration190",
    ends={
        Property(name="eol_ModelDeclarationStatement191", type=eol_ModelElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelElementType", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1))
    }
)
keyType192: BinaryAssociation = BinaryAssociation(
    name="keyType192",
    ends={
        Property(name="eol_AnyType193", type=eol_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapType", type=eol_AnyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueType194: BinaryAssociation = BinaryAssociation(
    name="valueType194",
    ends={
        Property(name="eol_AnyType196", type=eol_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapType195", type=eol_AnyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression197: BinaryAssociation = BinaryAssociation(
    name="expression197",
    ends={
        Property(name="eol_StringExpression198", type=eol_NativeType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NativeType", type=eol_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_eol_Block_EOLElement = Generalization(general=EOLElement, specific=eol_Block)
gen_eol_EOLLibraryModule_EOLElement = Generalization(general=EOLElement, specific=eol_EOLLibraryModule)
gen_eol_EOLModule_EOLLibraryModule = Generalization(general=EOLLibraryModule, specific=eol_EOLModule)
gen_eol_Import_EOLElement = Generalization(general=EOLElement, specific=eol_Import)
gen_eol_AnnotationBlock_Block = Generalization(general=Block, specific=eol_AnnotationBlock)
gen_eol_ExpressionOrStatementBlock_EOLElement = Generalization(general=EOLElement, specific=eol_ExpressionOrStatementBlock)
gen_eol_OperationDefinition_EOLElement = Generalization(general=EOLElement, specific=eol_OperationDefinition)
gen_eol_MultiplyOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_MultiplyOperatorExpression)
gen_eol_MinusOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_MinusOperatorExpression)
gen_eol_PlusOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_PlusOperatorExpression)
gen_eol_ComparisonOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_ComparisonOperatorExpression)
gen_eol_Expression_EOLElement = Generalization(general=EOLElement, specific=eol_Expression)
gen_eol_OperatorExpression_Expression = Generalization(general=Expression, specific=eol_OperatorExpression)
gen_eol_UnaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=eol_UnaryOperatorExpression)
gen_eol_NotOperatorExpression_UnaryOperatorExpression = Generalization(general=UnaryOperatorExpression, specific=eol_NotOperatorExpression)
gen_eol_NegativeOperatorExpression_UnaryOperatorExpression = Generalization(general=UnaryOperatorExpression, specific=eol_NegativeOperatorExpression)
gen_eol_BinaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=eol_BinaryOperatorExpression)
gen_eol_LogicalOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_LogicalOperatorExpression)
gen_eol_AndOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_AndOperatorExpression)
gen_eol_XorOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_XorOperatorExpression)
gen_eol_OrOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_OrOperatorExpression)
gen_eol_ImpliesOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_ImpliesOperatorExpression)
gen_eol_ArithmeticOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_ArithmeticOperatorExpression)
gen_eol_DivideOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_DivideOperatorExpression)
gen_eol_PropertyCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_PropertyCallExpression)
gen_eol_GreaterThanOrEqualToOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_GreaterThanOrEqualToOperatorExpression)
gen_eol_GreaterThanOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_GreaterThanOperatorExpression)
gen_eol_LessThanOrEqualToOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_LessThanOrEqualToOperatorExpression)
gen_eol_LessThanOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_LessThanOperatorExpression)
gen_eol_NotEqualsOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_NotEqualsOperatorExpression)
gen_eol_EqualsOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_EqualsOperatorExpression)
gen_eol_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=eol_VariableDeclarationExpression)
gen_eol_FormalParameterExpression_VariableDeclarationExpression = Generalization(general=VariableDeclarationExpression, specific=eol_FormalParameterExpression)
gen_eol_NameExpression_Expression = Generalization(general=Expression, specific=eol_NameExpression)
gen_eol_FeatureCallExpression_Expression = Generalization(general=Expression, specific=eol_FeatureCallExpression)
gen_eol_MethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_MethodCallExpression)
gen_eol_CollectionExpression_Expression = Generalization(general=Expression, specific=eol_CollectionExpression)
gen_eol_FOLMethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_FOLMethodCallExpression)
gen_eol_KeyValueExpression_Expression = Generalization(general=Expression, specific=eol_KeyValueExpression)
gen_eol_ModelDeclarationParameter_KeyValueExpression = Generalization(general=KeyValueExpression, specific=eol_ModelDeclarationParameter)
gen_eol_NewExpression_Expression = Generalization(general=Expression, specific=eol_NewExpression)
gen_eol_MapExpression_Expression = Generalization(general=Expression, specific=eol_MapExpression)
gen_eol_PrimitiveExpression_Expression = Generalization(general=Expression, specific=eol_PrimitiveExpression)
gen_eol_ComparableExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_ComparableExpression)
gen_eol_SummableExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_SummableExpression)
gen_eol_StringExpression_ComparableExpression = Generalization(general=ComparableExpression, specific=eol_StringExpression)
gen_eol_StringExpression_SummableExpression = Generalization(general=SummableExpression, specific=eol_StringExpression)
gen_eol_BooleanExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_BooleanExpression)
gen_eol_RealExpression_ComparableExpression = Generalization(general=ComparableExpression, specific=eol_RealExpression)
gen_eol_RealExpression_SummableExpression = Generalization(general=SummableExpression, specific=eol_RealExpression)
gen_eol_IntegerExpression_ComparableExpression = Generalization(general=ComparableExpression, specific=eol_IntegerExpression)
gen_eol_IntegerExpression_SummableExpression = Generalization(general=SummableExpression, specific=eol_IntegerExpression)
gen_eol_BagExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_BagExpression)
gen_eol_SetExpression_UniqueCollection = Generalization(general=UniqueCollection, specific=eol_SetExpression)
gen_eol_OrderedSetExpression_OrderedCollection = Generalization(general=OrderedCollection, specific=eol_OrderedSetExpression)
gen_eol_OrderedSetExpression_UniqueCollection = Generalization(general=UniqueCollection, specific=eol_OrderedSetExpression)
gen_eol_SequenceExpression_OrderedCollection = Generalization(general=OrderedCollection, specific=eol_SequenceExpression)
gen_eol_OrderedCollection_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_OrderedCollection)
gen_eol_UniqueCollection_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_UniqueCollection)
gen_eol_EnumerationLiteralExpression_Expression = Generalization(general=Expression, specific=eol_EnumerationLiteralExpression)
gen_eol_CollectionInitialisationExpression_Expression = Generalization(general=Expression, specific=eol_CollectionInitialisationExpression)
gen_eol_ExpressionRange_CollectionInitialisationExpression = Generalization(general=CollectionInitialisationExpression, specific=eol_ExpressionRange)
gen_eol_ExpressionList_CollectionInitialisationExpression = Generalization(general=CollectionInitialisationExpression, specific=eol_ExpressionList)
gen_eol_Statement_EOLElement = Generalization(general=EOLElement, specific=eol_Statement)
gen_eol_TransactionStatement_Statement = Generalization(general=Statement, specific=eol_TransactionStatement)
gen_eol_ExpressionStatement_Statement = Generalization(general=Statement, specific=eol_ExpressionStatement)
gen_eol_SwitchStatement_Statement = Generalization(general=Statement, specific=eol_SwitchStatement)
gen_eol_SwitchCaseStatement_Statement = Generalization(general=Statement, specific=eol_SwitchCaseStatement)
gen_eol_SwitchCaseDefaultStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_SwitchCaseDefaultStatement)
gen_eol_SwitchCaseExpressionStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_SwitchCaseExpressionStatement)
gen_eol_IfStatement_Statement = Generalization(general=Statement, specific=eol_IfStatement)
gen_eol_ForStatement_Statement = Generalization(general=Statement, specific=eol_ForStatement)
gen_eol_DeleteStatement_Statement = Generalization(general=Statement, specific=eol_DeleteStatement)
gen_eol_WhileStatement_Statement = Generalization(general=Statement, specific=eol_WhileStatement)
gen_eol_ReturnStatement_Statement = Generalization(general=Statement, specific=eol_ReturnStatement)
gen_eol_ThrowStatement_Statement = Generalization(general=Statement, specific=eol_ThrowStatement)
gen_eol_SimpleAnnotationStatement_AnnotationStatement = Generalization(general=AnnotationStatement, specific=eol_SimpleAnnotationStatement)
gen_eol_AssignmentStatement_Statement = Generalization(general=Statement, specific=eol_AssignmentStatement)
gen_eol_SpecialAssignmentStatement_AssignmentStatement = Generalization(general=AssignmentStatement, specific=eol_SpecialAssignmentStatement)
gen_eol_ContinueStatement_Statement = Generalization(general=Statement, specific=eol_ContinueStatement)
gen_eol_AbortStatement_Statement = Generalization(general=Statement, specific=eol_AbortStatement)
gen_eol_BreakStatement_Statement = Generalization(general=Statement, specific=eol_BreakStatement)
gen_eol_BreakAllStatement_Statement = Generalization(general=Statement, specific=eol_BreakAllStatement)
gen_eol_AnnotationStatement_Statement = Generalization(general=Statement, specific=eol_AnnotationStatement)
gen_eol_ModelType_AnyType = Generalization(general=AnyType, specific=eol_ModelType)
gen_eol_ModelElementType_AnyType = Generalization(general=AnyType, specific=eol_ModelElementType)
gen_eol_ExecutableAnnotationStatement_AnnotationStatement = Generalization(general=AnnotationStatement, specific=eol_ExecutableAnnotationStatement)
gen_eol_ModelDeclarationStatement_Statement = Generalization(general=Statement, specific=eol_ModelDeclarationStatement)
gen_eol_Type_EOLElement = Generalization(general=EOLElement, specific=eol_Type)
gen_eol_AnyType_Type = Generalization(general=Type, specific=eol_AnyType)
gen_eol_BagType_CollectionType = Generalization(general=CollectionType, specific=eol_BagType)
gen_eol_OrderedCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_OrderedCollectionType)
gen_eol_UniqueCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_UniqueCollectionType)
gen_eol_SetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_SetType)
gen_eol_OrderedSetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_OrderedSetType)
gen_eol_OrderedSetType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_OrderedSetType)
gen_eol_SequenceType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_SequenceType)
gen_eol_PrimitiveType_AnyType = Generalization(general=AnyType, specific=eol_PrimitiveType)
gen_eol_ComparablePrimitiveType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_ComparablePrimitiveType)
gen_eol_SummablePrimitiveType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_SummablePrimitiveType)
gen_eol_PseudoType_AnyType = Generalization(general=AnyType, specific=eol_PseudoType)
gen_eol_SelfType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfType)
gen_eol_SelfContentType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfContentType)
gen_eol_MapType_AnyType = Generalization(general=AnyType, specific=eol_MapType)
gen_eol_NativeType_AnyType = Generalization(general=AnyType, specific=eol_NativeType)
gen_eol_VoidType_AnyType = Generalization(general=AnyType, specific=eol_VoidType)
gen_eol_InvalidType_AnyType = Generalization(general=AnyType, specific=eol_InvalidType)
gen_eol_CollectionType_AnyType = Generalization(general=AnyType, specific=eol_CollectionType)
gen_eol_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_BooleanType)
gen_eol_RealType_ComparablePrimitiveType = Generalization(general=ComparablePrimitiveType, specific=eol_RealType)
gen_eol_RealType_SummablePrimitiveType = Generalization(general=SummablePrimitiveType, specific=eol_RealType)
gen_eol_IntegerType_RealType = Generalization(general=RealType, specific=eol_IntegerType)
gen_eol_StringType_ComparablePrimitiveType = Generalization(general=ComparablePrimitiveType, specific=eol_StringType)
gen_eol_StringType_SummablePrimitiveType = Generalization(general=SummablePrimitiveType, specific=eol_StringType)

# Domain Model
domain_model = DomainModel(
    name="eol",
    types={eol_EOLElement, eol_Statement, eol_TextRegion, eol_TextPosition, eol_EOLLibraryModule, EOLElement, eol_Import, eol_ModelDeclarationStatement, eol_OperationDefinition, eol_EOLModule, EOLLibraryModule, eol_Block, eol_AnnotationBlock, Block, eol_ExpressionOrStatementBlock, eol_Expression, eol_Type, eol_NameExpression, eol_FormalParameterExpression, eol_VariableDeclarationExpression, eol_MultiplyOperatorExpression, eol_MinusOperatorExpression, eol_PlusOperatorExpression, eol_ComparisonOperatorExpression, eol_GreaterThanOrEqualToOperatorExpression, ComparisonOperatorExpression, eol_OperatorExpression, Expression, eol_UnaryOperatorExpression, OperatorExpression, eol_NotOperatorExpression, UnaryOperatorExpression, eol_NegativeOperatorExpression, eol_BinaryOperatorExpression, eol_LogicalOperatorExpression, BinaryOperatorExpression, eol_AndOperatorExpression, LogicalOperatorExpression, eol_XorOperatorExpression, eol_OrOperatorExpression, eol_ImpliesOperatorExpression, eol_ArithmeticOperatorExpression, eol_DivideOperatorExpression, ArithmeticOperatorExpression, eol_PropertyCallExpression, eol_GreaterThanOperatorExpression, eol_LessThanOrEqualToOperatorExpression, eol_LessThanOperatorExpression, eol_NotEqualsOperatorExpression, eol_EqualsOperatorExpression, VariableDeclarationExpression, eol_FeatureCallExpression, eol_MethodCallExpression, FeatureCallExpression, eol_CollectionExpression, eol_FOLMethodCallExpression, eol_KeyValueExpression, eol_ModelDeclarationParameter, KeyValueExpression, eol_NewExpression, eol_MapExpression, eol_CollectionInitialisationExpression, eol_PrimitiveExpression, eol_ComparableExpression, PrimitiveExpression, eol_SummableExpression, eol_StringExpression, ComparableExpression, SummableExpression, eol_BooleanExpression, eol_RealExpression, eol_IntegerExpression, eol_BagExpression, CollectionExpression, eol_SetExpression, UniqueCollection, eol_OrderedSetExpression, OrderedCollection, eol_SequenceExpression, eol_OrderedCollection, eol_UniqueCollection, eol_EnumerationLiteralExpression, eol_SwitchCaseExpressionStatement, eol_SwitchCaseDefaultStatement, eol_ExpressionRange, CollectionInitialisationExpression, eol_ExpressionList, eol_TransactionStatement, Statement, eol_ExpressionStatement, eol_SwitchStatement, eol_SwitchCaseStatement, SwitchCaseStatement, eol_IfStatement, eol_ForStatement, eol_DeleteStatement, eol_WhileStatement, eol_ReturnStatement, eol_ThrowStatement, eol_SimpleAnnotationStatement, AnnotationStatement, eol_AssignmentStatement, eol_SpecialAssignmentStatement, AssignmentStatement, eol_ContinueStatement, eol_AbortStatement, eol_BreakStatement, eol_BreakAllStatement, eol_AnnotationStatement, eol_ModelType, AnyType, eol_ModelElementType, eol_ExecutableAnnotationStatement, eol_AnyType, Type, eol_BagType, CollectionType, eol_OrderedCollectionType, eol_UniqueCollectionType, eol_SetType, UniqueCollectionType, eol_OrderedSetType, OrderedCollectionType, eol_SequenceType, eol_PrimitiveType, eol_ComparablePrimitiveType, PrimitiveType, eol_SummablePrimitiveType, eol_PseudoType, eol_SelfType, PseudoType, eol_SelfContentType, eol_MapType, eol_NativeType, eol_VoidType, eol_InvalidType, eol_CollectionType, eol_BooleanType, eol_RealType, ComparablePrimitiveType, SummablePrimitiveType, eol_IntegerType, RealType, eol_StringType},
    associations={importedModule15, container1, region2, start4, end6, imports9, modelDeclarations10, operations12, block14, self41, _result43, dependingOperationDefinitions47, statements18, block20, expression22, condition24, contextType27, returnType29, annotationBlock32, body34, name37, parameters39, resolvedType49, expression52, lhs54, rhs56, method69, resolvedOperationDefinition72, name59, references62, target65, arguments67, keyValues98, contents100, property75, iterator77, conditions79, method82, resolvedFOLDefinition85, key88, value90, typeName93, parameters95, enumeration106, parameterList102, literal104, expression126, cases128, model109, start112, end114, expressions117, names119, body121, expression124, condition150, body153, default130, body132, expression134, condition137, ifBody139, elseIfBodies142, elseBody145, iterator148, expression163, condition156, body158, expression161, name172, expression165, lhs167, rhs169, values174, expression175, name177, driver180, aliases183, parameters186, dynamicTypes188, contentType199, resolvedModelDeclaration190, keyType192, valueType194, expression197},
    generalizations={gen_eol_Block_EOLElement, gen_eol_EOLLibraryModule_EOLElement, gen_eol_EOLModule_EOLLibraryModule, gen_eol_Import_EOLElement, gen_eol_AnnotationBlock_Block, gen_eol_ExpressionOrStatementBlock_EOLElement, gen_eol_OperationDefinition_EOLElement, gen_eol_MultiplyOperatorExpression_ArithmeticOperatorExpression, gen_eol_MinusOperatorExpression_ArithmeticOperatorExpression, gen_eol_PlusOperatorExpression_ArithmeticOperatorExpression, gen_eol_ComparisonOperatorExpression_BinaryOperatorExpression, gen_eol_Expression_EOLElement, gen_eol_OperatorExpression_Expression, gen_eol_UnaryOperatorExpression_OperatorExpression, gen_eol_NotOperatorExpression_UnaryOperatorExpression, gen_eol_NegativeOperatorExpression_UnaryOperatorExpression, gen_eol_BinaryOperatorExpression_OperatorExpression, gen_eol_LogicalOperatorExpression_BinaryOperatorExpression, gen_eol_AndOperatorExpression_LogicalOperatorExpression, gen_eol_XorOperatorExpression_LogicalOperatorExpression, gen_eol_OrOperatorExpression_LogicalOperatorExpression, gen_eol_ImpliesOperatorExpression_LogicalOperatorExpression, gen_eol_ArithmeticOperatorExpression_BinaryOperatorExpression, gen_eol_DivideOperatorExpression_ArithmeticOperatorExpression, gen_eol_PropertyCallExpression_FeatureCallExpression, gen_eol_GreaterThanOrEqualToOperatorExpression_ComparisonOperatorExpression, gen_eol_GreaterThanOperatorExpression_ComparisonOperatorExpression, gen_eol_LessThanOrEqualToOperatorExpression_ComparisonOperatorExpression, gen_eol_LessThanOperatorExpression_ComparisonOperatorExpression, gen_eol_NotEqualsOperatorExpression_ComparisonOperatorExpression, gen_eol_EqualsOperatorExpression_ComparisonOperatorExpression, gen_eol_VariableDeclarationExpression_Expression, gen_eol_FormalParameterExpression_VariableDeclarationExpression, gen_eol_NameExpression_Expression, gen_eol_FeatureCallExpression_Expression, gen_eol_MethodCallExpression_FeatureCallExpression, gen_eol_CollectionExpression_Expression, gen_eol_FOLMethodCallExpression_FeatureCallExpression, gen_eol_KeyValueExpression_Expression, gen_eol_ModelDeclarationParameter_KeyValueExpression, gen_eol_NewExpression_Expression, gen_eol_MapExpression_Expression, gen_eol_PrimitiveExpression_Expression, gen_eol_ComparableExpression_PrimitiveExpression, gen_eol_SummableExpression_PrimitiveExpression, gen_eol_StringExpression_ComparableExpression, gen_eol_StringExpression_SummableExpression, gen_eol_BooleanExpression_PrimitiveExpression, gen_eol_RealExpression_ComparableExpression, gen_eol_RealExpression_SummableExpression, gen_eol_IntegerExpression_ComparableExpression, gen_eol_IntegerExpression_SummableExpression, gen_eol_BagExpression_CollectionExpression, gen_eol_SetExpression_UniqueCollection, gen_eol_OrderedSetExpression_OrderedCollection, gen_eol_OrderedSetExpression_UniqueCollection, gen_eol_SequenceExpression_OrderedCollection, gen_eol_OrderedCollection_CollectionExpression, gen_eol_UniqueCollection_CollectionExpression, gen_eol_EnumerationLiteralExpression_Expression, gen_eol_CollectionInitialisationExpression_Expression, gen_eol_ExpressionRange_CollectionInitialisationExpression, gen_eol_ExpressionList_CollectionInitialisationExpression, gen_eol_Statement_EOLElement, gen_eol_TransactionStatement_Statement, gen_eol_ExpressionStatement_Statement, gen_eol_SwitchStatement_Statement, gen_eol_SwitchCaseStatement_Statement, gen_eol_SwitchCaseDefaultStatement_SwitchCaseStatement, gen_eol_SwitchCaseExpressionStatement_SwitchCaseStatement, gen_eol_IfStatement_Statement, gen_eol_ForStatement_Statement, gen_eol_DeleteStatement_Statement, gen_eol_WhileStatement_Statement, gen_eol_ReturnStatement_Statement, gen_eol_ThrowStatement_Statement, gen_eol_SimpleAnnotationStatement_AnnotationStatement, gen_eol_AssignmentStatement_Statement, gen_eol_SpecialAssignmentStatement_AssignmentStatement, gen_eol_ContinueStatement_Statement, gen_eol_AbortStatement_Statement, gen_eol_BreakStatement_Statement, gen_eol_BreakAllStatement_Statement, gen_eol_AnnotationStatement_Statement, gen_eol_ModelType_AnyType, gen_eol_ModelElementType_AnyType, gen_eol_ExecutableAnnotationStatement_AnnotationStatement, gen_eol_ModelDeclarationStatement_Statement, gen_eol_Type_EOLElement, gen_eol_AnyType_Type, gen_eol_BagType_CollectionType, gen_eol_OrderedCollectionType_CollectionType, gen_eol_UniqueCollectionType_CollectionType, gen_eol_SetType_UniqueCollectionType, gen_eol_OrderedSetType_UniqueCollectionType, gen_eol_OrderedSetType_OrderedCollectionType, gen_eol_SequenceType_OrderedCollectionType, gen_eol_PrimitiveType_AnyType, gen_eol_ComparablePrimitiveType_PrimitiveType, gen_eol_SummablePrimitiveType_PrimitiveType, gen_eol_PseudoType_AnyType, gen_eol_SelfType_PseudoType, gen_eol_SelfContentType_PseudoType, gen_eol_MapType_AnyType, gen_eol_NativeType_AnyType, gen_eol_VoidType_AnyType, gen_eol_InvalidType_AnyType, gen_eol_CollectionType_AnyType, gen_eol_BooleanType_PrimitiveType, gen_eol_RealType_ComparablePrimitiveType, gen_eol_RealType_SummablePrimitiveType, gen_eol_IntegerType_RealType, gen_eol_StringType_ComparablePrimitiveType, gen_eol_StringType_SummablePrimitiveType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)