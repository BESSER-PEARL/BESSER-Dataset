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
			EnumerationLiteral(name="RIGHT_SHIFT_UNSIGNED"),
			EnumerationLiteral(name="LESS")
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

# Classes
javaMM_SingleVariableDeclaration = Class(name="javaMM::SingleVariableDeclaration")
javaMM_TypeAccess = Class(name="javaMM::TypeAccess")
javaMM_AbstractMethodDeclaration = Class(name="javaMM::AbstractMethodDeclaration", is_abstract=True)
BodyDeclaration = Class(name="BodyDeclaration")
javaMM_Block = Class(name="javaMM::Block")
javaMM_AbstractTypeDeclaration = Class(name="javaMM::AbstractTypeDeclaration", is_abstract=True)
Type = Class(name="Type")
javaMM_BodyDeclaration = Class(name="javaMM::BodyDeclaration", is_abstract=True)
javaMM_Comment = Class(name="javaMM::Comment", is_abstract=True)
javaMM_TypeParameter = Class(name="javaMM::TypeParameter")
javaMM_MethodRef = Class(name="javaMM::MethodRef")
javaMM_AbstractMethodInvocation = Class(name="javaMM::AbstractMethodInvocation", is_abstract=True)
ASTNode = Class(name="ASTNode")
javaMM_Expression = Class(name="javaMM::Expression", is_abstract=True)
javaMM_Annotation = Class(name="javaMM::Annotation")
javaMM_AnnotationMemberValuePair = Class(name="javaMM::AnnotationMemberValuePair")
javaMM_Package = Class(name="javaMM::Package")
javaMM_AbstractTypeQualifiedExpression = Class(name="javaMM::AbstractTypeQualifiedExpression", is_abstract=True)
Expression = Class(name="Expression")
javaMM_AbstractVariablesContainer = Class(name="javaMM::AbstractVariablesContainer", is_abstract=True)
javaMM_CompilationUnit = Class(name="javaMM::CompilationUnit")
javaMM_VariableDeclarationFragment = Class(name="javaMM::VariableDeclarationFragment")
javaMM_Archive = Class(name="javaMM::Archive")
NamedElement = Class(name="NamedElement")
javaMM_ClassFile = Class(name="javaMM::ClassFile")
javaMM_Manifest = Class(name="javaMM::Manifest")
javaMM_AssertStatement = Class(name="javaMM::AssertStatement")
Statement = Class(name="Statement")
javaMM_ASTNode = Class(name="javaMM::ASTNode", is_abstract=True)
javaMM_ClassInstanceCreation = Class(name="javaMM::ClassInstanceCreation")
javaMM_ArrayAccess = Class(name="javaMM::ArrayAccess")
javaMM_AnnotationTypeMemberDeclaration = Class(name="javaMM::AnnotationTypeMemberDeclaration")
javaMM_AnnotationTypeDeclaration = Class(name="javaMM::AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
javaMM_AnonymousClassDeclaration = Class(name="javaMM::AnonymousClassDeclaration")
javaMM_ArrayType = Class(name="javaMM::ArrayType")
javaMM_Assignment = Class(name="javaMM::Assignment")
javaMM_ArrayCreation = Class(name="javaMM::ArrayCreation")
javaMM_ArrayInitializer = Class(name="javaMM::ArrayInitializer")
javaMM_ArrayLengthAccess = Class(name="javaMM::ArrayLengthAccess")
javaMM_Modifier = Class(name="javaMM::Modifier")
javaMM_BooleanLiteral = Class(name="javaMM::BooleanLiteral")
javaMM_BlockComment = Class(name="javaMM::BlockComment")
Comment = Class(name="Comment")
javaMM_Statement = Class(name="javaMM::Statement", is_abstract=True)
javaMM_CatchClause = Class(name="javaMM::CatchClause")
javaMM_BreakStatement = Class(name="javaMM::BreakStatement")
javaMM_LabeledStatement = Class(name="javaMM::LabeledStatement")
javaMM_CastExpression = Class(name="javaMM::CastExpression")
AbstractMethodInvocation = Class(name="AbstractMethodInvocation")
javaMM_CharacterLiteral = Class(name="javaMM::CharacterLiteral")
javaMM_ConstructorDeclaration = Class(name="javaMM::ConstructorDeclaration")
AbstractMethodDeclaration = Class(name="AbstractMethodDeclaration")
javaMM_ConditionalExpression = Class(name="javaMM::ConditionalExpression")
javaMM_ConstructorInvocation = Class(name="javaMM::ConstructorInvocation")
javaMM_ClassDeclaration = Class(name="javaMM::ClassDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
javaMM_ImportDeclaration = Class(name="javaMM::ImportDeclaration")
javaMM_ContinueStatement = Class(name="javaMM::ContinueStatement")
javaMM_DoStatement = Class(name="javaMM::DoStatement")
javaMM_EmptyStatement = Class(name="javaMM::EmptyStatement")
javaMM_EnhancedForStatement = Class(name="javaMM::EnhancedForStatement")
javaMM_EnumConstantDeclaration = Class(name="javaMM::EnumConstantDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
javaMM_EnumDeclaration = Class(name="javaMM::EnumDeclaration")
javaMM_ExpressionStatement = Class(name="javaMM::ExpressionStatement")
javaMM_FieldAccess = Class(name="javaMM::FieldAccess")
javaMM_SingleVariableAccess = Class(name="javaMM::SingleVariableAccess")
javaMM_FieldDeclaration = Class(name="javaMM::FieldDeclaration")
AbstractVariablesContainer = Class(name="AbstractVariablesContainer")
javaMM_ForStatement = Class(name="javaMM::ForStatement")
javaMM_InfixExpression = Class(name="javaMM::InfixExpression")
javaMM_IfStatement = Class(name="javaMM::IfStatement")
javaMM_NamedElement = Class(name="javaMM::NamedElement", is_abstract=True)
javaMM_Initializer = Class(name="javaMM::Initializer")
javaMM_InstanceofExpression = Class(name="javaMM::InstanceofExpression")
javaMM_MemberRef = Class(name="javaMM::MemberRef")
javaMM_InterfaceDeclaration = Class(name="javaMM::InterfaceDeclaration")
javaMM_Javadoc = Class(name="javaMM::Javadoc")
javaMM_TagElement = Class(name="javaMM::TagElement")
javaMM_LineComment = Class(name="javaMM::LineComment")
javaMM_ManifestAttribute = Class(name="javaMM::ManifestAttribute")
javaMM_ManifestEntry = Class(name="javaMM::ManifestEntry")
javaMM_MethodInvocation = Class(name="javaMM::MethodInvocation")
javaMM_MethodDeclaration = Class(name="javaMM::MethodDeclaration")
javaMM_Model = Class(name="javaMM::Model")
javaMM_Type = Class(name="javaMM::Type", is_abstract=True)
javaMM_UnresolvedItem = Class(name="javaMM::UnresolvedItem")
javaMM_MethodRefParameter = Class(name="javaMM::MethodRefParameter")
javaMM_VariableDeclarationExpression = Class(name="javaMM::VariableDeclarationExpression")
javaMM_NamespaceAccess = Class(name="javaMM::NamespaceAccess", is_abstract=True)
javaMM_NumberLiteral = Class(name="javaMM::NumberLiteral")
javaMM_NullLiteral = Class(name="javaMM::NullLiteral")
javaMM_VariableDeclarationStatement = Class(name="javaMM::VariableDeclarationStatement")
javaMM_ParameterizedType = Class(name="javaMM::ParameterizedType")
javaMM_ParenthesizedExpression = Class(name="javaMM::ParenthesizedExpression")
javaMM_PostfixExpression = Class(name="javaMM::PostfixExpression")
javaMM_PrefixExpression = Class(name="javaMM::PrefixExpression")
javaMM_PackageAccess = Class(name="javaMM::PackageAccess")
NamespaceAccess = Class(name="NamespaceAccess")
javaMM_PrimitiveTypeByte = Class(name="javaMM::PrimitiveTypeByte")
javaMM_PrimitiveTypeChar = Class(name="javaMM::PrimitiveTypeChar")
javaMM_PrimitiveTypeDouble = Class(name="javaMM::PrimitiveTypeDouble")
javaMM_PrimitiveTypeShort = Class(name="javaMM::PrimitiveTypeShort")
javaMM_PrimitiveTypeFloat = Class(name="javaMM::PrimitiveTypeFloat")
javaMM_PrimitiveTypeInt = Class(name="javaMM::PrimitiveTypeInt")
javaMM_PrimitiveType = Class(name="javaMM::PrimitiveType")
javaMM_PrimitiveTypeBoolean = Class(name="javaMM::PrimitiveTypeBoolean")
PrimitiveType = Class(name="PrimitiveType")
javaMM_PrimitiveTypeLong = Class(name="javaMM::PrimitiveTypeLong")
javaMM_PrimitiveTypeVoid = Class(name="javaMM::PrimitiveTypeVoid")
javaMM_ReturnStatement = Class(name="javaMM::ReturnStatement")
javaMM_VariableDeclaration = Class(name="javaMM::VariableDeclaration", is_abstract=True)
javaMM_SuperMethodInvocation = Class(name="javaMM::SuperMethodInvocation")
javaMM_SwitchCase = Class(name="javaMM::SwitchCase")
javaMM_SwitchStatement = Class(name="javaMM::SwitchStatement")
javaMM_StringLiteral = Class(name="javaMM::StringLiteral")
javaMM_SuperConstructorInvocation = Class(name="javaMM::SuperConstructorInvocation")
javaMM_SuperFieldAccess = Class(name="javaMM::SuperFieldAccess")
AbstractTypeQualifiedExpression = Class(name="AbstractTypeQualifiedExpression")
javaMM_TextElement = Class(name="javaMM::TextElement")
javaMM_ThisExpression = Class(name="javaMM::ThisExpression")
javaMM_ThrowStatement = Class(name="javaMM::ThrowStatement")
javaMM_TryStatement = Class(name="javaMM::TryStatement")
javaMM_SynchronizedStatement = Class(name="javaMM::SynchronizedStatement")
javaMM_TypeDeclaration = Class(name="javaMM::TypeDeclaration", is_abstract=True)
javaMM_TypeDeclarationStatement = Class(name="javaMM::TypeDeclarationStatement")
javaMM_TypeLiteral = Class(name="javaMM::TypeLiteral")
javaMM_UnresolvedItemAccess = Class(name="javaMM::UnresolvedItemAccess")
javaMM_UnresolvedAnnotationDeclaration = Class(name="javaMM::UnresolvedAnnotationDeclaration")
AnnotationTypeDeclaration = Class(name="AnnotationTypeDeclaration")
javaMM_UnresolvedLabeledStatement = Class(name="javaMM::UnresolvedLabeledStatement")
LabeledStatement = Class(name="LabeledStatement")
javaMM_UnresolvedMethodDeclaration = Class(name="javaMM::UnresolvedMethodDeclaration")
MethodDeclaration = Class(name="MethodDeclaration")
javaMM_UnresolvedSingleVariableDeclaration = Class(name="javaMM::UnresolvedSingleVariableDeclaration")
SingleVariableDeclaration = Class(name="SingleVariableDeclaration")
javaMM_UnresolvedType = Class(name="javaMM::UnresolvedType")
javaMM_UnresolvedTypeDeclaration = Class(name="javaMM::UnresolvedTypeDeclaration")
UnresolvedItem = Class(name="UnresolvedItem")
javaMM_UnresolvedAnnotationTypeMemberDeclaration = Class(name="javaMM::UnresolvedAnnotationTypeMemberDeclaration")
AnnotationTypeMemberDeclaration = Class(name="AnnotationTypeMemberDeclaration")
javaMM_UnresolvedClassDeclaration = Class(name="javaMM::UnresolvedClassDeclaration")
ClassDeclaration = Class(name="ClassDeclaration")
javaMM_UnresolvedEnumDeclaration = Class(name="javaMM::UnresolvedEnumDeclaration")
EnumDeclaration = Class(name="EnumDeclaration")
javaMM_UnresolvedInterfaceDeclaration = Class(name="javaMM::UnresolvedInterfaceDeclaration")
InterfaceDeclaration = Class(name="InterfaceDeclaration")
javaMM_UnresolvedVariableDeclarationFragment = Class(name="javaMM::UnresolvedVariableDeclarationFragment")
VariableDeclarationFragment = Class(name="VariableDeclarationFragment")
javaMM_WildCardType = Class(name="javaMM::WildCardType")
javaMM_WhileStatement = Class(name="javaMM::WhileStatement")

# javaMM_SingleVariableDeclaration class attributes and methods
javaMM_SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=BooleanType)
javaMM_SingleVariableDeclaration.attributes={javaMM_SingleVariableDeclaration_varargs}

# javaMM_TypeAccess class attributes and methods

# javaMM_AbstractMethodDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# javaMM_Block class attributes and methods

# javaMM_AbstractTypeDeclaration class attributes and methods

# Type class attributes and methods

# javaMM_BodyDeclaration class attributes and methods

# javaMM_Comment class attributes and methods
javaMM_Comment_content: Property = Property(name="content", type=StringType)
javaMM_Comment_enclosedByParent: Property = Property(name="enclosedByParent", type=BooleanType)
javaMM_Comment_prefixOfParent: Property = Property(name="prefixOfParent", type=BooleanType)
javaMM_Comment.attributes={javaMM_Comment_enclosedByParent, javaMM_Comment_content, javaMM_Comment_prefixOfParent}

# javaMM_TypeParameter class attributes and methods

# javaMM_MethodRef class attributes and methods

# javaMM_AbstractMethodInvocation class attributes and methods

# ASTNode class attributes and methods

# javaMM_Expression class attributes and methods

# javaMM_Annotation class attributes and methods

# javaMM_AnnotationMemberValuePair class attributes and methods

# javaMM_Package class attributes and methods

# javaMM_AbstractTypeQualifiedExpression class attributes and methods

# Expression class attributes and methods

# javaMM_AbstractVariablesContainer class attributes and methods

# javaMM_CompilationUnit class attributes and methods
javaMM_CompilationUnit_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
javaMM_CompilationUnit.attributes={javaMM_CompilationUnit_originalFilePath}

# javaMM_VariableDeclarationFragment class attributes and methods

# javaMM_Archive class attributes and methods
javaMM_Archive_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
javaMM_Archive.attributes={javaMM_Archive_originalFilePath}

# NamedElement class attributes and methods

# javaMM_ClassFile class attributes and methods
javaMM_ClassFile_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
javaMM_ClassFile.attributes={javaMM_ClassFile_originalFilePath}

# javaMM_Manifest class attributes and methods

# javaMM_AssertStatement class attributes and methods

# Statement class attributes and methods

# javaMM_ASTNode class attributes and methods

# javaMM_ClassInstanceCreation class attributes and methods

# javaMM_ArrayAccess class attributes and methods

# javaMM_AnnotationTypeMemberDeclaration class attributes and methods

# javaMM_AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# javaMM_AnonymousClassDeclaration class attributes and methods

# javaMM_ArrayType class attributes and methods
javaMM_ArrayType_dimensions: Property = Property(name="dimensions", type=IntegerType)
javaMM_ArrayType.attributes={javaMM_ArrayType_dimensions}

# javaMM_Assignment class attributes and methods
javaMM_Assignment_operator: Property = Property(name="operator", type=StringType)
javaMM_Assignment.attributes={javaMM_Assignment_operator}

# javaMM_ArrayCreation class attributes and methods

# javaMM_ArrayInitializer class attributes and methods

# javaMM_ArrayLengthAccess class attributes and methods

# javaMM_Modifier class attributes and methods
javaMM_Modifier_visibility: Property = Property(name="visibility", type=StringType)
javaMM_Modifier_inheritance: Property = Property(name="inheritance", type=StringType)
javaMM_Modifier_static: Property = Property(name="static", type=BooleanType)
javaMM_Modifier_transient: Property = Property(name="transient", type=BooleanType)
javaMM_Modifier_volatile: Property = Property(name="volatile", type=BooleanType)
javaMM_Modifier_native: Property = Property(name="native", type=BooleanType)
javaMM_Modifier_strictfp: Property = Property(name="strictfp", type=BooleanType)
javaMM_Modifier_synchronized: Property = Property(name="synchronized", type=BooleanType)
javaMM_Modifier.attributes={javaMM_Modifier_transient, javaMM_Modifier_volatile, javaMM_Modifier_visibility, javaMM_Modifier_synchronized, javaMM_Modifier_strictfp, javaMM_Modifier_native, javaMM_Modifier_inheritance, javaMM_Modifier_static}

# javaMM_BooleanLiteral class attributes and methods
javaMM_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
javaMM_BooleanLiteral.attributes={javaMM_BooleanLiteral_value}

# javaMM_BlockComment class attributes and methods

# Comment class attributes and methods

# javaMM_Statement class attributes and methods

# javaMM_CatchClause class attributes and methods

# javaMM_BreakStatement class attributes and methods

# javaMM_LabeledStatement class attributes and methods

# javaMM_CastExpression class attributes and methods

# AbstractMethodInvocation class attributes and methods

# javaMM_CharacterLiteral class attributes and methods
javaMM_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
javaMM_CharacterLiteral.attributes={javaMM_CharacterLiteral_escapedValue}

# javaMM_ConstructorDeclaration class attributes and methods

# AbstractMethodDeclaration class attributes and methods

# javaMM_ConditionalExpression class attributes and methods

# javaMM_ConstructorInvocation class attributes and methods

# javaMM_ClassDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# javaMM_ImportDeclaration class attributes and methods
javaMM_ImportDeclaration_static: Property = Property(name="static", type=BooleanType)
javaMM_ImportDeclaration.attributes={javaMM_ImportDeclaration_static}

# javaMM_ContinueStatement class attributes and methods

# javaMM_DoStatement class attributes and methods

# javaMM_EmptyStatement class attributes and methods

# javaMM_EnhancedForStatement class attributes and methods

# javaMM_EnumConstantDeclaration class attributes and methods

# VariableDeclaration class attributes and methods

# javaMM_EnumDeclaration class attributes and methods

# javaMM_ExpressionStatement class attributes and methods

# javaMM_FieldAccess class attributes and methods

# javaMM_SingleVariableAccess class attributes and methods

# javaMM_FieldDeclaration class attributes and methods

# AbstractVariablesContainer class attributes and methods

# javaMM_ForStatement class attributes and methods

# javaMM_InfixExpression class attributes and methods
javaMM_InfixExpression_operator: Property = Property(name="operator", type=StringType)
javaMM_InfixExpression.attributes={javaMM_InfixExpression_operator}

# javaMM_IfStatement class attributes and methods

# javaMM_NamedElement class attributes and methods
javaMM_NamedElement_name: Property = Property(name="name", type=StringType)
javaMM_NamedElement_proxy: Property = Property(name="proxy", type=BooleanType)
javaMM_NamedElement.attributes={javaMM_NamedElement_name, javaMM_NamedElement_proxy}

# javaMM_Initializer class attributes and methods

# javaMM_InstanceofExpression class attributes and methods

# javaMM_MemberRef class attributes and methods

# javaMM_InterfaceDeclaration class attributes and methods

# javaMM_Javadoc class attributes and methods

# javaMM_TagElement class attributes and methods
javaMM_TagElement_tagName: Property = Property(name="tagName", type=StringType)
javaMM_TagElement.attributes={javaMM_TagElement_tagName}

# javaMM_LineComment class attributes and methods

# javaMM_ManifestAttribute class attributes and methods
javaMM_ManifestAttribute_key: Property = Property(name="key", type=StringType)
javaMM_ManifestAttribute_value: Property = Property(name="value", type=StringType)
javaMM_ManifestAttribute.attributes={javaMM_ManifestAttribute_value, javaMM_ManifestAttribute_key}

# javaMM_ManifestEntry class attributes and methods
javaMM_ManifestEntry_name: Property = Property(name="name", type=StringType)
javaMM_ManifestEntry.attributes={javaMM_ManifestEntry_name}

# javaMM_MethodInvocation class attributes and methods

# javaMM_MethodDeclaration class attributes and methods
javaMM_MethodDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
javaMM_MethodDeclaration.attributes={javaMM_MethodDeclaration_extraArrayDimensions}

# javaMM_Model class attributes and methods
javaMM_Model_name: Property = Property(name="name", type=StringType)
javaMM_Model.attributes={javaMM_Model_name}

# javaMM_Type class attributes and methods

# javaMM_UnresolvedItem class attributes and methods

# javaMM_MethodRefParameter class attributes and methods
javaMM_MethodRefParameter_name: Property = Property(name="name", type=StringType)
javaMM_MethodRefParameter_varargs: Property = Property(name="varargs", type=BooleanType)
javaMM_MethodRefParameter.attributes={javaMM_MethodRefParameter_name, javaMM_MethodRefParameter_varargs}

# javaMM_VariableDeclarationExpression class attributes and methods

# javaMM_NamespaceAccess class attributes and methods

# javaMM_NumberLiteral class attributes and methods
javaMM_NumberLiteral_tokenValue: Property = Property(name="tokenValue", type=StringType)
javaMM_NumberLiteral.attributes={javaMM_NumberLiteral_tokenValue}

# javaMM_NullLiteral class attributes and methods

# javaMM_VariableDeclarationStatement class attributes and methods
javaMM_VariableDeclarationStatement_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
javaMM_VariableDeclarationStatement.attributes={javaMM_VariableDeclarationStatement_extraArrayDimensions}

# javaMM_ParameterizedType class attributes and methods

# javaMM_ParenthesizedExpression class attributes and methods

# javaMM_PostfixExpression class attributes and methods
javaMM_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
javaMM_PostfixExpression.attributes={javaMM_PostfixExpression_operator}

# javaMM_PrefixExpression class attributes and methods
javaMM_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
javaMM_PrefixExpression.attributes={javaMM_PrefixExpression_operator}

# javaMM_PackageAccess class attributes and methods

# NamespaceAccess class attributes and methods

# javaMM_PrimitiveTypeByte class attributes and methods

# javaMM_PrimitiveTypeChar class attributes and methods

# javaMM_PrimitiveTypeDouble class attributes and methods

# javaMM_PrimitiveTypeShort class attributes and methods

# javaMM_PrimitiveTypeFloat class attributes and methods

# javaMM_PrimitiveTypeInt class attributes and methods

# javaMM_PrimitiveType class attributes and methods

# javaMM_PrimitiveTypeBoolean class attributes and methods

# PrimitiveType class attributes and methods

# javaMM_PrimitiveTypeLong class attributes and methods

# javaMM_PrimitiveTypeVoid class attributes and methods

# javaMM_ReturnStatement class attributes and methods

# javaMM_VariableDeclaration class attributes and methods
javaMM_VariableDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
javaMM_VariableDeclaration.attributes={javaMM_VariableDeclaration_extraArrayDimensions}

# javaMM_SuperMethodInvocation class attributes and methods

# javaMM_SwitchCase class attributes and methods
javaMM_SwitchCase_default: Property = Property(name="default", type=BooleanType)
javaMM_SwitchCase.attributes={javaMM_SwitchCase_default}

# javaMM_SwitchStatement class attributes and methods

# javaMM_StringLiteral class attributes and methods
javaMM_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
javaMM_StringLiteral.attributes={javaMM_StringLiteral_escapedValue}

# javaMM_SuperConstructorInvocation class attributes and methods

# javaMM_SuperFieldAccess class attributes and methods

# AbstractTypeQualifiedExpression class attributes and methods

# javaMM_TextElement class attributes and methods
javaMM_TextElement_text: Property = Property(name="text", type=StringType)
javaMM_TextElement.attributes={javaMM_TextElement_text}

# javaMM_ThisExpression class attributes and methods

# javaMM_ThrowStatement class attributes and methods

# javaMM_TryStatement class attributes and methods

# javaMM_SynchronizedStatement class attributes and methods

# javaMM_TypeDeclaration class attributes and methods

# javaMM_TypeDeclarationStatement class attributes and methods

# javaMM_TypeLiteral class attributes and methods

# javaMM_UnresolvedItemAccess class attributes and methods

# javaMM_UnresolvedAnnotationDeclaration class attributes and methods

# AnnotationTypeDeclaration class attributes and methods

# javaMM_UnresolvedLabeledStatement class attributes and methods

# LabeledStatement class attributes and methods

# javaMM_UnresolvedMethodDeclaration class attributes and methods

# MethodDeclaration class attributes and methods

# javaMM_UnresolvedSingleVariableDeclaration class attributes and methods

# SingleVariableDeclaration class attributes and methods

# javaMM_UnresolvedType class attributes and methods

# javaMM_UnresolvedTypeDeclaration class attributes and methods

# UnresolvedItem class attributes and methods

# javaMM_UnresolvedAnnotationTypeMemberDeclaration class attributes and methods

# AnnotationTypeMemberDeclaration class attributes and methods

# javaMM_UnresolvedClassDeclaration class attributes and methods

# ClassDeclaration class attributes and methods

# javaMM_UnresolvedEnumDeclaration class attributes and methods

# EnumDeclaration class attributes and methods

# javaMM_UnresolvedInterfaceDeclaration class attributes and methods

# InterfaceDeclaration class attributes and methods

# javaMM_UnresolvedVariableDeclarationFragment class attributes and methods

# VariableDeclarationFragment class attributes and methods

# javaMM_WildCardType class attributes and methods
javaMM_WildCardType_upperBound: Property = Property(name="upperBound", type=BooleanType)
javaMM_WildCardType.attributes={javaMM_WildCardType_upperBound}

# javaMM_WhileStatement class attributes and methods

# Relationships
body0: BinaryAssociation = BinaryAssociation(
    name="body0",
    ends={
        Property(name="javaMM_AbstractMethodDeclaration", type=javaMM_Block, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="javaMM_Block", type=javaMM_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="SingleVariableDeclaration", type=javaMM_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methodDeclaration", type=javaMM_SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thrownExceptions2: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions2",
    ends={
        Property(name="javaMM_TypeAccess", type=javaMM_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AbstractMethodDeclaration3", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations14: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations14",
    ends={
        Property(name="BodyDeclaration", type=javaMM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractTypeDeclaration", type=javaMM_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsBeforeBody15: BinaryAssociation = BinaryAssociation(
    name="commentsBeforeBody15",
    ends={
        Property(name="javaMM_Comment", type=javaMM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AbstractTypeDeclaration", type=javaMM_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters4: BinaryAssociation = BinaryAssociation(
    name="typeParameters4",
    ends={
        Property(name="javaMM_TypeParameter", type=javaMM_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AbstractMethodDeclaration5", type=javaMM_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usagesInDocComments6: BinaryAssociation = BinaryAssociation(
    name="usagesInDocComments6",
    ends={
        Property(name="MethodRef", type=javaMM_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=javaMM_MethodRef, multiplicity=Multiplicity(0, 9999))
    }
)
usages7: BinaryAssociation = BinaryAssociation(
    name="usages7",
    ends={
        Property(name="AbstractMethodInvocation", type=javaMM_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="method8", type=javaMM_AbstractMethodInvocation, multiplicity=Multiplicity(0, 9999))
    }
)
method9: BinaryAssociation = BinaryAssociation(
    name="method9",
    ends={
        Property(name="AbstractMethodDeclaration", type=javaMM_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="usages", type=javaMM_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
arguments10: BinaryAssociation = BinaryAssociation(
    name="arguments10",
    ends={
        Property(name="javaMM_Expression", type=javaMM_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AbstractMethodInvocation", type=javaMM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments11: BinaryAssociation = BinaryAssociation(
    name="typeArguments11",
    ends={
        Property(name="javaMM_TypeAccess13", type=javaMM_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AbstractMethodInvocation12", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="javaMM_TypeAccess29", type=javaMM_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Annotation", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
commentsAfterBody16: BinaryAssociation = BinaryAssociation(
    name="commentsAfterBody16",
    ends={
        Property(name="javaMM_Comment18", type=javaMM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AbstractTypeDeclaration17", type=javaMM_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package19: BinaryAssociation = BinaryAssociation(
    name="package19",
    ends={
        Property(name="Package", type=javaMM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements", type=javaMM_Package, multiplicity=Multiplicity(0, 1))
    }
)
superInterfaces20: BinaryAssociation = BinaryAssociation(
    name="superInterfaces20",
    ends={
        Property(name="javaMM_TypeAccess22", type=javaMM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AbstractTypeDeclaration21", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier23: BinaryAssociation = BinaryAssociation(
    name="qualifier23",
    ends={
        Property(name="javaMM_TypeAccess24", type=javaMM_AbstractTypeQualifiedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AbstractTypeQualifiedExpression", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="javaMM_TypeAccess26", type=javaMM_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AbstractVariablesContainer", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalCompilationUnit42: BinaryAssociation = BinaryAssociation(
    name="originalCompilationUnit42",
    ends={
        Property(name="javaMM_CompilationUnit", type=javaMM_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ASTNode43", type=javaMM_CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
fragments27: BinaryAssociation = BinaryAssociation(
    name="fragments27",
    ends={
        Property(name="VariableDeclarationFragment", type=javaMM_AbstractVariablesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="variablesContainer", type=javaMM_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalClassFile44: BinaryAssociation = BinaryAssociation(
    name="originalClassFile44",
    ends={
        Property(name="javaMM_ClassFile46", type=javaMM_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ASTNode45", type=javaMM_ClassFile, multiplicity=Multiplicity(0, 1))
    }
)
values30: BinaryAssociation = BinaryAssociation(
    name="values30",
    ends={
        Property(name="javaMM_AnnotationMemberValuePair", type=javaMM_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Annotation31", type=javaMM_AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classFiles32: BinaryAssociation = BinaryAssociation(
    name="classFiles32",
    ends={
        Property(name="javaMM_ClassFile", type=javaMM_Archive, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Archive", type=javaMM_ClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifest33: BinaryAssociation = BinaryAssociation(
    name="manifest33",
    ends={
        Property(name="javaMM_Manifest", type=javaMM_Archive, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Archive34", type=javaMM_Manifest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message35: BinaryAssociation = BinaryAssociation(
    name="message35",
    ends={
        Property(name="javaMM_Expression36", type=javaMM_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AssertStatement", type=javaMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression37: BinaryAssociation = BinaryAssociation(
    name="expression37",
    ends={
        Property(name="javaMM_Expression39", type=javaMM_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AssertStatement38", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comments40: BinaryAssociation = BinaryAssociation(
    name="comments40",
    ends={
        Property(name="javaMM_Comment41", type=javaMM_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ASTNode", type=javaMM_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classInstanceCreation60: BinaryAssociation = BinaryAssociation(
    name="classInstanceCreation60",
    ends={
        Property(name="ClassInstanceCreation", type=javaMM_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclaration", type=javaMM_ClassInstanceCreation, multiplicity=Multiplicity(0, 1))
    }
)
array61: BinaryAssociation = BinaryAssociation(
    name="array61",
    ends={
        Property(name="javaMM_Expression62", type=javaMM_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ArrayAccess", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member47: BinaryAssociation = BinaryAssociation(
    name="member47",
    ends={
        Property(name="AnnotationTypeMemberDeclaration", type=javaMM_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="usages48", type=javaMM_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
value49: BinaryAssociation = BinaryAssociation(
    name="value49",
    ends={
        Property(name="javaMM_Expression51", type=javaMM_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AnnotationMemberValuePair50", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
default52: BinaryAssociation = BinaryAssociation(
    name="default52",
    ends={
        Property(name="javaMM_Expression53", type=javaMM_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AnnotationTypeMemberDeclaration", type=javaMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="javaMM_TypeAccess56", type=javaMM_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_AnnotationTypeMemberDeclaration55", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usages57: BinaryAssociation = BinaryAssociation(
    name="usages57",
    ends={
        Property(name="AnnotationMemberValuePair", type=javaMM_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="member", type=javaMM_AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999))
    }
)
bodyDeclarations58: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations58",
    ends={
        Property(name="BodyDeclaration59", type=javaMM_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclarationOwner", type=javaMM_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType78: BinaryAssociation = BinaryAssociation(
    name="elementType78",
    ends={
        Property(name="javaMM_TypeAccess79", type=javaMM_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ArrayType", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index63: BinaryAssociation = BinaryAssociation(
    name="index63",
    ends={
        Property(name="javaMM_Expression65", type=javaMM_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ArrayAccess64", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions66: BinaryAssociation = BinaryAssociation(
    name="dimensions66",
    ends={
        Property(name="javaMM_Expression67", type=javaMM_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ArrayCreation", type=javaMM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer68: BinaryAssociation = BinaryAssociation(
    name="initializer68",
    ends={
        Property(name="javaMM_ArrayInitializer", type=javaMM_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ArrayCreation69", type=javaMM_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="javaMM_TypeAccess72", type=javaMM_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ArrayCreation71", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions73: BinaryAssociation = BinaryAssociation(
    name="expressions73",
    ends={
        Property(name="javaMM_Expression75", type=javaMM_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ArrayInitializer74", type=javaMM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
array76: BinaryAssociation = BinaryAssociation(
    name="array76",
    ends={
        Property(name="javaMM_Expression77", type=javaMM_ArrayLengthAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ArrayLengthAccess", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifier90: BinaryAssociation = BinaryAssociation(
    name="modifier90",
    ends={
        Property(name="Modifier", type=javaMM_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclaration", type=javaMM_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftHandSide80: BinaryAssociation = BinaryAssociation(
    name="leftHandSide80",
    ends={
        Property(name="javaMM_Expression81", type=javaMM_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Assignment", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide82: BinaryAssociation = BinaryAssociation(
    name="rightHandSide82",
    ends={
        Property(name="javaMM_Expression84", type=javaMM_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Assignment83", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements91: BinaryAssociation = BinaryAssociation(
    name="statements91",
    ends={
        Property(name="javaMM_Statement", type=javaMM_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Block92", type=javaMM_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstractTypeDeclaration85: BinaryAssociation = BinaryAssociation(
    name="abstractTypeDeclaration85",
    ends={
        Property(name="AbstractTypeDeclaration", type=javaMM_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations", type=javaMM_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
annotations86: BinaryAssociation = BinaryAssociation(
    name="annotations86",
    ends={
        Property(name="javaMM_Annotation87", type=javaMM_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_BodyDeclaration", type=javaMM_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclarationOwner88: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclarationOwner88",
    ends={
        Property(name="AnonymousClassDeclaration", type=javaMM_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations89", type=javaMM_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
type96: BinaryAssociation = BinaryAssociation(
    name="type96",
    ends={
        Property(name="javaMM_TypeAccess98", type=javaMM_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_CastExpression97", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attachedSource106: BinaryAssociation = BinaryAssociation(
    name="attachedSource106",
    ends={
        Property(name="javaMM_CompilationUnit108", type=javaMM_ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ClassFile107", type=javaMM_CompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
label93: BinaryAssociation = BinaryAssociation(
    name="label93",
    ends={
        Property(name="LabeledStatement", type=javaMM_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInBreakStatements", type=javaMM_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
package109: BinaryAssociation = BinaryAssociation(
    name="package109",
    ends={
        Property(name="javaMM_Package", type=javaMM_ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ClassFile110", type=javaMM_Package, multiplicity=Multiplicity(0, 1))
    }
)
expression94: BinaryAssociation = BinaryAssociation(
    name="expression94",
    ends={
        Property(name="javaMM_Expression95", type=javaMM_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_CastExpression", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception99: BinaryAssociation = BinaryAssociation(
    name="exception99",
    ends={
        Property(name="SingleVariableDeclaration100", type=javaMM_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="catchClause", type=javaMM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anonymousClassDeclaration111: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration111",
    ends={
        Property(name="AnonymousClassDeclaration112", type=javaMM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="classInstanceCreation", type=javaMM_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body101: BinaryAssociation = BinaryAssociation(
    name="body101",
    ends={
        Property(name="javaMM_Block102", type=javaMM_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_CatchClause", type=javaMM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="javaMM_AbstractTypeDeclaration105", type=javaMM_ClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ClassFile104", type=javaMM_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
elseExpression118: BinaryAssociation = BinaryAssociation(
    name="elseExpression118",
    ends={
        Property(name="javaMM_Expression119", type=javaMM_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ConditionalExpression", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression113: BinaryAssociation = BinaryAssociation(
    name="expression113",
    ends={
        Property(name="javaMM_Expression114", type=javaMM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ClassInstanceCreation", type=javaMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression120: BinaryAssociation = BinaryAssociation(
    name="expression120",
    ends={
        Property(name="javaMM_Expression122", type=javaMM_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ConditionalExpression121", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type115: BinaryAssociation = BinaryAssociation(
    name="type115",
    ends={
        Property(name="javaMM_TypeAccess117", type=javaMM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ClassInstanceCreation116", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression123: BinaryAssociation = BinaryAssociation(
    name="thenExpression123",
    ends={
        Property(name="javaMM_Expression125", type=javaMM_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ConditionalExpression124", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superClass126: BinaryAssociation = BinaryAssociation(
    name="superClass126",
    ends={
        Property(name="javaMM_TypeAccess127", type=javaMM_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ClassDeclaration", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label139: BinaryAssociation = BinaryAssociation(
    name="label139",
    ends={
        Property(name="LabeledStatement140", type=javaMM_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInContinueStatements", type=javaMM_LabeledStatement, multiplicity=Multiplicity(0, 1))
    }
)
commentList128: BinaryAssociation = BinaryAssociation(
    name="commentList128",
    ends={
        Property(name="javaMM_Comment130", type=javaMM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_CompilationUnit129", type=javaMM_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
imports131: BinaryAssociation = BinaryAssociation(
    name="imports131",
    ends={
        Property(name="javaMM_ImportDeclaration", type=javaMM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_CompilationUnit132", type=javaMM_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package133: BinaryAssociation = BinaryAssociation(
    name="package133",
    ends={
        Property(name="javaMM_Package135", type=javaMM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_CompilationUnit134", type=javaMM_Package, multiplicity=Multiplicity(0, 1))
    }
)
types136: BinaryAssociation = BinaryAssociation(
    name="types136",
    ends={
        Property(name="javaMM_AbstractTypeDeclaration138", type=javaMM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_CompilationUnit137", type=javaMM_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
expression141: BinaryAssociation = BinaryAssociation(
    name="expression141",
    ends={
        Property(name="javaMM_Expression142", type=javaMM_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_DoStatement", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body143: BinaryAssociation = BinaryAssociation(
    name="body143",
    ends={
        Property(name="javaMM_Statement145", type=javaMM_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_DoStatement144", type=javaMM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body146: BinaryAssociation = BinaryAssociation(
    name="body146",
    ends={
        Property(name="javaMM_Statement147", type=javaMM_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_EnhancedForStatement", type=javaMM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression148: BinaryAssociation = BinaryAssociation(
    name="expression148",
    ends={
        Property(name="javaMM_Expression150", type=javaMM_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_EnhancedForStatement149", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter151: BinaryAssociation = BinaryAssociation(
    name="parameter151",
    ends={
        Property(name="SingleVariableDeclaration152", type=javaMM_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="enhancedForStatement", type=javaMM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anonymousClassDeclaration153: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration153",
    ends={
        Property(name="javaMM_AnonymousClassDeclaration", type=javaMM_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_EnumConstantDeclaration", type=javaMM_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments154: BinaryAssociation = BinaryAssociation(
    name="arguments154",
    ends={
        Property(name="javaMM_Expression156", type=javaMM_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_EnumConstantDeclaration155", type=javaMM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumConstants157: BinaryAssociation = BinaryAssociation(
    name="enumConstants157",
    ends={
        Property(name="javaMM_EnumConstantDeclaration158", type=javaMM_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_EnumDeclaration", type=javaMM_EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression159: BinaryAssociation = BinaryAssociation(
    name="expression159",
    ends={
        Property(name="javaMM_Expression160", type=javaMM_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ExpressionStatement", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
field161: BinaryAssociation = BinaryAssociation(
    name="field161",
    ends={
        Property(name="javaMM_SingleVariableAccess", type=javaMM_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_FieldAccess", type=javaMM_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression162: BinaryAssociation = BinaryAssociation(
    name="expression162",
    ends={
        Property(name="javaMM_Expression164", type=javaMM_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_FieldAccess163", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression165: BinaryAssociation = BinaryAssociation(
    name="expression165",
    ends={
        Property(name="javaMM_Expression166", type=javaMM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ForStatement", type=javaMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updaters167: BinaryAssociation = BinaryAssociation(
    name="updaters167",
    ends={
        Property(name="javaMM_Expression169", type=javaMM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ForStatement168", type=javaMM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializers170: BinaryAssociation = BinaryAssociation(
    name="initializers170",
    ends={
        Property(name="javaMM_Expression172", type=javaMM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ForStatement171", type=javaMM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body173: BinaryAssociation = BinaryAssociation(
    name="body173",
    ends={
        Property(name="javaMM_Statement175", type=javaMM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ForStatement174", type=javaMM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression176: BinaryAssociation = BinaryAssociation(
    name="expression176",
    ends={
        Property(name="javaMM_Expression177", type=javaMM_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_IfStatement", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement178: BinaryAssociation = BinaryAssociation(
    name="thenStatement178",
    ends={
        Property(name="javaMM_Statement180", type=javaMM_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_IfStatement179", type=javaMM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement181: BinaryAssociation = BinaryAssociation(
    name="elseStatement181",
    ends={
        Property(name="javaMM_Statement183", type=javaMM_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_IfStatement182", type=javaMM_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedElement184: BinaryAssociation = BinaryAssociation(
    name="importedElement184",
    ends={
        Property(name="NamedElement", type=javaMM_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInImports", type=javaMM_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand195: BinaryAssociation = BinaryAssociation(
    name="rightOperand195",
    ends={
        Property(name="javaMM_InstanceofExpression", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="javaMM_TypeAccess196", type=javaMM_InstanceofExpression, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand185: BinaryAssociation = BinaryAssociation(
    name="rightOperand185",
    ends={
        Property(name="javaMM_Expression186", type=javaMM_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_InfixExpression", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand187: BinaryAssociation = BinaryAssociation(
    name="leftOperand187",
    ends={
        Property(name="javaMM_Expression189", type=javaMM_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_InfixExpression188", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands190: BinaryAssociation = BinaryAssociation(
    name="extendedOperands190",
    ends={
        Property(name="javaMM_Expression192", type=javaMM_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_InfixExpression191", type=javaMM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body193: BinaryAssociation = BinaryAssociation(
    name="body193",
    ends={
        Property(name="javaMM_Block194", type=javaMM_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Initializer", type=javaMM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
entryAttributes208: BinaryAssociation = BinaryAssociation(
    name="entryAttributes208",
    ends={
        Property(name="javaMM_ManifestEntry", type=javaMM_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Manifest209", type=javaMM_ManifestEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand197: BinaryAssociation = BinaryAssociation(
    name="leftOperand197",
    ends={
        Property(name="javaMM_Expression199", type=javaMM_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_InstanceofExpression198", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes210: BinaryAssociation = BinaryAssociation(
    name="attributes210",
    ends={
        Property(name="javaMM_ManifestAttribute212", type=javaMM_ManifestEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ManifestEntry211", type=javaMM_ManifestAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags200: BinaryAssociation = BinaryAssociation(
    name="tags200",
    ends={
        Property(name="javaMM_TagElement", type=javaMM_Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Javadoc", type=javaMM_TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member213: BinaryAssociation = BinaryAssociation(
    name="member213",
    ends={
        Property(name="javaMM_NamedElement", type=javaMM_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_MemberRef", type=javaMM_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
body201: BinaryAssociation = BinaryAssociation(
    name="body201",
    ends={
        Property(name="javaMM_Statement202", type=javaMM_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_LabeledStatement", type=javaMM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usagesInBreakStatements203: BinaryAssociation = BinaryAssociation(
    name="usagesInBreakStatements203",
    ends={
        Property(name="BreakStatement", type=javaMM_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=javaMM_BreakStatement, multiplicity=Multiplicity(0, 9999))
    }
)
usagesInContinueStatements204: BinaryAssociation = BinaryAssociation(
    name="usagesInContinueStatements204",
    ends={
        Property(name="ContinueStatement", type=javaMM_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="label205", type=javaMM_ContinueStatement, multiplicity=Multiplicity(0, 9999))
    }
)
mainAttributes206: BinaryAssociation = BinaryAssociation(
    name="mainAttributes206",
    ends={
        Property(name="javaMM_ManifestAttribute", type=javaMM_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Manifest207", type=javaMM_ManifestAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType217: BinaryAssociation = BinaryAssociation(
    name="returnType217",
    ends={
        Property(name="javaMM_MethodDeclaration", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="javaMM_TypeAccess218", type=javaMM_MethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
redefinedMethodDeclaration220: BinaryAssociation = BinaryAssociation(
    name="redefinedMethodDeclaration220",
    ends={
        Property(name="MethodDeclaration", type=javaMM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinitions", type=javaMM_MethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
redefinitions222: BinaryAssociation = BinaryAssociation(
    name="redefinitions222",
    ends={
        Property(name="MethodDeclaration223", type=javaMM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinedMethodDeclaration", type=javaMM_MethodDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
expression224: BinaryAssociation = BinaryAssociation(
    name="expression224",
    ends={
        Property(name="javaMM_Expression225", type=javaMM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_MethodInvocation", type=javaMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method226: BinaryAssociation = BinaryAssociation(
    name="method226",
    ends={
        Property(name="AbstractMethodDeclaration227", type=javaMM_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInDocComments", type=javaMM_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
qualifier214: BinaryAssociation = BinaryAssociation(
    name="qualifier214",
    ends={
        Property(name="javaMM_TypeAccess216", type=javaMM_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_MemberRef215", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type232: BinaryAssociation = BinaryAssociation(
    name="type232",
    ends={
        Property(name="javaMM_MethodRefParameter233", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="javaMM_TypeAccess234", type=javaMM_MethodRefParameter, multiplicity=Multiplicity(1, 1))
    }
)
ownedElements235: BinaryAssociation = BinaryAssociation(
    name="ownedElements235",
    ends={
        Property(name="Package236", type=javaMM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=javaMM_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orphanTypes237: BinaryAssociation = BinaryAssociation(
    name="orphanTypes237",
    ends={
        Property(name="javaMM_Type", type=javaMM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Model", type=javaMM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unresolvedItems238: BinaryAssociation = BinaryAssociation(
    name="unresolvedItems238",
    ends={
        Property(name="javaMM_UnresolvedItem", type=javaMM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Model239", type=javaMM_UnresolvedItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits240: BinaryAssociation = BinaryAssociation(
    name="compilationUnits240",
    ends={
        Property(name="javaMM_CompilationUnit242", type=javaMM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Model241", type=javaMM_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classFiles243: BinaryAssociation = BinaryAssociation(
    name="classFiles243",
    ends={
        Property(name="javaMM_ClassFile245", type=javaMM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Model244", type=javaMM_ClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
archives246: BinaryAssociation = BinaryAssociation(
    name="archives246",
    ends={
        Property(name="javaMM_Archive248", type=javaMM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_Model247", type=javaMM_Archive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier228: BinaryAssociation = BinaryAssociation(
    name="qualifier228",
    ends={
        Property(name="javaMM_TypeAccess229", type=javaMM_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_MethodRef", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters230: BinaryAssociation = BinaryAssociation(
    name="parameters230",
    ends={
        Property(name="javaMM_MethodRefParameter", type=javaMM_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_MethodRef231", type=javaMM_MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDeclarationExpression256: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationExpression256",
    ends={
        Property(name="VariableDeclarationExpression", type=javaMM_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier257", type=javaMM_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1))
    }
)
usagesInImports258: BinaryAssociation = BinaryAssociation(
    name="usagesInImports258",
    ends={
        Property(name="ImportDeclaration", type=javaMM_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="importedElement", type=javaMM_ImportDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElements259: BinaryAssociation = BinaryAssociation(
    name="ownedElements259",
    ends={
        Property(name="AbstractTypeDeclaration260", type=javaMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=javaMM_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model261: BinaryAssociation = BinaryAssociation(
    name="model261",
    ends={
        Property(name="Model", type=javaMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements262", type=javaMM_Model, multiplicity=Multiplicity(0, 1))
    }
)
bodyDeclaration249: BinaryAssociation = BinaryAssociation(
    name="bodyDeclaration249",
    ends={
        Property(name="BodyDeclaration250", type=javaMM_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier", type=javaMM_BodyDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
singleVariableDeclaration251: BinaryAssociation = BinaryAssociation(
    name="singleVariableDeclaration251",
    ends={
        Property(name="SingleVariableDeclaration253", type=javaMM_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier252", type=javaMM_SingleVariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclarationStatement254: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationStatement254",
    ends={
        Property(name="VariableDeclarationStatement", type=javaMM_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier255", type=javaMM_VariableDeclarationStatement, multiplicity=Multiplicity(0, 1))
    }
)
type276: BinaryAssociation = BinaryAssociation(
    name="type276",
    ends={
        Property(name="javaMM_TypeAccess277", type=javaMM_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ParameterizedType", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments278: BinaryAssociation = BinaryAssociation(
    name="typeArguments278",
    ends={
        Property(name="javaMM_TypeAccess280", type=javaMM_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ParameterizedType279", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression281: BinaryAssociation = BinaryAssociation(
    name="expression281",
    ends={
        Property(name="javaMM_Expression282", type=javaMM_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ParenthesizedExpression", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand283: BinaryAssociation = BinaryAssociation(
    name="operand283",
    ends={
        Property(name="javaMM_Expression284", type=javaMM_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_PostfixExpression", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedPackages264: BinaryAssociation = BinaryAssociation(
    name="ownedPackages264",
    ends={
        Property(name="Package266", type=javaMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package265", type=javaMM_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package268: BinaryAssociation = BinaryAssociation(
    name="package268",
    ends={
        Property(name="Package269", type=javaMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPackages", type=javaMM_Package, multiplicity=Multiplicity(0, 1))
    }
)
usagesInPackageAccess270: BinaryAssociation = BinaryAssociation(
    name="usagesInPackageAccess270",
    ends={
        Property(name="PackageAccess", type=javaMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package271", type=javaMM_PackageAccess, multiplicity=Multiplicity(0, 9999))
    }
)
package272: BinaryAssociation = BinaryAssociation(
    name="package272",
    ends={
        Property(name="Package273", type=javaMM_PackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInPackageAccess", type=javaMM_Package, multiplicity=Multiplicity(1, 1))
    }
)
qualifier275: BinaryAssociation = BinaryAssociation(
    name="qualifier275",
    ends={
        Property(name="javaMM_PackageAccess", type=javaMM_PackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_PackageAccess274", type=javaMM_PackageAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand285: BinaryAssociation = BinaryAssociation(
    name="operand285",
    ends={
        Property(name="javaMM_Expression286", type=javaMM_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_PrefixExpression", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifier293: BinaryAssociation = BinaryAssociation(
    name="modifier293",
    ends={
        Property(name="Modifier294", type=javaMM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="singleVariableDeclaration", type=javaMM_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type295: BinaryAssociation = BinaryAssociation(
    name="type295",
    ends={
        Property(name="javaMM_TypeAccess296", type=javaMM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_SingleVariableDeclaration", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations297: BinaryAssociation = BinaryAssociation(
    name="annotations297",
    ends={
        Property(name="javaMM_Annotation299", type=javaMM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_SingleVariableDeclaration298", type=javaMM_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodDeclaration300: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration300",
    ends={
        Property(name="AbstractMethodDeclaration301", type=javaMM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=javaMM_AbstractMethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
catchClause302: BinaryAssociation = BinaryAssociation(
    name="catchClause302",
    ends={
        Property(name="CatchClause", type=javaMM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="exception", type=javaMM_CatchClause, multiplicity=Multiplicity(0, 1))
    }
)
expression287: BinaryAssociation = BinaryAssociation(
    name="expression287",
    ends={
        Property(name="javaMM_Expression288", type=javaMM_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ReturnStatement", type=javaMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable289: BinaryAssociation = BinaryAssociation(
    name="variable289",
    ends={
        Property(name="VariableDeclaration", type=javaMM_SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usageInVariableAccess", type=javaMM_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
qualifier290: BinaryAssociation = BinaryAssociation(
    name="qualifier290",
    ends={
        Property(name="javaMM_Expression292", type=javaMM_SingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_SingleVariableAccess291", type=javaMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field306: BinaryAssociation = BinaryAssociation(
    name="field306",
    ends={
        Property(name="javaMM_SingleVariableAccess307", type=javaMM_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_SuperFieldAccess", type=javaMM_SingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression308: BinaryAssociation = BinaryAssociation(
    name="expression308",
    ends={
        Property(name="javaMM_Expression309", type=javaMM_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_SwitchCase", type=javaMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression310: BinaryAssociation = BinaryAssociation(
    name="expression310",
    ends={
        Property(name="javaMM_Expression311", type=javaMM_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_SwitchStatement", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enhancedForStatement303: BinaryAssociation = BinaryAssociation(
    name="enhancedForStatement303",
    ends={
        Property(name="EnhancedForStatement", type=javaMM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=javaMM_EnhancedForStatement, multiplicity=Multiplicity(0, 1))
    }
)
expression304: BinaryAssociation = BinaryAssociation(
    name="expression304",
    ends={
        Property(name="javaMM_Expression305", type=javaMM_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_SuperConstructorInvocation", type=javaMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression323: BinaryAssociation = BinaryAssociation(
    name="expression323",
    ends={
        Property(name="javaMM_Expression324", type=javaMM_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_ThrowStatement", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body325: BinaryAssociation = BinaryAssociation(
    name="body325",
    ends={
        Property(name="javaMM_Block326", type=javaMM_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_TryStatement", type=javaMM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally327: BinaryAssociation = BinaryAssociation(
    name="finally327",
    ends={
        Property(name="javaMM_Block329", type=javaMM_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_TryStatement328", type=javaMM_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements312: BinaryAssociation = BinaryAssociation(
    name="statements312",
    ends={
        Property(name="javaMM_Statement314", type=javaMM_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_SwitchStatement313", type=javaMM_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body315: BinaryAssociation = BinaryAssociation(
    name="body315",
    ends={
        Property(name="javaMM_Block316", type=javaMM_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_SynchronizedStatement", type=javaMM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression317: BinaryAssociation = BinaryAssociation(
    name="expression317",
    ends={
        Property(name="javaMM_Expression319", type=javaMM_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_SynchronizedStatement318", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments320: BinaryAssociation = BinaryAssociation(
    name="fragments320",
    ends={
        Property(name="javaMM_ASTNode322", type=javaMM_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_TagElement321", type=javaMM_ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier335: BinaryAssociation = BinaryAssociation(
    name="qualifier335",
    ends={
        Property(name="javaMM_NamespaceAccess", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_TypeAccess336", type=javaMM_NamespaceAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters337: BinaryAssociation = BinaryAssociation(
    name="typeParameters337",
    ends={
        Property(name="javaMM_TypeParameter338", type=javaMM_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_TypeDeclaration", type=javaMM_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration339: BinaryAssociation = BinaryAssociation(
    name="declaration339",
    ends={
        Property(name="javaMM_AbstractTypeDeclaration340", type=javaMM_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_TypeDeclarationStatement", type=javaMM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type341: BinaryAssociation = BinaryAssociation(
    name="type341",
    ends={
        Property(name="javaMM_TypeAccess342", type=javaMM_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_TypeLiteral", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catchClauses330: BinaryAssociation = BinaryAssociation(
    name="catchClauses330",
    ends={
        Property(name="javaMM_CatchClause332", type=javaMM_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_TryStatement331", type=javaMM_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usagesInTypeAccess333: BinaryAssociation = BinaryAssociation(
    name="usagesInTypeAccess333",
    ends={
        Property(name="TypeAccess", type=javaMM_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
type334: BinaryAssociation = BinaryAssociation(
    name="type334",
    ends={
        Property(name="Type", type=javaMM_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInTypeAccess", type=javaMM_Type, multiplicity=Multiplicity(1, 1))
    }
)
element346: BinaryAssociation = BinaryAssociation(
    name="element346",
    ends={
        Property(name="javaMM_UnresolvedItem347", type=javaMM_UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_UnresolvedItemAccess", type=javaMM_UnresolvedItem, multiplicity=Multiplicity(0, 1))
    }
)
qualifier348: BinaryAssociation = BinaryAssociation(
    name="qualifier348",
    ends={
        Property(name="javaMM_ASTNode350", type=javaMM_UnresolvedItemAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_UnresolvedItemAccess349", type=javaMM_ASTNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bounds343: BinaryAssociation = BinaryAssociation(
    name="bounds343",
    ends={
        Property(name="javaMM_TypeAccess345", type=javaMM_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_TypeParameter344", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageInVariableAccess353: BinaryAssociation = BinaryAssociation(
    name="usageInVariableAccess353",
    ends={
        Property(name="SingleVariableAccess", type=javaMM_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=javaMM_SingleVariableAccess, multiplicity=Multiplicity(0, 9999))
    }
)
modifier354: BinaryAssociation = BinaryAssociation(
    name="modifier354",
    ends={
        Property(name="Modifier355", type=javaMM_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationExpression", type=javaMM_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations356: BinaryAssociation = BinaryAssociation(
    name="annotations356",
    ends={
        Property(name="javaMM_Annotation357", type=javaMM_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_VariableDeclarationExpression", type=javaMM_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer351: BinaryAssociation = BinaryAssociation(
    name="initializer351",
    ends={
        Property(name="javaMM_Expression352", type=javaMM_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_VariableDeclaration", type=javaMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations361: BinaryAssociation = BinaryAssociation(
    name="annotations361",
    ends={
        Property(name="javaMM_Annotation362", type=javaMM_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_VariableDeclarationStatement", type=javaMM_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bound363: BinaryAssociation = BinaryAssociation(
    name="bound363",
    ends={
        Property(name="javaMM_TypeAccess364", type=javaMM_WildCardType, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_WildCardType", type=javaMM_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variablesContainer358: BinaryAssociation = BinaryAssociation(
    name="variablesContainer358",
    ends={
        Property(name="AbstractVariablesContainer", type=javaMM_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=javaMM_AbstractVariablesContainer, multiplicity=Multiplicity(0, 1))
    }
)
modifier359: BinaryAssociation = BinaryAssociation(
    name="modifier359",
    ends={
        Property(name="Modifier360", type=javaMM_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationStatement", type=javaMM_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression365: BinaryAssociation = BinaryAssociation(
    name="expression365",
    ends={
        Property(name="javaMM_Expression366", type=javaMM_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_WhileStatement", type=javaMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body367: BinaryAssociation = BinaryAssociation(
    name="body367",
    ends={
        Property(name="javaMM_Statement369", type=javaMM_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaMM_WhileStatement368", type=javaMM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_javaMM_AbstractMethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=javaMM_AbstractMethodDeclaration)
gen_javaMM_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=javaMM_AbstractTypeDeclaration)
gen_javaMM_AbstractTypeDeclaration_Type = Generalization(general=Type, specific=javaMM_AbstractTypeDeclaration)
gen_javaMM_AbstractMethodInvocation_ASTNode = Generalization(general=ASTNode, specific=javaMM_AbstractMethodInvocation)
gen_javaMM_Annotation_Expression = Generalization(general=Expression, specific=javaMM_Annotation)
gen_javaMM_AbstractTypeQualifiedExpression_Expression = Generalization(general=Expression, specific=javaMM_AbstractTypeQualifiedExpression)
gen_javaMM_AbstractVariablesContainer_ASTNode = Generalization(general=ASTNode, specific=javaMM_AbstractVariablesContainer)
gen_javaMM_AnnotationMemberValuePair_NamedElement = Generalization(general=NamedElement, specific=javaMM_AnnotationMemberValuePair)
gen_javaMM_Archive_NamedElement = Generalization(general=NamedElement, specific=javaMM_Archive)
gen_javaMM_AssertStatement_Statement = Generalization(general=Statement, specific=javaMM_AssertStatement)
gen_javaMM_ArrayAccess_Expression = Generalization(general=Expression, specific=javaMM_ArrayAccess)
gen_javaMM_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=javaMM_AnnotationTypeDeclaration)
gen_javaMM_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=javaMM_AnnotationTypeMemberDeclaration)
gen_javaMM_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=javaMM_AnonymousClassDeclaration)
gen_javaMM_ArrayType_Type = Generalization(general=Type, specific=javaMM_ArrayType)
gen_javaMM_ArrayCreation_Expression = Generalization(general=Expression, specific=javaMM_ArrayCreation)
gen_javaMM_ArrayInitializer_Expression = Generalization(general=Expression, specific=javaMM_ArrayInitializer)
gen_javaMM_ArrayLengthAccess_Expression = Generalization(general=Expression, specific=javaMM_ArrayLengthAccess)
gen_javaMM_BooleanLiteral_Expression = Generalization(general=Expression, specific=javaMM_BooleanLiteral)
gen_javaMM_Assignment_Expression = Generalization(general=Expression, specific=javaMM_Assignment)
gen_javaMM_BlockComment_Comment = Generalization(general=Comment, specific=javaMM_BlockComment)
gen_javaMM_Block_Statement = Generalization(general=Statement, specific=javaMM_Block)
gen_javaMM_BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=javaMM_BodyDeclaration)
gen_javaMM_BreakStatement_Statement = Generalization(general=Statement, specific=javaMM_BreakStatement)
gen_javaMM_CastExpression_Expression = Generalization(general=Expression, specific=javaMM_CastExpression)
gen_javaMM_CatchClause_Statement = Generalization(general=Statement, specific=javaMM_CatchClause)
gen_javaMM_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=javaMM_ClassInstanceCreation)
gen_javaMM_ClassInstanceCreation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=javaMM_ClassInstanceCreation)
gen_javaMM_CharacterLiteral_Expression = Generalization(general=Expression, specific=javaMM_CharacterLiteral)
gen_javaMM_ClassFile_NamedElement = Generalization(general=NamedElement, specific=javaMM_ClassFile)
gen_javaMM_ConstructorDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=javaMM_ConstructorDeclaration)
gen_javaMM_ConditionalExpression_Expression = Generalization(general=Expression, specific=javaMM_ConditionalExpression)
gen_javaMM_ConstructorInvocation_Statement = Generalization(general=Statement, specific=javaMM_ConstructorInvocation)
gen_javaMM_ConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=javaMM_ConstructorInvocation)
gen_javaMM_ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=javaMM_ClassDeclaration)
gen_javaMM_Comment_ASTNode = Generalization(general=ASTNode, specific=javaMM_Comment)
gen_javaMM_CompilationUnit_NamedElement = Generalization(general=NamedElement, specific=javaMM_CompilationUnit)
gen_javaMM_ContinueStatement_Statement = Generalization(general=Statement, specific=javaMM_ContinueStatement)
gen_javaMM_DoStatement_Statement = Generalization(general=Statement, specific=javaMM_DoStatement)
gen_javaMM_EmptyStatement_Statement = Generalization(general=Statement, specific=javaMM_EmptyStatement)
gen_javaMM_EnhancedForStatement_Statement = Generalization(general=Statement, specific=javaMM_EnhancedForStatement)
gen_javaMM_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=javaMM_EnumConstantDeclaration)
gen_javaMM_EnumConstantDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=javaMM_EnumConstantDeclaration)
gen_javaMM_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=javaMM_EnumDeclaration)
gen_javaMM_Expression_ASTNode = Generalization(general=ASTNode, specific=javaMM_Expression)
gen_javaMM_ExpressionStatement_Statement = Generalization(general=Statement, specific=javaMM_ExpressionStatement)
gen_javaMM_FieldAccess_Expression = Generalization(general=Expression, specific=javaMM_FieldAccess)
gen_javaMM_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=javaMM_FieldDeclaration)
gen_javaMM_FieldDeclaration_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=javaMM_FieldDeclaration)
gen_javaMM_ForStatement_Statement = Generalization(general=Statement, specific=javaMM_ForStatement)
gen_javaMM_InfixExpression_Expression = Generalization(general=Expression, specific=javaMM_InfixExpression)
gen_javaMM_IfStatement_Statement = Generalization(general=Statement, specific=javaMM_IfStatement)
gen_javaMM_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=javaMM_ImportDeclaration)
gen_javaMM_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=javaMM_Initializer)
gen_javaMM_InstanceofExpression_Expression = Generalization(general=Expression, specific=javaMM_InstanceofExpression)
gen_javaMM_MemberRef_ASTNode = Generalization(general=ASTNode, specific=javaMM_MemberRef)
gen_javaMM_InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=javaMM_InterfaceDeclaration)
gen_javaMM_Javadoc_Comment = Generalization(general=Comment, specific=javaMM_Javadoc)
gen_javaMM_LabeledStatement_NamedElement = Generalization(general=NamedElement, specific=javaMM_LabeledStatement)
gen_javaMM_LabeledStatement_Statement = Generalization(general=Statement, specific=javaMM_LabeledStatement)
gen_javaMM_LineComment_Comment = Generalization(general=Comment, specific=javaMM_LineComment)
gen_javaMM_MethodInvocation_Expression = Generalization(general=Expression, specific=javaMM_MethodInvocation)
gen_javaMM_MethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=javaMM_MethodInvocation)
gen_javaMM_MethodRef_ASTNode = Generalization(general=ASTNode, specific=javaMM_MethodRef)
gen_javaMM_MethodDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=javaMM_MethodDeclaration)
gen_javaMM_Modifier_ASTNode = Generalization(general=ASTNode, specific=javaMM_Modifier)
gen_javaMM_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=javaMM_MethodRefParameter)
gen_javaMM_NamedElement_ASTNode = Generalization(general=ASTNode, specific=javaMM_NamedElement)
gen_javaMM_NamespaceAccess_ASTNode = Generalization(general=ASTNode, specific=javaMM_NamespaceAccess)
gen_javaMM_NumberLiteral_Expression = Generalization(general=Expression, specific=javaMM_NumberLiteral)
gen_javaMM_NullLiteral_Expression = Generalization(general=Expression, specific=javaMM_NullLiteral)
gen_javaMM_Package_NamedElement = Generalization(general=NamedElement, specific=javaMM_Package)
gen_javaMM_ParameterizedType_Type = Generalization(general=Type, specific=javaMM_ParameterizedType)
gen_javaMM_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=javaMM_ParenthesizedExpression)
gen_javaMM_PostfixExpression_Expression = Generalization(general=Expression, specific=javaMM_PostfixExpression)
gen_javaMM_PrefixExpression_Expression = Generalization(general=Expression, specific=javaMM_PrefixExpression)
gen_javaMM_PackageAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=javaMM_PackageAccess)
gen_javaMM_PrimitiveTypeBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=javaMM_PrimitiveTypeBoolean)
gen_javaMM_PrimitiveTypeByte_PrimitiveType = Generalization(general=PrimitiveType, specific=javaMM_PrimitiveTypeByte)
gen_javaMM_PrimitiveTypeChar_PrimitiveType = Generalization(general=PrimitiveType, specific=javaMM_PrimitiveTypeChar)
gen_javaMM_PrimitiveTypeDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=javaMM_PrimitiveTypeDouble)
gen_javaMM_PrimitiveTypeShort_PrimitiveType = Generalization(general=PrimitiveType, specific=javaMM_PrimitiveTypeShort)
gen_javaMM_PrimitiveTypeFloat_PrimitiveType = Generalization(general=PrimitiveType, specific=javaMM_PrimitiveTypeFloat)
gen_javaMM_PrimitiveTypeInt_PrimitiveType = Generalization(general=PrimitiveType, specific=javaMM_PrimitiveTypeInt)
gen_javaMM_PrimitiveType_Type = Generalization(general=Type, specific=javaMM_PrimitiveType)
gen_javaMM_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=javaMM_SingleVariableDeclaration)
gen_javaMM_PrimitiveTypeLong_PrimitiveType = Generalization(general=PrimitiveType, specific=javaMM_PrimitiveTypeLong)
gen_javaMM_PrimitiveTypeVoid_PrimitiveType = Generalization(general=PrimitiveType, specific=javaMM_PrimitiveTypeVoid)
gen_javaMM_ReturnStatement_Statement = Generalization(general=Statement, specific=javaMM_ReturnStatement)
gen_javaMM_SingleVariableAccess_Expression = Generalization(general=Expression, specific=javaMM_SingleVariableAccess)
gen_javaMM_SuperFieldAccess_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=javaMM_SuperFieldAccess)
gen_javaMM_SuperMethodInvocation_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=javaMM_SuperMethodInvocation)
gen_javaMM_SuperMethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=javaMM_SuperMethodInvocation)
gen_javaMM_SwitchCase_Statement = Generalization(general=Statement, specific=javaMM_SwitchCase)
gen_javaMM_SwitchStatement_Statement = Generalization(general=Statement, specific=javaMM_SwitchStatement)
gen_javaMM_Statement_ASTNode = Generalization(general=ASTNode, specific=javaMM_Statement)
gen_javaMM_StringLiteral_Expression = Generalization(general=Expression, specific=javaMM_StringLiteral)
gen_javaMM_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=javaMM_SuperConstructorInvocation)
gen_javaMM_SuperConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=javaMM_SuperConstructorInvocation)
gen_javaMM_TextElement_ASTNode = Generalization(general=ASTNode, specific=javaMM_TextElement)
gen_javaMM_ThisExpression_AbstractTypeQualifiedExpression = Generalization(general=AbstractTypeQualifiedExpression, specific=javaMM_ThisExpression)
gen_javaMM_ThrowStatement_Statement = Generalization(general=Statement, specific=javaMM_ThrowStatement)
gen_javaMM_TryStatement_Statement = Generalization(general=Statement, specific=javaMM_TryStatement)
gen_javaMM_SynchronizedStatement_Statement = Generalization(general=Statement, specific=javaMM_SynchronizedStatement)
gen_javaMM_TagElement_ASTNode = Generalization(general=ASTNode, specific=javaMM_TagElement)
gen_javaMM_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=javaMM_TypeDeclaration)
gen_javaMM_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=javaMM_TypeDeclarationStatement)
gen_javaMM_TypeLiteral_Expression = Generalization(general=Expression, specific=javaMM_TypeLiteral)
gen_javaMM_Type_NamedElement = Generalization(general=NamedElement, specific=javaMM_Type)
gen_javaMM_TypeAccess_Expression = Generalization(general=Expression, specific=javaMM_TypeAccess)
gen_javaMM_TypeAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=javaMM_TypeAccess)
gen_javaMM_UnresolvedItem_NamedElement = Generalization(general=NamedElement, specific=javaMM_UnresolvedItem)
gen_javaMM_UnresolvedItemAccess_Expression = Generalization(general=Expression, specific=javaMM_UnresolvedItemAccess)
gen_javaMM_UnresolvedItemAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=javaMM_UnresolvedItemAccess)
gen_javaMM_UnresolvedAnnotationDeclaration_AnnotationTypeDeclaration = Generalization(general=AnnotationTypeDeclaration, specific=javaMM_UnresolvedAnnotationDeclaration)
gen_javaMM_TypeParameter_Type = Generalization(general=Type, specific=javaMM_TypeParameter)
gen_javaMM_UnresolvedLabeledStatement_LabeledStatement = Generalization(general=LabeledStatement, specific=javaMM_UnresolvedLabeledStatement)
gen_javaMM_UnresolvedLabeledStatement_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedLabeledStatement)
gen_javaMM_UnresolvedMethodDeclaration_MethodDeclaration = Generalization(general=MethodDeclaration, specific=javaMM_UnresolvedMethodDeclaration)
gen_javaMM_UnresolvedMethodDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedMethodDeclaration)
gen_javaMM_UnresolvedSingleVariableDeclaration_SingleVariableDeclaration = Generalization(general=SingleVariableDeclaration, specific=javaMM_UnresolvedSingleVariableDeclaration)
gen_javaMM_UnresolvedSingleVariableDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedSingleVariableDeclaration)
gen_javaMM_UnresolvedType_Type = Generalization(general=Type, specific=javaMM_UnresolvedType)
gen_javaMM_UnresolvedType_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedType)
gen_javaMM_UnresolvedTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=javaMM_UnresolvedTypeDeclaration)
gen_javaMM_UnresolvedTypeDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedTypeDeclaration)
gen_javaMM_UnresolvedAnnotationDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedAnnotationDeclaration)
gen_javaMM_UnresolvedAnnotationTypeMemberDeclaration_AnnotationTypeMemberDeclaration = Generalization(general=AnnotationTypeMemberDeclaration, specific=javaMM_UnresolvedAnnotationTypeMemberDeclaration)
gen_javaMM_UnresolvedAnnotationTypeMemberDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedAnnotationTypeMemberDeclaration)
gen_javaMM_UnresolvedClassDeclaration_ClassDeclaration = Generalization(general=ClassDeclaration, specific=javaMM_UnresolvedClassDeclaration)
gen_javaMM_UnresolvedClassDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedClassDeclaration)
gen_javaMM_UnresolvedEnumDeclaration_EnumDeclaration = Generalization(general=EnumDeclaration, specific=javaMM_UnresolvedEnumDeclaration)
gen_javaMM_UnresolvedEnumDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedEnumDeclaration)
gen_javaMM_UnresolvedInterfaceDeclaration_InterfaceDeclaration = Generalization(general=InterfaceDeclaration, specific=javaMM_UnresolvedInterfaceDeclaration)
gen_javaMM_UnresolvedInterfaceDeclaration_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedInterfaceDeclaration)
gen_javaMM_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=javaMM_VariableDeclarationExpression)
gen_javaMM_VariableDeclarationExpression_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=javaMM_VariableDeclarationExpression)
gen_javaMM_UnresolvedVariableDeclarationFragment_VariableDeclarationFragment = Generalization(general=VariableDeclarationFragment, specific=javaMM_UnresolvedVariableDeclarationFragment)
gen_javaMM_UnresolvedVariableDeclarationFragment_UnresolvedItem = Generalization(general=UnresolvedItem, specific=javaMM_UnresolvedVariableDeclarationFragment)
gen_javaMM_VariableDeclaration_NamedElement = Generalization(general=NamedElement, specific=javaMM_VariableDeclaration)
gen_javaMM_WildCardType_Type = Generalization(general=Type, specific=javaMM_WildCardType)
gen_javaMM_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=javaMM_VariableDeclarationFragment)
gen_javaMM_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=javaMM_VariableDeclarationStatement)
gen_javaMM_VariableDeclarationStatement_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=javaMM_VariableDeclarationStatement)
gen_javaMM_WhileStatement_Statement = Generalization(general=Statement, specific=javaMM_WhileStatement)

# Domain Model
domain_model = DomainModel(
    name="javaMM",
    types={javaMM_SingleVariableDeclaration, javaMM_TypeAccess, javaMM_AbstractMethodDeclaration, BodyDeclaration, javaMM_Block, javaMM_AbstractTypeDeclaration, Type, javaMM_BodyDeclaration, javaMM_Comment, javaMM_TypeParameter, javaMM_MethodRef, javaMM_AbstractMethodInvocation, ASTNode, javaMM_Expression, javaMM_Annotation, javaMM_AnnotationMemberValuePair, javaMM_Package, javaMM_AbstractTypeQualifiedExpression, Expression, javaMM_AbstractVariablesContainer, javaMM_CompilationUnit, javaMM_VariableDeclarationFragment, javaMM_Archive, NamedElement, javaMM_ClassFile, javaMM_Manifest, javaMM_AssertStatement, Statement, javaMM_ASTNode, javaMM_ClassInstanceCreation, javaMM_ArrayAccess, javaMM_AnnotationTypeMemberDeclaration, javaMM_AnnotationTypeDeclaration, AbstractTypeDeclaration, javaMM_AnonymousClassDeclaration, javaMM_ArrayType, javaMM_Assignment, javaMM_ArrayCreation, javaMM_ArrayInitializer, javaMM_ArrayLengthAccess, javaMM_Modifier, javaMM_BooleanLiteral, javaMM_BlockComment, Comment, javaMM_Statement, javaMM_CatchClause, javaMM_BreakStatement, javaMM_LabeledStatement, javaMM_CastExpression, AbstractMethodInvocation, javaMM_CharacterLiteral, javaMM_ConstructorDeclaration, AbstractMethodDeclaration, javaMM_ConditionalExpression, javaMM_ConstructorInvocation, javaMM_ClassDeclaration, TypeDeclaration, javaMM_ImportDeclaration, javaMM_ContinueStatement, javaMM_DoStatement, javaMM_EmptyStatement, javaMM_EnhancedForStatement, javaMM_EnumConstantDeclaration, VariableDeclaration, javaMM_EnumDeclaration, javaMM_ExpressionStatement, javaMM_FieldAccess, javaMM_SingleVariableAccess, javaMM_FieldDeclaration, AbstractVariablesContainer, javaMM_ForStatement, javaMM_InfixExpression, javaMM_IfStatement, javaMM_NamedElement, javaMM_Initializer, javaMM_InstanceofExpression, javaMM_MemberRef, javaMM_InterfaceDeclaration, javaMM_Javadoc, javaMM_TagElement, javaMM_LineComment, javaMM_ManifestAttribute, javaMM_ManifestEntry, javaMM_MethodInvocation, javaMM_MethodDeclaration, javaMM_Model, javaMM_Type, javaMM_UnresolvedItem, javaMM_MethodRefParameter, javaMM_VariableDeclarationExpression, javaMM_NamespaceAccess, javaMM_NumberLiteral, javaMM_NullLiteral, javaMM_VariableDeclarationStatement, javaMM_ParameterizedType, javaMM_ParenthesizedExpression, javaMM_PostfixExpression, javaMM_PrefixExpression, javaMM_PackageAccess, NamespaceAccess, javaMM_PrimitiveTypeByte, javaMM_PrimitiveTypeChar, javaMM_PrimitiveTypeDouble, javaMM_PrimitiveTypeShort, javaMM_PrimitiveTypeFloat, javaMM_PrimitiveTypeInt, javaMM_PrimitiveType, javaMM_PrimitiveTypeBoolean, PrimitiveType, javaMM_PrimitiveTypeLong, javaMM_PrimitiveTypeVoid, javaMM_ReturnStatement, javaMM_VariableDeclaration, javaMM_SuperMethodInvocation, javaMM_SwitchCase, javaMM_SwitchStatement, javaMM_StringLiteral, javaMM_SuperConstructorInvocation, javaMM_SuperFieldAccess, AbstractTypeQualifiedExpression, javaMM_TextElement, javaMM_ThisExpression, javaMM_ThrowStatement, javaMM_TryStatement, javaMM_SynchronizedStatement, javaMM_TypeDeclaration, javaMM_TypeDeclarationStatement, javaMM_TypeLiteral, javaMM_UnresolvedItemAccess, javaMM_UnresolvedAnnotationDeclaration, AnnotationTypeDeclaration, javaMM_UnresolvedLabeledStatement, LabeledStatement, javaMM_UnresolvedMethodDeclaration, MethodDeclaration, javaMM_UnresolvedSingleVariableDeclaration, SingleVariableDeclaration, javaMM_UnresolvedType, javaMM_UnresolvedTypeDeclaration, UnresolvedItem, javaMM_UnresolvedAnnotationTypeMemberDeclaration, AnnotationTypeMemberDeclaration, javaMM_UnresolvedClassDeclaration, ClassDeclaration, javaMM_UnresolvedEnumDeclaration, EnumDeclaration, javaMM_UnresolvedInterfaceDeclaration, InterfaceDeclaration, javaMM_UnresolvedVariableDeclarationFragment, VariableDeclarationFragment, javaMM_WildCardType, javaMM_WhileStatement, AssignmentKind, InheritanceKind, InfixExpressionKind, VisibilityKind, PostfixExpressionKind, PrefixExpressionKind},
    associations={body0, parameters1, thrownExceptions2, bodyDeclarations14, commentsBeforeBody15, typeParameters4, usagesInDocComments6, usages7, method9, arguments10, typeArguments11, type28, commentsAfterBody16, package19, superInterfaces20, qualifier23, type25, originalCompilationUnit42, fragments27, originalClassFile44, values30, classFiles32, manifest33, message35, expression37, comments40, classInstanceCreation60, array61, member47, value49, default52, type54, usages57, bodyDeclarations58, elementType78, index63, dimensions66, initializer68, type70, expressions73, array76, modifier90, leftHandSide80, rightHandSide82, statements91, abstractTypeDeclaration85, annotations86, anonymousClassDeclarationOwner88, type96, attachedSource106, label93, package109, expression94, exception99, anonymousClassDeclaration111, body101, type103, elseExpression118, expression113, expression120, type115, thenExpression123, superClass126, label139, commentList128, imports131, package133, types136, expression141, body143, body146, expression148, parameter151, anonymousClassDeclaration153, arguments154, enumConstants157, expression159, field161, expression162, expression165, updaters167, initializers170, body173, expression176, thenStatement178, elseStatement181, importedElement184, rightOperand195, rightOperand185, leftOperand187, extendedOperands190, body193, entryAttributes208, leftOperand197, attributes210, tags200, member213, body201, usagesInBreakStatements203, usagesInContinueStatements204, mainAttributes206, returnType217, redefinedMethodDeclaration220, redefinitions222, expression224, method226, qualifier214, type232, ownedElements235, orphanTypes237, unresolvedItems238, compilationUnits240, classFiles243, archives246, qualifier228, parameters230, variableDeclarationExpression256, usagesInImports258, ownedElements259, model261, bodyDeclaration249, singleVariableDeclaration251, variableDeclarationStatement254, type276, typeArguments278, expression281, operand283, ownedPackages264, package268, usagesInPackageAccess270, package272, qualifier275, operand285, modifier293, type295, annotations297, methodDeclaration300, catchClause302, expression287, variable289, qualifier290, field306, expression308, expression310, enhancedForStatement303, expression304, expression323, body325, finally327, statements312, body315, expression317, fragments320, qualifier335, typeParameters337, declaration339, type341, catchClauses330, usagesInTypeAccess333, type334, element346, qualifier348, bounds343, usageInVariableAccess353, modifier354, annotations356, initializer351, annotations361, bound363, variablesContainer358, modifier359, expression365, body367},
    generalizations={gen_javaMM_AbstractMethodDeclaration_BodyDeclaration, gen_javaMM_AbstractTypeDeclaration_BodyDeclaration, gen_javaMM_AbstractTypeDeclaration_Type, gen_javaMM_AbstractMethodInvocation_ASTNode, gen_javaMM_Annotation_Expression, gen_javaMM_AbstractTypeQualifiedExpression_Expression, gen_javaMM_AbstractVariablesContainer_ASTNode, gen_javaMM_AnnotationMemberValuePair_NamedElement, gen_javaMM_Archive_NamedElement, gen_javaMM_AssertStatement_Statement, gen_javaMM_ArrayAccess_Expression, gen_javaMM_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_javaMM_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_javaMM_AnonymousClassDeclaration_ASTNode, gen_javaMM_ArrayType_Type, gen_javaMM_ArrayCreation_Expression, gen_javaMM_ArrayInitializer_Expression, gen_javaMM_ArrayLengthAccess_Expression, gen_javaMM_BooleanLiteral_Expression, gen_javaMM_Assignment_Expression, gen_javaMM_BlockComment_Comment, gen_javaMM_Block_Statement, gen_javaMM_BodyDeclaration_NamedElement, gen_javaMM_BreakStatement_Statement, gen_javaMM_CastExpression_Expression, gen_javaMM_CatchClause_Statement, gen_javaMM_ClassInstanceCreation_Expression, gen_javaMM_ClassInstanceCreation_AbstractMethodInvocation, gen_javaMM_CharacterLiteral_Expression, gen_javaMM_ClassFile_NamedElement, gen_javaMM_ConstructorDeclaration_AbstractMethodDeclaration, gen_javaMM_ConditionalExpression_Expression, gen_javaMM_ConstructorInvocation_Statement, gen_javaMM_ConstructorInvocation_AbstractMethodInvocation, gen_javaMM_ClassDeclaration_TypeDeclaration, gen_javaMM_Comment_ASTNode, gen_javaMM_CompilationUnit_NamedElement, gen_javaMM_ContinueStatement_Statement, gen_javaMM_DoStatement_Statement, gen_javaMM_EmptyStatement_Statement, gen_javaMM_EnhancedForStatement_Statement, gen_javaMM_EnumConstantDeclaration_BodyDeclaration, gen_javaMM_EnumConstantDeclaration_VariableDeclaration, gen_javaMM_EnumDeclaration_AbstractTypeDeclaration, gen_javaMM_Expression_ASTNode, gen_javaMM_ExpressionStatement_Statement, gen_javaMM_FieldAccess_Expression, gen_javaMM_FieldDeclaration_BodyDeclaration, gen_javaMM_FieldDeclaration_AbstractVariablesContainer, gen_javaMM_ForStatement_Statement, gen_javaMM_InfixExpression_Expression, gen_javaMM_IfStatement_Statement, gen_javaMM_ImportDeclaration_ASTNode, gen_javaMM_Initializer_BodyDeclaration, gen_javaMM_InstanceofExpression_Expression, gen_javaMM_MemberRef_ASTNode, gen_javaMM_InterfaceDeclaration_TypeDeclaration, gen_javaMM_Javadoc_Comment, gen_javaMM_LabeledStatement_NamedElement, gen_javaMM_LabeledStatement_Statement, gen_javaMM_LineComment_Comment, gen_javaMM_MethodInvocation_Expression, gen_javaMM_MethodInvocation_AbstractMethodInvocation, gen_javaMM_MethodRef_ASTNode, gen_javaMM_MethodDeclaration_AbstractMethodDeclaration, gen_javaMM_Modifier_ASTNode, gen_javaMM_MethodRefParameter_ASTNode, gen_javaMM_NamedElement_ASTNode, gen_javaMM_NamespaceAccess_ASTNode, gen_javaMM_NumberLiteral_Expression, gen_javaMM_NullLiteral_Expression, gen_javaMM_Package_NamedElement, gen_javaMM_ParameterizedType_Type, gen_javaMM_ParenthesizedExpression_Expression, gen_javaMM_PostfixExpression_Expression, gen_javaMM_PrefixExpression_Expression, gen_javaMM_PackageAccess_NamespaceAccess, gen_javaMM_PrimitiveTypeBoolean_PrimitiveType, gen_javaMM_PrimitiveTypeByte_PrimitiveType, gen_javaMM_PrimitiveTypeChar_PrimitiveType, gen_javaMM_PrimitiveTypeDouble_PrimitiveType, gen_javaMM_PrimitiveTypeShort_PrimitiveType, gen_javaMM_PrimitiveTypeFloat_PrimitiveType, gen_javaMM_PrimitiveTypeInt_PrimitiveType, gen_javaMM_PrimitiveType_Type, gen_javaMM_SingleVariableDeclaration_VariableDeclaration, gen_javaMM_PrimitiveTypeLong_PrimitiveType, gen_javaMM_PrimitiveTypeVoid_PrimitiveType, gen_javaMM_ReturnStatement_Statement, gen_javaMM_SingleVariableAccess_Expression, gen_javaMM_SuperFieldAccess_AbstractTypeQualifiedExpression, gen_javaMM_SuperMethodInvocation_AbstractTypeQualifiedExpression, gen_javaMM_SuperMethodInvocation_AbstractMethodInvocation, gen_javaMM_SwitchCase_Statement, gen_javaMM_SwitchStatement_Statement, gen_javaMM_Statement_ASTNode, gen_javaMM_StringLiteral_Expression, gen_javaMM_SuperConstructorInvocation_Statement, gen_javaMM_SuperConstructorInvocation_AbstractMethodInvocation, gen_javaMM_TextElement_ASTNode, gen_javaMM_ThisExpression_AbstractTypeQualifiedExpression, gen_javaMM_ThrowStatement_Statement, gen_javaMM_TryStatement_Statement, gen_javaMM_SynchronizedStatement_Statement, gen_javaMM_TagElement_ASTNode, gen_javaMM_TypeDeclaration_AbstractTypeDeclaration, gen_javaMM_TypeDeclarationStatement_Statement, gen_javaMM_TypeLiteral_Expression, gen_javaMM_Type_NamedElement, gen_javaMM_TypeAccess_Expression, gen_javaMM_TypeAccess_NamespaceAccess, gen_javaMM_UnresolvedItem_NamedElement, gen_javaMM_UnresolvedItemAccess_Expression, gen_javaMM_UnresolvedItemAccess_NamespaceAccess, gen_javaMM_UnresolvedAnnotationDeclaration_AnnotationTypeDeclaration, gen_javaMM_TypeParameter_Type, gen_javaMM_UnresolvedLabeledStatement_LabeledStatement, gen_javaMM_UnresolvedLabeledStatement_UnresolvedItem, gen_javaMM_UnresolvedMethodDeclaration_MethodDeclaration, gen_javaMM_UnresolvedMethodDeclaration_UnresolvedItem, gen_javaMM_UnresolvedSingleVariableDeclaration_SingleVariableDeclaration, gen_javaMM_UnresolvedSingleVariableDeclaration_UnresolvedItem, gen_javaMM_UnresolvedType_Type, gen_javaMM_UnresolvedType_UnresolvedItem, gen_javaMM_UnresolvedTypeDeclaration_AbstractTypeDeclaration, gen_javaMM_UnresolvedTypeDeclaration_UnresolvedItem, gen_javaMM_UnresolvedAnnotationDeclaration_UnresolvedItem, gen_javaMM_UnresolvedAnnotationTypeMemberDeclaration_AnnotationTypeMemberDeclaration, gen_javaMM_UnresolvedAnnotationTypeMemberDeclaration_UnresolvedItem, gen_javaMM_UnresolvedClassDeclaration_ClassDeclaration, gen_javaMM_UnresolvedClassDeclaration_UnresolvedItem, gen_javaMM_UnresolvedEnumDeclaration_EnumDeclaration, gen_javaMM_UnresolvedEnumDeclaration_UnresolvedItem, gen_javaMM_UnresolvedInterfaceDeclaration_InterfaceDeclaration, gen_javaMM_UnresolvedInterfaceDeclaration_UnresolvedItem, gen_javaMM_VariableDeclarationExpression_Expression, gen_javaMM_VariableDeclarationExpression_AbstractVariablesContainer, gen_javaMM_UnresolvedVariableDeclarationFragment_VariableDeclarationFragment, gen_javaMM_UnresolvedVariableDeclarationFragment_UnresolvedItem, gen_javaMM_VariableDeclaration_NamedElement, gen_javaMM_WildCardType_Type, gen_javaMM_VariableDeclarationFragment_VariableDeclaration, gen_javaMM_VariableDeclarationStatement_Statement, gen_javaMM_VariableDeclarationStatement_AbstractVariablesContainer, gen_javaMM_WhileStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)