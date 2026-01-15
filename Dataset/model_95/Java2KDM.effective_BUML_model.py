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

# Enumerations
InfixExpressionKind: Enumeration = Enumeration(
    name="InfixExpressionKind",
    literals={
            EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="DIVIDE"),
			EnumerationLiteral(name="REMAINDER"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="LEFT_SHIFT"),
			EnumerationLiteral(name="RIGHT_SHIFT_SIGNED"),
			EnumerationLiteral(name="RIGHT_SHIFT_UNSIGNED"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="CONDITIONAL_AND"),
			EnumerationLiteral(name="CONDITIONAL_OR"),
			EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="LESS_EQUALS"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS")
    }
)

PrefixExpressionKind: Enumeration = Enumeration(
    name="PrefixExpressionKind",
    literals={
            EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="COMPLEMENT"),
			EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT"),
			EnumerationLiteral(name="PLUS")
    }
)

PostfixExpressionKind: Enumeration = Enumeration(
    name="PostfixExpressionKind",
    literals={
            EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT")
    }
)

VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected")
    }
)

InheritanceKind: Enumeration = Enumeration(
    name="InheritanceKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="final")
    }
)

AssignmentKind: Enumeration = Enumeration(
    name="AssignmentKind",
    literals={
            EnumerationLiteral(name="PLUS_ASSIGN"),
			EnumerationLiteral(name="MINUS_ASSIGN"),
			EnumerationLiteral(name="TIMES_ASSIGN"),
			EnumerationLiteral(name="DIVIDE_ASSIGN"),
			EnumerationLiteral(name="BIT_AND_ASSIGN"),
			EnumerationLiteral(name="BIT_OR_ASSIGN"),
			EnumerationLiteral(name="BIT_XOR_ASSIGN"),
			EnumerationLiteral(name="REMAINDER_ASSIGN"),
			EnumerationLiteral(name="LEFT_SHIFT_ASSIGN"),
			EnumerationLiteral(name="RIGHT_SHIFT_SIGNED_ASSIGN"),
			EnumerationLiteral(name="RIGHT_SHIFT_UNSIGNED_ASSIGN"),
			EnumerationLiteral(name="ASSIGN")
    }
)

# Classes
java_MethodRef = Class(name="java::MethodRef")
java_PrimitiveTypeDouble = Class(name="java::PrimitiveTypeDouble")
PrimitiveType = Class(name="PrimitiveType")
java_WhileStatement = Class(name="java::WhileStatement")
java_Statement = Class(name="java::Statement", is_abstract=True)
java_MethodRefParameter = Class(name="java::MethodRefParameter")
ASTNode = Class(name="ASTNode")
java_SuperConstructorInvocation = Class(name="java::SuperConstructorInvocation")
Statement = Class(name="Statement")
AbstractMethodInvocation = Class(name="AbstractMethodInvocation")
java_Expression = Class(name="java::Expression", is_abstract=True)
java_TypeParameter = Class(name="java::TypeParameter")
java_PrimitiveTypeVoid = Class(name="java::PrimitiveTypeVoid")
java_InterfaceDeclaration = Class(name="java::InterfaceDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
java_UnresolvedTypeDeclaration = Class(name="java::UnresolvedTypeDeclaration")
UnresolvedItem = Class(name="UnresolvedItem")
java_TypeDeclaration = Class(name="java::TypeDeclaration", is_abstract=True)
java_StringLiteral = Class(name="java::StringLiteral")
Expression = Class(name="Expression")
java_AnnotationTypeDeclaration = Class(name="java::AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
java_SynchronizedStatement = Class(name="java::SynchronizedStatement")
java_Block = Class(name="java::Block")
java_ThisExpression = Class(name="java::ThisExpression")
AbstractTypeQualifiedExpression = Class(name="AbstractTypeQualifiedExpression")
java_VariableDeclarationFragment = Class(name="java::VariableDeclarationFragment")
VariableDeclaration = Class(name="VariableDeclaration")
java_AbstractVariablesContainer = Class(name="java::AbstractVariablesContainer", is_abstract=True)
java_WildCardType = Class(name="java::WildCardType")
Type = Class(name="Type")
java_TypeAccess = Class(name="java::TypeAccess")
java_EnumConstantDeclaration = Class(name="java::EnumConstantDeclaration")
BodyDeclaration = Class(name="BodyDeclaration")
java_TypeLiteral = Class(name="java::TypeLiteral")
java_AbstractMethodDeclaration = Class(name="java::AbstractMethodDeclaration", is_abstract=True)
java_SingleVariableDeclaration = Class(name="java::SingleVariableDeclaration")
java_PrimitiveTypeLong = Class(name="java::PrimitiveTypeLong")
java_PrimitiveTypeBoolean = Class(name="java::PrimitiveTypeBoolean")
java_CharacterLiteral = Class(name="java::CharacterLiteral")
java_FieldDeclaration = Class(name="java::FieldDeclaration")
AbstractVariablesContainer = Class(name="AbstractVariablesContainer")
java_Modifier = Class(name="java::Modifier")
java_AbstractTypeDeclaration = Class(name="java::AbstractTypeDeclaration", is_abstract=True)
java_Comment = Class(name="java::Comment", is_abstract=True)
java_PrimitiveTypeByte = Class(name="java::PrimitiveTypeByte")
java_ArrayInitializer = Class(name="java::ArrayInitializer")
java_BodyDeclaration = Class(name="java::BodyDeclaration", is_abstract=True)
java_AbstractMethodInvocation = Class(name="java::AbstractMethodInvocation", is_abstract=True)
java_AbstractTypeQualifiedExpression = Class(name="java::AbstractTypeQualifiedExpression", is_abstract=True)
java_Assignment = Class(name="java::Assignment")
java_PostfixExpression = Class(name="java::PostfixExpression")
java_ASTNode = Class(name="java::ASTNode", is_abstract=True)
java_AnnotationMemberValuePair = Class(name="java::AnnotationMemberValuePair")
NamedElement = Class(name="NamedElement")
java_AnnotationTypeMemberDeclaration = Class(name="java::AnnotationTypeMemberDeclaration")
java_EnumDeclaration = Class(name="java::EnumDeclaration")
java_ImportDeclaration = Class(name="java::ImportDeclaration")
java_NamedElement = Class(name="java::NamedElement", is_abstract=True)
java_EnhancedForStatement = Class(name="java::EnhancedForStatement")
java_EmptyStatement = Class(name="java::EmptyStatement")
java_ReturnStatement = Class(name="java::ReturnStatement")
java_ClassFile = Class(name="java::ClassFile")
java_CompilationUnit = Class(name="java::CompilationUnit")
NamespaceAccess = Class(name="NamespaceAccess")
java_Type = Class(name="java::Type", is_abstract=True)
java_PrimitiveTypeFloat = Class(name="java::PrimitiveTypeFloat")
java_PrimitiveType = Class(name="java::PrimitiveType")
java_ArrayLengthAccess = Class(name="java::ArrayLengthAccess")
java_SingleVariableAccess = Class(name="java::SingleVariableAccess")
java_VariableDeclaration = Class(name="java::VariableDeclaration", is_abstract=True)
java_Annotation = Class(name="java::Annotation")
java_MemberRef = Class(name="java::MemberRef")
java_SwitchStatement = Class(name="java::SwitchStatement")
java_ArrayCreation = Class(name="java::ArrayCreation")
java_UnresolvedItem = Class(name="java::UnresolvedItem")
java_ParenthesizedExpression = Class(name="java::ParenthesizedExpression")
java_PrimitiveTypeShort = Class(name="java::PrimitiveTypeShort")
java_MethodDeclaration = Class(name="java::MethodDeclaration")
AbstractMethodDeclaration = Class(name="AbstractMethodDeclaration")
java_UnresolvedItemAccess = Class(name="java::UnresolvedItemAccess")
java_IfStatement = Class(name="java::IfStatement")
java_InfixExpression = Class(name="java::InfixExpression")
java_Archive = Class(name="java::Archive")
java_BooleanLiteral = Class(name="java::BooleanLiteral")
java_ParameterizedType = Class(name="java::ParameterizedType")
java_SuperFieldAccess = Class(name="java::SuperFieldAccess")
java_TryStatement = Class(name="java::TryStatement")
java_CatchClause = Class(name="java::CatchClause")
java_ExpressionStatement = Class(name="java::ExpressionStatement")
java_Package = Class(name="java::Package")
java_BreakStatement = Class(name="java::BreakStatement")
java_LabeledStatement = Class(name="java::LabeledStatement")
java_TagElement = Class(name="java::TagElement")
java_ArrayType = Class(name="java::ArrayType")
java_PrefixExpression = Class(name="java::PrefixExpression")
java_AnonymousClassDeclaration = Class(name="java::AnonymousClassDeclaration")
java_SuperMethodInvocation = Class(name="java::SuperMethodInvocation")
java_ConstructorDeclaration = Class(name="java::ConstructorDeclaration")
java_PrimitiveTypeInt = Class(name="java::PrimitiveTypeInt")
java_SwitchCase = Class(name="java::SwitchCase")
java_NullLiteral = Class(name="java::NullLiteral")
java_ForStatement = Class(name="java::ForStatement")
java_ConditionalExpression = Class(name="java::ConditionalExpression")
java_ArrayAccess = Class(name="java::ArrayAccess")
java_VariableDeclarationExpression = Class(name="java::VariableDeclarationExpression")
java_PrimitiveTypeChar = Class(name="java::PrimitiveTypeChar")
java_Initializer = Class(name="java::Initializer")
java_DoStatement = Class(name="java::DoStatement")
java_ContinueStatement = Class(name="java::ContinueStatement")
java_InstanceofExpression = Class(name="java::InstanceofExpression")
java_AssertStatement = Class(name="java::AssertStatement")
java_TypeDeclarationStatement = Class(name="java::TypeDeclarationStatement")
java_ClassDeclaration = Class(name="java::ClassDeclaration")
java_MethodInvocation = Class(name="java::MethodInvocation")
java_FieldAccess = Class(name="java::FieldAccess")
java_CastExpression = Class(name="java::CastExpression")
java_ThrowStatement = Class(name="java::ThrowStatement")
java_ConstructorInvocation = Class(name="java::ConstructorInvocation")
java_NumberLiteral = Class(name="java::NumberLiteral")
java_ClassInstanceCreation = Class(name="java::ClassInstanceCreation")
java_VariableDeclarationStatement = Class(name="java::VariableDeclarationStatement")
java_Model = Class(name="java::Model")
java_NamespaceAccess = Class(name="java::NamespaceAccess", is_abstract=True)

# java_MethodRef class attributes and methods

# java_PrimitiveTypeDouble class attributes and methods

# PrimitiveType class attributes and methods

# java_WhileStatement class attributes and methods

# java_Statement class attributes and methods

# java_MethodRefParameter class attributes and methods

# ASTNode class attributes and methods

# java_SuperConstructorInvocation class attributes and methods

# Statement class attributes and methods

# AbstractMethodInvocation class attributes and methods

# java_Expression class attributes and methods

# java_TypeParameter class attributes and methods

# java_PrimitiveTypeVoid class attributes and methods

# java_InterfaceDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# java_UnresolvedTypeDeclaration class attributes and methods

# UnresolvedItem class attributes and methods

# java_TypeDeclaration class attributes and methods

# java_StringLiteral class attributes and methods
java_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
java_StringLiteral.attributes={java_StringLiteral_escapedValue}

# Expression class attributes and methods

# java_AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# java_SynchronizedStatement class attributes and methods

# java_Block class attributes and methods

# java_ThisExpression class attributes and methods

# AbstractTypeQualifiedExpression class attributes and methods

# java_VariableDeclarationFragment class attributes and methods

# VariableDeclaration class attributes and methods

# java_AbstractVariablesContainer class attributes and methods

# java_WildCardType class attributes and methods

# Type class attributes and methods

# java_TypeAccess class attributes and methods

# java_EnumConstantDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# java_TypeLiteral class attributes and methods

# java_AbstractMethodDeclaration class attributes and methods

# java_SingleVariableDeclaration class attributes and methods

# java_PrimitiveTypeLong class attributes and methods

# java_PrimitiveTypeBoolean class attributes and methods

# java_CharacterLiteral class attributes and methods
java_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
java_CharacterLiteral.attributes={java_CharacterLiteral_escapedValue}

# java_FieldDeclaration class attributes and methods

# AbstractVariablesContainer class attributes and methods

# java_Modifier class attributes and methods
java_Modifier_static: Property = Property(name="static", type=BooleanType)
java_Modifier_visibility: Property = Property(name="visibility", type=StringType)
java_Modifier_inheritance: Property = Property(name="inheritance", type=StringType)
java_Modifier.attributes={java_Modifier_visibility, java_Modifier_static, java_Modifier_inheritance}

# java_AbstractTypeDeclaration class attributes and methods

# java_Comment class attributes and methods
java_Comment_content: Property = Property(name="content", type=StringType)
java_Comment.attributes={java_Comment_content}

# java_PrimitiveTypeByte class attributes and methods

# java_ArrayInitializer class attributes and methods

# java_BodyDeclaration class attributes and methods

# java_AbstractMethodInvocation class attributes and methods

# java_AbstractTypeQualifiedExpression class attributes and methods

# java_Assignment class attributes and methods
java_Assignment_operator: Property = Property(name="operator", type=StringType)
java_Assignment.attributes={java_Assignment_operator}

# java_PostfixExpression class attributes and methods
java_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
java_PostfixExpression.attributes={java_PostfixExpression_operator}

# java_ASTNode class attributes and methods

# java_AnnotationMemberValuePair class attributes and methods

# NamedElement class attributes and methods

# java_AnnotationTypeMemberDeclaration class attributes and methods

# java_EnumDeclaration class attributes and methods

# java_ImportDeclaration class attributes and methods
java_ImportDeclaration_static: Property = Property(name="static", type=BooleanType)
java_ImportDeclaration.attributes={java_ImportDeclaration_static}

# java_NamedElement class attributes and methods
java_NamedElement_name: Property = Property(name="name", type=StringType)
java_NamedElement_proxy: Property = Property(name="proxy", type=BooleanType)
java_NamedElement.attributes={java_NamedElement_name, java_NamedElement_proxy}

# java_EnhancedForStatement class attributes and methods

# java_EmptyStatement class attributes and methods

# java_ReturnStatement class attributes and methods

# java_ClassFile class attributes and methods

# java_CompilationUnit class attributes and methods
java_CompilationUnit_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java_CompilationUnit.attributes={java_CompilationUnit_originalFilePath}

# NamespaceAccess class attributes and methods

# java_Type class attributes and methods

# java_PrimitiveTypeFloat class attributes and methods

# java_PrimitiveType class attributes and methods

# java_ArrayLengthAccess class attributes and methods

# java_SingleVariableAccess class attributes and methods

# java_VariableDeclaration class attributes and methods

# java_Annotation class attributes and methods

# java_MemberRef class attributes and methods

# java_SwitchStatement class attributes and methods

# java_ArrayCreation class attributes and methods

# java_UnresolvedItem class attributes and methods

# java_ParenthesizedExpression class attributes and methods

# java_PrimitiveTypeShort class attributes and methods

# java_MethodDeclaration class attributes and methods

# AbstractMethodDeclaration class attributes and methods

# java_UnresolvedItemAccess class attributes and methods

# java_IfStatement class attributes and methods

# java_InfixExpression class attributes and methods
java_InfixExpression_operator: Property = Property(name="operator", type=StringType)
java_InfixExpression.attributes={java_InfixExpression_operator}

# java_Archive class attributes and methods
java_Archive_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java_Archive.attributes={java_Archive_originalFilePath}

# java_BooleanLiteral class attributes and methods
java_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
java_BooleanLiteral.attributes={java_BooleanLiteral_value}

# java_ParameterizedType class attributes and methods

# java_SuperFieldAccess class attributes and methods

# java_TryStatement class attributes and methods

# java_CatchClause class attributes and methods

# java_ExpressionStatement class attributes and methods

# java_Package class attributes and methods

# java_BreakStatement class attributes and methods

# java_LabeledStatement class attributes and methods

# java_TagElement class attributes and methods

# java_ArrayType class attributes and methods
java_ArrayType_dimensions: Property = Property(name="dimensions", type=IntegerType)
java_ArrayType.attributes={java_ArrayType_dimensions}

# java_PrefixExpression class attributes and methods
java_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
java_PrefixExpression.attributes={java_PrefixExpression_operator}

# java_AnonymousClassDeclaration class attributes and methods

# java_SuperMethodInvocation class attributes and methods

# java_ConstructorDeclaration class attributes and methods

# java_PrimitiveTypeInt class attributes and methods

# java_SwitchCase class attributes and methods

# java_NullLiteral class attributes and methods

# java_ForStatement class attributes and methods

# java_ConditionalExpression class attributes and methods

# java_ArrayAccess class attributes and methods

# java_VariableDeclarationExpression class attributes and methods

# java_PrimitiveTypeChar class attributes and methods

# java_Initializer class attributes and methods

# java_DoStatement class attributes and methods

# java_ContinueStatement class attributes and methods

# java_InstanceofExpression class attributes and methods

# java_AssertStatement class attributes and methods

# java_TypeDeclarationStatement class attributes and methods

# java_ClassDeclaration class attributes and methods

# java_MethodInvocation class attributes and methods

# java_FieldAccess class attributes and methods

# java_CastExpression class attributes and methods

# java_ThrowStatement class attributes and methods

# java_ConstructorInvocation class attributes and methods

# java_NumberLiteral class attributes and methods
java_NumberLiteral_tokenValue: Property = Property(name="tokenValue", type=StringType)
java_NumberLiteral.attributes={java_NumberLiteral_tokenValue}

# java_ClassInstanceCreation class attributes and methods

# java_VariableDeclarationStatement class attributes and methods

# java_Model class attributes and methods
java_Model_name: Property = Property(name="name", type=StringType)
java_Model.attributes={java_Model_name}

# java_NamespaceAccess class attributes and methods

# Relationships
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="java_Expression2", type=java_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WhileStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body3: BinaryAssociation = BinaryAssociation(
    name="body3",
    ends={
        Property(name="java_Statement", type=java_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WhileStatement4", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression0: BinaryAssociation = BinaryAssociation(
    name="expression0",
    ends={
        Property(name="java_Expression", type=java_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SuperConstructorInvocation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thrownExceptions19: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions19",
    ends={
        Property(name="java_TypeAccess21", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration20", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters22: BinaryAssociation = BinaryAssociation(
    name="typeParameters22",
    ends={
        Property(name="java_TypeParameter", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration23", type=java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body5: BinaryAssociation = BinaryAssociation(
    name="body5",
    ends={
        Property(name="java_Block", type=java_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SynchronizedStatement", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression6: BinaryAssociation = BinaryAssociation(
    name="expression6",
    ends={
        Property(name="java_Expression8", type=java_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SynchronizedStatement7", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variablesContainer9: BinaryAssociation = BinaryAssociation(
    name="variablesContainer9",
    ends={
        Property(name="10", type=java_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(0, 1))
    }
)
bound11: BinaryAssociation = BinaryAssociation(
    name="bound11",
    ends={
        Property(name="java_TypeAccess", type=java_WildCardType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WildCardType", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="java_TypeAccess13", type=java_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeLiteral", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body14: BinaryAssociation = BinaryAssociation(
    name="body14",
    ends={
        Property(name="java_Block15", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration", type=java_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters16: BinaryAssociation = BinaryAssociation(
    name="parameters16",
    ends={
        Property(name="18", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsAfterBody33: BinaryAssociation = BinaryAssociation(
    name="commentsAfterBody33",
    ends={
        Property(name="java_Comment", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsBeforeBody34: BinaryAssociation = BinaryAssociation(
    name="commentsBeforeBody34",
    ends={
        Property(name="java_Comment36", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration35", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaces37: BinaryAssociation = BinaryAssociation(
    name="superInterfaces37",
    ends={
        Property(name="java_TypeAccess39", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration38", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters24: BinaryAssociation = BinaryAssociation(
    name="typeParameters24",
    ends={
        Property(name="java_TypeParameter25", type=java_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeDeclaration", type=java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier26: BinaryAssociation = BinaryAssociation(
    name="modifier26",
    ends={
        Property(name="java_Modifier", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableDeclaration", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="java_TypeAccess29", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableDeclaration28", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodDeclaration30: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration30",
    ends={
        Property(name="32", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="31", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
operand55: BinaryAssociation = BinaryAssociation(
    name="operand55",
    ends={
        Property(name="java_Expression56", type=java_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PostfixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyDeclarations40: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations40",
    ends={
        Property(name="42", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="41", type=java_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments43: BinaryAssociation = BinaryAssociation(
    name="arguments43",
    ends={
        Property(name="java_Expression44", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodInvocation", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method45: BinaryAssociation = BinaryAssociation(
    name="method45",
    ends={
        Property(name="java_AbstractMethodDeclaration47", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodInvocation46", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
qualifier48: BinaryAssociation = BinaryAssociation(
    name="qualifier48",
    ends={
        Property(name="java_TypeAccess49", type=java_AbstractTypeQualifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeQualifiedExpression", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftHandSide50: BinaryAssociation = BinaryAssociation(
    name="leftHandSide50",
    ends={
        Property(name="java_Expression51", type=java_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Assignment", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide52: BinaryAssociation = BinaryAssociation(
    name="rightHandSide52",
    ends={
        Property(name="java_Expression54", type=java_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Assignment53", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body65: BinaryAssociation = BinaryAssociation(
    name="body65",
    ends={
        Property(name="java_EnhancedForStatement", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="java_Statement66", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1))
    }
)
parameter67: BinaryAssociation = BinaryAssociation(
    name="parameter67",
    ends={
        Property(name="java_SingleVariableDeclaration69", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnhancedForStatement68", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression70: BinaryAssociation = BinaryAssociation(
    name="expression70",
    ends={
        Property(name="java_Expression72", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnhancedForStatement71", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions57: BinaryAssociation = BinaryAssociation(
    name="expressions57",
    ends={
        Property(name="java_Expression58", type=java_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayInitializer", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value59: BinaryAssociation = BinaryAssociation(
    name="value59",
    ends={
        Property(name="java_Expression60", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationMemberValuePair", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member61: BinaryAssociation = BinaryAssociation(
    name="member61",
    ends={
        Property(name="java_AnnotationTypeMemberDeclaration", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationMemberValuePair62", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
enumConstants63: BinaryAssociation = BinaryAssociation(
    name="enumConstants63",
    ends={
        Property(name="java_EnumConstantDeclaration", type=java_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnumDeclaration", type=java_EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement64: BinaryAssociation = BinaryAssociation(
    name="importedElement64",
    ends={
        Property(name="java_NamedElement", type=java_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ImportDeclaration", type=java_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
array84: BinaryAssociation = BinaryAssociation(
    name="array84",
    ends={
        Property(name="java_Expression85", type=java_ArrayLengthAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayLengthAccess", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression86: BinaryAssociation = BinaryAssociation(
    name="expression86",
    ends={
        Property(name="java_Expression87", type=java_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ReturnStatement", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comments73: BinaryAssociation = BinaryAssociation(
    name="comments73",
    ends={
        Property(name="java_Comment74", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalClassFile75: BinaryAssociation = BinaryAssociation(
    name="originalClassFile75",
    ends={
        Property(name="java_ClassFile", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode76", type=java_ClassFile, multiplicity=Multiplicity(0, 1))
    }
)
originalCompilationUnit77: BinaryAssociation = BinaryAssociation(
    name="originalCompilationUnit77",
    ends={
        Property(name="java_CompilationUnit", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode78", type=java_CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
statements79: BinaryAssociation = BinaryAssociation(
    name="statements79",
    ends={
        Property(name="java_Statement81", type=java_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Block80", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type82: BinaryAssociation = BinaryAssociation(
    name="type82",
    ends={
        Property(name="java_Type", type=java_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeAccess83", type=java_Type, multiplicity=Multiplicity(1, 1))
    }
)
variable101: BinaryAssociation = BinaryAssociation(
    name="variable101",
    ends={
        Property(name="java_VariableDeclaration", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableAccess", type=java_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
type102: BinaryAssociation = BinaryAssociation(
    name="type102",
    ends={
        Property(name="java_TypeAccess103", type=java_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Annotation", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression88: BinaryAssociation = BinaryAssociation(
    name="expression88",
    ends={
        Property(name="java_Expression89", type=java_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements90: BinaryAssociation = BinaryAssociation(
    name="statements90",
    ends={
        Property(name="java_Statement92", type=java_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchStatement91", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type93: BinaryAssociation = BinaryAssociation(
    name="type93",
    ends={
        Property(name="java_TypeAccess94", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions95: BinaryAssociation = BinaryAssociation(
    name="dimensions95",
    ends={
        Property(name="java_Expression97", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation96", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer98: BinaryAssociation = BinaryAssociation(
    name="initializer98",
    ends={
        Property(name="java_ArrayInitializer100", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation99", type=java_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression110: BinaryAssociation = BinaryAssociation(
    name="expression110",
    ends={
        Property(name="java_Expression111", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement112: BinaryAssociation = BinaryAssociation(
    name="elseStatement112",
    ends={
        Property(name="java_Statement114", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement113", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenStatement115: BinaryAssociation = BinaryAssociation(
    name="thenStatement115",
    ends={
        Property(name="java_Statement117", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement116", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values104: BinaryAssociation = BinaryAssociation(
    name="values104",
    ends={
        Property(name="java_AnnotationMemberValuePair106", type=java_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Annotation105", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression107: BinaryAssociation = BinaryAssociation(
    name="expression107",
    ends={
        Property(name="java_Expression108", type=java_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParenthesizedExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element109: BinaryAssociation = BinaryAssociation(
    name="element109",
    ends={
        Property(name="java_UnresolvedItem", type=java_UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_UnresolvedItemAccess", type=java_UnresolvedItem, multiplicity=Multiplicity(0, 1))
    }
)
type126: BinaryAssociation = BinaryAssociation(
    name="type126",
    ends={
        Property(name="java_TypeAccess128", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationTypeMemberDeclaration127", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand118: BinaryAssociation = BinaryAssociation(
    name="rightOperand118",
    ends={
        Property(name="java_Expression119", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand120: BinaryAssociation = BinaryAssociation(
    name="leftOperand120",
    ends={
        Property(name="java_Expression122", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression121", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands123: BinaryAssociation = BinaryAssociation(
    name="extendedOperands123",
    ends={
        Property(name="java_Expression125", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression124", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finally144: BinaryAssociation = BinaryAssociation(
    name="finally144",
    ends={
        Property(name="java_Block146", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement145", type=java_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type147: BinaryAssociation = BinaryAssociation(
    name="type147",
    ends={
        Property(name="java_TypeAccess148", type=java_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParameterizedType", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imports129: BinaryAssociation = BinaryAssociation(
    name="imports129",
    ends={
        Property(name="java_ImportDeclaration131", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit130", type=java_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types132: BinaryAssociation = BinaryAssociation(
    name="types132",
    ends={
        Property(name="java_AbstractTypeDeclaration134", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit133", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
field135: BinaryAssociation = BinaryAssociation(
    name="field135",
    ends={
        Property(name="java_SingleVariableAccess136", type=java_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SuperFieldAccess", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer137: BinaryAssociation = BinaryAssociation(
    name="initializer137",
    ends={
        Property(name="java_Expression139", type=java_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_VariableDeclaration138", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses140: BinaryAssociation = BinaryAssociation(
    name="catchClauses140",
    ends={
        Property(name="java_CatchClause", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement", type=java_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body141: BinaryAssociation = BinaryAssociation(
    name="body141",
    ends={
        Property(name="java_Block143", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement142", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression160: BinaryAssociation = BinaryAssociation(
    name="expression160",
    ends={
        Property(name="java_Expression161", type=java_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ExpressionStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifier162: BinaryAssociation = BinaryAssociation(
    name="modifier162",
    ends={
        Property(name="java_Modifier163", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_BodyDeclaration", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments149: BinaryAssociation = BinaryAssociation(
    name="typeArguments149",
    ends={
        Property(name="java_TypeAccess151", type=java_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParameterizedType150", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElements152: BinaryAssociation = BinaryAssociation(
    name="ownedElements152",
    ends={
        Property(name="java_AbstractTypeDeclaration153", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Package", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPackages155: BinaryAssociation = BinaryAssociation(
    name="ownedPackages155",
    ends={
        Property(name="java_Package156", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Package154", type=java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label157: BinaryAssociation = BinaryAssociation(
    name="label157",
    ends={
        Property(name="java_LabeledStatement", type=java_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_BreakStatement", type=java_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
elementType158: BinaryAssociation = BinaryAssociation(
    name="elementType158",
    ends={
        Property(name="java_TypeAccess159", type=java_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayType", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression179: BinaryAssociation = BinaryAssociation(
    name="expression179",
    ends={
        Property(name="java_Expression180", type=java_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchCase", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstractTypeDeclaration164: BinaryAssociation = BinaryAssociation(
    name="abstractTypeDeclaration164",
    ends={
        Property(name="166", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="165", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
anonymousClassDeclarationOwner167: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclarationOwner167",
    ends={
        Property(name="169", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="168", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
annotations170: BinaryAssociation = BinaryAssociation(
    name="annotations170",
    ends={
        Property(name="java_Annotation172", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_BodyDeclaration171", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body173: BinaryAssociation = BinaryAssociation(
    name="body173",
    ends={
        Property(name="java_Block175", type=java_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CatchClause174", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception176: BinaryAssociation = BinaryAssociation(
    name="exception176",
    ends={
        Property(name="java_SingleVariableDeclaration178", type=java_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CatchClause177", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression188: BinaryAssociation = BinaryAssociation(
    name="elseExpression188",
    ends={
        Property(name="java_Expression190", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression189", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand181: BinaryAssociation = BinaryAssociation(
    name="operand181",
    ends={
        Property(name="java_Expression182", type=java_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PrefixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression183: BinaryAssociation = BinaryAssociation(
    name="expression183",
    ends={
        Property(name="java_Expression184", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression191: BinaryAssociation = BinaryAssociation(
    name="expression191",
    ends={
        Property(name="java_Expression192", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression185: BinaryAssociation = BinaryAssociation(
    name="thenExpression185",
    ends={
        Property(name="java_Expression187", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression186", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updaters199: BinaryAssociation = BinaryAssociation(
    name="updaters199",
    ends={
        Property(name="java_Expression201", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement200", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
array202: BinaryAssociation = BinaryAssociation(
    name="array202",
    ends={
        Property(name="java_Expression203", type=java_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayAccess", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializers193: BinaryAssociation = BinaryAssociation(
    name="initializers193",
    ends={
        Property(name="java_Expression195", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement194", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body196: BinaryAssociation = BinaryAssociation(
    name="body196",
    ends={
        Property(name="java_Statement198", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement197", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type207: BinaryAssociation = BinaryAssociation(
    name="type207",
    ends={
        Property(name="java_TypeAccess208", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractVariablesContainer", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments209: BinaryAssociation = BinaryAssociation(
    name="fragments209",
    ends={
        Property(name="211", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="210", type=java_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
index204: BinaryAssociation = BinaryAssociation(
    name="index204",
    ends={
        Property(name="java_Expression206", type=java_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayAccess205", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label214: BinaryAssociation = BinaryAssociation(
    name="label214",
    ends={
        Property(name="java_LabeledStatement215", type=java_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ContinueStatement", type=java_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
expression216: BinaryAssociation = BinaryAssociation(
    name="expression216",
    ends={
        Property(name="java_Expression217", type=java_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_DoStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body218: BinaryAssociation = BinaryAssociation(
    name="body218",
    ends={
        Property(name="java_Statement220", type=java_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_DoStatement219", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body212: BinaryAssociation = BinaryAssociation(
    name="body212",
    ends={
        Property(name="java_Block213", type=java_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Initializer", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression221: BinaryAssociation = BinaryAssociation(
    name="expression221",
    ends={
        Property(name="java_AssertStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="java_Expression222", type=java_AssertStatement, multiplicity=Multiplicity(1, 1))
    }
)
message223: BinaryAssociation = BinaryAssociation(
    name="message223",
    ends={
        Property(name="java_Expression225", type=java_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AssertStatement224", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand226: BinaryAssociation = BinaryAssociation(
    name="rightOperand226",
    ends={
        Property(name="java_TypeAccess227", type=java_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InstanceofExpression", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration231: BinaryAssociation = BinaryAssociation(
    name="declaration231",
    ends={
        Property(name="java_AbstractTypeDeclaration232", type=java_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeDeclarationStatement", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superClass233: BinaryAssociation = BinaryAssociation(
    name="superClass233",
    ends={
        Property(name="java_TypeAccess234", type=java_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassDeclaration", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand228: BinaryAssociation = BinaryAssociation(
    name="leftOperand228",
    ends={
        Property(name="java_Expression230", type=java_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InstanceofExpression229", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
field237: BinaryAssociation = BinaryAssociation(
    name="field237",
    ends={
        Property(name="java_SingleVariableAccess239", type=java_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_FieldAccess238", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression240: BinaryAssociation = BinaryAssociation(
    name="expression240",
    ends={
        Property(name="java_Expression241", type=java_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodInvocation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression235: BinaryAssociation = BinaryAssociation(
    name="expression235",
    ends={
        Property(name="java_Expression236", type=java_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_FieldAccess", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression245: BinaryAssociation = BinaryAssociation(
    name="expression245",
    ends={
        Property(name="java_Expression246", type=java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CastExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type247: BinaryAssociation = BinaryAssociation(
    name="type247",
    ends={
        Property(name="java_TypeAccess249", type=java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CastExpression248", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyDeclarations242: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations242",
    ends={
        Property(name="244", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="243", type=java_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body252: BinaryAssociation = BinaryAssociation(
    name="body252",
    ends={
        Property(name="java_Statement254", type=java_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_LabeledStatement253", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression250: BinaryAssociation = BinaryAssociation(
    name="expression250",
    ends={
        Property(name="java_Expression251", type=java_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ThrowStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression257: BinaryAssociation = BinaryAssociation(
    name="expression257",
    ends={
        Property(name="java_Expression258", type=java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassInstanceCreation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations255: BinaryAssociation = BinaryAssociation(
    name="annotations255",
    ends={
        Property(name="java_Annotation256", type=java_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_VariableDeclarationStatement", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits264: BinaryAssociation = BinaryAssociation(
    name="compilationUnits264",
    ends={
        Property(name="java_CompilationUnit265", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model", type=java_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orphanTypes266: BinaryAssociation = BinaryAssociation(
    name="orphanTypes266",
    ends={
        Property(name="java_Type268", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model267", type=java_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archives269: BinaryAssociation = BinaryAssociation(
    name="archives269",
    ends={
        Property(name="java_Archive", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model270", type=java_Archive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type259: BinaryAssociation = BinaryAssociation(
    name="type259",
    ends={
        Property(name="java_TypeAccess261", type=java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassInstanceCreation260", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anonymousClassDeclaration262: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration262",
    ends={
        Property(name="java_AnonymousClassDeclaration", type=java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassInstanceCreation263", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedElements271: BinaryAssociation = BinaryAssociation(
    name="ownedElements271",
    ends={
        Property(name="java_Package273", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model272", type=java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_java_MethodRef_ASTNode = Generalization(general=ASTNode, specific=java_MethodRef)
gen_java_PrimitiveTypeDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeDouble)
gen_java_WhileStatement_Statement = Generalization(general=Statement, specific=java_WhileStatement)
gen_java_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=java_MethodRefParameter)
gen_java_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=java_SuperConstructorInvocation)
gen_java_SuperConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_SuperConstructorInvocation)
gen_java_PrimitiveTypeVoid_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeVoid)
gen_java_InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=java_InterfaceDeclaration)
gen_java_UnresolvedTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_UnresolvedTypeDeclaration)
gen_java_UnresolvedTypeDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedTypeDeclaration)
gen_java_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_TypeDeclaration)
gen_java_StringLiteral_Expression = Generalization(general=Expression, specific=java_StringLiteral)
gen_java_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_AnnotationTypeDeclaration)
gen_java_SynchronizedStatement_Statement = Generalization(general=Statement, specific=java_SynchronizedStatement)
gen_java_ThisExpression_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_ThisExpression)
gen_java_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_VariableDeclarationFragment)
gen_java_WildCardType_Type = Generalization(general=Type, specific=java_WildCardType)
gen_java_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_EnumConstantDeclaration)
gen_java_EnumConstantDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_EnumConstantDeclaration)
gen_java_TypeLiteral_Expression = Generalization(general=Expression, specific=java_TypeLiteral)
gen_java_AbstractMethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AbstractMethodDeclaration)
gen_java_PrimitiveTypeLong_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeLong)
gen_java_PrimitiveTypeBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeBoolean)
gen_java_CharacterLiteral_Expression = Generalization(general=Expression, specific=java_CharacterLiteral)
gen_java_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_FieldDeclaration)
gen_java_FieldDeclaration_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_FieldDeclaration)
gen_java_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_SingleVariableDeclaration)
gen_java_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AbstractTypeDeclaration)
gen_java_AbstractTypeDeclaration_Type = Generalization(general=Type, specific=java_AbstractTypeDeclaration)
gen_java_PrimitiveTypeByte_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeByte)
gen_java_ArrayInitializer_Expression = Generalization(general=Expression, specific=java_ArrayInitializer)
gen_java_AbstractMethodInvocation_ASTNode = Generalization(general=ASTNode, specific=java_AbstractMethodInvocation)
gen_java_AbstractTypeQualifiedExpression_Expression = Generalization(general=Expression, specific=java_AbstractTypeQualifiedExpression)
gen_java_Assignment_Expression = Generalization(general=Expression, specific=java_Assignment)
gen_java_PostfixExpression_Expression = Generalization(general=Expression, specific=java_PostfixExpression)
gen_java_AnnotationMemberValuePair_NamedElement = Generalization(general=NamedElement, specific=java_AnnotationMemberValuePair)
gen_java_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_EnumDeclaration)
gen_java_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=java_ImportDeclaration)
gen_java_EnhancedForStatement_Statement = Generalization(general=Statement, specific=java_EnhancedForStatement)
gen_java_EmptyStatement_Statement = Generalization(general=Statement, specific=java_EmptyStatement)
gen_java_ReturnStatement_Statement = Generalization(general=Statement, specific=java_ReturnStatement)
gen_java_Block_Statement = Generalization(general=Statement, specific=java_Block)
gen_java_TypeAccess_Expression = Generalization(general=Expression, specific=java_TypeAccess)
gen_java_TypeAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java_TypeAccess)
gen_java_TypeParameter_Type = Generalization(general=Type, specific=java_TypeParameter)
gen_java_PrimitiveTypeFloat_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeFloat)
gen_java_PrimitiveType_Type = Generalization(general=Type, specific=java_PrimitiveType)
gen_java_ArrayLengthAccess_Expression = Generalization(general=Expression, specific=java_ArrayLengthAccess)
gen_java_SingleVariableAccess_Expression = Generalization(general=Expression, specific=java_SingleVariableAccess)
gen_java_Annotation_Expression = Generalization(general=Expression, specific=java_Annotation)
gen_java_MemberRef_ASTNode = Generalization(general=ASTNode, specific=java_MemberRef)
gen_java_Statement_ASTNode = Generalization(general=ASTNode, specific=java_Statement)
gen_java_SwitchStatement_Statement = Generalization(general=Statement, specific=java_SwitchStatement)
gen_java_ArrayCreation_Expression = Generalization(general=Expression, specific=java_ArrayCreation)
gen_java_UnresolvedItem_NamedElement = Generalization(general=NamedElement, specific=java_UnresolvedItem)
gen_java_Modifier_ASTNode = Generalization(general=ASTNode, specific=java_Modifier)
gen_java_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=java_ParenthesizedExpression)
gen_java_PrimitiveTypeShort_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeShort)
gen_java_MethodDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=java_MethodDeclaration)
gen_java_UnresolvedItemAccess_Expression = Generalization(general=Expression, specific=java_UnresolvedItemAccess)
gen_java_UnresolvedItemAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java_UnresolvedItemAccess)
gen_java_IfStatement_Statement = Generalization(general=Statement, specific=java_IfStatement)
gen_java_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AnnotationTypeMemberDeclaration)
gen_java_CompilationUnit_NamedElement = Generalization(general=NamedElement, specific=java_CompilationUnit)
gen_java_InfixExpression_Expression = Generalization(general=Expression, specific=java_InfixExpression)
gen_java_Archive_NamedElement = Generalization(general=NamedElement, specific=java_Archive)
gen_java_BooleanLiteral_Expression = Generalization(general=Expression, specific=java_BooleanLiteral)
gen_java_ParameterizedType_Type = Generalization(general=Type, specific=java_ParameterizedType)
gen_java_SuperFieldAccess_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_SuperFieldAccess)
gen_java_VariableDeclaration_NamedElement = Generalization(general=NamedElement, specific=java_VariableDeclaration)
gen_java_TryStatement_Statement = Generalization(general=Statement, specific=java_TryStatement)
gen_java_ExpressionStatement_Statement = Generalization(general=Statement, specific=java_ExpressionStatement)
gen_java_BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=java_BodyDeclaration)
gen_java_Package_NamedElement = Generalization(general=NamedElement, specific=java_Package)
gen_java_BreakStatement_Statement = Generalization(general=Statement, specific=java_BreakStatement)
gen_java_TagElement_ASTNode = Generalization(general=ASTNode, specific=java_TagElement)
gen_java_ArrayType_Type = Generalization(general=Type, specific=java_ArrayType)
gen_java_Type_NamedElement = Generalization(general=NamedElement, specific=java_Type)
gen_java_PrefixExpression_Expression = Generalization(general=Expression, specific=java_PrefixExpression)
gen_java_SuperMethodInvocation_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_SuperMethodInvocation)
gen_java_SuperMethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_SuperMethodInvocation)
gen_java_ConstructorDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=java_ConstructorDeclaration)
gen_java_PrimitiveTypeInt_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeInt)
gen_java_CatchClause_Statement = Generalization(general=Statement, specific=java_CatchClause)
gen_java_SwitchCase_Statement = Generalization(general=Statement, specific=java_SwitchCase)
gen_java_NullLiteral_Expression = Generalization(general=Expression, specific=java_NullLiteral)
gen_java_ForStatement_Statement = Generalization(general=Statement, specific=java_ForStatement)
gen_java_ConditionalExpression_Expression = Generalization(general=Expression, specific=java_ConditionalExpression)
gen_java_ArrayAccess_Expression = Generalization(general=Expression, specific=java_ArrayAccess)
gen_java_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=java_VariableDeclarationExpression)
gen_java_VariableDeclarationExpression_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_VariableDeclarationExpression)
gen_java_PrimitiveTypeChar_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeChar)
gen_java_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_Initializer)
gen_java_AbstractVariablesContainer_ASTNode = Generalization(general=ASTNode, specific=java_AbstractVariablesContainer)
gen_java_ClassFile_NamedElement = Generalization(general=NamedElement, specific=java_ClassFile)
gen_java_DoStatement_Statement = Generalization(general=Statement, specific=java_DoStatement)
gen_java_ContinueStatement_Statement = Generalization(general=Statement, specific=java_ContinueStatement)
gen_java_InstanceofExpression_Expression = Generalization(general=Expression, specific=java_InstanceofExpression)
gen_java_AssertStatement_Statement = Generalization(general=Statement, specific=java_AssertStatement)
gen_java_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=java_TypeDeclarationStatement)
gen_java_ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=java_ClassDeclaration)
gen_java_Comment_ASTNode = Generalization(general=ASTNode, specific=java_Comment)
gen_java_MethodInvocation_Expression = Generalization(general=Expression, specific=java_MethodInvocation)
gen_java_MethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_MethodInvocation)
gen_java_FieldAccess_Expression = Generalization(general=Expression, specific=java_FieldAccess)
gen_java_ConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_ConstructorInvocation)
gen_java_CastExpression_Expression = Generalization(general=Expression, specific=java_CastExpression)
gen_java_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=java_AnonymousClassDeclaration)
gen_java_ConstructorInvocation_Statement = Generalization(general=Statement, specific=java_ConstructorInvocation)
gen_java_NamedElement_ASTNode = Generalization(general=ASTNode, specific=java_NamedElement)
gen_java_LabeledStatement_NamedElement = Generalization(general=NamedElement, specific=java_LabeledStatement)
gen_java_LabeledStatement_Statement = Generalization(general=Statement, specific=java_LabeledStatement)
gen_java_ThrowStatement_Statement = Generalization(general=Statement, specific=java_ThrowStatement)
gen_java_NumberLiteral_Expression = Generalization(general=Expression, specific=java_NumberLiteral)
gen_java_Expression_ASTNode = Generalization(general=ASTNode, specific=java_Expression)
gen_java_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=java_ClassInstanceCreation)
gen_java_ClassInstanceCreation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_ClassInstanceCreation)
gen_java_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=java_VariableDeclarationStatement)
gen_java_VariableDeclarationStatement_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_VariableDeclarationStatement)
gen_java_NamespaceAccess_ASTNode = Generalization(general=ASTNode, specific=java_NamespaceAccess)

# Domain Model
domain_model = DomainModel(
    name="java",
    types={java_MethodRef, java_PrimitiveTypeDouble, PrimitiveType, java_WhileStatement, java_Statement, java_MethodRefParameter, ASTNode, java_SuperConstructorInvocation, Statement, AbstractMethodInvocation, java_Expression, java_TypeParameter, java_PrimitiveTypeVoid, java_InterfaceDeclaration, TypeDeclaration, java_UnresolvedTypeDeclaration, UnresolvedItem, java_TypeDeclaration, java_StringLiteral, Expression, java_AnnotationTypeDeclaration, AbstractTypeDeclaration, java_SynchronizedStatement, java_Block, java_ThisExpression, AbstractTypeQualifiedExpression, java_VariableDeclarationFragment, VariableDeclaration, java_AbstractVariablesContainer, java_WildCardType, Type, java_TypeAccess, java_EnumConstantDeclaration, BodyDeclaration, java_TypeLiteral, java_AbstractMethodDeclaration, java_SingleVariableDeclaration, java_PrimitiveTypeLong, java_PrimitiveTypeBoolean, java_CharacterLiteral, java_FieldDeclaration, AbstractVariablesContainer, java_Modifier, java_AbstractTypeDeclaration, java_Comment, java_PrimitiveTypeByte, java_ArrayInitializer, java_BodyDeclaration, java_AbstractMethodInvocation, java_AbstractTypeQualifiedExpression, java_Assignment, java_PostfixExpression, java_ASTNode, java_AnnotationMemberValuePair, NamedElement, java_AnnotationTypeMemberDeclaration, java_EnumDeclaration, java_ImportDeclaration, java_NamedElement, java_EnhancedForStatement, java_EmptyStatement, java_ReturnStatement, java_ClassFile, java_CompilationUnit, NamespaceAccess, java_Type, java_PrimitiveTypeFloat, java_PrimitiveType, java_ArrayLengthAccess, java_SingleVariableAccess, java_VariableDeclaration, java_Annotation, java_MemberRef, java_SwitchStatement, java_ArrayCreation, java_UnresolvedItem, java_ParenthesizedExpression, java_PrimitiveTypeShort, java_MethodDeclaration, AbstractMethodDeclaration, java_UnresolvedItemAccess, java_IfStatement, java_InfixExpression, java_Archive, java_BooleanLiteral, java_ParameterizedType, java_SuperFieldAccess, java_TryStatement, java_CatchClause, java_ExpressionStatement, java_Package, java_BreakStatement, java_LabeledStatement, java_TagElement, java_ArrayType, java_PrefixExpression, java_AnonymousClassDeclaration, java_SuperMethodInvocation, java_ConstructorDeclaration, java_PrimitiveTypeInt, java_SwitchCase, java_NullLiteral, java_ForStatement, java_ConditionalExpression, java_ArrayAccess, java_VariableDeclarationExpression, java_PrimitiveTypeChar, java_Initializer, java_DoStatement, java_ContinueStatement, java_InstanceofExpression, java_AssertStatement, java_TypeDeclarationStatement, java_ClassDeclaration, java_MethodInvocation, java_FieldAccess, java_CastExpression, java_ThrowStatement, java_ConstructorInvocation, java_NumberLiteral, java_ClassInstanceCreation, java_VariableDeclarationStatement, java_Model, java_NamespaceAccess, InfixExpressionKind, PrefixExpressionKind, PostfixExpressionKind, VisibilityKind, InheritanceKind, AssignmentKind},
    associations={expression1, body3, expression0, thrownExceptions19, typeParameters22, body5, expression6, variablesContainer9, bound11, type12, body14, parameters16, commentsAfterBody33, commentsBeforeBody34, superInterfaces37, typeParameters24, modifier26, type27, methodDeclaration30, operand55, bodyDeclarations40, arguments43, method45, qualifier48, leftHandSide50, rightHandSide52, body65, parameter67, expression70, expressions57, value59, member61, enumConstants63, importedElement64, array84, expression86, comments73, originalClassFile75, originalCompilationUnit77, statements79, type82, variable101, type102, expression88, statements90, type93, dimensions95, initializer98, expression110, elseStatement112, thenStatement115, values104, expression107, element109, type126, rightOperand118, leftOperand120, extendedOperands123, finally144, type147, imports129, types132, field135, initializer137, catchClauses140, body141, expression160, modifier162, typeArguments149, ownedElements152, ownedPackages155, label157, elementType158, expression179, abstractTypeDeclaration164, anonymousClassDeclarationOwner167, annotations170, body173, exception176, elseExpression188, operand181, expression183, expression191, thenExpression185, updaters199, array202, initializers193, body196, type207, fragments209, index204, label214, expression216, body218, body212, expression221, message223, rightOperand226, declaration231, superClass233, leftOperand228, field237, expression240, expression235, expression245, type247, bodyDeclarations242, body252, expression250, expression257, annotations255, compilationUnits264, orphanTypes266, archives269, type259, anonymousClassDeclaration262, ownedElements271},
    generalizations={gen_java_MethodRef_ASTNode, gen_java_PrimitiveTypeDouble_PrimitiveType, gen_java_WhileStatement_Statement, gen_java_MethodRefParameter_ASTNode, gen_java_SuperConstructorInvocation_Statement, gen_java_SuperConstructorInvocation_AbstractMethodInvocation, gen_java_PrimitiveTypeVoid_PrimitiveType, gen_java_InterfaceDeclaration_TypeDeclaration, gen_java_UnresolvedTypeDeclaration_AbstractTypeDeclaration, gen_java_UnresolvedTypeDeclaration_UnresolvedItem, gen_java_TypeDeclaration_AbstractTypeDeclaration, gen_java_StringLiteral_Expression, gen_java_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_java_SynchronizedStatement_Statement, gen_java_ThisExpression_AbstractTypeQualifiedExpression, gen_java_VariableDeclarationFragment_VariableDeclaration, gen_java_WildCardType_Type, gen_java_EnumConstantDeclaration_BodyDeclaration, gen_java_EnumConstantDeclaration_VariableDeclaration, gen_java_TypeLiteral_Expression, gen_java_AbstractMethodDeclaration_BodyDeclaration, gen_java_PrimitiveTypeLong_PrimitiveType, gen_java_PrimitiveTypeBoolean_PrimitiveType, gen_java_CharacterLiteral_Expression, gen_java_FieldDeclaration_BodyDeclaration, gen_java_FieldDeclaration_AbstractVariablesContainer, gen_java_SingleVariableDeclaration_VariableDeclaration, gen_java_AbstractTypeDeclaration_BodyDeclaration, gen_java_AbstractTypeDeclaration_Type, gen_java_PrimitiveTypeByte_PrimitiveType, gen_java_ArrayInitializer_Expression, gen_java_AbstractMethodInvocation_ASTNode, gen_java_AbstractTypeQualifiedExpression_Expression, gen_java_Assignment_Expression, gen_java_PostfixExpression_Expression, gen_java_AnnotationMemberValuePair_NamedElement, gen_java_EnumDeclaration_AbstractTypeDeclaration, gen_java_ImportDeclaration_ASTNode, gen_java_EnhancedForStatement_Statement, gen_java_EmptyStatement_Statement, gen_java_ReturnStatement_Statement, gen_java_Block_Statement, gen_java_TypeAccess_Expression, gen_java_TypeAccess_NamespaceAccess, gen_java_TypeParameter_Type, gen_java_PrimitiveTypeFloat_PrimitiveType, gen_java_PrimitiveType_Type, gen_java_ArrayLengthAccess_Expression, gen_java_SingleVariableAccess_Expression, gen_java_Annotation_Expression, gen_java_MemberRef_ASTNode, gen_java_Statement_ASTNode, gen_java_SwitchStatement_Statement, gen_java_ArrayCreation_Expression, gen_java_UnresolvedItem_NamedElement, gen_java_Modifier_ASTNode, gen_java_ParenthesizedExpression_Expression, gen_java_PrimitiveTypeShort_PrimitiveType, gen_java_MethodDeclaration_AbstractMethodDeclaration, gen_java_UnresolvedItemAccess_Expression, gen_java_UnresolvedItemAccess_NamespaceAccess, gen_java_IfStatement_Statement, gen_java_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_java_CompilationUnit_NamedElement, gen_java_InfixExpression_Expression, gen_java_Archive_NamedElement, gen_java_BooleanLiteral_Expression, gen_java_ParameterizedType_Type, gen_java_SuperFieldAccess_AbstractTypeQualifiedExpression, gen_java_VariableDeclaration_NamedElement, gen_java_TryStatement_Statement, gen_java_ExpressionStatement_Statement, gen_java_BodyDeclaration_NamedElement, gen_java_Package_NamedElement, gen_java_BreakStatement_Statement, gen_java_TagElement_ASTNode, gen_java_ArrayType_Type, gen_java_Type_NamedElement, gen_java_PrefixExpression_Expression, gen_java_SuperMethodInvocation_AbstractTypeQualifiedExpression, gen_java_SuperMethodInvocation_AbstractMethodInvocation, gen_java_ConstructorDeclaration_AbstractMethodDeclaration, gen_java_PrimitiveTypeInt_PrimitiveType, gen_java_CatchClause_Statement, gen_java_SwitchCase_Statement, gen_java_NullLiteral_Expression, gen_java_ForStatement_Statement, gen_java_ConditionalExpression_Expression, gen_java_ArrayAccess_Expression, gen_java_VariableDeclarationExpression_Expression, gen_java_VariableDeclarationExpression_AbstractVariablesContainer, gen_java_PrimitiveTypeChar_PrimitiveType, gen_java_Initializer_BodyDeclaration, gen_java_AbstractVariablesContainer_ASTNode, gen_java_ClassFile_NamedElement, gen_java_DoStatement_Statement, gen_java_ContinueStatement_Statement, gen_java_InstanceofExpression_Expression, gen_java_AssertStatement_Statement, gen_java_TypeDeclarationStatement_Statement, gen_java_ClassDeclaration_TypeDeclaration, gen_java_Comment_ASTNode, gen_java_MethodInvocation_Expression, gen_java_MethodInvocation_AbstractMethodInvocation, gen_java_FieldAccess_Expression, gen_java_ConstructorInvocation_AbstractMethodInvocation, gen_java_CastExpression_Expression, gen_java_AnonymousClassDeclaration_ASTNode, gen_java_ConstructorInvocation_Statement, gen_java_NamedElement_ASTNode, gen_java_LabeledStatement_NamedElement, gen_java_LabeledStatement_Statement, gen_java_ThrowStatement_Statement, gen_java_NumberLiteral_Expression, gen_java_Expression_ASTNode, gen_java_ClassInstanceCreation_Expression, gen_java_ClassInstanceCreation_AbstractMethodInvocation, gen_java_VariableDeclarationStatement_Statement, gen_java_VariableDeclarationStatement_AbstractVariablesContainer, gen_java_NamespaceAccess_ASTNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)