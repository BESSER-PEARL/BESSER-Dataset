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
			EnumerationLiteral(name="REMAINDER_ASSIGN"),
			EnumerationLiteral(name="LEFT_SHIFT_ASSIGN"),
			EnumerationLiteral(name="RIGHT_SHIFT_SIGNED_ASSIGN"),
			EnumerationLiteral(name="RIGHT_SHIFT_UNSIGNED_ASSIGN"),
			EnumerationLiteral(name="DIVIDE_ASSIGN"),
			EnumerationLiteral(name="BIT_AND_ASSIGN"),
			EnumerationLiteral(name="BIT_OR_ASSIGN"),
			EnumerationLiteral(name="BIT_XOR_ASSIGN")
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
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="CONDITIONAL_AND"),
			EnumerationLiteral(name="CONDITIONAL_OR"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="LESS_EQUALS"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="XOR")
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
java_AbstractMethodDeclaration = Class(name="java::AbstractMethodDeclaration", is_abstract=True)
BodyDeclaration = Class(name="BodyDeclaration")
java_TypeParameter = Class(name="java::TypeParameter")
java_MethodRef = Class(name="java::MethodRef")
java_AbstractMethodInvocation = Class(name="java::AbstractMethodInvocation", is_abstract=True)
ASTNode = Class(name="ASTNode")
java_Expression = Class(name="java::Expression", is_abstract=True)
java_AbstractTypeDeclaration = Class(name="java::AbstractTypeDeclaration", is_abstract=True)
Type = Class(name="Type")
java_BodyDeclaration = Class(name="java::BodyDeclaration", is_abstract=True)
java_Block = Class(name="java::Block")
java_SingleVariableDeclaration = Class(name="java::SingleVariableDeclaration")
java_TypeAccess = Class(name="java::TypeAccess")
java_AbstractVariablesContainer = Class(name="java::AbstractVariablesContainer", is_abstract=True)
java_VariableDeclarationFragment = Class(name="java::VariableDeclarationFragment")
java_Annotation = Class(name="java::Annotation")
java_AnnotationMemberValuePair = Class(name="java::AnnotationMemberValuePair")
java_Archive = Class(name="java::Archive")
NamedElement = Class(name="NamedElement")
java_Manifest = Class(name="java::Manifest")
java_AssertStatement = Class(name="java::AssertStatement")
Statement = Class(name="Statement")
java_Comment = Class(name="java::Comment", is_abstract=True)
java_Package = Class(name="java::Package")
java_AbstractTypeQualifiedExpression = Class(name="java::AbstractTypeQualifiedExpression", is_abstract=True)
Expression = Class(name="Expression")
java_AnnotationTypeDeclaration = Class(name="java::AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
java_AnonymousClassDeclaration = Class(name="java::AnonymousClassDeclaration")
java_ArrayAccess = Class(name="java::ArrayAccess")
java_ASTNode = Class(name="java::ASTNode", is_abstract=True)
java_CompilationUnit = Class(name="java::CompilationUnit")
java_AnnotationTypeMemberDeclaration = Class(name="java::AnnotationTypeMemberDeclaration")
java_ArrayLengthAccess = Class(name="java::ArrayLengthAccess")
java_ArrayType = Class(name="java::ArrayType")
java_Assignment = Class(name="java::Assignment")
java_ArrayCreation = Class(name="java::ArrayCreation")
java_ArrayInitializer = Class(name="java::ArrayInitializer")
java_BlockComment = Class(name="java::BlockComment")
Comment = Class(name="Comment")
java_Statement = Class(name="java::Statement", is_abstract=True)
java_BreakStatement = Class(name="java::BreakStatement")
java_LabeledStatement = Class(name="java::LabeledStatement")
java_CastExpression = Class(name="java::CastExpression")
java_Modifier = Class(name="java::Modifier")
java_BooleanLiteral = Class(name="java::BooleanLiteral")
java_CatchClause = Class(name="java::CatchClause")
java_CharacterLiteral = Class(name="java::CharacterLiteral")
java_ConstructorInvocation = Class(name="java::ConstructorInvocation")
AbstractMethodInvocation = Class(name="AbstractMethodInvocation")
java_ConstructorDeclaration = Class(name="java::ConstructorDeclaration")
AbstractMethodDeclaration = Class(name="AbstractMethodDeclaration")
java_ConditionalExpression = Class(name="java::ConditionalExpression")
java_ClassDeclaration = Class(name="java::ClassDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
java_ContinueStatement = Class(name="java::ContinueStatement")
java_DoStatement = Class(name="java::DoStatement")
java_ImportDeclaration = Class(name="java::ImportDeclaration")
java_EnumConstantDeclaration = Class(name="java::EnumConstantDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
java_EmptyStatement = Class(name="java::EmptyStatement")
java_EnhancedForStatement = Class(name="java::EnhancedForStatement")
java_EnumDeclaration = Class(name="java::EnumDeclaration")
java_ExpressionStatement = Class(name="java::ExpressionStatement")
java_FieldDeclaration = Class(name="java::FieldDeclaration")
AbstractVariablesContainer = Class(name="AbstractVariablesContainer")
java_ForStatement = Class(name="java::ForStatement")
java_FieldAccess = Class(name="java::FieldAccess")
java_SingleVariableAccess = Class(name="java::SingleVariableAccess")
java_IfStatement = Class(name="java::IfStatement")
java_NamedElement = Class(name="java::NamedElement", is_abstract=True)
java_InfixExpression = Class(name="java::InfixExpression")
java_Initializer = Class(name="java::Initializer")
java_InstanceofExpression = Class(name="java::InstanceofExpression")
java_InterfaceDeclaration = Class(name="java::InterfaceDeclaration")
java_Javadoc = Class(name="java::Javadoc")
java_TagElement = Class(name="java::TagElement")
java_ManifestAttribute = Class(name="java::ManifestAttribute")
java_ManifestEntry = Class(name="java::ManifestEntry")
java_LineComment = Class(name="java::LineComment")
java_MethodDeclaration = Class(name="java::MethodDeclaration")
java_MethodInvocation = Class(name="java::MethodInvocation")
java_MemberRef = Class(name="java::MemberRef")
java_MethodRefParameter = Class(name="java::MethodRefParameter")
java_Model = Class(name="java::Model")
java_Type = Class(name="java::Type", is_abstract=True)
java_UnresolvedItem = Class(name="java::UnresolvedItem")
java_VariableDeclarationStatement = Class(name="java::VariableDeclarationStatement")
java_VariableDeclarationExpression = Class(name="java::VariableDeclarationExpression")
java_NamespaceAccess = Class(name="java::NamespaceAccess", is_abstract=True)
java_NumberLiteral = Class(name="java::NumberLiteral")
java_PackageAccess = Class(name="java::PackageAccess")
NamespaceAccess = Class(name="NamespaceAccess")
java_NullLiteral = Class(name="java::NullLiteral")
java_ParameterizedType = Class(name="java::ParameterizedType")
java_ParenthesizedExpression = Class(name="java::ParenthesizedExpression")
java_PostfixExpression = Class(name="java::PostfixExpression")
java_PrefixExpression = Class(name="java::PrefixExpression")
java_PrimitiveType = Class(name="java::PrimitiveType")
java_PrimitiveTypeBoolean = Class(name="java::PrimitiveTypeBoolean")
java_PrimitiveTypeShort = Class(name="java::PrimitiveTypeShort")
java_PrimitiveTypeFloat = Class(name="java::PrimitiveTypeFloat")
java_PrimitiveTypeInt = Class(name="java::PrimitiveTypeInt")
java_PrimitiveTypeLong = Class(name="java::PrimitiveTypeLong")
java_PrimitiveTypeVoid = Class(name="java::PrimitiveTypeVoid")
java_ReturnStatement = Class(name="java::ReturnStatement")
java_VariableDeclaration = Class(name="java::VariableDeclaration", is_abstract=True)
PrimitiveType = Class(name="PrimitiveType")
java_PrimitiveTypeByte = Class(name="java::PrimitiveTypeByte")
java_PrimitiveTypeChar = Class(name="java::PrimitiveTypeChar")
java_PrimitiveTypeDouble = Class(name="java::PrimitiveTypeDouble")
java_SuperConstructorInvocation = Class(name="java::SuperConstructorInvocation")
java_SuperFieldAccess = Class(name="java::SuperFieldAccess")
AbstractTypeQualifiedExpression = Class(name="AbstractTypeQualifiedExpression")
java_SuperMethodInvocation = Class(name="java::SuperMethodInvocation")
java_SwitchCase = Class(name="java::SwitchCase")
java_StringLiteral = Class(name="java::StringLiteral")
java_SynchronizedStatement = Class(name="java::SynchronizedStatement")
java_SwitchStatement = Class(name="java::SwitchStatement")
java_ThisExpression = Class(name="java::ThisExpression")
java_ThrowStatement = Class(name="java::ThrowStatement")
java_TryStatement = Class(name="java::TryStatement")
java_TextElement = Class(name="java::TextElement")
java_TypeDeclaration = Class(name="java::TypeDeclaration", is_abstract=True)
java_TypeDeclarationStatement = Class(name="java::TypeDeclarationStatement")
java_UnresolvedItemAccess = Class(name="java::UnresolvedItemAccess")
java_UnresolvedAnnotationDeclaration = Class(name="java::UnresolvedAnnotationDeclaration")
AnnotationTypeDeclaration = Class(name="AnnotationTypeDeclaration")
UnresolvedItem = Class(name="UnresolvedItem")
java_TypeLiteral = Class(name="java::TypeLiteral")
java_UnresolvedClassDeclaration = Class(name="java::UnresolvedClassDeclaration")
ClassDeclaration = Class(name="ClassDeclaration")
java_UnresolvedEnumDeclaration = Class(name="java::UnresolvedEnumDeclaration")
EnumDeclaration = Class(name="EnumDeclaration")
java_UnresolvedInterfaceDeclaration = Class(name="java::UnresolvedInterfaceDeclaration")
InterfaceDeclaration = Class(name="InterfaceDeclaration")
java_UnresolvedLabeledStatement = Class(name="java::UnresolvedLabeledStatement")
LabeledStatement = Class(name="LabeledStatement")
java_UnresolvedMethodDeclaration = Class(name="java::UnresolvedMethodDeclaration")
MethodDeclaration = Class(name="MethodDeclaration")
java_UnresolvedSingleVariableDeclaration = Class(name="java::UnresolvedSingleVariableDeclaration")
SingleVariableDeclaration = Class(name="SingleVariableDeclaration")
java_UnresolvedAnnotationTypeMemberDeclaration = Class(name="java::UnresolvedAnnotationTypeMemberDeclaration")
AnnotationTypeMemberDeclaration = Class(name="AnnotationTypeMemberDeclaration")
java_UnresolvedVariableDeclarationFragment = Class(name="java::UnresolvedVariableDeclarationFragment")
VariableDeclarationFragment = Class(name="VariableDeclarationFragment")
java_UnresolvedType = Class(name="java::UnresolvedType")
java_UnresolvedTypeDeclaration = Class(name="java::UnresolvedTypeDeclaration")
java_WildCardType = Class(name="java::WildCardType")
java_WhileStatement = Class(name="java::WhileStatement")

# java_AbstractMethodDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# java_TypeParameter class attributes and methods

# java_MethodRef class attributes and methods

# java_AbstractMethodInvocation class attributes and methods

# ASTNode class attributes and methods

# java_Expression class attributes and methods

# java_AbstractTypeDeclaration class attributes and methods

# Type class attributes and methods

# java_BodyDeclaration class attributes and methods

# java_Block class attributes and methods

# java_SingleVariableDeclaration class attributes and methods
java_SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=BooleanType)
java_SingleVariableDeclaration.attributes={java_SingleVariableDeclaration_varargs}

# java_TypeAccess class attributes and methods

# java_AbstractVariablesContainer class attributes and methods

# java_VariableDeclarationFragment class attributes and methods

# java_Annotation class attributes and methods

# java_AnnotationMemberValuePair class attributes and methods

# java_Archive class attributes and methods
java_Archive_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java_Archive.attributes={java_Archive_originalFilePath}

# NamedElement class attributes and methods

# java_Manifest class attributes and methods

# java_AssertStatement class attributes and methods

# Statement class attributes and methods

# java_Comment class attributes and methods
java_Comment_content: Property = Property(name="content", type=StringType)
java_Comment_enclosedByParent: Property = Property(name="enclosedByParent", type=BooleanType)
java_Comment_prefixOfParent: Property = Property(name="prefixOfParent", type=BooleanType)
java_Comment.attributes={java_Comment_content, java_Comment_prefixOfParent, java_Comment_enclosedByParent}

# java_Package class attributes and methods

# java_AbstractTypeQualifiedExpression class attributes and methods

# Expression class attributes and methods

# java_AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# java_AnonymousClassDeclaration class attributes and methods

# java_ArrayAccess class attributes and methods

# java_ASTNode class attributes and methods

# java_CompilationUnit class attributes and methods
java_CompilationUnit_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java_CompilationUnit.attributes={java_CompilationUnit_originalFilePath}

# java_AnnotationTypeMemberDeclaration class attributes and methods

# java_ArrayLengthAccess class attributes and methods

# java_ArrayType class attributes and methods
java_ArrayType_dimensions: Property = Property(name="dimensions", type=IntegerType)
java_ArrayType.attributes={java_ArrayType_dimensions}

# java_Assignment class attributes and methods
java_Assignment_operator: Property = Property(name="operator", type=StringType)
java_Assignment.attributes={java_Assignment_operator}

# java_ArrayCreation class attributes and methods

# java_ArrayInitializer class attributes and methods

# java_BlockComment class attributes and methods

# Comment class attributes and methods

# java_Statement class attributes and methods

# java_BreakStatement class attributes and methods

# java_LabeledStatement class attributes and methods

# java_CastExpression class attributes and methods

# java_Modifier class attributes and methods
java_Modifier_visibility: Property = Property(name="visibility", type=StringType)
java_Modifier_inheritance: Property = Property(name="inheritance", type=StringType)
java_Modifier_static: Property = Property(name="static", type=BooleanType)
java_Modifier_transient: Property = Property(name="transient", type=BooleanType)
java_Modifier_volatile: Property = Property(name="volatile", type=BooleanType)
java_Modifier_native: Property = Property(name="native", type=BooleanType)
java_Modifier_strictfp: Property = Property(name="strictfp", type=BooleanType)
java_Modifier_synchronized: Property = Property(name="synchronized", type=BooleanType)
java_Modifier.attributes={java_Modifier_volatile, java_Modifier_synchronized, java_Modifier_strictfp, java_Modifier_transient, java_Modifier_native, java_Modifier_static, java_Modifier_inheritance, java_Modifier_visibility}

# java_BooleanLiteral class attributes and methods
java_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
java_BooleanLiteral.attributes={java_BooleanLiteral_value}

# java_CatchClause class attributes and methods

# java_CharacterLiteral class attributes and methods
java_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
java_CharacterLiteral.attributes={java_CharacterLiteral_escapedValue}

# java_ConstructorInvocation class attributes and methods

# AbstractMethodInvocation class attributes and methods

# java_ConstructorDeclaration class attributes and methods

# AbstractMethodDeclaration class attributes and methods

# java_ConditionalExpression class attributes and methods

# java_ClassDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# java_ContinueStatement class attributes and methods

# java_DoStatement class attributes and methods

# java_ImportDeclaration class attributes and methods
java_ImportDeclaration_static: Property = Property(name="static", type=BooleanType)
java_ImportDeclaration.attributes={java_ImportDeclaration_static}

# java_EnumConstantDeclaration class attributes and methods

# VariableDeclaration class attributes and methods

# java_EmptyStatement class attributes and methods

# java_EnhancedForStatement class attributes and methods

# java_EnumDeclaration class attributes and methods

# java_ExpressionStatement class attributes and methods

# java_FieldDeclaration class attributes and methods

# AbstractVariablesContainer class attributes and methods

# java_ForStatement class attributes and methods

# java_FieldAccess class attributes and methods

# java_SingleVariableAccess class attributes and methods

# java_IfStatement class attributes and methods

# java_NamedElement class attributes and methods
java_NamedElement_name: Property = Property(name="name", type=StringType)
java_NamedElement_proxy: Property = Property(name="proxy", type=BooleanType)
java_NamedElement.attributes={java_NamedElement_name, java_NamedElement_proxy}

# java_InfixExpression class attributes and methods
java_InfixExpression_operator: Property = Property(name="operator", type=StringType)
java_InfixExpression.attributes={java_InfixExpression_operator}

# java_Initializer class attributes and methods

# java_InstanceofExpression class attributes and methods

# java_InterfaceDeclaration class attributes and methods

# java_Javadoc class attributes and methods

# java_TagElement class attributes and methods
java_TagElement_tagName: Property = Property(name="tagName", type=StringType)
java_TagElement.attributes={java_TagElement_tagName}

# java_ManifestAttribute class attributes and methods
java_ManifestAttribute_key: Property = Property(name="key", type=StringType)
java_ManifestAttribute_value: Property = Property(name="value", type=StringType)
java_ManifestAttribute.attributes={java_ManifestAttribute_key, java_ManifestAttribute_value}

# java_ManifestEntry class attributes and methods
java_ManifestEntry_name: Property = Property(name="name", type=StringType)
java_ManifestEntry.attributes={java_ManifestEntry_name}

# java_LineComment class attributes and methods

# java_MethodDeclaration class attributes and methods
java_MethodDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
java_MethodDeclaration.attributes={java_MethodDeclaration_extraArrayDimensions}

# java_MethodInvocation class attributes and methods

# java_MemberRef class attributes and methods

# java_MethodRefParameter class attributes and methods
java_MethodRefParameter_name: Property = Property(name="name", type=StringType)
java_MethodRefParameter_varargs: Property = Property(name="varargs", type=BooleanType)
java_MethodRefParameter.attributes={java_MethodRefParameter_name, java_MethodRefParameter_varargs}

# java_Model class attributes and methods
java_Model_name: Property = Property(name="name", type=StringType)
java_Model.attributes={java_Model_name}

# java_Type class attributes and methods

# java_UnresolvedItem class attributes and methods

# java_VariableDeclarationStatement class attributes and methods
java_VariableDeclarationStatement_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
java_VariableDeclarationStatement.attributes={java_VariableDeclarationStatement_extraArrayDimensions}

# java_VariableDeclarationExpression class attributes and methods

# java_NamespaceAccess class attributes and methods

# java_NumberLiteral class attributes and methods
java_NumberLiteral_tokenValue: Property = Property(name="tokenValue", type=StringType)
java_NumberLiteral.attributes={java_NumberLiteral_tokenValue}

# java_PackageAccess class attributes and methods

# NamespaceAccess class attributes and methods

# java_NullLiteral class attributes and methods

# java_ParameterizedType class attributes and methods

# java_ParenthesizedExpression class attributes and methods

# java_PostfixExpression class attributes and methods
java_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
java_PostfixExpression.attributes={java_PostfixExpression_operator}

# java_PrefixExpression class attributes and methods
java_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
java_PrefixExpression.attributes={java_PrefixExpression_operator}

# java_PrimitiveType class attributes and methods

# java_PrimitiveTypeBoolean class attributes and methods

# java_PrimitiveTypeShort class attributes and methods

# java_PrimitiveTypeFloat class attributes and methods

# java_PrimitiveTypeInt class attributes and methods

# java_PrimitiveTypeLong class attributes and methods

# java_PrimitiveTypeVoid class attributes and methods

# java_ReturnStatement class attributes and methods

# java_VariableDeclaration class attributes and methods
java_VariableDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
java_VariableDeclaration.attributes={java_VariableDeclaration_extraArrayDimensions}

# PrimitiveType class attributes and methods

# java_PrimitiveTypeByte class attributes and methods

# java_PrimitiveTypeChar class attributes and methods

# java_PrimitiveTypeDouble class attributes and methods

# java_SuperConstructorInvocation class attributes and methods

# java_SuperFieldAccess class attributes and methods

# AbstractTypeQualifiedExpression class attributes and methods

# java_SuperMethodInvocation class attributes and methods

# java_SwitchCase class attributes and methods
java_SwitchCase_default: Property = Property(name="default", type=BooleanType)
java_SwitchCase.attributes={java_SwitchCase_default}

# java_StringLiteral class attributes and methods
java_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
java_StringLiteral.attributes={java_StringLiteral_escapedValue}

# java_SynchronizedStatement class attributes and methods

# java_SwitchStatement class attributes and methods

# java_ThisExpression class attributes and methods

# java_ThrowStatement class attributes and methods

# java_TryStatement class attributes and methods

# java_TextElement class attributes and methods
java_TextElement_text: Property = Property(name="text", type=StringType)
java_TextElement.attributes={java_TextElement_text}

# java_TypeDeclaration class attributes and methods

# java_TypeDeclarationStatement class attributes and methods

# java_UnresolvedItemAccess class attributes and methods

# java_UnresolvedAnnotationDeclaration class attributes and methods

# AnnotationTypeDeclaration class attributes and methods

# UnresolvedItem class attributes and methods

# java_TypeLiteral class attributes and methods

# java_UnresolvedClassDeclaration class attributes and methods

# ClassDeclaration class attributes and methods

# java_UnresolvedEnumDeclaration class attributes and methods

# EnumDeclaration class attributes and methods

# java_UnresolvedInterfaceDeclaration class attributes and methods

# InterfaceDeclaration class attributes and methods

# java_UnresolvedLabeledStatement class attributes and methods

# LabeledStatement class attributes and methods

# java_UnresolvedMethodDeclaration class attributes and methods

# MethodDeclaration class attributes and methods

# java_UnresolvedSingleVariableDeclaration class attributes and methods

# SingleVariableDeclaration class attributes and methods

# java_UnresolvedAnnotationTypeMemberDeclaration class attributes and methods

# AnnotationTypeMemberDeclaration class attributes and methods

# java_UnresolvedVariableDeclarationFragment class attributes and methods

# VariableDeclarationFragment class attributes and methods

# java_UnresolvedType class attributes and methods

# java_UnresolvedTypeDeclaration class attributes and methods

# java_WildCardType class attributes and methods
java_WildCardType_upperBound: Property = Property(name="upperBound", type=BooleanType)
java_WildCardType.attributes={java_WildCardType_upperBound}

# java_WhileStatement class attributes and methods

# Relationships
typeParameters4: BinaryAssociation = BinaryAssociation(
    name="typeParameters4",
    ends={
        Property(name="java_TypeParameter", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration5", type=java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usagesInDocComments6: BinaryAssociation = BinaryAssociation(
    name="usagesInDocComments6",
    ends={
        Property(name="MethodRef", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=java_MethodRef, multiplicity=Multiplicity(0, 9999))
    }
)
usages7: BinaryAssociation = BinaryAssociation(
    name="usages7",
    ends={
        Property(name="AbstractMethodInvocation", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="method8", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(0, 9999))
    }
)
method9: BinaryAssociation = BinaryAssociation(
    name="method9",
    ends={
        Property(name="AbstractMethodDeclaration", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="usages", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
arguments10: BinaryAssociation = BinaryAssociation(
    name="arguments10",
    ends={
        Property(name="java_Expression", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodInvocation", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments11: BinaryAssociation = BinaryAssociation(
    name="typeArguments11",
    ends={
        Property(name="java_TypeAccess13", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodInvocation12", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations14: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations14",
    ends={
        Property(name="BodyDeclaration", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractTypeDeclaration", type=java_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body0: BinaryAssociation = BinaryAssociation(
    name="body0",
    ends={
        Property(name="java_Block", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration", type=java_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="SingleVariableDeclaration", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methodDeclaration", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thrownExceptions2: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions2",
    ends={
        Property(name="java_TypeAccess", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration3", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier23: BinaryAssociation = BinaryAssociation(
    name="qualifier23",
    ends={
        Property(name="java_TypeAccess24", type=java_AbstractTypeQualifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeQualifiedExpression", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="java_TypeAccess26", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractVariablesContainer", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments27: BinaryAssociation = BinaryAssociation(
    name="fragments27",
    ends={
        Property(name="VariableDeclarationFragment", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="variablesContainer", type=java_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="java_TypeAccess29", type=java_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Annotation", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values30: BinaryAssociation = BinaryAssociation(
    name="values30",
    ends={
        Property(name="java_AnnotationMemberValuePair", type=java_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Annotation31", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifest32: BinaryAssociation = BinaryAssociation(
    name="manifest32",
    ends={
        Property(name="java_Manifest", type=java_Archive, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Archive", type=java_Manifest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message33: BinaryAssociation = BinaryAssociation(
    name="message33",
    ends={
        Property(name="java_Expression34", type=java_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AssertStatement", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commentsBeforeBody15: BinaryAssociation = BinaryAssociation(
    name="commentsBeforeBody15",
    ends={
        Property(name="java_Comment", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsAfterBody16: BinaryAssociation = BinaryAssociation(
    name="commentsAfterBody16",
    ends={
        Property(name="java_Comment18", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration17", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package19: BinaryAssociation = BinaryAssociation(
    name="package19",
    ends={
        Property(name="Package", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements", type=java_Package, multiplicity=Multiplicity(0, 1))
    }
)
superInterfaces20: BinaryAssociation = BinaryAssociation(
    name="superInterfaces20",
    ends={
        Property(name="java_TypeAccess22", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration21", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value44: BinaryAssociation = BinaryAssociation(
    name="value44",
    ends={
        Property(name="java_Expression46", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationMemberValuePair45", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
default47: BinaryAssociation = BinaryAssociation(
    name="default47",
    ends={
        Property(name="java_Expression48", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationTypeMemberDeclaration", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="java_TypeAccess51", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationTypeMemberDeclaration50", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usages52: BinaryAssociation = BinaryAssociation(
    name="usages52",
    ends={
        Property(name="AnnotationMemberValuePair", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="member", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999))
    }
)
bodyDeclarations53: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations53",
    ends={
        Property(name="BodyDeclaration54", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclarationOwner", type=java_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
array55: BinaryAssociation = BinaryAssociation(
    name="array55",
    ends={
        Property(name="java_Expression56", type=java_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayAccess", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index57: BinaryAssociation = BinaryAssociation(
    name="index57",
    ends={
        Property(name="java_Expression59", type=java_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayAccess58", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression35: BinaryAssociation = BinaryAssociation(
    name="expression35",
    ends={
        Property(name="java_Expression37", type=java_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AssertStatement36", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comments38: BinaryAssociation = BinaryAssociation(
    name="comments38",
    ends={
        Property(name="java_Comment39", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalCompilationUnit40: BinaryAssociation = BinaryAssociation(
    name="originalCompilationUnit40",
    ends={
        Property(name="java_CompilationUnit", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode41", type=java_CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
member42: BinaryAssociation = BinaryAssociation(
    name="member42",
    ends={
        Property(name="AnnotationTypeMemberDeclaration", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="usages43", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
array70: BinaryAssociation = BinaryAssociation(
    name="array70",
    ends={
        Property(name="java_Expression71", type=java_ArrayLengthAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayLengthAccess", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType72: BinaryAssociation = BinaryAssociation(
    name="elementType72",
    ends={
        Property(name="java_TypeAccess73", type=java_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayType", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide74: BinaryAssociation = BinaryAssociation(
    name="leftHandSide74",
    ends={
        Property(name="java_Expression75", type=java_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Assignment", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide76: BinaryAssociation = BinaryAssociation(
    name="rightHandSide76",
    ends={
        Property(name="java_Expression78", type=java_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Assignment77", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions60: BinaryAssociation = BinaryAssociation(
    name="dimensions60",
    ends={
        Property(name="java_Expression61", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer62: BinaryAssociation = BinaryAssociation(
    name="initializer62",
    ends={
        Property(name="java_ArrayInitializer", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation63", type=java_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type64: BinaryAssociation = BinaryAssociation(
    name="type64",
    ends={
        Property(name="java_TypeAccess66", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation65", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions67: BinaryAssociation = BinaryAssociation(
    name="expressions67",
    ends={
        Property(name="java_Expression69", type=java_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayInitializer68", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstractTypeDeclaration79: BinaryAssociation = BinaryAssociation(
    name="abstractTypeDeclaration79",
    ends={
        Property(name="AbstractTypeDeclaration", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
annotations80: BinaryAssociation = BinaryAssociation(
    name="annotations80",
    ends={
        Property(name="java_Annotation81", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_BodyDeclaration", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements85: BinaryAssociation = BinaryAssociation(
    name="statements85",
    ends={
        Property(name="java_Statement", type=java_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Block86", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label87: BinaryAssociation = BinaryAssociation(
    name="label87",
    ends={
        Property(name="LabeledStatement", type=java_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInBreakStatements", type=java_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
anonymousClassDeclarationOwner82: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclarationOwner82",
    ends={
        Property(name="AnonymousClassDeclaration", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations83", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
modifier84: BinaryAssociation = BinaryAssociation(
    name="modifier84",
    ends={
        Property(name="Modifier", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclaration", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception93: BinaryAssociation = BinaryAssociation(
    name="exception93",
    ends={
        Property(name="SingleVariableDeclaration94", type=java_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="catchClause", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body95: BinaryAssociation = BinaryAssociation(
    name="body95",
    ends={
        Property(name="java_Block96", type=java_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CatchClause", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression88: BinaryAssociation = BinaryAssociation(
    name="expression88",
    ends={
        Property(name="java_Expression89", type=java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CastExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type90: BinaryAssociation = BinaryAssociation(
    name="type90",
    ends={
        Property(name="java_TypeAccess92", type=java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CastExpression91", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression99: BinaryAssociation = BinaryAssociation(
    name="expression99",
    ends={
        Property(name="java_Expression101", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression100", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression102: BinaryAssociation = BinaryAssociation(
    name="thenExpression102",
    ends={
        Property(name="java_Expression104", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression103", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression97: BinaryAssociation = BinaryAssociation(
    name="elseExpression97",
    ends={
        Property(name="java_Expression98", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
commentList107: BinaryAssociation = BinaryAssociation(
    name="commentList107",
    ends={
        Property(name="java_Comment109", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit108", type=java_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
superClass105: BinaryAssociation = BinaryAssociation(
    name="superClass105",
    ends={
        Property(name="java_TypeAccess106", type=java_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassDeclaration", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types114: BinaryAssociation = BinaryAssociation(
    name="types114",
    ends={
        Property(name="java_AbstractTypeDeclaration116", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit115", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
label117: BinaryAssociation = BinaryAssociation(
    name="label117",
    ends={
        Property(name="LabeledStatement118", type=java_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInContinueStatements", type=java_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
expression119: BinaryAssociation = BinaryAssociation(
    name="expression119",
    ends={
        Property(name="java_Expression120", type=java_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_DoStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imports110: BinaryAssociation = BinaryAssociation(
    name="imports110",
    ends={
        Property(name="java_ImportDeclaration", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit111", type=java_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package112: BinaryAssociation = BinaryAssociation(
    name="package112",
    ends={
        Property(name="java_Package", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit113", type=java_Package, multiplicity=Multiplicity(0, 1))
    }
)
body124: BinaryAssociation = BinaryAssociation(
    name="body124",
    ends={
        Property(name="java_Statement125", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnhancedForStatement", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="java_Expression128", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnhancedForStatement127", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter129: BinaryAssociation = BinaryAssociation(
    name="parameter129",
    ends={
        Property(name="SingleVariableDeclaration130", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="enhancedForStatement", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body121: BinaryAssociation = BinaryAssociation(
    name="body121",
    ends={
        Property(name="java_Statement123", type=java_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_DoStatement122", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumConstants135: BinaryAssociation = BinaryAssociation(
    name="enumConstants135",
    ends={
        Property(name="java_EnumConstantDeclaration136", type=java_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnumDeclaration", type=java_EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression137: BinaryAssociation = BinaryAssociation(
    name="expression137",
    ends={
        Property(name="java_Expression138", type=java_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ExpressionStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anonymousClassDeclaration131: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration131",
    ends={
        Property(name="java_AnonymousClassDeclaration", type=java_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnumConstantDeclaration", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments132: BinaryAssociation = BinaryAssociation(
    name="arguments132",
    ends={
        Property(name="java_Expression134", type=java_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnumConstantDeclaration133", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
field139: BinaryAssociation = BinaryAssociation(
    name="field139",
    ends={
        Property(name="java_SingleVariableAccess", type=java_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_FieldAccess", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression140: BinaryAssociation = BinaryAssociation(
    name="expression140",
    ends={
        Property(name="java_Expression142", type=java_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_FieldAccess141", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression143: BinaryAssociation = BinaryAssociation(
    name="expression143",
    ends={
        Property(name="java_Expression144", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializers148: BinaryAssociation = BinaryAssociation(
    name="initializers148",
    ends={
        Property(name="java_ForStatement149", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="java_Expression150", type=java_ForStatement, multiplicity=Multiplicity(1, 1))
    }
)
body151: BinaryAssociation = BinaryAssociation(
    name="body151",
    ends={
        Property(name="java_Statement153", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement152", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression154: BinaryAssociation = BinaryAssociation(
    name="expression154",
    ends={
        Property(name="java_Expression155", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updaters145: BinaryAssociation = BinaryAssociation(
    name="updaters145",
    ends={
        Property(name="java_Expression147", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement146", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement162: BinaryAssociation = BinaryAssociation(
    name="importedElement162",
    ends={
        Property(name="NamedElement", type=java_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInImports", type=java_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand163: BinaryAssociation = BinaryAssociation(
    name="rightOperand163",
    ends={
        Property(name="java_Expression164", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement156: BinaryAssociation = BinaryAssociation(
    name="thenStatement156",
    ends={
        Property(name="java_Statement158", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement157", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement159: BinaryAssociation = BinaryAssociation(
    name="elseStatement159",
    ends={
        Property(name="java_Statement161", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement160", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand165: BinaryAssociation = BinaryAssociation(
    name="leftOperand165",
    ends={
        Property(name="java_Expression167", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression166", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands168: BinaryAssociation = BinaryAssociation(
    name="extendedOperands168",
    ends={
        Property(name="java_Expression170", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression169", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body171: BinaryAssociation = BinaryAssociation(
    name="body171",
    ends={
        Property(name="java_Block172", type=java_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Initializer", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tags178: BinaryAssociation = BinaryAssociation(
    name="tags178",
    ends={
        Property(name="java_TagElement", type=java_Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Javadoc", type=java_TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body179: BinaryAssociation = BinaryAssociation(
    name="body179",
    ends={
        Property(name="java_Statement180", type=java_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_LabeledStatement", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand173: BinaryAssociation = BinaryAssociation(
    name="rightOperand173",
    ends={
        Property(name="java_TypeAccess174", type=java_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InstanceofExpression", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand175: BinaryAssociation = BinaryAssociation(
    name="leftOperand175",
    ends={
        Property(name="java_Expression177", type=java_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InstanceofExpression176", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mainAttributes184: BinaryAssociation = BinaryAssociation(
    name="mainAttributes184",
    ends={
        Property(name="java_ManifestAttribute", type=java_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Manifest185", type=java_ManifestAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryAttributes186: BinaryAssociation = BinaryAssociation(
    name="entryAttributes186",
    ends={
        Property(name="java_ManifestEntry", type=java_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Manifest187", type=java_ManifestEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes188: BinaryAssociation = BinaryAssociation(
    name="attributes188",
    ends={
        Property(name="java_ManifestAttribute190", type=java_ManifestEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ManifestEntry189", type=java_ManifestAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usagesInBreakStatements181: BinaryAssociation = BinaryAssociation(
    name="usagesInBreakStatements181",
    ends={
        Property(name="BreakStatement", type=java_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=java_BreakStatement, multiplicity=Multiplicity(0, 9999))
    }
)
usagesInContinueStatements182: BinaryAssociation = BinaryAssociation(
    name="usagesInContinueStatements182",
    ends={
        Property(name="ContinueStatement", type=java_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="label183", type=java_ContinueStatement, multiplicity=Multiplicity(0, 9999))
    }
)
returnType195: BinaryAssociation = BinaryAssociation(
    name="returnType195",
    ends={
        Property(name="java_TypeAccess196", type=java_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodDeclaration", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedMethodDeclaration198: BinaryAssociation = BinaryAssociation(
    name="redefinedMethodDeclaration198",
    ends={
        Property(name="MethodDeclaration", type=java_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinitions", type=java_MethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
redefinitions200: BinaryAssociation = BinaryAssociation(
    name="redefinitions200",
    ends={
        Property(name="MethodDeclaration201", type=java_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinedMethodDeclaration", type=java_MethodDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
expression202: BinaryAssociation = BinaryAssociation(
    name="expression202",
    ends={
        Property(name="java_Expression203", type=java_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodInvocation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member191: BinaryAssociation = BinaryAssociation(
    name="member191",
    ends={
        Property(name="java_NamedElement", type=java_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MemberRef", type=java_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
qualifier192: BinaryAssociation = BinaryAssociation(
    name="qualifier192",
    ends={
        Property(name="java_TypeAccess194", type=java_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MemberRef193", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier206: BinaryAssociation = BinaryAssociation(
    name="qualifier206",
    ends={
        Property(name="java_MethodRef", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="java_TypeAccess207", type=java_MethodRef, multiplicity=Multiplicity(1, 1))
    }
)
parameters208: BinaryAssociation = BinaryAssociation(
    name="parameters208",
    ends={
        Property(name="java_MethodRefParameter", type=java_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodRef209", type=java_MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type210: BinaryAssociation = BinaryAssociation(
    name="type210",
    ends={
        Property(name="java_TypeAccess212", type=java_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodRefParameter211", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
method204: BinaryAssociation = BinaryAssociation(
    name="method204",
    ends={
        Property(name="AbstractMethodDeclaration205", type=java_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInDocComments", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
compilationUnits218: BinaryAssociation = BinaryAssociation(
    name="compilationUnits218",
    ends={
        Property(name="java_CompilationUnit220", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model219", type=java_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archives221: BinaryAssociation = BinaryAssociation(
    name="archives221",
    ends={
        Property(name="java_Archive223", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model222", type=java_Archive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElements213: BinaryAssociation = BinaryAssociation(
    name="ownedElements213",
    ends={
        Property(name="Package214", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orphanTypes215: BinaryAssociation = BinaryAssociation(
    name="orphanTypes215",
    ends={
        Property(name="java_Type", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model", type=java_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unresolvedItems216: BinaryAssociation = BinaryAssociation(
    name="unresolvedItems216",
    ends={
        Property(name="java_UnresolvedItem", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model217", type=java_UnresolvedItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
singleVariableDeclaration226: BinaryAssociation = BinaryAssociation(
    name="singleVariableDeclaration226",
    ends={
        Property(name="SingleVariableDeclaration228", type=java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier227", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclarationStatement229: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationStatement229",
    ends={
        Property(name="VariableDeclarationStatement", type=java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier230", type=java_VariableDeclarationStatement, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclarationExpression231: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationExpression231",
    ends={
        Property(name="VariableDeclarationExpression", type=java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier232", type=java_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1))
    }
)
usagesInImports233: BinaryAssociation = BinaryAssociation(
    name="usagesInImports233",
    ends={
        Property(name="ImportDeclaration", type=java_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="importedElement", type=java_ImportDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
bodyDeclaration224: BinaryAssociation = BinaryAssociation(
    name="bodyDeclaration224",
    ends={
        Property(name="BodyDeclaration225", type=java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier", type=java_BodyDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ownedElements234: BinaryAssociation = BinaryAssociation(
    name="ownedElements234",
    ends={
        Property(name="AbstractTypeDeclaration235", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model236: BinaryAssociation = BinaryAssociation(
    name="model236",
    ends={
        Property(name="Model", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements237", type=java_Model, multiplicity=Multiplicity(0, 1))
    }
)
ownedPackages239: BinaryAssociation = BinaryAssociation(
    name="ownedPackages239",
    ends={
        Property(name="Package241", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package240", type=java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package243: BinaryAssociation = BinaryAssociation(
    name="package243",
    ends={
        Property(name="Package244", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPackages", type=java_Package, multiplicity=Multiplicity(0, 1))
    }
)
usagesInPackageAccess245: BinaryAssociation = BinaryAssociation(
    name="usagesInPackageAccess245",
    ends={
        Property(name="PackageAccess", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package246", type=java_PackageAccess, multiplicity=Multiplicity(0, 9999))
    }
)
type251: BinaryAssociation = BinaryAssociation(
    name="type251",
    ends={
        Property(name="java_TypeAccess252", type=java_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParameterizedType", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments253: BinaryAssociation = BinaryAssociation(
    name="typeArguments253",
    ends={
        Property(name="java_TypeAccess255", type=java_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParameterizedType254", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression256: BinaryAssociation = BinaryAssociation(
    name="expression256",
    ends={
        Property(name="java_Expression257", type=java_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParenthesizedExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
package247: BinaryAssociation = BinaryAssociation(
    name="package247",
    ends={
        Property(name="Package248", type=java_PackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInPackageAccess", type=java_Package, multiplicity=Multiplicity(1, 1))
    }
)
qualifier250: BinaryAssociation = BinaryAssociation(
    name="qualifier250",
    ends={
        Property(name="java_PackageAccess", type=java_PackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PackageAccess249", type=java_PackageAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand260: BinaryAssociation = BinaryAssociation(
    name="operand260",
    ends={
        Property(name="java_Expression261", type=java_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PrefixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand258: BinaryAssociation = BinaryAssociation(
    name="operand258",
    ends={
        Property(name="java_Expression259", type=java_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PostfixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression262: BinaryAssociation = BinaryAssociation(
    name="expression262",
    ends={
        Property(name="java_Expression263", type=java_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ReturnStatement", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable264: BinaryAssociation = BinaryAssociation(
    name="variable264",
    ends={
        Property(name="VariableDeclaration", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usageInVariableAccess", type=java_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
modifier268: BinaryAssociation = BinaryAssociation(
    name="modifier268",
    ends={
        Property(name="Modifier269", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="singleVariableDeclaration", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type270: BinaryAssociation = BinaryAssociation(
    name="type270",
    ends={
        Property(name="java_TypeAccess271", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableDeclaration", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations272: BinaryAssociation = BinaryAssociation(
    name="annotations272",
    ends={
        Property(name="java_Annotation274", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableDeclaration273", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodDeclaration275: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration275",
    ends={
        Property(name="AbstractMethodDeclaration276", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
catchClause277: BinaryAssociation = BinaryAssociation(
    name="catchClause277",
    ends={
        Property(name="CatchClause", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="exception", type=java_CatchClause, multiplicity=Multiplicity(0, 1))
    }
)
enhancedForStatement278: BinaryAssociation = BinaryAssociation(
    name="enhancedForStatement278",
    ends={
        Property(name="EnhancedForStatement", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=java_EnhancedForStatement, multiplicity=Multiplicity(0, 1))
    }
)
qualifier265: BinaryAssociation = BinaryAssociation(
    name="qualifier265",
    ends={
        Property(name="java_Expression267", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableAccess266", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression279: BinaryAssociation = BinaryAssociation(
    name="expression279",
    ends={
        Property(name="java_Expression280", type=java_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SuperConstructorInvocation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field281: BinaryAssociation = BinaryAssociation(
    name="field281",
    ends={
        Property(name="java_SingleVariableAccess282", type=java_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SuperFieldAccess", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression285: BinaryAssociation = BinaryAssociation(
    name="expression285",
    ends={
        Property(name="java_Expression286", type=java_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements287: BinaryAssociation = BinaryAssociation(
    name="statements287",
    ends={
        Property(name="java_Statement289", type=java_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchStatement288", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body290: BinaryAssociation = BinaryAssociation(
    name="body290",
    ends={
        Property(name="java_Block291", type=java_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SynchronizedStatement", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression292: BinaryAssociation = BinaryAssociation(
    name="expression292",
    ends={
        Property(name="java_Expression294", type=java_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SynchronizedStatement293", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression283: BinaryAssociation = BinaryAssociation(
    name="expression283",
    ends={
        Property(name="java_Expression284", type=java_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchCase", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression298: BinaryAssociation = BinaryAssociation(
    name="expression298",
    ends={
        Property(name="java_Expression299", type=java_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ThrowStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body300: BinaryAssociation = BinaryAssociation(
    name="body300",
    ends={
        Property(name="java_Block301", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally302: BinaryAssociation = BinaryAssociation(
    name="finally302",
    ends={
        Property(name="java_Block304", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement303", type=java_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses305: BinaryAssociation = BinaryAssociation(
    name="catchClauses305",
    ends={
        Property(name="java_CatchClause307", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement306", type=java_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments295: BinaryAssociation = BinaryAssociation(
    name="fragments295",
    ends={
        Property(name="java_ASTNode297", type=java_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TagElement296", type=java_ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type309: BinaryAssociation = BinaryAssociation(
    name="type309",
    ends={
        Property(name="Type", type=java_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInTypeAccess", type=java_Type, multiplicity=Multiplicity(1, 1))
    }
)
qualifier310: BinaryAssociation = BinaryAssociation(
    name="qualifier310",
    ends={
        Property(name="java_NamespaceAccess", type=java_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeAccess311", type=java_NamespaceAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters312: BinaryAssociation = BinaryAssociation(
    name="typeParameters312",
    ends={
        Property(name="java_TypeParameter313", type=java_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeDeclaration", type=java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration314: BinaryAssociation = BinaryAssociation(
    name="declaration314",
    ends={
        Property(name="java_AbstractTypeDeclaration315", type=java_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeDeclarationStatement", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usagesInTypeAccess308: BinaryAssociation = BinaryAssociation(
    name="usagesInTypeAccess308",
    ends={
        Property(name="TypeAccess", type=java_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
bounds318: BinaryAssociation = BinaryAssociation(
    name="bounds318",
    ends={
        Property(name="java_TypeAccess320", type=java_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeParameter319", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element321: BinaryAssociation = BinaryAssociation(
    name="element321",
    ends={
        Property(name="java_UnresolvedItem322", type=java_UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_UnresolvedItemAccess", type=java_UnresolvedItem, multiplicity=Multiplicity(0, 1))
    }
)
qualifier323: BinaryAssociation = BinaryAssociation(
    name="qualifier323",
    ends={
        Property(name="java_ASTNode325", type=java_UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_UnresolvedItemAccess324", type=java_ASTNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type316: BinaryAssociation = BinaryAssociation(
    name="type316",
    ends={
        Property(name="java_TypeAccess317", type=java_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeLiteral", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer326: BinaryAssociation = BinaryAssociation(
    name="initializer326",
    ends={
        Property(name="java_Expression327", type=java_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_VariableDeclaration", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usageInVariableAccess328: BinaryAssociation = BinaryAssociation(
    name="usageInVariableAccess328",
    ends={
        Property(name="SingleVariableAccess", type=java_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=java_SingleVariableAccess, multiplicity=Multiplicity(0, 9999))
    }
)
variablesContainer333: BinaryAssociation = BinaryAssociation(
    name="variablesContainer333",
    ends={
        Property(name="AbstractVariablesContainer", type=java_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(0, 1))
    }
)
modifier334: BinaryAssociation = BinaryAssociation(
    name="modifier334",
    ends={
        Property(name="Modifier335", type=java_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationStatement", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifier329: BinaryAssociation = BinaryAssociation(
    name="modifier329",
    ends={
        Property(name="Modifier330", type=java_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationExpression", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations331: BinaryAssociation = BinaryAssociation(
    name="annotations331",
    ends={
        Property(name="java_Annotation332", type=java_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_VariableDeclarationExpression", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bound338: BinaryAssociation = BinaryAssociation(
    name="bound338",
    ends={
        Property(name="java_TypeAccess339", type=java_WildCardType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WildCardType", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression340: BinaryAssociation = BinaryAssociation(
    name="expression340",
    ends={
        Property(name="java_Expression341", type=java_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WhileStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body342: BinaryAssociation = BinaryAssociation(
    name="body342",
    ends={
        Property(name="java_Statement344", type=java_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WhileStatement343", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations336: BinaryAssociation = BinaryAssociation(
    name="annotations336",
    ends={
        Property(name="java_Annotation337", type=java_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_VariableDeclarationStatement", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_java_AbstractMethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AbstractMethodDeclaration)
gen_java_AbstractMethodInvocation_ASTNode = Generalization(general=ASTNode, specific=java_AbstractMethodInvocation)
gen_java_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AbstractTypeDeclaration)
gen_java_AbstractTypeDeclaration_Type = Generalization(general=Type, specific=java_AbstractTypeDeclaration)
gen_java_AbstractVariablesContainer_ASTNode = Generalization(general=ASTNode, specific=java_AbstractVariablesContainer)
gen_java_Annotation_Expression = Generalization(general=Expression, specific=java_Annotation)
gen_java_Archive_NamedElement = Generalization(general=NamedElement, specific=java_Archive)
gen_java_AssertStatement_Statement = Generalization(general=Statement, specific=java_AssertStatement)
gen_java_AbstractTypeQualifiedExpression_Expression = Generalization(general=Expression, specific=java_AbstractTypeQualifiedExpression)
gen_java_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_AnnotationTypeDeclaration)
gen_java_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AnnotationTypeMemberDeclaration)
gen_java_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=java_AnonymousClassDeclaration)
gen_java_ArrayAccess_Expression = Generalization(general=Expression, specific=java_ArrayAccess)
gen_java_AnnotationMemberValuePair_NamedElement = Generalization(general=NamedElement, specific=java_AnnotationMemberValuePair)
gen_java_ArrayLengthAccess_Expression = Generalization(general=Expression, specific=java_ArrayLengthAccess)
gen_java_ArrayType_Type = Generalization(general=Type, specific=java_ArrayType)
gen_java_Assignment_Expression = Generalization(general=Expression, specific=java_Assignment)
gen_java_ArrayCreation_Expression = Generalization(general=Expression, specific=java_ArrayCreation)
gen_java_ArrayInitializer_Expression = Generalization(general=Expression, specific=java_ArrayInitializer)
gen_java_BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=java_BodyDeclaration)
gen_java_BlockComment_Comment = Generalization(general=Comment, specific=java_BlockComment)
gen_java_Block_Statement = Generalization(general=Statement, specific=java_Block)
gen_java_BreakStatement_Statement = Generalization(general=Statement, specific=java_BreakStatement)
gen_java_CastExpression_Expression = Generalization(general=Expression, specific=java_CastExpression)
gen_java_BooleanLiteral_Expression = Generalization(general=Expression, specific=java_BooleanLiteral)
gen_java_CatchClause_Statement = Generalization(general=Statement, specific=java_CatchClause)
gen_java_CharacterLiteral_Expression = Generalization(general=Expression, specific=java_CharacterLiteral)
gen_java_ConstructorInvocation_Statement = Generalization(general=Statement, specific=java_ConstructorInvocation)
gen_java_ConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_ConstructorInvocation)
gen_java_ConstructorDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=java_ConstructorDeclaration)
gen_java_ConditionalExpression_Expression = Generalization(general=Expression, specific=java_ConditionalExpression)
gen_java_Comment_ASTNode = Generalization(general=ASTNode, specific=java_Comment)
gen_java_CompilationUnit_NamedElement = Generalization(general=NamedElement, specific=java_CompilationUnit)
gen_java_ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=java_ClassDeclaration)
gen_java_ContinueStatement_Statement = Generalization(general=Statement, specific=java_ContinueStatement)
gen_java_DoStatement_Statement = Generalization(general=Statement, specific=java_DoStatement)
gen_java_EnhancedForStatement_Statement = Generalization(general=Statement, specific=java_EnhancedForStatement)
gen_java_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_EnumConstantDeclaration)
gen_java_EmptyStatement_Statement = Generalization(general=Statement, specific=java_EmptyStatement)
gen_java_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_EnumDeclaration)
gen_java_Expression_ASTNode = Generalization(general=ASTNode, specific=java_Expression)
gen_java_ExpressionStatement_Statement = Generalization(general=Statement, specific=java_ExpressionStatement)
gen_java_EnumConstantDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_EnumConstantDeclaration)
gen_java_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_FieldDeclaration)
gen_java_FieldDeclaration_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_FieldDeclaration)
gen_java_ForStatement_Statement = Generalization(general=Statement, specific=java_ForStatement)
gen_java_FieldAccess_Expression = Generalization(general=Expression, specific=java_FieldAccess)
gen_java_IfStatement_Statement = Generalization(general=Statement, specific=java_IfStatement)
gen_java_InfixExpression_Expression = Generalization(general=Expression, specific=java_InfixExpression)
gen_java_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=java_ImportDeclaration)
gen_java_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_Initializer)
gen_java_InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=java_InterfaceDeclaration)
gen_java_Javadoc_Comment = Generalization(general=Comment, specific=java_Javadoc)
gen_java_LabeledStatement_NamedElement = Generalization(general=NamedElement, specific=java_LabeledStatement)
gen_java_LabeledStatement_Statement = Generalization(general=Statement, specific=java_LabeledStatement)
gen_java_InstanceofExpression_Expression = Generalization(general=Expression, specific=java_InstanceofExpression)
gen_java_LineComment_Comment = Generalization(general=Comment, specific=java_LineComment)
gen_java_MethodDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=java_MethodDeclaration)
gen_java_MethodInvocation_Expression = Generalization(general=Expression, specific=java_MethodInvocation)
gen_java_MethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_MethodInvocation)
gen_java_MemberRef_ASTNode = Generalization(general=ASTNode, specific=java_MemberRef)
gen_java_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=java_MethodRefParameter)
gen_java_MethodRef_ASTNode = Generalization(general=ASTNode, specific=java_MethodRef)
gen_java_Modifier_ASTNode = Generalization(general=ASTNode, specific=java_Modifier)
gen_java_NamedElement_ASTNode = Generalization(general=ASTNode, specific=java_NamedElement)
gen_java_NamespaceAccess_ASTNode = Generalization(general=ASTNode, specific=java_NamespaceAccess)
gen_java_PackageAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java_PackageAccess)
gen_java_NumberLiteral_Expression = Generalization(general=Expression, specific=java_NumberLiteral)
gen_java_NullLiteral_Expression = Generalization(general=Expression, specific=java_NullLiteral)
gen_java_Package_NamedElement = Generalization(general=NamedElement, specific=java_Package)
gen_java_ParameterizedType_Type = Generalization(general=Type, specific=java_ParameterizedType)
gen_java_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=java_ParenthesizedExpression)
gen_java_PostfixExpression_Expression = Generalization(general=Expression, specific=java_PostfixExpression)
gen_java_PrefixExpression_Expression = Generalization(general=Expression, specific=java_PrefixExpression)
gen_java_PrimitiveType_Type = Generalization(general=Type, specific=java_PrimitiveType)
gen_java_PrimitiveTypeShort_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeShort)
gen_java_PrimitiveTypeFloat_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeFloat)
gen_java_PrimitiveTypeInt_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeInt)
gen_java_PrimitiveTypeLong_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeLong)
gen_java_PrimitiveTypeVoid_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeVoid)
gen_java_ReturnStatement_Statement = Generalization(general=Statement, specific=java_ReturnStatement)
gen_java_SingleVariableAccess_Expression = Generalization(general=Expression, specific=java_SingleVariableAccess)
gen_java_PrimitiveTypeBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeBoolean)
gen_java_PrimitiveTypeByte_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeByte)
gen_java_PrimitiveTypeChar_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeChar)
gen_java_PrimitiveTypeDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeDouble)
gen_java_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_SingleVariableDeclaration)
gen_java_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=java_SuperConstructorInvocation)
gen_java_SuperConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_SuperConstructorInvocation)
gen_java_SuperFieldAccess_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_SuperFieldAccess)
gen_java_SuperMethodInvocation_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_SuperMethodInvocation)
gen_java_SuperMethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_SuperMethodInvocation)
gen_java_SwitchCase_Statement = Generalization(general=Statement, specific=java_SwitchCase)
gen_java_Statement_ASTNode = Generalization(general=ASTNode, specific=java_Statement)
gen_java_StringLiteral_Expression = Generalization(general=Expression, specific=java_StringLiteral)
gen_java_SynchronizedStatement_Statement = Generalization(general=Statement, specific=java_SynchronizedStatement)
gen_java_TagElement_ASTNode = Generalization(general=ASTNode, specific=java_TagElement)
gen_java_SwitchStatement_Statement = Generalization(general=Statement, specific=java_SwitchStatement)
gen_java_ThisExpression_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_ThisExpression)
gen_java_ThrowStatement_Statement = Generalization(general=Statement, specific=java_ThrowStatement)
gen_java_TryStatement_Statement = Generalization(general=Statement, specific=java_TryStatement)
gen_java_TextElement_ASTNode = Generalization(general=ASTNode, specific=java_TextElement)
gen_java_TypeAccess_Expression = Generalization(general=Expression, specific=java_TypeAccess)
gen_java_TypeAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java_TypeAccess)
gen_java_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_TypeDeclaration)
gen_java_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=java_TypeDeclarationStatement)
gen_java_Type_NamedElement = Generalization(general=NamedElement, specific=java_Type)
gen_java_TypeParameter_Type = Generalization(general=Type, specific=java_TypeParameter)
gen_java_UnresolvedItem_NamedElement = Generalization(general=NamedElement, specific=java_UnresolvedItem)
gen_java_UnresolvedItemAccess_Expression = Generalization(general=Expression, specific=java_UnresolvedItemAccess)
gen_java_UnresolvedItemAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java_UnresolvedItemAccess)
gen_java_UnresolvedAnnotationDeclaration_AnnotationTypeDeclaration = Generalization(general=AnnotationTypeDeclaration, specific=java_UnresolvedAnnotationDeclaration)
gen_java_UnresolvedAnnotationDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedAnnotationDeclaration)
gen_java_TypeLiteral_Expression = Generalization(general=Expression, specific=java_TypeLiteral)
gen_java_UnresolvedClassDeclaration_ClassDeclaration = Generalization(general=ClassDeclaration, specific=java_UnresolvedClassDeclaration)
gen_java_UnresolvedClassDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedClassDeclaration)
gen_java_UnresolvedEnumDeclaration_EnumDeclaration = Generalization(general=EnumDeclaration, specific=java_UnresolvedEnumDeclaration)
gen_java_UnresolvedEnumDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedEnumDeclaration)
gen_java_UnresolvedInterfaceDeclaration_InterfaceDeclaration = Generalization(general=InterfaceDeclaration, specific=java_UnresolvedInterfaceDeclaration)
gen_java_UnresolvedInterfaceDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedInterfaceDeclaration)
gen_java_UnresolvedLabeledStatement_LabeledStatement = Generalization(general=LabeledStatement, specific=java_UnresolvedLabeledStatement)
gen_java_UnresolvedLabeledStatement_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedLabeledStatement)
gen_java_UnresolvedMethodDeclaration_MethodDeclaration = Generalization(general=MethodDeclaration, specific=java_UnresolvedMethodDeclaration)
gen_java_UnresolvedMethodDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedMethodDeclaration)
gen_java_UnresolvedSingleVariableDeclaration_SingleVariableDeclaration = Generalization(general=SingleVariableDeclaration, specific=java_UnresolvedSingleVariableDeclaration)
gen_java_UnresolvedSingleVariableDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedSingleVariableDeclaration)
gen_java_UnresolvedVariableDeclarationFragment_VariableDeclarationFragment = Generalization(general=VariableDeclarationFragment, specific=java_UnresolvedVariableDeclarationFragment)
gen_java_UnresolvedAnnotationTypeMemberDeclaration_AnnotationTypeMemberDeclaration = Generalization(general=AnnotationTypeMemberDeclaration, specific=java_UnresolvedAnnotationTypeMemberDeclaration)
gen_java_UnresolvedVariableDeclarationFragment_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedVariableDeclarationFragment)
gen_java_UnresolvedAnnotationTypeMemberDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedAnnotationTypeMemberDeclaration)
gen_java_VariableDeclaration_NamedElement = Generalization(general=NamedElement, specific=java_VariableDeclaration)
gen_java_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=java_VariableDeclarationExpression)
gen_java_VariableDeclarationExpression_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_VariableDeclarationExpression)
gen_java_UnresolvedType_Type = Generalization(general=Type, specific=java_UnresolvedType)
gen_java_UnresolvedType_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedType)
gen_java_UnresolvedTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_UnresolvedTypeDeclaration)
gen_java_UnresolvedTypeDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedTypeDeclaration)
gen_java_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_VariableDeclarationFragment)
gen_java_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=java_VariableDeclarationStatement)
gen_java_VariableDeclarationStatement_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_VariableDeclarationStatement)
gen_java_WildCardType_Type = Generalization(general=Type, specific=java_WildCardType)
gen_java_WhileStatement_Statement = Generalization(general=Statement, specific=java_WhileStatement)

# Domain Model
domain_model = DomainModel(
    name="java",
    types={java_AbstractMethodDeclaration, BodyDeclaration, java_TypeParameter, java_MethodRef, java_AbstractMethodInvocation, ASTNode, java_Expression, java_AbstractTypeDeclaration, Type, java_BodyDeclaration, java_Block, java_SingleVariableDeclaration, java_TypeAccess, java_AbstractVariablesContainer, java_VariableDeclarationFragment, java_Annotation, java_AnnotationMemberValuePair, java_Archive, NamedElement, java_Manifest, java_AssertStatement, Statement, java_Comment, java_Package, java_AbstractTypeQualifiedExpression, Expression, java_AnnotationTypeDeclaration, AbstractTypeDeclaration, java_AnonymousClassDeclaration, java_ArrayAccess, java_ASTNode, java_CompilationUnit, java_AnnotationTypeMemberDeclaration, java_ArrayLengthAccess, java_ArrayType, java_Assignment, java_ArrayCreation, java_ArrayInitializer, java_BlockComment, Comment, java_Statement, java_BreakStatement, java_LabeledStatement, java_CastExpression, java_Modifier, java_BooleanLiteral, java_CatchClause, java_CharacterLiteral, java_ConstructorInvocation, AbstractMethodInvocation, java_ConstructorDeclaration, AbstractMethodDeclaration, java_ConditionalExpression, java_ClassDeclaration, TypeDeclaration, java_ContinueStatement, java_DoStatement, java_ImportDeclaration, java_EnumConstantDeclaration, VariableDeclaration, java_EmptyStatement, java_EnhancedForStatement, java_EnumDeclaration, java_ExpressionStatement, java_FieldDeclaration, AbstractVariablesContainer, java_ForStatement, java_FieldAccess, java_SingleVariableAccess, java_IfStatement, java_NamedElement, java_InfixExpression, java_Initializer, java_InstanceofExpression, java_InterfaceDeclaration, java_Javadoc, java_TagElement, java_ManifestAttribute, java_ManifestEntry, java_LineComment, java_MethodDeclaration, java_MethodInvocation, java_MemberRef, java_MethodRefParameter, java_Model, java_Type, java_UnresolvedItem, java_VariableDeclarationStatement, java_VariableDeclarationExpression, java_NamespaceAccess, java_NumberLiteral, java_PackageAccess, NamespaceAccess, java_NullLiteral, java_ParameterizedType, java_ParenthesizedExpression, java_PostfixExpression, java_PrefixExpression, java_PrimitiveType, java_PrimitiveTypeBoolean, java_PrimitiveTypeShort, java_PrimitiveTypeFloat, java_PrimitiveTypeInt, java_PrimitiveTypeLong, java_PrimitiveTypeVoid, java_ReturnStatement, java_VariableDeclaration, PrimitiveType, java_PrimitiveTypeByte, java_PrimitiveTypeChar, java_PrimitiveTypeDouble, java_SuperConstructorInvocation, java_SuperFieldAccess, AbstractTypeQualifiedExpression, java_SuperMethodInvocation, java_SwitchCase, java_StringLiteral, java_SynchronizedStatement, java_SwitchStatement, java_ThisExpression, java_ThrowStatement, java_TryStatement, java_TextElement, java_TypeDeclaration, java_TypeDeclarationStatement, java_UnresolvedItemAccess, java_UnresolvedAnnotationDeclaration, AnnotationTypeDeclaration, UnresolvedItem, java_TypeLiteral, java_UnresolvedClassDeclaration, ClassDeclaration, java_UnresolvedEnumDeclaration, EnumDeclaration, java_UnresolvedInterfaceDeclaration, InterfaceDeclaration, java_UnresolvedLabeledStatement, LabeledStatement, java_UnresolvedMethodDeclaration, MethodDeclaration, java_UnresolvedSingleVariableDeclaration, SingleVariableDeclaration, java_UnresolvedAnnotationTypeMemberDeclaration, AnnotationTypeMemberDeclaration, java_UnresolvedVariableDeclarationFragment, VariableDeclarationFragment, java_UnresolvedType, java_UnresolvedTypeDeclaration, java_WildCardType, java_WhileStatement, AssignmentKind, InfixExpressionKind, InheritanceKind, PrefixExpressionKind, PostfixExpressionKind, VisibilityKind},
    associations={typeParameters4, usagesInDocComments6, usages7, method9, arguments10, typeArguments11, bodyDeclarations14, body0, parameters1, thrownExceptions2, qualifier23, type25, fragments27, type28, values30, manifest32, message33, commentsBeforeBody15, commentsAfterBody16, package19, superInterfaces20, value44, default47, type49, usages52, bodyDeclarations53, array55, index57, expression35, comments38, originalCompilationUnit40, member42, array70, elementType72, leftHandSide74, rightHandSide76, dimensions60, initializer62, type64, expressions67, abstractTypeDeclaration79, annotations80, statements85, label87, anonymousClassDeclarationOwner82, modifier84, exception93, body95, expression88, type90, expression99, thenExpression102, elseExpression97, commentList107, superClass105, types114, label117, expression119, imports110, package112, body124, expression126, parameter129, body121, enumConstants135, expression137, anonymousClassDeclaration131, arguments132, field139, expression140, expression143, initializers148, body151, expression154, updaters145, importedElement162, rightOperand163, thenStatement156, elseStatement159, leftOperand165, extendedOperands168, body171, tags178, body179, rightOperand173, leftOperand175, mainAttributes184, entryAttributes186, attributes188, usagesInBreakStatements181, usagesInContinueStatements182, returnType195, redefinedMethodDeclaration198, redefinitions200, expression202, member191, qualifier192, qualifier206, parameters208, type210, method204, compilationUnits218, archives221, ownedElements213, orphanTypes215, unresolvedItems216, singleVariableDeclaration226, variableDeclarationStatement229, variableDeclarationExpression231, usagesInImports233, bodyDeclaration224, ownedElements234, model236, ownedPackages239, package243, usagesInPackageAccess245, type251, typeArguments253, expression256, package247, qualifier250, operand260, operand258, expression262, variable264, modifier268, type270, annotations272, methodDeclaration275, catchClause277, enhancedForStatement278, qualifier265, expression279, field281, expression285, statements287, body290, expression292, expression283, expression298, body300, finally302, catchClauses305, fragments295, type309, qualifier310, typeParameters312, declaration314, usagesInTypeAccess308, bounds318, element321, qualifier323, type316, initializer326, usageInVariableAccess328, variablesContainer333, modifier334, modifier329, annotations331, bound338, expression340, body342, annotations336},
    generalizations={gen_java_AbstractMethodDeclaration_BodyDeclaration, gen_java_AbstractMethodInvocation_ASTNode, gen_java_AbstractTypeDeclaration_BodyDeclaration, gen_java_AbstractTypeDeclaration_Type, gen_java_AbstractVariablesContainer_ASTNode, gen_java_Annotation_Expression, gen_java_Archive_NamedElement, gen_java_AssertStatement_Statement, gen_java_AbstractTypeQualifiedExpression_Expression, gen_java_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_java_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_java_AnonymousClassDeclaration_ASTNode, gen_java_ArrayAccess_Expression, gen_java_AnnotationMemberValuePair_NamedElement, gen_java_ArrayLengthAccess_Expression, gen_java_ArrayType_Type, gen_java_Assignment_Expression, gen_java_ArrayCreation_Expression, gen_java_ArrayInitializer_Expression, gen_java_BodyDeclaration_NamedElement, gen_java_BlockComment_Comment, gen_java_Block_Statement, gen_java_BreakStatement_Statement, gen_java_CastExpression_Expression, gen_java_BooleanLiteral_Expression, gen_java_CatchClause_Statement, gen_java_CharacterLiteral_Expression, gen_java_ConstructorInvocation_Statement, gen_java_ConstructorInvocation_AbstractMethodInvocation, gen_java_ConstructorDeclaration_AbstractMethodDeclaration, gen_java_ConditionalExpression_Expression, gen_java_Comment_ASTNode, gen_java_CompilationUnit_NamedElement, gen_java_ClassDeclaration_TypeDeclaration, gen_java_ContinueStatement_Statement, gen_java_DoStatement_Statement, gen_java_EnhancedForStatement_Statement, gen_java_EnumConstantDeclaration_BodyDeclaration, gen_java_EmptyStatement_Statement, gen_java_EnumDeclaration_AbstractTypeDeclaration, gen_java_Expression_ASTNode, gen_java_ExpressionStatement_Statement, gen_java_EnumConstantDeclaration_VariableDeclaration, gen_java_FieldDeclaration_BodyDeclaration, gen_java_FieldDeclaration_AbstractVariablesContainer, gen_java_ForStatement_Statement, gen_java_FieldAccess_Expression, gen_java_IfStatement_Statement, gen_java_InfixExpression_Expression, gen_java_ImportDeclaration_ASTNode, gen_java_Initializer_BodyDeclaration, gen_java_InterfaceDeclaration_TypeDeclaration, gen_java_Javadoc_Comment, gen_java_LabeledStatement_NamedElement, gen_java_LabeledStatement_Statement, gen_java_InstanceofExpression_Expression, gen_java_LineComment_Comment, gen_java_MethodDeclaration_AbstractMethodDeclaration, gen_java_MethodInvocation_Expression, gen_java_MethodInvocation_AbstractMethodInvocation, gen_java_MemberRef_ASTNode, gen_java_MethodRefParameter_ASTNode, gen_java_MethodRef_ASTNode, gen_java_Modifier_ASTNode, gen_java_NamedElement_ASTNode, gen_java_NamespaceAccess_ASTNode, gen_java_PackageAccess_NamespaceAccess, gen_java_NumberLiteral_Expression, gen_java_NullLiteral_Expression, gen_java_Package_NamedElement, gen_java_ParameterizedType_Type, gen_java_ParenthesizedExpression_Expression, gen_java_PostfixExpression_Expression, gen_java_PrefixExpression_Expression, gen_java_PrimitiveType_Type, gen_java_PrimitiveTypeShort_PrimitiveType, gen_java_PrimitiveTypeFloat_PrimitiveType, gen_java_PrimitiveTypeInt_PrimitiveType, gen_java_PrimitiveTypeLong_PrimitiveType, gen_java_PrimitiveTypeVoid_PrimitiveType, gen_java_ReturnStatement_Statement, gen_java_SingleVariableAccess_Expression, gen_java_PrimitiveTypeBoolean_PrimitiveType, gen_java_PrimitiveTypeByte_PrimitiveType, gen_java_PrimitiveTypeChar_PrimitiveType, gen_java_PrimitiveTypeDouble_PrimitiveType, gen_java_SingleVariableDeclaration_VariableDeclaration, gen_java_SuperConstructorInvocation_Statement, gen_java_SuperConstructorInvocation_AbstractMethodInvocation, gen_java_SuperFieldAccess_AbstractTypeQualifiedExpression, gen_java_SuperMethodInvocation_AbstractTypeQualifiedExpression, gen_java_SuperMethodInvocation_AbstractMethodInvocation, gen_java_SwitchCase_Statement, gen_java_Statement_ASTNode, gen_java_StringLiteral_Expression, gen_java_SynchronizedStatement_Statement, gen_java_TagElement_ASTNode, gen_java_SwitchStatement_Statement, gen_java_ThisExpression_AbstractTypeQualifiedExpression, gen_java_ThrowStatement_Statement, gen_java_TryStatement_Statement, gen_java_TextElement_ASTNode, gen_java_TypeAccess_Expression, gen_java_TypeAccess_NamespaceAccess, gen_java_TypeDeclaration_AbstractTypeDeclaration, gen_java_TypeDeclarationStatement_Statement, gen_java_Type_NamedElement, gen_java_TypeParameter_Type, gen_java_UnresolvedItem_NamedElement, gen_java_UnresolvedItemAccess_Expression, gen_java_UnresolvedItemAccess_NamespaceAccess, gen_java_UnresolvedAnnotationDeclaration_AnnotationTypeDeclaration, gen_java_UnresolvedAnnotationDeclaration_UnresolvedItem, gen_java_TypeLiteral_Expression, gen_java_UnresolvedClassDeclaration_ClassDeclaration, gen_java_UnresolvedClassDeclaration_UnresolvedItem, gen_java_UnresolvedEnumDeclaration_EnumDeclaration, gen_java_UnresolvedEnumDeclaration_UnresolvedItem, gen_java_UnresolvedInterfaceDeclaration_InterfaceDeclaration, gen_java_UnresolvedInterfaceDeclaration_UnresolvedItem, gen_java_UnresolvedLabeledStatement_LabeledStatement, gen_java_UnresolvedLabeledStatement_UnresolvedItem, gen_java_UnresolvedMethodDeclaration_MethodDeclaration, gen_java_UnresolvedMethodDeclaration_UnresolvedItem, gen_java_UnresolvedSingleVariableDeclaration_SingleVariableDeclaration, gen_java_UnresolvedSingleVariableDeclaration_UnresolvedItem, gen_java_UnresolvedVariableDeclarationFragment_VariableDeclarationFragment, gen_java_UnresolvedAnnotationTypeMemberDeclaration_AnnotationTypeMemberDeclaration, gen_java_UnresolvedVariableDeclarationFragment_UnresolvedItem, gen_java_UnresolvedAnnotationTypeMemberDeclaration_UnresolvedItem, gen_java_VariableDeclaration_NamedElement, gen_java_VariableDeclarationExpression_Expression, gen_java_VariableDeclarationExpression_AbstractVariablesContainer, gen_java_UnresolvedType_Type, gen_java_UnresolvedType_UnresolvedItem, gen_java_UnresolvedTypeDeclaration_AbstractTypeDeclaration, gen_java_UnresolvedTypeDeclaration_UnresolvedItem, gen_java_VariableDeclarationFragment_VariableDeclaration, gen_java_VariableDeclarationStatement_Statement, gen_java_VariableDeclarationStatement_AbstractVariablesContainer, gen_java_WildCardType_Type, gen_java_WhileStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)