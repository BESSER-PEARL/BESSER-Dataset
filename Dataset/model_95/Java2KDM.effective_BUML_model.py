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
            EnumerationLiteral(name="ASSIGN"),
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
			EnumerationLiteral(name="RIGHT_SHIFT_UNSIGNED_ASSIGN")
    }
)

PrefixExpressionKind: Enumeration = Enumeration(
    name="PrefixExpressionKind",
    literals={
            EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="COMPLEMENT"),
			EnumerationLiteral(name="NOT")
    }
)

InfixExpressionKind: Enumeration = Enumeration(
    name="InfixExpressionKind",
    literals={
            EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="LESS_EQUALS"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="CONDITIONAL_AND"),
			EnumerationLiteral(name="CONDITIONAL_OR"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="DIVIDE"),
			EnumerationLiteral(name="REMAINDER"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="LEFT_SHIFT"),
			EnumerationLiteral(name="RIGHT_SHIFT_SIGNED"),
			EnumerationLiteral(name="RIGHT_SHIFT_UNSIGNED")
    }
)

# Classes
java_Expression = Class(name="java_Expression", is_abstract=True)
java_MethodRef = Class(name="java_MethodRef")
java_PrimitiveTypeDouble = Class(name="java_PrimitiveTypeDouble")
PrimitiveType = Class(name="PrimitiveType")
java_WhileStatement = Class(name="java_WhileStatement")
java_Statement = Class(name="java_Statement", is_abstract=True)
java_StringLiteral = Class(name="java_StringLiteral")
Expression = Class(name="Expression")
java_AnnotationTypeDeclaration = Class(name="java_AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
java_SynchronizedStatement = Class(name="java_SynchronizedStatement")
java_Block = Class(name="java_Block")
java_MethodRefParameter = Class(name="java_MethodRefParameter")
ASTNode = Class(name="ASTNode")
java_SuperConstructorInvocation = Class(name="java_SuperConstructorInvocation")
Statement = Class(name="Statement")
AbstractMethodInvocation = Class(name="AbstractMethodInvocation")
java_AbstractMethodDeclaration = Class(name="java_AbstractMethodDeclaration", is_abstract=True)
java_SingleVariableDeclaration = Class(name="java_SingleVariableDeclaration")
java_TypeParameter = Class(name="java_TypeParameter")
java_PrimitiveTypeVoid = Class(name="java_PrimitiveTypeVoid")
java_InterfaceDeclaration = Class(name="java_InterfaceDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
java_UnresolvedTypeDeclaration = Class(name="java_UnresolvedTypeDeclaration")
UnresolvedItem = Class(name="UnresolvedItem")
java_TypeDeclaration = Class(name="java_TypeDeclaration", is_abstract=True)
java_PrimitiveTypeLong = Class(name="java_PrimitiveTypeLong")
java_PrimitiveTypeBoolean = Class(name="java_PrimitiveTypeBoolean")
java_CharacterLiteral = Class(name="java_CharacterLiteral")
java_FieldDeclaration = Class(name="java_FieldDeclaration")
AbstractVariablesContainer = Class(name="AbstractVariablesContainer")
java_Modifier = Class(name="java_Modifier")
java_ThisExpression = Class(name="java_ThisExpression")
AbstractTypeQualifiedExpression = Class(name="AbstractTypeQualifiedExpression")
java_VariableDeclarationFragment = Class(name="java_VariableDeclarationFragment")
VariableDeclaration = Class(name="VariableDeclaration")
java_AbstractVariablesContainer = Class(name="java_AbstractVariablesContainer", is_abstract=True)
java_WildCardType = Class(name="java_WildCardType")
Type = Class(name="Type")
java_TypeAccess = Class(name="java_TypeAccess")
java_EnumConstantDeclaration = Class(name="java_EnumConstantDeclaration")
BodyDeclaration = Class(name="BodyDeclaration")
java_TypeLiteral = Class(name="java_TypeLiteral")
java_AbstractTypeQualifiedExpression = Class(name="java_AbstractTypeQualifiedExpression", is_abstract=True)
java_Assignment = Class(name="java_Assignment")
java_PostfixExpression = Class(name="java_PostfixExpression")
java_PrimitiveTypeByte = Class(name="java_PrimitiveTypeByte")
java_ArrayInitializer = Class(name="java_ArrayInitializer")
java_AnnotationMemberValuePair = Class(name="java_AnnotationMemberValuePair")
NamedElement = Class(name="NamedElement")
java_AbstractTypeDeclaration = Class(name="java_AbstractTypeDeclaration", is_abstract=True)
java_Comment = Class(name="java_Comment", is_abstract=True)
java_BodyDeclaration = Class(name="java_BodyDeclaration", is_abstract=True)
java_AbstractMethodInvocation = Class(name="java_AbstractMethodInvocation", is_abstract=True)
java_ClassFile = Class(name="java_ClassFile")
java_CompilationUnit = Class(name="java_CompilationUnit")
NamespaceAccess = Class(name="NamespaceAccess")
java_Type = Class(name="java_Type", is_abstract=True)
java_PrimitiveTypeFloat = Class(name="java_PrimitiveTypeFloat")
java_PrimitiveType = Class(name="java_PrimitiveType")
java_ArrayLengthAccess = Class(name="java_ArrayLengthAccess")
java_EmptyStatement = Class(name="java_EmptyStatement")
java_ReturnStatement = Class(name="java_ReturnStatement")
java_MemberRef = Class(name="java_MemberRef")
java_AnnotationTypeMemberDeclaration = Class(name="java_AnnotationTypeMemberDeclaration")
java_EnumDeclaration = Class(name="java_EnumDeclaration")
java_ImportDeclaration = Class(name="java_ImportDeclaration")
java_NamedElement = Class(name="java_NamedElement", is_abstract=True)
java_EnhancedForStatement = Class(name="java_EnhancedForStatement")
java_ASTNode = Class(name="java_ASTNode", is_abstract=True)
java_Annotation = Class(name="java_Annotation")
java_ParenthesizedExpression = Class(name="java_ParenthesizedExpression")
java_PrimitiveTypeShort = Class(name="java_PrimitiveTypeShort")
java_MethodDeclaration = Class(name="java_MethodDeclaration")
AbstractMethodDeclaration = Class(name="AbstractMethodDeclaration")
java_UnresolvedItemAccess = Class(name="java_UnresolvedItemAccess")
java_IfStatement = Class(name="java_IfStatement")
java_SwitchStatement = Class(name="java_SwitchStatement")
java_ArrayCreation = Class(name="java_ArrayCreation")
java_UnresolvedItem = Class(name="java_UnresolvedItem")
java_SingleVariableAccess = Class(name="java_SingleVariableAccess")
java_VariableDeclaration = Class(name="java_VariableDeclaration", is_abstract=True)
java_SuperFieldAccess = Class(name="java_SuperFieldAccess")
java_TryStatement = Class(name="java_TryStatement")
java_CatchClause = Class(name="java_CatchClause")
java_InfixExpression = Class(name="java_InfixExpression")
java_Archive = Class(name="java_Archive")
java_BooleanLiteral = Class(name="java_BooleanLiteral")
java_LabeledStatement = Class(name="java_LabeledStatement")
java_TagElement = Class(name="java_TagElement")
java_ArrayType = Class(name="java_ArrayType")
java_ExpressionStatement = Class(name="java_ExpressionStatement")
java_AnonymousClassDeclaration = Class(name="java_AnonymousClassDeclaration")
java_SuperMethodInvocation = Class(name="java_SuperMethodInvocation")
java_ParameterizedType = Class(name="java_ParameterizedType")
java_Package = Class(name="java_Package")
java_BreakStatement = Class(name="java_BreakStatement")
java_NullLiteral = Class(name="java_NullLiteral")
java_ForStatement = Class(name="java_ForStatement")
java_ArrayAccess = Class(name="java_ArrayAccess")
java_ConstructorDeclaration = Class(name="java_ConstructorDeclaration")
java_PrimitiveTypeInt = Class(name="java_PrimitiveTypeInt")
java_SwitchCase = Class(name="java_SwitchCase")
java_PrefixExpression = Class(name="java_PrefixExpression")
java_ConditionalExpression = Class(name="java_ConditionalExpression")
java_InstanceofExpression = Class(name="java_InstanceofExpression")
java_TypeDeclarationStatement = Class(name="java_TypeDeclarationStatement")
java_ClassDeclaration = Class(name="java_ClassDeclaration")
java_FieldAccess = Class(name="java_FieldAccess")
java_VariableDeclarationExpression = Class(name="java_VariableDeclarationExpression")
java_PrimitiveTypeChar = Class(name="java_PrimitiveTypeChar")
java_Initializer = Class(name="java_Initializer")
java_ContinueStatement = Class(name="java_ContinueStatement")
java_DoStatement = Class(name="java_DoStatement")
java_AssertStatement = Class(name="java_AssertStatement")
java_VariableDeclarationStatement = Class(name="java_VariableDeclarationStatement")
java_NumberLiteral = Class(name="java_NumberLiteral")
java_ClassInstanceCreation = Class(name="java_ClassInstanceCreation")
java_MethodInvocation = Class(name="java_MethodInvocation")
java_ConstructorInvocation = Class(name="java_ConstructorInvocation")
java_CastExpression = Class(name="java_CastExpression")
java_ThrowStatement = Class(name="java_ThrowStatement")
java_NamespaceAccess = Class(name="java_NamespaceAccess", is_abstract=True)
java_Model = Class(name="java_Model")

# java_Expression class attributes and methods

# java_MethodRef class attributes and methods

# java_PrimitiveTypeDouble class attributes and methods

# PrimitiveType class attributes and methods

# java_WhileStatement class attributes and methods

# java_Statement class attributes and methods

# java_StringLiteral class attributes and methods
java_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
java_StringLiteral.attributes={java_StringLiteral_escapedValue}

# Expression class attributes and methods

# java_AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# java_SynchronizedStatement class attributes and methods

# java_Block class attributes and methods

# java_MethodRefParameter class attributes and methods

# ASTNode class attributes and methods

# java_SuperConstructorInvocation class attributes and methods

# Statement class attributes and methods

# AbstractMethodInvocation class attributes and methods

# java_AbstractMethodDeclaration class attributes and methods

# java_SingleVariableDeclaration class attributes and methods

# java_TypeParameter class attributes and methods

# java_PrimitiveTypeVoid class attributes and methods

# java_InterfaceDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# java_UnresolvedTypeDeclaration class attributes and methods

# UnresolvedItem class attributes and methods

# java_TypeDeclaration class attributes and methods

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
java_Modifier.attributes={java_Modifier_inheritance, java_Modifier_static, java_Modifier_visibility}

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

# java_AbstractTypeQualifiedExpression class attributes and methods

# java_Assignment class attributes and methods
java_Assignment_operator: Property = Property(name="operator", type=StringType)
java_Assignment.attributes={java_Assignment_operator}

# java_PostfixExpression class attributes and methods
java_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
java_PostfixExpression.attributes={java_PostfixExpression_operator}

# java_PrimitiveTypeByte class attributes and methods

# java_ArrayInitializer class attributes and methods

# java_AnnotationMemberValuePair class attributes and methods

# NamedElement class attributes and methods

# java_AbstractTypeDeclaration class attributes and methods

# java_Comment class attributes and methods
java_Comment_content: Property = Property(name="content", type=StringType)
java_Comment.attributes={java_Comment_content}

# java_BodyDeclaration class attributes and methods

# java_AbstractMethodInvocation class attributes and methods

# java_ClassFile class attributes and methods

# java_CompilationUnit class attributes and methods
java_CompilationUnit_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java_CompilationUnit.attributes={java_CompilationUnit_originalFilePath}

# NamespaceAccess class attributes and methods

# java_Type class attributes and methods

# java_PrimitiveTypeFloat class attributes and methods

# java_PrimitiveType class attributes and methods

# java_ArrayLengthAccess class attributes and methods

# java_EmptyStatement class attributes and methods

# java_ReturnStatement class attributes and methods

# java_MemberRef class attributes and methods

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

# java_ASTNode class attributes and methods

# java_Annotation class attributes and methods

# java_ParenthesizedExpression class attributes and methods

# java_PrimitiveTypeShort class attributes and methods

# java_MethodDeclaration class attributes and methods

# AbstractMethodDeclaration class attributes and methods

# java_UnresolvedItemAccess class attributes and methods

# java_IfStatement class attributes and methods

# java_SwitchStatement class attributes and methods

# java_ArrayCreation class attributes and methods

# java_UnresolvedItem class attributes and methods

# java_SingleVariableAccess class attributes and methods

# java_VariableDeclaration class attributes and methods

# java_SuperFieldAccess class attributes and methods

# java_TryStatement class attributes and methods

# java_CatchClause class attributes and methods

# java_InfixExpression class attributes and methods
java_InfixExpression_operator: Property = Property(name="operator", type=StringType)
java_InfixExpression.attributes={java_InfixExpression_operator}

# java_Archive class attributes and methods
java_Archive_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java_Archive.attributes={java_Archive_originalFilePath}

# java_BooleanLiteral class attributes and methods
java_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
java_BooleanLiteral.attributes={java_BooleanLiteral_value}

# java_LabeledStatement class attributes and methods

# java_TagElement class attributes and methods

# java_ArrayType class attributes and methods
java_ArrayType_dimensions: Property = Property(name="dimensions", type=IntegerType)
java_ArrayType.attributes={java_ArrayType_dimensions}

# java_ExpressionStatement class attributes and methods

# java_AnonymousClassDeclaration class attributes and methods

# java_SuperMethodInvocation class attributes and methods

# java_ParameterizedType class attributes and methods

# java_Package class attributes and methods

# java_BreakStatement class attributes and methods

# java_NullLiteral class attributes and methods

# java_ForStatement class attributes and methods

# java_ArrayAccess class attributes and methods

# java_ConstructorDeclaration class attributes and methods

# java_PrimitiveTypeInt class attributes and methods

# java_SwitchCase class attributes and methods

# java_PrefixExpression class attributes and methods
java_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
java_PrefixExpression.attributes={java_PrefixExpression_operator}

# java_ConditionalExpression class attributes and methods

# java_InstanceofExpression class attributes and methods

# java_TypeDeclarationStatement class attributes and methods

# java_ClassDeclaration class attributes and methods

# java_FieldAccess class attributes and methods

# java_VariableDeclarationExpression class attributes and methods

# java_PrimitiveTypeChar class attributes and methods

# java_Initializer class attributes and methods

# java_ContinueStatement class attributes and methods

# java_DoStatement class attributes and methods

# java_AssertStatement class attributes and methods

# java_VariableDeclarationStatement class attributes and methods

# java_NumberLiteral class attributes and methods
java_NumberLiteral_tokenValue: Property = Property(name="tokenValue", type=StringType)
java_NumberLiteral.attributes={java_NumberLiteral_tokenValue}

# java_ClassInstanceCreation class attributes and methods

# java_MethodInvocation class attributes and methods

# java_ConstructorInvocation class attributes and methods

# java_CastExpression class attributes and methods

# java_ThrowStatement class attributes and methods

# java_NamespaceAccess class attributes and methods

# java_Model class attributes and methods
java_Model_name: Property = Property(name="name", type=StringType)
java_Model.attributes={java_Model_name}

# Relationships
expression0: BinaryAssociation = BinaryAssociation(
    name="expression0",
    ends={
        Property(name="java_Expression", type=java_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SuperConstructorInvocation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
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
body5: BinaryAssociation = BinaryAssociation(
    name="body5",
    ends={
        Property(name="java_Block", type=java_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SynchronizedStatement", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body13: BinaryAssociation = BinaryAssociation(
    name="body13",
    ends={
        Property(name="java_Block14", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration", type=java_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters15: BinaryAssociation = BinaryAssociation(
    name="parameters15",
    ends={
        Property(name="SingleVariableDeclaration", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methodDeclaration", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thrownExceptions16: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions16",
    ends={
        Property(name="java_TypeAccess18", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration17", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters19: BinaryAssociation = BinaryAssociation(
    name="typeParameters19",
    ends={
        Property(name="java_TypeParameter", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration20", type=java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters21: BinaryAssociation = BinaryAssociation(
    name="typeParameters21",
    ends={
        Property(name="java_TypeParameter22", type=java_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeDeclaration", type=java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="AbstractVariablesContainer", type=java_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(0, 1))
    }
)
bound10: BinaryAssociation = BinaryAssociation(
    name="bound10",
    ends={
        Property(name="java_TypeAccess", type=java_WildCardType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WildCardType", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="java_TypeAccess12", type=java_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeLiteral", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments36: BinaryAssociation = BinaryAssociation(
    name="arguments36",
    ends={
        Property(name="java_AbstractMethodInvocation", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="java_Expression37", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1))
    }
)
method38: BinaryAssociation = BinaryAssociation(
    name="method38",
    ends={
        Property(name="java_AbstractMethodDeclaration40", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodInvocation39", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
qualifier41: BinaryAssociation = BinaryAssociation(
    name="qualifier41",
    ends={
        Property(name="java_TypeAccess42", type=java_AbstractTypeQualifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeQualifiedExpression", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftHandSide43: BinaryAssociation = BinaryAssociation(
    name="leftHandSide43",
    ends={
        Property(name="java_Expression44", type=java_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Assignment", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide45: BinaryAssociation = BinaryAssociation(
    name="rightHandSide45",
    ends={
        Property(name="java_Expression47", type=java_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Assignment46", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand48: BinaryAssociation = BinaryAssociation(
    name="operand48",
    ends={
        Property(name="java_Expression49", type=java_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PostfixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions50: BinaryAssociation = BinaryAssociation(
    name="expressions50",
    ends={
        Property(name="java_Expression51", type=java_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayInitializer", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value52: BinaryAssociation = BinaryAssociation(
    name="value52",
    ends={
        Property(name="java_Expression53", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationMemberValuePair", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifier23: BinaryAssociation = BinaryAssociation(
    name="modifier23",
    ends={
        Property(name="java_Modifier", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableDeclaration", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="java_TypeAccess26", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableDeclaration25", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodDeclaration27: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration27",
    ends={
        Property(name="AbstractMethodDeclaration", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
commentsAfterBody28: BinaryAssociation = BinaryAssociation(
    name="commentsAfterBody28",
    ends={
        Property(name="java_Comment", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsBeforeBody29: BinaryAssociation = BinaryAssociation(
    name="commentsBeforeBody29",
    ends={
        Property(name="java_Comment31", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration30", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaces32: BinaryAssociation = BinaryAssociation(
    name="superInterfaces32",
    ends={
        Property(name="java_TypeAccess34", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration33", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations35: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations35",
    ends={
        Property(name="BodyDeclaration", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractTypeDeclaration", type=java_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalClassFile68: BinaryAssociation = BinaryAssociation(
    name="originalClassFile68",
    ends={
        Property(name="java_ClassFile", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode69", type=java_ClassFile, multiplicity=Multiplicity(0, 1))
    }
)
originalCompilationUnit70: BinaryAssociation = BinaryAssociation(
    name="originalCompilationUnit70",
    ends={
        Property(name="java_CompilationUnit", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode71", type=java_CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
statements72: BinaryAssociation = BinaryAssociation(
    name="statements72",
    ends={
        Property(name="java_Statement74", type=java_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Block73", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type75: BinaryAssociation = BinaryAssociation(
    name="type75",
    ends={
        Property(name="java_Type", type=java_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeAccess76", type=java_Type, multiplicity=Multiplicity(1, 1))
    }
)
array77: BinaryAssociation = BinaryAssociation(
    name="array77",
    ends={
        Property(name="java_Expression78", type=java_ArrayLengthAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayLengthAccess", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression79: BinaryAssociation = BinaryAssociation(
    name="expression79",
    ends={
        Property(name="java_Expression80", type=java_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ReturnStatement", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member54: BinaryAssociation = BinaryAssociation(
    name="member54",
    ends={
        Property(name="java_AnnotationTypeMemberDeclaration", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationMemberValuePair55", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
enumConstants56: BinaryAssociation = BinaryAssociation(
    name="enumConstants56",
    ends={
        Property(name="java_EnumConstantDeclaration", type=java_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnumDeclaration", type=java_EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement57: BinaryAssociation = BinaryAssociation(
    name="importedElement57",
    ends={
        Property(name="java_NamedElement", type=java_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ImportDeclaration", type=java_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
body58: BinaryAssociation = BinaryAssociation(
    name="body58",
    ends={
        Property(name="java_Statement59", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnhancedForStatement", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter60: BinaryAssociation = BinaryAssociation(
    name="parameter60",
    ends={
        Property(name="java_SingleVariableDeclaration62", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnhancedForStatement61", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression63: BinaryAssociation = BinaryAssociation(
    name="expression63",
    ends={
        Property(name="java_Expression65", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnhancedForStatement64", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comments66: BinaryAssociation = BinaryAssociation(
    name="comments66",
    ends={
        Property(name="java_Comment67", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type95: BinaryAssociation = BinaryAssociation(
    name="type95",
    ends={
        Property(name="java_TypeAccess96", type=java_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Annotation", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values97: BinaryAssociation = BinaryAssociation(
    name="values97",
    ends={
        Property(name="java_AnnotationMemberValuePair99", type=java_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Annotation98", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression100: BinaryAssociation = BinaryAssociation(
    name="expression100",
    ends={
        Property(name="java_Expression101", type=java_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParenthesizedExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element102: BinaryAssociation = BinaryAssociation(
    name="element102",
    ends={
        Property(name="java_UnresolvedItem", type=java_UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_UnresolvedItemAccess", type=java_UnresolvedItem, multiplicity=Multiplicity(0, 1))
    }
)
expression103: BinaryAssociation = BinaryAssociation(
    name="expression103",
    ends={
        Property(name="java_Expression104", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement105: BinaryAssociation = BinaryAssociation(
    name="elseStatement105",
    ends={
        Property(name="java_Statement107", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement106", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression81: BinaryAssociation = BinaryAssociation(
    name="expression81",
    ends={
        Property(name="java_Expression82", type=java_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements83: BinaryAssociation = BinaryAssociation(
    name="statements83",
    ends={
        Property(name="java_Statement85", type=java_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchStatement84", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type86: BinaryAssociation = BinaryAssociation(
    name="type86",
    ends={
        Property(name="java_TypeAccess87", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions88: BinaryAssociation = BinaryAssociation(
    name="dimensions88",
    ends={
        Property(name="java_Expression90", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation89", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer91: BinaryAssociation = BinaryAssociation(
    name="initializer91",
    ends={
        Property(name="java_ArrayInitializer93", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation92", type=java_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable94: BinaryAssociation = BinaryAssociation(
    name="variable94",
    ends={
        Property(name="java_VariableDeclaration", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableAccess", type=java_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
type119: BinaryAssociation = BinaryAssociation(
    name="type119",
    ends={
        Property(name="java_TypeAccess121", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationTypeMemberDeclaration120", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imports122: BinaryAssociation = BinaryAssociation(
    name="imports122",
    ends={
        Property(name="java_ImportDeclaration124", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit123", type=java_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types125: BinaryAssociation = BinaryAssociation(
    name="types125",
    ends={
        Property(name="java_AbstractTypeDeclaration127", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit126", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
field128: BinaryAssociation = BinaryAssociation(
    name="field128",
    ends={
        Property(name="java_SingleVariableAccess129", type=java_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SuperFieldAccess", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer130: BinaryAssociation = BinaryAssociation(
    name="initializer130",
    ends={
        Property(name="java_Expression132", type=java_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_VariableDeclaration131", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses133: BinaryAssociation = BinaryAssociation(
    name="catchClauses133",
    ends={
        Property(name="java_CatchClause", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement", type=java_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body134: BinaryAssociation = BinaryAssociation(
    name="body134",
    ends={
        Property(name="java_Block136", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement135", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally_137: BinaryAssociation = BinaryAssociation(
    name="finally_137",
    ends={
        Property(name="java_Block139", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement138", type=java_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenStatement108: BinaryAssociation = BinaryAssociation(
    name="thenStatement108",
    ends={
        Property(name="java_Statement110", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement109", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand111: BinaryAssociation = BinaryAssociation(
    name="rightOperand111",
    ends={
        Property(name="java_Expression112", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand113: BinaryAssociation = BinaryAssociation(
    name="leftOperand113",
    ends={
        Property(name="java_Expression115", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression114", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands116: BinaryAssociation = BinaryAssociation(
    name="extendedOperands116",
    ends={
        Property(name="java_Expression118", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression117", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label150: BinaryAssociation = BinaryAssociation(
    name="label150",
    ends={
        Property(name="java_LabeledStatement", type=java_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_BreakStatement", type=java_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
elementType151: BinaryAssociation = BinaryAssociation(
    name="elementType151",
    ends={
        Property(name="java_TypeAccess152", type=java_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayType", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression153: BinaryAssociation = BinaryAssociation(
    name="expression153",
    ends={
        Property(name="java_Expression154", type=java_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ExpressionStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifier155: BinaryAssociation = BinaryAssociation(
    name="modifier155",
    ends={
        Property(name="java_Modifier156", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_BodyDeclaration", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstractTypeDeclaration157: BinaryAssociation = BinaryAssociation(
    name="abstractTypeDeclaration157",
    ends={
        Property(name="AbstractTypeDeclaration", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
anonymousClassDeclarationOwner158: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclarationOwner158",
    ends={
        Property(name="AnonymousClassDeclaration", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations159", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
annotations160: BinaryAssociation = BinaryAssociation(
    name="annotations160",
    ends={
        Property(name="java_Annotation162", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_BodyDeclaration161", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type140: BinaryAssociation = BinaryAssociation(
    name="type140",
    ends={
        Property(name="java_TypeAccess141", type=java_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParameterizedType", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments142: BinaryAssociation = BinaryAssociation(
    name="typeArguments142",
    ends={
        Property(name="java_TypeAccess144", type=java_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParameterizedType143", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElements145: BinaryAssociation = BinaryAssociation(
    name="ownedElements145",
    ends={
        Property(name="java_AbstractTypeDeclaration146", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Package", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPackages148: BinaryAssociation = BinaryAssociation(
    name="ownedPackages148",
    ends={
        Property(name="java_Package149", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Package147", type=java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseExpression178: BinaryAssociation = BinaryAssociation(
    name="elseExpression178",
    ends={
        Property(name="java_Expression180", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression179", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression181: BinaryAssociation = BinaryAssociation(
    name="expression181",
    ends={
        Property(name="java_Expression182", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializers183: BinaryAssociation = BinaryAssociation(
    name="initializers183",
    ends={
        Property(name="java_Expression185", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement184", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body186: BinaryAssociation = BinaryAssociation(
    name="body186",
    ends={
        Property(name="java_Statement188", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement187", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updaters189: BinaryAssociation = BinaryAssociation(
    name="updaters189",
    ends={
        Property(name="java_Expression191", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement190", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
array192: BinaryAssociation = BinaryAssociation(
    name="array192",
    ends={
        Property(name="java_Expression193", type=java_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayAccess", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index194: BinaryAssociation = BinaryAssociation(
    name="index194",
    ends={
        Property(name="java_Expression196", type=java_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayAccess195", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type197: BinaryAssociation = BinaryAssociation(
    name="type197",
    ends={
        Property(name="java_TypeAccess198", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractVariablesContainer", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments199: BinaryAssociation = BinaryAssociation(
    name="fragments199",
    ends={
        Property(name="VariableDeclarationFragment", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="variablesContainer", type=java_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body163: BinaryAssociation = BinaryAssociation(
    name="body163",
    ends={
        Property(name="java_Block165", type=java_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CatchClause164", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception166: BinaryAssociation = BinaryAssociation(
    name="exception166",
    ends={
        Property(name="java_SingleVariableDeclaration168", type=java_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CatchClause167", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression169: BinaryAssociation = BinaryAssociation(
    name="expression169",
    ends={
        Property(name="java_Expression170", type=java_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchCase", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand171: BinaryAssociation = BinaryAssociation(
    name="operand171",
    ends={
        Property(name="java_Expression172", type=java_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PrefixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression173: BinaryAssociation = BinaryAssociation(
    name="expression173",
    ends={
        Property(name="java_Expression174", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression175: BinaryAssociation = BinaryAssociation(
    name="thenExpression175",
    ends={
        Property(name="java_Expression177", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression176", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message211: BinaryAssociation = BinaryAssociation(
    name="message211",
    ends={
        Property(name="java_Expression213", type=java_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AssertStatement212", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand214: BinaryAssociation = BinaryAssociation(
    name="rightOperand214",
    ends={
        Property(name="java_TypeAccess215", type=java_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InstanceofExpression", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand216: BinaryAssociation = BinaryAssociation(
    name="leftOperand216",
    ends={
        Property(name="java_Expression218", type=java_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InstanceofExpression217", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration219: BinaryAssociation = BinaryAssociation(
    name="declaration219",
    ends={
        Property(name="java_AbstractTypeDeclaration220", type=java_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeDeclarationStatement", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superClass221: BinaryAssociation = BinaryAssociation(
    name="superClass221",
    ends={
        Property(name="java_TypeAccess222", type=java_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassDeclaration", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression223: BinaryAssociation = BinaryAssociation(
    name="expression223",
    ends={
        Property(name="java_Expression224", type=java_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_FieldAccess", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body200: BinaryAssociation = BinaryAssociation(
    name="body200",
    ends={
        Property(name="java_Block201", type=java_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Initializer", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label202: BinaryAssociation = BinaryAssociation(
    name="label202",
    ends={
        Property(name="java_LabeledStatement203", type=java_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ContinueStatement", type=java_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
expression204: BinaryAssociation = BinaryAssociation(
    name="expression204",
    ends={
        Property(name="java_Expression205", type=java_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_DoStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body206: BinaryAssociation = BinaryAssociation(
    name="body206",
    ends={
        Property(name="java_Statement208", type=java_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_DoStatement207", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression209: BinaryAssociation = BinaryAssociation(
    name="expression209",
    ends={
        Property(name="java_Expression210", type=java_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AssertStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body239: BinaryAssociation = BinaryAssociation(
    name="body239",
    ends={
        Property(name="java_Statement241", type=java_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_LabeledStatement240", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations242: BinaryAssociation = BinaryAssociation(
    name="annotations242",
    ends={
        Property(name="java_Annotation243", type=java_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_VariableDeclarationStatement", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression244: BinaryAssociation = BinaryAssociation(
    name="expression244",
    ends={
        Property(name="java_Expression245", type=java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassInstanceCreation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type246: BinaryAssociation = BinaryAssociation(
    name="type246",
    ends={
        Property(name="java_TypeAccess248", type=java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassInstanceCreation247", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anonymousClassDeclaration249: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration249",
    ends={
        Property(name="java_AnonymousClassDeclaration", type=java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassInstanceCreation250", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field225: BinaryAssociation = BinaryAssociation(
    name="field225",
    ends={
        Property(name="java_SingleVariableAccess227", type=java_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_FieldAccess226", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression228: BinaryAssociation = BinaryAssociation(
    name="expression228",
    ends={
        Property(name="java_Expression229", type=java_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodInvocation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyDeclarations230: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations230",
    ends={
        Property(name="BodyDeclaration231", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclarationOwner", type=java_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression232: BinaryAssociation = BinaryAssociation(
    name="expression232",
    ends={
        Property(name="java_Expression233", type=java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CastExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type234: BinaryAssociation = BinaryAssociation(
    name="type234",
    ends={
        Property(name="java_TypeAccess236", type=java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CastExpression235", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression237: BinaryAssociation = BinaryAssociation(
    name="expression237",
    ends={
        Property(name="java_Expression238", type=java_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ThrowStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compilationUnits251: BinaryAssociation = BinaryAssociation(
    name="compilationUnits251",
    ends={
        Property(name="java_CompilationUnit252", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model", type=java_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orphanTypes253: BinaryAssociation = BinaryAssociation(
    name="orphanTypes253",
    ends={
        Property(name="java_Type255", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model254", type=java_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archives256: BinaryAssociation = BinaryAssociation(
    name="archives256",
    ends={
        Property(name="java_Archive", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model257", type=java_Archive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElements258: BinaryAssociation = BinaryAssociation(
    name="ownedElements258",
    ends={
        Property(name="java_Package260", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model259", type=java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_java_MethodRef_ASTNode = Generalization(general=ASTNode, specific=java_MethodRef)
gen_java_PrimitiveTypeDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeDouble)
gen_java_WhileStatement_Statement = Generalization(general=Statement, specific=java_WhileStatement)
gen_java_StringLiteral_Expression = Generalization(general=Expression, specific=java_StringLiteral)
gen_java_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_AnnotationTypeDeclaration)
gen_java_SynchronizedStatement_Statement = Generalization(general=Statement, specific=java_SynchronizedStatement)
gen_java_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=java_MethodRefParameter)
gen_java_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=java_SuperConstructorInvocation)
gen_java_SuperConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_SuperConstructorInvocation)
gen_java_AbstractMethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AbstractMethodDeclaration)
gen_java_PrimitiveTypeVoid_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeVoid)
gen_java_InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=java_InterfaceDeclaration)
gen_java_UnresolvedTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_UnresolvedTypeDeclaration)
gen_java_UnresolvedTypeDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedTypeDeclaration)
gen_java_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_TypeDeclaration)
gen_java_PrimitiveTypeLong_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeLong)
gen_java_PrimitiveTypeBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeBoolean)
gen_java_CharacterLiteral_Expression = Generalization(general=Expression, specific=java_CharacterLiteral)
gen_java_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_FieldDeclaration)
gen_java_FieldDeclaration_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_FieldDeclaration)
gen_java_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_SingleVariableDeclaration)
gen_java_ThisExpression_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_ThisExpression)
gen_java_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_VariableDeclarationFragment)
gen_java_WildCardType_Type = Generalization(general=Type, specific=java_WildCardType)
gen_java_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_EnumConstantDeclaration)
gen_java_EnumConstantDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_EnumConstantDeclaration)
gen_java_TypeLiteral_Expression = Generalization(general=Expression, specific=java_TypeLiteral)
gen_java_AbstractTypeQualifiedExpression_Expression = Generalization(general=Expression, specific=java_AbstractTypeQualifiedExpression)
gen_java_Assignment_Expression = Generalization(general=Expression, specific=java_Assignment)
gen_java_PostfixExpression_Expression = Generalization(general=Expression, specific=java_PostfixExpression)
gen_java_PrimitiveTypeByte_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeByte)
gen_java_ArrayInitializer_Expression = Generalization(general=Expression, specific=java_ArrayInitializer)
gen_java_AnnotationMemberValuePair_NamedElement = Generalization(general=NamedElement, specific=java_AnnotationMemberValuePair)
gen_java_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AbstractTypeDeclaration)
gen_java_AbstractTypeDeclaration_Type = Generalization(general=Type, specific=java_AbstractTypeDeclaration)
gen_java_AbstractMethodInvocation_ASTNode = Generalization(general=ASTNode, specific=java_AbstractMethodInvocation)
gen_java_Block_Statement = Generalization(general=Statement, specific=java_Block)
gen_java_TypeAccess_Expression = Generalization(general=Expression, specific=java_TypeAccess)
gen_java_TypeAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java_TypeAccess)
gen_java_TypeParameter_Type = Generalization(general=Type, specific=java_TypeParameter)
gen_java_PrimitiveTypeFloat_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeFloat)
gen_java_PrimitiveType_Type = Generalization(general=Type, specific=java_PrimitiveType)
gen_java_ArrayLengthAccess_Expression = Generalization(general=Expression, specific=java_ArrayLengthAccess)
gen_java_EmptyStatement_Statement = Generalization(general=Statement, specific=java_EmptyStatement)
gen_java_ReturnStatement_Statement = Generalization(general=Statement, specific=java_ReturnStatement)
gen_java_MemberRef_ASTNode = Generalization(general=ASTNode, specific=java_MemberRef)
gen_java_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_EnumDeclaration)
gen_java_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=java_ImportDeclaration)
gen_java_EnhancedForStatement_Statement = Generalization(general=Statement, specific=java_EnhancedForStatement)
gen_java_Annotation_Expression = Generalization(general=Expression, specific=java_Annotation)
gen_java_Modifier_ASTNode = Generalization(general=ASTNode, specific=java_Modifier)
gen_java_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=java_ParenthesizedExpression)
gen_java_PrimitiveTypeShort_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeShort)
gen_java_MethodDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=java_MethodDeclaration)
gen_java_UnresolvedItemAccess_Expression = Generalization(general=Expression, specific=java_UnresolvedItemAccess)
gen_java_UnresolvedItemAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java_UnresolvedItemAccess)
gen_java_IfStatement_Statement = Generalization(general=Statement, specific=java_IfStatement)
gen_java_Statement_ASTNode = Generalization(general=ASTNode, specific=java_Statement)
gen_java_SwitchStatement_Statement = Generalization(general=Statement, specific=java_SwitchStatement)
gen_java_ArrayCreation_Expression = Generalization(general=Expression, specific=java_ArrayCreation)
gen_java_UnresolvedItem_NamedElement = Generalization(general=NamedElement, specific=java_UnresolvedItem)
gen_java_SingleVariableAccess_Expression = Generalization(general=Expression, specific=java_SingleVariableAccess)
gen_java_CompilationUnit_NamedElement = Generalization(general=NamedElement, specific=java_CompilationUnit)
gen_java_SuperFieldAccess_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_SuperFieldAccess)
gen_java_VariableDeclaration_NamedElement = Generalization(general=NamedElement, specific=java_VariableDeclaration)
gen_java_TryStatement_Statement = Generalization(general=Statement, specific=java_TryStatement)
gen_java_InfixExpression_Expression = Generalization(general=Expression, specific=java_InfixExpression)
gen_java_Archive_NamedElement = Generalization(general=NamedElement, specific=java_Archive)
gen_java_BooleanLiteral_Expression = Generalization(general=Expression, specific=java_BooleanLiteral)
gen_java_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AnnotationTypeMemberDeclaration)
gen_java_TagElement_ASTNode = Generalization(general=ASTNode, specific=java_TagElement)
gen_java_ArrayType_Type = Generalization(general=Type, specific=java_ArrayType)
gen_java_ExpressionStatement_Statement = Generalization(general=Statement, specific=java_ExpressionStatement)
gen_java_BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=java_BodyDeclaration)
gen_java_SuperMethodInvocation_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_SuperMethodInvocation)
gen_java_ParameterizedType_Type = Generalization(general=Type, specific=java_ParameterizedType)
gen_java_Package_NamedElement = Generalization(general=NamedElement, specific=java_Package)
gen_java_BreakStatement_Statement = Generalization(general=Statement, specific=java_BreakStatement)
gen_java_NullLiteral_Expression = Generalization(general=Expression, specific=java_NullLiteral)
gen_java_ForStatement_Statement = Generalization(general=Statement, specific=java_ForStatement)
gen_java_ArrayAccess_Expression = Generalization(general=Expression, specific=java_ArrayAccess)
gen_java_AbstractVariablesContainer_ASTNode = Generalization(general=ASTNode, specific=java_AbstractVariablesContainer)
gen_java_SuperMethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_SuperMethodInvocation)
gen_java_ConstructorDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=java_ConstructorDeclaration)
gen_java_PrimitiveTypeInt_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeInt)
gen_java_CatchClause_Statement = Generalization(general=Statement, specific=java_CatchClause)
gen_java_SwitchCase_Statement = Generalization(general=Statement, specific=java_SwitchCase)
gen_java_Type_NamedElement = Generalization(general=NamedElement, specific=java_Type)
gen_java_PrefixExpression_Expression = Generalization(general=Expression, specific=java_PrefixExpression)
gen_java_ConditionalExpression_Expression = Generalization(general=Expression, specific=java_ConditionalExpression)
gen_java_InstanceofExpression_Expression = Generalization(general=Expression, specific=java_InstanceofExpression)
gen_java_Comment_ASTNode = Generalization(general=ASTNode, specific=java_Comment)
gen_java_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=java_TypeDeclarationStatement)
gen_java_ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=java_ClassDeclaration)
gen_java_FieldAccess_Expression = Generalization(general=Expression, specific=java_FieldAccess)
gen_java_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=java_VariableDeclarationExpression)
gen_java_VariableDeclarationExpression_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_VariableDeclarationExpression)
gen_java_PrimitiveTypeChar_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeChar)
gen_java_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_Initializer)
gen_java_ContinueStatement_Statement = Generalization(general=Statement, specific=java_ContinueStatement)
gen_java_ClassFile_NamedElement = Generalization(general=NamedElement, specific=java_ClassFile)
gen_java_DoStatement_Statement = Generalization(general=Statement, specific=java_DoStatement)
gen_java_AssertStatement_Statement = Generalization(general=Statement, specific=java_AssertStatement)
gen_java_NamedElement_ASTNode = Generalization(general=ASTNode, specific=java_NamedElement)
gen_java_LabeledStatement_NamedElement = Generalization(general=NamedElement, specific=java_LabeledStatement)
gen_java_LabeledStatement_Statement = Generalization(general=Statement, specific=java_LabeledStatement)
gen_java_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=java_VariableDeclarationStatement)
gen_java_VariableDeclarationStatement_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_VariableDeclarationStatement)
gen_java_NumberLiteral_Expression = Generalization(general=Expression, specific=java_NumberLiteral)
gen_java_Expression_ASTNode = Generalization(general=ASTNode, specific=java_Expression)
gen_java_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=java_ClassInstanceCreation)
gen_java_ClassInstanceCreation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_ClassInstanceCreation)
gen_java_MethodInvocation_Expression = Generalization(general=Expression, specific=java_MethodInvocation)
gen_java_MethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_MethodInvocation)
gen_java_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=java_AnonymousClassDeclaration)
gen_java_ConstructorInvocation_Statement = Generalization(general=Statement, specific=java_ConstructorInvocation)
gen_java_ConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_ConstructorInvocation)
gen_java_CastExpression_Expression = Generalization(general=Expression, specific=java_CastExpression)
gen_java_ThrowStatement_Statement = Generalization(general=Statement, specific=java_ThrowStatement)
gen_java_NamespaceAccess_ASTNode = Generalization(general=ASTNode, specific=java_NamespaceAccess)

# Domain Model
domain_model = DomainModel(
    name="java",
    types={java_Expression, java_MethodRef, java_PrimitiveTypeDouble, PrimitiveType, java_WhileStatement, java_Statement, java_StringLiteral, Expression, java_AnnotationTypeDeclaration, AbstractTypeDeclaration, java_SynchronizedStatement, java_Block, java_MethodRefParameter, ASTNode, java_SuperConstructorInvocation, Statement, AbstractMethodInvocation, java_AbstractMethodDeclaration, java_SingleVariableDeclaration, java_TypeParameter, java_PrimitiveTypeVoid, java_InterfaceDeclaration, TypeDeclaration, java_UnresolvedTypeDeclaration, UnresolvedItem, java_TypeDeclaration, java_PrimitiveTypeLong, java_PrimitiveTypeBoolean, java_CharacterLiteral, java_FieldDeclaration, AbstractVariablesContainer, java_Modifier, java_ThisExpression, AbstractTypeQualifiedExpression, java_VariableDeclarationFragment, VariableDeclaration, java_AbstractVariablesContainer, java_WildCardType, Type, java_TypeAccess, java_EnumConstantDeclaration, BodyDeclaration, java_TypeLiteral, java_AbstractTypeQualifiedExpression, java_Assignment, java_PostfixExpression, java_PrimitiveTypeByte, java_ArrayInitializer, java_AnnotationMemberValuePair, NamedElement, java_AbstractTypeDeclaration, java_Comment, java_BodyDeclaration, java_AbstractMethodInvocation, java_ClassFile, java_CompilationUnit, NamespaceAccess, java_Type, java_PrimitiveTypeFloat, java_PrimitiveType, java_ArrayLengthAccess, java_EmptyStatement, java_ReturnStatement, java_MemberRef, java_AnnotationTypeMemberDeclaration, java_EnumDeclaration, java_ImportDeclaration, java_NamedElement, java_EnhancedForStatement, java_ASTNode, java_Annotation, java_ParenthesizedExpression, java_PrimitiveTypeShort, java_MethodDeclaration, AbstractMethodDeclaration, java_UnresolvedItemAccess, java_IfStatement, java_SwitchStatement, java_ArrayCreation, java_UnresolvedItem, java_SingleVariableAccess, java_VariableDeclaration, java_SuperFieldAccess, java_TryStatement, java_CatchClause, java_InfixExpression, java_Archive, java_BooleanLiteral, java_LabeledStatement, java_TagElement, java_ArrayType, java_ExpressionStatement, java_AnonymousClassDeclaration, java_SuperMethodInvocation, java_ParameterizedType, java_Package, java_BreakStatement, java_NullLiteral, java_ForStatement, java_ArrayAccess, java_ConstructorDeclaration, java_PrimitiveTypeInt, java_SwitchCase, java_PrefixExpression, java_ConditionalExpression, java_InstanceofExpression, java_TypeDeclarationStatement, java_ClassDeclaration, java_FieldAccess, java_VariableDeclarationExpression, java_PrimitiveTypeChar, java_Initializer, java_ContinueStatement, java_DoStatement, java_AssertStatement, java_VariableDeclarationStatement, java_NumberLiteral, java_ClassInstanceCreation, java_MethodInvocation, java_ConstructorInvocation, java_CastExpression, java_ThrowStatement, java_NamespaceAccess, java_Model, PostfixExpressionKind, VisibilityKind, InheritanceKind, AssignmentKind, PrefixExpressionKind, InfixExpressionKind},
    associations={expression0, expression1, body3, body5, body13, parameters15, thrownExceptions16, typeParameters19, typeParameters21, expression6, variablesContainer9, bound10, type11, arguments36, method38, qualifier41, leftHandSide43, rightHandSide45, operand48, expressions50, value52, modifier23, type24, methodDeclaration27, commentsAfterBody28, commentsBeforeBody29, superInterfaces32, bodyDeclarations35, originalClassFile68, originalCompilationUnit70, statements72, type75, array77, expression79, member54, enumConstants56, importedElement57, body58, parameter60, expression63, comments66, type95, values97, expression100, element102, expression103, elseStatement105, expression81, statements83, type86, dimensions88, initializer91, variable94, type119, imports122, types125, field128, initializer130, catchClauses133, body134, finally_137, thenStatement108, rightOperand111, leftOperand113, extendedOperands116, label150, elementType151, expression153, modifier155, abstractTypeDeclaration157, anonymousClassDeclarationOwner158, annotations160, type140, typeArguments142, ownedElements145, ownedPackages148, elseExpression178, expression181, initializers183, body186, updaters189, array192, index194, type197, fragments199, body163, exception166, expression169, operand171, expression173, thenExpression175, message211, rightOperand214, leftOperand216, declaration219, superClass221, expression223, body200, label202, expression204, body206, expression209, body239, annotations242, expression244, type246, anonymousClassDeclaration249, field225, expression228, bodyDeclarations230, expression232, type234, expression237, compilationUnits251, orphanTypes253, archives256, ownedElements258},
    generalizations={gen_java_MethodRef_ASTNode, gen_java_PrimitiveTypeDouble_PrimitiveType, gen_java_WhileStatement_Statement, gen_java_StringLiteral_Expression, gen_java_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_java_SynchronizedStatement_Statement, gen_java_MethodRefParameter_ASTNode, gen_java_SuperConstructorInvocation_Statement, gen_java_SuperConstructorInvocation_AbstractMethodInvocation, gen_java_AbstractMethodDeclaration_BodyDeclaration, gen_java_PrimitiveTypeVoid_PrimitiveType, gen_java_InterfaceDeclaration_TypeDeclaration, gen_java_UnresolvedTypeDeclaration_AbstractTypeDeclaration, gen_java_UnresolvedTypeDeclaration_UnresolvedItem, gen_java_TypeDeclaration_AbstractTypeDeclaration, gen_java_PrimitiveTypeLong_PrimitiveType, gen_java_PrimitiveTypeBoolean_PrimitiveType, gen_java_CharacterLiteral_Expression, gen_java_FieldDeclaration_BodyDeclaration, gen_java_FieldDeclaration_AbstractVariablesContainer, gen_java_SingleVariableDeclaration_VariableDeclaration, gen_java_ThisExpression_AbstractTypeQualifiedExpression, gen_java_VariableDeclarationFragment_VariableDeclaration, gen_java_WildCardType_Type, gen_java_EnumConstantDeclaration_BodyDeclaration, gen_java_EnumConstantDeclaration_VariableDeclaration, gen_java_TypeLiteral_Expression, gen_java_AbstractTypeQualifiedExpression_Expression, gen_java_Assignment_Expression, gen_java_PostfixExpression_Expression, gen_java_PrimitiveTypeByte_PrimitiveType, gen_java_ArrayInitializer_Expression, gen_java_AnnotationMemberValuePair_NamedElement, gen_java_AbstractTypeDeclaration_BodyDeclaration, gen_java_AbstractTypeDeclaration_Type, gen_java_AbstractMethodInvocation_ASTNode, gen_java_Block_Statement, gen_java_TypeAccess_Expression, gen_java_TypeAccess_NamespaceAccess, gen_java_TypeParameter_Type, gen_java_PrimitiveTypeFloat_PrimitiveType, gen_java_PrimitiveType_Type, gen_java_ArrayLengthAccess_Expression, gen_java_EmptyStatement_Statement, gen_java_ReturnStatement_Statement, gen_java_MemberRef_ASTNode, gen_java_EnumDeclaration_AbstractTypeDeclaration, gen_java_ImportDeclaration_ASTNode, gen_java_EnhancedForStatement_Statement, gen_java_Annotation_Expression, gen_java_Modifier_ASTNode, gen_java_ParenthesizedExpression_Expression, gen_java_PrimitiveTypeShort_PrimitiveType, gen_java_MethodDeclaration_AbstractMethodDeclaration, gen_java_UnresolvedItemAccess_Expression, gen_java_UnresolvedItemAccess_NamespaceAccess, gen_java_IfStatement_Statement, gen_java_Statement_ASTNode, gen_java_SwitchStatement_Statement, gen_java_ArrayCreation_Expression, gen_java_UnresolvedItem_NamedElement, gen_java_SingleVariableAccess_Expression, gen_java_CompilationUnit_NamedElement, gen_java_SuperFieldAccess_AbstractTypeQualifiedExpression, gen_java_VariableDeclaration_NamedElement, gen_java_TryStatement_Statement, gen_java_InfixExpression_Expression, gen_java_Archive_NamedElement, gen_java_BooleanLiteral_Expression, gen_java_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_java_TagElement_ASTNode, gen_java_ArrayType_Type, gen_java_ExpressionStatement_Statement, gen_java_BodyDeclaration_NamedElement, gen_java_SuperMethodInvocation_AbstractTypeQualifiedExpression, gen_java_ParameterizedType_Type, gen_java_Package_NamedElement, gen_java_BreakStatement_Statement, gen_java_NullLiteral_Expression, gen_java_ForStatement_Statement, gen_java_ArrayAccess_Expression, gen_java_AbstractVariablesContainer_ASTNode, gen_java_SuperMethodInvocation_AbstractMethodInvocation, gen_java_ConstructorDeclaration_AbstractMethodDeclaration, gen_java_PrimitiveTypeInt_PrimitiveType, gen_java_CatchClause_Statement, gen_java_SwitchCase_Statement, gen_java_Type_NamedElement, gen_java_PrefixExpression_Expression, gen_java_ConditionalExpression_Expression, gen_java_InstanceofExpression_Expression, gen_java_Comment_ASTNode, gen_java_TypeDeclarationStatement_Statement, gen_java_ClassDeclaration_TypeDeclaration, gen_java_FieldAccess_Expression, gen_java_VariableDeclarationExpression_Expression, gen_java_VariableDeclarationExpression_AbstractVariablesContainer, gen_java_PrimitiveTypeChar_PrimitiveType, gen_java_Initializer_BodyDeclaration, gen_java_ContinueStatement_Statement, gen_java_ClassFile_NamedElement, gen_java_DoStatement_Statement, gen_java_AssertStatement_Statement, gen_java_NamedElement_ASTNode, gen_java_LabeledStatement_NamedElement, gen_java_LabeledStatement_Statement, gen_java_VariableDeclarationStatement_Statement, gen_java_VariableDeclarationStatement_AbstractVariablesContainer, gen_java_NumberLiteral_Expression, gen_java_Expression_ASTNode, gen_java_ClassInstanceCreation_Expression, gen_java_ClassInstanceCreation_AbstractMethodInvocation, gen_java_MethodInvocation_Expression, gen_java_MethodInvocation_AbstractMethodInvocation, gen_java_AnonymousClassDeclaration_ASTNode, gen_java_ConstructorInvocation_Statement, gen_java_ConstructorInvocation_AbstractMethodInvocation, gen_java_CastExpression_Expression, gen_java_ThrowStatement_Statement, gen_java_NamespaceAccess_ASTNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)