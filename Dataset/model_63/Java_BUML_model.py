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
			EnumerationLiteral(name="RIGHT_SHIFT_UNSIGNED"),
			EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="LESS_EQUALS"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="XOR")
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
Java_TypeParameter = Class(name="Java::TypeParameter")
Java_MethodRef = Class(name="Java::MethodRef")
Java_AbstractMethodInvocation = Class(name="Java::AbstractMethodInvocation", is_abstract=True)
Java_AbstractMethodDeclaration = Class(name="Java::AbstractMethodDeclaration", is_abstract=True)
BodyDeclaration = Class(name="BodyDeclaration")
Java_Block = Class(name="Java::Block")
Java_SingleVariableDeclaration = Class(name="Java::SingleVariableDeclaration")
Java_TypeAccess = Class(name="Java::TypeAccess")
Java_Package = Class(name="Java::Package")
Java_AbstractTypeQualifiedExpression = Class(name="Java::AbstractTypeQualifiedExpression", is_abstract=True)
Expression = Class(name="Expression")
ASTNode = Class(name="ASTNode")
Java_Expression = Class(name="Java::Expression", is_abstract=True)
Java_AbstractTypeDeclaration = Class(name="Java::AbstractTypeDeclaration", is_abstract=True)
Type = Class(name="Type")
Java_BodyDeclaration = Class(name="Java::BodyDeclaration", is_abstract=True)
Java_Comment = Class(name="Java::Comment", is_abstract=True)
Java_ClassFile = Class(name="Java::ClassFile")
Java_Manifest = Class(name="Java::Manifest")
Java_AssertStatement = Class(name="Java::AssertStatement")
Statement = Class(name="Statement")
Java_AbstractVariablesContainer = Class(name="Java::AbstractVariablesContainer", is_abstract=True)
Java_VariableDeclarationFragment = Class(name="Java::VariableDeclarationFragment")
Java_Annotation = Class(name="Java::Annotation")
Java_AnnotationMemberValuePair = Class(name="Java::AnnotationMemberValuePair")
Java_Archive = Class(name="Java::Archive")
NamedElement = Class(name="NamedElement")
Java_AnnotationTypeDeclaration = Class(name="Java::AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
Java_ASTNode = Class(name="Java::ASTNode", is_abstract=True)
Java_CompilationUnit = Class(name="Java::CompilationUnit")
Java_AnnotationTypeMemberDeclaration = Class(name="Java::AnnotationTypeMemberDeclaration")
Java_ArrayCreation = Class(name="Java::ArrayCreation")
Java_ArrayInitializer = Class(name="Java::ArrayInitializer")
Java_AnonymousClassDeclaration = Class(name="Java::AnonymousClassDeclaration")
Java_ClassInstanceCreation = Class(name="Java::ClassInstanceCreation")
Java_ArrayAccess = Class(name="Java::ArrayAccess")
Java_ArrayType = Class(name="Java::ArrayType")
Java_Assignment = Class(name="Java::Assignment")
Java_ArrayLengthAccess = Class(name="Java::ArrayLengthAccess")
Java_Modifier = Class(name="Java::Modifier")
Java_BooleanLiteral = Class(name="Java::BooleanLiteral")
Java_BlockComment = Class(name="Java::BlockComment")
Comment = Class(name="Comment")
Java_Statement = Class(name="Java::Statement", is_abstract=True)
Java_BreakStatement = Class(name="Java::BreakStatement")
Java_LabeledStatement = Class(name="Java::LabeledStatement")
AbstractMethodInvocation = Class(name="AbstractMethodInvocation")
Java_ConstructorDeclaration = Class(name="Java::ConstructorDeclaration")
AbstractMethodDeclaration = Class(name="AbstractMethodDeclaration")
Java_ConditionalExpression = Class(name="Java::ConditionalExpression")
Java_CastExpression = Class(name="Java::CastExpression")
Java_CatchClause = Class(name="Java::CatchClause")
Java_CharacterLiteral = Class(name="Java::CharacterLiteral")
Java_ImportDeclaration = Class(name="Java::ImportDeclaration")
Java_ContinueStatement = Class(name="Java::ContinueStatement")
Java_DoStatement = Class(name="Java::DoStatement")
Java_EmptyStatement = Class(name="Java::EmptyStatement")
Java_EnhancedForStatement = Class(name="Java::EnhancedForStatement")
Java_ConstructorInvocation = Class(name="Java::ConstructorInvocation")
Java_ClassDeclaration = Class(name="Java::ClassDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
Java_EnumConstantDeclaration = Class(name="Java::EnumConstantDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
Java_EnumDeclaration = Class(name="Java::EnumDeclaration")
Java_IfStatement = Class(name="Java::IfStatement")
Java_ExpressionStatement = Class(name="Java::ExpressionStatement")
Java_FieldAccess = Class(name="Java::FieldAccess")
Java_SingleVariableAccess = Class(name="Java::SingleVariableAccess")
Java_FieldDeclaration = Class(name="Java::FieldDeclaration")
AbstractVariablesContainer = Class(name="AbstractVariablesContainer")
Java_ForStatement = Class(name="Java::ForStatement")
Java_Initializer = Class(name="Java::Initializer")
Java_NamedElement = Class(name="Java::NamedElement", is_abstract=True)
Java_InfixExpression = Class(name="Java::InfixExpression")
Java_MemberRef = Class(name="Java::MemberRef")
Java_InstanceofExpression = Class(name="Java::InstanceofExpression")
Java_InterfaceDeclaration = Class(name="Java::InterfaceDeclaration")
Java_Javadoc = Class(name="Java::Javadoc")
Java_TagElement = Class(name="Java::TagElement")
Java_LineComment = Class(name="Java::LineComment")
Java_ManifestAttribute = Class(name="Java::ManifestAttribute")
Java_ManifestEntry = Class(name="Java::ManifestEntry")
Java_Model = Class(name="Java::Model")
Java_Type = Class(name="Java::Type", is_abstract=True)
Java_UnresolvedItem = Class(name="Java::UnresolvedItem")
Java_MethodDeclaration = Class(name="Java::MethodDeclaration")
Java_MethodInvocation = Class(name="Java::MethodInvocation")
Java_MethodRefParameter = Class(name="Java::MethodRefParameter")
Java_VariableDeclarationStatement = Class(name="Java::VariableDeclarationStatement")
Java_VariableDeclarationExpression = Class(name="Java::VariableDeclarationExpression")
Java_PackageAccess = Class(name="Java::PackageAccess")
NamespaceAccess = Class(name="NamespaceAccess")
Java_NamespaceAccess = Class(name="Java::NamespaceAccess", is_abstract=True)
Java_NumberLiteral = Class(name="Java::NumberLiteral")
Java_NullLiteral = Class(name="Java::NullLiteral")
Java_PrefixExpression = Class(name="Java::PrefixExpression")
Java_ParameterizedType = Class(name="Java::ParameterizedType")
Java_ParenthesizedExpression = Class(name="Java::ParenthesizedExpression")
Java_PostfixExpression = Class(name="Java::PostfixExpression")
Java_PrimitiveType = Class(name="Java::PrimitiveType")
Java_PrimitiveTypeBoolean = Class(name="Java::PrimitiveTypeBoolean")
PrimitiveType = Class(name="PrimitiveType")
Java_PrimitiveTypeByte = Class(name="Java::PrimitiveTypeByte")
Java_PrimitiveTypeChar = Class(name="Java::PrimitiveTypeChar")
Java_PrimitiveTypeDouble = Class(name="Java::PrimitiveTypeDouble")
Java_PrimitiveTypeShort = Class(name="Java::PrimitiveTypeShort")
Java_PrimitiveTypeFloat = Class(name="Java::PrimitiveTypeFloat")
Java_PrimitiveTypeInt = Class(name="Java::PrimitiveTypeInt")
Java_PrimitiveTypeLong = Class(name="Java::PrimitiveTypeLong")
Java_PrimitiveTypeVoid = Class(name="Java::PrimitiveTypeVoid")
Java_ReturnStatement = Class(name="Java::ReturnStatement")
Java_VariableDeclaration = Class(name="Java::VariableDeclaration", is_abstract=True)
Java_SuperFieldAccess = Class(name="Java::SuperFieldAccess")
AbstractTypeQualifiedExpression = Class(name="AbstractTypeQualifiedExpression")
Java_SuperMethodInvocation = Class(name="Java::SuperMethodInvocation")
Java_SwitchCase = Class(name="Java::SwitchCase")
Java_StringLiteral = Class(name="Java::StringLiteral")
Java_SuperConstructorInvocation = Class(name="Java::SuperConstructorInvocation")
Java_TextElement = Class(name="Java::TextElement")
Java_SwitchStatement = Class(name="Java::SwitchStatement")
Java_SynchronizedStatement = Class(name="Java::SynchronizedStatement")
Java_TypeDeclaration = Class(name="Java::TypeDeclaration", is_abstract=True)
Java_ThisExpression = Class(name="Java::ThisExpression")
Java_ThrowStatement = Class(name="Java::ThrowStatement")
Java_TryStatement = Class(name="Java::TryStatement")
UnresolvedItem = Class(name="UnresolvedItem")
Java_TypeDeclarationStatement = Class(name="Java::TypeDeclarationStatement")
Java_TypeLiteral = Class(name="Java::TypeLiteral")
Java_UnresolvedItemAccess = Class(name="Java::UnresolvedItemAccess")
Java_UnresolvedAnnotationDeclaration = Class(name="Java::UnresolvedAnnotationDeclaration")
AnnotationTypeDeclaration = Class(name="AnnotationTypeDeclaration")
Java_UnresolvedAnnotationTypeMemberDeclaration = Class(name="Java::UnresolvedAnnotationTypeMemberDeclaration")
AnnotationTypeMemberDeclaration = Class(name="AnnotationTypeMemberDeclaration")
Java_UnresolvedClassDeclaration = Class(name="Java::UnresolvedClassDeclaration")
ClassDeclaration = Class(name="ClassDeclaration")
Java_UnresolvedEnumDeclaration = Class(name="Java::UnresolvedEnumDeclaration")
EnumDeclaration = Class(name="EnumDeclaration")
Java_UnresolvedInterfaceDeclaration = Class(name="Java::UnresolvedInterfaceDeclaration")
InterfaceDeclaration = Class(name="InterfaceDeclaration")
Java_UnresolvedLabeledStatement = Class(name="Java::UnresolvedLabeledStatement")
LabeledStatement = Class(name="LabeledStatement")
Java_UnresolvedMethodDeclaration = Class(name="Java::UnresolvedMethodDeclaration")
MethodDeclaration = Class(name="MethodDeclaration")
Java_UnresolvedSingleVariableDeclaration = Class(name="Java::UnresolvedSingleVariableDeclaration")
SingleVariableDeclaration = Class(name="SingleVariableDeclaration")
Java_UnresolvedType = Class(name="Java::UnresolvedType")
Java_UnresolvedTypeDeclaration = Class(name="Java::UnresolvedTypeDeclaration")
Java_UnresolvedVariableDeclarationFragment = Class(name="Java::UnresolvedVariableDeclarationFragment")
VariableDeclarationFragment = Class(name="VariableDeclarationFragment")
Java_WhileStatement = Class(name="Java::WhileStatement")
Java_WildCardType = Class(name="Java::WildCardType")

# Java_TypeParameter class attributes and methods

# Java_MethodRef class attributes and methods

# Java_AbstractMethodInvocation class attributes and methods

# Java_AbstractMethodDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# Java_Block class attributes and methods

# Java_SingleVariableDeclaration class attributes and methods
Java_SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=BooleanType)
Java_SingleVariableDeclaration.attributes={Java_SingleVariableDeclaration_varargs}

# Java_TypeAccess class attributes and methods

# Java_Package class attributes and methods

# Java_AbstractTypeQualifiedExpression class attributes and methods

# Expression class attributes and methods

# ASTNode class attributes and methods

# Java_Expression class attributes and methods

# Java_AbstractTypeDeclaration class attributes and methods

# Type class attributes and methods

# Java_BodyDeclaration class attributes and methods

# Java_Comment class attributes and methods
Java_Comment_content: Property = Property(name="content", type=StringType)
Java_Comment_enclosedByParent: Property = Property(name="enclosedByParent", type=BooleanType)
Java_Comment_prefixOfParent: Property = Property(name="prefixOfParent", type=BooleanType)
Java_Comment.attributes={Java_Comment_content, Java_Comment_prefixOfParent, Java_Comment_enclosedByParent}

# Java_ClassFile class attributes and methods
Java_ClassFile_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
Java_ClassFile.attributes={Java_ClassFile_originalFilePath}

# Java_Manifest class attributes and methods

# Java_AssertStatement class attributes and methods

# Statement class attributes and methods

# Java_AbstractVariablesContainer class attributes and methods

# Java_VariableDeclarationFragment class attributes and methods

# Java_Annotation class attributes and methods

# Java_AnnotationMemberValuePair class attributes and methods

# Java_Archive class attributes and methods
Java_Archive_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
Java_Archive.attributes={Java_Archive_originalFilePath}

# NamedElement class attributes and methods

# Java_AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# Java_ASTNode class attributes and methods

# Java_CompilationUnit class attributes and methods
Java_CompilationUnit_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
Java_CompilationUnit.attributes={Java_CompilationUnit_originalFilePath}

# Java_AnnotationTypeMemberDeclaration class attributes and methods

# Java_ArrayCreation class attributes and methods

# Java_ArrayInitializer class attributes and methods

# Java_AnonymousClassDeclaration class attributes and methods

# Java_ClassInstanceCreation class attributes and methods

# Java_ArrayAccess class attributes and methods

# Java_ArrayType class attributes and methods
Java_ArrayType_dimensions: Property = Property(name="dimensions", type=IntegerType)
Java_ArrayType.attributes={Java_ArrayType_dimensions}

# Java_Assignment class attributes and methods
Java_Assignment_operator: Property = Property(name="operator", type=StringType)
Java_Assignment.attributes={Java_Assignment_operator}

# Java_ArrayLengthAccess class attributes and methods

# Java_Modifier class attributes and methods
Java_Modifier_visibility: Property = Property(name="visibility", type=StringType)
Java_Modifier_inheritance: Property = Property(name="inheritance", type=StringType)
Java_Modifier_static: Property = Property(name="static", type=BooleanType)
Java_Modifier_transient: Property = Property(name="transient", type=BooleanType)
Java_Modifier_volatile: Property = Property(name="volatile", type=BooleanType)
Java_Modifier_native: Property = Property(name="native", type=BooleanType)
Java_Modifier_strictfp: Property = Property(name="strictfp", type=BooleanType)
Java_Modifier_synchronized: Property = Property(name="synchronized", type=BooleanType)
Java_Modifier.attributes={Java_Modifier_inheritance, Java_Modifier_synchronized, Java_Modifier_strictfp, Java_Modifier_native, Java_Modifier_volatile, Java_Modifier_static, Java_Modifier_transient, Java_Modifier_visibility}

# Java_BooleanLiteral class attributes and methods
Java_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
Java_BooleanLiteral.attributes={Java_BooleanLiteral_value}

# Java_BlockComment class attributes and methods

# Comment class attributes and methods

# Java_Statement class attributes and methods

# Java_BreakStatement class attributes and methods

# Java_LabeledStatement class attributes and methods

# AbstractMethodInvocation class attributes and methods

# Java_ConstructorDeclaration class attributes and methods

# AbstractMethodDeclaration class attributes and methods

# Java_ConditionalExpression class attributes and methods

# Java_CastExpression class attributes and methods

# Java_CatchClause class attributes and methods

# Java_CharacterLiteral class attributes and methods
Java_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
Java_CharacterLiteral.attributes={Java_CharacterLiteral_escapedValue}

# Java_ImportDeclaration class attributes and methods
Java_ImportDeclaration_static: Property = Property(name="static", type=BooleanType)
Java_ImportDeclaration.attributes={Java_ImportDeclaration_static}

# Java_ContinueStatement class attributes and methods

# Java_DoStatement class attributes and methods

# Java_EmptyStatement class attributes and methods

# Java_EnhancedForStatement class attributes and methods

# Java_ConstructorInvocation class attributes and methods

# Java_ClassDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# Java_EnumConstantDeclaration class attributes and methods

# VariableDeclaration class attributes and methods

# Java_EnumDeclaration class attributes and methods

# Java_IfStatement class attributes and methods

# Java_ExpressionStatement class attributes and methods

# Java_FieldAccess class attributes and methods

# Java_SingleVariableAccess class attributes and methods

# Java_FieldDeclaration class attributes and methods

# AbstractVariablesContainer class attributes and methods

# Java_ForStatement class attributes and methods

# Java_Initializer class attributes and methods

# Java_NamedElement class attributes and methods
Java_NamedElement_name: Property = Property(name="name", type=StringType)
Java_NamedElement_proxy: Property = Property(name="proxy", type=BooleanType)
Java_NamedElement.attributes={Java_NamedElement_name, Java_NamedElement_proxy}

# Java_InfixExpression class attributes and methods
Java_InfixExpression_operator: Property = Property(name="operator", type=StringType)
Java_InfixExpression.attributes={Java_InfixExpression_operator}

# Java_MemberRef class attributes and methods

# Java_InstanceofExpression class attributes and methods

# Java_InterfaceDeclaration class attributes and methods

# Java_Javadoc class attributes and methods

# Java_TagElement class attributes and methods
Java_TagElement_tagName: Property = Property(name="tagName", type=StringType)
Java_TagElement.attributes={Java_TagElement_tagName}

# Java_LineComment class attributes and methods

# Java_ManifestAttribute class attributes and methods
Java_ManifestAttribute_value: Property = Property(name="value", type=StringType)
Java_ManifestAttribute_key: Property = Property(name="key", type=StringType)
Java_ManifestAttribute.attributes={Java_ManifestAttribute_key, Java_ManifestAttribute_value}

# Java_ManifestEntry class attributes and methods
Java_ManifestEntry_name: Property = Property(name="name", type=StringType)
Java_ManifestEntry.attributes={Java_ManifestEntry_name}

# Java_Model class attributes and methods
Java_Model_name: Property = Property(name="name", type=StringType)
Java_Model.attributes={Java_Model_name}

# Java_Type class attributes and methods

# Java_UnresolvedItem class attributes and methods

# Java_MethodDeclaration class attributes and methods
Java_MethodDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
Java_MethodDeclaration.attributes={Java_MethodDeclaration_extraArrayDimensions}

# Java_MethodInvocation class attributes and methods

# Java_MethodRefParameter class attributes and methods
Java_MethodRefParameter_name: Property = Property(name="name", type=StringType)
Java_MethodRefParameter_varargs: Property = Property(name="varargs", type=BooleanType)
Java_MethodRefParameter.attributes={Java_MethodRefParameter_name, Java_MethodRefParameter_varargs}

# Java_VariableDeclarationStatement class attributes and methods
Java_VariableDeclarationStatement_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
Java_VariableDeclarationStatement.attributes={Java_VariableDeclarationStatement_extraArrayDimensions}

# Java_VariableDeclarationExpression class attributes and methods

# Java_PackageAccess class attributes and methods

# NamespaceAccess class attributes and methods

# Java_NamespaceAccess class attributes and methods

# Java_NumberLiteral class attributes and methods
Java_NumberLiteral_tokenValue: Property = Property(name="tokenValue", type=StringType)
Java_NumberLiteral.attributes={Java_NumberLiteral_tokenValue}

# Java_NullLiteral class attributes and methods

# Java_PrefixExpression class attributes and methods
Java_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
Java_PrefixExpression.attributes={Java_PrefixExpression_operator}

# Java_ParameterizedType class attributes and methods

# Java_ParenthesizedExpression class attributes and methods

# Java_PostfixExpression class attributes and methods
Java_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
Java_PostfixExpression.attributes={Java_PostfixExpression_operator}

# Java_PrimitiveType class attributes and methods

# Java_PrimitiveTypeBoolean class attributes and methods

# PrimitiveType class attributes and methods

# Java_PrimitiveTypeByte class attributes and methods

# Java_PrimitiveTypeChar class attributes and methods

# Java_PrimitiveTypeDouble class attributes and methods

# Java_PrimitiveTypeShort class attributes and methods

# Java_PrimitiveTypeFloat class attributes and methods

# Java_PrimitiveTypeInt class attributes and methods

# Java_PrimitiveTypeLong class attributes and methods

# Java_PrimitiveTypeVoid class attributes and methods

# Java_ReturnStatement class attributes and methods

# Java_VariableDeclaration class attributes and methods
Java_VariableDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
Java_VariableDeclaration.attributes={Java_VariableDeclaration_extraArrayDimensions}

# Java_SuperFieldAccess class attributes and methods

# AbstractTypeQualifiedExpression class attributes and methods

# Java_SuperMethodInvocation class attributes and methods

# Java_SwitchCase class attributes and methods
Java_SwitchCase_default: Property = Property(name="default", type=BooleanType)
Java_SwitchCase.attributes={Java_SwitchCase_default}

# Java_StringLiteral class attributes and methods
Java_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
Java_StringLiteral.attributes={Java_StringLiteral_escapedValue}

# Java_SuperConstructorInvocation class attributes and methods

# Java_TextElement class attributes and methods
Java_TextElement_text: Property = Property(name="text", type=StringType)
Java_TextElement.attributes={Java_TextElement_text}

# Java_SwitchStatement class attributes and methods

# Java_SynchronizedStatement class attributes and methods

# Java_TypeDeclaration class attributes and methods

# Java_ThisExpression class attributes and methods

# Java_ThrowStatement class attributes and methods

# Java_TryStatement class attributes and methods

# UnresolvedItem class attributes and methods

# Java_TypeDeclarationStatement class attributes and methods

# Java_TypeLiteral class attributes and methods

# Java_UnresolvedItemAccess class attributes and methods

# Java_UnresolvedAnnotationDeclaration class attributes and methods

# AnnotationTypeDeclaration class attributes and methods

# Java_UnresolvedAnnotationTypeMemberDeclaration class attributes and methods

# AnnotationTypeMemberDeclaration class attributes and methods

# Java_UnresolvedClassDeclaration class attributes and methods

# ClassDeclaration class attributes and methods

# Java_UnresolvedEnumDeclaration class attributes and methods

# EnumDeclaration class attributes and methods

# Java_UnresolvedInterfaceDeclaration class attributes and methods

# InterfaceDeclaration class attributes and methods

# Java_UnresolvedLabeledStatement class attributes and methods

# LabeledStatement class attributes and methods

# Java_UnresolvedMethodDeclaration class attributes and methods

# MethodDeclaration class attributes and methods

# Java_UnresolvedSingleVariableDeclaration class attributes and methods

# SingleVariableDeclaration class attributes and methods

# Java_UnresolvedType class attributes and methods

# Java_UnresolvedTypeDeclaration class attributes and methods

# Java_UnresolvedVariableDeclarationFragment class attributes and methods

# VariableDeclarationFragment class attributes and methods

# Java_WhileStatement class attributes and methods

# Java_WildCardType class attributes and methods
Java_WildCardType_upperBound: Property = Property(name="upperBound", type=BooleanType)
Java_WildCardType.attributes={Java_WildCardType_upperBound}

# Relationships
typeParameters4: BinaryAssociation = BinaryAssociation(
    name="typeParameters4",
    ends={
        Property(name="Java_TypeParameter", type=Java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AbstractMethodDeclaration5", type=Java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usagesInDocComments6: BinaryAssociation = BinaryAssociation(
    name="usagesInDocComments6",
    ends={
        Property(name="MethodRef", type=Java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=Java_MethodRef, multiplicity=Multiplicity(0, 9999))
    }
)
usages7: BinaryAssociation = BinaryAssociation(
    name="usages7",
    ends={
        Property(name="AbstractMethodInvocation", type=Java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="method8", type=Java_AbstractMethodInvocation, multiplicity=Multiplicity(0, 9999))
    }
)
body0: BinaryAssociation = BinaryAssociation(
    name="body0",
    ends={
        Property(name="Java_Block", type=Java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AbstractMethodDeclaration", type=Java_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="SingleVariableDeclaration", type=Java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methodDeclaration", type=Java_SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thrownExceptions2: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions2",
    ends={
        Property(name="Java_TypeAccess", type=Java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AbstractMethodDeclaration3", type=Java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsAfterBody16: BinaryAssociation = BinaryAssociation(
    name="commentsAfterBody16",
    ends={
        Property(name="Java_Comment18", type=Java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AbstractTypeDeclaration17", type=Java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package19: BinaryAssociation = BinaryAssociation(
    name="package19",
    ends={
        Property(name="Package", type=Java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements", type=Java_Package, multiplicity=Multiplicity(0, 1))
    }
)
superInterfaces20: BinaryAssociation = BinaryAssociation(
    name="superInterfaces20",
    ends={
        Property(name="Java_TypeAccess22", type=Java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AbstractTypeDeclaration21", type=Java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method9: BinaryAssociation = BinaryAssociation(
    name="method9",
    ends={
        Property(name="AbstractMethodDeclaration", type=Java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="usages", type=Java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
arguments10: BinaryAssociation = BinaryAssociation(
    name="arguments10",
    ends={
        Property(name="Java_Expression", type=Java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AbstractMethodInvocation", type=Java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments11: BinaryAssociation = BinaryAssociation(
    name="typeArguments11",
    ends={
        Property(name="Java_TypeAccess13", type=Java_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AbstractMethodInvocation12", type=Java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations14: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations14",
    ends={
        Property(name="BodyDeclaration", type=Java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractTypeDeclaration", type=Java_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsBeforeBody15: BinaryAssociation = BinaryAssociation(
    name="commentsBeforeBody15",
    ends={
        Property(name="Java_Comment", type=Java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AbstractTypeDeclaration", type=Java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classFiles32: BinaryAssociation = BinaryAssociation(
    name="classFiles32",
    ends={
        Property(name="Java_ClassFile", type=Java_Archive, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Archive", type=Java_ClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifest33: BinaryAssociation = BinaryAssociation(
    name="manifest33",
    ends={
        Property(name="Java_Manifest", type=Java_Archive, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Archive34", type=Java_Manifest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier23: BinaryAssociation = BinaryAssociation(
    name="qualifier23",
    ends={
        Property(name="Java_TypeAccess24", type=Java_AbstractTypeQualifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AbstractTypeQualifiedExpression", type=Java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="Java_TypeAccess26", type=Java_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AbstractVariablesContainer", type=Java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments27: BinaryAssociation = BinaryAssociation(
    name="fragments27",
    ends={
        Property(name="VariableDeclarationFragment", type=Java_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="variablesContainer", type=Java_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="Java_TypeAccess29", type=Java_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Annotation", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values30: BinaryAssociation = BinaryAssociation(
    name="values30",
    ends={
        Property(name="Java_AnnotationMemberValuePair", type=Java_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Annotation31", type=Java_AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default52: BinaryAssociation = BinaryAssociation(
    name="default52",
    ends={
        Property(name="Java_Expression53", type=Java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AnnotationTypeMemberDeclaration", type=Java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="Java_TypeAccess56", type=Java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AnnotationTypeMemberDeclaration55", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message35: BinaryAssociation = BinaryAssociation(
    name="message35",
    ends={
        Property(name="Java_Expression36", type=Java_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AssertStatement", type=Java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression37: BinaryAssociation = BinaryAssociation(
    name="expression37",
    ends={
        Property(name="Java_Expression39", type=Java_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AssertStatement38", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comments40: BinaryAssociation = BinaryAssociation(
    name="comments40",
    ends={
        Property(name="Java_Comment41", type=Java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ASTNode", type=Java_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalCompilationUnit42: BinaryAssociation = BinaryAssociation(
    name="originalCompilationUnit42",
    ends={
        Property(name="Java_CompilationUnit", type=Java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ASTNode43", type=Java_CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
originalClassFile44: BinaryAssociation = BinaryAssociation(
    name="originalClassFile44",
    ends={
        Property(name="Java_ClassFile46", type=Java_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ASTNode45", type=Java_ClassFile, multiplicity=Multiplicity(0, 1))
    }
)
member47: BinaryAssociation = BinaryAssociation(
    name="member47",
    ends={
        Property(name="AnnotationTypeMemberDeclaration", type=Java_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="usages48", type=Java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
value49: BinaryAssociation = BinaryAssociation(
    name="value49",
    ends={
        Property(name="Java_Expression51", type=Java_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_AnnotationMemberValuePair50", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index63: BinaryAssociation = BinaryAssociation(
    name="index63",
    ends={
        Property(name="Java_Expression65", type=Java_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ArrayAccess64", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions66: BinaryAssociation = BinaryAssociation(
    name="dimensions66",
    ends={
        Property(name="Java_Expression67", type=Java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ArrayCreation", type=Java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer68: BinaryAssociation = BinaryAssociation(
    name="initializer68",
    ends={
        Property(name="Java_ArrayInitializer", type=Java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ArrayCreation69", type=Java_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usages57: BinaryAssociation = BinaryAssociation(
    name="usages57",
    ends={
        Property(name="AnnotationMemberValuePair", type=Java_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="member", type=Java_AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999))
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="Java_TypeAccess72", type=Java_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ArrayCreation71", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyDeclarations58: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations58",
    ends={
        Property(name="BodyDeclaration59", type=Java_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclarationOwner", type=Java_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classInstanceCreation60: BinaryAssociation = BinaryAssociation(
    name="classInstanceCreation60",
    ends={
        Property(name="ClassInstanceCreation", type=Java_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclaration", type=Java_ClassInstanceCreation, multiplicity=Multiplicity(0, 1))
    }
)
array61: BinaryAssociation = BinaryAssociation(
    name="array61",
    ends={
        Property(name="Java_Expression62", type=Java_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ArrayAccess", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType78: BinaryAssociation = BinaryAssociation(
    name="elementType78",
    ends={
        Property(name="Java_TypeAccess79", type=Java_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ArrayType", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide80: BinaryAssociation = BinaryAssociation(
    name="leftHandSide80",
    ends={
        Property(name="Java_Expression81", type=Java_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Assignment", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide82: BinaryAssociation = BinaryAssociation(
    name="rightHandSide82",
    ends={
        Property(name="Java_Expression84", type=Java_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Assignment83", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions73: BinaryAssociation = BinaryAssociation(
    name="expressions73",
    ends={
        Property(name="Java_Expression75", type=Java_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ArrayInitializer74", type=Java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
array76: BinaryAssociation = BinaryAssociation(
    name="array76",
    ends={
        Property(name="Java_Expression77", type=Java_ArrayLengthAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ArrayLengthAccess", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
abstractTypeDeclaration85: BinaryAssociation = BinaryAssociation(
    name="abstractTypeDeclaration85",
    ends={
        Property(name="bodyDeclarations", type=Java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1)),
        Property(name="AbstractTypeDeclaration", type=Java_BodyDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
annotations86: BinaryAssociation = BinaryAssociation(
    name="annotations86",
    ends={
        Property(name="Java_Annotation87", type=Java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_BodyDeclaration", type=Java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclarationOwner88: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclarationOwner88",
    ends={
        Property(name="AnonymousClassDeclaration", type=Java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations89", type=Java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
modifier90: BinaryAssociation = BinaryAssociation(
    name="modifier90",
    ends={
        Property(name="Modifier", type=Java_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclaration", type=Java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements91: BinaryAssociation = BinaryAssociation(
    name="statements91",
    ends={
        Property(name="Java_Statement", type=Java_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Block92", type=Java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label93: BinaryAssociation = BinaryAssociation(
    name="label93",
    ends={
        Property(name="LabeledStatement", type=Java_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInBreakStatements", type=Java_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="Java_AbstractTypeDeclaration105", type=Java_ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ClassFile104", type=Java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
attachedSource106: BinaryAssociation = BinaryAssociation(
    name="attachedSource106",
    ends={
        Property(name="Java_CompilationUnit108", type=Java_ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ClassFile107", type=Java_CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
package109: BinaryAssociation = BinaryAssociation(
    name="package109",
    ends={
        Property(name="Java_Package", type=Java_ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ClassFile110", type=Java_Package, multiplicity=Multiplicity(0, 1))
    }
)
anonymousClassDeclaration111: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration111",
    ends={
        Property(name="AnonymousClassDeclaration112", type=Java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="classInstanceCreation", type=Java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression113: BinaryAssociation = BinaryAssociation(
    name="expression113",
    ends={
        Property(name="Java_Expression114", type=Java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ClassInstanceCreation", type=Java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type115: BinaryAssociation = BinaryAssociation(
    name="type115",
    ends={
        Property(name="Java_TypeAccess117", type=Java_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ClassInstanceCreation116", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression94: BinaryAssociation = BinaryAssociation(
    name="expression94",
    ends={
        Property(name="Java_Expression95", type=Java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_CastExpression", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type96: BinaryAssociation = BinaryAssociation(
    name="type96",
    ends={
        Property(name="Java_TypeAccess98", type=Java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_CastExpression97", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception99: BinaryAssociation = BinaryAssociation(
    name="exception99",
    ends={
        Property(name="SingleVariableDeclaration100", type=Java_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="catchClause", type=Java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body101: BinaryAssociation = BinaryAssociation(
    name="body101",
    ends={
        Property(name="Java_Block102", type=Java_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_CatchClause", type=Java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
commentList128: BinaryAssociation = BinaryAssociation(
    name="commentList128",
    ends={
        Property(name="Java_Comment130", type=Java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_CompilationUnit129", type=Java_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
imports131: BinaryAssociation = BinaryAssociation(
    name="imports131",
    ends={
        Property(name="Java_ImportDeclaration", type=Java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_CompilationUnit132", type=Java_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package133: BinaryAssociation = BinaryAssociation(
    name="package133",
    ends={
        Property(name="Java_Package135", type=Java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_CompilationUnit134", type=Java_Package, multiplicity=Multiplicity(0, 1))
    }
)
types136: BinaryAssociation = BinaryAssociation(
    name="types136",
    ends={
        Property(name="Java_AbstractTypeDeclaration138", type=Java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_CompilationUnit137", type=Java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
label139: BinaryAssociation = BinaryAssociation(
    name="label139",
    ends={
        Property(name="LabeledStatement140", type=Java_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInContinueStatements", type=Java_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
expression141: BinaryAssociation = BinaryAssociation(
    name="expression141",
    ends={
        Property(name="Java_Expression142", type=Java_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_DoStatement", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body143: BinaryAssociation = BinaryAssociation(
    name="body143",
    ends={
        Property(name="Java_Statement145", type=Java_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_DoStatement144", type=Java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression118: BinaryAssociation = BinaryAssociation(
    name="elseExpression118",
    ends={
        Property(name="Java_Expression119", type=Java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ConditionalExpression", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body146: BinaryAssociation = BinaryAssociation(
    name="body146",
    ends={
        Property(name="Java_Statement147", type=Java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_EnhancedForStatement", type=Java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression120: BinaryAssociation = BinaryAssociation(
    name="expression120",
    ends={
        Property(name="Java_Expression122", type=Java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ConditionalExpression121", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression148: BinaryAssociation = BinaryAssociation(
    name="expression148",
    ends={
        Property(name="Java_Expression150", type=Java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_EnhancedForStatement149", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression123: BinaryAssociation = BinaryAssociation(
    name="thenExpression123",
    ends={
        Property(name="Java_Expression125", type=Java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ConditionalExpression124", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter151: BinaryAssociation = BinaryAssociation(
    name="parameter151",
    ends={
        Property(name="SingleVariableDeclaration152", type=Java_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="enhancedForStatement", type=Java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superClass126: BinaryAssociation = BinaryAssociation(
    name="superClass126",
    ends={
        Property(name="Java_TypeAccess127", type=Java_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ClassDeclaration", type=Java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonymousClassDeclaration153: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration153",
    ends={
        Property(name="Java_AnonymousClassDeclaration", type=Java_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_EnumConstantDeclaration", type=Java_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body173: BinaryAssociation = BinaryAssociation(
    name="body173",
    ends={
        Property(name="Java_Statement175", type=Java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ForStatement174", type=Java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumConstants157: BinaryAssociation = BinaryAssociation(
    name="enumConstants157",
    ends={
        Property(name="Java_EnumConstantDeclaration158", type=Java_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_EnumDeclaration", type=Java_EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression176: BinaryAssociation = BinaryAssociation(
    name="expression176",
    ends={
        Property(name="Java_Expression177", type=Java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_IfStatement", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression159: BinaryAssociation = BinaryAssociation(
    name="expression159",
    ends={
        Property(name="Java_Expression160", type=Java_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ExpressionStatement", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
field161: BinaryAssociation = BinaryAssociation(
    name="field161",
    ends={
        Property(name="Java_SingleVariableAccess", type=Java_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_FieldAccess", type=Java_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression162: BinaryAssociation = BinaryAssociation(
    name="expression162",
    ends={
        Property(name="Java_Expression164", type=Java_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_FieldAccess163", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression165: BinaryAssociation = BinaryAssociation(
    name="expression165",
    ends={
        Property(name="Java_Expression166", type=Java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ForStatement", type=Java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updaters167: BinaryAssociation = BinaryAssociation(
    name="updaters167",
    ends={
        Property(name="Java_Expression169", type=Java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ForStatement168", type=Java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializers170: BinaryAssociation = BinaryAssociation(
    name="initializers170",
    ends={
        Property(name="Java_Expression172", type=Java_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ForStatement171", type=Java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments154: BinaryAssociation = BinaryAssociation(
    name="arguments154",
    ends={
        Property(name="Java_Expression156", type=Java_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_EnumConstantDeclaration155", type=Java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body193: BinaryAssociation = BinaryAssociation(
    name="body193",
    ends={
        Property(name="Java_Block194", type=Java_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Initializer", type=Java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement178: BinaryAssociation = BinaryAssociation(
    name="thenStatement178",
    ends={
        Property(name="Java_Statement180", type=Java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_IfStatement179", type=Java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement181: BinaryAssociation = BinaryAssociation(
    name="elseStatement181",
    ends={
        Property(name="Java_Statement183", type=Java_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_IfStatement182", type=Java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedElement184: BinaryAssociation = BinaryAssociation(
    name="importedElement184",
    ends={
        Property(name="NamedElement", type=Java_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInImports", type=Java_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand185: BinaryAssociation = BinaryAssociation(
    name="rightOperand185",
    ends={
        Property(name="Java_Expression186", type=Java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_InfixExpression", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand187: BinaryAssociation = BinaryAssociation(
    name="leftOperand187",
    ends={
        Property(name="Java_Expression189", type=Java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_InfixExpression188", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands190: BinaryAssociation = BinaryAssociation(
    name="extendedOperands190",
    ends={
        Property(name="Java_Expression192", type=Java_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_InfixExpression191", type=Java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes210: BinaryAssociation = BinaryAssociation(
    name="attributes210",
    ends={
        Property(name="Java_ManifestAttribute212", type=Java_ManifestEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ManifestEntry211", type=Java_ManifestAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member213: BinaryAssociation = BinaryAssociation(
    name="member213",
    ends={
        Property(name="Java_NamedElement", type=Java_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MemberRef", type=Java_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
qualifier214: BinaryAssociation = BinaryAssociation(
    name="qualifier214",
    ends={
        Property(name="Java_TypeAccess216", type=Java_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MemberRef215", type=Java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand195: BinaryAssociation = BinaryAssociation(
    name="rightOperand195",
    ends={
        Property(name="Java_TypeAccess196", type=Java_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_InstanceofExpression", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand197: BinaryAssociation = BinaryAssociation(
    name="leftOperand197",
    ends={
        Property(name="Java_Expression199", type=Java_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_InstanceofExpression198", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tags200: BinaryAssociation = BinaryAssociation(
    name="tags200",
    ends={
        Property(name="Java_TagElement", type=Java_Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Javadoc", type=Java_TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body201: BinaryAssociation = BinaryAssociation(
    name="body201",
    ends={
        Property(name="Java_Statement202", type=Java_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_LabeledStatement", type=Java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usagesInBreakStatements203: BinaryAssociation = BinaryAssociation(
    name="usagesInBreakStatements203",
    ends={
        Property(name="BreakStatement", type=Java_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=Java_BreakStatement, multiplicity=Multiplicity(0, 9999))
    }
)
usagesInContinueStatements204: BinaryAssociation = BinaryAssociation(
    name="usagesInContinueStatements204",
    ends={
        Property(name="ContinueStatement", type=Java_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="label205", type=Java_ContinueStatement, multiplicity=Multiplicity(0, 9999))
    }
)
mainAttributes206: BinaryAssociation = BinaryAssociation(
    name="mainAttributes206",
    ends={
        Property(name="Java_ManifestAttribute", type=Java_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Manifest207", type=Java_ManifestAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryAttributes208: BinaryAssociation = BinaryAssociation(
    name="entryAttributes208",
    ends={
        Property(name="Java_ManifestEntry", type=Java_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Manifest209", type=Java_ManifestEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElements235: BinaryAssociation = BinaryAssociation(
    name="ownedElements235",
    ends={
        Property(name="Package236", type=Java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=Java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orphanTypes237: BinaryAssociation = BinaryAssociation(
    name="orphanTypes237",
    ends={
        Property(name="Java_Type", type=Java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Model", type=Java_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType217: BinaryAssociation = BinaryAssociation(
    name="returnType217",
    ends={
        Property(name="Java_TypeAccess218", type=Java_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MethodDeclaration", type=Java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedMethodDeclaration220: BinaryAssociation = BinaryAssociation(
    name="redefinedMethodDeclaration220",
    ends={
        Property(name="MethodDeclaration", type=Java_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinitions", type=Java_MethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
redefinitions222: BinaryAssociation = BinaryAssociation(
    name="redefinitions222",
    ends={
        Property(name="MethodDeclaration223", type=Java_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinedMethodDeclaration", type=Java_MethodDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
expression224: BinaryAssociation = BinaryAssociation(
    name="expression224",
    ends={
        Property(name="Java_Expression225", type=Java_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MethodInvocation", type=Java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method226: BinaryAssociation = BinaryAssociation(
    name="method226",
    ends={
        Property(name="AbstractMethodDeclaration227", type=Java_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInDocComments", type=Java_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
qualifier228: BinaryAssociation = BinaryAssociation(
    name="qualifier228",
    ends={
        Property(name="Java_TypeAccess229", type=Java_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MethodRef", type=Java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters230: BinaryAssociation = BinaryAssociation(
    name="parameters230",
    ends={
        Property(name="Java_MethodRefParameter", type=Java_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MethodRef231", type=Java_MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type232: BinaryAssociation = BinaryAssociation(
    name="type232",
    ends={
        Property(name="Java_TypeAccess234", type=Java_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MethodRefParameter233", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
singleVariableDeclaration251: BinaryAssociation = BinaryAssociation(
    name="singleVariableDeclaration251",
    ends={
        Property(name="SingleVariableDeclaration253", type=Java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier252", type=Java_SingleVariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclarationStatement254: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationStatement254",
    ends={
        Property(name="VariableDeclarationStatement", type=Java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier255", type=Java_VariableDeclarationStatement, multiplicity=Multiplicity(0, 1))
    }
)
unresolvedItems238: BinaryAssociation = BinaryAssociation(
    name="unresolvedItems238",
    ends={
        Property(name="Java_UnresolvedItem", type=Java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Model239", type=Java_UnresolvedItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits240: BinaryAssociation = BinaryAssociation(
    name="compilationUnits240",
    ends={
        Property(name="Java_CompilationUnit242", type=Java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Model241", type=Java_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classFiles243: BinaryAssociation = BinaryAssociation(
    name="classFiles243",
    ends={
        Property(name="Java_ClassFile245", type=Java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Model244", type=Java_ClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archives246: BinaryAssociation = BinaryAssociation(
    name="archives246",
    ends={
        Property(name="Java_Archive248", type=Java_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Model247", type=Java_Archive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usagesInPackageAccess270: BinaryAssociation = BinaryAssociation(
    name="usagesInPackageAccess270",
    ends={
        Property(name="PackageAccess", type=Java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package271", type=Java_PackageAccess, multiplicity=Multiplicity(0, 9999))
    }
)
bodyDeclaration249: BinaryAssociation = BinaryAssociation(
    name="bodyDeclaration249",
    ends={
        Property(name="BodyDeclaration250", type=Java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier", type=Java_BodyDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclarationExpression256: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationExpression256",
    ends={
        Property(name="VariableDeclarationExpression", type=Java_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier257", type=Java_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1))
    }
)
usagesInImports258: BinaryAssociation = BinaryAssociation(
    name="usagesInImports258",
    ends={
        Property(name="ImportDeclaration", type=Java_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="importedElement", type=Java_ImportDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElements259: BinaryAssociation = BinaryAssociation(
    name="ownedElements259",
    ends={
        Property(name="AbstractTypeDeclaration260", type=Java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=Java_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model261: BinaryAssociation = BinaryAssociation(
    name="model261",
    ends={
        Property(name="Model", type=Java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements262", type=Java_Model, multiplicity=Multiplicity(0, 1))
    }
)
ownedPackages264: BinaryAssociation = BinaryAssociation(
    name="ownedPackages264",
    ends={
        Property(name="Package266", type=Java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package265", type=Java_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package268: BinaryAssociation = BinaryAssociation(
    name="package268",
    ends={
        Property(name="Package269", type=Java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPackages", type=Java_Package, multiplicity=Multiplicity(0, 1))
    }
)
operand285: BinaryAssociation = BinaryAssociation(
    name="operand285",
    ends={
        Property(name="Java_Expression286", type=Java_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_PrefixExpression", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
package272: BinaryAssociation = BinaryAssociation(
    name="package272",
    ends={
        Property(name="Package273", type=Java_PackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInPackageAccess", type=Java_Package, multiplicity=Multiplicity(1, 1))
    }
)
qualifier275: BinaryAssociation = BinaryAssociation(
    name="qualifier275",
    ends={
        Property(name="Java_PackageAccess", type=Java_PackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_PackageAccess274", type=Java_PackageAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type276: BinaryAssociation = BinaryAssociation(
    name="type276",
    ends={
        Property(name="Java_TypeAccess277", type=Java_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ParameterizedType", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments278: BinaryAssociation = BinaryAssociation(
    name="typeArguments278",
    ends={
        Property(name="Java_TypeAccess280", type=Java_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ParameterizedType279", type=Java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression281: BinaryAssociation = BinaryAssociation(
    name="expression281",
    ends={
        Property(name="Java_Expression282", type=Java_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ParenthesizedExpression", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand283: BinaryAssociation = BinaryAssociation(
    name="operand283",
    ends={
        Property(name="Java_Expression284", type=Java_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_PostfixExpression", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier290: BinaryAssociation = BinaryAssociation(
    name="qualifier290",
    ends={
        Property(name="Java_Expression292", type=Java_SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_SingleVariableAccess291", type=Java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifier293: BinaryAssociation = BinaryAssociation(
    name="modifier293",
    ends={
        Property(name="Modifier294", type=Java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="singleVariableDeclaration", type=Java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type295: BinaryAssociation = BinaryAssociation(
    name="type295",
    ends={
        Property(name="Java_TypeAccess296", type=Java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_SingleVariableDeclaration", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression287: BinaryAssociation = BinaryAssociation(
    name="expression287",
    ends={
        Property(name="Java_Expression288", type=Java_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ReturnStatement", type=Java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable289: BinaryAssociation = BinaryAssociation(
    name="variable289",
    ends={
        Property(name="VariableDeclaration", type=Java_SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usageInVariableAccess", type=Java_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
field306: BinaryAssociation = BinaryAssociation(
    name="field306",
    ends={
        Property(name="Java_SingleVariableAccess307", type=Java_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_SuperFieldAccess", type=Java_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations297: BinaryAssociation = BinaryAssociation(
    name="annotations297",
    ends={
        Property(name="Java_Annotation299", type=Java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_SingleVariableDeclaration298", type=Java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodDeclaration300: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration300",
    ends={
        Property(name="AbstractMethodDeclaration301", type=Java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Java_AbstractMethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
catchClause302: BinaryAssociation = BinaryAssociation(
    name="catchClause302",
    ends={
        Property(name="CatchClause", type=Java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="exception", type=Java_CatchClause, multiplicity=Multiplicity(0, 1))
    }
)
enhancedForStatement303: BinaryAssociation = BinaryAssociation(
    name="enhancedForStatement303",
    ends={
        Property(name="EnhancedForStatement", type=Java_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=Java_EnhancedForStatement, multiplicity=Multiplicity(0, 1))
    }
)
expression304: BinaryAssociation = BinaryAssociation(
    name="expression304",
    ends={
        Property(name="Java_Expression305", type=Java_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_SuperConstructorInvocation", type=Java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments320: BinaryAssociation = BinaryAssociation(
    name="fragments320",
    ends={
        Property(name="Java_ASTNode322", type=Java_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_TagElement321", type=Java_ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression308: BinaryAssociation = BinaryAssociation(
    name="expression308",
    ends={
        Property(name="Java_Expression309", type=Java_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_SwitchCase", type=Java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression310: BinaryAssociation = BinaryAssociation(
    name="expression310",
    ends={
        Property(name="Java_Expression311", type=Java_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_SwitchStatement", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements312: BinaryAssociation = BinaryAssociation(
    name="statements312",
    ends={
        Property(name="Java_Statement314", type=Java_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_SwitchStatement313", type=Java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body315: BinaryAssociation = BinaryAssociation(
    name="body315",
    ends={
        Property(name="Java_Block316", type=Java_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_SynchronizedStatement", type=Java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression317: BinaryAssociation = BinaryAssociation(
    name="expression317",
    ends={
        Property(name="Java_Expression319", type=Java_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_SynchronizedStatement318", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier335: BinaryAssociation = BinaryAssociation(
    name="qualifier335",
    ends={
        Property(name="Java_NamespaceAccess", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_TypeAccess336", type=Java_NamespaceAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression323: BinaryAssociation = BinaryAssociation(
    name="expression323",
    ends={
        Property(name="Java_Expression324", type=Java_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_ThrowStatement", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body325: BinaryAssociation = BinaryAssociation(
    name="body325",
    ends={
        Property(name="Java_Block326", type=Java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_TryStatement", type=Java_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally327: BinaryAssociation = BinaryAssociation(
    name="finally327",
    ends={
        Property(name="Java_Block329", type=Java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_TryStatement328", type=Java_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses330: BinaryAssociation = BinaryAssociation(
    name="catchClauses330",
    ends={
        Property(name="Java_CatchClause332", type=Java_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_TryStatement331", type=Java_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usagesInTypeAccess333: BinaryAssociation = BinaryAssociation(
    name="usagesInTypeAccess333",
    ends={
        Property(name="TypeAccess", type=Java_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=Java_TypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
type334: BinaryAssociation = BinaryAssociation(
    name="type334",
    ends={
        Property(name="Type", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInTypeAccess", type=Java_Type, multiplicity=Multiplicity(1, 1))
    }
)
typeParameters337: BinaryAssociation = BinaryAssociation(
    name="typeParameters337",
    ends={
        Property(name="Java_TypeParameter338", type=Java_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_TypeDeclaration", type=Java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration339: BinaryAssociation = BinaryAssociation(
    name="declaration339",
    ends={
        Property(name="Java_AbstractTypeDeclaration340", type=Java_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_TypeDeclarationStatement", type=Java_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type341: BinaryAssociation = BinaryAssociation(
    name="type341",
    ends={
        Property(name="Java_TypeAccess342", type=Java_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_TypeLiteral", type=Java_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bounds343: BinaryAssociation = BinaryAssociation(
    name="bounds343",
    ends={
        Property(name="Java_TypeAccess345", type=Java_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_TypeParameter344", type=Java_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element346: BinaryAssociation = BinaryAssociation(
    name="element346",
    ends={
        Property(name="Java_UnresolvedItem347", type=Java_UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_UnresolvedItemAccess", type=Java_UnresolvedItem, multiplicity=Multiplicity(0, 1))
    }
)
qualifier348: BinaryAssociation = BinaryAssociation(
    name="qualifier348",
    ends={
        Property(name="Java_ASTNode350", type=Java_UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_UnresolvedItemAccess349", type=Java_ASTNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usageInVariableAccess353: BinaryAssociation = BinaryAssociation(
    name="usageInVariableAccess353",
    ends={
        Property(name="SingleVariableAccess", type=Java_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=Java_SingleVariableAccess, multiplicity=Multiplicity(0, 9999))
    }
)
initializer351: BinaryAssociation = BinaryAssociation(
    name="initializer351",
    ends={
        Property(name="Java_Expression352", type=Java_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_VariableDeclaration", type=Java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bound363: BinaryAssociation = BinaryAssociation(
    name="bound363",
    ends={
        Property(name="Java_TypeAccess364", type=Java_WildCardType, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_WildCardType", type=Java_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression365: BinaryAssociation = BinaryAssociation(
    name="expression365",
    ends={
        Property(name="Java_Expression366", type=Java_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_WhileStatement", type=Java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body367: BinaryAssociation = BinaryAssociation(
    name="body367",
    ends={
        Property(name="Java_Statement369", type=Java_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_WhileStatement368", type=Java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifier354: BinaryAssociation = BinaryAssociation(
    name="modifier354",
    ends={
        Property(name="Modifier355", type=Java_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationExpression", type=Java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations356: BinaryAssociation = BinaryAssociation(
    name="annotations356",
    ends={
        Property(name="Java_Annotation357", type=Java_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_VariableDeclarationExpression", type=Java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variablesContainer358: BinaryAssociation = BinaryAssociation(
    name="variablesContainer358",
    ends={
        Property(name="AbstractVariablesContainer", type=Java_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=Java_AbstractVariablesContainer, multiplicity=Multiplicity(0, 1))
    }
)
modifier359: BinaryAssociation = BinaryAssociation(
    name="modifier359",
    ends={
        Property(name="Modifier360", type=Java_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationStatement", type=Java_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations361: BinaryAssociation = BinaryAssociation(
    name="annotations361",
    ends={
        Property(name="Java_Annotation362", type=Java_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_VariableDeclarationStatement", type=Java_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Java_AbstractMethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java_AbstractMethodDeclaration)
gen_Java_AbstractTypeQualifiedExpression_Expression = Generalization(general=Expression, specific=Java_AbstractTypeQualifiedExpression)
gen_Java_AbstractMethodInvocation_ASTNode = Generalization(general=ASTNode, specific=Java_AbstractMethodInvocation)
gen_Java_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java_AbstractTypeDeclaration)
gen_Java_AbstractTypeDeclaration_Type = Generalization(general=Type, specific=Java_AbstractTypeDeclaration)
gen_Java_AssertStatement_Statement = Generalization(general=Statement, specific=Java_AssertStatement)
gen_Java_AbstractVariablesContainer_ASTNode = Generalization(general=ASTNode, specific=Java_AbstractVariablesContainer)
gen_Java_Annotation_Expression = Generalization(general=Expression, specific=Java_Annotation)
gen_Java_Archive_NamedElement = Generalization(general=NamedElement, specific=Java_Archive)
gen_Java_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=Java_AnnotationTypeDeclaration)
gen_Java_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java_AnnotationTypeMemberDeclaration)
gen_Java_AnnotationMemberValuePair_NamedElement = Generalization(general=NamedElement, specific=Java_AnnotationMemberValuePair)
gen_Java_ArrayCreation_Expression = Generalization(general=Expression, specific=Java_ArrayCreation)
gen_Java_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=Java_AnonymousClassDeclaration)
gen_Java_ArrayAccess_Expression = Generalization(general=Expression, specific=Java_ArrayAccess)
gen_Java_ArrayType_Type = Generalization(general=Type, specific=Java_ArrayType)
gen_Java_Assignment_Expression = Generalization(general=Expression, specific=Java_Assignment)
gen_Java_ArrayInitializer_Expression = Generalization(general=Expression, specific=Java_ArrayInitializer)
gen_Java_ArrayLengthAccess_Expression = Generalization(general=Expression, specific=Java_ArrayLengthAccess)
gen_Java_BooleanLiteral_Expression = Generalization(general=Expression, specific=Java_BooleanLiteral)
gen_Java_BlockComment_Comment = Generalization(general=Comment, specific=Java_BlockComment)
gen_Java_Block_Statement = Generalization(general=Statement, specific=Java_Block)
gen_Java_BreakStatement_Statement = Generalization(general=Statement, specific=Java_BreakStatement)
gen_Java_BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=Java_BodyDeclaration)
gen_Java_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=Java_ClassInstanceCreation)
gen_Java_ClassInstanceCreation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=Java_ClassInstanceCreation)
gen_Java_ConstructorDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=Java_ConstructorDeclaration)
gen_Java_ConditionalExpression_Expression = Generalization(general=Expression, specific=Java_ConditionalExpression)
gen_Java_CastExpression_Expression = Generalization(general=Expression, specific=Java_CastExpression)
gen_Java_CatchClause_Statement = Generalization(general=Statement, specific=Java_CatchClause)
gen_Java_CharacterLiteral_Expression = Generalization(general=Expression, specific=Java_CharacterLiteral)
gen_Java_ClassFile_NamedElement = Generalization(general=NamedElement, specific=Java_ClassFile)
gen_Java_CompilationUnit_NamedElement = Generalization(general=NamedElement, specific=Java_CompilationUnit)
gen_Java_ContinueStatement_Statement = Generalization(general=Statement, specific=Java_ContinueStatement)
gen_Java_DoStatement_Statement = Generalization(general=Statement, specific=Java_DoStatement)
gen_Java_EmptyStatement_Statement = Generalization(general=Statement, specific=Java_EmptyStatement)
gen_Java_EnhancedForStatement_Statement = Generalization(general=Statement, specific=Java_EnhancedForStatement)
gen_Java_ConstructorInvocation_Statement = Generalization(general=Statement, specific=Java_ConstructorInvocation)
gen_Java_ConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=Java_ConstructorInvocation)
gen_Java_ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=Java_ClassDeclaration)
gen_Java_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java_EnumConstantDeclaration)
gen_Java_EnumConstantDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=Java_EnumConstantDeclaration)
gen_Java_Comment_ASTNode = Generalization(general=ASTNode, specific=Java_Comment)
gen_Java_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=Java_EnumDeclaration)
gen_Java_IfStatement_Statement = Generalization(general=Statement, specific=Java_IfStatement)
gen_Java_Expression_ASTNode = Generalization(general=ASTNode, specific=Java_Expression)
gen_Java_ExpressionStatement_Statement = Generalization(general=Statement, specific=Java_ExpressionStatement)
gen_Java_FieldAccess_Expression = Generalization(general=Expression, specific=Java_FieldAccess)
gen_Java_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java_FieldDeclaration)
gen_Java_FieldDeclaration_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=Java_FieldDeclaration)
gen_Java_ForStatement_Statement = Generalization(general=Statement, specific=Java_ForStatement)
gen_Java_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java_Initializer)
gen_Java_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=Java_ImportDeclaration)
gen_Java_InfixExpression_Expression = Generalization(general=Expression, specific=Java_InfixExpression)
gen_Java_MemberRef_ASTNode = Generalization(general=ASTNode, specific=Java_MemberRef)
gen_Java_InstanceofExpression_Expression = Generalization(general=Expression, specific=Java_InstanceofExpression)
gen_Java_InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=Java_InterfaceDeclaration)
gen_Java_Javadoc_Comment = Generalization(general=Comment, specific=Java_Javadoc)
gen_Java_LabeledStatement_NamedElement = Generalization(general=NamedElement, specific=Java_LabeledStatement)
gen_Java_LabeledStatement_Statement = Generalization(general=Statement, specific=Java_LabeledStatement)
gen_Java_LineComment_Comment = Generalization(general=Comment, specific=Java_LineComment)
gen_Java_MethodDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=Java_MethodDeclaration)
gen_Java_MethodInvocation_Expression = Generalization(general=Expression, specific=Java_MethodInvocation)
gen_Java_MethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=Java_MethodInvocation)
gen_Java_MethodRef_ASTNode = Generalization(general=ASTNode, specific=Java_MethodRef)
gen_Java_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=Java_MethodRefParameter)
gen_Java_Modifier_ASTNode = Generalization(general=ASTNode, specific=Java_Modifier)
gen_Java_PackageAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=Java_PackageAccess)
gen_Java_NamedElement_ASTNode = Generalization(general=ASTNode, specific=Java_NamedElement)
gen_Java_NamespaceAccess_ASTNode = Generalization(general=ASTNode, specific=Java_NamespaceAccess)
gen_Java_NumberLiteral_Expression = Generalization(general=Expression, specific=Java_NumberLiteral)
gen_Java_NullLiteral_Expression = Generalization(general=Expression, specific=Java_NullLiteral)
gen_Java_Package_NamedElement = Generalization(general=NamedElement, specific=Java_Package)
gen_Java_PrefixExpression_Expression = Generalization(general=Expression, specific=Java_PrefixExpression)
gen_Java_ParameterizedType_Type = Generalization(general=Type, specific=Java_ParameterizedType)
gen_Java_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=Java_ParenthesizedExpression)
gen_Java_PostfixExpression_Expression = Generalization(general=Expression, specific=Java_PostfixExpression)
gen_Java_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=Java_SingleVariableDeclaration)
gen_Java_PrimitiveType_Type = Generalization(general=Type, specific=Java_PrimitiveType)
gen_Java_PrimitiveTypeBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=Java_PrimitiveTypeBoolean)
gen_Java_PrimitiveTypeByte_PrimitiveType = Generalization(general=PrimitiveType, specific=Java_PrimitiveTypeByte)
gen_Java_PrimitiveTypeChar_PrimitiveType = Generalization(general=PrimitiveType, specific=Java_PrimitiveTypeChar)
gen_Java_PrimitiveTypeDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=Java_PrimitiveTypeDouble)
gen_Java_PrimitiveTypeShort_PrimitiveType = Generalization(general=PrimitiveType, specific=Java_PrimitiveTypeShort)
gen_Java_PrimitiveTypeFloat_PrimitiveType = Generalization(general=PrimitiveType, specific=Java_PrimitiveTypeFloat)
gen_Java_PrimitiveTypeInt_PrimitiveType = Generalization(general=PrimitiveType, specific=Java_PrimitiveTypeInt)
gen_Java_PrimitiveTypeLong_PrimitiveType = Generalization(general=PrimitiveType, specific=Java_PrimitiveTypeLong)
gen_Java_PrimitiveTypeVoid_PrimitiveType = Generalization(general=PrimitiveType, specific=Java_PrimitiveTypeVoid)
gen_Java_ReturnStatement_Statement = Generalization(general=Statement, specific=Java_ReturnStatement)
gen_Java_SingleVariableAccess_Expression = Generalization(general=Expression, specific=Java_SingleVariableAccess)
gen_Java_SuperFieldAccess_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=Java_SuperFieldAccess)
gen_Java_SuperMethodInvocation_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=Java_SuperMethodInvocation)
gen_Java_SuperMethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=Java_SuperMethodInvocation)
gen_Java_SwitchCase_Statement = Generalization(general=Statement, specific=Java_SwitchCase)
gen_Java_Statement_ASTNode = Generalization(general=ASTNode, specific=Java_Statement)
gen_Java_StringLiteral_Expression = Generalization(general=Expression, specific=Java_StringLiteral)
gen_Java_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=Java_SuperConstructorInvocation)
gen_Java_SuperConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=Java_SuperConstructorInvocation)
gen_Java_TextElement_ASTNode = Generalization(general=ASTNode, specific=Java_TextElement)
gen_Java_SwitchStatement_Statement = Generalization(general=Statement, specific=Java_SwitchStatement)
gen_Java_SynchronizedStatement_Statement = Generalization(general=Statement, specific=Java_SynchronizedStatement)
gen_Java_TagElement_ASTNode = Generalization(general=ASTNode, specific=Java_TagElement)
gen_Java_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=Java_TypeDeclaration)
gen_Java_ThisExpression_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=Java_ThisExpression)
gen_Java_ThrowStatement_Statement = Generalization(general=Statement, specific=Java_ThrowStatement)
gen_Java_TryStatement_Statement = Generalization(general=Statement, specific=Java_TryStatement)
gen_Java_Type_NamedElement = Generalization(general=NamedElement, specific=Java_Type)
gen_Java_TypeAccess_Expression = Generalization(general=Expression, specific=Java_TypeAccess)
gen_Java_TypeAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=Java_TypeAccess)
gen_Java_UnresolvedAnnotationDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedAnnotationDeclaration)
gen_Java_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=Java_TypeDeclarationStatement)
gen_Java_TypeLiteral_Expression = Generalization(general=Expression, specific=Java_TypeLiteral)
gen_Java_TypeParameter_Type = Generalization(general=Type, specific=Java_TypeParameter)
gen_Java_UnresolvedItem_NamedElement = Generalization(general=NamedElement, specific=Java_UnresolvedItem)
gen_Java_UnresolvedItemAccess_Expression = Generalization(general=Expression, specific=Java_UnresolvedItemAccess)
gen_Java_UnresolvedItemAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=Java_UnresolvedItemAccess)
gen_Java_UnresolvedAnnotationDeclaration_AnnotationTypeDeclaration = Generalization(general=AnnotationTypeDeclaration, specific=Java_UnresolvedAnnotationDeclaration)
gen_Java_UnresolvedAnnotationTypeMemberDeclaration_AnnotationTypeMemberDeclaration = Generalization(general=AnnotationTypeMemberDeclaration, specific=Java_UnresolvedAnnotationTypeMemberDeclaration)
gen_Java_UnresolvedAnnotationTypeMemberDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedAnnotationTypeMemberDeclaration)
gen_Java_UnresolvedClassDeclaration_ClassDeclaration = Generalization(general=ClassDeclaration, specific=Java_UnresolvedClassDeclaration)
gen_Java_UnresolvedClassDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedClassDeclaration)
gen_Java_UnresolvedEnumDeclaration_EnumDeclaration = Generalization(general=EnumDeclaration, specific=Java_UnresolvedEnumDeclaration)
gen_Java_UnresolvedEnumDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedEnumDeclaration)
gen_Java_UnresolvedInterfaceDeclaration_InterfaceDeclaration = Generalization(general=InterfaceDeclaration, specific=Java_UnresolvedInterfaceDeclaration)
gen_Java_UnresolvedInterfaceDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedInterfaceDeclaration)
gen_Java_UnresolvedLabeledStatement_LabeledStatement = Generalization(general=LabeledStatement, specific=Java_UnresolvedLabeledStatement)
gen_Java_UnresolvedLabeledStatement_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedLabeledStatement)
gen_Java_UnresolvedMethodDeclaration_MethodDeclaration = Generalization(general=MethodDeclaration, specific=Java_UnresolvedMethodDeclaration)
gen_Java_UnresolvedMethodDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedMethodDeclaration)
gen_Java_UnresolvedSingleVariableDeclaration_SingleVariableDeclaration = Generalization(general=SingleVariableDeclaration, specific=Java_UnresolvedSingleVariableDeclaration)
gen_Java_UnresolvedSingleVariableDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedSingleVariableDeclaration)
gen_Java_UnresolvedType_Type = Generalization(general=Type, specific=Java_UnresolvedType)
gen_Java_UnresolvedType_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedType)
gen_Java_UnresolvedTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=Java_UnresolvedTypeDeclaration)
gen_Java_UnresolvedTypeDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedTypeDeclaration)
gen_Java_UnresolvedVariableDeclarationFragment_VariableDeclarationFragment = Generalization(general=VariableDeclarationFragment, specific=Java_UnresolvedVariableDeclarationFragment)
gen_Java_UnresolvedVariableDeclarationFragment_UnresolvedItem = Generalization(general=UnresolvedItem, specific=Java_UnresolvedVariableDeclarationFragment)
gen_Java_VariableDeclaration_NamedElement = Generalization(general=NamedElement, specific=Java_VariableDeclaration)
gen_Java_WhileStatement_Statement = Generalization(general=Statement, specific=Java_WhileStatement)
gen_Java_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=Java_VariableDeclarationExpression)
gen_Java_VariableDeclarationExpression_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=Java_VariableDeclarationExpression)
gen_Java_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=Java_VariableDeclarationFragment)
gen_Java_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=Java_VariableDeclarationStatement)
gen_Java_VariableDeclarationStatement_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=Java_VariableDeclarationStatement)
gen_Java_WildCardType_Type = Generalization(general=Type, specific=Java_WildCardType)

# Domain Model
domain_model = DomainModel(
    name="Java",
    types={Java_TypeParameter, Java_MethodRef, Java_AbstractMethodInvocation, Java_AbstractMethodDeclaration, BodyDeclaration, Java_Block, Java_SingleVariableDeclaration, Java_TypeAccess, Java_Package, Java_AbstractTypeQualifiedExpression, Expression, ASTNode, Java_Expression, Java_AbstractTypeDeclaration, Type, Java_BodyDeclaration, Java_Comment, Java_ClassFile, Java_Manifest, Java_AssertStatement, Statement, Java_AbstractVariablesContainer, Java_VariableDeclarationFragment, Java_Annotation, Java_AnnotationMemberValuePair, Java_Archive, NamedElement, Java_AnnotationTypeDeclaration, AbstractTypeDeclaration, Java_ASTNode, Java_CompilationUnit, Java_AnnotationTypeMemberDeclaration, Java_ArrayCreation, Java_ArrayInitializer, Java_AnonymousClassDeclaration, Java_ClassInstanceCreation, Java_ArrayAccess, Java_ArrayType, Java_Assignment, Java_ArrayLengthAccess, Java_Modifier, Java_BooleanLiteral, Java_BlockComment, Comment, Java_Statement, Java_BreakStatement, Java_LabeledStatement, AbstractMethodInvocation, Java_ConstructorDeclaration, AbstractMethodDeclaration, Java_ConditionalExpression, Java_CastExpression, Java_CatchClause, Java_CharacterLiteral, Java_ImportDeclaration, Java_ContinueStatement, Java_DoStatement, Java_EmptyStatement, Java_EnhancedForStatement, Java_ConstructorInvocation, Java_ClassDeclaration, TypeDeclaration, Java_EnumConstantDeclaration, VariableDeclaration, Java_EnumDeclaration, Java_IfStatement, Java_ExpressionStatement, Java_FieldAccess, Java_SingleVariableAccess, Java_FieldDeclaration, AbstractVariablesContainer, Java_ForStatement, Java_Initializer, Java_NamedElement, Java_InfixExpression, Java_MemberRef, Java_InstanceofExpression, Java_InterfaceDeclaration, Java_Javadoc, Java_TagElement, Java_LineComment, Java_ManifestAttribute, Java_ManifestEntry, Java_Model, Java_Type, Java_UnresolvedItem, Java_MethodDeclaration, Java_MethodInvocation, Java_MethodRefParameter, Java_VariableDeclarationStatement, Java_VariableDeclarationExpression, Java_PackageAccess, NamespaceAccess, Java_NamespaceAccess, Java_NumberLiteral, Java_NullLiteral, Java_PrefixExpression, Java_ParameterizedType, Java_ParenthesizedExpression, Java_PostfixExpression, Java_PrimitiveType, Java_PrimitiveTypeBoolean, PrimitiveType, Java_PrimitiveTypeByte, Java_PrimitiveTypeChar, Java_PrimitiveTypeDouble, Java_PrimitiveTypeShort, Java_PrimitiveTypeFloat, Java_PrimitiveTypeInt, Java_PrimitiveTypeLong, Java_PrimitiveTypeVoid, Java_ReturnStatement, Java_VariableDeclaration, Java_SuperFieldAccess, AbstractTypeQualifiedExpression, Java_SuperMethodInvocation, Java_SwitchCase, Java_StringLiteral, Java_SuperConstructorInvocation, Java_TextElement, Java_SwitchStatement, Java_SynchronizedStatement, Java_TypeDeclaration, Java_ThisExpression, Java_ThrowStatement, Java_TryStatement, UnresolvedItem, Java_TypeDeclarationStatement, Java_TypeLiteral, Java_UnresolvedItemAccess, Java_UnresolvedAnnotationDeclaration, AnnotationTypeDeclaration, Java_UnresolvedAnnotationTypeMemberDeclaration, AnnotationTypeMemberDeclaration, Java_UnresolvedClassDeclaration, ClassDeclaration, Java_UnresolvedEnumDeclaration, EnumDeclaration, Java_UnresolvedInterfaceDeclaration, InterfaceDeclaration, Java_UnresolvedLabeledStatement, LabeledStatement, Java_UnresolvedMethodDeclaration, MethodDeclaration, Java_UnresolvedSingleVariableDeclaration, SingleVariableDeclaration, Java_UnresolvedType, Java_UnresolvedTypeDeclaration, Java_UnresolvedVariableDeclarationFragment, VariableDeclarationFragment, Java_WhileStatement, Java_WildCardType, AssignmentKind, InheritanceKind, InfixExpressionKind, PostfixExpressionKind, PrefixExpressionKind, VisibilityKind},
    associations={typeParameters4, usagesInDocComments6, usages7, body0, parameters1, thrownExceptions2, commentsAfterBody16, package19, superInterfaces20, method9, arguments10, typeArguments11, bodyDeclarations14, commentsBeforeBody15, classFiles32, manifest33, qualifier23, type25, fragments27, type28, values30, default52, type54, message35, expression37, comments40, originalCompilationUnit42, originalClassFile44, member47, value49, index63, dimensions66, initializer68, usages57, type70, bodyDeclarations58, classInstanceCreation60, array61, elementType78, leftHandSide80, rightHandSide82, expressions73, array76, abstractTypeDeclaration85, annotations86, anonymousClassDeclarationOwner88, modifier90, statements91, label93, type103, attachedSource106, package109, anonymousClassDeclaration111, expression113, type115, expression94, type96, exception99, body101, commentList128, imports131, package133, types136, label139, expression141, body143, elseExpression118, body146, expression120, expression148, thenExpression123, parameter151, superClass126, anonymousClassDeclaration153, body173, enumConstants157, expression176, expression159, field161, expression162, expression165, updaters167, initializers170, arguments154, body193, thenStatement178, elseStatement181, importedElement184, rightOperand185, leftOperand187, extendedOperands190, attributes210, member213, qualifier214, rightOperand195, leftOperand197, tags200, body201, usagesInBreakStatements203, usagesInContinueStatements204, mainAttributes206, entryAttributes208, ownedElements235, orphanTypes237, returnType217, redefinedMethodDeclaration220, redefinitions222, expression224, method226, qualifier228, parameters230, type232, singleVariableDeclaration251, variableDeclarationStatement254, unresolvedItems238, compilationUnits240, classFiles243, archives246, usagesInPackageAccess270, bodyDeclaration249, variableDeclarationExpression256, usagesInImports258, ownedElements259, model261, ownedPackages264, package268, operand285, package272, qualifier275, type276, typeArguments278, expression281, operand283, qualifier290, modifier293, type295, expression287, variable289, field306, annotations297, methodDeclaration300, catchClause302, enhancedForStatement303, expression304, fragments320, expression308, expression310, statements312, body315, expression317, qualifier335, expression323, body325, finally327, catchClauses330, usagesInTypeAccess333, type334, typeParameters337, declaration339, type341, bounds343, element346, qualifier348, usageInVariableAccess353, initializer351, bound363, expression365, body367, modifier354, annotations356, variablesContainer358, modifier359, annotations361},
    generalizations={gen_Java_AbstractMethodDeclaration_BodyDeclaration, gen_Java_AbstractTypeQualifiedExpression_Expression, gen_Java_AbstractMethodInvocation_ASTNode, gen_Java_AbstractTypeDeclaration_BodyDeclaration, gen_Java_AbstractTypeDeclaration_Type, gen_Java_AssertStatement_Statement, gen_Java_AbstractVariablesContainer_ASTNode, gen_Java_Annotation_Expression, gen_Java_Archive_NamedElement, gen_Java_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_Java_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_Java_AnnotationMemberValuePair_NamedElement, gen_Java_ArrayCreation_Expression, gen_Java_AnonymousClassDeclaration_ASTNode, gen_Java_ArrayAccess_Expression, gen_Java_ArrayType_Type, gen_Java_Assignment_Expression, gen_Java_ArrayInitializer_Expression, gen_Java_ArrayLengthAccess_Expression, gen_Java_BooleanLiteral_Expression, gen_Java_BlockComment_Comment, gen_Java_Block_Statement, gen_Java_BreakStatement_Statement, gen_Java_BodyDeclaration_NamedElement, gen_Java_ClassInstanceCreation_Expression, gen_Java_ClassInstanceCreation_AbstractMethodInvocation, gen_Java_ConstructorDeclaration_AbstractMethodDeclaration, gen_Java_ConditionalExpression_Expression, gen_Java_CastExpression_Expression, gen_Java_CatchClause_Statement, gen_Java_CharacterLiteral_Expression, gen_Java_ClassFile_NamedElement, gen_Java_CompilationUnit_NamedElement, gen_Java_ContinueStatement_Statement, gen_Java_DoStatement_Statement, gen_Java_EmptyStatement_Statement, gen_Java_EnhancedForStatement_Statement, gen_Java_ConstructorInvocation_Statement, gen_Java_ConstructorInvocation_AbstractMethodInvocation, gen_Java_ClassDeclaration_TypeDeclaration, gen_Java_EnumConstantDeclaration_BodyDeclaration, gen_Java_EnumConstantDeclaration_VariableDeclaration, gen_Java_Comment_ASTNode, gen_Java_EnumDeclaration_AbstractTypeDeclaration, gen_Java_IfStatement_Statement, gen_Java_Expression_ASTNode, gen_Java_ExpressionStatement_Statement, gen_Java_FieldAccess_Expression, gen_Java_FieldDeclaration_BodyDeclaration, gen_Java_FieldDeclaration_AbstractVariablesContainer, gen_Java_ForStatement_Statement, gen_Java_Initializer_BodyDeclaration, gen_Java_ImportDeclaration_ASTNode, gen_Java_InfixExpression_Expression, gen_Java_MemberRef_ASTNode, gen_Java_InstanceofExpression_Expression, gen_Java_InterfaceDeclaration_TypeDeclaration, gen_Java_Javadoc_Comment, gen_Java_LabeledStatement_NamedElement, gen_Java_LabeledStatement_Statement, gen_Java_LineComment_Comment, gen_Java_MethodDeclaration_AbstractMethodDeclaration, gen_Java_MethodInvocation_Expression, gen_Java_MethodInvocation_AbstractMethodInvocation, gen_Java_MethodRef_ASTNode, gen_Java_MethodRefParameter_ASTNode, gen_Java_Modifier_ASTNode, gen_Java_PackageAccess_NamespaceAccess, gen_Java_NamedElement_ASTNode, gen_Java_NamespaceAccess_ASTNode, gen_Java_NumberLiteral_Expression, gen_Java_NullLiteral_Expression, gen_Java_Package_NamedElement, gen_Java_PrefixExpression_Expression, gen_Java_ParameterizedType_Type, gen_Java_ParenthesizedExpression_Expression, gen_Java_PostfixExpression_Expression, gen_Java_SingleVariableDeclaration_VariableDeclaration, gen_Java_PrimitiveType_Type, gen_Java_PrimitiveTypeBoolean_PrimitiveType, gen_Java_PrimitiveTypeByte_PrimitiveType, gen_Java_PrimitiveTypeChar_PrimitiveType, gen_Java_PrimitiveTypeDouble_PrimitiveType, gen_Java_PrimitiveTypeShort_PrimitiveType, gen_Java_PrimitiveTypeFloat_PrimitiveType, gen_Java_PrimitiveTypeInt_PrimitiveType, gen_Java_PrimitiveTypeLong_PrimitiveType, gen_Java_PrimitiveTypeVoid_PrimitiveType, gen_Java_ReturnStatement_Statement, gen_Java_SingleVariableAccess_Expression, gen_Java_SuperFieldAccess_AbstractTypeQualifiedExpression, gen_Java_SuperMethodInvocation_AbstractTypeQualifiedExpression, gen_Java_SuperMethodInvocation_AbstractMethodInvocation, gen_Java_SwitchCase_Statement, gen_Java_Statement_ASTNode, gen_Java_StringLiteral_Expression, gen_Java_SuperConstructorInvocation_Statement, gen_Java_SuperConstructorInvocation_AbstractMethodInvocation, gen_Java_TextElement_ASTNode, gen_Java_SwitchStatement_Statement, gen_Java_SynchronizedStatement_Statement, gen_Java_TagElement_ASTNode, gen_Java_TypeDeclaration_AbstractTypeDeclaration, gen_Java_ThisExpression_AbstractTypeQualifiedExpression, gen_Java_ThrowStatement_Statement, gen_Java_TryStatement_Statement, gen_Java_Type_NamedElement, gen_Java_TypeAccess_Expression, gen_Java_TypeAccess_NamespaceAccess, gen_Java_UnresolvedAnnotationDeclaration_UnresolvedItem, gen_Java_TypeDeclarationStatement_Statement, gen_Java_TypeLiteral_Expression, gen_Java_TypeParameter_Type, gen_Java_UnresolvedItem_NamedElement, gen_Java_UnresolvedItemAccess_Expression, gen_Java_UnresolvedItemAccess_NamespaceAccess, gen_Java_UnresolvedAnnotationDeclaration_AnnotationTypeDeclaration, gen_Java_UnresolvedAnnotationTypeMemberDeclaration_AnnotationTypeMemberDeclaration, gen_Java_UnresolvedAnnotationTypeMemberDeclaration_UnresolvedItem, gen_Java_UnresolvedClassDeclaration_ClassDeclaration, gen_Java_UnresolvedClassDeclaration_UnresolvedItem, gen_Java_UnresolvedEnumDeclaration_EnumDeclaration, gen_Java_UnresolvedEnumDeclaration_UnresolvedItem, gen_Java_UnresolvedInterfaceDeclaration_InterfaceDeclaration, gen_Java_UnresolvedInterfaceDeclaration_UnresolvedItem, gen_Java_UnresolvedLabeledStatement_LabeledStatement, gen_Java_UnresolvedLabeledStatement_UnresolvedItem, gen_Java_UnresolvedMethodDeclaration_MethodDeclaration, gen_Java_UnresolvedMethodDeclaration_UnresolvedItem, gen_Java_UnresolvedSingleVariableDeclaration_SingleVariableDeclaration, gen_Java_UnresolvedSingleVariableDeclaration_UnresolvedItem, gen_Java_UnresolvedType_Type, gen_Java_UnresolvedType_UnresolvedItem, gen_Java_UnresolvedTypeDeclaration_AbstractTypeDeclaration, gen_Java_UnresolvedTypeDeclaration_UnresolvedItem, gen_Java_UnresolvedVariableDeclarationFragment_VariableDeclarationFragment, gen_Java_UnresolvedVariableDeclarationFragment_UnresolvedItem, gen_Java_VariableDeclaration_NamedElement, gen_Java_WhileStatement_Statement, gen_Java_VariableDeclarationExpression_Expression, gen_Java_VariableDeclarationExpression_AbstractVariablesContainer, gen_Java_VariableDeclarationFragment_VariableDeclaration, gen_Java_VariableDeclarationStatement_Statement, gen_Java_VariableDeclarationStatement_AbstractVariablesContainer, gen_Java_WildCardType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)