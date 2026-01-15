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

InheritanceKind: Enumeration = Enumeration(
    name="InheritanceKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="final")
    }
)

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
			EnumerationLiteral(name="CONDITIONAL_OR")
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

# Classes
BodyDeclaration = Class(name="BodyDeclaration")
java__Block = Class(name="java::::Block")
java__SingleVariableDeclaration = Class(name="java::::SingleVariableDeclaration")
java__TypeAccess = Class(name="java::::TypeAccess")
java__AbstractMethodDeclaration = Class(name="java::::AbstractMethodDeclaration", is_abstract=True)
java__AbstractMethodInvocation = Class(name="java::::AbstractMethodInvocation", is_abstract=True)
ASTNode = Class(name="ASTNode")
java__Expression = Class(name="java::::Expression", is_abstract=True)
java__TypeParameter = Class(name="java::::TypeParameter")
java__MethodRef = Class(name="java::::MethodRef")
java__Package = Class(name="java::::Package")
java__AbstractTypeQualifiedExpression = Class(name="java::::AbstractTypeQualifiedExpression", is_abstract=True)
Expression = Class(name="Expression")
java__AbstractVariablesContainer = Class(name="java::::AbstractVariablesContainer", is_abstract=True)
java__AbstractTypeDeclaration = Class(name="java::::AbstractTypeDeclaration", is_abstract=True)
Type = Class(name="Type")
java__BodyDeclaration = Class(name="java::::BodyDeclaration", is_abstract=True)
java__Comment = Class(name="java::::Comment", is_abstract=True)
java__AnnotationMemberValuePair = Class(name="java::::AnnotationMemberValuePair")
java__Archive = Class(name="java::::Archive")
NamedElement = Class(name="NamedElement")
java__ClassFile = Class(name="java::::ClassFile")
java__Manifest = Class(name="java::::Manifest")
java__AssertStatement = Class(name="java::::AssertStatement")
Statement = Class(name="Statement")
java__VariableDeclarationFragment = Class(name="java::::VariableDeclarationFragment")
java__Annotation = Class(name="java::::Annotation")
java__CompilationUnit = Class(name="java::::CompilationUnit")
java__AnnotationTypeMemberDeclaration = Class(name="java::::AnnotationTypeMemberDeclaration")
java__AnnotationTypeDeclaration = Class(name="java::::AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
java__ASTNode = Class(name="java::::ASTNode", is_abstract=True)
java__AnonymousClassDeclaration = Class(name="java::::AnonymousClassDeclaration")
java__ClassInstanceCreation = Class(name="java::::ClassInstanceCreation")
java__ArrayAccess = Class(name="java::::ArrayAccess")
java__ArrayInitializer = Class(name="java::::ArrayInitializer")
java__ArrayLengthAccess = Class(name="java::::ArrayLengthAccess")
java__ArrayCreation = Class(name="java::::ArrayCreation")
java__Assignment = Class(name="java::::Assignment")
java__ArrayType = Class(name="java::::ArrayType")
java__Modifier = Class(name="java::::Modifier")
java__BooleanLiteral = Class(name="java::::BooleanLiteral")
java__BlockComment = Class(name="java::::BlockComment")
Comment = Class(name="Comment")
java__CastExpression = Class(name="java::::CastExpression")
java__CatchClause = Class(name="java::::CatchClause")
java__CharacterLiteral = Class(name="java::::CharacterLiteral")
java__Statement = Class(name="java::::Statement", is_abstract=True)
java__BreakStatement = Class(name="java::::BreakStatement")
java__LabeledStatement = Class(name="java::::LabeledStatement")
AbstractMethodInvocation = Class(name="AbstractMethodInvocation")
java__ConstructorDeclaration = Class(name="java::::ConstructorDeclaration")
AbstractMethodDeclaration = Class(name="AbstractMethodDeclaration")
java__ConstructorInvocation = Class(name="java::::ConstructorInvocation")
java__ClassDeclaration = Class(name="java::::ClassDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
java__ConditionalExpression = Class(name="java::::ConditionalExpression")
java__ImportDeclaration = Class(name="java::::ImportDeclaration")
java__ContinueStatement = Class(name="java::::ContinueStatement")
java__DoStatement = Class(name="java::::DoStatement")
java__EmptyStatement = Class(name="java::::EmptyStatement")
java__EnhancedForStatement = Class(name="java::::EnhancedForStatement")
java__EnumConstantDeclaration = Class(name="java::::EnumConstantDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
java__EnumDeclaration = Class(name="java::::EnumDeclaration")
java__ExpressionStatement = Class(name="java::::ExpressionStatement")
java__FieldAccess = Class(name="java::::FieldAccess")
java__SingleVariableAccess = Class(name="java::::SingleVariableAccess")
java__IfStatement = Class(name="java::::IfStatement")
java__FieldDeclaration = Class(name="java::::FieldDeclaration")
AbstractVariablesContainer = Class(name="AbstractVariablesContainer")
java__ForStatement = Class(name="java::::ForStatement")
java__NamedElement = Class(name="java::::NamedElement", is_abstract=True)
java__InfixExpression = Class(name="java::::InfixExpression")
java__Initializer = Class(name="java::::Initializer")
java__LineComment = Class(name="java::::LineComment")
java__InstanceofExpression = Class(name="java::::InstanceofExpression")
java__InterfaceDeclaration = Class(name="java::::InterfaceDeclaration")
java__Javadoc = Class(name="java::::Javadoc")
java__TagElement = Class(name="java::::TagElement")
java__MethodDeclaration = Class(name="java::::MethodDeclaration")
java__ManifestAttribute = Class(name="java::::ManifestAttribute")
java__ManifestEntry = Class(name="java::::ManifestEntry")
java__MemberRef = Class(name="java::::MemberRef")
java__MethodRefParameter = Class(name="java::::MethodRefParameter")
java__MethodInvocation = Class(name="java::::MethodInvocation")
java__Model = Class(name="java::::Model")
java__Type = Class(name="java::::Type", is_abstract=True)
java__UnresolvedItem = Class(name="java::::UnresolvedItem")
java__VariableDeclarationStatement = Class(name="java::::VariableDeclarationStatement")
java__VariableDeclarationExpression = Class(name="java::::VariableDeclarationExpression")
java__NamespaceAccess = Class(name="java::::NamespaceAccess", is_abstract=True)
java__NumberLiteral = Class(name="java::::NumberLiteral")
java__NullLiteral = Class(name="java::::NullLiteral")
java__ParenthesizedExpression = Class(name="java::::ParenthesizedExpression")
java__PackageAccess = Class(name="java::::PackageAccess")
NamespaceAccess = Class(name="NamespaceAccess")
java__ParameterizedType = Class(name="java::::ParameterizedType")
java__PostfixExpression = Class(name="java::::PostfixExpression")
java__PrefixExpression = Class(name="java::::PrefixExpression")
java__PrimitiveType = Class(name="java::::PrimitiveType")
java__PrimitiveTypeBoolean = Class(name="java::::PrimitiveTypeBoolean")
PrimitiveType = Class(name="PrimitiveType")
java__PrimitiveTypeByte = Class(name="java::::PrimitiveTypeByte")
java__PrimitiveTypeChar = Class(name="java::::PrimitiveTypeChar")
java__PrimitiveTypeDouble = Class(name="java::::PrimitiveTypeDouble")
java__PrimitiveTypeShort = Class(name="java::::PrimitiveTypeShort")
java__PrimitiveTypeFloat = Class(name="java::::PrimitiveTypeFloat")
java__PrimitiveTypeInt = Class(name="java::::PrimitiveTypeInt")
java__PrimitiveTypeLong = Class(name="java::::PrimitiveTypeLong")
java__PrimitiveTypeVoid = Class(name="java::::PrimitiveTypeVoid")
java__ReturnStatement = Class(name="java::::ReturnStatement")
java__VariableDeclaration = Class(name="java::::VariableDeclaration", is_abstract=True)
java__StringLiteral = Class(name="java::::StringLiteral")
java__SuperConstructorInvocation = Class(name="java::::SuperConstructorInvocation")
java__SuperFieldAccess = Class(name="java::::SuperFieldAccess")
AbstractTypeQualifiedExpression = Class(name="AbstractTypeQualifiedExpression")
java__SuperMethodInvocation = Class(name="java::::SuperMethodInvocation")
java__TextElement = Class(name="java::::TextElement")
java__SwitchCase = Class(name="java::::SwitchCase")
java__SwitchStatement = Class(name="java::::SwitchStatement")
java__SynchronizedStatement = Class(name="java::::SynchronizedStatement")
java__ThisExpression = Class(name="java::::ThisExpression")
java__ThrowStatement = Class(name="java::::ThrowStatement")
java__TryStatement = Class(name="java::::TryStatement")
java__TypeDeclarationStatement = Class(name="java::::TypeDeclarationStatement")
java__TypeDeclaration = Class(name="java::::TypeDeclaration", is_abstract=True)
java__UnresolvedAnnotationDeclaration = Class(name="java::::UnresolvedAnnotationDeclaration")
AnnotationTypeDeclaration = Class(name="AnnotationTypeDeclaration")
UnresolvedItem = Class(name="UnresolvedItem")
java__UnresolvedAnnotationTypeMemberDeclaration = Class(name="java::::UnresolvedAnnotationTypeMemberDeclaration")
AnnotationTypeMemberDeclaration = Class(name="AnnotationTypeMemberDeclaration")
java__UnresolvedClassDeclaration = Class(name="java::::UnresolvedClassDeclaration")
ClassDeclaration = Class(name="ClassDeclaration")
java__TypeLiteral = Class(name="java::::TypeLiteral")
java__UnresolvedItemAccess = Class(name="java::::UnresolvedItemAccess")
java__UnresolvedEnumDeclaration = Class(name="java::::UnresolvedEnumDeclaration")
EnumDeclaration = Class(name="EnumDeclaration")
java__UnresolvedInterfaceDeclaration = Class(name="java::::UnresolvedInterfaceDeclaration")
InterfaceDeclaration = Class(name="InterfaceDeclaration")
java__UnresolvedLabeledStatement = Class(name="java::::UnresolvedLabeledStatement")
LabeledStatement = Class(name="LabeledStatement")
java__UnresolvedMethodDeclaration = Class(name="java::::UnresolvedMethodDeclaration")
MethodDeclaration = Class(name="MethodDeclaration")
java__UnresolvedSingleVariableDeclaration = Class(name="java::::UnresolvedSingleVariableDeclaration")
SingleVariableDeclaration = Class(name="SingleVariableDeclaration")
java__UnresolvedType = Class(name="java::::UnresolvedType")
java__UnresolvedTypeDeclaration = Class(name="java::::UnresolvedTypeDeclaration")
java__UnresolvedVariableDeclarationFragment = Class(name="java::::UnresolvedVariableDeclarationFragment")
VariableDeclarationFragment = Class(name="VariableDeclarationFragment")
java__WildCardType = Class(name="java::::WildCardType")
java__WhileStatement = Class(name="java::::WhileStatement")
java__Test = Class(name="java::::Test")

# BodyDeclaration class attributes and methods

# java__Block class attributes and methods

# java__SingleVariableDeclaration class attributes and methods
java__SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=BooleanType)
java__SingleVariableDeclaration.attributes={java__SingleVariableDeclaration_varargs}

# java__TypeAccess class attributes and methods

# java__AbstractMethodDeclaration class attributes and methods

# java__AbstractMethodInvocation class attributes and methods

# ASTNode class attributes and methods

# java__Expression class attributes and methods

# java__TypeParameter class attributes and methods

# java__MethodRef class attributes and methods

# java__Package class attributes and methods

# java__AbstractTypeQualifiedExpression class attributes and methods

# Expression class attributes and methods

# java__AbstractVariablesContainer class attributes and methods

# java__AbstractTypeDeclaration class attributes and methods

# Type class attributes and methods

# java__BodyDeclaration class attributes and methods

# java__Comment class attributes and methods
java__Comment_content: Property = Property(name="content", type=StringType)
java__Comment_enclosedByParent: Property = Property(name="enclosedByParent", type=BooleanType)
java__Comment_prefixOfParent: Property = Property(name="prefixOfParent", type=BooleanType)
java__Comment.attributes={java__Comment_content, java__Comment_enclosedByParent, java__Comment_prefixOfParent}

# java__AnnotationMemberValuePair class attributes and methods

# java__Archive class attributes and methods
java__Archive_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java__Archive.attributes={java__Archive_originalFilePath}

# NamedElement class attributes and methods

# java__ClassFile class attributes and methods
java__ClassFile_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java__ClassFile.attributes={java__ClassFile_originalFilePath}

# java__Manifest class attributes and methods

# java__AssertStatement class attributes and methods

# Statement class attributes and methods

# java__VariableDeclarationFragment class attributes and methods

# java__Annotation class attributes and methods

# java__CompilationUnit class attributes and methods
java__CompilationUnit_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java__CompilationUnit.attributes={java__CompilationUnit_originalFilePath}

# java__AnnotationTypeMemberDeclaration class attributes and methods

# java__AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# java__ASTNode class attributes and methods

# java__AnonymousClassDeclaration class attributes and methods

# java__ClassInstanceCreation class attributes and methods

# java__ArrayAccess class attributes and methods

# java__ArrayInitializer class attributes and methods

# java__ArrayLengthAccess class attributes and methods

# java__ArrayCreation class attributes and methods

# java__Assignment class attributes and methods
java__Assignment_operator: Property = Property(name="operator", type=StringType)
java__Assignment.attributes={java__Assignment_operator}

# java__ArrayType class attributes and methods
java__ArrayType_dimensions: Property = Property(name="dimensions", type=IntegerType)
java__ArrayType.attributes={java__ArrayType_dimensions}

# java__Modifier class attributes and methods
java__Modifier_visibility: Property = Property(name="visibility", type=StringType)
java__Modifier_inheritance: Property = Property(name="inheritance", type=StringType)
java__Modifier_static: Property = Property(name="static", type=BooleanType)
java__Modifier_transient: Property = Property(name="transient", type=BooleanType)
java__Modifier_volatile: Property = Property(name="volatile", type=BooleanType)
java__Modifier_native: Property = Property(name="native", type=BooleanType)
java__Modifier_strictfp: Property = Property(name="strictfp", type=BooleanType)
java__Modifier_synchronized: Property = Property(name="synchronized", type=BooleanType)
java__Modifier.attributes={java__Modifier_native, java__Modifier_static, java__Modifier_visibility, java__Modifier_transient, java__Modifier_strictfp, java__Modifier_inheritance, java__Modifier_volatile, java__Modifier_synchronized}

# java__BooleanLiteral class attributes and methods
java__BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
java__BooleanLiteral.attributes={java__BooleanLiteral_value}

# java__BlockComment class attributes and methods

# Comment class attributes and methods

# java__CastExpression class attributes and methods

# java__CatchClause class attributes and methods

# java__CharacterLiteral class attributes and methods
java__CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
java__CharacterLiteral.attributes={java__CharacterLiteral_escapedValue}

# java__Statement class attributes and methods

# java__BreakStatement class attributes and methods

# java__LabeledStatement class attributes and methods

# AbstractMethodInvocation class attributes and methods

# java__ConstructorDeclaration class attributes and methods

# AbstractMethodDeclaration class attributes and methods

# java__ConstructorInvocation class attributes and methods

# java__ClassDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# java__ConditionalExpression class attributes and methods

# java__ImportDeclaration class attributes and methods
java__ImportDeclaration_static: Property = Property(name="static", type=BooleanType)
java__ImportDeclaration.attributes={java__ImportDeclaration_static}

# java__ContinueStatement class attributes and methods

# java__DoStatement class attributes and methods

# java__EmptyStatement class attributes and methods

# java__EnhancedForStatement class attributes and methods

# java__EnumConstantDeclaration class attributes and methods

# VariableDeclaration class attributes and methods

# java__EnumDeclaration class attributes and methods

# java__ExpressionStatement class attributes and methods

# java__FieldAccess class attributes and methods

# java__SingleVariableAccess class attributes and methods

# java__IfStatement class attributes and methods

# java__FieldDeclaration class attributes and methods

# AbstractVariablesContainer class attributes and methods

# java__ForStatement class attributes and methods

# java__NamedElement class attributes and methods
java__NamedElement_name: Property = Property(name="name", type=StringType)
java__NamedElement_proxy: Property = Property(name="proxy", type=BooleanType)
java__NamedElement.attributes={java__NamedElement_proxy, java__NamedElement_name}

# java__InfixExpression class attributes and methods
java__InfixExpression_operator: Property = Property(name="operator", type=StringType)
java__InfixExpression.attributes={java__InfixExpression_operator}

# java__Initializer class attributes and methods

# java__LineComment class attributes and methods

# java__InstanceofExpression class attributes and methods

# java__InterfaceDeclaration class attributes and methods

# java__Javadoc class attributes and methods

# java__TagElement class attributes and methods
java__TagElement_tagName: Property = Property(name="tagName", type=StringType)
java__TagElement.attributes={java__TagElement_tagName}

# java__MethodDeclaration class attributes and methods
java__MethodDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
java__MethodDeclaration.attributes={java__MethodDeclaration_extraArrayDimensions}

# java__ManifestAttribute class attributes and methods
java__ManifestAttribute_key: Property = Property(name="key", type=StringType)
java__ManifestAttribute_value: Property = Property(name="value", type=StringType)
java__ManifestAttribute.attributes={java__ManifestAttribute_value, java__ManifestAttribute_key}

# java__ManifestEntry class attributes and methods
java__ManifestEntry_name: Property = Property(name="name", type=StringType)
java__ManifestEntry.attributes={java__ManifestEntry_name}

# java__MemberRef class attributes and methods

# java__MethodRefParameter class attributes and methods
java__MethodRefParameter_name: Property = Property(name="name", type=StringType)
java__MethodRefParameter_varargs: Property = Property(name="varargs", type=BooleanType)
java__MethodRefParameter.attributes={java__MethodRefParameter_varargs, java__MethodRefParameter_name}

# java__MethodInvocation class attributes and methods

# java__Model class attributes and methods
java__Model_name: Property = Property(name="name", type=StringType)
java__Model.attributes={java__Model_name}

# java__Type class attributes and methods

# java__UnresolvedItem class attributes and methods

# java__VariableDeclarationStatement class attributes and methods
java__VariableDeclarationStatement_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
java__VariableDeclarationStatement.attributes={java__VariableDeclarationStatement_extraArrayDimensions}

# java__VariableDeclarationExpression class attributes and methods

# java__NamespaceAccess class attributes and methods

# java__NumberLiteral class attributes and methods
java__NumberLiteral_tokenValue: Property = Property(name="tokenValue", type=StringType)
java__NumberLiteral.attributes={java__NumberLiteral_tokenValue}

# java__NullLiteral class attributes and methods

# java__ParenthesizedExpression class attributes and methods

# java__PackageAccess class attributes and methods

# NamespaceAccess class attributes and methods

# java__ParameterizedType class attributes and methods

# java__PostfixExpression class attributes and methods
java__PostfixExpression_operator: Property = Property(name="operator", type=StringType)
java__PostfixExpression.attributes={java__PostfixExpression_operator}

# java__PrefixExpression class attributes and methods
java__PrefixExpression_operator: Property = Property(name="operator", type=StringType)
java__PrefixExpression.attributes={java__PrefixExpression_operator}

# java__PrimitiveType class attributes and methods

# java__PrimitiveTypeBoolean class attributes and methods

# PrimitiveType class attributes and methods

# java__PrimitiveTypeByte class attributes and methods

# java__PrimitiveTypeChar class attributes and methods

# java__PrimitiveTypeDouble class attributes and methods

# java__PrimitiveTypeShort class attributes and methods

# java__PrimitiveTypeFloat class attributes and methods

# java__PrimitiveTypeInt class attributes and methods

# java__PrimitiveTypeLong class attributes and methods

# java__PrimitiveTypeVoid class attributes and methods

# java__ReturnStatement class attributes and methods

# java__VariableDeclaration class attributes and methods
java__VariableDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
java__VariableDeclaration.attributes={java__VariableDeclaration_extraArrayDimensions}

# java__StringLiteral class attributes and methods
java__StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
java__StringLiteral.attributes={java__StringLiteral_escapedValue}

# java__SuperConstructorInvocation class attributes and methods

# java__SuperFieldAccess class attributes and methods

# AbstractTypeQualifiedExpression class attributes and methods

# java__SuperMethodInvocation class attributes and methods

# java__TextElement class attributes and methods
java__TextElement_text: Property = Property(name="text", type=StringType)
java__TextElement.attributes={java__TextElement_text}

# java__SwitchCase class attributes and methods
java__SwitchCase_default: Property = Property(name="default", type=BooleanType)
java__SwitchCase.attributes={java__SwitchCase_default}

# java__SwitchStatement class attributes and methods

# java__SynchronizedStatement class attributes and methods

# java__ThisExpression class attributes and methods

# java__ThrowStatement class attributes and methods

# java__TryStatement class attributes and methods

# java__TypeDeclarationStatement class attributes and methods

# java__TypeDeclaration class attributes and methods

# java__UnresolvedAnnotationDeclaration class attributes and methods

# AnnotationTypeDeclaration class attributes and methods

# UnresolvedItem class attributes and methods

# java__UnresolvedAnnotationTypeMemberDeclaration class attributes and methods

# AnnotationTypeMemberDeclaration class attributes and methods

# java__UnresolvedClassDeclaration class attributes and methods

# ClassDeclaration class attributes and methods

# java__TypeLiteral class attributes and methods

# java__UnresolvedItemAccess class attributes and methods

# java__UnresolvedEnumDeclaration class attributes and methods

# EnumDeclaration class attributes and methods

# java__UnresolvedInterfaceDeclaration class attributes and methods

# InterfaceDeclaration class attributes and methods

# java__UnresolvedLabeledStatement class attributes and methods

# LabeledStatement class attributes and methods

# java__UnresolvedMethodDeclaration class attributes and methods

# MethodDeclaration class attributes and methods

# java__UnresolvedSingleVariableDeclaration class attributes and methods

# SingleVariableDeclaration class attributes and methods

# java__UnresolvedType class attributes and methods

# java__UnresolvedTypeDeclaration class attributes and methods

# java__UnresolvedVariableDeclarationFragment class attributes and methods

# VariableDeclarationFragment class attributes and methods

# java__WildCardType class attributes and methods
java__WildCardType_upperBound: Property = Property(name="upperBound", type=BooleanType)
java__WildCardType.attributes={java__WildCardType_upperBound}

# java__WhileStatement class attributes and methods

# java__Test class attributes and methods
java__Test_m_thrownExceptions2: Method = Method(name="thrownExceptions2", parameters={}, type=BodyDeclaration)
java__Test.methods={java__Test_m_thrownExceptions2}

# Relationships
body0: BinaryAssociation = BinaryAssociation(
    name="body0",
    ends={
        Property(name="java__Block", type=java__AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AbstractMethodDeclaration", type=java__Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="SingleVariableDeclaration", type=java__AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methodDeclaration", type=java__SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usagesInDocComments6: BinaryAssociation = BinaryAssociation(
    name="usagesInDocComments6",
    ends={
        Property(name="method", type=java__MethodRef, multiplicity=Multiplicity(0, 9999)),
        Property(name="MethodRef", type=java__AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
usages7: BinaryAssociation = BinaryAssociation(
    name="usages7",
    ends={
        Property(name="AbstractMethodInvocation", type=java__AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="method8", type=java__AbstractMethodInvocation, multiplicity=Multiplicity(0, 9999))
    }
)
method9: BinaryAssociation = BinaryAssociation(
    name="method9",
    ends={
        Property(name="AbstractMethodDeclaration", type=java__AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="usages", type=java__AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
arguments10: BinaryAssociation = BinaryAssociation(
    name="arguments10",
    ends={
        Property(name="java__Expression", type=java__AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AbstractMethodInvocation", type=java__Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments11: BinaryAssociation = BinaryAssociation(
    name="typeArguments11",
    ends={
        Property(name="java__TypeAccess13", type=java__AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AbstractMethodInvocation12", type=java__TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thrownExceptions2: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions2",
    ends={
        Property(name="java__TypeAccess", type=java__AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AbstractMethodDeclaration3", type=java__TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters4: BinaryAssociation = BinaryAssociation(
    name="typeParameters4",
    ends={
        Property(name="java__TypeParameter", type=java__AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AbstractMethodDeclaration5", type=java__TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsAfterBody16: BinaryAssociation = BinaryAssociation(
    name="commentsAfterBody16",
    ends={
        Property(name="java__Comment18", type=java__AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AbstractTypeDeclaration17", type=java__Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package19: BinaryAssociation = BinaryAssociation(
    name="package19",
    ends={
        Property(name="Package", type=java__AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements", type=java__Package, multiplicity=Multiplicity(0, 1))
    }
)
superInterfaces20: BinaryAssociation = BinaryAssociation(
    name="superInterfaces20",
    ends={
        Property(name="java__TypeAccess22", type=java__AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AbstractTypeDeclaration21", type=java__TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier23: BinaryAssociation = BinaryAssociation(
    name="qualifier23",
    ends={
        Property(name="java__TypeAccess24", type=java__AbstractTypeQualifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AbstractTypeQualifiedExpression", type=java__TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="java__TypeAccess26", type=java__AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AbstractVariablesContainer", type=java__TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyDeclarations14: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations14",
    ends={
        Property(name="BodyDeclaration", type=java__AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractTypeDeclaration", type=java__BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsBeforeBody15: BinaryAssociation = BinaryAssociation(
    name="commentsBeforeBody15",
    ends={
        Property(name="java__Comment", type=java__AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AbstractTypeDeclaration", type=java__Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values30: BinaryAssociation = BinaryAssociation(
    name="values30",
    ends={
        Property(name="java__AnnotationMemberValuePair", type=java__Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Annotation31", type=java__AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classFiles32: BinaryAssociation = BinaryAssociation(
    name="classFiles32",
    ends={
        Property(name="java__ClassFile", type=java__Archive, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Archive", type=java__ClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifest33: BinaryAssociation = BinaryAssociation(
    name="manifest33",
    ends={
        Property(name="java__Manifest", type=java__Archive, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Archive34", type=java__Manifest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message35: BinaryAssociation = BinaryAssociation(
    name="message35",
    ends={
        Property(name="java__Expression36", type=java__AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AssertStatement", type=java__Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments27: BinaryAssociation = BinaryAssociation(
    name="fragments27",
    ends={
        Property(name="VariableDeclarationFragment", type=java__AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="variablesContainer", type=java__VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="java__TypeAccess29", type=java__Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Annotation", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
originalCompilationUnit42: BinaryAssociation = BinaryAssociation(
    name="originalCompilationUnit42",
    ends={
        Property(name="java__CompilationUnit", type=java__ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ASTNode43", type=java__CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
originalClassFile44: BinaryAssociation = BinaryAssociation(
    name="originalClassFile44",
    ends={
        Property(name="java__ClassFile46", type=java__ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ASTNode45", type=java__ClassFile, multiplicity=Multiplicity(0, 1))
    }
)
member47: BinaryAssociation = BinaryAssociation(
    name="member47",
    ends={
        Property(name="AnnotationTypeMemberDeclaration", type=java__AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="usages48", type=java__AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
value49: BinaryAssociation = BinaryAssociation(
    name="value49",
    ends={
        Property(name="java__Expression51", type=java__AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AnnotationMemberValuePair50", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression37: BinaryAssociation = BinaryAssociation(
    name="expression37",
    ends={
        Property(name="java__Expression39", type=java__AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AssertStatement38", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comments40: BinaryAssociation = BinaryAssociation(
    name="comments40",
    ends={
        Property(name="java__Comment41", type=java__ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ASTNode", type=java__Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usages57: BinaryAssociation = BinaryAssociation(
    name="usages57",
    ends={
        Property(name="AnnotationMemberValuePair", type=java__AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="member", type=java__AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999))
    }
)
bodyDeclarations58: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations58",
    ends={
        Property(name="BodyDeclaration59", type=java__AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclarationOwner", type=java__BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classInstanceCreation60: BinaryAssociation = BinaryAssociation(
    name="classInstanceCreation60",
    ends={
        Property(name="ClassInstanceCreation", type=java__AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclaration", type=java__ClassInstanceCreation, multiplicity=Multiplicity(0, 1))
    }
)
default52: BinaryAssociation = BinaryAssociation(
    name="default52",
    ends={
        Property(name="java__Expression53", type=java__AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AnnotationTypeMemberDeclaration", type=java__Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="java__TypeAccess56", type=java__AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__AnnotationTypeMemberDeclaration55", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions66: BinaryAssociation = BinaryAssociation(
    name="dimensions66",
    ends={
        Property(name="java__Expression67", type=java__ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ArrayCreation", type=java__Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer68: BinaryAssociation = BinaryAssociation(
    name="initializer68",
    ends={
        Property(name="java__ArrayInitializer", type=java__ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ArrayCreation69", type=java__ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="java__TypeAccess72", type=java__ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ArrayCreation71", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions73: BinaryAssociation = BinaryAssociation(
    name="expressions73",
    ends={
        Property(name="java__Expression75", type=java__ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ArrayInitializer74", type=java__Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
array61: BinaryAssociation = BinaryAssociation(
    name="array61",
    ends={
        Property(name="java__Expression62", type=java__ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ArrayAccess", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index63: BinaryAssociation = BinaryAssociation(
    name="index63",
    ends={
        Property(name="java__Expression65", type=java__ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ArrayAccess64", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType78: BinaryAssociation = BinaryAssociation(
    name="elementType78",
    ends={
        Property(name="java__ArrayType", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="java__TypeAccess79", type=java__ArrayType, multiplicity=Multiplicity(1, 1))
    }
)
leftHandSide80: BinaryAssociation = BinaryAssociation(
    name="leftHandSide80",
    ends={
        Property(name="java__Expression81", type=java__Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Assignment", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide82: BinaryAssociation = BinaryAssociation(
    name="rightHandSide82",
    ends={
        Property(name="java__Expression84", type=java__Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Assignment83", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array76: BinaryAssociation = BinaryAssociation(
    name="array76",
    ends={
        Property(name="java__Expression77", type=java__ArrayLengthAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ArrayLengthAccess", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
abstractTypeDeclaration85: BinaryAssociation = BinaryAssociation(
    name="abstractTypeDeclaration85",
    ends={
        Property(name="AbstractTypeDeclaration", type=java__BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations", type=java__AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
annotations86: BinaryAssociation = BinaryAssociation(
    name="annotations86",
    ends={
        Property(name="java__Annotation87", type=java__BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__BodyDeclaration", type=java__Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclarationOwner88: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclarationOwner88",
    ends={
        Property(name="AnonymousClassDeclaration", type=java__BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations89", type=java__AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
modifier90: BinaryAssociation = BinaryAssociation(
    name="modifier90",
    ends={
        Property(name="Modifier", type=java__BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclaration", type=java__Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression94: BinaryAssociation = BinaryAssociation(
    name="expression94",
    ends={
        Property(name="java__Expression95", type=java__CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__CastExpression", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type96: BinaryAssociation = BinaryAssociation(
    name="type96",
    ends={
        Property(name="java__TypeAccess98", type=java__CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__CastExpression97", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception99: BinaryAssociation = BinaryAssociation(
    name="exception99",
    ends={
        Property(name="SingleVariableDeclaration100", type=java__CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="catchClause", type=java__SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body101: BinaryAssociation = BinaryAssociation(
    name="body101",
    ends={
        Property(name="java__Block102", type=java__CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="java__CatchClause", type=java__Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements91: BinaryAssociation = BinaryAssociation(
    name="statements91",
    ends={
        Property(name="java__Statement", type=java__Block, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Block92", type=java__Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label93: BinaryAssociation = BinaryAssociation(
    name="label93",
    ends={
        Property(name="LabeledStatement", type=java__BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInBreakStatements", type=java__LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
package109: BinaryAssociation = BinaryAssociation(
    name="package109",
    ends={
        Property(name="java__Package", type=java__ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ClassFile110", type=java__Package, multiplicity=Multiplicity(0, 1))
    }
)
anonymousClassDeclaration111: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration111",
    ends={
        Property(name="AnonymousClassDeclaration112", type=java__ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="classInstanceCreation", type=java__AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression113: BinaryAssociation = BinaryAssociation(
    name="expression113",
    ends={
        Property(name="java__Expression114", type=java__ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ClassInstanceCreation", type=java__Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type115: BinaryAssociation = BinaryAssociation(
    name="type115",
    ends={
        Property(name="java__TypeAccess117", type=java__ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ClassInstanceCreation116", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="java__AbstractTypeDeclaration105", type=java__ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ClassFile104", type=java__AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
attachedSource106: BinaryAssociation = BinaryAssociation(
    name="attachedSource106",
    ends={
        Property(name="java__CompilationUnit108", type=java__ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ClassFile107", type=java__CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
package133: BinaryAssociation = BinaryAssociation(
    name="package133",
    ends={
        Property(name="java__CompilationUnit134", type=java__Package, multiplicity=Multiplicity(0, 1)),
        Property(name="java__Package135", type=java__CompilationUnit, multiplicity=Multiplicity(1, 1))
    }
)
thenExpression123: BinaryAssociation = BinaryAssociation(
    name="thenExpression123",
    ends={
        Property(name="java__Expression125", type=java__ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ConditionalExpression124", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superClass126: BinaryAssociation = BinaryAssociation(
    name="superClass126",
    ends={
        Property(name="java__TypeAccess127", type=java__ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ClassDeclaration", type=java__TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression118: BinaryAssociation = BinaryAssociation(
    name="elseExpression118",
    ends={
        Property(name="java__Expression119", type=java__ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ConditionalExpression", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
commentList128: BinaryAssociation = BinaryAssociation(
    name="commentList128",
    ends={
        Property(name="java__Comment130", type=java__CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java__CompilationUnit129", type=java__Comment, multiplicity=Multiplicity(0, 9999))
    }
)
expression120: BinaryAssociation = BinaryAssociation(
    name="expression120",
    ends={
        Property(name="java__Expression122", type=java__ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ConditionalExpression121", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imports131: BinaryAssociation = BinaryAssociation(
    name="imports131",
    ends={
        Property(name="java__ImportDeclaration", type=java__CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java__CompilationUnit132", type=java__ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter151: BinaryAssociation = BinaryAssociation(
    name="parameter151",
    ends={
        Property(name="SingleVariableDeclaration152", type=java__EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="enhancedForStatement", type=java__SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types136: BinaryAssociation = BinaryAssociation(
    name="types136",
    ends={
        Property(name="java__AbstractTypeDeclaration138", type=java__CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java__CompilationUnit137", type=java__AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
label139: BinaryAssociation = BinaryAssociation(
    name="label139",
    ends={
        Property(name="LabeledStatement140", type=java__ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInContinueStatements", type=java__LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
expression141: BinaryAssociation = BinaryAssociation(
    name="expression141",
    ends={
        Property(name="java__Expression142", type=java__DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__DoStatement", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body143: BinaryAssociation = BinaryAssociation(
    name="body143",
    ends={
        Property(name="java__Statement145", type=java__DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__DoStatement144", type=java__Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body146: BinaryAssociation = BinaryAssociation(
    name="body146",
    ends={
        Property(name="java__Statement147", type=java__EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__EnhancedForStatement", type=java__Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression148: BinaryAssociation = BinaryAssociation(
    name="expression148",
    ends={
        Property(name="java__Expression150", type=java__EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__EnhancedForStatement149", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
field161: BinaryAssociation = BinaryAssociation(
    name="field161",
    ends={
        Property(name="java__SingleVariableAccess", type=java__FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__FieldAccess", type=java__SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anonymousClassDeclaration153: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration153",
    ends={
        Property(name="java__AnonymousClassDeclaration", type=java__EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__EnumConstantDeclaration", type=java__AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments154: BinaryAssociation = BinaryAssociation(
    name="arguments154",
    ends={
        Property(name="java__Expression156", type=java__EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__EnumConstantDeclaration155", type=java__Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumConstants157: BinaryAssociation = BinaryAssociation(
    name="enumConstants157",
    ends={
        Property(name="java__EnumConstantDeclaration158", type=java__EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__EnumDeclaration", type=java__EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression159: BinaryAssociation = BinaryAssociation(
    name="expression159",
    ends={
        Property(name="java__Expression160", type=java__ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ExpressionStatement", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression162: BinaryAssociation = BinaryAssociation(
    name="expression162",
    ends={
        Property(name="java__Expression164", type=java__FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__FieldAccess163", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression165: BinaryAssociation = BinaryAssociation(
    name="expression165",
    ends={
        Property(name="java__Expression166", type=java__ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ForStatement", type=java__Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updaters167: BinaryAssociation = BinaryAssociation(
    name="updaters167",
    ends={
        Property(name="java__Expression169", type=java__ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ForStatement168", type=java__Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializers170: BinaryAssociation = BinaryAssociation(
    name="initializers170",
    ends={
        Property(name="java__Expression172", type=java__ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ForStatement171", type=java__Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body173: BinaryAssociation = BinaryAssociation(
    name="body173",
    ends={
        Property(name="java__Statement175", type=java__ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ForStatement174", type=java__Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand187: BinaryAssociation = BinaryAssociation(
    name="leftOperand187",
    ends={
        Property(name="java__Expression189", type=java__InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__InfixExpression188", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression176: BinaryAssociation = BinaryAssociation(
    name="expression176",
    ends={
        Property(name="java__Expression177", type=java__IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__IfStatement", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement178: BinaryAssociation = BinaryAssociation(
    name="thenStatement178",
    ends={
        Property(name="java__Statement180", type=java__IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__IfStatement179", type=java__Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement181: BinaryAssociation = BinaryAssociation(
    name="elseStatement181",
    ends={
        Property(name="java__Statement183", type=java__IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__IfStatement182", type=java__Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedElement184: BinaryAssociation = BinaryAssociation(
    name="importedElement184",
    ends={
        Property(name="NamedElement", type=java__ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInImports", type=java__NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand185: BinaryAssociation = BinaryAssociation(
    name="rightOperand185",
    ends={
        Property(name="java__Expression186", type=java__InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__InfixExpression", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands190: BinaryAssociation = BinaryAssociation(
    name="extendedOperands190",
    ends={
        Property(name="java__Expression192", type=java__InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__InfixExpression191", type=java__Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usagesInContinueStatements204: BinaryAssociation = BinaryAssociation(
    name="usagesInContinueStatements204",
    ends={
        Property(name="ContinueStatement", type=java__LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="label205", type=java__ContinueStatement, multiplicity=Multiplicity(0, 9999))
    }
)
body193: BinaryAssociation = BinaryAssociation(
    name="body193",
    ends={
        Property(name="java__Block194", type=java__Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Initializer", type=java__Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand195: BinaryAssociation = BinaryAssociation(
    name="rightOperand195",
    ends={
        Property(name="java__TypeAccess196", type=java__InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__InstanceofExpression", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand197: BinaryAssociation = BinaryAssociation(
    name="leftOperand197",
    ends={
        Property(name="java__Expression199", type=java__InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__InstanceofExpression198", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tags200: BinaryAssociation = BinaryAssociation(
    name="tags200",
    ends={
        Property(name="java__TagElement", type=java__Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Javadoc", type=java__TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body201: BinaryAssociation = BinaryAssociation(
    name="body201",
    ends={
        Property(name="java__Statement202", type=java__LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__LabeledStatement", type=java__Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usagesInBreakStatements203: BinaryAssociation = BinaryAssociation(
    name="usagesInBreakStatements203",
    ends={
        Property(name="BreakStatement", type=java__LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=java__BreakStatement, multiplicity=Multiplicity(0, 9999))
    }
)
qualifier214: BinaryAssociation = BinaryAssociation(
    name="qualifier214",
    ends={
        Property(name="java__TypeAccess216", type=java__MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java__MemberRef215", type=java__TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mainAttributes206: BinaryAssociation = BinaryAssociation(
    name="mainAttributes206",
    ends={
        Property(name="java__ManifestAttribute", type=java__Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Manifest207", type=java__ManifestAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryAttributes208: BinaryAssociation = BinaryAssociation(
    name="entryAttributes208",
    ends={
        Property(name="java__ManifestEntry", type=java__Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Manifest209", type=java__ManifestEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes210: BinaryAssociation = BinaryAssociation(
    name="attributes210",
    ends={
        Property(name="java__ManifestAttribute212", type=java__ManifestEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ManifestEntry211", type=java__ManifestAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member213: BinaryAssociation = BinaryAssociation(
    name="member213",
    ends={
        Property(name="java__NamedElement", type=java__MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java__MemberRef", type=java__NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
qualifier228: BinaryAssociation = BinaryAssociation(
    name="qualifier228",
    ends={
        Property(name="java__TypeAccess229", type=java__MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java__MethodRef", type=java__TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters230: BinaryAssociation = BinaryAssociation(
    name="parameters230",
    ends={
        Property(name="java__MethodRefParameter", type=java__MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java__MethodRef231", type=java__MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType217: BinaryAssociation = BinaryAssociation(
    name="returnType217",
    ends={
        Property(name="java__TypeAccess218", type=java__MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__MethodDeclaration", type=java__TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedMethodDeclaration220: BinaryAssociation = BinaryAssociation(
    name="redefinedMethodDeclaration220",
    ends={
        Property(name="MethodDeclaration", type=java__MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinitions", type=java__MethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
redefinitions222: BinaryAssociation = BinaryAssociation(
    name="redefinitions222",
    ends={
        Property(name="MethodDeclaration223", type=java__MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinedMethodDeclaration", type=java__MethodDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
expression224: BinaryAssociation = BinaryAssociation(
    name="expression224",
    ends={
        Property(name="java__Expression225", type=java__MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__MethodInvocation", type=java__Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method226: BinaryAssociation = BinaryAssociation(
    name="method226",
    ends={
        Property(name="AbstractMethodDeclaration227", type=java__MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInDocComments", type=java__AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
compilationUnits240: BinaryAssociation = BinaryAssociation(
    name="compilationUnits240",
    ends={
        Property(name="java__CompilationUnit242", type=java__Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Model241", type=java__CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classFiles243: BinaryAssociation = BinaryAssociation(
    name="classFiles243",
    ends={
        Property(name="java__ClassFile245", type=java__Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Model244", type=java__ClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type232: BinaryAssociation = BinaryAssociation(
    name="type232",
    ends={
        Property(name="java__TypeAccess234", type=java__MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="java__MethodRefParameter233", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedElements235: BinaryAssociation = BinaryAssociation(
    name="ownedElements235",
    ends={
        Property(name="Package236", type=java__Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=java__Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orphanTypes237: BinaryAssociation = BinaryAssociation(
    name="orphanTypes237",
    ends={
        Property(name="java__Type", type=java__Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Model", type=java__Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unresolvedItems238: BinaryAssociation = BinaryAssociation(
    name="unresolvedItems238",
    ends={
        Property(name="java__UnresolvedItem", type=java__Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Model239", type=java__UnresolvedItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
singleVariableDeclaration251: BinaryAssociation = BinaryAssociation(
    name="singleVariableDeclaration251",
    ends={
        Property(name="SingleVariableDeclaration253", type=java__Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier252", type=java__SingleVariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclarationStatement254: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationStatement254",
    ends={
        Property(name="VariableDeclarationStatement", type=java__Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier255", type=java__VariableDeclarationStatement, multiplicity=Multiplicity(0, 1))
    }
)
archives246: BinaryAssociation = BinaryAssociation(
    name="archives246",
    ends={
        Property(name="java__Archive248", type=java__Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Model247", type=java__Archive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclaration249: BinaryAssociation = BinaryAssociation(
    name="bodyDeclaration249",
    ends={
        Property(name="BodyDeclaration250", type=java__Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier", type=java__BodyDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ownedElements259: BinaryAssociation = BinaryAssociation(
    name="ownedElements259",
    ends={
        Property(name="AbstractTypeDeclaration260", type=java__Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=java__AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model261: BinaryAssociation = BinaryAssociation(
    name="model261",
    ends={
        Property(name="Model", type=java__Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements262", type=java__Model, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclarationExpression256: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationExpression256",
    ends={
        Property(name="VariableDeclarationExpression", type=java__Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier257", type=java__VariableDeclarationExpression, multiplicity=Multiplicity(0, 1))
    }
)
usagesInImports258: BinaryAssociation = BinaryAssociation(
    name="usagesInImports258",
    ends={
        Property(name="ImportDeclaration", type=java__NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="importedElement", type=java__ImportDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
typeArguments278: BinaryAssociation = BinaryAssociation(
    name="typeArguments278",
    ends={
        Property(name="java__TypeAccess280", type=java__ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ParameterizedType279", type=java__TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPackages264: BinaryAssociation = BinaryAssociation(
    name="ownedPackages264",
    ends={
        Property(name="Package266", type=java__Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package265", type=java__Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package268: BinaryAssociation = BinaryAssociation(
    name="package268",
    ends={
        Property(name="Package269", type=java__Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPackages", type=java__Package, multiplicity=Multiplicity(0, 1))
    }
)
usagesInPackageAccess270: BinaryAssociation = BinaryAssociation(
    name="usagesInPackageAccess270",
    ends={
        Property(name="PackageAccess", type=java__Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package271", type=java__PackageAccess, multiplicity=Multiplicity(0, 9999))
    }
)
package272: BinaryAssociation = BinaryAssociation(
    name="package272",
    ends={
        Property(name="Package273", type=java__PackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInPackageAccess", type=java__Package, multiplicity=Multiplicity(1, 1))
    }
)
qualifier275: BinaryAssociation = BinaryAssociation(
    name="qualifier275",
    ends={
        Property(name="java__PackageAccess", type=java__PackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__PackageAccess274", type=java__PackageAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type276: BinaryAssociation = BinaryAssociation(
    name="type276",
    ends={
        Property(name="java__TypeAccess277", type=java__ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ParameterizedType", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression281: BinaryAssociation = BinaryAssociation(
    name="expression281",
    ends={
        Property(name="java__Expression282", type=java__ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ParenthesizedExpression", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand283: BinaryAssociation = BinaryAssociation(
    name="operand283",
    ends={
        Property(name="java__Expression284", type=java__PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__PostfixExpression", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand285: BinaryAssociation = BinaryAssociation(
    name="operand285",
    ends={
        Property(name="java__Expression286", type=java__PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__PrefixExpression", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression287: BinaryAssociation = BinaryAssociation(
    name="expression287",
    ends={
        Property(name="java__Expression288", type=java__ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ReturnStatement", type=java__Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodDeclaration300: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration300",
    ends={
        Property(name="AbstractMethodDeclaration301", type=java__SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=java__AbstractMethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
catchClause302: BinaryAssociation = BinaryAssociation(
    name="catchClause302",
    ends={
        Property(name="CatchClause", type=java__SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="exception", type=java__CatchClause, multiplicity=Multiplicity(0, 1))
    }
)
variable289: BinaryAssociation = BinaryAssociation(
    name="variable289",
    ends={
        Property(name="VariableDeclaration", type=java__SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usageInVariableAccess", type=java__VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
qualifier290: BinaryAssociation = BinaryAssociation(
    name="qualifier290",
    ends={
        Property(name="java__Expression292", type=java__SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__SingleVariableAccess291", type=java__Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifier293: BinaryAssociation = BinaryAssociation(
    name="modifier293",
    ends={
        Property(name="Modifier294", type=java__SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="singleVariableDeclaration", type=java__Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type295: BinaryAssociation = BinaryAssociation(
    name="type295",
    ends={
        Property(name="java__TypeAccess296", type=java__SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__SingleVariableDeclaration", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations297: BinaryAssociation = BinaryAssociation(
    name="annotations297",
    ends={
        Property(name="java__Annotation299", type=java__SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__SingleVariableDeclaration298", type=java__Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enhancedForStatement303: BinaryAssociation = BinaryAssociation(
    name="enhancedForStatement303",
    ends={
        Property(name="EnhancedForStatement", type=java__SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=java__EnhancedForStatement, multiplicity=Multiplicity(0, 1))
    }
)
expression304: BinaryAssociation = BinaryAssociation(
    name="expression304",
    ends={
        Property(name="java__Expression305", type=java__SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java__SuperConstructorInvocation", type=java__Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field306: BinaryAssociation = BinaryAssociation(
    name="field306",
    ends={
        Property(name="java__SingleVariableAccess307", type=java__SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__SuperFieldAccess", type=java__SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments320: BinaryAssociation = BinaryAssociation(
    name="fragments320",
    ends={
        Property(name="java__ASTNode322", type=java__TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__TagElement321", type=java__ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression308: BinaryAssociation = BinaryAssociation(
    name="expression308",
    ends={
        Property(name="java__Expression309", type=java__SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="java__SwitchCase", type=java__Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression310: BinaryAssociation = BinaryAssociation(
    name="expression310",
    ends={
        Property(name="java__Expression311", type=java__SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__SwitchStatement", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements312: BinaryAssociation = BinaryAssociation(
    name="statements312",
    ends={
        Property(name="java__Statement314", type=java__SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__SwitchStatement313", type=java__Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body315: BinaryAssociation = BinaryAssociation(
    name="body315",
    ends={
        Property(name="java__Block316", type=java__SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__SynchronizedStatement", type=java__Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression317: BinaryAssociation = BinaryAssociation(
    name="expression317",
    ends={
        Property(name="java__Expression319", type=java__SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__SynchronizedStatement318", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catchClauses330: BinaryAssociation = BinaryAssociation(
    name="catchClauses330",
    ends={
        Property(name="java__CatchClause332", type=java__TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__TryStatement331", type=java__CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression323: BinaryAssociation = BinaryAssociation(
    name="expression323",
    ends={
        Property(name="java__Expression324", type=java__ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__ThrowStatement", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body325: BinaryAssociation = BinaryAssociation(
    name="body325",
    ends={
        Property(name="java__Block326", type=java__TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__TryStatement", type=java__Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally327: BinaryAssociation = BinaryAssociation(
    name="finally327",
    ends={
        Property(name="java__Block329", type=java__TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__TryStatement328", type=java__Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration339: BinaryAssociation = BinaryAssociation(
    name="declaration339",
    ends={
        Property(name="java__AbstractTypeDeclaration340", type=java__TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__TypeDeclarationStatement", type=java__AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usagesInTypeAccess333: BinaryAssociation = BinaryAssociation(
    name="usagesInTypeAccess333",
    ends={
        Property(name="TypeAccess", type=java__Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=java__TypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
type334: BinaryAssociation = BinaryAssociation(
    name="type334",
    ends={
        Property(name="Type", type=java__TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInTypeAccess", type=java__Type, multiplicity=Multiplicity(1, 1))
    }
)
qualifier335: BinaryAssociation = BinaryAssociation(
    name="qualifier335",
    ends={
        Property(name="java__NamespaceAccess", type=java__TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__TypeAccess336", type=java__NamespaceAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters337: BinaryAssociation = BinaryAssociation(
    name="typeParameters337",
    ends={
        Property(name="java__TypeParameter338", type=java__TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__TypeDeclaration", type=java__TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type341: BinaryAssociation = BinaryAssociation(
    name="type341",
    ends={
        Property(name="java__TypeAccess342", type=java__TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="java__TypeLiteral", type=java__TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bounds343: BinaryAssociation = BinaryAssociation(
    name="bounds343",
    ends={
        Property(name="java__TypeAccess345", type=java__TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="java__TypeParameter344", type=java__TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element346: BinaryAssociation = BinaryAssociation(
    name="element346",
    ends={
        Property(name="java__UnresolvedItem347", type=java__UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__UnresolvedItemAccess", type=java__UnresolvedItem, multiplicity=Multiplicity(0, 1))
    }
)
qualifier348: BinaryAssociation = BinaryAssociation(
    name="qualifier348",
    ends={
        Property(name="java__ASTNode350", type=java__UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java__UnresolvedItemAccess349", type=java__ASTNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifier354: BinaryAssociation = BinaryAssociation(
    name="modifier354",
    ends={
        Property(name="variableDeclarationExpression", type=java__Modifier, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Modifier355", type=java__VariableDeclarationExpression, multiplicity=Multiplicity(1, 1))
    }
)
annotations356: BinaryAssociation = BinaryAssociation(
    name="annotations356",
    ends={
        Property(name="java__Annotation357", type=java__VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java__VariableDeclarationExpression", type=java__Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variablesContainer358: BinaryAssociation = BinaryAssociation(
    name="variablesContainer358",
    ends={
        Property(name="AbstractVariablesContainer", type=java__VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=java__AbstractVariablesContainer, multiplicity=Multiplicity(0, 1))
    }
)
initializer351: BinaryAssociation = BinaryAssociation(
    name="initializer351",
    ends={
        Property(name="java__Expression352", type=java__VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java__VariableDeclaration", type=java__Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usageInVariableAccess353: BinaryAssociation = BinaryAssociation(
    name="usageInVariableAccess353",
    ends={
        Property(name="SingleVariableAccess", type=java__VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=java__SingleVariableAccess, multiplicity=Multiplicity(0, 9999))
    }
)
modifier359: BinaryAssociation = BinaryAssociation(
    name="modifier359",
    ends={
        Property(name="Modifier360", type=java__VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationStatement", type=java__Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations361: BinaryAssociation = BinaryAssociation(
    name="annotations361",
    ends={
        Property(name="java__Annotation362", type=java__VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__VariableDeclarationStatement", type=java__Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bound363: BinaryAssociation = BinaryAssociation(
    name="bound363",
    ends={
        Property(name="java__TypeAccess364", type=java__WildCardType, multiplicity=Multiplicity(1, 1)),
        Property(name="java__WildCardType", type=java__TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression365: BinaryAssociation = BinaryAssociation(
    name="expression365",
    ends={
        Property(name="java__Expression366", type=java__WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__WhileStatement", type=java__Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body367: BinaryAssociation = BinaryAssociation(
    name="body367",
    ends={
        Property(name="java__Statement369", type=java__WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java__WhileStatement368", type=java__Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thrownExceptions370: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions370",
    ends={
        Property(name="java__TypeAccess371", type=java__Test, multiplicity=Multiplicity(1, 1)),
        Property(name="java__Test", type=java__TypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_java__AbstractMethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java__AbstractMethodDeclaration)
gen_java__AbstractMethodInvocation_ASTNode = Generalization(general=ASTNode, specific=java__AbstractMethodInvocation)
gen_java__AbstractTypeQualifiedExpression_Expression = Generalization(general=Expression, specific=java__AbstractTypeQualifiedExpression)
gen_java__AbstractVariablesContainer_ASTNode = Generalization(general=ASTNode, specific=java__AbstractVariablesContainer)
gen_java__AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java__AbstractTypeDeclaration)
gen_java__AbstractTypeDeclaration_Type = Generalization(general=Type, specific=java__AbstractTypeDeclaration)
gen_java__Archive_NamedElement = Generalization(general=NamedElement, specific=java__Archive)
gen_java__AssertStatement_Statement = Generalization(general=Statement, specific=java__AssertStatement)
gen_java__Annotation_Expression = Generalization(general=Expression, specific=java__Annotation)
gen_java__AnnotationMemberValuePair_NamedElement = Generalization(general=NamedElement, specific=java__AnnotationMemberValuePair)
gen_java__AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java__AnnotationTypeDeclaration)
gen_java__AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=java__AnonymousClassDeclaration)
gen_java__ArrayAccess_Expression = Generalization(general=Expression, specific=java__ArrayAccess)
gen_java__AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java__AnnotationTypeMemberDeclaration)
gen_java__ArrayInitializer_Expression = Generalization(general=Expression, specific=java__ArrayInitializer)
gen_java__ArrayCreation_Expression = Generalization(general=Expression, specific=java__ArrayCreation)
gen_java__Assignment_Expression = Generalization(general=Expression, specific=java__Assignment)
gen_java__ArrayLengthAccess_Expression = Generalization(general=Expression, specific=java__ArrayLengthAccess)
gen_java__ArrayType_Type = Generalization(general=Type, specific=java__ArrayType)
gen_java__BooleanLiteral_Expression = Generalization(general=Expression, specific=java__BooleanLiteral)
gen_java__BlockComment_Comment = Generalization(general=Comment, specific=java__BlockComment)
gen_java__BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=java__BodyDeclaration)
gen_java__CastExpression_Expression = Generalization(general=Expression, specific=java__CastExpression)
gen_java__CatchClause_Statement = Generalization(general=Statement, specific=java__CatchClause)
gen_java__CharacterLiteral_Expression = Generalization(general=Expression, specific=java__CharacterLiteral)
gen_java__Block_Statement = Generalization(general=Statement, specific=java__Block)
gen_java__BreakStatement_Statement = Generalization(general=Statement, specific=java__BreakStatement)
gen_java__ClassInstanceCreation_Expression = Generalization(general=Expression, specific=java__ClassInstanceCreation)
gen_java__ClassInstanceCreation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java__ClassInstanceCreation)
gen_java__ConstructorDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=java__ConstructorDeclaration)
gen_java__ClassFile_NamedElement = Generalization(general=NamedElement, specific=java__ClassFile)
gen_java__ConstructorInvocation_Statement = Generalization(general=Statement, specific=java__ConstructorInvocation)
gen_java__ConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java__ConstructorInvocation)
gen_java__ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=java__ClassDeclaration)
gen_java__Comment_ASTNode = Generalization(general=ASTNode, specific=java__Comment)
gen_java__CompilationUnit_NamedElement = Generalization(general=NamedElement, specific=java__CompilationUnit)
gen_java__ConditionalExpression_Expression = Generalization(general=Expression, specific=java__ConditionalExpression)
gen_java__ContinueStatement_Statement = Generalization(general=Statement, specific=java__ContinueStatement)
gen_java__DoStatement_Statement = Generalization(general=Statement, specific=java__DoStatement)
gen_java__EmptyStatement_Statement = Generalization(general=Statement, specific=java__EmptyStatement)
gen_java__EnhancedForStatement_Statement = Generalization(general=Statement, specific=java__EnhancedForStatement)
gen_java__EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java__EnumConstantDeclaration)
gen_java__EnumConstantDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java__EnumConstantDeclaration)
gen_java__EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java__EnumDeclaration)
gen_java__Expression_ASTNode = Generalization(general=ASTNode, specific=java__Expression)
gen_java__ExpressionStatement_Statement = Generalization(general=Statement, specific=java__ExpressionStatement)
gen_java__FieldAccess_Expression = Generalization(general=Expression, specific=java__FieldAccess)
gen_java__IfStatement_Statement = Generalization(general=Statement, specific=java__IfStatement)
gen_java__FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java__FieldDeclaration)
gen_java__FieldDeclaration_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java__FieldDeclaration)
gen_java__ForStatement_Statement = Generalization(general=Statement, specific=java__ForStatement)
gen_java__ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=java__ImportDeclaration)
gen_java__InfixExpression_Expression = Generalization(general=Expression, specific=java__InfixExpression)
gen_java__Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java__Initializer)
gen_java__LineComment_Comment = Generalization(general=Comment, specific=java__LineComment)
gen_java__InstanceofExpression_Expression = Generalization(general=Expression, specific=java__InstanceofExpression)
gen_java__InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=java__InterfaceDeclaration)
gen_java__Javadoc_Comment = Generalization(general=Comment, specific=java__Javadoc)
gen_java__LabeledStatement_NamedElement = Generalization(general=NamedElement, specific=java__LabeledStatement)
gen_java__LabeledStatement_Statement = Generalization(general=Statement, specific=java__LabeledStatement)
gen_java__MethodDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=java__MethodDeclaration)
gen_java__MemberRef_ASTNode = Generalization(general=ASTNode, specific=java__MemberRef)
gen_java__MethodInvocation_Expression = Generalization(general=Expression, specific=java__MethodInvocation)
gen_java__MethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java__MethodInvocation)
gen_java__MethodRef_ASTNode = Generalization(general=ASTNode, specific=java__MethodRef)
gen_java__MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=java__MethodRefParameter)
gen_java__Modifier_ASTNode = Generalization(general=ASTNode, specific=java__Modifier)
gen_java__NamedElement_ASTNode = Generalization(general=ASTNode, specific=java__NamedElement)
gen_java__NamespaceAccess_ASTNode = Generalization(general=ASTNode, specific=java__NamespaceAccess)
gen_java__NumberLiteral_Expression = Generalization(general=Expression, specific=java__NumberLiteral)
gen_java__NullLiteral_Expression = Generalization(general=Expression, specific=java__NullLiteral)
gen_java__Package_NamedElement = Generalization(general=NamedElement, specific=java__Package)
gen_java__PackageAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java__PackageAccess)
gen_java__ParameterizedType_Type = Generalization(general=Type, specific=java__ParameterizedType)
gen_java__ParenthesizedExpression_Expression = Generalization(general=Expression, specific=java__ParenthesizedExpression)
gen_java__PostfixExpression_Expression = Generalization(general=Expression, specific=java__PostfixExpression)
gen_java__PrefixExpression_Expression = Generalization(general=Expression, specific=java__PrefixExpression)
gen_java__SingleVariableAccess_Expression = Generalization(general=Expression, specific=java__SingleVariableAccess)
gen_java__PrimitiveType_Type = Generalization(general=Type, specific=java__PrimitiveType)
gen_java__PrimitiveTypeBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=java__PrimitiveTypeBoolean)
gen_java__PrimitiveTypeByte_PrimitiveType = Generalization(general=PrimitiveType, specific=java__PrimitiveTypeByte)
gen_java__PrimitiveTypeChar_PrimitiveType = Generalization(general=PrimitiveType, specific=java__PrimitiveTypeChar)
gen_java__PrimitiveTypeDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=java__PrimitiveTypeDouble)
gen_java__PrimitiveTypeShort_PrimitiveType = Generalization(general=PrimitiveType, specific=java__PrimitiveTypeShort)
gen_java__PrimitiveTypeFloat_PrimitiveType = Generalization(general=PrimitiveType, specific=java__PrimitiveTypeFloat)
gen_java__PrimitiveTypeInt_PrimitiveType = Generalization(general=PrimitiveType, specific=java__PrimitiveTypeInt)
gen_java__PrimitiveTypeLong_PrimitiveType = Generalization(general=PrimitiveType, specific=java__PrimitiveTypeLong)
gen_java__PrimitiveTypeVoid_PrimitiveType = Generalization(general=PrimitiveType, specific=java__PrimitiveTypeVoid)
gen_java__ReturnStatement_Statement = Generalization(general=Statement, specific=java__ReturnStatement)
gen_java__SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java__SingleVariableDeclaration)
gen_java__SuperMethodInvocation_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java__SuperMethodInvocation)
gen_java__SuperMethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java__SuperMethodInvocation)
gen_java__Statement_ASTNode = Generalization(general=ASTNode, specific=java__Statement)
gen_java__StringLiteral_Expression = Generalization(general=Expression, specific=java__StringLiteral)
gen_java__SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=java__SuperConstructorInvocation)
gen_java__SuperConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java__SuperConstructorInvocation)
gen_java__SuperFieldAccess_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java__SuperFieldAccess)
gen_java__TextElement_ASTNode = Generalization(general=ASTNode, specific=java__TextElement)
gen_java__SwitchCase_Statement = Generalization(general=Statement, specific=java__SwitchCase)
gen_java__SwitchStatement_Statement = Generalization(general=Statement, specific=java__SwitchStatement)
gen_java__SynchronizedStatement_Statement = Generalization(general=Statement, specific=java__SynchronizedStatement)
gen_java__TagElement_ASTNode = Generalization(general=ASTNode, specific=java__TagElement)
gen_java__ThisExpression_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java__ThisExpression)
gen_java__ThrowStatement_Statement = Generalization(general=Statement, specific=java__ThrowStatement)
gen_java__TryStatement_Statement = Generalization(general=Statement, specific=java__TryStatement)
gen_java__TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=java__TypeDeclarationStatement)
gen_java__Type_NamedElement = Generalization(general=NamedElement, specific=java__Type)
gen_java__TypeAccess_Expression = Generalization(general=Expression, specific=java__TypeAccess)
gen_java__TypeAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java__TypeAccess)
gen_java__TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java__TypeDeclaration)
gen_java__UnresolvedAnnotationDeclaration_AnnotationTypeDeclaration = Generalization(general=AnnotationTypeDeclaration, specific=java__UnresolvedAnnotationDeclaration)
gen_java__UnresolvedAnnotationDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedAnnotationDeclaration)
gen_java__UnresolvedAnnotationTypeMemberDeclaration_AnnotationTypeMemberDeclaration = Generalization(general=AnnotationTypeMemberDeclaration, specific=java__UnresolvedAnnotationTypeMemberDeclaration)
gen_java__UnresolvedAnnotationTypeMemberDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedAnnotationTypeMemberDeclaration)
gen_java__UnresolvedClassDeclaration_ClassDeclaration = Generalization(general=ClassDeclaration, specific=java__UnresolvedClassDeclaration)
gen_java__TypeLiteral_Expression = Generalization(general=Expression, specific=java__TypeLiteral)
gen_java__TypeParameter_Type = Generalization(general=Type, specific=java__TypeParameter)
gen_java__UnresolvedItem_NamedElement = Generalization(general=NamedElement, specific=java__UnresolvedItem)
gen_java__UnresolvedItemAccess_Expression = Generalization(general=Expression, specific=java__UnresolvedItemAccess)
gen_java__UnresolvedItemAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java__UnresolvedItemAccess)
gen_java__VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java__VariableDeclarationFragment)
gen_java__VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=java__VariableDeclarationStatement)
gen_java__VariableDeclarationStatement_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java__VariableDeclarationStatement)
gen_java__UnresolvedClassDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedClassDeclaration)
gen_java__UnresolvedEnumDeclaration_EnumDeclaration = Generalization(general=EnumDeclaration, specific=java__UnresolvedEnumDeclaration)
gen_java__UnresolvedEnumDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedEnumDeclaration)
gen_java__UnresolvedInterfaceDeclaration_InterfaceDeclaration = Generalization(general=InterfaceDeclaration, specific=java__UnresolvedInterfaceDeclaration)
gen_java__UnresolvedInterfaceDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedInterfaceDeclaration)
gen_java__UnresolvedLabeledStatement_LabeledStatement = Generalization(general=LabeledStatement, specific=java__UnresolvedLabeledStatement)
gen_java__UnresolvedLabeledStatement_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedLabeledStatement)
gen_java__UnresolvedMethodDeclaration_MethodDeclaration = Generalization(general=MethodDeclaration, specific=java__UnresolvedMethodDeclaration)
gen_java__UnresolvedMethodDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedMethodDeclaration)
gen_java__UnresolvedSingleVariableDeclaration_SingleVariableDeclaration = Generalization(general=SingleVariableDeclaration, specific=java__UnresolvedSingleVariableDeclaration)
gen_java__UnresolvedSingleVariableDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedSingleVariableDeclaration)
gen_java__UnresolvedType_Type = Generalization(general=Type, specific=java__UnresolvedType)
gen_java__UnresolvedType_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedType)
gen_java__UnresolvedTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java__UnresolvedTypeDeclaration)
gen_java__UnresolvedTypeDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedTypeDeclaration)
gen_java__UnresolvedVariableDeclarationFragment_VariableDeclarationFragment = Generalization(general=VariableDeclarationFragment, specific=java__UnresolvedVariableDeclarationFragment)
gen_java__UnresolvedVariableDeclarationFragment_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java__UnresolvedVariableDeclarationFragment)
gen_java__VariableDeclaration_NamedElement = Generalization(general=NamedElement, specific=java__VariableDeclaration)
gen_java__VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=java__VariableDeclarationExpression)
gen_java__VariableDeclarationExpression_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java__VariableDeclarationExpression)
gen_java__WildCardType_Type = Generalization(general=Type, specific=java__WildCardType)
gen_java__WhileStatement_Statement = Generalization(general=Statement, specific=java__WhileStatement)

# Domain Model
domain_model = DomainModel(
    name="java_",
    types={BodyDeclaration, java__Block, java__SingleVariableDeclaration, java__TypeAccess, java__AbstractMethodDeclaration, java__AbstractMethodInvocation, ASTNode, java__Expression, java__TypeParameter, java__MethodRef, java__Package, java__AbstractTypeQualifiedExpression, Expression, java__AbstractVariablesContainer, java__AbstractTypeDeclaration, Type, java__BodyDeclaration, java__Comment, java__AnnotationMemberValuePair, java__Archive, NamedElement, java__ClassFile, java__Manifest, java__AssertStatement, Statement, java__VariableDeclarationFragment, java__Annotation, java__CompilationUnit, java__AnnotationTypeMemberDeclaration, java__AnnotationTypeDeclaration, AbstractTypeDeclaration, java__ASTNode, java__AnonymousClassDeclaration, java__ClassInstanceCreation, java__ArrayAccess, java__ArrayInitializer, java__ArrayLengthAccess, java__ArrayCreation, java__Assignment, java__ArrayType, java__Modifier, java__BooleanLiteral, java__BlockComment, Comment, java__CastExpression, java__CatchClause, java__CharacterLiteral, java__Statement, java__BreakStatement, java__LabeledStatement, AbstractMethodInvocation, java__ConstructorDeclaration, AbstractMethodDeclaration, java__ConstructorInvocation, java__ClassDeclaration, TypeDeclaration, java__ConditionalExpression, java__ImportDeclaration, java__ContinueStatement, java__DoStatement, java__EmptyStatement, java__EnhancedForStatement, java__EnumConstantDeclaration, VariableDeclaration, java__EnumDeclaration, java__ExpressionStatement, java__FieldAccess, java__SingleVariableAccess, java__IfStatement, java__FieldDeclaration, AbstractVariablesContainer, java__ForStatement, java__NamedElement, java__InfixExpression, java__Initializer, java__LineComment, java__InstanceofExpression, java__InterfaceDeclaration, java__Javadoc, java__TagElement, java__MethodDeclaration, java__ManifestAttribute, java__ManifestEntry, java__MemberRef, java__MethodRefParameter, java__MethodInvocation, java__Model, java__Type, java__UnresolvedItem, java__VariableDeclarationStatement, java__VariableDeclarationExpression, java__NamespaceAccess, java__NumberLiteral, java__NullLiteral, java__ParenthesizedExpression, java__PackageAccess, NamespaceAccess, java__ParameterizedType, java__PostfixExpression, java__PrefixExpression, java__PrimitiveType, java__PrimitiveTypeBoolean, PrimitiveType, java__PrimitiveTypeByte, java__PrimitiveTypeChar, java__PrimitiveTypeDouble, java__PrimitiveTypeShort, java__PrimitiveTypeFloat, java__PrimitiveTypeInt, java__PrimitiveTypeLong, java__PrimitiveTypeVoid, java__ReturnStatement, java__VariableDeclaration, java__StringLiteral, java__SuperConstructorInvocation, java__SuperFieldAccess, AbstractTypeQualifiedExpression, java__SuperMethodInvocation, java__TextElement, java__SwitchCase, java__SwitchStatement, java__SynchronizedStatement, java__ThisExpression, java__ThrowStatement, java__TryStatement, java__TypeDeclarationStatement, java__TypeDeclaration, java__UnresolvedAnnotationDeclaration, AnnotationTypeDeclaration, UnresolvedItem, java__UnresolvedAnnotationTypeMemberDeclaration, AnnotationTypeMemberDeclaration, java__UnresolvedClassDeclaration, ClassDeclaration, java__TypeLiteral, java__UnresolvedItemAccess, java__UnresolvedEnumDeclaration, EnumDeclaration, java__UnresolvedInterfaceDeclaration, InterfaceDeclaration, java__UnresolvedLabeledStatement, LabeledStatement, java__UnresolvedMethodDeclaration, MethodDeclaration, java__UnresolvedSingleVariableDeclaration, SingleVariableDeclaration, java__UnresolvedType, java__UnresolvedTypeDeclaration, java__UnresolvedVariableDeclarationFragment, VariableDeclarationFragment, java__WildCardType, java__WhileStatement, java__Test, AssignmentKind, InheritanceKind, InfixExpressionKind, PrefixExpressionKind, PostfixExpressionKind, VisibilityKind},
    associations={body0, parameters1, usagesInDocComments6, usages7, method9, arguments10, typeArguments11, thrownExceptions2, typeParameters4, commentsAfterBody16, package19, superInterfaces20, qualifier23, type25, bodyDeclarations14, commentsBeforeBody15, values30, classFiles32, manifest33, message35, fragments27, type28, originalCompilationUnit42, originalClassFile44, member47, value49, expression37, comments40, usages57, bodyDeclarations58, classInstanceCreation60, default52, type54, dimensions66, initializer68, type70, expressions73, array61, index63, elementType78, leftHandSide80, rightHandSide82, array76, abstractTypeDeclaration85, annotations86, anonymousClassDeclarationOwner88, modifier90, expression94, type96, exception99, body101, statements91, label93, package109, anonymousClassDeclaration111, expression113, type115, type103, attachedSource106, package133, thenExpression123, superClass126, elseExpression118, commentList128, expression120, imports131, parameter151, types136, label139, expression141, body143, body146, expression148, field161, anonymousClassDeclaration153, arguments154, enumConstants157, expression159, expression162, expression165, updaters167, initializers170, body173, leftOperand187, expression176, thenStatement178, elseStatement181, importedElement184, rightOperand185, extendedOperands190, usagesInContinueStatements204, body193, rightOperand195, leftOperand197, tags200, body201, usagesInBreakStatements203, qualifier214, mainAttributes206, entryAttributes208, attributes210, member213, qualifier228, parameters230, returnType217, redefinedMethodDeclaration220, redefinitions222, expression224, method226, compilationUnits240, classFiles243, type232, ownedElements235, orphanTypes237, unresolvedItems238, singleVariableDeclaration251, variableDeclarationStatement254, archives246, bodyDeclaration249, ownedElements259, model261, variableDeclarationExpression256, usagesInImports258, typeArguments278, ownedPackages264, package268, usagesInPackageAccess270, package272, qualifier275, type276, expression281, operand283, operand285, expression287, methodDeclaration300, catchClause302, variable289, qualifier290, modifier293, type295, annotations297, enhancedForStatement303, expression304, field306, fragments320, expression308, expression310, statements312, body315, expression317, catchClauses330, expression323, body325, finally327, declaration339, usagesInTypeAccess333, type334, qualifier335, typeParameters337, type341, bounds343, element346, qualifier348, modifier354, annotations356, variablesContainer358, initializer351, usageInVariableAccess353, modifier359, annotations361, bound363, expression365, body367, thrownExceptions370},
    generalizations={gen_java__AbstractMethodDeclaration_BodyDeclaration, gen_java__AbstractMethodInvocation_ASTNode, gen_java__AbstractTypeQualifiedExpression_Expression, gen_java__AbstractVariablesContainer_ASTNode, gen_java__AbstractTypeDeclaration_BodyDeclaration, gen_java__AbstractTypeDeclaration_Type, gen_java__Archive_NamedElement, gen_java__AssertStatement_Statement, gen_java__Annotation_Expression, gen_java__AnnotationMemberValuePair_NamedElement, gen_java__AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_java__AnonymousClassDeclaration_ASTNode, gen_java__ArrayAccess_Expression, gen_java__AnnotationTypeMemberDeclaration_BodyDeclaration, gen_java__ArrayInitializer_Expression, gen_java__ArrayCreation_Expression, gen_java__Assignment_Expression, gen_java__ArrayLengthAccess_Expression, gen_java__ArrayType_Type, gen_java__BooleanLiteral_Expression, gen_java__BlockComment_Comment, gen_java__BodyDeclaration_NamedElement, gen_java__CastExpression_Expression, gen_java__CatchClause_Statement, gen_java__CharacterLiteral_Expression, gen_java__Block_Statement, gen_java__BreakStatement_Statement, gen_java__ClassInstanceCreation_Expression, gen_java__ClassInstanceCreation_AbstractMethodInvocation, gen_java__ConstructorDeclaration_AbstractMethodDeclaration, gen_java__ClassFile_NamedElement, gen_java__ConstructorInvocation_Statement, gen_java__ConstructorInvocation_AbstractMethodInvocation, gen_java__ClassDeclaration_TypeDeclaration, gen_java__Comment_ASTNode, gen_java__CompilationUnit_NamedElement, gen_java__ConditionalExpression_Expression, gen_java__ContinueStatement_Statement, gen_java__DoStatement_Statement, gen_java__EmptyStatement_Statement, gen_java__EnhancedForStatement_Statement, gen_java__EnumConstantDeclaration_BodyDeclaration, gen_java__EnumConstantDeclaration_VariableDeclaration, gen_java__EnumDeclaration_AbstractTypeDeclaration, gen_java__Expression_ASTNode, gen_java__ExpressionStatement_Statement, gen_java__FieldAccess_Expression, gen_java__IfStatement_Statement, gen_java__FieldDeclaration_BodyDeclaration, gen_java__FieldDeclaration_AbstractVariablesContainer, gen_java__ForStatement_Statement, gen_java__ImportDeclaration_ASTNode, gen_java__InfixExpression_Expression, gen_java__Initializer_BodyDeclaration, gen_java__LineComment_Comment, gen_java__InstanceofExpression_Expression, gen_java__InterfaceDeclaration_TypeDeclaration, gen_java__Javadoc_Comment, gen_java__LabeledStatement_NamedElement, gen_java__LabeledStatement_Statement, gen_java__MethodDeclaration_AbstractMethodDeclaration, gen_java__MemberRef_ASTNode, gen_java__MethodInvocation_Expression, gen_java__MethodInvocation_AbstractMethodInvocation, gen_java__MethodRef_ASTNode, gen_java__MethodRefParameter_ASTNode, gen_java__Modifier_ASTNode, gen_java__NamedElement_ASTNode, gen_java__NamespaceAccess_ASTNode, gen_java__NumberLiteral_Expression, gen_java__NullLiteral_Expression, gen_java__Package_NamedElement, gen_java__PackageAccess_NamespaceAccess, gen_java__ParameterizedType_Type, gen_java__ParenthesizedExpression_Expression, gen_java__PostfixExpression_Expression, gen_java__PrefixExpression_Expression, gen_java__SingleVariableAccess_Expression, gen_java__PrimitiveType_Type, gen_java__PrimitiveTypeBoolean_PrimitiveType, gen_java__PrimitiveTypeByte_PrimitiveType, gen_java__PrimitiveTypeChar_PrimitiveType, gen_java__PrimitiveTypeDouble_PrimitiveType, gen_java__PrimitiveTypeShort_PrimitiveType, gen_java__PrimitiveTypeFloat_PrimitiveType, gen_java__PrimitiveTypeInt_PrimitiveType, gen_java__PrimitiveTypeLong_PrimitiveType, gen_java__PrimitiveTypeVoid_PrimitiveType, gen_java__ReturnStatement_Statement, gen_java__SingleVariableDeclaration_VariableDeclaration, gen_java__SuperMethodInvocation_AbstractTypeQualifiedExpression, gen_java__SuperMethodInvocation_AbstractMethodInvocation, gen_java__Statement_ASTNode, gen_java__StringLiteral_Expression, gen_java__SuperConstructorInvocation_Statement, gen_java__SuperConstructorInvocation_AbstractMethodInvocation, gen_java__SuperFieldAccess_AbstractTypeQualifiedExpression, gen_java__TextElement_ASTNode, gen_java__SwitchCase_Statement, gen_java__SwitchStatement_Statement, gen_java__SynchronizedStatement_Statement, gen_java__TagElement_ASTNode, gen_java__ThisExpression_AbstractTypeQualifiedExpression, gen_java__ThrowStatement_Statement, gen_java__TryStatement_Statement, gen_java__TypeDeclarationStatement_Statement, gen_java__Type_NamedElement, gen_java__TypeAccess_Expression, gen_java__TypeAccess_NamespaceAccess, gen_java__TypeDeclaration_AbstractTypeDeclaration, gen_java__UnresolvedAnnotationDeclaration_AnnotationTypeDeclaration, gen_java__UnresolvedAnnotationDeclaration_UnresolvedItem, gen_java__UnresolvedAnnotationTypeMemberDeclaration_AnnotationTypeMemberDeclaration, gen_java__UnresolvedAnnotationTypeMemberDeclaration_UnresolvedItem, gen_java__UnresolvedClassDeclaration_ClassDeclaration, gen_java__TypeLiteral_Expression, gen_java__TypeParameter_Type, gen_java__UnresolvedItem_NamedElement, gen_java__UnresolvedItemAccess_Expression, gen_java__UnresolvedItemAccess_NamespaceAccess, gen_java__VariableDeclarationFragment_VariableDeclaration, gen_java__VariableDeclarationStatement_Statement, gen_java__VariableDeclarationStatement_AbstractVariablesContainer, gen_java__UnresolvedClassDeclaration_UnresolvedItem, gen_java__UnresolvedEnumDeclaration_EnumDeclaration, gen_java__UnresolvedEnumDeclaration_UnresolvedItem, gen_java__UnresolvedInterfaceDeclaration_InterfaceDeclaration, gen_java__UnresolvedInterfaceDeclaration_UnresolvedItem, gen_java__UnresolvedLabeledStatement_LabeledStatement, gen_java__UnresolvedLabeledStatement_UnresolvedItem, gen_java__UnresolvedMethodDeclaration_MethodDeclaration, gen_java__UnresolvedMethodDeclaration_UnresolvedItem, gen_java__UnresolvedSingleVariableDeclaration_SingleVariableDeclaration, gen_java__UnresolvedSingleVariableDeclaration_UnresolvedItem, gen_java__UnresolvedType_Type, gen_java__UnresolvedType_UnresolvedItem, gen_java__UnresolvedTypeDeclaration_AbstractTypeDeclaration, gen_java__UnresolvedTypeDeclaration_UnresolvedItem, gen_java__UnresolvedVariableDeclarationFragment_VariableDeclarationFragment, gen_java__UnresolvedVariableDeclarationFragment_UnresolvedItem, gen_java__VariableDeclaration_NamedElement, gen_java__VariableDeclarationExpression_Expression, gen_java__VariableDeclarationExpression_AbstractVariablesContainer, gen_java__WildCardType_Type, gen_java__WhileStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)