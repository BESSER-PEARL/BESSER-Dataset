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
gastm_SourceFile = Class(name="gastm::SourceFile")
GASTMSourceObject = Class(name="GASTMSourceObject")
gastm_CompilationUnit = Class(name="gastm::CompilationUnit")
SourceFile = Class(name="SourceFile")
gastm_GASTMObject = Class(name="gastm::GASTMObject")
gastm_GASTMSourceObject = Class(name="gastm::GASTMSourceObject", is_abstract=True)
GASTMObject = Class(name="GASTMObject")
gastm_GASTMSemanticObject = Class(name="gastm::GASTMSemanticObject", is_abstract=True)
gastm_GASTMSyntaxObject = Class(name="gastm::GASTMSyntaxObject", is_abstract=True)
gastm_SourceLocation = Class(name="gastm::SourceLocation")
gastm_PreprocessorElement = Class(name="gastm::PreprocessorElement", is_abstract=True)
gastm_AnnotationExpression = Class(name="gastm::AnnotationExpression")
Scope = Class(name="Scope")
gastm_FunctionScope = Class(name="gastm::FunctionScope")
gastm_AggregateScope = Class(name="gastm::AggregateScope")
gastm_BlockScope = Class(name="gastm::BlockScope")
GASTMSyntaxObject = Class(name="GASTMSyntaxObject")
gastm_Type = Class(name="gastm::Type", is_abstract=True)
gastm_Expression = Class(name="gastm::Expression", is_abstract=True)
gastm_DefinitionObject = Class(name="gastm::DefinitionObject", is_abstract=True)
gastm_ProgramScope = Class(name="gastm::ProgramScope")
gastm_SourceFileReference = Class(name="gastm::SourceFileReference")
gastm_Project = Class(name="gastm::Project")
GASTMSemanticObject = Class(name="GASTMSemanticObject")
gastm_GlobalScope = Class(name="gastm::GlobalScope")
gastm_Scope = Class(name="gastm::Scope")
gastm_UnaryOperator = Class(name="gastm::UnaryOperator", is_abstract=True)
gastm_BinaryOperator = Class(name="gastm::BinaryOperator", is_abstract=True)
gastm_StorageSpecification = Class(name="gastm::StorageSpecification", is_abstract=True)
gastm_VirtualSpecification = Class(name="gastm::VirtualSpecification", is_abstract=True)
gastm_AccessKind = Class(name="gastm::AccessKind")
gastm_ActualParameter = Class(name="gastm::ActualParameter", is_abstract=True)
gastm_FunctionMemberAttributes = Class(name="gastm::FunctionMemberAttributes")
gastm_TypeReference = Class(name="gastm::TypeReference", is_abstract=True)
gastm_Statement = Class(name="gastm::Statement", is_abstract=True)
gastm_MinorSyntaxObject = Class(name="gastm::MinorSyntaxObject", is_abstract=True)
gastm_Dimension = Class(name="gastm::Dimension")
MinorSyntaxObject = Class(name="MinorSyntaxObject")
gastm_Name = Class(name="gastm::Name")
gastm_SwitchCase = Class(name="gastm::SwitchCase")
gastm_CatchBlock = Class(name="gastm::CatchBlock")
gastm_TypeDefinition = Class(name="gastm::TypeDefinition")
gastm_NameSpaceDefinition = Class(name="gastm::NameSpaceDefinition")
gastm_NameSpaceType = Class(name="gastm::NameSpaceType")
gastm_LabelDefinition = Class(name="gastm::LabelDefinition")
gastm_DerivesFrom = Class(name="gastm::DerivesFrom")
gastm_NamedTypeReference = Class(name="gastm::NamedTypeReference")
gastm_MemberObject = Class(name="gastm::MemberObject")
gastm_DeclarationOrDefinition = Class(name="gastm::DeclarationOrDefinition", is_abstract=True)
DefinitionObject = Class(name="DefinitionObject")
gastm_FunctionDefinition = Class(name="gastm::FunctionDefinition")
Definition = Class(name="Definition")
gastm_FormalParameterDefinition = Class(name="gastm::FormalParameterDefinition")
gastm_LabelType = Class(name="gastm::LabelType")
gastm_TypeDeclaration = Class(name="gastm::TypeDeclaration")
gastm_Definition = Class(name="gastm::Definition", is_abstract=True)
DeclarationOrDefinition = Class(name="DeclarationOrDefinition")
gastm_Declaration = Class(name="gastm::Declaration", is_abstract=True)
gastm_External = Class(name="gastm::External")
StorageSpecification = Class(name="StorageSpecification")
gastm_FunctionPersistent = Class(name="gastm::FunctionPersistent")
gastm_FileLocal = Class(name="gastm::FileLocal")
gastm_PerClassMember = Class(name="gastm::PerClassMember")
gastm_NoDef = Class(name="gastm::NoDef")
gastm_Virtual = Class(name="gastm::Virtual")
VirtualSpecification = Class(name="VirtualSpecification")
gastm_VariableDefinition = Class(name="gastm::VariableDefinition")
DataDefinition = Class(name="DataDefinition")
gastm_BitFieldDefinition = Class(name="gastm::BitFieldDefinition")
gastm_EntryDefinition = Class(name="gastm::EntryDefinition")
gastm_DataDefinition = Class(name="gastm::DataDefinition", is_abstract=True)
gastm_EnumLiteralDefinition = Class(name="gastm::EnumLiteralDefinition")
gastm_FunctionDeclaration = Class(name="gastm::FunctionDeclaration")
Declaration = Class(name="Declaration")
gastm_FormalParameterDeclaration = Class(name="gastm::FormalParameterDeclaration")
gastm_VariableDeclaration = Class(name="gastm::VariableDeclaration")
gastm_MacroDefinition = Class(name="gastm::MacroDefinition")
gastm_Comment = Class(name="gastm::Comment")
gastm_FunctionType = Class(name="gastm::FunctionType")
Type = Class(name="Type")
gastm_FormalParameterType = Class(name="gastm::FormalParameterType", is_abstract=True)
gastm_NamedTypeDefinition = Class(name="gastm::NamedTypeDefinition")
TypeDefinition = Class(name="TypeDefinition")
gastm_NamedType = Class(name="gastm::NamedType")
gastm_AggregateTypeDefinition = Class(name="gastm::AggregateTypeDefinition")
gastm_AggregateType = Class(name="gastm::AggregateType", is_abstract=True)
gastm_EnumTypeDefinition = Class(name="gastm::EnumTypeDefinition")
gastm_EnumType = Class(name="gastm::EnumType")
gastm_AggregateTypeDeclaration = Class(name="gastm::AggregateTypeDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
gastm_EnumTypeDeclaration = Class(name="gastm::EnumTypeDeclaration")
gastm_IncludeUnit = Class(name="gastm::IncludeUnit")
PreprocessorElement = Class(name="PreprocessorElement")
gastm_MacroCall = Class(name="gastm::MacroCall")
gastm_ExceptionType = Class(name="gastm::ExceptionType")
gastm_DataType = Class(name="gastm::DataType", is_abstract=True)
gastm_PrimitiveType = Class(name="gastm::PrimitiveType", is_abstract=True)
DataType = Class(name="DataType")
gastm_ConstructedType = Class(name="gastm::ConstructedType", is_abstract=True)
gastm_PointerType = Class(name="gastm::PointerType")
gastm_ReferenceType = Class(name="gastm::ReferenceType")
gastm_RangeType = Class(name="gastm::RangeType")
gastm_ArrayType = Class(name="gastm::ArrayType")
gastm_StructureType = Class(name="gastm::StructureType")
AggregateType = Class(name="AggregateType")
gastm_UnionType = Class(name="gastm::UnionType")
gastm_ClassType = Class(name="gastm::ClassType")
gastm_AnnotationType = Class(name="gastm::AnnotationType")
gastm_ByValueFormalParameterType = Class(name="gastm::ByValueFormalParameterType")
FormalParameterType = Class(name="FormalParameterType")
gastm_ByReferenceFormalParameterType = Class(name="gastm::ByReferenceFormalParameterType")
gastm_NumberType = Class(name="gastm::NumberType", is_abstract=True)
PrimitiveType = Class(name="PrimitiveType")
gastm_Void = Class(name="gastm::Void")
gastm_Boolean = Class(name="gastm::Boolean")
gastm_IntegralType = Class(name="gastm::IntegralType", is_abstract=True)
NumberType = Class(name="NumberType")
gastm_RealType = Class(name="gastm::RealType", is_abstract=True)
gastm_Byte = Class(name="gastm::Byte")
gastm_Character = Class(name="gastm::Character")
gastm_ShortInteger = Class(name="gastm::ShortInteger")
IntegralType = Class(name="IntegralType")
gastm_Integer = Class(name="gastm::Integer")
IntegerLiteral = Class(name="IntegerLiteral")
gastm_LongInteger = Class(name="gastm::LongInteger")
gastm_Real = Class(name="gastm::Real")
RealType = Class(name="RealType")
gastm_Double = Class(name="gastm::Double")
gastm_LongDouble = Class(name="gastm::LongDouble")
gastm_CollectionType = Class(name="gastm::CollectionType")
ConstructedType = Class(name="ConstructedType")
gastm_LabeledStatement = Class(name="gastm::LabeledStatement")
gastm_BlockStatement = Class(name="gastm::BlockStatement")
gastm_EmptyStatement = Class(name="gastm::EmptyStatement")
gastm_IfStatement = Class(name="gastm::IfStatement")
gastm_Public = Class(name="gastm::Public")
AccessKind = Class(name="AccessKind")
gastm_Protected = Class(name="gastm::Protected")
gastm_Private = Class(name="gastm::Private")
gastm_UnnamedTypeReference = Class(name="gastm::UnnamedTypeReference")
TypeReference = Class(name="TypeReference")
gastm_ExpressionStatement = Class(name="gastm::ExpressionStatement")
Statement = Class(name="Statement")
gastm_JumpStatement = Class(name="gastm::JumpStatement")
gastm_BreakStatement = Class(name="gastm::BreakStatement")
gastm_LabelAccess = Class(name="gastm::LabelAccess")
gastm_ContinueStatement = Class(name="gastm::ContinueStatement")
gastm_DeclarationOrDefinitionStatement = Class(name="gastm::DeclarationOrDefinitionStatement")
gastm_ThrowStatement = Class(name="gastm::ThrowStatement")
gastm_SwitchStatement = Class(name="gastm::SwitchStatement")
gastm_ReturnStatement = Class(name="gastm::ReturnStatement")
gastm_LoopStatement = Class(name="gastm::LoopStatement")
gastm_TryStatement = Class(name="gastm::TryStatement")
gastm_WhileStatement = Class(name="gastm::WhileStatement")
LoopStatement = Class(name="LoopStatement")
gastm_DoWhileStatement = Class(name="gastm::DoWhileStatement")
gastm_ForStatement = Class(name="gastm::ForStatement", is_abstract=True)
gastm_DeleteStatement = Class(name="gastm::DeleteStatement")
gastm_TerminateStatement = Class(name="gastm::TerminateStatement")
gastm_CaseBlock = Class(name="gastm::CaseBlock")
SwitchCase = Class(name="SwitchCase")
gastm_DefaultBlock = Class(name="gastm::DefaultBlock")
gastm_AggregateExpression = Class(name="gastm::AggregateExpression")
gastm_UnaryExpression = Class(name="gastm::UnaryExpression")
gastm_BinaryExpression = Class(name="gastm::BinaryExpression")
gastm_ForCheckBeforeStatement = Class(name="gastm::ForCheckBeforeStatement")
ForStatement = Class(name="ForStatement")
gastm_ForCheckAfterStatement = Class(name="gastm::ForCheckAfterStatement")
gastm_TypesCatchBlock = Class(name="gastm::TypesCatchBlock")
CatchBlock = Class(name="CatchBlock")
gastm_VariableCatchBlock = Class(name="gastm::VariableCatchBlock")
gastm_Literal = Class(name="gastm::Literal")
Expression = Class(name="Expression")
gastm_CastExpression = Class(name="gastm::CastExpression")
gastm_NewExpression = Class(name="gastm::NewExpression")
gastm_NameReference = Class(name="gastm::NameReference", is_abstract=True)
gastm_ConditionalExpression = Class(name="gastm::ConditionalExpression")
gastm_RangeExpression = Class(name="gastm::RangeExpression")
gastm_FunctionCallExpression = Class(name="gastm::FunctionCallExpression")
gastm_CollectionExpression = Class(name="gastm::CollectionExpression")
gastm_ArrayAccess = Class(name="gastm::ArrayAccess")
gastm_BooleanLiteral = Class(name="gastm::BooleanLiteral")
gastm_BitLiteral = Class(name="gastm::BitLiteral")
gastm_EnumLiteral = Class(name="gastm::EnumLiteral")
gastm_UnaryPlus = Class(name="gastm::UnaryPlus")
UnaryOperator = Class(name="UnaryOperator")
gastm_UnaryMinus = Class(name="gastm::UnaryMinus")
gastm_Not = Class(name="gastm::Not")
gastm_BitNot = Class(name="gastm::BitNot")
gastm_AddressOf = Class(name="gastm::AddressOf")
gastm_IdentifierReference = Class(name="gastm::IdentifierReference")
NameReference = Class(name="NameReference")
gastm_QualifiedIdentifierReference = Class(name="gastm::QualifiedIdentifierReference", is_abstract=True)
gastm_TypeQualifiedIdentifierReference = Class(name="gastm::TypeQualifiedIdentifierReference")
gastm_QualifiedOverPointer = Class(name="gastm::QualifiedOverPointer")
QualifiedIdentifierReference = Class(name="QualifiedIdentifierReference")
gastm_QualifiedOverData = Class(name="gastm::QualifiedOverData")
gastm_IntegerLiteral = Class(name="gastm::IntegerLiteral")
Literal = Class(name="Literal")
gastm_CharLiteral = Class(name="gastm::CharLiteral")
gastm_RealLiteral = Class(name="gastm::RealLiteral")
gastm_StringLiteral = Class(name="gastm::StringLiteral")
gastm_BitAnd = Class(name="gastm::BitAnd")
gastm_BitOr = Class(name="gastm::BitOr")
gastm_BitXor = Class(name="gastm::BitXor")
gastm_BitLeftShift = Class(name="gastm::BitLeftShift")
gastm_BitRightShift = Class(name="gastm::BitRightShift")
gastm_Assign = Class(name="gastm::Assign")
gastm_OperatorAssign = Class(name="gastm::OperatorAssign")
gastm_ActualParameterExpression = Class(name="gastm::ActualParameterExpression", is_abstract=True)
ActualParameter = Class(name="ActualParameter")
gastm_Deref = Class(name="gastm::Deref")
gastm_Increment = Class(name="gastm::Increment")
gastm_Decrement = Class(name="gastm::Decrement")
gastm_PostIncrement = Class(name="gastm::PostIncrement")
gastm_PostDecrement = Class(name="gastm::PostDecrement")
gastm_Add = Class(name="gastm::Add")
BinaryOperator = Class(name="BinaryOperator")
gastm_Subtract = Class(name="gastm::Subtract")
gastm_Multiply = Class(name="gastm::Multiply")
gastm_Divide = Class(name="gastm::Divide")
gastm_Modulus = Class(name="gastm::Modulus")
gastm_Exponent = Class(name="gastm::Exponent")
gastm_And = Class(name="gastm::And")
gastm_Or = Class(name="gastm::Or")
gastm_Equal = Class(name="gastm::Equal")
gastm_NotEqual = Class(name="gastm::NotEqual")
gastm_Greater = Class(name="gastm::Greater")
gastm_NotGreater = Class(name="gastm::NotGreater")
gastm_Less = Class(name="gastm::Less")
gastm_NotLess = Class(name="gastm::NotLess")
gastm_MissingActualParameter = Class(name="gastm::MissingActualParameter")
gastm_ByValueActualParameterExpression = Class(name="gastm::ByValueActualParameterExpression")
ActualParameterExpression = Class(name="ActualParameterExpression")
gastm_ByReferenceActualParameterExpression = Class(name="gastm::ByReferenceActualParameterExpression")

# gastm_SourceFile class attributes and methods
gastm_SourceFile_path: Property = Property(name="path", type=StringType)
gastm_SourceFile.attributes={gastm_SourceFile_path}

# GASTMSourceObject class attributes and methods

# gastm_CompilationUnit class attributes and methods
gastm_CompilationUnit_language: Property = Property(name="language", type=StringType)
gastm_CompilationUnit.attributes={gastm_CompilationUnit_language}

# SourceFile class attributes and methods

# gastm_GASTMObject class attributes and methods

# gastm_GASTMSourceObject class attributes and methods

# GASTMObject class attributes and methods

# gastm_GASTMSemanticObject class attributes and methods

# gastm_GASTMSyntaxObject class attributes and methods

# gastm_SourceLocation class attributes and methods
gastm_SourceLocation_startLine: Property = Property(name="startLine", type=StringType)
gastm_SourceLocation_startPosition: Property = Property(name="startPosition", type=StringType)
gastm_SourceLocation_endLine: Property = Property(name="endLine", type=StringType)
gastm_SourceLocation_endPosition: Property = Property(name="endPosition", type=StringType)
gastm_SourceLocation.attributes={gastm_SourceLocation_endPosition, gastm_SourceLocation_startPosition, gastm_SourceLocation_startLine, gastm_SourceLocation_endLine}

# gastm_PreprocessorElement class attributes and methods

# gastm_AnnotationExpression class attributes and methods

# Scope class attributes and methods

# gastm_FunctionScope class attributes and methods

# gastm_AggregateScope class attributes and methods

# gastm_BlockScope class attributes and methods

# GASTMSyntaxObject class attributes and methods

# gastm_Type class attributes and methods
gastm_Type_isConst: Property = Property(name="isConst", type=StringType)
gastm_Type.attributes={gastm_Type_isConst}

# gastm_Expression class attributes and methods

# gastm_DefinitionObject class attributes and methods

# gastm_ProgramScope class attributes and methods

# gastm_SourceFileReference class attributes and methods

# gastm_Project class attributes and methods

# GASTMSemanticObject class attributes and methods

# gastm_GlobalScope class attributes and methods

# gastm_Scope class attributes and methods

# gastm_UnaryOperator class attributes and methods

# gastm_BinaryOperator class attributes and methods

# gastm_StorageSpecification class attributes and methods

# gastm_VirtualSpecification class attributes and methods

# gastm_AccessKind class attributes and methods

# gastm_ActualParameter class attributes and methods

# gastm_FunctionMemberAttributes class attributes and methods
gastm_FunctionMemberAttributes_isFriend: Property = Property(name="isFriend", type=StringType)
gastm_FunctionMemberAttributes_isInLine: Property = Property(name="isInLine", type=StringType)
gastm_FunctionMemberAttributes_isThisConst: Property = Property(name="isThisConst", type=StringType)
gastm_FunctionMemberAttributes.attributes={gastm_FunctionMemberAttributes_isFriend, gastm_FunctionMemberAttributes_isThisConst, gastm_FunctionMemberAttributes_isInLine}

# gastm_TypeReference class attributes and methods

# gastm_Statement class attributes and methods

# gastm_MinorSyntaxObject class attributes and methods

# gastm_Dimension class attributes and methods

# MinorSyntaxObject class attributes and methods

# gastm_Name class attributes and methods
gastm_Name_nameString: Property = Property(name="nameString", type=StringType)
gastm_Name.attributes={gastm_Name_nameString}

# gastm_SwitchCase class attributes and methods
gastm_SwitchCase_isEvaluateAllCases: Property = Property(name="isEvaluateAllCases", type=StringType)
gastm_SwitchCase.attributes={gastm_SwitchCase_isEvaluateAllCases}

# gastm_CatchBlock class attributes and methods

# gastm_TypeDefinition class attributes and methods

# gastm_NameSpaceDefinition class attributes and methods

# gastm_NameSpaceType class attributes and methods

# gastm_LabelDefinition class attributes and methods

# gastm_DerivesFrom class attributes and methods

# gastm_NamedTypeReference class attributes and methods

# gastm_MemberObject class attributes and methods
gastm_MemberObject_offset: Property = Property(name="offset", type=StringType)
gastm_MemberObject.attributes={gastm_MemberObject_offset}

# gastm_DeclarationOrDefinition class attributes and methods
gastm_DeclarationOrDefinition_linkageSpecifier: Property = Property(name="linkageSpecifier", type=StringType)
gastm_DeclarationOrDefinition.attributes={gastm_DeclarationOrDefinition_linkageSpecifier}

# DefinitionObject class attributes and methods

# gastm_FunctionDefinition class attributes and methods

# Definition class attributes and methods

# gastm_FormalParameterDefinition class attributes and methods

# gastm_LabelType class attributes and methods

# gastm_TypeDeclaration class attributes and methods

# gastm_Definition class attributes and methods

# DeclarationOrDefinition class attributes and methods

# gastm_Declaration class attributes and methods

# gastm_External class attributes and methods

# StorageSpecification class attributes and methods

# gastm_FunctionPersistent class attributes and methods

# gastm_FileLocal class attributes and methods

# gastm_PerClassMember class attributes and methods

# gastm_NoDef class attributes and methods

# gastm_Virtual class attributes and methods

# VirtualSpecification class attributes and methods

# gastm_VariableDefinition class attributes and methods

# DataDefinition class attributes and methods

# gastm_BitFieldDefinition class attributes and methods

# gastm_EntryDefinition class attributes and methods

# gastm_DataDefinition class attributes and methods
gastm_DataDefinition_isMutable: Property = Property(name="isMutable", type=StringType)
gastm_DataDefinition.attributes={gastm_DataDefinition_isMutable}

# gastm_EnumLiteralDefinition class attributes and methods

# gastm_FunctionDeclaration class attributes and methods

# Declaration class attributes and methods

# gastm_FormalParameterDeclaration class attributes and methods

# gastm_VariableDeclaration class attributes and methods
gastm_VariableDeclaration_isMutable: Property = Property(name="isMutable", type=StringType)
gastm_VariableDeclaration.attributes={gastm_VariableDeclaration_isMutable}

# gastm_MacroDefinition class attributes and methods
gastm_MacroDefinition_macroName: Property = Property(name="macroName", type=StringType)
gastm_MacroDefinition_body: Property = Property(name="body", type=StringType)
gastm_MacroDefinition.attributes={gastm_MacroDefinition_macroName, gastm_MacroDefinition_body}

# gastm_Comment class attributes and methods
gastm_Comment_body: Property = Property(name="body", type=StringType)
gastm_Comment.attributes={gastm_Comment_body}

# gastm_FunctionType class attributes and methods

# Type class attributes and methods

# gastm_FormalParameterType class attributes and methods

# gastm_NamedTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# gastm_NamedType class attributes and methods

# gastm_AggregateTypeDefinition class attributes and methods

# gastm_AggregateType class attributes and methods

# gastm_EnumTypeDefinition class attributes and methods

# gastm_EnumType class attributes and methods

# gastm_AggregateTypeDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# gastm_EnumTypeDeclaration class attributes and methods

# gastm_IncludeUnit class attributes and methods

# PreprocessorElement class attributes and methods

# gastm_MacroCall class attributes and methods

# gastm_ExceptionType class attributes and methods

# gastm_DataType class attributes and methods

# gastm_PrimitiveType class attributes and methods

# DataType class attributes and methods

# gastm_ConstructedType class attributes and methods

# gastm_PointerType class attributes and methods
gastm_PointerType_size: Property = Property(name="size", type=StringType)
gastm_PointerType.attributes={gastm_PointerType_size}

# gastm_ReferenceType class attributes and methods

# gastm_RangeType class attributes and methods

# gastm_ArrayType class attributes and methods

# gastm_StructureType class attributes and methods

# AggregateType class attributes and methods

# gastm_UnionType class attributes and methods

# gastm_ClassType class attributes and methods

# gastm_AnnotationType class attributes and methods

# gastm_ByValueFormalParameterType class attributes and methods

# FormalParameterType class attributes and methods

# gastm_ByReferenceFormalParameterType class attributes and methods

# gastm_NumberType class attributes and methods
gastm_NumberType_isSigned: Property = Property(name="isSigned", type=StringType)
gastm_NumberType.attributes={gastm_NumberType_isSigned}

# PrimitiveType class attributes and methods

# gastm_Void class attributes and methods

# gastm_Boolean class attributes and methods

# gastm_IntegralType class attributes and methods
gastm_IntegralType_size: Property = Property(name="size", type=StringType)
gastm_IntegralType.attributes={gastm_IntegralType_size}

# NumberType class attributes and methods

# gastm_RealType class attributes and methods
gastm_RealType_precision: Property = Property(name="precision", type=StringType)
gastm_RealType.attributes={gastm_RealType_precision}

# gastm_Byte class attributes and methods

# gastm_Character class attributes and methods

# gastm_ShortInteger class attributes and methods

# IntegralType class attributes and methods

# gastm_Integer class attributes and methods

# IntegerLiteral class attributes and methods

# gastm_LongInteger class attributes and methods

# gastm_Real class attributes and methods

# RealType class attributes and methods

# gastm_Double class attributes and methods

# gastm_LongDouble class attributes and methods

# gastm_CollectionType class attributes and methods

# ConstructedType class attributes and methods

# gastm_LabeledStatement class attributes and methods

# gastm_BlockStatement class attributes and methods

# gastm_EmptyStatement class attributes and methods

# gastm_IfStatement class attributes and methods

# gastm_Public class attributes and methods

# AccessKind class attributes and methods

# gastm_Protected class attributes and methods

# gastm_Private class attributes and methods

# gastm_UnnamedTypeReference class attributes and methods

# TypeReference class attributes and methods

# gastm_ExpressionStatement class attributes and methods

# Statement class attributes and methods

# gastm_JumpStatement class attributes and methods

# gastm_BreakStatement class attributes and methods

# gastm_LabelAccess class attributes and methods

# gastm_ContinueStatement class attributes and methods

# gastm_DeclarationOrDefinitionStatement class attributes and methods

# gastm_ThrowStatement class attributes and methods

# gastm_SwitchStatement class attributes and methods

# gastm_ReturnStatement class attributes and methods

# gastm_LoopStatement class attributes and methods

# gastm_TryStatement class attributes and methods

# gastm_WhileStatement class attributes and methods

# LoopStatement class attributes and methods

# gastm_DoWhileStatement class attributes and methods

# gastm_ForStatement class attributes and methods

# gastm_DeleteStatement class attributes and methods

# gastm_TerminateStatement class attributes and methods

# gastm_CaseBlock class attributes and methods

# SwitchCase class attributes and methods

# gastm_DefaultBlock class attributes and methods

# gastm_AggregateExpression class attributes and methods

# gastm_UnaryExpression class attributes and methods

# gastm_BinaryExpression class attributes and methods

# gastm_ForCheckBeforeStatement class attributes and methods

# ForStatement class attributes and methods

# gastm_ForCheckAfterStatement class attributes and methods

# gastm_TypesCatchBlock class attributes and methods

# CatchBlock class attributes and methods

# gastm_VariableCatchBlock class attributes and methods

# gastm_Literal class attributes and methods
gastm_Literal_value: Property = Property(name="value", type=StringType)
gastm_Literal.attributes={gastm_Literal_value}

# Expression class attributes and methods

# gastm_CastExpression class attributes and methods

# gastm_NewExpression class attributes and methods

# gastm_NameReference class attributes and methods

# gastm_ConditionalExpression class attributes and methods

# gastm_RangeExpression class attributes and methods

# gastm_FunctionCallExpression class attributes and methods

# gastm_CollectionExpression class attributes and methods

# gastm_ArrayAccess class attributes and methods

# gastm_BooleanLiteral class attributes and methods

# gastm_BitLiteral class attributes and methods

# gastm_EnumLiteral class attributes and methods

# gastm_UnaryPlus class attributes and methods

# UnaryOperator class attributes and methods

# gastm_UnaryMinus class attributes and methods

# gastm_Not class attributes and methods

# gastm_BitNot class attributes and methods

# gastm_AddressOf class attributes and methods

# gastm_IdentifierReference class attributes and methods

# NameReference class attributes and methods

# gastm_QualifiedIdentifierReference class attributes and methods

# gastm_TypeQualifiedIdentifierReference class attributes and methods

# gastm_QualifiedOverPointer class attributes and methods

# QualifiedIdentifierReference class attributes and methods

# gastm_QualifiedOverData class attributes and methods

# gastm_IntegerLiteral class attributes and methods

# Literal class attributes and methods

# gastm_CharLiteral class attributes and methods

# gastm_RealLiteral class attributes and methods

# gastm_StringLiteral class attributes and methods

# gastm_BitAnd class attributes and methods

# gastm_BitOr class attributes and methods

# gastm_BitXor class attributes and methods

# gastm_BitLeftShift class attributes and methods

# gastm_BitRightShift class attributes and methods

# gastm_Assign class attributes and methods

# gastm_OperatorAssign class attributes and methods

# gastm_ActualParameterExpression class attributes and methods

# ActualParameter class attributes and methods

# gastm_Deref class attributes and methods

# gastm_Increment class attributes and methods

# gastm_Decrement class attributes and methods

# gastm_PostIncrement class attributes and methods

# gastm_PostDecrement class attributes and methods

# gastm_Add class attributes and methods

# BinaryOperator class attributes and methods

# gastm_Subtract class attributes and methods

# gastm_Multiply class attributes and methods

# gastm_Divide class attributes and methods

# gastm_Modulus class attributes and methods

# gastm_Exponent class attributes and methods

# gastm_And class attributes and methods

# gastm_Or class attributes and methods

# gastm_Equal class attributes and methods

# gastm_NotEqual class attributes and methods

# gastm_Greater class attributes and methods

# gastm_NotGreater class attributes and methods

# gastm_Less class attributes and methods

# gastm_NotLess class attributes and methods

# gastm_MissingActualParameter class attributes and methods

# gastm_ByValueActualParameterExpression class attributes and methods

# ActualParameterExpression class attributes and methods

# gastm_ByReferenceActualParameterExpression class attributes and methods

# Relationships
annotations3: BinaryAssociation = BinaryAssociation(
    name="annotations3",
    ends={
        Property(name="gastm_GASTMSyntaxObject4", type=gastm_AnnotationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="gastm_AnnotationExpression", type=gastm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1))
    }
)
inSourceFile5: BinaryAssociation = BinaryAssociation(
    name="inSourceFile5",
    ends={
        Property(name="gastm_SourceFile", type=gastm_SourceLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SourceLocation6", type=gastm_SourceFile, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
locationInfo0: BinaryAssociation = BinaryAssociation(
    name="locationInfo0",
    ends={
        Property(name="gastm_SourceLocation", type=gastm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_GASTMSyntaxObject", type=gastm_SourceLocation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
preProcessorElements1: BinaryAssociation = BinaryAssociation(
    name="preProcessorElements1",
    ends={
        Property(name="gastm_PreprocessorElement", type=gastm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_GASTMSyntaxObject2", type=gastm_PreprocessorElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childScope22: BinaryAssociation = BinaryAssociation(
    name="childScope22",
    ends={
        Property(name="gastm_Scope23", type=gastm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Scope21", type=gastm_Scope, multiplicity=Multiplicity(0, 9999))
    }
)
fragments7: BinaryAssociation = BinaryAssociation(
    name="fragments7",
    ends={
        Property(name="gastm_DefinitionObject", type=gastm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CompilationUnit", type=gastm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope8: BinaryAssociation = BinaryAssociation(
    name="opensScope8",
    ends={
        Property(name="gastm_ProgramScope", type=gastm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CompilationUnit9", type=gastm_ProgramScope, multiplicity=Multiplicity(0, 1))
    }
)
locationInfo10: BinaryAssociation = BinaryAssociation(
    name="locationInfo10",
    ends={
        Property(name="gastm_SourceLocation11", type=gastm_SourceFileReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SourceFileReference", type=gastm_SourceLocation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ofSourceFile12: BinaryAssociation = BinaryAssociation(
    name="ofSourceFile12",
    ends={
        Property(name="gastm_SourceFile14", type=gastm_SourceFileReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SourceFileReference13", type=gastm_SourceFile, multiplicity=Multiplicity(1, 1))
    }
)
files15: BinaryAssociation = BinaryAssociation(
    name="files15",
    ends={
        Property(name="gastm_CompilationUnit16", type=gastm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Project", type=gastm_CompilationUnit, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outerScope17: BinaryAssociation = BinaryAssociation(
    name="outerScope17",
    ends={
        Property(name="gastm_GlobalScope", type=gastm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Project18", type=gastm_GlobalScope, multiplicity=Multiplicity(0, 1))
    }
)
definitionObject19: BinaryAssociation = BinaryAssociation(
    name="definitionObject19",
    ends={
        Property(name="gastm_DefinitionObject20", type=gastm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Scope", type=gastm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionType24: BinaryAssociation = BinaryAssociation(
    name="expressionType24",
    ends={
        Property(name="gastm_TypeReference", type=gastm_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Expression", type=gastm_TypeReference, multiplicity=Multiplicity(1, 1))
    }
)
lowBound25: BinaryAssociation = BinaryAssociation(
    name="lowBound25",
    ends={
        Property(name="gastm_Expression26", type=gastm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Dimension", type=gastm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
highBound27: BinaryAssociation = BinaryAssociation(
    name="highBound27",
    ends={
        Property(name="gastm_Expression29", type=gastm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Dimension28", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body30: BinaryAssociation = BinaryAssociation(
    name="body30",
    ends={
        Property(name="gastm_Statement", type=gastm_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SwitchCase", type=gastm_Statement, multiplicity=Multiplicity(1, 9999))
    }
)
body31: BinaryAssociation = BinaryAssociation(
    name="body31",
    ends={
        Property(name="gastm_Statement32", type=gastm_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CatchBlock", type=gastm_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeName46: BinaryAssociation = BinaryAssociation(
    name="typeName46",
    ends={
        Property(name="gastm_Name", type=gastm_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TypeDefinition", type=gastm_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nameSpace47: BinaryAssociation = BinaryAssociation(
    name="nameSpace47",
    ends={
        Property(name="gastm_Name48", type=gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NameSpaceDefinition", type=gastm_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body49: BinaryAssociation = BinaryAssociation(
    name="body49",
    ends={
        Property(name="gastm_DefinitionObject51", type=gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NameSpaceDefinition50", type=gastm_DefinitionObject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
nameSpaceType52: BinaryAssociation = BinaryAssociation(
    name="nameSpaceType52",
    ends={
        Property(name="gastm_NameSpaceType", type=gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NameSpaceDefinition53", type=gastm_NameSpaceType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
virtualSpecifier33: BinaryAssociation = BinaryAssociation(
    name="virtualSpecifier33",
    ends={
        Property(name="gastm_VirtualSpecification", type=gastm_FunctionMemberAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionMemberAttributes", type=gastm_VirtualSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
virtualSpecifier34: BinaryAssociation = BinaryAssociation(
    name="virtualSpecifier34",
    ends={
        Property(name="gastm_VirtualSpecification35", type=gastm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DerivesFrom", type=gastm_VirtualSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessKind36: BinaryAssociation = BinaryAssociation(
    name="accessKind36",
    ends={
        Property(name="gastm_AccessKind", type=gastm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DerivesFrom37", type=gastm_AccessKind, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
className38: BinaryAssociation = BinaryAssociation(
    name="className38",
    ends={
        Property(name="gastm_NamedTypeReference", type=gastm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DerivesFrom39", type=gastm_NamedTypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member40: BinaryAssociation = BinaryAssociation(
    name="member40",
    ends={
        Property(name="gastm_DefinitionObject41", type=gastm_MemberObject, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_MemberObject", type=gastm_DefinitionObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
storageSpecifiers42: BinaryAssociation = BinaryAssociation(
    name="storageSpecifiers42",
    ends={
        Property(name="gastm_StorageSpecification", type=gastm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DeclarationOrDefinition", type=gastm_StorageSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accessKind43: BinaryAssociation = BinaryAssociation(
    name="accessKind43",
    ends={
        Property(name="gastm_AccessKind45", type=gastm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DeclarationOrDefinition44", type=gastm_AccessKind, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarationType70: BinaryAssociation = BinaryAssociation(
    name="declarationType70",
    ends={
        Property(name="gastm_TypeReference72", type=gastm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Declaration71", type=gastm_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType73: BinaryAssociation = BinaryAssociation(
    name="returnType73",
    ends={
        Property(name="gastm_TypeReference74", type=gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDefinition", type=gastm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters75: BinaryAssociation = BinaryAssociation(
    name="formalParameters75",
    ends={
        Property(name="gastm_FormalParameterDefinition", type=gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDefinition76", type=gastm_FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body77: BinaryAssociation = BinaryAssociation(
    name="body77",
    ends={
        Property(name="gastm_Statement79", type=gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDefinition78", type=gastm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes80: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes80",
    ends={
        Property(name="gastm_FunctionMemberAttributes82", type=gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDefinition81", type=gastm_FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opensScope83: BinaryAssociation = BinaryAssociation(
    name="opensScope83",
    ends={
        Property(name="gastm_FunctionScope", type=gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDefinition84", type=gastm_FunctionScope, multiplicity=Multiplicity(1, 1))
    }
)
labelName54: BinaryAssociation = BinaryAssociation(
    name="labelName54",
    ends={
        Property(name="gastm_Name55", type=gastm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabelDefinition", type=gastm_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
labelType56: BinaryAssociation = BinaryAssociation(
    name="labelType56",
    ends={
        Property(name="gastm_LabelType", type=gastm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabelDefinition57", type=gastm_LabelType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeRef58: BinaryAssociation = BinaryAssociation(
    name="typeRef58",
    ends={
        Property(name="gastm_TypeReference59", type=gastm_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TypeDeclaration", type=gastm_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
identifierName60: BinaryAssociation = BinaryAssociation(
    name="identifierName60",
    ends={
        Property(name="gastm_Name61", type=gastm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Definition", type=gastm_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitionType62: BinaryAssociation = BinaryAssociation(
    name="definitionType62",
    ends={
        Property(name="gastm_TypeReference64", type=gastm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Definition63", type=gastm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defRef65: BinaryAssociation = BinaryAssociation(
    name="defRef65",
    ends={
        Property(name="gastm_Definition66", type=gastm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Declaration", type=gastm_Definition, multiplicity=Multiplicity(1, 1))
    }
)
identifierName67: BinaryAssociation = BinaryAssociation(
    name="identifierName67",
    ends={
        Property(name="gastm_Name69", type=gastm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Declaration68", type=gastm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters85: BinaryAssociation = BinaryAssociation(
    name="formalParameters85",
    ends={
        Property(name="gastm_FormalParameterDefinition86", type=gastm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_EntryDefinition", type=gastm_FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body87: BinaryAssociation = BinaryAssociation(
    name="body87",
    ends={
        Property(name="gastm_Statement89", type=gastm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_EntryDefinition88", type=gastm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue90: BinaryAssociation = BinaryAssociation(
    name="initialValue90",
    ends={
        Property(name="gastm_Expression91", type=gastm_DataDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DataDefinition", type=gastm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value92: BinaryAssociation = BinaryAssociation(
    name="value92",
    ends={
        Property(name="gastm_Expression93", type=gastm_EnumLiteralDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_EnumLiteralDefinition", type=gastm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters94: BinaryAssociation = BinaryAssociation(
    name="formalParameters94",
    ends={
        Property(name="gastm_FormalParameterDeclaration", type=gastm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDeclaration", type=gastm_FormalParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes95: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes95",
    ends={
        Property(name="gastm_FunctionMemberAttributes97", type=gastm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDeclaration96", type=gastm_FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo105: BinaryAssociation = BinaryAssociation(
    name="refersTo105",
    ends={
        Property(name="gastm_MacroDefinition", type=gastm_MacroCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_MacroCall", type=gastm_MacroDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType106: BinaryAssociation = BinaryAssociation(
    name="returnType106",
    ends={
        Property(name="gastm_TypeReference107", type=gastm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionType", type=gastm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterTypes108: BinaryAssociation = BinaryAssociation(
    name="parameterTypes108",
    ends={
        Property(name="gastm_FormalParameterType", type=gastm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionType109", type=gastm_FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bitFieldSize98: BinaryAssociation = BinaryAssociation(
    name="bitFieldSize98",
    ends={
        Property(name="gastm_Expression99", type=gastm_BitFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BitFieldDefinition", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitionType100: BinaryAssociation = BinaryAssociation(
    name="definitionType100",
    ends={
        Property(name="gastm_NamedType", type=gastm_NamedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NamedTypeDefinition", type=gastm_NamedType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
aggregateType101: BinaryAssociation = BinaryAssociation(
    name="aggregateType101",
    ends={
        Property(name="gastm_AggregateType", type=gastm_AggregateTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AggregateTypeDefinition", type=gastm_AggregateType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitionType102: BinaryAssociation = BinaryAssociation(
    name="definitionType102",
    ends={
        Property(name="gastm_EnumType", type=gastm_EnumTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_EnumTypeDefinition", type=gastm_EnumType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
file103: BinaryAssociation = BinaryAssociation(
    name="file103",
    ends={
        Property(name="gastm_SourceFileReference104", type=gastm_IncludeUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_IncludeUnit", type=gastm_SourceFileReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
opensScope118: BinaryAssociation = BinaryAssociation(
    name="opensScope118",
    ends={
        Property(name="gastm_AggregateScope", type=gastm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AggregateType119", type=gastm_AggregateScope, multiplicity=Multiplicity(1, 1))
    }
)
type120: BinaryAssociation = BinaryAssociation(
    name="type120",
    ends={
        Property(name="gastm_TypeReference122", type=gastm_FormalParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FormalParameterType121", type=gastm_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body123: BinaryAssociation = BinaryAssociation(
    name="body123",
    ends={
        Property(name="gastm_Type", type=gastm_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NamedType124", type=gastm_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumLiterals110: BinaryAssociation = BinaryAssociation(
    name="enumLiterals110",
    ends={
        Property(name="gastm_EnumLiteralDefinition112", type=gastm_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_EnumType111", type=gastm_EnumLiteralDefinition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
baseType113: BinaryAssociation = BinaryAssociation(
    name="baseType113",
    ends={
        Property(name="gastm_TypeReference114", type=gastm_ConstructedType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ConstructedType", type=gastm_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
members115: BinaryAssociation = BinaryAssociation(
    name="members115",
    ends={
        Property(name="gastm_MemberObject117", type=gastm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AggregateType116", type=gastm_MemberObject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ranks125: BinaryAssociation = BinaryAssociation(
    name="ranks125",
    ends={
        Property(name="gastm_Dimension126", type=gastm_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ArrayType", type=gastm_Dimension, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
derivesFrom127: BinaryAssociation = BinaryAssociation(
    name="derivesFrom127",
    ends={
        Property(name="gastm_DerivesFrom128", type=gastm_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ClassType", type=gastm_DerivesFrom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target142: BinaryAssociation = BinaryAssociation(
    name="target142",
    ends={
        Property(name="gastm_LabelAccess143", type=gastm_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ContinueStatement", type=gastm_LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label144: BinaryAssociation = BinaryAssociation(
    name="label144",
    ends={
        Property(name="gastm_LabelDefinition145", type=gastm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabeledStatement", type=gastm_LabelDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement146: BinaryAssociation = BinaryAssociation(
    name="statement146",
    ends={
        Property(name="gastm_Statement148", type=gastm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabeledStatement147", type=gastm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subStatements149: BinaryAssociation = BinaryAssociation(
    name="subStatements149",
    ends={
        Property(name="gastm_Statement150", type=gastm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BlockStatement", type=gastm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope151: BinaryAssociation = BinaryAssociation(
    name="opensScope151",
    ends={
        Property(name="gastm_BlockScope", type=gastm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BlockStatement152", type=gastm_BlockScope, multiplicity=Multiplicity(1, 1))
    }
)
condition153: BinaryAssociation = BinaryAssociation(
    name="condition153",
    ends={
        Property(name="gastm_Expression154", type=gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_IfStatement", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type129: BinaryAssociation = BinaryAssociation(
    name="type129",
    ends={
        Property(name="gastm_Type130", type=gastm_UnnamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_UnnamedTypeReference", type=gastm_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeName131: BinaryAssociation = BinaryAssociation(
    name="typeName131",
    ends={
        Property(name="gastm_Name133", type=gastm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NamedTypeReference132", type=gastm_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type134: BinaryAssociation = BinaryAssociation(
    name="type134",
    ends={
        Property(name="gastm_TypeDefinition136", type=gastm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NamedTypeReference135", type=gastm_TypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression137: BinaryAssociation = BinaryAssociation(
    name="expression137",
    ends={
        Property(name="gastm_Expression138", type=gastm_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ExpressionStatement", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target139: BinaryAssociation = BinaryAssociation(
    name="target139",
    ends={
        Property(name="gastm_Expression140", type=gastm_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_JumpStatement", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target141: BinaryAssociation = BinaryAssociation(
    name="target141",
    ends={
        Property(name="gastm_LabelAccess", type=gastm_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BreakStatement", type=gastm_LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchBlocks175: BinaryAssociation = BinaryAssociation(
    name="catchBlocks175",
    ends={
        Property(name="gastm_CatchBlock177", type=gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TryStatement176", type=gastm_CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalStatement178: BinaryAssociation = BinaryAssociation(
    name="finalStatement178",
    ends={
        Property(name="gastm_Statement180", type=gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TryStatement179", type=gastm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declOrDefn181: BinaryAssociation = BinaryAssociation(
    name="declOrDefn181",
    ends={
        Property(name="gastm_DefinitionObject182", type=gastm_DeclarationOrDefinitionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DeclarationOrDefinitionStatement", type=gastm_DefinitionObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenBody155: BinaryAssociation = BinaryAssociation(
    name="thenBody155",
    ends={
        Property(name="gastm_Statement157", type=gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_IfStatement156", type=gastm_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception183: BinaryAssociation = BinaryAssociation(
    name="exception183",
    ends={
        Property(name="gastm_Expression184", type=gastm_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ThrowStatement", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBody158: BinaryAssociation = BinaryAssociation(
    name="elseBody158",
    ends={
        Property(name="gastm_Statement160", type=gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_IfStatement159", type=gastm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchExpression161: BinaryAssociation = BinaryAssociation(
    name="switchExpression161",
    ends={
        Property(name="gastm_Expression162", type=gastm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SwitchStatement", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases163: BinaryAssociation = BinaryAssociation(
    name="cases163",
    ends={
        Property(name="gastm_SwitchCase165", type=gastm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SwitchStatement164", type=gastm_SwitchCase, multiplicity=Multiplicity(1, 1))
    }
)
returnValue166: BinaryAssociation = BinaryAssociation(
    name="returnValue166",
    ends={
        Property(name="gastm_Expression167", type=gastm_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ReturnStatement", type=gastm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition168: BinaryAssociation = BinaryAssociation(
    name="condition168",
    ends={
        Property(name="gastm_Expression169", type=gastm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LoopStatement", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body170: BinaryAssociation = BinaryAssociation(
    name="body170",
    ends={
        Property(name="gastm_Statement172", type=gastm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LoopStatement171", type=gastm_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guardedStatement173: BinaryAssociation = BinaryAssociation(
    name="guardedStatement173",
    ends={
        Property(name="gastm_Statement174", type=gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TryStatement", type=gastm_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initBody189: BinaryAssociation = BinaryAssociation(
    name="initBody189",
    ends={
        Property(name="gastm_Expression190", type=gastm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ForStatement", type=gastm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand185: BinaryAssociation = BinaryAssociation(
    name="operand185",
    ends={
        Property(name="gastm_Expression186", type=gastm_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DeleteStatement", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
caseExpressions187: BinaryAssociation = BinaryAssociation(
    name="caseExpressions187",
    ends={
        Property(name="gastm_Expression188", type=gastm_CaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CaseBlock", type=gastm_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subExpressions203: BinaryAssociation = BinaryAssociation(
    name="subExpressions203",
    ends={
        Property(name="gastm_Expression204", type=gastm_AggregateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AggregateExpression", type=gastm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operator205: BinaryAssociation = BinaryAssociation(
    name="operator205",
    ends={
        Property(name="gastm_UnaryOperator", type=gastm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_UnaryExpression", type=gastm_UnaryOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand206: BinaryAssociation = BinaryAssociation(
    name="operand206",
    ends={
        Property(name="gastm_Expression208", type=gastm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_UnaryExpression207", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator209: BinaryAssociation = BinaryAssociation(
    name="operator209",
    ends={
        Property(name="gastm_BinaryOperator", type=gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BinaryExpression", type=gastm_BinaryOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterationBody191: BinaryAssociation = BinaryAssociation(
    name="iterationBody191",
    ends={
        Property(name="gastm_Expression193", type=gastm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ForStatement192", type=gastm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions194: BinaryAssociation = BinaryAssociation(
    name="exceptions194",
    ends={
        Property(name="gastm_Type195", type=gastm_TypesCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TypesCatchBlock", type=gastm_Type, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
exceptionVariable196: BinaryAssociation = BinaryAssociation(
    name="exceptionVariable196",
    ends={
        Property(name="gastm_DataDefinition197", type=gastm_VariableCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_VariableCatchBlock", type=gastm_DataDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
castType198: BinaryAssociation = BinaryAssociation(
    name="castType198",
    ends={
        Property(name="gastm_TypeReference199", type=gastm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CastExpression", type=gastm_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression200: BinaryAssociation = BinaryAssociation(
    name="expression200",
    ends={
        Property(name="gastm_Expression202", type=gastm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CastExpression201", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
calledFunction229: BinaryAssociation = BinaryAssociation(
    name="calledFunction229",
    ends={
        Property(name="gastm_FunctionCallExpression", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="gastm_Expression230", type=gastm_FunctionCallExpression, multiplicity=Multiplicity(1, 1))
    }
)
actualParams231: BinaryAssociation = BinaryAssociation(
    name="actualParams231",
    ends={
        Property(name="gastm_ActualParameter", type=gastm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionCallExpression232", type=gastm_ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
newType233: BinaryAssociation = BinaryAssociation(
    name="newType233",
    ends={
        Property(name="gastm_TypeReference234", type=gastm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NewExpression", type=gastm_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualParams235: BinaryAssociation = BinaryAssociation(
    name="actualParams235",
    ends={
        Property(name="gastm_ActualParameter237", type=gastm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NewExpression236", type=gastm_ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand210: BinaryAssociation = BinaryAssociation(
    name="leftOperand210",
    ends={
        Property(name="gastm_Expression212", type=gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BinaryExpression211", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand213: BinaryAssociation = BinaryAssociation(
    name="rightOperand213",
    ends={
        Property(name="gastm_Expression215", type=gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BinaryExpression214", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition216: BinaryAssociation = BinaryAssociation(
    name="condition216",
    ends={
        Property(name="gastm_Expression217", type=gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ConditionalExpression", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
onTrueOperand218: BinaryAssociation = BinaryAssociation(
    name="onTrueOperand218",
    ends={
        Property(name="gastm_Expression220", type=gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ConditionalExpression219", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
onFalseOperand221: BinaryAssociation = BinaryAssociation(
    name="onFalseOperand221",
    ends={
        Property(name="gastm_Expression223", type=gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ConditionalExpression222", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fromExpression224: BinaryAssociation = BinaryAssociation(
    name="fromExpression224",
    ends={
        Property(name="gastm_Expression225", type=gastm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_RangeExpression", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
toExpression226: BinaryAssociation = BinaryAssociation(
    name="toExpression226",
    ends={
        Property(name="gastm_Expression228", type=gastm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_RangeExpression227", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subscripts251: BinaryAssociation = BinaryAssociation(
    name="subscripts251",
    ends={
        Property(name="gastm_Expression253", type=gastm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ArrayAccess252", type=gastm_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
annotationType254: BinaryAssociation = BinaryAssociation(
    name="annotationType254",
    ends={
        Property(name="gastm_TypeReference256", type=gastm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AnnotationExpression255", type=gastm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberValues257: BinaryAssociation = BinaryAssociation(
    name="memberValues257",
    ends={
        Property(name="gastm_Expression259", type=gastm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AnnotationExpression258", type=gastm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionList260: BinaryAssociation = BinaryAssociation(
    name="expressionList260",
    ends={
        Property(name="gastm_Expression261", type=gastm_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CollectionExpression", type=gastm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name238: BinaryAssociation = BinaryAssociation(
    name="name238",
    ends={
        Property(name="gastm_Name239", type=gastm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NameReference", type=gastm_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refersTo240: BinaryAssociation = BinaryAssociation(
    name="refersTo240",
    ends={
        Property(name="gastm_DefinitionObject242", type=gastm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NameReference241", type=gastm_DefinitionObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
labelName243: BinaryAssociation = BinaryAssociation(
    name="labelName243",
    ends={
        Property(name="gastm_Name245", type=gastm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabelAccess244", type=gastm_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
labelDefinition246: BinaryAssociation = BinaryAssociation(
    name="labelDefinition246",
    ends={
        Property(name="gastm_LabelDefinition248", type=gastm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabelAccess247", type=gastm_LabelDefinition, multiplicity=Multiplicity(1, 1))
    }
)
arrayName249: BinaryAssociation = BinaryAssociation(
    name="arrayName249",
    ends={
        Property(name="gastm_Expression250", type=gastm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ArrayAccess", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifiers262: BinaryAssociation = BinaryAssociation(
    name="qualifiers262",
    ends={
        Property(name="gastm_Expression263", type=gastm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_QualifiedIdentifierReference", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member264: BinaryAssociation = BinaryAssociation(
    name="member264",
    ends={
        Property(name="gastm_IdentifierReference", type=gastm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_QualifiedIdentifierReference265", type=gastm_IdentifierReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
aggregateType266: BinaryAssociation = BinaryAssociation(
    name="aggregateType266",
    ends={
        Property(name="gastm_TypeReference267", type=gastm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TypeQualifiedIdentifierReference", type=gastm_TypeReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
member268: BinaryAssociation = BinaryAssociation(
    name="member268",
    ends={
        Property(name="gastm_IdentifierReference270", type=gastm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TypeQualifiedIdentifierReference269", type=gastm_IdentifierReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator271: BinaryAssociation = BinaryAssociation(
    name="operator271",
    ends={
        Property(name="gastm_BinaryOperator272", type=gastm_OperatorAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_OperatorAssign", type=gastm_BinaryOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value273: BinaryAssociation = BinaryAssociation(
    name="value273",
    ends={
        Property(name="gastm_Expression274", type=gastm_ActualParameterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ActualParameterExpression", type=gastm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_gastm_SourceFile_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=gastm_SourceFile)
gen_gastm_SourceLocation_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=gastm_SourceLocation)
gen_gastm_CompilationUnit_SourceFile = Generalization(general=SourceFile, specific=gastm_CompilationUnit)
gen_gastm_GASTMSourceObject_GASTMObject = Generalization(general=GASTMObject, specific=gastm_GASTMSourceObject)
gen_gastm_GASTMSemanticObject_GASTMObject = Generalization(general=GASTMObject, specific=gastm_GASTMSemanticObject)
gen_gastm_GASTMSyntaxObject_GASTMObject = Generalization(general=GASTMObject, specific=gastm_GASTMSyntaxObject)
gen_gastm_ProgramScope_Scope = Generalization(general=Scope, specific=gastm_ProgramScope)
gen_gastm_FunctionScope_Scope = Generalization(general=Scope, specific=gastm_FunctionScope)
gen_gastm_AggregateScope_Scope = Generalization(general=Scope, specific=gastm_AggregateScope)
gen_gastm_BlockScope_Scope = Generalization(general=Scope, specific=gastm_BlockScope)
gen_gastm_GlobalScope_Scope = Generalization(general=Scope, specific=gastm_GlobalScope)
gen_gastm_PreprocessorElement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_PreprocessorElement)
gen_gastm_DefinitionObject_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_DefinitionObject)
gen_gastm_Type_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_Type)
gen_gastm_Expression_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_Expression)
gen_gastm_SourceFileReference_SourceFile = Generalization(general=SourceFile, specific=gastm_SourceFileReference)
gen_gastm_Project_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=gastm_Project)
gen_gastm_Scope_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=gastm_Scope)
gen_gastm_UnaryOperator_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_UnaryOperator)
gen_gastm_BinaryOperator_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_BinaryOperator)
gen_gastm_StorageSpecification_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_StorageSpecification)
gen_gastm_VirtualSpecification_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_VirtualSpecification)
gen_gastm_AccessKind_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_AccessKind)
gen_gastm_ActualParameter_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_ActualParameter)
gen_gastm_FunctionMemberAttributes_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_FunctionMemberAttributes)
gen_gastm_Statement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_Statement)
gen_gastm_MinorSyntaxObject_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_MinorSyntaxObject)
gen_gastm_Dimension_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_Dimension)
gen_gastm_Name_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_Name)
gen_gastm_SwitchCase_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_SwitchCase)
gen_gastm_CatchBlock_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_CatchBlock)
gen_gastm_TypeDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=gastm_TypeDefinition)
gen_gastm_NameSpaceDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=gastm_NameSpaceDefinition)
gen_gastm_LabelDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=gastm_LabelDefinition)
gen_gastm_DerivesFrom_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_DerivesFrom)
gen_gastm_MemberObject_MinorSyntaxObject = Generalization(general=MinorSyntaxObject, specific=gastm_MemberObject)
gen_gastm_DeclarationOrDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=gastm_DeclarationOrDefinition)
gen_gastm_FunctionDefinition_Definition = Generalization(general=Definition, specific=gastm_FunctionDefinition)
gen_gastm_TypeDeclaration_DefinitionObject = Generalization(general=DefinitionObject, specific=gastm_TypeDeclaration)
gen_gastm_Definition_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=gastm_Definition)
gen_gastm_Declaration_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=gastm_Declaration)
gen_gastm_FormalParameterDeclaration_Declaration = Generalization(general=Declaration, specific=gastm_FormalParameterDeclaration)
gen_gastm_External_StorageSpecification = Generalization(general=StorageSpecification, specific=gastm_External)
gen_gastm_FunctionPersistent_StorageSpecification = Generalization(general=StorageSpecification, specific=gastm_FunctionPersistent)
gen_gastm_FileLocal_StorageSpecification = Generalization(general=StorageSpecification, specific=gastm_FileLocal)
gen_gastm_PerClassMember_StorageSpecification = Generalization(general=StorageSpecification, specific=gastm_PerClassMember)
gen_gastm_NoDef_StorageSpecification = Generalization(general=StorageSpecification, specific=gastm_NoDef)
gen_gastm_Virtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=gastm_Virtual)
gen_gastm_VariableDefinition_DataDefinition = Generalization(general=DataDefinition, specific=gastm_VariableDefinition)
gen_gastm_FormalParameterDefinition_DataDefinition = Generalization(general=DataDefinition, specific=gastm_FormalParameterDefinition)
gen_gastm_BitFieldDefinition_DataDefinition = Generalization(general=DataDefinition, specific=gastm_BitFieldDefinition)
gen_gastm_EntryDefinition_Definition = Generalization(general=Definition, specific=gastm_EntryDefinition)
gen_gastm_DataDefinition_Definition = Generalization(general=Definition, specific=gastm_DataDefinition)
gen_gastm_EnumLiteralDefinition_Definition = Generalization(general=Definition, specific=gastm_EnumLiteralDefinition)
gen_gastm_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=gastm_FunctionDeclaration)
gen_gastm_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=gastm_VariableDeclaration)
gen_gastm_MacroDefinition_PreprocessorElement = Generalization(general=PreprocessorElement, specific=gastm_MacroDefinition)
gen_gastm_Comment_PreprocessorElement = Generalization(general=PreprocessorElement, specific=gastm_Comment)
gen_gastm_FunctionType_Type = Generalization(general=Type, specific=gastm_FunctionType)
gen_gastm_NamedTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=gastm_NamedTypeDefinition)
gen_gastm_AggregateTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=gastm_AggregateTypeDefinition)
gen_gastm_EnumTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=gastm_EnumTypeDefinition)
gen_gastm_AggregateTypeDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=gastm_AggregateTypeDeclaration)
gen_gastm_EnumTypeDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=gastm_EnumTypeDeclaration)
gen_gastm_IncludeUnit_PreprocessorElement = Generalization(general=PreprocessorElement, specific=gastm_IncludeUnit)
gen_gastm_MacroCall_PreprocessorElement = Generalization(general=PreprocessorElement, specific=gastm_MacroCall)
gen_gastm_ExceptionType_DataType = Generalization(general=DataType, specific=gastm_ExceptionType)
gen_gastm_FormalParameterType_DataType = Generalization(general=DataType, specific=gastm_FormalParameterType)
gen_gastm_NamedType_DataType = Generalization(general=DataType, specific=gastm_NamedType)
gen_gastm_DataType_Type = Generalization(general=Type, specific=gastm_DataType)
gen_gastm_LabelType_Type = Generalization(general=Type, specific=gastm_LabelType)
gen_gastm_NameSpaceType_Type = Generalization(general=Type, specific=gastm_NameSpaceType)
gen_gastm_TypeReference_Type = Generalization(general=Type, specific=gastm_TypeReference)
gen_gastm_PrimitiveType_DataType = Generalization(general=DataType, specific=gastm_PrimitiveType)
gen_gastm_EnumType_DataType = Generalization(general=DataType, specific=gastm_EnumType)
gen_gastm_ConstructedType_DataType = Generalization(general=DataType, specific=gastm_ConstructedType)
gen_gastm_AggregateType_DataType = Generalization(general=DataType, specific=gastm_AggregateType)
gen_gastm_PointerType_ConstructedType = Generalization(general=ConstructedType, specific=gastm_PointerType)
gen_gastm_ReferenceType_ConstructedType = Generalization(general=ConstructedType, specific=gastm_ReferenceType)
gen_gastm_RangeType_ConstructedType = Generalization(general=ConstructedType, specific=gastm_RangeType)
gen_gastm_ArrayType_ConstructedType = Generalization(general=ConstructedType, specific=gastm_ArrayType)
gen_gastm_StructureType_AggregateType = Generalization(general=AggregateType, specific=gastm_StructureType)
gen_gastm_UnionType_AggregateType = Generalization(general=AggregateType, specific=gastm_UnionType)
gen_gastm_ClassType_AggregateType = Generalization(general=AggregateType, specific=gastm_ClassType)
gen_gastm_AnnotationType_AggregateType = Generalization(general=AggregateType, specific=gastm_AnnotationType)
gen_gastm_ByValueFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=gastm_ByValueFormalParameterType)
gen_gastm_NumberType_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_NumberType)
gen_gastm_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_Void)
gen_gastm_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_Boolean)
gen_gastm_IntegralType_NumberType = Generalization(general=NumberType, specific=gastm_IntegralType)
gen_gastm_RealType_NumberType = Generalization(general=NumberType, specific=gastm_RealType)
gen_gastm_Byte_NumberType = Generalization(general=NumberType, specific=gastm_Byte)
gen_gastm_Character_NumberType = Generalization(general=NumberType, specific=gastm_Character)
gen_gastm_ShortInteger_IntegralType = Generalization(general=IntegralType, specific=gastm_ShortInteger)
gen_gastm_Integer_IntegerLiteral = Generalization(general=IntegerLiteral, specific=gastm_Integer)
gen_gastm_LongInteger_IntegralType = Generalization(general=IntegralType, specific=gastm_LongInteger)
gen_gastm_Real_RealType = Generalization(general=RealType, specific=gastm_Real)
gen_gastm_Double_RealType = Generalization(general=RealType, specific=gastm_Double)
gen_gastm_LongDouble_RealType = Generalization(general=RealType, specific=gastm_LongDouble)
gen_gastm_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=gastm_CollectionType)
gen_gastm_LabeledStatement_Statement = Generalization(general=Statement, specific=gastm_LabeledStatement)
gen_gastm_BlockStatement_Statement = Generalization(general=Statement, specific=gastm_BlockStatement)
gen_gastm_EmptyStatement_Statement = Generalization(general=Statement, specific=gastm_EmptyStatement)
gen_gastm_IfStatement_Statement = Generalization(general=Statement, specific=gastm_IfStatement)
gen_gastm_ByReferenceFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=gastm_ByReferenceFormalParameterType)
gen_gastm_Public_AccessKind = Generalization(general=AccessKind, specific=gastm_Public)
gen_gastm_Protected_AccessKind = Generalization(general=AccessKind, specific=gastm_Protected)
gen_gastm_Private_AccessKind = Generalization(general=AccessKind, specific=gastm_Private)
gen_gastm_UnnamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=gastm_UnnamedTypeReference)
gen_gastm_NamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=gastm_NamedTypeReference)
gen_gastm_ExpressionStatement_Statement = Generalization(general=Statement, specific=gastm_ExpressionStatement)
gen_gastm_JumpStatement_Statement = Generalization(general=Statement, specific=gastm_JumpStatement)
gen_gastm_BreakStatement_Statement = Generalization(general=Statement, specific=gastm_BreakStatement)
gen_gastm_ContinueStatement_Statement = Generalization(general=Statement, specific=gastm_ContinueStatement)
gen_gastm_DeclarationOrDefinitionStatement_Statement = Generalization(general=Statement, specific=gastm_DeclarationOrDefinitionStatement)
gen_gastm_ThrowStatement_Statement = Generalization(general=Statement, specific=gastm_ThrowStatement)
gen_gastm_SwitchStatement_Statement = Generalization(general=Statement, specific=gastm_SwitchStatement)
gen_gastm_ReturnStatement_Statement = Generalization(general=Statement, specific=gastm_ReturnStatement)
gen_gastm_LoopStatement_Statement = Generalization(general=Statement, specific=gastm_LoopStatement)
gen_gastm_TryStatement_Statement = Generalization(general=Statement, specific=gastm_TryStatement)
gen_gastm_WhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=gastm_WhileStatement)
gen_gastm_DoWhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=gastm_DoWhileStatement)
gen_gastm_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=gastm_ForStatement)
gen_gastm_DeleteStatement_Statement = Generalization(general=Statement, specific=gastm_DeleteStatement)
gen_gastm_TerminateStatement_Statement = Generalization(general=Statement, specific=gastm_TerminateStatement)
gen_gastm_CaseBlock_SwitchCase = Generalization(general=SwitchCase, specific=gastm_CaseBlock)
gen_gastm_DefaultBlock_SwitchCase = Generalization(general=SwitchCase, specific=gastm_DefaultBlock)
gen_gastm_AggregateExpression_Expression = Generalization(general=Expression, specific=gastm_AggregateExpression)
gen_gastm_UnaryExpression_Expression = Generalization(general=Expression, specific=gastm_UnaryExpression)
gen_gastm_BinaryExpression_Expression = Generalization(general=Expression, specific=gastm_BinaryExpression)
gen_gastm_ForCheckBeforeStatement_ForStatement = Generalization(general=ForStatement, specific=gastm_ForCheckBeforeStatement)
gen_gastm_ForCheckAfterStatement_ForStatement = Generalization(general=ForStatement, specific=gastm_ForCheckAfterStatement)
gen_gastm_TypesCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=gastm_TypesCatchBlock)
gen_gastm_VariableCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=gastm_VariableCatchBlock)
gen_gastm_Literal_Expression = Generalization(general=Expression, specific=gastm_Literal)
gen_gastm_CastExpression_Expression = Generalization(general=Expression, specific=gastm_CastExpression)
gen_gastm_NewExpression_Expression = Generalization(general=Expression, specific=gastm_NewExpression)
gen_gastm_NameReference_Expression = Generalization(general=Expression, specific=gastm_NameReference)
gen_gastm_ConditionalExpression_Expression = Generalization(general=Expression, specific=gastm_ConditionalExpression)
gen_gastm_RangeExpression_Expression = Generalization(general=Expression, specific=gastm_RangeExpression)
gen_gastm_FunctionCallExpression_Expression = Generalization(general=Expression, specific=gastm_FunctionCallExpression)
gen_gastm_AnnotationExpression_Expression = Generalization(general=Expression, specific=gastm_AnnotationExpression)
gen_gastm_CollectionExpression_Expression = Generalization(general=Expression, specific=gastm_CollectionExpression)
gen_gastm_LabelAccess_Expression = Generalization(general=Expression, specific=gastm_LabelAccess)
gen_gastm_ArrayAccess_Expression = Generalization(general=Expression, specific=gastm_ArrayAccess)
gen_gastm_BooleanLiteral_Literal = Generalization(general=Literal, specific=gastm_BooleanLiteral)
gen_gastm_BitLiteral_Literal = Generalization(general=Literal, specific=gastm_BitLiteral)
gen_gastm_EnumLiteral_Literal = Generalization(general=Literal, specific=gastm_EnumLiteral)
gen_gastm_UnaryPlus_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_UnaryPlus)
gen_gastm_UnaryMinus_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_UnaryMinus)
gen_gastm_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_Not)
gen_gastm_BitNot_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_BitNot)
gen_gastm_AddressOf_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_AddressOf)
gen_gastm_IdentifierReference_NameReference = Generalization(general=NameReference, specific=gastm_IdentifierReference)
gen_gastm_QualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=gastm_QualifiedIdentifierReference)
gen_gastm_TypeQualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=gastm_TypeQualifiedIdentifierReference)
gen_gastm_QualifiedOverPointer_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=gastm_QualifiedOverPointer)
gen_gastm_QualifiedOverData_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=gastm_QualifiedOverData)
gen_gastm_IntegerLiteral_Literal = Generalization(general=Literal, specific=gastm_IntegerLiteral)
gen_gastm_CharLiteral_Literal = Generalization(general=Literal, specific=gastm_CharLiteral)
gen_gastm_RealLiteral_Literal = Generalization(general=Literal, specific=gastm_RealLiteral)
gen_gastm_StringLiteral_Literal = Generalization(general=Literal, specific=gastm_StringLiteral)
gen_gastm_BitAnd_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_BitAnd)
gen_gastm_BitOr_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_BitOr)
gen_gastm_BitXor_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_BitXor)
gen_gastm_BitLeftShift_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_BitLeftShift)
gen_gastm_BitRightShift_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_BitRightShift)
gen_gastm_Assign_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Assign)
gen_gastm_OperatorAssign_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_OperatorAssign)
gen_gastm_ActualParameterExpression_ActualParameter = Generalization(general=ActualParameter, specific=gastm_ActualParameterExpression)
gen_gastm_Deref_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_Deref)
gen_gastm_Increment_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_Increment)
gen_gastm_Decrement_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_Decrement)
gen_gastm_PostIncrement_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_PostIncrement)
gen_gastm_PostDecrement_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_PostDecrement)
gen_gastm_Add_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Add)
gen_gastm_Subtract_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Subtract)
gen_gastm_Multiply_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Multiply)
gen_gastm_Divide_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Divide)
gen_gastm_Modulus_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Modulus)
gen_gastm_Exponent_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Exponent)
gen_gastm_And_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_And)
gen_gastm_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Or)
gen_gastm_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Equal)
gen_gastm_NotEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_NotEqual)
gen_gastm_Greater_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Greater)
gen_gastm_NotGreater_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_NotGreater)
gen_gastm_Less_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Less)
gen_gastm_NotLess_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_NotLess)
gen_gastm_MissingActualParameter_ActualParameter = Generalization(general=ActualParameter, specific=gastm_MissingActualParameter)
gen_gastm_ByValueActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=gastm_ByValueActualParameterExpression)
gen_gastm_ByReferenceActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=gastm_ByReferenceActualParameterExpression)

# Domain Model
domain_model = DomainModel(
    name="gastm",
    types={gastm_SourceFile, GASTMSourceObject, gastm_CompilationUnit, SourceFile, gastm_GASTMObject, gastm_GASTMSourceObject, GASTMObject, gastm_GASTMSemanticObject, gastm_GASTMSyntaxObject, gastm_SourceLocation, gastm_PreprocessorElement, gastm_AnnotationExpression, Scope, gastm_FunctionScope, gastm_AggregateScope, gastm_BlockScope, GASTMSyntaxObject, gastm_Type, gastm_Expression, gastm_DefinitionObject, gastm_ProgramScope, gastm_SourceFileReference, gastm_Project, GASTMSemanticObject, gastm_GlobalScope, gastm_Scope, gastm_UnaryOperator, gastm_BinaryOperator, gastm_StorageSpecification, gastm_VirtualSpecification, gastm_AccessKind, gastm_ActualParameter, gastm_FunctionMemberAttributes, gastm_TypeReference, gastm_Statement, gastm_MinorSyntaxObject, gastm_Dimension, MinorSyntaxObject, gastm_Name, gastm_SwitchCase, gastm_CatchBlock, gastm_TypeDefinition, gastm_NameSpaceDefinition, gastm_NameSpaceType, gastm_LabelDefinition, gastm_DerivesFrom, gastm_NamedTypeReference, gastm_MemberObject, gastm_DeclarationOrDefinition, DefinitionObject, gastm_FunctionDefinition, Definition, gastm_FormalParameterDefinition, gastm_LabelType, gastm_TypeDeclaration, gastm_Definition, DeclarationOrDefinition, gastm_Declaration, gastm_External, StorageSpecification, gastm_FunctionPersistent, gastm_FileLocal, gastm_PerClassMember, gastm_NoDef, gastm_Virtual, VirtualSpecification, gastm_VariableDefinition, DataDefinition, gastm_BitFieldDefinition, gastm_EntryDefinition, gastm_DataDefinition, gastm_EnumLiteralDefinition, gastm_FunctionDeclaration, Declaration, gastm_FormalParameterDeclaration, gastm_VariableDeclaration, gastm_MacroDefinition, gastm_Comment, gastm_FunctionType, Type, gastm_FormalParameterType, gastm_NamedTypeDefinition, TypeDefinition, gastm_NamedType, gastm_AggregateTypeDefinition, gastm_AggregateType, gastm_EnumTypeDefinition, gastm_EnumType, gastm_AggregateTypeDeclaration, TypeDeclaration, gastm_EnumTypeDeclaration, gastm_IncludeUnit, PreprocessorElement, gastm_MacroCall, gastm_ExceptionType, gastm_DataType, gastm_PrimitiveType, DataType, gastm_ConstructedType, gastm_PointerType, gastm_ReferenceType, gastm_RangeType, gastm_ArrayType, gastm_StructureType, AggregateType, gastm_UnionType, gastm_ClassType, gastm_AnnotationType, gastm_ByValueFormalParameterType, FormalParameterType, gastm_ByReferenceFormalParameterType, gastm_NumberType, PrimitiveType, gastm_Void, gastm_Boolean, gastm_IntegralType, NumberType, gastm_RealType, gastm_Byte, gastm_Character, gastm_ShortInteger, IntegralType, gastm_Integer, IntegerLiteral, gastm_LongInteger, gastm_Real, RealType, gastm_Double, gastm_LongDouble, gastm_CollectionType, ConstructedType, gastm_LabeledStatement, gastm_BlockStatement, gastm_EmptyStatement, gastm_IfStatement, gastm_Public, AccessKind, gastm_Protected, gastm_Private, gastm_UnnamedTypeReference, TypeReference, gastm_ExpressionStatement, Statement, gastm_JumpStatement, gastm_BreakStatement, gastm_LabelAccess, gastm_ContinueStatement, gastm_DeclarationOrDefinitionStatement, gastm_ThrowStatement, gastm_SwitchStatement, gastm_ReturnStatement, gastm_LoopStatement, gastm_TryStatement, gastm_WhileStatement, LoopStatement, gastm_DoWhileStatement, gastm_ForStatement, gastm_DeleteStatement, gastm_TerminateStatement, gastm_CaseBlock, SwitchCase, gastm_DefaultBlock, gastm_AggregateExpression, gastm_UnaryExpression, gastm_BinaryExpression, gastm_ForCheckBeforeStatement, ForStatement, gastm_ForCheckAfterStatement, gastm_TypesCatchBlock, CatchBlock, gastm_VariableCatchBlock, gastm_Literal, Expression, gastm_CastExpression, gastm_NewExpression, gastm_NameReference, gastm_ConditionalExpression, gastm_RangeExpression, gastm_FunctionCallExpression, gastm_CollectionExpression, gastm_ArrayAccess, gastm_BooleanLiteral, gastm_BitLiteral, gastm_EnumLiteral, gastm_UnaryPlus, UnaryOperator, gastm_UnaryMinus, gastm_Not, gastm_BitNot, gastm_AddressOf, gastm_IdentifierReference, NameReference, gastm_QualifiedIdentifierReference, gastm_TypeQualifiedIdentifierReference, gastm_QualifiedOverPointer, QualifiedIdentifierReference, gastm_QualifiedOverData, gastm_IntegerLiteral, Literal, gastm_CharLiteral, gastm_RealLiteral, gastm_StringLiteral, gastm_BitAnd, gastm_BitOr, gastm_BitXor, gastm_BitLeftShift, gastm_BitRightShift, gastm_Assign, gastm_OperatorAssign, gastm_ActualParameterExpression, ActualParameter, gastm_Deref, gastm_Increment, gastm_Decrement, gastm_PostIncrement, gastm_PostDecrement, gastm_Add, BinaryOperator, gastm_Subtract, gastm_Multiply, gastm_Divide, gastm_Modulus, gastm_Exponent, gastm_And, gastm_Or, gastm_Equal, gastm_NotEqual, gastm_Greater, gastm_NotGreater, gastm_Less, gastm_NotLess, gastm_MissingActualParameter, gastm_ByValueActualParameterExpression, ActualParameterExpression, gastm_ByReferenceActualParameterExpression},
    associations={annotations3, inSourceFile5, locationInfo0, preProcessorElements1, childScope22, fragments7, opensScope8, locationInfo10, ofSourceFile12, files15, outerScope17, definitionObject19, expressionType24, lowBound25, highBound27, body30, body31, typeName46, nameSpace47, body49, nameSpaceType52, virtualSpecifier33, virtualSpecifier34, accessKind36, className38, member40, storageSpecifiers42, accessKind43, declarationType70, returnType73, formalParameters75, body77, functionMemberAttributes80, opensScope83, labelName54, labelType56, typeRef58, identifierName60, definitionType62, defRef65, identifierName67, formalParameters85, body87, initialValue90, value92, formalParameters94, functionMemberAttributes95, refersTo105, returnType106, parameterTypes108, bitFieldSize98, definitionType100, aggregateType101, definitionType102, file103, opensScope118, type120, body123, enumLiterals110, baseType113, members115, ranks125, derivesFrom127, target142, label144, statement146, subStatements149, opensScope151, condition153, type129, typeName131, type134, expression137, target139, target141, catchBlocks175, finalStatement178, declOrDefn181, thenBody155, exception183, elseBody158, switchExpression161, cases163, returnValue166, condition168, body170, guardedStatement173, initBody189, operand185, caseExpressions187, subExpressions203, operator205, operand206, operator209, iterationBody191, exceptions194, exceptionVariable196, castType198, expression200, calledFunction229, actualParams231, newType233, actualParams235, leftOperand210, rightOperand213, condition216, onTrueOperand218, onFalseOperand221, fromExpression224, toExpression226, subscripts251, annotationType254, memberValues257, expressionList260, name238, refersTo240, labelName243, labelDefinition246, arrayName249, qualifiers262, member264, aggregateType266, member268, operator271, value273},
    generalizations={gen_gastm_SourceFile_GASTMSourceObject, gen_gastm_SourceLocation_GASTMSourceObject, gen_gastm_CompilationUnit_SourceFile, gen_gastm_GASTMSourceObject_GASTMObject, gen_gastm_GASTMSemanticObject_GASTMObject, gen_gastm_GASTMSyntaxObject_GASTMObject, gen_gastm_ProgramScope_Scope, gen_gastm_FunctionScope_Scope, gen_gastm_AggregateScope_Scope, gen_gastm_BlockScope_Scope, gen_gastm_GlobalScope_Scope, gen_gastm_PreprocessorElement_GASTMSyntaxObject, gen_gastm_DefinitionObject_GASTMSyntaxObject, gen_gastm_Type_GASTMSyntaxObject, gen_gastm_Expression_GASTMSyntaxObject, gen_gastm_SourceFileReference_SourceFile, gen_gastm_Project_GASTMSemanticObject, gen_gastm_Scope_GASTMSemanticObject, gen_gastm_UnaryOperator_MinorSyntaxObject, gen_gastm_BinaryOperator_MinorSyntaxObject, gen_gastm_StorageSpecification_MinorSyntaxObject, gen_gastm_VirtualSpecification_MinorSyntaxObject, gen_gastm_AccessKind_MinorSyntaxObject, gen_gastm_ActualParameter_MinorSyntaxObject, gen_gastm_FunctionMemberAttributes_MinorSyntaxObject, gen_gastm_Statement_GASTMSyntaxObject, gen_gastm_MinorSyntaxObject_GASTMSyntaxObject, gen_gastm_Dimension_MinorSyntaxObject, gen_gastm_Name_MinorSyntaxObject, gen_gastm_SwitchCase_MinorSyntaxObject, gen_gastm_CatchBlock_MinorSyntaxObject, gen_gastm_TypeDefinition_DefinitionObject, gen_gastm_NameSpaceDefinition_DefinitionObject, gen_gastm_LabelDefinition_DefinitionObject, gen_gastm_DerivesFrom_MinorSyntaxObject, gen_gastm_MemberObject_MinorSyntaxObject, gen_gastm_DeclarationOrDefinition_DefinitionObject, gen_gastm_FunctionDefinition_Definition, gen_gastm_TypeDeclaration_DefinitionObject, gen_gastm_Definition_DeclarationOrDefinition, gen_gastm_Declaration_DeclarationOrDefinition, gen_gastm_FormalParameterDeclaration_Declaration, gen_gastm_External_StorageSpecification, gen_gastm_FunctionPersistent_StorageSpecification, gen_gastm_FileLocal_StorageSpecification, gen_gastm_PerClassMember_StorageSpecification, gen_gastm_NoDef_StorageSpecification, gen_gastm_Virtual_VirtualSpecification, gen_gastm_VariableDefinition_DataDefinition, gen_gastm_FormalParameterDefinition_DataDefinition, gen_gastm_BitFieldDefinition_DataDefinition, gen_gastm_EntryDefinition_Definition, gen_gastm_DataDefinition_Definition, gen_gastm_EnumLiteralDefinition_Definition, gen_gastm_FunctionDeclaration_Declaration, gen_gastm_VariableDeclaration_Declaration, gen_gastm_MacroDefinition_PreprocessorElement, gen_gastm_Comment_PreprocessorElement, gen_gastm_FunctionType_Type, gen_gastm_NamedTypeDefinition_TypeDefinition, gen_gastm_AggregateTypeDefinition_TypeDefinition, gen_gastm_EnumTypeDefinition_TypeDefinition, gen_gastm_AggregateTypeDeclaration_TypeDeclaration, gen_gastm_EnumTypeDeclaration_TypeDeclaration, gen_gastm_IncludeUnit_PreprocessorElement, gen_gastm_MacroCall_PreprocessorElement, gen_gastm_ExceptionType_DataType, gen_gastm_FormalParameterType_DataType, gen_gastm_NamedType_DataType, gen_gastm_DataType_Type, gen_gastm_LabelType_Type, gen_gastm_NameSpaceType_Type, gen_gastm_TypeReference_Type, gen_gastm_PrimitiveType_DataType, gen_gastm_EnumType_DataType, gen_gastm_ConstructedType_DataType, gen_gastm_AggregateType_DataType, gen_gastm_PointerType_ConstructedType, gen_gastm_ReferenceType_ConstructedType, gen_gastm_RangeType_ConstructedType, gen_gastm_ArrayType_ConstructedType, gen_gastm_StructureType_AggregateType, gen_gastm_UnionType_AggregateType, gen_gastm_ClassType_AggregateType, gen_gastm_AnnotationType_AggregateType, gen_gastm_ByValueFormalParameterType_FormalParameterType, gen_gastm_NumberType_PrimitiveType, gen_gastm_Void_PrimitiveType, gen_gastm_Boolean_PrimitiveType, gen_gastm_IntegralType_NumberType, gen_gastm_RealType_NumberType, gen_gastm_Byte_NumberType, gen_gastm_Character_NumberType, gen_gastm_ShortInteger_IntegralType, gen_gastm_Integer_IntegerLiteral, gen_gastm_LongInteger_IntegralType, gen_gastm_Real_RealType, gen_gastm_Double_RealType, gen_gastm_LongDouble_RealType, gen_gastm_CollectionType_ConstructedType, gen_gastm_LabeledStatement_Statement, gen_gastm_BlockStatement_Statement, gen_gastm_EmptyStatement_Statement, gen_gastm_IfStatement_Statement, gen_gastm_ByReferenceFormalParameterType_FormalParameterType, gen_gastm_Public_AccessKind, gen_gastm_Protected_AccessKind, gen_gastm_Private_AccessKind, gen_gastm_UnnamedTypeReference_TypeReference, gen_gastm_NamedTypeReference_TypeReference, gen_gastm_ExpressionStatement_Statement, gen_gastm_JumpStatement_Statement, gen_gastm_BreakStatement_Statement, gen_gastm_ContinueStatement_Statement, gen_gastm_DeclarationOrDefinitionStatement_Statement, gen_gastm_ThrowStatement_Statement, gen_gastm_SwitchStatement_Statement, gen_gastm_ReturnStatement_Statement, gen_gastm_LoopStatement_Statement, gen_gastm_TryStatement_Statement, gen_gastm_WhileStatement_LoopStatement, gen_gastm_DoWhileStatement_LoopStatement, gen_gastm_ForStatement_LoopStatement, gen_gastm_DeleteStatement_Statement, gen_gastm_TerminateStatement_Statement, gen_gastm_CaseBlock_SwitchCase, gen_gastm_DefaultBlock_SwitchCase, gen_gastm_AggregateExpression_Expression, gen_gastm_UnaryExpression_Expression, gen_gastm_BinaryExpression_Expression, gen_gastm_ForCheckBeforeStatement_ForStatement, gen_gastm_ForCheckAfterStatement_ForStatement, gen_gastm_TypesCatchBlock_CatchBlock, gen_gastm_VariableCatchBlock_CatchBlock, gen_gastm_Literal_Expression, gen_gastm_CastExpression_Expression, gen_gastm_NewExpression_Expression, gen_gastm_NameReference_Expression, gen_gastm_ConditionalExpression_Expression, gen_gastm_RangeExpression_Expression, gen_gastm_FunctionCallExpression_Expression, gen_gastm_AnnotationExpression_Expression, gen_gastm_CollectionExpression_Expression, gen_gastm_LabelAccess_Expression, gen_gastm_ArrayAccess_Expression, gen_gastm_BooleanLiteral_Literal, gen_gastm_BitLiteral_Literal, gen_gastm_EnumLiteral_Literal, gen_gastm_UnaryPlus_UnaryOperator, gen_gastm_UnaryMinus_UnaryOperator, gen_gastm_Not_UnaryOperator, gen_gastm_BitNot_UnaryOperator, gen_gastm_AddressOf_UnaryOperator, gen_gastm_IdentifierReference_NameReference, gen_gastm_QualifiedIdentifierReference_NameReference, gen_gastm_TypeQualifiedIdentifierReference_NameReference, gen_gastm_QualifiedOverPointer_QualifiedIdentifierReference, gen_gastm_QualifiedOverData_QualifiedIdentifierReference, gen_gastm_IntegerLiteral_Literal, gen_gastm_CharLiteral_Literal, gen_gastm_RealLiteral_Literal, gen_gastm_StringLiteral_Literal, gen_gastm_BitAnd_BinaryOperator, gen_gastm_BitOr_BinaryOperator, gen_gastm_BitXor_BinaryOperator, gen_gastm_BitLeftShift_BinaryOperator, gen_gastm_BitRightShift_BinaryOperator, gen_gastm_Assign_BinaryOperator, gen_gastm_OperatorAssign_BinaryOperator, gen_gastm_ActualParameterExpression_ActualParameter, gen_gastm_Deref_UnaryOperator, gen_gastm_Increment_UnaryOperator, gen_gastm_Decrement_UnaryOperator, gen_gastm_PostIncrement_UnaryOperator, gen_gastm_PostDecrement_UnaryOperator, gen_gastm_Add_BinaryOperator, gen_gastm_Subtract_BinaryOperator, gen_gastm_Multiply_BinaryOperator, gen_gastm_Divide_BinaryOperator, gen_gastm_Modulus_BinaryOperator, gen_gastm_Exponent_BinaryOperator, gen_gastm_And_BinaryOperator, gen_gastm_Or_BinaryOperator, gen_gastm_Equal_BinaryOperator, gen_gastm_NotEqual_BinaryOperator, gen_gastm_Greater_BinaryOperator, gen_gastm_NotGreater_BinaryOperator, gen_gastm_Less_BinaryOperator, gen_gastm_NotLess_BinaryOperator, gen_gastm_MissingActualParameter_ActualParameter, gen_gastm_ByValueActualParameterExpression_ActualParameterExpression, gen_gastm_ByReferenceActualParameterExpression_ActualParameterExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)