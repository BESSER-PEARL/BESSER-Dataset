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
eol_Import = Class(name="eol::Import")
eol_ModelDeclarationStatement = Class(name="eol::ModelDeclarationStatement")
eol_OperationDefinition = Class(name="eol::OperationDefinition")
eol_EOLModule = Class(name="eol::EOLModule")
EOLLibraryModule = Class(name="EOLLibraryModule")
eol_Block = Class(name="eol::Block")
eol_Statement = Class(name="eol::Statement", is_abstract=True)
eol_AnnotationBlock = Class(name="eol::AnnotationBlock")
Block = Class(name="Block")
eol_ExpressionOrStatementBlock = Class(name="eol::ExpressionOrStatementBlock")
eol_Expression = Class(name="eol::Expression", is_abstract=True)
eol_EOLLibraryModule = Class(name="eol::EOLLibraryModule")
eol_NameExpression = Class(name="eol::NameExpression")
eol_FormalParameterExpression = Class(name="eol::FormalParameterExpression")
eol_VariableDeclarationExpression = Class(name="eol::VariableDeclarationExpression")
eol_Type = Class(name="eol::Type")
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
eol_MultiplyOperatorExpression = Class(name="eol::MultiplyOperatorExpression")
eol_MinusOperatorExpression = Class(name="eol::MinusOperatorExpression")
eol_PlusOperatorExpression = Class(name="eol::PlusOperatorExpression")
eol_ComparisonOperatorExpression = Class(name="eol::ComparisonOperatorExpression", is_abstract=True)
eol_GreaterThanOrEqualToOperatorExpression = Class(name="eol::GreaterThanOrEqualToOperatorExpression")
ComparisonOperatorExpression = Class(name="ComparisonOperatorExpression")
eol_NotEqualsOperatorExpression = Class(name="eol::NotEqualsOperatorExpression")
eol_EqualsOperatorExpression = Class(name="eol::EqualsOperatorExpression")
VariableDeclarationExpression = Class(name="VariableDeclarationExpression")
eol_FeatureCallExpression = Class(name="eol::FeatureCallExpression", is_abstract=True)
eol_MethodCallExpression = Class(name="eol::MethodCallExpression")
FeatureCallExpression = Class(name="FeatureCallExpression")
eol_GreaterThanOperatorExpression = Class(name="eol::GreaterThanOperatorExpression")
eol_LessThanOrEqualToOperatorExpression = Class(name="eol::LessThanOrEqualToOperatorExpression")
eol_LessThanOperatorExpression = Class(name="eol::LessThanOperatorExpression")
eol_PropertyCallExpression = Class(name="eol::PropertyCallExpression")
eol_FOLMethodCallExpression = Class(name="eol::FOLMethodCallExpression")
eol_KeyValueExpression = Class(name="eol::KeyValueExpression")
eol_ModelDeclarationParameter = Class(name="eol::ModelDeclarationParameter")
KeyValueExpression = Class(name="KeyValueExpression")
eol_NewExpression = Class(name="eol::NewExpression")
eol_MapExpression = Class(name="eol::MapExpression")
eol_CollectionExpression = Class(name="eol::CollectionExpression", is_abstract=True)
eol_CollectionInitialisationExpression = Class(name="eol::CollectionInitialisationExpression", is_abstract=True)
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
eol_PrimitiveExpression = Class(name="eol::PrimitiveExpression", is_abstract=True)
eol_OrderedCollection = Class(name="eol::OrderedCollection", is_abstract=True)
eol_ExpressionList = Class(name="eol::ExpressionList")
eol_UniqueCollection = Class(name="eol::UniqueCollection", is_abstract=True)
eol_EnumerationLiteralExpression = Class(name="eol::EnumerationLiteralExpression")
eol_SequenceExpression = Class(name="eol::SequenceExpression")
eol_ExpressionRange = Class(name="eol::ExpressionRange")
CollectionInitialisationExpression = Class(name="CollectionInitialisationExpression")
SwitchCaseStatement = Class(name="SwitchCaseStatement")
eol_IfStatement = Class(name="eol::IfStatement")
eol_TransactionStatement = Class(name="eol::TransactionStatement")
Statement = Class(name="Statement")
eol_ExpressionStatement = Class(name="eol::ExpressionStatement")
eol_SwitchStatement = Class(name="eol::SwitchStatement")
eol_SwitchCaseExpressionStatement = Class(name="eol::SwitchCaseExpressionStatement")
eol_SwitchCaseDefaultStatement = Class(name="eol::SwitchCaseDefaultStatement")
eol_SwitchCaseStatement = Class(name="eol::SwitchCaseStatement", is_abstract=True)
eol_ThrowStatement = Class(name="eol::ThrowStatement")
eol_DeleteStatement = Class(name="eol::DeleteStatement")
eol_AssignmentStatement = Class(name="eol::AssignmentStatement")
eol_ForStatement = Class(name="eol::ForStatement")
eol_WhileStatement = Class(name="eol::WhileStatement")
eol_ReturnStatement = Class(name="eol::ReturnStatement")
eol_AnyType = Class(name="eol::AnyType")
Type = Class(name="Type")
eol_SpecialAssignmentStatement = Class(name="eol::SpecialAssignmentStatement")
AssignmentStatement = Class(name="AssignmentStatement")
eol_ContinueStatement = Class(name="eol::ContinueStatement")
eol_AbortStatement = Class(name="eol::AbortStatement")
eol_BreakStatement = Class(name="eol::BreakStatement")
eol_BreakAllStatement = Class(name="eol::BreakAllStatement")
eol_AnnotationStatement = Class(name="eol::AnnotationStatement", is_abstract=True)
eol_SimpleAnnotationStatement = Class(name="eol::SimpleAnnotationStatement")
AnnotationStatement = Class(name="AnnotationStatement")
eol_ExecutableAnnotationStatement = Class(name="eol::ExecutableAnnotationStatement")
eol_VoidType = Class(name="eol::VoidType")
eol_InvalidType = Class(name="eol::InvalidType")
eol_CollectionType = Class(name="eol::CollectionType")
eol_BagType = Class(name="eol::BagType")
CollectionType = Class(name="CollectionType")
eol_OrderedCollectionType = Class(name="eol::OrderedCollectionType", is_abstract=True)
eol_UniqueCollectionType = Class(name="eol::UniqueCollectionType", is_abstract=True)
eol_SetType = Class(name="eol::SetType")
UniqueCollectionType = Class(name="UniqueCollectionType")
eol_OrderedSetType = Class(name="eol::OrderedSetType")
eol_ModelType = Class(name="eol::ModelType")
AnyType = Class(name="AnyType")
eol_ModelElementType = Class(name="eol::ModelElementType")
eol_PseudoType = Class(name="eol::PseudoType", is_abstract=True)
eol_SelfType = Class(name="eol::SelfType")
PseudoType = Class(name="PseudoType")
eol_SelfContentType = Class(name="eol::SelfContentType")
eol_MapType = Class(name="eol::MapType")
eol_NativeType = Class(name="eol::NativeType")
OrderedCollectionType = Class(name="OrderedCollectionType")
eol_SequenceType = Class(name="eol::SequenceType")
eol_PrimitiveType = Class(name="eol::PrimitiveType", is_abstract=True)
eol_ComparablePrimitiveType = Class(name="eol::ComparablePrimitiveType", is_abstract=True)
PrimitiveType = Class(name="PrimitiveType")
eol_SummablePrimitiveType = Class(name="eol::SummablePrimitiveType", is_abstract=True)
eol_BooleanType = Class(name="eol::BooleanType")
eol_RealType = Class(name="eol::RealType")
ComparablePrimitiveType = Class(name="ComparablePrimitiveType")
SummablePrimitiveType = Class(name="SummablePrimitiveType")
eol_IntegerType = Class(name="eol::IntegerType")
RealType = Class(name="RealType")
eol_StringType = Class(name="eol::StringType")

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

# eol_Statement class attributes and methods

# eol_AnnotationBlock class attributes and methods

# Block class attributes and methods

# eol_ExpressionOrStatementBlock class attributes and methods

# eol_Expression class attributes and methods
eol_Expression_inBrackets: Property = Property(name="inBrackets", type=BooleanType)
eol_Expression.attributes={eol_Expression_inBrackets}

# eol_EOLLibraryModule class attributes and methods
eol_EOLLibraryModule_name: Property = Property(name="name", type=StringType)
eol_EOLLibraryModule.attributes={eol_EOLLibraryModule_name}

# eol_NameExpression class attributes and methods
eol_NameExpression_name: Property = Property(name="name", type=StringType)
eol_NameExpression_resolvedContent: Property = Property(name="resolvedContent", type=StringType)
eol_NameExpression_isType: Property = Property(name="isType", type=BooleanType)
eol_NameExpression.attributes={eol_NameExpression_isType, eol_NameExpression_name, eol_NameExpression_resolvedContent}

# eol_FormalParameterExpression class attributes and methods

# eol_VariableDeclarationExpression class attributes and methods
eol_VariableDeclarationExpression_create: Property = Property(name="create", type=BooleanType)
eol_VariableDeclarationExpression.attributes={eol_VariableDeclarationExpression_create}

# eol_Type class attributes and methods

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

# eol_MultiplyOperatorExpression class attributes and methods

# eol_MinusOperatorExpression class attributes and methods

# eol_PlusOperatorExpression class attributes and methods

# eol_ComparisonOperatorExpression class attributes and methods

# eol_GreaterThanOrEqualToOperatorExpression class attributes and methods

# ComparisonOperatorExpression class attributes and methods

# eol_NotEqualsOperatorExpression class attributes and methods

# eol_EqualsOperatorExpression class attributes and methods

# VariableDeclarationExpression class attributes and methods

# eol_FeatureCallExpression class attributes and methods
eol_FeatureCallExpression_arrow: Property = Property(name="arrow", type=BooleanType)
eol_FeatureCallExpression.attributes={eol_FeatureCallExpression_arrow}

# eol_MethodCallExpression class attributes and methods

# FeatureCallExpression class attributes and methods

# eol_GreaterThanOperatorExpression class attributes and methods

# eol_LessThanOrEqualToOperatorExpression class attributes and methods

# eol_LessThanOperatorExpression class attributes and methods

# eol_PropertyCallExpression class attributes and methods
eol_PropertyCallExpression_extended: Property = Property(name="extended", type=BooleanType)
eol_PropertyCallExpression.attributes={eol_PropertyCallExpression_extended}

# eol_FOLMethodCallExpression class attributes and methods

# eol_KeyValueExpression class attributes and methods

# eol_ModelDeclarationParameter class attributes and methods

# KeyValueExpression class attributes and methods

# eol_NewExpression class attributes and methods

# eol_MapExpression class attributes and methods

# eol_CollectionExpression class attributes and methods

# eol_CollectionInitialisationExpression class attributes and methods

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

# eol_PrimitiveExpression class attributes and methods

# eol_OrderedCollection class attributes and methods

# eol_ExpressionList class attributes and methods

# eol_UniqueCollection class attributes and methods

# eol_EnumerationLiteralExpression class attributes and methods

# eol_SequenceExpression class attributes and methods

# eol_ExpressionRange class attributes and methods

# CollectionInitialisationExpression class attributes and methods

# SwitchCaseStatement class attributes and methods

# eol_IfStatement class attributes and methods

# eol_TransactionStatement class attributes and methods

# Statement class attributes and methods

# eol_ExpressionStatement class attributes and methods

# eol_SwitchStatement class attributes and methods

# eol_SwitchCaseExpressionStatement class attributes and methods

# eol_SwitchCaseDefaultStatement class attributes and methods

# eol_SwitchCaseStatement class attributes and methods

# eol_ThrowStatement class attributes and methods

# eol_DeleteStatement class attributes and methods

# eol_AssignmentStatement class attributes and methods

# eol_ForStatement class attributes and methods

# eol_WhileStatement class attributes and methods

# eol_ReturnStatement class attributes and methods

# eol_AnyType class attributes and methods
eol_AnyType_declared: Property = Property(name="declared", type=BooleanType)
eol_AnyType.attributes={eol_AnyType_declared}

# Type class attributes and methods

# eol_SpecialAssignmentStatement class attributes and methods

# AssignmentStatement class attributes and methods

# eol_ContinueStatement class attributes and methods

# eol_AbortStatement class attributes and methods

# eol_BreakStatement class attributes and methods

# eol_BreakAllStatement class attributes and methods

# eol_AnnotationStatement class attributes and methods

# eol_SimpleAnnotationStatement class attributes and methods

# AnnotationStatement class attributes and methods

# eol_ExecutableAnnotationStatement class attributes and methods

# eol_VoidType class attributes and methods

# eol_InvalidType class attributes and methods

# eol_CollectionType class attributes and methods

# eol_BagType class attributes and methods

# CollectionType class attributes and methods

# eol_OrderedCollectionType class attributes and methods

# eol_UniqueCollectionType class attributes and methods

# eol_SetType class attributes and methods

# UniqueCollectionType class attributes and methods

# eol_OrderedSetType class attributes and methods

# eol_ModelType class attributes and methods
eol_ModelType_resolvedIMetamodel: Property = Property(name="resolvedIMetamodel", type=StringType)
eol_ModelType_modelName: Property = Property(name="modelName", type=StringType)
eol_ModelType.attributes={eol_ModelType_resolvedIMetamodel, eol_ModelType_modelName}

# AnyType class attributes and methods

# eol_ModelElementType class attributes and methods
eol_ModelElementType_modelName: Property = Property(name="modelName", type=StringType)
eol_ModelElementType_elementName: Property = Property(name="elementName", type=StringType)
eol_ModelElementType_resolvedIMetamodel: Property = Property(name="resolvedIMetamodel", type=StringType)
eol_ModelElementType_resolvedIPackage: Property = Property(name="resolvedIPackage", type=StringType)
eol_ModelElementType_modelElementType: Property = Property(name="modelElementType", type=StringType)
eol_ModelElementType.attributes={eol_ModelElementType_modelName, eol_ModelElementType_resolvedIPackage, eol_ModelElementType_elementName, eol_ModelElementType_resolvedIMetamodel, eol_ModelElementType_modelElementType}

# eol_PseudoType class attributes and methods

# eol_SelfType class attributes and methods

# PseudoType class attributes and methods

# eol_SelfContentType class attributes and methods

# eol_MapType class attributes and methods

# eol_NativeType class attributes and methods

# OrderedCollectionType class attributes and methods

# eol_SequenceType class attributes and methods

# eol_PrimitiveType class attributes and methods

# eol_ComparablePrimitiveType class attributes and methods

# PrimitiveType class attributes and methods

# eol_SummablePrimitiveType class attributes and methods

# eol_BooleanType class attributes and methods

# eol_RealType class attributes and methods

# ComparablePrimitiveType class attributes and methods

# SummablePrimitiveType class attributes and methods

# eol_IntegerType class attributes and methods

# RealType class attributes and methods

# eol_StringType class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="eol_Import", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLLibraryModule", type=eol_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelDeclarations1: BinaryAssociation = BinaryAssociation(
    name="modelDeclarations1",
    ends={
        Property(name="eol_ModelDeclarationStatement", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLLibraryModule2", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations3: BinaryAssociation = BinaryAssociation(
    name="operations3",
    ends={
        Property(name="eol_OperationDefinition", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLLibraryModule4", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block5: BinaryAssociation = BinaryAssociation(
    name="block5",
    ends={
        Property(name="eol_Block", type=eol_EOLModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLModule", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedModule6: BinaryAssociation = BinaryAssociation(
    name="importedModule6",
    ends={
        Property(name="eol_EOLLibraryModule8", type=eol_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Import7", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements9: BinaryAssociation = BinaryAssociation(
    name="statements9",
    ends={
        Property(name="eol_Statement", type=eol_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Block10", type=eol_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block11: BinaryAssociation = BinaryAssociation(
    name="block11",
    ends={
        Property(name="eol_Block12", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionOrStatementBlock", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression13: BinaryAssociation = BinaryAssociation(
    name="expression13",
    ends={
        Property(name="eol_Expression", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionOrStatementBlock14", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="eol_Expression17", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionOrStatementBlock16", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationBlock23: BinaryAssociation = BinaryAssociation(
    name="annotationBlock23",
    ends={
        Property(name="eol_AnnotationBlock", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition24", type=eol_AnnotationBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body25: BinaryAssociation = BinaryAssociation(
    name="body25",
    ends={
        Property(name="eol_Block27", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition26", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name28: BinaryAssociation = BinaryAssociation(
    name="name28",
    ends={
        Property(name="eol_NameExpression", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition29", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters30: BinaryAssociation = BinaryAssociation(
    name="parameters30",
    ends={
        Property(name="eol_FormalParameterExpression", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition31", type=eol_FormalParameterExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
self32: BinaryAssociation = BinaryAssociation(
    name="self32",
    ends={
        Property(name="eol_VariableDeclarationExpression", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition33", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
_result34: BinaryAssociation = BinaryAssociation(
    name="_result34",
    ends={
        Property(name="eol_VariableDeclarationExpression36", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition35", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependingOperationDefinitions38: BinaryAssociation = BinaryAssociation(
    name="dependingOperationDefinitions38",
    ends={
        Property(name="eol_OperationDefinition39", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition37", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
contextType18: BinaryAssociation = BinaryAssociation(
    name="contextType18",
    ends={
        Property(name="eol_Type", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition19", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedType40: BinaryAssociation = BinaryAssociation(
    name="resolvedType40",
    ends={
        Property(name="eol_Type42", type=eol_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Expression41", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType20: BinaryAssociation = BinaryAssociation(
    name="returnType20",
    ends={
        Property(name="eol_Type22", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition21", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression43: BinaryAssociation = BinaryAssociation(
    name="expression43",
    ends={
        Property(name="eol_Expression44", type=eol_UnaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_UnaryOperatorExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs45: BinaryAssociation = BinaryAssociation(
    name="lhs45",
    ends={
        Property(name="eol_Expression46", type=eol_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_BinaryOperatorExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs47: BinaryAssociation = BinaryAssociation(
    name="rhs47",
    ends={
        Property(name="eol_Expression49", type=eol_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_BinaryOperatorExpression48", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name50: BinaryAssociation = BinaryAssociation(
    name="name50",
    ends={
        Property(name="eol_NameExpression52", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression51", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
references53: BinaryAssociation = BinaryAssociation(
    name="references53",
    ends={
        Property(name="eol_NameExpression55", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression54", type=eol_NameExpression, multiplicity=Multiplicity(0, 9999))
    }
)
target56: BinaryAssociation = BinaryAssociation(
    name="target56",
    ends={
        Property(name="eol_Expression57", type=eol_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FeatureCallExpression", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments58: BinaryAssociation = BinaryAssociation(
    name="arguments58",
    ends={
        Property(name="eol_Expression59", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolvedOperationDefinition63: BinaryAssociation = BinaryAssociation(
    name="resolvedOperationDefinition63",
    ends={
        Property(name="eol_MethodCallExpression64", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 1)),
        Property(name="eol_OperationDefinition65", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1))
    }
)
property66: BinaryAssociation = BinaryAssociation(
    name="property66",
    ends={
        Property(name="eol_NameExpression67", type=eol_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_PropertyCallExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator68: BinaryAssociation = BinaryAssociation(
    name="iterator68",
    ends={
        Property(name="eol_FormalParameterExpression69", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression", type=eol_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditions70: BinaryAssociation = BinaryAssociation(
    name="conditions70",
    ends={
        Property(name="eol_Expression72", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression71", type=eol_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
method73: BinaryAssociation = BinaryAssociation(
    name="method73",
    ends={
        Property(name="eol_NameExpression75", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression74", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedFOLDefinition76: BinaryAssociation = BinaryAssociation(
    name="resolvedFOLDefinition76",
    ends={
        Property(name="eol_OperationDefinition78", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression77", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 1))
    }
)
method60: BinaryAssociation = BinaryAssociation(
    name="method60",
    ends={
        Property(name="eol_NameExpression62", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression61", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value81: BinaryAssociation = BinaryAssociation(
    name="value81",
    ends={
        Property(name="eol_Expression83", type=eol_KeyValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_KeyValueExpression82", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeName84: BinaryAssociation = BinaryAssociation(
    name="typeName84",
    ends={
        Property(name="eol_NameExpression85", type=eol_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NewExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters86: BinaryAssociation = BinaryAssociation(
    name="parameters86",
    ends={
        Property(name="eol_Expression88", type=eol_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NewExpression87", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyValues89: BinaryAssociation = BinaryAssociation(
    name="keyValues89",
    ends={
        Property(name="eol_KeyValueExpression90", type=eol_MapExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapExpression", type=eol_KeyValueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents91: BinaryAssociation = BinaryAssociation(
    name="contents91",
    ends={
        Property(name="eol_Expression92", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterList93: BinaryAssociation = BinaryAssociation(
    name="parameterList93",
    ends={
        Property(name="eol_CollectionInitialisationExpression", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression94", type=eol_CollectionInitialisationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key79: BinaryAssociation = BinaryAssociation(
    name="key79",
    ends={
        Property(name="eol_Expression80", type=eol_KeyValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_KeyValueExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
start103: BinaryAssociation = BinaryAssociation(
    name="start103",
    ends={
        Property(name="eol_Expression104", type=eol_ExpressionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionRange", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end105: BinaryAssociation = BinaryAssociation(
    name="end105",
    ends={
        Property(name="eol_Expression107", type=eol_ExpressionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionRange106", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions108: BinaryAssociation = BinaryAssociation(
    name="expressions108",
    ends={
        Property(name="eol_Expression109", type=eol_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionList", type=eol_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
literal95: BinaryAssociation = BinaryAssociation(
    name="literal95",
    ends={
        Property(name="eol_NameExpression96", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumeration97: BinaryAssociation = BinaryAssociation(
    name="enumeration97",
    ends={
        Property(name="eol_NameExpression99", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression98", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model100: BinaryAssociation = BinaryAssociation(
    name="model100",
    ends={
        Property(name="eol_NameExpression102", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression101", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body123: BinaryAssociation = BinaryAssociation(
    name="body123",
    ends={
        Property(name="eol_ExpressionOrStatementBlock124", type=eol_SwitchCaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchCaseStatement", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression125: BinaryAssociation = BinaryAssociation(
    name="expression125",
    ends={
        Property(name="eol_Expression127", type=eol_SwitchCaseExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchCaseExpressionStatement126", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition128: BinaryAssociation = BinaryAssociation(
    name="condition128",
    ends={
        Property(name="eol_Expression129", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifBody130: BinaryAssociation = BinaryAssociation(
    name="ifBody130",
    ends={
        Property(name="eol_ExpressionOrStatementBlock132", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement131", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
names110: BinaryAssociation = BinaryAssociation(
    name="names110",
    ends={
        Property(name="eol_NameExpression111", type=eol_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TransactionStatement", type=eol_NameExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body112: BinaryAssociation = BinaryAssociation(
    name="body112",
    ends={
        Property(name="eol_ExpressionOrStatementBlock114", type=eol_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TransactionStatement113", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression115: BinaryAssociation = BinaryAssociation(
    name="expression115",
    ends={
        Property(name="eol_Expression116", type=eol_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
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
expression154: BinaryAssociation = BinaryAssociation(
    name="expression154",
    ends={
        Property(name="eol_Expression155", type=eol_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ThrowStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression156: BinaryAssociation = BinaryAssociation(
    name="expression156",
    ends={
        Property(name="eol_Expression157", type=eol_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_DeleteStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs158: BinaryAssociation = BinaryAssociation(
    name="lhs158",
    ends={
        Property(name="eol_Expression159", type=eol_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AssignmentStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs160: BinaryAssociation = BinaryAssociation(
    name="rhs160",
    ends={
        Property(name="eol_Expression162", type=eol_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AssignmentStatement161", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseIfBodies133: BinaryAssociation = BinaryAssociation(
    name="elseIfBodies133",
    ends={
        Property(name="eol_ExpressionOrStatementBlock135", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement134", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseBody136: BinaryAssociation = BinaryAssociation(
    name="elseBody136",
    ends={
        Property(name="eol_ExpressionOrStatementBlock138", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement137", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterator139: BinaryAssociation = BinaryAssociation(
    name="iterator139",
    ends={
        Property(name="eol_FormalParameterExpression140", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement", type=eol_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition141: BinaryAssociation = BinaryAssociation(
    name="condition141",
    ends={
        Property(name="eol_Expression143", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement142", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body144: BinaryAssociation = BinaryAssociation(
    name="body144",
    ends={
        Property(name="eol_ExpressionOrStatementBlock146", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement145", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition147: BinaryAssociation = BinaryAssociation(
    name="condition147",
    ends={
        Property(name="eol_Expression148", type=eol_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_WhileStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body149: BinaryAssociation = BinaryAssociation(
    name="body149",
    ends={
        Property(name="eol_ExpressionOrStatementBlock151", type=eol_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_WhileStatement150", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression152: BinaryAssociation = BinaryAssociation(
    name="expression152",
    ends={
        Property(name="eol_Expression153", type=eol_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ReturnStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
driver171: BinaryAssociation = BinaryAssociation(
    name="driver171",
    ends={
        Property(name="eol_NameExpression173", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement172", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
aliases174: BinaryAssociation = BinaryAssociation(
    name="aliases174",
    ends={
        Property(name="eol_VariableDeclarationExpression176", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement175", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters177: BinaryAssociation = BinaryAssociation(
    name="parameters177",
    ends={
        Property(name="eol_ModelDeclarationParameter", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement178", type=eol_ModelDeclarationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dynamicTypes179: BinaryAssociation = BinaryAssociation(
    name="dynamicTypes179",
    ends={
        Property(name="eol_Type180", type=eol_AnyType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnyType", type=eol_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name163: BinaryAssociation = BinaryAssociation(
    name="name163",
    ends={
        Property(name="eol_NameExpression164", type=eol_AnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnnotationStatement", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values165: BinaryAssociation = BinaryAssociation(
    name="values165",
    ends={
        Property(name="eol_StringExpression", type=eol_SimpleAnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SimpleAnnotationStatement", type=eol_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression166: BinaryAssociation = BinaryAssociation(
    name="expression166",
    ends={
        Property(name="eol_Expression167", type=eol_ExecutableAnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExecutableAnnotationStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name168: BinaryAssociation = BinaryAssociation(
    name="name168",
    ends={
        Property(name="eol_VariableDeclarationExpression170", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement169", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression188: BinaryAssociation = BinaryAssociation(
    name="expression188",
    ends={
        Property(name="eol_StringExpression189", type=eol_NativeType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NativeType", type=eol_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contentType190: BinaryAssociation = BinaryAssociation(
    name="contentType190",
    ends={
        Property(name="eol_Type191", type=eol_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionType", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedModelDeclaration181: BinaryAssociation = BinaryAssociation(
    name="resolvedModelDeclaration181",
    ends={
        Property(name="eol_ModelDeclarationStatement182", type=eol_ModelElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelElementType", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1))
    }
)
keyType183: BinaryAssociation = BinaryAssociation(
    name="keyType183",
    ends={
        Property(name="eol_AnyType184", type=eol_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapType", type=eol_AnyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueType185: BinaryAssociation = BinaryAssociation(
    name="valueType185",
    ends={
        Property(name="eol_AnyType187", type=eol_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapType186", type=eol_AnyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_eol_EOLModule_EOLLibraryModule = Generalization(general=EOLLibraryModule, specific=eol_EOLModule)
gen_eol_AnnotationBlock_Block = Generalization(general=Block, specific=eol_AnnotationBlock)
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
gen_eol_MultiplyOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_MultiplyOperatorExpression)
gen_eol_MinusOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_MinusOperatorExpression)
gen_eol_PlusOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_PlusOperatorExpression)
gen_eol_ComparisonOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_ComparisonOperatorExpression)
gen_eol_GreaterThanOrEqualToOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_GreaterThanOrEqualToOperatorExpression)
gen_eol_NotEqualsOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_NotEqualsOperatorExpression)
gen_eol_EqualsOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_EqualsOperatorExpression)
gen_eol_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=eol_VariableDeclarationExpression)
gen_eol_FormalParameterExpression_VariableDeclarationExpression = Generalization(general=VariableDeclarationExpression, specific=eol_FormalParameterExpression)
gen_eol_NameExpression_Expression = Generalization(general=Expression, specific=eol_NameExpression)
gen_eol_FeatureCallExpression_Expression = Generalization(general=Expression, specific=eol_FeatureCallExpression)
gen_eol_MethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_MethodCallExpression)
gen_eol_GreaterThanOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_GreaterThanOperatorExpression)
gen_eol_LessThanOrEqualToOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_LessThanOrEqualToOperatorExpression)
gen_eol_LessThanOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_LessThanOperatorExpression)
gen_eol_PropertyCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_PropertyCallExpression)
gen_eol_FOLMethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_FOLMethodCallExpression)
gen_eol_KeyValueExpression_Expression = Generalization(general=Expression, specific=eol_KeyValueExpression)
gen_eol_ModelDeclarationParameter_KeyValueExpression = Generalization(general=KeyValueExpression, specific=eol_ModelDeclarationParameter)
gen_eol_NewExpression_Expression = Generalization(general=Expression, specific=eol_NewExpression)
gen_eol_MapExpression_Expression = Generalization(general=Expression, specific=eol_MapExpression)
gen_eol_CollectionExpression_Expression = Generalization(general=Expression, specific=eol_CollectionExpression)
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
gen_eol_OrderedCollection_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_OrderedCollection)
gen_eol_ExpressionList_CollectionInitialisationExpression = Generalization(general=CollectionInitialisationExpression, specific=eol_ExpressionList)
gen_eol_UniqueCollection_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_UniqueCollection)
gen_eol_EnumerationLiteralExpression_Expression = Generalization(general=Expression, specific=eol_EnumerationLiteralExpression)
gen_eol_CollectionInitialisationExpression_Expression = Generalization(general=Expression, specific=eol_CollectionInitialisationExpression)
gen_eol_SequenceExpression_OrderedCollection = Generalization(general=OrderedCollection, specific=eol_SequenceExpression)
gen_eol_ExpressionRange_CollectionInitialisationExpression = Generalization(general=CollectionInitialisationExpression, specific=eol_ExpressionRange)
gen_eol_SwitchCaseStatement_Statement = Generalization(general=Statement, specific=eol_SwitchCaseStatement)
gen_eol_SwitchCaseDefaultStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_SwitchCaseDefaultStatement)
gen_eol_SwitchCaseExpressionStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_SwitchCaseExpressionStatement)
gen_eol_IfStatement_Statement = Generalization(general=Statement, specific=eol_IfStatement)
gen_eol_TransactionStatement_Statement = Generalization(general=Statement, specific=eol_TransactionStatement)
gen_eol_ExpressionStatement_Statement = Generalization(general=Statement, specific=eol_ExpressionStatement)
gen_eol_SwitchStatement_Statement = Generalization(general=Statement, specific=eol_SwitchStatement)
gen_eol_ThrowStatement_Statement = Generalization(general=Statement, specific=eol_ThrowStatement)
gen_eol_DeleteStatement_Statement = Generalization(general=Statement, specific=eol_DeleteStatement)
gen_eol_AssignmentStatement_Statement = Generalization(general=Statement, specific=eol_AssignmentStatement)
gen_eol_ForStatement_Statement = Generalization(general=Statement, specific=eol_ForStatement)
gen_eol_WhileStatement_Statement = Generalization(general=Statement, specific=eol_WhileStatement)
gen_eol_ReturnStatement_Statement = Generalization(general=Statement, specific=eol_ReturnStatement)
gen_eol_AnyType_Type = Generalization(general=Type, specific=eol_AnyType)
gen_eol_SpecialAssignmentStatement_AssignmentStatement = Generalization(general=AssignmentStatement, specific=eol_SpecialAssignmentStatement)
gen_eol_ContinueStatement_Statement = Generalization(general=Statement, specific=eol_ContinueStatement)
gen_eol_AbortStatement_Statement = Generalization(general=Statement, specific=eol_AbortStatement)
gen_eol_BreakStatement_Statement = Generalization(general=Statement, specific=eol_BreakStatement)
gen_eol_BreakAllStatement_Statement = Generalization(general=Statement, specific=eol_BreakAllStatement)
gen_eol_AnnotationStatement_Statement = Generalization(general=Statement, specific=eol_AnnotationStatement)
gen_eol_SimpleAnnotationStatement_AnnotationStatement = Generalization(general=AnnotationStatement, specific=eol_SimpleAnnotationStatement)
gen_eol_ExecutableAnnotationStatement_AnnotationStatement = Generalization(general=AnnotationStatement, specific=eol_ExecutableAnnotationStatement)
gen_eol_ModelDeclarationStatement_Statement = Generalization(general=Statement, specific=eol_ModelDeclarationStatement)
gen_eol_VoidType_AnyType = Generalization(general=AnyType, specific=eol_VoidType)
gen_eol_InvalidType_AnyType = Generalization(general=AnyType, specific=eol_InvalidType)
gen_eol_CollectionType_AnyType = Generalization(general=AnyType, specific=eol_CollectionType)
gen_eol_BagType_CollectionType = Generalization(general=CollectionType, specific=eol_BagType)
gen_eol_OrderedCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_OrderedCollectionType)
gen_eol_UniqueCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_UniqueCollectionType)
gen_eol_SetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_SetType)
gen_eol_OrderedSetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_OrderedSetType)
gen_eol_ModelType_AnyType = Generalization(general=AnyType, specific=eol_ModelType)
gen_eol_ModelElementType_AnyType = Generalization(general=AnyType, specific=eol_ModelElementType)
gen_eol_PseudoType_AnyType = Generalization(general=AnyType, specific=eol_PseudoType)
gen_eol_SelfType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfType)
gen_eol_SelfContentType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfContentType)
gen_eol_MapType_AnyType = Generalization(general=AnyType, specific=eol_MapType)
gen_eol_NativeType_AnyType = Generalization(general=AnyType, specific=eol_NativeType)
gen_eol_OrderedSetType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_OrderedSetType)
gen_eol_SequenceType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_SequenceType)
gen_eol_PrimitiveType_AnyType = Generalization(general=AnyType, specific=eol_PrimitiveType)
gen_eol_ComparablePrimitiveType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_ComparablePrimitiveType)
gen_eol_SummablePrimitiveType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_SummablePrimitiveType)
gen_eol_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_BooleanType)
gen_eol_RealType_ComparablePrimitiveType = Generalization(general=ComparablePrimitiveType, specific=eol_RealType)
gen_eol_RealType_SummablePrimitiveType = Generalization(general=SummablePrimitiveType, specific=eol_RealType)
gen_eol_IntegerType_RealType = Generalization(general=RealType, specific=eol_IntegerType)
gen_eol_StringType_ComparablePrimitiveType = Generalization(general=ComparablePrimitiveType, specific=eol_StringType)
gen_eol_StringType_SummablePrimitiveType = Generalization(general=SummablePrimitiveType, specific=eol_StringType)

# Domain Model
domain_model = DomainModel(
    name="eol",
    types={eol_Import, eol_ModelDeclarationStatement, eol_OperationDefinition, eol_EOLModule, EOLLibraryModule, eol_Block, eol_Statement, eol_AnnotationBlock, Block, eol_ExpressionOrStatementBlock, eol_Expression, eol_EOLLibraryModule, eol_NameExpression, eol_FormalParameterExpression, eol_VariableDeclarationExpression, eol_Type, eol_OperatorExpression, Expression, eol_UnaryOperatorExpression, OperatorExpression, eol_NotOperatorExpression, UnaryOperatorExpression, eol_NegativeOperatorExpression, eol_BinaryOperatorExpression, eol_LogicalOperatorExpression, BinaryOperatorExpression, eol_AndOperatorExpression, LogicalOperatorExpression, eol_XorOperatorExpression, eol_OrOperatorExpression, eol_ImpliesOperatorExpression, eol_ArithmeticOperatorExpression, eol_DivideOperatorExpression, ArithmeticOperatorExpression, eol_MultiplyOperatorExpression, eol_MinusOperatorExpression, eol_PlusOperatorExpression, eol_ComparisonOperatorExpression, eol_GreaterThanOrEqualToOperatorExpression, ComparisonOperatorExpression, eol_NotEqualsOperatorExpression, eol_EqualsOperatorExpression, VariableDeclarationExpression, eol_FeatureCallExpression, eol_MethodCallExpression, FeatureCallExpression, eol_GreaterThanOperatorExpression, eol_LessThanOrEqualToOperatorExpression, eol_LessThanOperatorExpression, eol_PropertyCallExpression, eol_FOLMethodCallExpression, eol_KeyValueExpression, eol_ModelDeclarationParameter, KeyValueExpression, eol_NewExpression, eol_MapExpression, eol_CollectionExpression, eol_CollectionInitialisationExpression, eol_ComparableExpression, PrimitiveExpression, eol_SummableExpression, eol_StringExpression, ComparableExpression, SummableExpression, eol_BooleanExpression, eol_RealExpression, eol_IntegerExpression, eol_BagExpression, CollectionExpression, eol_SetExpression, UniqueCollection, eol_OrderedSetExpression, OrderedCollection, eol_PrimitiveExpression, eol_OrderedCollection, eol_ExpressionList, eol_UniqueCollection, eol_EnumerationLiteralExpression, eol_SequenceExpression, eol_ExpressionRange, CollectionInitialisationExpression, SwitchCaseStatement, eol_IfStatement, eol_TransactionStatement, Statement, eol_ExpressionStatement, eol_SwitchStatement, eol_SwitchCaseExpressionStatement, eol_SwitchCaseDefaultStatement, eol_SwitchCaseStatement, eol_ThrowStatement, eol_DeleteStatement, eol_AssignmentStatement, eol_ForStatement, eol_WhileStatement, eol_ReturnStatement, eol_AnyType, Type, eol_SpecialAssignmentStatement, AssignmentStatement, eol_ContinueStatement, eol_AbortStatement, eol_BreakStatement, eol_BreakAllStatement, eol_AnnotationStatement, eol_SimpleAnnotationStatement, AnnotationStatement, eol_ExecutableAnnotationStatement, eol_VoidType, eol_InvalidType, eol_CollectionType, eol_BagType, CollectionType, eol_OrderedCollectionType, eol_UniqueCollectionType, eol_SetType, UniqueCollectionType, eol_OrderedSetType, eol_ModelType, AnyType, eol_ModelElementType, eol_PseudoType, eol_SelfType, PseudoType, eol_SelfContentType, eol_MapType, eol_NativeType, OrderedCollectionType, eol_SequenceType, eol_PrimitiveType, eol_ComparablePrimitiveType, PrimitiveType, eol_SummablePrimitiveType, eol_BooleanType, eol_RealType, ComparablePrimitiveType, SummablePrimitiveType, eol_IntegerType, RealType, eol_StringType},
    associations={imports0, modelDeclarations1, operations3, block5, importedModule6, statements9, block11, expression13, condition15, annotationBlock23, body25, name28, parameters30, self32, _result34, dependingOperationDefinitions38, contextType18, resolvedType40, returnType20, expression43, lhs45, rhs47, name50, references53, target56, arguments58, resolvedOperationDefinition63, property66, iterator68, conditions70, method73, resolvedFOLDefinition76, method60, value81, typeName84, parameters86, keyValues89, contents91, parameterList93, key79, start103, end105, expressions108, literal95, enumeration97, model100, body123, expression125, condition128, ifBody130, names110, body112, expression115, expression117, cases119, default121, expression154, expression156, lhs158, rhs160, elseIfBodies133, elseBody136, iterator139, condition141, body144, condition147, body149, expression152, driver171, aliases174, parameters177, dynamicTypes179, name163, values165, expression166, name168, expression188, contentType190, resolvedModelDeclaration181, keyType183, valueType185},
    generalizations={gen_eol_EOLModule_EOLLibraryModule, gen_eol_AnnotationBlock_Block, gen_eol_OperatorExpression_Expression, gen_eol_UnaryOperatorExpression_OperatorExpression, gen_eol_NotOperatorExpression_UnaryOperatorExpression, gen_eol_NegativeOperatorExpression_UnaryOperatorExpression, gen_eol_BinaryOperatorExpression_OperatorExpression, gen_eol_LogicalOperatorExpression_BinaryOperatorExpression, gen_eol_AndOperatorExpression_LogicalOperatorExpression, gen_eol_XorOperatorExpression_LogicalOperatorExpression, gen_eol_OrOperatorExpression_LogicalOperatorExpression, gen_eol_ImpliesOperatorExpression_LogicalOperatorExpression, gen_eol_ArithmeticOperatorExpression_BinaryOperatorExpression, gen_eol_DivideOperatorExpression_ArithmeticOperatorExpression, gen_eol_MultiplyOperatorExpression_ArithmeticOperatorExpression, gen_eol_MinusOperatorExpression_ArithmeticOperatorExpression, gen_eol_PlusOperatorExpression_ArithmeticOperatorExpression, gen_eol_ComparisonOperatorExpression_BinaryOperatorExpression, gen_eol_GreaterThanOrEqualToOperatorExpression_ComparisonOperatorExpression, gen_eol_NotEqualsOperatorExpression_ComparisonOperatorExpression, gen_eol_EqualsOperatorExpression_ComparisonOperatorExpression, gen_eol_VariableDeclarationExpression_Expression, gen_eol_FormalParameterExpression_VariableDeclarationExpression, gen_eol_NameExpression_Expression, gen_eol_FeatureCallExpression_Expression, gen_eol_MethodCallExpression_FeatureCallExpression, gen_eol_GreaterThanOperatorExpression_ComparisonOperatorExpression, gen_eol_LessThanOrEqualToOperatorExpression_ComparisonOperatorExpression, gen_eol_LessThanOperatorExpression_ComparisonOperatorExpression, gen_eol_PropertyCallExpression_FeatureCallExpression, gen_eol_FOLMethodCallExpression_FeatureCallExpression, gen_eol_KeyValueExpression_Expression, gen_eol_ModelDeclarationParameter_KeyValueExpression, gen_eol_NewExpression_Expression, gen_eol_MapExpression_Expression, gen_eol_CollectionExpression_Expression, gen_eol_PrimitiveExpression_Expression, gen_eol_ComparableExpression_PrimitiveExpression, gen_eol_SummableExpression_PrimitiveExpression, gen_eol_StringExpression_ComparableExpression, gen_eol_StringExpression_SummableExpression, gen_eol_BooleanExpression_PrimitiveExpression, gen_eol_RealExpression_ComparableExpression, gen_eol_RealExpression_SummableExpression, gen_eol_IntegerExpression_ComparableExpression, gen_eol_IntegerExpression_SummableExpression, gen_eol_BagExpression_CollectionExpression, gen_eol_SetExpression_UniqueCollection, gen_eol_OrderedSetExpression_OrderedCollection, gen_eol_OrderedSetExpression_UniqueCollection, gen_eol_OrderedCollection_CollectionExpression, gen_eol_ExpressionList_CollectionInitialisationExpression, gen_eol_UniqueCollection_CollectionExpression, gen_eol_EnumerationLiteralExpression_Expression, gen_eol_CollectionInitialisationExpression_Expression, gen_eol_SequenceExpression_OrderedCollection, gen_eol_ExpressionRange_CollectionInitialisationExpression, gen_eol_SwitchCaseStatement_Statement, gen_eol_SwitchCaseDefaultStatement_SwitchCaseStatement, gen_eol_SwitchCaseExpressionStatement_SwitchCaseStatement, gen_eol_IfStatement_Statement, gen_eol_TransactionStatement_Statement, gen_eol_ExpressionStatement_Statement, gen_eol_SwitchStatement_Statement, gen_eol_ThrowStatement_Statement, gen_eol_DeleteStatement_Statement, gen_eol_AssignmentStatement_Statement, gen_eol_ForStatement_Statement, gen_eol_WhileStatement_Statement, gen_eol_ReturnStatement_Statement, gen_eol_AnyType_Type, gen_eol_SpecialAssignmentStatement_AssignmentStatement, gen_eol_ContinueStatement_Statement, gen_eol_AbortStatement_Statement, gen_eol_BreakStatement_Statement, gen_eol_BreakAllStatement_Statement, gen_eol_AnnotationStatement_Statement, gen_eol_SimpleAnnotationStatement_AnnotationStatement, gen_eol_ExecutableAnnotationStatement_AnnotationStatement, gen_eol_ModelDeclarationStatement_Statement, gen_eol_VoidType_AnyType, gen_eol_InvalidType_AnyType, gen_eol_CollectionType_AnyType, gen_eol_BagType_CollectionType, gen_eol_OrderedCollectionType_CollectionType, gen_eol_UniqueCollectionType_CollectionType, gen_eol_SetType_UniqueCollectionType, gen_eol_OrderedSetType_UniqueCollectionType, gen_eol_ModelType_AnyType, gen_eol_ModelElementType_AnyType, gen_eol_PseudoType_AnyType, gen_eol_SelfType_PseudoType, gen_eol_SelfContentType_PseudoType, gen_eol_MapType_AnyType, gen_eol_NativeType_AnyType, gen_eol_OrderedSetType_OrderedCollectionType, gen_eol_SequenceType_OrderedCollectionType, gen_eol_PrimitiveType_AnyType, gen_eol_ComparablePrimitiveType_PrimitiveType, gen_eol_SummablePrimitiveType_PrimitiveType, gen_eol_BooleanType_PrimitiveType, gen_eol_RealType_ComparablePrimitiveType, gen_eol_RealType_SummablePrimitiveType, gen_eol_IntegerType_RealType, gen_eol_StringType_ComparablePrimitiveType, gen_eol_StringType_SummablePrimitiveType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)