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
astm_Project = Class(name="astm::Project")
GASTMSemanticObject = Class(name="GASTMSemanticObject")
astm_GASTMObject = Class(name="astm::GASTMObject")
astm_GASTMSourceObject = Class(name="astm::GASTMSourceObject", is_abstract=True)
astm_GASTMSemanticObject = Class(name="astm::GASTMSemanticObject", is_abstract=True)
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
astm_PreprocessorElement = Class(name="astm::PreprocessorElement", is_abstract=True)
astm_AnnotationExpression = Class(name="astm::AnnotationExpression")
OtherSyntaxObject = Class(name="OtherSyntaxObject")
astm_CompilationUnit = Class(name="astm::CompilationUnit")
astm_GlobalScope = Class(name="astm::GlobalScope")
astm_Scope = Class(name="astm::Scope")
astm_DefinitionObject = Class(name="astm::DefinitionObject", is_abstract=True)
astm_GASTMSyntaxObject = Class(name="astm::GASTMSyntaxObject", is_abstract=True)
GASTMObject = Class(name="GASTMObject")
astm_Definition = Class(name="astm::Definition", is_abstract=True)
DeclarationOrDefinition = Class(name="DeclarationOrDefinition")
astm_TypeReference = Class(name="astm::TypeReference", is_abstract=True)
astm_Declaration = Class(name="astm::Declaration", is_abstract=True)
astm_ProgramScope = Class(name="astm::ProgramScope")
astm_Name = Class(name="astm::Name")
astm_DeclarationOrDefinition = Class(name="astm::DeclarationOrDefinition", is_abstract=True)
DefinitionObject = Class(name="DefinitionObject")
astm_VariableDeclaration = Class(name="astm::VariableDeclaration")
astm_FunctionDefinition = Class(name="astm::FunctionDefinition")
Definition = Class(name="Definition")
astm_FunctionDeclaration = Class(name="astm::FunctionDeclaration")
Declaration = Class(name="Declaration")
astm_FormalParameterDeclaration = Class(name="astm::FormalParameterDeclaration")
astm_FunctionMemberAttributes = Class(name="astm::FunctionMemberAttributes")
astm_VirtualSpecification = Class(name="astm::VirtualSpecification", is_abstract=True)
astm_EntryDefinition = Class(name="astm::EntryDefinition")
astm_FormalParameterDefinition = Class(name="astm::FormalParameterDefinition")
astm_Statement = Class(name="astm::Statement", is_abstract=True)
astm_FunctionScope = Class(name="astm::FunctionScope")
astm_NameSpaceDefinition = Class(name="astm::NameSpaceDefinition")
astm_DataDefinition = Class(name="astm::DataDefinition", is_abstract=True)
astm_Expression = Class(name="astm::Expression", is_abstract=True)
astm_BitFieldDefinition = Class(name="astm::BitFieldDefinition")
DataDefinition = Class(name="DataDefinition")
astm_EnumLiteralDefinition = Class(name="astm::EnumLiteralDefinition")
astm_TypeDefinition = Class(name="astm::TypeDefinition")
astm_NamedTypeDefinition = Class(name="astm::NamedTypeDefinition")
TypeDefinition = Class(name="TypeDefinition")
astm_NamedType = Class(name="astm::NamedType")
astm_AggregateTypeDefinition = Class(name="astm::AggregateTypeDefinition")
astm_AggregateType = Class(name="astm::AggregateType", is_abstract=True)
astm_EnumType = Class(name="astm::EnumType")
astm_ConstructedType = Class(name="astm::ConstructedType", is_abstract=True)
astm_AggregateScope = Class(name="astm::AggregateScope")
astm_ArrayType = Class(name="astm::ArrayType")
ConstructedType = Class(name="ConstructedType")
astm_NameSpaceType = Class(name="astm::NameSpaceType")
astm_LabelDefinition = Class(name="astm::LabelDefinition")
astm_LabelType = Class(name="astm::LabelType")
astm_IncludeUnit = Class(name="astm::IncludeUnit")
PreprocessorElement = Class(name="PreprocessorElement")
astm_MacroCall = Class(name="astm::MacroCall")
astm_MacroDefinition = Class(name="astm::MacroDefinition")
astm_Comment = Class(name="astm::Comment")
astm_Type = Class(name="astm::Type", is_abstract=True)
GASTMSyntaxObject = Class(name="GASTMSyntaxObject")
astm_PrimitiveType = Class(name="astm::PrimitiveType", is_abstract=True)
DataType = Class(name="DataType")
astm_UnnamedTypeReference = Class(name="astm::UnnamedTypeReference")
TypeReference = Class(name="TypeReference")
astm_NamedTypeReference = Class(name="astm::NamedTypeReference")
astm_Dimension = Class(name="astm::Dimension")
astm_FunctionType = Class(name="astm::FunctionType")
Type = Class(name="Type")
astm_FormalParameterType = Class(name="astm::FormalParameterType", is_abstract=True)
astm_ClassType = Class(name="astm::ClassType")
AggregateType = Class(name="AggregateType")
astm_DerivesFrom = Class(name="astm::DerivesFrom")
astm_LabelAccess = Class(name="astm::LabelAccess")
astm_ContinueStatement = Class(name="astm::ContinueStatement")
astm_LabeledStatement = Class(name="astm::LabeledStatement")
astm_DeleteStatement = Class(name="astm::DeleteStatement")
Statement = Class(name="Statement")
astm_DeclarationOrDefinitionStatement = Class(name="astm::DeclarationOrDefinitionStatement")
astm_ExpressionStatement = Class(name="astm::ExpressionStatement")
astm_JumpStatement = Class(name="astm::JumpStatement")
astm_BreakStatement = Class(name="astm::BreakStatement")
astm_EmptyStatement = Class(name="astm::EmptyStatement")
astm_IfStatement = Class(name="astm::IfStatement")
astm_BlockStatement = Class(name="astm::BlockStatement")
astm_BlockScope = Class(name="astm::BlockScope")
astm_ReturnStatement = Class(name="astm::ReturnStatement")
astm_SwitchStatement = Class(name="astm::SwitchStatement")
astm_SwitchCase = Class(name="astm::SwitchCase")
astm_ForStatement = Class(name="astm::ForStatement", is_abstract=True)
LoopStatement = Class(name="LoopStatement")
astm_CaseBlock = Class(name="astm::CaseBlock")
SwitchCase = Class(name="SwitchCase")
astm_LoopStatement = Class(name="astm::LoopStatement")
astm_TryStatement = Class(name="astm::TryStatement")
astm_CatchBlock = Class(name="astm::CatchBlock")
astm_ThrowStatement = Class(name="astm::ThrowStatement")
astm_TypesCatchBlock = Class(name="astm::TypesCatchBlock")
CatchBlock = Class(name="CatchBlock")
astm_VariableCatchBlock = Class(name="astm::VariableCatchBlock")
astm_ArrayAccess = Class(name="astm::ArrayAccess")
astm_NameReference = Class(name="astm::NameReference", is_abstract=True)
Expression = Class(name="Expression")
astm_QualifiedIdentifierReference = Class(name="astm::QualifiedIdentifierReference", is_abstract=True)
NameReference = Class(name="NameReference")
astm_IdentifierReference = Class(name="astm::IdentifierReference")
astm_Literal = Class(name="astm::Literal")
astm_CastExpression = Class(name="astm::CastExpression")
astm_TypeQualifiedIdentifierReference = Class(name="astm::TypeQualifiedIdentifierReference")
astm_BinaryExpression = Class(name="astm::BinaryExpression")
astm_UnaryExpression = Class(name="astm::UnaryExpression")
astm_OperatorAssign = Class(name="astm::OperatorAssign")
BinaryOperator = Class(name="BinaryOperator")
astm_ConditionalExpression = Class(name="astm::ConditionalExpression")
astm_RangeExpression = Class(name="astm::RangeExpression")
astm_ActualParameterExpression = Class(name="astm::ActualParameterExpression")
ActualParameter = Class(name="ActualParameter")
astm_FunctionCallExpression = Class(name="astm::FunctionCallExpression")
astm_NewExpression = Class(name="astm::NewExpression")
Scope = Class(name="Scope")
astm_External = Class(name="astm::External")
StorageSpecification = Class(name="StorageSpecification")
astm_FunctionPersistent = Class(name="astm::FunctionPersistent")
astm_FileLocal = Class(name="astm::FileLocal")
astm_PerClassMember = Class(name="astm::PerClassMember")
astm_NoDef = Class(name="astm::NoDef")
astm_Virtual = Class(name="astm::Virtual")
VirtualSpecification = Class(name="VirtualSpecification")
astm_VariableDefinition = Class(name="astm::VariableDefinition")
astm_FunctionMemberAttribute = Class(name="astm::FunctionMemberAttribute")
astm_LongDouble = Class(name="astm::LongDouble")
astm_Character = Class(name="astm::Character")
astm_String = Class(name="astm::String")
astm_Boolean = Class(name="astm::Boolean")
astm_WideCharacter = Class(name="astm::WideCharacter")
astm_CollectionType = Class(name="astm::CollectionType")
astm_PureVirtual = Class(name="astm::PureVirtual")
astm_NonVirtual = Class(name="astm::NonVirtual")
astm_ExceptionType = Class(name="astm::ExceptionType")
astm_Void = Class(name="astm::Void")
PrimitiveType = Class(name="PrimitiveType")
astm_Byte = Class(name="astm::Byte")
astm_ShortInteger = Class(name="astm::ShortInteger")
astm_Integer = Class(name="astm::Integer")
astm_LongInteger = Class(name="astm::LongInteger")
astm_Float = Class(name="astm::Float")
astm_Double = Class(name="astm::Double")
astm_DefaultBlock = Class(name="astm::DefaultBlock")
astm_WhileStatement = Class(name="astm::WhileStatement")
astm_DoWhileStatement = Class(name="astm::DoWhileStatement")
astm_ForCheckBeforeStatement = Class(name="astm::ForCheckBeforeStatement")
ForStatement = Class(name="ForStatement")
astm_ForCheckAfterStatement = Class(name="astm::ForCheckAfterStatement")
astm_AggregateExpression = Class(name="astm::AggregateExpression")
astm_PointerType = Class(name="astm::PointerType")
astm_ReferenceType = Class(name="astm::ReferenceType")
astm_RangeType = Class(name="astm::RangeType")
astm_StructureType = Class(name="astm::StructureType")
astm_UnionType = Class(name="astm::UnionType")
astm_AnnotationType = Class(name="astm::AnnotationType")
astm_ByValueFormalParameterType = Class(name="astm::ByValueFormalParameterType")
FormalParameterType = Class(name="FormalParameterType")
astm_ByReferenceFormalParameterType = Class(name="astm::ByReferenceFormalParameterType")
astm_Public = Class(name="astm::Public")
AccessKind = Class(name="AccessKind")
astm_Protected = Class(name="astm::Protected")
astm_Private = Class(name="astm::Private")
astm_TerminateStatement = Class(name="astm::TerminateStatement")
astm_AddressOf = Class(name="astm::AddressOf")
astm_Deref = Class(name="astm::Deref")
astm_Increment = Class(name="astm::Increment")
astm_Decrement = Class(name="astm::Decrement")
astm_PostIncrement = Class(name="astm::PostIncrement")
astm_PostDecrement = Class(name="astm::PostDecrement")
astm_Add = Class(name="astm::Add")
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
astm_BitNot = Class(name="astm::BitNot")
astm_NotLess = Class(name="astm::NotLess")
astm_BitAnd = Class(name="astm::BitAnd")
astm_BitOr = Class(name="astm::BitOr")
astm_BitXor = Class(name="astm::BitXor")
astm_BitLeftShift = Class(name="astm::BitLeftShift")
astm_BitRightShift = Class(name="astm::BitRightShift")
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
astm_Assign = Class(name="astm::Assign")
astm_MissingActualParameter = Class(name="astm::MissingActualParameter")
astm_ByValueActualParameterExpression = Class(name="astm::ByValueActualParameterExpression")
ActualParameterExpression = Class(name="ActualParameterExpression")
astm_ByReferenceActualParameterExpression = Class(name="astm::ByReferenceActualParameterExpression")
astm_SpecificClassType = Class(name="astm::SpecificClassType")
ClassType = Class(name="ClassType")

# astm_Project class attributes and methods

# GASTMSemanticObject class attributes and methods

# astm_GASTMObject class attributes and methods

# astm_GASTMSourceObject class attributes and methods

# astm_GASTMSemanticObject class attributes and methods

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
astm_SourceLocation.attributes={astm_SourceLocation_startColumn, astm_SourceLocation_startLine, astm_SourceLocation_endLine, astm_SourceLocation_endColumn}

# astm_PreprocessorElement class attributes and methods

# astm_AnnotationExpression class attributes and methods

# OtherSyntaxObject class attributes and methods

# astm_CompilationUnit class attributes and methods
astm_CompilationUnit_language: Property = Property(name="language", type=StringType)
astm_CompilationUnit.attributes={astm_CompilationUnit_language}

# astm_GlobalScope class attributes and methods

# astm_Scope class attributes and methods

# astm_DefinitionObject class attributes and methods

# astm_GASTMSyntaxObject class attributes and methods

# GASTMObject class attributes and methods

# astm_Definition class attributes and methods

# DeclarationOrDefinition class attributes and methods

# astm_TypeReference class attributes and methods

# astm_Declaration class attributes and methods

# astm_ProgramScope class attributes and methods

# astm_Name class attributes and methods
astm_Name_nameString: Property = Property(name="nameString", type=StringType)
astm_Name.attributes={astm_Name_nameString}

# astm_DeclarationOrDefinition class attributes and methods
astm_DeclarationOrDefinition_isRegister: Property = Property(name="isRegister", type=BooleanType)
astm_DeclarationOrDefinition_linkageSpecifier: Property = Property(name="linkageSpecifier", type=StringType)
astm_DeclarationOrDefinition.attributes={astm_DeclarationOrDefinition_linkageSpecifier, astm_DeclarationOrDefinition_isRegister}

# DefinitionObject class attributes and methods

# astm_VariableDeclaration class attributes and methods
astm_VariableDeclaration_isMutable: Property = Property(name="isMutable", type=BooleanType)
astm_VariableDeclaration.attributes={astm_VariableDeclaration_isMutable}

# astm_FunctionDefinition class attributes and methods

# Definition class attributes and methods

# astm_FunctionDeclaration class attributes and methods

# Declaration class attributes and methods

# astm_FormalParameterDeclaration class attributes and methods

# astm_FunctionMemberAttributes class attributes and methods
astm_FunctionMemberAttributes_isFriend: Property = Property(name="isFriend", type=BooleanType)
astm_FunctionMemberAttributes_isInline: Property = Property(name="isInline", type=BooleanType)
astm_FunctionMemberAttributes_isThisConst: Property = Property(name="isThisConst", type=BooleanType)
astm_FunctionMemberAttributes.attributes={astm_FunctionMemberAttributes_isThisConst, astm_FunctionMemberAttributes_isInline, astm_FunctionMemberAttributes_isFriend}

# astm_VirtualSpecification class attributes and methods

# astm_EntryDefinition class attributes and methods

# astm_FormalParameterDefinition class attributes and methods

# astm_Statement class attributes and methods

# astm_FunctionScope class attributes and methods

# astm_NameSpaceDefinition class attributes and methods

# astm_DataDefinition class attributes and methods
astm_DataDefinition_isMutable: Property = Property(name="isMutable", type=BooleanType)
astm_DataDefinition.attributes={astm_DataDefinition_isMutable}

# astm_Expression class attributes and methods

# astm_BitFieldDefinition class attributes and methods

# DataDefinition class attributes and methods

# astm_EnumLiteralDefinition class attributes and methods

# astm_TypeDefinition class attributes and methods

# astm_NamedTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# astm_NamedType class attributes and methods

# astm_AggregateTypeDefinition class attributes and methods

# astm_AggregateType class attributes and methods

# astm_EnumType class attributes and methods

# astm_ConstructedType class attributes and methods

# astm_AggregateScope class attributes and methods

# astm_ArrayType class attributes and methods

# ConstructedType class attributes and methods

# astm_NameSpaceType class attributes and methods

# astm_LabelDefinition class attributes and methods

# astm_LabelType class attributes and methods

# astm_IncludeUnit class attributes and methods

# PreprocessorElement class attributes and methods

# astm_MacroCall class attributes and methods

# astm_MacroDefinition class attributes and methods
astm_MacroDefinition_macroName: Property = Property(name="macroName", type=StringType)
astm_MacroDefinition_body: Property = Property(name="body", type=StringType)
astm_MacroDefinition.attributes={astm_MacroDefinition_body, astm_MacroDefinition_macroName}

# astm_Comment class attributes and methods
astm_Comment_text: Property = Property(name="text", type=StringType)
astm_Comment.attributes={astm_Comment_text}

# astm_Type class attributes and methods
astm_Type_isConst: Property = Property(name="isConst", type=BooleanType)
astm_Type_isVolatile: Property = Property(name="isVolatile", type=BooleanType)
astm_Type.attributes={astm_Type_isConst, astm_Type_isVolatile}

# GASTMSyntaxObject class attributes and methods

# astm_PrimitiveType class attributes and methods
astm_PrimitiveType_isSigned: Property = Property(name="isSigned", type=BooleanType)
astm_PrimitiveType.attributes={astm_PrimitiveType_isSigned}

# DataType class attributes and methods

# astm_UnnamedTypeReference class attributes and methods

# TypeReference class attributes and methods

# astm_NamedTypeReference class attributes and methods

# astm_Dimension class attributes and methods

# astm_FunctionType class attributes and methods

# Type class attributes and methods

# astm_FormalParameterType class attributes and methods

# astm_ClassType class attributes and methods

# AggregateType class attributes and methods

# astm_DerivesFrom class attributes and methods
astm_DerivesFrom_isVirtual: Property = Property(name="isVirtual", type=BooleanType)
astm_DerivesFrom.attributes={astm_DerivesFrom_isVirtual}

# astm_LabelAccess class attributes and methods

# astm_ContinueStatement class attributes and methods

# astm_LabeledStatement class attributes and methods

# astm_DeleteStatement class attributes and methods

# Statement class attributes and methods

# astm_DeclarationOrDefinitionStatement class attributes and methods

# astm_ExpressionStatement class attributes and methods

# astm_JumpStatement class attributes and methods

# astm_BreakStatement class attributes and methods

# astm_EmptyStatement class attributes and methods

# astm_IfStatement class attributes and methods

# astm_BlockStatement class attributes and methods

# astm_BlockScope class attributes and methods

# astm_ReturnStatement class attributes and methods

# astm_SwitchStatement class attributes and methods

# astm_SwitchCase class attributes and methods

# astm_ForStatement class attributes and methods

# LoopStatement class attributes and methods

# astm_CaseBlock class attributes and methods

# SwitchCase class attributes and methods

# astm_LoopStatement class attributes and methods

# astm_TryStatement class attributes and methods

# astm_CatchBlock class attributes and methods

# astm_ThrowStatement class attributes and methods

# astm_TypesCatchBlock class attributes and methods

# CatchBlock class attributes and methods

# astm_VariableCatchBlock class attributes and methods

# astm_ArrayAccess class attributes and methods

# astm_NameReference class attributes and methods

# Expression class attributes and methods

# astm_QualifiedIdentifierReference class attributes and methods

# NameReference class attributes and methods

# astm_IdentifierReference class attributes and methods

# astm_Literal class attributes and methods
astm_Literal_value: Property = Property(name="value", type=StringType)
astm_Literal.attributes={astm_Literal_value}

# astm_CastExpression class attributes and methods

# astm_TypeQualifiedIdentifierReference class attributes and methods

# astm_BinaryExpression class attributes and methods

# astm_UnaryExpression class attributes and methods

# astm_OperatorAssign class attributes and methods

# BinaryOperator class attributes and methods

# astm_ConditionalExpression class attributes and methods

# astm_RangeExpression class attributes and methods

# astm_ActualParameterExpression class attributes and methods

# ActualParameter class attributes and methods

# astm_FunctionCallExpression class attributes and methods

# astm_NewExpression class attributes and methods

# Scope class attributes and methods

# astm_External class attributes and methods

# StorageSpecification class attributes and methods

# astm_FunctionPersistent class attributes and methods

# astm_FileLocal class attributes and methods

# astm_PerClassMember class attributes and methods

# astm_NoDef class attributes and methods

# astm_Virtual class attributes and methods

# VirtualSpecification class attributes and methods

# astm_VariableDefinition class attributes and methods

# astm_FunctionMemberAttribute class attributes and methods

# astm_LongDouble class attributes and methods

# astm_Character class attributes and methods

# astm_String class attributes and methods

# astm_Boolean class attributes and methods

# astm_WideCharacter class attributes and methods

# astm_CollectionType class attributes and methods

# astm_PureVirtual class attributes and methods

# astm_NonVirtual class attributes and methods

# astm_ExceptionType class attributes and methods

# astm_Void class attributes and methods

# PrimitiveType class attributes and methods

# astm_Byte class attributes and methods

# astm_ShortInteger class attributes and methods

# astm_Integer class attributes and methods

# astm_LongInteger class attributes and methods

# astm_Float class attributes and methods

# astm_Double class attributes and methods

# astm_DefaultBlock class attributes and methods

# astm_WhileStatement class attributes and methods

# astm_DoWhileStatement class attributes and methods

# astm_ForCheckBeforeStatement class attributes and methods

# ForStatement class attributes and methods

# astm_ForCheckAfterStatement class attributes and methods

# astm_AggregateExpression class attributes and methods

# astm_PointerType class attributes and methods

# astm_ReferenceType class attributes and methods

# astm_RangeType class attributes and methods

# astm_StructureType class attributes and methods

# astm_UnionType class attributes and methods

# astm_AnnotationType class attributes and methods

# astm_ByValueFormalParameterType class attributes and methods

# FormalParameterType class attributes and methods

# astm_ByReferenceFormalParameterType class attributes and methods

# astm_Public class attributes and methods

# AccessKind class attributes and methods

# astm_Protected class attributes and methods

# astm_Private class attributes and methods

# astm_TerminateStatement class attributes and methods

# astm_AddressOf class attributes and methods

# astm_Deref class attributes and methods

# astm_Increment class attributes and methods

# astm_Decrement class attributes and methods

# astm_PostIncrement class attributes and methods

# astm_PostDecrement class attributes and methods

# astm_Add class attributes and methods

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

# astm_BitNot class attributes and methods

# astm_NotLess class attributes and methods

# astm_BitAnd class attributes and methods

# astm_BitOr class attributes and methods

# astm_BitXor class attributes and methods

# astm_BitLeftShift class attributes and methods

# astm_BitRightShift class attributes and methods

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

# astm_Assign class attributes and methods

# astm_MissingActualParameter class attributes and methods

# astm_ByValueActualParameterExpression class attributes and methods

# ActualParameterExpression class attributes and methods

# astm_ByReferenceActualParameterExpression class attributes and methods

# astm_SpecificClassType class attributes and methods
astm_SpecificClassType_package: Property = Property(name="package", type=StringType)
astm_SpecificClassType_imports: Property = Property(name="imports", type=StringType)
astm_SpecificClassType.attributes={astm_SpecificClassType_imports, astm_SpecificClassType_package}

# ClassType class attributes and methods

# Relationships
inSourceFile0: BinaryAssociation = BinaryAssociation(
    name="inSourceFile0",
    ends={
        Property(name="astm_SourceFile", type=astm_SourceLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SourceLocation", type=astm_SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preProcessorElements10: BinaryAssociation = BinaryAssociation(
    name="preProcessorElements10",
    ends={
        Property(name="astm_PreprocessorElement", type=astm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_GASTMSyntaxObject11", type=astm_PreprocessorElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations12: BinaryAssociation = BinaryAssociation(
    name="annotations12",
    ends={
        Property(name="astm_AnnotationExpression", type=astm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_GASTMSyntaxObject13", type=astm_AnnotationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files1: BinaryAssociation = BinaryAssociation(
    name="files1",
    ends={
        Property(name="astm_CompilationUnit", type=astm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Project", type=astm_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outerScope2: BinaryAssociation = BinaryAssociation(
    name="outerScope2",
    ends={
        Property(name="astm_GlobalScope", type=astm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Project3", type=astm_GlobalScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionObject4: BinaryAssociation = BinaryAssociation(
    name="definitionObject4",
    ends={
        Property(name="astm_DefinitionObject", type=astm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Scope", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childScope6: BinaryAssociation = BinaryAssociation(
    name="childScope6",
    ends={
        Property(name="astm_Scope7", type=astm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Scope5", type=astm_Scope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locationInfo8: BinaryAssociation = BinaryAssociation(
    name="locationInfo8",
    ends={
        Property(name="astm_SourceLocation9", type=astm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_GASTMSyntaxObject", type=astm_SourceLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessKind20: BinaryAssociation = BinaryAssociation(
    name="accessKind20",
    ends={
        Property(name="astm_OtherSyntaxObject22", type=astm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeclarationOrDefinition21", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierName23: BinaryAssociation = BinaryAssociation(
    name="identifierName23",
    ends={
        Property(name="astm_Name", type=astm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Definition", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType24: BinaryAssociation = BinaryAssociation(
    name="definitionType24",
    ends={
        Property(name="astm_TypeReference", type=astm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Definition25", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments14: BinaryAssociation = BinaryAssociation(
    name="fragments14",
    ends={
        Property(name="astm_DefinitionObject16", type=astm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CompilationUnit15", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope17: BinaryAssociation = BinaryAssociation(
    name="opensScope17",
    ends={
        Property(name="astm_ProgramScope", type=astm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CompilationUnit18", type=astm_ProgramScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
storageSpecifiers19: BinaryAssociation = BinaryAssociation(
    name="storageSpecifiers19",
    ends={
        Property(name="astm_OtherSyntaxObject", type=astm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeclarationOrDefinition", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defRef26: BinaryAssociation = BinaryAssociation(
    name="defRef26",
    ends={
        Property(name="astm_Definition27", type=astm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Declaration", type=astm_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierName28: BinaryAssociation = BinaryAssociation(
    name="identifierName28",
    ends={
        Property(name="astm_Name30", type=astm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Declaration29", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarationType31: BinaryAssociation = BinaryAssociation(
    name="declarationType31",
    ends={
        Property(name="astm_TypeReference33", type=astm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Declaration32", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters34: BinaryAssociation = BinaryAssociation(
    name="formalParameters34",
    ends={
        Property(name="astm_FormalParameterDeclaration", type=astm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDeclaration", type=astm_FormalParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes35: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes35",
    ends={
        Property(name="astm_FunctionMemberAttributes", type=astm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDeclaration36", type=astm_FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opensScope46: BinaryAssociation = BinaryAssociation(
    name="opensScope46",
    ends={
        Property(name="astm_FunctionScope", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition47", type=astm_FunctionScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
virtualSpecifier48: BinaryAssociation = BinaryAssociation(
    name="virtualSpecifier48",
    ends={
        Property(name="astm_VirtualSpecification", type=astm_FunctionMemberAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionMemberAttributes49", type=astm_VirtualSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters50: BinaryAssociation = BinaryAssociation(
    name="formalParameters50",
    ends={
        Property(name="astm_FormalParameterDefinition51", type=astm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EntryDefinition", type=astm_FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body52: BinaryAssociation = BinaryAssociation(
    name="body52",
    ends={
        Property(name="astm_Statement54", type=astm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EntryDefinition53", type=astm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType37: BinaryAssociation = BinaryAssociation(
    name="returnType37",
    ends={
        Property(name="astm_TypeReference38", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters39: BinaryAssociation = BinaryAssociation(
    name="formalParameters39",
    ends={
        Property(name="astm_FormalParameterDefinition", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition40", type=astm_FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body41: BinaryAssociation = BinaryAssociation(
    name="body41",
    ends={
        Property(name="astm_Statement", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition42", type=astm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes43: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes43",
    ends={
        Property(name="astm_FunctionMemberAttributes45", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition44", type=astm_FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameSpace64: BinaryAssociation = BinaryAssociation(
    name="nameSpace64",
    ends={
        Property(name="astm_Name65", type=astm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameSpaceDefinition", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body66: BinaryAssociation = BinaryAssociation(
    name="body66",
    ends={
        Property(name="astm_DefinitionObject68", type=astm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameSpaceDefinition67", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue55: BinaryAssociation = BinaryAssociation(
    name="initialValue55",
    ends={
        Property(name="astm_Expression", type=astm_DataDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DataDefinition", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bitFieldSize56: BinaryAssociation = BinaryAssociation(
    name="bitFieldSize56",
    ends={
        Property(name="astm_Expression57", type=astm_BitFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BitFieldDefinition", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value58: BinaryAssociation = BinaryAssociation(
    name="value58",
    ends={
        Property(name="astm_Expression59", type=astm_EnumLiteralDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EnumLiteralDefinition", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name60: BinaryAssociation = BinaryAssociation(
    name="name60",
    ends={
        Property(name="astm_Name61", type=astm_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypeDefinition", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType62: BinaryAssociation = BinaryAssociation(
    name="definitionType62",
    ends={
        Property(name="astm_NamedType", type=astm_NamedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedTypeDefinition", type=astm_NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType63: BinaryAssociation = BinaryAssociation(
    name="aggregateType63",
    ends={
        Property(name="astm_AggregateType", type=astm_AggregateTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AggregateTypeDefinition", type=astm_AggregateType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumLiterals78: BinaryAssociation = BinaryAssociation(
    name="enumLiterals78",
    ends={
        Property(name="astm_EnumLiteralDefinition79", type=astm_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EnumType", type=astm_EnumLiteralDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType80: BinaryAssociation = BinaryAssociation(
    name="baseType80",
    ends={
        Property(name="astm_TypeReference81", type=astm_ConstructedType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConstructedType", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members82: BinaryAssociation = BinaryAssociation(
    name="members82",
    ends={
        Property(name="astm_DefinitionObject84", type=astm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AggregateType83", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope85: BinaryAssociation = BinaryAssociation(
    name="opensScope85",
    ends={
        Property(name="astm_AggregateScope", type=astm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AggregateType86", type=astm_AggregateScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameSpaceType69: BinaryAssociation = BinaryAssociation(
    name="nameSpaceType69",
    ends={
        Property(name="astm_NameSpaceType", type=astm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameSpaceDefinition70", type=astm_NameSpaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelName71: BinaryAssociation = BinaryAssociation(
    name="labelName71",
    ends={
        Property(name="astm_Name72", type=astm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelDefinition", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelType73: BinaryAssociation = BinaryAssociation(
    name="labelType73",
    ends={
        Property(name="astm_LabelType", type=astm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelDefinition74", type=astm_LabelType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file75: BinaryAssociation = BinaryAssociation(
    name="file75",
    ends={
        Property(name="astm_SourceFile76", type=astm_IncludeUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IncludeUnit", type=astm_SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo77: BinaryAssociation = BinaryAssociation(
    name="refersTo77",
    ends={
        Property(name="astm_MacroDefinition", type=astm_MacroCall, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_MacroCall", type=astm_MacroDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessKind104: BinaryAssociation = BinaryAssociation(
    name="accessKind104",
    ends={
        Property(name="astm_OtherSyntaxObject106", type=astm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DerivesFrom105", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className107: BinaryAssociation = BinaryAssociation(
    name="className107",
    ends={
        Property(name="astm_NamedType109", type=astm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DerivesFrom108", type=astm_NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type110: BinaryAssociation = BinaryAssociation(
    name="type110",
    ends={
        Property(name="astm_Type111", type=astm_UnnamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_UnnamedTypeReference", type=astm_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name112: BinaryAssociation = BinaryAssociation(
    name="name112",
    ends={
        Property(name="astm_Name113", type=astm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedTypeReference", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ranks87: BinaryAssociation = BinaryAssociation(
    name="ranks87",
    ends={
        Property(name="astm_Dimension", type=astm_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ArrayType", type=astm_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lowBound88: BinaryAssociation = BinaryAssociation(
    name="lowBound88",
    ends={
        Property(name="astm_Expression90", type=astm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Dimension89", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
highBound91: BinaryAssociation = BinaryAssociation(
    name="highBound91",
    ends={
        Property(name="astm_Expression93", type=astm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Dimension92", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType94: BinaryAssociation = BinaryAssociation(
    name="returnType94",
    ends={
        Property(name="astm_TypeReference95", type=astm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionType", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterTypes96: BinaryAssociation = BinaryAssociation(
    name="parameterTypes96",
    ends={
        Property(name="astm_FormalParameterType", type=astm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionType97", type=astm_FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type98: BinaryAssociation = BinaryAssociation(
    name="type98",
    ends={
        Property(name="astm_TypeReference100", type=astm_FormalParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FormalParameterType99", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body101: BinaryAssociation = BinaryAssociation(
    name="body101",
    ends={
        Property(name="astm_Type", type=astm_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedType102", type=astm_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivesFrom103: BinaryAssociation = BinaryAssociation(
    name="derivesFrom103",
    ends={
        Property(name="astm_DerivesFrom", type=astm_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ClassType", type=astm_DerivesFrom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target125: BinaryAssociation = BinaryAssociation(
    name="target125",
    ends={
        Property(name="astm_LabelAccess", type=astm_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BreakStatement", type=astm_LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target126: BinaryAssociation = BinaryAssociation(
    name="target126",
    ends={
        Property(name="astm_LabelAccess127", type=astm_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ContinueStatement", type=astm_LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type114: BinaryAssociation = BinaryAssociation(
    name="type114",
    ends={
        Property(name="astm_TypeDefinition116", type=astm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedTypeReference115", type=astm_TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
label128: BinaryAssociation = BinaryAssociation(
    name="label128",
    ends={
        Property(name="astm_LabelDefinition129", type=astm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabeledStatement", type=astm_LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand117: BinaryAssociation = BinaryAssociation(
    name="operand117",
    ends={
        Property(name="astm_Expression118", type=astm_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeleteStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declOrDefn119: BinaryAssociation = BinaryAssociation(
    name="declOrDefn119",
    ends={
        Property(name="astm_DefinitionObject120", type=astm_DeclarationOrDefinitionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeclarationOrDefinitionStatement", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression121: BinaryAssociation = BinaryAssociation(
    name="expression121",
    ends={
        Property(name="astm_Expression122", type=astm_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ExpressionStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target123: BinaryAssociation = BinaryAssociation(
    name="target123",
    ends={
        Property(name="astm_Expression124", type=astm_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_JumpStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition137: BinaryAssociation = BinaryAssociation(
    name="condition137",
    ends={
        Property(name="astm_Expression138", type=astm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IfStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBody139: BinaryAssociation = BinaryAssociation(
    name="thenBody139",
    ends={
        Property(name="astm_Statement141", type=astm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IfStatement140", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBody142: BinaryAssociation = BinaryAssociation(
    name="elseBody142",
    ends={
        Property(name="astm_Statement144", type=astm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IfStatement143", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement130: BinaryAssociation = BinaryAssociation(
    name="statement130",
    ends={
        Property(name="astm_Statement132", type=astm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabeledStatement131", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subStatements133: BinaryAssociation = BinaryAssociation(
    name="subStatements133",
    ends={
        Property(name="astm_Statement134", type=astm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BlockStatement", type=astm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope135: BinaryAssociation = BinaryAssociation(
    name="opensScope135",
    ends={
        Property(name="astm_BlockScope", type=astm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BlockStatement136", type=astm_BlockScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseExpressions152: BinaryAssociation = BinaryAssociation(
    name="caseExpressions152",
    ends={
        Property(name="astm_Expression153", type=astm_CaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CaseBlock", type=astm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
switchExpression145: BinaryAssociation = BinaryAssociation(
    name="switchExpression145",
    ends={
        Property(name="astm_Expression146", type=astm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SwitchStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases147: BinaryAssociation = BinaryAssociation(
    name="cases147",
    ends={
        Property(name="astm_SwitchCase", type=astm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SwitchStatement148", type=astm_SwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body149: BinaryAssociation = BinaryAssociation(
    name="body149",
    ends={
        Property(name="astm_Statement151", type=astm_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SwitchCase150", type=astm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initBody161: BinaryAssociation = BinaryAssociation(
    name="initBody161",
    ends={
        Property(name="astm_Expression162", type=astm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ForStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationBody163: BinaryAssociation = BinaryAssociation(
    name="iterationBody163",
    ends={
        Property(name="astm_Expression165", type=astm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ForStatement164", type=astm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue154: BinaryAssociation = BinaryAssociation(
    name="returnValue154",
    ends={
        Property(name="astm_Expression155", type=astm_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ReturnStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition156: BinaryAssociation = BinaryAssociation(
    name="condition156",
    ends={
        Property(name="astm_Expression157", type=astm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LoopStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body158: BinaryAssociation = BinaryAssociation(
    name="body158",
    ends={
        Property(name="astm_Statement160", type=astm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LoopStatement159", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalStatement170: BinaryAssociation = BinaryAssociation(
    name="finalStatement170",
    ends={
        Property(name="astm_Statement172", type=astm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TryStatement171", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body173: BinaryAssociation = BinaryAssociation(
    name="body173",
    ends={
        Property(name="astm_Statement175", type=astm_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CatchBlock174", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guardedStatement166: BinaryAssociation = BinaryAssociation(
    name="guardedStatement166",
    ends={
        Property(name="astm_Statement167", type=astm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TryStatement", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchBlocks168: BinaryAssociation = BinaryAssociation(
    name="catchBlocks168",
    ends={
        Property(name="astm_CatchBlock", type=astm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TryStatement169", type=astm_CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionVariable178: BinaryAssociation = BinaryAssociation(
    name="exceptionVariable178",
    ends={
        Property(name="astm_VariableCatchBlock", type=astm_DataDefinition, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="astm_DataDefinition179", type=astm_VariableCatchBlock, multiplicity=Multiplicity(1, 1))
    }
)
exception180: BinaryAssociation = BinaryAssociation(
    name="exception180",
    ends={
        Property(name="astm_Expression181", type=astm_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ThrowStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions176: BinaryAssociation = BinaryAssociation(
    name="exceptions176",
    ends={
        Property(name="astm_Type177", type=astm_TypesCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypesCatchBlock", type=astm_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name185: BinaryAssociation = BinaryAssociation(
    name="name185",
    ends={
        Property(name="astm_Name186", type=astm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameReference", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo187: BinaryAssociation = BinaryAssociation(
    name="refersTo187",
    ends={
        Property(name="astm_DefinitionObject189", type=astm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameReference188", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 1))
    }
)
expressionType182: BinaryAssociation = BinaryAssociation(
    name="expressionType182",
    ends={
        Property(name="astm_TypeReference184", type=astm_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Expression183", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiers195: BinaryAssociation = BinaryAssociation(
    name="qualifiers195",
    ends={
        Property(name="astm_Expression196", type=astm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_QualifiedIdentifierReference", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member197: BinaryAssociation = BinaryAssociation(
    name="member197",
    ends={
        Property(name="astm_IdentifierReference", type=astm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_QualifiedIdentifierReference198", type=astm_IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayName190: BinaryAssociation = BinaryAssociation(
    name="arrayName190",
    ends={
        Property(name="astm_Expression191", type=astm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ArrayAccess", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subscripts192: BinaryAssociation = BinaryAssociation(
    name="subscripts192",
    ends={
        Property(name="astm_Expression194", type=astm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ArrayAccess193", type=astm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
castType204: BinaryAssociation = BinaryAssociation(
    name="castType204",
    ends={
        Property(name="astm_TypeReference205", type=astm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CastExpression", type=astm_TypeReference, multiplicity=Multiplicity(0, 1))
    }
)
aggregateType199: BinaryAssociation = BinaryAssociation(
    name="aggregateType199",
    ends={
        Property(name="astm_TypeReference200", type=astm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypeQualifiedIdentifierReference", type=astm_TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member201: BinaryAssociation = BinaryAssociation(
    name="member201",
    ends={
        Property(name="astm_IdentifierReference203", type=astm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypeQualifiedIdentifierReference202", type=astm_IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand211: BinaryAssociation = BinaryAssociation(
    name="operand211",
    ends={
        Property(name="astm_Expression213", type=astm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_UnaryExpression212", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression206: BinaryAssociation = BinaryAssociation(
    name="expression206",
    ends={
        Property(name="astm_Expression208", type=astm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CastExpression207", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator209: BinaryAssociation = BinaryAssociation(
    name="operator209",
    ends={
        Property(name="astm_OtherSyntaxObject210", type=astm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_UnaryExpression", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator222: BinaryAssociation = BinaryAssociation(
    name="operator222",
    ends={
        Property(name="astm_OtherSyntaxObject223", type=astm_OperatorAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_OperatorAssign", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator214: BinaryAssociation = BinaryAssociation(
    name="operator214",
    ends={
        Property(name="astm_OtherSyntaxObject215", type=astm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BinaryExpression", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand216: BinaryAssociation = BinaryAssociation(
    name="leftOperand216",
    ends={
        Property(name="astm_Expression218", type=astm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BinaryExpression217", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand219: BinaryAssociation = BinaryAssociation(
    name="rightOperand219",
    ends={
        Property(name="astm_Expression221", type=astm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BinaryExpression220", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromExpression232: BinaryAssociation = BinaryAssociation(
    name="fromExpression232",
    ends={
        Property(name="astm_Expression233", type=astm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_RangeExpression", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition224: BinaryAssociation = BinaryAssociation(
    name="condition224",
    ends={
        Property(name="astm_Expression225", type=astm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConditionalExpression", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onTrueOperand226: BinaryAssociation = BinaryAssociation(
    name="onTrueOperand226",
    ends={
        Property(name="astm_Expression228", type=astm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConditionalExpression227", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onFalseOperand229: BinaryAssociation = BinaryAssociation(
    name="onFalseOperand229",
    ends={
        Property(name="astm_Expression231", type=astm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConditionalExpression230", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams239: BinaryAssociation = BinaryAssociation(
    name="actualParams239",
    ends={
        Property(name="astm_OtherSyntaxObject241", type=astm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionCallExpression240", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value242: BinaryAssociation = BinaryAssociation(
    name="value242",
    ends={
        Property(name="astm_Expression243", type=astm_ActualParameterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ActualParameterExpression", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toExpression234: BinaryAssociation = BinaryAssociation(
    name="toExpression234",
    ends={
        Property(name="astm_Expression236", type=astm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_RangeExpression235", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
calledFunction237: BinaryAssociation = BinaryAssociation(
    name="calledFunction237",
    ends={
        Property(name="astm_Expression238", type=astm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionCallExpression", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name249: BinaryAssociation = BinaryAssociation(
    name="name249",
    ends={
        Property(name="astm_Name251", type=astm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelAccess250", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition252: BinaryAssociation = BinaryAssociation(
    name="definition252",
    ends={
        Property(name="astm_LabelDefinition254", type=astm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelAccess253", type=astm_LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newType244: BinaryAssociation = BinaryAssociation(
    name="newType244",
    ends={
        Property(name="astm_TypeReference245", type=astm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NewExpression", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams246: BinaryAssociation = BinaryAssociation(
    name="actualParams246",
    ends={
        Property(name="astm_OtherSyntaxObject248", type=astm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NewExpression247", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationType255: BinaryAssociation = BinaryAssociation(
    name="annotationType255",
    ends={
        Property(name="astm_TypeReference257", type=astm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AnnotationExpression256", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberValues258: BinaryAssociation = BinaryAssociation(
    name="memberValues258",
    ends={
        Property(name="astm_Expression260", type=astm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AnnotationExpression259", type=astm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_astm_Project_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=astm_Project)
gen_astm_SourceFile_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=astm_SourceFile)
gen_astm_SourceLocation_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=astm_SourceLocation)
gen_astm_CompilationUnit_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_CompilationUnit)
gen_astm_Scope_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=astm_Scope)
gen_astm_GASTMSyntaxObject_GASTMObject = Generalization(general=GASTMObject, specific=astm_GASTMSyntaxObject)
gen_astm_Definition_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=astm_Definition)
gen_astm_Declaration_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=astm_Declaration)
gen_astm_Name_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_Name)
gen_astm_DeclarationOrDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_DeclarationOrDefinition)
gen_astm_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=astm_VariableDeclaration)
gen_astm_FunctionDefinition_Definition = Generalization(general=Definition, specific=astm_FunctionDefinition)
gen_astm_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=astm_FunctionDeclaration)
gen_astm_EntryDefinition_Definition = Generalization(general=Definition, specific=astm_EntryDefinition)
gen_astm_NameSpaceDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_NameSpaceDefinition)
gen_astm_DataDefinition_Definition = Generalization(general=Definition, specific=astm_DataDefinition)
gen_astm_BitFieldDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_BitFieldDefinition)
gen_astm_EnumLiteralDefinition_Definition = Generalization(general=Definition, specific=astm_EnumLiteralDefinition)
gen_astm_TypeDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_TypeDefinition)
gen_astm_NamedTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=astm_NamedTypeDefinition)
gen_astm_AggregateTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=astm_AggregateTypeDefinition)
gen_astm_EnumType_DataType = Generalization(general=DataType, specific=astm_EnumType)
gen_astm_ConstructedType_DataType = Generalization(general=DataType, specific=astm_ConstructedType)
gen_astm_AggregateType_DataType = Generalization(general=DataType, specific=astm_AggregateType)
gen_astm_LabelDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_LabelDefinition)
gen_astm_IncludeUnit_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_IncludeUnit)
gen_astm_MacroCall_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_MacroCall)
gen_astm_MacroDefinition_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_MacroDefinition)
gen_astm_Comment_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_Comment)
gen_astm_Type_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_Type)
gen_astm_PrimitiveType_DataType = Generalization(general=DataType, specific=astm_PrimitiveType)
gen_astm_UnnamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=astm_UnnamedTypeReference)
gen_astm_NamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=astm_NamedTypeReference)
gen_astm_ArrayType_ConstructedType = Generalization(general=ConstructedType, specific=astm_ArrayType)
gen_astm_Dimension_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_Dimension)
gen_astm_FunctionType_Type = Generalization(general=Type, specific=astm_FunctionType)
gen_astm_FormalParameterType_DataType = Generalization(general=DataType, specific=astm_FormalParameterType)
gen_astm_NamedType_DataType = Generalization(general=DataType, specific=astm_NamedType)
gen_astm_ClassType_AggregateType = Generalization(general=AggregateType, specific=astm_ClassType)
gen_astm_DerivesFrom_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_DerivesFrom)
gen_astm_ContinueStatement_Statement = Generalization(general=Statement, specific=astm_ContinueStatement)
gen_astm_LabeledStatement_Statement = Generalization(general=Statement, specific=astm_LabeledStatement)
gen_astm_DeleteStatement_Statement = Generalization(general=Statement, specific=astm_DeleteStatement)
gen_astm_DeclarationOrDefinitionStatement_Statement = Generalization(general=Statement, specific=astm_DeclarationOrDefinitionStatement)
gen_astm_ExpressionStatement_Statement = Generalization(general=Statement, specific=astm_ExpressionStatement)
gen_astm_JumpStatement_Statement = Generalization(general=Statement, specific=astm_JumpStatement)
gen_astm_BreakStatement_Statement = Generalization(general=Statement, specific=astm_BreakStatement)
gen_astm_EmptyStatement_Statement = Generalization(general=Statement, specific=astm_EmptyStatement)
gen_astm_IfStatement_Statement = Generalization(general=Statement, specific=astm_IfStatement)
gen_astm_BlockStatement_Statement = Generalization(general=Statement, specific=astm_BlockStatement)
gen_astm_ReturnStatement_Statement = Generalization(general=Statement, specific=astm_ReturnStatement)
gen_astm_SwitchStatement_Statement = Generalization(general=Statement, specific=astm_SwitchStatement)
gen_astm_SwitchCase_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_SwitchCase)
gen_astm_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_ForStatement)
gen_astm_CaseBlock_SwitchCase = Generalization(general=SwitchCase, specific=astm_CaseBlock)
gen_astm_LoopStatement_Statement = Generalization(general=Statement, specific=astm_LoopStatement)
gen_astm_CatchBlock_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_CatchBlock)
gen_astm_TryStatement_Statement = Generalization(general=Statement, specific=astm_TryStatement)
gen_astm_ThrowStatement_Statement = Generalization(general=Statement, specific=astm_ThrowStatement)
gen_astm_TypesCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=astm_TypesCatchBlock)
gen_astm_VariableCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=astm_VariableCatchBlock)
gen_astm_Expression_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_Expression)
gen_astm_NameReference_Expression = Generalization(general=Expression, specific=astm_NameReference)
gen_astm_QualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_QualifiedIdentifierReference)
gen_astm_ArrayAccess_Expression = Generalization(general=Expression, specific=astm_ArrayAccess)
gen_astm_Literal_Expression = Generalization(general=Expression, specific=astm_Literal)
gen_astm_CastExpression_Expression = Generalization(general=Expression, specific=astm_CastExpression)
gen_astm_TypeQualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_TypeQualifiedIdentifierReference)
gen_astm_BinaryExpression_Expression = Generalization(general=Expression, specific=astm_BinaryExpression)
gen_astm_UnaryExpression_Expression = Generalization(general=Expression, specific=astm_UnaryExpression)
gen_astm_OperatorAssign_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_OperatorAssign)
gen_astm_ConditionalExpression_Expression = Generalization(general=Expression, specific=astm_ConditionalExpression)
gen_astm_RangeExpression_Expression = Generalization(general=Expression, specific=astm_RangeExpression)
gen_astm_ActualParameterExpression_ActualParameter = Generalization(general=ActualParameter, specific=astm_ActualParameterExpression)
gen_astm_FunctionCallExpression_Expression = Generalization(general=Expression, specific=astm_FunctionCallExpression)
gen_astm_LabelAccess_Expression = Generalization(general=Expression, specific=astm_LabelAccess)
gen_astm_NewExpression_Expression = Generalization(general=Expression, specific=astm_NewExpression)
gen_astm_GlobalScope_Scope = Generalization(general=Scope, specific=astm_GlobalScope)
gen_astm_PreprocessorElement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_PreprocessorElement)
gen_astm_DefinitionObject_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_DefinitionObject)
gen_astm_ProgramScope_Scope = Generalization(general=Scope, specific=astm_ProgramScope)
gen_astm_TypeReference_Type = Generalization(general=Type, specific=astm_TypeReference)
gen_astm_AnnotationExpression_Expression = Generalization(general=Expression, specific=astm_AnnotationExpression)
gen_astm_External_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_External)
gen_astm_FunctionPersistent_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_FunctionPersistent)
gen_astm_FileLocal_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_FileLocal)
gen_astm_PerClassMember_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_PerClassMember)
gen_astm_NoDef_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_NoDef)
gen_astm_Virtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_Virtual)
gen_astm_Statement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_Statement)
gen_astm_FunctionScope_Scope = Generalization(general=Scope, specific=astm_FunctionScope)
gen_astm_NameSpaceType_Type = Generalization(general=Type, specific=astm_NameSpaceType)
gen_astm_LabelType_Type = Generalization(general=Type, specific=astm_LabelType)
gen_astm_AggregateScope_Scope = Generalization(general=Scope, specific=astm_AggregateScope)
gen_astm_BlockScope_Scope = Generalization(general=Scope, specific=astm_BlockScope)
gen_astm_IdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_IdentifierReference)
gen_astm_FormalParameterDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_FormalParameterDefinition)
gen_astm_VirtualSpecification_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_VirtualSpecification)
gen_astm_FormalParameterDeclaration_Declaration = Generalization(general=Declaration, specific=astm_FormalParameterDeclaration)
gen_astm_VariableDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_VariableDefinition)
gen_astm_FunctionMemberAttribute_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_FunctionMemberAttribute)
gen_astm_LongDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_LongDouble)
gen_astm_Character_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Character)
gen_astm_String_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_String)
gen_astm_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Boolean)
gen_astm_WideCharacter_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_WideCharacter)
gen_astm_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=astm_CollectionType)
gen_astm_PureVirtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_PureVirtual)
gen_astm_NonVirtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_NonVirtual)
gen_astm_ExceptionType_DataType = Generalization(general=DataType, specific=astm_ExceptionType)
gen_astm_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Void)
gen_astm_Byte_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Byte)
gen_astm_ShortInteger_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_ShortInteger)
gen_astm_Integer_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Integer)
gen_astm_LongInteger_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_LongInteger)
gen_astm_Float_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Float)
gen_astm_Double_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Double)
gen_astm_DefaultBlock_SwitchCase = Generalization(general=SwitchCase, specific=astm_DefaultBlock)
gen_astm_WhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_WhileStatement)
gen_astm_DoWhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_DoWhileStatement)
gen_astm_ForCheckBeforeStatement_ForStatement = Generalization(general=ForStatement, specific=astm_ForCheckBeforeStatement)
gen_astm_ForCheckAfterStatement_ForStatement = Generalization(general=ForStatement, specific=astm_ForCheckAfterStatement)
gen_astm_AggregateExpression_Expression = Generalization(general=Expression, specific=astm_AggregateExpression)
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
gen_astm_TerminateStatement_Statement = Generalization(general=Statement, specific=astm_TerminateStatement)
gen_astm_AddressOf_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_AddressOf)
gen_astm_Deref_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Deref)
gen_astm_Increment_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Increment)
gen_astm_Decrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Decrement)
gen_astm_PostIncrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_PostIncrement)
gen_astm_PostDecrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_PostDecrement)
gen_astm_Add_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Add)
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
gen_astm_BitNot_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_BitNot)
gen_astm_NotLess_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_NotLess)
gen_astm_BitAnd_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitAnd)
gen_astm_BitOr_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitOr)
gen_astm_BitXor_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitXor)
gen_astm_BitLeftShift_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitLeftShift)
gen_astm_BitRightShift_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitRightShift)
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
gen_astm_Assign_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Assign)
gen_astm_MissingActualParameter_ActualParameter = Generalization(general=ActualParameter, specific=astm_MissingActualParameter)
gen_astm_ByValueActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=astm_ByValueActualParameterExpression)
gen_astm_ByReferenceActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=astm_ByReferenceActualParameterExpression)
gen_astm_SpecificClassType_ClassType = Generalization(general=ClassType, specific=astm_SpecificClassType)

# Domain Model
domain_model = DomainModel(
    name="astm",
    types={astm_Project, GASTMSemanticObject, astm_GASTMObject, astm_GASTMSourceObject, astm_GASTMSemanticObject, astm_OtherSyntaxObject, astm_StorageSpecification, astm_DataType, astm_AccessKind, astm_UnaryOperator, astm_BinaryOperator, astm_ActualParameter, astm_SourceFile, GASTMSourceObject, astm_SourceLocation, astm_PreprocessorElement, astm_AnnotationExpression, OtherSyntaxObject, astm_CompilationUnit, astm_GlobalScope, astm_Scope, astm_DefinitionObject, astm_GASTMSyntaxObject, GASTMObject, astm_Definition, DeclarationOrDefinition, astm_TypeReference, astm_Declaration, astm_ProgramScope, astm_Name, astm_DeclarationOrDefinition, DefinitionObject, astm_VariableDeclaration, astm_FunctionDefinition, Definition, astm_FunctionDeclaration, Declaration, astm_FormalParameterDeclaration, astm_FunctionMemberAttributes, astm_VirtualSpecification, astm_EntryDefinition, astm_FormalParameterDefinition, astm_Statement, astm_FunctionScope, astm_NameSpaceDefinition, astm_DataDefinition, astm_Expression, astm_BitFieldDefinition, DataDefinition, astm_EnumLiteralDefinition, astm_TypeDefinition, astm_NamedTypeDefinition, TypeDefinition, astm_NamedType, astm_AggregateTypeDefinition, astm_AggregateType, astm_EnumType, astm_ConstructedType, astm_AggregateScope, astm_ArrayType, ConstructedType, astm_NameSpaceType, astm_LabelDefinition, astm_LabelType, astm_IncludeUnit, PreprocessorElement, astm_MacroCall, astm_MacroDefinition, astm_Comment, astm_Type, GASTMSyntaxObject, astm_PrimitiveType, DataType, astm_UnnamedTypeReference, TypeReference, astm_NamedTypeReference, astm_Dimension, astm_FunctionType, Type, astm_FormalParameterType, astm_ClassType, AggregateType, astm_DerivesFrom, astm_LabelAccess, astm_ContinueStatement, astm_LabeledStatement, astm_DeleteStatement, Statement, astm_DeclarationOrDefinitionStatement, astm_ExpressionStatement, astm_JumpStatement, astm_BreakStatement, astm_EmptyStatement, astm_IfStatement, astm_BlockStatement, astm_BlockScope, astm_ReturnStatement, astm_SwitchStatement, astm_SwitchCase, astm_ForStatement, LoopStatement, astm_CaseBlock, SwitchCase, astm_LoopStatement, astm_TryStatement, astm_CatchBlock, astm_ThrowStatement, astm_TypesCatchBlock, CatchBlock, astm_VariableCatchBlock, astm_ArrayAccess, astm_NameReference, Expression, astm_QualifiedIdentifierReference, NameReference, astm_IdentifierReference, astm_Literal, astm_CastExpression, astm_TypeQualifiedIdentifierReference, astm_BinaryExpression, astm_UnaryExpression, astm_OperatorAssign, BinaryOperator, astm_ConditionalExpression, astm_RangeExpression, astm_ActualParameterExpression, ActualParameter, astm_FunctionCallExpression, astm_NewExpression, Scope, astm_External, StorageSpecification, astm_FunctionPersistent, astm_FileLocal, astm_PerClassMember, astm_NoDef, astm_Virtual, VirtualSpecification, astm_VariableDefinition, astm_FunctionMemberAttribute, astm_LongDouble, astm_Character, astm_String, astm_Boolean, astm_WideCharacter, astm_CollectionType, astm_PureVirtual, astm_NonVirtual, astm_ExceptionType, astm_Void, PrimitiveType, astm_Byte, astm_ShortInteger, astm_Integer, astm_LongInteger, astm_Float, astm_Double, astm_DefaultBlock, astm_WhileStatement, astm_DoWhileStatement, astm_ForCheckBeforeStatement, ForStatement, astm_ForCheckAfterStatement, astm_AggregateExpression, astm_PointerType, astm_ReferenceType, astm_RangeType, astm_StructureType, astm_UnionType, astm_AnnotationType, astm_ByValueFormalParameterType, FormalParameterType, astm_ByReferenceFormalParameterType, astm_Public, AccessKind, astm_Protected, astm_Private, astm_TerminateStatement, astm_AddressOf, astm_Deref, astm_Increment, astm_Decrement, astm_PostIncrement, astm_PostDecrement, astm_Add, astm_QualifiedOverPointer, QualifiedIdentifierReference, astm_QualifiedOverData, astm_IntegerlLiteral, Literal, astm_StringLiteral, astm_CharLiteral, astm_RealLiteral, astm_BooleanLiteral, astm_BitLiteral, astm_UnaryPlus, UnaryOperator, astm_Negate, astm_Not, astm_BitNot, astm_NotLess, astm_BitAnd, astm_BitOr, astm_BitXor, astm_BitLeftShift, astm_BitRightShift, astm_Subtract, astm_Multiply, astm_Divide, astm_Modulus, astm_Exponent, astm_And, astm_Or, astm_Equal, astm_NotEqual, astm_Greater, astm_NotGreater, astm_Less, astm_Assign, astm_MissingActualParameter, astm_ByValueActualParameterExpression, ActualParameterExpression, astm_ByReferenceActualParameterExpression, astm_SpecificClassType, ClassType},
    associations={inSourceFile0, preProcessorElements10, annotations12, files1, outerScope2, definitionObject4, childScope6, locationInfo8, accessKind20, identifierName23, definitionType24, fragments14, opensScope17, storageSpecifiers19, defRef26, identifierName28, declarationType31, formalParameters34, functionMemberAttributes35, opensScope46, virtualSpecifier48, formalParameters50, body52, returnType37, formalParameters39, body41, functionMemberAttributes43, nameSpace64, body66, initialValue55, bitFieldSize56, value58, name60, definitionType62, aggregateType63, enumLiterals78, baseType80, members82, opensScope85, nameSpaceType69, labelName71, labelType73, file75, refersTo77, accessKind104, className107, type110, name112, ranks87, lowBound88, highBound91, returnType94, parameterTypes96, type98, body101, derivesFrom103, target125, target126, type114, label128, operand117, declOrDefn119, expression121, target123, condition137, thenBody139, elseBody142, statement130, subStatements133, opensScope135, caseExpressions152, switchExpression145, cases147, body149, initBody161, iterationBody163, returnValue154, condition156, body158, finalStatement170, body173, guardedStatement166, catchBlocks168, exceptionVariable178, exception180, exceptions176, name185, refersTo187, expressionType182, qualifiers195, member197, arrayName190, subscripts192, castType204, aggregateType199, member201, operand211, expression206, operator209, operator222, operator214, leftOperand216, rightOperand219, fromExpression232, condition224, onTrueOperand226, onFalseOperand229, actualParams239, value242, toExpression234, calledFunction237, name249, definition252, newType244, actualParams246, annotationType255, memberValues258},
    generalizations={gen_astm_Project_GASTMSemanticObject, gen_astm_SourceFile_GASTMSourceObject, gen_astm_SourceLocation_GASTMSourceObject, gen_astm_CompilationUnit_OtherSyntaxObject, gen_astm_Scope_GASTMSemanticObject, gen_astm_GASTMSyntaxObject_GASTMObject, gen_astm_Definition_DeclarationOrDefinition, gen_astm_Declaration_DeclarationOrDefinition, gen_astm_Name_OtherSyntaxObject, gen_astm_DeclarationOrDefinition_DefinitionObject, gen_astm_VariableDeclaration_Declaration, gen_astm_FunctionDefinition_Definition, gen_astm_FunctionDeclaration_Declaration, gen_astm_EntryDefinition_Definition, gen_astm_NameSpaceDefinition_DefinitionObject, gen_astm_DataDefinition_Definition, gen_astm_BitFieldDefinition_DataDefinition, gen_astm_EnumLiteralDefinition_Definition, gen_astm_TypeDefinition_DefinitionObject, gen_astm_NamedTypeDefinition_TypeDefinition, gen_astm_AggregateTypeDefinition_TypeDefinition, gen_astm_EnumType_DataType, gen_astm_ConstructedType_DataType, gen_astm_AggregateType_DataType, gen_astm_LabelDefinition_DefinitionObject, gen_astm_IncludeUnit_PreprocessorElement, gen_astm_MacroCall_PreprocessorElement, gen_astm_MacroDefinition_PreprocessorElement, gen_astm_Comment_PreprocessorElement, gen_astm_Type_GASTMSyntaxObject, gen_astm_PrimitiveType_DataType, gen_astm_UnnamedTypeReference_TypeReference, gen_astm_NamedTypeReference_TypeReference, gen_astm_ArrayType_ConstructedType, gen_astm_Dimension_OtherSyntaxObject, gen_astm_FunctionType_Type, gen_astm_FormalParameterType_DataType, gen_astm_NamedType_DataType, gen_astm_ClassType_AggregateType, gen_astm_DerivesFrom_OtherSyntaxObject, gen_astm_ContinueStatement_Statement, gen_astm_LabeledStatement_Statement, gen_astm_DeleteStatement_Statement, gen_astm_DeclarationOrDefinitionStatement_Statement, gen_astm_ExpressionStatement_Statement, gen_astm_JumpStatement_Statement, gen_astm_BreakStatement_Statement, gen_astm_EmptyStatement_Statement, gen_astm_IfStatement_Statement, gen_astm_BlockStatement_Statement, gen_astm_ReturnStatement_Statement, gen_astm_SwitchStatement_Statement, gen_astm_SwitchCase_OtherSyntaxObject, gen_astm_ForStatement_LoopStatement, gen_astm_CaseBlock_SwitchCase, gen_astm_LoopStatement_Statement, gen_astm_CatchBlock_OtherSyntaxObject, gen_astm_TryStatement_Statement, gen_astm_ThrowStatement_Statement, gen_astm_TypesCatchBlock_CatchBlock, gen_astm_VariableCatchBlock_CatchBlock, gen_astm_Expression_GASTMSyntaxObject, gen_astm_NameReference_Expression, gen_astm_QualifiedIdentifierReference_NameReference, gen_astm_ArrayAccess_Expression, gen_astm_Literal_Expression, gen_astm_CastExpression_Expression, gen_astm_TypeQualifiedIdentifierReference_NameReference, gen_astm_BinaryExpression_Expression, gen_astm_UnaryExpression_Expression, gen_astm_OperatorAssign_BinaryOperator, gen_astm_ConditionalExpression_Expression, gen_astm_RangeExpression_Expression, gen_astm_ActualParameterExpression_ActualParameter, gen_astm_FunctionCallExpression_Expression, gen_astm_LabelAccess_Expression, gen_astm_NewExpression_Expression, gen_astm_GlobalScope_Scope, gen_astm_PreprocessorElement_GASTMSyntaxObject, gen_astm_DefinitionObject_GASTMSyntaxObject, gen_astm_ProgramScope_Scope, gen_astm_TypeReference_Type, gen_astm_AnnotationExpression_Expression, gen_astm_External_StorageSpecification, gen_astm_FunctionPersistent_StorageSpecification, gen_astm_FileLocal_StorageSpecification, gen_astm_PerClassMember_StorageSpecification, gen_astm_NoDef_StorageSpecification, gen_astm_Virtual_VirtualSpecification, gen_astm_Statement_GASTMSyntaxObject, gen_astm_FunctionScope_Scope, gen_astm_NameSpaceType_Type, gen_astm_LabelType_Type, gen_astm_AggregateScope_Scope, gen_astm_BlockScope_Scope, gen_astm_IdentifierReference_NameReference, gen_astm_FormalParameterDefinition_DataDefinition, gen_astm_VirtualSpecification_OtherSyntaxObject, gen_astm_FormalParameterDeclaration_Declaration, gen_astm_VariableDefinition_DataDefinition, gen_astm_FunctionMemberAttribute_OtherSyntaxObject, gen_astm_LongDouble_PrimitiveType, gen_astm_Character_PrimitiveType, gen_astm_String_PrimitiveType, gen_astm_Boolean_PrimitiveType, gen_astm_WideCharacter_PrimitiveType, gen_astm_CollectionType_ConstructedType, gen_astm_PureVirtual_VirtualSpecification, gen_astm_NonVirtual_VirtualSpecification, gen_astm_ExceptionType_DataType, gen_astm_Void_PrimitiveType, gen_astm_Byte_PrimitiveType, gen_astm_ShortInteger_PrimitiveType, gen_astm_Integer_PrimitiveType, gen_astm_LongInteger_PrimitiveType, gen_astm_Float_PrimitiveType, gen_astm_Double_PrimitiveType, gen_astm_DefaultBlock_SwitchCase, gen_astm_WhileStatement_LoopStatement, gen_astm_DoWhileStatement_LoopStatement, gen_astm_ForCheckBeforeStatement_ForStatement, gen_astm_ForCheckAfterStatement_ForStatement, gen_astm_AggregateExpression_Expression, gen_astm_PointerType_ConstructedType, gen_astm_ReferenceType_ConstructedType, gen_astm_RangeType_ConstructedType, gen_astm_StructureType_AggregateType, gen_astm_UnionType_AggregateType, gen_astm_AnnotationType_AggregateType, gen_astm_ByValueFormalParameterType_FormalParameterType, gen_astm_ByReferenceFormalParameterType_FormalParameterType, gen_astm_Public_AccessKind, gen_astm_Protected_AccessKind, gen_astm_Private_AccessKind, gen_astm_TerminateStatement_Statement, gen_astm_AddressOf_UnaryOperator, gen_astm_Deref_UnaryOperator, gen_astm_Increment_UnaryOperator, gen_astm_Decrement_UnaryOperator, gen_astm_PostIncrement_UnaryOperator, gen_astm_PostDecrement_UnaryOperator, gen_astm_Add_BinaryOperator, gen_astm_QualifiedOverPointer_QualifiedIdentifierReference, gen_astm_QualifiedOverData_QualifiedIdentifierReference, gen_astm_IntegerlLiteral_Literal, gen_astm_StringLiteral_Literal, gen_astm_CharLiteral_Literal, gen_astm_RealLiteral_Literal, gen_astm_BooleanLiteral_Literal, gen_astm_BitLiteral_Literal, gen_astm_UnaryPlus_UnaryOperator, gen_astm_Negate_UnaryOperator, gen_astm_Not_UnaryOperator, gen_astm_BitNot_UnaryOperator, gen_astm_NotLess_BinaryOperator, gen_astm_BitAnd_BinaryOperator, gen_astm_BitOr_BinaryOperator, gen_astm_BitXor_BinaryOperator, gen_astm_BitLeftShift_BinaryOperator, gen_astm_BitRightShift_BinaryOperator, gen_astm_Subtract_BinaryOperator, gen_astm_Multiply_BinaryOperator, gen_astm_Divide_BinaryOperator, gen_astm_Modulus_BinaryOperator, gen_astm_Exponent_BinaryOperator, gen_astm_And_BinaryOperator, gen_astm_Or_BinaryOperator, gen_astm_Equal_BinaryOperator, gen_astm_NotEqual_BinaryOperator, gen_astm_Greater_BinaryOperator, gen_astm_NotGreater_BinaryOperator, gen_astm_Less_BinaryOperator, gen_astm_Assign_BinaryOperator, gen_astm_MissingActualParameter_ActualParameter, gen_astm_ByValueActualParameterExpression_ActualParameterExpression, gen_astm_ByReferenceActualParameterExpression_ActualParameterExpression, gen_astm_SpecificClassType_ClassType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)