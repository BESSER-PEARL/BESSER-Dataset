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
astm_gastm_GASTMObject = Class(name="astm::gastm::GASTMObject")
astm_gastm_GASTMSourceObject = Class(name="astm::gastm::GASTMSourceObject", is_abstract=True)
astm_gastm_GASTMSemanticObject = Class(name="astm::gastm::GASTMSemanticObject", is_abstract=True)
astm_gastm_OtherSyntaxObject = Class(name="astm::gastm::OtherSyntaxObject", is_abstract=True)
GASTMSyntaxObject = Class(name="GASTMSyntaxObject")
astm_gastm_StorageSpecification = Class(name="astm::gastm::StorageSpecification", is_abstract=True)
astm_gastm_DataType = Class(name="astm::gastm::DataType", is_abstract=True)
Type = Class(name="Type")
astm_gastm_AccessKind = Class(name="astm::gastm::AccessKind")
AnnotationExpression = Class(name="AnnotationExpression")
astm_gastm_CompilationUnit = Class(name="astm::gastm::CompilationUnit")
OtherSyntaxObject = Class(name="OtherSyntaxObject")
astm_gastm_UnaryOperator = Class(name="astm::gastm::UnaryOperator", is_abstract=True)
astm_gastm_BinaryOperator = Class(name="astm::gastm::BinaryOperator", is_abstract=True)
astm_gastm_ActualParameter = Class(name="astm::gastm::ActualParameter", is_abstract=True)
astm_gastm_SourceFile = Class(name="astm::gastm::SourceFile")
GASTMSourceObject = Class(name="GASTMSourceObject")
astm_gastm_SourceLocation = Class(name="astm::gastm::SourceLocation")
SourceFile = Class(name="SourceFile")
astm_gastm_Project = Class(name="astm::gastm::Project")
GASTMSemanticObject = Class(name="GASTMSemanticObject")
CompilationUnit = Class(name="CompilationUnit")
GlobalScope = Class(name="GlobalScope")
astm_gastm_Scope = Class(name="astm::gastm::Scope")
DefinitionObject = Class(name="DefinitionObject")
Scope = Class(name="Scope")
astm_gastm_GASTMSyntaxObject = Class(name="astm::gastm::GASTMSyntaxObject", is_abstract=True)
GASTMObject = Class(name="GASTMObject")
SourceLocation = Class(name="SourceLocation")
PreprocessorElement = Class(name="PreprocessorElement")
astm_gastm_FunctionDeclaration = Class(name="astm::gastm::FunctionDeclaration")
Declaration = Class(name="Declaration")
FormalParameterDeclaration = Class(name="FormalParameterDeclaration")
FunctionMemberAttributes = Class(name="FunctionMemberAttributes")
ProgramScope = Class(name="ProgramScope")
astm_gastm_Name = Class(name="astm::gastm::Name")
astm_gastm_DeclarationOrDefinition = Class(name="astm::gastm::DeclarationOrDefinition", is_abstract=True)
astm_gastm_Definition = Class(name="astm::gastm::Definition", is_abstract=True)
DeclarationOrDefinition = Class(name="DeclarationOrDefinition")
Name = Class(name="Name")
TypeReference = Class(name="TypeReference")
astm_gastm_Declaration = Class(name="astm::gastm::Declaration", is_abstract=True)
Definition = Class(name="Definition")
astm_gastm_DataDefinition = Class(name="astm::gastm::DataDefinition", is_abstract=True)
Expression = Class(name="Expression")
astm_gastm_BitFieldDefinition = Class(name="astm::gastm::BitFieldDefinition")
DataDefinition = Class(name="DataDefinition")
astm_gastm_VariableDeclaration = Class(name="astm::gastm::VariableDeclaration")
astm_gastm_FunctionDefinition = Class(name="astm::gastm::FunctionDefinition")
FormalParameterDefinition = Class(name="FormalParameterDefinition")
Statement = Class(name="Statement")
FunctionScope = Class(name="FunctionScope")
astm_gastm_FunctionMemberAttributes = Class(name="astm::gastm::FunctionMemberAttributes")
VirtualSpecification = Class(name="VirtualSpecification")
astm_gastm_EntryDefinition = Class(name="astm::gastm::EntryDefinition")
LabelType = Class(name="LabelType")
astm_gastm_IncludeUnit = Class(name="astm::gastm::IncludeUnit")
astm_gastm_EnumLiteralDefinition = Class(name="astm::gastm::EnumLiteralDefinition")
astm_gastm_TypeDefinition = Class(name="astm::gastm::TypeDefinition")
astm_gastm_NamedTypeDefinition = Class(name="astm::gastm::NamedTypeDefinition")
TypeDefinition = Class(name="TypeDefinition")
NamedType = Class(name="NamedType")
astm_gastm_AggregateTypeDefinition = Class(name="astm::gastm::AggregateTypeDefinition")
AggregateType = Class(name="AggregateType")
astm_gastm_NameSpaceDefinition = Class(name="astm::gastm::NameSpaceDefinition")
NameSpaceType = Class(name="NameSpaceType")
astm_gastm_LabelDefinition = Class(name="astm::gastm::LabelDefinition")
AggregateScope = Class(name="AggregateScope")
astm_gastm_ArrayType = Class(name="astm::gastm::ArrayType")
ConstructedType = Class(name="ConstructedType")
Dimension = Class(name="Dimension")
astm_gastm_Dimension = Class(name="astm::gastm::Dimension")
astm_gastm_MacroCall = Class(name="astm::gastm::MacroCall")
MacroDefinition = Class(name="MacroDefinition")
astm_gastm_MacroDefinition = Class(name="astm::gastm::MacroDefinition")
astm_gastm_Comment = Class(name="astm::gastm::Comment")
astm_gastm_Type = Class(name="astm::gastm::Type", is_abstract=True)
astm_gastm_PrimitiveType = Class(name="astm::gastm::PrimitiveType", is_abstract=True)
DataType = Class(name="DataType")
astm_gastm_EnumType = Class(name="astm::gastm::EnumType")
EnumLiteralDefinition = Class(name="EnumLiteralDefinition")
astm_gastm_ConstructedType = Class(name="astm::gastm::ConstructedType", is_abstract=True)
astm_gastm_AggregateType = Class(name="astm::gastm::AggregateType", is_abstract=True)
astm_gastm_UnnamedTypeReference = Class(name="astm::gastm::UnnamedTypeReference")
astm_gastm_NamedTypeReference = Class(name="astm::gastm::NamedTypeReference")
astm_gastm_FunctionType = Class(name="astm::gastm::FunctionType")
FormalParameterType = Class(name="FormalParameterType")
astm_gastm_FormalParameterType = Class(name="astm::gastm::FormalParameterType", is_abstract=True)
astm_gastm_NamedType = Class(name="astm::gastm::NamedType")
astm_gastm_ClassType = Class(name="astm::gastm::ClassType")
DerivesFrom = Class(name="DerivesFrom")
astm_gastm_DerivesFrom = Class(name="astm::gastm::DerivesFrom")
astm_gastm_BreakStatement = Class(name="astm::gastm::BreakStatement")
astm_gastm_DeleteStatement = Class(name="astm::gastm::DeleteStatement")
astm_gastm_DeclarationOrDefinitionStatement = Class(name="astm::gastm::DeclarationOrDefinitionStatement")
astm_gastm_ExpressionStatement = Class(name="astm::gastm::ExpressionStatement")
astm_gastm_JumpStatement = Class(name="astm::gastm::JumpStatement")
LabelAccess = Class(name="LabelAccess")
astm_gastm_SwitchStatement = Class(name="astm::gastm::SwitchStatement")
astm_gastm_ContinueStatement = Class(name="astm::gastm::ContinueStatement")
astm_gastm_LabeledStatement = Class(name="astm::gastm::LabeledStatement")
LabelDefinition = Class(name="LabelDefinition")
astm_gastm_BlockStatement = Class(name="astm::gastm::BlockStatement")
BlockScope = Class(name="BlockScope")
astm_gastm_EmptyStatement = Class(name="astm::gastm::EmptyStatement")
astm_gastm_IfStatement = Class(name="astm::gastm::IfStatement")
astm_gastm_TryStatement = Class(name="astm::gastm::TryStatement")
CatchBlock = Class(name="CatchBlock")
SwitchCase = Class(name="SwitchCase")
astm_gastm_SwitchCase = Class(name="astm::gastm::SwitchCase")
astm_gastm_CaseBlock = Class(name="astm::gastm::CaseBlock")
astm_gastm_ReturnStatement = Class(name="astm::gastm::ReturnStatement")
astm_gastm_LoopStatement = Class(name="astm::gastm::LoopStatement")
astm_gastm_ForStatement = Class(name="astm::gastm::ForStatement", is_abstract=True)
LoopStatement = Class(name="LoopStatement")
astm_gastm_QualifiedIdentifierReference = Class(name="astm::gastm::QualifiedIdentifierReference", is_abstract=True)
NameReference = Class(name="NameReference")
IdentifierReference = Class(name="IdentifierReference")
astm_gastm_TypeQualifiedIdentifierReference = Class(name="astm::gastm::TypeQualifiedIdentifierReference")
astm_gastm_CatchBlock = Class(name="astm::gastm::CatchBlock")
astm_gastm_TypesCatchBlock = Class(name="astm::gastm::TypesCatchBlock")
astm_gastm_VariableCatchBlock = Class(name="astm::gastm::VariableCatchBlock")
astm_gastm_ThrowStatement = Class(name="astm::gastm::ThrowStatement")
astm_gastm_Expression = Class(name="astm::gastm::Expression", is_abstract=True)
astm_gastm_NameReference = Class(name="astm::gastm::NameReference", is_abstract=True)
astm_gastm_ArrayAccess = Class(name="astm::gastm::ArrayAccess")
astm_gastm_OperatorAssign = Class(name="astm::gastm::OperatorAssign")
BinaryOperator = Class(name="BinaryOperator")
astm_gastm_Literal = Class(name="astm::gastm::Literal")
astm_gastm_CastExpression = Class(name="astm::gastm::CastExpression")
astm_gastm_UnaryExpression = Class(name="astm::gastm::UnaryExpression")
astm_gastm_BinaryExpression = Class(name="astm::gastm::BinaryExpression")
ActualParameter = Class(name="ActualParameter")
astm_gastm_ConditionalExpression = Class(name="astm::gastm::ConditionalExpression")
astm_gastm_RangeExpression = Class(name="astm::gastm::RangeExpression")
astm_gastm_FunctionCallExpression = Class(name="astm::gastm::FunctionCallExpression")
astm_gastm_ActualParameterExpression = Class(name="astm::gastm::ActualParameterExpression")
astm_gastm_NewExpression = Class(name="astm::gastm::NewExpression")
astm_gastm_LabelAccess = Class(name="astm::gastm::LabelAccess")
astm_gastm_AnnotationExpression = Class(name="astm::gastm::AnnotationExpression")
astm_gastm_GlobalScope = Class(name="astm::gastm::GlobalScope")
astm_gastm_PreprocessorElement = Class(name="astm::gastm::PreprocessorElement", is_abstract=True)
astm_gastm_DefinitionObject = Class(name="astm::gastm::DefinitionObject", is_abstract=True)
astm_gastm_ProgramScope = Class(name="astm::gastm::ProgramScope")
astm_gastm_TypeReference = Class(name="astm::gastm::TypeReference", is_abstract=True)
astm_gastm_Statement = Class(name="astm::gastm::Statement", is_abstract=True)
astm_gastm_FunctionScope = Class(name="astm::gastm::FunctionScope")
astm_gastm_NameSpaceType = Class(name="astm::gastm::NameSpaceType")
astm_gastm_LabelType = Class(name="astm::gastm::LabelType")
astm_gastm_AggregateScope = Class(name="astm::gastm::AggregateScope")
astm_gastm_BlockScope = Class(name="astm::gastm::BlockScope")
astm_gastm_IdentifierReference = Class(name="astm::gastm::IdentifierReference")
astm_gastm_PointerType = Class(name="astm::gastm::PointerType")
astm_gastm_FormalParameterDefinition = Class(name="astm::gastm::FormalParameterDefinition")
astm_gastm_ReferenceType = Class(name="astm::gastm::ReferenceType")
astm_gastm_RangeType = Class(name="astm::gastm::RangeType")
astm_gastm_VirtualSpecification = Class(name="astm::gastm::VirtualSpecification", is_abstract=True)
astm_gastm_StructureType = Class(name="astm::gastm::StructureType")
astm_gastm_UnionType = Class(name="astm::gastm::UnionType")
astm_gastm_FormalParameterDeclaration = Class(name="astm::gastm::FormalParameterDeclaration")
astm_gastm_AnnotationType = Class(name="astm::gastm::AnnotationType")
astm_gastm_VariableDefinition = Class(name="astm::gastm::VariableDefinition")
astm_gastm_FunctionMemberAttribute = Class(name="astm::gastm::FunctionMemberAttribute")
astm_gastm_External = Class(name="astm::gastm::External")
StorageSpecification = Class(name="StorageSpecification")
astm_gastm_FunctionPersistent = Class(name="astm::gastm::FunctionPersistent")
astm_gastm_FileLocal = Class(name="astm::gastm::FileLocal")
astm_gastm_PerClassMember = Class(name="astm::gastm::PerClassMember")
astm_gastm_NoDef = Class(name="astm::gastm::NoDef")
astm_gastm_Virtual = Class(name="astm::gastm::Virtual")
astm_gastm_PureVirtual = Class(name="astm::gastm::PureVirtual")
astm_gastm_NonVirtual = Class(name="astm::gastm::NonVirtual")
astm_gastm_ExceptionType = Class(name="astm::gastm::ExceptionType")
astm_gastm_Void = Class(name="astm::gastm::Void")
PrimitiveType = Class(name="PrimitiveType")
astm_gastm_Byte = Class(name="astm::gastm::Byte")
astm_gastm_ShortInteger = Class(name="astm::gastm::ShortInteger")
astm_gastm_Integer = Class(name="astm::gastm::Integer")
astm_gastm_LongInteger = Class(name="astm::gastm::LongInteger")
astm_gastm_Float = Class(name="astm::gastm::Float")
astm_gastm_Double = Class(name="astm::gastm::Double")
astm_gastm_LongDouble = Class(name="astm::gastm::LongDouble")
astm_gastm_Character = Class(name="astm::gastm::Character")
astm_gastm_String = Class(name="astm::gastm::String")
astm_gastm_Boolean = Class(name="astm::gastm::Boolean")
astm_gastm_WideCharacter = Class(name="astm::gastm::WideCharacter")
astm_gastm_CollectionType = Class(name="astm::gastm::CollectionType")
astm_gastm_Not = Class(name="astm::gastm::Not")
astm_gastm_BitNot = Class(name="astm::gastm::BitNot")
astm_gastm_AddressOf = Class(name="astm::gastm::AddressOf")
astm_gastm_Deref = Class(name="astm::gastm::Deref")
astm_gastm_Increment = Class(name="astm::gastm::Increment")
astm_gastm_Decrement = Class(name="astm::gastm::Decrement")
astm_gastm_PostIncrement = Class(name="astm::gastm::PostIncrement")
astm_gastm_PostDecrement = Class(name="astm::gastm::PostDecrement")
astm_gastm_Add = Class(name="astm::gastm::Add")
astm_gastm_ByValueFormalParameterType = Class(name="astm::gastm::ByValueFormalParameterType")
astm_gastm_ByReferenceFormalParameterType = Class(name="astm::gastm::ByReferenceFormalParameterType")
astm_gastm_Public = Class(name="astm::gastm::Public")
AccessKind = Class(name="AccessKind")
astm_gastm_Protected = Class(name="astm::gastm::Protected")
astm_gastm_Private = Class(name="astm::gastm::Private")
astm_gastm_TerminateStatement = Class(name="astm::gastm::TerminateStatement")
astm_gastm_DefaultBlock = Class(name="astm::gastm::DefaultBlock")
astm_gastm_WhileStatement = Class(name="astm::gastm::WhileStatement")
astm_gastm_DoWhileStatement = Class(name="astm::gastm::DoWhileStatement")
astm_gastm_ForCheckBeforeStatement = Class(name="astm::gastm::ForCheckBeforeStatement")
ForStatement = Class(name="ForStatement")
astm_gastm_ForCheckAfterStatement = Class(name="astm::gastm::ForCheckAfterStatement")
astm_gastm_AggregateExpression = Class(name="astm::gastm::AggregateExpression")
astm_gastm_QualifiedOverPointer = Class(name="astm::gastm::QualifiedOverPointer")
QualifiedIdentifierReference = Class(name="QualifiedIdentifierReference")
astm_gastm_QualifiedOverData = Class(name="astm::gastm::QualifiedOverData")
astm_gastm_IntegerLiteral = Class(name="astm::gastm::IntegerLiteral")
Literal = Class(name="Literal")
astm_gastm_StringLiteral = Class(name="astm::gastm::StringLiteral")
astm_gastm_CharLiteral = Class(name="astm::gastm::CharLiteral")
astm_gastm_RealLiteral = Class(name="astm::gastm::RealLiteral")
astm_gastm_BooleanLiteral = Class(name="astm::gastm::BooleanLiteral")
astm_gastm_BitLiteral = Class(name="astm::gastm::BitLiteral")
astm_gastm_UnaryPlus = Class(name="astm::gastm::UnaryPlus")
UnaryOperator = Class(name="UnaryOperator")
astm_gastm_Negate = Class(name="astm::gastm::Negate")
astm_gastm_SpecificGreaterEqual = Class(name="astm::gastm::SpecificGreaterEqual")
astm_gastm_SpecificIn = Class(name="astm::gastm::SpecificIn")
astm_gastm_SpecificLike = Class(name="astm::gastm::SpecificLike")
astm_gastm_SpecificConcatString = Class(name="astm::gastm::SpecificConcatString")
astm_gastm_SpecificSelectStatement = Class(name="astm::gastm::SpecificSelectStatement")
astm_sastm_DelphiUnit = Class(name="astm::sastm::DelphiUnit")
astm_gastm_Subtract = Class(name="astm::gastm::Subtract")
astm_gastm_Multiply = Class(name="astm::gastm::Multiply")
astm_gastm_Divide = Class(name="astm::gastm::Divide")
astm_gastm_Modulus = Class(name="astm::gastm::Modulus")
astm_gastm_Exponent = Class(name="astm::gastm::Exponent")
astm_gastm_And = Class(name="astm::gastm::And")
astm_gastm_Or = Class(name="astm::gastm::Or")
astm_gastm_Equal = Class(name="astm::gastm::Equal")
astm_gastm_NotEqual = Class(name="astm::gastm::NotEqual")
astm_gastm_Greater = Class(name="astm::gastm::Greater")
astm_gastm_NotGreater = Class(name="astm::gastm::NotGreater")
astm_gastm_Less = Class(name="astm::gastm::Less")
astm_gastm_NotLess = Class(name="astm::gastm::NotLess")
astm_gastm_BitAnd = Class(name="astm::gastm::BitAnd")
astm_gastm_BitOr = Class(name="astm::gastm::BitOr")
astm_gastm_BitXor = Class(name="astm::gastm::BitXor")
astm_gastm_BitLeftShift = Class(name="astm::gastm::BitLeftShift")
astm_gastm_BitRightShift = Class(name="astm::gastm::BitRightShift")
astm_gastm_Assign = Class(name="astm::gastm::Assign")
astm_gastm_MissingActualParameter = Class(name="astm::gastm::MissingActualParameter")
astm_gastm_ByValueActualParameterExpression = Class(name="astm::gastm::ByValueActualParameterExpression")
ActualParameterExpression = Class(name="ActualParameterExpression")
astm_gastm_ByReferenceActualParameterExpression = Class(name="astm::gastm::ByReferenceActualParameterExpression")
astm_gastm_SpecificTriggerDefinition = Class(name="astm::gastm::SpecificTriggerDefinition")
astm_gastm_SpecificLessEqual = Class(name="astm::gastm::SpecificLessEqual")
astm_sastm_DelphiWithStatement = Class(name="astm::sastm::DelphiWithStatement")
DelphiInterfaceSection = Class(name="DelphiInterfaceSection")
DelphiImplementationSection = Class(name="DelphiImplementationSection")
astm_sastm_DelphiInterfaceSection = Class(name="astm::sastm::DelphiInterfaceSection")
NamedTypeReference = Class(name="NamedTypeReference")
astm_sastm_DelphiImplementationSection = Class(name="astm::sastm::DelphiImplementationSection")
astm_sastm_DelphiBlockStatement = Class(name="astm::sastm::DelphiBlockStatement")
BlockStatement = Class(name="BlockStatement")
astm_sastm_DelphiFunctionCallExpression = Class(name="astm::sastm::DelphiFunctionCallExpression")
FunctionCallExpression = Class(name="FunctionCallExpression")

# astm_gastm_GASTMObject class attributes and methods

# astm_gastm_GASTMSourceObject class attributes and methods

# astm_gastm_GASTMSemanticObject class attributes and methods

# astm_gastm_OtherSyntaxObject class attributes and methods

# GASTMSyntaxObject class attributes and methods

# astm_gastm_StorageSpecification class attributes and methods

# astm_gastm_DataType class attributes and methods

# Type class attributes and methods

# astm_gastm_AccessKind class attributes and methods

# AnnotationExpression class attributes and methods

# astm_gastm_CompilationUnit class attributes and methods
astm_gastm_CompilationUnit_language: Property = Property(name="language", type=StringType)
astm_gastm_CompilationUnit.attributes={astm_gastm_CompilationUnit_language}

# OtherSyntaxObject class attributes and methods

# astm_gastm_UnaryOperator class attributes and methods

# astm_gastm_BinaryOperator class attributes and methods

# astm_gastm_ActualParameter class attributes and methods

# astm_gastm_SourceFile class attributes and methods
astm_gastm_SourceFile_pathName: Property = Property(name="pathName", type=StringType)
astm_gastm_SourceFile.attributes={astm_gastm_SourceFile_pathName}

# GASTMSourceObject class attributes and methods

# astm_gastm_SourceLocation class attributes and methods
astm_gastm_SourceLocation_startLine: Property = Property(name="startLine", type=IntegerType)
astm_gastm_SourceLocation_startColumn: Property = Property(name="startColumn", type=IntegerType)
astm_gastm_SourceLocation_endLine: Property = Property(name="endLine", type=IntegerType)
astm_gastm_SourceLocation_endColumn: Property = Property(name="endColumn", type=IntegerType)
astm_gastm_SourceLocation.attributes={astm_gastm_SourceLocation_endLine, astm_gastm_SourceLocation_startColumn, astm_gastm_SourceLocation_startLine, astm_gastm_SourceLocation_endColumn}

# SourceFile class attributes and methods

# astm_gastm_Project class attributes and methods

# GASTMSemanticObject class attributes and methods

# CompilationUnit class attributes and methods

# GlobalScope class attributes and methods

# astm_gastm_Scope class attributes and methods

# DefinitionObject class attributes and methods

# Scope class attributes and methods

# astm_gastm_GASTMSyntaxObject class attributes and methods

# GASTMObject class attributes and methods

# SourceLocation class attributes and methods

# PreprocessorElement class attributes and methods

# astm_gastm_FunctionDeclaration class attributes and methods

# Declaration class attributes and methods

# FormalParameterDeclaration class attributes and methods

# FunctionMemberAttributes class attributes and methods

# ProgramScope class attributes and methods

# astm_gastm_Name class attributes and methods
astm_gastm_Name_nameString: Property = Property(name="nameString", type=StringType)
astm_gastm_Name.attributes={astm_gastm_Name_nameString}

# astm_gastm_DeclarationOrDefinition class attributes and methods
astm_gastm_DeclarationOrDefinition_isRegister: Property = Property(name="isRegister", type=BooleanType)
astm_gastm_DeclarationOrDefinition_linkageSpecifier: Property = Property(name="linkageSpecifier", type=StringType)
astm_gastm_DeclarationOrDefinition.attributes={astm_gastm_DeclarationOrDefinition_linkageSpecifier, astm_gastm_DeclarationOrDefinition_isRegister}

# astm_gastm_Definition class attributes and methods

# DeclarationOrDefinition class attributes and methods

# Name class attributes and methods

# TypeReference class attributes and methods

# astm_gastm_Declaration class attributes and methods

# Definition class attributes and methods

# astm_gastm_DataDefinition class attributes and methods
astm_gastm_DataDefinition_isMutable: Property = Property(name="isMutable", type=BooleanType)
astm_gastm_DataDefinition.attributes={astm_gastm_DataDefinition_isMutable}

# Expression class attributes and methods

# astm_gastm_BitFieldDefinition class attributes and methods

# DataDefinition class attributes and methods

# astm_gastm_VariableDeclaration class attributes and methods
astm_gastm_VariableDeclaration_isMutable: Property = Property(name="isMutable", type=BooleanType)
astm_gastm_VariableDeclaration.attributes={astm_gastm_VariableDeclaration_isMutable}

# astm_gastm_FunctionDefinition class attributes and methods

# FormalParameterDefinition class attributes and methods

# Statement class attributes and methods

# FunctionScope class attributes and methods

# astm_gastm_FunctionMemberAttributes class attributes and methods
astm_gastm_FunctionMemberAttributes_isFriend: Property = Property(name="isFriend", type=BooleanType)
astm_gastm_FunctionMemberAttributes_isInline: Property = Property(name="isInline", type=BooleanType)
astm_gastm_FunctionMemberAttributes_isThisConst: Property = Property(name="isThisConst", type=BooleanType)
astm_gastm_FunctionMemberAttributes.attributes={astm_gastm_FunctionMemberAttributes_isThisConst, astm_gastm_FunctionMemberAttributes_isInline, astm_gastm_FunctionMemberAttributes_isFriend}

# VirtualSpecification class attributes and methods

# astm_gastm_EntryDefinition class attributes and methods

# LabelType class attributes and methods

# astm_gastm_IncludeUnit class attributes and methods

# astm_gastm_EnumLiteralDefinition class attributes and methods

# astm_gastm_TypeDefinition class attributes and methods

# astm_gastm_NamedTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# NamedType class attributes and methods

# astm_gastm_AggregateTypeDefinition class attributes and methods

# AggregateType class attributes and methods

# astm_gastm_NameSpaceDefinition class attributes and methods

# NameSpaceType class attributes and methods

# astm_gastm_LabelDefinition class attributes and methods

# AggregateScope class attributes and methods

# astm_gastm_ArrayType class attributes and methods

# ConstructedType class attributes and methods

# Dimension class attributes and methods

# astm_gastm_Dimension class attributes and methods

# astm_gastm_MacroCall class attributes and methods

# MacroDefinition class attributes and methods

# astm_gastm_MacroDefinition class attributes and methods
astm_gastm_MacroDefinition_macroName: Property = Property(name="macroName", type=StringType)
astm_gastm_MacroDefinition_body: Property = Property(name="body", type=StringType)
astm_gastm_MacroDefinition.attributes={astm_gastm_MacroDefinition_body, astm_gastm_MacroDefinition_macroName}

# astm_gastm_Comment class attributes and methods
astm_gastm_Comment_text: Property = Property(name="text", type=StringType)
astm_gastm_Comment.attributes={astm_gastm_Comment_text}

# astm_gastm_Type class attributes and methods
astm_gastm_Type_isConst: Property = Property(name="isConst", type=BooleanType)
astm_gastm_Type_isVolatile: Property = Property(name="isVolatile", type=BooleanType)
astm_gastm_Type.attributes={astm_gastm_Type_isConst, astm_gastm_Type_isVolatile}

# astm_gastm_PrimitiveType class attributes and methods
astm_gastm_PrimitiveType_isSigned: Property = Property(name="isSigned", type=BooleanType)
astm_gastm_PrimitiveType.attributes={astm_gastm_PrimitiveType_isSigned}

# DataType class attributes and methods

# astm_gastm_EnumType class attributes and methods

# EnumLiteralDefinition class attributes and methods

# astm_gastm_ConstructedType class attributes and methods

# astm_gastm_AggregateType class attributes and methods

# astm_gastm_UnnamedTypeReference class attributes and methods

# astm_gastm_NamedTypeReference class attributes and methods

# astm_gastm_FunctionType class attributes and methods

# FormalParameterType class attributes and methods

# astm_gastm_FormalParameterType class attributes and methods

# astm_gastm_NamedType class attributes and methods

# astm_gastm_ClassType class attributes and methods

# DerivesFrom class attributes and methods

# astm_gastm_DerivesFrom class attributes and methods
astm_gastm_DerivesFrom_isVirtual: Property = Property(name="isVirtual", type=BooleanType)
astm_gastm_DerivesFrom.attributes={astm_gastm_DerivesFrom_isVirtual}

# astm_gastm_BreakStatement class attributes and methods

# astm_gastm_DeleteStatement class attributes and methods

# astm_gastm_DeclarationOrDefinitionStatement class attributes and methods

# astm_gastm_ExpressionStatement class attributes and methods

# astm_gastm_JumpStatement class attributes and methods

# LabelAccess class attributes and methods

# astm_gastm_SwitchStatement class attributes and methods

# astm_gastm_ContinueStatement class attributes and methods

# astm_gastm_LabeledStatement class attributes and methods

# LabelDefinition class attributes and methods

# astm_gastm_BlockStatement class attributes and methods

# BlockScope class attributes and methods

# astm_gastm_EmptyStatement class attributes and methods

# astm_gastm_IfStatement class attributes and methods

# astm_gastm_TryStatement class attributes and methods

# CatchBlock class attributes and methods

# SwitchCase class attributes and methods

# astm_gastm_SwitchCase class attributes and methods

# astm_gastm_CaseBlock class attributes and methods

# astm_gastm_ReturnStatement class attributes and methods

# astm_gastm_LoopStatement class attributes and methods

# astm_gastm_ForStatement class attributes and methods

# LoopStatement class attributes and methods

# astm_gastm_QualifiedIdentifierReference class attributes and methods

# NameReference class attributes and methods

# IdentifierReference class attributes and methods

# astm_gastm_TypeQualifiedIdentifierReference class attributes and methods

# astm_gastm_CatchBlock class attributes and methods

# astm_gastm_TypesCatchBlock class attributes and methods

# astm_gastm_VariableCatchBlock class attributes and methods

# astm_gastm_ThrowStatement class attributes and methods

# astm_gastm_Expression class attributes and methods

# astm_gastm_NameReference class attributes and methods

# astm_gastm_ArrayAccess class attributes and methods

# astm_gastm_OperatorAssign class attributes and methods

# BinaryOperator class attributes and methods

# astm_gastm_Literal class attributes and methods
astm_gastm_Literal_value: Property = Property(name="value", type=StringType)
astm_gastm_Literal.attributes={astm_gastm_Literal_value}

# astm_gastm_CastExpression class attributes and methods

# astm_gastm_UnaryExpression class attributes and methods

# astm_gastm_BinaryExpression class attributes and methods

# ActualParameter class attributes and methods

# astm_gastm_ConditionalExpression class attributes and methods

# astm_gastm_RangeExpression class attributes and methods

# astm_gastm_FunctionCallExpression class attributes and methods

# astm_gastm_ActualParameterExpression class attributes and methods

# astm_gastm_NewExpression class attributes and methods

# astm_gastm_LabelAccess class attributes and methods

# astm_gastm_AnnotationExpression class attributes and methods

# astm_gastm_GlobalScope class attributes and methods

# astm_gastm_PreprocessorElement class attributes and methods

# astm_gastm_DefinitionObject class attributes and methods

# astm_gastm_ProgramScope class attributes and methods

# astm_gastm_TypeReference class attributes and methods

# astm_gastm_Statement class attributes and methods

# astm_gastm_FunctionScope class attributes and methods

# astm_gastm_NameSpaceType class attributes and methods

# astm_gastm_LabelType class attributes and methods

# astm_gastm_AggregateScope class attributes and methods

# astm_gastm_BlockScope class attributes and methods

# astm_gastm_IdentifierReference class attributes and methods

# astm_gastm_PointerType class attributes and methods

# astm_gastm_FormalParameterDefinition class attributes and methods

# astm_gastm_ReferenceType class attributes and methods

# astm_gastm_RangeType class attributes and methods

# astm_gastm_VirtualSpecification class attributes and methods

# astm_gastm_StructureType class attributes and methods

# astm_gastm_UnionType class attributes and methods

# astm_gastm_FormalParameterDeclaration class attributes and methods

# astm_gastm_AnnotationType class attributes and methods

# astm_gastm_VariableDefinition class attributes and methods

# astm_gastm_FunctionMemberAttribute class attributes and methods

# astm_gastm_External class attributes and methods

# StorageSpecification class attributes and methods

# astm_gastm_FunctionPersistent class attributes and methods

# astm_gastm_FileLocal class attributes and methods

# astm_gastm_PerClassMember class attributes and methods

# astm_gastm_NoDef class attributes and methods

# astm_gastm_Virtual class attributes and methods

# astm_gastm_PureVirtual class attributes and methods

# astm_gastm_NonVirtual class attributes and methods

# astm_gastm_ExceptionType class attributes and methods

# astm_gastm_Void class attributes and methods

# PrimitiveType class attributes and methods

# astm_gastm_Byte class attributes and methods

# astm_gastm_ShortInteger class attributes and methods

# astm_gastm_Integer class attributes and methods

# astm_gastm_LongInteger class attributes and methods

# astm_gastm_Float class attributes and methods

# astm_gastm_Double class attributes and methods

# astm_gastm_LongDouble class attributes and methods

# astm_gastm_Character class attributes and methods

# astm_gastm_String class attributes and methods

# astm_gastm_Boolean class attributes and methods

# astm_gastm_WideCharacter class attributes and methods

# astm_gastm_CollectionType class attributes and methods

# astm_gastm_Not class attributes and methods

# astm_gastm_BitNot class attributes and methods

# astm_gastm_AddressOf class attributes and methods

# astm_gastm_Deref class attributes and methods

# astm_gastm_Increment class attributes and methods

# astm_gastm_Decrement class attributes and methods

# astm_gastm_PostIncrement class attributes and methods

# astm_gastm_PostDecrement class attributes and methods

# astm_gastm_Add class attributes and methods

# astm_gastm_ByValueFormalParameterType class attributes and methods

# astm_gastm_ByReferenceFormalParameterType class attributes and methods

# astm_gastm_Public class attributes and methods

# AccessKind class attributes and methods

# astm_gastm_Protected class attributes and methods

# astm_gastm_Private class attributes and methods

# astm_gastm_TerminateStatement class attributes and methods

# astm_gastm_DefaultBlock class attributes and methods

# astm_gastm_WhileStatement class attributes and methods

# astm_gastm_DoWhileStatement class attributes and methods

# astm_gastm_ForCheckBeforeStatement class attributes and methods

# ForStatement class attributes and methods

# astm_gastm_ForCheckAfterStatement class attributes and methods

# astm_gastm_AggregateExpression class attributes and methods

# astm_gastm_QualifiedOverPointer class attributes and methods

# QualifiedIdentifierReference class attributes and methods

# astm_gastm_QualifiedOverData class attributes and methods

# astm_gastm_IntegerLiteral class attributes and methods

# Literal class attributes and methods

# astm_gastm_StringLiteral class attributes and methods

# astm_gastm_CharLiteral class attributes and methods

# astm_gastm_RealLiteral class attributes and methods

# astm_gastm_BooleanLiteral class attributes and methods

# astm_gastm_BitLiteral class attributes and methods

# astm_gastm_UnaryPlus class attributes and methods

# UnaryOperator class attributes and methods

# astm_gastm_Negate class attributes and methods

# astm_gastm_SpecificGreaterEqual class attributes and methods

# astm_gastm_SpecificIn class attributes and methods

# astm_gastm_SpecificLike class attributes and methods

# astm_gastm_SpecificConcatString class attributes and methods

# astm_gastm_SpecificSelectStatement class attributes and methods

# astm_sastm_DelphiUnit class attributes and methods

# astm_gastm_Subtract class attributes and methods

# astm_gastm_Multiply class attributes and methods

# astm_gastm_Divide class attributes and methods

# astm_gastm_Modulus class attributes and methods

# astm_gastm_Exponent class attributes and methods

# astm_gastm_And class attributes and methods

# astm_gastm_Or class attributes and methods

# astm_gastm_Equal class attributes and methods

# astm_gastm_NotEqual class attributes and methods

# astm_gastm_Greater class attributes and methods

# astm_gastm_NotGreater class attributes and methods

# astm_gastm_Less class attributes and methods

# astm_gastm_NotLess class attributes and methods

# astm_gastm_BitAnd class attributes and methods

# astm_gastm_BitOr class attributes and methods

# astm_gastm_BitXor class attributes and methods

# astm_gastm_BitLeftShift class attributes and methods

# astm_gastm_BitRightShift class attributes and methods

# astm_gastm_Assign class attributes and methods

# astm_gastm_MissingActualParameter class attributes and methods

# astm_gastm_ByValueActualParameterExpression class attributes and methods

# ActualParameterExpression class attributes and methods

# astm_gastm_ByReferenceActualParameterExpression class attributes and methods

# astm_gastm_SpecificTriggerDefinition class attributes and methods

# astm_gastm_SpecificLessEqual class attributes and methods

# astm_sastm_DelphiWithStatement class attributes and methods

# DelphiInterfaceSection class attributes and methods

# DelphiImplementationSection class attributes and methods

# astm_sastm_DelphiInterfaceSection class attributes and methods

# NamedTypeReference class attributes and methods

# astm_sastm_DelphiImplementationSection class attributes and methods

# astm_sastm_DelphiBlockStatement class attributes and methods

# BlockStatement class attributes and methods

# astm_sastm_DelphiFunctionCallExpression class attributes and methods

# FunctionCallExpression class attributes and methods

# Relationships
preProcessorElements8: BinaryAssociation = BinaryAssociation(
    name="preProcessorElements8",
    ends={
        Property(name="PreprocessorElement", type=astm_gastm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_GASTMSyntaxObject9", type=PreprocessorElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations10: BinaryAssociation = BinaryAssociation(
    name="annotations10",
    ends={
        Property(name="AnnotationExpression", type=astm_gastm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_GASTMSyntaxObject11", type=AnnotationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments12: BinaryAssociation = BinaryAssociation(
    name="fragments12",
    ends={
        Property(name="DefinitionObject13", type=astm_gastm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CompilationUnit", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inSourceFile0: BinaryAssociation = BinaryAssociation(
    name="inSourceFile0",
    ends={
        Property(name="SourceFile", type=astm_gastm_SourceLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_SourceLocation", type=SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
files1: BinaryAssociation = BinaryAssociation(
    name="files1",
    ends={
        Property(name="CompilationUnit", type=astm_gastm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Project", type=CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outerScope2: BinaryAssociation = BinaryAssociation(
    name="outerScope2",
    ends={
        Property(name="GlobalScope", type=astm_gastm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Project3", type=GlobalScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionObject4: BinaryAssociation = BinaryAssociation(
    name="definitionObject4",
    ends={
        Property(name="DefinitionObject", type=astm_gastm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Scope", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childScope5: BinaryAssociation = BinaryAssociation(
    name="childScope5",
    ends={
        Property(name="Scope", type=astm_gastm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Scope6", type=Scope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locationInfo7: BinaryAssociation = BinaryAssociation(
    name="locationInfo7",
    ends={
        Property(name="SourceLocation", type=astm_gastm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_GASTMSyntaxObject", type=SourceLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters30: BinaryAssociation = BinaryAssociation(
    name="formalParameters30",
    ends={
        Property(name="FormalParameterDeclaration", type=astm_gastm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDeclaration", type=FormalParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes31: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes31",
    ends={
        Property(name="FunctionMemberAttributes", type=astm_gastm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDeclaration32", type=FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType33: BinaryAssociation = BinaryAssociation(
    name="returnType33",
    ends={
        Property(name="TypeReference35", type=astm_gastm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDeclaration34", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opensScope14: BinaryAssociation = BinaryAssociation(
    name="opensScope14",
    ends={
        Property(name="ProgramScope", type=astm_gastm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CompilationUnit15", type=ProgramScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
storageSpecifiers16: BinaryAssociation = BinaryAssociation(
    name="storageSpecifiers16",
    ends={
        Property(name="OtherSyntaxObject", type=astm_gastm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DeclarationOrDefinition", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessKind17: BinaryAssociation = BinaryAssociation(
    name="accessKind17",
    ends={
        Property(name="OtherSyntaxObject19", type=astm_gastm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DeclarationOrDefinition18", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierName20: BinaryAssociation = BinaryAssociation(
    name="identifierName20",
    ends={
        Property(name="Name", type=astm_gastm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Definition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType21: BinaryAssociation = BinaryAssociation(
    name="definitionType21",
    ends={
        Property(name="TypeReference", type=astm_gastm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Definition22", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defRef23: BinaryAssociation = BinaryAssociation(
    name="defRef23",
    ends={
        Property(name="Definition", type=astm_gastm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Declaration", type=Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierName24: BinaryAssociation = BinaryAssociation(
    name="identifierName24",
    ends={
        Property(name="Name26", type=astm_gastm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Declaration25", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarationType27: BinaryAssociation = BinaryAssociation(
    name="declarationType27",
    ends={
        Property(name="TypeReference29", type=astm_gastm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Declaration28", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue53: BinaryAssociation = BinaryAssociation(
    name="initialValue53",
    ends={
        Property(name="Expression", type=astm_gastm_DataDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DataDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bitFieldSize54: BinaryAssociation = BinaryAssociation(
    name="bitFieldSize54",
    ends={
        Property(name="Expression55", type=astm_gastm_BitFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BitFieldDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType36: BinaryAssociation = BinaryAssociation(
    name="returnType36",
    ends={
        Property(name="TypeReference37", type=astm_gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDefinition", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters38: BinaryAssociation = BinaryAssociation(
    name="formalParameters38",
    ends={
        Property(name="FormalParameterDefinition", type=astm_gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDefinition39", type=FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body40: BinaryAssociation = BinaryAssociation(
    name="body40",
    ends={
        Property(name="Statement", type=astm_gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDefinition41", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes42: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes42",
    ends={
        Property(name="FunctionMemberAttributes44", type=astm_gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDefinition43", type=FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opensScope45: BinaryAssociation = BinaryAssociation(
    name="opensScope45",
    ends={
        Property(name="FunctionScope", type=astm_gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDefinition46", type=FunctionScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
virtualSpecifier47: BinaryAssociation = BinaryAssociation(
    name="virtualSpecifier47",
    ends={
        Property(name="VirtualSpecification", type=astm_gastm_FunctionMemberAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionMemberAttributes", type=VirtualSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters48: BinaryAssociation = BinaryAssociation(
    name="formalParameters48",
    ends={
        Property(name="FormalParameterDefinition49", type=astm_gastm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_EntryDefinition", type=FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body50: BinaryAssociation = BinaryAssociation(
    name="body50",
    ends={
        Property(name="Statement52", type=astm_gastm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_EntryDefinition51", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelName69: BinaryAssociation = BinaryAssociation(
    name="labelName69",
    ends={
        Property(name="Name70", type=astm_gastm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabelDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelType71: BinaryAssociation = BinaryAssociation(
    name="labelType71",
    ends={
        Property(name="LabelType", type=astm_gastm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabelDefinition72", type=LabelType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file73: BinaryAssociation = BinaryAssociation(
    name="file73",
    ends={
        Property(name="SourceFile74", type=astm_gastm_IncludeUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_IncludeUnit", type=SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value56: BinaryAssociation = BinaryAssociation(
    name="value56",
    ends={
        Property(name="Expression57", type=astm_gastm_EnumLiteralDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_EnumLiteralDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name58: BinaryAssociation = BinaryAssociation(
    name="name58",
    ends={
        Property(name="Name59", type=astm_gastm_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TypeDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType60: BinaryAssociation = BinaryAssociation(
    name="definitionType60",
    ends={
        Property(name="NamedType", type=astm_gastm_NamedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NamedTypeDefinition", type=NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType61: BinaryAssociation = BinaryAssociation(
    name="aggregateType61",
    ends={
        Property(name="AggregateType", type=astm_gastm_AggregateTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_AggregateTypeDefinition", type=AggregateType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameSpace62: BinaryAssociation = BinaryAssociation(
    name="nameSpace62",
    ends={
        Property(name="Name63", type=astm_gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NameSpaceDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body64: BinaryAssociation = BinaryAssociation(
    name="body64",
    ends={
        Property(name="DefinitionObject66", type=astm_gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NameSpaceDefinition65", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameSpaceType67: BinaryAssociation = BinaryAssociation(
    name="nameSpaceType67",
    ends={
        Property(name="NameSpaceType", type=astm_gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NameSpaceDefinition68", type=NameSpaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opensScope81: BinaryAssociation = BinaryAssociation(
    name="opensScope81",
    ends={
        Property(name="AggregateScope", type=astm_gastm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_AggregateType82", type=AggregateScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ranks83: BinaryAssociation = BinaryAssociation(
    name="ranks83",
    ends={
        Property(name="Dimension", type=astm_gastm_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ArrayType", type=Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refersTo75: BinaryAssociation = BinaryAssociation(
    name="refersTo75",
    ends={
        Property(name="MacroDefinition", type=astm_gastm_MacroCall, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_MacroCall", type=MacroDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumLiterals76: BinaryAssociation = BinaryAssociation(
    name="enumLiterals76",
    ends={
        Property(name="EnumLiteralDefinition", type=astm_gastm_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_EnumType", type=EnumLiteralDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType77: BinaryAssociation = BinaryAssociation(
    name="baseType77",
    ends={
        Property(name="TypeReference78", type=astm_gastm_ConstructedType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ConstructedType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members79: BinaryAssociation = BinaryAssociation(
    name="members79",
    ends={
        Property(name="DefinitionObject80", type=astm_gastm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_AggregateType", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
className99: BinaryAssociation = BinaryAssociation(
    name="className99",
    ends={
        Property(name="NamedType101", type=astm_gastm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DerivesFrom100", type=NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type102: BinaryAssociation = BinaryAssociation(
    name="type102",
    ends={
        Property(name="Type103", type=astm_gastm_UnnamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_UnnamedTypeReference", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowBound84: BinaryAssociation = BinaryAssociation(
    name="lowBound84",
    ends={
        Property(name="Expression85", type=astm_gastm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Dimension", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
highBound86: BinaryAssociation = BinaryAssociation(
    name="highBound86",
    ends={
        Property(name="Expression88", type=astm_gastm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Dimension87", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType89: BinaryAssociation = BinaryAssociation(
    name="returnType89",
    ends={
        Property(name="TypeReference90", type=astm_gastm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterTypes91: BinaryAssociation = BinaryAssociation(
    name="parameterTypes91",
    ends={
        Property(name="FormalParameterType", type=astm_gastm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionType92", type=FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type93: BinaryAssociation = BinaryAssociation(
    name="type93",
    ends={
        Property(name="TypeReference94", type=astm_gastm_FormalParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FormalParameterType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body95: BinaryAssociation = BinaryAssociation(
    name="body95",
    ends={
        Property(name="Type", type=astm_gastm_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NamedType", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivesFrom96: BinaryAssociation = BinaryAssociation(
    name="derivesFrom96",
    ends={
        Property(name="DerivesFrom", type=astm_gastm_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ClassType", type=DerivesFrom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessKind97: BinaryAssociation = BinaryAssociation(
    name="accessKind97",
    ends={
        Property(name="OtherSyntaxObject98", type=astm_gastm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DerivesFrom", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name104: BinaryAssociation = BinaryAssociation(
    name="name104",
    ends={
        Property(name="Name105", type=astm_gastm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NamedTypeReference", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type106: BinaryAssociation = BinaryAssociation(
    name="type106",
    ends={
        Property(name="TypeDefinition", type=astm_gastm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NamedTypeReference107", type=TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
operand108: BinaryAssociation = BinaryAssociation(
    name="operand108",
    ends={
        Property(name="Expression109", type=astm_gastm_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DeleteStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declOrDefn110: BinaryAssociation = BinaryAssociation(
    name="declOrDefn110",
    ends={
        Property(name="DefinitionObject111", type=astm_gastm_DeclarationOrDefinitionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DeclarationOrDefinitionStatement", type=DefinitionObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression112: BinaryAssociation = BinaryAssociation(
    name="expression112",
    ends={
        Property(name="Expression113", type=astm_gastm_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ExpressionStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target114: BinaryAssociation = BinaryAssociation(
    name="target114",
    ends={
        Property(name="Expression115", type=astm_gastm_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_JumpStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBody129: BinaryAssociation = BinaryAssociation(
    name="thenBody129",
    ends={
        Property(name="Statement131", type=astm_gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_IfStatement130", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBody132: BinaryAssociation = BinaryAssociation(
    name="elseBody132",
    ends={
        Property(name="Statement134", type=astm_gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_IfStatement133", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target116: BinaryAssociation = BinaryAssociation(
    name="target116",
    ends={
        Property(name="LabelAccess", type=astm_gastm_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BreakStatement", type=LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchExpression135: BinaryAssociation = BinaryAssociation(
    name="switchExpression135",
    ends={
        Property(name="Expression136", type=astm_gastm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_SwitchStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target117: BinaryAssociation = BinaryAssociation(
    name="target117",
    ends={
        Property(name="LabelAccess118", type=astm_gastm_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ContinueStatement", type=LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label119: BinaryAssociation = BinaryAssociation(
    name="label119",
    ends={
        Property(name="LabelDefinition", type=astm_gastm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabeledStatement", type=LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement120: BinaryAssociation = BinaryAssociation(
    name="statement120",
    ends={
        Property(name="Statement122", type=astm_gastm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabeledStatement121", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subStatements123: BinaryAssociation = BinaryAssociation(
    name="subStatements123",
    ends={
        Property(name="Statement124", type=astm_gastm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BlockStatement", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope125: BinaryAssociation = BinaryAssociation(
    name="opensScope125",
    ends={
        Property(name="BlockScope", type=astm_gastm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BlockStatement126", type=BlockScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition127: BinaryAssociation = BinaryAssociation(
    name="condition127",
    ends={
        Property(name="Expression128", type=astm_gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_IfStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guardedStatement155: BinaryAssociation = BinaryAssociation(
    name="guardedStatement155",
    ends={
        Property(name="Statement156", type=astm_gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TryStatement", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchBlocks157: BinaryAssociation = BinaryAssociation(
    name="catchBlocks157",
    ends={
        Property(name="CatchBlock", type=astm_gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TryStatement158", type=CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalStatement159: BinaryAssociation = BinaryAssociation(
    name="finalStatement159",
    ends={
        Property(name="Statement161", type=astm_gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TryStatement160", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases137: BinaryAssociation = BinaryAssociation(
    name="cases137",
    ends={
        Property(name="SwitchCase", type=astm_gastm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_SwitchStatement138", type=SwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body139: BinaryAssociation = BinaryAssociation(
    name="body139",
    ends={
        Property(name="Statement140", type=astm_gastm_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_SwitchCase", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caseExpressions141: BinaryAssociation = BinaryAssociation(
    name="caseExpressions141",
    ends={
        Property(name="Expression142", type=astm_gastm_CaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CaseBlock", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue143: BinaryAssociation = BinaryAssociation(
    name="returnValue143",
    ends={
        Property(name="Expression144", type=astm_gastm_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition145: BinaryAssociation = BinaryAssociation(
    name="condition145",
    ends={
        Property(name="Expression146", type=astm_gastm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LoopStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body147: BinaryAssociation = BinaryAssociation(
    name="body147",
    ends={
        Property(name="Statement149", type=astm_gastm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LoopStatement148", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initBody150: BinaryAssociation = BinaryAssociation(
    name="initBody150",
    ends={
        Property(name="Expression151", type=astm_gastm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ForStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationBody152: BinaryAssociation = BinaryAssociation(
    name="iterationBody152",
    ends={
        Property(name="Expression154", type=astm_gastm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ForStatement153", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifiers181: BinaryAssociation = BinaryAssociation(
    name="qualifiers181",
    ends={
        Property(name="Expression182", type=astm_gastm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_QualifiedIdentifierReference", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member183: BinaryAssociation = BinaryAssociation(
    name="member183",
    ends={
        Property(name="IdentifierReference", type=astm_gastm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_QualifiedIdentifierReference184", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType185: BinaryAssociation = BinaryAssociation(
    name="aggregateType185",
    ends={
        Property(name="TypeReference186", type=astm_gastm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TypeQualifiedIdentifierReference", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body162: BinaryAssociation = BinaryAssociation(
    name="body162",
    ends={
        Property(name="Statement163", type=astm_gastm_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CatchBlock", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions164: BinaryAssociation = BinaryAssociation(
    name="exceptions164",
    ends={
        Property(name="Type165", type=astm_gastm_TypesCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TypesCatchBlock", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionVariable166: BinaryAssociation = BinaryAssociation(
    name="exceptionVariable166",
    ends={
        Property(name="DataDefinition", type=astm_gastm_VariableCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_VariableCatchBlock", type=DataDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception167: BinaryAssociation = BinaryAssociation(
    name="exception167",
    ends={
        Property(name="Expression168", type=astm_gastm_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ThrowStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionType169: BinaryAssociation = BinaryAssociation(
    name="expressionType169",
    ends={
        Property(name="TypeReference170", type=astm_gastm_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Expression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name171: BinaryAssociation = BinaryAssociation(
    name="name171",
    ends={
        Property(name="Name172", type=astm_gastm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NameReference", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo173: BinaryAssociation = BinaryAssociation(
    name="refersTo173",
    ends={
        Property(name="DefinitionObject175", type=astm_gastm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NameReference174", type=DefinitionObject, multiplicity=Multiplicity(0, 1))
    }
)
arrayName176: BinaryAssociation = BinaryAssociation(
    name="arrayName176",
    ends={
        Property(name="Expression177", type=astm_gastm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ArrayAccess", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subscripts178: BinaryAssociation = BinaryAssociation(
    name="subscripts178",
    ends={
        Property(name="Expression180", type=astm_gastm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ArrayAccess179", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightOperand205: BinaryAssociation = BinaryAssociation(
    name="rightOperand205",
    ends={
        Property(name="Expression207", type=astm_gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BinaryExpression206", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator208: BinaryAssociation = BinaryAssociation(
    name="operator208",
    ends={
        Property(name="OtherSyntaxObject209", type=astm_gastm_OperatorAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_OperatorAssign", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member187: BinaryAssociation = BinaryAssociation(
    name="member187",
    ends={
        Property(name="IdentifierReference189", type=astm_gastm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TypeQualifiedIdentifierReference188", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
castType190: BinaryAssociation = BinaryAssociation(
    name="castType190",
    ends={
        Property(name="TypeReference191", type=astm_gastm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CastExpression", type=TypeReference, multiplicity=Multiplicity(0, 1))
    }
)
expression192: BinaryAssociation = BinaryAssociation(
    name="expression192",
    ends={
        Property(name="Expression194", type=astm_gastm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CastExpression193", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator195: BinaryAssociation = BinaryAssociation(
    name="operator195",
    ends={
        Property(name="OtherSyntaxObject196", type=astm_gastm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_UnaryExpression", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand197: BinaryAssociation = BinaryAssociation(
    name="operand197",
    ends={
        Property(name="Expression199", type=astm_gastm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_UnaryExpression198", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator200: BinaryAssociation = BinaryAssociation(
    name="operator200",
    ends={
        Property(name="OtherSyntaxObject201", type=astm_gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BinaryExpression", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand202: BinaryAssociation = BinaryAssociation(
    name="leftOperand202",
    ends={
        Property(name="Expression204", type=astm_gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BinaryExpression203", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
calledFunction223: BinaryAssociation = BinaryAssociation(
    name="calledFunction223",
    ends={
        Property(name="Expression224", type=astm_gastm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionCallExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams225: BinaryAssociation = BinaryAssociation(
    name="actualParams225",
    ends={
        Property(name="ActualParameter", type=astm_gastm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionCallExpression226", type=ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition210: BinaryAssociation = BinaryAssociation(
    name="condition210",
    ends={
        Property(name="Expression211", type=astm_gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ConditionalExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onTrueOperand212: BinaryAssociation = BinaryAssociation(
    name="onTrueOperand212",
    ends={
        Property(name="Expression214", type=astm_gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ConditionalExpression213", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onFalseOperand215: BinaryAssociation = BinaryAssociation(
    name="onFalseOperand215",
    ends={
        Property(name="Expression217", type=astm_gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ConditionalExpression216", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromExpression218: BinaryAssociation = BinaryAssociation(
    name="fromExpression218",
    ends={
        Property(name="Expression219", type=astm_gastm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_RangeExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toExpression220: BinaryAssociation = BinaryAssociation(
    name="toExpression220",
    ends={
        Property(name="Expression222", type=astm_gastm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_RangeExpression221", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationType239: BinaryAssociation = BinaryAssociation(
    name="annotationType239",
    ends={
        Property(name="TypeReference240", type=astm_gastm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_AnnotationExpression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberValues241: BinaryAssociation = BinaryAssociation(
    name="memberValues241",
    ends={
        Property(name="Expression243", type=astm_gastm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_AnnotationExpression242", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value227: BinaryAssociation = BinaryAssociation(
    name="value227",
    ends={
        Property(name="Expression228", type=astm_gastm_ActualParameterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ActualParameterExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newType229: BinaryAssociation = BinaryAssociation(
    name="newType229",
    ends={
        Property(name="TypeReference230", type=astm_gastm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NewExpression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams231: BinaryAssociation = BinaryAssociation(
    name="actualParams231",
    ends={
        Property(name="OtherSyntaxObject233", type=astm_gastm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NewExpression232", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name234: BinaryAssociation = BinaryAssociation(
    name="name234",
    ends={
        Property(name="Name235", type=astm_gastm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabelAccess", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition236: BinaryAssociation = BinaryAssociation(
    name="definition236",
    ends={
        Property(name="LabelDefinition238", type=astm_gastm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabelAccess237", type=LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body244: BinaryAssociation = BinaryAssociation(
    name="body244",
    ends={
        Property(name="Statement245", type=astm_gastm_SpecificTriggerDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_SpecificTriggerDefinition", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
withs265: BinaryAssociation = BinaryAssociation(
    name="withs265",
    ends={
        Property(name="DefinitionObject266", type=astm_sastm_DelphiWithStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_DelphiWithStatement", type=DefinitionObject, multiplicity=Multiplicity(0, 9999))
    }
)
name246: BinaryAssociation = BinaryAssociation(
    name="name246",
    ends={
        Property(name="Name247", type=astm_sastm_DelphiUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_DelphiUnit", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interface248: BinaryAssociation = BinaryAssociation(
    name="interface248",
    ends={
        Property(name="DelphiInterfaceSection", type=astm_sastm_DelphiUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_DelphiUnit249", type=DelphiInterfaceSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementation250: BinaryAssociation = BinaryAssociation(
    name="implementation250",
    ends={
        Property(name="DelphiImplementationSection", type=astm_sastm_DelphiUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_DelphiUnit251", type=DelphiImplementationSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uses252: BinaryAssociation = BinaryAssociation(
    name="uses252",
    ends={
        Property(name="NamedTypeReference", type=astm_sastm_DelphiInterfaceSection, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_DelphiInterfaceSection", type=NamedTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uses253: BinaryAssociation = BinaryAssociation(
    name="uses253",
    ends={
        Property(name="NamedTypeReference254", type=astm_sastm_DelphiImplementationSection, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_DelphiImplementationSection", type=NamedTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exports255: BinaryAssociation = BinaryAssociation(
    name="exports255",
    ends={
        Property(name="NamedTypeReference257", type=astm_sastm_DelphiImplementationSection, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_DelphiImplementationSection256", type=NamedTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exports258: BinaryAssociation = BinaryAssociation(
    name="exports258",
    ends={
        Property(name="NamedTypeReference259", type=astm_sastm_DelphiBlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_DelphiBlockStatement", type=NamedTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations260: BinaryAssociation = BinaryAssociation(
    name="declarations260",
    ends={
        Property(name="DefinitionObject262", type=astm_sastm_DelphiBlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_DelphiBlockStatement261", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applyTo263: BinaryAssociation = BinaryAssociation(
    name="applyTo263",
    ends={
        Property(name="DefinitionObject264", type=astm_sastm_DelphiFunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_DelphiFunctionCallExpression", type=DefinitionObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_astm_gastm_OtherSyntaxObject_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_gastm_OtherSyntaxObject)
gen_astm_gastm_DataType_Type = Generalization(general=Type, specific=astm_gastm_DataType)
gen_astm_gastm_CompilationUnit_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_CompilationUnit)
gen_astm_gastm_SourceFile_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=astm_gastm_SourceFile)
gen_astm_gastm_SourceLocation_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=astm_gastm_SourceLocation)
gen_astm_gastm_Project_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=astm_gastm_Project)
gen_astm_gastm_Scope_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=astm_gastm_Scope)
gen_astm_gastm_GASTMSyntaxObject_GASTMObject = Generalization(general=GASTMObject, specific=astm_gastm_GASTMSyntaxObject)
gen_astm_gastm_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=astm_gastm_FunctionDeclaration)
gen_astm_gastm_Name_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_Name)
gen_astm_gastm_DeclarationOrDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_gastm_DeclarationOrDefinition)
gen_astm_gastm_Definition_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=astm_gastm_Definition)
gen_astm_gastm_Declaration_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=astm_gastm_Declaration)
gen_astm_gastm_DataDefinition_Definition = Generalization(general=Definition, specific=astm_gastm_DataDefinition)
gen_astm_gastm_BitFieldDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_gastm_BitFieldDefinition)
gen_astm_gastm_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=astm_gastm_VariableDeclaration)
gen_astm_gastm_FunctionDefinition_Definition = Generalization(general=Definition, specific=astm_gastm_FunctionDefinition)
gen_astm_gastm_EntryDefinition_Definition = Generalization(general=Definition, specific=astm_gastm_EntryDefinition)
gen_astm_gastm_IncludeUnit_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_gastm_IncludeUnit)
gen_astm_gastm_EnumLiteralDefinition_Definition = Generalization(general=Definition, specific=astm_gastm_EnumLiteralDefinition)
gen_astm_gastm_TypeDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_gastm_TypeDefinition)
gen_astm_gastm_NamedTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=astm_gastm_NamedTypeDefinition)
gen_astm_gastm_AggregateTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=astm_gastm_AggregateTypeDefinition)
gen_astm_gastm_NameSpaceDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_gastm_NameSpaceDefinition)
gen_astm_gastm_LabelDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_gastm_LabelDefinition)
gen_astm_gastm_ArrayType_ConstructedType = Generalization(general=ConstructedType, specific=astm_gastm_ArrayType)
gen_astm_gastm_Dimension_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_Dimension)
gen_astm_gastm_MacroCall_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_gastm_MacroCall)
gen_astm_gastm_MacroDefinition_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_gastm_MacroDefinition)
gen_astm_gastm_Comment_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_gastm_Comment)
gen_astm_gastm_Type_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_gastm_Type)
gen_astm_gastm_PrimitiveType_DataType = Generalization(general=DataType, specific=astm_gastm_PrimitiveType)
gen_astm_gastm_EnumType_DataType = Generalization(general=DataType, specific=astm_gastm_EnumType)
gen_astm_gastm_ConstructedType_DataType = Generalization(general=DataType, specific=astm_gastm_ConstructedType)
gen_astm_gastm_AggregateType_DataType = Generalization(general=DataType, specific=astm_gastm_AggregateType)
gen_astm_gastm_UnnamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=astm_gastm_UnnamedTypeReference)
gen_astm_gastm_NamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=astm_gastm_NamedTypeReference)
gen_astm_gastm_FunctionType_Type = Generalization(general=Type, specific=astm_gastm_FunctionType)
gen_astm_gastm_FormalParameterType_DataType = Generalization(general=DataType, specific=astm_gastm_FormalParameterType)
gen_astm_gastm_NamedType_DataType = Generalization(general=DataType, specific=astm_gastm_NamedType)
gen_astm_gastm_ClassType_AggregateType = Generalization(general=AggregateType, specific=astm_gastm_ClassType)
gen_astm_gastm_DerivesFrom_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_DerivesFrom)
gen_astm_gastm_BreakStatement_Statement = Generalization(general=Statement, specific=astm_gastm_BreakStatement)
gen_astm_gastm_DeleteStatement_Statement = Generalization(general=Statement, specific=astm_gastm_DeleteStatement)
gen_astm_gastm_DeclarationOrDefinitionStatement_Statement = Generalization(general=Statement, specific=astm_gastm_DeclarationOrDefinitionStatement)
gen_astm_gastm_ExpressionStatement_Statement = Generalization(general=Statement, specific=astm_gastm_ExpressionStatement)
gen_astm_gastm_JumpStatement_Statement = Generalization(general=Statement, specific=astm_gastm_JumpStatement)
gen_astm_gastm_SwitchStatement_Statement = Generalization(general=Statement, specific=astm_gastm_SwitchStatement)
gen_astm_gastm_ContinueStatement_Statement = Generalization(general=Statement, specific=astm_gastm_ContinueStatement)
gen_astm_gastm_LabeledStatement_Statement = Generalization(general=Statement, specific=astm_gastm_LabeledStatement)
gen_astm_gastm_BlockStatement_Statement = Generalization(general=Statement, specific=astm_gastm_BlockStatement)
gen_astm_gastm_EmptyStatement_Statement = Generalization(general=Statement, specific=astm_gastm_EmptyStatement)
gen_astm_gastm_IfStatement_Statement = Generalization(general=Statement, specific=astm_gastm_IfStatement)
gen_astm_gastm_TryStatement_Statement = Generalization(general=Statement, specific=astm_gastm_TryStatement)
gen_astm_gastm_SwitchCase_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_SwitchCase)
gen_astm_gastm_CaseBlock_SwitchCase = Generalization(general=SwitchCase, specific=astm_gastm_CaseBlock)
gen_astm_gastm_ReturnStatement_Statement = Generalization(general=Statement, specific=astm_gastm_ReturnStatement)
gen_astm_gastm_LoopStatement_Statement = Generalization(general=Statement, specific=astm_gastm_LoopStatement)
gen_astm_gastm_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_gastm_ForStatement)
gen_astm_gastm_QualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_gastm_QualifiedIdentifierReference)
gen_astm_gastm_TypeQualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_gastm_TypeQualifiedIdentifierReference)
gen_astm_gastm_CatchBlock_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_CatchBlock)
gen_astm_gastm_TypesCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=astm_gastm_TypesCatchBlock)
gen_astm_gastm_VariableCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=astm_gastm_VariableCatchBlock)
gen_astm_gastm_ThrowStatement_Statement = Generalization(general=Statement, specific=astm_gastm_ThrowStatement)
gen_astm_gastm_Expression_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_gastm_Expression)
gen_astm_gastm_NameReference_Expression = Generalization(general=Expression, specific=astm_gastm_NameReference)
gen_astm_gastm_ArrayAccess_Expression = Generalization(general=Expression, specific=astm_gastm_ArrayAccess)
gen_astm_gastm_OperatorAssign_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_OperatorAssign)
gen_astm_gastm_Literal_Expression = Generalization(general=Expression, specific=astm_gastm_Literal)
gen_astm_gastm_CastExpression_Expression = Generalization(general=Expression, specific=astm_gastm_CastExpression)
gen_astm_gastm_UnaryExpression_Expression = Generalization(general=Expression, specific=astm_gastm_UnaryExpression)
gen_astm_gastm_BinaryExpression_Expression = Generalization(general=Expression, specific=astm_gastm_BinaryExpression)
gen_astm_gastm_ConditionalExpression_Expression = Generalization(general=Expression, specific=astm_gastm_ConditionalExpression)
gen_astm_gastm_RangeExpression_Expression = Generalization(general=Expression, specific=astm_gastm_RangeExpression)
gen_astm_gastm_FunctionCallExpression_Expression = Generalization(general=Expression, specific=astm_gastm_FunctionCallExpression)
gen_astm_gastm_ActualParameterExpression_ActualParameter = Generalization(general=ActualParameter, specific=astm_gastm_ActualParameterExpression)
gen_astm_gastm_NewExpression_Expression = Generalization(general=Expression, specific=astm_gastm_NewExpression)
gen_astm_gastm_LabelAccess_Expression = Generalization(general=Expression, specific=astm_gastm_LabelAccess)
gen_astm_gastm_AnnotationExpression_Expression = Generalization(general=Expression, specific=astm_gastm_AnnotationExpression)
gen_astm_gastm_GlobalScope_Scope = Generalization(general=Scope, specific=astm_gastm_GlobalScope)
gen_astm_gastm_PreprocessorElement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_gastm_PreprocessorElement)
gen_astm_gastm_DefinitionObject_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_gastm_DefinitionObject)
gen_astm_gastm_ProgramScope_Scope = Generalization(general=Scope, specific=astm_gastm_ProgramScope)
gen_astm_gastm_TypeReference_Type = Generalization(general=Type, specific=astm_gastm_TypeReference)
gen_astm_gastm_Statement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_gastm_Statement)
gen_astm_gastm_FunctionScope_Scope = Generalization(general=Scope, specific=astm_gastm_FunctionScope)
gen_astm_gastm_NameSpaceType_Type = Generalization(general=Type, specific=astm_gastm_NameSpaceType)
gen_astm_gastm_LabelType_Type = Generalization(general=Type, specific=astm_gastm_LabelType)
gen_astm_gastm_AggregateScope_Scope = Generalization(general=Scope, specific=astm_gastm_AggregateScope)
gen_astm_gastm_BlockScope_Scope = Generalization(general=Scope, specific=astm_gastm_BlockScope)
gen_astm_gastm_IdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_gastm_IdentifierReference)
gen_astm_gastm_PointerType_ConstructedType = Generalization(general=ConstructedType, specific=astm_gastm_PointerType)
gen_astm_gastm_FormalParameterDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_gastm_FormalParameterDefinition)
gen_astm_gastm_ReferenceType_ConstructedType = Generalization(general=ConstructedType, specific=astm_gastm_ReferenceType)
gen_astm_gastm_RangeType_ConstructedType = Generalization(general=ConstructedType, specific=astm_gastm_RangeType)
gen_astm_gastm_VirtualSpecification_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_VirtualSpecification)
gen_astm_gastm_StructureType_AggregateType = Generalization(general=AggregateType, specific=astm_gastm_StructureType)
gen_astm_gastm_UnionType_AggregateType = Generalization(general=AggregateType, specific=astm_gastm_UnionType)
gen_astm_gastm_AnnotationType_AggregateType = Generalization(general=AggregateType, specific=astm_gastm_AnnotationType)
gen_astm_gastm_FormalParameterDeclaration_Declaration = Generalization(general=Declaration, specific=astm_gastm_FormalParameterDeclaration)
gen_astm_gastm_VariableDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_gastm_VariableDefinition)
gen_astm_gastm_FunctionMemberAttribute_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_FunctionMemberAttribute)
gen_astm_gastm_External_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_gastm_External)
gen_astm_gastm_FunctionPersistent_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_gastm_FunctionPersistent)
gen_astm_gastm_FileLocal_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_gastm_FileLocal)
gen_astm_gastm_PerClassMember_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_gastm_PerClassMember)
gen_astm_gastm_NoDef_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_gastm_NoDef)
gen_astm_gastm_Virtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_gastm_Virtual)
gen_astm_gastm_PureVirtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_gastm_PureVirtual)
gen_astm_gastm_NonVirtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_gastm_NonVirtual)
gen_astm_gastm_ExceptionType_DataType = Generalization(general=DataType, specific=astm_gastm_ExceptionType)
gen_astm_gastm_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_Void)
gen_astm_gastm_Byte_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_Byte)
gen_astm_gastm_ShortInteger_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_ShortInteger)
gen_astm_gastm_Integer_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_Integer)
gen_astm_gastm_LongInteger_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_LongInteger)
gen_astm_gastm_Float_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_Float)
gen_astm_gastm_Double_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_Double)
gen_astm_gastm_LongDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_LongDouble)
gen_astm_gastm_Character_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_Character)
gen_astm_gastm_String_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_String)
gen_astm_gastm_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_Boolean)
gen_astm_gastm_WideCharacter_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_WideCharacter)
gen_astm_gastm_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=astm_gastm_CollectionType)
gen_astm_gastm_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_Not)
gen_astm_gastm_BitNot_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_BitNot)
gen_astm_gastm_AddressOf_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_AddressOf)
gen_astm_gastm_Deref_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_Deref)
gen_astm_gastm_Increment_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_Increment)
gen_astm_gastm_Decrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_Decrement)
gen_astm_gastm_PostIncrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_PostIncrement)
gen_astm_gastm_PostDecrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_PostDecrement)
gen_astm_gastm_Add_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Add)
gen_astm_gastm_ByValueFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=astm_gastm_ByValueFormalParameterType)
gen_astm_gastm_ByReferenceFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=astm_gastm_ByReferenceFormalParameterType)
gen_astm_gastm_Public_AccessKind = Generalization(general=AccessKind, specific=astm_gastm_Public)
gen_astm_gastm_Protected_AccessKind = Generalization(general=AccessKind, specific=astm_gastm_Protected)
gen_astm_gastm_Private_AccessKind = Generalization(general=AccessKind, specific=astm_gastm_Private)
gen_astm_gastm_TerminateStatement_Statement = Generalization(general=Statement, specific=astm_gastm_TerminateStatement)
gen_astm_gastm_DefaultBlock_SwitchCase = Generalization(general=SwitchCase, specific=astm_gastm_DefaultBlock)
gen_astm_gastm_WhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_gastm_WhileStatement)
gen_astm_gastm_DoWhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_gastm_DoWhileStatement)
gen_astm_gastm_ForCheckBeforeStatement_ForStatement = Generalization(general=ForStatement, specific=astm_gastm_ForCheckBeforeStatement)
gen_astm_gastm_ForCheckAfterStatement_ForStatement = Generalization(general=ForStatement, specific=astm_gastm_ForCheckAfterStatement)
gen_astm_gastm_AggregateExpression_Expression = Generalization(general=Expression, specific=astm_gastm_AggregateExpression)
gen_astm_gastm_QualifiedOverPointer_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=astm_gastm_QualifiedOverPointer)
gen_astm_gastm_QualifiedOverData_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=astm_gastm_QualifiedOverData)
gen_astm_gastm_IntegerLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_IntegerLiteral)
gen_astm_gastm_StringLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_StringLiteral)
gen_astm_gastm_CharLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_CharLiteral)
gen_astm_gastm_RealLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_RealLiteral)
gen_astm_gastm_BooleanLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_BooleanLiteral)
gen_astm_gastm_BitLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_BitLiteral)
gen_astm_gastm_UnaryPlus_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_UnaryPlus)
gen_astm_gastm_Negate_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_Negate)
gen_astm_gastm_SpecificGreaterEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_SpecificGreaterEqual)
gen_astm_gastm_SpecificIn_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_SpecificIn)
gen_astm_gastm_SpecificLike_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_SpecificLike)
gen_astm_gastm_SpecificConcatString_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_SpecificConcatString)
gen_astm_gastm_SpecificSelectStatement_Statement = Generalization(general=Statement, specific=astm_gastm_SpecificSelectStatement)
gen_astm_sastm_DelphiUnit_CompilationUnit = Generalization(general=CompilationUnit, specific=astm_sastm_DelphiUnit)
gen_astm_gastm_Subtract_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Subtract)
gen_astm_gastm_Multiply_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Multiply)
gen_astm_gastm_Divide_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Divide)
gen_astm_gastm_Modulus_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Modulus)
gen_astm_gastm_Exponent_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Exponent)
gen_astm_gastm_And_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_And)
gen_astm_gastm_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Or)
gen_astm_gastm_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Equal)
gen_astm_gastm_NotEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_NotEqual)
gen_astm_gastm_Greater_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Greater)
gen_astm_gastm_NotGreater_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_NotGreater)
gen_astm_gastm_Less_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Less)
gen_astm_gastm_NotLess_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_NotLess)
gen_astm_gastm_BitAnd_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_BitAnd)
gen_astm_gastm_BitOr_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_BitOr)
gen_astm_gastm_BitXor_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_BitXor)
gen_astm_gastm_BitLeftShift_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_BitLeftShift)
gen_astm_gastm_BitRightShift_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_BitRightShift)
gen_astm_gastm_Assign_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Assign)
gen_astm_gastm_MissingActualParameter_ActualParameter = Generalization(general=ActualParameter, specific=astm_gastm_MissingActualParameter)
gen_astm_gastm_ByValueActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=astm_gastm_ByValueActualParameterExpression)
gen_astm_gastm_ByReferenceActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=astm_gastm_ByReferenceActualParameterExpression)
gen_astm_gastm_SpecificTriggerDefinition_Definition = Generalization(general=Definition, specific=astm_gastm_SpecificTriggerDefinition)
gen_astm_gastm_SpecificLessEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_SpecificLessEqual)
gen_astm_sastm_DelphiWithStatement_BlockStatement = Generalization(general=BlockStatement, specific=astm_sastm_DelphiWithStatement)
gen_astm_sastm_DelphiInterfaceSection_CompilationUnit = Generalization(general=CompilationUnit, specific=astm_sastm_DelphiInterfaceSection)
gen_astm_sastm_DelphiImplementationSection_CompilationUnit = Generalization(general=CompilationUnit, specific=astm_sastm_DelphiImplementationSection)
gen_astm_sastm_DelphiBlockStatement_BlockStatement = Generalization(general=BlockStatement, specific=astm_sastm_DelphiBlockStatement)
gen_astm_sastm_DelphiFunctionCallExpression_FunctionCallExpression = Generalization(general=FunctionCallExpression, specific=astm_sastm_DelphiFunctionCallExpression)

# Domain Model
domain_model = DomainModel(
    name="astm",
    types={astm_gastm_GASTMObject, astm_gastm_GASTMSourceObject, astm_gastm_GASTMSemanticObject, astm_gastm_OtherSyntaxObject, GASTMSyntaxObject, astm_gastm_StorageSpecification, astm_gastm_DataType, Type, astm_gastm_AccessKind, AnnotationExpression, astm_gastm_CompilationUnit, OtherSyntaxObject, astm_gastm_UnaryOperator, astm_gastm_BinaryOperator, astm_gastm_ActualParameter, astm_gastm_SourceFile, GASTMSourceObject, astm_gastm_SourceLocation, SourceFile, astm_gastm_Project, GASTMSemanticObject, CompilationUnit, GlobalScope, astm_gastm_Scope, DefinitionObject, Scope, astm_gastm_GASTMSyntaxObject, GASTMObject, SourceLocation, PreprocessorElement, astm_gastm_FunctionDeclaration, Declaration, FormalParameterDeclaration, FunctionMemberAttributes, ProgramScope, astm_gastm_Name, astm_gastm_DeclarationOrDefinition, astm_gastm_Definition, DeclarationOrDefinition, Name, TypeReference, astm_gastm_Declaration, Definition, astm_gastm_DataDefinition, Expression, astm_gastm_BitFieldDefinition, DataDefinition, astm_gastm_VariableDeclaration, astm_gastm_FunctionDefinition, FormalParameterDefinition, Statement, FunctionScope, astm_gastm_FunctionMemberAttributes, VirtualSpecification, astm_gastm_EntryDefinition, LabelType, astm_gastm_IncludeUnit, astm_gastm_EnumLiteralDefinition, astm_gastm_TypeDefinition, astm_gastm_NamedTypeDefinition, TypeDefinition, NamedType, astm_gastm_AggregateTypeDefinition, AggregateType, astm_gastm_NameSpaceDefinition, NameSpaceType, astm_gastm_LabelDefinition, AggregateScope, astm_gastm_ArrayType, ConstructedType, Dimension, astm_gastm_Dimension, astm_gastm_MacroCall, MacroDefinition, astm_gastm_MacroDefinition, astm_gastm_Comment, astm_gastm_Type, astm_gastm_PrimitiveType, DataType, astm_gastm_EnumType, EnumLiteralDefinition, astm_gastm_ConstructedType, astm_gastm_AggregateType, astm_gastm_UnnamedTypeReference, astm_gastm_NamedTypeReference, astm_gastm_FunctionType, FormalParameterType, astm_gastm_FormalParameterType, astm_gastm_NamedType, astm_gastm_ClassType, DerivesFrom, astm_gastm_DerivesFrom, astm_gastm_BreakStatement, astm_gastm_DeleteStatement, astm_gastm_DeclarationOrDefinitionStatement, astm_gastm_ExpressionStatement, astm_gastm_JumpStatement, LabelAccess, astm_gastm_SwitchStatement, astm_gastm_ContinueStatement, astm_gastm_LabeledStatement, LabelDefinition, astm_gastm_BlockStatement, BlockScope, astm_gastm_EmptyStatement, astm_gastm_IfStatement, astm_gastm_TryStatement, CatchBlock, SwitchCase, astm_gastm_SwitchCase, astm_gastm_CaseBlock, astm_gastm_ReturnStatement, astm_gastm_LoopStatement, astm_gastm_ForStatement, LoopStatement, astm_gastm_QualifiedIdentifierReference, NameReference, IdentifierReference, astm_gastm_TypeQualifiedIdentifierReference, astm_gastm_CatchBlock, astm_gastm_TypesCatchBlock, astm_gastm_VariableCatchBlock, astm_gastm_ThrowStatement, astm_gastm_Expression, astm_gastm_NameReference, astm_gastm_ArrayAccess, astm_gastm_OperatorAssign, BinaryOperator, astm_gastm_Literal, astm_gastm_CastExpression, astm_gastm_UnaryExpression, astm_gastm_BinaryExpression, ActualParameter, astm_gastm_ConditionalExpression, astm_gastm_RangeExpression, astm_gastm_FunctionCallExpression, astm_gastm_ActualParameterExpression, astm_gastm_NewExpression, astm_gastm_LabelAccess, astm_gastm_AnnotationExpression, astm_gastm_GlobalScope, astm_gastm_PreprocessorElement, astm_gastm_DefinitionObject, astm_gastm_ProgramScope, astm_gastm_TypeReference, astm_gastm_Statement, astm_gastm_FunctionScope, astm_gastm_NameSpaceType, astm_gastm_LabelType, astm_gastm_AggregateScope, astm_gastm_BlockScope, astm_gastm_IdentifierReference, astm_gastm_PointerType, astm_gastm_FormalParameterDefinition, astm_gastm_ReferenceType, astm_gastm_RangeType, astm_gastm_VirtualSpecification, astm_gastm_StructureType, astm_gastm_UnionType, astm_gastm_FormalParameterDeclaration, astm_gastm_AnnotationType, astm_gastm_VariableDefinition, astm_gastm_FunctionMemberAttribute, astm_gastm_External, StorageSpecification, astm_gastm_FunctionPersistent, astm_gastm_FileLocal, astm_gastm_PerClassMember, astm_gastm_NoDef, astm_gastm_Virtual, astm_gastm_PureVirtual, astm_gastm_NonVirtual, astm_gastm_ExceptionType, astm_gastm_Void, PrimitiveType, astm_gastm_Byte, astm_gastm_ShortInteger, astm_gastm_Integer, astm_gastm_LongInteger, astm_gastm_Float, astm_gastm_Double, astm_gastm_LongDouble, astm_gastm_Character, astm_gastm_String, astm_gastm_Boolean, astm_gastm_WideCharacter, astm_gastm_CollectionType, astm_gastm_Not, astm_gastm_BitNot, astm_gastm_AddressOf, astm_gastm_Deref, astm_gastm_Increment, astm_gastm_Decrement, astm_gastm_PostIncrement, astm_gastm_PostDecrement, astm_gastm_Add, astm_gastm_ByValueFormalParameterType, astm_gastm_ByReferenceFormalParameterType, astm_gastm_Public, AccessKind, astm_gastm_Protected, astm_gastm_Private, astm_gastm_TerminateStatement, astm_gastm_DefaultBlock, astm_gastm_WhileStatement, astm_gastm_DoWhileStatement, astm_gastm_ForCheckBeforeStatement, ForStatement, astm_gastm_ForCheckAfterStatement, astm_gastm_AggregateExpression, astm_gastm_QualifiedOverPointer, QualifiedIdentifierReference, astm_gastm_QualifiedOverData, astm_gastm_IntegerLiteral, Literal, astm_gastm_StringLiteral, astm_gastm_CharLiteral, astm_gastm_RealLiteral, astm_gastm_BooleanLiteral, astm_gastm_BitLiteral, astm_gastm_UnaryPlus, UnaryOperator, astm_gastm_Negate, astm_gastm_SpecificGreaterEqual, astm_gastm_SpecificIn, astm_gastm_SpecificLike, astm_gastm_SpecificConcatString, astm_gastm_SpecificSelectStatement, astm_sastm_DelphiUnit, astm_gastm_Subtract, astm_gastm_Multiply, astm_gastm_Divide, astm_gastm_Modulus, astm_gastm_Exponent, astm_gastm_And, astm_gastm_Or, astm_gastm_Equal, astm_gastm_NotEqual, astm_gastm_Greater, astm_gastm_NotGreater, astm_gastm_Less, astm_gastm_NotLess, astm_gastm_BitAnd, astm_gastm_BitOr, astm_gastm_BitXor, astm_gastm_BitLeftShift, astm_gastm_BitRightShift, astm_gastm_Assign, astm_gastm_MissingActualParameter, astm_gastm_ByValueActualParameterExpression, ActualParameterExpression, astm_gastm_ByReferenceActualParameterExpression, astm_gastm_SpecificTriggerDefinition, astm_gastm_SpecificLessEqual, astm_sastm_DelphiWithStatement, DelphiInterfaceSection, DelphiImplementationSection, astm_sastm_DelphiInterfaceSection, NamedTypeReference, astm_sastm_DelphiImplementationSection, astm_sastm_DelphiBlockStatement, BlockStatement, astm_sastm_DelphiFunctionCallExpression, FunctionCallExpression},
    associations={preProcessorElements8, annotations10, fragments12, inSourceFile0, files1, outerScope2, definitionObject4, childScope5, locationInfo7, formalParameters30, functionMemberAttributes31, returnType33, opensScope14, storageSpecifiers16, accessKind17, identifierName20, definitionType21, defRef23, identifierName24, declarationType27, initialValue53, bitFieldSize54, returnType36, formalParameters38, body40, functionMemberAttributes42, opensScope45, virtualSpecifier47, formalParameters48, body50, labelName69, labelType71, file73, value56, name58, definitionType60, aggregateType61, nameSpace62, body64, nameSpaceType67, opensScope81, ranks83, refersTo75, enumLiterals76, baseType77, members79, className99, type102, lowBound84, highBound86, returnType89, parameterTypes91, type93, body95, derivesFrom96, accessKind97, name104, type106, operand108, declOrDefn110, expression112, target114, thenBody129, elseBody132, target116, switchExpression135, target117, label119, statement120, subStatements123, opensScope125, condition127, guardedStatement155, catchBlocks157, finalStatement159, cases137, body139, caseExpressions141, returnValue143, condition145, body147, initBody150, iterationBody152, qualifiers181, member183, aggregateType185, body162, exceptions164, exceptionVariable166, exception167, expressionType169, name171, refersTo173, arrayName176, subscripts178, rightOperand205, operator208, member187, castType190, expression192, operator195, operand197, operator200, leftOperand202, calledFunction223, actualParams225, condition210, onTrueOperand212, onFalseOperand215, fromExpression218, toExpression220, annotationType239, memberValues241, value227, newType229, actualParams231, name234, definition236, body244, withs265, name246, interface248, implementation250, uses252, uses253, exports255, exports258, declarations260, applyTo263},
    generalizations={gen_astm_gastm_OtherSyntaxObject_GASTMSyntaxObject, gen_astm_gastm_DataType_Type, gen_astm_gastm_CompilationUnit_OtherSyntaxObject, gen_astm_gastm_SourceFile_GASTMSourceObject, gen_astm_gastm_SourceLocation_GASTMSourceObject, gen_astm_gastm_Project_GASTMSemanticObject, gen_astm_gastm_Scope_GASTMSemanticObject, gen_astm_gastm_GASTMSyntaxObject_GASTMObject, gen_astm_gastm_FunctionDeclaration_Declaration, gen_astm_gastm_Name_OtherSyntaxObject, gen_astm_gastm_DeclarationOrDefinition_DefinitionObject, gen_astm_gastm_Definition_DeclarationOrDefinition, gen_astm_gastm_Declaration_DeclarationOrDefinition, gen_astm_gastm_DataDefinition_Definition, gen_astm_gastm_BitFieldDefinition_DataDefinition, gen_astm_gastm_VariableDeclaration_Declaration, gen_astm_gastm_FunctionDefinition_Definition, gen_astm_gastm_EntryDefinition_Definition, gen_astm_gastm_IncludeUnit_PreprocessorElement, gen_astm_gastm_EnumLiteralDefinition_Definition, gen_astm_gastm_TypeDefinition_DefinitionObject, gen_astm_gastm_NamedTypeDefinition_TypeDefinition, gen_astm_gastm_AggregateTypeDefinition_TypeDefinition, gen_astm_gastm_NameSpaceDefinition_DefinitionObject, gen_astm_gastm_LabelDefinition_DefinitionObject, gen_astm_gastm_ArrayType_ConstructedType, gen_astm_gastm_Dimension_OtherSyntaxObject, gen_astm_gastm_MacroCall_PreprocessorElement, gen_astm_gastm_MacroDefinition_PreprocessorElement, gen_astm_gastm_Comment_PreprocessorElement, gen_astm_gastm_Type_GASTMSyntaxObject, gen_astm_gastm_PrimitiveType_DataType, gen_astm_gastm_EnumType_DataType, gen_astm_gastm_ConstructedType_DataType, gen_astm_gastm_AggregateType_DataType, gen_astm_gastm_UnnamedTypeReference_TypeReference, gen_astm_gastm_NamedTypeReference_TypeReference, gen_astm_gastm_FunctionType_Type, gen_astm_gastm_FormalParameterType_DataType, gen_astm_gastm_NamedType_DataType, gen_astm_gastm_ClassType_AggregateType, gen_astm_gastm_DerivesFrom_OtherSyntaxObject, gen_astm_gastm_BreakStatement_Statement, gen_astm_gastm_DeleteStatement_Statement, gen_astm_gastm_DeclarationOrDefinitionStatement_Statement, gen_astm_gastm_ExpressionStatement_Statement, gen_astm_gastm_JumpStatement_Statement, gen_astm_gastm_SwitchStatement_Statement, gen_astm_gastm_ContinueStatement_Statement, gen_astm_gastm_LabeledStatement_Statement, gen_astm_gastm_BlockStatement_Statement, gen_astm_gastm_EmptyStatement_Statement, gen_astm_gastm_IfStatement_Statement, gen_astm_gastm_TryStatement_Statement, gen_astm_gastm_SwitchCase_OtherSyntaxObject, gen_astm_gastm_CaseBlock_SwitchCase, gen_astm_gastm_ReturnStatement_Statement, gen_astm_gastm_LoopStatement_Statement, gen_astm_gastm_ForStatement_LoopStatement, gen_astm_gastm_QualifiedIdentifierReference_NameReference, gen_astm_gastm_TypeQualifiedIdentifierReference_NameReference, gen_astm_gastm_CatchBlock_OtherSyntaxObject, gen_astm_gastm_TypesCatchBlock_CatchBlock, gen_astm_gastm_VariableCatchBlock_CatchBlock, gen_astm_gastm_ThrowStatement_Statement, gen_astm_gastm_Expression_GASTMSyntaxObject, gen_astm_gastm_NameReference_Expression, gen_astm_gastm_ArrayAccess_Expression, gen_astm_gastm_OperatorAssign_BinaryOperator, gen_astm_gastm_Literal_Expression, gen_astm_gastm_CastExpression_Expression, gen_astm_gastm_UnaryExpression_Expression, gen_astm_gastm_BinaryExpression_Expression, gen_astm_gastm_ConditionalExpression_Expression, gen_astm_gastm_RangeExpression_Expression, gen_astm_gastm_FunctionCallExpression_Expression, gen_astm_gastm_ActualParameterExpression_ActualParameter, gen_astm_gastm_NewExpression_Expression, gen_astm_gastm_LabelAccess_Expression, gen_astm_gastm_AnnotationExpression_Expression, gen_astm_gastm_GlobalScope_Scope, gen_astm_gastm_PreprocessorElement_GASTMSyntaxObject, gen_astm_gastm_DefinitionObject_GASTMSyntaxObject, gen_astm_gastm_ProgramScope_Scope, gen_astm_gastm_TypeReference_Type, gen_astm_gastm_Statement_GASTMSyntaxObject, gen_astm_gastm_FunctionScope_Scope, gen_astm_gastm_NameSpaceType_Type, gen_astm_gastm_LabelType_Type, gen_astm_gastm_AggregateScope_Scope, gen_astm_gastm_BlockScope_Scope, gen_astm_gastm_IdentifierReference_NameReference, gen_astm_gastm_PointerType_ConstructedType, gen_astm_gastm_FormalParameterDefinition_DataDefinition, gen_astm_gastm_ReferenceType_ConstructedType, gen_astm_gastm_RangeType_ConstructedType, gen_astm_gastm_VirtualSpecification_OtherSyntaxObject, gen_astm_gastm_StructureType_AggregateType, gen_astm_gastm_UnionType_AggregateType, gen_astm_gastm_AnnotationType_AggregateType, gen_astm_gastm_FormalParameterDeclaration_Declaration, gen_astm_gastm_VariableDefinition_DataDefinition, gen_astm_gastm_FunctionMemberAttribute_OtherSyntaxObject, gen_astm_gastm_External_StorageSpecification, gen_astm_gastm_FunctionPersistent_StorageSpecification, gen_astm_gastm_FileLocal_StorageSpecification, gen_astm_gastm_PerClassMember_StorageSpecification, gen_astm_gastm_NoDef_StorageSpecification, gen_astm_gastm_Virtual_VirtualSpecification, gen_astm_gastm_PureVirtual_VirtualSpecification, gen_astm_gastm_NonVirtual_VirtualSpecification, gen_astm_gastm_ExceptionType_DataType, gen_astm_gastm_Void_PrimitiveType, gen_astm_gastm_Byte_PrimitiveType, gen_astm_gastm_ShortInteger_PrimitiveType, gen_astm_gastm_Integer_PrimitiveType, gen_astm_gastm_LongInteger_PrimitiveType, gen_astm_gastm_Float_PrimitiveType, gen_astm_gastm_Double_PrimitiveType, gen_astm_gastm_LongDouble_PrimitiveType, gen_astm_gastm_Character_PrimitiveType, gen_astm_gastm_String_PrimitiveType, gen_astm_gastm_Boolean_PrimitiveType, gen_astm_gastm_WideCharacter_PrimitiveType, gen_astm_gastm_CollectionType_ConstructedType, gen_astm_gastm_Not_UnaryOperator, gen_astm_gastm_BitNot_UnaryOperator, gen_astm_gastm_AddressOf_UnaryOperator, gen_astm_gastm_Deref_UnaryOperator, gen_astm_gastm_Increment_UnaryOperator, gen_astm_gastm_Decrement_UnaryOperator, gen_astm_gastm_PostIncrement_UnaryOperator, gen_astm_gastm_PostDecrement_UnaryOperator, gen_astm_gastm_Add_BinaryOperator, gen_astm_gastm_ByValueFormalParameterType_FormalParameterType, gen_astm_gastm_ByReferenceFormalParameterType_FormalParameterType, gen_astm_gastm_Public_AccessKind, gen_astm_gastm_Protected_AccessKind, gen_astm_gastm_Private_AccessKind, gen_astm_gastm_TerminateStatement_Statement, gen_astm_gastm_DefaultBlock_SwitchCase, gen_astm_gastm_WhileStatement_LoopStatement, gen_astm_gastm_DoWhileStatement_LoopStatement, gen_astm_gastm_ForCheckBeforeStatement_ForStatement, gen_astm_gastm_ForCheckAfterStatement_ForStatement, gen_astm_gastm_AggregateExpression_Expression, gen_astm_gastm_QualifiedOverPointer_QualifiedIdentifierReference, gen_astm_gastm_QualifiedOverData_QualifiedIdentifierReference, gen_astm_gastm_IntegerLiteral_Literal, gen_astm_gastm_StringLiteral_Literal, gen_astm_gastm_CharLiteral_Literal, gen_astm_gastm_RealLiteral_Literal, gen_astm_gastm_BooleanLiteral_Literal, gen_astm_gastm_BitLiteral_Literal, gen_astm_gastm_UnaryPlus_UnaryOperator, gen_astm_gastm_Negate_UnaryOperator, gen_astm_gastm_SpecificGreaterEqual_BinaryOperator, gen_astm_gastm_SpecificIn_BinaryOperator, gen_astm_gastm_SpecificLike_BinaryOperator, gen_astm_gastm_SpecificConcatString_BinaryOperator, gen_astm_gastm_SpecificSelectStatement_Statement, gen_astm_sastm_DelphiUnit_CompilationUnit, gen_astm_gastm_Subtract_BinaryOperator, gen_astm_gastm_Multiply_BinaryOperator, gen_astm_gastm_Divide_BinaryOperator, gen_astm_gastm_Modulus_BinaryOperator, gen_astm_gastm_Exponent_BinaryOperator, gen_astm_gastm_And_BinaryOperator, gen_astm_gastm_Or_BinaryOperator, gen_astm_gastm_Equal_BinaryOperator, gen_astm_gastm_NotEqual_BinaryOperator, gen_astm_gastm_Greater_BinaryOperator, gen_astm_gastm_NotGreater_BinaryOperator, gen_astm_gastm_Less_BinaryOperator, gen_astm_gastm_NotLess_BinaryOperator, gen_astm_gastm_BitAnd_BinaryOperator, gen_astm_gastm_BitOr_BinaryOperator, gen_astm_gastm_BitXor_BinaryOperator, gen_astm_gastm_BitLeftShift_BinaryOperator, gen_astm_gastm_BitRightShift_BinaryOperator, gen_astm_gastm_Assign_BinaryOperator, gen_astm_gastm_MissingActualParameter_ActualParameter, gen_astm_gastm_ByValueActualParameterExpression_ActualParameterExpression, gen_astm_gastm_ByReferenceActualParameterExpression_ActualParameterExpression, gen_astm_gastm_SpecificTriggerDefinition_Definition, gen_astm_gastm_SpecificLessEqual_BinaryOperator, gen_astm_sastm_DelphiWithStatement_BlockStatement, gen_astm_sastm_DelphiInterfaceSection_CompilationUnit, gen_astm_sastm_DelphiImplementationSection_CompilationUnit, gen_astm_sastm_DelphiBlockStatement_BlockStatement, gen_astm_sastm_DelphiFunctionCallExpression_FunctionCallExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)