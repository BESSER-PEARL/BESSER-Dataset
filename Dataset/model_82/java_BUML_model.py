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
			EnumerationLiteral(name="CONDITIONAL_OR"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="DIVIDE")
    }
)

PostfixExpressionKind: Enumeration = Enumeration(
    name="PostfixExpressionKind",
    literals={
            EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT")
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
java_TypeAccess = Class(name="java::TypeAccess")
java_TypeParameter = Class(name="java::TypeParameter")
java_AbstractMethodInvocation = Class(name="java::AbstractMethodInvocation", is_abstract=True)
ASTNode = Class(name="ASTNode")
java_Expression = Class(name="java::Expression", is_abstract=True)
java_AbstractMethodDeclaration = Class(name="java::AbstractMethodDeclaration", is_abstract=True)
BodyDeclaration = Class(name="BodyDeclaration")
java_Block = Class(name="java::Block")
java_SingleVariableDeclaration = Class(name="java::SingleVariableDeclaration")
java_AbstractTypeQualifiedExpression = Class(name="java::AbstractTypeQualifiedExpression", is_abstract=True)
Expression = Class(name="Expression")
java_AbstractVariablesContainer = Class(name="java::AbstractVariablesContainer", is_abstract=True)
java_VariableDeclarationFragment = Class(name="java::VariableDeclarationFragment")
java_AbstractTypeDeclaration = Class(name="java::AbstractTypeDeclaration", is_abstract=True)
Type = Class(name="Type")
java_BodyDeclaration = Class(name="java::BodyDeclaration", is_abstract=True)
java_Comment = Class(name="java::Comment", is_abstract=True)
java_Package = Class(name="java::Package")
java_AssertStatement = Class(name="java::AssertStatement")
Statement = Class(name="Statement")
java_ASTNode = Class(name="java::ASTNode", is_abstract=True)
java_CompilationUnit = Class(name="java::CompilationUnit")
java_Annotation = Class(name="java::Annotation")
java_AnnotationMemberValuePair = Class(name="java::AnnotationMemberValuePair")
java_Archive = Class(name="java::Archive")
NamedElement = Class(name="NamedElement")
java_ClassFile = Class(name="java::ClassFile")
java_Manifest = Class(name="java::Manifest")
java_AnnotationTypeDeclaration = Class(name="java::AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
java_AnonymousClassDeclaration = Class(name="java::AnonymousClassDeclaration")
java_ClassInstanceCreation = Class(name="java::ClassInstanceCreation")
java_AnnotationTypeMemberDeclaration = Class(name="java::AnnotationTypeMemberDeclaration")
java_ArrayInitializer = Class(name="java::ArrayInitializer")
java_ArrayLengthAccess = Class(name="java::ArrayLengthAccess")
java_ArrayType = Class(name="java::ArrayType")
java_ArrayAccess = Class(name="java::ArrayAccess")
java_ArrayCreation = Class(name="java::ArrayCreation")
java_Assignment = Class(name="java::Assignment")
java_BlockComment = Class(name="java::BlockComment")
Comment = Class(name="Comment")
java_Statement = Class(name="java::Statement", is_abstract=True)
java_BreakStatement = Class(name="java::BreakStatement")
java_LabeledStatement = Class(name="java::LabeledStatement")
java_CastExpression = Class(name="java::CastExpression")
java_Modifier = Class(name="java::Modifier")
java_CharacterLiteral = Class(name="java::CharacterLiteral")
java_BooleanLiteral = Class(name="java::BooleanLiteral")
AbstractMethodInvocation = Class(name="AbstractMethodInvocation")
java_CatchClause = Class(name="java::CatchClause")
java_ConstructorDeclaration = Class(name="java::ConstructorDeclaration")
AbstractMethodDeclaration = Class(name="AbstractMethodDeclaration")
java_ConditionalExpression = Class(name="java::ConditionalExpression")
java_ConstructorInvocation = Class(name="java::ConstructorInvocation")
java_ImportDeclaration = Class(name="java::ImportDeclaration")
java_ClassDeclaration = Class(name="java::ClassDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
java_EmptyStatement = Class(name="java::EmptyStatement")
java_EnhancedForStatement = Class(name="java::EnhancedForStatement")
java_ContinueStatement = Class(name="java::ContinueStatement")
java_EnumConstantDeclaration = Class(name="java::EnumConstantDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
java_DoStatement = Class(name="java::DoStatement")
java_EnumDeclaration = Class(name="java::EnumDeclaration")
java_ExpressionStatement = Class(name="java::ExpressionStatement")
java_FieldAccess = Class(name="java::FieldAccess")
java_SingleVariableAccess = Class(name="java::SingleVariableAccess")
java_ForStatement = Class(name="java::ForStatement")
java_IfStatement = Class(name="java::IfStatement")
java_FieldDeclaration = Class(name="java::FieldDeclaration")
AbstractVariablesContainer = Class(name="AbstractVariablesContainer")
java_NamedElement = Class(name="java::NamedElement", is_abstract=True)
java_InfixExpression = Class(name="java::InfixExpression")
java_InstanceofExpression = Class(name="java::InstanceofExpression")
java_InterfaceDeclaration = Class(name="java::InterfaceDeclaration")
java_Javadoc = Class(name="java::Javadoc")
java_TagElement = Class(name="java::TagElement")
java_Initializer = Class(name="java::Initializer")
java_ManifestAttribute = Class(name="java::ManifestAttribute")
java_ManifestEntry = Class(name="java::ManifestEntry")
java_MemberRef = Class(name="java::MemberRef")
java_LineComment = Class(name="java::LineComment")
java_MethodInvocation = Class(name="java::MethodInvocation")
java_MethodRef = Class(name="java::MethodRef")
java_MethodDeclaration = Class(name="java::MethodDeclaration")
java_Model = Class(name="java::Model")
java_Type = Class(name="java::Type", is_abstract=True)
java_UnresolvedItem = Class(name="java::UnresolvedItem")
java_MethodRefParameter = Class(name="java::MethodRefParameter")
java_VariableDeclarationStatement = Class(name="java::VariableDeclarationStatement")
java_VariableDeclarationExpression = Class(name="java::VariableDeclarationExpression")
java_NamespaceAccess = Class(name="java::NamespaceAccess", is_abstract=True)
java_NumberLiteral = Class(name="java::NumberLiteral")
java_NullLiteral = Class(name="java::NullLiteral")
java_PackageAccess = Class(name="java::PackageAccess")
NamespaceAccess = Class(name="NamespaceAccess")
java_ParameterizedType = Class(name="java::ParameterizedType")
java_ParenthesizedExpression = Class(name="java::ParenthesizedExpression")
java_PostfixExpression = Class(name="java::PostfixExpression")
java_PrimitiveTypeInt = Class(name="java::PrimitiveTypeInt")
java_PrimitiveTypeLong = Class(name="java::PrimitiveTypeLong")
java_PrimitiveTypeVoid = Class(name="java::PrimitiveTypeVoid")
java_PrefixExpression = Class(name="java::PrefixExpression")
java_PrimitiveType = Class(name="java::PrimitiveType")
java_PrimitiveTypeBoolean = Class(name="java::PrimitiveTypeBoolean")
PrimitiveType = Class(name="PrimitiveType")
java_PrimitiveTypeByte = Class(name="java::PrimitiveTypeByte")
java_PrimitiveTypeChar = Class(name="java::PrimitiveTypeChar")
java_PrimitiveTypeDouble = Class(name="java::PrimitiveTypeDouble")
java_PrimitiveTypeShort = Class(name="java::PrimitiveTypeShort")
java_PrimitiveTypeFloat = Class(name="java::PrimitiveTypeFloat")
java_ReturnStatement = Class(name="java::ReturnStatement")
java_VariableDeclaration = Class(name="java::VariableDeclaration", is_abstract=True)
java_StringLiteral = Class(name="java::StringLiteral")
java_SuperFieldAccess = Class(name="java::SuperFieldAccess")
AbstractTypeQualifiedExpression = Class(name="AbstractTypeQualifiedExpression")
java_SuperMethodInvocation = Class(name="java::SuperMethodInvocation")
java_SwitchCase = Class(name="java::SwitchCase")
java_SwitchStatement = Class(name="java::SwitchStatement")
java_SuperConstructorInvocation = Class(name="java::SuperConstructorInvocation")
java_TextElement = Class(name="java::TextElement")
java_ThisExpression = Class(name="java::ThisExpression")
java_ThrowStatement = Class(name="java::ThrowStatement")
java_TryStatement = Class(name="java::TryStatement")
java_SynchronizedStatement = Class(name="java::SynchronizedStatement")
java_TypeLiteral = Class(name="java::TypeLiteral")
java_UnresolvedItemAccess = Class(name="java::UnresolvedItemAccess")
java_UnresolvedAnnotationDeclaration = Class(name="java::UnresolvedAnnotationDeclaration")
AnnotationTypeDeclaration = Class(name="AnnotationTypeDeclaration")
UnresolvedItem = Class(name="UnresolvedItem")
java_UnresolvedAnnotationTypeMemberDeclaration = Class(name="java::UnresolvedAnnotationTypeMemberDeclaration")
AnnotationTypeMemberDeclaration = Class(name="AnnotationTypeMemberDeclaration")
java_UnresolvedClassDeclaration = Class(name="java::UnresolvedClassDeclaration")
ClassDeclaration = Class(name="ClassDeclaration")
java_UnresolvedEnumDeclaration = Class(name="java::UnresolvedEnumDeclaration")
EnumDeclaration = Class(name="EnumDeclaration")
java_UnresolvedInterfaceDeclaration = Class(name="java::UnresolvedInterfaceDeclaration")
InterfaceDeclaration = Class(name="InterfaceDeclaration")
java_TypeDeclaration = Class(name="java::TypeDeclaration", is_abstract=True)
java_TypeDeclarationStatement = Class(name="java::TypeDeclarationStatement")
java_UnresolvedType = Class(name="java::UnresolvedType")
java_UnresolvedTypeDeclaration = Class(name="java::UnresolvedTypeDeclaration")
java_UnresolvedVariableDeclarationFragment = Class(name="java::UnresolvedVariableDeclarationFragment")
VariableDeclarationFragment = Class(name="VariableDeclarationFragment")
java_UnresolvedLabeledStatement = Class(name="java::UnresolvedLabeledStatement")
LabeledStatement = Class(name="LabeledStatement")
java_UnresolvedMethodDeclaration = Class(name="java::UnresolvedMethodDeclaration")
MethodDeclaration = Class(name="MethodDeclaration")
java_UnresolvedSingleVariableDeclaration = Class(name="java::UnresolvedSingleVariableDeclaration")
SingleVariableDeclaration = Class(name="SingleVariableDeclaration")
java_WhileStatement = Class(name="java::WhileStatement")
java_WildCardType = Class(name="java::WildCardType")

# java_TypeAccess class attributes and methods

# java_TypeParameter class attributes and methods

# java_AbstractMethodInvocation class attributes and methods

# ASTNode class attributes and methods

# java_Expression class attributes and methods

# java_AbstractMethodDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# java_Block class attributes and methods

# java_SingleVariableDeclaration class attributes and methods
java_SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=BooleanType)
java_SingleVariableDeclaration.attributes={java_SingleVariableDeclaration_varargs}

# java_AbstractTypeQualifiedExpression class attributes and methods

# Expression class attributes and methods

# java_AbstractVariablesContainer class attributes and methods

# java_VariableDeclarationFragment class attributes and methods

# java_AbstractTypeDeclaration class attributes and methods

# Type class attributes and methods

# java_BodyDeclaration class attributes and methods

# java_Comment class attributes and methods
java_Comment_content: Property = Property(name="content", type=StringType)
java_Comment_enclosedByParent: Property = Property(name="enclosedByParent", type=BooleanType)
java_Comment_prefixOfParent: Property = Property(name="prefixOfParent", type=BooleanType)
java_Comment.attributes={java_Comment_enclosedByParent, java_Comment_prefixOfParent, java_Comment_content}

# java_Package class attributes and methods

# java_AssertStatement class attributes and methods

# Statement class attributes and methods

# java_ASTNode class attributes and methods

# java_CompilationUnit class attributes and methods
java_CompilationUnit_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java_CompilationUnit.attributes={java_CompilationUnit_originalFilePath}

# java_Annotation class attributes and methods

# java_AnnotationMemberValuePair class attributes and methods

# java_Archive class attributes and methods
java_Archive_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java_Archive.attributes={java_Archive_originalFilePath}

# NamedElement class attributes and methods

# java_ClassFile class attributes and methods
java_ClassFile_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
java_ClassFile.attributes={java_ClassFile_originalFilePath}

# java_Manifest class attributes and methods

# java_AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# java_AnonymousClassDeclaration class attributes and methods

# java_ClassInstanceCreation class attributes and methods

# java_AnnotationTypeMemberDeclaration class attributes and methods

# java_ArrayInitializer class attributes and methods

# java_ArrayLengthAccess class attributes and methods

# java_ArrayType class attributes and methods
java_ArrayType_dimensions: Property = Property(name="dimensions", type=IntegerType)
java_ArrayType.attributes={java_ArrayType_dimensions}

# java_ArrayAccess class attributes and methods

# java_ArrayCreation class attributes and methods

# java_Assignment class attributes and methods
java_Assignment_operator: Property = Property(name="operator", type=StringType)
java_Assignment.attributes={java_Assignment_operator}

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
java_Modifier.attributes={java_Modifier_volatile, java_Modifier_native, java_Modifier_static, java_Modifier_synchronized, java_Modifier_visibility, java_Modifier_inheritance, java_Modifier_strictfp, java_Modifier_transient}

# java_CharacterLiteral class attributes and methods
java_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
java_CharacterLiteral.attributes={java_CharacterLiteral_escapedValue}

# java_BooleanLiteral class attributes and methods
java_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
java_BooleanLiteral.attributes={java_BooleanLiteral_value}

# AbstractMethodInvocation class attributes and methods

# java_CatchClause class attributes and methods

# java_ConstructorDeclaration class attributes and methods

# AbstractMethodDeclaration class attributes and methods

# java_ConditionalExpression class attributes and methods

# java_ConstructorInvocation class attributes and methods

# java_ImportDeclaration class attributes and methods
java_ImportDeclaration_static: Property = Property(name="static", type=BooleanType)
java_ImportDeclaration.attributes={java_ImportDeclaration_static}

# java_ClassDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# java_EmptyStatement class attributes and methods

# java_EnhancedForStatement class attributes and methods

# java_ContinueStatement class attributes and methods

# java_EnumConstantDeclaration class attributes and methods

# VariableDeclaration class attributes and methods

# java_DoStatement class attributes and methods

# java_EnumDeclaration class attributes and methods

# java_ExpressionStatement class attributes and methods

# java_FieldAccess class attributes and methods

# java_SingleVariableAccess class attributes and methods

# java_ForStatement class attributes and methods

# java_IfStatement class attributes and methods

# java_FieldDeclaration class attributes and methods

# AbstractVariablesContainer class attributes and methods

# java_NamedElement class attributes and methods
java_NamedElement_name: Property = Property(name="name", type=StringType)
java_NamedElement_proxy: Property = Property(name="proxy", type=BooleanType)
java_NamedElement.attributes={java_NamedElement_proxy, java_NamedElement_name}

# java_InfixExpression class attributes and methods
java_InfixExpression_operator: Property = Property(name="operator", type=StringType)
java_InfixExpression.attributes={java_InfixExpression_operator}

# java_InstanceofExpression class attributes and methods

# java_InterfaceDeclaration class attributes and methods

# java_Javadoc class attributes and methods

# java_TagElement class attributes and methods
java_TagElement_tagName: Property = Property(name="tagName", type=StringType)
java_TagElement.attributes={java_TagElement_tagName}

# java_Initializer class attributes and methods

# java_ManifestAttribute class attributes and methods
java_ManifestAttribute_key: Property = Property(name="key", type=StringType)
java_ManifestAttribute_value: Property = Property(name="value", type=StringType)
java_ManifestAttribute.attributes={java_ManifestAttribute_key, java_ManifestAttribute_value}

# java_ManifestEntry class attributes and methods
java_ManifestEntry_name: Property = Property(name="name", type=StringType)
java_ManifestEntry.attributes={java_ManifestEntry_name}

# java_MemberRef class attributes and methods

# java_LineComment class attributes and methods

# java_MethodInvocation class attributes and methods

# java_MethodRef class attributes and methods

# java_MethodDeclaration class attributes and methods
java_MethodDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
java_MethodDeclaration.attributes={java_MethodDeclaration_extraArrayDimensions}

# java_Model class attributes and methods
java_Model_name: Property = Property(name="name", type=StringType)
java_Model.attributes={java_Model_name}

# java_Type class attributes and methods

# java_UnresolvedItem class attributes and methods

# java_MethodRefParameter class attributes and methods
java_MethodRefParameter_name: Property = Property(name="name", type=StringType)
java_MethodRefParameter_varargs: Property = Property(name="varargs", type=BooleanType)
java_MethodRefParameter.attributes={java_MethodRefParameter_name, java_MethodRefParameter_varargs}

# java_VariableDeclarationStatement class attributes and methods
java_VariableDeclarationStatement_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
java_VariableDeclarationStatement.attributes={java_VariableDeclarationStatement_extraArrayDimensions}

# java_VariableDeclarationExpression class attributes and methods

# java_NamespaceAccess class attributes and methods

# java_NumberLiteral class attributes and methods
java_NumberLiteral_tokenValue: Property = Property(name="tokenValue", type=StringType)
java_NumberLiteral.attributes={java_NumberLiteral_tokenValue}

# java_NullLiteral class attributes and methods

# java_PackageAccess class attributes and methods

# NamespaceAccess class attributes and methods

# java_ParameterizedType class attributes and methods

# java_ParenthesizedExpression class attributes and methods

# java_PostfixExpression class attributes and methods
java_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
java_PostfixExpression.attributes={java_PostfixExpression_operator}

# java_PrimitiveTypeInt class attributes and methods

# java_PrimitiveTypeLong class attributes and methods

# java_PrimitiveTypeVoid class attributes and methods

# java_PrefixExpression class attributes and methods
java_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
java_PrefixExpression.attributes={java_PrefixExpression_operator}

# java_PrimitiveType class attributes and methods

# java_PrimitiveTypeBoolean class attributes and methods

# PrimitiveType class attributes and methods

# java_PrimitiveTypeByte class attributes and methods

# java_PrimitiveTypeChar class attributes and methods

# java_PrimitiveTypeDouble class attributes and methods

# java_PrimitiveTypeShort class attributes and methods

# java_PrimitiveTypeFloat class attributes and methods

# java_ReturnStatement class attributes and methods

# java_VariableDeclaration class attributes and methods
java_VariableDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
java_VariableDeclaration.attributes={java_VariableDeclaration_extraArrayDimensions}

# java_StringLiteral class attributes and methods
java_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
java_StringLiteral.attributes={java_StringLiteral_escapedValue}

# java_SuperFieldAccess class attributes and methods

# AbstractTypeQualifiedExpression class attributes and methods

# java_SuperMethodInvocation class attributes and methods

# java_SwitchCase class attributes and methods
java_SwitchCase_default: Property = Property(name="default", type=BooleanType)
java_SwitchCase.attributes={java_SwitchCase_default}

# java_SwitchStatement class attributes and methods

# java_SuperConstructorInvocation class attributes and methods

# java_TextElement class attributes and methods
java_TextElement_text: Property = Property(name="text", type=StringType)
java_TextElement.attributes={java_TextElement_text}

# java_ThisExpression class attributes and methods

# java_ThrowStatement class attributes and methods

# java_TryStatement class attributes and methods

# java_SynchronizedStatement class attributes and methods

# java_TypeLiteral class attributes and methods

# java_UnresolvedItemAccess class attributes and methods

# java_UnresolvedAnnotationDeclaration class attributes and methods

# AnnotationTypeDeclaration class attributes and methods

# UnresolvedItem class attributes and methods

# java_UnresolvedAnnotationTypeMemberDeclaration class attributes and methods

# AnnotationTypeMemberDeclaration class attributes and methods

# java_UnresolvedClassDeclaration class attributes and methods

# ClassDeclaration class attributes and methods

# java_UnresolvedEnumDeclaration class attributes and methods

# EnumDeclaration class attributes and methods

# java_UnresolvedInterfaceDeclaration class attributes and methods

# InterfaceDeclaration class attributes and methods

# java_TypeDeclaration class attributes and methods

# java_TypeDeclarationStatement class attributes and methods

# java_UnresolvedType class attributes and methods

# java_UnresolvedTypeDeclaration class attributes and methods

# java_UnresolvedVariableDeclarationFragment class attributes and methods

# VariableDeclarationFragment class attributes and methods

# java_UnresolvedLabeledStatement class attributes and methods

# LabeledStatement class attributes and methods

# java_UnresolvedMethodDeclaration class attributes and methods

# MethodDeclaration class attributes and methods

# java_UnresolvedSingleVariableDeclaration class attributes and methods

# SingleVariableDeclaration class attributes and methods

# java_WhileStatement class attributes and methods

# java_WildCardType class attributes and methods
java_WildCardType_upperBound: Property = Property(name="upperBound", type=BooleanType)
java_WildCardType.attributes={java_WildCardType_upperBound}

# Relationships
thrownExceptions2: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions2",
    ends={
        Property(name="java_TypeAccess", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration3", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters4: BinaryAssociation = BinaryAssociation(
    name="typeParameters4",
    ends={
        Property(name="java_TypeParameter", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodDeclaration5", type=java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method6: BinaryAssociation = BinaryAssociation(
    name="method6",
    ends={
        Property(name="java_AbstractMethodDeclaration7", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodInvocation", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
arguments8: BinaryAssociation = BinaryAssociation(
    name="arguments8",
    ends={
        Property(name="java_Expression", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodInvocation9", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
superInterfaces19: BinaryAssociation = BinaryAssociation(
    name="superInterfaces19",
    ends={
        Property(name="java_TypeAccess21", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration20", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier22: BinaryAssociation = BinaryAssociation(
    name="qualifier22",
    ends={
        Property(name="java_TypeAccess23", type=java_AbstractTypeQualifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeQualifiedExpression", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="java_TypeAccess25", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractVariablesContainer", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments26: BinaryAssociation = BinaryAssociation(
    name="fragments26",
    ends={
        Property(name="VariableDeclarationFragment", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="variablesContainer", type=java_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments10: BinaryAssociation = BinaryAssociation(
    name="typeArguments10",
    ends={
        Property(name="java_TypeAccess12", type=java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractMethodInvocation11", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations13: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations13",
    ends={
        Property(name="BodyDeclaration", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractTypeDeclaration", type=java_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsBeforeBody14: BinaryAssociation = BinaryAssociation(
    name="commentsBeforeBody14",
    ends={
        Property(name="java_Comment", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsAfterBody15: BinaryAssociation = BinaryAssociation(
    name="commentsAfterBody15",
    ends={
        Property(name="java_Comment17", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AbstractTypeDeclaration16", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package18: BinaryAssociation = BinaryAssociation(
    name="package18",
    ends={
        Property(name="Package", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements", type=java_Package, multiplicity=Multiplicity(0, 1))
    }
)
manifest32: BinaryAssociation = BinaryAssociation(
    name="manifest32",
    ends={
        Property(name="java_Manifest", type=java_Archive, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Archive33", type=java_Manifest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message34: BinaryAssociation = BinaryAssociation(
    name="message34",
    ends={
        Property(name="java_Expression35", type=java_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AssertStatement", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression36: BinaryAssociation = BinaryAssociation(
    name="expression36",
    ends={
        Property(name="java_Expression38", type=java_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AssertStatement37", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comments39: BinaryAssociation = BinaryAssociation(
    name="comments39",
    ends={
        Property(name="java_Comment40", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode", type=java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalCompilationUnit41: BinaryAssociation = BinaryAssociation(
    name="originalCompilationUnit41",
    ends={
        Property(name="java_CompilationUnit", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode42", type=java_CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="java_TypeAccess28", type=java_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Annotation", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values29: BinaryAssociation = BinaryAssociation(
    name="values29",
    ends={
        Property(name="java_AnnotationMemberValuePair", type=java_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Annotation30", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classFiles31: BinaryAssociation = BinaryAssociation(
    name="classFiles31",
    ends={
        Property(name="java_ClassFile", type=java_Archive, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Archive", type=java_ClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default51: BinaryAssociation = BinaryAssociation(
    name="default51",
    ends={
        Property(name="java_Expression53", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationTypeMemberDeclaration52", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="java_TypeAccess56", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationTypeMemberDeclaration55", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyDeclarations57: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations57",
    ends={
        Property(name="BodyDeclaration58", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclarationOwner", type=java_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classInstanceCreation59: BinaryAssociation = BinaryAssociation(
    name="classInstanceCreation59",
    ends={
        Property(name="ClassInstanceCreation", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclaration", type=java_ClassInstanceCreation, multiplicity=Multiplicity(0, 1))
    }
)
originalClassFile43: BinaryAssociation = BinaryAssociation(
    name="originalClassFile43",
    ends={
        Property(name="java_ClassFile45", type=java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ASTNode44", type=java_ClassFile, multiplicity=Multiplicity(0, 1))
    }
)
member46: BinaryAssociation = BinaryAssociation(
    name="member46",
    ends={
        Property(name="java_AnnotationTypeMemberDeclaration", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationMemberValuePair47", type=java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
value48: BinaryAssociation = BinaryAssociation(
    name="value48",
    ends={
        Property(name="java_Expression50", type=java_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationMemberValuePair49", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer67: BinaryAssociation = BinaryAssociation(
    name="initializer67",
    ends={
        Property(name="java_ArrayInitializer", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation68", type=java_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type69: BinaryAssociation = BinaryAssociation(
    name="type69",
    ends={
        Property(name="java_TypeAccess71", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation70", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions72: BinaryAssociation = BinaryAssociation(
    name="expressions72",
    ends={
        Property(name="java_Expression74", type=java_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayInitializer73", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
array75: BinaryAssociation = BinaryAssociation(
    name="array75",
    ends={
        Property(name="java_Expression76", type=java_ArrayLengthAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayLengthAccess", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType77: BinaryAssociation = BinaryAssociation(
    name="elementType77",
    ends={
        Property(name="java_TypeAccess78", type=java_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayType", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array60: BinaryAssociation = BinaryAssociation(
    name="array60",
    ends={
        Property(name="java_Expression61", type=java_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayAccess", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index62: BinaryAssociation = BinaryAssociation(
    name="index62",
    ends={
        Property(name="java_Expression64", type=java_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayAccess63", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions65: BinaryAssociation = BinaryAssociation(
    name="dimensions65",
    ends={
        Property(name="java_Expression66", type=java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayCreation", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightHandSide81: BinaryAssociation = BinaryAssociation(
    name="rightHandSide81",
    ends={
        Property(name="java_Assignment82", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="java_Expression83", type=java_Assignment, multiplicity=Multiplicity(1, 1))
    }
)
abstractTypeDeclaration84: BinaryAssociation = BinaryAssociation(
    name="abstractTypeDeclaration84",
    ends={
        Property(name="AbstractTypeDeclaration", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
annotations85: BinaryAssociation = BinaryAssociation(
    name="annotations85",
    ends={
        Property(name="java_Annotation86", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_BodyDeclaration", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftHandSide79: BinaryAssociation = BinaryAssociation(
    name="leftHandSide79",
    ends={
        Property(name="java_Expression80", type=java_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Assignment", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements90: BinaryAssociation = BinaryAssociation(
    name="statements90",
    ends={
        Property(name="java_Statement", type=java_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Block91", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label92: BinaryAssociation = BinaryAssociation(
    name="label92",
    ends={
        Property(name="java_LabeledStatement", type=java_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_BreakStatement", type=java_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
expression93: BinaryAssociation = BinaryAssociation(
    name="expression93",
    ends={
        Property(name="java_Expression94", type=java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CastExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anonymousClassDeclarationOwner87: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclarationOwner87",
    ends={
        Property(name="AnonymousClassDeclaration", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations88", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
modifier89: BinaryAssociation = BinaryAssociation(
    name="modifier89",
    ends={
        Property(name="Modifier", type=java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclaration", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type102: BinaryAssociation = BinaryAssociation(
    name="type102",
    ends={
        Property(name="java_AbstractTypeDeclaration104", type=java_ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassFile103", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
attachedSource105: BinaryAssociation = BinaryAssociation(
    name="attachedSource105",
    ends={
        Property(name="java_CompilationUnit107", type=java_ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassFile106", type=java_CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
package108: BinaryAssociation = BinaryAssociation(
    name="package108",
    ends={
        Property(name="java_Package", type=java_ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassFile109", type=java_Package, multiplicity=Multiplicity(0, 1))
    }
)
anonymousClassDeclaration110: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration110",
    ends={
        Property(name="AnonymousClassDeclaration111", type=java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="classInstanceCreation", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type95: BinaryAssociation = BinaryAssociation(
    name="type95",
    ends={
        Property(name="java_TypeAccess97", type=java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CastExpression96", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception98: BinaryAssociation = BinaryAssociation(
    name="exception98",
    ends={
        Property(name="SingleVariableDeclaration99", type=java_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="catchClause", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body100: BinaryAssociation = BinaryAssociation(
    name="body100",
    ends={
        Property(name="java_Block101", type=java_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CatchClause", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression117: BinaryAssociation = BinaryAssociation(
    name="elseExpression117",
    ends={
        Property(name="java_Expression118", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression119: BinaryAssociation = BinaryAssociation(
    name="expression119",
    ends={
        Property(name="java_Expression121", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression120", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression122: BinaryAssociation = BinaryAssociation(
    name="thenExpression122",
    ends={
        Property(name="java_Expression124", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression123", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression112: BinaryAssociation = BinaryAssociation(
    name="expression112",
    ends={
        Property(name="java_Expression113", type=java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassInstanceCreation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type114: BinaryAssociation = BinaryAssociation(
    name="type114",
    ends={
        Property(name="java_TypeAccess116", type=java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassInstanceCreation115", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
commentList127: BinaryAssociation = BinaryAssociation(
    name="commentList127",
    ends={
        Property(name="java_Comment129", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit128", type=java_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
imports130: BinaryAssociation = BinaryAssociation(
    name="imports130",
    ends={
        Property(name="java_ImportDeclaration", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit131", type=java_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package132: BinaryAssociation = BinaryAssociation(
    name="package132",
    ends={
        Property(name="java_Package134", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit133", type=java_Package, multiplicity=Multiplicity(0, 1))
    }
)
types135: BinaryAssociation = BinaryAssociation(
    name="types135",
    ends={
        Property(name="java_AbstractTypeDeclaration137", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit136", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
superClass125: BinaryAssociation = BinaryAssociation(
    name="superClass125",
    ends={
        Property(name="java_TypeAccess126", type=java_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassDeclaration", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression140: BinaryAssociation = BinaryAssociation(
    name="expression140",
    ends={
        Property(name="java_Expression141", type=java_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_DoStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body142: BinaryAssociation = BinaryAssociation(
    name="body142",
    ends={
        Property(name="java_Statement144", type=java_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_DoStatement143", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body145: BinaryAssociation = BinaryAssociation(
    name="body145",
    ends={
        Property(name="java_Statement146", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnhancedForStatement", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression147: BinaryAssociation = BinaryAssociation(
    name="expression147",
    ends={
        Property(name="java_Expression149", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnhancedForStatement148", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter150: BinaryAssociation = BinaryAssociation(
    name="parameter150",
    ends={
        Property(name="SingleVariableDeclaration151", type=java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="enhancedForStatement", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label138: BinaryAssociation = BinaryAssociation(
    name="label138",
    ends={
        Property(name="java_LabeledStatement139", type=java_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ContinueStatement", type=java_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
arguments153: BinaryAssociation = BinaryAssociation(
    name="arguments153",
    ends={
        Property(name="java_Expression155", type=java_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnumConstantDeclaration154", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumConstants156: BinaryAssociation = BinaryAssociation(
    name="enumConstants156",
    ends={
        Property(name="java_EnumConstantDeclaration157", type=java_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnumDeclaration", type=java_EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression158: BinaryAssociation = BinaryAssociation(
    name="expression158",
    ends={
        Property(name="java_Expression159", type=java_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ExpressionStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
field160: BinaryAssociation = BinaryAssociation(
    name="field160",
    ends={
        Property(name="java_SingleVariableAccess", type=java_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_FieldAccess", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anonymousClassDeclaration152: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration152",
    ends={
        Property(name="java_AnonymousClassDeclaration", type=java_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnumConstantDeclaration", type=java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression164: BinaryAssociation = BinaryAssociation(
    name="expression164",
    ends={
        Property(name="java_Expression165", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updaters166: BinaryAssociation = BinaryAssociation(
    name="updaters166",
    ends={
        Property(name="java_Expression168", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement167", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializers169: BinaryAssociation = BinaryAssociation(
    name="initializers169",
    ends={
        Property(name="java_Expression171", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement170", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body172: BinaryAssociation = BinaryAssociation(
    name="body172",
    ends={
        Property(name="java_Statement174", type=java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForStatement173", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression175: BinaryAssociation = BinaryAssociation(
    name="expression175",
    ends={
        Property(name="java_Expression176", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression161: BinaryAssociation = BinaryAssociation(
    name="expression161",
    ends={
        Property(name="java_Expression163", type=java_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_FieldAccess162", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement180: BinaryAssociation = BinaryAssociation(
    name="elseStatement180",
    ends={
        Property(name="java_IfStatement181", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="java_Statement182", type=java_IfStatement, multiplicity=Multiplicity(1, 1))
    }
)
importedElement183: BinaryAssociation = BinaryAssociation(
    name="importedElement183",
    ends={
        Property(name="java_NamedElement", type=java_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ImportDeclaration184", type=java_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand185: BinaryAssociation = BinaryAssociation(
    name="rightOperand185",
    ends={
        Property(name="java_Expression186", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand187: BinaryAssociation = BinaryAssociation(
    name="leftOperand187",
    ends={
        Property(name="java_Expression189", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression188", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands190: BinaryAssociation = BinaryAssociation(
    name="extendedOperands190",
    ends={
        Property(name="java_Expression192", type=java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InfixExpression191", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenStatement177: BinaryAssociation = BinaryAssociation(
    name="thenStatement177",
    ends={
        Property(name="java_Statement179", type=java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_IfStatement178", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body193: BinaryAssociation = BinaryAssociation(
    name="body193",
    ends={
        Property(name="java_Initializer", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="java_Block194", type=java_Initializer, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand195: BinaryAssociation = BinaryAssociation(
    name="rightOperand195",
    ends={
        Property(name="java_TypeAccess196", type=java_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InstanceofExpression", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand197: BinaryAssociation = BinaryAssociation(
    name="leftOperand197",
    ends={
        Property(name="java_Expression199", type=java_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InstanceofExpression198", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tags200: BinaryAssociation = BinaryAssociation(
    name="tags200",
    ends={
        Property(name="java_TagElement", type=java_Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Javadoc", type=java_TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body201: BinaryAssociation = BinaryAssociation(
    name="body201",
    ends={
        Property(name="java_Statement203", type=java_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_LabeledStatement202", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mainAttributes204: BinaryAssociation = BinaryAssociation(
    name="mainAttributes204",
    ends={
        Property(name="java_ManifestAttribute", type=java_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Manifest205", type=java_ManifestAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryAttributes206: BinaryAssociation = BinaryAssociation(
    name="entryAttributes206",
    ends={
        Property(name="java_ManifestEntry", type=java_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Manifest207", type=java_ManifestEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes208: BinaryAssociation = BinaryAssociation(
    name="attributes208",
    ends={
        Property(name="java_ManifestAttribute210", type=java_ManifestEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ManifestEntry209", type=java_ManifestAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member211: BinaryAssociation = BinaryAssociation(
    name="member211",
    ends={
        Property(name="java_NamedElement212", type=java_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MemberRef", type=java_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
returnType216: BinaryAssociation = BinaryAssociation(
    name="returnType216",
    ends={
        Property(name="java_TypeAccess217", type=java_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodDeclaration", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedMethodDeclaration219: BinaryAssociation = BinaryAssociation(
    name="redefinedMethodDeclaration219",
    ends={
        Property(name="MethodDeclaration", type=java_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinitions", type=java_MethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
redefinitions221: BinaryAssociation = BinaryAssociation(
    name="redefinitions221",
    ends={
        Property(name="MethodDeclaration222", type=java_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinedMethodDeclaration", type=java_MethodDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
expression223: BinaryAssociation = BinaryAssociation(
    name="expression223",
    ends={
        Property(name="java_Expression224", type=java_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodInvocation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method225: BinaryAssociation = BinaryAssociation(
    name="method225",
    ends={
        Property(name="java_AbstractMethodDeclaration226", type=java_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodRef", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
qualifier227: BinaryAssociation = BinaryAssociation(
    name="qualifier227",
    ends={
        Property(name="java_TypeAccess229", type=java_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodRef228", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier213: BinaryAssociation = BinaryAssociation(
    name="qualifier213",
    ends={
        Property(name="java_TypeAccess215", type=java_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MemberRef214", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classFiles243: BinaryAssociation = BinaryAssociation(
    name="classFiles243",
    ends={
        Property(name="java_ClassFile245", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model244", type=java_ClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type232: BinaryAssociation = BinaryAssociation(
    name="type232",
    ends={
        Property(name="java_TypeAccess234", type=java_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodRefParameter233", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedElements235: BinaryAssociation = BinaryAssociation(
    name="ownedElements235",
    ends={
        Property(name="Package236", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orphanTypes237: BinaryAssociation = BinaryAssociation(
    name="orphanTypes237",
    ends={
        Property(name="java_Type", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model", type=java_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unresolvedItems238: BinaryAssociation = BinaryAssociation(
    name="unresolvedItems238",
    ends={
        Property(name="java_UnresolvedItem", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model239", type=java_UnresolvedItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits240: BinaryAssociation = BinaryAssociation(
    name="compilationUnits240",
    ends={
        Property(name="java_CompilationUnit242", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model241", type=java_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters230: BinaryAssociation = BinaryAssociation(
    name="parameters230",
    ends={
        Property(name="java_MethodRefParameter", type=java_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MethodRef231", type=java_MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archives246: BinaryAssociation = BinaryAssociation(
    name="archives246",
    ends={
        Property(name="java_Archive248", type=java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Model247", type=java_Archive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclaration249: BinaryAssociation = BinaryAssociation(
    name="bodyDeclaration249",
    ends={
        Property(name="BodyDeclaration250", type=java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier", type=java_BodyDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
singleVariableDeclaration251: BinaryAssociation = BinaryAssociation(
    name="singleVariableDeclaration251",
    ends={
        Property(name="SingleVariableDeclaration253", type=java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier252", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclarationStatement254: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationStatement254",
    ends={
        Property(name="VariableDeclarationStatement", type=java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier255", type=java_VariableDeclarationStatement, multiplicity=Multiplicity(0, 1))
    }
)
package267: BinaryAssociation = BinaryAssociation(
    name="package267",
    ends={
        Property(name="Package268", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPackages", type=java_Package, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclarationExpression256: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationExpression256",
    ends={
        Property(name="VariableDeclarationExpression", type=java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier257", type=java_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1))
    }
)
ownedElements258: BinaryAssociation = BinaryAssociation(
    name="ownedElements258",
    ends={
        Property(name="AbstractTypeDeclaration259", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model260: BinaryAssociation = BinaryAssociation(
    name="model260",
    ends={
        Property(name="Model", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements261", type=java_Model, multiplicity=Multiplicity(0, 1))
    }
)
ownedPackages263: BinaryAssociation = BinaryAssociation(
    name="ownedPackages263",
    ends={
        Property(name="Package265", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package264", type=java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package269: BinaryAssociation = BinaryAssociation(
    name="package269",
    ends={
        Property(name="java_Package270", type=java_PackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PackageAccess", type=java_Package, multiplicity=Multiplicity(1, 1))
    }
)
qualifier272: BinaryAssociation = BinaryAssociation(
    name="qualifier272",
    ends={
        Property(name="java_PackageAccess273", type=java_PackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PackageAccess271", type=java_PackageAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type274: BinaryAssociation = BinaryAssociation(
    name="type274",
    ends={
        Property(name="java_TypeAccess275", type=java_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParameterizedType", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments276: BinaryAssociation = BinaryAssociation(
    name="typeArguments276",
    ends={
        Property(name="java_TypeAccess278", type=java_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParameterizedType277", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression279: BinaryAssociation = BinaryAssociation(
    name="expression279",
    ends={
        Property(name="java_Expression280", type=java_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ParenthesizedExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand281: BinaryAssociation = BinaryAssociation(
    name="operand281",
    ends={
        Property(name="java_Expression282", type=java_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PostfixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand283: BinaryAssociation = BinaryAssociation(
    name="operand283",
    ends={
        Property(name="java_Expression284", type=java_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PrefixExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodDeclaration299: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration299",
    ends={
        Property(name="AbstractMethodDeclaration", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=java_AbstractMethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
catchClause300: BinaryAssociation = BinaryAssociation(
    name="catchClause300",
    ends={
        Property(name="CatchClause", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="exception", type=java_CatchClause, multiplicity=Multiplicity(0, 1))
    }
)
expression285: BinaryAssociation = BinaryAssociation(
    name="expression285",
    ends={
        Property(name="java_Expression286", type=java_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ReturnStatement", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enhancedForStatement301: BinaryAssociation = BinaryAssociation(
    name="enhancedForStatement301",
    ends={
        Property(name="EnhancedForStatement", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=java_EnhancedForStatement, multiplicity=Multiplicity(0, 1))
    }
)
variable287: BinaryAssociation = BinaryAssociation(
    name="variable287",
    ends={
        Property(name="java_VariableDeclaration", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableAccess288", type=java_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
qualifier289: BinaryAssociation = BinaryAssociation(
    name="qualifier289",
    ends={
        Property(name="java_Expression291", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableAccess290", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifier292: BinaryAssociation = BinaryAssociation(
    name="modifier292",
    ends={
        Property(name="Modifier293", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="singleVariableDeclaration", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type294: BinaryAssociation = BinaryAssociation(
    name="type294",
    ends={
        Property(name="java_TypeAccess295", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableDeclaration", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations296: BinaryAssociation = BinaryAssociation(
    name="annotations296",
    ends={
        Property(name="java_Annotation298", type=java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleVariableDeclaration297", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
field304: BinaryAssociation = BinaryAssociation(
    name="field304",
    ends={
        Property(name="java_SingleVariableAccess305", type=java_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SuperFieldAccess", type=java_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression306: BinaryAssociation = BinaryAssociation(
    name="expression306",
    ends={
        Property(name="java_Expression307", type=java_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchCase", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression308: BinaryAssociation = BinaryAssociation(
    name="expression308",
    ends={
        Property(name="java_Expression309", type=java_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements310: BinaryAssociation = BinaryAssociation(
    name="statements310",
    ends={
        Property(name="java_Statement312", type=java_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SwitchStatement311", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression302: BinaryAssociation = BinaryAssociation(
    name="expression302",
    ends={
        Property(name="java_Expression303", type=java_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SuperConstructorInvocation", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments318: BinaryAssociation = BinaryAssociation(
    name="fragments318",
    ends={
        Property(name="java_ASTNode320", type=java_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TagElement319", type=java_ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression321: BinaryAssociation = BinaryAssociation(
    name="expression321",
    ends={
        Property(name="java_Expression322", type=java_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ThrowStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body323: BinaryAssociation = BinaryAssociation(
    name="body323",
    ends={
        Property(name="java_Block324", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally325: BinaryAssociation = BinaryAssociation(
    name="finally325",
    ends={
        Property(name="java_Block327", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement326", type=java_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses328: BinaryAssociation = BinaryAssociation(
    name="catchClauses328",
    ends={
        Property(name="java_CatchClause330", type=java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryStatement329", type=java_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type331: BinaryAssociation = BinaryAssociation(
    name="type331",
    ends={
        Property(name="java_Type333", type=java_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeAccess332", type=java_Type, multiplicity=Multiplicity(1, 1))
    }
)
body313: BinaryAssociation = BinaryAssociation(
    name="body313",
    ends={
        Property(name="java_Block314", type=java_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SynchronizedStatement", type=java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression315: BinaryAssociation = BinaryAssociation(
    name="expression315",
    ends={
        Property(name="java_Expression317", type=java_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SynchronizedStatement316", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration338: BinaryAssociation = BinaryAssociation(
    name="declaration338",
    ends={
        Property(name="java_AbstractTypeDeclaration339", type=java_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeDeclarationStatement", type=java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type340: BinaryAssociation = BinaryAssociation(
    name="type340",
    ends={
        Property(name="java_TypeAccess341", type=java_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeLiteral", type=java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bounds342: BinaryAssociation = BinaryAssociation(
    name="bounds342",
    ends={
        Property(name="java_TypeAccess344", type=java_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeParameter343", type=java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element345: BinaryAssociation = BinaryAssociation(
    name="element345",
    ends={
        Property(name="java_UnresolvedItem346", type=java_UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_UnresolvedItemAccess", type=java_UnresolvedItem, multiplicity=Multiplicity(0, 1))
    }
)
qualifier347: BinaryAssociation = BinaryAssociation(
    name="qualifier347",
    ends={
        Property(name="java_ASTNode349", type=java_UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_UnresolvedItemAccess348", type=java_ASTNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier334: BinaryAssociation = BinaryAssociation(
    name="qualifier334",
    ends={
        Property(name="java_NamespaceAccess", type=java_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeAccess335", type=java_NamespaceAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters336: BinaryAssociation = BinaryAssociation(
    name="typeParameters336",
    ends={
        Property(name="java_TypeParameter337", type=java_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeDeclaration", type=java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer350: BinaryAssociation = BinaryAssociation(
    name="initializer350",
    ends={
        Property(name="java_Expression352", type=java_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_VariableDeclaration351", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variablesContainer357: BinaryAssociation = BinaryAssociation(
    name="variablesContainer357",
    ends={
        Property(name="AbstractVariablesContainer", type=java_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=java_AbstractVariablesContainer, multiplicity=Multiplicity(0, 1))
    }
)
modifier358: BinaryAssociation = BinaryAssociation(
    name="modifier358",
    ends={
        Property(name="Modifier359", type=java_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationStatement", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations360: BinaryAssociation = BinaryAssociation(
    name="annotations360",
    ends={
        Property(name="java_Annotation361", type=java_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_VariableDeclarationStatement", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier353: BinaryAssociation = BinaryAssociation(
    name="modifier353",
    ends={
        Property(name="Modifier354", type=java_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationExpression", type=java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations355: BinaryAssociation = BinaryAssociation(
    name="annotations355",
    ends={
        Property(name="java_Annotation356", type=java_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_VariableDeclarationExpression", type=java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bound362: BinaryAssociation = BinaryAssociation(
    name="bound362",
    ends={
        Property(name="java_TypeAccess363", type=java_WildCardType, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WildCardType", type=java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression364: BinaryAssociation = BinaryAssociation(
    name="expression364",
    ends={
        Property(name="java_Expression365", type=java_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WhileStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body366: BinaryAssociation = BinaryAssociation(
    name="body366",
    ends={
        Property(name="java_Statement368", type=java_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WhileStatement367", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_java_AbstractMethodInvocation_ASTNode = Generalization(general=ASTNode, specific=java_AbstractMethodInvocation)
gen_java_AbstractMethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AbstractMethodDeclaration)
gen_java_AbstractTypeQualifiedExpression_Expression = Generalization(general=Expression, specific=java_AbstractTypeQualifiedExpression)
gen_java_AbstractVariablesContainer_ASTNode = Generalization(general=ASTNode, specific=java_AbstractVariablesContainer)
gen_java_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AbstractTypeDeclaration)
gen_java_AbstractTypeDeclaration_Type = Generalization(general=Type, specific=java_AbstractTypeDeclaration)
gen_java_AssertStatement_Statement = Generalization(general=Statement, specific=java_AssertStatement)
gen_java_Annotation_Expression = Generalization(general=Expression, specific=java_Annotation)
gen_java_Archive_NamedElement = Generalization(general=NamedElement, specific=java_Archive)
gen_java_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_AnnotationTypeDeclaration)
gen_java_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_AnnotationTypeMemberDeclaration)
gen_java_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=java_AnonymousClassDeclaration)
gen_java_AnnotationMemberValuePair_NamedElement = Generalization(general=NamedElement, specific=java_AnnotationMemberValuePair)
gen_java_ArrayInitializer_Expression = Generalization(general=Expression, specific=java_ArrayInitializer)
gen_java_ArrayLengthAccess_Expression = Generalization(general=Expression, specific=java_ArrayLengthAccess)
gen_java_ArrayType_Type = Generalization(general=Type, specific=java_ArrayType)
gen_java_ArrayAccess_Expression = Generalization(general=Expression, specific=java_ArrayAccess)
gen_java_ArrayCreation_Expression = Generalization(general=Expression, specific=java_ArrayCreation)
gen_java_BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=java_BodyDeclaration)
gen_java_Assignment_Expression = Generalization(general=Expression, specific=java_Assignment)
gen_java_BlockComment_Comment = Generalization(general=Comment, specific=java_BlockComment)
gen_java_Block_Statement = Generalization(general=Statement, specific=java_Block)
gen_java_BreakStatement_Statement = Generalization(general=Statement, specific=java_BreakStatement)
gen_java_CastExpression_Expression = Generalization(general=Expression, specific=java_CastExpression)
gen_java_CharacterLiteral_Expression = Generalization(general=Expression, specific=java_CharacterLiteral)
gen_java_BooleanLiteral_Expression = Generalization(general=Expression, specific=java_BooleanLiteral)
gen_java_ClassFile_NamedElement = Generalization(general=NamedElement, specific=java_ClassFile)
gen_java_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=java_ClassInstanceCreation)
gen_java_ClassInstanceCreation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_ClassInstanceCreation)
gen_java_CatchClause_Statement = Generalization(general=Statement, specific=java_CatchClause)
gen_java_ConstructorDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=java_ConstructorDeclaration)
gen_java_ConditionalExpression_Expression = Generalization(general=Expression, specific=java_ConditionalExpression)
gen_java_ConstructorInvocation_Statement = Generalization(general=Statement, specific=java_ConstructorInvocation)
gen_java_ConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_ConstructorInvocation)
gen_java_CompilationUnit_NamedElement = Generalization(general=NamedElement, specific=java_CompilationUnit)
gen_java_ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=java_ClassDeclaration)
gen_java_Comment_ASTNode = Generalization(general=ASTNode, specific=java_Comment)
gen_java_EmptyStatement_Statement = Generalization(general=Statement, specific=java_EmptyStatement)
gen_java_EnhancedForStatement_Statement = Generalization(general=Statement, specific=java_EnhancedForStatement)
gen_java_ContinueStatement_Statement = Generalization(general=Statement, specific=java_ContinueStatement)
gen_java_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_EnumConstantDeclaration)
gen_java_DoStatement_Statement = Generalization(general=Statement, specific=java_DoStatement)
gen_java_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_EnumDeclaration)
gen_java_Expression_ASTNode = Generalization(general=ASTNode, specific=java_Expression)
gen_java_ExpressionStatement_Statement = Generalization(general=Statement, specific=java_ExpressionStatement)
gen_java_FieldAccess_Expression = Generalization(general=Expression, specific=java_FieldAccess)
gen_java_EnumConstantDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_EnumConstantDeclaration)
gen_java_FieldDeclaration_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_FieldDeclaration)
gen_java_ForStatement_Statement = Generalization(general=Statement, specific=java_ForStatement)
gen_java_IfStatement_Statement = Generalization(general=Statement, specific=java_IfStatement)
gen_java_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_FieldDeclaration)
gen_java_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=java_ImportDeclaration)
gen_java_InfixExpression_Expression = Generalization(general=Expression, specific=java_InfixExpression)
gen_java_InstanceofExpression_Expression = Generalization(general=Expression, specific=java_InstanceofExpression)
gen_java_InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=java_InterfaceDeclaration)
gen_java_Javadoc_Comment = Generalization(general=Comment, specific=java_Javadoc)
gen_java_LabeledStatement_NamedElement = Generalization(general=NamedElement, specific=java_LabeledStatement)
gen_java_LabeledStatement_Statement = Generalization(general=Statement, specific=java_LabeledStatement)
gen_java_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=java_Initializer)
gen_java_MemberRef_ASTNode = Generalization(general=ASTNode, specific=java_MemberRef)
gen_java_LineComment_Comment = Generalization(general=Comment, specific=java_LineComment)
gen_java_MethodInvocation_Expression = Generalization(general=Expression, specific=java_MethodInvocation)
gen_java_MethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_MethodInvocation)
gen_java_MethodRef_ASTNode = Generalization(general=ASTNode, specific=java_MethodRef)
gen_java_MethodDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=java_MethodDeclaration)
gen_java_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=java_MethodRefParameter)
gen_java_Modifier_ASTNode = Generalization(general=ASTNode, specific=java_Modifier)
gen_java_NamedElement_ASTNode = Generalization(general=ASTNode, specific=java_NamedElement)
gen_java_NamespaceAccess_ASTNode = Generalization(general=ASTNode, specific=java_NamespaceAccess)
gen_java_NumberLiteral_Expression = Generalization(general=Expression, specific=java_NumberLiteral)
gen_java_NullLiteral_Expression = Generalization(general=Expression, specific=java_NullLiteral)
gen_java_Package_NamedElement = Generalization(general=NamedElement, specific=java_Package)
gen_java_PackageAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java_PackageAccess)
gen_java_ParameterizedType_Type = Generalization(general=Type, specific=java_ParameterizedType)
gen_java_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=java_ParenthesizedExpression)
gen_java_PostfixExpression_Expression = Generalization(general=Expression, specific=java_PostfixExpression)
gen_java_PrimitiveTypeInt_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeInt)
gen_java_PrimitiveTypeLong_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeLong)
gen_java_PrefixExpression_Expression = Generalization(general=Expression, specific=java_PrefixExpression)
gen_java_PrimitiveType_Type = Generalization(general=Type, specific=java_PrimitiveType)
gen_java_PrimitiveTypeBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeBoolean)
gen_java_PrimitiveTypeByte_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeByte)
gen_java_PrimitiveTypeChar_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeChar)
gen_java_PrimitiveTypeDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeDouble)
gen_java_PrimitiveTypeShort_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeShort)
gen_java_PrimitiveTypeFloat_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeFloat)
gen_java_PrimitiveTypeVoid_PrimitiveType = Generalization(general=PrimitiveType, specific=java_PrimitiveTypeVoid)
gen_java_ReturnStatement_Statement = Generalization(general=Statement, specific=java_ReturnStatement)
gen_java_SingleVariableAccess_Expression = Generalization(general=Expression, specific=java_SingleVariableAccess)
gen_java_Statement_ASTNode = Generalization(general=ASTNode, specific=java_Statement)
gen_java_StringLiteral_Expression = Generalization(general=Expression, specific=java_StringLiteral)
gen_java_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_SingleVariableDeclaration)
gen_java_SuperFieldAccess_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_SuperFieldAccess)
gen_java_SuperMethodInvocation_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_SuperMethodInvocation)
gen_java_SuperMethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_SuperMethodInvocation)
gen_java_SwitchCase_Statement = Generalization(general=Statement, specific=java_SwitchCase)
gen_java_SwitchStatement_Statement = Generalization(general=Statement, specific=java_SwitchStatement)
gen_java_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=java_SuperConstructorInvocation)
gen_java_SuperConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=java_SuperConstructorInvocation)
gen_java_TextElement_ASTNode = Generalization(general=ASTNode, specific=java_TextElement)
gen_java_ThisExpression_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=java_ThisExpression)
gen_java_ThrowStatement_Statement = Generalization(general=Statement, specific=java_ThrowStatement)
gen_java_TryStatement_Statement = Generalization(general=Statement, specific=java_TryStatement)
gen_java_Type_NamedElement = Generalization(general=NamedElement, specific=java_Type)
gen_java_TypeAccess_Expression = Generalization(general=Expression, specific=java_TypeAccess)
gen_java_TypeAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java_TypeAccess)
gen_java_SynchronizedStatement_Statement = Generalization(general=Statement, specific=java_SynchronizedStatement)
gen_java_TagElement_ASTNode = Generalization(general=ASTNode, specific=java_TagElement)
gen_java_TypeLiteral_Expression = Generalization(general=Expression, specific=java_TypeLiteral)
gen_java_TypeParameter_Type = Generalization(general=Type, specific=java_TypeParameter)
gen_java_UnresolvedItem_NamedElement = Generalization(general=NamedElement, specific=java_UnresolvedItem)
gen_java_UnresolvedItemAccess_Expression = Generalization(general=Expression, specific=java_UnresolvedItemAccess)
gen_java_UnresolvedItemAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=java_UnresolvedItemAccess)
gen_java_UnresolvedAnnotationDeclaration_AnnotationTypeDeclaration = Generalization(general=AnnotationTypeDeclaration, specific=java_UnresolvedAnnotationDeclaration)
gen_java_UnresolvedAnnotationDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedAnnotationDeclaration)
gen_java_UnresolvedAnnotationTypeMemberDeclaration_AnnotationTypeMemberDeclaration = Generalization(general=AnnotationTypeMemberDeclaration, specific=java_UnresolvedAnnotationTypeMemberDeclaration)
gen_java_UnresolvedAnnotationTypeMemberDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedAnnotationTypeMemberDeclaration)
gen_java_UnresolvedClassDeclaration_ClassDeclaration = Generalization(general=ClassDeclaration, specific=java_UnresolvedClassDeclaration)
gen_java_UnresolvedClassDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedClassDeclaration)
gen_java_UnresolvedEnumDeclaration_EnumDeclaration = Generalization(general=EnumDeclaration, specific=java_UnresolvedEnumDeclaration)
gen_java_UnresolvedEnumDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedEnumDeclaration)
gen_java_UnresolvedInterfaceDeclaration_InterfaceDeclaration = Generalization(general=InterfaceDeclaration, specific=java_UnresolvedInterfaceDeclaration)
gen_java_UnresolvedInterfaceDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedInterfaceDeclaration)
gen_java_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_TypeDeclaration)
gen_java_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=java_TypeDeclarationStatement)
gen_java_UnresolvedSingleVariableDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedSingleVariableDeclaration)
gen_java_UnresolvedType_Type = Generalization(general=Type, specific=java_UnresolvedType)
gen_java_UnresolvedType_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedType)
gen_java_UnresolvedTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=java_UnresolvedTypeDeclaration)
gen_java_UnresolvedTypeDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedTypeDeclaration)
gen_java_UnresolvedVariableDeclarationFragment_VariableDeclarationFragment = Generalization(general=VariableDeclarationFragment, specific=java_UnresolvedVariableDeclarationFragment)
gen_java_UnresolvedVariableDeclarationFragment_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedVariableDeclarationFragment)
gen_java_VariableDeclaration_NamedElement = Generalization(general=NamedElement, specific=java_VariableDeclaration)
gen_java_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=java_VariableDeclarationExpression)
gen_java_VariableDeclarationExpression_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_VariableDeclarationExpression)
gen_java_UnresolvedLabeledStatement_LabeledStatement = Generalization(general=LabeledStatement, specific=java_UnresolvedLabeledStatement)
gen_java_UnresolvedLabeledStatement_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedLabeledStatement)
gen_java_UnresolvedMethodDeclaration_MethodDeclaration = Generalization(general=MethodDeclaration, specific=java_UnresolvedMethodDeclaration)
gen_java_UnresolvedMethodDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=java_UnresolvedMethodDeclaration)
gen_java_UnresolvedSingleVariableDeclaration_SingleVariableDeclaration = Generalization(general=SingleVariableDeclaration, specific=java_UnresolvedSingleVariableDeclaration)
gen_java_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=java_VariableDeclarationFragment)
gen_java_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=java_VariableDeclarationStatement)
gen_java_VariableDeclarationStatement_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=java_VariableDeclarationStatement)
gen_java_WhileStatement_Statement = Generalization(general=Statement, specific=java_WhileStatement)
gen_java_WildCardType_Type = Generalization(general=Type, specific=java_WildCardType)

# Domain Model
domain_model = DomainModel(
    name="java",
    types={java_TypeAccess, java_TypeParameter, java_AbstractMethodInvocation, ASTNode, java_Expression, java_AbstractMethodDeclaration, BodyDeclaration, java_Block, java_SingleVariableDeclaration, java_AbstractTypeQualifiedExpression, Expression, java_AbstractVariablesContainer, java_VariableDeclarationFragment, java_AbstractTypeDeclaration, Type, java_BodyDeclaration, java_Comment, java_Package, java_AssertStatement, Statement, java_ASTNode, java_CompilationUnit, java_Annotation, java_AnnotationMemberValuePair, java_Archive, NamedElement, java_ClassFile, java_Manifest, java_AnnotationTypeDeclaration, AbstractTypeDeclaration, java_AnonymousClassDeclaration, java_ClassInstanceCreation, java_AnnotationTypeMemberDeclaration, java_ArrayInitializer, java_ArrayLengthAccess, java_ArrayType, java_ArrayAccess, java_ArrayCreation, java_Assignment, java_BlockComment, Comment, java_Statement, java_BreakStatement, java_LabeledStatement, java_CastExpression, java_Modifier, java_CharacterLiteral, java_BooleanLiteral, AbstractMethodInvocation, java_CatchClause, java_ConstructorDeclaration, AbstractMethodDeclaration, java_ConditionalExpression, java_ConstructorInvocation, java_ImportDeclaration, java_ClassDeclaration, TypeDeclaration, java_EmptyStatement, java_EnhancedForStatement, java_ContinueStatement, java_EnumConstantDeclaration, VariableDeclaration, java_DoStatement, java_EnumDeclaration, java_ExpressionStatement, java_FieldAccess, java_SingleVariableAccess, java_ForStatement, java_IfStatement, java_FieldDeclaration, AbstractVariablesContainer, java_NamedElement, java_InfixExpression, java_InstanceofExpression, java_InterfaceDeclaration, java_Javadoc, java_TagElement, java_Initializer, java_ManifestAttribute, java_ManifestEntry, java_MemberRef, java_LineComment, java_MethodInvocation, java_MethodRef, java_MethodDeclaration, java_Model, java_Type, java_UnresolvedItem, java_MethodRefParameter, java_VariableDeclarationStatement, java_VariableDeclarationExpression, java_NamespaceAccess, java_NumberLiteral, java_NullLiteral, java_PackageAccess, NamespaceAccess, java_ParameterizedType, java_ParenthesizedExpression, java_PostfixExpression, java_PrimitiveTypeInt, java_PrimitiveTypeLong, java_PrimitiveTypeVoid, java_PrefixExpression, java_PrimitiveType, java_PrimitiveTypeBoolean, PrimitiveType, java_PrimitiveTypeByte, java_PrimitiveTypeChar, java_PrimitiveTypeDouble, java_PrimitiveTypeShort, java_PrimitiveTypeFloat, java_ReturnStatement, java_VariableDeclaration, java_StringLiteral, java_SuperFieldAccess, AbstractTypeQualifiedExpression, java_SuperMethodInvocation, java_SwitchCase, java_SwitchStatement, java_SuperConstructorInvocation, java_TextElement, java_ThisExpression, java_ThrowStatement, java_TryStatement, java_SynchronizedStatement, java_TypeLiteral, java_UnresolvedItemAccess, java_UnresolvedAnnotationDeclaration, AnnotationTypeDeclaration, UnresolvedItem, java_UnresolvedAnnotationTypeMemberDeclaration, AnnotationTypeMemberDeclaration, java_UnresolvedClassDeclaration, ClassDeclaration, java_UnresolvedEnumDeclaration, EnumDeclaration, java_UnresolvedInterfaceDeclaration, InterfaceDeclaration, java_TypeDeclaration, java_TypeDeclarationStatement, java_UnresolvedType, java_UnresolvedTypeDeclaration, java_UnresolvedVariableDeclarationFragment, VariableDeclarationFragment, java_UnresolvedLabeledStatement, LabeledStatement, java_UnresolvedMethodDeclaration, MethodDeclaration, java_UnresolvedSingleVariableDeclaration, SingleVariableDeclaration, java_WhileStatement, java_WildCardType, AssignmentKind, InheritanceKind, InfixExpressionKind, PostfixExpressionKind, PrefixExpressionKind, VisibilityKind},
    associations={thrownExceptions2, typeParameters4, method6, arguments8, body0, parameters1, superInterfaces19, qualifier22, type24, fragments26, typeArguments10, bodyDeclarations13, commentsBeforeBody14, commentsAfterBody15, package18, manifest32, message34, expression36, comments39, originalCompilationUnit41, type27, values29, classFiles31, default51, type54, bodyDeclarations57, classInstanceCreation59, originalClassFile43, member46, value48, initializer67, type69, expressions72, array75, elementType77, array60, index62, dimensions65, rightHandSide81, abstractTypeDeclaration84, annotations85, leftHandSide79, statements90, label92, expression93, anonymousClassDeclarationOwner87, modifier89, type102, attachedSource105, package108, anonymousClassDeclaration110, type95, exception98, body100, elseExpression117, expression119, thenExpression122, expression112, type114, commentList127, imports130, package132, types135, superClass125, expression140, body142, body145, expression147, parameter150, label138, arguments153, enumConstants156, expression158, field160, anonymousClassDeclaration152, expression164, updaters166, initializers169, body172, expression175, expression161, elseStatement180, importedElement183, rightOperand185, leftOperand187, extendedOperands190, thenStatement177, body193, rightOperand195, leftOperand197, tags200, body201, mainAttributes204, entryAttributes206, attributes208, member211, returnType216, redefinedMethodDeclaration219, redefinitions221, expression223, method225, qualifier227, qualifier213, classFiles243, type232, ownedElements235, orphanTypes237, unresolvedItems238, compilationUnits240, parameters230, archives246, bodyDeclaration249, singleVariableDeclaration251, variableDeclarationStatement254, package267, variableDeclarationExpression256, ownedElements258, model260, ownedPackages263, package269, qualifier272, type274, typeArguments276, expression279, operand281, operand283, methodDeclaration299, catchClause300, expression285, enhancedForStatement301, variable287, qualifier289, modifier292, type294, annotations296, field304, expression306, expression308, statements310, expression302, fragments318, expression321, body323, finally325, catchClauses328, type331, body313, expression315, declaration338, type340, bounds342, element345, qualifier347, qualifier334, typeParameters336, initializer350, variablesContainer357, modifier358, annotations360, modifier353, annotations355, bound362, expression364, body366},
    generalizations={gen_java_AbstractMethodInvocation_ASTNode, gen_java_AbstractMethodDeclaration_BodyDeclaration, gen_java_AbstractTypeQualifiedExpression_Expression, gen_java_AbstractVariablesContainer_ASTNode, gen_java_AbstractTypeDeclaration_BodyDeclaration, gen_java_AbstractTypeDeclaration_Type, gen_java_AssertStatement_Statement, gen_java_Annotation_Expression, gen_java_Archive_NamedElement, gen_java_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_java_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_java_AnonymousClassDeclaration_ASTNode, gen_java_AnnotationMemberValuePair_NamedElement, gen_java_ArrayInitializer_Expression, gen_java_ArrayLengthAccess_Expression, gen_java_ArrayType_Type, gen_java_ArrayAccess_Expression, gen_java_ArrayCreation_Expression, gen_java_BodyDeclaration_NamedElement, gen_java_Assignment_Expression, gen_java_BlockComment_Comment, gen_java_Block_Statement, gen_java_BreakStatement_Statement, gen_java_CastExpression_Expression, gen_java_CharacterLiteral_Expression, gen_java_BooleanLiteral_Expression, gen_java_ClassFile_NamedElement, gen_java_ClassInstanceCreation_Expression, gen_java_ClassInstanceCreation_AbstractMethodInvocation, gen_java_CatchClause_Statement, gen_java_ConstructorDeclaration_AbstractMethodDeclaration, gen_java_ConditionalExpression_Expression, gen_java_ConstructorInvocation_Statement, gen_java_ConstructorInvocation_AbstractMethodInvocation, gen_java_CompilationUnit_NamedElement, gen_java_ClassDeclaration_TypeDeclaration, gen_java_Comment_ASTNode, gen_java_EmptyStatement_Statement, gen_java_EnhancedForStatement_Statement, gen_java_ContinueStatement_Statement, gen_java_EnumConstantDeclaration_BodyDeclaration, gen_java_DoStatement_Statement, gen_java_EnumDeclaration_AbstractTypeDeclaration, gen_java_Expression_ASTNode, gen_java_ExpressionStatement_Statement, gen_java_FieldAccess_Expression, gen_java_EnumConstantDeclaration_VariableDeclaration, gen_java_FieldDeclaration_AbstractVariablesContainer, gen_java_ForStatement_Statement, gen_java_IfStatement_Statement, gen_java_FieldDeclaration_BodyDeclaration, gen_java_ImportDeclaration_ASTNode, gen_java_InfixExpression_Expression, gen_java_InstanceofExpression_Expression, gen_java_InterfaceDeclaration_TypeDeclaration, gen_java_Javadoc_Comment, gen_java_LabeledStatement_NamedElement, gen_java_LabeledStatement_Statement, gen_java_Initializer_BodyDeclaration, gen_java_MemberRef_ASTNode, gen_java_LineComment_Comment, gen_java_MethodInvocation_Expression, gen_java_MethodInvocation_AbstractMethodInvocation, gen_java_MethodRef_ASTNode, gen_java_MethodDeclaration_AbstractMethodDeclaration, gen_java_MethodRefParameter_ASTNode, gen_java_Modifier_ASTNode, gen_java_NamedElement_ASTNode, gen_java_NamespaceAccess_ASTNode, gen_java_NumberLiteral_Expression, gen_java_NullLiteral_Expression, gen_java_Package_NamedElement, gen_java_PackageAccess_NamespaceAccess, gen_java_ParameterizedType_Type, gen_java_ParenthesizedExpression_Expression, gen_java_PostfixExpression_Expression, gen_java_PrimitiveTypeInt_PrimitiveType, gen_java_PrimitiveTypeLong_PrimitiveType, gen_java_PrefixExpression_Expression, gen_java_PrimitiveType_Type, gen_java_PrimitiveTypeBoolean_PrimitiveType, gen_java_PrimitiveTypeByte_PrimitiveType, gen_java_PrimitiveTypeChar_PrimitiveType, gen_java_PrimitiveTypeDouble_PrimitiveType, gen_java_PrimitiveTypeShort_PrimitiveType, gen_java_PrimitiveTypeFloat_PrimitiveType, gen_java_PrimitiveTypeVoid_PrimitiveType, gen_java_ReturnStatement_Statement, gen_java_SingleVariableAccess_Expression, gen_java_Statement_ASTNode, gen_java_StringLiteral_Expression, gen_java_SingleVariableDeclaration_VariableDeclaration, gen_java_SuperFieldAccess_AbstractTypeQualifiedExpression, gen_java_SuperMethodInvocation_AbstractTypeQualifiedExpression, gen_java_SuperMethodInvocation_AbstractMethodInvocation, gen_java_SwitchCase_Statement, gen_java_SwitchStatement_Statement, gen_java_SuperConstructorInvocation_Statement, gen_java_SuperConstructorInvocation_AbstractMethodInvocation, gen_java_TextElement_ASTNode, gen_java_ThisExpression_AbstractTypeQualifiedExpression, gen_java_ThrowStatement_Statement, gen_java_TryStatement_Statement, gen_java_Type_NamedElement, gen_java_TypeAccess_Expression, gen_java_TypeAccess_NamespaceAccess, gen_java_SynchronizedStatement_Statement, gen_java_TagElement_ASTNode, gen_java_TypeLiteral_Expression, gen_java_TypeParameter_Type, gen_java_UnresolvedItem_NamedElement, gen_java_UnresolvedItemAccess_Expression, gen_java_UnresolvedItemAccess_NamespaceAccess, gen_java_UnresolvedAnnotationDeclaration_AnnotationTypeDeclaration, gen_java_UnresolvedAnnotationDeclaration_UnresolvedItem, gen_java_UnresolvedAnnotationTypeMemberDeclaration_AnnotationTypeMemberDeclaration, gen_java_UnresolvedAnnotationTypeMemberDeclaration_UnresolvedItem, gen_java_UnresolvedClassDeclaration_ClassDeclaration, gen_java_UnresolvedClassDeclaration_UnresolvedItem, gen_java_UnresolvedEnumDeclaration_EnumDeclaration, gen_java_UnresolvedEnumDeclaration_UnresolvedItem, gen_java_UnresolvedInterfaceDeclaration_InterfaceDeclaration, gen_java_UnresolvedInterfaceDeclaration_UnresolvedItem, gen_java_TypeDeclaration_AbstractTypeDeclaration, gen_java_TypeDeclarationStatement_Statement, gen_java_UnresolvedSingleVariableDeclaration_UnresolvedItem, gen_java_UnresolvedType_Type, gen_java_UnresolvedType_UnresolvedItem, gen_java_UnresolvedTypeDeclaration_AbstractTypeDeclaration, gen_java_UnresolvedTypeDeclaration_UnresolvedItem, gen_java_UnresolvedVariableDeclarationFragment_VariableDeclarationFragment, gen_java_UnresolvedVariableDeclarationFragment_UnresolvedItem, gen_java_VariableDeclaration_NamedElement, gen_java_VariableDeclarationExpression_Expression, gen_java_VariableDeclarationExpression_AbstractVariablesContainer, gen_java_UnresolvedLabeledStatement_LabeledStatement, gen_java_UnresolvedLabeledStatement_UnresolvedItem, gen_java_UnresolvedMethodDeclaration_MethodDeclaration, gen_java_UnresolvedMethodDeclaration_UnresolvedItem, gen_java_UnresolvedSingleVariableDeclaration_SingleVariableDeclaration, gen_java_VariableDeclarationFragment_VariableDeclaration, gen_java_VariableDeclarationStatement_Statement, gen_java_VariableDeclarationStatement_AbstractVariablesContainer, gen_java_WhileStatement_Statement, gen_java_WildCardType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)