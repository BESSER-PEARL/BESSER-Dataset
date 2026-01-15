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
eol_TextPosition = Class(name="eol::TextPosition")
eol_TextRegion = Class(name="eol::TextRegion")
eol_IModel = Class(name="eol::IModel")
EOLElement = Class(name="EOLElement")
eol_NameExpression = Class(name="eol::NameExpression")
eol_IPackage = Class(name="eol::IPackage")
eol_StringExpression = Class(name="eol::StringExpression")
eol_Statement = Class(name="eol::Statement", is_abstract=True)
eol_AnnotationBlock = Class(name="eol::AnnotationBlock")
Block = Class(name="Block")
eol_ExpressionOrStatementBlock = Class(name="eol::ExpressionOrStatementBlock")
eol_EOLLibraryModule = Class(name="eol::EOLLibraryModule")
eol_Import = Class(name="eol::Import")
eol_ModelDeclarationStatement = Class(name="eol::ModelDeclarationStatement")
eol_OperationDefinition = Class(name="eol::OperationDefinition")
eol_EOLProgram = Class(name="eol::EOLProgram")
EOLLibraryModule = Class(name="EOLLibraryModule")
eol_Block = Class(name="eol::Block")
eol_OperatorExpression = Class(name="eol::OperatorExpression", is_abstract=True)
Expression = Class(name="Expression")
eol_UnaryOperatorExpression = Class(name="eol::UnaryOperatorExpression", is_abstract=True)
OperatorExpression = Class(name="OperatorExpression")
eol_NotOperatorExpression = Class(name="eol::NotOperatorExpression")
UnaryOperatorExpression = Class(name="UnaryOperatorExpression")
eol_Expression = Class(name="eol::Expression", is_abstract=True)
eol_Type = Class(name="eol::Type")
eol_FormalParameterExpression = Class(name="eol::FormalParameterExpression")
eol_VariableDeclarationExpression = Class(name="eol::VariableDeclarationExpression")
eol_LessThanOrEqualToOperatorExpression = Class(name="eol::LessThanOrEqualToOperatorExpression")
eol_LessThanOperatorExpression = Class(name="eol::LessThanOperatorExpression")
eol_NotEqualsOperatorExpression = Class(name="eol::NotEqualsOperatorExpression")
eol_EqualsOperatorExpression = Class(name="eol::EqualsOperatorExpression")
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
eol_GreaterThanOperatorExpression = Class(name="eol::GreaterThanOperatorExpression")
eol_FOLMethodCallExpression = Class(name="eol::FOLMethodCallExpression")
VariableDeclarationExpression = Class(name="VariableDeclarationExpression")
eol_FeatureCallExpression = Class(name="eol::FeatureCallExpression", is_abstract=True)
eol_MethodCallExpression = Class(name="eol::MethodCallExpression")
FeatureCallExpression = Class(name="FeatureCallExpression")
eol_PropertyCallExpression = Class(name="eol::PropertyCallExpression")
eol_CollectionInitialisationExpression = Class(name="eol::CollectionInitialisationExpression", is_abstract=True)
eol_PrimitiveExpression = Class(name="eol::PrimitiveExpression", is_abstract=True)
eol_ComparableExpression = Class(name="eol::ComparableExpression", is_abstract=True)
PrimitiveExpression = Class(name="PrimitiveExpression")
eol_SummableExpression = Class(name="eol::SummableExpression", is_abstract=True)
ComparableExpression = Class(name="ComparableExpression")
SummableExpression = Class(name="SummableExpression")
eol_BooleanExpression = Class(name="eol::BooleanExpression")
eol_KeyValueExpression = Class(name="eol::KeyValueExpression")
eol_ModelDeclarationParameter = Class(name="eol::ModelDeclarationParameter")
KeyValueExpression = Class(name="KeyValueExpression")
eol_NewExpression = Class(name="eol::NewExpression")
eol_MapExpression = Class(name="eol::MapExpression")
eol_CollectionExpression = Class(name="eol::CollectionExpression", is_abstract=True)
eol_ExpressionRange = Class(name="eol::ExpressionRange")
CollectionInitialisationExpression = Class(name="CollectionInitialisationExpression")
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
eol_SwitchCaseDefaultStatement = Class(name="eol::SwitchCaseDefaultStatement")
eol_SwitchCaseStatement = Class(name="eol::SwitchCaseStatement", is_abstract=True)
SwitchCaseStatement = Class(name="SwitchCaseStatement")
eol_ExpressionList = Class(name="eol::ExpressionList")
eol_TransactionStatement = Class(name="eol::TransactionStatement")
Statement = Class(name="Statement")
eol_ExpressionStatement = Class(name="eol::ExpressionStatement")
eol_SwitchStatement = Class(name="eol::SwitchStatement")
eol_SwitchCaseExpressionStatement = Class(name="eol::SwitchCaseExpressionStatement")
eol_ReturnStatement = Class(name="eol::ReturnStatement")
eol_ThrowStatement = Class(name="eol::ThrowStatement")
eol_DeleteStatement = Class(name="eol::DeleteStatement")
eol_IfStatement = Class(name="eol::IfStatement")
eol_ForStatement = Class(name="eol::ForStatement")
eol_WhileStatement = Class(name="eol::WhileStatement")
eol_ExecutableAnnotationStatement = Class(name="eol::ExecutableAnnotationStatement")
eol_AssignmentStatement = Class(name="eol::AssignmentStatement")
eol_SpecialAssignmentStatement = Class(name="eol::SpecialAssignmentStatement")
AssignmentStatement = Class(name="AssignmentStatement")
eol_ContinueStatement = Class(name="eol::ContinueStatement")
eol_AbortStatement = Class(name="eol::AbortStatement")
eol_BreakStatement = Class(name="eol::BreakStatement")
eol_BreakAllStatement = Class(name="eol::BreakAllStatement")
eol_AnnotationStatement = Class(name="eol::AnnotationStatement")
eol_SimpleAnnotationStatement = Class(name="eol::SimpleAnnotationStatement")
AnnotationStatement = Class(name="AnnotationStatement")
eol_PseudoType = Class(name="eol::PseudoType", is_abstract=True)
eol_SelfType = Class(name="eol::SelfType")
PseudoType = Class(name="PseudoType")
eol_SelfContentType = Class(name="eol::SelfContentType")
eol_SelfInnermostContentType = Class(name="eol::SelfInnermostContentType")
eol_MapType = Class(name="eol::MapType")
eol_AnyType = Class(name="eol::AnyType")
Type = Class(name="Type")
eol_ModelType = Class(name="eol::ModelType")
AnyType = Class(name="AnyType")
eol_ModelElementType = Class(name="eol::ModelElementType")
eol_SummablePrimitiveType = Class(name="eol::SummablePrimitiveType", is_abstract=True)
eol_BooleanType = Class(name="eol::BooleanType")
eol_RealType = Class(name="eol::RealType")
ComparablePrimitiveType = Class(name="ComparablePrimitiveType")
SummablePrimitiveType = Class(name="SummablePrimitiveType")
eol_IntegerType = Class(name="eol::IntegerType")
RealType = Class(name="RealType")
eol_StringType = Class(name="eol::StringType")
eol_NativeType = Class(name="eol::NativeType")
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
OrderedCollectionType = Class(name="OrderedCollectionType")
eol_SequenceType = Class(name="eol::SequenceType")
eol_PrimitiveType = Class(name="eol::PrimitiveType", is_abstract=True)
eol_ComparablePrimitiveType = Class(name="eol::ComparablePrimitiveType", is_abstract=True)
PrimitiveType = Class(name="PrimitiveType")

# eol_EOLElement class attributes and methods
eol_EOLElement_uri: Property = Property(name="uri", type=StringType)
eol_EOLElement.attributes={eol_EOLElement_uri}

# eol_TextPosition class attributes and methods
eol_TextPosition_line: Property = Property(name="line", type=IntegerType)
eol_TextPosition_column: Property = Property(name="column", type=IntegerType)
eol_TextPosition.attributes={eol_TextPosition_line, eol_TextPosition_column}

# eol_TextRegion class attributes and methods

# eol_IModel class attributes and methods
eol_IModel_iMetamodelDriver: Property = Property(name="iMetamodelDriver", type=StringType)
eol_IModel.attributes={eol_IModel_iMetamodelDriver}

# EOLElement class attributes and methods

# eol_NameExpression class attributes and methods
eol_NameExpression_name: Property = Property(name="name", type=StringType)
eol_NameExpression_resolvedContent: Property = Property(name="resolvedContent", type=StringType)
eol_NameExpression_isType: Property = Property(name="isType", type=BooleanType)
eol_NameExpression.attributes={eol_NameExpression_name, eol_NameExpression_resolvedContent, eol_NameExpression_isType}

# eol_IPackage class attributes and methods
eol_IPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
eol_IPackage_iPackageDriver: Property = Property(name="iPackageDriver", type=StringType)
eol_IPackage_name: Property = Property(name="name", type=StringType)
eol_IPackage.attributes={eol_IPackage_name, eol_IPackage_nsPrefix, eol_IPackage_iPackageDriver}

# eol_StringExpression class attributes and methods
eol_StringExpression_value: Property = Property(name="value", type=StringType)
eol_StringExpression.attributes={eol_StringExpression_value}

# eol_Statement class attributes and methods

# eol_AnnotationBlock class attributes and methods

# Block class attributes and methods

# eol_ExpressionOrStatementBlock class attributes and methods

# eol_EOLLibraryModule class attributes and methods
eol_EOLLibraryModule_name: Property = Property(name="name", type=StringType)
eol_EOLLibraryModule.attributes={eol_EOLLibraryModule_name}

# eol_Import class attributes and methods
eol_Import_imported: Property = Property(name="imported", type=StringType)
eol_Import.attributes={eol_Import_imported}

# eol_ModelDeclarationStatement class attributes and methods

# eol_OperationDefinition class attributes and methods

# eol_EOLProgram class attributes and methods

# EOLLibraryModule class attributes and methods

# eol_Block class attributes and methods

# eol_OperatorExpression class attributes and methods

# Expression class attributes and methods

# eol_UnaryOperatorExpression class attributes and methods

# OperatorExpression class attributes and methods

# eol_NotOperatorExpression class attributes and methods

# UnaryOperatorExpression class attributes and methods

# eol_Expression class attributes and methods

# eol_Type class attributes and methods

# eol_FormalParameterExpression class attributes and methods

# eol_VariableDeclarationExpression class attributes and methods
eol_VariableDeclarationExpression_create: Property = Property(name="create", type=BooleanType)
eol_VariableDeclarationExpression.attributes={eol_VariableDeclarationExpression_create}

# eol_LessThanOrEqualToOperatorExpression class attributes and methods

# eol_LessThanOperatorExpression class attributes and methods

# eol_NotEqualsOperatorExpression class attributes and methods

# eol_EqualsOperatorExpression class attributes and methods

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

# eol_GreaterThanOperatorExpression class attributes and methods

# eol_FOLMethodCallExpression class attributes and methods

# VariableDeclarationExpression class attributes and methods

# eol_FeatureCallExpression class attributes and methods
eol_FeatureCallExpression_isArrow: Property = Property(name="isArrow", type=BooleanType)
eol_FeatureCallExpression.attributes={eol_FeatureCallExpression_isArrow}

# eol_MethodCallExpression class attributes and methods

# FeatureCallExpression class attributes and methods

# eol_PropertyCallExpression class attributes and methods
eol_PropertyCallExpression_extended: Property = Property(name="extended", type=BooleanType)
eol_PropertyCallExpression.attributes={eol_PropertyCallExpression_extended}

# eol_CollectionInitialisationExpression class attributes and methods

# eol_PrimitiveExpression class attributes and methods

# eol_ComparableExpression class attributes and methods

# PrimitiveExpression class attributes and methods

# eol_SummableExpression class attributes and methods

# ComparableExpression class attributes and methods

# SummableExpression class attributes and methods

# eol_BooleanExpression class attributes and methods
eol_BooleanExpression_value: Property = Property(name="value", type=BooleanType)
eol_BooleanExpression.attributes={eol_BooleanExpression_value}

# eol_KeyValueExpression class attributes and methods

# eol_ModelDeclarationParameter class attributes and methods

# KeyValueExpression class attributes and methods

# eol_NewExpression class attributes and methods

# eol_MapExpression class attributes and methods

# eol_CollectionExpression class attributes and methods

# eol_ExpressionRange class attributes and methods

# CollectionInitialisationExpression class attributes and methods

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

# eol_SwitchCaseDefaultStatement class attributes and methods

# eol_SwitchCaseStatement class attributes and methods

# SwitchCaseStatement class attributes and methods

# eol_ExpressionList class attributes and methods

# eol_TransactionStatement class attributes and methods

# Statement class attributes and methods

# eol_ExpressionStatement class attributes and methods

# eol_SwitchStatement class attributes and methods

# eol_SwitchCaseExpressionStatement class attributes and methods

# eol_ReturnStatement class attributes and methods

# eol_ThrowStatement class attributes and methods

# eol_DeleteStatement class attributes and methods

# eol_IfStatement class attributes and methods

# eol_ForStatement class attributes and methods

# eol_WhileStatement class attributes and methods

# eol_ExecutableAnnotationStatement class attributes and methods

# eol_AssignmentStatement class attributes and methods

# eol_SpecialAssignmentStatement class attributes and methods

# AssignmentStatement class attributes and methods

# eol_ContinueStatement class attributes and methods

# eol_AbortStatement class attributes and methods

# eol_BreakStatement class attributes and methods

# eol_BreakAllStatement class attributes and methods

# eol_AnnotationStatement class attributes and methods

# eol_SimpleAnnotationStatement class attributes and methods

# AnnotationStatement class attributes and methods

# eol_PseudoType class attributes and methods

# eol_SelfType class attributes and methods

# PseudoType class attributes and methods

# eol_SelfContentType class attributes and methods

# eol_SelfInnermostContentType class attributes and methods

# eol_MapType class attributes and methods

# eol_AnyType class attributes and methods
eol_AnyType_declared: Property = Property(name="declared", type=BooleanType)
eol_AnyType.attributes={eol_AnyType_declared}

# Type class attributes and methods

# eol_ModelType class attributes and methods

# AnyType class attributes and methods

# eol_ModelElementType class attributes and methods
eol_ModelElementType_modelType: Property = Property(name="modelType", type=StringType)
eol_ModelElementType_modelName: Property = Property(name="modelName", type=StringType)
eol_ModelElementType_elementName: Property = Property(name="elementName", type=StringType)
eol_ModelElementType.attributes={eol_ModelElementType_modelType, eol_ModelElementType_elementName, eol_ModelElementType_modelName}

# eol_SummablePrimitiveType class attributes and methods

# eol_BooleanType class attributes and methods

# eol_RealType class attributes and methods

# ComparablePrimitiveType class attributes and methods

# SummablePrimitiveType class attributes and methods

# eol_IntegerType class attributes and methods

# RealType class attributes and methods

# eol_StringType class attributes and methods

# eol_NativeType class attributes and methods

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

# OrderedCollectionType class attributes and methods

# eol_SequenceType class attributes and methods

# eol_PrimitiveType class attributes and methods

# eol_ComparablePrimitiveType class attributes and methods

# PrimitiveType class attributes and methods

# Relationships
subPackages16: BinaryAssociation = BinaryAssociation(
    name="subPackages16",
    ends={
        Property(name="eol_IPackage17", type=eol_IPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IPackage15", type=eol_IPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start18: BinaryAssociation = BinaryAssociation(
    name="start18",
    ends={
        Property(name="eol_TextPosition", type=eol_TextRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TextRegion19", type=eol_TextPosition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end20: BinaryAssociation = BinaryAssociation(
    name="end20",
    ends={
        Property(name="eol_TextPosition22", type=eol_TextRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TextRegion21", type=eol_TextPosition, multiplicity=Multiplicity(0, 1), is_composite=True)
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
name4: BinaryAssociation = BinaryAssociation(
    name="name4",
    ends={
        Property(name="eol_NameExpression", type=eol_IModel, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IModel", type=eol_NameExpression, multiplicity=Multiplicity(1, 1))
    }
)
aliases5: BinaryAssociation = BinaryAssociation(
    name="aliases5",
    ends={
        Property(name="eol_NameExpression7", type=eol_IModel, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IModel6", type=eol_NameExpression, multiplicity=Multiplicity(0, 9999))
    }
)
driver8: BinaryAssociation = BinaryAssociation(
    name="driver8",
    ends={
        Property(name="eol_NameExpression10", type=eol_IModel, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IModel9", type=eol_NameExpression, multiplicity=Multiplicity(1, 1))
    }
)
iPackages11: BinaryAssociation = BinaryAssociation(
    name="iPackages11",
    ends={
        Property(name="eol_IPackage", type=eol_IModel, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IModel12", type=eol_IPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nsURI13: BinaryAssociation = BinaryAssociation(
    name="nsURI13",
    ends={
        Property(name="eol_StringExpression", type=eol_IPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IPackage14", type=eol_StringExpression, multiplicity=Multiplicity(0, 1))
    }
)
importedModule32: BinaryAssociation = BinaryAssociation(
    name="importedModule32",
    ends={
        Property(name="eol_Import33", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="eol_EOLLibraryModule34", type=eol_Import, multiplicity=Multiplicity(1, 1))
    }
)
statements35: BinaryAssociation = BinaryAssociation(
    name="statements35",
    ends={
        Property(name="eol_Statement", type=eol_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Block36", type=eol_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block37: BinaryAssociation = BinaryAssociation(
    name="block37",
    ends={
        Property(name="eol_Block38", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionOrStatementBlock", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports23: BinaryAssociation = BinaryAssociation(
    name="imports23",
    ends={
        Property(name="eol_Import", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLLibraryModule", type=eol_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iModels24: BinaryAssociation = BinaryAssociation(
    name="iModels24",
    ends={
        Property(name="eol_IModel26", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLLibraryModule25", type=eol_IModel, multiplicity=Multiplicity(0, 9999))
    }
)
modelDeclarations27: BinaryAssociation = BinaryAssociation(
    name="modelDeclarations27",
    ends={
        Property(name="eol_ModelDeclarationStatement", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLLibraryModule28", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations29: BinaryAssociation = BinaryAssociation(
    name="operations29",
    ends={
        Property(name="eol_OperationDefinition", type=eol_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLLibraryModule30", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block31: BinaryAssociation = BinaryAssociation(
    name="block31",
    ends={
        Property(name="eol_Block", type=eol_EOLProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EOLProgram", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resolvedType64: BinaryAssociation = BinaryAssociation(
    name="resolvedType64",
    ends={
        Property(name="eol_Type66", type=eol_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_Expression65", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression67: BinaryAssociation = BinaryAssociation(
    name="expression67",
    ends={
        Property(name="eol_Expression68", type=eol_UnaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_UnaryOperatorExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression39: BinaryAssociation = BinaryAssociation(
    name="expression39",
    ends={
        Property(name="eol_Expression", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionOrStatementBlock40", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contextType41: BinaryAssociation = BinaryAssociation(
    name="contextType41",
    ends={
        Property(name="eol_Type", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition42", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType43: BinaryAssociation = BinaryAssociation(
    name="returnType43",
    ends={
        Property(name="eol_Type45", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition44", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotationBlock46: BinaryAssociation = BinaryAssociation(
    name="annotationBlock46",
    ends={
        Property(name="eol_AnnotationBlock", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition47", type=eol_AnnotationBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body48: BinaryAssociation = BinaryAssociation(
    name="body48",
    ends={
        Property(name="eol_Block50", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition49", type=eol_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name51: BinaryAssociation = BinaryAssociation(
    name="name51",
    ends={
        Property(name="eol_NameExpression53", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition52", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters54: BinaryAssociation = BinaryAssociation(
    name="parameters54",
    ends={
        Property(name="eol_FormalParameterExpression", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition55", type=eol_FormalParameterExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
self56: BinaryAssociation = BinaryAssociation(
    name="self56",
    ends={
        Property(name="eol_VariableDeclarationExpression", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition57", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result58: BinaryAssociation = BinaryAssociation(
    name="result58",
    ends={
        Property(name="eol_VariableDeclarationExpression60", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition59", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependingOperationDefinitions62: BinaryAssociation = BinaryAssociation(
    name="dependingOperationDefinitions62",
    ends={
        Property(name="eol_OperationDefinition63", type=eol_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_OperationDefinition61", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
name74: BinaryAssociation = BinaryAssociation(
    name="name74",
    ends={
        Property(name="eol_NameExpression76", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression75", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters77: BinaryAssociation = BinaryAssociation(
    name="parameters77",
    ends={
        Property(name="eol_Expression79", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression78", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs69: BinaryAssociation = BinaryAssociation(
    name="lhs69",
    ends={
        Property(name="eol_Expression70", type=eol_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_BinaryOperatorExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs71: BinaryAssociation = BinaryAssociation(
    name="rhs71",
    ends={
        Property(name="eol_Expression73", type=eol_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_BinaryOperatorExpression72", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property93: BinaryAssociation = BinaryAssociation(
    name="property93",
    ends={
        Property(name="eol_NameExpression94", type=eol_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_PropertyCallExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator95: BinaryAssociation = BinaryAssociation(
    name="iterator95",
    ends={
        Property(name="eol_FormalParameterExpression96", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression", type=eol_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition97: BinaryAssociation = BinaryAssociation(
    name="condition97",
    ends={
        Property(name="eol_Expression99", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression98", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
method100: BinaryAssociation = BinaryAssociation(
    name="method100",
    ends={
        Property(name="eol_NameExpression102", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression101", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
references80: BinaryAssociation = BinaryAssociation(
    name="references80",
    ends={
        Property(name="eol_NameExpression82", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_VariableDeclarationExpression81", type=eol_NameExpression, multiplicity=Multiplicity(0, 9999))
    }
)
target83: BinaryAssociation = BinaryAssociation(
    name="target83",
    ends={
        Property(name="eol_Expression84", type=eol_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FeatureCallExpression", type=eol_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments85: BinaryAssociation = BinaryAssociation(
    name="arguments85",
    ends={
        Property(name="eol_Expression86", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method87: BinaryAssociation = BinaryAssociation(
    name="method87",
    ends={
        Property(name="eol_NameExpression89", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression88", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolvedOperationDefinition90: BinaryAssociation = BinaryAssociation(
    name="resolvedOperationDefinition90",
    ends={
        Property(name="eol_OperationDefinition92", type=eol_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MethodCallExpression91", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 1))
    }
)
parameterList120: BinaryAssociation = BinaryAssociation(
    name="parameterList120",
    ends={
        Property(name="eol_CollectionInitialisationExpression", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression121", type=eol_CollectionInitialisationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resolvedFOLDefinition103: BinaryAssociation = BinaryAssociation(
    name="resolvedFOLDefinition103",
    ends={
        Property(name="eol_OperationDefinition105", type=eol_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_FOLMethodCallExpression104", type=eol_OperationDefinition, multiplicity=Multiplicity(0, 1))
    }
)
key106: BinaryAssociation = BinaryAssociation(
    name="key106",
    ends={
        Property(name="eol_Expression107", type=eol_KeyValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_KeyValueExpression", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value108: BinaryAssociation = BinaryAssociation(
    name="value108",
    ends={
        Property(name="eol_Expression110", type=eol_KeyValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_KeyValueExpression109", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeName111: BinaryAssociation = BinaryAssociation(
    name="typeName111",
    ends={
        Property(name="eol_NameExpression112", type=eol_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NewExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters113: BinaryAssociation = BinaryAssociation(
    name="parameters113",
    ends={
        Property(name="eol_Expression115", type=eol_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NewExpression114", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyValues116: BinaryAssociation = BinaryAssociation(
    name="keyValues116",
    ends={
        Property(name="eol_KeyValueExpression117", type=eol_MapExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapExpression", type=eol_KeyValueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents118: BinaryAssociation = BinaryAssociation(
    name="contents118",
    ends={
        Property(name="eol_Expression119", type=eol_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionExpression", type=eol_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iModel127: BinaryAssociation = BinaryAssociation(
    name="iModel127",
    ends={
        Property(name="eol_IModel129", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression128", type=eol_IModel, multiplicity=Multiplicity(0, 1))
    }
)
model130: BinaryAssociation = BinaryAssociation(
    name="model130",
    ends={
        Property(name="eol_NameExpression132", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression131", type=eol_NameExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start133: BinaryAssociation = BinaryAssociation(
    name="start133",
    ends={
        Property(name="eol_Expression134", type=eol_ExpressionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionRange", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literal122: BinaryAssociation = BinaryAssociation(
    name="literal122",
    ends={
        Property(name="eol_NameExpression123", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumeration124: BinaryAssociation = BinaryAssociation(
    name="enumeration124",
    ends={
        Property(name="eol_NameExpression126", type=eol_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_EnumerationLiteralExpression125", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
default151: BinaryAssociation = BinaryAssociation(
    name="default151",
    ends={
        Property(name="eol_SwitchCaseDefaultStatement", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement152", type=eol_SwitchCaseDefaultStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body153: BinaryAssociation = BinaryAssociation(
    name="body153",
    ends={
        Property(name="eol_ExpressionOrStatementBlock154", type=eol_SwitchCaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchCaseStatement", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression155: BinaryAssociation = BinaryAssociation(
    name="expression155",
    ends={
        Property(name="eol_Expression157", type=eol_SwitchCaseExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchCaseExpressionStatement156", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end135: BinaryAssociation = BinaryAssociation(
    name="end135",
    ends={
        Property(name="eol_Expression137", type=eol_ExpressionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionRange136", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions138: BinaryAssociation = BinaryAssociation(
    name="expressions138",
    ends={
        Property(name="eol_Expression139", type=eol_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionList", type=eol_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
names140: BinaryAssociation = BinaryAssociation(
    name="names140",
    ends={
        Property(name="eol_NameExpression141", type=eol_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TransactionStatement", type=eol_NameExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body142: BinaryAssociation = BinaryAssociation(
    name="body142",
    ends={
        Property(name="eol_ExpressionOrStatementBlock144", type=eol_TransactionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_TransactionStatement143", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression145: BinaryAssociation = BinaryAssociation(
    name="expression145",
    ends={
        Property(name="eol_Expression146", type=eol_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExpressionStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression147: BinaryAssociation = BinaryAssociation(
    name="expression147",
    ends={
        Property(name="eol_Expression148", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases149: BinaryAssociation = BinaryAssociation(
    name="cases149",
    ends={
        Property(name="eol_SwitchCaseExpressionStatement", type=eol_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SwitchStatement150", type=eol_SwitchCaseExpressionStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression179: BinaryAssociation = BinaryAssociation(
    name="expression179",
    ends={
        Property(name="eol_Expression180", type=eol_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ReturnStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression181: BinaryAssociation = BinaryAssociation(
    name="expression181",
    ends={
        Property(name="eol_Expression182", type=eol_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ThrowStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition158: BinaryAssociation = BinaryAssociation(
    name="condition158",
    ends={
        Property(name="eol_Expression159", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifBody160: BinaryAssociation = BinaryAssociation(
    name="ifBody160",
    ends={
        Property(name="eol_ExpressionOrStatementBlock162", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement161", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBody163: BinaryAssociation = BinaryAssociation(
    name="elseBody163",
    ends={
        Property(name="eol_ExpressionOrStatementBlock165", type=eol_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_IfStatement164", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterator166: BinaryAssociation = BinaryAssociation(
    name="iterator166",
    ends={
        Property(name="eol_FormalParameterExpression167", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement", type=eol_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition168: BinaryAssociation = BinaryAssociation(
    name="condition168",
    ends={
        Property(name="eol_Expression170", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement169", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body171: BinaryAssociation = BinaryAssociation(
    name="body171",
    ends={
        Property(name="eol_ExpressionOrStatementBlock173", type=eol_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ForStatement172", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition174: BinaryAssociation = BinaryAssociation(
    name="condition174",
    ends={
        Property(name="eol_Expression175", type=eol_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_WhileStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body176: BinaryAssociation = BinaryAssociation(
    name="body176",
    ends={
        Property(name="eol_ExpressionOrStatementBlock178", type=eol_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_WhileStatement177", type=eol_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression194: BinaryAssociation = BinaryAssociation(
    name="expression194",
    ends={
        Property(name="eol_Expression195", type=eol_ExecutableAnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ExecutableAnnotationStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name196: BinaryAssociation = BinaryAssociation(
    name="name196",
    ends={
        Property(name="eol_VariableDeclarationExpression198", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement197", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
driver199: BinaryAssociation = BinaryAssociation(
    name="driver199",
    ends={
        Property(name="eol_NameExpression201", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement200", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alias202: BinaryAssociation = BinaryAssociation(
    name="alias202",
    ends={
        Property(name="eol_VariableDeclarationExpression204", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement203", type=eol_VariableDeclarationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression183: BinaryAssociation = BinaryAssociation(
    name="expression183",
    ends={
        Property(name="eol_Expression184", type=eol_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_DeleteStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs185: BinaryAssociation = BinaryAssociation(
    name="lhs185",
    ends={
        Property(name="eol_Expression186", type=eol_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AssignmentStatement", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs187: BinaryAssociation = BinaryAssociation(
    name="rhs187",
    ends={
        Property(name="eol_Expression189", type=eol_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AssignmentStatement188", type=eol_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name190: BinaryAssociation = BinaryAssociation(
    name="name190",
    ends={
        Property(name="eol_NameExpression191", type=eol_AnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnnotationStatement", type=eol_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values192: BinaryAssociation = BinaryAssociation(
    name="values192",
    ends={
        Property(name="eol_StringExpression193", type=eol_SimpleAnnotationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_SimpleAnnotationStatement", type=eol_StringExpression, multiplicity=Multiplicity(0, 9999))
    }
)
resolvedIPackage219: BinaryAssociation = BinaryAssociation(
    name="resolvedIPackage219",
    ends={
        Property(name="eol_IPackage221", type=eol_ModelElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelElementType220", type=eol_IPackage, multiplicity=Multiplicity(0, 1))
    }
)
keyType222: BinaryAssociation = BinaryAssociation(
    name="keyType222",
    ends={
        Property(name="eol_AnyType223", type=eol_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapType", type=eol_AnyType, multiplicity=Multiplicity(0, 1))
    }
)
imodel205: BinaryAssociation = BinaryAssociation(
    name="imodel205",
    ends={
        Property(name="eol_IModel207", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement206", type=eol_IModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters208: BinaryAssociation = BinaryAssociation(
    name="parameters208",
    ends={
        Property(name="eol_ModelDeclarationParameter", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelDeclarationStatement209", type=eol_ModelDeclarationParameter, multiplicity=Multiplicity(0, 9999))
    }
)
dynamicTypes210: BinaryAssociation = BinaryAssociation(
    name="dynamicTypes210",
    ends={
        Property(name="eol_Type211", type=eol_AnyType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_AnyType", type=eol_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolvedIModel212: BinaryAssociation = BinaryAssociation(
    name="resolvedIModel212",
    ends={
        Property(name="eol_IModel213", type=eol_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelType", type=eol_IModel, multiplicity=Multiplicity(1, 1))
    }
)
resolvedIModel214: BinaryAssociation = BinaryAssociation(
    name="resolvedIModel214",
    ends={
        Property(name="eol_IModel215", type=eol_ModelElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelElementType", type=eol_IModel, multiplicity=Multiplicity(1, 1))
    }
)
resolvedModelDeclaration216: BinaryAssociation = BinaryAssociation(
    name="resolvedModelDeclaration216",
    ends={
        Property(name="eol_ModelDeclarationStatement218", type=eol_ModelElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_ModelElementType217", type=eol_ModelDeclarationStatement, multiplicity=Multiplicity(1, 1))
    }
)
valueType224: BinaryAssociation = BinaryAssociation(
    name="valueType224",
    ends={
        Property(name="eol_AnyType226", type=eol_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_MapType225", type=eol_AnyType, multiplicity=Multiplicity(0, 1))
    }
)
expression227: BinaryAssociation = BinaryAssociation(
    name="expression227",
    ends={
        Property(name="eol_StringExpression228", type=eol_NativeType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_NativeType", type=eol_StringExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contentType229: BinaryAssociation = BinaryAssociation(
    name="contentType229",
    ends={
        Property(name="eol_Type230", type=eol_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_CollectionType", type=eol_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_eol_TextRegion_EOLElement = Generalization(general=EOLElement, specific=eol_TextRegion)
gen_eol_IModel_EOLElement = Generalization(general=EOLElement, specific=eol_IModel)
gen_eol_IPackage_EOLElement = Generalization(general=EOLElement, specific=eol_IPackage)
gen_eol_Block_EOLElement = Generalization(general=EOLElement, specific=eol_Block)
gen_eol_AnnotationBlock_Block = Generalization(general=Block, specific=eol_AnnotationBlock)
gen_eol_ExpressionOrStatementBlock_EOLElement = Generalization(general=EOLElement, specific=eol_ExpressionOrStatementBlock)
gen_eol_TextPosition_EOLElement = Generalization(general=EOLElement, specific=eol_TextPosition)
gen_eol_EOLLibraryModule_EOLElement = Generalization(general=EOLElement, specific=eol_EOLLibraryModule)
gen_eol_EOLProgram_EOLLibraryModule = Generalization(general=EOLLibraryModule, specific=eol_EOLProgram)
gen_eol_Import_EOLElement = Generalization(general=EOLElement, specific=eol_Import)
gen_eol_Expression_EOLElement = Generalization(general=EOLElement, specific=eol_Expression)
gen_eol_OperatorExpression_Expression = Generalization(general=Expression, specific=eol_OperatorExpression)
gen_eol_UnaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=eol_UnaryOperatorExpression)
gen_eol_OperationDefinition_EOLElement = Generalization(general=EOLElement, specific=eol_OperationDefinition)
gen_eol_LessThanOrEqualToOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_LessThanOrEqualToOperatorExpression)
gen_eol_LessThanOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_LessThanOperatorExpression)
gen_eol_NotEqualsOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_NotEqualsOperatorExpression)
gen_eol_EqualsOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_EqualsOperatorExpression)
gen_eol_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=eol_VariableDeclarationExpression)
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
gen_eol_GreaterThanOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_GreaterThanOperatorExpression)
gen_eol_FOLMethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_FOLMethodCallExpression)
gen_eol_FormalParameterExpression_VariableDeclarationExpression = Generalization(general=VariableDeclarationExpression, specific=eol_FormalParameterExpression)
gen_eol_NameExpression_Expression = Generalization(general=Expression, specific=eol_NameExpression)
gen_eol_FeatureCallExpression_Expression = Generalization(general=Expression, specific=eol_FeatureCallExpression)
gen_eol_MethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_MethodCallExpression)
gen_eol_PropertyCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_PropertyCallExpression)
gen_eol_PrimitiveExpression_Expression = Generalization(general=Expression, specific=eol_PrimitiveExpression)
gen_eol_ComparableExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_ComparableExpression)
gen_eol_SummableExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_SummableExpression)
gen_eol_StringExpression_ComparableExpression = Generalization(general=ComparableExpression, specific=eol_StringExpression)
gen_eol_StringExpression_SummableExpression = Generalization(general=SummableExpression, specific=eol_StringExpression)
gen_eol_KeyValueExpression_Expression = Generalization(general=Expression, specific=eol_KeyValueExpression)
gen_eol_ModelDeclarationParameter_KeyValueExpression = Generalization(general=KeyValueExpression, specific=eol_ModelDeclarationParameter)
gen_eol_NewExpression_Expression = Generalization(general=Expression, specific=eol_NewExpression)
gen_eol_MapExpression_Expression = Generalization(general=Expression, specific=eol_MapExpression)
gen_eol_CollectionExpression_Expression = Generalization(general=Expression, specific=eol_CollectionExpression)
gen_eol_CollectionInitialisationExpression_Expression = Generalization(general=Expression, specific=eol_CollectionInitialisationExpression)
gen_eol_ExpressionRange_CollectionInitialisationExpression = Generalization(general=CollectionInitialisationExpression, specific=eol_ExpressionRange)
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
gen_eol_SwitchCaseStatement_Statement = Generalization(general=Statement, specific=eol_SwitchCaseStatement)
gen_eol_SwitchCaseDefaultStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_SwitchCaseDefaultStatement)
gen_eol_SwitchCaseExpressionStatement_SwitchCaseStatement = Generalization(general=SwitchCaseStatement, specific=eol_SwitchCaseExpressionStatement)
gen_eol_ExpressionList_CollectionInitialisationExpression = Generalization(general=CollectionInitialisationExpression, specific=eol_ExpressionList)
gen_eol_Statement_EOLElement = Generalization(general=EOLElement, specific=eol_Statement)
gen_eol_TransactionStatement_Statement = Generalization(general=Statement, specific=eol_TransactionStatement)
gen_eol_ExpressionStatement_Statement = Generalization(general=Statement, specific=eol_ExpressionStatement)
gen_eol_SwitchStatement_Statement = Generalization(general=Statement, specific=eol_SwitchStatement)
gen_eol_ReturnStatement_Statement = Generalization(general=Statement, specific=eol_ReturnStatement)
gen_eol_ThrowStatement_Statement = Generalization(general=Statement, specific=eol_ThrowStatement)
gen_eol_DeleteStatement_Statement = Generalization(general=Statement, specific=eol_DeleteStatement)
gen_eol_IfStatement_Statement = Generalization(general=Statement, specific=eol_IfStatement)
gen_eol_ForStatement_Statement = Generalization(general=Statement, specific=eol_ForStatement)
gen_eol_WhileStatement_Statement = Generalization(general=Statement, specific=eol_WhileStatement)
gen_eol_ExecutableAnnotationStatement_AnnotationStatement = Generalization(general=AnnotationStatement, specific=eol_ExecutableAnnotationStatement)
gen_eol_ModelDeclarationStatement_Statement = Generalization(general=Statement, specific=eol_ModelDeclarationStatement)
gen_eol_AssignmentStatement_Statement = Generalization(general=Statement, specific=eol_AssignmentStatement)
gen_eol_SpecialAssignmentStatement_AssignmentStatement = Generalization(general=AssignmentStatement, specific=eol_SpecialAssignmentStatement)
gen_eol_ContinueStatement_Statement = Generalization(general=Statement, specific=eol_ContinueStatement)
gen_eol_AbortStatement_Statement = Generalization(general=Statement, specific=eol_AbortStatement)
gen_eol_BreakStatement_Statement = Generalization(general=Statement, specific=eol_BreakStatement)
gen_eol_BreakAllStatement_Statement = Generalization(general=Statement, specific=eol_BreakAllStatement)
gen_eol_AnnotationStatement_Statement = Generalization(general=Statement, specific=eol_AnnotationStatement)
gen_eol_SimpleAnnotationStatement_AnnotationStatement = Generalization(general=AnnotationStatement, specific=eol_SimpleAnnotationStatement)
gen_eol_PseudoType_AnyType = Generalization(general=AnyType, specific=eol_PseudoType)
gen_eol_SelfType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfType)
gen_eol_SelfContentType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfContentType)
gen_eol_SelfInnermostContentType_PseudoType = Generalization(general=PseudoType, specific=eol_SelfInnermostContentType)
gen_eol_MapType_AnyType = Generalization(general=AnyType, specific=eol_MapType)
gen_eol_Type_EOLElement = Generalization(general=EOLElement, specific=eol_Type)
gen_eol_AnyType_Type = Generalization(general=Type, specific=eol_AnyType)
gen_eol_ModelType_AnyType = Generalization(general=AnyType, specific=eol_ModelType)
gen_eol_ModelElementType_AnyType = Generalization(general=AnyType, specific=eol_ModelElementType)
gen_eol_SummablePrimitiveType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_SummablePrimitiveType)
gen_eol_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_BooleanType)
gen_eol_RealType_ComparablePrimitiveType = Generalization(general=ComparablePrimitiveType, specific=eol_RealType)
gen_eol_RealType_SummablePrimitiveType = Generalization(general=SummablePrimitiveType, specific=eol_RealType)
gen_eol_IntegerType_RealType = Generalization(general=RealType, specific=eol_IntegerType)
gen_eol_StringType_ComparablePrimitiveType = Generalization(general=ComparablePrimitiveType, specific=eol_StringType)
gen_eol_StringType_SummablePrimitiveType = Generalization(general=SummablePrimitiveType, specific=eol_StringType)
gen_eol_NativeType_AnyType = Generalization(general=AnyType, specific=eol_NativeType)
gen_eol_VoidType_AnyType = Generalization(general=AnyType, specific=eol_VoidType)
gen_eol_InvalidType_AnyType = Generalization(general=AnyType, specific=eol_InvalidType)
gen_eol_CollectionType_AnyType = Generalization(general=AnyType, specific=eol_CollectionType)
gen_eol_BagType_CollectionType = Generalization(general=CollectionType, specific=eol_BagType)
gen_eol_OrderedCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_OrderedCollectionType)
gen_eol_UniqueCollectionType_CollectionType = Generalization(general=CollectionType, specific=eol_UniqueCollectionType)
gen_eol_SetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_SetType)
gen_eol_OrderedSetType_UniqueCollectionType = Generalization(general=UniqueCollectionType, specific=eol_OrderedSetType)
gen_eol_OrderedSetType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_OrderedSetType)
gen_eol_SequenceType_OrderedCollectionType = Generalization(general=OrderedCollectionType, specific=eol_SequenceType)
gen_eol_PrimitiveType_AnyType = Generalization(general=AnyType, specific=eol_PrimitiveType)
gen_eol_ComparablePrimitiveType_PrimitiveType = Generalization(general=PrimitiveType, specific=eol_ComparablePrimitiveType)

# Domain Model
domain_model = DomainModel(
    name="eol",
    types={eol_EOLElement, eol_TextPosition, eol_TextRegion, eol_IModel, EOLElement, eol_NameExpression, eol_IPackage, eol_StringExpression, eol_Statement, eol_AnnotationBlock, Block, eol_ExpressionOrStatementBlock, eol_EOLLibraryModule, eol_Import, eol_ModelDeclarationStatement, eol_OperationDefinition, eol_EOLProgram, EOLLibraryModule, eol_Block, eol_OperatorExpression, Expression, eol_UnaryOperatorExpression, OperatorExpression, eol_NotOperatorExpression, UnaryOperatorExpression, eol_Expression, eol_Type, eol_FormalParameterExpression, eol_VariableDeclarationExpression, eol_LessThanOrEqualToOperatorExpression, eol_LessThanOperatorExpression, eol_NotEqualsOperatorExpression, eol_EqualsOperatorExpression, eol_NegativeOperatorExpression, eol_BinaryOperatorExpression, eol_LogicalOperatorExpression, BinaryOperatorExpression, eol_AndOperatorExpression, LogicalOperatorExpression, eol_XorOperatorExpression, eol_OrOperatorExpression, eol_ImpliesOperatorExpression, eol_ArithmeticOperatorExpression, eol_DivideOperatorExpression, ArithmeticOperatorExpression, eol_MultiplyOperatorExpression, eol_MinusOperatorExpression, eol_PlusOperatorExpression, eol_ComparisonOperatorExpression, eol_GreaterThanOrEqualToOperatorExpression, ComparisonOperatorExpression, eol_GreaterThanOperatorExpression, eol_FOLMethodCallExpression, VariableDeclarationExpression, eol_FeatureCallExpression, eol_MethodCallExpression, FeatureCallExpression, eol_PropertyCallExpression, eol_CollectionInitialisationExpression, eol_PrimitiveExpression, eol_ComparableExpression, PrimitiveExpression, eol_SummableExpression, ComparableExpression, SummableExpression, eol_BooleanExpression, eol_KeyValueExpression, eol_ModelDeclarationParameter, KeyValueExpression, eol_NewExpression, eol_MapExpression, eol_CollectionExpression, eol_ExpressionRange, CollectionInitialisationExpression, eol_RealExpression, eol_IntegerExpression, eol_BagExpression, CollectionExpression, eol_SetExpression, UniqueCollection, eol_OrderedSetExpression, OrderedCollection, eol_SequenceExpression, eol_OrderedCollection, eol_UniqueCollection, eol_EnumerationLiteralExpression, eol_SwitchCaseDefaultStatement, eol_SwitchCaseStatement, SwitchCaseStatement, eol_ExpressionList, eol_TransactionStatement, Statement, eol_ExpressionStatement, eol_SwitchStatement, eol_SwitchCaseExpressionStatement, eol_ReturnStatement, eol_ThrowStatement, eol_DeleteStatement, eol_IfStatement, eol_ForStatement, eol_WhileStatement, eol_ExecutableAnnotationStatement, eol_AssignmentStatement, eol_SpecialAssignmentStatement, AssignmentStatement, eol_ContinueStatement, eol_AbortStatement, eol_BreakStatement, eol_BreakAllStatement, eol_AnnotationStatement, eol_SimpleAnnotationStatement, AnnotationStatement, eol_PseudoType, eol_SelfType, PseudoType, eol_SelfContentType, eol_SelfInnermostContentType, eol_MapType, eol_AnyType, Type, eol_ModelType, AnyType, eol_ModelElementType, eol_SummablePrimitiveType, eol_BooleanType, eol_RealType, ComparablePrimitiveType, SummablePrimitiveType, eol_IntegerType, RealType, eol_StringType, eol_NativeType, eol_VoidType, eol_InvalidType, eol_CollectionType, eol_BagType, CollectionType, eol_OrderedCollectionType, eol_UniqueCollectionType, eol_SetType, UniqueCollectionType, eol_OrderedSetType, OrderedCollectionType, eol_SequenceType, eol_PrimitiveType, eol_ComparablePrimitiveType, PrimitiveType},
    associations={subPackages16, start18, end20, container1, region2, name4, aliases5, driver8, iPackages11, nsURI13, importedModule32, statements35, block37, imports23, iModels24, modelDeclarations27, operations29, block31, resolvedType64, expression67, expression39, contextType41, returnType43, annotationBlock46, body48, name51, parameters54, self56, result58, dependingOperationDefinitions62, name74, parameters77, lhs69, rhs71, property93, iterator95, condition97, method100, references80, target83, arguments85, method87, resolvedOperationDefinition90, parameterList120, resolvedFOLDefinition103, key106, value108, typeName111, parameters113, keyValues116, contents118, iModel127, model130, start133, literal122, enumeration124, default151, body153, expression155, end135, expressions138, names140, body142, expression145, expression147, cases149, expression179, expression181, condition158, ifBody160, elseBody163, iterator166, condition168, body171, condition174, body176, expression194, name196, driver199, alias202, expression183, lhs185, rhs187, name190, values192, resolvedIPackage219, keyType222, imodel205, parameters208, dynamicTypes210, resolvedIModel212, resolvedIModel214, resolvedModelDeclaration216, valueType224, expression227, contentType229},
    generalizations={gen_eol_TextRegion_EOLElement, gen_eol_IModel_EOLElement, gen_eol_IPackage_EOLElement, gen_eol_Block_EOLElement, gen_eol_AnnotationBlock_Block, gen_eol_ExpressionOrStatementBlock_EOLElement, gen_eol_TextPosition_EOLElement, gen_eol_EOLLibraryModule_EOLElement, gen_eol_EOLProgram_EOLLibraryModule, gen_eol_Import_EOLElement, gen_eol_Expression_EOLElement, gen_eol_OperatorExpression_Expression, gen_eol_UnaryOperatorExpression_OperatorExpression, gen_eol_OperationDefinition_EOLElement, gen_eol_LessThanOrEqualToOperatorExpression_ComparisonOperatorExpression, gen_eol_LessThanOperatorExpression_ComparisonOperatorExpression, gen_eol_NotEqualsOperatorExpression_ComparisonOperatorExpression, gen_eol_EqualsOperatorExpression_ComparisonOperatorExpression, gen_eol_VariableDeclarationExpression_Expression, gen_eol_NotOperatorExpression_UnaryOperatorExpression, gen_eol_NegativeOperatorExpression_UnaryOperatorExpression, gen_eol_BinaryOperatorExpression_OperatorExpression, gen_eol_LogicalOperatorExpression_BinaryOperatorExpression, gen_eol_AndOperatorExpression_LogicalOperatorExpression, gen_eol_XorOperatorExpression_LogicalOperatorExpression, gen_eol_OrOperatorExpression_LogicalOperatorExpression, gen_eol_ImpliesOperatorExpression_LogicalOperatorExpression, gen_eol_ArithmeticOperatorExpression_BinaryOperatorExpression, gen_eol_DivideOperatorExpression_ArithmeticOperatorExpression, gen_eol_MultiplyOperatorExpression_ArithmeticOperatorExpression, gen_eol_MinusOperatorExpression_ArithmeticOperatorExpression, gen_eol_PlusOperatorExpression_ArithmeticOperatorExpression, gen_eol_ComparisonOperatorExpression_BinaryOperatorExpression, gen_eol_GreaterThanOrEqualToOperatorExpression_ComparisonOperatorExpression, gen_eol_GreaterThanOperatorExpression_ComparisonOperatorExpression, gen_eol_FOLMethodCallExpression_FeatureCallExpression, gen_eol_FormalParameterExpression_VariableDeclarationExpression, gen_eol_NameExpression_Expression, gen_eol_FeatureCallExpression_Expression, gen_eol_MethodCallExpression_FeatureCallExpression, gen_eol_PropertyCallExpression_FeatureCallExpression, gen_eol_PrimitiveExpression_Expression, gen_eol_ComparableExpression_PrimitiveExpression, gen_eol_SummableExpression_PrimitiveExpression, gen_eol_StringExpression_ComparableExpression, gen_eol_StringExpression_SummableExpression, gen_eol_KeyValueExpression_Expression, gen_eol_ModelDeclarationParameter_KeyValueExpression, gen_eol_NewExpression_Expression, gen_eol_MapExpression_Expression, gen_eol_CollectionExpression_Expression, gen_eol_CollectionInitialisationExpression_Expression, gen_eol_ExpressionRange_CollectionInitialisationExpression, gen_eol_BooleanExpression_PrimitiveExpression, gen_eol_RealExpression_ComparableExpression, gen_eol_RealExpression_SummableExpression, gen_eol_IntegerExpression_ComparableExpression, gen_eol_IntegerExpression_SummableExpression, gen_eol_BagExpression_CollectionExpression, gen_eol_SetExpression_UniqueCollection, gen_eol_OrderedSetExpression_OrderedCollection, gen_eol_OrderedSetExpression_UniqueCollection, gen_eol_SequenceExpression_OrderedCollection, gen_eol_OrderedCollection_CollectionExpression, gen_eol_UniqueCollection_CollectionExpression, gen_eol_EnumerationLiteralExpression_Expression, gen_eol_SwitchCaseStatement_Statement, gen_eol_SwitchCaseDefaultStatement_SwitchCaseStatement, gen_eol_SwitchCaseExpressionStatement_SwitchCaseStatement, gen_eol_ExpressionList_CollectionInitialisationExpression, gen_eol_Statement_EOLElement, gen_eol_TransactionStatement_Statement, gen_eol_ExpressionStatement_Statement, gen_eol_SwitchStatement_Statement, gen_eol_ReturnStatement_Statement, gen_eol_ThrowStatement_Statement, gen_eol_DeleteStatement_Statement, gen_eol_IfStatement_Statement, gen_eol_ForStatement_Statement, gen_eol_WhileStatement_Statement, gen_eol_ExecutableAnnotationStatement_AnnotationStatement, gen_eol_ModelDeclarationStatement_Statement, gen_eol_AssignmentStatement_Statement, gen_eol_SpecialAssignmentStatement_AssignmentStatement, gen_eol_ContinueStatement_Statement, gen_eol_AbortStatement_Statement, gen_eol_BreakStatement_Statement, gen_eol_BreakAllStatement_Statement, gen_eol_AnnotationStatement_Statement, gen_eol_SimpleAnnotationStatement_AnnotationStatement, gen_eol_PseudoType_AnyType, gen_eol_SelfType_PseudoType, gen_eol_SelfContentType_PseudoType, gen_eol_SelfInnermostContentType_PseudoType, gen_eol_MapType_AnyType, gen_eol_Type_EOLElement, gen_eol_AnyType_Type, gen_eol_ModelType_AnyType, gen_eol_ModelElementType_AnyType, gen_eol_SummablePrimitiveType_PrimitiveType, gen_eol_BooleanType_PrimitiveType, gen_eol_RealType_ComparablePrimitiveType, gen_eol_RealType_SummablePrimitiveType, gen_eol_IntegerType_RealType, gen_eol_StringType_ComparablePrimitiveType, gen_eol_StringType_SummablePrimitiveType, gen_eol_NativeType_AnyType, gen_eol_VoidType_AnyType, gen_eol_InvalidType_AnyType, gen_eol_CollectionType_AnyType, gen_eol_BagType_CollectionType, gen_eol_OrderedCollectionType_CollectionType, gen_eol_UniqueCollectionType_CollectionType, gen_eol_SetType_UniqueCollectionType, gen_eol_OrderedSetType_UniqueCollectionType, gen_eol_OrderedSetType_OrderedCollectionType, gen_eol_SequenceType_OrderedCollectionType, gen_eol_PrimitiveType_AnyType, gen_eol_ComparablePrimitiveType_PrimitiveType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)