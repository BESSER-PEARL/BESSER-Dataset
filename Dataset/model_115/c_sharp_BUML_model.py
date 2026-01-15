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
c_sharp_common_NamespaceOrTypeName = Class(name="c::sharp::common::NamespaceOrTypeName")
Identifier = Class(name="Identifier")
c_sharp_common_Identifier = Class(name="c::sharp::common::Identifier")
common_NamedElement = Class(name="common::NamedElement")
expressions_PrimaryNoArrayCreationExpression = Class(name="expressions::PrimaryNoArrayCreationExpression")
c_sharp_common_NamedElement = Class(name="c::sharp::common::NamedElement", is_abstract=True)
c_sharp_namespaces_NamespaceBody = Class(name="c::sharp::namespaces::NamespaceBody")
c_sharp_namespaces_TypeDeclaration = Class(name="c::sharp::namespaces::TypeDeclaration", is_abstract=True)
namespaces_NamespaceMemberDeclaration = Class(name="namespaces::NamespaceMemberDeclaration")
classes_ClassMemberDeclaration = Class(name="classes::ClassMemberDeclaration")
c_sharp_classes_Class = Class(name="c::sharp::classes::Class")
c_sharp_namespaces_CompilationUnit = Class(name="c::sharp::namespaces::CompilationUnit")
namespaces_TypeDeclaration = Class(name="namespaces::TypeDeclaration")
UsingDirective = Class(name="UsingDirective")
GlobalAttributes = Class(name="GlobalAttributes")
NamespaceMemberDeclaration = Class(name="NamespaceMemberDeclaration")
c_sharp_namespaces_UsingDirective = Class(name="c::sharp::namespaces::UsingDirective")
NamedElement = Class(name="NamedElement")
NamespaceOrTypeName = Class(name="NamespaceOrTypeName")
c_sharp_namespaces_NamespaceMemberDeclaration = Class(name="c::sharp::namespaces::NamespaceMemberDeclaration", is_abstract=True)
c_sharp_namespaces_Namespace = Class(name="c::sharp::namespaces::Namespace")
NamespaceBody = Class(name="NamespaceBody")
c_sharp_classes_Method = Class(name="c::sharp::classes::Method")
Type = Class(name="Type")
Attributes = Class(name="Attributes")
Modifier = Class(name="Modifier")
ClassBase = Class(name="ClassBase")
ClassMemberDeclaration = Class(name="ClassMemberDeclaration")
c_sharp_classes_ClassBase = Class(name="c::sharp::classes::ClassBase")
ClassOrInterfaceOrDelegateOrEnumType = Class(name="ClassOrInterfaceOrDelegateOrEnumType")
c_sharp_classes_Block = Class(name="c::sharp::classes::Block")
Statement = Class(name="Statement")
c_sharp_classes_VariableInitializer = Class(name="c::sharp::classes::VariableInitializer", is_abstract=True)
c_sharp_classes_ClassMemberDeclaration = Class(name="c::sharp::classes::ClassMemberDeclaration", is_abstract=True)
c_sharp_classes_ConstantDeclaration = Class(name="c::sharp::classes::ConstantDeclaration")
ConstantDeclarator = Class(name="ConstantDeclarator")
FormalParameterList = Class(name="FormalParameterList")
c_sharp_classes_FieldDeclaration = Class(name="c::sharp::classes::FieldDeclaration")
Block = Class(name="Block")
c_sharp_classes_FormalParameterList = Class(name="c::sharp::classes::FormalParameterList")
FixedParameter = Class(name="FixedParameter")
ParameterArray = Class(name="ParameterArray")
c_sharp_classes_FixedParameter = Class(name="c::sharp::classes::FixedParameter")
Ref = Class(name="Ref")
Out = Class(name="Out")
c_sharp_classes_ParameterArray = Class(name="c::sharp::classes::ParameterArray")
Params = Class(name="Params")
ArrayType = Class(name="ArrayType")
c_sharp_attributes_GlobalAttributes = Class(name="c::sharp::attributes::GlobalAttributes")
GlobalAttributeTarget = Class(name="GlobalAttributeTarget")
Attribute = Class(name="Attribute")
c_sharp_attributes_GlobalAttributeTarget = Class(name="c::sharp::attributes::GlobalAttributeTarget")
c_sharp_attributes_Attributes = Class(name="c::sharp::attributes::Attributes")
AttributeTarget = Class(name="AttributeTarget")
c_sharp_attributes_AttributeTarget = Class(name="c::sharp::attributes::AttributeTarget")
Event = Class(name="Event")
Return = Class(name="Return")
VariableDeclarator = Class(name="VariableDeclarator")
c_sharp_arrays_StackallocInitializer = Class(name="c::sharp::arrays::StackallocInitializer")
VariableInitializer = Class(name="VariableInitializer")
Expression = Class(name="Expression")
c_sharp_arrays_ArrayInitializer = Class(name="c::sharp::arrays::ArrayInitializer")
c_sharp_arrays_ArrayType = Class(name="c::sharp::arrays::ArrayType")
NonArrayType = Class(name="NonArrayType")
RankSpecifier = Class(name="RankSpecifier")
c_sharp_arrays_RankSpecifier = Class(name="c::sharp::arrays::RankSpecifier")
c_sharp_statements_DeclarationStatement = Class(name="c::sharp::statements::DeclarationStatement")
VariableDeclaration = Class(name="VariableDeclaration")
LocalConstantDeclaration = Class(name="LocalConstantDeclaration")
c_sharp_statements_EmbeddedStatement = Class(name="c::sharp::statements::EmbeddedStatement", is_abstract=True)
c_sharp_statements_SimpleEmbeddedStatement = Class(name="c::sharp::statements::SimpleEmbeddedStatement")
EmbeddedStatement = Class(name="EmbeddedStatement")
Unsafe = Class(name="Unsafe")
c_sharp_attributes_Attribute = Class(name="c::sharp::attributes::Attribute")
AttributeArguments = Class(name="AttributeArguments")
c_sharp_attributes_AttributeArguments = Class(name="c::sharp::attributes::AttributeArguments")
ExpressionList = Class(name="ExpressionList")
NamedArgumentList = Class(name="NamedArgumentList")
c_sharp_attributes_NamedArgumentList = Class(name="c::sharp::attributes::NamedArgumentList")
NamedArgument = Class(name="NamedArgument")
c_sharp_attributes_NamedArgument = Class(name="c::sharp::attributes::NamedArgument")
c_sharp_statements_Statement = Class(name="c::sharp::statements::Statement", is_abstract=True)
c_sharp_statements_LabeledStatement = Class(name="c::sharp::statements::LabeledStatement")
Case = Class(name="Case")
statements_Statement = Class(name="statements::Statement")
c_sharp_statements_IterationStatement = Class(name="c::sharp::statements::IterationStatement", is_abstract=True)
c_sharp_statements_WhileStatement = Class(name="c::sharp::statements::WhileStatement")
IterationStatement = Class(name="IterationStatement")
c_sharp_statements_EmptyStatement = Class(name="c::sharp::statements::EmptyStatement")
c_sharp_statements_ExpressionStatement = Class(name="c::sharp::statements::ExpressionStatement")
StatementExpression = Class(name="StatementExpression")
c_sharp_statements_SelectionStatement = Class(name="c::sharp::statements::SelectionStatement", is_abstract=True)
c_sharp_statements_IfStatement = Class(name="c::sharp::statements::IfStatement")
SelectionStatement = Class(name="SelectionStatement")
c_sharp_statements_SwitchStatement = Class(name="c::sharp::statements::SwitchStatement")
SwitchSection = Class(name="SwitchSection")
c_sharp_statements_SwitchSection = Class(name="c::sharp::statements::SwitchSection")
SwitchLabel = Class(name="SwitchLabel")
c_sharp_statements_SwitchLabel = Class(name="c::sharp::statements::SwitchLabel")
Default = Class(name="Default")
c_sharp_statements_ForInitializer = Class(name="c::sharp::statements::ForInitializer", is_abstract=True)
c_sharp_statements_JumpStatement = Class(name="c::sharp::statements::JumpStatement", is_abstract=True)
c_sharp_statements_BreakStatement = Class(name="c::sharp::statements::BreakStatement")
JumpStatement = Class(name="JumpStatement")
c_sharp_statements_ContinueStatement = Class(name="c::sharp::statements::ContinueStatement")
c_sharp_statements_GotoStatement = Class(name="c::sharp::statements::GotoStatement")
c_sharp_statements_DoStatement = Class(name="c::sharp::statements::DoStatement")
c_sharp_statements_ForStatement = Class(name="c::sharp::statements::ForStatement")
ForInitializer = Class(name="ForInitializer")
StatementExpressionList = Class(name="StatementExpressionList")
c_sharp_statements_ForeachStatement = Class(name="c::sharp::statements::ForeachStatement")
c_sharp_statements_ReturnStatement = Class(name="c::sharp::statements::ReturnStatement")
c_sharp_statements_GeneralCatchClause = Class(name="c::sharp::statements::GeneralCatchClause")
c_sharp_statements_FinallyClause = Class(name="c::sharp::statements::FinallyClause")
c_sharp_statements_CheckedStatement = Class(name="c::sharp::statements::CheckedStatement")
c_sharp_statements_ThrowStatement = Class(name="c::sharp::statements::ThrowStatement")
c_sharp_statements_TryStatement = Class(name="c::sharp::statements::TryStatement")
SpecificCatchClause = Class(name="SpecificCatchClause")
GeneralCatchClause = Class(name="GeneralCatchClause")
FinallyClause = Class(name="FinallyClause")
c_sharp_statements_SpecificCatchClause = Class(name="c::sharp::statements::SpecificCatchClause")
PointerType = Class(name="PointerType")
FixedPointerDeclarator = Class(name="FixedPointerDeclarator")
c_sharp_statements_FixedPointerDeclarator = Class(name="c::sharp::statements::FixedPointerDeclarator")
c_sharp_statements_UncheckedStatement = Class(name="c::sharp::statements::UncheckedStatement")
c_sharp_statements_LockStatement = Class(name="c::sharp::statements::LockStatement")
c_sharp_statements_ResourceAcquisition = Class(name="c::sharp::statements::ResourceAcquisition", is_abstract=True)
c_sharp_statements_UsingStatement = Class(name="c::sharp::statements::UsingStatement")
ResourceAcquisition = Class(name="ResourceAcquisition")
c_sharp_statements_FixedStatement = Class(name="c::sharp::statements::FixedStatement")
c_sharp_expressions_StatementExpression = Class(name="c::sharp::expressions::StatementExpression", is_abstract=True)
c_sharp_expressions_StatementExpressionList = Class(name="c::sharp::expressions::StatementExpressionList")
c_sharp_expressions_Expression = Class(name="c::sharp::expressions::Expression", is_abstract=True)
classes_VariableInitializer = Class(name="classes::VariableInitializer")
c_sharp_expressions_ExpressionList = Class(name="c::sharp::expressions::ExpressionList")
c_sharp_expressions_Argument = Class(name="c::sharp::expressions::Argument")
c_sharp_statements_VariableDeclaration = Class(name="c::sharp::statements::VariableDeclaration")
statements_ForInitializer = Class(name="statements::ForInitializer")
statements_ResourceAcquisition = Class(name="statements::ResourceAcquisition")
c_sharp_statements_VariableDeclarator = Class(name="c::sharp::statements::VariableDeclarator")
c_sharp_statements_LocalConstantDeclaration = Class(name="c::sharp::statements::LocalConstantDeclaration")
c_sharp_statements_ConstantDeclarator = Class(name="c::sharp::statements::ConstantDeclarator")
c_sharp_expressions_InvocationExpression = Class(name="c::sharp::expressions::InvocationExpression")
expressions_PrimaryExtendedExpressionType = Class(name="expressions::PrimaryExtendedExpressionType")
expressions_StatementExpression = Class(name="expressions::StatementExpression")
ArgumentList = Class(name="ArgumentList")
c_sharp_expressions_PostIncrementExpression = Class(name="c::sharp::expressions::PostIncrementExpression")
c_sharp_expressions_PostDecrementExpression = Class(name="c::sharp::expressions::PostDecrementExpression")
c_sharp_expressions_PointerMemberAccess = Class(name="c::sharp::expressions::PointerMemberAccess")
c_sharp_expressions_BaseAccess = Class(name="c::sharp::expressions::BaseAccess")
PrimaryNoArrayCreationExpression = Class(name="PrimaryNoArrayCreationExpression")
c_sharp_expressions_ArgumentList = Class(name="c::sharp::expressions::ArgumentList")
Argument = Class(name="Argument")
c_sharp_expressions_PrimaryExpression = Class(name="c::sharp::expressions::PrimaryExpression", is_abstract=True)
c_sharp_expressions_PrimaryNoArrayCreationExpression = Class(name="c::sharp::expressions::PrimaryNoArrayCreationExpression", is_abstract=True)
PrimaryExpression = Class(name="PrimaryExpression")
c_sharp_expressions_PrimaryExtendedExpressionType = Class(name="c::sharp::expressions::PrimaryExtendedExpressionType", is_abstract=True)
c_sharp_expressions_MemberAccess = Class(name="c::sharp::expressions::MemberAccess")
PrimaryExtendedExpressionType = Class(name="PrimaryExtendedExpressionType")
SimpleType = Class(name="SimpleType")
c_sharp_expressions_ElementAccess = Class(name="c::sharp::expressions::ElementAccess")
ArrayInitializer = Class(name="ArrayInitializer")
c_sharp_expressions_ParenthesizedExpression = Class(name="c::sharp::expressions::ParenthesizedExpression")
c_sharp_expressions_UnaryExpression = Class(name="c::sharp::expressions::UnaryExpression")
MemberAccess = Class(name="MemberAccess")
c_sharp_expressions_ObjectCreationExpression = Class(name="c::sharp::expressions::ObjectCreationExpression")
c_sharp_expressions_ArrayCreationExpression = Class(name="c::sharp::expressions::ArrayCreationExpression")
CastExpression = Class(name="CastExpression")
AddressOfExpression = Class(name="AddressOfExpression")
c_sharp_expressions_ConditionalExpression = Class(name="c::sharp::expressions::ConditionalExpression")
ConditionalOrExpression = Class(name="ConditionalOrExpression")
Addition = Class(name="Addition")
Subtraction = Class(name="Subtraction")
Negate = Class(name="Negate")
Complement = Class(name="Complement")
Multiplication = Class(name="Multiplication")
UnaryExpression = Class(name="UnaryExpression")
PreIncrementExpression = Class(name="PreIncrementExpression")
PreDecrementExpression = Class(name="PreDecrementExpression")
c_sharp_expressions_CheckedExpression = Class(name="c::sharp::expressions::CheckedExpression")
c_sharp_expressions_UncheckedExpression = Class(name="c::sharp::expressions::UncheckedExpression")
c_sharp_expressions_SizeOfExpression = Class(name="c::sharp::expressions::SizeOfExpression")
c_sharp_expressions_AssignmentExpression = Class(name="c::sharp::expressions::AssignmentExpression")
expressions_Expression = Class(name="expressions::Expression")
AssignmentOperator = Class(name="AssignmentOperator")
c_sharp_expressions_TypeOfExpression = Class(name="c::sharp::expressions::TypeOfExpression")
c_sharp_expressions_DelegateCreationExpression = Class(name="c::sharp::expressions::DelegateCreationExpression")
c_sharp_expressions_MultiplicativeExpression = Class(name="c::sharp::expressions::MultiplicativeExpression")
Division = Class(name="Division")
Remainder = Class(name="Remainder")
c_sharp_expressions_PreIncrementExpression = Class(name="c::sharp::expressions::PreIncrementExpression")
c_sharp_expressions_PreDecrementExpression = Class(name="c::sharp::expressions::PreDecrementExpression")
c_sharp_expressions_CastExpression = Class(name="c::sharp::expressions::CastExpression")
LeftShift = Class(name="LeftShift")
c_sharp_expressions_AddressOfExpression = Class(name="c::sharp::expressions::AddressOfExpression")
AdditiveExpression = Class(name="AdditiveExpression")
c_sharp_expressions_AdditiveExpression = Class(name="c::sharp::expressions::AdditiveExpression")
MultiplicativeExpression = Class(name="MultiplicativeExpression")
c_sharp_expressions_ShiftExpression = Class(name="c::sharp::expressions::ShiftExpression")
RightShift = Class(name="RightShift")
c_sharp_expressions_EqualityExpression = Class(name="c::sharp::expressions::EqualityExpression")
RelationalExpression = Class(name="RelationalExpression")
Equal = Class(name="Equal")
c_sharp_expressions_RelationalExpression = Class(name="c::sharp::expressions::RelationalExpression")
ShiftExpression = Class(name="ShiftExpression")
LessThan = Class(name="LessThan")
LessThanOrEqual = Class(name="LessThanOrEqual")
GreaterThan = Class(name="GreaterThan")
GreaterThanOrEqual = Class(name="GreaterThanOrEqual")
ConditionalAnd = Class(name="ConditionalAnd")
c_sharp_expressions_ConditionalOrExpression = Class(name="c::sharp::expressions::ConditionalOrExpression")
ConditionalAndExpression = Class(name="ConditionalAndExpression")
ConditionalOr = Class(name="ConditionalOr")
c_sharp_types_Type = Class(name="c::sharp::types::Type", is_abstract=True)
NotEqual = Class(name="NotEqual")
c_sharp_expressions_AndExpression = Class(name="c::sharp::expressions::AndExpression")
EqualityExpression = Class(name="EqualityExpression")
And = Class(name="And")
c_sharp_expressions_ExclusiveOrExpression = Class(name="c::sharp::expressions::ExclusiveOrExpression")
AndExpression = Class(name="AndExpression")
ExclusiveOr = Class(name="ExclusiveOr")
c_sharp_expressions_InclusiveOrExpression = Class(name="c::sharp::expressions::InclusiveOrExpression")
ExclusiveOrExpression = Class(name="ExclusiveOrExpression")
InclusiveOr = Class(name="InclusiveOr")
c_sharp_expressions_ConditionalAndExpression = Class(name="c::sharp::expressions::ConditionalAndExpression")
InclusiveOrExpression = Class(name="InclusiveOrExpression")
c_sharp_types_Object = Class(name="c::sharp::types::Object")
c_sharp_types_String = Class(name="c::sharp::types::String")
c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType = Class(name="c::sharp::types::ClassOrInterfaceOrDelegateOrEnumType")
ReferenceType = Class(name="ReferenceType")
c_sharp_types_PointerType = Class(name="c::sharp::types::PointerType")
c_sharp_types_NonArrayType = Class(name="c::sharp::types::NonArrayType", is_abstract=True)
c_sharp_types_ReferenceType = Class(name="c::sharp::types::ReferenceType", is_abstract=True)
types_NonArrayType = Class(name="types::NonArrayType")
types_Type = Class(name="types::Type")
c_sharp_types_SimpleType = Class(name="c::sharp::types::SimpleType", is_abstract=True)
c_sharp_types_Void = Class(name="c::sharp::types::Void")
c_sharp_types_Decimal = Class(name="c::sharp::types::Decimal")
c_sharp_types_Bool = Class(name="c::sharp::types::Bool")
c_sharp_types_SByte = Class(name="c::sharp::types::SByte")
c_sharp_types_Byte = Class(name="c::sharp::types::Byte")
c_sharp_types_Short = Class(name="c::sharp::types::Short")
c_sharp_types_UShort = Class(name="c::sharp::types::UShort")
c_sharp_types_Int = Class(name="c::sharp::types::Int")
c_sharp_types_UInt = Class(name="c::sharp::types::UInt")
c_sharp_types_Long = Class(name="c::sharp::types::Long")
c_sharp_types_ULong = Class(name="c::sharp::types::ULong")
c_sharp_types_Char = Class(name="c::sharp::types::Char")
c_sharp_types_Float = Class(name="c::sharp::types::Float")
c_sharp_types_Double = Class(name="c::sharp::types::Double")
c_sharp_literals_DecimalIntegerLiteral = Class(name="c::sharp::literals::DecimalIntegerLiteral")
c_sharp_literals_HexadecimalIntegerLiteral = Class(name="c::sharp::literals::HexadecimalIntegerLiteral")
c_sharp_literals_RealLiteral = Class(name="c::sharp::literals::RealLiteral")
c_sharp_literals_NullLiteral = Class(name="c::sharp::literals::NullLiteral")
c_sharp_literals_This = Class(name="c::sharp::literals::This")
c_sharp_literals_CharacterLiteral = Class(name="c::sharp::literals::CharacterLiteral")
c_sharp_modifiers_Modifier = Class(name="c::sharp::modifiers::Modifier", is_abstract=True)
c_sharp_modifiers_Abstract = Class(name="c::sharp::modifiers::Abstract")
c_sharp_modifiers_Extern = Class(name="c::sharp::modifiers::Extern")
c_sharp_modifiers_Internal = Class(name="c::sharp::modifiers::Internal")
c_sharp_modifiers_New = Class(name="c::sharp::modifiers::New")
c_sharp_modifiers_OverrideModifier = Class(name="c::sharp::modifiers::OverrideModifier")
c_sharp_modifiers_Private = Class(name="c::sharp::modifiers::Private")
c_sharp_modifiers_Protected = Class(name="c::sharp::modifiers::Protected")
c_sharp_modifiers_Public = Class(name="c::sharp::modifiers::Public")
c_sharp_modifiers_Partial = Class(name="c::sharp::modifiers::Partial")
c_sharp_modifiers_ReadOnly = Class(name="c::sharp::modifiers::ReadOnly")
c_sharp_modifiers_Sealed = Class(name="c::sharp::modifiers::Sealed")
c_sharp_modifiers_Static = Class(name="c::sharp::modifiers::Static")
c_sharp_modifiers_Unsafe = Class(name="c::sharp::modifiers::Unsafe")
c_sharp_modifiers_Virtual = Class(name="c::sharp::modifiers::Virtual")
c_sharp_modifiers_Volatile = Class(name="c::sharp::modifiers::Volatile")
c_sharp_literals_Literal = Class(name="c::sharp::literals::Literal", is_abstract=True)
c_sharp_literals_BooleanLiteral = Class(name="c::sharp::literals::BooleanLiteral")
Literal = Class(name="Literal")
c_sharp_operators_AssignmentRightShift = Class(name="c::sharp::operators::AssignmentRightShift")
c_sharp_operators_AssignmentUnsignedRightShift = Class(name="c::sharp::operators::AssignmentUnsignedRightShift")
c_sharp_operators_Equal = Class(name="c::sharp::operators::Equal")
EqualityOperator = Class(name="EqualityOperator")
c_sharp_operators_NotEqual = Class(name="c::sharp::operators::NotEqual")
c_sharp_operators_GreaterThan = Class(name="c::sharp::operators::GreaterThan")
RelationOperator = Class(name="RelationOperator")
c_sharp_operators_GreaterThanOrEqual = Class(name="c::sharp::operators::GreaterThanOrEqual")
c_sharp_operators_LessThan = Class(name="c::sharp::operators::LessThan")
c_sharp_operators_LessThanOrEqual = Class(name="c::sharp::operators::LessThanOrEqual")
c_sharp_operators_Addition = Class(name="c::sharp::operators::Addition")
operators_AdditiveOperator = Class(name="operators::AdditiveOperator")
operators_UnaryOperator = Class(name="operators::UnaryOperator")
c_sharp_operators_Subtraction = Class(name="c::sharp::operators::Subtraction")
c_sharp_operators_Division = Class(name="c::sharp::operators::Division")
MultiplicativeOperator = Class(name="MultiplicativeOperator")
c_sharp_literals_StringLiteral = Class(name="c::sharp::literals::StringLiteral")
c_sharp_operators_Multiplication = Class(name="c::sharp::operators::Multiplication")
c_sharp_keywords_Out = Class(name="c::sharp::keywords::Out")
c_sharp_keywords_Ref = Class(name="c::sharp::keywords::Ref")
c_sharp_keywords_Params = Class(name="c::sharp::keywords::Params")
c_sharp_keywords_Case = Class(name="c::sharp::keywords::Case")
c_sharp_keywords_Default = Class(name="c::sharp::keywords::Default")
c_sharp_keywords_Return = Class(name="c::sharp::keywords::Return")
c_sharp_keywords_Event = Class(name="c::sharp::keywords::Event")
c_sharp_operators_Operator = Class(name="c::sharp::operators::Operator", is_abstract=True)
c_sharp_operators_AdditiveOperator = Class(name="c::sharp::operators::AdditiveOperator", is_abstract=True)
Operator = Class(name="Operator")
c_sharp_operators_AssignmentOperator = Class(name="c::sharp::operators::AssignmentOperator", is_abstract=True)
c_sharp_operators_EqualityOperator = Class(name="c::sharp::operators::EqualityOperator", is_abstract=True)
c_sharp_operators_MultiplicativeOperator = Class(name="c::sharp::operators::MultiplicativeOperator", is_abstract=True)
c_sharp_operators_RelationOperator = Class(name="c::sharp::operators::RelationOperator", is_abstract=True)
c_sharp_operators_ShiftOperator = Class(name="c::sharp::operators::ShiftOperator", is_abstract=True)
c_sharp_operators_UnaryOperator = Class(name="c::sharp::operators::UnaryOperator", is_abstract=True)
c_sharp_operators_UnaryModificationOperator = Class(name="c::sharp::operators::UnaryModificationOperator", is_abstract=True)
c_sharp_operators_Assignment = Class(name="c::sharp::operators::Assignment")
c_sharp_operators_AssignmentAnd = Class(name="c::sharp::operators::AssignmentAnd")
c_sharp_operators_AssignmentDivision = Class(name="c::sharp::operators::AssignmentDivision")
c_sharp_operators_AssignmentExclusiveOr = Class(name="c::sharp::operators::AssignmentExclusiveOr")
c_sharp_operators_AssignmentMinus = Class(name="c::sharp::operators::AssignmentMinus")
c_sharp_operators_AssignmentModulo = Class(name="c::sharp::operators::AssignmentModulo")
c_sharp_operators_AssignmentMultiplication = Class(name="c::sharp::operators::AssignmentMultiplication")
c_sharp_operators_AssignmentLeftShift = Class(name="c::sharp::operators::AssignmentLeftShift")
c_sharp_operators_AssignmentOr = Class(name="c::sharp::operators::AssignmentOr")
c_sharp_operators_AssignmentPlus = Class(name="c::sharp::operators::AssignmentPlus")
c_sharp_operators_Remainder = Class(name="c::sharp::operators::Remainder")
c_sharp_operators_Complement = Class(name="c::sharp::operators::Complement")
UnaryOperator = Class(name="UnaryOperator")
c_sharp_operators_MinusMinus = Class(name="c::sharp::operators::MinusMinus")
UnaryModificationOperator = Class(name="UnaryModificationOperator")
c_sharp_operators_Negate = Class(name="c::sharp::operators::Negate")
c_sharp_operators_PlusPlus = Class(name="c::sharp::operators::PlusPlus")
c_sharp_operators_LeftShift = Class(name="c::sharp::operators::LeftShift")
ShiftOperator = Class(name="ShiftOperator")
c_sharp_operators_RightShift = Class(name="c::sharp::operators::RightShift")
c_sharp_operators_UnsignedRightShift = Class(name="c::sharp::operators::UnsignedRightShift")
c_sharp_operators_And = Class(name="c::sharp::operators::And")
c_sharp_operators_ExclusiveOr = Class(name="c::sharp::operators::ExclusiveOr")
c_sharp_operators_InclusiveOr = Class(name="c::sharp::operators::InclusiveOr")
c_sharp_operators_ConditionalAnd = Class(name="c::sharp::operators::ConditionalAnd")
c_sharp_operators_ConditionalOr = Class(name="c::sharp::operators::ConditionalOr")

# c_sharp_common_NamespaceOrTypeName class attributes and methods

# Identifier class attributes and methods

# c_sharp_common_Identifier class attributes and methods

# common_NamedElement class attributes and methods

# expressions_PrimaryNoArrayCreationExpression class attributes and methods

# c_sharp_common_NamedElement class attributes and methods
c_sharp_common_NamedElement_name: Property = Property(name="name", type=StringType)
c_sharp_common_NamedElement.attributes={c_sharp_common_NamedElement_name}

# c_sharp_namespaces_NamespaceBody class attributes and methods

# c_sharp_namespaces_TypeDeclaration class attributes and methods

# namespaces_NamespaceMemberDeclaration class attributes and methods

# classes_ClassMemberDeclaration class attributes and methods

# c_sharp_classes_Class class attributes and methods

# c_sharp_namespaces_CompilationUnit class attributes and methods

# namespaces_TypeDeclaration class attributes and methods

# UsingDirective class attributes and methods

# GlobalAttributes class attributes and methods

# NamespaceMemberDeclaration class attributes and methods

# c_sharp_namespaces_UsingDirective class attributes and methods

# NamedElement class attributes and methods

# NamespaceOrTypeName class attributes and methods

# c_sharp_namespaces_NamespaceMemberDeclaration class attributes and methods

# c_sharp_namespaces_Namespace class attributes and methods

# NamespaceBody class attributes and methods

# c_sharp_classes_Method class attributes and methods

# Type class attributes and methods

# Attributes class attributes and methods

# Modifier class attributes and methods

# ClassBase class attributes and methods

# ClassMemberDeclaration class attributes and methods

# c_sharp_classes_ClassBase class attributes and methods

# ClassOrInterfaceOrDelegateOrEnumType class attributes and methods

# c_sharp_classes_Block class attributes and methods

# Statement class attributes and methods

# c_sharp_classes_VariableInitializer class attributes and methods

# c_sharp_classes_ClassMemberDeclaration class attributes and methods

# c_sharp_classes_ConstantDeclaration class attributes and methods

# ConstantDeclarator class attributes and methods

# FormalParameterList class attributes and methods

# c_sharp_classes_FieldDeclaration class attributes and methods

# Block class attributes and methods

# c_sharp_classes_FormalParameterList class attributes and methods

# FixedParameter class attributes and methods

# ParameterArray class attributes and methods

# c_sharp_classes_FixedParameter class attributes and methods

# Ref class attributes and methods

# Out class attributes and methods

# c_sharp_classes_ParameterArray class attributes and methods

# Params class attributes and methods

# ArrayType class attributes and methods

# c_sharp_attributes_GlobalAttributes class attributes and methods

# GlobalAttributeTarget class attributes and methods

# Attribute class attributes and methods

# c_sharp_attributes_GlobalAttributeTarget class attributes and methods

# c_sharp_attributes_Attributes class attributes and methods

# AttributeTarget class attributes and methods

# c_sharp_attributes_AttributeTarget class attributes and methods

# Event class attributes and methods

# Return class attributes and methods

# VariableDeclarator class attributes and methods

# c_sharp_arrays_StackallocInitializer class attributes and methods

# VariableInitializer class attributes and methods

# Expression class attributes and methods

# c_sharp_arrays_ArrayInitializer class attributes and methods

# c_sharp_arrays_ArrayType class attributes and methods

# NonArrayType class attributes and methods

# RankSpecifier class attributes and methods

# c_sharp_arrays_RankSpecifier class attributes and methods

# c_sharp_statements_DeclarationStatement class attributes and methods

# VariableDeclaration class attributes and methods

# LocalConstantDeclaration class attributes and methods

# c_sharp_statements_EmbeddedStatement class attributes and methods

# c_sharp_statements_SimpleEmbeddedStatement class attributes and methods

# EmbeddedStatement class attributes and methods

# Unsafe class attributes and methods

# c_sharp_attributes_Attribute class attributes and methods

# AttributeArguments class attributes and methods

# c_sharp_attributes_AttributeArguments class attributes and methods

# ExpressionList class attributes and methods

# NamedArgumentList class attributes and methods

# c_sharp_attributes_NamedArgumentList class attributes and methods

# NamedArgument class attributes and methods

# c_sharp_attributes_NamedArgument class attributes and methods

# c_sharp_statements_Statement class attributes and methods

# c_sharp_statements_LabeledStatement class attributes and methods

# Case class attributes and methods

# statements_Statement class attributes and methods

# c_sharp_statements_IterationStatement class attributes and methods

# c_sharp_statements_WhileStatement class attributes and methods

# IterationStatement class attributes and methods

# c_sharp_statements_EmptyStatement class attributes and methods

# c_sharp_statements_ExpressionStatement class attributes and methods

# StatementExpression class attributes and methods

# c_sharp_statements_SelectionStatement class attributes and methods

# c_sharp_statements_IfStatement class attributes and methods

# SelectionStatement class attributes and methods

# c_sharp_statements_SwitchStatement class attributes and methods

# SwitchSection class attributes and methods

# c_sharp_statements_SwitchSection class attributes and methods

# SwitchLabel class attributes and methods

# c_sharp_statements_SwitchLabel class attributes and methods

# Default class attributes and methods

# c_sharp_statements_ForInitializer class attributes and methods

# c_sharp_statements_JumpStatement class attributes and methods

# c_sharp_statements_BreakStatement class attributes and methods

# JumpStatement class attributes and methods

# c_sharp_statements_ContinueStatement class attributes and methods

# c_sharp_statements_GotoStatement class attributes and methods

# c_sharp_statements_DoStatement class attributes and methods

# c_sharp_statements_ForStatement class attributes and methods

# ForInitializer class attributes and methods

# StatementExpressionList class attributes and methods

# c_sharp_statements_ForeachStatement class attributes and methods

# c_sharp_statements_ReturnStatement class attributes and methods

# c_sharp_statements_GeneralCatchClause class attributes and methods

# c_sharp_statements_FinallyClause class attributes and methods

# c_sharp_statements_CheckedStatement class attributes and methods

# c_sharp_statements_ThrowStatement class attributes and methods

# c_sharp_statements_TryStatement class attributes and methods

# SpecificCatchClause class attributes and methods

# GeneralCatchClause class attributes and methods

# FinallyClause class attributes and methods

# c_sharp_statements_SpecificCatchClause class attributes and methods

# PointerType class attributes and methods

# FixedPointerDeclarator class attributes and methods

# c_sharp_statements_FixedPointerDeclarator class attributes and methods

# c_sharp_statements_UncheckedStatement class attributes and methods

# c_sharp_statements_LockStatement class attributes and methods

# c_sharp_statements_ResourceAcquisition class attributes and methods

# c_sharp_statements_UsingStatement class attributes and methods

# ResourceAcquisition class attributes and methods

# c_sharp_statements_FixedStatement class attributes and methods

# c_sharp_expressions_StatementExpression class attributes and methods

# c_sharp_expressions_StatementExpressionList class attributes and methods

# c_sharp_expressions_Expression class attributes and methods

# classes_VariableInitializer class attributes and methods

# c_sharp_expressions_ExpressionList class attributes and methods

# c_sharp_expressions_Argument class attributes and methods

# c_sharp_statements_VariableDeclaration class attributes and methods

# statements_ForInitializer class attributes and methods

# statements_ResourceAcquisition class attributes and methods

# c_sharp_statements_VariableDeclarator class attributes and methods

# c_sharp_statements_LocalConstantDeclaration class attributes and methods

# c_sharp_statements_ConstantDeclarator class attributes and methods

# c_sharp_expressions_InvocationExpression class attributes and methods

# expressions_PrimaryExtendedExpressionType class attributes and methods

# expressions_StatementExpression class attributes and methods

# ArgumentList class attributes and methods

# c_sharp_expressions_PostIncrementExpression class attributes and methods

# c_sharp_expressions_PostDecrementExpression class attributes and methods

# c_sharp_expressions_PointerMemberAccess class attributes and methods

# c_sharp_expressions_BaseAccess class attributes and methods

# PrimaryNoArrayCreationExpression class attributes and methods

# c_sharp_expressions_ArgumentList class attributes and methods

# Argument class attributes and methods

# c_sharp_expressions_PrimaryExpression class attributes and methods

# c_sharp_expressions_PrimaryNoArrayCreationExpression class attributes and methods

# PrimaryExpression class attributes and methods

# c_sharp_expressions_PrimaryExtendedExpressionType class attributes and methods

# c_sharp_expressions_MemberAccess class attributes and methods

# PrimaryExtendedExpressionType class attributes and methods

# SimpleType class attributes and methods

# c_sharp_expressions_ElementAccess class attributes and methods

# ArrayInitializer class attributes and methods

# c_sharp_expressions_ParenthesizedExpression class attributes and methods

# c_sharp_expressions_UnaryExpression class attributes and methods

# MemberAccess class attributes and methods

# c_sharp_expressions_ObjectCreationExpression class attributes and methods

# c_sharp_expressions_ArrayCreationExpression class attributes and methods

# CastExpression class attributes and methods

# AddressOfExpression class attributes and methods

# c_sharp_expressions_ConditionalExpression class attributes and methods

# ConditionalOrExpression class attributes and methods

# Addition class attributes and methods

# Subtraction class attributes and methods

# Negate class attributes and methods

# Complement class attributes and methods

# Multiplication class attributes and methods

# UnaryExpression class attributes and methods

# PreIncrementExpression class attributes and methods

# PreDecrementExpression class attributes and methods

# c_sharp_expressions_CheckedExpression class attributes and methods

# c_sharp_expressions_UncheckedExpression class attributes and methods

# c_sharp_expressions_SizeOfExpression class attributes and methods

# c_sharp_expressions_AssignmentExpression class attributes and methods

# expressions_Expression class attributes and methods

# AssignmentOperator class attributes and methods

# c_sharp_expressions_TypeOfExpression class attributes and methods

# c_sharp_expressions_DelegateCreationExpression class attributes and methods

# c_sharp_expressions_MultiplicativeExpression class attributes and methods

# Division class attributes and methods

# Remainder class attributes and methods

# c_sharp_expressions_PreIncrementExpression class attributes and methods

# c_sharp_expressions_PreDecrementExpression class attributes and methods

# c_sharp_expressions_CastExpression class attributes and methods

# LeftShift class attributes and methods

# c_sharp_expressions_AddressOfExpression class attributes and methods

# AdditiveExpression class attributes and methods

# c_sharp_expressions_AdditiveExpression class attributes and methods

# MultiplicativeExpression class attributes and methods

# c_sharp_expressions_ShiftExpression class attributes and methods

# RightShift class attributes and methods

# c_sharp_expressions_EqualityExpression class attributes and methods

# RelationalExpression class attributes and methods

# Equal class attributes and methods

# c_sharp_expressions_RelationalExpression class attributes and methods

# ShiftExpression class attributes and methods

# LessThan class attributes and methods

# LessThanOrEqual class attributes and methods

# GreaterThan class attributes and methods

# GreaterThanOrEqual class attributes and methods

# ConditionalAnd class attributes and methods

# c_sharp_expressions_ConditionalOrExpression class attributes and methods

# ConditionalAndExpression class attributes and methods

# ConditionalOr class attributes and methods

# c_sharp_types_Type class attributes and methods

# NotEqual class attributes and methods

# c_sharp_expressions_AndExpression class attributes and methods

# EqualityExpression class attributes and methods

# And class attributes and methods

# c_sharp_expressions_ExclusiveOrExpression class attributes and methods

# AndExpression class attributes and methods

# ExclusiveOr class attributes and methods

# c_sharp_expressions_InclusiveOrExpression class attributes and methods

# ExclusiveOrExpression class attributes and methods

# InclusiveOr class attributes and methods

# c_sharp_expressions_ConditionalAndExpression class attributes and methods

# InclusiveOrExpression class attributes and methods

# c_sharp_types_Object class attributes and methods

# c_sharp_types_String class attributes and methods

# c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType class attributes and methods

# ReferenceType class attributes and methods

# c_sharp_types_PointerType class attributes and methods

# c_sharp_types_NonArrayType class attributes and methods

# c_sharp_types_ReferenceType class attributes and methods

# types_NonArrayType class attributes and methods

# types_Type class attributes and methods

# c_sharp_types_SimpleType class attributes and methods

# c_sharp_types_Void class attributes and methods

# c_sharp_types_Decimal class attributes and methods

# c_sharp_types_Bool class attributes and methods

# c_sharp_types_SByte class attributes and methods

# c_sharp_types_Byte class attributes and methods

# c_sharp_types_Short class attributes and methods

# c_sharp_types_UShort class attributes and methods

# c_sharp_types_Int class attributes and methods

# c_sharp_types_UInt class attributes and methods

# c_sharp_types_Long class attributes and methods

# c_sharp_types_ULong class attributes and methods

# c_sharp_types_Char class attributes and methods

# c_sharp_types_Float class attributes and methods

# c_sharp_types_Double class attributes and methods

# c_sharp_literals_DecimalIntegerLiteral class attributes and methods
c_sharp_literals_DecimalIntegerLiteral_value: Property = Property(name="value", type=StringType)
c_sharp_literals_DecimalIntegerLiteral.attributes={c_sharp_literals_DecimalIntegerLiteral_value}

# c_sharp_literals_HexadecimalIntegerLiteral class attributes and methods
c_sharp_literals_HexadecimalIntegerLiteral_value: Property = Property(name="value", type=StringType)
c_sharp_literals_HexadecimalIntegerLiteral.attributes={c_sharp_literals_HexadecimalIntegerLiteral_value}

# c_sharp_literals_RealLiteral class attributes and methods
c_sharp_literals_RealLiteral_value: Property = Property(name="value", type=StringType)
c_sharp_literals_RealLiteral.attributes={c_sharp_literals_RealLiteral_value}

# c_sharp_literals_NullLiteral class attributes and methods

# c_sharp_literals_This class attributes and methods

# c_sharp_literals_CharacterLiteral class attributes and methods
c_sharp_literals_CharacterLiteral_value: Property = Property(name="value", type=StringType)
c_sharp_literals_CharacterLiteral.attributes={c_sharp_literals_CharacterLiteral_value}

# c_sharp_modifiers_Modifier class attributes and methods

# c_sharp_modifiers_Abstract class attributes and methods

# c_sharp_modifiers_Extern class attributes and methods

# c_sharp_modifiers_Internal class attributes and methods

# c_sharp_modifiers_New class attributes and methods

# c_sharp_modifiers_OverrideModifier class attributes and methods

# c_sharp_modifiers_Private class attributes and methods

# c_sharp_modifiers_Protected class attributes and methods

# c_sharp_modifiers_Public class attributes and methods

# c_sharp_modifiers_Partial class attributes and methods

# c_sharp_modifiers_ReadOnly class attributes and methods

# c_sharp_modifiers_Sealed class attributes and methods

# c_sharp_modifiers_Static class attributes and methods

# c_sharp_modifiers_Unsafe class attributes and methods

# c_sharp_modifiers_Virtual class attributes and methods

# c_sharp_modifiers_Volatile class attributes and methods

# c_sharp_literals_Literal class attributes and methods

# c_sharp_literals_BooleanLiteral class attributes and methods
c_sharp_literals_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
c_sharp_literals_BooleanLiteral.attributes={c_sharp_literals_BooleanLiteral_value}

# Literal class attributes and methods

# c_sharp_operators_AssignmentRightShift class attributes and methods

# c_sharp_operators_AssignmentUnsignedRightShift class attributes and methods

# c_sharp_operators_Equal class attributes and methods

# EqualityOperator class attributes and methods

# c_sharp_operators_NotEqual class attributes and methods

# c_sharp_operators_GreaterThan class attributes and methods

# RelationOperator class attributes and methods

# c_sharp_operators_GreaterThanOrEqual class attributes and methods

# c_sharp_operators_LessThan class attributes and methods

# c_sharp_operators_LessThanOrEqual class attributes and methods

# c_sharp_operators_Addition class attributes and methods

# operators_AdditiveOperator class attributes and methods

# operators_UnaryOperator class attributes and methods

# c_sharp_operators_Subtraction class attributes and methods

# c_sharp_operators_Division class attributes and methods

# MultiplicativeOperator class attributes and methods

# c_sharp_literals_StringLiteral class attributes and methods
c_sharp_literals_StringLiteral_value: Property = Property(name="value", type=StringType)
c_sharp_literals_StringLiteral.attributes={c_sharp_literals_StringLiteral_value}

# c_sharp_operators_Multiplication class attributes and methods

# c_sharp_keywords_Out class attributes and methods

# c_sharp_keywords_Ref class attributes and methods

# c_sharp_keywords_Params class attributes and methods

# c_sharp_keywords_Case class attributes and methods

# c_sharp_keywords_Default class attributes and methods

# c_sharp_keywords_Return class attributes and methods

# c_sharp_keywords_Event class attributes and methods

# c_sharp_operators_Operator class attributes and methods

# c_sharp_operators_AdditiveOperator class attributes and methods

# Operator class attributes and methods

# c_sharp_operators_AssignmentOperator class attributes and methods

# c_sharp_operators_EqualityOperator class attributes and methods

# c_sharp_operators_MultiplicativeOperator class attributes and methods

# c_sharp_operators_RelationOperator class attributes and methods

# c_sharp_operators_ShiftOperator class attributes and methods

# c_sharp_operators_UnaryOperator class attributes and methods

# c_sharp_operators_UnaryModificationOperator class attributes and methods

# c_sharp_operators_Assignment class attributes and methods

# c_sharp_operators_AssignmentAnd class attributes and methods

# c_sharp_operators_AssignmentDivision class attributes and methods

# c_sharp_operators_AssignmentExclusiveOr class attributes and methods

# c_sharp_operators_AssignmentMinus class attributes and methods

# c_sharp_operators_AssignmentModulo class attributes and methods

# c_sharp_operators_AssignmentMultiplication class attributes and methods

# c_sharp_operators_AssignmentLeftShift class attributes and methods

# c_sharp_operators_AssignmentOr class attributes and methods

# c_sharp_operators_AssignmentPlus class attributes and methods

# c_sharp_operators_Remainder class attributes and methods

# c_sharp_operators_Complement class attributes and methods

# UnaryOperator class attributes and methods

# c_sharp_operators_MinusMinus class attributes and methods

# UnaryModificationOperator class attributes and methods

# c_sharp_operators_Negate class attributes and methods

# c_sharp_operators_PlusPlus class attributes and methods

# c_sharp_operators_LeftShift class attributes and methods

# ShiftOperator class attributes and methods

# c_sharp_operators_RightShift class attributes and methods

# c_sharp_operators_UnsignedRightShift class attributes and methods

# c_sharp_operators_And class attributes and methods

# c_sharp_operators_ExclusiveOr class attributes and methods

# c_sharp_operators_InclusiveOr class attributes and methods

# c_sharp_operators_ConditionalAnd class attributes and methods

# c_sharp_operators_ConditionalOr class attributes and methods

# Relationships
parts0: BinaryAssociation = BinaryAssociation(
    name="parts0",
    ends={
        Property(name="Identifier", type=c_sharp_common_NamespaceOrTypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_common_NamespaceOrTypeName", type=Identifier, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
usingDirectives11: BinaryAssociation = BinaryAssociation(
    name="usingDirectives11",
    ends={
        Property(name="UsingDirective12", type=c_sharp_namespaces_NamespaceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_namespaces_NamespaceBody", type=UsingDirective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespaceMemberDeclaration13: BinaryAssociation = BinaryAssociation(
    name="namespaceMemberDeclaration13",
    ends={
        Property(name="NamespaceMemberDeclaration15", type=c_sharp_namespaces_NamespaceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_namespaces_NamespaceBody14", type=NamespaceMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usingDirectives1: BinaryAssociation = BinaryAssociation(
    name="usingDirectives1",
    ends={
        Property(name="UsingDirective", type=c_sharp_namespaces_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_namespaces_CompilationUnit", type=UsingDirective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalAttributes2: BinaryAssociation = BinaryAssociation(
    name="globalAttributes2",
    ends={
        Property(name="GlobalAttributes", type=c_sharp_namespaces_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_namespaces_CompilationUnit3", type=GlobalAttributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespaceMemberDeclaration4: BinaryAssociation = BinaryAssociation(
    name="namespaceMemberDeclaration4",
    ends={
        Property(name="NamespaceMemberDeclaration", type=c_sharp_namespaces_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_namespaces_CompilationUnit5", type=NamespaceMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespaceOrTypeName6: BinaryAssociation = BinaryAssociation(
    name="namespaceOrTypeName6",
    ends={
        Property(name="NamespaceOrTypeName", type=c_sharp_namespaces_UsingDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_namespaces_UsingDirective", type=NamespaceOrTypeName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
namespaceName7: BinaryAssociation = BinaryAssociation(
    name="namespaceName7",
    ends={
        Property(name="NamespaceOrTypeName8", type=c_sharp_namespaces_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_namespaces_Namespace", type=NamespaceOrTypeName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
namespaceBody9: BinaryAssociation = BinaryAssociation(
    name="namespaceBody9",
    ends={
        Property(name="NamespaceBody", type=c_sharp_namespaces_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_namespaces_Namespace10", type=NamespaceBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes24: BinaryAssociation = BinaryAssociation(
    name="attributes24",
    ends={
        Property(name="Attributes25", type=c_sharp_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Method", type=Attributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers26: BinaryAssociation = BinaryAssociation(
    name="modifiers26",
    ends={
        Property(name="Modifier28", type=c_sharp_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Method27", type=Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType29: BinaryAssociation = BinaryAssociation(
    name="returnType29",
    ends={
        Property(name="Type", type=c_sharp_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Method30", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceType31: BinaryAssociation = BinaryAssociation(
    name="interfaceType31",
    ends={
        Property(name="ClassOrInterfaceOrDelegateOrEnumType33", type=c_sharp_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Method32", type=ClassOrInterfaceOrDelegateOrEnumType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes16: BinaryAssociation = BinaryAssociation(
    name="attributes16",
    ends={
        Property(name="Attributes", type=c_sharp_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Class", type=Attributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers17: BinaryAssociation = BinaryAssociation(
    name="modifiers17",
    ends={
        Property(name="Modifier", type=c_sharp_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Class18", type=Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classBase19: BinaryAssociation = BinaryAssociation(
    name="classBase19",
    ends={
        Property(name="ClassBase", type=c_sharp_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Class20", type=ClassBase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classMemberDeclarations21: BinaryAssociation = BinaryAssociation(
    name="classMemberDeclarations21",
    ends={
        Property(name="ClassMemberDeclaration", type=c_sharp_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Class22", type=ClassMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types23: BinaryAssociation = BinaryAssociation(
    name="types23",
    ends={
        Property(name="ClassOrInterfaceOrDelegateOrEnumType", type=c_sharp_classes_ClassBase, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_ClassBase", type=ClassOrInterfaceOrDelegateOrEnumType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
statement62: BinaryAssociation = BinaryAssociation(
    name="statement62",
    ends={
        Property(name="Statement", type=c_sharp_classes_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Block", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes63: BinaryAssociation = BinaryAssociation(
    name="attributes63",
    ends={
        Property(name="Attributes64", type=c_sharp_classes_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_ConstantDeclaration", type=Attributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers65: BinaryAssociation = BinaryAssociation(
    name="modifiers65",
    ends={
        Property(name="Modifier67", type=c_sharp_classes_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_ConstantDeclaration66", type=Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type68: BinaryAssociation = BinaryAssociation(
    name="type68",
    ends={
        Property(name="Type70", type=c_sharp_classes_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_ConstantDeclaration69", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constantDeclarator71: BinaryAssociation = BinaryAssociation(
    name="constantDeclarator71",
    ends={
        Property(name="ConstantDeclarator", type=c_sharp_classes_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_ConstantDeclaration72", type=ConstantDeclarator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
formalParameterList34: BinaryAssociation = BinaryAssociation(
    name="formalParameterList34",
    ends={
        Property(name="FormalParameterList", type=c_sharp_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Method35", type=FormalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block36: BinaryAssociation = BinaryAssociation(
    name="block36",
    ends={
        Property(name="Block", type=c_sharp_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_Method37", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fixedParameter38: BinaryAssociation = BinaryAssociation(
    name="fixedParameter38",
    ends={
        Property(name="FixedParameter", type=c_sharp_classes_FormalParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FormalParameterList", type=FixedParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterArray39: BinaryAssociation = BinaryAssociation(
    name="parameterArray39",
    ends={
        Property(name="ParameterArray", type=c_sharp_classes_FormalParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FormalParameterList40", type=ParameterArray, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes41: BinaryAssociation = BinaryAssociation(
    name="attributes41",
    ends={
        Property(name="Attributes42", type=c_sharp_classes_FixedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FixedParameter", type=Attributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref43: BinaryAssociation = BinaryAssociation(
    name="ref43",
    ends={
        Property(name="Ref", type=c_sharp_classes_FixedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FixedParameter44", type=Ref, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
out45: BinaryAssociation = BinaryAssociation(
    name="out45",
    ends={
        Property(name="Out", type=c_sharp_classes_FixedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FixedParameter46", type=Out, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type47: BinaryAssociation = BinaryAssociation(
    name="type47",
    ends={
        Property(name="Type49", type=c_sharp_classes_FixedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FixedParameter48", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier50: BinaryAssociation = BinaryAssociation(
    name="identifier50",
    ends={
        Property(name="Identifier52", type=c_sharp_classes_FixedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FixedParameter51", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes53: BinaryAssociation = BinaryAssociation(
    name="attributes53",
    ends={
        Property(name="Attributes54", type=c_sharp_classes_ParameterArray, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_ParameterArray", type=Attributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params55: BinaryAssociation = BinaryAssociation(
    name="params55",
    ends={
        Property(name="Params", type=c_sharp_classes_ParameterArray, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_ParameterArray56", type=Params, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayType57: BinaryAssociation = BinaryAssociation(
    name="arrayType57",
    ends={
        Property(name="ArrayType", type=c_sharp_classes_ParameterArray, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_ParameterArray58", type=ArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier59: BinaryAssociation = BinaryAssociation(
    name="identifier59",
    ends={
        Property(name="Identifier61", type=c_sharp_classes_ParameterArray, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_ParameterArray60", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
globalAttributeTarget91: BinaryAssociation = BinaryAssociation(
    name="globalAttributeTarget91",
    ends={
        Property(name="GlobalAttributeTarget", type=c_sharp_attributes_GlobalAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_GlobalAttributes", type=GlobalAttributeTarget, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attribute92: BinaryAssociation = BinaryAssociation(
    name="attribute92",
    ends={
        Property(name="Attribute", type=c_sharp_attributes_GlobalAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_GlobalAttributes93", type=Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
identifier94: BinaryAssociation = BinaryAssociation(
    name="identifier94",
    ends={
        Property(name="Identifier95", type=c_sharp_attributes_GlobalAttributeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_GlobalAttributeTarget", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributeTarget96: BinaryAssociation = BinaryAssociation(
    name="attributeTarget96",
    ends={
        Property(name="AttributeTarget", type=c_sharp_attributes_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_Attributes", type=AttributeTarget, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attribute97: BinaryAssociation = BinaryAssociation(
    name="attribute97",
    ends={
        Property(name="Attribute99", type=c_sharp_attributes_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_Attributes98", type=Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
event100: BinaryAssociation = BinaryAssociation(
    name="event100",
    ends={
        Property(name="Event", type=c_sharp_attributes_AttributeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_AttributeTarget", type=Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes73: BinaryAssociation = BinaryAssociation(
    name="attributes73",
    ends={
        Property(name="Attributes74", type=c_sharp_classes_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FieldDeclaration", type=Attributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers75: BinaryAssociation = BinaryAssociation(
    name="modifiers75",
    ends={
        Property(name="Modifier77", type=c_sharp_classes_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FieldDeclaration76", type=Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type78: BinaryAssociation = BinaryAssociation(
    name="type78",
    ends={
        Property(name="Type80", type=c_sharp_classes_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FieldDeclaration79", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDeclarator81: BinaryAssociation = BinaryAssociation(
    name="variableDeclarator81",
    ends={
        Property(name="VariableDeclarator", type=c_sharp_classes_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_classes_FieldDeclaration82", type=VariableDeclarator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type83: BinaryAssociation = BinaryAssociation(
    name="type83",
    ends={
        Property(name="Type84", type=c_sharp_arrays_StackallocInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_arrays_StackallocInitializer", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression85: BinaryAssociation = BinaryAssociation(
    name="expression85",
    ends={
        Property(name="Expression", type=c_sharp_arrays_StackallocInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_arrays_StackallocInitializer86", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableInitializer87: BinaryAssociation = BinaryAssociation(
    name="variableInitializer87",
    ends={
        Property(name="VariableInitializer", type=c_sharp_arrays_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_arrays_ArrayInitializer", type=VariableInitializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonArrayType88: BinaryAssociation = BinaryAssociation(
    name="nonArrayType88",
    ends={
        Property(name="NonArrayType", type=c_sharp_arrays_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_arrays_ArrayType", type=NonArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rankSpecifier89: BinaryAssociation = BinaryAssociation(
    name="rankSpecifier89",
    ends={
        Property(name="RankSpecifier", type=c_sharp_arrays_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_arrays_ArrayType90", type=RankSpecifier, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variableDeclaration121: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration121",
    ends={
        Property(name="VariableDeclaration", type=c_sharp_statements_DeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_DeclarationStatement", type=VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localConstantDeclaration122: BinaryAssociation = BinaryAssociation(
    name="localConstantDeclaration122",
    ends={
        Property(name="LocalConstantDeclaration", type=c_sharp_statements_DeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_DeclarationStatement123", type=LocalConstantDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unsafe124: BinaryAssociation = BinaryAssociation(
    name="unsafe124",
    ends={
        Property(name="Unsafe", type=c_sharp_statements_SimpleEmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SimpleEmbeddedStatement", type=Unsafe, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
return101: BinaryAssociation = BinaryAssociation(
    name="return101",
    ends={
        Property(name="Return", type=c_sharp_attributes_AttributeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_AttributeTarget102", type=Return, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="Type105", type=c_sharp_attributes_AttributeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_AttributeTarget104", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namespaceOrTypeName106: BinaryAssociation = BinaryAssociation(
    name="namespaceOrTypeName106",
    ends={
        Property(name="NamespaceOrTypeName107", type=c_sharp_attributes_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_Attribute", type=NamespaceOrTypeName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributeArguments108: BinaryAssociation = BinaryAssociation(
    name="attributeArguments108",
    ends={
        Property(name="AttributeArguments", type=c_sharp_attributes_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_Attribute109", type=AttributeArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList110: BinaryAssociation = BinaryAssociation(
    name="expressionList110",
    ends={
        Property(name="ExpressionList", type=c_sharp_attributes_AttributeArguments, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_AttributeArguments", type=ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedArgumentList111: BinaryAssociation = BinaryAssociation(
    name="namedArgumentList111",
    ends={
        Property(name="NamedArgumentList", type=c_sharp_attributes_AttributeArguments, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_AttributeArguments112", type=NamedArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedArgument113: BinaryAssociation = BinaryAssociation(
    name="namedArgument113",
    ends={
        Property(name="NamedArgument", type=c_sharp_attributes_NamedArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_NamedArgumentList", type=NamedArgument, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
identifier114: BinaryAssociation = BinaryAssociation(
    name="identifier114",
    ends={
        Property(name="Identifier115", type=c_sharp_attributes_NamedArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_NamedArgument", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression116: BinaryAssociation = BinaryAssociation(
    name="expression116",
    ends={
        Property(name="Expression118", type=c_sharp_attributes_NamedArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_attributes_NamedArgument117", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case142: BinaryAssociation = BinaryAssociation(
    name="case142",
    ends={
        Property(name="Case", type=c_sharp_statements_SwitchLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SwitchLabel143", type=Case, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement119: BinaryAssociation = BinaryAssociation(
    name="statement119",
    ends={
        Property(name="Statement120", type=c_sharp_statements_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_LabeledStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression144: BinaryAssociation = BinaryAssociation(
    name="expression144",
    ends={
        Property(name="Expression146", type=c_sharp_statements_SwitchLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SwitchLabel145", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression147: BinaryAssociation = BinaryAssociation(
    name="expression147",
    ends={
        Property(name="Expression148", type=c_sharp_statements_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_WhileStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block125: BinaryAssociation = BinaryAssociation(
    name="block125",
    ends={
        Property(name="Block127", type=c_sharp_statements_SimpleEmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SimpleEmbeddedStatement126", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStatement149: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement149",
    ends={
        Property(name="EmbeddedStatement151", type=c_sharp_statements_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_WhileStatement150", type=EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementExpression128: BinaryAssociation = BinaryAssociation(
    name="statementExpression128",
    ends={
        Property(name="StatementExpression", type=c_sharp_statements_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ExpressionStatement", type=StatementExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression129: BinaryAssociation = BinaryAssociation(
    name="expression129",
    ends={
        Property(name="Expression130", type=c_sharp_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_IfStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
embeddedStatement131: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement131",
    ends={
        Property(name="EmbeddedStatement", type=c_sharp_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_IfStatement132", type=EmbeddedStatement, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
expression133: BinaryAssociation = BinaryAssociation(
    name="expression133",
    ends={
        Property(name="Expression134", type=c_sharp_statements_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SwitchStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
switchSection135: BinaryAssociation = BinaryAssociation(
    name="switchSection135",
    ends={
        Property(name="SwitchSection", type=c_sharp_statements_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SwitchStatement136", type=SwitchSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
switchLabel137: BinaryAssociation = BinaryAssociation(
    name="switchLabel137",
    ends={
        Property(name="SwitchLabel", type=c_sharp_statements_SwitchSection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SwitchSection", type=SwitchLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement138: BinaryAssociation = BinaryAssociation(
    name="statement138",
    ends={
        Property(name="Statement140", type=c_sharp_statements_SwitchSection, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SwitchSection139", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default141: BinaryAssociation = BinaryAssociation(
    name="default141",
    ends={
        Property(name="Default", type=c_sharp_statements_SwitchLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SwitchLabel", type=Default, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression171: BinaryAssociation = BinaryAssociation(
    name="expression171",
    ends={
        Property(name="Expression173", type=c_sharp_statements_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ForeachStatement172", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStatement174: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement174",
    ends={
        Property(name="EmbeddedStatement176", type=c_sharp_statements_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ForeachStatement175", type=EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStatement152: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement152",
    ends={
        Property(name="EmbeddedStatement153", type=c_sharp_statements_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_DoStatement", type=EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression154: BinaryAssociation = BinaryAssociation(
    name="expression154",
    ends={
        Property(name="Expression156", type=c_sharp_statements_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_DoStatement155", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forInitializer157: BinaryAssociation = BinaryAssociation(
    name="forInitializer157",
    ends={
        Property(name="ForInitializer", type=c_sharp_statements_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ForStatement", type=ForInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression158: BinaryAssociation = BinaryAssociation(
    name="expression158",
    ends={
        Property(name="Expression160", type=c_sharp_statements_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ForStatement159", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementExpressionList161: BinaryAssociation = BinaryAssociation(
    name="statementExpressionList161",
    ends={
        Property(name="StatementExpressionList", type=c_sharp_statements_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ForStatement162", type=StatementExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStatement163: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement163",
    ends={
        Property(name="EmbeddedStatement165", type=c_sharp_statements_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ForStatement164", type=EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type166: BinaryAssociation = BinaryAssociation(
    name="type166",
    ends={
        Property(name="Type167", type=c_sharp_statements_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ForeachStatement", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier168: BinaryAssociation = BinaryAssociation(
    name="identifier168",
    ends={
        Property(name="Identifier170", type=c_sharp_statements_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ForeachStatement169", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default177: BinaryAssociation = BinaryAssociation(
    name="default177",
    ends={
        Property(name="Default178", type=c_sharp_statements_GotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_GotoStatement", type=Default, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case179: BinaryAssociation = BinaryAssociation(
    name="case179",
    ends={
        Property(name="Case181", type=c_sharp_statements_GotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_GotoStatement180", type=Case, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression182: BinaryAssociation = BinaryAssociation(
    name="expression182",
    ends={
        Property(name="Expression184", type=c_sharp_statements_GotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_GotoStatement183", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier185: BinaryAssociation = BinaryAssociation(
    name="identifier185",
    ends={
        Property(name="Identifier187", type=c_sharp_statements_GotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_GotoStatement186", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression188: BinaryAssociation = BinaryAssociation(
    name="expression188",
    ends={
        Property(name="Expression189", type=c_sharp_statements_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block205: BinaryAssociation = BinaryAssociation(
    name="block205",
    ends={
        Property(name="Block207", type=c_sharp_statements_SpecificCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SpecificCatchClause206", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block208: BinaryAssociation = BinaryAssociation(
    name="block208",
    ends={
        Property(name="Block209", type=c_sharp_statements_GeneralCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_GeneralCatchClause", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block210: BinaryAssociation = BinaryAssociation(
    name="block210",
    ends={
        Property(name="Block211", type=c_sharp_statements_FinallyClause, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_FinallyClause", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block212: BinaryAssociation = BinaryAssociation(
    name="block212",
    ends={
        Property(name="Block213", type=c_sharp_statements_CheckedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_CheckedStatement", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression190: BinaryAssociation = BinaryAssociation(
    name="expression190",
    ends={
        Property(name="Expression191", type=c_sharp_statements_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ThrowStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block192: BinaryAssociation = BinaryAssociation(
    name="block192",
    ends={
        Property(name="Block193", type=c_sharp_statements_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_TryStatement", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specificCatchClause194: BinaryAssociation = BinaryAssociation(
    name="specificCatchClause194",
    ends={
        Property(name="SpecificCatchClause", type=c_sharp_statements_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_TryStatement195", type=SpecificCatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalCatchClause196: BinaryAssociation = BinaryAssociation(
    name="generalCatchClause196",
    ends={
        Property(name="GeneralCatchClause", type=c_sharp_statements_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_TryStatement197", type=GeneralCatchClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finallyClause198: BinaryAssociation = BinaryAssociation(
    name="finallyClause198",
    ends={
        Property(name="FinallyClause", type=c_sharp_statements_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_TryStatement199", type=FinallyClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classType200: BinaryAssociation = BinaryAssociation(
    name="classType200",
    ends={
        Property(name="ClassOrInterfaceOrDelegateOrEnumType201", type=c_sharp_statements_SpecificCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SpecificCatchClause", type=ClassOrInterfaceOrDelegateOrEnumType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier202: BinaryAssociation = BinaryAssociation(
    name="identifier202",
    ends={
        Property(name="Identifier204", type=c_sharp_statements_SpecificCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_SpecificCatchClause203", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointerType225: BinaryAssociation = BinaryAssociation(
    name="pointerType225",
    ends={
        Property(name="PointerType", type=c_sharp_statements_FixedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_FixedStatement", type=PointerType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fixedPointerDeclarator226: BinaryAssociation = BinaryAssociation(
    name="fixedPointerDeclarator226",
    ends={
        Property(name="FixedPointerDeclarator", type=c_sharp_statements_FixedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_FixedStatement227", type=FixedPointerDeclarator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
embeddedStatement228: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement228",
    ends={
        Property(name="EmbeddedStatement230", type=c_sharp_statements_FixedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_FixedStatement229", type=EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier231: BinaryAssociation = BinaryAssociation(
    name="identifier231",
    ends={
        Property(name="Identifier232", type=c_sharp_statements_FixedPointerDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_FixedPointerDeclarator", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression233: BinaryAssociation = BinaryAssociation(
    name="expression233",
    ends={
        Property(name="Expression235", type=c_sharp_statements_FixedPointerDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_FixedPointerDeclarator234", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block214: BinaryAssociation = BinaryAssociation(
    name="block214",
    ends={
        Property(name="Block215", type=c_sharp_statements_UncheckedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_UncheckedStatement", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression216: BinaryAssociation = BinaryAssociation(
    name="expression216",
    ends={
        Property(name="Expression217", type=c_sharp_statements_LockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_LockStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStatement218: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement218",
    ends={
        Property(name="EmbeddedStatement220", type=c_sharp_statements_LockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_LockStatement219", type=EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceAcquisition221: BinaryAssociation = BinaryAssociation(
    name="resourceAcquisition221",
    ends={
        Property(name="ResourceAcquisition", type=c_sharp_statements_UsingStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_UsingStatement", type=ResourceAcquisition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStatement222: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement222",
    ends={
        Property(name="EmbeddedStatement224", type=c_sharp_statements_UsingStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_UsingStatement223", type=EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementExpression250: BinaryAssociation = BinaryAssociation(
    name="statementExpression250",
    ends={
        Property(name="StatementExpression251", type=c_sharp_expressions_StatementExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_StatementExpressionList", type=StatementExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression252: BinaryAssociation = BinaryAssociation(
    name="expression252",
    ends={
        Property(name="Expression253", type=c_sharp_expressions_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ExpressionList", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
out254: BinaryAssociation = BinaryAssociation(
    name="out254",
    ends={
        Property(name="Out255", type=c_sharp_expressions_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_Argument", type=Out, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type236: BinaryAssociation = BinaryAssociation(
    name="type236",
    ends={
        Property(name="Type237", type=c_sharp_statements_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_VariableDeclaration", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
VariableDeclarator238: BinaryAssociation = BinaryAssociation(
    name="VariableDeclarator238",
    ends={
        Property(name="VariableDeclarator240", type=c_sharp_statements_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_VariableDeclaration239", type=VariableDeclarator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
VariableInitializer241: BinaryAssociation = BinaryAssociation(
    name="VariableInitializer241",
    ends={
        Property(name="VariableInitializer242", type=c_sharp_statements_VariableDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_VariableDeclarator", type=VariableInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type243: BinaryAssociation = BinaryAssociation(
    name="type243",
    ends={
        Property(name="Type244", type=c_sharp_statements_LocalConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_LocalConstantDeclaration", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constantDeclarator245: BinaryAssociation = BinaryAssociation(
    name="constantDeclarator245",
    ends={
        Property(name="ConstantDeclarator247", type=c_sharp_statements_LocalConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_LocalConstantDeclaration246", type=ConstantDeclarator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression248: BinaryAssociation = BinaryAssociation(
    name="expression248",
    ends={
        Property(name="Expression249", type=c_sharp_statements_ConstantDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_statements_ConstantDeclarator", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argumentList269: BinaryAssociation = BinaryAssociation(
    name="argumentList269",
    ends={
        Property(name="ArgumentList", type=c_sharp_expressions_InvocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_InvocationExpression", type=ArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier270: BinaryAssociation = BinaryAssociation(
    name="identifier270",
    ends={
        Property(name="Identifier271", type=c_sharp_expressions_PointerMemberAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_PointerMemberAccess", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref256: BinaryAssociation = BinaryAssociation(
    name="ref256",
    ends={
        Property(name="Ref258", type=c_sharp_expressions_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_Argument257", type=Ref, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression259: BinaryAssociation = BinaryAssociation(
    name="expression259",
    ends={
        Property(name="Expression261", type=c_sharp_expressions_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_Argument260", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument262: BinaryAssociation = BinaryAssociation(
    name="argument262",
    ends={
        Property(name="Argument", type=c_sharp_expressions_ArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ArgumentList", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleType263: BinaryAssociation = BinaryAssociation(
    name="simpleType263",
    ends={
        Property(name="SimpleType", type=c_sharp_expressions_MemberAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_MemberAccess", type=SimpleType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier264: BinaryAssociation = BinaryAssociation(
    name="identifier264",
    ends={
        Property(name="Identifier266", type=c_sharp_expressions_MemberAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_MemberAccess265", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList267: BinaryAssociation = BinaryAssociation(
    name="expressionList267",
    ends={
        Property(name="ExpressionList268", type=c_sharp_expressions_ElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ElementAccess", type=ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayInitializer293: BinaryAssociation = BinaryAssociation(
    name="arrayInitializer293",
    ends={
        Property(name="ArrayInitializer", type=c_sharp_expressions_ArrayCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ArrayCreationExpression294", type=ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression295: BinaryAssociation = BinaryAssociation(
    name="expression295",
    ends={
        Property(name="Expression296", type=c_sharp_expressions_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ParenthesizedExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
memberAccess297: BinaryAssociation = BinaryAssociation(
    name="memberAccess297",
    ends={
        Property(name="MemberAccess", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression", type=MemberAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExpression298: BinaryAssociation = BinaryAssociation(
    name="primaryExpression298",
    ends={
        Property(name="PrimaryExpression", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression299", type=PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExtendedExpressionType300: BinaryAssociation = BinaryAssociation(
    name="primaryExtendedExpressionType300",
    ends={
        Property(name="PrimaryExtendedExpressionType", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression301", type=PrimaryExtendedExpressionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionList272: BinaryAssociation = BinaryAssociation(
    name="expressionList272",
    ends={
        Property(name="ExpressionList273", type=c_sharp_expressions_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_BaseAccess", type=ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier274: BinaryAssociation = BinaryAssociation(
    name="identifier274",
    ends={
        Property(name="Identifier276", type=c_sharp_expressions_BaseAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_BaseAccess275", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type277: BinaryAssociation = BinaryAssociation(
    name="type277",
    ends={
        Property(name="Type278", type=c_sharp_expressions_ObjectCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ObjectCreationExpression", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argumentList279: BinaryAssociation = BinaryAssociation(
    name="argumentList279",
    ends={
        Property(name="ArgumentList281", type=c_sharp_expressions_ObjectCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ObjectCreationExpression280", type=ArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type282: BinaryAssociation = BinaryAssociation(
    name="type282",
    ends={
        Property(name="Type283", type=c_sharp_expressions_ArrayCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ArrayCreationExpression", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arrayType284: BinaryAssociation = BinaryAssociation(
    name="arrayType284",
    ends={
        Property(name="ArrayType286", type=c_sharp_expressions_ArrayCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ArrayCreationExpression285", type=ArrayType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressionList287: BinaryAssociation = BinaryAssociation(
    name="expressionList287",
    ends={
        Property(name="ExpressionList289", type=c_sharp_expressions_ArrayCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ArrayCreationExpression288", type=ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rankSpecifier290: BinaryAssociation = BinaryAssociation(
    name="rankSpecifier290",
    ends={
        Property(name="RankSpecifier292", type=c_sharp_expressions_ArrayCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ArrayCreationExpression291", type=RankSpecifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preDecrementExpression316: BinaryAssociation = BinaryAssociation(
    name="preDecrementExpression316",
    ends={
        Property(name="c_sharp_expressions_UnaryExpression317", type=PreDecrementExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="PreDecrementExpression", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1))
    }
)
castExpression318: BinaryAssociation = BinaryAssociation(
    name="castExpression318",
    ends={
        Property(name="CastExpression", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression319", type=CastExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addressOfExpression320: BinaryAssociation = BinaryAssociation(
    name="addressOfExpression320",
    ends={
        Property(name="AddressOfExpression", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression321", type=AddressOfExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression322: BinaryAssociation = BinaryAssociation(
    name="expression322",
    ends={
        Property(name="Expression323", type=c_sharp_expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ConditionalExpression", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addition302: BinaryAssociation = BinaryAssociation(
    name="addition302",
    ends={
        Property(name="Addition", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression303", type=Addition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subtraction304: BinaryAssociation = BinaryAssociation(
    name="subtraction304",
    ends={
        Property(name="Subtraction", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression305", type=Subtraction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negate306: BinaryAssociation = BinaryAssociation(
    name="negate306",
    ends={
        Property(name="Negate", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression307", type=Negate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
complement308: BinaryAssociation = BinaryAssociation(
    name="complement308",
    ends={
        Property(name="Complement", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression309", type=Complement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
multiplication310: BinaryAssociation = BinaryAssociation(
    name="multiplication310",
    ends={
        Property(name="Multiplication", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression311", type=Multiplication, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unaryExpression312: BinaryAssociation = BinaryAssociation(
    name="unaryExpression312",
    ends={
        Property(name="UnaryExpression", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression313", type=UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preIncrementExpression314: BinaryAssociation = BinaryAssociation(
    name="preIncrementExpression314",
    ends={
        Property(name="PreIncrementExpression", type=c_sharp_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UnaryExpression315", type=PreIncrementExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression340: BinaryAssociation = BinaryAssociation(
    name="expression340",
    ends={
        Property(name="Expression341", type=c_sharp_expressions_CheckedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_CheckedExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression342: BinaryAssociation = BinaryAssociation(
    name="expression342",
    ends={
        Property(name="Expression343", type=c_sharp_expressions_UncheckedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_UncheckedExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type344: BinaryAssociation = BinaryAssociation(
    name="type344",
    ends={
        Property(name="Type345", type=c_sharp_expressions_SizeOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_SizeOfExpression", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionalOrExpression324: BinaryAssociation = BinaryAssociation(
    name="conditionalOrExpression324",
    ends={
        Property(name="ConditionalOrExpression", type=c_sharp_expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ConditionalExpression325", type=ConditionalOrExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
unaryExpression326: BinaryAssociation = BinaryAssociation(
    name="unaryExpression326",
    ends={
        Property(name="UnaryExpression327", type=c_sharp_expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_AssignmentExpression", type=UnaryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignmentOperator328: BinaryAssociation = BinaryAssociation(
    name="assignmentOperator328",
    ends={
        Property(name="AssignmentOperator", type=c_sharp_expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_AssignmentExpression329", type=AssignmentOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression330: BinaryAssociation = BinaryAssociation(
    name="expression330",
    ends={
        Property(name="Expression332", type=c_sharp_expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_AssignmentExpression331", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type333: BinaryAssociation = BinaryAssociation(
    name="type333",
    ends={
        Property(name="Type334", type=c_sharp_expressions_TypeOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_TypeOfExpression", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delegateType335: BinaryAssociation = BinaryAssociation(
    name="delegateType335",
    ends={
        Property(name="ClassOrInterfaceOrDelegateOrEnumType336", type=c_sharp_expressions_DelegateCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_DelegateCreationExpression", type=ClassOrInterfaceOrDelegateOrEnumType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression337: BinaryAssociation = BinaryAssociation(
    name="expression337",
    ends={
        Property(name="Expression339", type=c_sharp_expressions_DelegateCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_DelegateCreationExpression338", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression355: BinaryAssociation = BinaryAssociation(
    name="unaryExpression355",
    ends={
        Property(name="UnaryExpression356", type=c_sharp_expressions_AddressOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_AddressOfExpression", type=UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression357: BinaryAssociation = BinaryAssociation(
    name="unaryExpression357",
    ends={
        Property(name="UnaryExpression358", type=c_sharp_expressions_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_MultiplicativeExpression", type=UnaryExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
multiplication359: BinaryAssociation = BinaryAssociation(
    name="multiplication359",
    ends={
        Property(name="Multiplication361", type=c_sharp_expressions_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_MultiplicativeExpression360", type=Multiplication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
division362: BinaryAssociation = BinaryAssociation(
    name="division362",
    ends={
        Property(name="Division", type=c_sharp_expressions_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_MultiplicativeExpression363", type=Division, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression346: BinaryAssociation = BinaryAssociation(
    name="unaryExpression346",
    ends={
        Property(name="UnaryExpression347", type=c_sharp_expressions_PreIncrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_PreIncrementExpression", type=UnaryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unaryExpression348: BinaryAssociation = BinaryAssociation(
    name="unaryExpression348",
    ends={
        Property(name="UnaryExpression349", type=c_sharp_expressions_PreDecrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_PreDecrementExpression", type=UnaryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type350: BinaryAssociation = BinaryAssociation(
    name="type350",
    ends={
        Property(name="Type351", type=c_sharp_expressions_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_CastExpression", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression352: BinaryAssociation = BinaryAssociation(
    name="unaryExpression352",
    ends={
        Property(name="UnaryExpression354", type=c_sharp_expressions_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_CastExpression353", type=UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftShift374: BinaryAssociation = BinaryAssociation(
    name="leftShift374",
    ends={
        Property(name="LeftShift", type=c_sharp_expressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ShiftExpression375", type=LeftShift, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remainder376: BinaryAssociation = BinaryAssociation(
    name="remainder376",
    ends={
        Property(name="Remainder378", type=c_sharp_expressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ShiftExpression377", type=Remainder, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remainder364: BinaryAssociation = BinaryAssociation(
    name="remainder364",
    ends={
        Property(name="Remainder", type=c_sharp_expressions_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_MultiplicativeExpression365", type=Remainder, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicativeExpression366: BinaryAssociation = BinaryAssociation(
    name="multiplicativeExpression366",
    ends={
        Property(name="MultiplicativeExpression", type=c_sharp_expressions_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_AdditiveExpression", type=MultiplicativeExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
addition367: BinaryAssociation = BinaryAssociation(
    name="addition367",
    ends={
        Property(name="Addition369", type=c_sharp_expressions_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_AdditiveExpression368", type=Addition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtraction370: BinaryAssociation = BinaryAssociation(
    name="subtraction370",
    ends={
        Property(name="Subtraction372", type=c_sharp_expressions_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_AdditiveExpression371", type=Subtraction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightShift373: BinaryAssociation = BinaryAssociation(
    name="rightShift373",
    ends={
        Property(name="RightShift", type=c_sharp_expressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ShiftExpression", type=RightShift, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relationalExpression393: BinaryAssociation = BinaryAssociation(
    name="relationalExpression393",
    ends={
        Property(name="RelationalExpression", type=c_sharp_expressions_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_EqualityExpression", type=RelationalExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
equal394: BinaryAssociation = BinaryAssociation(
    name="equal394",
    ends={
        Property(name="Equal", type=c_sharp_expressions_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_EqualityExpression395", type=Equal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additiveExpression379: BinaryAssociation = BinaryAssociation(
    name="additiveExpression379",
    ends={
        Property(name="AdditiveExpression", type=c_sharp_expressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ShiftExpression380", type=AdditiveExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shiftExpression381: BinaryAssociation = BinaryAssociation(
    name="shiftExpression381",
    ends={
        Property(name="ShiftExpression", type=c_sharp_expressions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_RelationalExpression", type=ShiftExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type382: BinaryAssociation = BinaryAssociation(
    name="type382",
    ends={
        Property(name="Type384", type=c_sharp_expressions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_RelationalExpression383", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lessThan385: BinaryAssociation = BinaryAssociation(
    name="lessThan385",
    ends={
        Property(name="LessThan", type=c_sharp_expressions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_RelationalExpression386", type=LessThan, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lessThanOrEqual387: BinaryAssociation = BinaryAssociation(
    name="lessThanOrEqual387",
    ends={
        Property(name="LessThanOrEqual", type=c_sharp_expressions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_RelationalExpression388", type=LessThanOrEqual, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
greaterThan389: BinaryAssociation = BinaryAssociation(
    name="greaterThan389",
    ends={
        Property(name="GreaterThan", type=c_sharp_expressions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_RelationalExpression390", type=GreaterThan, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
greaterThanOrEqual391: BinaryAssociation = BinaryAssociation(
    name="greaterThanOrEqual391",
    ends={
        Property(name="GreaterThanOrEqual", type=c_sharp_expressions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_RelationalExpression392", type=GreaterThanOrEqual, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionalAnd408: BinaryAssociation = BinaryAssociation(
    name="conditionalAnd408",
    ends={
        Property(name="ConditionalAnd", type=c_sharp_expressions_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ConditionalAndExpression409", type=ConditionalAnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionalAndExpression410: BinaryAssociation = BinaryAssociation(
    name="conditionalAndExpression410",
    ends={
        Property(name="ConditionalAndExpression", type=c_sharp_expressions_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ConditionalOrExpression", type=ConditionalAndExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
conditionalOr411: BinaryAssociation = BinaryAssociation(
    name="conditionalOr411",
    ends={
        Property(name="ConditionalOr", type=c_sharp_expressions_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ConditionalOrExpression412", type=ConditionalOr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notEqual396: BinaryAssociation = BinaryAssociation(
    name="notEqual396",
    ends={
        Property(name="NotEqual", type=c_sharp_expressions_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_EqualityExpression397", type=NotEqual, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equalityExpression398: BinaryAssociation = BinaryAssociation(
    name="equalityExpression398",
    ends={
        Property(name="EqualityExpression", type=c_sharp_expressions_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_AndExpression", type=EqualityExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
and399: BinaryAssociation = BinaryAssociation(
    name="and399",
    ends={
        Property(name="And", type=c_sharp_expressions_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_AndExpression400", type=And, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
andExpression401: BinaryAssociation = BinaryAssociation(
    name="andExpression401",
    ends={
        Property(name="AndExpression", type=c_sharp_expressions_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ExclusiveOrExpression", type=AndExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
exclusiveOr402: BinaryAssociation = BinaryAssociation(
    name="exclusiveOr402",
    ends={
        Property(name="ExclusiveOr", type=c_sharp_expressions_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ExclusiveOrExpression403", type=ExclusiveOr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exclusiveOrExpression404: BinaryAssociation = BinaryAssociation(
    name="exclusiveOrExpression404",
    ends={
        Property(name="ExclusiveOrExpression", type=c_sharp_expressions_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_InclusiveOrExpression", type=ExclusiveOrExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inclusiveOr405: BinaryAssociation = BinaryAssociation(
    name="inclusiveOr405",
    ends={
        Property(name="InclusiveOr", type=c_sharp_expressions_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_InclusiveOrExpression406", type=InclusiveOr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inclusiveOrExpression407: BinaryAssociation = BinaryAssociation(
    name="inclusiveOrExpression407",
    ends={
        Property(name="InclusiveOrExpression", type=c_sharp_expressions_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_expressions_ConditionalAndExpression", type=InclusiveOrExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
namespaceOrTypeName413: BinaryAssociation = BinaryAssociation(
    name="namespaceOrTypeName413",
    ends={
        Property(name="NamespaceOrTypeName414", type=c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType", type=NamespaceOrTypeName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simpleType415: BinaryAssociation = BinaryAssociation(
    name="simpleType415",
    ends={
        Property(name="SimpleType416", type=c_sharp_types_PointerType, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_types_PointerType", type=SimpleType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referenceType417: BinaryAssociation = BinaryAssociation(
    name="referenceType417",
    ends={
        Property(name="ReferenceType", type=c_sharp_types_PointerType, multiplicity=Multiplicity(1, 1)),
        Property(name="c_sharp_types_PointerType418", type=ReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_c_sharp_common_Identifier_common_NamedElement = Generalization(general=common_NamedElement, specific=c_sharp_common_Identifier)
gen_c_sharp_common_Identifier_expressions_PrimaryNoArrayCreationExpression = Generalization(general=expressions_PrimaryNoArrayCreationExpression, specific=c_sharp_common_Identifier)
gen_c_sharp_namespaces_TypeDeclaration_namespaces_NamespaceMemberDeclaration = Generalization(general=namespaces_NamespaceMemberDeclaration, specific=c_sharp_namespaces_TypeDeclaration)
gen_c_sharp_namespaces_TypeDeclaration_classes_ClassMemberDeclaration = Generalization(general=classes_ClassMemberDeclaration, specific=c_sharp_namespaces_TypeDeclaration)
gen_c_sharp_classes_Class_namespaces_TypeDeclaration = Generalization(general=namespaces_TypeDeclaration, specific=c_sharp_classes_Class)
gen_c_sharp_classes_Class_common_NamedElement = Generalization(general=common_NamedElement, specific=c_sharp_classes_Class)
gen_c_sharp_namespaces_UsingDirective_NamedElement = Generalization(general=NamedElement, specific=c_sharp_namespaces_UsingDirective)
gen_c_sharp_namespaces_Namespace_NamespaceMemberDeclaration = Generalization(general=NamespaceMemberDeclaration, specific=c_sharp_namespaces_Namespace)
gen_c_sharp_classes_Method_classes_ClassMemberDeclaration = Generalization(general=classes_ClassMemberDeclaration, specific=c_sharp_classes_Method)
gen_c_sharp_classes_Method_common_NamedElement = Generalization(general=common_NamedElement, specific=c_sharp_classes_Method)
gen_c_sharp_classes_ConstantDeclaration_ClassMemberDeclaration = Generalization(general=ClassMemberDeclaration, specific=c_sharp_classes_ConstantDeclaration)
gen_c_sharp_classes_FieldDeclaration_ClassMemberDeclaration = Generalization(general=ClassMemberDeclaration, specific=c_sharp_classes_FieldDeclaration)
gen_c_sharp_arrays_StackallocInitializer_VariableInitializer = Generalization(general=VariableInitializer, specific=c_sharp_arrays_StackallocInitializer)
gen_c_sharp_arrays_ArrayInitializer_VariableInitializer = Generalization(general=VariableInitializer, specific=c_sharp_arrays_ArrayInitializer)
gen_c_sharp_arrays_ArrayType_Type = Generalization(general=Type, specific=c_sharp_arrays_ArrayType)
gen_c_sharp_statements_DeclarationStatement_Statement = Generalization(general=Statement, specific=c_sharp_statements_DeclarationStatement)
gen_c_sharp_statements_EmbeddedStatement_Statement = Generalization(general=Statement, specific=c_sharp_statements_EmbeddedStatement)
gen_c_sharp_statements_SimpleEmbeddedStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_SimpleEmbeddedStatement)
gen_c_sharp_statements_LabeledStatement_statements_Statement = Generalization(general=statements_Statement, specific=c_sharp_statements_LabeledStatement)
gen_c_sharp_statements_LabeledStatement_common_NamedElement = Generalization(general=common_NamedElement, specific=c_sharp_statements_LabeledStatement)
gen_c_sharp_statements_IterationStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_IterationStatement)
gen_c_sharp_statements_WhileStatement_IterationStatement = Generalization(general=IterationStatement, specific=c_sharp_statements_WhileStatement)
gen_c_sharp_statements_EmptyStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_EmptyStatement)
gen_c_sharp_statements_ExpressionStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_ExpressionStatement)
gen_c_sharp_statements_SelectionStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_SelectionStatement)
gen_c_sharp_statements_IfStatement_SelectionStatement = Generalization(general=SelectionStatement, specific=c_sharp_statements_IfStatement)
gen_c_sharp_statements_SwitchStatement_SelectionStatement = Generalization(general=SelectionStatement, specific=c_sharp_statements_SwitchStatement)
gen_c_sharp_statements_JumpStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_JumpStatement)
gen_c_sharp_statements_BreakStatement_JumpStatement = Generalization(general=JumpStatement, specific=c_sharp_statements_BreakStatement)
gen_c_sharp_statements_ContinueStatement_JumpStatement = Generalization(general=JumpStatement, specific=c_sharp_statements_ContinueStatement)
gen_c_sharp_statements_GotoStatement_JumpStatement = Generalization(general=JumpStatement, specific=c_sharp_statements_GotoStatement)
gen_c_sharp_statements_DoStatement_IterationStatement = Generalization(general=IterationStatement, specific=c_sharp_statements_DoStatement)
gen_c_sharp_statements_ForStatement_IterationStatement = Generalization(general=IterationStatement, specific=c_sharp_statements_ForStatement)
gen_c_sharp_statements_ForeachStatement_IterationStatement = Generalization(general=IterationStatement, specific=c_sharp_statements_ForeachStatement)
gen_c_sharp_statements_ReturnStatement_JumpStatement = Generalization(general=JumpStatement, specific=c_sharp_statements_ReturnStatement)
gen_c_sharp_statements_CheckedStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_CheckedStatement)
gen_c_sharp_statements_ThrowStatement_JumpStatement = Generalization(general=JumpStatement, specific=c_sharp_statements_ThrowStatement)
gen_c_sharp_statements_TryStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_TryStatement)
gen_c_sharp_statements_UncheckedStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_UncheckedStatement)
gen_c_sharp_statements_LockStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_LockStatement)
gen_c_sharp_statements_UsingStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_UsingStatement)
gen_c_sharp_statements_FixedStatement_EmbeddedStatement = Generalization(general=EmbeddedStatement, specific=c_sharp_statements_FixedStatement)
gen_c_sharp_expressions_StatementExpressionList_ForInitializer = Generalization(general=ForInitializer, specific=c_sharp_expressions_StatementExpressionList)
gen_c_sharp_expressions_Expression_classes_VariableInitializer = Generalization(general=classes_VariableInitializer, specific=c_sharp_expressions_Expression)
gen_c_sharp_expressions_Expression_statements_ResourceAcquisition = Generalization(general=statements_ResourceAcquisition, specific=c_sharp_expressions_Expression)
gen_c_sharp_statements_VariableDeclaration_statements_ForInitializer = Generalization(general=statements_ForInitializer, specific=c_sharp_statements_VariableDeclaration)
gen_c_sharp_statements_VariableDeclaration_statements_ResourceAcquisition = Generalization(general=statements_ResourceAcquisition, specific=c_sharp_statements_VariableDeclaration)
gen_c_sharp_statements_VariableDeclarator_NamedElement = Generalization(general=NamedElement, specific=c_sharp_statements_VariableDeclarator)
gen_c_sharp_statements_ConstantDeclarator_NamedElement = Generalization(general=NamedElement, specific=c_sharp_statements_ConstantDeclarator)
gen_c_sharp_expressions_InvocationExpression_expressions_PrimaryExtendedExpressionType = Generalization(general=expressions_PrimaryExtendedExpressionType, specific=c_sharp_expressions_InvocationExpression)
gen_c_sharp_expressions_InvocationExpression_expressions_StatementExpression = Generalization(general=expressions_StatementExpression, specific=c_sharp_expressions_InvocationExpression)
gen_c_sharp_expressions_PostIncrementExpression_expressions_PrimaryExtendedExpressionType = Generalization(general=expressions_PrimaryExtendedExpressionType, specific=c_sharp_expressions_PostIncrementExpression)
gen_c_sharp_expressions_PostIncrementExpression_expressions_StatementExpression = Generalization(general=expressions_StatementExpression, specific=c_sharp_expressions_PostIncrementExpression)
gen_c_sharp_expressions_PostDecrementExpression_expressions_PrimaryExtendedExpressionType = Generalization(general=expressions_PrimaryExtendedExpressionType, specific=c_sharp_expressions_PostDecrementExpression)
gen_c_sharp_expressions_PostDecrementExpression_expressions_StatementExpression = Generalization(general=expressions_StatementExpression, specific=c_sharp_expressions_PostDecrementExpression)
gen_c_sharp_expressions_PointerMemberAccess_PrimaryExtendedExpressionType = Generalization(general=PrimaryExtendedExpressionType, specific=c_sharp_expressions_PointerMemberAccess)
gen_c_sharp_expressions_BaseAccess_PrimaryNoArrayCreationExpression = Generalization(general=PrimaryNoArrayCreationExpression, specific=c_sharp_expressions_BaseAccess)
gen_c_sharp_expressions_PrimaryNoArrayCreationExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=c_sharp_expressions_PrimaryNoArrayCreationExpression)
gen_c_sharp_expressions_MemberAccess_PrimaryExtendedExpressionType = Generalization(general=PrimaryExtendedExpressionType, specific=c_sharp_expressions_MemberAccess)
gen_c_sharp_expressions_ElementAccess_PrimaryExtendedExpressionType = Generalization(general=PrimaryExtendedExpressionType, specific=c_sharp_expressions_ElementAccess)
gen_c_sharp_expressions_ParenthesizedExpression_PrimaryNoArrayCreationExpression = Generalization(general=PrimaryNoArrayCreationExpression, specific=c_sharp_expressions_ParenthesizedExpression)
gen_c_sharp_expressions_ObjectCreationExpression_expressions_PrimaryNoArrayCreationExpression = Generalization(general=expressions_PrimaryNoArrayCreationExpression, specific=c_sharp_expressions_ObjectCreationExpression)
gen_c_sharp_expressions_ObjectCreationExpression_expressions_StatementExpression = Generalization(general=expressions_StatementExpression, specific=c_sharp_expressions_ObjectCreationExpression)
gen_c_sharp_expressions_ArrayCreationExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=c_sharp_expressions_ArrayCreationExpression)
gen_c_sharp_expressions_ConditionalExpression_Expression = Generalization(general=Expression, specific=c_sharp_expressions_ConditionalExpression)
gen_c_sharp_expressions_CheckedExpression_PrimaryNoArrayCreationExpression = Generalization(general=PrimaryNoArrayCreationExpression, specific=c_sharp_expressions_CheckedExpression)
gen_c_sharp_expressions_UncheckedExpression_PrimaryNoArrayCreationExpression = Generalization(general=PrimaryNoArrayCreationExpression, specific=c_sharp_expressions_UncheckedExpression)
gen_c_sharp_expressions_SizeOfExpression_PrimaryNoArrayCreationExpression = Generalization(general=PrimaryNoArrayCreationExpression, specific=c_sharp_expressions_SizeOfExpression)
gen_c_sharp_expressions_AssignmentExpression_expressions_Expression = Generalization(general=expressions_Expression, specific=c_sharp_expressions_AssignmentExpression)
gen_c_sharp_expressions_AssignmentExpression_expressions_StatementExpression = Generalization(general=expressions_StatementExpression, specific=c_sharp_expressions_AssignmentExpression)
gen_c_sharp_expressions_TypeOfExpression_PrimaryNoArrayCreationExpression = Generalization(general=PrimaryNoArrayCreationExpression, specific=c_sharp_expressions_TypeOfExpression)
gen_c_sharp_expressions_DelegateCreationExpression_PrimaryNoArrayCreationExpression = Generalization(general=PrimaryNoArrayCreationExpression, specific=c_sharp_expressions_DelegateCreationExpression)
gen_c_sharp_expressions_PreIncrementExpression_StatementExpression = Generalization(general=StatementExpression, specific=c_sharp_expressions_PreIncrementExpression)
gen_c_sharp_expressions_PreDecrementExpression_StatementExpression = Generalization(general=StatementExpression, specific=c_sharp_expressions_PreDecrementExpression)
gen_c_sharp_types_Double_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Double)
gen_c_sharp_types_Object_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Object)
gen_c_sharp_types_String_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_String)
gen_c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType_ReferenceType = Generalization(general=ReferenceType, specific=c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType)
gen_c_sharp_types_PointerType_types_Type = Generalization(general=types_Type, specific=c_sharp_types_PointerType)
gen_c_sharp_types_ReferenceType_types_NonArrayType = Generalization(general=types_NonArrayType, specific=c_sharp_types_ReferenceType)
gen_c_sharp_types_ReferenceType_types_Type = Generalization(general=types_Type, specific=c_sharp_types_ReferenceType)
gen_c_sharp_types_SimpleType_types_Type = Generalization(general=types_Type, specific=c_sharp_types_SimpleType)
gen_c_sharp_types_SimpleType_types_NonArrayType = Generalization(general=types_NonArrayType, specific=c_sharp_types_SimpleType)
gen_c_sharp_types_Void_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Void)
gen_c_sharp_types_Decimal_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Decimal)
gen_c_sharp_types_Bool_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Bool)
gen_c_sharp_types_SByte_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_SByte)
gen_c_sharp_types_Byte_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Byte)
gen_c_sharp_types_Short_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Short)
gen_c_sharp_types_UShort_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_UShort)
gen_c_sharp_types_Int_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Int)
gen_c_sharp_types_UInt_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_UInt)
gen_c_sharp_types_Long_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Long)
gen_c_sharp_types_ULong_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_ULong)
gen_c_sharp_types_Char_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Char)
gen_c_sharp_types_Float_SimpleType = Generalization(general=SimpleType, specific=c_sharp_types_Float)
gen_c_sharp_literals_DecimalIntegerLiteral_Literal = Generalization(general=Literal, specific=c_sharp_literals_DecimalIntegerLiteral)
gen_c_sharp_literals_HexadecimalIntegerLiteral_Literal = Generalization(general=Literal, specific=c_sharp_literals_HexadecimalIntegerLiteral)
gen_c_sharp_literals_RealLiteral_Literal = Generalization(general=Literal, specific=c_sharp_literals_RealLiteral)
gen_c_sharp_literals_NullLiteral_Literal = Generalization(general=Literal, specific=c_sharp_literals_NullLiteral)
gen_c_sharp_literals_This_Literal = Generalization(general=Literal, specific=c_sharp_literals_This)
gen_c_sharp_literals_CharacterLiteral_Literal = Generalization(general=Literal, specific=c_sharp_literals_CharacterLiteral)
gen_c_sharp_types_PointerType_types_NonArrayType = Generalization(general=types_NonArrayType, specific=c_sharp_types_PointerType)
gen_c_sharp_modifiers_Abstract_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Abstract)
gen_c_sharp_modifiers_Extern_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Extern)
gen_c_sharp_modifiers_Internal_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Internal)
gen_c_sharp_modifiers_New_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_New)
gen_c_sharp_modifiers_OverrideModifier_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_OverrideModifier)
gen_c_sharp_modifiers_Private_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Private)
gen_c_sharp_modifiers_Protected_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Protected)
gen_c_sharp_modifiers_Public_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Public)
gen_c_sharp_modifiers_Partial_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Partial)
gen_c_sharp_modifiers_ReadOnly_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_ReadOnly)
gen_c_sharp_modifiers_Sealed_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Sealed)
gen_c_sharp_modifiers_Static_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Static)
gen_c_sharp_modifiers_Unsafe_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Unsafe)
gen_c_sharp_modifiers_Virtual_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Virtual)
gen_c_sharp_modifiers_Volatile_Modifier = Generalization(general=Modifier, specific=c_sharp_modifiers_Volatile)
gen_c_sharp_literals_Literal_PrimaryNoArrayCreationExpression = Generalization(general=PrimaryNoArrayCreationExpression, specific=c_sharp_literals_Literal)
gen_c_sharp_literals_BooleanLiteral_Literal = Generalization(general=Literal, specific=c_sharp_literals_BooleanLiteral)
gen_c_sharp_operators_AssignmentRightShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentRightShift)
gen_c_sharp_operators_AssignmentUnsignedRightShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentUnsignedRightShift)
gen_c_sharp_operators_Equal_EqualityOperator = Generalization(general=EqualityOperator, specific=c_sharp_operators_Equal)
gen_c_sharp_operators_NotEqual_EqualityOperator = Generalization(general=EqualityOperator, specific=c_sharp_operators_NotEqual)
gen_c_sharp_operators_GreaterThan_RelationOperator = Generalization(general=RelationOperator, specific=c_sharp_operators_GreaterThan)
gen_c_sharp_operators_GreaterThanOrEqual_RelationOperator = Generalization(general=RelationOperator, specific=c_sharp_operators_GreaterThanOrEqual)
gen_c_sharp_operators_LessThan_RelationOperator = Generalization(general=RelationOperator, specific=c_sharp_operators_LessThan)
gen_c_sharp_operators_LessThanOrEqual_RelationOperator = Generalization(general=RelationOperator, specific=c_sharp_operators_LessThanOrEqual)
gen_c_sharp_operators_Addition_operators_AdditiveOperator = Generalization(general=operators_AdditiveOperator, specific=c_sharp_operators_Addition)
gen_c_sharp_operators_Addition_operators_UnaryOperator = Generalization(general=operators_UnaryOperator, specific=c_sharp_operators_Addition)
gen_c_sharp_operators_Subtraction_operators_AdditiveOperator = Generalization(general=operators_AdditiveOperator, specific=c_sharp_operators_Subtraction)
gen_c_sharp_operators_Subtraction_operators_UnaryOperator = Generalization(general=operators_UnaryOperator, specific=c_sharp_operators_Subtraction)
gen_c_sharp_operators_Division_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=c_sharp_operators_Division)
gen_c_sharp_literals_StringLiteral_Literal = Generalization(general=Literal, specific=c_sharp_literals_StringLiteral)
gen_c_sharp_operators_Multiplication_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=c_sharp_operators_Multiplication)
gen_c_sharp_operators_AdditiveOperator_Operator = Generalization(general=Operator, specific=c_sharp_operators_AdditiveOperator)
gen_c_sharp_operators_AssignmentOperator_Operator = Generalization(general=Operator, specific=c_sharp_operators_AssignmentOperator)
gen_c_sharp_operators_EqualityOperator_Operator = Generalization(general=Operator, specific=c_sharp_operators_EqualityOperator)
gen_c_sharp_operators_MultiplicativeOperator_Operator = Generalization(general=Operator, specific=c_sharp_operators_MultiplicativeOperator)
gen_c_sharp_operators_RelationOperator_Operator = Generalization(general=Operator, specific=c_sharp_operators_RelationOperator)
gen_c_sharp_operators_ShiftOperator_Operator = Generalization(general=Operator, specific=c_sharp_operators_ShiftOperator)
gen_c_sharp_operators_UnaryOperator_Operator = Generalization(general=Operator, specific=c_sharp_operators_UnaryOperator)
gen_c_sharp_operators_UnaryModificationOperator_Operator = Generalization(general=Operator, specific=c_sharp_operators_UnaryModificationOperator)
gen_c_sharp_operators_Assignment_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_Assignment)
gen_c_sharp_operators_AssignmentAnd_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentAnd)
gen_c_sharp_operators_AssignmentDivision_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentDivision)
gen_c_sharp_operators_AssignmentExclusiveOr_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentExclusiveOr)
gen_c_sharp_operators_AssignmentMinus_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentMinus)
gen_c_sharp_operators_AssignmentModulo_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentModulo)
gen_c_sharp_operators_AssignmentMultiplication_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentMultiplication)
gen_c_sharp_operators_AssignmentLeftShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentLeftShift)
gen_c_sharp_operators_AssignmentOr_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentOr)
gen_c_sharp_operators_AssignmentPlus_AssignmentOperator = Generalization(general=AssignmentOperator, specific=c_sharp_operators_AssignmentPlus)
gen_c_sharp_operators_Remainder_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=c_sharp_operators_Remainder)
gen_c_sharp_operators_Complement_UnaryOperator = Generalization(general=UnaryOperator, specific=c_sharp_operators_Complement)
gen_c_sharp_operators_MinusMinus_UnaryModificationOperator = Generalization(general=UnaryModificationOperator, specific=c_sharp_operators_MinusMinus)
gen_c_sharp_operators_Negate_UnaryOperator = Generalization(general=UnaryOperator, specific=c_sharp_operators_Negate)
gen_c_sharp_operators_PlusPlus_UnaryModificationOperator = Generalization(general=UnaryModificationOperator, specific=c_sharp_operators_PlusPlus)
gen_c_sharp_operators_LeftShift_ShiftOperator = Generalization(general=ShiftOperator, specific=c_sharp_operators_LeftShift)
gen_c_sharp_operators_RightShift_ShiftOperator = Generalization(general=ShiftOperator, specific=c_sharp_operators_RightShift)
gen_c_sharp_operators_UnsignedRightShift_ShiftOperator = Generalization(general=ShiftOperator, specific=c_sharp_operators_UnsignedRightShift)
gen_c_sharp_operators_And_UnaryOperator = Generalization(general=UnaryOperator, specific=c_sharp_operators_And)
gen_c_sharp_operators_ExclusiveOr_UnaryOperator = Generalization(general=UnaryOperator, specific=c_sharp_operators_ExclusiveOr)
gen_c_sharp_operators_InclusiveOr_UnaryOperator = Generalization(general=UnaryOperator, specific=c_sharp_operators_InclusiveOr)
gen_c_sharp_operators_ConditionalAnd_UnaryOperator = Generalization(general=UnaryOperator, specific=c_sharp_operators_ConditionalAnd)
gen_c_sharp_operators_ConditionalOr_UnaryOperator = Generalization(general=UnaryOperator, specific=c_sharp_operators_ConditionalOr)

# Domain Model
domain_model = DomainModel(
    name="c_sharp",
    types={c_sharp_common_NamespaceOrTypeName, Identifier, c_sharp_common_Identifier, common_NamedElement, expressions_PrimaryNoArrayCreationExpression, c_sharp_common_NamedElement, c_sharp_namespaces_NamespaceBody, c_sharp_namespaces_TypeDeclaration, namespaces_NamespaceMemberDeclaration, classes_ClassMemberDeclaration, c_sharp_classes_Class, c_sharp_namespaces_CompilationUnit, namespaces_TypeDeclaration, UsingDirective, GlobalAttributes, NamespaceMemberDeclaration, c_sharp_namespaces_UsingDirective, NamedElement, NamespaceOrTypeName, c_sharp_namespaces_NamespaceMemberDeclaration, c_sharp_namespaces_Namespace, NamespaceBody, c_sharp_classes_Method, Type, Attributes, Modifier, ClassBase, ClassMemberDeclaration, c_sharp_classes_ClassBase, ClassOrInterfaceOrDelegateOrEnumType, c_sharp_classes_Block, Statement, c_sharp_classes_VariableInitializer, c_sharp_classes_ClassMemberDeclaration, c_sharp_classes_ConstantDeclaration, ConstantDeclarator, FormalParameterList, c_sharp_classes_FieldDeclaration, Block, c_sharp_classes_FormalParameterList, FixedParameter, ParameterArray, c_sharp_classes_FixedParameter, Ref, Out, c_sharp_classes_ParameterArray, Params, ArrayType, c_sharp_attributes_GlobalAttributes, GlobalAttributeTarget, Attribute, c_sharp_attributes_GlobalAttributeTarget, c_sharp_attributes_Attributes, AttributeTarget, c_sharp_attributes_AttributeTarget, Event, Return, VariableDeclarator, c_sharp_arrays_StackallocInitializer, VariableInitializer, Expression, c_sharp_arrays_ArrayInitializer, c_sharp_arrays_ArrayType, NonArrayType, RankSpecifier, c_sharp_arrays_RankSpecifier, c_sharp_statements_DeclarationStatement, VariableDeclaration, LocalConstantDeclaration, c_sharp_statements_EmbeddedStatement, c_sharp_statements_SimpleEmbeddedStatement, EmbeddedStatement, Unsafe, c_sharp_attributes_Attribute, AttributeArguments, c_sharp_attributes_AttributeArguments, ExpressionList, NamedArgumentList, c_sharp_attributes_NamedArgumentList, NamedArgument, c_sharp_attributes_NamedArgument, c_sharp_statements_Statement, c_sharp_statements_LabeledStatement, Case, statements_Statement, c_sharp_statements_IterationStatement, c_sharp_statements_WhileStatement, IterationStatement, c_sharp_statements_EmptyStatement, c_sharp_statements_ExpressionStatement, StatementExpression, c_sharp_statements_SelectionStatement, c_sharp_statements_IfStatement, SelectionStatement, c_sharp_statements_SwitchStatement, SwitchSection, c_sharp_statements_SwitchSection, SwitchLabel, c_sharp_statements_SwitchLabel, Default, c_sharp_statements_ForInitializer, c_sharp_statements_JumpStatement, c_sharp_statements_BreakStatement, JumpStatement, c_sharp_statements_ContinueStatement, c_sharp_statements_GotoStatement, c_sharp_statements_DoStatement, c_sharp_statements_ForStatement, ForInitializer, StatementExpressionList, c_sharp_statements_ForeachStatement, c_sharp_statements_ReturnStatement, c_sharp_statements_GeneralCatchClause, c_sharp_statements_FinallyClause, c_sharp_statements_CheckedStatement, c_sharp_statements_ThrowStatement, c_sharp_statements_TryStatement, SpecificCatchClause, GeneralCatchClause, FinallyClause, c_sharp_statements_SpecificCatchClause, PointerType, FixedPointerDeclarator, c_sharp_statements_FixedPointerDeclarator, c_sharp_statements_UncheckedStatement, c_sharp_statements_LockStatement, c_sharp_statements_ResourceAcquisition, c_sharp_statements_UsingStatement, ResourceAcquisition, c_sharp_statements_FixedStatement, c_sharp_expressions_StatementExpression, c_sharp_expressions_StatementExpressionList, c_sharp_expressions_Expression, classes_VariableInitializer, c_sharp_expressions_ExpressionList, c_sharp_expressions_Argument, c_sharp_statements_VariableDeclaration, statements_ForInitializer, statements_ResourceAcquisition, c_sharp_statements_VariableDeclarator, c_sharp_statements_LocalConstantDeclaration, c_sharp_statements_ConstantDeclarator, c_sharp_expressions_InvocationExpression, expressions_PrimaryExtendedExpressionType, expressions_StatementExpression, ArgumentList, c_sharp_expressions_PostIncrementExpression, c_sharp_expressions_PostDecrementExpression, c_sharp_expressions_PointerMemberAccess, c_sharp_expressions_BaseAccess, PrimaryNoArrayCreationExpression, c_sharp_expressions_ArgumentList, Argument, c_sharp_expressions_PrimaryExpression, c_sharp_expressions_PrimaryNoArrayCreationExpression, PrimaryExpression, c_sharp_expressions_PrimaryExtendedExpressionType, c_sharp_expressions_MemberAccess, PrimaryExtendedExpressionType, SimpleType, c_sharp_expressions_ElementAccess, ArrayInitializer, c_sharp_expressions_ParenthesizedExpression, c_sharp_expressions_UnaryExpression, MemberAccess, c_sharp_expressions_ObjectCreationExpression, c_sharp_expressions_ArrayCreationExpression, CastExpression, AddressOfExpression, c_sharp_expressions_ConditionalExpression, ConditionalOrExpression, Addition, Subtraction, Negate, Complement, Multiplication, UnaryExpression, PreIncrementExpression, PreDecrementExpression, c_sharp_expressions_CheckedExpression, c_sharp_expressions_UncheckedExpression, c_sharp_expressions_SizeOfExpression, c_sharp_expressions_AssignmentExpression, expressions_Expression, AssignmentOperator, c_sharp_expressions_TypeOfExpression, c_sharp_expressions_DelegateCreationExpression, c_sharp_expressions_MultiplicativeExpression, Division, Remainder, c_sharp_expressions_PreIncrementExpression, c_sharp_expressions_PreDecrementExpression, c_sharp_expressions_CastExpression, LeftShift, c_sharp_expressions_AddressOfExpression, AdditiveExpression, c_sharp_expressions_AdditiveExpression, MultiplicativeExpression, c_sharp_expressions_ShiftExpression, RightShift, c_sharp_expressions_EqualityExpression, RelationalExpression, Equal, c_sharp_expressions_RelationalExpression, ShiftExpression, LessThan, LessThanOrEqual, GreaterThan, GreaterThanOrEqual, ConditionalAnd, c_sharp_expressions_ConditionalOrExpression, ConditionalAndExpression, ConditionalOr, c_sharp_types_Type, NotEqual, c_sharp_expressions_AndExpression, EqualityExpression, And, c_sharp_expressions_ExclusiveOrExpression, AndExpression, ExclusiveOr, c_sharp_expressions_InclusiveOrExpression, ExclusiveOrExpression, InclusiveOr, c_sharp_expressions_ConditionalAndExpression, InclusiveOrExpression, c_sharp_types_Object, c_sharp_types_String, c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType, ReferenceType, c_sharp_types_PointerType, c_sharp_types_NonArrayType, c_sharp_types_ReferenceType, types_NonArrayType, types_Type, c_sharp_types_SimpleType, c_sharp_types_Void, c_sharp_types_Decimal, c_sharp_types_Bool, c_sharp_types_SByte, c_sharp_types_Byte, c_sharp_types_Short, c_sharp_types_UShort, c_sharp_types_Int, c_sharp_types_UInt, c_sharp_types_Long, c_sharp_types_ULong, c_sharp_types_Char, c_sharp_types_Float, c_sharp_types_Double, c_sharp_literals_DecimalIntegerLiteral, c_sharp_literals_HexadecimalIntegerLiteral, c_sharp_literals_RealLiteral, c_sharp_literals_NullLiteral, c_sharp_literals_This, c_sharp_literals_CharacterLiteral, c_sharp_modifiers_Modifier, c_sharp_modifiers_Abstract, c_sharp_modifiers_Extern, c_sharp_modifiers_Internal, c_sharp_modifiers_New, c_sharp_modifiers_OverrideModifier, c_sharp_modifiers_Private, c_sharp_modifiers_Protected, c_sharp_modifiers_Public, c_sharp_modifiers_Partial, c_sharp_modifiers_ReadOnly, c_sharp_modifiers_Sealed, c_sharp_modifiers_Static, c_sharp_modifiers_Unsafe, c_sharp_modifiers_Virtual, c_sharp_modifiers_Volatile, c_sharp_literals_Literal, c_sharp_literals_BooleanLiteral, Literal, c_sharp_operators_AssignmentRightShift, c_sharp_operators_AssignmentUnsignedRightShift, c_sharp_operators_Equal, EqualityOperator, c_sharp_operators_NotEqual, c_sharp_operators_GreaterThan, RelationOperator, c_sharp_operators_GreaterThanOrEqual, c_sharp_operators_LessThan, c_sharp_operators_LessThanOrEqual, c_sharp_operators_Addition, operators_AdditiveOperator, operators_UnaryOperator, c_sharp_operators_Subtraction, c_sharp_operators_Division, MultiplicativeOperator, c_sharp_literals_StringLiteral, c_sharp_operators_Multiplication, c_sharp_keywords_Out, c_sharp_keywords_Ref, c_sharp_keywords_Params, c_sharp_keywords_Case, c_sharp_keywords_Default, c_sharp_keywords_Return, c_sharp_keywords_Event, c_sharp_operators_Operator, c_sharp_operators_AdditiveOperator, Operator, c_sharp_operators_AssignmentOperator, c_sharp_operators_EqualityOperator, c_sharp_operators_MultiplicativeOperator, c_sharp_operators_RelationOperator, c_sharp_operators_ShiftOperator, c_sharp_operators_UnaryOperator, c_sharp_operators_UnaryModificationOperator, c_sharp_operators_Assignment, c_sharp_operators_AssignmentAnd, c_sharp_operators_AssignmentDivision, c_sharp_operators_AssignmentExclusiveOr, c_sharp_operators_AssignmentMinus, c_sharp_operators_AssignmentModulo, c_sharp_operators_AssignmentMultiplication, c_sharp_operators_AssignmentLeftShift, c_sharp_operators_AssignmentOr, c_sharp_operators_AssignmentPlus, c_sharp_operators_Remainder, c_sharp_operators_Complement, UnaryOperator, c_sharp_operators_MinusMinus, UnaryModificationOperator, c_sharp_operators_Negate, c_sharp_operators_PlusPlus, c_sharp_operators_LeftShift, ShiftOperator, c_sharp_operators_RightShift, c_sharp_operators_UnsignedRightShift, c_sharp_operators_And, c_sharp_operators_ExclusiveOr, c_sharp_operators_InclusiveOr, c_sharp_operators_ConditionalAnd, c_sharp_operators_ConditionalOr},
    associations={parts0, usingDirectives11, namespaceMemberDeclaration13, usingDirectives1, globalAttributes2, namespaceMemberDeclaration4, namespaceOrTypeName6, namespaceName7, namespaceBody9, attributes24, modifiers26, returnType29, interfaceType31, attributes16, modifiers17, classBase19, classMemberDeclarations21, types23, statement62, attributes63, modifiers65, type68, constantDeclarator71, formalParameterList34, block36, fixedParameter38, parameterArray39, attributes41, ref43, out45, type47, identifier50, attributes53, params55, arrayType57, identifier59, globalAttributeTarget91, attribute92, identifier94, attributeTarget96, attribute97, event100, attributes73, modifiers75, type78, variableDeclarator81, type83, expression85, variableInitializer87, nonArrayType88, rankSpecifier89, variableDeclaration121, localConstantDeclaration122, unsafe124, return101, type103, namespaceOrTypeName106, attributeArguments108, expressionList110, namedArgumentList111, namedArgument113, identifier114, expression116, case142, statement119, expression144, expression147, block125, embeddedStatement149, statementExpression128, expression129, embeddedStatement131, expression133, switchSection135, switchLabel137, statement138, default141, expression171, embeddedStatement174, embeddedStatement152, expression154, forInitializer157, expression158, statementExpressionList161, embeddedStatement163, type166, identifier168, default177, case179, expression182, identifier185, expression188, block205, block208, block210, block212, expression190, block192, specificCatchClause194, generalCatchClause196, finallyClause198, classType200, identifier202, pointerType225, fixedPointerDeclarator226, embeddedStatement228, identifier231, expression233, block214, expression216, embeddedStatement218, resourceAcquisition221, embeddedStatement222, statementExpression250, expression252, out254, type236, VariableDeclarator238, VariableInitializer241, type243, constantDeclarator245, expression248, argumentList269, identifier270, ref256, expression259, argument262, simpleType263, identifier264, expressionList267, arrayInitializer293, expression295, memberAccess297, primaryExpression298, primaryExtendedExpressionType300, expressionList272, identifier274, type277, argumentList279, type282, arrayType284, expressionList287, rankSpecifier290, preDecrementExpression316, castExpression318, addressOfExpression320, expression322, addition302, subtraction304, negate306, complement308, multiplication310, unaryExpression312, preIncrementExpression314, expression340, expression342, type344, conditionalOrExpression324, unaryExpression326, assignmentOperator328, expression330, type333, delegateType335, expression337, unaryExpression355, unaryExpression357, multiplication359, division362, unaryExpression346, unaryExpression348, type350, unaryExpression352, leftShift374, remainder376, remainder364, multiplicativeExpression366, addition367, subtraction370, rightShift373, relationalExpression393, equal394, additiveExpression379, shiftExpression381, type382, lessThan385, lessThanOrEqual387, greaterThan389, greaterThanOrEqual391, conditionalAnd408, conditionalAndExpression410, conditionalOr411, notEqual396, equalityExpression398, and399, andExpression401, exclusiveOr402, exclusiveOrExpression404, inclusiveOr405, inclusiveOrExpression407, namespaceOrTypeName413, simpleType415, referenceType417},
    generalizations={gen_c_sharp_common_Identifier_common_NamedElement, gen_c_sharp_common_Identifier_expressions_PrimaryNoArrayCreationExpression, gen_c_sharp_namespaces_TypeDeclaration_namespaces_NamespaceMemberDeclaration, gen_c_sharp_namespaces_TypeDeclaration_classes_ClassMemberDeclaration, gen_c_sharp_classes_Class_namespaces_TypeDeclaration, gen_c_sharp_classes_Class_common_NamedElement, gen_c_sharp_namespaces_UsingDirective_NamedElement, gen_c_sharp_namespaces_Namespace_NamespaceMemberDeclaration, gen_c_sharp_classes_Method_classes_ClassMemberDeclaration, gen_c_sharp_classes_Method_common_NamedElement, gen_c_sharp_classes_ConstantDeclaration_ClassMemberDeclaration, gen_c_sharp_classes_FieldDeclaration_ClassMemberDeclaration, gen_c_sharp_arrays_StackallocInitializer_VariableInitializer, gen_c_sharp_arrays_ArrayInitializer_VariableInitializer, gen_c_sharp_arrays_ArrayType_Type, gen_c_sharp_statements_DeclarationStatement_Statement, gen_c_sharp_statements_EmbeddedStatement_Statement, gen_c_sharp_statements_SimpleEmbeddedStatement_EmbeddedStatement, gen_c_sharp_statements_LabeledStatement_statements_Statement, gen_c_sharp_statements_LabeledStatement_common_NamedElement, gen_c_sharp_statements_IterationStatement_EmbeddedStatement, gen_c_sharp_statements_WhileStatement_IterationStatement, gen_c_sharp_statements_EmptyStatement_EmbeddedStatement, gen_c_sharp_statements_ExpressionStatement_EmbeddedStatement, gen_c_sharp_statements_SelectionStatement_EmbeddedStatement, gen_c_sharp_statements_IfStatement_SelectionStatement, gen_c_sharp_statements_SwitchStatement_SelectionStatement, gen_c_sharp_statements_JumpStatement_EmbeddedStatement, gen_c_sharp_statements_BreakStatement_JumpStatement, gen_c_sharp_statements_ContinueStatement_JumpStatement, gen_c_sharp_statements_GotoStatement_JumpStatement, gen_c_sharp_statements_DoStatement_IterationStatement, gen_c_sharp_statements_ForStatement_IterationStatement, gen_c_sharp_statements_ForeachStatement_IterationStatement, gen_c_sharp_statements_ReturnStatement_JumpStatement, gen_c_sharp_statements_CheckedStatement_EmbeddedStatement, gen_c_sharp_statements_ThrowStatement_JumpStatement, gen_c_sharp_statements_TryStatement_EmbeddedStatement, gen_c_sharp_statements_UncheckedStatement_EmbeddedStatement, gen_c_sharp_statements_LockStatement_EmbeddedStatement, gen_c_sharp_statements_UsingStatement_EmbeddedStatement, gen_c_sharp_statements_FixedStatement_EmbeddedStatement, gen_c_sharp_expressions_StatementExpressionList_ForInitializer, gen_c_sharp_expressions_Expression_classes_VariableInitializer, gen_c_sharp_expressions_Expression_statements_ResourceAcquisition, gen_c_sharp_statements_VariableDeclaration_statements_ForInitializer, gen_c_sharp_statements_VariableDeclaration_statements_ResourceAcquisition, gen_c_sharp_statements_VariableDeclarator_NamedElement, gen_c_sharp_statements_ConstantDeclarator_NamedElement, gen_c_sharp_expressions_InvocationExpression_expressions_PrimaryExtendedExpressionType, gen_c_sharp_expressions_InvocationExpression_expressions_StatementExpression, gen_c_sharp_expressions_PostIncrementExpression_expressions_PrimaryExtendedExpressionType, gen_c_sharp_expressions_PostIncrementExpression_expressions_StatementExpression, gen_c_sharp_expressions_PostDecrementExpression_expressions_PrimaryExtendedExpressionType, gen_c_sharp_expressions_PostDecrementExpression_expressions_StatementExpression, gen_c_sharp_expressions_PointerMemberAccess_PrimaryExtendedExpressionType, gen_c_sharp_expressions_BaseAccess_PrimaryNoArrayCreationExpression, gen_c_sharp_expressions_PrimaryNoArrayCreationExpression_PrimaryExpression, gen_c_sharp_expressions_MemberAccess_PrimaryExtendedExpressionType, gen_c_sharp_expressions_ElementAccess_PrimaryExtendedExpressionType, gen_c_sharp_expressions_ParenthesizedExpression_PrimaryNoArrayCreationExpression, gen_c_sharp_expressions_ObjectCreationExpression_expressions_PrimaryNoArrayCreationExpression, gen_c_sharp_expressions_ObjectCreationExpression_expressions_StatementExpression, gen_c_sharp_expressions_ArrayCreationExpression_PrimaryExpression, gen_c_sharp_expressions_ConditionalExpression_Expression, gen_c_sharp_expressions_CheckedExpression_PrimaryNoArrayCreationExpression, gen_c_sharp_expressions_UncheckedExpression_PrimaryNoArrayCreationExpression, gen_c_sharp_expressions_SizeOfExpression_PrimaryNoArrayCreationExpression, gen_c_sharp_expressions_AssignmentExpression_expressions_Expression, gen_c_sharp_expressions_AssignmentExpression_expressions_StatementExpression, gen_c_sharp_expressions_TypeOfExpression_PrimaryNoArrayCreationExpression, gen_c_sharp_expressions_DelegateCreationExpression_PrimaryNoArrayCreationExpression, gen_c_sharp_expressions_PreIncrementExpression_StatementExpression, gen_c_sharp_expressions_PreDecrementExpression_StatementExpression, gen_c_sharp_types_Double_SimpleType, gen_c_sharp_types_Object_SimpleType, gen_c_sharp_types_String_SimpleType, gen_c_sharp_types_ClassOrInterfaceOrDelegateOrEnumType_ReferenceType, gen_c_sharp_types_PointerType_types_Type, gen_c_sharp_types_ReferenceType_types_NonArrayType, gen_c_sharp_types_ReferenceType_types_Type, gen_c_sharp_types_SimpleType_types_Type, gen_c_sharp_types_SimpleType_types_NonArrayType, gen_c_sharp_types_Void_SimpleType, gen_c_sharp_types_Decimal_SimpleType, gen_c_sharp_types_Bool_SimpleType, gen_c_sharp_types_SByte_SimpleType, gen_c_sharp_types_Byte_SimpleType, gen_c_sharp_types_Short_SimpleType, gen_c_sharp_types_UShort_SimpleType, gen_c_sharp_types_Int_SimpleType, gen_c_sharp_types_UInt_SimpleType, gen_c_sharp_types_Long_SimpleType, gen_c_sharp_types_ULong_SimpleType, gen_c_sharp_types_Char_SimpleType, gen_c_sharp_types_Float_SimpleType, gen_c_sharp_literals_DecimalIntegerLiteral_Literal, gen_c_sharp_literals_HexadecimalIntegerLiteral_Literal, gen_c_sharp_literals_RealLiteral_Literal, gen_c_sharp_literals_NullLiteral_Literal, gen_c_sharp_literals_This_Literal, gen_c_sharp_literals_CharacterLiteral_Literal, gen_c_sharp_types_PointerType_types_NonArrayType, gen_c_sharp_modifiers_Abstract_Modifier, gen_c_sharp_modifiers_Extern_Modifier, gen_c_sharp_modifiers_Internal_Modifier, gen_c_sharp_modifiers_New_Modifier, gen_c_sharp_modifiers_OverrideModifier_Modifier, gen_c_sharp_modifiers_Private_Modifier, gen_c_sharp_modifiers_Protected_Modifier, gen_c_sharp_modifiers_Public_Modifier, gen_c_sharp_modifiers_Partial_Modifier, gen_c_sharp_modifiers_ReadOnly_Modifier, gen_c_sharp_modifiers_Sealed_Modifier, gen_c_sharp_modifiers_Static_Modifier, gen_c_sharp_modifiers_Unsafe_Modifier, gen_c_sharp_modifiers_Virtual_Modifier, gen_c_sharp_modifiers_Volatile_Modifier, gen_c_sharp_literals_Literal_PrimaryNoArrayCreationExpression, gen_c_sharp_literals_BooleanLiteral_Literal, gen_c_sharp_operators_AssignmentRightShift_AssignmentOperator, gen_c_sharp_operators_AssignmentUnsignedRightShift_AssignmentOperator, gen_c_sharp_operators_Equal_EqualityOperator, gen_c_sharp_operators_NotEqual_EqualityOperator, gen_c_sharp_operators_GreaterThan_RelationOperator, gen_c_sharp_operators_GreaterThanOrEqual_RelationOperator, gen_c_sharp_operators_LessThan_RelationOperator, gen_c_sharp_operators_LessThanOrEqual_RelationOperator, gen_c_sharp_operators_Addition_operators_AdditiveOperator, gen_c_sharp_operators_Addition_operators_UnaryOperator, gen_c_sharp_operators_Subtraction_operators_AdditiveOperator, gen_c_sharp_operators_Subtraction_operators_UnaryOperator, gen_c_sharp_operators_Division_MultiplicativeOperator, gen_c_sharp_literals_StringLiteral_Literal, gen_c_sharp_operators_Multiplication_MultiplicativeOperator, gen_c_sharp_operators_AdditiveOperator_Operator, gen_c_sharp_operators_AssignmentOperator_Operator, gen_c_sharp_operators_EqualityOperator_Operator, gen_c_sharp_operators_MultiplicativeOperator_Operator, gen_c_sharp_operators_RelationOperator_Operator, gen_c_sharp_operators_ShiftOperator_Operator, gen_c_sharp_operators_UnaryOperator_Operator, gen_c_sharp_operators_UnaryModificationOperator_Operator, gen_c_sharp_operators_Assignment_AssignmentOperator, gen_c_sharp_operators_AssignmentAnd_AssignmentOperator, gen_c_sharp_operators_AssignmentDivision_AssignmentOperator, gen_c_sharp_operators_AssignmentExclusiveOr_AssignmentOperator, gen_c_sharp_operators_AssignmentMinus_AssignmentOperator, gen_c_sharp_operators_AssignmentModulo_AssignmentOperator, gen_c_sharp_operators_AssignmentMultiplication_AssignmentOperator, gen_c_sharp_operators_AssignmentLeftShift_AssignmentOperator, gen_c_sharp_operators_AssignmentOr_AssignmentOperator, gen_c_sharp_operators_AssignmentPlus_AssignmentOperator, gen_c_sharp_operators_Remainder_MultiplicativeOperator, gen_c_sharp_operators_Complement_UnaryOperator, gen_c_sharp_operators_MinusMinus_UnaryModificationOperator, gen_c_sharp_operators_Negate_UnaryOperator, gen_c_sharp_operators_PlusPlus_UnaryModificationOperator, gen_c_sharp_operators_LeftShift_ShiftOperator, gen_c_sharp_operators_RightShift_ShiftOperator, gen_c_sharp_operators_UnsignedRightShift_ShiftOperator, gen_c_sharp_operators_And_UnaryOperator, gen_c_sharp_operators_ExclusiveOr_UnaryOperator, gen_c_sharp_operators_InclusiveOr_UnaryOperator, gen_c_sharp_operators_ConditionalAnd_UnaryOperator, gen_c_sharp_operators_ConditionalOr_UnaryOperator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)