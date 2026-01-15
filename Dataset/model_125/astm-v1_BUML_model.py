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
astm_OtherSyntaxObject = Class(name="astm::OtherSyntaxObject", is_abstract=True)
astm_StorageSpecification = Class(name="astm::StorageSpecification", is_abstract=True)
astm_DataType = Class(name="astm::DataType", is_abstract=True)
astm_AccessKind = Class(name="astm::AccessKind")
astm_UnaryOperator = Class(name="astm::UnaryOperator", is_abstract=True)
astm_BinaryOperator = Class(name="astm::BinaryOperator", is_abstract=True)
astm_ActualParameter = Class(name="astm::ActualParameter", is_abstract=True)
astm_SourceFile = Class(name="astm::SourceFile")
GASTMSourceObject = Class(name="GASTMSourceObject")
astm_SourceLocation = Class(name="astm::SourceLocation")
astm_GASTMObject = Class(name="astm::GASTMObject")
astm_GASTMSourceObject = Class(name="astm::GASTMSourceObject", is_abstract=True)
astm_GASTMSemanticObject = Class(name="astm::GASTMSemanticObject", is_abstract=True)
CompilationUnit = Class(name="CompilationUnit")
GlobalScope = Class(name="GlobalScope")
astm_Scope = Class(name="astm::Scope")
DefinitionObject = Class(name="DefinitionObject")
Scope = Class(name="Scope")
astm_GASTMSyntaxObject = Class(name="astm::GASTMSyntaxObject", is_abstract=True)
GASTMObject = Class(name="GASTMObject")
SourceFile = Class(name="SourceFile")
astm_Project = Class(name="astm::Project")
GASTMSemanticObject = Class(name="GASTMSemanticObject")
AnnotationExpression = Class(name="AnnotationExpression")
astm_CompilationUnit = Class(name="astm::CompilationUnit")
OtherSyntaxObject = Class(name="OtherSyntaxObject")
ProgramScope = Class(name="ProgramScope")
astm_Name = Class(name="astm::Name")
astm_DeclarationOrDefinition = Class(name="astm::DeclarationOrDefinition", is_abstract=True)
SourceLocation = Class(name="SourceLocation")
PreprocessorElement = Class(name="PreprocessorElement")
astm_Definition = Class(name="astm::Definition", is_abstract=True)
DeclarationOrDefinition = Class(name="DeclarationOrDefinition")
Name = Class(name="Name")
TypeReference = Class(name="TypeReference")
astm_Declaration = Class(name="astm::Declaration", is_abstract=True)
Definition = Class(name="Definition")
astm_VariableDeclaration = Class(name="astm::VariableDeclaration")
astm_FunctionDefinition = Class(name="astm::FunctionDefinition")
FormalParameterDefinition = Class(name="FormalParameterDefinition")
Statement = Class(name="Statement")
FunctionScope = Class(name="FunctionScope")
astm_FunctionDeclaration = Class(name="astm::FunctionDeclaration")
Declaration = Class(name="Declaration")
FormalParameterDeclaration = Class(name="FormalParameterDeclaration")
FunctionMemberAttributes = Class(name="FunctionMemberAttributes")
VirtualSpecification = Class(name="VirtualSpecification")
astm_EntryDefinition = Class(name="astm::EntryDefinition")
astm_DataDefinition = Class(name="astm::DataDefinition", is_abstract=True)
Expression = Class(name="Expression")
astm_FunctionMemberAttributes = Class(name="astm::FunctionMemberAttributes")
astm_TypeDefinition = Class(name="astm::TypeDefinition")
astm_NamedTypeDefinition = Class(name="astm::NamedTypeDefinition")
TypeDefinition = Class(name="TypeDefinition")
NamedType = Class(name="NamedType")
astm_AggregateTypeDefinition = Class(name="astm::AggregateTypeDefinition")
AggregateType = Class(name="AggregateType")
astm_NameSpaceDefinition = Class(name="astm::NameSpaceDefinition")
astm_BitFieldDefinition = Class(name="astm::BitFieldDefinition")
DataDefinition = Class(name="DataDefinition")
astm_EnumLiteralDefinition = Class(name="astm::EnumLiteralDefinition")
astm_LabelDefinition = Class(name="astm::LabelDefinition")
LabelType = Class(name="LabelType")
astm_IncludeUnit = Class(name="astm::IncludeUnit")
astm_MacroCall = Class(name="astm::MacroCall")
MacroDefinition = Class(name="MacroDefinition")
astm_MacroDefinition = Class(name="astm::MacroDefinition")
NameSpaceType = Class(name="NameSpaceType")
astm_Type = Class(name="astm::Type", is_abstract=True)
GASTMSyntaxObject = Class(name="GASTMSyntaxObject")
astm_PrimitiveType = Class(name="astm::PrimitiveType", is_abstract=True)
DataType = Class(name="DataType")
astm_EnumType = Class(name="astm::EnumType")
EnumLiteralDefinition = Class(name="EnumLiteralDefinition")
astm_ConstructedType = Class(name="astm::ConstructedType", is_abstract=True)
astm_AggregateType = Class(name="astm::AggregateType", is_abstract=True)
astm_Comment = Class(name="astm::Comment")
astm_ArrayType = Class(name="astm::ArrayType")
ConstructedType = Class(name="ConstructedType")
Dimension = Class(name="Dimension")
astm_Dimension = Class(name="astm::Dimension")
astm_FunctionType = Class(name="astm::FunctionType")
Type = Class(name="Type")
AggregateScope = Class(name="AggregateScope")
astm_FormalParameterType = Class(name="astm::FormalParameterType", is_abstract=True)
astm_NamedType = Class(name="astm::NamedType")
astm_ClassType = Class(name="astm::ClassType")
DerivesFrom = Class(name="DerivesFrom")
astm_DerivesFrom = Class(name="astm::DerivesFrom")
FormalParameterType = Class(name="FormalParameterType")
astm_NamedTypeReference = Class(name="astm::NamedTypeReference")
astm_DeleteStatement = Class(name="astm::DeleteStatement")
astm_UnnamedTypeReference = Class(name="astm::UnnamedTypeReference")
astm_JumpStatement = Class(name="astm::JumpStatement")
astm_BreakStatement = Class(name="astm::BreakStatement")
LabelAccess = Class(name="LabelAccess")
astm_ContinueStatement = Class(name="astm::ContinueStatement")
astm_LabeledStatement = Class(name="astm::LabeledStatement")
astm_DeclarationOrDefinitionStatement = Class(name="astm::DeclarationOrDefinitionStatement")
astm_ExpressionStatement = Class(name="astm::ExpressionStatement")
astm_BlockStatement = Class(name="astm::BlockStatement")
BlockScope = Class(name="BlockScope")
astm_EmptyStatement = Class(name="astm::EmptyStatement")
astm_IfStatement = Class(name="astm::IfStatement")
LabelDefinition = Class(name="LabelDefinition")
astm_SwitchStatement = Class(name="astm::SwitchStatement")
SwitchCase = Class(name="SwitchCase")
astm_SwitchCase = Class(name="astm::SwitchCase")
astm_CaseBlock = Class(name="astm::CaseBlock")
astm_ReturnStatement = Class(name="astm::ReturnStatement")
astm_LoopStatement = Class(name="astm::LoopStatement")
astm_ForStatement = Class(name="astm::ForStatement", is_abstract=True)
LoopStatement = Class(name="LoopStatement")
astm_TryStatement = Class(name="astm::TryStatement")
CatchBlock = Class(name="CatchBlock")
astm_CatchBlock = Class(name="astm::CatchBlock")
astm_TypesCatchBlock = Class(name="astm::TypesCatchBlock")
astm_VariableCatchBlock = Class(name="astm::VariableCatchBlock")
astm_ThrowStatement = Class(name="astm::ThrowStatement")
astm_Expression = Class(name="astm::Expression", is_abstract=True)
astm_NameReference = Class(name="astm::NameReference", is_abstract=True)
astm_ArrayAccess = Class(name="astm::ArrayAccess")
astm_QualifiedIdentifierReference = Class(name="astm::QualifiedIdentifierReference", is_abstract=True)
NameReference = Class(name="NameReference")
IdentifierReference = Class(name="IdentifierReference")
astm_TypeQualifiedIdentifierReference = Class(name="astm::TypeQualifiedIdentifierReference")
astm_Literal = Class(name="astm::Literal")
astm_CastExpression = Class(name="astm::CastExpression")
astm_UnaryExpression = Class(name="astm::UnaryExpression")
astm_BinaryExpression = Class(name="astm::BinaryExpression")
astm_OperatorAssign = Class(name="astm::OperatorAssign")
BinaryOperator = Class(name="BinaryOperator")
astm_ConditionalExpression = Class(name="astm::ConditionalExpression")
astm_RangeExpression = Class(name="astm::RangeExpression")
astm_NewExpression = Class(name="astm::NewExpression")
astm_FunctionCallExpression = Class(name="astm::FunctionCallExpression")
ActualParameter = Class(name="ActualParameter")
astm_ActualParameterExpression = Class(name="astm::ActualParameterExpression")
astm_LabelAccess = Class(name="astm::LabelAccess")
astm_AnnotationExpression = Class(name="astm::AnnotationExpression")
astm_GlobalScope = Class(name="astm::GlobalScope")
astm_PreprocessorElement = Class(name="astm::PreprocessorElement", is_abstract=True)
astm_DefinitionObject = Class(name="astm::DefinitionObject", is_abstract=True)
astm_ProgramScope = Class(name="astm::ProgramScope")
astm_TypeReference = Class(name="astm::TypeReference", is_abstract=True)
astm_Statement = Class(name="astm::Statement", is_abstract=True)
astm_FunctionScope = Class(name="astm::FunctionScope")
astm_NameSpaceType = Class(name="astm::NameSpaceType")
astm_LabelType = Class(name="astm::LabelType")
astm_AggregateScope = Class(name="astm::AggregateScope")
astm_BlockScope = Class(name="astm::BlockScope")
astm_IdentifierReference = Class(name="astm::IdentifierReference")
astm_VirtualSpecification = Class(name="astm::VirtualSpecification", is_abstract=True)
astm_Float = Class(name="astm::Float")
astm_FormalParameterDefinition = Class(name="astm::FormalParameterDefinition")
astm_FormalParameterDeclaration = Class(name="astm::FormalParameterDeclaration")
astm_Double = Class(name="astm::Double")
astm_VariableDefinition = Class(name="astm::VariableDefinition")
astm_FunctionMemberAttribute = Class(name="astm::FunctionMemberAttribute")
astm_External = Class(name="astm::External")
StorageSpecification = Class(name="StorageSpecification")
astm_FunctionPersistent = Class(name="astm::FunctionPersistent")
astm_FileLocal = Class(name="astm::FileLocal")
astm_PerClassMember = Class(name="astm::PerClassMember")
astm_NoDef = Class(name="astm::NoDef")
astm_Virtual = Class(name="astm::Virtual")
astm_PureVirtual = Class(name="astm::PureVirtual")
astm_NonVirtual = Class(name="astm::NonVirtual")
astm_ExceptionType = Class(name="astm::ExceptionType")
astm_Void = Class(name="astm::Void")
PrimitiveType = Class(name="PrimitiveType")
astm_Byte = Class(name="astm::Byte")
astm_ShortInteger = Class(name="astm::ShortInteger")
astm_Integer = Class(name="astm::Integer")
astm_LongInteger = Class(name="astm::LongInteger")
astm_TerminateStatement = Class(name="astm::TerminateStatement")
astm_LongDouble = Class(name="astm::LongDouble")
astm_Character = Class(name="astm::Character")
astm_String = Class(name="astm::String")
astm_Boolean = Class(name="astm::Boolean")
astm_WideCharacter = Class(name="astm::WideCharacter")
astm_CollectionType = Class(name="astm::CollectionType")
astm_PointerType = Class(name="astm::PointerType")
astm_ReferenceType = Class(name="astm::ReferenceType")
astm_RangeType = Class(name="astm::RangeType")
astm_StructureType = Class(name="astm::StructureType")
astm_UnionType = Class(name="astm::UnionType")
astm_AnnotationType = Class(name="astm::AnnotationType")
astm_ByValueFormalParameterType = Class(name="astm::ByValueFormalParameterType")
astm_ByReferenceFormalParameterType = Class(name="astm::ByReferenceFormalParameterType")
astm_Public = Class(name="astm::Public")
AccessKind = Class(name="AccessKind")
astm_Protected = Class(name="astm::Protected")
astm_Private = Class(name="astm::Private")
astm_BitNot = Class(name="astm::BitNot")
astm_AddressOf = Class(name="astm::AddressOf")
astm_DefaultBlock = Class(name="astm::DefaultBlock")
astm_WhileStatement = Class(name="astm::WhileStatement")
astm_DoWhileStatement = Class(name="astm::DoWhileStatement")
astm_ForCheckBeforeStatement = Class(name="astm::ForCheckBeforeStatement")
ForStatement = Class(name="ForStatement")
astm_ForCheckAfterStatement = Class(name="astm::ForCheckAfterStatement")
astm_AggregateExpression = Class(name="astm::AggregateExpression")
astm_QualifiedOverPointer = Class(name="astm::QualifiedOverPointer")
QualifiedIdentifierReference = Class(name="QualifiedIdentifierReference")
astm_QualifiedOverData = Class(name="astm::QualifiedOverData")
astm_IntegerlLiteral = Class(name="astm::IntegerlLiteral")
Literal = Class(name="Literal")
astm_StringLiteral = Class(name="astm::StringLiteral")
astm_CharLiteral = Class(name="astm::CharLiteral")
astm_RealLiteral = Class(name="astm::RealLiteral")
astm_BooleanLiteral = Class(name="astm::BooleanLiteral")
astm_BitLiteral = Class(name="astm::BitLiteral")
astm_UnaryPlus = Class(name="astm::UnaryPlus")
UnaryOperator = Class(name="UnaryOperator")
astm_Negate = Class(name="astm::Negate")
astm_Not = Class(name="astm::Not")
astm_Deref = Class(name="astm::Deref")
astm_Increment = Class(name="astm::Increment")
astm_Decrement = Class(name="astm::Decrement")
astm_PostIncrement = Class(name="astm::PostIncrement")
astm_PostDecrement = Class(name="astm::PostDecrement")
astm_Add = Class(name="astm::Add")
astm_Subtract = Class(name="astm::Subtract")
astm_Multiply = Class(name="astm::Multiply")
astm_Divide = Class(name="astm::Divide")
astm_Modulus = Class(name="astm::Modulus")
astm_Exponent = Class(name="astm::Exponent")
astm_And = Class(name="astm::And")
astm_Or = Class(name="astm::Or")
astm_Equal = Class(name="astm::Equal")
astm_NotEqual = Class(name="astm::NotEqual")
astm_Greater = Class(name="astm::Greater")
astm_NotGreater = Class(name="astm::NotGreater")
astm_Less = Class(name="astm::Less")
astm_NotLess = Class(name="astm::NotLess")
astm_BitAnd = Class(name="astm::BitAnd")
astm_BitOr = Class(name="astm::BitOr")
astm_BitXor = Class(name="astm::BitXor")
astm_BitRightShift = Class(name="astm::BitRightShift")
astm_BitLeftShift = Class(name="astm::BitLeftShift")
astm_Assign = Class(name="astm::Assign")
astm_MissingActualParameter = Class(name="astm::MissingActualParameter")
astm_ByValueActualParameterExpression = Class(name="astm::ByValueActualParameterExpression")
ActualParameterExpression = Class(name="ActualParameterExpression")
astm_ByReferenceActualParameterExpression = Class(name="astm::ByReferenceActualParameterExpression")
astm_SpecificTriggerDefinition = Class(name="astm::SpecificTriggerDefinition")
astm_SpecificLessEqual = Class(name="astm::SpecificLessEqual")
astm_SpecificGreaterEqual = Class(name="astm::SpecificGreaterEqual")
astm_SpecificIn = Class(name="astm::SpecificIn")
astm_SpecificLike = Class(name="astm::SpecificLike")
astm_SpecificConcatString = Class(name="astm::SpecificConcatString")
astm_SpecificSelectStatement = Class(name="astm::SpecificSelectStatement")

# astm_OtherSyntaxObject class attributes and methods

# astm_StorageSpecification class attributes and methods

# astm_DataType class attributes and methods

# astm_AccessKind class attributes and methods

# astm_UnaryOperator class attributes and methods

# astm_BinaryOperator class attributes and methods

# astm_ActualParameter class attributes and methods

# astm_SourceFile class attributes and methods
astm_SourceFile_pathName: Property = Property(name="pathName", type=StringType)
astm_SourceFile.attributes={astm_SourceFile_pathName}

# GASTMSourceObject class attributes and methods

# astm_SourceLocation class attributes and methods
astm_SourceLocation_startLine: Property = Property(name="startLine", type=IntegerType)
astm_SourceLocation_startColumn: Property = Property(name="startColumn", type=IntegerType)
astm_SourceLocation_endLine: Property = Property(name="endLine", type=IntegerType)
astm_SourceLocation_endColumn: Property = Property(name="endColumn", type=IntegerType)
astm_SourceLocation.attributes={astm_SourceLocation_startLine, astm_SourceLocation_startColumn, astm_SourceLocation_endColumn, astm_SourceLocation_endLine}

# astm_GASTMObject class attributes and methods

# astm_GASTMSourceObject class attributes and methods

# astm_GASTMSemanticObject class attributes and methods

# CompilationUnit class attributes and methods

# GlobalScope class attributes and methods

# astm_Scope class attributes and methods

# DefinitionObject class attributes and methods

# Scope class attributes and methods

# astm_GASTMSyntaxObject class attributes and methods

# GASTMObject class attributes and methods

# SourceFile class attributes and methods

# astm_Project class attributes and methods

# GASTMSemanticObject class attributes and methods

# AnnotationExpression class attributes and methods

# astm_CompilationUnit class attributes and methods
astm_CompilationUnit_language: Property = Property(name="language", type=StringType)
astm_CompilationUnit.attributes={astm_CompilationUnit_language}

# OtherSyntaxObject class attributes and methods

# ProgramScope class attributes and methods

# astm_Name class attributes and methods
astm_Name_nameString: Property = Property(name="nameString", type=StringType)
astm_Name.attributes={astm_Name_nameString}

# astm_DeclarationOrDefinition class attributes and methods
astm_DeclarationOrDefinition_isRegister: Property = Property(name="isRegister", type=BooleanType)
astm_DeclarationOrDefinition_linkageSpecifier: Property = Property(name="linkageSpecifier", type=StringType)
astm_DeclarationOrDefinition.attributes={astm_DeclarationOrDefinition_linkageSpecifier, astm_DeclarationOrDefinition_isRegister}

# SourceLocation class attributes and methods

# PreprocessorElement class attributes and methods

# astm_Definition class attributes and methods

# DeclarationOrDefinition class attributes and methods

# Name class attributes and methods

# TypeReference class attributes and methods

# astm_Declaration class attributes and methods

# Definition class attributes and methods

# astm_VariableDeclaration class attributes and methods
astm_VariableDeclaration_isMutable: Property = Property(name="isMutable", type=BooleanType)
astm_VariableDeclaration.attributes={astm_VariableDeclaration_isMutable}

# astm_FunctionDefinition class attributes and methods

# FormalParameterDefinition class attributes and methods

# Statement class attributes and methods

# FunctionScope class attributes and methods

# astm_FunctionDeclaration class attributes and methods

# Declaration class attributes and methods

# FormalParameterDeclaration class attributes and methods

# FunctionMemberAttributes class attributes and methods

# VirtualSpecification class attributes and methods

# astm_EntryDefinition class attributes and methods

# astm_DataDefinition class attributes and methods
astm_DataDefinition_isMutable: Property = Property(name="isMutable", type=BooleanType)
astm_DataDefinition.attributes={astm_DataDefinition_isMutable}

# Expression class attributes and methods

# astm_FunctionMemberAttributes class attributes and methods
astm_FunctionMemberAttributes_isFriend: Property = Property(name="isFriend", type=BooleanType)
astm_FunctionMemberAttributes_isInline: Property = Property(name="isInline", type=BooleanType)
astm_FunctionMemberAttributes_isThisConst: Property = Property(name="isThisConst", type=BooleanType)
astm_FunctionMemberAttributes.attributes={astm_FunctionMemberAttributes_isThisConst, astm_FunctionMemberAttributes_isFriend, astm_FunctionMemberAttributes_isInline}

# astm_TypeDefinition class attributes and methods

# astm_NamedTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# NamedType class attributes and methods

# astm_AggregateTypeDefinition class attributes and methods

# AggregateType class attributes and methods

# astm_NameSpaceDefinition class attributes and methods

# astm_BitFieldDefinition class attributes and methods

# DataDefinition class attributes and methods

# astm_EnumLiteralDefinition class attributes and methods

# astm_LabelDefinition class attributes and methods

# LabelType class attributes and methods

# astm_IncludeUnit class attributes and methods

# astm_MacroCall class attributes and methods

# MacroDefinition class attributes and methods

# astm_MacroDefinition class attributes and methods
astm_MacroDefinition_macroName: Property = Property(name="macroName", type=StringType)
astm_MacroDefinition_body: Property = Property(name="body", type=StringType)
astm_MacroDefinition.attributes={astm_MacroDefinition_body, astm_MacroDefinition_macroName}

# NameSpaceType class attributes and methods

# astm_Type class attributes and methods
astm_Type_isConst: Property = Property(name="isConst", type=BooleanType)
astm_Type_isVolatile: Property = Property(name="isVolatile", type=BooleanType)
astm_Type.attributes={astm_Type_isConst, astm_Type_isVolatile}

# GASTMSyntaxObject class attributes and methods

# astm_PrimitiveType class attributes and methods
astm_PrimitiveType_isSigned: Property = Property(name="isSigned", type=BooleanType)
astm_PrimitiveType.attributes={astm_PrimitiveType_isSigned}

# DataType class attributes and methods

# astm_EnumType class attributes and methods

# EnumLiteralDefinition class attributes and methods

# astm_ConstructedType class attributes and methods

# astm_AggregateType class attributes and methods

# astm_Comment class attributes and methods
astm_Comment_text: Property = Property(name="text", type=StringType)
astm_Comment.attributes={astm_Comment_text}

# astm_ArrayType class attributes and methods

# ConstructedType class attributes and methods

# Dimension class attributes and methods

# astm_Dimension class attributes and methods

# astm_FunctionType class attributes and methods

# Type class attributes and methods

# AggregateScope class attributes and methods

# astm_FormalParameterType class attributes and methods

# astm_NamedType class attributes and methods

# astm_ClassType class attributes and methods

# DerivesFrom class attributes and methods

# astm_DerivesFrom class attributes and methods
astm_DerivesFrom_isVirtual: Property = Property(name="isVirtual", type=BooleanType)
astm_DerivesFrom.attributes={astm_DerivesFrom_isVirtual}

# FormalParameterType class attributes and methods

# astm_NamedTypeReference class attributes and methods

# astm_DeleteStatement class attributes and methods

# astm_UnnamedTypeReference class attributes and methods

# astm_JumpStatement class attributes and methods

# astm_BreakStatement class attributes and methods

# LabelAccess class attributes and methods

# astm_ContinueStatement class attributes and methods

# astm_LabeledStatement class attributes and methods

# astm_DeclarationOrDefinitionStatement class attributes and methods

# astm_ExpressionStatement class attributes and methods

# astm_BlockStatement class attributes and methods

# BlockScope class attributes and methods

# astm_EmptyStatement class attributes and methods

# astm_IfStatement class attributes and methods

# LabelDefinition class attributes and methods

# astm_SwitchStatement class attributes and methods

# SwitchCase class attributes and methods

# astm_SwitchCase class attributes and methods

# astm_CaseBlock class attributes and methods

# astm_ReturnStatement class attributes and methods

# astm_LoopStatement class attributes and methods

# astm_ForStatement class attributes and methods

# LoopStatement class attributes and methods

# astm_TryStatement class attributes and methods

# CatchBlock class attributes and methods

# astm_CatchBlock class attributes and methods

# astm_TypesCatchBlock class attributes and methods

# astm_VariableCatchBlock class attributes and methods

# astm_ThrowStatement class attributes and methods

# astm_Expression class attributes and methods

# astm_NameReference class attributes and methods

# astm_ArrayAccess class attributes and methods

# astm_QualifiedIdentifierReference class attributes and methods

# NameReference class attributes and methods

# IdentifierReference class attributes and methods

# astm_TypeQualifiedIdentifierReference class attributes and methods

# astm_Literal class attributes and methods
astm_Literal_value: Property = Property(name="value", type=StringType)
astm_Literal.attributes={astm_Literal_value}

# astm_CastExpression class attributes and methods

# astm_UnaryExpression class attributes and methods

# astm_BinaryExpression class attributes and methods

# astm_OperatorAssign class attributes and methods

# BinaryOperator class attributes and methods

# astm_ConditionalExpression class attributes and methods

# astm_RangeExpression class attributes and methods

# astm_NewExpression class attributes and methods

# astm_FunctionCallExpression class attributes and methods

# ActualParameter class attributes and methods

# astm_ActualParameterExpression class attributes and methods

# astm_LabelAccess class attributes and methods

# astm_AnnotationExpression class attributes and methods

# astm_GlobalScope class attributes and methods

# astm_PreprocessorElement class attributes and methods

# astm_DefinitionObject class attributes and methods

# astm_ProgramScope class attributes and methods

# astm_TypeReference class attributes and methods

# astm_Statement class attributes and methods

# astm_FunctionScope class attributes and methods

# astm_NameSpaceType class attributes and methods

# astm_LabelType class attributes and methods

# astm_AggregateScope class attributes and methods

# astm_BlockScope class attributes and methods

# astm_IdentifierReference class attributes and methods

# astm_VirtualSpecification class attributes and methods

# astm_Float class attributes and methods

# astm_FormalParameterDefinition class attributes and methods

# astm_FormalParameterDeclaration class attributes and methods

# astm_Double class attributes and methods

# astm_VariableDefinition class attributes and methods

# astm_FunctionMemberAttribute class attributes and methods

# astm_External class attributes and methods

# StorageSpecification class attributes and methods

# astm_FunctionPersistent class attributes and methods

# astm_FileLocal class attributes and methods

# astm_PerClassMember class attributes and methods

# astm_NoDef class attributes and methods

# astm_Virtual class attributes and methods

# astm_PureVirtual class attributes and methods

# astm_NonVirtual class attributes and methods

# astm_ExceptionType class attributes and methods

# astm_Void class attributes and methods

# PrimitiveType class attributes and methods

# astm_Byte class attributes and methods

# astm_ShortInteger class attributes and methods

# astm_Integer class attributes and methods

# astm_LongInteger class attributes and methods

# astm_TerminateStatement class attributes and methods

# astm_LongDouble class attributes and methods

# astm_Character class attributes and methods

# astm_String class attributes and methods

# astm_Boolean class attributes and methods

# astm_WideCharacter class attributes and methods

# astm_CollectionType class attributes and methods

# astm_PointerType class attributes and methods

# astm_ReferenceType class attributes and methods

# astm_RangeType class attributes and methods

# astm_StructureType class attributes and methods

# astm_UnionType class attributes and methods

# astm_AnnotationType class attributes and methods

# astm_ByValueFormalParameterType class attributes and methods

# astm_ByReferenceFormalParameterType class attributes and methods

# astm_Public class attributes and methods

# AccessKind class attributes and methods

# astm_Protected class attributes and methods

# astm_Private class attributes and methods

# astm_BitNot class attributes and methods

# astm_AddressOf class attributes and methods

# astm_DefaultBlock class attributes and methods

# astm_WhileStatement class attributes and methods

# astm_DoWhileStatement class attributes and methods

# astm_ForCheckBeforeStatement class attributes and methods

# ForStatement class attributes and methods

# astm_ForCheckAfterStatement class attributes and methods

# astm_AggregateExpression class attributes and methods

# astm_QualifiedOverPointer class attributes and methods

# QualifiedIdentifierReference class attributes and methods

# astm_QualifiedOverData class attributes and methods

# astm_IntegerlLiteral class attributes and methods

# Literal class attributes and methods

# astm_StringLiteral class attributes and methods

# astm_CharLiteral class attributes and methods

# astm_RealLiteral class attributes and methods

# astm_BooleanLiteral class attributes and methods

# astm_BitLiteral class attributes and methods

# astm_UnaryPlus class attributes and methods

# UnaryOperator class attributes and methods

# astm_Negate class attributes and methods

# astm_Not class attributes and methods

# astm_Deref class attributes and methods

# astm_Increment class attributes and methods

# astm_Decrement class attributes and methods

# astm_PostIncrement class attributes and methods

# astm_PostDecrement class attributes and methods

# astm_Add class attributes and methods

# astm_Subtract class attributes and methods

# astm_Multiply class attributes and methods

# astm_Divide class attributes and methods

# astm_Modulus class attributes and methods

# astm_Exponent class attributes and methods

# astm_And class attributes and methods

# astm_Or class attributes and methods

# astm_Equal class attributes and methods

# astm_NotEqual class attributes and methods

# astm_Greater class attributes and methods

# astm_NotGreater class attributes and methods

# astm_Less class attributes and methods

# astm_NotLess class attributes and methods

# astm_BitAnd class attributes and methods

# astm_BitOr class attributes and methods

# astm_BitXor class attributes and methods

# astm_BitRightShift class attributes and methods

# astm_BitLeftShift class attributes and methods

# astm_Assign class attributes and methods

# astm_MissingActualParameter class attributes and methods

# astm_ByValueActualParameterExpression class attributes and methods

# ActualParameterExpression class attributes and methods

# astm_ByReferenceActualParameterExpression class attributes and methods

# astm_SpecificTriggerDefinition class attributes and methods

# astm_SpecificLessEqual class attributes and methods

# astm_SpecificGreaterEqual class attributes and methods

# astm_SpecificIn class attributes and methods

# astm_SpecificLike class attributes and methods

# astm_SpecificConcatString class attributes and methods

# astm_SpecificSelectStatement class attributes and methods

# Relationships
files1: BinaryAssociation = BinaryAssociation(
    name="files1",
    ends={
        Property(name="CompilationUnit", type=astm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Project", type=CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outerScope2: BinaryAssociation = BinaryAssociation(
    name="outerScope2",
    ends={
        Property(name="GlobalScope", type=astm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Project3", type=GlobalScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionObject4: BinaryAssociation = BinaryAssociation(
    name="definitionObject4",
    ends={
        Property(name="DefinitionObject", type=astm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Scope", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childScope5: BinaryAssociation = BinaryAssociation(
    name="childScope5",
    ends={
        Property(name="Scope", type=astm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Scope6", type=Scope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inSourceFile0: BinaryAssociation = BinaryAssociation(
    name="inSourceFile0",
    ends={
        Property(name="SourceFile", type=astm_SourceLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SourceLocation", type=SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations10: BinaryAssociation = BinaryAssociation(
    name="annotations10",
    ends={
        Property(name="AnnotationExpression", type=astm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_GASTMSyntaxObject11", type=AnnotationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments12: BinaryAssociation = BinaryAssociation(
    name="fragments12",
    ends={
        Property(name="DefinitionObject13", type=astm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CompilationUnit", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope14: BinaryAssociation = BinaryAssociation(
    name="opensScope14",
    ends={
        Property(name="ProgramScope", type=astm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CompilationUnit15", type=ProgramScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
locationInfo7: BinaryAssociation = BinaryAssociation(
    name="locationInfo7",
    ends={
        Property(name="SourceLocation", type=astm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_GASTMSyntaxObject", type=SourceLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preProcessorElements8: BinaryAssociation = BinaryAssociation(
    name="preProcessorElements8",
    ends={
        Property(name="PreprocessorElement", type=astm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_GASTMSyntaxObject9", type=PreprocessorElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifierName20: BinaryAssociation = BinaryAssociation(
    name="identifierName20",
    ends={
        Property(name="Name", type=astm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Definition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType21: BinaryAssociation = BinaryAssociation(
    name="definitionType21",
    ends={
        Property(name="TypeReference", type=astm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Definition22", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defRef23: BinaryAssociation = BinaryAssociation(
    name="defRef23",
    ends={
        Property(name="Definition", type=astm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Declaration", type=Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierName24: BinaryAssociation = BinaryAssociation(
    name="identifierName24",
    ends={
        Property(name="Name26", type=astm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Declaration25", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarationType27: BinaryAssociation = BinaryAssociation(
    name="declarationType27",
    ends={
        Property(name="TypeReference29", type=astm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Declaration28", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
storageSpecifiers16: BinaryAssociation = BinaryAssociation(
    name="storageSpecifiers16",
    ends={
        Property(name="OtherSyntaxObject", type=astm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeclarationOrDefinition", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessKind17: BinaryAssociation = BinaryAssociation(
    name="accessKind17",
    ends={
        Property(name="OtherSyntaxObject19", type=astm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeclarationOrDefinition18", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType33: BinaryAssociation = BinaryAssociation(
    name="returnType33",
    ends={
        Property(name="TypeReference34", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters35: BinaryAssociation = BinaryAssociation(
    name="formalParameters35",
    ends={
        Property(name="FormalParameterDefinition", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition36", type=FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body37: BinaryAssociation = BinaryAssociation(
    name="body37",
    ends={
        Property(name="Statement", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition38", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes39: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes39",
    ends={
        Property(name="FunctionMemberAttributes41", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition40", type=FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opensScope42: BinaryAssociation = BinaryAssociation(
    name="opensScope42",
    ends={
        Property(name="FunctionScope", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition43", type=FunctionScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters30: BinaryAssociation = BinaryAssociation(
    name="formalParameters30",
    ends={
        Property(name="FormalParameterDeclaration", type=astm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDeclaration", type=FormalParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes31: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes31",
    ends={
        Property(name="FunctionMemberAttributes", type=astm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDeclaration32", type=FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
virtualSpecifier44: BinaryAssociation = BinaryAssociation(
    name="virtualSpecifier44",
    ends={
        Property(name="VirtualSpecification", type=astm_FunctionMemberAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionMemberAttributes", type=VirtualSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters45: BinaryAssociation = BinaryAssociation(
    name="formalParameters45",
    ends={
        Property(name="FormalParameterDefinition46", type=astm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EntryDefinition", type=FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body47: BinaryAssociation = BinaryAssociation(
    name="body47",
    ends={
        Property(name="Statement49", type=astm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EntryDefinition48", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue50: BinaryAssociation = BinaryAssociation(
    name="initialValue50",
    ends={
        Property(name="Expression", type=astm_DataDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DataDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name55: BinaryAssociation = BinaryAssociation(
    name="name55",
    ends={
        Property(name="Name56", type=astm_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypeDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType57: BinaryAssociation = BinaryAssociation(
    name="definitionType57",
    ends={
        Property(name="NamedType", type=astm_NamedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedTypeDefinition", type=NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType58: BinaryAssociation = BinaryAssociation(
    name="aggregateType58",
    ends={
        Property(name="AggregateType", type=astm_AggregateTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AggregateTypeDefinition", type=AggregateType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameSpace59: BinaryAssociation = BinaryAssociation(
    name="nameSpace59",
    ends={
        Property(name="Name60", type=astm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameSpaceDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bitFieldSize51: BinaryAssociation = BinaryAssociation(
    name="bitFieldSize51",
    ends={
        Property(name="Expression52", type=astm_BitFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BitFieldDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value53: BinaryAssociation = BinaryAssociation(
    name="value53",
    ends={
        Property(name="Expression54", type=astm_EnumLiteralDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EnumLiteralDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelName66: BinaryAssociation = BinaryAssociation(
    name="labelName66",
    ends={
        Property(name="Name67", type=astm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelType68: BinaryAssociation = BinaryAssociation(
    name="labelType68",
    ends={
        Property(name="LabelType", type=astm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelDefinition69", type=LabelType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file70: BinaryAssociation = BinaryAssociation(
    name="file70",
    ends={
        Property(name="SourceFile71", type=astm_IncludeUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IncludeUnit", type=SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo72: BinaryAssociation = BinaryAssociation(
    name="refersTo72",
    ends={
        Property(name="MacroDefinition", type=astm_MacroCall, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_MacroCall", type=MacroDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body61: BinaryAssociation = BinaryAssociation(
    name="body61",
    ends={
        Property(name="DefinitionObject63", type=astm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameSpaceDefinition62", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameSpaceType64: BinaryAssociation = BinaryAssociation(
    name="nameSpaceType64",
    ends={
        Property(name="NameSpaceType", type=astm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameSpaceDefinition65", type=NameSpaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumLiterals73: BinaryAssociation = BinaryAssociation(
    name="enumLiterals73",
    ends={
        Property(name="EnumLiteralDefinition", type=astm_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EnumType", type=EnumLiteralDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType74: BinaryAssociation = BinaryAssociation(
    name="baseType74",
    ends={
        Property(name="TypeReference75", type=astm_ConstructedType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConstructedType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ranks80: BinaryAssociation = BinaryAssociation(
    name="ranks80",
    ends={
        Property(name="Dimension", type=astm_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ArrayType", type=Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lowBound81: BinaryAssociation = BinaryAssociation(
    name="lowBound81",
    ends={
        Property(name="Expression82", type=astm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Dimension", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
highBound83: BinaryAssociation = BinaryAssociation(
    name="highBound83",
    ends={
        Property(name="Expression85", type=astm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Dimension84", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType86: BinaryAssociation = BinaryAssociation(
    name="returnType86",
    ends={
        Property(name="TypeReference87", type=astm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members76: BinaryAssociation = BinaryAssociation(
    name="members76",
    ends={
        Property(name="DefinitionObject77", type=astm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AggregateType", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope78: BinaryAssociation = BinaryAssociation(
    name="opensScope78",
    ends={
        Property(name="AggregateScope", type=astm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AggregateType79", type=AggregateScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type90: BinaryAssociation = BinaryAssociation(
    name="type90",
    ends={
        Property(name="TypeReference91", type=astm_FormalParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FormalParameterType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body92: BinaryAssociation = BinaryAssociation(
    name="body92",
    ends={
        Property(name="Type", type=astm_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedType", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivesFrom93: BinaryAssociation = BinaryAssociation(
    name="derivesFrom93",
    ends={
        Property(name="DerivesFrom", type=astm_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ClassType", type=DerivesFrom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterTypes88: BinaryAssociation = BinaryAssociation(
    name="parameterTypes88",
    ends={
        Property(name="FormalParameterType", type=astm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionType89", type=FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type99: BinaryAssociation = BinaryAssociation(
    name="type99",
    ends={
        Property(name="Type100", type=astm_UnnamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_UnnamedTypeReference", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name101: BinaryAssociation = BinaryAssociation(
    name="name101",
    ends={
        Property(name="Name102", type=astm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedTypeReference", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="TypeDefinition", type=astm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedTypeReference104", type=TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
operand105: BinaryAssociation = BinaryAssociation(
    name="operand105",
    ends={
        Property(name="Expression106", type=astm_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeleteStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessKind94: BinaryAssociation = BinaryAssociation(
    name="accessKind94",
    ends={
        Property(name="OtherSyntaxObject95", type=astm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DerivesFrom", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className96: BinaryAssociation = BinaryAssociation(
    name="className96",
    ends={
        Property(name="NamedType98", type=astm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DerivesFrom97", type=NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target111: BinaryAssociation = BinaryAssociation(
    name="target111",
    ends={
        Property(name="Expression112", type=astm_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_JumpStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target113: BinaryAssociation = BinaryAssociation(
    name="target113",
    ends={
        Property(name="LabelAccess", type=astm_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BreakStatement", type=LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target114: BinaryAssociation = BinaryAssociation(
    name="target114",
    ends={
        Property(name="LabelAccess115", type=astm_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ContinueStatement", type=LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declOrDefn107: BinaryAssociation = BinaryAssociation(
    name="declOrDefn107",
    ends={
        Property(name="DefinitionObject108", type=astm_DeclarationOrDefinitionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeclarationOrDefinitionStatement", type=DefinitionObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression109: BinaryAssociation = BinaryAssociation(
    name="expression109",
    ends={
        Property(name="Expression110", type=astm_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ExpressionStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subStatements120: BinaryAssociation = BinaryAssociation(
    name="subStatements120",
    ends={
        Property(name="Statement121", type=astm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BlockStatement", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope122: BinaryAssociation = BinaryAssociation(
    name="opensScope122",
    ends={
        Property(name="BlockScope", type=astm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BlockStatement123", type=BlockScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition124: BinaryAssociation = BinaryAssociation(
    name="condition124",
    ends={
        Property(name="Expression125", type=astm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IfStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label116: BinaryAssociation = BinaryAssociation(
    name="label116",
    ends={
        Property(name="LabelDefinition", type=astm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabeledStatement", type=LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBody126: BinaryAssociation = BinaryAssociation(
    name="thenBody126",
    ends={
        Property(name="Statement128", type=astm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IfStatement127", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement117: BinaryAssociation = BinaryAssociation(
    name="statement117",
    ends={
        Property(name="Statement119", type=astm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabeledStatement118", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBody129: BinaryAssociation = BinaryAssociation(
    name="elseBody129",
    ends={
        Property(name="Statement131", type=astm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IfStatement130", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body144: BinaryAssociation = BinaryAssociation(
    name="body144",
    ends={
        Property(name="Statement146", type=astm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LoopStatement145", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchExpression132: BinaryAssociation = BinaryAssociation(
    name="switchExpression132",
    ends={
        Property(name="Expression133", type=astm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SwitchStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases134: BinaryAssociation = BinaryAssociation(
    name="cases134",
    ends={
        Property(name="SwitchCase", type=astm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SwitchStatement135", type=SwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body136: BinaryAssociation = BinaryAssociation(
    name="body136",
    ends={
        Property(name="Statement137", type=astm_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SwitchCase", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caseExpressions138: BinaryAssociation = BinaryAssociation(
    name="caseExpressions138",
    ends={
        Property(name="Expression139", type=astm_CaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CaseBlock", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue140: BinaryAssociation = BinaryAssociation(
    name="returnValue140",
    ends={
        Property(name="Expression141", type=astm_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition142: BinaryAssociation = BinaryAssociation(
    name="condition142",
    ends={
        Property(name="Expression143", type=astm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LoopStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions161: BinaryAssociation = BinaryAssociation(
    name="exceptions161",
    ends={
        Property(name="Type162", type=astm_TypesCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypesCatchBlock", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initBody147: BinaryAssociation = BinaryAssociation(
    name="initBody147",
    ends={
        Property(name="Expression148", type=astm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ForStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationBody149: BinaryAssociation = BinaryAssociation(
    name="iterationBody149",
    ends={
        Property(name="Expression151", type=astm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ForStatement150", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guardedStatement152: BinaryAssociation = BinaryAssociation(
    name="guardedStatement152",
    ends={
        Property(name="Statement153", type=astm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TryStatement", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchBlocks154: BinaryAssociation = BinaryAssociation(
    name="catchBlocks154",
    ends={
        Property(name="CatchBlock", type=astm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TryStatement155", type=CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalStatement156: BinaryAssociation = BinaryAssociation(
    name="finalStatement156",
    ends={
        Property(name="Statement158", type=astm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TryStatement157", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body159: BinaryAssociation = BinaryAssociation(
    name="body159",
    ends={
        Property(name="Statement160", type=astm_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CatchBlock", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayName173: BinaryAssociation = BinaryAssociation(
    name="arrayName173",
    ends={
        Property(name="astm_ArrayAccess", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Expression174", type=astm_ArrayAccess, multiplicity=Multiplicity(1, 1))
    }
)
exceptionVariable163: BinaryAssociation = BinaryAssociation(
    name="exceptionVariable163",
    ends={
        Property(name="DataDefinition", type=astm_VariableCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_VariableCatchBlock", type=DataDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception164: BinaryAssociation = BinaryAssociation(
    name="exception164",
    ends={
        Property(name="Expression165", type=astm_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ThrowStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionType166: BinaryAssociation = BinaryAssociation(
    name="expressionType166",
    ends={
        Property(name="TypeReference167", type=astm_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Expression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name168: BinaryAssociation = BinaryAssociation(
    name="name168",
    ends={
        Property(name="Name169", type=astm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameReference", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo170: BinaryAssociation = BinaryAssociation(
    name="refersTo170",
    ends={
        Property(name="DefinitionObject172", type=astm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameReference171", type=DefinitionObject, multiplicity=Multiplicity(0, 1))
    }
)
castType187: BinaryAssociation = BinaryAssociation(
    name="castType187",
    ends={
        Property(name="TypeReference188", type=astm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CastExpression", type=TypeReference, multiplicity=Multiplicity(0, 1))
    }
)
subscripts175: BinaryAssociation = BinaryAssociation(
    name="subscripts175",
    ends={
        Property(name="Expression177", type=astm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ArrayAccess176", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifiers178: BinaryAssociation = BinaryAssociation(
    name="qualifiers178",
    ends={
        Property(name="Expression179", type=astm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_QualifiedIdentifierReference", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member180: BinaryAssociation = BinaryAssociation(
    name="member180",
    ends={
        Property(name="IdentifierReference", type=astm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_QualifiedIdentifierReference181", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType182: BinaryAssociation = BinaryAssociation(
    name="aggregateType182",
    ends={
        Property(name="TypeReference183", type=astm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypeQualifiedIdentifierReference", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member184: BinaryAssociation = BinaryAssociation(
    name="member184",
    ends={
        Property(name="IdentifierReference186", type=astm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypeQualifiedIdentifierReference185", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand202: BinaryAssociation = BinaryAssociation(
    name="rightOperand202",
    ends={
        Property(name="Expression204", type=astm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BinaryExpression203", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression189: BinaryAssociation = BinaryAssociation(
    name="expression189",
    ends={
        Property(name="Expression191", type=astm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CastExpression190", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator192: BinaryAssociation = BinaryAssociation(
    name="operator192",
    ends={
        Property(name="OtherSyntaxObject193", type=astm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_UnaryExpression", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand194: BinaryAssociation = BinaryAssociation(
    name="operand194",
    ends={
        Property(name="Expression196", type=astm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_UnaryExpression195", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator197: BinaryAssociation = BinaryAssociation(
    name="operator197",
    ends={
        Property(name="OtherSyntaxObject198", type=astm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BinaryExpression", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand199: BinaryAssociation = BinaryAssociation(
    name="leftOperand199",
    ends={
        Property(name="Expression201", type=astm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BinaryExpression200", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromExpression215: BinaryAssociation = BinaryAssociation(
    name="fromExpression215",
    ends={
        Property(name="Expression216", type=astm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_RangeExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator205: BinaryAssociation = BinaryAssociation(
    name="operator205",
    ends={
        Property(name="OtherSyntaxObject206", type=astm_OperatorAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_OperatorAssign", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition207: BinaryAssociation = BinaryAssociation(
    name="condition207",
    ends={
        Property(name="Expression208", type=astm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConditionalExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onTrueOperand209: BinaryAssociation = BinaryAssociation(
    name="onTrueOperand209",
    ends={
        Property(name="Expression211", type=astm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConditionalExpression210", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onFalseOperand212: BinaryAssociation = BinaryAssociation(
    name="onFalseOperand212",
    ends={
        Property(name="Expression214", type=astm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConditionalExpression213", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toExpression217: BinaryAssociation = BinaryAssociation(
    name="toExpression217",
    ends={
        Property(name="Expression219", type=astm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_RangeExpression218", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
calledFunction220: BinaryAssociation = BinaryAssociation(
    name="calledFunction220",
    ends={
        Property(name="Expression221", type=astm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionCallExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams222: BinaryAssociation = BinaryAssociation(
    name="actualParams222",
    ends={
        Property(name="ActualParameter", type=astm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionCallExpression223", type=ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value224: BinaryAssociation = BinaryAssociation(
    name="value224",
    ends={
        Property(name="Expression225", type=astm_ActualParameterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ActualParameterExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberValues238: BinaryAssociation = BinaryAssociation(
    name="memberValues238",
    ends={
        Property(name="Expression240", type=astm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AnnotationExpression239", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
newType226: BinaryAssociation = BinaryAssociation(
    name="newType226",
    ends={
        Property(name="TypeReference227", type=astm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NewExpression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams228: BinaryAssociation = BinaryAssociation(
    name="actualParams228",
    ends={
        Property(name="OtherSyntaxObject230", type=astm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NewExpression229", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name231: BinaryAssociation = BinaryAssociation(
    name="name231",
    ends={
        Property(name="Name232", type=astm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelAccess", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition233: BinaryAssociation = BinaryAssociation(
    name="definition233",
    ends={
        Property(name="LabelDefinition235", type=astm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelAccess234", type=LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationType236: BinaryAssociation = BinaryAssociation(
    name="annotationType236",
    ends={
        Property(name="TypeReference237", type=astm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AnnotationExpression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body241: BinaryAssociation = BinaryAssociation(
    name="body241",
    ends={
        Property(name="Statement242", type=astm_SpecificTriggerDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SpecificTriggerDefinition", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_astm_SourceFile_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=astm_SourceFile)
gen_astm_SourceLocation_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=astm_SourceLocation)
gen_astm_Scope_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=astm_Scope)
gen_astm_GASTMSyntaxObject_GASTMObject = Generalization(general=GASTMObject, specific=astm_GASTMSyntaxObject)
gen_astm_Project_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=astm_Project)
gen_astm_CompilationUnit_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_CompilationUnit)
gen_astm_Name_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_Name)
gen_astm_DeclarationOrDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_DeclarationOrDefinition)
gen_astm_Definition_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=astm_Definition)
gen_astm_Declaration_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=astm_Declaration)
gen_astm_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=astm_VariableDeclaration)
gen_astm_FunctionDefinition_Definition = Generalization(general=Definition, specific=astm_FunctionDefinition)
gen_astm_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=astm_FunctionDeclaration)
gen_astm_EntryDefinition_Definition = Generalization(general=Definition, specific=astm_EntryDefinition)
gen_astm_DataDefinition_Definition = Generalization(general=Definition, specific=astm_DataDefinition)
gen_astm_TypeDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_TypeDefinition)
gen_astm_NamedTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=astm_NamedTypeDefinition)
gen_astm_AggregateTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=astm_AggregateTypeDefinition)
gen_astm_NameSpaceDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_NameSpaceDefinition)
gen_astm_BitFieldDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_BitFieldDefinition)
gen_astm_EnumLiteralDefinition_Definition = Generalization(general=Definition, specific=astm_EnumLiteralDefinition)
gen_astm_LabelDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_LabelDefinition)
gen_astm_IncludeUnit_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_IncludeUnit)
gen_astm_MacroCall_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_MacroCall)
gen_astm_MacroDefinition_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_MacroDefinition)
gen_astm_Type_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_Type)
gen_astm_PrimitiveType_DataType = Generalization(general=DataType, specific=astm_PrimitiveType)
gen_astm_EnumType_DataType = Generalization(general=DataType, specific=astm_EnumType)
gen_astm_ConstructedType_DataType = Generalization(general=DataType, specific=astm_ConstructedType)
gen_astm_AggregateType_DataType = Generalization(general=DataType, specific=astm_AggregateType)
gen_astm_Comment_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_Comment)
gen_astm_ArrayType_ConstructedType = Generalization(general=ConstructedType, specific=astm_ArrayType)
gen_astm_Dimension_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_Dimension)
gen_astm_FunctionType_Type = Generalization(general=Type, specific=astm_FunctionType)
gen_astm_FormalParameterType_DataType = Generalization(general=DataType, specific=astm_FormalParameterType)
gen_astm_NamedType_DataType = Generalization(general=DataType, specific=astm_NamedType)
gen_astm_ClassType_AggregateType = Generalization(general=AggregateType, specific=astm_ClassType)
gen_astm_DerivesFrom_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_DerivesFrom)
gen_astm_NamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=astm_NamedTypeReference)
gen_astm_DeleteStatement_Statement = Generalization(general=Statement, specific=astm_DeleteStatement)
gen_astm_UnnamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=astm_UnnamedTypeReference)
gen_astm_JumpStatement_Statement = Generalization(general=Statement, specific=astm_JumpStatement)
gen_astm_BreakStatement_Statement = Generalization(general=Statement, specific=astm_BreakStatement)
gen_astm_ContinueStatement_Statement = Generalization(general=Statement, specific=astm_ContinueStatement)
gen_astm_LabeledStatement_Statement = Generalization(general=Statement, specific=astm_LabeledStatement)
gen_astm_DeclarationOrDefinitionStatement_Statement = Generalization(general=Statement, specific=astm_DeclarationOrDefinitionStatement)
gen_astm_ExpressionStatement_Statement = Generalization(general=Statement, specific=astm_ExpressionStatement)
gen_astm_BlockStatement_Statement = Generalization(general=Statement, specific=astm_BlockStatement)
gen_astm_EmptyStatement_Statement = Generalization(general=Statement, specific=astm_EmptyStatement)
gen_astm_IfStatement_Statement = Generalization(general=Statement, specific=astm_IfStatement)
gen_astm_SwitchStatement_Statement = Generalization(general=Statement, specific=astm_SwitchStatement)
gen_astm_SwitchCase_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_SwitchCase)
gen_astm_CaseBlock_SwitchCase = Generalization(general=SwitchCase, specific=astm_CaseBlock)
gen_astm_ReturnStatement_Statement = Generalization(general=Statement, specific=astm_ReturnStatement)
gen_astm_LoopStatement_Statement = Generalization(general=Statement, specific=astm_LoopStatement)
gen_astm_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_ForStatement)
gen_astm_TryStatement_Statement = Generalization(general=Statement, specific=astm_TryStatement)
gen_astm_CatchBlock_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_CatchBlock)
gen_astm_TypesCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=astm_TypesCatchBlock)
gen_astm_VariableCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=astm_VariableCatchBlock)
gen_astm_ThrowStatement_Statement = Generalization(general=Statement, specific=astm_ThrowStatement)
gen_astm_Expression_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_Expression)
gen_astm_NameReference_Expression = Generalization(general=Expression, specific=astm_NameReference)
gen_astm_ArrayAccess_Expression = Generalization(general=Expression, specific=astm_ArrayAccess)
gen_astm_QualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_QualifiedIdentifierReference)
gen_astm_TypeQualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_TypeQualifiedIdentifierReference)
gen_astm_Literal_Expression = Generalization(general=Expression, specific=astm_Literal)
gen_astm_CastExpression_Expression = Generalization(general=Expression, specific=astm_CastExpression)
gen_astm_UnaryExpression_Expression = Generalization(general=Expression, specific=astm_UnaryExpression)
gen_astm_BinaryExpression_Expression = Generalization(general=Expression, specific=astm_BinaryExpression)
gen_astm_OperatorAssign_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_OperatorAssign)
gen_astm_ConditionalExpression_Expression = Generalization(general=Expression, specific=astm_ConditionalExpression)
gen_astm_RangeExpression_Expression = Generalization(general=Expression, specific=astm_RangeExpression)
gen_astm_FunctionCallExpression_Expression = Generalization(general=Expression, specific=astm_FunctionCallExpression)
gen_astm_ActualParameterExpression_ActualParameter = Generalization(general=ActualParameter, specific=astm_ActualParameterExpression)
gen_astm_NewExpression_Expression = Generalization(general=Expression, specific=astm_NewExpression)
gen_astm_LabelAccess_Expression = Generalization(general=Expression, specific=astm_LabelAccess)
gen_astm_AnnotationExpression_Expression = Generalization(general=Expression, specific=astm_AnnotationExpression)
gen_astm_GlobalScope_Scope = Generalization(general=Scope, specific=astm_GlobalScope)
gen_astm_PreprocessorElement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_PreprocessorElement)
gen_astm_DefinitionObject_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_DefinitionObject)
gen_astm_ProgramScope_Scope = Generalization(general=Scope, specific=astm_ProgramScope)
gen_astm_TypeReference_Type = Generalization(general=Type, specific=astm_TypeReference)
gen_astm_Statement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_Statement)
gen_astm_FunctionScope_Scope = Generalization(general=Scope, specific=astm_FunctionScope)
gen_astm_NameSpaceType_Type = Generalization(general=Type, specific=astm_NameSpaceType)
gen_astm_LabelType_Type = Generalization(general=Type, specific=astm_LabelType)
gen_astm_AggregateScope_Scope = Generalization(general=Scope, specific=astm_AggregateScope)
gen_astm_BlockScope_Scope = Generalization(general=Scope, specific=astm_BlockScope)
gen_astm_IdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_IdentifierReference)
gen_astm_VirtualSpecification_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_VirtualSpecification)
gen_astm_Float_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Float)
gen_astm_FormalParameterDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_FormalParameterDefinition)
gen_astm_FormalParameterDeclaration_Declaration = Generalization(general=Declaration, specific=astm_FormalParameterDeclaration)
gen_astm_Double_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Double)
gen_astm_VariableDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_VariableDefinition)
gen_astm_FunctionMemberAttribute_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_FunctionMemberAttribute)
gen_astm_External_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_External)
gen_astm_FunctionPersistent_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_FunctionPersistent)
gen_astm_FileLocal_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_FileLocal)
gen_astm_PerClassMember_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_PerClassMember)
gen_astm_NoDef_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_NoDef)
gen_astm_Virtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_Virtual)
gen_astm_PureVirtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_PureVirtual)
gen_astm_NonVirtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_NonVirtual)
gen_astm_ExceptionType_DataType = Generalization(general=DataType, specific=astm_ExceptionType)
gen_astm_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Void)
gen_astm_Byte_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Byte)
gen_astm_ShortInteger_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_ShortInteger)
gen_astm_Integer_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Integer)
gen_astm_LongInteger_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_LongInteger)
gen_astm_TerminateStatement_Statement = Generalization(general=Statement, specific=astm_TerminateStatement)
gen_astm_LongDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_LongDouble)
gen_astm_Character_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Character)
gen_astm_String_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_String)
gen_astm_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Boolean)
gen_astm_WideCharacter_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_WideCharacter)
gen_astm_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=astm_CollectionType)
gen_astm_PointerType_ConstructedType = Generalization(general=ConstructedType, specific=astm_PointerType)
gen_astm_ReferenceType_ConstructedType = Generalization(general=ConstructedType, specific=astm_ReferenceType)
gen_astm_RangeType_ConstructedType = Generalization(general=ConstructedType, specific=astm_RangeType)
gen_astm_StructureType_AggregateType = Generalization(general=AggregateType, specific=astm_StructureType)
gen_astm_UnionType_AggregateType = Generalization(general=AggregateType, specific=astm_UnionType)
gen_astm_AnnotationType_AggregateType = Generalization(general=AggregateType, specific=astm_AnnotationType)
gen_astm_ByValueFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=astm_ByValueFormalParameterType)
gen_astm_ByReferenceFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=astm_ByReferenceFormalParameterType)
gen_astm_Public_AccessKind = Generalization(general=AccessKind, specific=astm_Public)
gen_astm_Protected_AccessKind = Generalization(general=AccessKind, specific=astm_Protected)
gen_astm_Private_AccessKind = Generalization(general=AccessKind, specific=astm_Private)
gen_astm_BitNot_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_BitNot)
gen_astm_AddressOf_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_AddressOf)
gen_astm_DefaultBlock_SwitchCase = Generalization(general=SwitchCase, specific=astm_DefaultBlock)
gen_astm_WhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_WhileStatement)
gen_astm_DoWhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_DoWhileStatement)
gen_astm_ForCheckBeforeStatement_ForStatement = Generalization(general=ForStatement, specific=astm_ForCheckBeforeStatement)
gen_astm_ForCheckAfterStatement_ForStatement = Generalization(general=ForStatement, specific=astm_ForCheckAfterStatement)
gen_astm_AggregateExpression_Expression = Generalization(general=Expression, specific=astm_AggregateExpression)
gen_astm_QualifiedOverPointer_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=astm_QualifiedOverPointer)
gen_astm_QualifiedOverData_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=astm_QualifiedOverData)
gen_astm_IntegerlLiteral_Literal = Generalization(general=Literal, specific=astm_IntegerlLiteral)
gen_astm_StringLiteral_Literal = Generalization(general=Literal, specific=astm_StringLiteral)
gen_astm_CharLiteral_Literal = Generalization(general=Literal, specific=astm_CharLiteral)
gen_astm_RealLiteral_Literal = Generalization(general=Literal, specific=astm_RealLiteral)
gen_astm_BooleanLiteral_Literal = Generalization(general=Literal, specific=astm_BooleanLiteral)
gen_astm_BitLiteral_Literal = Generalization(general=Literal, specific=astm_BitLiteral)
gen_astm_UnaryPlus_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_UnaryPlus)
gen_astm_Negate_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Negate)
gen_astm_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Not)
gen_astm_Deref_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Deref)
gen_astm_Increment_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Increment)
gen_astm_Decrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Decrement)
gen_astm_PostIncrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_PostIncrement)
gen_astm_PostDecrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_PostDecrement)
gen_astm_Add_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Add)
gen_astm_Subtract_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Subtract)
gen_astm_Multiply_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Multiply)
gen_astm_Divide_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Divide)
gen_astm_Modulus_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Modulus)
gen_astm_Exponent_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Exponent)
gen_astm_And_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_And)
gen_astm_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Or)
gen_astm_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Equal)
gen_astm_NotEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_NotEqual)
gen_astm_Greater_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Greater)
gen_astm_NotGreater_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_NotGreater)
gen_astm_Less_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Less)
gen_astm_NotLess_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_NotLess)
gen_astm_BitAnd_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitAnd)
gen_astm_BitOr_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitOr)
gen_astm_BitXor_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitXor)
gen_astm_BitRightShift_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitRightShift)
gen_astm_BitLeftShift_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitLeftShift)
gen_astm_Assign_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Assign)
gen_astm_MissingActualParameter_ActualParameter = Generalization(general=ActualParameter, specific=astm_MissingActualParameter)
gen_astm_ByValueActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=astm_ByValueActualParameterExpression)
gen_astm_ByReferenceActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=astm_ByReferenceActualParameterExpression)
gen_astm_SpecificTriggerDefinition_Definition = Generalization(general=Definition, specific=astm_SpecificTriggerDefinition)
gen_astm_SpecificLessEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_SpecificLessEqual)
gen_astm_SpecificGreaterEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_SpecificGreaterEqual)
gen_astm_SpecificIn_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_SpecificIn)
gen_astm_SpecificLike_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_SpecificLike)
gen_astm_SpecificConcatString_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_SpecificConcatString)
gen_astm_SpecificSelectStatement_Statement = Generalization(general=Statement, specific=astm_SpecificSelectStatement)

# Domain Model
domain_model = DomainModel(
    name="astm",
    types={astm_OtherSyntaxObject, astm_StorageSpecification, astm_DataType, astm_AccessKind, astm_UnaryOperator, astm_BinaryOperator, astm_ActualParameter, astm_SourceFile, GASTMSourceObject, astm_SourceLocation, astm_GASTMObject, astm_GASTMSourceObject, astm_GASTMSemanticObject, CompilationUnit, GlobalScope, astm_Scope, DefinitionObject, Scope, astm_GASTMSyntaxObject, GASTMObject, SourceFile, astm_Project, GASTMSemanticObject, AnnotationExpression, astm_CompilationUnit, OtherSyntaxObject, ProgramScope, astm_Name, astm_DeclarationOrDefinition, SourceLocation, PreprocessorElement, astm_Definition, DeclarationOrDefinition, Name, TypeReference, astm_Declaration, Definition, astm_VariableDeclaration, astm_FunctionDefinition, FormalParameterDefinition, Statement, FunctionScope, astm_FunctionDeclaration, Declaration, FormalParameterDeclaration, FunctionMemberAttributes, VirtualSpecification, astm_EntryDefinition, astm_DataDefinition, Expression, astm_FunctionMemberAttributes, astm_TypeDefinition, astm_NamedTypeDefinition, TypeDefinition, NamedType, astm_AggregateTypeDefinition, AggregateType, astm_NameSpaceDefinition, astm_BitFieldDefinition, DataDefinition, astm_EnumLiteralDefinition, astm_LabelDefinition, LabelType, astm_IncludeUnit, astm_MacroCall, MacroDefinition, astm_MacroDefinition, NameSpaceType, astm_Type, GASTMSyntaxObject, astm_PrimitiveType, DataType, astm_EnumType, EnumLiteralDefinition, astm_ConstructedType, astm_AggregateType, astm_Comment, astm_ArrayType, ConstructedType, Dimension, astm_Dimension, astm_FunctionType, Type, AggregateScope, astm_FormalParameterType, astm_NamedType, astm_ClassType, DerivesFrom, astm_DerivesFrom, FormalParameterType, astm_NamedTypeReference, astm_DeleteStatement, astm_UnnamedTypeReference, astm_JumpStatement, astm_BreakStatement, LabelAccess, astm_ContinueStatement, astm_LabeledStatement, astm_DeclarationOrDefinitionStatement, astm_ExpressionStatement, astm_BlockStatement, BlockScope, astm_EmptyStatement, astm_IfStatement, LabelDefinition, astm_SwitchStatement, SwitchCase, astm_SwitchCase, astm_CaseBlock, astm_ReturnStatement, astm_LoopStatement, astm_ForStatement, LoopStatement, astm_TryStatement, CatchBlock, astm_CatchBlock, astm_TypesCatchBlock, astm_VariableCatchBlock, astm_ThrowStatement, astm_Expression, astm_NameReference, astm_ArrayAccess, astm_QualifiedIdentifierReference, NameReference, IdentifierReference, astm_TypeQualifiedIdentifierReference, astm_Literal, astm_CastExpression, astm_UnaryExpression, astm_BinaryExpression, astm_OperatorAssign, BinaryOperator, astm_ConditionalExpression, astm_RangeExpression, astm_NewExpression, astm_FunctionCallExpression, ActualParameter, astm_ActualParameterExpression, astm_LabelAccess, astm_AnnotationExpression, astm_GlobalScope, astm_PreprocessorElement, astm_DefinitionObject, astm_ProgramScope, astm_TypeReference, astm_Statement, astm_FunctionScope, astm_NameSpaceType, astm_LabelType, astm_AggregateScope, astm_BlockScope, astm_IdentifierReference, astm_VirtualSpecification, astm_Float, astm_FormalParameterDefinition, astm_FormalParameterDeclaration, astm_Double, astm_VariableDefinition, astm_FunctionMemberAttribute, astm_External, StorageSpecification, astm_FunctionPersistent, astm_FileLocal, astm_PerClassMember, astm_NoDef, astm_Virtual, astm_PureVirtual, astm_NonVirtual, astm_ExceptionType, astm_Void, PrimitiveType, astm_Byte, astm_ShortInteger, astm_Integer, astm_LongInteger, astm_TerminateStatement, astm_LongDouble, astm_Character, astm_String, astm_Boolean, astm_WideCharacter, astm_CollectionType, astm_PointerType, astm_ReferenceType, astm_RangeType, astm_StructureType, astm_UnionType, astm_AnnotationType, astm_ByValueFormalParameterType, astm_ByReferenceFormalParameterType, astm_Public, AccessKind, astm_Protected, astm_Private, astm_BitNot, astm_AddressOf, astm_DefaultBlock, astm_WhileStatement, astm_DoWhileStatement, astm_ForCheckBeforeStatement, ForStatement, astm_ForCheckAfterStatement, astm_AggregateExpression, astm_QualifiedOverPointer, QualifiedIdentifierReference, astm_QualifiedOverData, astm_IntegerlLiteral, Literal, astm_StringLiteral, astm_CharLiteral, astm_RealLiteral, astm_BooleanLiteral, astm_BitLiteral, astm_UnaryPlus, UnaryOperator, astm_Negate, astm_Not, astm_Deref, astm_Increment, astm_Decrement, astm_PostIncrement, astm_PostDecrement, astm_Add, astm_Subtract, astm_Multiply, astm_Divide, astm_Modulus, astm_Exponent, astm_And, astm_Or, astm_Equal, astm_NotEqual, astm_Greater, astm_NotGreater, astm_Less, astm_NotLess, astm_BitAnd, astm_BitOr, astm_BitXor, astm_BitRightShift, astm_BitLeftShift, astm_Assign, astm_MissingActualParameter, astm_ByValueActualParameterExpression, ActualParameterExpression, astm_ByReferenceActualParameterExpression, astm_SpecificTriggerDefinition, astm_SpecificLessEqual, astm_SpecificGreaterEqual, astm_SpecificIn, astm_SpecificLike, astm_SpecificConcatString, astm_SpecificSelectStatement},
    associations={files1, outerScope2, definitionObject4, childScope5, inSourceFile0, annotations10, fragments12, opensScope14, locationInfo7, preProcessorElements8, identifierName20, definitionType21, defRef23, identifierName24, declarationType27, storageSpecifiers16, accessKind17, returnType33, formalParameters35, body37, functionMemberAttributes39, opensScope42, formalParameters30, functionMemberAttributes31, virtualSpecifier44, formalParameters45, body47, initialValue50, name55, definitionType57, aggregateType58, nameSpace59, bitFieldSize51, value53, labelName66, labelType68, file70, refersTo72, body61, nameSpaceType64, enumLiterals73, baseType74, ranks80, lowBound81, highBound83, returnType86, members76, opensScope78, type90, body92, derivesFrom93, parameterTypes88, type99, name101, type103, operand105, accessKind94, className96, target111, target113, target114, declOrDefn107, expression109, subStatements120, opensScope122, condition124, label116, thenBody126, statement117, elseBody129, body144, switchExpression132, cases134, body136, caseExpressions138, returnValue140, condition142, exceptions161, initBody147, iterationBody149, guardedStatement152, catchBlocks154, finalStatement156, body159, arrayName173, exceptionVariable163, exception164, expressionType166, name168, refersTo170, castType187, subscripts175, qualifiers178, member180, aggregateType182, member184, rightOperand202, expression189, operator192, operand194, operator197, leftOperand199, fromExpression215, operator205, condition207, onTrueOperand209, onFalseOperand212, toExpression217, calledFunction220, actualParams222, value224, memberValues238, newType226, actualParams228, name231, definition233, annotationType236, body241},
    generalizations={gen_astm_SourceFile_GASTMSourceObject, gen_astm_SourceLocation_GASTMSourceObject, gen_astm_Scope_GASTMSemanticObject, gen_astm_GASTMSyntaxObject_GASTMObject, gen_astm_Project_GASTMSemanticObject, gen_astm_CompilationUnit_OtherSyntaxObject, gen_astm_Name_OtherSyntaxObject, gen_astm_DeclarationOrDefinition_DefinitionObject, gen_astm_Definition_DeclarationOrDefinition, gen_astm_Declaration_DeclarationOrDefinition, gen_astm_VariableDeclaration_Declaration, gen_astm_FunctionDefinition_Definition, gen_astm_FunctionDeclaration_Declaration, gen_astm_EntryDefinition_Definition, gen_astm_DataDefinition_Definition, gen_astm_TypeDefinition_DefinitionObject, gen_astm_NamedTypeDefinition_TypeDefinition, gen_astm_AggregateTypeDefinition_TypeDefinition, gen_astm_NameSpaceDefinition_DefinitionObject, gen_astm_BitFieldDefinition_DataDefinition, gen_astm_EnumLiteralDefinition_Definition, gen_astm_LabelDefinition_DefinitionObject, gen_astm_IncludeUnit_PreprocessorElement, gen_astm_MacroCall_PreprocessorElement, gen_astm_MacroDefinition_PreprocessorElement, gen_astm_Type_GASTMSyntaxObject, gen_astm_PrimitiveType_DataType, gen_astm_EnumType_DataType, gen_astm_ConstructedType_DataType, gen_astm_AggregateType_DataType, gen_astm_Comment_PreprocessorElement, gen_astm_ArrayType_ConstructedType, gen_astm_Dimension_OtherSyntaxObject, gen_astm_FunctionType_Type, gen_astm_FormalParameterType_DataType, gen_astm_NamedType_DataType, gen_astm_ClassType_AggregateType, gen_astm_DerivesFrom_OtherSyntaxObject, gen_astm_NamedTypeReference_TypeReference, gen_astm_DeleteStatement_Statement, gen_astm_UnnamedTypeReference_TypeReference, gen_astm_JumpStatement_Statement, gen_astm_BreakStatement_Statement, gen_astm_ContinueStatement_Statement, gen_astm_LabeledStatement_Statement, gen_astm_DeclarationOrDefinitionStatement_Statement, gen_astm_ExpressionStatement_Statement, gen_astm_BlockStatement_Statement, gen_astm_EmptyStatement_Statement, gen_astm_IfStatement_Statement, gen_astm_SwitchStatement_Statement, gen_astm_SwitchCase_OtherSyntaxObject, gen_astm_CaseBlock_SwitchCase, gen_astm_ReturnStatement_Statement, gen_astm_LoopStatement_Statement, gen_astm_ForStatement_LoopStatement, gen_astm_TryStatement_Statement, gen_astm_CatchBlock_OtherSyntaxObject, gen_astm_TypesCatchBlock_CatchBlock, gen_astm_VariableCatchBlock_CatchBlock, gen_astm_ThrowStatement_Statement, gen_astm_Expression_GASTMSyntaxObject, gen_astm_NameReference_Expression, gen_astm_ArrayAccess_Expression, gen_astm_QualifiedIdentifierReference_NameReference, gen_astm_TypeQualifiedIdentifierReference_NameReference, gen_astm_Literal_Expression, gen_astm_CastExpression_Expression, gen_astm_UnaryExpression_Expression, gen_astm_BinaryExpression_Expression, gen_astm_OperatorAssign_BinaryOperator, gen_astm_ConditionalExpression_Expression, gen_astm_RangeExpression_Expression, gen_astm_FunctionCallExpression_Expression, gen_astm_ActualParameterExpression_ActualParameter, gen_astm_NewExpression_Expression, gen_astm_LabelAccess_Expression, gen_astm_AnnotationExpression_Expression, gen_astm_GlobalScope_Scope, gen_astm_PreprocessorElement_GASTMSyntaxObject, gen_astm_DefinitionObject_GASTMSyntaxObject, gen_astm_ProgramScope_Scope, gen_astm_TypeReference_Type, gen_astm_Statement_GASTMSyntaxObject, gen_astm_FunctionScope_Scope, gen_astm_NameSpaceType_Type, gen_astm_LabelType_Type, gen_astm_AggregateScope_Scope, gen_astm_BlockScope_Scope, gen_astm_IdentifierReference_NameReference, gen_astm_VirtualSpecification_OtherSyntaxObject, gen_astm_Float_PrimitiveType, gen_astm_FormalParameterDefinition_DataDefinition, gen_astm_FormalParameterDeclaration_Declaration, gen_astm_Double_PrimitiveType, gen_astm_VariableDefinition_DataDefinition, gen_astm_FunctionMemberAttribute_OtherSyntaxObject, gen_astm_External_StorageSpecification, gen_astm_FunctionPersistent_StorageSpecification, gen_astm_FileLocal_StorageSpecification, gen_astm_PerClassMember_StorageSpecification, gen_astm_NoDef_StorageSpecification, gen_astm_Virtual_VirtualSpecification, gen_astm_PureVirtual_VirtualSpecification, gen_astm_NonVirtual_VirtualSpecification, gen_astm_ExceptionType_DataType, gen_astm_Void_PrimitiveType, gen_astm_Byte_PrimitiveType, gen_astm_ShortInteger_PrimitiveType, gen_astm_Integer_PrimitiveType, gen_astm_LongInteger_PrimitiveType, gen_astm_TerminateStatement_Statement, gen_astm_LongDouble_PrimitiveType, gen_astm_Character_PrimitiveType, gen_astm_String_PrimitiveType, gen_astm_Boolean_PrimitiveType, gen_astm_WideCharacter_PrimitiveType, gen_astm_CollectionType_ConstructedType, gen_astm_PointerType_ConstructedType, gen_astm_ReferenceType_ConstructedType, gen_astm_RangeType_ConstructedType, gen_astm_StructureType_AggregateType, gen_astm_UnionType_AggregateType, gen_astm_AnnotationType_AggregateType, gen_astm_ByValueFormalParameterType_FormalParameterType, gen_astm_ByReferenceFormalParameterType_FormalParameterType, gen_astm_Public_AccessKind, gen_astm_Protected_AccessKind, gen_astm_Private_AccessKind, gen_astm_BitNot_UnaryOperator, gen_astm_AddressOf_UnaryOperator, gen_astm_DefaultBlock_SwitchCase, gen_astm_WhileStatement_LoopStatement, gen_astm_DoWhileStatement_LoopStatement, gen_astm_ForCheckBeforeStatement_ForStatement, gen_astm_ForCheckAfterStatement_ForStatement, gen_astm_AggregateExpression_Expression, gen_astm_QualifiedOverPointer_QualifiedIdentifierReference, gen_astm_QualifiedOverData_QualifiedIdentifierReference, gen_astm_IntegerlLiteral_Literal, gen_astm_StringLiteral_Literal, gen_astm_CharLiteral_Literal, gen_astm_RealLiteral_Literal, gen_astm_BooleanLiteral_Literal, gen_astm_BitLiteral_Literal, gen_astm_UnaryPlus_UnaryOperator, gen_astm_Negate_UnaryOperator, gen_astm_Not_UnaryOperator, gen_astm_Deref_UnaryOperator, gen_astm_Increment_UnaryOperator, gen_astm_Decrement_UnaryOperator, gen_astm_PostIncrement_UnaryOperator, gen_astm_PostDecrement_UnaryOperator, gen_astm_Add_BinaryOperator, gen_astm_Subtract_BinaryOperator, gen_astm_Multiply_BinaryOperator, gen_astm_Divide_BinaryOperator, gen_astm_Modulus_BinaryOperator, gen_astm_Exponent_BinaryOperator, gen_astm_And_BinaryOperator, gen_astm_Or_BinaryOperator, gen_astm_Equal_BinaryOperator, gen_astm_NotEqual_BinaryOperator, gen_astm_Greater_BinaryOperator, gen_astm_NotGreater_BinaryOperator, gen_astm_Less_BinaryOperator, gen_astm_NotLess_BinaryOperator, gen_astm_BitAnd_BinaryOperator, gen_astm_BitOr_BinaryOperator, gen_astm_BitXor_BinaryOperator, gen_astm_BitRightShift_BinaryOperator, gen_astm_BitLeftShift_BinaryOperator, gen_astm_Assign_BinaryOperator, gen_astm_MissingActualParameter_ActualParameter, gen_astm_ByValueActualParameterExpression_ActualParameterExpression, gen_astm_ByReferenceActualParameterExpression_ActualParameterExpression, gen_astm_SpecificTriggerDefinition_Definition, gen_astm_SpecificLessEqual_BinaryOperator, gen_astm_SpecificGreaterEqual_BinaryOperator, gen_astm_SpecificIn_BinaryOperator, gen_astm_SpecificLike_BinaryOperator, gen_astm_SpecificConcatString_BinaryOperator, gen_astm_SpecificSelectStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)