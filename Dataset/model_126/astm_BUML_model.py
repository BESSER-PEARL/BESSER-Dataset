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
astm_DelphiImplementationSection = Class(name="astm::DelphiImplementationSection")
astm_NamedTypeReference = Class(name="astm::NamedTypeReference")
astm_DelphiBlockStatement = Class(name="astm::DelphiBlockStatement")
BlockStatement = Class(name="BlockStatement")
astm_DefinitionObject = Class(name="astm::DefinitionObject", is_abstract=True)
astm_DelphiFunctionCallExpression = Class(name="astm::DelphiFunctionCallExpression")
FunctionCallExpression = Class(name="FunctionCallExpression")
astm_DelphiUnit = Class(name="astm::DelphiUnit")
CompilationUnit = Class(name="CompilationUnit")
astm_Name = Class(name="astm::Name")
astm_DelphiInterfaceSection = Class(name="astm::DelphiInterfaceSection")
astm_DataType = Class(name="astm::DataType", is_abstract=True)
Type = Class(name="Type")
astm_AccessKind = Class(name="astm::AccessKind")
astm_UnaryOperator = Class(name="astm::UnaryOperator", is_abstract=True)
Operator = Class(name="Operator")
astm_BinaryOperator = Class(name="astm::BinaryOperator", is_abstract=True)
astm_ActualParameter = Class(name="astm::ActualParameter", is_abstract=True)
astm_SourceFile = Class(name="astm::SourceFile")
GASTMSourceObject = Class(name="GASTMSourceObject")
astm_SourceLocation = Class(name="astm::SourceLocation")
astm_Project = Class(name="astm::Project")
GASTMSemanticObject = Class(name="GASTMSemanticObject")
astm_CompilationUnit = Class(name="astm::CompilationUnit")
astm_DelphiWithStatement = Class(name="astm::DelphiWithStatement")
astm_GASTMObject = Class(name="astm::GASTMObject")
Visitable = Class(name="Visitable")
astm_GASTMSourceObject = Class(name="astm::GASTMSourceObject", is_abstract=True)
astm_GASTMSemanticObject = Class(name="astm::GASTMSemanticObject", is_abstract=True)
astm_OtherSyntaxObject = Class(name="astm::OtherSyntaxObject", is_abstract=True)
GASTMSyntaxObject = Class(name="GASTMSyntaxObject")
astm_StorageSpecification = Class(name="astm::StorageSpecification", is_abstract=True)
astm_PreprocessorElement = Class(name="astm::PreprocessorElement", is_abstract=True)
astm_AnnotationExpression = Class(name="astm::AnnotationExpression")
OtherSyntaxObject = Class(name="OtherSyntaxObject")
astm_ProgramScope = Class(name="astm::ProgramScope")
astm_DeclarationOrDefinition = Class(name="astm::DeclarationOrDefinition", is_abstract=True)
DefinitionObject = Class(name="DefinitionObject")
astm_GlobalScope = Class(name="astm::GlobalScope")
astm_Scope = Class(name="astm::Scope")
astm_GASTMSyntaxObject = Class(name="astm::GASTMSyntaxObject", is_abstract=True)
GASTMObject = Class(name="GASTMObject")
astm_FunctionDeclaration = Class(name="astm::FunctionDeclaration")
Declaration = Class(name="Declaration")
astm_FormalParameterDeclaration = Class(name="astm::FormalParameterDeclaration")
astm_FunctionMemberAttributes = Class(name="astm::FunctionMemberAttributes")
astm_VariableDeclaration = Class(name="astm::VariableDeclaration")
astm_FunctionDefinition = Class(name="astm::FunctionDefinition")
Definition = Class(name="Definition")
astm_FormalParameterDefinition = Class(name="astm::FormalParameterDefinition")
astm_Definition = Class(name="astm::Definition", is_abstract=True)
DeclarationOrDefinition = Class(name="DeclarationOrDefinition")
astm_TypeReference = Class(name="astm::TypeReference", is_abstract=True)
astm_Declaration = Class(name="astm::Declaration", is_abstract=True)
astm_VirtualSpecification = Class(name="astm::VirtualSpecification", is_abstract=True)
astm_EntryDefinition = Class(name="astm::EntryDefinition")
astm_DataDefinition = Class(name="astm::DataDefinition", is_abstract=True)
astm_Expression = Class(name="astm::Expression", is_abstract=True)
astm_BitFieldDefinition = Class(name="astm::BitFieldDefinition")
DataDefinition = Class(name="DataDefinition")
astm_Statement = Class(name="astm::Statement", is_abstract=True)
astm_FunctionScope = Class(name="astm::FunctionScope")
astm_NameSpaceDefinition = Class(name="astm::NameSpaceDefinition")
astm_NameSpaceType = Class(name="astm::NameSpaceType")
astm_LabelDefinition = Class(name="astm::LabelDefinition")
astm_LabelType = Class(name="astm::LabelType")
astm_IncludeUnit = Class(name="astm::IncludeUnit")
PreprocessorElement = Class(name="PreprocessorElement")
astm_MacroCall = Class(name="astm::MacroCall")
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
astm_Dimension = Class(name="astm::Dimension")
astm_MacroDefinition = Class(name="astm::MacroDefinition")
astm_Comment = Class(name="astm::Comment")
astm_Type = Class(name="astm::Type", is_abstract=True)
astm_PrimitiveType = Class(name="astm::PrimitiveType", is_abstract=True)
DataType = Class(name="DataType")
astm_ClassType = Class(name="astm::ClassType")
AggregateType = Class(name="AggregateType")
astm_DerivesFrom = Class(name="astm::DerivesFrom")
astm_UnnamedTypeReference = Class(name="astm::UnnamedTypeReference")
TypeReference = Class(name="TypeReference")
astm_FunctionType = Class(name="astm::FunctionType")
astm_BreakStatement = Class(name="astm::BreakStatement")
astm_LabelAccess = Class(name="astm::LabelAccess")
astm_FormalParameterType = Class(name="astm::FormalParameterType", is_abstract=True)
astm_ContinueStatement = Class(name="astm::ContinueStatement")
astm_LabeledStatement = Class(name="astm::LabeledStatement")
astm_BlockStatement = Class(name="astm::BlockStatement")
astm_BlockScope = Class(name="astm::BlockScope")
astm_DeleteStatement = Class(name="astm::DeleteStatement")
Statement = Class(name="Statement")
astm_DeclarationOrDefinitionStatement = Class(name="astm::DeclarationOrDefinitionStatement")
astm_ExpressionStatement = Class(name="astm::ExpressionStatement")
astm_JumpStatement = Class(name="astm::JumpStatement")
astm_ReturnStatement = Class(name="astm::ReturnStatement")
astm_LoopStatement = Class(name="astm::LoopStatement")
astm_ForStatement = Class(name="astm::ForStatement", is_abstract=True)
LoopStatement = Class(name="LoopStatement")
astm_TryStatement = Class(name="astm::TryStatement")
astm_CatchBlock = Class(name="astm::CatchBlock")
astm_EmptyStatement = Class(name="astm::EmptyStatement")
astm_IfStatement = Class(name="astm::IfStatement")
astm_SwitchStatement = Class(name="astm::SwitchStatement")
astm_SwitchCase = Class(name="astm::SwitchCase")
astm_CaseBlock = Class(name="astm::CaseBlock")
SwitchCase = Class(name="SwitchCase")
astm_VariableCatchBlock = Class(name="astm::VariableCatchBlock")
astm_ThrowStatement = Class(name="astm::ThrowStatement")
astm_TypesCatchBlock = Class(name="astm::TypesCatchBlock")
CatchBlock = Class(name="CatchBlock")
astm_QualifiedIdentifierReference = Class(name="astm::QualifiedIdentifierReference", is_abstract=True)
NameReference = Class(name="NameReference")
astm_IdentifierReference = Class(name="astm::IdentifierReference")
astm_TypeQualifiedIdentifierReference = Class(name="astm::TypeQualifiedIdentifierReference")
astm_NameReference = Class(name="astm::NameReference", is_abstract=True)
Expression = Class(name="Expression")
astm_ArrayAccess = Class(name="astm::ArrayAccess")
astm_UnaryExpression = Class(name="astm::UnaryExpression")
astm_BinaryExpression = Class(name="astm::BinaryExpression")
astm_Literal = Class(name="astm::Literal")
astm_CastExpression = Class(name="astm::CastExpression")
astm_ConditionalExpression = Class(name="astm::ConditionalExpression")
astm_OperatorAssign = Class(name="astm::OperatorAssign")
BinaryOperator = Class(name="BinaryOperator")
astm_FunctionCallExpression = Class(name="astm::FunctionCallExpression")
astm_ActualParameterExpression = Class(name="astm::ActualParameterExpression")
ActualParameter = Class(name="ActualParameter")
astm_RangeExpression = Class(name="astm::RangeExpression")
astm_NewExpression = Class(name="astm::NewExpression")
astm_VariableDefinition = Class(name="astm::VariableDefinition")
astm_FunctionMemberAttribute = Class(name="astm::FunctionMemberAttribute")
astm_External = Class(name="astm::External")
StorageSpecification = Class(name="StorageSpecification")
astm_FunctionPersistent = Class(name="astm::FunctionPersistent")
Scope = Class(name="Scope")
astm_Byte = Class(name="astm::Byte")
astm_ShortInteger = Class(name="astm::ShortInteger")
astm_Integer = Class(name="astm::Integer")
astm_LongInteger = Class(name="astm::LongInteger")
astm_Float = Class(name="astm::Float")
astm_Double = Class(name="astm::Double")
astm_LongDouble = Class(name="astm::LongDouble")
astm_Character = Class(name="astm::Character")
astm_String = Class(name="astm::String")
astm_Boolean = Class(name="astm::Boolean")
astm_WideCharacter = Class(name="astm::WideCharacter")
astm_FileLocal = Class(name="astm::FileLocal")
astm_PerClassMember = Class(name="astm::PerClassMember")
astm_NoDef = Class(name="astm::NoDef")
astm_Virtual = Class(name="astm::Virtual")
VirtualSpecification = Class(name="VirtualSpecification")
astm_PureVirtual = Class(name="astm::PureVirtual")
astm_NonVirtual = Class(name="astm::NonVirtual")
astm_ExceptionType = Class(name="astm::ExceptionType")
astm_Void = Class(name="astm::Void")
PrimitiveType = Class(name="PrimitiveType")
astm_ByValueFormalParameterType = Class(name="astm::ByValueFormalParameterType")
FormalParameterType = Class(name="FormalParameterType")
astm_ByReferenceFormalParameterType = Class(name="astm::ByReferenceFormalParameterType")
astm_Public = Class(name="astm::Public")
AccessKind = Class(name="AccessKind")
astm_Protected = Class(name="astm::Protected")
astm_Private = Class(name="astm::Private")
astm_TerminateStatement = Class(name="astm::TerminateStatement")
astm_DefaultBlock = Class(name="astm::DefaultBlock")
astm_WhileStatement = Class(name="astm::WhileStatement")
astm_DoWhileStatement = Class(name="astm::DoWhileStatement")
astm_ForCheckBeforeStatement = Class(name="astm::ForCheckBeforeStatement")
ForStatement = Class(name="ForStatement")
astm_ForCheckAfterStatement = Class(name="astm::ForCheckAfterStatement")
astm_CollectionType = Class(name="astm::CollectionType")
astm_PointerType = Class(name="astm::PointerType")
astm_ReferenceType = Class(name="astm::ReferenceType")
astm_RangeType = Class(name="astm::RangeType")
astm_StructureType = Class(name="astm::StructureType")
astm_UnionType = Class(name="astm::UnionType")
astm_AnnotationType = Class(name="astm::AnnotationType")
astm_BitLiteral = Class(name="astm::BitLiteral")
astm_UnaryPlus = Class(name="astm::UnaryPlus")
UnaryOperator = Class(name="UnaryOperator")
astm_Negate = Class(name="astm::Negate")
astm_Not = Class(name="astm::Not")
astm_BitNot = Class(name="astm::BitNot")
astm_AddressOf = Class(name="astm::AddressOf")
astm_Deref = Class(name="astm::Deref")
astm_Increment = Class(name="astm::Increment")
astm_Decrement = Class(name="astm::Decrement")
astm_PostIncrement = Class(name="astm::PostIncrement")
astm_PostDecrement = Class(name="astm::PostDecrement")
astm_AggregateExpression = Class(name="astm::AggregateExpression")
astm_QualifiedOverPointer = Class(name="astm::QualifiedOverPointer")
QualifiedIdentifierReference = Class(name="QualifiedIdentifierReference")
astm_QualifiedOverData = Class(name="astm::QualifiedOverData")
astm_IntegerLiteral = Class(name="astm::IntegerLiteral")
Literal = Class(name="Literal")
astm_StringLiteral = Class(name="astm::StringLiteral")
astm_CharLiteral = Class(name="astm::CharLiteral")
astm_RealLiteral = Class(name="astm::RealLiteral")
astm_BooleanLiteral = Class(name="astm::BooleanLiteral")
astm_Equal = Class(name="astm::Equal")
astm_NotEqual = Class(name="astm::NotEqual")
astm_Greater = Class(name="astm::Greater")
astm_NotGreater = Class(name="astm::NotGreater")
astm_Less = Class(name="astm::Less")
astm_NotLess = Class(name="astm::NotLess")
astm_BitAnd = Class(name="astm::BitAnd")
astm_BitOr = Class(name="astm::BitOr")
astm_BitXor = Class(name="astm::BitXor")
astm_BitLeftShift = Class(name="astm::BitLeftShift")
astm_BitRightShift = Class(name="astm::BitRightShift")
astm_Assign = Class(name="astm::Assign")
astm_Add = Class(name="astm::Add")
astm_Subtract = Class(name="astm::Subtract")
astm_Multiply = Class(name="astm::Multiply")
astm_Divide = Class(name="astm::Divide")
astm_Modulus = Class(name="astm::Modulus")
astm_Exponent = Class(name="astm::Exponent")
astm_And = Class(name="astm::And")
astm_Or = Class(name="astm::Or")
astm_SpecificGreaterEqual = Class(name="astm::SpecificGreaterEqual")
astm_SpecificIn = Class(name="astm::SpecificIn")
astm_SpecificLike = Class(name="astm::SpecificLike")
astm_SpecificConcatString = Class(name="astm::SpecificConcatString")
astm_SpecificSelectStatement = Class(name="astm::SpecificSelectStatement")
astm_Visitable = Class(name="astm::Visitable", is_abstract=True)
astm_Operator = Class(name="astm::Operator")
astm_MissingActualParameter = Class(name="astm::MissingActualParameter")
astm_ByValueActualParameterExpression = Class(name="astm::ByValueActualParameterExpression")
ActualParameterExpression = Class(name="ActualParameterExpression")
astm_ByReferenceActualParameterExpression = Class(name="astm::ByReferenceActualParameterExpression")
astm_SpecificTriggerDefinition = Class(name="astm::SpecificTriggerDefinition")
astm_SpecificLessEqual = Class(name="astm::SpecificLessEqual")

# astm_DelphiImplementationSection class attributes and methods

# astm_NamedTypeReference class attributes and methods

# astm_DelphiBlockStatement class attributes and methods

# BlockStatement class attributes and methods

# astm_DefinitionObject class attributes and methods

# astm_DelphiFunctionCallExpression class attributes and methods

# FunctionCallExpression class attributes and methods

# astm_DelphiUnit class attributes and methods

# CompilationUnit class attributes and methods

# astm_Name class attributes and methods
astm_Name_nameString: Property = Property(name="nameString", type=StringType)
astm_Name.attributes={astm_Name_nameString}

# astm_DelphiInterfaceSection class attributes and methods

# astm_DataType class attributes and methods

# Type class attributes and methods

# astm_AccessKind class attributes and methods

# astm_UnaryOperator class attributes and methods

# Operator class attributes and methods

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
astm_SourceLocation.attributes={astm_SourceLocation_endColumn, astm_SourceLocation_startColumn, astm_SourceLocation_endLine, astm_SourceLocation_startLine}

# astm_Project class attributes and methods

# GASTMSemanticObject class attributes and methods

# astm_CompilationUnit class attributes and methods
astm_CompilationUnit_language: Property = Property(name="language", type=StringType)
astm_CompilationUnit.attributes={astm_CompilationUnit_language}

# astm_DelphiWithStatement class attributes and methods

# astm_GASTMObject class attributes and methods

# Visitable class attributes and methods

# astm_GASTMSourceObject class attributes and methods

# astm_GASTMSemanticObject class attributes and methods

# astm_OtherSyntaxObject class attributes and methods

# GASTMSyntaxObject class attributes and methods

# astm_StorageSpecification class attributes and methods

# astm_PreprocessorElement class attributes and methods

# astm_AnnotationExpression class attributes and methods

# OtherSyntaxObject class attributes and methods

# astm_ProgramScope class attributes and methods

# astm_DeclarationOrDefinition class attributes and methods
astm_DeclarationOrDefinition_isRegister: Property = Property(name="isRegister", type=BooleanType)
astm_DeclarationOrDefinition_linkageSpecifier: Property = Property(name="linkageSpecifier", type=StringType)
astm_DeclarationOrDefinition.attributes={astm_DeclarationOrDefinition_isRegister, astm_DeclarationOrDefinition_linkageSpecifier}

# DefinitionObject class attributes and methods

# astm_GlobalScope class attributes and methods

# astm_Scope class attributes and methods

# astm_GASTMSyntaxObject class attributes and methods

# GASTMObject class attributes and methods

# astm_FunctionDeclaration class attributes and methods

# Declaration class attributes and methods

# astm_FormalParameterDeclaration class attributes and methods

# astm_FunctionMemberAttributes class attributes and methods
astm_FunctionMemberAttributes_isInline: Property = Property(name="isInline", type=BooleanType)
astm_FunctionMemberAttributes_isThisConst: Property = Property(name="isThisConst", type=BooleanType)
astm_FunctionMemberAttributes_isFriend: Property = Property(name="isFriend", type=BooleanType)
astm_FunctionMemberAttributes.attributes={astm_FunctionMemberAttributes_isFriend, astm_FunctionMemberAttributes_isInline, astm_FunctionMemberAttributes_isThisConst}

# astm_VariableDeclaration class attributes and methods
astm_VariableDeclaration_isMutable: Property = Property(name="isMutable", type=BooleanType)
astm_VariableDeclaration.attributes={astm_VariableDeclaration_isMutable}

# astm_FunctionDefinition class attributes and methods

# Definition class attributes and methods

# astm_FormalParameterDefinition class attributes and methods

# astm_Definition class attributes and methods

# DeclarationOrDefinition class attributes and methods

# astm_TypeReference class attributes and methods

# astm_Declaration class attributes and methods

# astm_VirtualSpecification class attributes and methods

# astm_EntryDefinition class attributes and methods

# astm_DataDefinition class attributes and methods
astm_DataDefinition_isMutable: Property = Property(name="isMutable", type=BooleanType)
astm_DataDefinition.attributes={astm_DataDefinition_isMutable}

# astm_Expression class attributes and methods

# astm_BitFieldDefinition class attributes and methods

# DataDefinition class attributes and methods

# astm_Statement class attributes and methods

# astm_FunctionScope class attributes and methods

# astm_NameSpaceDefinition class attributes and methods

# astm_NameSpaceType class attributes and methods

# astm_LabelDefinition class attributes and methods

# astm_LabelType class attributes and methods

# astm_IncludeUnit class attributes and methods

# PreprocessorElement class attributes and methods

# astm_MacroCall class attributes and methods

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

# astm_Dimension class attributes and methods

# astm_MacroDefinition class attributes and methods
astm_MacroDefinition_macroName: Property = Property(name="macroName", type=StringType)
astm_MacroDefinition_body: Property = Property(name="body", type=StringType)
astm_MacroDefinition.attributes={astm_MacroDefinition_macroName, astm_MacroDefinition_body}

# astm_Comment class attributes and methods
astm_Comment_text: Property = Property(name="text", type=StringType)
astm_Comment.attributes={astm_Comment_text}

# astm_Type class attributes and methods
astm_Type_isConst: Property = Property(name="isConst", type=BooleanType)
astm_Type_isVolatile: Property = Property(name="isVolatile", type=BooleanType)
astm_Type.attributes={astm_Type_isVolatile, astm_Type_isConst}

# astm_PrimitiveType class attributes and methods
astm_PrimitiveType_isSigned: Property = Property(name="isSigned", type=BooleanType)
astm_PrimitiveType.attributes={astm_PrimitiveType_isSigned}

# DataType class attributes and methods

# astm_ClassType class attributes and methods

# AggregateType class attributes and methods

# astm_DerivesFrom class attributes and methods
astm_DerivesFrom_isVirtual: Property = Property(name="isVirtual", type=BooleanType)
astm_DerivesFrom.attributes={astm_DerivesFrom_isVirtual}

# astm_UnnamedTypeReference class attributes and methods

# TypeReference class attributes and methods

# astm_FunctionType class attributes and methods

# astm_BreakStatement class attributes and methods

# astm_LabelAccess class attributes and methods

# astm_FormalParameterType class attributes and methods

# astm_ContinueStatement class attributes and methods

# astm_LabeledStatement class attributes and methods

# astm_BlockStatement class attributes and methods

# astm_BlockScope class attributes and methods

# astm_DeleteStatement class attributes and methods

# Statement class attributes and methods

# astm_DeclarationOrDefinitionStatement class attributes and methods

# astm_ExpressionStatement class attributes and methods

# astm_JumpStatement class attributes and methods

# astm_ReturnStatement class attributes and methods

# astm_LoopStatement class attributes and methods

# astm_ForStatement class attributes and methods

# LoopStatement class attributes and methods

# astm_TryStatement class attributes and methods

# astm_CatchBlock class attributes and methods

# astm_EmptyStatement class attributes and methods

# astm_IfStatement class attributes and methods

# astm_SwitchStatement class attributes and methods

# astm_SwitchCase class attributes and methods

# astm_CaseBlock class attributes and methods

# SwitchCase class attributes and methods

# astm_VariableCatchBlock class attributes and methods

# astm_ThrowStatement class attributes and methods

# astm_TypesCatchBlock class attributes and methods

# CatchBlock class attributes and methods

# astm_QualifiedIdentifierReference class attributes and methods

# NameReference class attributes and methods

# astm_IdentifierReference class attributes and methods

# astm_TypeQualifiedIdentifierReference class attributes and methods

# astm_NameReference class attributes and methods

# Expression class attributes and methods

# astm_ArrayAccess class attributes and methods

# astm_UnaryExpression class attributes and methods

# astm_BinaryExpression class attributes and methods

# astm_Literal class attributes and methods
astm_Literal_value: Property = Property(name="value", type=StringType)
astm_Literal.attributes={astm_Literal_value}

# astm_CastExpression class attributes and methods

# astm_ConditionalExpression class attributes and methods

# astm_OperatorAssign class attributes and methods

# BinaryOperator class attributes and methods

# astm_FunctionCallExpression class attributes and methods

# astm_ActualParameterExpression class attributes and methods

# ActualParameter class attributes and methods

# astm_RangeExpression class attributes and methods

# astm_NewExpression class attributes and methods

# astm_VariableDefinition class attributes and methods

# astm_FunctionMemberAttribute class attributes and methods

# astm_External class attributes and methods

# StorageSpecification class attributes and methods

# astm_FunctionPersistent class attributes and methods

# Scope class attributes and methods

# astm_Byte class attributes and methods

# astm_ShortInteger class attributes and methods

# astm_Integer class attributes and methods

# astm_LongInteger class attributes and methods

# astm_Float class attributes and methods

# astm_Double class attributes and methods

# astm_LongDouble class attributes and methods

# astm_Character class attributes and methods

# astm_String class attributes and methods

# astm_Boolean class attributes and methods

# astm_WideCharacter class attributes and methods

# astm_FileLocal class attributes and methods

# astm_PerClassMember class attributes and methods

# astm_NoDef class attributes and methods

# astm_Virtual class attributes and methods

# VirtualSpecification class attributes and methods

# astm_PureVirtual class attributes and methods

# astm_NonVirtual class attributes and methods

# astm_ExceptionType class attributes and methods

# astm_Void class attributes and methods

# PrimitiveType class attributes and methods

# astm_ByValueFormalParameterType class attributes and methods

# FormalParameterType class attributes and methods

# astm_ByReferenceFormalParameterType class attributes and methods

# astm_Public class attributes and methods

# AccessKind class attributes and methods

# astm_Protected class attributes and methods

# astm_Private class attributes and methods

# astm_TerminateStatement class attributes and methods

# astm_DefaultBlock class attributes and methods

# astm_WhileStatement class attributes and methods

# astm_DoWhileStatement class attributes and methods

# astm_ForCheckBeforeStatement class attributes and methods

# ForStatement class attributes and methods

# astm_ForCheckAfterStatement class attributes and methods

# astm_CollectionType class attributes and methods

# astm_PointerType class attributes and methods

# astm_ReferenceType class attributes and methods

# astm_RangeType class attributes and methods

# astm_StructureType class attributes and methods

# astm_UnionType class attributes and methods

# astm_AnnotationType class attributes and methods

# astm_BitLiteral class attributes and methods

# astm_UnaryPlus class attributes and methods

# UnaryOperator class attributes and methods

# astm_Negate class attributes and methods

# astm_Not class attributes and methods

# astm_BitNot class attributes and methods

# astm_AddressOf class attributes and methods

# astm_Deref class attributes and methods

# astm_Increment class attributes and methods

# astm_Decrement class attributes and methods

# astm_PostIncrement class attributes and methods

# astm_PostDecrement class attributes and methods

# astm_AggregateExpression class attributes and methods

# astm_QualifiedOverPointer class attributes and methods

# QualifiedIdentifierReference class attributes and methods

# astm_QualifiedOverData class attributes and methods

# astm_IntegerLiteral class attributes and methods

# Literal class attributes and methods

# astm_StringLiteral class attributes and methods

# astm_CharLiteral class attributes and methods

# astm_RealLiteral class attributes and methods

# astm_BooleanLiteral class attributes and methods

# astm_Equal class attributes and methods

# astm_NotEqual class attributes and methods

# astm_Greater class attributes and methods

# astm_NotGreater class attributes and methods

# astm_Less class attributes and methods

# astm_NotLess class attributes and methods

# astm_BitAnd class attributes and methods

# astm_BitOr class attributes and methods

# astm_BitXor class attributes and methods

# astm_BitLeftShift class attributes and methods

# astm_BitRightShift class attributes and methods

# astm_Assign class attributes and methods

# astm_Add class attributes and methods

# astm_Subtract class attributes and methods

# astm_Multiply class attributes and methods

# astm_Divide class attributes and methods

# astm_Modulus class attributes and methods

# astm_Exponent class attributes and methods

# astm_And class attributes and methods

# astm_Or class attributes and methods

# astm_SpecificGreaterEqual class attributes and methods

# astm_SpecificIn class attributes and methods

# astm_SpecificLike class attributes and methods

# astm_SpecificConcatString class attributes and methods

# astm_SpecificSelectStatement class attributes and methods

# astm_Visitable class attributes and methods

# astm_Operator class attributes and methods

# astm_MissingActualParameter class attributes and methods

# astm_ByValueActualParameterExpression class attributes and methods

# ActualParameterExpression class attributes and methods

# astm_ByReferenceActualParameterExpression class attributes and methods

# astm_SpecificTriggerDefinition class attributes and methods

# astm_SpecificLessEqual class attributes and methods

# Relationships
implementation3: BinaryAssociation = BinaryAssociation(
    name="implementation3",
    ends={
        Property(name="astm_DelphiImplementationSection", type=astm_DelphiUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DelphiUnit4", type=astm_DelphiImplementationSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uses5: BinaryAssociation = BinaryAssociation(
    name="uses5",
    ends={
        Property(name="astm_NamedTypeReference", type=astm_DelphiInterfaceSection, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DelphiInterfaceSection6", type=astm_NamedTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uses7: BinaryAssociation = BinaryAssociation(
    name="uses7",
    ends={
        Property(name="astm_NamedTypeReference9", type=astm_DelphiImplementationSection, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DelphiImplementationSection8", type=astm_NamedTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exports10: BinaryAssociation = BinaryAssociation(
    name="exports10",
    ends={
        Property(name="astm_NamedTypeReference12", type=astm_DelphiImplementationSection, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DelphiImplementationSection11", type=astm_NamedTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exports13: BinaryAssociation = BinaryAssociation(
    name="exports13",
    ends={
        Property(name="astm_NamedTypeReference14", type=astm_DelphiBlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DelphiBlockStatement", type=astm_NamedTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations15: BinaryAssociation = BinaryAssociation(
    name="declarations15",
    ends={
        Property(name="astm_DefinitionObject", type=astm_DelphiBlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DelphiBlockStatement16", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name0: BinaryAssociation = BinaryAssociation(
    name="name0",
    ends={
        Property(name="astm_Name", type=astm_DelphiUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DelphiUnit", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interface1: BinaryAssociation = BinaryAssociation(
    name="interface1",
    ends={
        Property(name="astm_DelphiInterfaceSection", type=astm_DelphiUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DelphiUnit2", type=astm_DelphiInterfaceSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inSourceFile21: BinaryAssociation = BinaryAssociation(
    name="inSourceFile21",
    ends={
        Property(name="astm_SourceFile", type=astm_SourceLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SourceLocation", type=astm_SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applyTo17: BinaryAssociation = BinaryAssociation(
    name="applyTo17",
    ends={
        Property(name="astm_DefinitionObject18", type=astm_DelphiFunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DelphiFunctionCallExpression", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 1))
    }
)
withs19: BinaryAssociation = BinaryAssociation(
    name="withs19",
    ends={
        Property(name="astm_DefinitionObject20", type=astm_DelphiWithStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DelphiWithStatement", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 9999))
    }
)
preProcessorElements32: BinaryAssociation = BinaryAssociation(
    name="preProcessorElements32",
    ends={
        Property(name="astm_PreprocessorElement", type=astm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_GASTMSyntaxObject33", type=astm_PreprocessorElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations34: BinaryAssociation = BinaryAssociation(
    name="annotations34",
    ends={
        Property(name="astm_AnnotationExpression", type=astm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_GASTMSyntaxObject35", type=astm_AnnotationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments36: BinaryAssociation = BinaryAssociation(
    name="fragments36",
    ends={
        Property(name="astm_DefinitionObject38", type=astm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CompilationUnit37", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope39: BinaryAssociation = BinaryAssociation(
    name="opensScope39",
    ends={
        Property(name="astm_ProgramScope", type=astm_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CompilationUnit40", type=astm_ProgramScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
storageSpecifiers41: BinaryAssociation = BinaryAssociation(
    name="storageSpecifiers41",
    ends={
        Property(name="astm_OtherSyntaxObject", type=astm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeclarationOrDefinition", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
files22: BinaryAssociation = BinaryAssociation(
    name="files22",
    ends={
        Property(name="astm_CompilationUnit", type=astm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Project", type=astm_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outerScope23: BinaryAssociation = BinaryAssociation(
    name="outerScope23",
    ends={
        Property(name="astm_GlobalScope", type=astm_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Project24", type=astm_GlobalScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionObject25: BinaryAssociation = BinaryAssociation(
    name="definitionObject25",
    ends={
        Property(name="astm_DefinitionObject26", type=astm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Scope", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childScope28: BinaryAssociation = BinaryAssociation(
    name="childScope28",
    ends={
        Property(name="astm_Scope29", type=astm_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Scope27", type=astm_Scope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locationInfo30: BinaryAssociation = BinaryAssociation(
    name="locationInfo30",
    ends={
        Property(name="astm_SourceLocation31", type=astm_GASTMSyntaxObject, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_GASTMSyntaxObject", type=astm_SourceLocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierName51: BinaryAssociation = BinaryAssociation(
    name="identifierName51",
    ends={
        Property(name="astm_Name53", type=astm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Declaration52", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarationType54: BinaryAssociation = BinaryAssociation(
    name="declarationType54",
    ends={
        Property(name="astm_TypeReference56", type=astm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Declaration55", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters57: BinaryAssociation = BinaryAssociation(
    name="formalParameters57",
    ends={
        Property(name="astm_FormalParameterDeclaration", type=astm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDeclaration", type=astm_FormalParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes58: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes58",
    ends={
        Property(name="astm_FunctionMemberAttributes", type=astm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDeclaration59", type=astm_FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType60: BinaryAssociation = BinaryAssociation(
    name="returnType60",
    ends={
        Property(name="astm_TypeReference62", type=astm_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDeclaration61", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType63: BinaryAssociation = BinaryAssociation(
    name="returnType63",
    ends={
        Property(name="astm_TypeReference64", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters65: BinaryAssociation = BinaryAssociation(
    name="formalParameters65",
    ends={
        Property(name="astm_FormalParameterDefinition", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition66", type=astm_FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessKind42: BinaryAssociation = BinaryAssociation(
    name="accessKind42",
    ends={
        Property(name="astm_OtherSyntaxObject44", type=astm_DeclarationOrDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeclarationOrDefinition43", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierName45: BinaryAssociation = BinaryAssociation(
    name="identifierName45",
    ends={
        Property(name="astm_Name46", type=astm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Definition", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType47: BinaryAssociation = BinaryAssociation(
    name="definitionType47",
    ends={
        Property(name="astm_TypeReference", type=astm_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Definition48", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defRef49: BinaryAssociation = BinaryAssociation(
    name="defRef49",
    ends={
        Property(name="astm_Definition50", type=astm_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Declaration", type=astm_Definition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
virtualSpecifier74: BinaryAssociation = BinaryAssociation(
    name="virtualSpecifier74",
    ends={
        Property(name="astm_VirtualSpecification", type=astm_FunctionMemberAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionMemberAttributes75", type=astm_VirtualSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters76: BinaryAssociation = BinaryAssociation(
    name="formalParameters76",
    ends={
        Property(name="astm_FormalParameterDefinition77", type=astm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EntryDefinition", type=astm_FormalParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body78: BinaryAssociation = BinaryAssociation(
    name="body78",
    ends={
        Property(name="astm_Statement80", type=astm_EntryDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EntryDefinition79", type=astm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue81: BinaryAssociation = BinaryAssociation(
    name="initialValue81",
    ends={
        Property(name="astm_Expression", type=astm_DataDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DataDefinition", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bitFieldSize82: BinaryAssociation = BinaryAssociation(
    name="bitFieldSize82",
    ends={
        Property(name="astm_Expression83", type=astm_BitFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BitFieldDefinition", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body67: BinaryAssociation = BinaryAssociation(
    name="body67",
    ends={
        Property(name="astm_Statement", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition68", type=astm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMemberAttributes69: BinaryAssociation = BinaryAssociation(
    name="functionMemberAttributes69",
    ends={
        Property(name="astm_FunctionMemberAttributes71", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition70", type=astm_FunctionMemberAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opensScope72: BinaryAssociation = BinaryAssociation(
    name="opensScope72",
    ends={
        Property(name="astm_FunctionScope", type=astm_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionDefinition73", type=astm_FunctionScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameSpace90: BinaryAssociation = BinaryAssociation(
    name="nameSpace90",
    ends={
        Property(name="astm_Name91", type=astm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameSpaceDefinition", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body92: BinaryAssociation = BinaryAssociation(
    name="body92",
    ends={
        Property(name="astm_DefinitionObject94", type=astm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameSpaceDefinition93", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameSpaceType95: BinaryAssociation = BinaryAssociation(
    name="nameSpaceType95",
    ends={
        Property(name="astm_NameSpaceType", type=astm_NameSpaceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameSpaceDefinition96", type=astm_NameSpaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelName97: BinaryAssociation = BinaryAssociation(
    name="labelName97",
    ends={
        Property(name="astm_Name98", type=astm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelDefinition", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelType99: BinaryAssociation = BinaryAssociation(
    name="labelType99",
    ends={
        Property(name="astm_LabelType", type=astm_LabelDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelDefinition100", type=astm_LabelType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file101: BinaryAssociation = BinaryAssociation(
    name="file101",
    ends={
        Property(name="astm_SourceFile102", type=astm_IncludeUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IncludeUnit", type=astm_SourceFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value84: BinaryAssociation = BinaryAssociation(
    name="value84",
    ends={
        Property(name="astm_Expression85", type=astm_EnumLiteralDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EnumLiteralDefinition", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name86: BinaryAssociation = BinaryAssociation(
    name="name86",
    ends={
        Property(name="astm_Name87", type=astm_TypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypeDefinition", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionType88: BinaryAssociation = BinaryAssociation(
    name="definitionType88",
    ends={
        Property(name="astm_NamedType", type=astm_NamedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedTypeDefinition", type=astm_NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType89: BinaryAssociation = BinaryAssociation(
    name="aggregateType89",
    ends={
        Property(name="astm_AggregateType", type=astm_AggregateTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AggregateTypeDefinition", type=astm_AggregateType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumLiterals104: BinaryAssociation = BinaryAssociation(
    name="enumLiterals104",
    ends={
        Property(name="astm_EnumLiteralDefinition105", type=astm_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_EnumType", type=astm_EnumLiteralDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType106: BinaryAssociation = BinaryAssociation(
    name="baseType106",
    ends={
        Property(name="astm_TypeReference107", type=astm_ConstructedType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConstructedType", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members108: BinaryAssociation = BinaryAssociation(
    name="members108",
    ends={
        Property(name="astm_DefinitionObject110", type=astm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AggregateType109", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope111: BinaryAssociation = BinaryAssociation(
    name="opensScope111",
    ends={
        Property(name="astm_AggregateScope", type=astm_AggregateType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AggregateType112", type=astm_AggregateScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ranks113: BinaryAssociation = BinaryAssociation(
    name="ranks113",
    ends={
        Property(name="astm_Dimension", type=astm_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ArrayType", type=astm_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refersTo103: BinaryAssociation = BinaryAssociation(
    name="refersTo103",
    ends={
        Property(name="astm_MacroDefinition", type=astm_MacroCall, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_MacroCall", type=astm_MacroDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterTypes122: BinaryAssociation = BinaryAssociation(
    name="parameterTypes122",
    ends={
        Property(name="astm_FormalParameterType", type=astm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionType123", type=astm_FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type124: BinaryAssociation = BinaryAssociation(
    name="type124",
    ends={
        Property(name="astm_TypeReference126", type=astm_FormalParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FormalParameterType125", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body127: BinaryAssociation = BinaryAssociation(
    name="body127",
    ends={
        Property(name="astm_Type", type=astm_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedType128", type=astm_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivesFrom129: BinaryAssociation = BinaryAssociation(
    name="derivesFrom129",
    ends={
        Property(name="astm_DerivesFrom", type=astm_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ClassType", type=astm_DerivesFrom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessKind130: BinaryAssociation = BinaryAssociation(
    name="accessKind130",
    ends={
        Property(name="astm_OtherSyntaxObject132", type=astm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DerivesFrom131", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className133: BinaryAssociation = BinaryAssociation(
    name="className133",
    ends={
        Property(name="astm_NamedType135", type=astm_DerivesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DerivesFrom134", type=astm_NamedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowBound114: BinaryAssociation = BinaryAssociation(
    name="lowBound114",
    ends={
        Property(name="astm_Expression116", type=astm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Dimension115", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
highBound117: BinaryAssociation = BinaryAssociation(
    name="highBound117",
    ends={
        Property(name="astm_Expression119", type=astm_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Dimension118", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target150: BinaryAssociation = BinaryAssociation(
    name="target150",
    ends={
        Property(name="astm_Expression151", type=astm_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_JumpStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType120: BinaryAssociation = BinaryAssociation(
    name="returnType120",
    ends={
        Property(name="astm_TypeReference121", type=astm_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionType", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target152: BinaryAssociation = BinaryAssociation(
    name="target152",
    ends={
        Property(name="astm_LabelAccess", type=astm_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BreakStatement", type=astm_LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target153: BinaryAssociation = BinaryAssociation(
    name="target153",
    ends={
        Property(name="astm_LabelAccess154", type=astm_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ContinueStatement", type=astm_LabelAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label155: BinaryAssociation = BinaryAssociation(
    name="label155",
    ends={
        Property(name="astm_LabelDefinition156", type=astm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabeledStatement", type=astm_LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement157: BinaryAssociation = BinaryAssociation(
    name="statement157",
    ends={
        Property(name="astm_Statement159", type=astm_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabeledStatement158", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subStatements160: BinaryAssociation = BinaryAssociation(
    name="subStatements160",
    ends={
        Property(name="astm_Statement161", type=astm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BlockStatement", type=astm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opensScope162: BinaryAssociation = BinaryAssociation(
    name="opensScope162",
    ends={
        Property(name="astm_BlockScope", type=astm_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BlockStatement163", type=astm_BlockScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type136: BinaryAssociation = BinaryAssociation(
    name="type136",
    ends={
        Property(name="astm_Type137", type=astm_UnnamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_UnnamedTypeReference", type=astm_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name138: BinaryAssociation = BinaryAssociation(
    name="name138",
    ends={
        Property(name="astm_Name140", type=astm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedTypeReference139", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type141: BinaryAssociation = BinaryAssociation(
    name="type141",
    ends={
        Property(name="astm_TypeDefinition143", type=astm_NamedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NamedTypeReference142", type=astm_TypeDefinition, multiplicity=Multiplicity(0, 1))
    }
)
operand144: BinaryAssociation = BinaryAssociation(
    name="operand144",
    ends={
        Property(name="astm_Expression145", type=astm_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeleteStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declOrDefn146: BinaryAssociation = BinaryAssociation(
    name="declOrDefn146",
    ends={
        Property(name="astm_DefinitionObject147", type=astm_DeclarationOrDefinitionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_DeclarationOrDefinitionStatement", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression148: BinaryAssociation = BinaryAssociation(
    name="expression148",
    ends={
        Property(name="astm_Expression149", type=astm_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ExpressionStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValue181: BinaryAssociation = BinaryAssociation(
    name="returnValue181",
    ends={
        Property(name="astm_Expression182", type=astm_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ReturnStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition183: BinaryAssociation = BinaryAssociation(
    name="condition183",
    ends={
        Property(name="astm_Expression184", type=astm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LoopStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body185: BinaryAssociation = BinaryAssociation(
    name="body185",
    ends={
        Property(name="astm_Statement187", type=astm_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LoopStatement186", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initBody188: BinaryAssociation = BinaryAssociation(
    name="initBody188",
    ends={
        Property(name="astm_Expression189", type=astm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ForStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationBody190: BinaryAssociation = BinaryAssociation(
    name="iterationBody190",
    ends={
        Property(name="astm_Expression192", type=astm_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ForStatement191", type=astm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guardedStatement193: BinaryAssociation = BinaryAssociation(
    name="guardedStatement193",
    ends={
        Property(name="astm_Statement194", type=astm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TryStatement", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchBlocks195: BinaryAssociation = BinaryAssociation(
    name="catchBlocks195",
    ends={
        Property(name="astm_CatchBlock", type=astm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TryStatement196", type=astm_CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition164: BinaryAssociation = BinaryAssociation(
    name="condition164",
    ends={
        Property(name="astm_Expression165", type=astm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IfStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBody166: BinaryAssociation = BinaryAssociation(
    name="thenBody166",
    ends={
        Property(name="astm_Statement168", type=astm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IfStatement167", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBody169: BinaryAssociation = BinaryAssociation(
    name="elseBody169",
    ends={
        Property(name="astm_Statement171", type=astm_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_IfStatement170", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchExpression172: BinaryAssociation = BinaryAssociation(
    name="switchExpression172",
    ends={
        Property(name="astm_Expression173", type=astm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SwitchStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases174: BinaryAssociation = BinaryAssociation(
    name="cases174",
    ends={
        Property(name="astm_SwitchCase", type=astm_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SwitchStatement175", type=astm_SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body176: BinaryAssociation = BinaryAssociation(
    name="body176",
    ends={
        Property(name="astm_Statement178", type=astm_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SwitchCase177", type=astm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caseExpressions179: BinaryAssociation = BinaryAssociation(
    name="caseExpressions179",
    ends={
        Property(name="astm_Expression180", type=astm_CaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CaseBlock", type=astm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions203: BinaryAssociation = BinaryAssociation(
    name="exceptions203",
    ends={
        Property(name="astm_Type204", type=astm_TypesCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypesCatchBlock", type=astm_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionVariable205: BinaryAssociation = BinaryAssociation(
    name="exceptionVariable205",
    ends={
        Property(name="astm_DataDefinition206", type=astm_VariableCatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_VariableCatchBlock", type=astm_DataDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception207: BinaryAssociation = BinaryAssociation(
    name="exception207",
    ends={
        Property(name="astm_Expression208", type=astm_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ThrowStatement", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionType209: BinaryAssociation = BinaryAssociation(
    name="expressionType209",
    ends={
        Property(name="astm_TypeReference211", type=astm_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_Expression210", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalStatement197: BinaryAssociation = BinaryAssociation(
    name="finalStatement197",
    ends={
        Property(name="astm_Statement199", type=astm_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TryStatement198", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body200: BinaryAssociation = BinaryAssociation(
    name="body200",
    ends={
        Property(name="astm_Statement202", type=astm_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CatchBlock201", type=astm_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subscripts219: BinaryAssociation = BinaryAssociation(
    name="subscripts219",
    ends={
        Property(name="astm_Expression221", type=astm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ArrayAccess220", type=astm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifiers222: BinaryAssociation = BinaryAssociation(
    name="qualifiers222",
    ends={
        Property(name="astm_Expression223", type=astm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_QualifiedIdentifierReference", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member224: BinaryAssociation = BinaryAssociation(
    name="member224",
    ends={
        Property(name="astm_IdentifierReference", type=astm_QualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_QualifiedIdentifierReference225", type=astm_IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregateType226: BinaryAssociation = BinaryAssociation(
    name="aggregateType226",
    ends={
        Property(name="astm_TypeReference227", type=astm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypeQualifiedIdentifierReference", type=astm_TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member228: BinaryAssociation = BinaryAssociation(
    name="member228",
    ends={
        Property(name="astm_IdentifierReference230", type=astm_TypeQualifiedIdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_TypeQualifiedIdentifierReference229", type=astm_IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name212: BinaryAssociation = BinaryAssociation(
    name="name212",
    ends={
        Property(name="astm_Name213", type=astm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameReference", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo214: BinaryAssociation = BinaryAssociation(
    name="refersTo214",
    ends={
        Property(name="astm_DefinitionObject216", type=astm_NameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NameReference215", type=astm_DefinitionObject, multiplicity=Multiplicity(0, 1))
    }
)
arrayName217: BinaryAssociation = BinaryAssociation(
    name="arrayName217",
    ends={
        Property(name="astm_Expression218", type=astm_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ArrayAccess", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator236: BinaryAssociation = BinaryAssociation(
    name="operator236",
    ends={
        Property(name="astm_OtherSyntaxObject237", type=astm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_UnaryExpression", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand238: BinaryAssociation = BinaryAssociation(
    name="operand238",
    ends={
        Property(name="astm_Expression240", type=astm_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_UnaryExpression239", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator241: BinaryAssociation = BinaryAssociation(
    name="operator241",
    ends={
        Property(name="astm_OtherSyntaxObject242", type=astm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BinaryExpression", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
castType231: BinaryAssociation = BinaryAssociation(
    name="castType231",
    ends={
        Property(name="astm_TypeReference232", type=astm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CastExpression", type=astm_TypeReference, multiplicity=Multiplicity(0, 1))
    }
)
operator249: BinaryAssociation = BinaryAssociation(
    name="operator249",
    ends={
        Property(name="astm_OperatorAssign", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="astm_OtherSyntaxObject250", type=astm_OperatorAssign, multiplicity=Multiplicity(1, 1))
    }
)
expression233: BinaryAssociation = BinaryAssociation(
    name="expression233",
    ends={
        Property(name="astm_Expression235", type=astm_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_CastExpression234", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition251: BinaryAssociation = BinaryAssociation(
    name="condition251",
    ends={
        Property(name="astm_Expression252", type=astm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConditionalExpression", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onTrueOperand253: BinaryAssociation = BinaryAssociation(
    name="onTrueOperand253",
    ends={
        Property(name="astm_Expression255", type=astm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConditionalExpression254", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onFalseOperand256: BinaryAssociation = BinaryAssociation(
    name="onFalseOperand256",
    ends={
        Property(name="astm_Expression258", type=astm_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ConditionalExpression257", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand243: BinaryAssociation = BinaryAssociation(
    name="leftOperand243",
    ends={
        Property(name="astm_Expression245", type=astm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BinaryExpression244", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand246: BinaryAssociation = BinaryAssociation(
    name="rightOperand246",
    ends={
        Property(name="astm_Expression248", type=astm_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_BinaryExpression247", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
calledFunction264: BinaryAssociation = BinaryAssociation(
    name="calledFunction264",
    ends={
        Property(name="astm_Expression265", type=astm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionCallExpression", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams266: BinaryAssociation = BinaryAssociation(
    name="actualParams266",
    ends={
        Property(name="astm_ActualParameter", type=astm_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_FunctionCallExpression267", type=astm_ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value268: BinaryAssociation = BinaryAssociation(
    name="value268",
    ends={
        Property(name="astm_Expression269", type=astm_ActualParameterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_ActualParameterExpression", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromExpression259: BinaryAssociation = BinaryAssociation(
    name="fromExpression259",
    ends={
        Property(name="astm_Expression260", type=astm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_RangeExpression", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toExpression261: BinaryAssociation = BinaryAssociation(
    name="toExpression261",
    ends={
        Property(name="astm_Expression263", type=astm_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_RangeExpression262", type=astm_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name275: BinaryAssociation = BinaryAssociation(
    name="name275",
    ends={
        Property(name="astm_Name277", type=astm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelAccess276", type=astm_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition278: BinaryAssociation = BinaryAssociation(
    name="definition278",
    ends={
        Property(name="astm_LabelDefinition280", type=astm_LabelAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_LabelAccess279", type=astm_LabelDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationType281: BinaryAssociation = BinaryAssociation(
    name="annotationType281",
    ends={
        Property(name="astm_TypeReference283", type=astm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AnnotationExpression282", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberValues284: BinaryAssociation = BinaryAssociation(
    name="memberValues284",
    ends={
        Property(name="astm_Expression286", type=astm_AnnotationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_AnnotationExpression285", type=astm_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
newType270: BinaryAssociation = BinaryAssociation(
    name="newType270",
    ends={
        Property(name="astm_TypeReference271", type=astm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NewExpression", type=astm_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParams272: BinaryAssociation = BinaryAssociation(
    name="actualParams272",
    ends={
        Property(name="astm_OtherSyntaxObject274", type=astm_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_NewExpression273", type=astm_OtherSyntaxObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body287: BinaryAssociation = BinaryAssociation(
    name="body287",
    ends={
        Property(name="astm_Statement288", type=astm_SpecificTriggerDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="astm_SpecificTriggerDefinition", type=astm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_astm_DelphiInterfaceSection_CompilationUnit = Generalization(general=CompilationUnit, specific=astm_DelphiInterfaceSection)
gen_astm_DelphiImplementationSection_CompilationUnit = Generalization(general=CompilationUnit, specific=astm_DelphiImplementationSection)
gen_astm_DelphiBlockStatement_BlockStatement = Generalization(general=BlockStatement, specific=astm_DelphiBlockStatement)
gen_astm_DelphiUnit_CompilationUnit = Generalization(general=CompilationUnit, specific=astm_DelphiUnit)
gen_astm_DataType_Type = Generalization(general=Type, specific=astm_DataType)
gen_astm_AccessKind_Visitable = Generalization(general=Visitable, specific=astm_AccessKind)
gen_astm_UnaryOperator_Operator = Generalization(general=Operator, specific=astm_UnaryOperator)
gen_astm_BinaryOperator_Operator = Generalization(general=Operator, specific=astm_BinaryOperator)
gen_astm_ActualParameter_Visitable = Generalization(general=Visitable, specific=astm_ActualParameter)
gen_astm_SourceFile_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=astm_SourceFile)
gen_astm_SourceLocation_GASTMSourceObject = Generalization(general=GASTMSourceObject, specific=astm_SourceLocation)
gen_astm_Project_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=astm_Project)
gen_astm_DelphiFunctionCallExpression_FunctionCallExpression = Generalization(general=FunctionCallExpression, specific=astm_DelphiFunctionCallExpression)
gen_astm_DelphiWithStatement_BlockStatement = Generalization(general=BlockStatement, specific=astm_DelphiWithStatement)
gen_astm_GASTMObject_Visitable = Generalization(general=Visitable, specific=astm_GASTMObject)
gen_astm_GASTMSourceObject_Visitable = Generalization(general=Visitable, specific=astm_GASTMSourceObject)
gen_astm_GASTMSemanticObject_Visitable = Generalization(general=Visitable, specific=astm_GASTMSemanticObject)
gen_astm_OtherSyntaxObject_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_OtherSyntaxObject)
gen_astm_StorageSpecification_Visitable = Generalization(general=Visitable, specific=astm_StorageSpecification)
gen_astm_CompilationUnit_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_CompilationUnit)
gen_astm_Name_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_Name)
gen_astm_DeclarationOrDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_DeclarationOrDefinition)
gen_astm_Scope_GASTMSemanticObject = Generalization(general=GASTMSemanticObject, specific=astm_Scope)
gen_astm_GASTMSyntaxObject_GASTMObject = Generalization(general=GASTMObject, specific=astm_GASTMSyntaxObject)
gen_astm_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=astm_FunctionDeclaration)
gen_astm_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=astm_VariableDeclaration)
gen_astm_FunctionDefinition_Definition = Generalization(general=Definition, specific=astm_FunctionDefinition)
gen_astm_Definition_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=astm_Definition)
gen_astm_Declaration_DeclarationOrDefinition = Generalization(general=DeclarationOrDefinition, specific=astm_Declaration)
gen_astm_EntryDefinition_Definition = Generalization(general=Definition, specific=astm_EntryDefinition)
gen_astm_DataDefinition_Definition = Generalization(general=Definition, specific=astm_DataDefinition)
gen_astm_BitFieldDefinition_DataDefinition = Generalization(general=DataDefinition, specific=astm_BitFieldDefinition)
gen_astm_FunctionMemberAttributes_Visitable = Generalization(general=Visitable, specific=astm_FunctionMemberAttributes)
gen_astm_NameSpaceDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_NameSpaceDefinition)
gen_astm_LabelDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_LabelDefinition)
gen_astm_IncludeUnit_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_IncludeUnit)
gen_astm_MacroCall_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_MacroCall)
gen_astm_EnumLiteralDefinition_Definition = Generalization(general=Definition, specific=astm_EnumLiteralDefinition)
gen_astm_TypeDefinition_DefinitionObject = Generalization(general=DefinitionObject, specific=astm_TypeDefinition)
gen_astm_NamedTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=astm_NamedTypeDefinition)
gen_astm_AggregateTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=astm_AggregateTypeDefinition)
gen_astm_EnumType_DataType = Generalization(general=DataType, specific=astm_EnumType)
gen_astm_ConstructedType_DataType = Generalization(general=DataType, specific=astm_ConstructedType)
gen_astm_AggregateType_DataType = Generalization(general=DataType, specific=astm_AggregateType)
gen_astm_ArrayType_ConstructedType = Generalization(general=ConstructedType, specific=astm_ArrayType)
gen_astm_Dimension_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_Dimension)
gen_astm_MacroDefinition_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_MacroDefinition)
gen_astm_Comment_PreprocessorElement = Generalization(general=PreprocessorElement, specific=astm_Comment)
gen_astm_Type_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_Type)
gen_astm_PrimitiveType_DataType = Generalization(general=DataType, specific=astm_PrimitiveType)
gen_astm_FormalParameterType_DataType = Generalization(general=DataType, specific=astm_FormalParameterType)
gen_astm_NamedType_DataType = Generalization(general=DataType, specific=astm_NamedType)
gen_astm_ClassType_AggregateType = Generalization(general=AggregateType, specific=astm_ClassType)
gen_astm_DerivesFrom_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_DerivesFrom)
gen_astm_UnnamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=astm_UnnamedTypeReference)
gen_astm_FunctionType_Type = Generalization(general=Type, specific=astm_FunctionType)
gen_astm_BreakStatement_Statement = Generalization(general=Statement, specific=astm_BreakStatement)
gen_astm_ContinueStatement_Statement = Generalization(general=Statement, specific=astm_ContinueStatement)
gen_astm_LabeledStatement_Statement = Generalization(general=Statement, specific=astm_LabeledStatement)
gen_astm_BlockStatement_Statement = Generalization(general=Statement, specific=astm_BlockStatement)
gen_astm_NamedTypeReference_TypeReference = Generalization(general=TypeReference, specific=astm_NamedTypeReference)
gen_astm_DeleteStatement_Statement = Generalization(general=Statement, specific=astm_DeleteStatement)
gen_astm_DeclarationOrDefinitionStatement_Statement = Generalization(general=Statement, specific=astm_DeclarationOrDefinitionStatement)
gen_astm_ExpressionStatement_Statement = Generalization(general=Statement, specific=astm_ExpressionStatement)
gen_astm_JumpStatement_Statement = Generalization(general=Statement, specific=astm_JumpStatement)
gen_astm_ReturnStatement_Statement = Generalization(general=Statement, specific=astm_ReturnStatement)
gen_astm_LoopStatement_Statement = Generalization(general=Statement, specific=astm_LoopStatement)
gen_astm_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_ForStatement)
gen_astm_TryStatement_Statement = Generalization(general=Statement, specific=astm_TryStatement)
gen_astm_EmptyStatement_Statement = Generalization(general=Statement, specific=astm_EmptyStatement)
gen_astm_IfStatement_Statement = Generalization(general=Statement, specific=astm_IfStatement)
gen_astm_SwitchStatement_Statement = Generalization(general=Statement, specific=astm_SwitchStatement)
gen_astm_SwitchCase_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_SwitchCase)
gen_astm_CaseBlock_SwitchCase = Generalization(general=SwitchCase, specific=astm_CaseBlock)
gen_astm_TypesCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=astm_TypesCatchBlock)
gen_astm_VariableCatchBlock_CatchBlock = Generalization(general=CatchBlock, specific=astm_VariableCatchBlock)
gen_astm_ThrowStatement_Statement = Generalization(general=Statement, specific=astm_ThrowStatement)
gen_astm_Expression_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_Expression)
gen_astm_CatchBlock_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_CatchBlock)
gen_astm_QualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_QualifiedIdentifierReference)
gen_astm_TypeQualifiedIdentifierReference_NameReference = Generalization(general=NameReference, specific=astm_TypeQualifiedIdentifierReference)
gen_astm_NameReference_Expression = Generalization(general=Expression, specific=astm_NameReference)
gen_astm_ArrayAccess_Expression = Generalization(general=Expression, specific=astm_ArrayAccess)
gen_astm_UnaryExpression_Expression = Generalization(general=Expression, specific=astm_UnaryExpression)
gen_astm_BinaryExpression_Expression = Generalization(general=Expression, specific=astm_BinaryExpression)
gen_astm_Literal_Expression = Generalization(general=Expression, specific=astm_Literal)
gen_astm_CastExpression_Expression = Generalization(general=Expression, specific=astm_CastExpression)
gen_astm_ConditionalExpression_Expression = Generalization(general=Expression, specific=astm_ConditionalExpression)
gen_astm_OperatorAssign_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_OperatorAssign)
gen_astm_FunctionCallExpression_Expression = Generalization(general=Expression, specific=astm_FunctionCallExpression)
gen_astm_ActualParameterExpression_ActualParameter = Generalization(general=ActualParameter, specific=astm_ActualParameterExpression)
gen_astm_RangeExpression_Expression = Generalization(general=Expression, specific=astm_RangeExpression)
gen_astm_LabelAccess_Expression = Generalization(general=Expression, specific=astm_LabelAccess)
gen_astm_AnnotationExpression_Expression = Generalization(general=Expression, specific=astm_AnnotationExpression)
gen_astm_NewExpression_Expression = Generalization(general=Expression, specific=astm_NewExpression)
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
gen_astm_External_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_External)
gen_astm_FunctionPersistent_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_FunctionPersistent)
gen_astm_GlobalScope_Scope = Generalization(general=Scope, specific=astm_GlobalScope)
gen_astm_PreprocessorElement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_PreprocessorElement)
gen_astm_DefinitionObject_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_DefinitionObject)
gen_astm_ProgramScope_Scope = Generalization(general=Scope, specific=astm_ProgramScope)
gen_astm_TypeReference_Type = Generalization(general=Type, specific=astm_TypeReference)
gen_astm_Statement_GASTMSyntaxObject = Generalization(general=GASTMSyntaxObject, specific=astm_Statement)
gen_astm_Byte_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Byte)
gen_astm_ShortInteger_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_ShortInteger)
gen_astm_Integer_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Integer)
gen_astm_LongInteger_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_LongInteger)
gen_astm_Float_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Float)
gen_astm_Double_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Double)
gen_astm_LongDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_LongDouble)
gen_astm_Character_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Character)
gen_astm_String_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_String)
gen_astm_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Boolean)
gen_astm_WideCharacter_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_WideCharacter)
gen_astm_FileLocal_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_FileLocal)
gen_astm_PerClassMember_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_PerClassMember)
gen_astm_NoDef_StorageSpecification = Generalization(general=StorageSpecification, specific=astm_NoDef)
gen_astm_Virtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_Virtual)
gen_astm_PureVirtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_PureVirtual)
gen_astm_NonVirtual_VirtualSpecification = Generalization(general=VirtualSpecification, specific=astm_NonVirtual)
gen_astm_ExceptionType_DataType = Generalization(general=DataType, specific=astm_ExceptionType)
gen_astm_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=astm_Void)
gen_astm_ByValueFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=astm_ByValueFormalParameterType)
gen_astm_ByReferenceFormalParameterType_FormalParameterType = Generalization(general=FormalParameterType, specific=astm_ByReferenceFormalParameterType)
gen_astm_Public_AccessKind = Generalization(general=AccessKind, specific=astm_Public)
gen_astm_Protected_AccessKind = Generalization(general=AccessKind, specific=astm_Protected)
gen_astm_Private_AccessKind = Generalization(general=AccessKind, specific=astm_Private)
gen_astm_TerminateStatement_Statement = Generalization(general=Statement, specific=astm_TerminateStatement)
gen_astm_DefaultBlock_SwitchCase = Generalization(general=SwitchCase, specific=astm_DefaultBlock)
gen_astm_WhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_WhileStatement)
gen_astm_DoWhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=astm_DoWhileStatement)
gen_astm_ForCheckBeforeStatement_ForStatement = Generalization(general=ForStatement, specific=astm_ForCheckBeforeStatement)
gen_astm_ForCheckAfterStatement_ForStatement = Generalization(general=ForStatement, specific=astm_ForCheckAfterStatement)
gen_astm_CollectionType_ConstructedType = Generalization(general=ConstructedType, specific=astm_CollectionType)
gen_astm_PointerType_ConstructedType = Generalization(general=ConstructedType, specific=astm_PointerType)
gen_astm_ReferenceType_ConstructedType = Generalization(general=ConstructedType, specific=astm_ReferenceType)
gen_astm_RangeType_ConstructedType = Generalization(general=ConstructedType, specific=astm_RangeType)
gen_astm_StructureType_AggregateType = Generalization(general=AggregateType, specific=astm_StructureType)
gen_astm_UnionType_AggregateType = Generalization(general=AggregateType, specific=astm_UnionType)
gen_astm_AnnotationType_AggregateType = Generalization(general=AggregateType, specific=astm_AnnotationType)
gen_astm_BooleanLiteral_Literal = Generalization(general=Literal, specific=astm_BooleanLiteral)
gen_astm_BitLiteral_Literal = Generalization(general=Literal, specific=astm_BitLiteral)
gen_astm_UnaryPlus_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_UnaryPlus)
gen_astm_Negate_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Negate)
gen_astm_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Not)
gen_astm_BitNot_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_BitNot)
gen_astm_AddressOf_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_AddressOf)
gen_astm_Deref_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Deref)
gen_astm_Increment_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Increment)
gen_astm_Decrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_Decrement)
gen_astm_PostIncrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_PostIncrement)
gen_astm_PostDecrement_UnaryOperator = Generalization(general=UnaryOperator, specific=astm_PostDecrement)
gen_astm_AggregateExpression_Expression = Generalization(general=Expression, specific=astm_AggregateExpression)
gen_astm_QualifiedOverPointer_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=astm_QualifiedOverPointer)
gen_astm_QualifiedOverData_QualifiedIdentifierReference = Generalization(general=QualifiedIdentifierReference, specific=astm_QualifiedOverData)
gen_astm_IntegerLiteral_Literal = Generalization(general=Literal, specific=astm_IntegerLiteral)
gen_astm_StringLiteral_Literal = Generalization(general=Literal, specific=astm_StringLiteral)
gen_astm_CharLiteral_Literal = Generalization(general=Literal, specific=astm_CharLiteral)
gen_astm_RealLiteral_Literal = Generalization(general=Literal, specific=astm_RealLiteral)
gen_astm_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Equal)
gen_astm_NotEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_NotEqual)
gen_astm_Greater_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Greater)
gen_astm_NotGreater_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_NotGreater)
gen_astm_Less_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Less)
gen_astm_NotLess_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_NotLess)
gen_astm_BitAnd_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitAnd)
gen_astm_BitOr_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitOr)
gen_astm_BitXor_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitXor)
gen_astm_BitLeftShift_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitLeftShift)
gen_astm_BitRightShift_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_BitRightShift)
gen_astm_Assign_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Assign)
gen_astm_Add_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Add)
gen_astm_Subtract_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Subtract)
gen_astm_Multiply_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Multiply)
gen_astm_Divide_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Divide)
gen_astm_Modulus_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Modulus)
gen_astm_Exponent_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Exponent)
gen_astm_And_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_And)
gen_astm_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_Or)
gen_astm_SpecificGreaterEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_SpecificGreaterEqual)
gen_astm_SpecificIn_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_SpecificIn)
gen_astm_SpecificLike_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_SpecificLike)
gen_astm_SpecificConcatString_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_SpecificConcatString)
gen_astm_SpecificSelectStatement_Statement = Generalization(general=Statement, specific=astm_SpecificSelectStatement)
gen_astm_Operator_OtherSyntaxObject = Generalization(general=OtherSyntaxObject, specific=astm_Operator)
gen_astm_MissingActualParameter_ActualParameter = Generalization(general=ActualParameter, specific=astm_MissingActualParameter)
gen_astm_ByValueActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=astm_ByValueActualParameterExpression)
gen_astm_ByReferenceActualParameterExpression_ActualParameterExpression = Generalization(general=ActualParameterExpression, specific=astm_ByReferenceActualParameterExpression)
gen_astm_SpecificTriggerDefinition_Definition = Generalization(general=Definition, specific=astm_SpecificTriggerDefinition)
gen_astm_SpecificLessEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=astm_SpecificLessEqual)

# Domain Model
domain_model = DomainModel(
    name="astm",
    types={astm_DelphiImplementationSection, astm_NamedTypeReference, astm_DelphiBlockStatement, BlockStatement, astm_DefinitionObject, astm_DelphiFunctionCallExpression, FunctionCallExpression, astm_DelphiUnit, CompilationUnit, astm_Name, astm_DelphiInterfaceSection, astm_DataType, Type, astm_AccessKind, astm_UnaryOperator, Operator, astm_BinaryOperator, astm_ActualParameter, astm_SourceFile, GASTMSourceObject, astm_SourceLocation, astm_Project, GASTMSemanticObject, astm_CompilationUnit, astm_DelphiWithStatement, astm_GASTMObject, Visitable, astm_GASTMSourceObject, astm_GASTMSemanticObject, astm_OtherSyntaxObject, GASTMSyntaxObject, astm_StorageSpecification, astm_PreprocessorElement, astm_AnnotationExpression, OtherSyntaxObject, astm_ProgramScope, astm_DeclarationOrDefinition, DefinitionObject, astm_GlobalScope, astm_Scope, astm_GASTMSyntaxObject, GASTMObject, astm_FunctionDeclaration, Declaration, astm_FormalParameterDeclaration, astm_FunctionMemberAttributes, astm_VariableDeclaration, astm_FunctionDefinition, Definition, astm_FormalParameterDefinition, astm_Definition, DeclarationOrDefinition, astm_TypeReference, astm_Declaration, astm_VirtualSpecification, astm_EntryDefinition, astm_DataDefinition, astm_Expression, astm_BitFieldDefinition, DataDefinition, astm_Statement, astm_FunctionScope, astm_NameSpaceDefinition, astm_NameSpaceType, astm_LabelDefinition, astm_LabelType, astm_IncludeUnit, PreprocessorElement, astm_MacroCall, astm_EnumLiteralDefinition, astm_TypeDefinition, astm_NamedTypeDefinition, TypeDefinition, astm_NamedType, astm_AggregateTypeDefinition, astm_AggregateType, astm_EnumType, astm_ConstructedType, astm_AggregateScope, astm_ArrayType, ConstructedType, astm_Dimension, astm_MacroDefinition, astm_Comment, astm_Type, astm_PrimitiveType, DataType, astm_ClassType, AggregateType, astm_DerivesFrom, astm_UnnamedTypeReference, TypeReference, astm_FunctionType, astm_BreakStatement, astm_LabelAccess, astm_FormalParameterType, astm_ContinueStatement, astm_LabeledStatement, astm_BlockStatement, astm_BlockScope, astm_DeleteStatement, Statement, astm_DeclarationOrDefinitionStatement, astm_ExpressionStatement, astm_JumpStatement, astm_ReturnStatement, astm_LoopStatement, astm_ForStatement, LoopStatement, astm_TryStatement, astm_CatchBlock, astm_EmptyStatement, astm_IfStatement, astm_SwitchStatement, astm_SwitchCase, astm_CaseBlock, SwitchCase, astm_VariableCatchBlock, astm_ThrowStatement, astm_TypesCatchBlock, CatchBlock, astm_QualifiedIdentifierReference, NameReference, astm_IdentifierReference, astm_TypeQualifiedIdentifierReference, astm_NameReference, Expression, astm_ArrayAccess, astm_UnaryExpression, astm_BinaryExpression, astm_Literal, astm_CastExpression, astm_ConditionalExpression, astm_OperatorAssign, BinaryOperator, astm_FunctionCallExpression, astm_ActualParameterExpression, ActualParameter, astm_RangeExpression, astm_NewExpression, astm_VariableDefinition, astm_FunctionMemberAttribute, astm_External, StorageSpecification, astm_FunctionPersistent, Scope, astm_Byte, astm_ShortInteger, astm_Integer, astm_LongInteger, astm_Float, astm_Double, astm_LongDouble, astm_Character, astm_String, astm_Boolean, astm_WideCharacter, astm_FileLocal, astm_PerClassMember, astm_NoDef, astm_Virtual, VirtualSpecification, astm_PureVirtual, astm_NonVirtual, astm_ExceptionType, astm_Void, PrimitiveType, astm_ByValueFormalParameterType, FormalParameterType, astm_ByReferenceFormalParameterType, astm_Public, AccessKind, astm_Protected, astm_Private, astm_TerminateStatement, astm_DefaultBlock, astm_WhileStatement, astm_DoWhileStatement, astm_ForCheckBeforeStatement, ForStatement, astm_ForCheckAfterStatement, astm_CollectionType, astm_PointerType, astm_ReferenceType, astm_RangeType, astm_StructureType, astm_UnionType, astm_AnnotationType, astm_BitLiteral, astm_UnaryPlus, UnaryOperator, astm_Negate, astm_Not, astm_BitNot, astm_AddressOf, astm_Deref, astm_Increment, astm_Decrement, astm_PostIncrement, astm_PostDecrement, astm_AggregateExpression, astm_QualifiedOverPointer, QualifiedIdentifierReference, astm_QualifiedOverData, astm_IntegerLiteral, Literal, astm_StringLiteral, astm_CharLiteral, astm_RealLiteral, astm_BooleanLiteral, astm_Equal, astm_NotEqual, astm_Greater, astm_NotGreater, astm_Less, astm_NotLess, astm_BitAnd, astm_BitOr, astm_BitXor, astm_BitLeftShift, astm_BitRightShift, astm_Assign, astm_Add, astm_Subtract, astm_Multiply, astm_Divide, astm_Modulus, astm_Exponent, astm_And, astm_Or, astm_SpecificGreaterEqual, astm_SpecificIn, astm_SpecificLike, astm_SpecificConcatString, astm_SpecificSelectStatement, astm_Visitable, astm_Operator, astm_MissingActualParameter, astm_ByValueActualParameterExpression, ActualParameterExpression, astm_ByReferenceActualParameterExpression, astm_SpecificTriggerDefinition, astm_SpecificLessEqual},
    associations={implementation3, uses5, uses7, exports10, exports13, declarations15, name0, interface1, inSourceFile21, applyTo17, withs19, preProcessorElements32, annotations34, fragments36, opensScope39, storageSpecifiers41, files22, outerScope23, definitionObject25, childScope28, locationInfo30, identifierName51, declarationType54, formalParameters57, functionMemberAttributes58, returnType60, returnType63, formalParameters65, accessKind42, identifierName45, definitionType47, defRef49, virtualSpecifier74, formalParameters76, body78, initialValue81, bitFieldSize82, body67, functionMemberAttributes69, opensScope72, nameSpace90, body92, nameSpaceType95, labelName97, labelType99, file101, value84, name86, definitionType88, aggregateType89, enumLiterals104, baseType106, members108, opensScope111, ranks113, refersTo103, parameterTypes122, type124, body127, derivesFrom129, accessKind130, className133, lowBound114, highBound117, target150, returnType120, target152, target153, label155, statement157, subStatements160, opensScope162, type136, name138, type141, operand144, declOrDefn146, expression148, returnValue181, condition183, body185, initBody188, iterationBody190, guardedStatement193, catchBlocks195, condition164, thenBody166, elseBody169, switchExpression172, cases174, body176, caseExpressions179, exceptions203, exceptionVariable205, exception207, expressionType209, finalStatement197, body200, subscripts219, qualifiers222, member224, aggregateType226, member228, name212, refersTo214, arrayName217, operator236, operand238, operator241, castType231, operator249, expression233, condition251, onTrueOperand253, onFalseOperand256, leftOperand243, rightOperand246, calledFunction264, actualParams266, value268, fromExpression259, toExpression261, name275, definition278, annotationType281, memberValues284, newType270, actualParams272, body287},
    generalizations={gen_astm_DelphiInterfaceSection_CompilationUnit, gen_astm_DelphiImplementationSection_CompilationUnit, gen_astm_DelphiBlockStatement_BlockStatement, gen_astm_DelphiUnit_CompilationUnit, gen_astm_DataType_Type, gen_astm_AccessKind_Visitable, gen_astm_UnaryOperator_Operator, gen_astm_BinaryOperator_Operator, gen_astm_ActualParameter_Visitable, gen_astm_SourceFile_GASTMSourceObject, gen_astm_SourceLocation_GASTMSourceObject, gen_astm_Project_GASTMSemanticObject, gen_astm_DelphiFunctionCallExpression_FunctionCallExpression, gen_astm_DelphiWithStatement_BlockStatement, gen_astm_GASTMObject_Visitable, gen_astm_GASTMSourceObject_Visitable, gen_astm_GASTMSemanticObject_Visitable, gen_astm_OtherSyntaxObject_GASTMSyntaxObject, gen_astm_StorageSpecification_Visitable, gen_astm_CompilationUnit_OtherSyntaxObject, gen_astm_Name_OtherSyntaxObject, gen_astm_DeclarationOrDefinition_DefinitionObject, gen_astm_Scope_GASTMSemanticObject, gen_astm_GASTMSyntaxObject_GASTMObject, gen_astm_FunctionDeclaration_Declaration, gen_astm_VariableDeclaration_Declaration, gen_astm_FunctionDefinition_Definition, gen_astm_Definition_DeclarationOrDefinition, gen_astm_Declaration_DeclarationOrDefinition, gen_astm_EntryDefinition_Definition, gen_astm_DataDefinition_Definition, gen_astm_BitFieldDefinition_DataDefinition, gen_astm_FunctionMemberAttributes_Visitable, gen_astm_NameSpaceDefinition_DefinitionObject, gen_astm_LabelDefinition_DefinitionObject, gen_astm_IncludeUnit_PreprocessorElement, gen_astm_MacroCall_PreprocessorElement, gen_astm_EnumLiteralDefinition_Definition, gen_astm_TypeDefinition_DefinitionObject, gen_astm_NamedTypeDefinition_TypeDefinition, gen_astm_AggregateTypeDefinition_TypeDefinition, gen_astm_EnumType_DataType, gen_astm_ConstructedType_DataType, gen_astm_AggregateType_DataType, gen_astm_ArrayType_ConstructedType, gen_astm_Dimension_OtherSyntaxObject, gen_astm_MacroDefinition_PreprocessorElement, gen_astm_Comment_PreprocessorElement, gen_astm_Type_GASTMSyntaxObject, gen_astm_PrimitiveType_DataType, gen_astm_FormalParameterType_DataType, gen_astm_NamedType_DataType, gen_astm_ClassType_AggregateType, gen_astm_DerivesFrom_OtherSyntaxObject, gen_astm_UnnamedTypeReference_TypeReference, gen_astm_FunctionType_Type, gen_astm_BreakStatement_Statement, gen_astm_ContinueStatement_Statement, gen_astm_LabeledStatement_Statement, gen_astm_BlockStatement_Statement, gen_astm_NamedTypeReference_TypeReference, gen_astm_DeleteStatement_Statement, gen_astm_DeclarationOrDefinitionStatement_Statement, gen_astm_ExpressionStatement_Statement, gen_astm_JumpStatement_Statement, gen_astm_ReturnStatement_Statement, gen_astm_LoopStatement_Statement, gen_astm_ForStatement_LoopStatement, gen_astm_TryStatement_Statement, gen_astm_EmptyStatement_Statement, gen_astm_IfStatement_Statement, gen_astm_SwitchStatement_Statement, gen_astm_SwitchCase_OtherSyntaxObject, gen_astm_CaseBlock_SwitchCase, gen_astm_TypesCatchBlock_CatchBlock, gen_astm_VariableCatchBlock_CatchBlock, gen_astm_ThrowStatement_Statement, gen_astm_Expression_GASTMSyntaxObject, gen_astm_CatchBlock_OtherSyntaxObject, gen_astm_QualifiedIdentifierReference_NameReference, gen_astm_TypeQualifiedIdentifierReference_NameReference, gen_astm_NameReference_Expression, gen_astm_ArrayAccess_Expression, gen_astm_UnaryExpression_Expression, gen_astm_BinaryExpression_Expression, gen_astm_Literal_Expression, gen_astm_CastExpression_Expression, gen_astm_ConditionalExpression_Expression, gen_astm_OperatorAssign_BinaryOperator, gen_astm_FunctionCallExpression_Expression, gen_astm_ActualParameterExpression_ActualParameter, gen_astm_RangeExpression_Expression, gen_astm_LabelAccess_Expression, gen_astm_AnnotationExpression_Expression, gen_astm_NewExpression_Expression, gen_astm_FunctionScope_Scope, gen_astm_NameSpaceType_Type, gen_astm_LabelType_Type, gen_astm_AggregateScope_Scope, gen_astm_BlockScope_Scope, gen_astm_IdentifierReference_NameReference, gen_astm_FormalParameterDefinition_DataDefinition, gen_astm_VirtualSpecification_OtherSyntaxObject, gen_astm_FormalParameterDeclaration_Declaration, gen_astm_VariableDefinition_DataDefinition, gen_astm_FunctionMemberAttribute_OtherSyntaxObject, gen_astm_External_StorageSpecification, gen_astm_FunctionPersistent_StorageSpecification, gen_astm_GlobalScope_Scope, gen_astm_PreprocessorElement_GASTMSyntaxObject, gen_astm_DefinitionObject_GASTMSyntaxObject, gen_astm_ProgramScope_Scope, gen_astm_TypeReference_Type, gen_astm_Statement_GASTMSyntaxObject, gen_astm_Byte_PrimitiveType, gen_astm_ShortInteger_PrimitiveType, gen_astm_Integer_PrimitiveType, gen_astm_LongInteger_PrimitiveType, gen_astm_Float_PrimitiveType, gen_astm_Double_PrimitiveType, gen_astm_LongDouble_PrimitiveType, gen_astm_Character_PrimitiveType, gen_astm_String_PrimitiveType, gen_astm_Boolean_PrimitiveType, gen_astm_WideCharacter_PrimitiveType, gen_astm_FileLocal_StorageSpecification, gen_astm_PerClassMember_StorageSpecification, gen_astm_NoDef_StorageSpecification, gen_astm_Virtual_VirtualSpecification, gen_astm_PureVirtual_VirtualSpecification, gen_astm_NonVirtual_VirtualSpecification, gen_astm_ExceptionType_DataType, gen_astm_Void_PrimitiveType, gen_astm_ByValueFormalParameterType_FormalParameterType, gen_astm_ByReferenceFormalParameterType_FormalParameterType, gen_astm_Public_AccessKind, gen_astm_Protected_AccessKind, gen_astm_Private_AccessKind, gen_astm_TerminateStatement_Statement, gen_astm_DefaultBlock_SwitchCase, gen_astm_WhileStatement_LoopStatement, gen_astm_DoWhileStatement_LoopStatement, gen_astm_ForCheckBeforeStatement_ForStatement, gen_astm_ForCheckAfterStatement_ForStatement, gen_astm_CollectionType_ConstructedType, gen_astm_PointerType_ConstructedType, gen_astm_ReferenceType_ConstructedType, gen_astm_RangeType_ConstructedType, gen_astm_StructureType_AggregateType, gen_astm_UnionType_AggregateType, gen_astm_AnnotationType_AggregateType, gen_astm_BooleanLiteral_Literal, gen_astm_BitLiteral_Literal, gen_astm_UnaryPlus_UnaryOperator, gen_astm_Negate_UnaryOperator, gen_astm_Not_UnaryOperator, gen_astm_BitNot_UnaryOperator, gen_astm_AddressOf_UnaryOperator, gen_astm_Deref_UnaryOperator, gen_astm_Increment_UnaryOperator, gen_astm_Decrement_UnaryOperator, gen_astm_PostIncrement_UnaryOperator, gen_astm_PostDecrement_UnaryOperator, gen_astm_AggregateExpression_Expression, gen_astm_QualifiedOverPointer_QualifiedIdentifierReference, gen_astm_QualifiedOverData_QualifiedIdentifierReference, gen_astm_IntegerLiteral_Literal, gen_astm_StringLiteral_Literal, gen_astm_CharLiteral_Literal, gen_astm_RealLiteral_Literal, gen_astm_Equal_BinaryOperator, gen_astm_NotEqual_BinaryOperator, gen_astm_Greater_BinaryOperator, gen_astm_NotGreater_BinaryOperator, gen_astm_Less_BinaryOperator, gen_astm_NotLess_BinaryOperator, gen_astm_BitAnd_BinaryOperator, gen_astm_BitOr_BinaryOperator, gen_astm_BitXor_BinaryOperator, gen_astm_BitLeftShift_BinaryOperator, gen_astm_BitRightShift_BinaryOperator, gen_astm_Assign_BinaryOperator, gen_astm_Add_BinaryOperator, gen_astm_Subtract_BinaryOperator, gen_astm_Multiply_BinaryOperator, gen_astm_Divide_BinaryOperator, gen_astm_Modulus_BinaryOperator, gen_astm_Exponent_BinaryOperator, gen_astm_And_BinaryOperator, gen_astm_Or_BinaryOperator, gen_astm_SpecificGreaterEqual_BinaryOperator, gen_astm_SpecificIn_BinaryOperator, gen_astm_SpecificLike_BinaryOperator, gen_astm_SpecificConcatString_BinaryOperator, gen_astm_SpecificSelectStatement_Statement, gen_astm_Operator_OtherSyntaxObject, gen_astm_MissingActualParameter_ActualParameter, gen_astm_ByValueActualParameterExpression_ActualParameterExpression, gen_astm_ByReferenceActualParameterExpression_ActualParameterExpression, gen_astm_SpecificTriggerDefinition_Definition, gen_astm_SpecificLessEqual_BinaryOperator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)