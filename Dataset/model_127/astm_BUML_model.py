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
astm_gastm_SourceLocation = Class(name="astm::gastm::SourceLocation")
astm_gastm_GASTMObject = Class(name="astm::gastm::GASTMObject")
astm_gastm_GASTMSourceObject = Class(name="astm::gastm::GASTMSourceObject", is_abstract=True)
astm_gastm_GASTMSemanticObject = Class(name="astm::gastm::GASTMSemanticObject", is_abstract=True)
astm_gastm_OtherSyntaxObject = Class(name="astm::gastm::OtherSyntaxObject", is_abstract=True)
astm_gastm_StorageSpecification = Class(name="astm::gastm::StorageSpecification", is_abstract=True)
astm_gastm_DataType = Class(name="astm::gastm::DataType", is_abstract=True)
astm_gastm_AccessKind = Class(name="astm::gastm::AccessKind")
astm_gastm_UnaryOperator = Class(name="astm::gastm::UnaryOperator", is_abstract=True)
astm_gastm_BinaryOperator = Class(name="astm::gastm::BinaryOperator", is_abstract=True)
astm_gastm_ActualParameter = Class(name="astm::gastm::ActualParameter", is_abstract=True)
astm_gastm_SourceFile = Class(name="astm::gastm::SourceFile")
GASTMSourceObject = Class(name="GASTMSourceObject")
SourceLocation = Class(name="SourceLocation")
PreprocessorElement = Class(name="PreprocessorElement")
AnnotationExpression = Class(name="AnnotationExpression")
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
astm_gastm_Definition = Class(name="astm::gastm::Definition", is_abstract=True)
DeclarationOrDefinition = Class(name="DeclarationOrDefinition")
Name = Class(name="Name")
TypeReference = Class(name="TypeReference")
astm_gastm_CompilationUnit = Class(name="astm::gastm::CompilationUnit")
OtherSyntaxObject = Class(name="OtherSyntaxObject")
ProgramScope = Class(name="ProgramScope")
astm_gastm_Name = Class(name="astm::gastm::Name")
astm_gastm_DeclarationOrDefinition = Class(name="astm::gastm::DeclarationOrDefinition", is_abstract=True)
FormalParameterDefinition = Class(name="FormalParameterDefinition")
Statement = Class(name="Statement")
astm_gastm_Declaration = Class(name="astm::gastm::Declaration", is_abstract=True)
Definition = Class(name="Definition")
astm_gastm_FunctionDeclaration = Class(name="astm::gastm::FunctionDeclaration")
Declaration = Class(name="Declaration")
FormalParameterDeclaration = Class(name="FormalParameterDeclaration")
FunctionMemberAttributes = Class(name="FunctionMemberAttributes")
astm_gastm_VariableDeclaration = Class(name="astm::gastm::VariableDeclaration")
astm_gastm_FunctionDefinition = Class(name="astm::gastm::FunctionDefinition")
astm_gastm_DataDefinition = Class(name="astm::gastm::DataDefinition", is_abstract=True)
Expression = Class(name="Expression")
astm_gastm_BitFieldDefinition = Class(name="astm::gastm::BitFieldDefinition")
DataDefinition = Class(name="DataDefinition")
FunctionScope = Class(name="FunctionScope")
astm_gastm_FunctionMemberAttributes = Class(name="astm::gastm::FunctionMemberAttributes")
VirtualSpecification = Class(name="VirtualSpecification")
astm_gastm_EntryDefinition = Class(name="astm::gastm::EntryDefinition")
NameSpaceType = Class(name="NameSpaceType")
astm_gastm_EnumLiteralDefinition = Class(name="astm::gastm::EnumLiteralDefinition")
astm_gastm_TypeDefinition = Class(name="astm::gastm::TypeDefinition")
astm_gastm_NamedTypeDefinition = Class(name="astm::gastm::NamedTypeDefinition")
TypeDefinition = Class(name="TypeDefinition")
NamedType = Class(name="NamedType")
astm_gastm_AggregateTypeDefinition = Class(name="astm::gastm::AggregateTypeDefinition")
AggregateType = Class(name="AggregateType")
astm_gastm_NameSpaceDefinition = Class(name="astm::gastm::NameSpaceDefinition")
astm_gastm_Type = Class(name="astm::gastm::Type", is_abstract=True)
GASTMSyntaxObject = Class(name="GASTMSyntaxObject")
astm_gastm_PrimitiveType = Class(name="astm::gastm::PrimitiveType", is_abstract=True)
astm_gastm_LabelDefinition = Class(name="astm::gastm::LabelDefinition")
LabelType = Class(name="LabelType")
astm_gastm_IncludeUnit = Class(name="astm::gastm::IncludeUnit")
astm_gastm_MacroCall = Class(name="astm::gastm::MacroCall")
MacroDefinition = Class(name="MacroDefinition")
astm_gastm_MacroDefinition = Class(name="astm::gastm::MacroDefinition")
astm_gastm_Comment = Class(name="astm::gastm::Comment")
astm_gastm_Dimension = Class(name="astm::gastm::Dimension")
DataType = Class(name="DataType")
astm_gastm_EnumType = Class(name="astm::gastm::EnumType")
EnumLiteralDefinition = Class(name="EnumLiteralDefinition")
astm_gastm_ConstructedType = Class(name="astm::gastm::ConstructedType", is_abstract=True)
astm_gastm_AggregateType = Class(name="astm::gastm::AggregateType", is_abstract=True)
AggregateScope = Class(name="AggregateScope")
astm_gastm_ArrayType = Class(name="astm::gastm::ArrayType")
ConstructedType = Class(name="ConstructedType")
Dimension = Class(name="Dimension")
astm_gastm_DerivesFrom = Class(name="astm::gastm::DerivesFrom")
astm_gastm_FunctionType = Class(name="astm::gastm::FunctionType")
Type = Class(name="Type")
FormalParameterType = Class(name="FormalParameterType")
astm_gastm_FormalParameterType = Class(name="astm::gastm::FormalParameterType", is_abstract=True)
astm_gastm_NamedType = Class(name="astm::gastm::NamedType")
astm_gastm_ClassType = Class(name="astm::gastm::ClassType")
DerivesFrom = Class(name="DerivesFrom")
astm_gastm_DeclarationOrDefinitionStatement = Class(name="astm::gastm::DeclarationOrDefinitionStatement")
astm_gastm_UnnamedTypeReference = Class(name="astm::gastm::UnnamedTypeReference")
astm_gastm_NamedTypeReference = Class(name="astm::gastm::NamedTypeReference")
astm_gastm_DeleteStatement = Class(name="astm::gastm::DeleteStatement")
astm_gastm_ExpressionStatement = Class(name="astm::gastm::ExpressionStatement")
astm_gastm_JumpStatement = Class(name="astm::gastm::JumpStatement")
astm_gastm_BreakStatement = Class(name="astm::gastm::BreakStatement")
LabelAccess = Class(name="LabelAccess")
astm_gastm_ContinueStatement = Class(name="astm::gastm::ContinueStatement")
astm_gastm_LabeledStatement = Class(name="astm::gastm::LabeledStatement")
LabelDefinition = Class(name="LabelDefinition")
SwitchCase = Class(name="SwitchCase")
astm_gastm_BlockStatement = Class(name="astm::gastm::BlockStatement")
astm_gastm_SwitchCase = Class(name="astm::gastm::SwitchCase")
BlockScope = Class(name="BlockScope")
astm_gastm_EmptyStatement = Class(name="astm::gastm::EmptyStatement")
astm_gastm_IfStatement = Class(name="astm::gastm::IfStatement")
astm_gastm_SwitchStatement = Class(name="astm::gastm::SwitchStatement")
astm_gastm_ForStatement = Class(name="astm::gastm::ForStatement", is_abstract=True)
LoopStatement = Class(name="LoopStatement")
astm_gastm_CaseBlock = Class(name="astm::gastm::CaseBlock")
astm_gastm_ReturnStatement = Class(name="astm::gastm::ReturnStatement")
astm_gastm_LoopStatement = Class(name="astm::gastm::LoopStatement")
astm_gastm_TypesCatchBlock = Class(name="astm::gastm::TypesCatchBlock")
astm_gastm_TryStatement = Class(name="astm::gastm::TryStatement")
CatchBlock = Class(name="CatchBlock")
astm_gastm_CatchBlock = Class(name="astm::gastm::CatchBlock")
astm_gastm_ArrayAccess = Class(name="astm::gastm::ArrayAccess")
astm_gastm_VariableCatchBlock = Class(name="astm::gastm::VariableCatchBlock")
astm_gastm_ThrowStatement = Class(name="astm::gastm::ThrowStatement")
astm_gastm_Expression = Class(name="astm::gastm::Expression", is_abstract=True)
astm_gastm_NameReference = Class(name="astm::gastm::NameReference", is_abstract=True)
astm_gastm_CastExpression = Class(name="astm::gastm::CastExpression")
astm_gastm_QualifiedIdentifierReference = Class(name="astm::gastm::QualifiedIdentifierReference", is_abstract=True)
NameReference = Class(name="NameReference")
IdentifierReference = Class(name="IdentifierReference")
astm_gastm_TypeQualifiedIdentifierReference = Class(name="astm::gastm::TypeQualifiedIdentifierReference")
astm_gastm_Literal = Class(name="astm::gastm::Literal")
astm_gastm_UnaryExpression = Class(name="astm::gastm::UnaryExpression")
astm_gastm_BinaryExpression = Class(name="astm::gastm::BinaryExpression")
astm_gastm_OperatorAssign = Class(name="astm::gastm::OperatorAssign")
BinaryOperator = Class(name="BinaryOperator")
astm_gastm_ConditionalExpression = Class(name="astm::gastm::ConditionalExpression")
astm_gastm_RangeExpression = Class(name="astm::gastm::RangeExpression")
astm_gastm_FunctionCallExpression = Class(name="astm::gastm::FunctionCallExpression")
ActualParameter = Class(name="ActualParameter")
astm_gastm_ActualParameterExpression = Class(name="astm::gastm::ActualParameterExpression")
astm_gastm_NewExpression = Class(name="astm::gastm::NewExpression")
astm_gastm_GlobalScope = Class(name="astm::gastm::GlobalScope")
astm_gastm_PreprocessorElement = Class(name="astm::gastm::PreprocessorElement", is_abstract=True)
astm_gastm_LabelAccess = Class(name="astm::gastm::LabelAccess")
astm_gastm_AnnotationExpression = Class(name="astm::gastm::AnnotationExpression")
StorageSpecification = Class(name="StorageSpecification")
astm_gastm_FunctionPersistent = Class(name="astm::gastm::FunctionPersistent")
astm_gastm_FileLocal = Class(name="astm::gastm::FileLocal")
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
astm_gastm_FormalParameterDefinition = Class(name="astm::gastm::FormalParameterDefinition")
astm_gastm_VirtualSpecification = Class(name="astm::gastm::VirtualSpecification", is_abstract=True)
astm_gastm_FormalParameterDeclaration = Class(name="astm::gastm::FormalParameterDeclaration")
astm_gastm_VariableDefinition = Class(name="astm::gastm::VariableDefinition")
astm_gastm_FunctionMemberAttribute = Class(name="astm::gastm::FunctionMemberAttribute")
astm_gastm_External = Class(name="astm::gastm::External")
astm_gastm_String = Class(name="astm::gastm::String")
astm_gastm_Boolean = Class(name="astm::gastm::Boolean")
astm_gastm_WideCharacter = Class(name="astm::gastm::WideCharacter")
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
astm_gastm_ForCheckBeforeStatement = Class(name="astm::gastm::ForCheckBeforeStatement")
ForStatement = Class(name="ForStatement")
astm_gastm_ForCheckAfterStatement = Class(name="astm::gastm::ForCheckAfterStatement")
astm_gastm_CollectionType = Class(name="astm::gastm::CollectionType")
astm_gastm_PointerType = Class(name="astm::gastm::PointerType")
astm_gastm_ReferenceType = Class(name="astm::gastm::ReferenceType")
astm_gastm_RangeType = Class(name="astm::gastm::RangeType")
astm_gastm_StructureType = Class(name="astm::gastm::StructureType")
astm_gastm_UnionType = Class(name="astm::gastm::UnionType")
astm_gastm_AnnotationType = Class(name="astm::gastm::AnnotationType")
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
astm_gastm_Decrement = Class(name="astm::gastm::Decrement")
astm_gastm_PostIncrement = Class(name="astm::gastm::PostIncrement")
astm_gastm_PostDecrement = Class(name="astm::gastm::PostDecrement")
astm_gastm_AggregateExpression = Class(name="astm::gastm::AggregateExpression")
astm_gastm_QualifiedOverPointer = Class(name="astm::gastm::QualifiedOverPointer")
QualifiedIdentifierReference = Class(name="QualifiedIdentifierReference")
astm_gastm_QualifiedOverData = Class(name="astm::gastm::QualifiedOverData")
astm_gastm_IntegerlLiteral = Class(name="astm::gastm::IntegerlLiteral")
Literal = Class(name="Literal")
astm_gastm_StringLiteral = Class(name="astm::gastm::StringLiteral")
astm_gastm_CharLiteral = Class(name="astm::gastm::CharLiteral")
astm_gastm_RealLiteral = Class(name="astm::gastm::RealLiteral")
astm_gastm_BooleanLiteral = Class(name="astm::gastm::BooleanLiteral")
astm_gastm_BitLiteral = Class(name="astm::gastm::BitLiteral")
astm_gastm_UnaryPlus = Class(name="astm::gastm::UnaryPlus")
UnaryOperator = Class(name="UnaryOperator")
astm_gastm_Negate = Class(name="astm::gastm::Negate")
astm_gastm_Not = Class(name="astm::gastm::Not")
astm_gastm_BitNot = Class(name="astm::gastm::BitNot")
astm_gastm_AddressOf = Class(name="astm::gastm::AddressOf")
astm_gastm_Deref = Class(name="astm::gastm::Deref")
astm_gastm_Increment = Class(name="astm::gastm::Increment")
astm_gastm_BitXor = Class(name="astm::gastm::BitXor")
astm_gastm_BitLeftShift = Class(name="astm::gastm::BitLeftShift")
astm_gastm_BitRightShift = Class(name="astm::gastm::BitRightShift")
astm_gastm_Add = Class(name="astm::gastm::Add")
astm_gastm_Assign = Class(name="astm::gastm::Assign")
astm_gastm_Subtract = Class(name="astm::gastm::Subtract")
astm_gastm_MissingActualParameter = Class(name="astm::gastm::MissingActualParameter")
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
astm_sastm_RDBDatabaseDefinition = Class(name="astm::sastm::RDBDatabaseDefinition")
RDBTableSpaceReference = Class(name="RDBTableSpaceReference")
astm_sastm_RDBTableSpaceReference = Class(name="astm::sastm::RDBTableSpaceReference")
astm_sastm_RDBUserDefinition = Class(name="astm::sastm::RDBUserDefinition")
astm_gastm_ByValueActualParameterExpression = Class(name="astm::gastm::ByValueActualParameterExpression")
ActualParameterExpression = Class(name="ActualParameterExpression")
NameSpaceDefinition = Class(name="NameSpaceDefinition")
astm_gastm_ByReferenceActualParameterExpression = Class(name="astm::gastm::ByReferenceActualParameterExpression")
astm_gastm_SpecificTriggerDefinition = Class(name="astm::gastm::SpecificTriggerDefinition")
astm_sastm_RDBTableSpaceDefinition = Class(name="astm::sastm::RDBTableSpaceDefinition")
astm_sastm_RDBTableDefinition = Class(name="astm::sastm::RDBTableDefinition")
astm_gastm_SpecificLessEqual = Class(name="astm::gastm::SpecificLessEqual")
RDBColumnReference = Class(name="RDBColumnReference")
astm_gastm_SpecificGreaterEqual = Class(name="astm::gastm::SpecificGreaterEqual")
astm_gastm_SpecificIn = Class(name="astm::gastm::SpecificIn")
astm_gastm_SpecificLike = Class(name="astm::gastm::SpecificLike")
astm_gastm_SpecificConcatString = Class(name="astm::gastm::SpecificConcatString")
astm_gastm_SpecificSelectStatement = Class(name="astm::gastm::SpecificSelectStatement")
RDBTrigger = Class(name="RDBTrigger")
astm_sastm_RDBColumnDefinition = Class(name="astm::sastm::RDBColumnDefinition")
RDBColumnType = Class(name="RDBColumnType")
astm_sastm_RDBViewDefinition = Class(name="astm::sastm::RDBViewDefinition")
AggregateTypeDefinition = Class(name="AggregateTypeDefinition")
RDBColumnDefinition = Class(name="RDBColumnDefinition")
RDBConstraint = Class(name="RDBConstraint")
RDBIndex = Class(name="RDBIndex")
astm_sastm_RDBCursorDefinition = Class(name="astm::sastm::RDBCursorDefinition")
astm_sastm_RDBIndex = Class(name="astm::sastm::RDBIndex")
astm_sastm_RDBTrigger = Class(name="astm::sastm::RDBTrigger")
gastm_OtherSyntaxObject = Class(name="gastm::OtherSyntaxObject")
gastm_Definition = Class(name="gastm::Definition")
astm_sastm_RDBConstraint = Class(name="astm::sastm::RDBConstraint")
astm_sastm_RDBCheckConstraint = Class(name="astm::sastm::RDBCheckConstraint")
astm_sastm_RDBRefIntegrity = Class(name="astm::sastm::RDBRefIntegrity")
astm_sastm_RDBIndexColumn = Class(name="astm::sastm::RDBIndexColumn")
IncludeUnit = Class(name="IncludeUnit")
astm_sastm_RDBConnectStatement = Class(name="astm::sastm::RDBConnectStatement")
NamedTypeDefinition = Class(name="NamedTypeDefinition")
astm_sastm_RDBSelectStatement = Class(name="astm::sastm::RDBSelectStatement")
RDBSelectExpression = Class(name="RDBSelectExpression")
RDBHostVariableReference = Class(name="RDBHostVariableReference")
astm_sastm_RDBInsertStatement = Class(name="astm::sastm::RDBInsertStatement")
RDBTableReference = Class(name="RDBTableReference")
astm_sastm_RDBUniqueKey = Class(name="astm::sastm::RDBUniqueKey")
astm_sastm_RDBModifyStatement = Class(name="astm::sastm::RDBModifyStatement", is_abstract=True)
astm_sastm_RDBUpdateStatement = Class(name="astm::sastm::RDBUpdateStatement")
RDBModifyStatement = Class(name="RDBModifyStatement")
astm_sastm_RDBCursorStatement = Class(name="astm::sastm::RDBCursorStatement", is_abstract=True)
astm_sastm_RDBFetchCursorStatement = Class(name="astm::sastm::RDBFetchCursorStatement")
astm_sastm_RDBHostVariableReference = Class(name="astm::sastm::RDBHostVariableReference")
astm_sastm_RDBSelectExpression = Class(name="astm::sastm::RDBSelectExpression")
astm_sastm_RDBOpenCursorStatement = Class(name="astm::sastm::RDBOpenCursorStatement")
RDBCursorStatement = Class(name="RDBCursorStatement")
astm_sastm_RDBTableReference = Class(name="astm::sastm::RDBTableReference")
astm_sastm_RDBTableAlias = Class(name="astm::sastm::RDBTableAlias")
astm_sastm_RDBColumnReference = Class(name="astm::sastm::RDBColumnReference")
astm_sastm_RDBDataBaseType = Class(name="astm::sastm::RDBDataBaseType")
astm_sastm_RDBUserType = Class(name="astm::sastm::RDBUserType")
astm_sastm_RDBCursorType = Class(name="astm::sastm::RDBCursorType")
astm_sastm_RDBColumnType = Class(name="astm::sastm::RDBColumnType", is_abstract=True)
astm_sastm_RDBInteger = Class(name="astm::sastm::RDBInteger")
astm_sastm_RDBInt = Class(name="astm::sastm::RDBInt")
astm_sastm_RDBReal = Class(name="astm::sastm::RDBReal")
astm_sastm_RDBFloat = Class(name="astm::sastm::RDBFloat")
astm_sastm_RDBDecimal = Class(name="astm::sastm::RDBDecimal")
astm_sastm_RDBNumber = Class(name="astm::sastm::RDBNumber")
astm_sastm_RDBLong = Class(name="astm::sastm::RDBLong")
astm_sastm_RDBChar = Class(name="astm::sastm::RDBChar")
astm_sastm_RDBVarchar = Class(name="astm::sastm::RDBVarchar")
astm_sastm_RDBString = Class(name="astm::sastm::RDBString")
astm_sastm_RDBRaw = Class(name="astm::sastm::RDBRaw")
astm_sastm_RDBDate = Class(name="astm::sastm::RDBDate")
astm_sastm_RDBTableSpaceType = Class(name="astm::sastm::RDBTableSpaceType")
astm_sastm_RDBTableType = Class(name="astm::sastm::RDBTableType")
astm_sastm_RDBViewType = Class(name="astm::sastm::RDBViewType")
astm_sastm_RDBClob = Class(name="astm::sastm::RDBClob")
astm_sastm_RDBNClob = Class(name="astm::sastm::RDBNClob")
astm_sastm_RDBBFile = Class(name="astm::sastm::RDBBFile")
astm_sastm_RDBDeleteStatement = Class(name="astm::sastm::RDBDeleteStatement")
astm_sastm_RDBCloseCursorStatement = Class(name="astm::sastm::RDBCloseCursorStatement")
astm_sastm_RDBHostVariableExpression = Class(name="astm::sastm::RDBHostVariableExpression")
astm_sastm_RDBTimestamp = Class(name="astm::sastm::RDBTimestamp")
astm_sastm_RDBRowid = Class(name="astm::sastm::RDBRowid")
astm_sastm_RDBBoolean = Class(name="astm::sastm::RDBBoolean")
astm_sastm_RDBBlob = Class(name="astm::sastm::RDBBlob")

# astm_gastm_SourceLocation class attributes and methods
astm_gastm_SourceLocation_startLine: Property = Property(name="startLine", type=IntegerType)
astm_gastm_SourceLocation_startColumn: Property = Property(name="startColumn", type=IntegerType)
astm_gastm_SourceLocation_endLine: Property = Property(name="endLine", type=IntegerType)
astm_gastm_SourceLocation_endColumn: Property = Property(name="endColumn", type=IntegerType)
astm_gastm_SourceLocation.attributes={astm_gastm_SourceLocation_endColumn, astm_gastm_SourceLocation_startColumn, astm_gastm_SourceLocation_endLine, astm_gastm_SourceLocation_startLine}

# astm_gastm_GASTMObject class attributes and methods

# astm_gastm_GASTMSourceObject class attributes and methods

# astm_gastm_GASTMSemanticObject class attributes and methods

# astm_gastm_OtherSyntaxObject class attributes and methods

# astm_gastm_StorageSpecification class attributes and methods

# astm_gastm_DataType class attributes and methods

# astm_gastm_AccessKind class attributes and methods

# astm_gastm_UnaryOperator class attributes and methods

# astm_gastm_BinaryOperator class attributes and methods

# astm_gastm_ActualParameter class attributes and methods

# astm_gastm_SourceFile class attributes and methods
astm_gastm_SourceFile_pathName: Property = Property(name="pathName", type=StringType)
astm_gastm_SourceFile.attributes={astm_gastm_SourceFile_pathName}

# GASTMSourceObject class attributes and methods

# SourceLocation class attributes and methods

# PreprocessorElement class attributes and methods

# AnnotationExpression class attributes and methods

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

# astm_gastm_Definition class attributes and methods

# DeclarationOrDefinition class attributes and methods

# Name class attributes and methods

# TypeReference class attributes and methods

# astm_gastm_CompilationUnit class attributes and methods
astm_gastm_CompilationUnit_language: Property = Property(name="language", type=StringType)
astm_gastm_CompilationUnit.attributes={astm_gastm_CompilationUnit_language}

# OtherSyntaxObject class attributes and methods

# ProgramScope class attributes and methods

# astm_gastm_Name class attributes and methods
astm_gastm_Name_nameString: Property = Property(name="nameString", type=StringType)
astm_gastm_Name.attributes={astm_gastm_Name_nameString}

# astm_gastm_DeclarationOrDefinition class attributes and methods
astm_gastm_DeclarationOrDefinition_isRegister: Property = Property(name="isRegister", type=BooleanType)
astm_gastm_DeclarationOrDefinition_linkageSpecifier: Property = Property(name="linkageSpecifier", type=StringType)
astm_gastm_DeclarationOrDefinition.attributes={astm_gastm_DeclarationOrDefinition_isRegister, astm_gastm_DeclarationOrDefinition_linkageSpecifier}

# FormalParameterDefinition class attributes and methods

# Statement class attributes and methods

# astm_gastm_Declaration class attributes and methods

# Definition class attributes and methods

# astm_gastm_FunctionDeclaration class attributes and methods

# Declaration class attributes and methods

# FormalParameterDeclaration class attributes and methods

# FunctionMemberAttributes class attributes and methods

# astm_gastm_VariableDeclaration class attributes and methods
astm_gastm_VariableDeclaration_isMutable: Property = Property(name="isMutable", type=BooleanType)
astm_gastm_VariableDeclaration.attributes={astm_gastm_VariableDeclaration_isMutable}

# astm_gastm_FunctionDefinition class attributes and methods

# astm_gastm_DataDefinition class attributes and methods
astm_gastm_DataDefinition_isMutable: Property = Property(name="isMutable", type=BooleanType)
astm_gastm_DataDefinition.attributes={astm_gastm_DataDefinition_isMutable}

# Expression class attributes and methods

# astm_gastm_BitFieldDefinition class attributes and methods

# DataDefinition class attributes and methods

# FunctionScope class attributes and methods

# astm_gastm_FunctionMemberAttributes class attributes and methods
astm_gastm_FunctionMemberAttributes_isFriend: Property = Property(name="isFriend", type=BooleanType)
astm_gastm_FunctionMemberAttributes_isInline: Property = Property(name="isInline", type=BooleanType)
astm_gastm_FunctionMemberAttributes_isThisConst: Property = Property(name="isThisConst", type=BooleanType)
astm_gastm_FunctionMemberAttributes.attributes={astm_gastm_FunctionMemberAttributes_isThisConst, astm_gastm_FunctionMemberAttributes_isFriend, astm_gastm_FunctionMemberAttributes_isInline}

# VirtualSpecification class attributes and methods

# astm_gastm_EntryDefinition class attributes and methods

# NameSpaceType class attributes and methods

# astm_gastm_EnumLiteralDefinition class attributes and methods

# astm_gastm_TypeDefinition class attributes and methods

# astm_gastm_NamedTypeDefinition class attributes and methods

# TypeDefinition class attributes and methods

# NamedType class attributes and methods

# astm_gastm_AggregateTypeDefinition class attributes and methods

# AggregateType class attributes and methods

# astm_gastm_NameSpaceDefinition class attributes and methods

# astm_gastm_Type class attributes and methods
astm_gastm_Type_isConst: Property = Property(name="isConst", type=BooleanType)
astm_gastm_Type_isVolatile: Property = Property(name="isVolatile", type=BooleanType)
astm_gastm_Type.attributes={astm_gastm_Type_isConst, astm_gastm_Type_isVolatile}

# GASTMSyntaxObject class attributes and methods

# astm_gastm_PrimitiveType class attributes and methods
astm_gastm_PrimitiveType_isSigned: Property = Property(name="isSigned", type=BooleanType)
astm_gastm_PrimitiveType.attributes={astm_gastm_PrimitiveType_isSigned}

# astm_gastm_LabelDefinition class attributes and methods

# LabelType class attributes and methods

# astm_gastm_IncludeUnit class attributes and methods

# astm_gastm_MacroCall class attributes and methods

# MacroDefinition class attributes and methods

# astm_gastm_MacroDefinition class attributes and methods
astm_gastm_MacroDefinition_macroName: Property = Property(name="macroName", type=StringType)
astm_gastm_MacroDefinition_body: Property = Property(name="body", type=StringType)
astm_gastm_MacroDefinition.attributes={astm_gastm_MacroDefinition_body, astm_gastm_MacroDefinition_macroName}

# astm_gastm_Comment class attributes and methods
astm_gastm_Comment_text: Property = Property(name="text", type=StringType)
astm_gastm_Comment.attributes={astm_gastm_Comment_text}

# astm_gastm_Dimension class attributes and methods

# DataType class attributes and methods

# astm_gastm_EnumType class attributes and methods

# EnumLiteralDefinition class attributes and methods

# astm_gastm_ConstructedType class attributes and methods

# astm_gastm_AggregateType class attributes and methods

# AggregateScope class attributes and methods

# astm_gastm_ArrayType class attributes and methods

# ConstructedType class attributes and methods

# Dimension class attributes and methods

# astm_gastm_DerivesFrom class attributes and methods
astm_gastm_DerivesFrom_isVirtual: Property = Property(name="isVirtual", type=BooleanType)
astm_gastm_DerivesFrom.attributes={astm_gastm_DerivesFrom_isVirtual}

# astm_gastm_FunctionType class attributes and methods

# Type class attributes and methods

# FormalParameterType class attributes and methods

# astm_gastm_FormalParameterType class attributes and methods

# astm_gastm_NamedType class attributes and methods

# astm_gastm_ClassType class attributes and methods

# DerivesFrom class attributes and methods

# astm_gastm_DeclarationOrDefinitionStatement class attributes and methods

# astm_gastm_UnnamedTypeReference class attributes and methods

# astm_gastm_NamedTypeReference class attributes and methods

# astm_gastm_DeleteStatement class attributes and methods

# astm_gastm_ExpressionStatement class attributes and methods

# astm_gastm_JumpStatement class attributes and methods

# astm_gastm_BreakStatement class attributes and methods

# LabelAccess class attributes and methods

# astm_gastm_ContinueStatement class attributes and methods

# astm_gastm_LabeledStatement class attributes and methods

# LabelDefinition class attributes and methods

# SwitchCase class attributes and methods

# astm_gastm_BlockStatement class attributes and methods

# astm_gastm_SwitchCase class attributes and methods

# BlockScope class attributes and methods

# astm_gastm_EmptyStatement class attributes and methods

# astm_gastm_IfStatement class attributes and methods

# astm_gastm_SwitchStatement class attributes and methods

# astm_gastm_ForStatement class attributes and methods

# LoopStatement class attributes and methods

# astm_gastm_CaseBlock class attributes and methods

# astm_gastm_ReturnStatement class attributes and methods

# astm_gastm_LoopStatement class attributes and methods

# astm_gastm_TypesCatchBlock class attributes and methods

# astm_gastm_TryStatement class attributes and methods

# CatchBlock class attributes and methods

# astm_gastm_CatchBlock class attributes and methods

# astm_gastm_ArrayAccess class attributes and methods

# astm_gastm_VariableCatchBlock class attributes and methods

# astm_gastm_ThrowStatement class attributes and methods

# astm_gastm_Expression class attributes and methods

# astm_gastm_NameReference class attributes and methods

# astm_gastm_CastExpression class attributes and methods

# astm_gastm_QualifiedIdentifierReference class attributes and methods

# NameReference class attributes and methods

# IdentifierReference class attributes and methods

# astm_gastm_TypeQualifiedIdentifierReference class attributes and methods

# astm_gastm_Literal class attributes and methods
astm_gastm_Literal_value: Property = Property(name="value", type=StringType)
astm_gastm_Literal.attributes={astm_gastm_Literal_value}

# astm_gastm_UnaryExpression class attributes and methods

# astm_gastm_BinaryExpression class attributes and methods

# astm_gastm_OperatorAssign class attributes and methods

# BinaryOperator class attributes and methods

# astm_gastm_ConditionalExpression class attributes and methods

# astm_gastm_RangeExpression class attributes and methods

# astm_gastm_FunctionCallExpression class attributes and methods

# ActualParameter class attributes and methods

# astm_gastm_ActualParameterExpression class attributes and methods

# astm_gastm_NewExpression class attributes and methods

# astm_gastm_GlobalScope class attributes and methods

# astm_gastm_PreprocessorElement class attributes and methods

# astm_gastm_LabelAccess class attributes and methods

# astm_gastm_AnnotationExpression class attributes and methods

# StorageSpecification class attributes and methods

# astm_gastm_FunctionPersistent class attributes and methods

# astm_gastm_FileLocal class attributes and methods

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

# astm_gastm_FormalParameterDefinition class attributes and methods

# astm_gastm_VirtualSpecification class attributes and methods

# astm_gastm_FormalParameterDeclaration class attributes and methods

# astm_gastm_VariableDefinition class attributes and methods

# astm_gastm_FunctionMemberAttribute class attributes and methods

# astm_gastm_External class attributes and methods

# astm_gastm_String class attributes and methods

# astm_gastm_Boolean class attributes and methods

# astm_gastm_WideCharacter class attributes and methods

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

# astm_gastm_ForCheckBeforeStatement class attributes and methods

# ForStatement class attributes and methods

# astm_gastm_ForCheckAfterStatement class attributes and methods

# astm_gastm_CollectionType class attributes and methods

# astm_gastm_PointerType class attributes and methods

# astm_gastm_ReferenceType class attributes and methods

# astm_gastm_RangeType class attributes and methods

# astm_gastm_StructureType class attributes and methods

# astm_gastm_UnionType class attributes and methods

# astm_gastm_AnnotationType class attributes and methods

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

# astm_gastm_Decrement class attributes and methods

# astm_gastm_PostIncrement class attributes and methods

# astm_gastm_PostDecrement class attributes and methods

# astm_gastm_AggregateExpression class attributes and methods

# astm_gastm_QualifiedOverPointer class attributes and methods

# QualifiedIdentifierReference class attributes and methods

# astm_gastm_QualifiedOverData class attributes and methods

# astm_gastm_IntegerlLiteral class attributes and methods

# Literal class attributes and methods

# astm_gastm_StringLiteral class attributes and methods

# astm_gastm_CharLiteral class attributes and methods

# astm_gastm_RealLiteral class attributes and methods

# astm_gastm_BooleanLiteral class attributes and methods

# astm_gastm_BitLiteral class attributes and methods

# astm_gastm_UnaryPlus class attributes and methods

# UnaryOperator class attributes and methods

# astm_gastm_Negate class attributes and methods

# astm_gastm_Not class attributes and methods

# astm_gastm_BitNot class attributes and methods

# astm_gastm_AddressOf class attributes and methods

# astm_gastm_Deref class attributes and methods

# astm_gastm_Increment class attributes and methods

# astm_gastm_BitXor class attributes and methods

# astm_gastm_BitLeftShift class attributes and methods

# astm_gastm_BitRightShift class attributes and methods

# astm_gastm_Add class attributes and methods

# astm_gastm_Assign class attributes and methods

# astm_gastm_Subtract class attributes and methods

# astm_gastm_MissingActualParameter class attributes and methods

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

# astm_sastm_RDBDatabaseDefinition class attributes and methods

# RDBTableSpaceReference class attributes and methods

# astm_sastm_RDBTableSpaceReference class attributes and methods

# astm_sastm_RDBUserDefinition class attributes and methods

# astm_gastm_ByValueActualParameterExpression class attributes and methods

# ActualParameterExpression class attributes and methods

# NameSpaceDefinition class attributes and methods

# astm_gastm_ByReferenceActualParameterExpression class attributes and methods

# astm_gastm_SpecificTriggerDefinition class attributes and methods

# astm_sastm_RDBTableSpaceDefinition class attributes and methods

# astm_sastm_RDBTableDefinition class attributes and methods

# astm_gastm_SpecificLessEqual class attributes and methods

# RDBColumnReference class attributes and methods

# astm_gastm_SpecificGreaterEqual class attributes and methods

# astm_gastm_SpecificIn class attributes and methods

# astm_gastm_SpecificLike class attributes and methods

# astm_gastm_SpecificConcatString class attributes and methods

# astm_gastm_SpecificSelectStatement class attributes and methods

# RDBTrigger class attributes and methods

# astm_sastm_RDBColumnDefinition class attributes and methods
astm_sastm_RDBColumnDefinition_NotNull: Property = Property(name="NotNull", type=BooleanType)
astm_sastm_RDBColumnDefinition.attributes={astm_sastm_RDBColumnDefinition_NotNull}

# RDBColumnType class attributes and methods

# astm_sastm_RDBViewDefinition class attributes and methods

# AggregateTypeDefinition class attributes and methods

# RDBColumnDefinition class attributes and methods

# RDBConstraint class attributes and methods

# RDBIndex class attributes and methods

# astm_sastm_RDBCursorDefinition class attributes and methods

# astm_sastm_RDBIndex class attributes and methods
astm_sastm_RDBIndex_NotNull: Property = Property(name="NotNull", type=BooleanType)
astm_sastm_RDBIndex_IsUnique: Property = Property(name="IsUnique", type=BooleanType)
astm_sastm_RDBIndex.attributes={astm_sastm_RDBIndex_NotNull, astm_sastm_RDBIndex_IsUnique}

# astm_sastm_RDBTrigger class attributes and methods

# gastm_OtherSyntaxObject class attributes and methods

# gastm_Definition class attributes and methods

# astm_sastm_RDBConstraint class attributes and methods

# astm_sastm_RDBCheckConstraint class attributes and methods
astm_sastm_RDBCheckConstraint_RDBConstraintText: Property = Property(name="RDBConstraintText", type=StringType)
astm_sastm_RDBCheckConstraint_RDBConstraintType: Property = Property(name="RDBConstraintType", type=StringType)
astm_sastm_RDBCheckConstraint.attributes={astm_sastm_RDBCheckConstraint_RDBConstraintType, astm_sastm_RDBCheckConstraint_RDBConstraintText}

# astm_sastm_RDBRefIntegrity class attributes and methods

# astm_sastm_RDBIndexColumn class attributes and methods
astm_sastm_RDBIndexColumn_AscendingOrDescending: Property = Property(name="AscendingOrDescending", type=StringType)
astm_sastm_RDBIndexColumn.attributes={astm_sastm_RDBIndexColumn_AscendingOrDescending}

# IncludeUnit class attributes and methods

# astm_sastm_RDBConnectStatement class attributes and methods

# NamedTypeDefinition class attributes and methods

# astm_sastm_RDBSelectStatement class attributes and methods

# RDBSelectExpression class attributes and methods

# RDBHostVariableReference class attributes and methods

# astm_sastm_RDBInsertStatement class attributes and methods

# RDBTableReference class attributes and methods

# astm_sastm_RDBUniqueKey class attributes and methods

# astm_sastm_RDBModifyStatement class attributes and methods

# astm_sastm_RDBUpdateStatement class attributes and methods

# RDBModifyStatement class attributes and methods

# astm_sastm_RDBCursorStatement class attributes and methods

# astm_sastm_RDBFetchCursorStatement class attributes and methods

# astm_sastm_RDBHostVariableReference class attributes and methods

# astm_sastm_RDBSelectExpression class attributes and methods

# astm_sastm_RDBOpenCursorStatement class attributes and methods

# RDBCursorStatement class attributes and methods

# astm_sastm_RDBTableReference class attributes and methods

# astm_sastm_RDBTableAlias class attributes and methods

# astm_sastm_RDBColumnReference class attributes and methods

# astm_sastm_RDBDataBaseType class attributes and methods

# astm_sastm_RDBUserType class attributes and methods

# astm_sastm_RDBCursorType class attributes and methods

# astm_sastm_RDBColumnType class attributes and methods

# astm_sastm_RDBInteger class attributes and methods

# astm_sastm_RDBInt class attributes and methods

# astm_sastm_RDBReal class attributes and methods

# astm_sastm_RDBFloat class attributes and methods

# astm_sastm_RDBDecimal class attributes and methods

# astm_sastm_RDBNumber class attributes and methods

# astm_sastm_RDBLong class attributes and methods

# astm_sastm_RDBChar class attributes and methods

# astm_sastm_RDBVarchar class attributes and methods

# astm_sastm_RDBString class attributes and methods

# astm_sastm_RDBRaw class attributes and methods

# astm_sastm_RDBDate class attributes and methods

# astm_sastm_RDBTableSpaceType class attributes and methods

# astm_sastm_RDBTableType class attributes and methods

# astm_sastm_RDBViewType class attributes and methods

# astm_sastm_RDBClob class attributes and methods

# astm_sastm_RDBNClob class attributes and methods

# astm_sastm_RDBBFile class attributes and methods

# astm_sastm_RDBDeleteStatement class attributes and methods

# astm_sastm_RDBCloseCursorStatement class attributes and methods

# astm_sastm_RDBHostVariableExpression class attributes and methods

# astm_sastm_RDBTimestamp class attributes and methods

# astm_sastm_RDBRowid class attributes and methods

# astm_sastm_RDBBoolean class attributes and methods

# astm_sastm_RDBBlob class attributes and methods

# Relationships
locationInfo7: BinaryAssociation = BinaryAssociation(
    name="locationInfo7",
    ends={
        Property(name="SourceLocation", type=astm_gastm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_GASTMSyntaxObject", type=SourceLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
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
fragments12: BinaryAssociation = BinaryAssociation(
    name="fragments12",
    ends={
        Property(name="DefinitionObject13", type=astm_gastm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CompilationUnit", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
returnType33: BinaryAssociation = BinaryAssociation(
    name="returnType33",
    ends={
        Property(name="TypeReference34", type=astm_gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDefinition", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters35: BinaryAssociation = BinaryAssociation(
    name="formalParameters35",
    ends={
        Property(name="FormalParameterDefinition", type=astm_gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDefinition36", type=FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
initialValue50: BinaryAssociation = BinaryAssociation(
    name="initialValue50",
    ends={
        Property(name="Expression", type=astm_gastm_DataDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DataDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body37: BinaryAssociation = BinaryAssociation(
    name="body37",
    ends={
        Property(name="Statement", type=astm_gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDefinition38", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes39: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes39",
    ends={
        Property(name="FunctionMemberAttributes41", type=astm_gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDefinition40", type=FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opensScope42: BinaryAssociation = BinaryAssociation(
    name="opensScope42",
    ends={
        Property(name="FunctionScope", type=astm_gastm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionDefinition43", type=FunctionScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
virtualSpecifier44: BinaryAssociation = BinaryAssociation(
    name="virtualSpecifier44",
    ends={
        Property(name="VirtualSpecification", type=astm_gastm_FunctionMemberAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionMemberAttributes", type=VirtualSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters45: BinaryAssociation = BinaryAssociation(
    name="formalParameters45",
    ends={
        Property(name="FormalParameterDefinition46", type=astm_gastm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_EntryDefinition", type=FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body47: BinaryAssociation = BinaryAssociation(
    name="body47",
    ends={
        Property(name="Statement49", type=astm_gastm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_EntryDefinition48", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameSpace59: BinaryAssociation = BinaryAssociation(
    name="nameSpace59",
    ends={
        Property(name="Name60", type=astm_gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NameSpaceDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body61: BinaryAssociation = BinaryAssociation(
    name="body61",
    ends={
        Property(name="DefinitionObject63", type=astm_gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NameSpaceDefinition62", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameSpaceType64: BinaryAssociation = BinaryAssociation(
    name="nameSpaceType64",
    ends={
        Property(name="NameSpaceType", type=astm_gastm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NameSpaceDefinition65", type=NameSpaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bitFieldSize51: BinaryAssociation = BinaryAssociation(
    name="bitFieldSize51",
    ends={
        Property(name="Expression52", type=astm_gastm_BitFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BitFieldDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value53: BinaryAssociation = BinaryAssociation(
    name="value53",
    ends={
        Property(name="Expression54", type=astm_gastm_EnumLiteralDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_EnumLiteralDefinition", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name55: BinaryAssociation = BinaryAssociation(
    name="name55",
    ends={
        Property(name="Name56", type=astm_gastm_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TypeDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType57: BinaryAssociation = BinaryAssociation(
    name="definitionType57",
    ends={
        Property(name="NamedType", type=astm_gastm_NamedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NamedTypeDefinition", type=NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType58: BinaryAssociation = BinaryAssociation(
    name="aggregateType58",
    ends={
        Property(name="AggregateType", type=astm_gastm_AggregateTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_AggregateTypeDefinition", type=AggregateType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelName66: BinaryAssociation = BinaryAssociation(
    name="labelName66",
    ends={
        Property(name="Name67", type=astm_gastm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabelDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelType68: BinaryAssociation = BinaryAssociation(
    name="labelType68",
    ends={
        Property(name="LabelType", type=astm_gastm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabelDefinition69", type=LabelType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file70: BinaryAssociation = BinaryAssociation(
    name="file70",
    ends={
        Property(name="SourceFile71", type=astm_gastm_IncludeUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_IncludeUnit", type=SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo72: BinaryAssociation = BinaryAssociation(
    name="refersTo72",
    ends={
        Property(name="MacroDefinition", type=astm_gastm_MacroCall, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_MacroCall", type=MacroDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ranks80: BinaryAssociation = BinaryAssociation(
    name="ranks80",
    ends={
        Property(name="astm_gastm_ArrayType", type=Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Dimension", type=astm_gastm_ArrayType, multiplicity=Multiplicity(1, 1))
    }
)
lowBound81: BinaryAssociation = BinaryAssociation(
    name="lowBound81",
    ends={
        Property(name="Expression82", type=astm_gastm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Dimension", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumLiterals73: BinaryAssociation = BinaryAssociation(
    name="enumLiterals73",
    ends={
        Property(name="EnumLiteralDefinition", type=astm_gastm_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_EnumType", type=EnumLiteralDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType74: BinaryAssociation = BinaryAssociation(
    name="baseType74",
    ends={
        Property(name="TypeReference75", type=astm_gastm_ConstructedType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ConstructedType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members76: BinaryAssociation = BinaryAssociation(
    name="members76",
    ends={
        Property(name="DefinitionObject77", type=astm_gastm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_AggregateType", type=DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope78: BinaryAssociation = BinaryAssociation(
    name="opensScope78",
    ends={
        Property(name="AggregateScope", type=astm_gastm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_AggregateType79", type=AggregateScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessKind94: BinaryAssociation = BinaryAssociation(
    name="accessKind94",
    ends={
        Property(name="OtherSyntaxObject95", type=astm_gastm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DerivesFrom", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
highBound83: BinaryAssociation = BinaryAssociation(
    name="highBound83",
    ends={
        Property(name="Expression85", type=astm_gastm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Dimension84", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType86: BinaryAssociation = BinaryAssociation(
    name="returnType86",
    ends={
        Property(name="TypeReference87", type=astm_gastm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterTypes88: BinaryAssociation = BinaryAssociation(
    name="parameterTypes88",
    ends={
        Property(name="FormalParameterType", type=astm_gastm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionType89", type=FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type90: BinaryAssociation = BinaryAssociation(
    name="type90",
    ends={
        Property(name="TypeReference91", type=astm_gastm_FormalParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FormalParameterType", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body92: BinaryAssociation = BinaryAssociation(
    name="body92",
    ends={
        Property(name="Type", type=astm_gastm_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NamedType", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivesFrom93: BinaryAssociation = BinaryAssociation(
    name="derivesFrom93",
    ends={
        Property(name="DerivesFrom", type=astm_gastm_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ClassType", type=DerivesFrom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declOrDefn107: BinaryAssociation = BinaryAssociation(
    name="declOrDefn107",
    ends={
        Property(name="DefinitionObject108", type=astm_gastm_DeclarationOrDefinitionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DeclarationOrDefinitionStatement", type=DefinitionObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className96: BinaryAssociation = BinaryAssociation(
    name="className96",
    ends={
        Property(name="NamedType98", type=astm_gastm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DerivesFrom97", type=NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type99: BinaryAssociation = BinaryAssociation(
    name="type99",
    ends={
        Property(name="Type100", type=astm_gastm_UnnamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_UnnamedTypeReference", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name101: BinaryAssociation = BinaryAssociation(
    name="name101",
    ends={
        Property(name="Name102", type=astm_gastm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NamedTypeReference", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="TypeDefinition", type=astm_gastm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NamedTypeReference104", type=TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
operand105: BinaryAssociation = BinaryAssociation(
    name="operand105",
    ends={
        Property(name="Expression106", type=astm_gastm_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_DeleteStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement117: BinaryAssociation = BinaryAssociation(
    name="statement117",
    ends={
        Property(name="Statement119", type=astm_gastm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabeledStatement118", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression109: BinaryAssociation = BinaryAssociation(
    name="expression109",
    ends={
        Property(name="Expression110", type=astm_gastm_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ExpressionStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target111: BinaryAssociation = BinaryAssociation(
    name="target111",
    ends={
        Property(name="Expression112", type=astm_gastm_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_JumpStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target113: BinaryAssociation = BinaryAssociation(
    name="target113",
    ends={
        Property(name="LabelAccess", type=astm_gastm_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BreakStatement", type=LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target114: BinaryAssociation = BinaryAssociation(
    name="target114",
    ends={
        Property(name="LabelAccess115", type=astm_gastm_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ContinueStatement", type=LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchExpression132: BinaryAssociation = BinaryAssociation(
    name="switchExpression132",
    ends={
        Property(name="Expression133", type=astm_gastm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_SwitchStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label116: BinaryAssociation = BinaryAssociation(
    name="label116",
    ends={
        Property(name="LabelDefinition", type=astm_gastm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabeledStatement", type=LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases134: BinaryAssociation = BinaryAssociation(
    name="cases134",
    ends={
        Property(name="SwitchCase", type=astm_gastm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_SwitchStatement135", type=SwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subStatements120: BinaryAssociation = BinaryAssociation(
    name="subStatements120",
    ends={
        Property(name="Statement121", type=astm_gastm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BlockStatement", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope122: BinaryAssociation = BinaryAssociation(
    name="opensScope122",
    ends={
        Property(name="BlockScope", type=astm_gastm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BlockStatement123", type=BlockScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition124: BinaryAssociation = BinaryAssociation(
    name="condition124",
    ends={
        Property(name="Expression125", type=astm_gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_IfStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBody126: BinaryAssociation = BinaryAssociation(
    name="thenBody126",
    ends={
        Property(name="Statement128", type=astm_gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_IfStatement127", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBody129: BinaryAssociation = BinaryAssociation(
    name="elseBody129",
    ends={
        Property(name="Statement131", type=astm_gastm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_IfStatement130", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initBody147: BinaryAssociation = BinaryAssociation(
    name="initBody147",
    ends={
        Property(name="Expression148", type=astm_gastm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ForStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body136: BinaryAssociation = BinaryAssociation(
    name="body136",
    ends={
        Property(name="Statement137", type=astm_gastm_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_SwitchCase", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caseExpressions138: BinaryAssociation = BinaryAssociation(
    name="caseExpressions138",
    ends={
        Property(name="Expression139", type=astm_gastm_CaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CaseBlock", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue140: BinaryAssociation = BinaryAssociation(
    name="returnValue140",
    ends={
        Property(name="Expression141", type=astm_gastm_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition142: BinaryAssociation = BinaryAssociation(
    name="condition142",
    ends={
        Property(name="Expression143", type=astm_gastm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LoopStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body144: BinaryAssociation = BinaryAssociation(
    name="body144",
    ends={
        Property(name="Statement146", type=astm_gastm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LoopStatement145", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions161: BinaryAssociation = BinaryAssociation(
    name="exceptions161",
    ends={
        Property(name="Type162", type=astm_gastm_TypesCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TypesCatchBlock", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterationBody149: BinaryAssociation = BinaryAssociation(
    name="iterationBody149",
    ends={
        Property(name="Expression151", type=astm_gastm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ForStatement150", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guardedStatement152: BinaryAssociation = BinaryAssociation(
    name="guardedStatement152",
    ends={
        Property(name="Statement153", type=astm_gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TryStatement", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchBlocks154: BinaryAssociation = BinaryAssociation(
    name="catchBlocks154",
    ends={
        Property(name="CatchBlock", type=astm_gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TryStatement155", type=CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalStatement156: BinaryAssociation = BinaryAssociation(
    name="finalStatement156",
    ends={
        Property(name="Statement158", type=astm_gastm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TryStatement157", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body159: BinaryAssociation = BinaryAssociation(
    name="body159",
    ends={
        Property(name="Statement160", type=astm_gastm_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CatchBlock", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayName173: BinaryAssociation = BinaryAssociation(
    name="arrayName173",
    ends={
        Property(name="Expression174", type=astm_gastm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ArrayAccess", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptionVariable163: BinaryAssociation = BinaryAssociation(
    name="exceptionVariable163",
    ends={
        Property(name="DataDefinition", type=astm_gastm_VariableCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_VariableCatchBlock", type=DataDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception164: BinaryAssociation = BinaryAssociation(
    name="exception164",
    ends={
        Property(name="Expression165", type=astm_gastm_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ThrowStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionType166: BinaryAssociation = BinaryAssociation(
    name="expressionType166",
    ends={
        Property(name="TypeReference167", type=astm_gastm_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_Expression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name168: BinaryAssociation = BinaryAssociation(
    name="name168",
    ends={
        Property(name="Name169", type=astm_gastm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NameReference", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo170: BinaryAssociation = BinaryAssociation(
    name="refersTo170",
    ends={
        Property(name="DefinitionObject172", type=astm_gastm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NameReference171", type=DefinitionObject, multiplicity=Multiplicity(0, 1))
    }
)
castType187: BinaryAssociation = BinaryAssociation(
    name="castType187",
    ends={
        Property(name="TypeReference188", type=astm_gastm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CastExpression", type=TypeReference, multiplicity=Multiplicity(0, 1))
    }
)
subscripts175: BinaryAssociation = BinaryAssociation(
    name="subscripts175",
    ends={
        Property(name="Expression177", type=astm_gastm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ArrayAccess176", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifiers178: BinaryAssociation = BinaryAssociation(
    name="qualifiers178",
    ends={
        Property(name="Expression179", type=astm_gastm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_QualifiedIdentifierReference", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member180: BinaryAssociation = BinaryAssociation(
    name="member180",
    ends={
        Property(name="IdentifierReference", type=astm_gastm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_QualifiedIdentifierReference181", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType182: BinaryAssociation = BinaryAssociation(
    name="aggregateType182",
    ends={
        Property(name="TypeReference183", type=astm_gastm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TypeQualifiedIdentifierReference", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member184: BinaryAssociation = BinaryAssociation(
    name="member184",
    ends={
        Property(name="IdentifierReference186", type=astm_gastm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_TypeQualifiedIdentifierReference185", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand202: BinaryAssociation = BinaryAssociation(
    name="rightOperand202",
    ends={
        Property(name="Expression204", type=astm_gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BinaryExpression203", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression189: BinaryAssociation = BinaryAssociation(
    name="expression189",
    ends={
        Property(name="Expression191", type=astm_gastm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_CastExpression190", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator192: BinaryAssociation = BinaryAssociation(
    name="operator192",
    ends={
        Property(name="OtherSyntaxObject193", type=astm_gastm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_UnaryExpression", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand194: BinaryAssociation = BinaryAssociation(
    name="operand194",
    ends={
        Property(name="Expression196", type=astm_gastm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_UnaryExpression195", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator197: BinaryAssociation = BinaryAssociation(
    name="operator197",
    ends={
        Property(name="OtherSyntaxObject198", type=astm_gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BinaryExpression", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromExpression215: BinaryAssociation = BinaryAssociation(
    name="fromExpression215",
    ends={
        Property(name="Expression216", type=astm_gastm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_RangeExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand199: BinaryAssociation = BinaryAssociation(
    name="leftOperand199",
    ends={
        Property(name="Expression201", type=astm_gastm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_BinaryExpression200", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator205: BinaryAssociation = BinaryAssociation(
    name="operator205",
    ends={
        Property(name="OtherSyntaxObject206", type=astm_gastm_OperatorAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_OperatorAssign", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition207: BinaryAssociation = BinaryAssociation(
    name="condition207",
    ends={
        Property(name="Expression208", type=astm_gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ConditionalExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onTrueOperand209: BinaryAssociation = BinaryAssociation(
    name="onTrueOperand209",
    ends={
        Property(name="Expression211", type=astm_gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ConditionalExpression210", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onFalseOperand212: BinaryAssociation = BinaryAssociation(
    name="onFalseOperand212",
    ends={
        Property(name="Expression214", type=astm_gastm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ConditionalExpression213", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newType226: BinaryAssociation = BinaryAssociation(
    name="newType226",
    ends={
        Property(name="TypeReference227", type=astm_gastm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NewExpression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toExpression217: BinaryAssociation = BinaryAssociation(
    name="toExpression217",
    ends={
        Property(name="Expression219", type=astm_gastm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_RangeExpression218", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
calledFunction220: BinaryAssociation = BinaryAssociation(
    name="calledFunction220",
    ends={
        Property(name="Expression221", type=astm_gastm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionCallExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams222: BinaryAssociation = BinaryAssociation(
    name="actualParams222",
    ends={
        Property(name="ActualParameter", type=astm_gastm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_FunctionCallExpression223", type=ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value224: BinaryAssociation = BinaryAssociation(
    name="value224",
    ends={
        Property(name="Expression225", type=astm_gastm_ActualParameterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_ActualParameterExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams228: BinaryAssociation = BinaryAssociation(
    name="actualParams228",
    ends={
        Property(name="OtherSyntaxObject230", type=astm_gastm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_NewExpression229", type=OtherSyntaxObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name231: BinaryAssociation = BinaryAssociation(
    name="name231",
    ends={
        Property(name="Name232", type=astm_gastm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabelAccess", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition233: BinaryAssociation = BinaryAssociation(
    name="definition233",
    ends={
        Property(name="LabelDefinition235", type=astm_gastm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_LabelAccess234", type=LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationType236: BinaryAssociation = BinaryAssociation(
    name="annotationType236",
    ends={
        Property(name="TypeReference237", type=astm_gastm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_AnnotationExpression", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberValues238: BinaryAssociation = BinaryAssociation(
    name="memberValues238",
    ends={
        Property(name="Expression240", type=astm_gastm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_AnnotationExpression239", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TableSpace243: BinaryAssociation = BinaryAssociation(
    name="TableSpace243",
    ends={
        Property(name="RDBTableSpaceReference", type=astm_sastm_RDBDatabaseDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBDatabaseDefinition", type=RDBTableSpaceReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Owns244: BinaryAssociation = BinaryAssociation(
    name="Owns244",
    ends={
        Property(name="NameSpaceDefinition", type=astm_sastm_RDBUserDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBUserDefinition", type=NameSpaceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body241: BinaryAssociation = BinaryAssociation(
    name="body241",
    ends={
        Property(name="Statement242", type=astm_gastm_SpecificTriggerDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_gastm_SpecificTriggerDefinition", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Table245: BinaryAssociation = BinaryAssociation(
    name="Table245",
    ends={
        Property(name="NameSpaceDefinition246", type=astm_sastm_RDBTableSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBTableSpaceDefinition", type=NameSpaceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PrimKey247: BinaryAssociation = BinaryAssociation(
    name="PrimKey247",
    ends={
        Property(name="RDBColumnReference", type=astm_sastm_RDBTableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBTableDefinition", type=RDBColumnReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Trigger254: BinaryAssociation = BinaryAssociation(
    name="Trigger254",
    ends={
        Property(name="RDBTrigger", type=astm_sastm_RDBTableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBTableDefinition255", type=RDBTrigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name256: BinaryAssociation = BinaryAssociation(
    name="name256",
    ends={
        Property(name="Name257", type=astm_sastm_RDBColumnDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBColumnDefinition", type=Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type258: BinaryAssociation = BinaryAssociation(
    name="type258",
    ends={
        Property(name="RDBColumnType", type=astm_sastm_RDBColumnDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBColumnDefinition259", type=RDBColumnType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DefinedBy260: BinaryAssociation = BinaryAssociation(
    name="DefinedBy260",
    ends={
        Property(name="AggregateTypeDefinition", type=astm_sastm_RDBViewDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBViewDefinition", type=AggregateTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Column248: BinaryAssociation = BinaryAssociation(
    name="Column248",
    ends={
        Property(name="RDBColumnDefinition", type=astm_sastm_RDBTableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBTableDefinition249", type=RDBColumnDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Constraint250: BinaryAssociation = BinaryAssociation(
    name="Constraint250",
    ends={
        Property(name="RDBConstraint", type=astm_sastm_RDBTableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBTableDefinition251", type=RDBConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Index252: BinaryAssociation = BinaryAssociation(
    name="Index252",
    ends={
        Property(name="RDBIndex", type=astm_sastm_RDBTableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBTableDefinition253", type=RDBIndex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
SelectExpression261: BinaryAssociation = BinaryAssociation(
    name="SelectExpression261",
    ends={
        Property(name="AggregateTypeDefinition262", type=astm_sastm_RDBCursorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBCursorDefinition", type=AggregateTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Column265: BinaryAssociation = BinaryAssociation(
    name="Column265",
    ends={
        Property(name="IncludeUnit", type=astm_sastm_RDBIndexColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBIndexColumn", type=IncludeUnit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body266: BinaryAssociation = BinaryAssociation(
    name="body266",
    ends={
        Property(name="Statement267", type=astm_sastm_RDBTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBTrigger", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ForeignKey268: BinaryAssociation = BinaryAssociation(
    name="ForeignKey268",
    ends={
        Property(name="RDBColumnReference269", type=astm_sastm_RDBRefIntegrity, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBRefIntegrity", type=RDBColumnReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IndexColumn263: BinaryAssociation = BinaryAssociation(
    name="IndexColumn263",
    ends={
        Property(name="Name264", type=astm_sastm_RDBIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBIndex", type=Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Column275: BinaryAssociation = BinaryAssociation(
    name="Column275",
    ends={
        Property(name="RDBColumnReference276", type=astm_sastm_RDBUniqueKey, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBUniqueKey", type=RDBColumnReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ConnectString277: BinaryAssociation = BinaryAssociation(
    name="ConnectString277",
    ends={
        Property(name="NamedTypeDefinition", type=astm_sastm_RDBConnectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBConnectStatement", type=NamedTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SelectExpression278: BinaryAssociation = BinaryAssociation(
    name="SelectExpression278",
    ends={
        Property(name="RDBSelectExpression", type=astm_sastm_RDBSelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBSelectStatement", type=RDBSelectExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IntoVariable279: BinaryAssociation = BinaryAssociation(
    name="IntoVariable279",
    ends={
        Property(name="RDBHostVariableReference", type=astm_sastm_RDBSelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBSelectStatement280", type=RDBHostVariableReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntoTable281: BinaryAssociation = BinaryAssociation(
    name="IntoTable281",
    ends={
        Property(name="NameSpaceDefinition282", type=astm_sastm_RDBInsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBInsertStatement", type=NameSpaceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ParentKey270: BinaryAssociation = BinaryAssociation(
    name="ParentKey270",
    ends={
        Property(name="RDBColumnReference272", type=astm_sastm_RDBRefIntegrity, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBRefIntegrity271", type=RDBColumnReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ParentTable273: BinaryAssociation = BinaryAssociation(
    name="ParentTable273",
    ends={
        Property(name="RDBTableReference", type=astm_sastm_RDBRefIntegrity, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBRefIntegrity274", type=RDBTableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Table289: BinaryAssociation = BinaryAssociation(
    name="Table289",
    ends={
        Property(name="NameSpaceDefinition290", type=astm_sastm_RDBModifyStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBModifyStatement", type=NameSpaceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Where291: BinaryAssociation = BinaryAssociation(
    name="Where291",
    ends={
        Property(name="Expression293", type=astm_sastm_RDBModifyStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBModifyStatement292", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Values294: BinaryAssociation = BinaryAssociation(
    name="Values294",
    ends={
        Property(name="Expression295", type=astm_sastm_RDBUpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBUpdateStatement", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Columns283: BinaryAssociation = BinaryAssociation(
    name="Columns283",
    ends={
        Property(name="IncludeUnit285", type=astm_sastm_RDBInsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBInsertStatement284", type=IncludeUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Values286: BinaryAssociation = BinaryAssociation(
    name="Values286",
    ends={
        Property(name="Expression288", type=astm_sastm_RDBInsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBInsertStatement287", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Values298: BinaryAssociation = BinaryAssociation(
    name="Values298",
    ends={
        Property(name="Expression299", type=astm_sastm_RDBOpenCursorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBOpenCursorStatement", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Into300: BinaryAssociation = BinaryAssociation(
    name="Into300",
    ends={
        Property(name="RDBHostVariableReference301", type=astm_sastm_RDBFetchCursorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBFetchCursorStatement", type=RDBHostVariableReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BaseVariable302: BinaryAssociation = BinaryAssociation(
    name="BaseVariable302",
    ends={
        Property(name="Expression303", type=astm_sastm_RDBHostVariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBHostVariableReference", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Indicator304: BinaryAssociation = BinaryAssociation(
    name="Indicator304",
    ends={
        Property(name="Expression306", type=astm_sastm_RDBHostVariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBHostVariableReference305", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Cursor296: BinaryAssociation = BinaryAssociation(
    name="Cursor296",
    ends={
        Property(name="Expression297", type=astm_sastm_RDBCursorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBCursorStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Where312: BinaryAssociation = BinaryAssociation(
    name="Where312",
    ends={
        Property(name="Expression314", type=astm_sastm_RDBSelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBSelectExpression313", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Alias315: BinaryAssociation = BinaryAssociation(
    name="Alias315",
    ends={
        Property(name="LabelDefinition316", type=astm_sastm_RDBTableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBTableReference", type=LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Table317: BinaryAssociation = BinaryAssociation(
    name="Table317",
    ends={
        Property(name="Expression318", type=astm_sastm_RDBColumnReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBColumnReference", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Table307: BinaryAssociation = BinaryAssociation(
    name="Table307",
    ends={
        Property(name="RDBTableReference308", type=astm_sastm_RDBSelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBSelectExpression", type=RDBTableReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Column309: BinaryAssociation = BinaryAssociation(
    name="Column309",
    ends={
        Property(name="RDBColumnReference311", type=astm_sastm_RDBSelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_sastm_RDBSelectExpression310", type=RDBColumnReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_astm_gastm_SourceLocation_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=astm_gastm_SourceLocation)
gen_astm_gastm_SourceFile_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=astm_gastm_SourceFile)
gen_astm_gastm_Project_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=astm_gastm_Project)
gen_astm_gastm_Scope_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=astm_gastm_Scope)
gen_astm_gastm_GASTMSyntaxObject_GASTMObject = Generalization(general=GASTMObject, specific=astm_gastm_GASTMSyntaxObject)
gen_astm_gastm_Definition_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=astm_gastm_Definition)
gen_astm_gastm_CompilationUnit_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_CompilationUnit)
gen_astm_gastm_Name_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_Name)
gen_astm_gastm_DeclarationOrDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_gastm_DeclarationOrDefinition)
gen_astm_gastm_Declaration_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=astm_gastm_Declaration)
gen_astm_gastm_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=astm_gastm_FunctionDeclaration)
gen_astm_gastm_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=astm_gastm_VariableDeclaration)
gen_astm_gastm_FunctionDefinition_Definition = Generalization(general=Definition, specific=astm_gastm_FunctionDefinition)
gen_astm_gastm_DataDefinition_Definition = Generalization(general=Definition, specific=astm_gastm_DataDefinition)
gen_astm_gastm_EntryDefinition_Definition = Generalization(general=Definition, specific=astm_gastm_EntryDefinition)
gen_astm_gastm_BitFieldDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_gastm_BitFieldDefinition)
gen_astm_gastm_EnumLiteralDefinition_Definition = Generalization(general=Definition, specific=astm_gastm_EnumLiteralDefinition)
gen_astm_gastm_TypeDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_gastm_TypeDefinition)
gen_astm_gastm_NamedTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=astm_gastm_NamedTypeDefinition)
gen_astm_gastm_AggregateTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=astm_gastm_AggregateTypeDefinition)
gen_astm_gastm_NameSpaceDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_gastm_NameSpaceDefinition)
gen_astm_gastm_Type_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_gastm_Type)
gen_astm_gastm_LabelDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_gastm_LabelDefinition)
gen_astm_gastm_IncludeUnit_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_gastm_IncludeUnit)
gen_astm_gastm_MacroCall_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_gastm_MacroCall)
gen_astm_gastm_MacroDefinition_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_gastm_MacroDefinition)
gen_astm_gastm_Comment_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_gastm_Comment)
gen_astm_gastm_Dimension_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_Dimension)
gen_astm_gastm_PrimitiveType_DataType = Generalization(general=DataType, specific=astm_gastm_PrimitiveType)
gen_astm_gastm_EnumType_DataType = Generalization(general=DataType, specific=astm_gastm_EnumType)
gen_astm_gastm_ConstructedType_DataType = Generalization(general=DataType, specific=astm_gastm_ConstructedType)
gen_astm_gastm_AggregateType_DataType = Generalization(general=DataType, specific=astm_gastm_AggregateType)
gen_astm_gastm_ArrayType_ConstructedType = Generalization(general=ConstructedType, specific=astm_gastm_ArrayType)
gen_astm_gastm_DerivesFrom_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_DerivesFrom)
gen_astm_gastm_FunctionType_Type = Generalization(general=Type, specific=astm_gastm_FunctionType)
gen_astm_gastm_FormalParameterType_DataType = Generalization(general=DataType, specific=astm_gastm_FormalParameterType)
gen_astm_gastm_NamedType_DataType = Generalization(general=DataType, specific=astm_gastm_NamedType)
gen_astm_gastm_ClassType_AggregateType = Generalization(general=AggregateType, specific=astm_gastm_ClassType)
gen_astm_gastm_DeclarationOrDefinitionStatement_Statement = Generalization(general=Statement, specific=astm_gastm_DeclarationOrDefinitionStatement)
gen_astm_gastm_UnnamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=astm_gastm_UnnamedTypeReference)
gen_astm_gastm_NamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=astm_gastm_NamedTypeReference)
gen_astm_gastm_DeleteStatement_Statement = Generalization(general=Statement, specific=astm_gastm_DeleteStatement)
gen_astm_gastm_ExpressionStatement_Statement = Generalization(general=Statement, specific=astm_gastm_ExpressionStatement)
gen_astm_gastm_JumpStatement_Statement = Generalization(general=Statement, specific=astm_gastm_JumpStatement)
gen_astm_gastm_BreakStatement_Statement = Generalization(general=Statement, specific=astm_gastm_BreakStatement)
gen_astm_gastm_ContinueStatement_Statement = Generalization(general=Statement, specific=astm_gastm_ContinueStatement)
gen_astm_gastm_LabeledStatement_Statement = Generalization(general=Statement, specific=astm_gastm_LabeledStatement)
gen_astm_gastm_BlockStatement_Statement = Generalization(general=Statement, specific=astm_gastm_BlockStatement)
gen_astm_gastm_SwitchCase_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_SwitchCase)
gen_astm_gastm_EmptyStatement_Statement = Generalization(general=Statement, specific=astm_gastm_EmptyStatement)
gen_astm_gastm_IfStatement_Statement = Generalization(general=Statement, specific=astm_gastm_IfStatement)
gen_astm_gastm_SwitchStatement_Statement = Generalization(general=Statement, specific=astm_gastm_SwitchStatement)
gen_astm_gastm_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_gastm_ForStatement)
gen_astm_gastm_CaseBlock_SwitchCase = Generalization(general=SwitchCase, specific=astm_gastm_CaseBlock)
gen_astm_gastm_ReturnStatement_Statement = Generalization(general=Statement, specific=astm_gastm_ReturnStatement)
gen_astm_gastm_LoopStatement_Statement = Generalization(general=Statement, specific=astm_gastm_LoopStatement)
gen_astm_gastm_TypesCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=astm_gastm_TypesCatchBlock)
gen_astm_gastm_TryStatement_Statement = Generalization(general=Statement, specific=astm_gastm_TryStatement)
gen_astm_gastm_CatchBlock_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_CatchBlock)
gen_astm_gastm_ArrayAccess_Expression = Generalization(general=Expression, specific=astm_gastm_ArrayAccess)
gen_astm_gastm_VariableCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=astm_gastm_VariableCatchBlock)
gen_astm_gastm_ThrowStatement_Statement = Generalization(general=Statement, specific=astm_gastm_ThrowStatement)
gen_astm_gastm_Expression_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_gastm_Expression)
gen_astm_gastm_NameReference_Expression = Generalization(general=Expression, specific=astm_gastm_NameReference)
gen_astm_gastm_CastExpression_Expression = Generalization(general=Expression, specific=astm_gastm_CastExpression)
gen_astm_gastm_QualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_gastm_QualifiedIdentifierReference)
gen_astm_gastm_TypeQualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_gastm_TypeQualifiedIdentifierReference)
gen_astm_gastm_Literal_Expression = Generalization(general=Expression, specific=astm_gastm_Literal)
gen_astm_gastm_UnaryExpression_Expression = Generalization(general=Expression, specific=astm_gastm_UnaryExpression)
gen_astm_gastm_BinaryExpression_Expression = Generalization(general=Expression, specific=astm_gastm_BinaryExpression)
gen_astm_gastm_OperatorAssign_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_OperatorAssign)
gen_astm_gastm_ConditionalExpression_Expression = Generalization(general=Expression, specific=astm_gastm_ConditionalExpression)
gen_astm_gastm_RangeExpression_Expression = Generalization(general=Expression, specific=astm_gastm_RangeExpression)
gen_astm_gastm_FunctionCallExpression_Expression = Generalization(general=Expression, specific=astm_gastm_FunctionCallExpression)
gen_astm_gastm_ActualParameterExpression_ActualParameter = Generalization(general=ActualParameter, specific=astm_gastm_ActualParameterExpression)
gen_astm_gastm_NewExpression_Expression = Generalization(general=Expression, specific=astm_gastm_NewExpression)
gen_astm_gastm_GlobalScope_Scope = Generalization(general=Scope, specific=astm_gastm_GlobalScope)
gen_astm_gastm_PreprocessorElement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_gastm_PreprocessorElement)
gen_astm_gastm_LabelAccess_Expression = Generalization(general=Expression, specific=astm_gastm_LabelAccess)
gen_astm_gastm_AnnotationExpression_Expression = Generalization(general=Expression, specific=astm_gastm_AnnotationExpression)
gen_astm_gastm_External_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_gastm_External)
gen_astm_gastm_FunctionPersistent_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_gastm_FunctionPersistent)
gen_astm_gastm_FileLocal_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_gastm_FileLocal)
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
gen_astm_gastm_FormalParameterDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_gastm_FormalParameterDefinition)
gen_astm_gastm_VirtualSpecification_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_VirtualSpecification)
gen_astm_gastm_FormalParameterDeclaration_Declaration = Generalization(general=Declaration, specific=astm_gastm_FormalParameterDeclaration)
gen_astm_gastm_VariableDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_gastm_VariableDefinition)
gen_astm_gastm_FunctionMemberAttribute_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_gastm_FunctionMemberAttribute)
gen_astm_gastm_String_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_String)
gen_astm_gastm_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_Boolean)
gen_astm_gastm_WideCharacter_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_gastm_WideCharacter)
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
gen_astm_gastm_ForCheckBeforeStatement_ForStatement = Generalization(general=ForStatement, specific=astm_gastm_ForCheckBeforeStatement)
gen_astm_gastm_ForCheckAfterStatement_ForStatement = Generalization(general=ForStatement, specific=astm_gastm_ForCheckAfterStatement)
gen_astm_gastm_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=astm_gastm_CollectionType)
gen_astm_gastm_PointerType_ConstructedType = Generalization(general=ConstructedType, specific=astm_gastm_PointerType)
gen_astm_gastm_ReferenceType_ConstructedType = Generalization(general=ConstructedType, specific=astm_gastm_ReferenceType)
gen_astm_gastm_RangeType_ConstructedType = Generalization(general=ConstructedType, specific=astm_gastm_RangeType)
gen_astm_gastm_StructureType_AggregateType = Generalization(general=AggregateType, specific=astm_gastm_StructureType)
gen_astm_gastm_UnionType_AggregateType = Generalization(general=AggregateType, specific=astm_gastm_UnionType)
gen_astm_gastm_AnnotationType_AggregateType = Generalization(general=AggregateType, specific=astm_gastm_AnnotationType)
gen_astm_gastm_ByValueFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=astm_gastm_ByValueFormalParameterType)
gen_astm_gastm_ByReferenceFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=astm_gastm_ByReferenceFormalParameterType)
gen_astm_gastm_Public_AccessKind = Generalization(general=AccessKind, specific=astm_gastm_Public)
gen_astm_gastm_Protected_AccessKind = Generalization(general=AccessKind, specific=astm_gastm_Protected)
gen_astm_gastm_Private_AccessKind = Generalization(general=AccessKind, specific=astm_gastm_Private)
gen_astm_gastm_TerminateStatement_Statement = Generalization(general=Statement, specific=astm_gastm_TerminateStatement)
gen_astm_gastm_DefaultBlock_SwitchCase = Generalization(general=SwitchCase, specific=astm_gastm_DefaultBlock)
gen_astm_gastm_WhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_gastm_WhileStatement)
gen_astm_gastm_DoWhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_gastm_DoWhileStatement)
gen_astm_gastm_Decrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_Decrement)
gen_astm_gastm_PostIncrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_PostIncrement)
gen_astm_gastm_PostDecrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_PostDecrement)
gen_astm_gastm_AggregateExpression_Expression = Generalization(general=Expression, specific=astm_gastm_AggregateExpression)
gen_astm_gastm_QualifiedOverPointer_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=astm_gastm_QualifiedOverPointer)
gen_astm_gastm_QualifiedOverData_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=astm_gastm_QualifiedOverData)
gen_astm_gastm_IntegerlLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_IntegerlLiteral)
gen_astm_gastm_StringLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_StringLiteral)
gen_astm_gastm_CharLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_CharLiteral)
gen_astm_gastm_RealLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_RealLiteral)
gen_astm_gastm_BooleanLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_BooleanLiteral)
gen_astm_gastm_BitLiteral_Literal = Generalization(general=Literal, specific=astm_gastm_BitLiteral)
gen_astm_gastm_UnaryPlus_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_UnaryPlus)
gen_astm_gastm_Negate_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_Negate)
gen_astm_gastm_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_Not)
gen_astm_gastm_BitNot_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_BitNot)
gen_astm_gastm_AddressOf_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_AddressOf)
gen_astm_gastm_Deref_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_Deref)
gen_astm_gastm_Increment_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_gastm_Increment)
gen_astm_gastm_BitXor_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_BitXor)
gen_astm_gastm_BitLeftShift_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_BitLeftShift)
gen_astm_gastm_BitRightShift_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_BitRightShift)
gen_astm_gastm_Add_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Add)
gen_astm_gastm_Assign_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_Assign)
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
gen_astm_sastm_RDBDatabaseDefinition_Definition = Generalization(general=Definition, specific=astm_sastm_RDBDatabaseDefinition)
gen_astm_gastm_MissingActualParameter_ActualParameter = Generalization(general=ActualParameter, specific=astm_gastm_MissingActualParameter)
gen_astm_sastm_RDBUserDefinition_Definition = Generalization(general=Definition, specific=astm_sastm_RDBUserDefinition)
gen_astm_gastm_ByValueActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=astm_gastm_ByValueActualParameterExpression)
gen_astm_gastm_ByReferenceActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=astm_gastm_ByReferenceActualParameterExpression)
gen_astm_gastm_SpecificTriggerDefinition_Definition = Generalization(general=Definition, specific=astm_gastm_SpecificTriggerDefinition)
gen_astm_sastm_RDBTableSpaceDefinition_Definition = Generalization(general=Definition, specific=astm_sastm_RDBTableSpaceDefinition)
gen_astm_sastm_RDBTableDefinition_Definition = Generalization(general=Definition, specific=astm_sastm_RDBTableDefinition)
gen_astm_gastm_SpecificLessEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_SpecificLessEqual)
gen_astm_gastm_SpecificGreaterEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_SpecificGreaterEqual)
gen_astm_gastm_SpecificIn_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_SpecificIn)
gen_astm_gastm_SpecificLike_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_SpecificLike)
gen_astm_gastm_SpecificConcatString_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_gastm_SpecificConcatString)
gen_astm_gastm_SpecificSelectStatement_Statement = Generalization(general=Statement, specific=astm_gastm_SpecificSelectStatement)
gen_astm_sastm_RDBColumnDefinition_Definition = Generalization(general=Definition, specific=astm_sastm_RDBColumnDefinition)
gen_astm_sastm_RDBViewDefinition_Definition = Generalization(general=Definition, specific=astm_sastm_RDBViewDefinition)
gen_astm_sastm_RDBCursorDefinition_Definition = Generalization(general=Definition, specific=astm_sastm_RDBCursorDefinition)
gen_astm_sastm_RDBIndex_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_sastm_RDBIndex)
gen_astm_sastm_RDBTrigger_gastm_OtherSyntaxObject = Generalization(general=gastm_OtherSyntaxObject, specific=astm_sastm_RDBTrigger)
gen_astm_sastm_RDBTrigger_gastm_Definition = Generalization(general=gastm_Definition, specific=astm_sastm_RDBTrigger)
gen_astm_sastm_RDBConstraint_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_sastm_RDBConstraint)
gen_astm_sastm_RDBCheckConstraint_RDBConstraint = Generalization(general=RDBConstraint, specific=astm_sastm_RDBCheckConstraint)
gen_astm_sastm_RDBRefIntegrity_RDBConstraint = Generalization(general=RDBConstraint, specific=astm_sastm_RDBRefIntegrity)
gen_astm_sastm_RDBIndexColumn_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_sastm_RDBIndexColumn)
gen_astm_sastm_RDBConnectStatement_Statement = Generalization(general=Statement, specific=astm_sastm_RDBConnectStatement)
gen_astm_sastm_RDBSelectStatement_Statement = Generalization(general=Statement, specific=astm_sastm_RDBSelectStatement)
gen_astm_sastm_RDBInsertStatement_Statement = Generalization(general=Statement, specific=astm_sastm_RDBInsertStatement)
gen_astm_sastm_RDBUniqueKey_RDBConstraint = Generalization(general=RDBConstraint, specific=astm_sastm_RDBUniqueKey)
gen_astm_sastm_RDBModifyStatement_Statement = Generalization(general=Statement, specific=astm_sastm_RDBModifyStatement)
gen_astm_sastm_RDBUpdateStatement_RDBModifyStatement = Generalization(general=RDBModifyStatement, specific=astm_sastm_RDBUpdateStatement)
gen_astm_sastm_RDBCursorStatement_Statement = Generalization(general=Statement, specific=astm_sastm_RDBCursorStatement)
gen_astm_sastm_RDBFetchCursorStatement_RDBCursorStatement = Generalization(general=RDBCursorStatement, specific=astm_sastm_RDBFetchCursorStatement)
gen_astm_sastm_RDBSelectExpression_Expression = Generalization(general=Expression, specific=astm_sastm_RDBSelectExpression)
gen_astm_sastm_RDBOpenCursorStatement_RDBCursorStatement = Generalization(general=RDBCursorStatement, specific=astm_sastm_RDBOpenCursorStatement)
gen_astm_sastm_RDBTableReference_IdentifierReference = Generalization(general=IdentifierReference, specific=astm_sastm_RDBTableReference)
gen_astm_sastm_RDBTableAlias_IdentifierReference = Generalization(general=IdentifierReference, specific=astm_sastm_RDBTableAlias)
gen_astm_sastm_RDBColumnReference_IdentifierReference = Generalization(general=IdentifierReference, specific=astm_sastm_RDBColumnReference)
gen_astm_sastm_RDBDataBaseType_DataType = Generalization(general=DataType, specific=astm_sastm_RDBDataBaseType)
gen_astm_sastm_RDBCursorType_DataType = Generalization(general=DataType, specific=astm_sastm_RDBCursorType)
gen_astm_sastm_RDBColumnType_DataType = Generalization(general=DataType, specific=astm_sastm_RDBColumnType)
gen_astm_sastm_RDBInteger_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBInteger)
gen_astm_sastm_RDBInt_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBInt)
gen_astm_sastm_RDBReal_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBReal)
gen_astm_sastm_RDBFloat_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBFloat)
gen_astm_sastm_RDBDecimal_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBDecimal)
gen_astm_sastm_RDBNumber_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBNumber)
gen_astm_sastm_RDBLong_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBLong)
gen_astm_sastm_RDBChar_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBChar)
gen_astm_sastm_RDBVarchar_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBVarchar)
gen_astm_sastm_RDBString_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBString)
gen_astm_sastm_RDBRaw_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBRaw)
gen_astm_sastm_RDBDate_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBDate)
gen_astm_sastm_RDBUserType_DataType = Generalization(general=DataType, specific=astm_sastm_RDBUserType)
gen_astm_sastm_RDBTableSpaceType_DataType = Generalization(general=DataType, specific=astm_sastm_RDBTableSpaceType)
gen_astm_sastm_RDBTableType_DataType = Generalization(general=DataType, specific=astm_sastm_RDBTableType)
gen_astm_sastm_RDBViewType_DataType = Generalization(general=DataType, specific=astm_sastm_RDBViewType)
gen_astm_sastm_RDBClob_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBClob)
gen_astm_sastm_RDBNClob_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBNClob)
gen_astm_sastm_RDBBFile_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBBFile)
gen_astm_sastm_RDBDeleteStatement_RDBModifyStatement = Generalization(general=RDBModifyStatement, specific=astm_sastm_RDBDeleteStatement)
gen_astm_sastm_RDBCloseCursorStatement_RDBCursorStatement = Generalization(general=RDBCursorStatement, specific=astm_sastm_RDBCloseCursorStatement)
gen_astm_sastm_RDBHostVariableExpression_Expression = Generalization(general=Expression, specific=astm_sastm_RDBHostVariableExpression)
gen_astm_sastm_RDBTimestamp_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBTimestamp)
gen_astm_sastm_RDBRowid_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBRowid)
gen_astm_sastm_RDBBoolean_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBBoolean)
gen_astm_sastm_RDBBlob_RDBColumnType = Generalization(general=RDBColumnType, specific=astm_sastm_RDBBlob)

# Domain Model
domain_model = DomainModel(
    name="astm",
    types={astm_gastm_SourceLocation, astm_gastm_GASTMObject, astm_gastm_GASTMSourceObject, astm_gastm_GASTMSemanticObject, astm_gastm_OtherSyntaxObject, astm_gastm_StorageSpecification, astm_gastm_DataType, astm_gastm_AccessKind, astm_gastm_UnaryOperator, astm_gastm_BinaryOperator, astm_gastm_ActualParameter, astm_gastm_SourceFile, GASTMSourceObject, SourceLocation, PreprocessorElement, AnnotationExpression, SourceFile, astm_gastm_Project, GASTMSemanticObject, CompilationUnit, GlobalScope, astm_gastm_Scope, DefinitionObject, Scope, astm_gastm_GASTMSyntaxObject, GASTMObject, astm_gastm_Definition, DeclarationOrDefinition, Name, TypeReference, astm_gastm_CompilationUnit, OtherSyntaxObject, ProgramScope, astm_gastm_Name, astm_gastm_DeclarationOrDefinition, FormalParameterDefinition, Statement, astm_gastm_Declaration, Definition, astm_gastm_FunctionDeclaration, Declaration, FormalParameterDeclaration, FunctionMemberAttributes, astm_gastm_VariableDeclaration, astm_gastm_FunctionDefinition, astm_gastm_DataDefinition, Expression, astm_gastm_BitFieldDefinition, DataDefinition, FunctionScope, astm_gastm_FunctionMemberAttributes, VirtualSpecification, astm_gastm_EntryDefinition, NameSpaceType, astm_gastm_EnumLiteralDefinition, astm_gastm_TypeDefinition, astm_gastm_NamedTypeDefinition, TypeDefinition, NamedType, astm_gastm_AggregateTypeDefinition, AggregateType, astm_gastm_NameSpaceDefinition, astm_gastm_Type, GASTMSyntaxObject, astm_gastm_PrimitiveType, astm_gastm_LabelDefinition, LabelType, astm_gastm_IncludeUnit, astm_gastm_MacroCall, MacroDefinition, astm_gastm_MacroDefinition, astm_gastm_Comment, astm_gastm_Dimension, DataType, astm_gastm_EnumType, EnumLiteralDefinition, astm_gastm_ConstructedType, astm_gastm_AggregateType, AggregateScope, astm_gastm_ArrayType, ConstructedType, Dimension, astm_gastm_DerivesFrom, astm_gastm_FunctionType, Type, FormalParameterType, astm_gastm_FormalParameterType, astm_gastm_NamedType, astm_gastm_ClassType, DerivesFrom, astm_gastm_DeclarationOrDefinitionStatement, astm_gastm_UnnamedTypeReference, astm_gastm_NamedTypeReference, astm_gastm_DeleteStatement, astm_gastm_ExpressionStatement, astm_gastm_JumpStatement, astm_gastm_BreakStatement, LabelAccess, astm_gastm_ContinueStatement, astm_gastm_LabeledStatement, LabelDefinition, SwitchCase, astm_gastm_BlockStatement, astm_gastm_SwitchCase, BlockScope, astm_gastm_EmptyStatement, astm_gastm_IfStatement, astm_gastm_SwitchStatement, astm_gastm_ForStatement, LoopStatement, astm_gastm_CaseBlock, astm_gastm_ReturnStatement, astm_gastm_LoopStatement, astm_gastm_TypesCatchBlock, astm_gastm_TryStatement, CatchBlock, astm_gastm_CatchBlock, astm_gastm_ArrayAccess, astm_gastm_VariableCatchBlock, astm_gastm_ThrowStatement, astm_gastm_Expression, astm_gastm_NameReference, astm_gastm_CastExpression, astm_gastm_QualifiedIdentifierReference, NameReference, IdentifierReference, astm_gastm_TypeQualifiedIdentifierReference, astm_gastm_Literal, astm_gastm_UnaryExpression, astm_gastm_BinaryExpression, astm_gastm_OperatorAssign, BinaryOperator, astm_gastm_ConditionalExpression, astm_gastm_RangeExpression, astm_gastm_FunctionCallExpression, ActualParameter, astm_gastm_ActualParameterExpression, astm_gastm_NewExpression, astm_gastm_GlobalScope, astm_gastm_PreprocessorElement, astm_gastm_LabelAccess, astm_gastm_AnnotationExpression, StorageSpecification, astm_gastm_FunctionPersistent, astm_gastm_FileLocal, astm_gastm_DefinitionObject, astm_gastm_ProgramScope, astm_gastm_TypeReference, astm_gastm_Statement, astm_gastm_FunctionScope, astm_gastm_NameSpaceType, astm_gastm_LabelType, astm_gastm_AggregateScope, astm_gastm_BlockScope, astm_gastm_IdentifierReference, astm_gastm_FormalParameterDefinition, astm_gastm_VirtualSpecification, astm_gastm_FormalParameterDeclaration, astm_gastm_VariableDefinition, astm_gastm_FunctionMemberAttribute, astm_gastm_External, astm_gastm_String, astm_gastm_Boolean, astm_gastm_WideCharacter, astm_gastm_PerClassMember, astm_gastm_NoDef, astm_gastm_Virtual, astm_gastm_PureVirtual, astm_gastm_NonVirtual, astm_gastm_ExceptionType, astm_gastm_Void, PrimitiveType, astm_gastm_Byte, astm_gastm_ShortInteger, astm_gastm_Integer, astm_gastm_LongInteger, astm_gastm_Float, astm_gastm_Double, astm_gastm_LongDouble, astm_gastm_Character, astm_gastm_ForCheckBeforeStatement, ForStatement, astm_gastm_ForCheckAfterStatement, astm_gastm_CollectionType, astm_gastm_PointerType, astm_gastm_ReferenceType, astm_gastm_RangeType, astm_gastm_StructureType, astm_gastm_UnionType, astm_gastm_AnnotationType, astm_gastm_ByValueFormalParameterType, astm_gastm_ByReferenceFormalParameterType, astm_gastm_Public, AccessKind, astm_gastm_Protected, astm_gastm_Private, astm_gastm_TerminateStatement, astm_gastm_DefaultBlock, astm_gastm_WhileStatement, astm_gastm_DoWhileStatement, astm_gastm_Decrement, astm_gastm_PostIncrement, astm_gastm_PostDecrement, astm_gastm_AggregateExpression, astm_gastm_QualifiedOverPointer, QualifiedIdentifierReference, astm_gastm_QualifiedOverData, astm_gastm_IntegerlLiteral, Literal, astm_gastm_StringLiteral, astm_gastm_CharLiteral, astm_gastm_RealLiteral, astm_gastm_BooleanLiteral, astm_gastm_BitLiteral, astm_gastm_UnaryPlus, UnaryOperator, astm_gastm_Negate, astm_gastm_Not, astm_gastm_BitNot, astm_gastm_AddressOf, astm_gastm_Deref, astm_gastm_Increment, astm_gastm_BitXor, astm_gastm_BitLeftShift, astm_gastm_BitRightShift, astm_gastm_Add, astm_gastm_Assign, astm_gastm_Subtract, astm_gastm_MissingActualParameter, astm_gastm_Multiply, astm_gastm_Divide, astm_gastm_Modulus, astm_gastm_Exponent, astm_gastm_And, astm_gastm_Or, astm_gastm_Equal, astm_gastm_NotEqual, astm_gastm_Greater, astm_gastm_NotGreater, astm_gastm_Less, astm_gastm_NotLess, astm_gastm_BitAnd, astm_gastm_BitOr, astm_sastm_RDBDatabaseDefinition, RDBTableSpaceReference, astm_sastm_RDBTableSpaceReference, astm_sastm_RDBUserDefinition, astm_gastm_ByValueActualParameterExpression, ActualParameterExpression, NameSpaceDefinition, astm_gastm_ByReferenceActualParameterExpression, astm_gastm_SpecificTriggerDefinition, astm_sastm_RDBTableSpaceDefinition, astm_sastm_RDBTableDefinition, astm_gastm_SpecificLessEqual, RDBColumnReference, astm_gastm_SpecificGreaterEqual, astm_gastm_SpecificIn, astm_gastm_SpecificLike, astm_gastm_SpecificConcatString, astm_gastm_SpecificSelectStatement, RDBTrigger, astm_sastm_RDBColumnDefinition, RDBColumnType, astm_sastm_RDBViewDefinition, AggregateTypeDefinition, RDBColumnDefinition, RDBConstraint, RDBIndex, astm_sastm_RDBCursorDefinition, astm_sastm_RDBIndex, astm_sastm_RDBTrigger, gastm_OtherSyntaxObject, gastm_Definition, astm_sastm_RDBConstraint, astm_sastm_RDBCheckConstraint, astm_sastm_RDBRefIntegrity, astm_sastm_RDBIndexColumn, IncludeUnit, astm_sastm_RDBConnectStatement, NamedTypeDefinition, astm_sastm_RDBSelectStatement, RDBSelectExpression, RDBHostVariableReference, astm_sastm_RDBInsertStatement, RDBTableReference, astm_sastm_RDBUniqueKey, astm_sastm_RDBModifyStatement, astm_sastm_RDBUpdateStatement, RDBModifyStatement, astm_sastm_RDBCursorStatement, astm_sastm_RDBFetchCursorStatement, astm_sastm_RDBHostVariableReference, astm_sastm_RDBSelectExpression, astm_sastm_RDBOpenCursorStatement, RDBCursorStatement, astm_sastm_RDBTableReference, astm_sastm_RDBTableAlias, astm_sastm_RDBColumnReference, astm_sastm_RDBDataBaseType, astm_sastm_RDBUserType, astm_sastm_RDBCursorType, astm_sastm_RDBColumnType, astm_sastm_RDBInteger, astm_sastm_RDBInt, astm_sastm_RDBReal, astm_sastm_RDBFloat, astm_sastm_RDBDecimal, astm_sastm_RDBNumber, astm_sastm_RDBLong, astm_sastm_RDBChar, astm_sastm_RDBVarchar, astm_sastm_RDBString, astm_sastm_RDBRaw, astm_sastm_RDBDate, astm_sastm_RDBTableSpaceType, astm_sastm_RDBTableType, astm_sastm_RDBViewType, astm_sastm_RDBClob, astm_sastm_RDBNClob, astm_sastm_RDBBFile, astm_sastm_RDBDeleteStatement, astm_sastm_RDBCloseCursorStatement, astm_sastm_RDBHostVariableExpression, astm_sastm_RDBTimestamp, astm_sastm_RDBRowid, astm_sastm_RDBBoolean, astm_sastm_RDBBlob},
    associations={locationInfo7, preProcessorElements8, annotations10, inSourceFile0, files1, outerScope2, definitionObject4, childScope5, identifierName20, definitionType21, fragments12, opensScope14, storageSpecifiers16, accessKind17, returnType33, formalParameters35, defRef23, identifierName24, declarationType27, formalParameters30, functionMemberAttributes31, initialValue50, body37, functionMemberAttributes39, opensScope42, virtualSpecifier44, formalParameters45, body47, nameSpace59, body61, nameSpaceType64, bitFieldSize51, value53, name55, definitionType57, aggregateType58, labelName66, labelType68, file70, refersTo72, ranks80, lowBound81, enumLiterals73, baseType74, members76, opensScope78, accessKind94, highBound83, returnType86, parameterTypes88, type90, body92, derivesFrom93, declOrDefn107, className96, type99, name101, type103, operand105, statement117, expression109, target111, target113, target114, switchExpression132, label116, cases134, subStatements120, opensScope122, condition124, thenBody126, elseBody129, initBody147, body136, caseExpressions138, returnValue140, condition142, body144, exceptions161, iterationBody149, guardedStatement152, catchBlocks154, finalStatement156, body159, arrayName173, exceptionVariable163, exception164, expressionType166, name168, refersTo170, castType187, subscripts175, qualifiers178, member180, aggregateType182, member184, rightOperand202, expression189, operator192, operand194, operator197, fromExpression215, leftOperand199, operator205, condition207, onTrueOperand209, onFalseOperand212, newType226, toExpression217, calledFunction220, actualParams222, value224, actualParams228, name231, definition233, annotationType236, memberValues238, TableSpace243, Owns244, body241, Table245, PrimKey247, Trigger254, name256, type258, DefinedBy260, Column248, Constraint250, Index252, SelectExpression261, Column265, body266, ForeignKey268, IndexColumn263, Column275, ConnectString277, SelectExpression278, IntoVariable279, IntoTable281, ParentKey270, ParentTable273, Table289, Where291, Values294, Columns283, Values286, Values298, Into300, BaseVariable302, Indicator304, Cursor296, Where312, Alias315, Table317, Table307, Column309},
    generalizations={gen_astm_gastm_SourceLocation_GASTMSourceObject, gen_astm_gastm_SourceFile_GASTMSourceObject, gen_astm_gastm_Project_GASTMSemanticObject, gen_astm_gastm_Scope_GASTMSemanticObject, gen_astm_gastm_GASTMSyntaxObject_GASTMObject, gen_astm_gastm_Definition_DeclarationOrDefinition, gen_astm_gastm_CompilationUnit_OtherSyntaxObject, gen_astm_gastm_Name_OtherSyntaxObject, gen_astm_gastm_DeclarationOrDefinition_DefinitionObject, gen_astm_gastm_Declaration_DeclarationOrDefinition, gen_astm_gastm_FunctionDeclaration_Declaration, gen_astm_gastm_VariableDeclaration_Declaration, gen_astm_gastm_FunctionDefinition_Definition, gen_astm_gastm_DataDefinition_Definition, gen_astm_gastm_EntryDefinition_Definition, gen_astm_gastm_BitFieldDefinition_DataDefinition, gen_astm_gastm_EnumLiteralDefinition_Definition, gen_astm_gastm_TypeDefinition_DefinitionObject, gen_astm_gastm_NamedTypeDefinition_TypeDefinition, gen_astm_gastm_AggregateTypeDefinition_TypeDefinition, gen_astm_gastm_NameSpaceDefinition_DefinitionObject, gen_astm_gastm_Type_GASTMSyntaxObject, gen_astm_gastm_LabelDefinition_DefinitionObject, gen_astm_gastm_IncludeUnit_PreprocessorElement, gen_astm_gastm_MacroCall_PreprocessorElement, gen_astm_gastm_MacroDefinition_PreprocessorElement, gen_astm_gastm_Comment_PreprocessorElement, gen_astm_gastm_Dimension_OtherSyntaxObject, gen_astm_gastm_PrimitiveType_DataType, gen_astm_gastm_EnumType_DataType, gen_astm_gastm_ConstructedType_DataType, gen_astm_gastm_AggregateType_DataType, gen_astm_gastm_ArrayType_ConstructedType, gen_astm_gastm_DerivesFrom_OtherSyntaxObject, gen_astm_gastm_FunctionType_Type, gen_astm_gastm_FormalParameterType_DataType, gen_astm_gastm_NamedType_DataType, gen_astm_gastm_ClassType_AggregateType, gen_astm_gastm_DeclarationOrDefinitionStatement_Statement, gen_astm_gastm_UnnamedTypeReference_TypeReference, gen_astm_gastm_NamedTypeReference_TypeReference, gen_astm_gastm_DeleteStatement_Statement, gen_astm_gastm_ExpressionStatement_Statement, gen_astm_gastm_JumpStatement_Statement, gen_astm_gastm_BreakStatement_Statement, gen_astm_gastm_ContinueStatement_Statement, gen_astm_gastm_LabeledStatement_Statement, gen_astm_gastm_BlockStatement_Statement, gen_astm_gastm_SwitchCase_OtherSyntaxObject, gen_astm_gastm_EmptyStatement_Statement, gen_astm_gastm_IfStatement_Statement, gen_astm_gastm_SwitchStatement_Statement, gen_astm_gastm_ForStatement_LoopStatement, gen_astm_gastm_CaseBlock_SwitchCase, gen_astm_gastm_ReturnStatement_Statement, gen_astm_gastm_LoopStatement_Statement, gen_astm_gastm_TypesCatchBlock_CatchBlock, gen_astm_gastm_TryStatement_Statement, gen_astm_gastm_CatchBlock_OtherSyntaxObject, gen_astm_gastm_ArrayAccess_Expression, gen_astm_gastm_VariableCatchBlock_CatchBlock, gen_astm_gastm_ThrowStatement_Statement, gen_astm_gastm_Expression_GASTMSyntaxObject, gen_astm_gastm_NameReference_Expression, gen_astm_gastm_CastExpression_Expression, gen_astm_gastm_QualifiedIdentifierReference_NameReference, gen_astm_gastm_TypeQualifiedIdentifierReference_NameReference, gen_astm_gastm_Literal_Expression, gen_astm_gastm_UnaryExpression_Expression, gen_astm_gastm_BinaryExpression_Expression, gen_astm_gastm_OperatorAssign_BinaryOperator, gen_astm_gastm_ConditionalExpression_Expression, gen_astm_gastm_RangeExpression_Expression, gen_astm_gastm_FunctionCallExpression_Expression, gen_astm_gastm_ActualParameterExpression_ActualParameter, gen_astm_gastm_NewExpression_Expression, gen_astm_gastm_GlobalScope_Scope, gen_astm_gastm_PreprocessorElement_GASTMSyntaxObject, gen_astm_gastm_LabelAccess_Expression, gen_astm_gastm_AnnotationExpression_Expression, gen_astm_gastm_External_StorageSpecification, gen_astm_gastm_FunctionPersistent_StorageSpecification, gen_astm_gastm_FileLocal_StorageSpecification, gen_astm_gastm_DefinitionObject_GASTMSyntaxObject, gen_astm_gastm_ProgramScope_Scope, gen_astm_gastm_TypeReference_Type, gen_astm_gastm_Statement_GASTMSyntaxObject, gen_astm_gastm_FunctionScope_Scope, gen_astm_gastm_NameSpaceType_Type, gen_astm_gastm_LabelType_Type, gen_astm_gastm_AggregateScope_Scope, gen_astm_gastm_BlockScope_Scope, gen_astm_gastm_IdentifierReference_NameReference, gen_astm_gastm_FormalParameterDefinition_DataDefinition, gen_astm_gastm_VirtualSpecification_OtherSyntaxObject, gen_astm_gastm_FormalParameterDeclaration_Declaration, gen_astm_gastm_VariableDefinition_DataDefinition, gen_astm_gastm_FunctionMemberAttribute_OtherSyntaxObject, gen_astm_gastm_String_PrimitiveType, gen_astm_gastm_Boolean_PrimitiveType, gen_astm_gastm_WideCharacter_PrimitiveType, gen_astm_gastm_PerClassMember_StorageSpecification, gen_astm_gastm_NoDef_StorageSpecification, gen_astm_gastm_Virtual_VirtualSpecification, gen_astm_gastm_PureVirtual_VirtualSpecification, gen_astm_gastm_NonVirtual_VirtualSpecification, gen_astm_gastm_ExceptionType_DataType, gen_astm_gastm_Void_PrimitiveType, gen_astm_gastm_Byte_PrimitiveType, gen_astm_gastm_ShortInteger_PrimitiveType, gen_astm_gastm_Integer_PrimitiveType, gen_astm_gastm_LongInteger_PrimitiveType, gen_astm_gastm_Float_PrimitiveType, gen_astm_gastm_Double_PrimitiveType, gen_astm_gastm_LongDouble_PrimitiveType, gen_astm_gastm_Character_PrimitiveType, gen_astm_gastm_ForCheckBeforeStatement_ForStatement, gen_astm_gastm_ForCheckAfterStatement_ForStatement, gen_astm_gastm_CollectionType_ConstructedType, gen_astm_gastm_PointerType_ConstructedType, gen_astm_gastm_ReferenceType_ConstructedType, gen_astm_gastm_RangeType_ConstructedType, gen_astm_gastm_StructureType_AggregateType, gen_astm_gastm_UnionType_AggregateType, gen_astm_gastm_AnnotationType_AggregateType, gen_astm_gastm_ByValueFormalParameterType_FormalParameterType, gen_astm_gastm_ByReferenceFormalParameterType_FormalParameterType, gen_astm_gastm_Public_AccessKind, gen_astm_gastm_Protected_AccessKind, gen_astm_gastm_Private_AccessKind, gen_astm_gastm_TerminateStatement_Statement, gen_astm_gastm_DefaultBlock_SwitchCase, gen_astm_gastm_WhileStatement_LoopStatement, gen_astm_gastm_DoWhileStatement_LoopStatement, gen_astm_gastm_Decrement_UnaryOperator, gen_astm_gastm_PostIncrement_UnaryOperator, gen_astm_gastm_PostDecrement_UnaryOperator, gen_astm_gastm_AggregateExpression_Expression, gen_astm_gastm_QualifiedOverPointer_QualifiedIdentifierReference, gen_astm_gastm_QualifiedOverData_QualifiedIdentifierReference, gen_astm_gastm_IntegerlLiteral_Literal, gen_astm_gastm_StringLiteral_Literal, gen_astm_gastm_CharLiteral_Literal, gen_astm_gastm_RealLiteral_Literal, gen_astm_gastm_BooleanLiteral_Literal, gen_astm_gastm_BitLiteral_Literal, gen_astm_gastm_UnaryPlus_UnaryOperator, gen_astm_gastm_Negate_UnaryOperator, gen_astm_gastm_Not_UnaryOperator, gen_astm_gastm_BitNot_UnaryOperator, gen_astm_gastm_AddressOf_UnaryOperator, gen_astm_gastm_Deref_UnaryOperator, gen_astm_gastm_Increment_UnaryOperator, gen_astm_gastm_BitXor_BinaryOperator, gen_astm_gastm_BitLeftShift_BinaryOperator, gen_astm_gastm_BitRightShift_BinaryOperator, gen_astm_gastm_Add_BinaryOperator, gen_astm_gastm_Assign_BinaryOperator, gen_astm_gastm_Subtract_BinaryOperator, gen_astm_gastm_Multiply_BinaryOperator, gen_astm_gastm_Divide_BinaryOperator, gen_astm_gastm_Modulus_BinaryOperator, gen_astm_gastm_Exponent_BinaryOperator, gen_astm_gastm_And_BinaryOperator, gen_astm_gastm_Or_BinaryOperator, gen_astm_gastm_Equal_BinaryOperator, gen_astm_gastm_NotEqual_BinaryOperator, gen_astm_gastm_Greater_BinaryOperator, gen_astm_gastm_NotGreater_BinaryOperator, gen_astm_gastm_Less_BinaryOperator, gen_astm_gastm_NotLess_BinaryOperator, gen_astm_gastm_BitAnd_BinaryOperator, gen_astm_gastm_BitOr_BinaryOperator, gen_astm_sastm_RDBDatabaseDefinition_Definition, gen_astm_gastm_MissingActualParameter_ActualParameter, gen_astm_sastm_RDBUserDefinition_Definition, gen_astm_gastm_ByValueActualParameterExpression_ActualParameterExpression, gen_astm_gastm_ByReferenceActualParameterExpression_ActualParameterExpression, gen_astm_gastm_SpecificTriggerDefinition_Definition, gen_astm_sastm_RDBTableSpaceDefinition_Definition, gen_astm_sastm_RDBTableDefinition_Definition, gen_astm_gastm_SpecificLessEqual_BinaryOperator, gen_astm_gastm_SpecificGreaterEqual_BinaryOperator, gen_astm_gastm_SpecificIn_BinaryOperator, gen_astm_gastm_SpecificLike_BinaryOperator, gen_astm_gastm_SpecificConcatString_BinaryOperator, gen_astm_gastm_SpecificSelectStatement_Statement, gen_astm_sastm_RDBColumnDefinition_Definition, gen_astm_sastm_RDBViewDefinition_Definition, gen_astm_sastm_RDBCursorDefinition_Definition, gen_astm_sastm_RDBIndex_OtherSyntaxObject, gen_astm_sastm_RDBTrigger_gastm_OtherSyntaxObject, gen_astm_sastm_RDBTrigger_gastm_Definition, gen_astm_sastm_RDBConstraint_OtherSyntaxObject, gen_astm_sastm_RDBCheckConstraint_RDBConstraint, gen_astm_sastm_RDBRefIntegrity_RDBConstraint, gen_astm_sastm_RDBIndexColumn_OtherSyntaxObject, gen_astm_sastm_RDBConnectStatement_Statement, gen_astm_sastm_RDBSelectStatement_Statement, gen_astm_sastm_RDBInsertStatement_Statement, gen_astm_sastm_RDBUniqueKey_RDBConstraint, gen_astm_sastm_RDBModifyStatement_Statement, gen_astm_sastm_RDBUpdateStatement_RDBModifyStatement, gen_astm_sastm_RDBCursorStatement_Statement, gen_astm_sastm_RDBFetchCursorStatement_RDBCursorStatement, gen_astm_sastm_RDBSelectExpression_Expression, gen_astm_sastm_RDBOpenCursorStatement_RDBCursorStatement, gen_astm_sastm_RDBTableReference_IdentifierReference, gen_astm_sastm_RDBTableAlias_IdentifierReference, gen_astm_sastm_RDBColumnReference_IdentifierReference, gen_astm_sastm_RDBDataBaseType_DataType, gen_astm_sastm_RDBCursorType_DataType, gen_astm_sastm_RDBColumnType_DataType, gen_astm_sastm_RDBInteger_RDBColumnType, gen_astm_sastm_RDBInt_RDBColumnType, gen_astm_sastm_RDBReal_RDBColumnType, gen_astm_sastm_RDBFloat_RDBColumnType, gen_astm_sastm_RDBDecimal_RDBColumnType, gen_astm_sastm_RDBNumber_RDBColumnType, gen_astm_sastm_RDBLong_RDBColumnType, gen_astm_sastm_RDBChar_RDBColumnType, gen_astm_sastm_RDBVarchar_RDBColumnType, gen_astm_sastm_RDBString_RDBColumnType, gen_astm_sastm_RDBRaw_RDBColumnType, gen_astm_sastm_RDBDate_RDBColumnType, gen_astm_sastm_RDBUserType_DataType, gen_astm_sastm_RDBTableSpaceType_DataType, gen_astm_sastm_RDBTableType_DataType, gen_astm_sastm_RDBViewType_DataType, gen_astm_sastm_RDBClob_RDBColumnType, gen_astm_sastm_RDBNClob_RDBColumnType, gen_astm_sastm_RDBBFile_RDBColumnType, gen_astm_sastm_RDBDeleteStatement_RDBModifyStatement, gen_astm_sastm_RDBCloseCursorStatement_RDBCursorStatement, gen_astm_sastm_RDBHostVariableExpression_Expression, gen_astm_sastm_RDBTimestamp_RDBColumnType, gen_astm_sastm_RDBRowid_RDBColumnType, gen_astm_sastm_RDBBoolean_RDBColumnType, gen_astm_sastm_RDBBlob_RDBColumnType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)