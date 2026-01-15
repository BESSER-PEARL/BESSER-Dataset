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
gastm_OtherSyntaxObject = Class(name="gastm::OtherSyntaxObject", is_abstract=True)
gastm_StorageSpecification = Class(name="gastm::StorageSpecification", is_abstract=True)
gastm_DataType = Class(name="gastm::DataType", is_abstract=True)
gastm_AccessKind = Class(name="gastm::AccessKind")
gastm_UnaryOperator = Class(name="gastm::UnaryOperator", is_abstract=True)
gastm_BinaryOperator = Class(name="gastm::BinaryOperator", is_abstract=True)
gastm_ActualParameter = Class(name="gastm::ActualParameter", is_abstract=True)
gastm_SourceFile = Class(name="gastm::SourceFile")
GASTMSourceObject = Class(name="GASTMSourceObject")
gastm_GASTMObject = Class(name="gastm::GASTMObject")
gastm_GASTMSourceObject = Class(name="gastm::GASTMSourceObject", is_abstract=True)
gastm_GASTMSemanticObject = Class(name="gastm::GASTMSemanticObject", is_abstract=True)
gastm_Definition = Class(name="gastm::Definition", is_abstract=True)
DeclarationOrDefinition = Class(name="DeclarationOrDefinition")
Name = Class(name="Name")
TypeReference = Class(name="TypeReference")
gastm_SourceLocation = Class(name="gastm::SourceLocation")
SourceFile = Class(name="SourceFile")
gastm_Project = Class(name="gastm::Project")
GASTMSemanticObject = Class(name="GASTMSemanticObject")
CompilationUnit = Class(name="CompilationUnit")
GlobalScope = Class(name="GlobalScope")
gastm_Scope = Class(name="gastm::Scope")
DefinitionObject = Class(name="DefinitionObject")
Scope = Class(name="Scope")
gastm_GASTMSyntaxObject = Class(name="gastm::GASTMSyntaxObject", is_abstract=True)
GASTMObject = Class(name="GASTMObject")
SourceLocation = Class(name="SourceLocation")
PreprocessorElement = Class(name="PreprocessorElement")
AnnotationExpression = Class(name="AnnotationExpression")
gastm_CompilationUnit = Class(name="gastm::CompilationUnit")
OtherSyntaxObject = Class(name="OtherSyntaxObject")
ProgramScope = Class(name="ProgramScope")
gastm_Name = Class(name="gastm::Name")
gastm_DeclarationOrDefinition = Class(name="gastm::DeclarationOrDefinition", is_abstract=True)
FunctionScope = Class(name="FunctionScope")
gastm_FunctionMemberAttributes = Class(name="gastm::FunctionMemberAttributes")
VirtualSpecification = Class(name="VirtualSpecification")
gastm_Declaration = Class(name="gastm::Declaration", is_abstract=True)
Definition = Class(name="Definition")
gastm_FunctionDeclaration = Class(name="gastm::FunctionDeclaration")
Declaration = Class(name="Declaration")
FormalParameterDeclaration = Class(name="FormalParameterDeclaration")
FunctionMemberAttributes = Class(name="FunctionMemberAttributes")
gastm_VariableDeclaration = Class(name="gastm::VariableDeclaration")
gastm_FunctionDefinition = Class(name="gastm::FunctionDefinition")
FormalParameterDefinition = Class(name="FormalParameterDefinition")
Statement = Class(name="Statement")
LabelType = Class(name="LabelType")
gastm_IncludeUnit = Class(name="gastm::IncludeUnit")
gastm_MacroCall = Class(name="gastm::MacroCall")
MacroDefinition = Class(name="MacroDefinition")
gastm_MacroDefinition = Class(name="gastm::MacroDefinition")
gastm_EntryDefinition = Class(name="gastm::EntryDefinition")
gastm_DataDefinition = Class(name="gastm::DataDefinition", is_abstract=True)
Expression = Class(name="Expression")
gastm_BitFieldDefinition = Class(name="gastm::BitFieldDefinition")
DataDefinition = Class(name="DataDefinition")
gastm_EnumLiteralDefinition = Class(name="gastm::EnumLiteralDefinition")
gastm_TypeDefinition = Class(name="gastm::TypeDefinition")
gastm_NamedTypeDefinition = Class(name="gastm::NamedTypeDefinition")
TypeDefinition = Class(name="TypeDefinition")
NamedType = Class(name="NamedType")
gastm_AggregateTypeDefinition = Class(name="gastm::AggregateTypeDefinition")
AggregateType = Class(name="AggregateType")
gastm_NameSpaceDefinition = Class(name="gastm::NameSpaceDefinition")
NameSpaceType = Class(name="NameSpaceType")
gastm_LabelDefinition = Class(name="gastm::LabelDefinition")
FormalParameterType = Class(name="FormalParameterType")
gastm_FormalParameterType = Class(name="gastm::FormalParameterType", is_abstract=True)
gastm_NamedType = Class(name="gastm::NamedType")
gastm_ClassType = Class(name="gastm::ClassType")
gastm_Comment = Class(name="gastm::Comment")
gastm_Type = Class(name="gastm::Type", is_abstract=True)
GASTMSyntaxObject = Class(name="GASTMSyntaxObject")
gastm_PrimitiveType = Class(name="gastm::PrimitiveType", is_abstract=True)
DataType = Class(name="DataType")
gastm_EnumType = Class(name="gastm::EnumType")
EnumLiteralDefinition = Class(name="EnumLiteralDefinition")
gastm_ConstructedType = Class(name="gastm::ConstructedType", is_abstract=True)
gastm_AggregateType = Class(name="gastm::AggregateType", is_abstract=True)
AggregateScope = Class(name="AggregateScope")
gastm_ArrayType = Class(name="gastm::ArrayType")
ConstructedType = Class(name="ConstructedType")
Dimension = Class(name="Dimension")
gastm_Dimension = Class(name="gastm::Dimension")
gastm_FunctionType = Class(name="gastm::FunctionType")
Type = Class(name="Type")
gastm_JumpStatement = Class(name="gastm::JumpStatement")
gastm_BreakStatement = Class(name="gastm::BreakStatement")
LabelAccess = Class(name="LabelAccess")
DerivesFrom = Class(name="DerivesFrom")
gastm_DerivesFrom = Class(name="gastm::DerivesFrom")
gastm_UnnamedTypeReference = Class(name="gastm::UnnamedTypeReference")
gastm_NamedTypeReference = Class(name="gastm::NamedTypeReference")
gastm_DeleteStatement = Class(name="gastm::DeleteStatement")
gastm_DeclarationOrDefinitionStatement = Class(name="gastm::DeclarationOrDefinitionStatement")
gastm_ExpressionStatement = Class(name="gastm::ExpressionStatement")
gastm_SwitchStatement = Class(name="gastm::SwitchStatement")
SwitchCase = Class(name="SwitchCase")
gastm_ContinueStatement = Class(name="gastm::ContinueStatement")
gastm_LabeledStatement = Class(name="gastm::LabeledStatement")
LabelDefinition = Class(name="LabelDefinition")
gastm_BlockStatement = Class(name="gastm::BlockStatement")
BlockScope = Class(name="BlockScope")
gastm_EmptyStatement = Class(name="gastm::EmptyStatement")
gastm_IfStatement = Class(name="gastm::IfStatement")
gastm_TryStatement = Class(name="gastm::TryStatement")
gastm_SwitchCase = Class(name="gastm::SwitchCase")
gastm_CaseBlock = Class(name="gastm::CaseBlock")
gastm_ReturnStatement = Class(name="gastm::ReturnStatement")
gastm_LoopStatement = Class(name="gastm::LoopStatement")
gastm_ForStatement = Class(name="gastm::ForStatement", is_abstract=True)
LoopStatement = Class(name="LoopStatement")
gastm_Expression = Class(name="gastm::Expression", is_abstract=True)
gastm_NameReference = Class(name="gastm::NameReference", is_abstract=True)
CatchBlock = Class(name="CatchBlock")
gastm_CatchBlock = Class(name="gastm::CatchBlock")
gastm_TypesCatchBlock = Class(name="gastm::TypesCatchBlock")
gastm_VariableCatchBlock = Class(name="gastm::VariableCatchBlock")
gastm_ThrowStatement = Class(name="gastm::ThrowStatement")
gastm_CastExpression = Class(name="gastm::CastExpression")
gastm_ArrayAccess = Class(name="gastm::ArrayAccess")
gastm_QualifiedIdentifierReference = Class(name="gastm::QualifiedIdentifierReference", is_abstract=True)
NameReference = Class(name="NameReference")
IdentifierReference = Class(name="IdentifierReference")
gastm_TypeQualifiedIdentifierReference = Class(name="gastm::TypeQualifiedIdentifierReference")
gastm_Literal = Class(name="gastm::Literal")
gastm_ConditionalExpression = Class(name="gastm::ConditionalExpression")
gastm_UnaryExpression = Class(name="gastm::UnaryExpression")
gastm_BinaryExpression = Class(name="gastm::BinaryExpression")
gastm_OperatorAssign = Class(name="gastm::OperatorAssign")
BinaryOperator = Class(name="BinaryOperator")
gastm_ActualParameterExpression = Class(name="gastm::ActualParameterExpression")
gastm_NewExpression = Class(name="gastm::NewExpression")
gastm_RangeExpression = Class(name="gastm::RangeExpression")
gastm_FunctionCallExpression = Class(name="gastm::FunctionCallExpression")
ActualParameter = Class(name="ActualParameter")
gastm_PreprocessorElement = Class(name="gastm::PreprocessorElement", is_abstract=True)
gastm_DefinitionObject = Class(name="gastm::DefinitionObject", is_abstract=True)
gastm_ProgramScope = Class(name="gastm::ProgramScope")
gastm_TypeReference = Class(name="gastm::TypeReference", is_abstract=True)
gastm_Statement = Class(name="gastm::Statement", is_abstract=True)
gastm_FunctionScope = Class(name="gastm::FunctionScope")
gastm_NameSpaceType = Class(name="gastm::NameSpaceType")
gastm_LabelType = Class(name="gastm::LabelType")
gastm_AggregateScope = Class(name="gastm::AggregateScope")
gastm_LabelAccess = Class(name="gastm::LabelAccess")
gastm_AnnotationExpression = Class(name="gastm::AnnotationExpression")
gastm_GlobalScope = Class(name="gastm::GlobalScope")
gastm_ShortInteger = Class(name="gastm::ShortInteger")
gastm_Integer = Class(name="gastm::Integer")
gastm_LongInteger = Class(name="gastm::LongInteger")
gastm_Float = Class(name="gastm::Float")
gastm_Double = Class(name="gastm::Double")
gastm_LongDouble = Class(name="gastm::LongDouble")
gastm_Character = Class(name="gastm::Character")
gastm_String = Class(name="gastm::String")
gastm_Boolean = Class(name="gastm::Boolean")
gastm_WideCharacter = Class(name="gastm::WideCharacter")
gastm_BlockScope = Class(name="gastm::BlockScope")
gastm_IdentifierReference = Class(name="gastm::IdentifierReference")
gastm_FormalParameterDefinition = Class(name="gastm::FormalParameterDefinition")
gastm_VirtualSpecification = Class(name="gastm::VirtualSpecification", is_abstract=True)
gastm_FormalParameterDeclaration = Class(name="gastm::FormalParameterDeclaration")
gastm_VariableDefinition = Class(name="gastm::VariableDefinition")
gastm_FunctionMemberAttribute = Class(name="gastm::FunctionMemberAttribute")
gastm_External = Class(name="gastm::External")
StorageSpecification = Class(name="StorageSpecification")
gastm_FunctionPersistent = Class(name="gastm::FunctionPersistent")
gastm_FileLocal = Class(name="gastm::FileLocal")
gastm_PerClassMember = Class(name="gastm::PerClassMember")
gastm_NoDef = Class(name="gastm::NoDef")
gastm_Virtual = Class(name="gastm::Virtual")
gastm_PureVirtual = Class(name="gastm::PureVirtual")
gastm_NonVirtual = Class(name="gastm::NonVirtual")
gastm_ExceptionType = Class(name="gastm::ExceptionType")
gastm_Void = Class(name="gastm::Void")
PrimitiveType = Class(name="PrimitiveType")
gastm_Byte = Class(name="gastm::Byte")
gastm_ForCheckBeforeStatement = Class(name="gastm::ForCheckBeforeStatement")
ForStatement = Class(name="ForStatement")
gastm_ForCheckAfterStatement = Class(name="gastm::ForCheckAfterStatement")
gastm_AggregateExpression = Class(name="gastm::AggregateExpression")
gastm_QualifiedOverPointer = Class(name="gastm::QualifiedOverPointer")
QualifiedIdentifierReference = Class(name="QualifiedIdentifierReference")
gastm_QualifiedOverData = Class(name="gastm::QualifiedOverData")
gastm_IntegerlLiteral = Class(name="gastm::IntegerlLiteral")
Literal = Class(name="Literal")
gastm_StringLiteral = Class(name="gastm::StringLiteral")
gastm_CharLiteral = Class(name="gastm::CharLiteral")
gastm_RealLiteral = Class(name="gastm::RealLiteral")
gastm_CollectionType = Class(name="gastm::CollectionType")
gastm_PointerType = Class(name="gastm::PointerType")
gastm_ReferenceType = Class(name="gastm::ReferenceType")
gastm_RangeType = Class(name="gastm::RangeType")
gastm_StructureType = Class(name="gastm::StructureType")
gastm_UnionType = Class(name="gastm::UnionType")
gastm_AnnotationType = Class(name="gastm::AnnotationType")
gastm_ByValueFormalParameterType = Class(name="gastm::ByValueFormalParameterType")
gastm_ByReferenceFormalParameterType = Class(name="gastm::ByReferenceFormalParameterType")
gastm_Public = Class(name="gastm::Public")
AccessKind = Class(name="AccessKind")
gastm_Protected = Class(name="gastm::Protected")
gastm_Private = Class(name="gastm::Private")
gastm_TerminateStatement = Class(name="gastm::TerminateStatement")
gastm_DefaultBlock = Class(name="gastm::DefaultBlock")
gastm_WhileStatement = Class(name="gastm::WhileStatement")
gastm_DoWhileStatement = Class(name="gastm::DoWhileStatement")
gastm_Or = Class(name="gastm::Or")
gastm_Equal = Class(name="gastm::Equal")
gastm_NotEqual = Class(name="gastm::NotEqual")
gastm_Greater = Class(name="gastm::Greater")
gastm_NotGreater = Class(name="gastm::NotGreater")
gastm_Less = Class(name="gastm::Less")
gastm_NotLess = Class(name="gastm::NotLess")
gastm_BitAnd = Class(name="gastm::BitAnd")
gastm_BitOr = Class(name="gastm::BitOr")
gastm_BitXor = Class(name="gastm::BitXor")
gastm_BitLeftShift = Class(name="gastm::BitLeftShift")
gastm_BooleanLiteral = Class(name="gastm::BooleanLiteral")
gastm_BitLiteral = Class(name="gastm::BitLiteral")
gastm_UnaryPlus = Class(name="gastm::UnaryPlus")
UnaryOperator = Class(name="UnaryOperator")
gastm_Negate = Class(name="gastm::Negate")
gastm_Not = Class(name="gastm::Not")
gastm_BitNot = Class(name="gastm::BitNot")
gastm_AddressOf = Class(name="gastm::AddressOf")
gastm_Deref = Class(name="gastm::Deref")
gastm_Increment = Class(name="gastm::Increment")
gastm_Decrement = Class(name="gastm::Decrement")
gastm_PostIncrement = Class(name="gastm::PostIncrement")
gastm_PostDecrement = Class(name="gastm::PostDecrement")
gastm_Add = Class(name="gastm::Add")
gastm_Subtract = Class(name="gastm::Subtract")
gastm_Multiply = Class(name="gastm::Multiply")
gastm_Divide = Class(name="gastm::Divide")
gastm_Modulus = Class(name="gastm::Modulus")
gastm_Exponent = Class(name="gastm::Exponent")
gastm_And = Class(name="gastm::And")
gastm_SpecificLike = Class(name="gastm::SpecificLike")
gastm_SpecificConcatString = Class(name="gastm::SpecificConcatString")
gastm_SpecificSelectStatement = Class(name="gastm::SpecificSelectStatement")
sastm_RDBDatabaseDefinition = Class(name="sastm::RDBDatabaseDefinition")
RDBTableSpaceReference = Class(name="RDBTableSpaceReference")
sastm_RDBTableSpaceReference = Class(name="sastm::RDBTableSpaceReference")
sastm_RDBUserDefinition = Class(name="sastm::RDBUserDefinition")
NameSpaceDefinition = Class(name="NameSpaceDefinition")
sastm_RDBTableSpaceDefinition = Class(name="sastm::RDBTableSpaceDefinition")
sastm_RDBTableDefinition = Class(name="sastm::RDBTableDefinition")
gastm_BitRightShift = Class(name="gastm::BitRightShift")
gastm_Assign = Class(name="gastm::Assign")
gastm_MissingActualParameter = Class(name="gastm::MissingActualParameter")
gastm_ByValueActualParameterExpression = Class(name="gastm::ByValueActualParameterExpression")
ActualParameterExpression = Class(name="ActualParameterExpression")
gastm_ByReferenceActualParameterExpression = Class(name="gastm::ByReferenceActualParameterExpression")
gastm_SpecificTriggerDefinition = Class(name="gastm::SpecificTriggerDefinition")
gastm_SpecificLessEqual = Class(name="gastm::SpecificLessEqual")
gastm_SpecificGreaterEqual = Class(name="gastm::SpecificGreaterEqual")
gastm_SpecificIn = Class(name="gastm::SpecificIn")
sastm_RDBTrigger = Class(name="sastm::RDBTrigger")
sastm_RDBConstraint = Class(name="sastm::RDBConstraint")
sastm_RDBCheckConstraint = Class(name="sastm::RDBCheckConstraint")
RDBConstraint = Class(name="RDBConstraint")
sastm_RDBRefIntegrity = Class(name="sastm::RDBRefIntegrity")
IncludeUnit = Class(name="IncludeUnit")
Project = Class(name="Project")
sastm_RDBColumnDefinition = Class(name="sastm::RDBColumnDefinition")
sastm_RDBViewDefinition = Class(name="sastm::RDBViewDefinition")
AggregateTypeDefinition = Class(name="AggregateTypeDefinition")
sastm_RDBCursorDefinition = Class(name="sastm::RDBCursorDefinition")
sastm_RDBIndex = Class(name="sastm::RDBIndex")
sastm_RDBIndexColumn = Class(name="sastm::RDBIndexColumn")
sastm_RDBModifyStatement = Class(name="sastm::RDBModifyStatement", is_abstract=True)
sastm_RDBUniqueKey = Class(name="sastm::RDBUniqueKey")
sastm_RDBConnectStatement = Class(name="sastm::RDBConnectStatement")
NamedTypeDefinition = Class(name="NamedTypeDefinition")
sastm_RDBSelectStatement = Class(name="sastm::RDBSelectStatement")
sastm_RDBInsertStatement = Class(name="sastm::RDBInsertStatement")
sastm_RDBHostVariableReference = Class(name="sastm::RDBHostVariableReference")
sastm_RDBSelectExpression = Class(name="sastm::RDBSelectExpression")
sastm_RDBUpdateStatement = Class(name="sastm::RDBUpdateStatement")
RDBModifyStatement = Class(name="RDBModifyStatement")
sastm_RDBCursorStatement = Class(name="sastm::RDBCursorStatement", is_abstract=True)
sastm_RDBOpenCursorStatement = Class(name="sastm::RDBOpenCursorStatement")
RDBCursorStatement = Class(name="RDBCursorStatement")
sastm_RDBFetchCursorStatement = Class(name="sastm::RDBFetchCursorStatement")
RDBHostVariableReference = Class(name="RDBHostVariableReference")
sastm_RDBNumber = Class(name="sastm::RDBNumber")
sastm_RDBLong = Class(name="sastm::RDBLong")
sastm_RDBChar = Class(name="sastm::RDBChar")
sastm_RDBVarchar = Class(name="sastm::RDBVarchar")
sastm_RDBString = Class(name="sastm::RDBString")
sastm_RDBRaw = Class(name="sastm::RDBRaw")
sastm_RDBDate = Class(name="sastm::RDBDate")
sastm_RDBTimestamp = Class(name="sastm::RDBTimestamp")
sastm_RDBRowid = Class(name="sastm::RDBRowid")
sastm_RDBBoolean = Class(name="sastm::RDBBoolean")
sastm_RDBBlob = Class(name="sastm::RDBBlob")
sastm_RDBClob = Class(name="sastm::RDBClob")
sastm_RDBNClob = Class(name="sastm::RDBNClob")
sastm_RDBBFile = Class(name="sastm::RDBBFile")
sastm_RDBTableReference = Class(name="sastm::RDBTableReference")
sastm_RDBTableAlias = Class(name="sastm::RDBTableAlias")
sastm_RDBColumnReference = Class(name="sastm::RDBColumnReference")
sastm_RDBDataBaseType = Class(name="sastm::RDBDataBaseType")
sastm_RDBUserType = Class(name="sastm::RDBUserType")
sastm_RDBTableSpaceType = Class(name="sastm::RDBTableSpaceType")
sastm_RDBTableType = Class(name="sastm::RDBTableType")
sastm_RDBViewType = Class(name="sastm::RDBViewType")
sastm_RDBCursorType = Class(name="sastm::RDBCursorType")
sastm_RDBInteger = Class(name="sastm::RDBInteger")
sastm_RDBInt = Class(name="sastm::RDBInt")
sastm_RDBReal = Class(name="sastm::RDBReal")
sastm_RDBFloat = Class(name="sastm::RDBFloat")
sastm_RDBDecimal = Class(name="sastm::RDBDecimal")
sastm_RDBDeleteStatement = Class(name="sastm::RDBDeleteStatement")
sastm_RDBCloseCursorStatement = Class(name="sastm::RDBCloseCursorStatement")
sastm_RDBHostVariableExpression = Class(name="sastm::RDBHostVariableExpression")

# gastm_OtherSyntaxObject class attributes and methods

# gastm_StorageSpecification class attributes and methods

# gastm_DataType class attributes and methods

# gastm_AccessKind class attributes and methods

# gastm_UnaryOperator class attributes and methods

# gastm_BinaryOperator class attributes and methods

# gastm_ActualParameter class attributes and methods

# gastm_SourceFile class attributes and methods
gastm_SourceFile_pathName: Property = Property(name="pathName", type=StringType)
gastm_SourceFile.attributes={gastm_SourceFile_pathName}

# GASTMSourceObject class attributes and methods

# gastm_GASTMObject class attributes and methods

# gastm_GASTMSourceObject class attributes and methods

# gastm_GASTMSemanticObject class attributes and methods

# gastm_Definition class attributes and methods

# DeclarationOrDefinition class attributes and methods

# Name class attributes and methods

# TypeReference class attributes and methods

# gastm_SourceLocation class attributes and methods
gastm_SourceLocation_startLine: Property = Property(name="startLine", type=IntegerType)
gastm_SourceLocation_startColumn: Property = Property(name="startColumn", type=IntegerType)
gastm_SourceLocation_endLine: Property = Property(name="endLine", type=IntegerType)
gastm_SourceLocation_endColumn: Property = Property(name="endColumn", type=IntegerType)
gastm_SourceLocation.attributes={gastm_SourceLocation_endColumn, gastm_SourceLocation_startColumn, gastm_SourceLocation_startLine, gastm_SourceLocation_endLine}

# SourceFile class attributes and methods

# gastm_Project class attributes and methods

# GASTMSemanticObject class attributes and methods

# CompilationUnit class attributes and methods

# GlobalScope class attributes and methods

# gastm_Scope class attributes and methods

# DefinitionObject class attributes and methods

# Scope class attributes and methods

# gastm_GASTMSyntaxObject class attributes and methods

# GASTMObject class attributes and methods

# SourceLocation class attributes and methods

# PreprocessorElement class attributes and methods

# AnnotationExpression class attributes and methods

# gastm_CompilationUnit class attributes and methods
gastm_CompilationUnit_language: Property = Property(name="language", type=StringType)
gastm_CompilationUnit.attributes={gastm_CompilationUnit_language}

# OtherSyntaxObject class attributes and methods

# ProgramScope class attributes and methods

# gastm_Name class attributes and methods
gastm_Name_nameString: Property = Property(name="nameString", type=StringType)
gastm_Name.attributes={gastm_Name_nameString}

# gastm_DeclarationOrDefinition class attributes and methods
gastm_DeclarationOrDefinition_isRegister: Property = Property(name="isRegister", type=BooleanType)
gastm_DeclarationOrDefinition_linkageSpecifier: Property = Property(name="linkageSpecifier", type=StringType)
gastm_DeclarationOrDefinition.attributes={gastm_DeclarationOrDefinition_linkageSpecifier, gastm_DeclarationOrDefinition_isRegister}

# FunctionScope class attributes and methods

# gastm_FunctionMemberAttributes class attributes and methods
gastm_FunctionMemberAttributes_isFriend: Property = Property(name="isFriend", type=BooleanType)
gastm_FunctionMemberAttributes_isInline: Property = Property(name="isInline", type=BooleanType)
gastm_FunctionMemberAttributes_isThisConst: Property = Property(name="isThisConst", type=BooleanType)
gastm_FunctionMemberAttributes.attributes={gastm_FunctionMemberAttributes_isThisConst, gastm_FunctionMemberAttributes_isInline, gastm_FunctionMemberAttributes_isFriend}

# VirtualSpecification class attributes and methods

# gastm_Declaration class attributes and methods

# Definition class attributes and methods

# gastm_FunctionDeclaration class attributes and methods

# Declaration class attributes and methods

# FormalParameterDeclaration class attributes and methods

# FunctionMemberAttributes class attributes and methods

# gastm_VariableDeclaration class attributes and methods
gastm_VariableDeclaration_isMutable: Property = Property(name="isMutable", type=BooleanType)
gastm_VariableDeclaration.attributes={gastm_VariableDeclaration_isMutable}

# gastm_FunctionDefinition class attributes and methods

# FormalParameterDefinition class attributes and methods

# Statement class attributes and methods

# LabelType class attributes and methods

# gastm_IncludeUnit class attributes and methods

# gastm_MacroCall class attributes and methods

# MacroDefinition class attributes and methods

# gastm_MacroDefinition class attributes and methods
gastm_MacroDefinition_macroName: Property = Property(name="macroName", type=StringType)
gastm_MacroDefinition_body: Property = Property(name="body", type=StringType)
gastm_MacroDefinition.attributes={gastm_MacroDefinition_macroName, gastm_MacroDefinition_body}

# gastm_EntryDefinition class attributes and methods

# gastm_DataDefinition class attributes and methods
gastm_DataDefinition_isMutable: Property = Property(name="isMutable", type=BooleanType)
gastm_DataDefinition.attributes={gastm_DataDefinition_isMutable}

# Expression class attributes and methods

# gastm_BitFieldDefinition class attributes and methods

# DataDefinition class attributes and methods

# gastm_EnumLiteralDefinition class attributes and methods

# gastm_TypeDefinition class attributes and methods

# gastm_NamedTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# NamedType class attributes and methods

# gastm_AggregateTypeDefinition class attributes and methods

# AggregateType class attributes and methods

# gastm_NameSpaceDefinition class attributes and methods

# NameSpaceType class attributes and methods

# gastm_LabelDefinition class attributes and methods

# FormalParameterType class attributes and methods

# gastm_FormalParameterType class attributes and methods

# gastm_NamedType class attributes and methods

# gastm_ClassType class attributes and methods

# gastm_Comment class attributes and methods
gastm_Comment_text: Property = Property(name="text", type=StringType)
gastm_Comment.attributes={gastm_Comment_text}

# gastm_Type class attributes and methods
gastm_Type_isConst: Property = Property(name="isConst", type=BooleanType)
gastm_Type_isVolatile: Property = Property(name="isVolatile", type=BooleanType)
gastm_Type.attributes={gastm_Type_isVolatile, gastm_Type_isConst}

# GASTMSyntaxObject class attributes and methods

# gastm_PrimitiveType class attributes and methods
gastm_PrimitiveType_isSigned: Property = Property(name="isSigned", type=BooleanType)
gastm_PrimitiveType.attributes={gastm_PrimitiveType_isSigned}

# DataType class attributes and methods

# gastm_EnumType class attributes and methods

# EnumLiteralDefinition class attributes and methods

# gastm_ConstructedType class attributes and methods

# gastm_AggregateType class attributes and methods

# AggregateScope class attributes and methods

# gastm_ArrayType class attributes and methods

# ConstructedType class attributes and methods

# Dimension class attributes and methods

# gastm_Dimension class attributes and methods

# gastm_FunctionType class attributes and methods

# Type class attributes and methods

# gastm_JumpStatement class attributes and methods

# gastm_BreakStatement class attributes and methods

# LabelAccess class attributes and methods

# DerivesFrom class attributes and methods

# gastm_DerivesFrom class attributes and methods
gastm_DerivesFrom_isVirtual: Property = Property(name="isVirtual", type=BooleanType)
gastm_DerivesFrom.attributes={gastm_DerivesFrom_isVirtual}

# gastm_UnnamedTypeReference class attributes and methods

# gastm_NamedTypeReference class attributes and methods

# gastm_DeleteStatement class attributes and methods

# gastm_DeclarationOrDefinitionStatement class attributes and methods

# gastm_ExpressionStatement class attributes and methods

# gastm_SwitchStatement class attributes and methods

# SwitchCase class attributes and methods

# gastm_ContinueStatement class attributes and methods

# gastm_LabeledStatement class attributes and methods

# LabelDefinition class attributes and methods

# gastm_BlockStatement class attributes and methods

# BlockScope class attributes and methods

# gastm_EmptyStatement class attributes and methods

# gastm_IfStatement class attributes and methods

# gastm_TryStatement class attributes and methods

# gastm_SwitchCase class attributes and methods

# gastm_CaseBlock class attributes and methods

# gastm_ReturnStatement class attributes and methods

# gastm_LoopStatement class attributes and methods

# gastm_ForStatement class attributes and methods

# LoopStatement class attributes and methods

# gastm_Expression class attributes and methods

# gastm_NameReference class attributes and methods

# CatchBlock class attributes and methods

# gastm_CatchBlock class attributes and methods

# gastm_TypesCatchBlock class attributes and methods

# gastm_VariableCatchBlock class attributes and methods

# gastm_ThrowStatement class attributes and methods

# gastm_CastExpression class attributes and methods

# gastm_ArrayAccess class attributes and methods

# gastm_QualifiedIdentifierReference class attributes and methods

# NameReference class attributes and methods

# IdentifierReference class attributes and methods

# gastm_TypeQualifiedIdentifierReference class attributes and methods

# gastm_Literal class attributes and methods
gastm_Literal_value: Property = Property(name="value", type=StringType)
gastm_Literal.attributes={gastm_Literal_value}

# gastm_ConditionalExpression class attributes and methods

# gastm_UnaryExpression class attributes and methods

# gastm_BinaryExpression class attributes and methods

# gastm_OperatorAssign class attributes and methods

# BinaryOperator class attributes and methods

# gastm_ActualParameterExpression class attributes and methods

# gastm_NewExpression class attributes and methods

# gastm_RangeExpression class attributes and methods

# gastm_FunctionCallExpression class attributes and methods

# ActualParameter class attributes and methods

# gastm_PreprocessorElement class attributes and methods

# gastm_DefinitionObject class attributes and methods

# gastm_ProgramScope class attributes and methods

# gastm_TypeReference class attributes and methods

# gastm_Statement class attributes and methods

# gastm_FunctionScope class attributes and methods

# gastm_NameSpaceType class attributes and methods

# gastm_LabelType class attributes and methods

# gastm_AggregateScope class attributes and methods

# gastm_LabelAccess class attributes and methods

# gastm_AnnotationExpression class attributes and methods

# gastm_GlobalScope class attributes and methods

# gastm_ShortInteger class attributes and methods

# gastm_Integer class attributes and methods

# gastm_LongInteger class attributes and methods

# gastm_Float class attributes and methods

# gastm_Double class attributes and methods

# gastm_LongDouble class attributes and methods

# gastm_Character class attributes and methods

# gastm_String class attributes and methods

# gastm_Boolean class attributes and methods

# gastm_WideCharacter class attributes and methods

# gastm_BlockScope class attributes and methods

# gastm_IdentifierReference class attributes and methods

# gastm_FormalParameterDefinition class attributes and methods

# gastm_VirtualSpecification class attributes and methods

# gastm_FormalParameterDeclaration class attributes and methods

# gastm_VariableDefinition class attributes and methods

# gastm_FunctionMemberAttribute class attributes and methods

# gastm_External class attributes and methods

# StorageSpecification class attributes and methods

# gastm_FunctionPersistent class attributes and methods

# gastm_FileLocal class attributes and methods

# gastm_PerClassMember class attributes and methods

# gastm_NoDef class attributes and methods

# gastm_Virtual class attributes and methods

# gastm_PureVirtual class attributes and methods

# gastm_NonVirtual class attributes and methods

# gastm_ExceptionType class attributes and methods

# gastm_Void class attributes and methods

# PrimitiveType class attributes and methods

# gastm_Byte class attributes and methods

# gastm_ForCheckBeforeStatement class attributes and methods

# ForStatement class attributes and methods

# gastm_ForCheckAfterStatement class attributes and methods

# gastm_AggregateExpression class attributes and methods

# gastm_QualifiedOverPointer class attributes and methods

# QualifiedIdentifierReference class attributes and methods

# gastm_QualifiedOverData class attributes and methods

# gastm_IntegerlLiteral class attributes and methods

# Literal class attributes and methods

# gastm_StringLiteral class attributes and methods

# gastm_CharLiteral class attributes and methods

# gastm_RealLiteral class attributes and methods

# gastm_CollectionType class attributes and methods

# gastm_PointerType class attributes and methods

# gastm_ReferenceType class attributes and methods

# gastm_RangeType class attributes and methods

# gastm_StructureType class attributes and methods

# gastm_UnionType class attributes and methods

# gastm_AnnotationType class attributes and methods

# gastm_ByValueFormalParameterType class attributes and methods

# gastm_ByReferenceFormalParameterType class attributes and methods

# gastm_Public class attributes and methods

# AccessKind class attributes and methods

# gastm_Protected class attributes and methods

# gastm_Private class attributes and methods

# gastm_TerminateStatement class attributes and methods

# gastm_DefaultBlock class attributes and methods

# gastm_WhileStatement class attributes and methods

# gastm_DoWhileStatement class attributes and methods

# gastm_Or class attributes and methods

# gastm_Equal class attributes and methods

# gastm_NotEqual class attributes and methods

# gastm_Greater class attributes and methods

# gastm_NotGreater class attributes and methods

# gastm_Less class attributes and methods

# gastm_NotLess class attributes and methods

# gastm_BitAnd class attributes and methods

# gastm_BitOr class attributes and methods

# gastm_BitXor class attributes and methods

# gastm_BitLeftShift class attributes and methods

# gastm_BooleanLiteral class attributes and methods

# gastm_BitLiteral class attributes and methods

# gastm_UnaryPlus class attributes and methods

# UnaryOperator class attributes and methods

# gastm_Negate class attributes and methods

# gastm_Not class attributes and methods

# gastm_BitNot class attributes and methods

# gastm_AddressOf class attributes and methods

# gastm_Deref class attributes and methods

# gastm_Increment class attributes and methods

# gastm_Decrement class attributes and methods

# gastm_PostIncrement class attributes and methods

# gastm_PostDecrement class attributes and methods

# gastm_Add class attributes and methods

# gastm_Subtract class attributes and methods

# gastm_Multiply class attributes and methods

# gastm_Divide class attributes and methods

# gastm_Modulus class attributes and methods

# gastm_Exponent class attributes and methods

# gastm_And class attributes and methods

# gastm_SpecificLike class attributes and methods

# gastm_SpecificConcatString class attributes and methods

# gastm_SpecificSelectStatement class attributes and methods

# sastm_RDBDatabaseDefinition class attributes and methods

# RDBTableSpaceReference class attributes and methods

# sastm_RDBTableSpaceReference class attributes and methods

# sastm_RDBUserDefinition class attributes and methods

# NameSpaceDefinition class attributes and methods

# sastm_RDBTableSpaceDefinition class attributes and methods

# sastm_RDBTableDefinition class attributes and methods

# gastm_BitRightShift class attributes and methods

# gastm_Assign class attributes and methods

# gastm_MissingActualParameter class attributes and methods

# gastm_ByValueActualParameterExpression class attributes and methods

# ActualParameterExpression class attributes and methods

# gastm_ByReferenceActualParameterExpression class attributes and methods

# gastm_SpecificTriggerDefinition class attributes and methods

# gastm_SpecificLessEqual class attributes and methods

# gastm_SpecificGreaterEqual class attributes and methods

# gastm_SpecificIn class attributes and methods

# sastm_RDBTrigger class attributes and methods

# sastm_RDBConstraint class attributes and methods

# sastm_RDBCheckConstraint class attributes and methods
sastm_RDBCheckConstraint_RDBConstraintText: Property = Property(name="RDBConstraintText", type=StringType)
sastm_RDBCheckConstraint_RDBConstraintType: Property = Property(name="RDBConstraintType", type=StringType)
sastm_RDBCheckConstraint.attributes={sastm_RDBCheckConstraint_RDBConstraintType, sastm_RDBCheckConstraint_RDBConstraintText}

# RDBConstraint class attributes and methods

# sastm_RDBRefIntegrity class attributes and methods

# IncludeUnit class attributes and methods

# Project class attributes and methods

# sastm_RDBColumnDefinition class attributes and methods
sastm_RDBColumnDefinition_NotNull: Property = Property(name="NotNull", type=BooleanType)
sastm_RDBColumnDefinition.attributes={sastm_RDBColumnDefinition_NotNull}

# sastm_RDBViewDefinition class attributes and methods

# AggregateTypeDefinition class attributes and methods

# sastm_RDBCursorDefinition class attributes and methods

# sastm_RDBIndex class attributes and methods
sastm_RDBIndex_NotNull: Property = Property(name="NotNull", type=BooleanType)
sastm_RDBIndex_IsUnique: Property = Property(name="IsUnique", type=BooleanType)
sastm_RDBIndex.attributes={sastm_RDBIndex_NotNull, sastm_RDBIndex_IsUnique}

# sastm_RDBIndexColumn class attributes and methods
sastm_RDBIndexColumn_AscendingOrDescending: Property = Property(name="AscendingOrDescending", type=StringType)
sastm_RDBIndexColumn.attributes={sastm_RDBIndexColumn_AscendingOrDescending}

# sastm_RDBModifyStatement class attributes and methods

# sastm_RDBUniqueKey class attributes and methods

# sastm_RDBConnectStatement class attributes and methods

# NamedTypeDefinition class attributes and methods

# sastm_RDBSelectStatement class attributes and methods

# sastm_RDBInsertStatement class attributes and methods

# sastm_RDBHostVariableReference class attributes and methods

# sastm_RDBSelectExpression class attributes and methods

# sastm_RDBUpdateStatement class attributes and methods

# RDBModifyStatement class attributes and methods

# sastm_RDBCursorStatement class attributes and methods

# sastm_RDBOpenCursorStatement class attributes and methods

# RDBCursorStatement class attributes and methods

# sastm_RDBFetchCursorStatement class attributes and methods

# RDBHostVariableReference class attributes and methods

# sastm_RDBNumber class attributes and methods

# sastm_RDBLong class attributes and methods

# sastm_RDBChar class attributes and methods

# sastm_RDBVarchar class attributes and methods

# sastm_RDBString class attributes and methods

# sastm_RDBRaw class attributes and methods

# sastm_RDBDate class attributes and methods

# sastm_RDBTimestamp class attributes and methods

# sastm_RDBRowid class attributes and methods

# sastm_RDBBoolean class attributes and methods

# sastm_RDBBlob class attributes and methods

# sastm_RDBClob class attributes and methods

# sastm_RDBNClob class attributes and methods

# sastm_RDBBFile class attributes and methods

# sastm_RDBTableReference class attributes and methods

# sastm_RDBTableAlias class attributes and methods

# sastm_RDBColumnReference class attributes and methods

# sastm_RDBDataBaseType class attributes and methods

# sastm_RDBUserType class attributes and methods

# sastm_RDBTableSpaceType class attributes and methods

# sastm_RDBTableType class attributes and methods

# sastm_RDBViewType class attributes and methods

# sastm_RDBCursorType class attributes and methods

# sastm_RDBInteger class attributes and methods

# sastm_RDBInt class attributes and methods

# sastm_RDBReal class attributes and methods

# sastm_RDBFloat class attributes and methods

# sastm_RDBDecimal class attributes and methods

# sastm_RDBDeleteStatement class attributes and methods

# sastm_RDBCloseCursorStatement class attributes and methods

# sastm_RDBHostVariableExpression class attributes and methods

# Relationships
storageSpecifiers16: BinaryAssociation = BinaryAssociation(
    name="storageSpecifiers16",
    ends={
        Property(name="OtherSyntaxObject", type=gastm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DeclarationOrDefinition", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessKind17: BinaryAssociation = BinaryAssociation(
    name="accessKind17",
    ends={
        Property(name="OtherSyntaxObject19", type=gastm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DeclarationOrDefinition18", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierName20: BinaryAssociation = BinaryAssociation(
    name="identifierName20",
    ends={
        Property(name="Name", type=gastm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Definition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inSourceFile0: BinaryAssociation = BinaryAssociation(
    name="inSourceFile0",
    ends={
        Property(name="SourceFile", type=gastm_SourceLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SourceLocation", type=SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
files1: BinaryAssociation = BinaryAssociation(
    name="files1",
    ends={
        Property(name="CompilationUnit", type=gastm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Project", type=CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outerScope2: BinaryAssociation = BinaryAssociation(
    name="outerScope2",
    ends={
        Property(name="GlobalScope", type=gastm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Project3", type=GlobalScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionObject4: BinaryAssociation = BinaryAssociation(
    name="definitionObject4",
    ends={
        Property(name="DefinitionObject", type=gastm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Scope", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childScope5: BinaryAssociation = BinaryAssociation(
    name="childScope5",
    ends={
        Property(name="Scope", type=gastm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Scope6", type=Scope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locationInfo7: BinaryAssociation = BinaryAssociation(
    name="locationInfo7",
    ends={
        Property(name="SourceLocation", type=gastm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_GASTMSyntaxObject", type=SourceLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preProcessorElements8: BinaryAssociation = BinaryAssociation(
    name="preProcessorElements8",
    ends={
        Property(name="PreprocessorElement", type=gastm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_GASTMSyntaxObject9", type=PreprocessorElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations10: BinaryAssociation = BinaryAssociation(
    name="annotations10",
    ends={
        Property(name="AnnotationExpression", type=gastm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_GASTMSyntaxObject11", type=AnnotationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments12: BinaryAssociation = BinaryAssociation(
    name="fragments12",
    ends={
        Property(name="DefinitionObject13", type=gastm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CompilationUnit", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope14: BinaryAssociation = BinaryAssociation(
    name="opensScope14",
    ends={
        Property(name="ProgramScope", type=gastm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CompilationUnit15", type=ProgramScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opensScope42: BinaryAssociation = BinaryAssociation(
    name="opensScope42",
    ends={
        Property(name="FunctionScope", type=gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDefinition43", type=FunctionScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
virtualSpecifier44: BinaryAssociation = BinaryAssociation(
    name="virtualSpecifier44",
    ends={
        Property(name="VirtualSpecification", type=gastm_FunctionMemberAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionMemberAttributes", type=VirtualSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType21: BinaryAssociation = BinaryAssociation(
    name="definitionType21",
    ends={
        Property(name="TypeReference", type=gastm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Definition22", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defRef23: BinaryAssociation = BinaryAssociation(
    name="defRef23",
    ends={
        Property(name="Definition", type=gastm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Declaration", type=Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierName24: BinaryAssociation = BinaryAssociation(
    name="identifierName24",
    ends={
        Property(name="Name26", type=gastm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Declaration25", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarationType27: BinaryAssociation = BinaryAssociation(
    name="declarationType27",
    ends={
        Property(name="TypeReference29", type=gastm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Declaration28", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters30: BinaryAssociation = BinaryAssociation(
    name="formalParameters30",
    ends={
        Property(name="FormalParameterDeclaration", type=gastm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDeclaration", type=FormalParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes31: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes31",
    ends={
        Property(name="FunctionMemberAttributes", type=gastm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDeclaration32", type=FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType33: BinaryAssociation = BinaryAssociation(
    name="returnType33",
    ends={
        Property(name="TypeReference34", type=gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDefinition", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters35: BinaryAssociation = BinaryAssociation(
    name="formalParameters35",
    ends={
        Property(name="FormalParameterDefinition", type=gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDefinition36", type=FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body37: BinaryAssociation = BinaryAssociation(
    name="body37",
    ends={
        Property(name="Statement", type=gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDefinition38", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes39: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes39",
    ends={
        Property(name="FunctionMemberAttributes41", type=gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionDefinition40", type=FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelName66: BinaryAssociation = BinaryAssociation(
    name="labelName66",
    ends={
        Property(name="Name67", type=gastm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabelDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelType68: BinaryAssociation = BinaryAssociation(
    name="labelType68",
    ends={
        Property(name="LabelType", type=gastm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabelDefinition69", type=LabelType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file70: BinaryAssociation = BinaryAssociation(
    name="file70",
    ends={
        Property(name="SourceFile71", type=gastm_IncludeUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_IncludeUnit", type=SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo72: BinaryAssociation = BinaryAssociation(
    name="refersTo72",
    ends={
        Property(name="MacroDefinition", type=gastm_MacroCall, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_MacroCall", type=MacroDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters45: BinaryAssociation = BinaryAssociation(
    name="formalParameters45",
    ends={
        Property(name="FormalParameterDefinition46", type=gastm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_EntryDefinition", type=FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body47: BinaryAssociation = BinaryAssociation(
    name="body47",
    ends={
        Property(name="Statement49", type=gastm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_EntryDefinition48", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue50: BinaryAssociation = BinaryAssociation(
    name="initialValue50",
    ends={
        Property(name="Expression", type=gastm_DataDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DataDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bitFieldSize51: BinaryAssociation = BinaryAssociation(
    name="bitFieldSize51",
    ends={
        Property(name="Expression52", type=gastm_BitFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BitFieldDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value53: BinaryAssociation = BinaryAssociation(
    name="value53",
    ends={
        Property(name="Expression54", type=gastm_EnumLiteralDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_EnumLiteralDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name55: BinaryAssociation = BinaryAssociation(
    name="name55",
    ends={
        Property(name="Name56", type=gastm_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TypeDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType57: BinaryAssociation = BinaryAssociation(
    name="definitionType57",
    ends={
        Property(name="NamedType", type=gastm_NamedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NamedTypeDefinition", type=NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType58: BinaryAssociation = BinaryAssociation(
    name="aggregateType58",
    ends={
        Property(name="AggregateType", type=gastm_AggregateTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AggregateTypeDefinition", type=AggregateType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameSpace59: BinaryAssociation = BinaryAssociation(
    name="nameSpace59",
    ends={
        Property(name="Name60", type=gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NameSpaceDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body61: BinaryAssociation = BinaryAssociation(
    name="body61",
    ends={
        Property(name="DefinitionObject63", type=gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NameSpaceDefinition62", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameSpaceType64: BinaryAssociation = BinaryAssociation(
    name="nameSpaceType64",
    ends={
        Property(name="NameSpaceType", type=gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NameSpaceDefinition65", type=NameSpaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterTypes88: BinaryAssociation = BinaryAssociation(
    name="parameterTypes88",
    ends={
        Property(name="FormalParameterType", type=gastm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionType89", type=FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type90: BinaryAssociation = BinaryAssociation(
    name="type90",
    ends={
        Property(name="TypeReference91", type=gastm_FormalParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FormalParameterType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body92: BinaryAssociation = BinaryAssociation(
    name="body92",
    ends={
        Property(name="Type", type=gastm_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NamedType", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumLiterals73: BinaryAssociation = BinaryAssociation(
    name="enumLiterals73",
    ends={
        Property(name="EnumLiteralDefinition", type=gastm_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_EnumType", type=EnumLiteralDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType74: BinaryAssociation = BinaryAssociation(
    name="baseType74",
    ends={
        Property(name="TypeReference75", type=gastm_ConstructedType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ConstructedType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members76: BinaryAssociation = BinaryAssociation(
    name="members76",
    ends={
        Property(name="DefinitionObject77", type=gastm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AggregateType", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope78: BinaryAssociation = BinaryAssociation(
    name="opensScope78",
    ends={
        Property(name="AggregateScope", type=gastm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AggregateType79", type=AggregateScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ranks80: BinaryAssociation = BinaryAssociation(
    name="ranks80",
    ends={
        Property(name="Dimension", type=gastm_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ArrayType", type=Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lowBound81: BinaryAssociation = BinaryAssociation(
    name="lowBound81",
    ends={
        Property(name="Expression82", type=gastm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Dimension", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
highBound83: BinaryAssociation = BinaryAssociation(
    name="highBound83",
    ends={
        Property(name="Expression85", type=gastm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Dimension84", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType86: BinaryAssociation = BinaryAssociation(
    name="returnType86",
    ends={
        Property(name="TypeReference87", type=gastm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target111: BinaryAssociation = BinaryAssociation(
    name="target111",
    ends={
        Property(name="Expression112", type=gastm_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_JumpStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target113: BinaryAssociation = BinaryAssociation(
    name="target113",
    ends={
        Property(name="LabelAccess", type=gastm_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BreakStatement", type=LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivesFrom93: BinaryAssociation = BinaryAssociation(
    name="derivesFrom93",
    ends={
        Property(name="DerivesFrom", type=gastm_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ClassType", type=DerivesFrom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessKind94: BinaryAssociation = BinaryAssociation(
    name="accessKind94",
    ends={
        Property(name="OtherSyntaxObject95", type=gastm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DerivesFrom", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className96: BinaryAssociation = BinaryAssociation(
    name="className96",
    ends={
        Property(name="NamedType98", type=gastm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DerivesFrom97", type=NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type99: BinaryAssociation = BinaryAssociation(
    name="type99",
    ends={
        Property(name="Type100", type=gastm_UnnamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_UnnamedTypeReference", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name101: BinaryAssociation = BinaryAssociation(
    name="name101",
    ends={
        Property(name="Name102", type=gastm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NamedTypeReference", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="TypeDefinition", type=gastm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NamedTypeReference104", type=TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
operand105: BinaryAssociation = BinaryAssociation(
    name="operand105",
    ends={
        Property(name="Expression106", type=gastm_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DeleteStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declOrDefn107: BinaryAssociation = BinaryAssociation(
    name="declOrDefn107",
    ends={
        Property(name="DefinitionObject108", type=gastm_DeclarationOrDefinitionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_DeclarationOrDefinitionStatement", type=DefinitionObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression109: BinaryAssociation = BinaryAssociation(
    name="expression109",
    ends={
        Property(name="Expression110", type=gastm_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ExpressionStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBody129: BinaryAssociation = BinaryAssociation(
    name="elseBody129",
    ends={
        Property(name="Statement131", type=gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_IfStatement130", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchExpression132: BinaryAssociation = BinaryAssociation(
    name="switchExpression132",
    ends={
        Property(name="Expression133", type=gastm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SwitchStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases134: BinaryAssociation = BinaryAssociation(
    name="cases134",
    ends={
        Property(name="SwitchCase", type=gastm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SwitchStatement135", type=SwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target114: BinaryAssociation = BinaryAssociation(
    name="target114",
    ends={
        Property(name="LabelAccess115", type=gastm_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ContinueStatement", type=LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label116: BinaryAssociation = BinaryAssociation(
    name="label116",
    ends={
        Property(name="LabelDefinition", type=gastm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabeledStatement", type=LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement117: BinaryAssociation = BinaryAssociation(
    name="statement117",
    ends={
        Property(name="Statement119", type=gastm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabeledStatement118", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subStatements120: BinaryAssociation = BinaryAssociation(
    name="subStatements120",
    ends={
        Property(name="Statement121", type=gastm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BlockStatement", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope122: BinaryAssociation = BinaryAssociation(
    name="opensScope122",
    ends={
        Property(name="BlockScope", type=gastm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BlockStatement123", type=BlockScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition124: BinaryAssociation = BinaryAssociation(
    name="condition124",
    ends={
        Property(name="Expression125", type=gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_IfStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBody126: BinaryAssociation = BinaryAssociation(
    name="thenBody126",
    ends={
        Property(name="Statement128", type=gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_IfStatement127", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initBody147: BinaryAssociation = BinaryAssociation(
    name="initBody147",
    ends={
        Property(name="Expression148", type=gastm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ForStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationBody149: BinaryAssociation = BinaryAssociation(
    name="iterationBody149",
    ends={
        Property(name="Expression151", type=gastm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ForStatement150", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guardedStatement152: BinaryAssociation = BinaryAssociation(
    name="guardedStatement152",
    ends={
        Property(name="Statement153", type=gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TryStatement", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body136: BinaryAssociation = BinaryAssociation(
    name="body136",
    ends={
        Property(name="Statement137", type=gastm_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SwitchCase", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caseExpressions138: BinaryAssociation = BinaryAssociation(
    name="caseExpressions138",
    ends={
        Property(name="Expression139", type=gastm_CaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CaseBlock", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue140: BinaryAssociation = BinaryAssociation(
    name="returnValue140",
    ends={
        Property(name="Expression141", type=gastm_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition142: BinaryAssociation = BinaryAssociation(
    name="condition142",
    ends={
        Property(name="Expression143", type=gastm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LoopStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body144: BinaryAssociation = BinaryAssociation(
    name="body144",
    ends={
        Property(name="Statement146", type=gastm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LoopStatement145", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionType166: BinaryAssociation = BinaryAssociation(
    name="expressionType166",
    ends={
        Property(name="TypeReference167", type=gastm_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_Expression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name168: BinaryAssociation = BinaryAssociation(
    name="name168",
    ends={
        Property(name="Name169", type=gastm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NameReference", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchBlocks154: BinaryAssociation = BinaryAssociation(
    name="catchBlocks154",
    ends={
        Property(name="CatchBlock", type=gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TryStatement155", type=CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalStatement156: BinaryAssociation = BinaryAssociation(
    name="finalStatement156",
    ends={
        Property(name="Statement158", type=gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TryStatement157", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body159: BinaryAssociation = BinaryAssociation(
    name="body159",
    ends={
        Property(name="Statement160", type=gastm_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CatchBlock", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions161: BinaryAssociation = BinaryAssociation(
    name="exceptions161",
    ends={
        Property(name="Type162", type=gastm_TypesCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TypesCatchBlock", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionVariable163: BinaryAssociation = BinaryAssociation(
    name="exceptionVariable163",
    ends={
        Property(name="DataDefinition", type=gastm_VariableCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_VariableCatchBlock", type=DataDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception164: BinaryAssociation = BinaryAssociation(
    name="exception164",
    ends={
        Property(name="Expression165", type=gastm_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ThrowStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
castType187: BinaryAssociation = BinaryAssociation(
    name="castType187",
    ends={
        Property(name="TypeReference188", type=gastm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CastExpression", type=TypeReference, multiplicity=Multiplicity(0, 1))
    }
)
expression189: BinaryAssociation = BinaryAssociation(
    name="expression189",
    ends={
        Property(name="Expression191", type=gastm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_CastExpression190", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo170: BinaryAssociation = BinaryAssociation(
    name="refersTo170",
    ends={
        Property(name="DefinitionObject172", type=gastm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NameReference171", type=DefinitionObject, multiplicity=Multiplicity(0, 1))
    }
)
arrayName173: BinaryAssociation = BinaryAssociation(
    name="arrayName173",
    ends={
        Property(name="Expression174", type=gastm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ArrayAccess", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subscripts175: BinaryAssociation = BinaryAssociation(
    name="subscripts175",
    ends={
        Property(name="Expression177", type=gastm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ArrayAccess176", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifiers178: BinaryAssociation = BinaryAssociation(
    name="qualifiers178",
    ends={
        Property(name="Expression179", type=gastm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_QualifiedIdentifierReference", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member180: BinaryAssociation = BinaryAssociation(
    name="member180",
    ends={
        Property(name="IdentifierReference", type=gastm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_QualifiedIdentifierReference181", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType182: BinaryAssociation = BinaryAssociation(
    name="aggregateType182",
    ends={
        Property(name="TypeReference183", type=gastm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TypeQualifiedIdentifierReference", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member184: BinaryAssociation = BinaryAssociation(
    name="member184",
    ends={
        Property(name="IdentifierReference186", type=gastm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_TypeQualifiedIdentifierReference185", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition207: BinaryAssociation = BinaryAssociation(
    name="condition207",
    ends={
        Property(name="Expression208", type=gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ConditionalExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onTrueOperand209: BinaryAssociation = BinaryAssociation(
    name="onTrueOperand209",
    ends={
        Property(name="Expression211", type=gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ConditionalExpression210", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator192: BinaryAssociation = BinaryAssociation(
    name="operator192",
    ends={
        Property(name="OtherSyntaxObject193", type=gastm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_UnaryExpression", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand194: BinaryAssociation = BinaryAssociation(
    name="operand194",
    ends={
        Property(name="Expression196", type=gastm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_UnaryExpression195", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator197: BinaryAssociation = BinaryAssociation(
    name="operator197",
    ends={
        Property(name="OtherSyntaxObject198", type=gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BinaryExpression", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand199: BinaryAssociation = BinaryAssociation(
    name="leftOperand199",
    ends={
        Property(name="Expression201", type=gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BinaryExpression200", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand202: BinaryAssociation = BinaryAssociation(
    name="rightOperand202",
    ends={
        Property(name="Expression204", type=gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_BinaryExpression203", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator205: BinaryAssociation = BinaryAssociation(
    name="operator205",
    ends={
        Property(name="OtherSyntaxObject206", type=gastm_OperatorAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_OperatorAssign", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value224: BinaryAssociation = BinaryAssociation(
    name="value224",
    ends={
        Property(name="Expression225", type=gastm_ActualParameterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ActualParameterExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onFalseOperand212: BinaryAssociation = BinaryAssociation(
    name="onFalseOperand212",
    ends={
        Property(name="Expression214", type=gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_ConditionalExpression213", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromExpression215: BinaryAssociation = BinaryAssociation(
    name="fromExpression215",
    ends={
        Property(name="Expression216", type=gastm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_RangeExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toExpression217: BinaryAssociation = BinaryAssociation(
    name="toExpression217",
    ends={
        Property(name="Expression219", type=gastm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_RangeExpression218", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
calledFunction220: BinaryAssociation = BinaryAssociation(
    name="calledFunction220",
    ends={
        Property(name="Expression221", type=gastm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionCallExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams222: BinaryAssociation = BinaryAssociation(
    name="actualParams222",
    ends={
        Property(name="ActualParameter", type=gastm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_FunctionCallExpression223", type=ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
newType226: BinaryAssociation = BinaryAssociation(
    name="newType226",
    ends={
        Property(name="TypeReference227", type=gastm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NewExpression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams228: BinaryAssociation = BinaryAssociation(
    name="actualParams228",
    ends={
        Property(name="OtherSyntaxObject230", type=gastm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_NewExpression229", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name231: BinaryAssociation = BinaryAssociation(
    name="name231",
    ends={
        Property(name="Name232", type=gastm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabelAccess", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition233: BinaryAssociation = BinaryAssociation(
    name="definition233",
    ends={
        Property(name="LabelDefinition235", type=gastm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_LabelAccess234", type=LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationType236: BinaryAssociation = BinaryAssociation(
    name="annotationType236",
    ends={
        Property(name="TypeReference237", type=gastm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AnnotationExpression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberValues238: BinaryAssociation = BinaryAssociation(
    name="memberValues238",
    ends={
        Property(name="Expression240", type=gastm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_AnnotationExpression239", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TableSpace243: BinaryAssociation = BinaryAssociation(
    name="TableSpace243",
    ends={
        Property(name="RDBTableSpaceReference", type=sastm_RDBDatabaseDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBDatabaseDefinition", type=RDBTableSpaceReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Owns244: BinaryAssociation = BinaryAssociation(
    name="Owns244",
    ends={
        Property(name="NameSpaceDefinition", type=sastm_RDBUserDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBUserDefinition", type=NameSpaceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Table245: BinaryAssociation = BinaryAssociation(
    name="Table245",
    ends={
        Property(name="NameSpaceDefinition246", type=sastm_RDBTableSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBTableSpaceDefinition", type=NameSpaceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body241: BinaryAssociation = BinaryAssociation(
    name="body241",
    ends={
        Property(name="Statement242", type=gastm_SpecificTriggerDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="gastm_SpecificTriggerDefinition", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Column262: BinaryAssociation = BinaryAssociation(
    name="Column262",
    ends={
        Property(name="IncludeUnit263", type=sastm_RDBIndexColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBIndexColumn", type=IncludeUnit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ForeignKey264: BinaryAssociation = BinaryAssociation(
    name="ForeignKey264",
    ends={
        Property(name="IncludeUnit265", type=sastm_RDBRefIntegrity, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBRefIntegrity", type=IncludeUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PrimKey247: BinaryAssociation = BinaryAssociation(
    name="PrimKey247",
    ends={
        Property(name="IncludeUnit", type=sastm_RDBTableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBTableDefinition", type=IncludeUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Column248: BinaryAssociation = BinaryAssociation(
    name="Column248",
    ends={
        Property(name="Project", type=sastm_RDBTableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBTableDefinition249", type=Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Constraint250: BinaryAssociation = BinaryAssociation(
    name="Constraint250",
    ends={
        Property(name="GASTMObject", type=sastm_RDBTableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBTableDefinition251", type=GASTMObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Index252: BinaryAssociation = BinaryAssociation(
    name="Index252",
    ends={
        Property(name="CompilationUnit254", type=sastm_RDBTableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBTableDefinition253", type=CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Trigger255: BinaryAssociation = BinaryAssociation(
    name="Trigger255",
    ends={
        Property(name="DeclarationOrDefinition", type=sastm_RDBTableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBTableDefinition256", type=DeclarationOrDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DefinedBy257: BinaryAssociation = BinaryAssociation(
    name="DefinedBy257",
    ends={
        Property(name="AggregateTypeDefinition", type=sastm_RDBViewDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBViewDefinition", type=AggregateTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SelectExpression258: BinaryAssociation = BinaryAssociation(
    name="SelectExpression258",
    ends={
        Property(name="AggregateTypeDefinition259", type=sastm_RDBCursorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBCursorDefinition", type=AggregateTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IndexColumn260: BinaryAssociation = BinaryAssociation(
    name="IndexColumn260",
    ends={
        Property(name="Name261", type=sastm_RDBIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBIndex", type=Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Columns282: BinaryAssociation = BinaryAssociation(
    name="Columns282",
    ends={
        Property(name="IncludeUnit284", type=sastm_RDBInsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBInsertStatement283", type=IncludeUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Values285: BinaryAssociation = BinaryAssociation(
    name="Values285",
    ends={
        Property(name="Expression287", type=sastm_RDBInsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBInsertStatement286", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ParentKey266: BinaryAssociation = BinaryAssociation(
    name="ParentKey266",
    ends={
        Property(name="IncludeUnit268", type=sastm_RDBRefIntegrity, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBRefIntegrity267", type=IncludeUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ParentTable269: BinaryAssociation = BinaryAssociation(
    name="ParentTable269",
    ends={
        Property(name="IncludeUnit271", type=sastm_RDBRefIntegrity, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBRefIntegrity270", type=IncludeUnit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Column272: BinaryAssociation = BinaryAssociation(
    name="Column272",
    ends={
        Property(name="IncludeUnit273", type=sastm_RDBUniqueKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBUniqueKey", type=IncludeUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ConnectString274: BinaryAssociation = BinaryAssociation(
    name="ConnectString274",
    ends={
        Property(name="NamedTypeDefinition", type=sastm_RDBConnectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBConnectStatement", type=NamedTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SelectExpression275: BinaryAssociation = BinaryAssociation(
    name="SelectExpression275",
    ends={
        Property(name="AggregateTypeDefinition276", type=sastm_RDBSelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBSelectStatement", type=AggregateTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IntoVariable277: BinaryAssociation = BinaryAssociation(
    name="IntoVariable277",
    ends={
        Property(name="NamedTypeDefinition279", type=sastm_RDBSelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBSelectStatement278", type=NamedTypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntoTable280: BinaryAssociation = BinaryAssociation(
    name="IntoTable280",
    ends={
        Property(name="NameSpaceDefinition281", type=sastm_RDBInsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBInsertStatement", type=NameSpaceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BaseVariable300: BinaryAssociation = BinaryAssociation(
    name="BaseVariable300",
    ends={
        Property(name="Expression301", type=sastm_RDBHostVariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBHostVariableReference", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Indicator302: BinaryAssociation = BinaryAssociation(
    name="Indicator302",
    ends={
        Property(name="Expression304", type=sastm_RDBHostVariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBHostVariableReference303", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Table288: BinaryAssociation = BinaryAssociation(
    name="Table288",
    ends={
        Property(name="NameSpaceDefinition289", type=sastm_RDBModifyStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBModifyStatement", type=NameSpaceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Table305: BinaryAssociation = BinaryAssociation(
    name="Table305",
    ends={
        Property(name="NameSpaceDefinition306", type=sastm_RDBSelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBSelectExpression", type=NameSpaceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Where290: BinaryAssociation = BinaryAssociation(
    name="Where290",
    ends={
        Property(name="Expression292", type=sastm_RDBModifyStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBModifyStatement291", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Column307: BinaryAssociation = BinaryAssociation(
    name="Column307",
    ends={
        Property(name="IncludeUnit309", type=sastm_RDBSelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBSelectExpression308", type=IncludeUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Values293: BinaryAssociation = BinaryAssociation(
    name="Values293",
    ends={
        Property(name="Expression294", type=sastm_RDBUpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBUpdateStatement", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Cursor295: BinaryAssociation = BinaryAssociation(
    name="Cursor295",
    ends={
        Property(name="Expression296", type=sastm_RDBCursorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBCursorStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Values297: BinaryAssociation = BinaryAssociation(
    name="Values297",
    ends={
        Property(name="Expression298", type=sastm_RDBOpenCursorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBOpenCursorStatement", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Into299: BinaryAssociation = BinaryAssociation(
    name="Into299",
    ends={
        Property(name="RDBHostVariableReference", type=sastm_RDBFetchCursorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBFetchCursorStatement", type=RDBHostVariableReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Where310: BinaryAssociation = BinaryAssociation(
    name="Where310",
    ends={
        Property(name="Expression312", type=sastm_RDBSelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBSelectExpression311", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Alias313: BinaryAssociation = BinaryAssociation(
    name="Alias313",
    ends={
        Property(name="LabelDefinition314", type=sastm_RDBTableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBTableReference", type=LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Table315: BinaryAssociation = BinaryAssociation(
    name="Table315",
    ends={
        Property(name="Expression316", type=sastm_RDBColumnReference, multiplicity=Multiplicity(1, 1)),
        Property(name="sastm_RDBColumnReference", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_gastm_SourceFile_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=gastm_SourceFile)
gen_gastm_Definition_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=gastm_Definition)
gen_gastm_SourceLocation_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=gastm_SourceLocation)
gen_gastm_Project_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=gastm_Project)
gen_gastm_Scope_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=gastm_Scope)
gen_gastm_GASTMSyntaxObject_GASTMObject = Generalization(general=GASTMObject, specific=gastm_GASTMSyntaxObject)
gen_gastm_CompilationUnit_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=gastm_CompilationUnit)
gen_gastm_Name_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=gastm_Name)
gen_gastm_DeclarationOrDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=gastm_DeclarationOrDefinition)
gen_gastm_Declaration_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=gastm_Declaration)
gen_gastm_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=gastm_FunctionDeclaration)
gen_gastm_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=gastm_VariableDeclaration)
gen_gastm_FunctionDefinition_Definition = Generalization(general=Definition, specific=gastm_FunctionDefinition)
gen_gastm_IncludeUnit_PreprocessorElement = Generalization(general=PreprocessorElement, specific=gastm_IncludeUnit)
gen_gastm_MacroCall_PreprocessorElement = Generalization(general=PreprocessorElement, specific=gastm_MacroCall)
gen_gastm_MacroDefinition_PreprocessorElement = Generalization(general=PreprocessorElement, specific=gastm_MacroDefinition)
gen_gastm_EntryDefinition_Definition = Generalization(general=Definition, specific=gastm_EntryDefinition)
gen_gastm_DataDefinition_Definition = Generalization(general=Definition, specific=gastm_DataDefinition)
gen_gastm_BitFieldDefinition_DataDefinition = Generalization(general=DataDefinition, specific=gastm_BitFieldDefinition)
gen_gastm_EnumLiteralDefinition_Definition = Generalization(general=Definition, specific=gastm_EnumLiteralDefinition)
gen_gastm_TypeDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=gastm_TypeDefinition)
gen_gastm_NamedTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=gastm_NamedTypeDefinition)
gen_gastm_AggregateTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=gastm_AggregateTypeDefinition)
gen_gastm_NameSpaceDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=gastm_NameSpaceDefinition)
gen_gastm_LabelDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=gastm_LabelDefinition)
gen_gastm_FormalParameterType_DataType = Generalization(general=DataType, specific=gastm_FormalParameterType)
gen_gastm_NamedType_DataType = Generalization(general=DataType, specific=gastm_NamedType)
gen_gastm_ClassType_AggregateType = Generalization(general=AggregateType, specific=gastm_ClassType)
gen_gastm_Comment_PreprocessorElement = Generalization(general=PreprocessorElement, specific=gastm_Comment)
gen_gastm_Type_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_Type)
gen_gastm_PrimitiveType_DataType = Generalization(general=DataType, specific=gastm_PrimitiveType)
gen_gastm_EnumType_DataType = Generalization(general=DataType, specific=gastm_EnumType)
gen_gastm_ConstructedType_DataType = Generalization(general=DataType, specific=gastm_ConstructedType)
gen_gastm_AggregateType_DataType = Generalization(general=DataType, specific=gastm_AggregateType)
gen_gastm_ArrayType_ConstructedType = Generalization(general=ConstructedType, specific=gastm_ArrayType)
gen_gastm_Dimension_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=gastm_Dimension)
gen_gastm_FunctionType_Type = Generalization(general=Type, specific=gastm_FunctionType)
gen_gastm_JumpStatement_Statement = Generalization(general=Statement, specific=gastm_JumpStatement)
gen_gastm_BreakStatement_Statement = Generalization(general=Statement, specific=gastm_BreakStatement)
gen_gastm_DerivesFrom_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=gastm_DerivesFrom)
gen_gastm_UnnamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=gastm_UnnamedTypeReference)
gen_gastm_NamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=gastm_NamedTypeReference)
gen_gastm_DeleteStatement_Statement = Generalization(general=Statement, specific=gastm_DeleteStatement)
gen_gastm_DeclarationOrDefinitionStatement_Statement = Generalization(general=Statement, specific=gastm_DeclarationOrDefinitionStatement)
gen_gastm_ExpressionStatement_Statement = Generalization(general=Statement, specific=gastm_ExpressionStatement)
gen_gastm_SwitchStatement_Statement = Generalization(general=Statement, specific=gastm_SwitchStatement)
gen_gastm_ContinueStatement_Statement = Generalization(general=Statement, specific=gastm_ContinueStatement)
gen_gastm_LabeledStatement_Statement = Generalization(general=Statement, specific=gastm_LabeledStatement)
gen_gastm_BlockStatement_Statement = Generalization(general=Statement, specific=gastm_BlockStatement)
gen_gastm_EmptyStatement_Statement = Generalization(general=Statement, specific=gastm_EmptyStatement)
gen_gastm_IfStatement_Statement = Generalization(general=Statement, specific=gastm_IfStatement)
gen_gastm_TryStatement_Statement = Generalization(general=Statement, specific=gastm_TryStatement)
gen_gastm_SwitchCase_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=gastm_SwitchCase)
gen_gastm_CaseBlock_SwitchCase = Generalization(general=SwitchCase, specific=gastm_CaseBlock)
gen_gastm_ReturnStatement_Statement = Generalization(general=Statement, specific=gastm_ReturnStatement)
gen_gastm_LoopStatement_Statement = Generalization(general=Statement, specific=gastm_LoopStatement)
gen_gastm_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=gastm_ForStatement)
gen_gastm_Expression_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_Expression)
gen_gastm_NameReference_Expression = Generalization(general=Expression, specific=gastm_NameReference)
gen_gastm_CatchBlock_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=gastm_CatchBlock)
gen_gastm_TypesCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=gastm_TypesCatchBlock)
gen_gastm_VariableCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=gastm_VariableCatchBlock)
gen_gastm_ThrowStatement_Statement = Generalization(general=Statement, specific=gastm_ThrowStatement)
gen_gastm_CastExpression_Expression = Generalization(general=Expression, specific=gastm_CastExpression)
gen_gastm_ArrayAccess_Expression = Generalization(general=Expression, specific=gastm_ArrayAccess)
gen_gastm_QualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=gastm_QualifiedIdentifierReference)
gen_gastm_TypeQualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=gastm_TypeQualifiedIdentifierReference)
gen_gastm_Literal_Expression = Generalization(general=Expression, specific=gastm_Literal)
gen_gastm_ConditionalExpression_Expression = Generalization(general=Expression, specific=gastm_ConditionalExpression)
gen_gastm_UnaryExpression_Expression = Generalization(general=Expression, specific=gastm_UnaryExpression)
gen_gastm_BinaryExpression_Expression = Generalization(general=Expression, specific=gastm_BinaryExpression)
gen_gastm_OperatorAssign_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_OperatorAssign)
gen_gastm_ActualParameterExpression_ActualParameter = Generalization(general=ActualParameter, specific=gastm_ActualParameterExpression)
gen_gastm_NewExpression_Expression = Generalization(general=Expression, specific=gastm_NewExpression)
gen_gastm_RangeExpression_Expression = Generalization(general=Expression, specific=gastm_RangeExpression)
gen_gastm_FunctionCallExpression_Expression = Generalization(general=Expression, specific=gastm_FunctionCallExpression)
gen_gastm_PreprocessorElement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_PreprocessorElement)
gen_gastm_DefinitionObject_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_DefinitionObject)
gen_gastm_ProgramScope_Scope = Generalization(general=Scope, specific=gastm_ProgramScope)
gen_gastm_TypeReference_Type = Generalization(general=Type, specific=gastm_TypeReference)
gen_gastm_Statement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=gastm_Statement)
gen_gastm_FunctionScope_Scope = Generalization(general=Scope, specific=gastm_FunctionScope)
gen_gastm_NameSpaceType_Type = Generalization(general=Type, specific=gastm_NameSpaceType)
gen_gastm_LabelType_Type = Generalization(general=Type, specific=gastm_LabelType)
gen_gastm_AggregateScope_Scope = Generalization(general=Scope, specific=gastm_AggregateScope)
gen_gastm_LabelAccess_Expression = Generalization(general=Expression, specific=gastm_LabelAccess)
gen_gastm_AnnotationExpression_Expression = Generalization(general=Expression, specific=gastm_AnnotationExpression)
gen_gastm_GlobalScope_Scope = Generalization(general=Scope, specific=gastm_GlobalScope)
gen_gastm_Byte_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_Byte)
gen_gastm_ShortInteger_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_ShortInteger)
gen_gastm_Integer_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_Integer)
gen_gastm_LongInteger_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_LongInteger)
gen_gastm_Float_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_Float)
gen_gastm_Double_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_Double)
gen_gastm_LongDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_LongDouble)
gen_gastm_Character_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_Character)
gen_gastm_String_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_String)
gen_gastm_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_Boolean)
gen_gastm_WideCharacter_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_WideCharacter)
gen_gastm_BlockScope_Scope = Generalization(general=Scope, specific=gastm_BlockScope)
gen_gastm_IdentifierReference_NameReference = Generalization(general=NameReference, specific=gastm_IdentifierReference)
gen_gastm_FormalParameterDefinition_DataDefinition = Generalization(general=DataDefinition, specific=gastm_FormalParameterDefinition)
gen_gastm_VirtualSpecification_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=gastm_VirtualSpecification)
gen_gastm_FormalParameterDeclaration_Declaration = Generalization(general=Declaration, specific=gastm_FormalParameterDeclaration)
gen_gastm_VariableDefinition_DataDefinition = Generalization(general=DataDefinition, specific=gastm_VariableDefinition)
gen_gastm_FunctionMemberAttribute_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=gastm_FunctionMemberAttribute)
gen_gastm_External_StorageSpecification = Generalization(general=StorageSpecification, specific=gastm_External)
gen_gastm_FunctionPersistent_StorageSpecification = Generalization(general=StorageSpecification, specific=gastm_FunctionPersistent)
gen_gastm_FileLocal_StorageSpecification = Generalization(general=StorageSpecification, specific=gastm_FileLocal)
gen_gastm_PerClassMember_StorageSpecification = Generalization(general=StorageSpecification, specific=gastm_PerClassMember)
gen_gastm_NoDef_StorageSpecification = Generalization(general=StorageSpecification, specific=gastm_NoDef)
gen_gastm_Virtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=gastm_Virtual)
gen_gastm_PureVirtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=gastm_PureVirtual)
gen_gastm_NonVirtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=gastm_NonVirtual)
gen_gastm_ExceptionType_DataType = Generalization(general=DataType, specific=gastm_ExceptionType)
gen_gastm_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=gastm_Void)
gen_gastm_ForCheckBeforeStatement_ForStatement = Generalization(general=ForStatement, specific=gastm_ForCheckBeforeStatement)
gen_gastm_ForCheckAfterStatement_ForStatement = Generalization(general=ForStatement, specific=gastm_ForCheckAfterStatement)
gen_gastm_AggregateExpression_Expression = Generalization(general=Expression, specific=gastm_AggregateExpression)
gen_gastm_QualifiedOverPointer_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=gastm_QualifiedOverPointer)
gen_gastm_QualifiedOverData_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=gastm_QualifiedOverData)
gen_gastm_IntegerlLiteral_Literal = Generalization(general=Literal, specific=gastm_IntegerlLiteral)
gen_gastm_StringLiteral_Literal = Generalization(general=Literal, specific=gastm_StringLiteral)
gen_gastm_CharLiteral_Literal = Generalization(general=Literal, specific=gastm_CharLiteral)
gen_gastm_RealLiteral_Literal = Generalization(general=Literal, specific=gastm_RealLiteral)
gen_gastm_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=gastm_CollectionType)
gen_gastm_PointerType_ConstructedType = Generalization(general=ConstructedType, specific=gastm_PointerType)
gen_gastm_ReferenceType_ConstructedType = Generalization(general=ConstructedType, specific=gastm_ReferenceType)
gen_gastm_RangeType_ConstructedType = Generalization(general=ConstructedType, specific=gastm_RangeType)
gen_gastm_StructureType_AggregateType = Generalization(general=AggregateType, specific=gastm_StructureType)
gen_gastm_UnionType_AggregateType = Generalization(general=AggregateType, specific=gastm_UnionType)
gen_gastm_AnnotationType_AggregateType = Generalization(general=AggregateType, specific=gastm_AnnotationType)
gen_gastm_ByValueFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=gastm_ByValueFormalParameterType)
gen_gastm_ByReferenceFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=gastm_ByReferenceFormalParameterType)
gen_gastm_Public_AccessKind = Generalization(general=AccessKind, specific=gastm_Public)
gen_gastm_Protected_AccessKind = Generalization(general=AccessKind, specific=gastm_Protected)
gen_gastm_Private_AccessKind = Generalization(general=AccessKind, specific=gastm_Private)
gen_gastm_TerminateStatement_Statement = Generalization(general=Statement, specific=gastm_TerminateStatement)
gen_gastm_DefaultBlock_SwitchCase = Generalization(general=SwitchCase, specific=gastm_DefaultBlock)
gen_gastm_WhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=gastm_WhileStatement)
gen_gastm_DoWhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=gastm_DoWhileStatement)
gen_gastm_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Or)
gen_gastm_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Equal)
gen_gastm_NotEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_NotEqual)
gen_gastm_Greater_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Greater)
gen_gastm_NotGreater_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_NotGreater)
gen_gastm_Less_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Less)
gen_gastm_NotLess_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_NotLess)
gen_gastm_BitAnd_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_BitAnd)
gen_gastm_BitOr_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_BitOr)
gen_gastm_BitXor_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_BitXor)
gen_gastm_BitLeftShift_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_BitLeftShift)
gen_gastm_BooleanLiteral_Literal = Generalization(general=Literal, specific=gastm_BooleanLiteral)
gen_gastm_BitLiteral_Literal = Generalization(general=Literal, specific=gastm_BitLiteral)
gen_gastm_UnaryPlus_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_UnaryPlus)
gen_gastm_Negate_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_Negate)
gen_gastm_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_Not)
gen_gastm_BitNot_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_BitNot)
gen_gastm_AddressOf_UnaryOperator = Generalization(general=UnaryOperator, specific=gastm_AddressOf)
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
gen_gastm_SpecificLike_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_SpecificLike)
gen_gastm_SpecificConcatString_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_SpecificConcatString)
gen_gastm_SpecificSelectStatement_Statement = Generalization(general=Statement, specific=gastm_SpecificSelectStatement)
gen_sastm_RDBDatabaseDefinition_Definition = Generalization(general=Definition, specific=sastm_RDBDatabaseDefinition)
gen_sastm_RDBUserDefinition_Definition = Generalization(general=Definition, specific=sastm_RDBUserDefinition)
gen_sastm_RDBTableSpaceDefinition_Definition = Generalization(general=Definition, specific=sastm_RDBTableSpaceDefinition)
gen_sastm_RDBTableDefinition_Definition = Generalization(general=Definition, specific=sastm_RDBTableDefinition)
gen_gastm_BitRightShift_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_BitRightShift)
gen_gastm_Assign_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_Assign)
gen_gastm_MissingActualParameter_ActualParameter = Generalization(general=ActualParameter, specific=gastm_MissingActualParameter)
gen_gastm_ByValueActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=gastm_ByValueActualParameterExpression)
gen_gastm_ByReferenceActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=gastm_ByReferenceActualParameterExpression)
gen_gastm_SpecificTriggerDefinition_Definition = Generalization(general=Definition, specific=gastm_SpecificTriggerDefinition)
gen_gastm_SpecificLessEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_SpecificLessEqual)
gen_gastm_SpecificGreaterEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_SpecificGreaterEqual)
gen_gastm_SpecificIn_BinaryOperator = Generalization(general=BinaryOperator, specific=gastm_SpecificIn)
gen_sastm_RDBTrigger_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=sastm_RDBTrigger)
gen_sastm_RDBConstraint_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=sastm_RDBConstraint)
gen_sastm_RDBCheckConstraint_RDBConstraint = Generalization(general=RDBConstraint, specific=sastm_RDBCheckConstraint)
gen_sastm_RDBRefIntegrity_RDBConstraint = Generalization(general=RDBConstraint, specific=sastm_RDBRefIntegrity)
gen_sastm_RDBColumnDefinition_Definition = Generalization(general=Definition, specific=sastm_RDBColumnDefinition)
gen_sastm_RDBViewDefinition_Definition = Generalization(general=Definition, specific=sastm_RDBViewDefinition)
gen_sastm_RDBCursorDefinition_Definition = Generalization(general=Definition, specific=sastm_RDBCursorDefinition)
gen_sastm_RDBIndex_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=sastm_RDBIndex)
gen_sastm_RDBIndexColumn_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=sastm_RDBIndexColumn)
gen_sastm_RDBModifyStatement_Statement = Generalization(general=Statement, specific=sastm_RDBModifyStatement)
gen_sastm_RDBUniqueKey_RDBConstraint = Generalization(general=RDBConstraint, specific=sastm_RDBUniqueKey)
gen_sastm_RDBConnectStatement_Statement = Generalization(general=Statement, specific=sastm_RDBConnectStatement)
gen_sastm_RDBSelectStatement_Statement = Generalization(general=Statement, specific=sastm_RDBSelectStatement)
gen_sastm_RDBInsertStatement_Statement = Generalization(general=Statement, specific=sastm_RDBInsertStatement)
gen_sastm_RDBSelectExpression_Expression = Generalization(general=Expression, specific=sastm_RDBSelectExpression)
gen_sastm_RDBUpdateStatement_RDBModifyStatement = Generalization(general=RDBModifyStatement, specific=sastm_RDBUpdateStatement)
gen_sastm_RDBCursorStatement_Statement = Generalization(general=Statement, specific=sastm_RDBCursorStatement)
gen_sastm_RDBOpenCursorStatement_RDBCursorStatement = Generalization(general=RDBCursorStatement, specific=sastm_RDBOpenCursorStatement)
gen_sastm_RDBFetchCursorStatement_RDBCursorStatement = Generalization(general=RDBCursorStatement, specific=sastm_RDBFetchCursorStatement)
gen_sastm_RDBNumber_DataType = Generalization(general=DataType, specific=sastm_RDBNumber)
gen_sastm_RDBLong_DataType = Generalization(general=DataType, specific=sastm_RDBLong)
gen_sastm_RDBChar_DataType = Generalization(general=DataType, specific=sastm_RDBChar)
gen_sastm_RDBVarchar_DataType = Generalization(general=DataType, specific=sastm_RDBVarchar)
gen_sastm_RDBString_DataType = Generalization(general=DataType, specific=sastm_RDBString)
gen_sastm_RDBRaw_DataType = Generalization(general=DataType, specific=sastm_RDBRaw)
gen_sastm_RDBDate_DataType = Generalization(general=DataType, specific=sastm_RDBDate)
gen_sastm_RDBTimestamp_DataType = Generalization(general=DataType, specific=sastm_RDBTimestamp)
gen_sastm_RDBRowid_DataType = Generalization(general=DataType, specific=sastm_RDBRowid)
gen_sastm_RDBBoolean_DataType = Generalization(general=DataType, specific=sastm_RDBBoolean)
gen_sastm_RDBBlob_DataType = Generalization(general=DataType, specific=sastm_RDBBlob)
gen_sastm_RDBClob_DataType = Generalization(general=DataType, specific=sastm_RDBClob)
gen_sastm_RDBNClob_DataType = Generalization(general=DataType, specific=sastm_RDBNClob)
gen_sastm_RDBBFile_DataType = Generalization(general=DataType, specific=sastm_RDBBFile)
gen_sastm_RDBTableReference_IdentifierReference = Generalization(general=IdentifierReference, specific=sastm_RDBTableReference)
gen_sastm_RDBTableAlias_IdentifierReference = Generalization(general=IdentifierReference, specific=sastm_RDBTableAlias)
gen_sastm_RDBColumnReference_IdentifierReference = Generalization(general=IdentifierReference, specific=sastm_RDBColumnReference)
gen_sastm_RDBDataBaseType_DataType = Generalization(general=DataType, specific=sastm_RDBDataBaseType)
gen_sastm_RDBUserType_DataType = Generalization(general=DataType, specific=sastm_RDBUserType)
gen_sastm_RDBTableSpaceType_DataType = Generalization(general=DataType, specific=sastm_RDBTableSpaceType)
gen_sastm_RDBTableType_DataType = Generalization(general=DataType, specific=sastm_RDBTableType)
gen_sastm_RDBViewType_DataType = Generalization(general=DataType, specific=sastm_RDBViewType)
gen_sastm_RDBCursorType_DataType = Generalization(general=DataType, specific=sastm_RDBCursorType)
gen_sastm_RDBInteger_DataType = Generalization(general=DataType, specific=sastm_RDBInteger)
gen_sastm_RDBInt_DataType = Generalization(general=DataType, specific=sastm_RDBInt)
gen_sastm_RDBReal_DataType = Generalization(general=DataType, specific=sastm_RDBReal)
gen_sastm_RDBFloat_DataType = Generalization(general=DataType, specific=sastm_RDBFloat)
gen_sastm_RDBDecimal_DataType = Generalization(general=DataType, specific=sastm_RDBDecimal)
gen_sastm_RDBDeleteStatement_RDBModifyStatement = Generalization(general=RDBModifyStatement, specific=sastm_RDBDeleteStatement)
gen_sastm_RDBCloseCursorStatement_RDBCursorStatement = Generalization(general=RDBCursorStatement, specific=sastm_RDBCloseCursorStatement)
gen_sastm_RDBHostVariableExpression_Expression = Generalization(general=Expression, specific=sastm_RDBHostVariableExpression)

# Domain Model
domain_model = DomainModel(
    name="sastm",
    types={gastm_OtherSyntaxObject, gastm_StorageSpecification, gastm_DataType, gastm_AccessKind, gastm_UnaryOperator, gastm_BinaryOperator, gastm_ActualParameter, gastm_SourceFile, GASTMSourceObject, gastm_GASTMObject, gastm_GASTMSourceObject, gastm_GASTMSemanticObject, gastm_Definition, DeclarationOrDefinition, Name, TypeReference, gastm_SourceLocation, SourceFile, gastm_Project, GASTMSemanticObject, CompilationUnit, GlobalScope, gastm_Scope, DefinitionObject, Scope, gastm_GASTMSyntaxObject, GASTMObject, SourceLocation, PreprocessorElement, AnnotationExpression, gastm_CompilationUnit, OtherSyntaxObject, ProgramScope, gastm_Name, gastm_DeclarationOrDefinition, FunctionScope, gastm_FunctionMemberAttributes, VirtualSpecification, gastm_Declaration, Definition, gastm_FunctionDeclaration, Declaration, FormalParameterDeclaration, FunctionMemberAttributes, gastm_VariableDeclaration, gastm_FunctionDefinition, FormalParameterDefinition, Statement, LabelType, gastm_IncludeUnit, gastm_MacroCall, MacroDefinition, gastm_MacroDefinition, gastm_EntryDefinition, gastm_DataDefinition, Expression, gastm_BitFieldDefinition, DataDefinition, gastm_EnumLiteralDefinition, gastm_TypeDefinition, gastm_NamedTypeDefinition, TypeDefinition, NamedType, gastm_AggregateTypeDefinition, AggregateType, gastm_NameSpaceDefinition, NameSpaceType, gastm_LabelDefinition, FormalParameterType, gastm_FormalParameterType, gastm_NamedType, gastm_ClassType, gastm_Comment, gastm_Type, GASTMSyntaxObject, gastm_PrimitiveType, DataType, gastm_EnumType, EnumLiteralDefinition, gastm_ConstructedType, gastm_AggregateType, AggregateScope, gastm_ArrayType, ConstructedType, Dimension, gastm_Dimension, gastm_FunctionType, Type, gastm_JumpStatement, gastm_BreakStatement, LabelAccess, DerivesFrom, gastm_DerivesFrom, gastm_UnnamedTypeReference, gastm_NamedTypeReference, gastm_DeleteStatement, gastm_DeclarationOrDefinitionStatement, gastm_ExpressionStatement, gastm_SwitchStatement, SwitchCase, gastm_ContinueStatement, gastm_LabeledStatement, LabelDefinition, gastm_BlockStatement, BlockScope, gastm_EmptyStatement, gastm_IfStatement, gastm_TryStatement, gastm_SwitchCase, gastm_CaseBlock, gastm_ReturnStatement, gastm_LoopStatement, gastm_ForStatement, LoopStatement, gastm_Expression, gastm_NameReference, CatchBlock, gastm_CatchBlock, gastm_TypesCatchBlock, gastm_VariableCatchBlock, gastm_ThrowStatement, gastm_CastExpression, gastm_ArrayAccess, gastm_QualifiedIdentifierReference, NameReference, IdentifierReference, gastm_TypeQualifiedIdentifierReference, gastm_Literal, gastm_ConditionalExpression, gastm_UnaryExpression, gastm_BinaryExpression, gastm_OperatorAssign, BinaryOperator, gastm_ActualParameterExpression, gastm_NewExpression, gastm_RangeExpression, gastm_FunctionCallExpression, ActualParameter, gastm_PreprocessorElement, gastm_DefinitionObject, gastm_ProgramScope, gastm_TypeReference, gastm_Statement, gastm_FunctionScope, gastm_NameSpaceType, gastm_LabelType, gastm_AggregateScope, gastm_LabelAccess, gastm_AnnotationExpression, gastm_GlobalScope, gastm_ShortInteger, gastm_Integer, gastm_LongInteger, gastm_Float, gastm_Double, gastm_LongDouble, gastm_Character, gastm_String, gastm_Boolean, gastm_WideCharacter, gastm_BlockScope, gastm_IdentifierReference, gastm_FormalParameterDefinition, gastm_VirtualSpecification, gastm_FormalParameterDeclaration, gastm_VariableDefinition, gastm_FunctionMemberAttribute, gastm_External, StorageSpecification, gastm_FunctionPersistent, gastm_FileLocal, gastm_PerClassMember, gastm_NoDef, gastm_Virtual, gastm_PureVirtual, gastm_NonVirtual, gastm_ExceptionType, gastm_Void, PrimitiveType, gastm_Byte, gastm_ForCheckBeforeStatement, ForStatement, gastm_ForCheckAfterStatement, gastm_AggregateExpression, gastm_QualifiedOverPointer, QualifiedIdentifierReference, gastm_QualifiedOverData, gastm_IntegerlLiteral, Literal, gastm_StringLiteral, gastm_CharLiteral, gastm_RealLiteral, gastm_CollectionType, gastm_PointerType, gastm_ReferenceType, gastm_RangeType, gastm_StructureType, gastm_UnionType, gastm_AnnotationType, gastm_ByValueFormalParameterType, gastm_ByReferenceFormalParameterType, gastm_Public, AccessKind, gastm_Protected, gastm_Private, gastm_TerminateStatement, gastm_DefaultBlock, gastm_WhileStatement, gastm_DoWhileStatement, gastm_Or, gastm_Equal, gastm_NotEqual, gastm_Greater, gastm_NotGreater, gastm_Less, gastm_NotLess, gastm_BitAnd, gastm_BitOr, gastm_BitXor, gastm_BitLeftShift, gastm_BooleanLiteral, gastm_BitLiteral, gastm_UnaryPlus, UnaryOperator, gastm_Negate, gastm_Not, gastm_BitNot, gastm_AddressOf, gastm_Deref, gastm_Increment, gastm_Decrement, gastm_PostIncrement, gastm_PostDecrement, gastm_Add, gastm_Subtract, gastm_Multiply, gastm_Divide, gastm_Modulus, gastm_Exponent, gastm_And, gastm_SpecificLike, gastm_SpecificConcatString, gastm_SpecificSelectStatement, sastm_RDBDatabaseDefinition, RDBTableSpaceReference, sastm_RDBTableSpaceReference, sastm_RDBUserDefinition, NameSpaceDefinition, sastm_RDBTableSpaceDefinition, sastm_RDBTableDefinition, gastm_BitRightShift, gastm_Assign, gastm_MissingActualParameter, gastm_ByValueActualParameterExpression, ActualParameterExpression, gastm_ByReferenceActualParameterExpression, gastm_SpecificTriggerDefinition, gastm_SpecificLessEqual, gastm_SpecificGreaterEqual, gastm_SpecificIn, sastm_RDBTrigger, sastm_RDBConstraint, sastm_RDBCheckConstraint, RDBConstraint, sastm_RDBRefIntegrity, IncludeUnit, Project, sastm_RDBColumnDefinition, sastm_RDBViewDefinition, AggregateTypeDefinition, sastm_RDBCursorDefinition, sastm_RDBIndex, sastm_RDBIndexColumn, sastm_RDBModifyStatement, sastm_RDBUniqueKey, sastm_RDBConnectStatement, NamedTypeDefinition, sastm_RDBSelectStatement, sastm_RDBInsertStatement, sastm_RDBHostVariableReference, sastm_RDBSelectExpression, sastm_RDBUpdateStatement, RDBModifyStatement, sastm_RDBCursorStatement, sastm_RDBOpenCursorStatement, RDBCursorStatement, sastm_RDBFetchCursorStatement, RDBHostVariableReference, sastm_RDBNumber, sastm_RDBLong, sastm_RDBChar, sastm_RDBVarchar, sastm_RDBString, sastm_RDBRaw, sastm_RDBDate, sastm_RDBTimestamp, sastm_RDBRowid, sastm_RDBBoolean, sastm_RDBBlob, sastm_RDBClob, sastm_RDBNClob, sastm_RDBBFile, sastm_RDBTableReference, sastm_RDBTableAlias, sastm_RDBColumnReference, sastm_RDBDataBaseType, sastm_RDBUserType, sastm_RDBTableSpaceType, sastm_RDBTableType, sastm_RDBViewType, sastm_RDBCursorType, sastm_RDBInteger, sastm_RDBInt, sastm_RDBReal, sastm_RDBFloat, sastm_RDBDecimal, sastm_RDBDeleteStatement, sastm_RDBCloseCursorStatement, sastm_RDBHostVariableExpression},
    associations={storageSpecifiers16, accessKind17, identifierName20, inSourceFile0, files1, outerScope2, definitionObject4, childScope5, locationInfo7, preProcessorElements8, annotations10, fragments12, opensScope14, opensScope42, virtualSpecifier44, definitionType21, defRef23, identifierName24, declarationType27, formalParameters30, functionMemberAttributes31, returnType33, formalParameters35, body37, functionMemberAttributes39, labelName66, labelType68, file70, refersTo72, formalParameters45, body47, initialValue50, bitFieldSize51, value53, name55, definitionType57, aggregateType58, nameSpace59, body61, nameSpaceType64, parameterTypes88, type90, body92, enumLiterals73, baseType74, members76, opensScope78, ranks80, lowBound81, highBound83, returnType86, target111, target113, derivesFrom93, accessKind94, className96, type99, name101, type103, operand105, declOrDefn107, expression109, elseBody129, switchExpression132, cases134, target114, label116, statement117, subStatements120, opensScope122, condition124, thenBody126, initBody147, iterationBody149, guardedStatement152, body136, caseExpressions138, returnValue140, condition142, body144, expressionType166, name168, catchBlocks154, finalStatement156, body159, exceptions161, exceptionVariable163, exception164, castType187, expression189, refersTo170, arrayName173, subscripts175, qualifiers178, member180, aggregateType182, member184, condition207, onTrueOperand209, operator192, operand194, operator197, leftOperand199, rightOperand202, operator205, value224, onFalseOperand212, fromExpression215, toExpression217, calledFunction220, actualParams222, newType226, actualParams228, name231, definition233, annotationType236, memberValues238, TableSpace243, Owns244, Table245, body241, Column262, ForeignKey264, PrimKey247, Column248, Constraint250, Index252, Trigger255, DefinedBy257, SelectExpression258, IndexColumn260, Columns282, Values285, ParentKey266, ParentTable269, Column272, ConnectString274, SelectExpression275, IntoVariable277, IntoTable280, BaseVariable300, Indicator302, Table288, Table305, Where290, Column307, Values293, Cursor295, Values297, Into299, Where310, Alias313, Table315},
    generalizations={gen_gastm_SourceFile_GASTMSourceObject, gen_gastm_Definition_DeclarationOrDefinition, gen_gastm_SourceLocation_GASTMSourceObject, gen_gastm_Project_GASTMSemanticObject, gen_gastm_Scope_GASTMSemanticObject, gen_gastm_GASTMSyntaxObject_GASTMObject, gen_gastm_CompilationUnit_OtherSyntaxObject, gen_gastm_Name_OtherSyntaxObject, gen_gastm_DeclarationOrDefinition_DefinitionObject, gen_gastm_Declaration_DeclarationOrDefinition, gen_gastm_FunctionDeclaration_Declaration, gen_gastm_VariableDeclaration_Declaration, gen_gastm_FunctionDefinition_Definition, gen_gastm_IncludeUnit_PreprocessorElement, gen_gastm_MacroCall_PreprocessorElement, gen_gastm_MacroDefinition_PreprocessorElement, gen_gastm_EntryDefinition_Definition, gen_gastm_DataDefinition_Definition, gen_gastm_BitFieldDefinition_DataDefinition, gen_gastm_EnumLiteralDefinition_Definition, gen_gastm_TypeDefinition_DefinitionObject, gen_gastm_NamedTypeDefinition_TypeDefinition, gen_gastm_AggregateTypeDefinition_TypeDefinition, gen_gastm_NameSpaceDefinition_DefinitionObject, gen_gastm_LabelDefinition_DefinitionObject, gen_gastm_FormalParameterType_DataType, gen_gastm_NamedType_DataType, gen_gastm_ClassType_AggregateType, gen_gastm_Comment_PreprocessorElement, gen_gastm_Type_GASTMSyntaxObject, gen_gastm_PrimitiveType_DataType, gen_gastm_EnumType_DataType, gen_gastm_ConstructedType_DataType, gen_gastm_AggregateType_DataType, gen_gastm_ArrayType_ConstructedType, gen_gastm_Dimension_OtherSyntaxObject, gen_gastm_FunctionType_Type, gen_gastm_JumpStatement_Statement, gen_gastm_BreakStatement_Statement, gen_gastm_DerivesFrom_OtherSyntaxObject, gen_gastm_UnnamedTypeReference_TypeReference, gen_gastm_NamedTypeReference_TypeReference, gen_gastm_DeleteStatement_Statement, gen_gastm_DeclarationOrDefinitionStatement_Statement, gen_gastm_ExpressionStatement_Statement, gen_gastm_SwitchStatement_Statement, gen_gastm_ContinueStatement_Statement, gen_gastm_LabeledStatement_Statement, gen_gastm_BlockStatement_Statement, gen_gastm_EmptyStatement_Statement, gen_gastm_IfStatement_Statement, gen_gastm_TryStatement_Statement, gen_gastm_SwitchCase_OtherSyntaxObject, gen_gastm_CaseBlock_SwitchCase, gen_gastm_ReturnStatement_Statement, gen_gastm_LoopStatement_Statement, gen_gastm_ForStatement_LoopStatement, gen_gastm_Expression_GASTMSyntaxObject, gen_gastm_NameReference_Expression, gen_gastm_CatchBlock_OtherSyntaxObject, gen_gastm_TypesCatchBlock_CatchBlock, gen_gastm_VariableCatchBlock_CatchBlock, gen_gastm_ThrowStatement_Statement, gen_gastm_CastExpression_Expression, gen_gastm_ArrayAccess_Expression, gen_gastm_QualifiedIdentifierReference_NameReference, gen_gastm_TypeQualifiedIdentifierReference_NameReference, gen_gastm_Literal_Expression, gen_gastm_ConditionalExpression_Expression, gen_gastm_UnaryExpression_Expression, gen_gastm_BinaryExpression_Expression, gen_gastm_OperatorAssign_BinaryOperator, gen_gastm_ActualParameterExpression_ActualParameter, gen_gastm_NewExpression_Expression, gen_gastm_RangeExpression_Expression, gen_gastm_FunctionCallExpression_Expression, gen_gastm_PreprocessorElement_GASTMSyntaxObject, gen_gastm_DefinitionObject_GASTMSyntaxObject, gen_gastm_ProgramScope_Scope, gen_gastm_TypeReference_Type, gen_gastm_Statement_GASTMSyntaxObject, gen_gastm_FunctionScope_Scope, gen_gastm_NameSpaceType_Type, gen_gastm_LabelType_Type, gen_gastm_AggregateScope_Scope, gen_gastm_LabelAccess_Expression, gen_gastm_AnnotationExpression_Expression, gen_gastm_GlobalScope_Scope, gen_gastm_Byte_PrimitiveType, gen_gastm_ShortInteger_PrimitiveType, gen_gastm_Integer_PrimitiveType, gen_gastm_LongInteger_PrimitiveType, gen_gastm_Float_PrimitiveType, gen_gastm_Double_PrimitiveType, gen_gastm_LongDouble_PrimitiveType, gen_gastm_Character_PrimitiveType, gen_gastm_String_PrimitiveType, gen_gastm_Boolean_PrimitiveType, gen_gastm_WideCharacter_PrimitiveType, gen_gastm_BlockScope_Scope, gen_gastm_IdentifierReference_NameReference, gen_gastm_FormalParameterDefinition_DataDefinition, gen_gastm_VirtualSpecification_OtherSyntaxObject, gen_gastm_FormalParameterDeclaration_Declaration, gen_gastm_VariableDefinition_DataDefinition, gen_gastm_FunctionMemberAttribute_OtherSyntaxObject, gen_gastm_External_StorageSpecification, gen_gastm_FunctionPersistent_StorageSpecification, gen_gastm_FileLocal_StorageSpecification, gen_gastm_PerClassMember_StorageSpecification, gen_gastm_NoDef_StorageSpecification, gen_gastm_Virtual_VirtualSpecification, gen_gastm_PureVirtual_VirtualSpecification, gen_gastm_NonVirtual_VirtualSpecification, gen_gastm_ExceptionType_DataType, gen_gastm_Void_PrimitiveType, gen_gastm_ForCheckBeforeStatement_ForStatement, gen_gastm_ForCheckAfterStatement_ForStatement, gen_gastm_AggregateExpression_Expression, gen_gastm_QualifiedOverPointer_QualifiedIdentifierReference, gen_gastm_QualifiedOverData_QualifiedIdentifierReference, gen_gastm_IntegerlLiteral_Literal, gen_gastm_StringLiteral_Literal, gen_gastm_CharLiteral_Literal, gen_gastm_RealLiteral_Literal, gen_gastm_CollectionType_ConstructedType, gen_gastm_PointerType_ConstructedType, gen_gastm_ReferenceType_ConstructedType, gen_gastm_RangeType_ConstructedType, gen_gastm_StructureType_AggregateType, gen_gastm_UnionType_AggregateType, gen_gastm_AnnotationType_AggregateType, gen_gastm_ByValueFormalParameterType_FormalParameterType, gen_gastm_ByReferenceFormalParameterType_FormalParameterType, gen_gastm_Public_AccessKind, gen_gastm_Protected_AccessKind, gen_gastm_Private_AccessKind, gen_gastm_TerminateStatement_Statement, gen_gastm_DefaultBlock_SwitchCase, gen_gastm_WhileStatement_LoopStatement, gen_gastm_DoWhileStatement_LoopStatement, gen_gastm_Or_BinaryOperator, gen_gastm_Equal_BinaryOperator, gen_gastm_NotEqual_BinaryOperator, gen_gastm_Greater_BinaryOperator, gen_gastm_NotGreater_BinaryOperator, gen_gastm_Less_BinaryOperator, gen_gastm_NotLess_BinaryOperator, gen_gastm_BitAnd_BinaryOperator, gen_gastm_BitOr_BinaryOperator, gen_gastm_BitXor_BinaryOperator, gen_gastm_BitLeftShift_BinaryOperator, gen_gastm_BooleanLiteral_Literal, gen_gastm_BitLiteral_Literal, gen_gastm_UnaryPlus_UnaryOperator, gen_gastm_Negate_UnaryOperator, gen_gastm_Not_UnaryOperator, gen_gastm_BitNot_UnaryOperator, gen_gastm_AddressOf_UnaryOperator, gen_gastm_Deref_UnaryOperator, gen_gastm_Increment_UnaryOperator, gen_gastm_Decrement_UnaryOperator, gen_gastm_PostIncrement_UnaryOperator, gen_gastm_PostDecrement_UnaryOperator, gen_gastm_Add_BinaryOperator, gen_gastm_Subtract_BinaryOperator, gen_gastm_Multiply_BinaryOperator, gen_gastm_Divide_BinaryOperator, gen_gastm_Modulus_BinaryOperator, gen_gastm_Exponent_BinaryOperator, gen_gastm_And_BinaryOperator, gen_gastm_SpecificLike_BinaryOperator, gen_gastm_SpecificConcatString_BinaryOperator, gen_gastm_SpecificSelectStatement_Statement, gen_sastm_RDBDatabaseDefinition_Definition, gen_sastm_RDBUserDefinition_Definition, gen_sastm_RDBTableSpaceDefinition_Definition, gen_sastm_RDBTableDefinition_Definition, gen_gastm_BitRightShift_BinaryOperator, gen_gastm_Assign_BinaryOperator, gen_gastm_MissingActualParameter_ActualParameter, gen_gastm_ByValueActualParameterExpression_ActualParameterExpression, gen_gastm_ByReferenceActualParameterExpression_ActualParameterExpression, gen_gastm_SpecificTriggerDefinition_Definition, gen_gastm_SpecificLessEqual_BinaryOperator, gen_gastm_SpecificGreaterEqual_BinaryOperator, gen_gastm_SpecificIn_BinaryOperator, gen_sastm_RDBTrigger_OtherSyntaxObject, gen_sastm_RDBConstraint_OtherSyntaxObject, gen_sastm_RDBCheckConstraint_RDBConstraint, gen_sastm_RDBRefIntegrity_RDBConstraint, gen_sastm_RDBColumnDefinition_Definition, gen_sastm_RDBViewDefinition_Definition, gen_sastm_RDBCursorDefinition_Definition, gen_sastm_RDBIndex_OtherSyntaxObject, gen_sastm_RDBIndexColumn_OtherSyntaxObject, gen_sastm_RDBModifyStatement_Statement, gen_sastm_RDBUniqueKey_RDBConstraint, gen_sastm_RDBConnectStatement_Statement, gen_sastm_RDBSelectStatement_Statement, gen_sastm_RDBInsertStatement_Statement, gen_sastm_RDBSelectExpression_Expression, gen_sastm_RDBUpdateStatement_RDBModifyStatement, gen_sastm_RDBCursorStatement_Statement, gen_sastm_RDBOpenCursorStatement_RDBCursorStatement, gen_sastm_RDBFetchCursorStatement_RDBCursorStatement, gen_sastm_RDBNumber_DataType, gen_sastm_RDBLong_DataType, gen_sastm_RDBChar_DataType, gen_sastm_RDBVarchar_DataType, gen_sastm_RDBString_DataType, gen_sastm_RDBRaw_DataType, gen_sastm_RDBDate_DataType, gen_sastm_RDBTimestamp_DataType, gen_sastm_RDBRowid_DataType, gen_sastm_RDBBoolean_DataType, gen_sastm_RDBBlob_DataType, gen_sastm_RDBClob_DataType, gen_sastm_RDBNClob_DataType, gen_sastm_RDBBFile_DataType, gen_sastm_RDBTableReference_IdentifierReference, gen_sastm_RDBTableAlias_IdentifierReference, gen_sastm_RDBColumnReference_IdentifierReference, gen_sastm_RDBDataBaseType_DataType, gen_sastm_RDBUserType_DataType, gen_sastm_RDBTableSpaceType_DataType, gen_sastm_RDBTableType_DataType, gen_sastm_RDBViewType_DataType, gen_sastm_RDBCursorType_DataType, gen_sastm_RDBInteger_DataType, gen_sastm_RDBInt_DataType, gen_sastm_RDBReal_DataType, gen_sastm_RDBFloat_DataType, gen_sastm_RDBDecimal_DataType, gen_sastm_RDBDeleteStatement_RDBModifyStatement, gen_sastm_RDBCloseCursorStatement_RDBCursorStatement, gen_sastm_RDBHostVariableExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)