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
AssignementOperatorKind: Enumeration = Enumeration(
    name="AssignementOperatorKind",
    literals={
            EnumerationLiteral(name="RIGHT_SHIFT_SIGNED_ASSIGN"),
			EnumerationLiteral(name="BIT_XOR_ASSIGN"),
			EnumerationLiteral(name="TIMES_ASSIGN"),
			EnumerationLiteral(name="LEFT_SHIFT_ASSIGN"),
			EnumerationLiteral(name="MINUS_ASSIGN"),
			EnumerationLiteral(name="BIT_OR_ASSIGN"),
			EnumerationLiteral(name="PLUS_ASSIGN"),
			EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="RIGHT_SHIFT_UNSIGNED_ASSIGN"),
			EnumerationLiteral(name="REMAINDER_ASSIGN"),
			EnumerationLiteral(name="DIVIDE_ASSIGN"),
			EnumerationLiteral(name="BIT_AND_ASSIGN")
    }
)

InfixExpressionOperatorKind: Enumeration = Enumeration(
    name="InfixExpressionOperatorKind",
    literals={
            EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="RIGHT_SHIFT_SIGNED"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="LESS_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="CONDITIONAL_OR"),
			EnumerationLiteral(name="REMAINDER"),
			EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="LEFT_SHIFT"),
			EnumerationLiteral(name="RIGHT_SHIFT_UNSIGNED"),
			EnumerationLiteral(name="CONDITIONAL_AND"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="DIVIDE")
    }
)

PostfixExpresssionOperatorKind: Enumeration = Enumeration(
    name="PostfixExpresssionOperatorKind",
    literals={
            EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT")
    }
)

PrefixExpresssionOperatorKind: Enumeration = Enumeration(
    name="PrefixExpresssionOperatorKind",
    literals={
            EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="DECREMENT"),
			EnumerationLiteral(name="COMPLEMENT"),
			EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="PLUS")
    }
)

# Classes
Javadoc = Class(name="Javadoc")
JavaAbstractSyntax_CatchClause = Class(name="JavaAbstractSyntax::CatchClause")
Block = Class(name="Block")
JavaAbstractSyntax_AST = Class(name="JavaAbstractSyntax::AST")
ASTNode = Class(name="ASTNode")
JavaAbstractSyntax_ASTNode = Class(name="JavaAbstractSyntax::ASTNode", is_abstract=True)
JavaAbstractSyntax_AnonymousClassDeclaration = Class(name="JavaAbstractSyntax::AnonymousClassDeclaration")
BodyDeclaration = Class(name="BodyDeclaration")
JavaAbstractSyntax_BodyDeclaration = Class(name="JavaAbstractSyntax::BodyDeclaration", is_abstract=True)
ExtendedModifier = Class(name="ExtendedModifier")
JavaAbstractSyntax_Expression = Class(name="JavaAbstractSyntax::Expression", is_abstract=True)
JavaAbstractSyntax_ImportDeclaration = Class(name="JavaAbstractSyntax::ImportDeclaration")
SingleVariableDeclaration = Class(name="SingleVariableDeclaration")
JavaAbstractSyntax_Comment = Class(name="JavaAbstractSyntax::Comment", is_abstract=True)
JavaAbstractSyntax_CompilationUnit = Class(name="JavaAbstractSyntax::CompilationUnit")
Comment = Class(name="Comment")
PackageDeclaration = Class(name="PackageDeclaration")
ImportDeclaration = Class(name="ImportDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
JavaAbstractSyntax_MemberRef = Class(name="JavaAbstractSyntax::MemberRef")
SimpleName = Class(name="SimpleName")
Name = Class(name="Name")
JavaAbstractSyntax_MemberValuePair = Class(name="JavaAbstractSyntax::MemberValuePair")
Expression = Class(name="Expression")
JavaAbstractSyntax_MethodRef = Class(name="JavaAbstractSyntax::MethodRef")
MethodRefParameter = Class(name="MethodRefParameter")
JavaAbstractSyntax_MethodRefParameter = Class(name="JavaAbstractSyntax::MethodRefParameter")
Type = Class(name="Type")
JavaAbstractSyntax_ExtendedModifier = Class(name="JavaAbstractSyntax::ExtendedModifier", is_abstract=True)
JavaAbstractSyntax_Modifier = Class(name="JavaAbstractSyntax::Modifier")
JavaAbstractSyntax_TypeParameter = Class(name="JavaAbstractSyntax::TypeParameter")
JavaAbstractSyntax_PackageDeclaration = Class(name="JavaAbstractSyntax::PackageDeclaration")
Annotation = Class(name="Annotation")
JavaAbstractSyntax_Statement = Class(name="JavaAbstractSyntax::Statement", is_abstract=True)
JavaAbstractSyntax_TagElement = Class(name="JavaAbstractSyntax::TagElement")
JavaAbstractSyntax_TextElement = Class(name="JavaAbstractSyntax::TextElement")
JavaAbstractSyntax_Type = Class(name="JavaAbstractSyntax::Type", is_abstract=True)
JavaAbstractSyntax_VariableDeclaration = Class(name="JavaAbstractSyntax::VariableDeclaration", is_abstract=True)
JavaAbstractSyntax_AbstractTypeDeclaration = Class(name="JavaAbstractSyntax::AbstractTypeDeclaration", is_abstract=True)
JavaAbstractSyntax_AnnotationTypeMemberDeclaration = Class(name="JavaAbstractSyntax::AnnotationTypeMemberDeclaration")
JavaAbstractSyntax_EnumConstantDeclaration = Class(name="JavaAbstractSyntax::EnumConstantDeclaration")
AnonymousClassDeclaration = Class(name="AnonymousClassDeclaration")
JavaAbstractSyntax_FieldDeclaration = Class(name="JavaAbstractSyntax::FieldDeclaration")
VariableDeclarationFragment = Class(name="VariableDeclarationFragment")
JavaAbstractSyntax_Initializer = Class(name="JavaAbstractSyntax::Initializer")
JavaAbstractSyntax_MethodDeclaration = Class(name="JavaAbstractSyntax::MethodDeclaration")
JavaAbstractSyntax_LineComment = Class(name="JavaAbstractSyntax::LineComment")
JavaAbstractSyntax_Annotation = Class(name="JavaAbstractSyntax::Annotation", is_abstract=True)
JavaAbstractSyntax_ArrayAccess = Class(name="JavaAbstractSyntax::ArrayAccess")
TypeParameter = Class(name="TypeParameter")
JavaAbstractSyntax_AnnotationTypeDeclaration = Class(name="JavaAbstractSyntax::AnnotationTypeDeclaration")
JavaAbstractSyntax_EnumDeclaration = Class(name="JavaAbstractSyntax::EnumDeclaration")
EnumConstantDeclaration = Class(name="EnumConstantDeclaration")
JavaAbstractSyntax_TypeDeclaration = Class(name="JavaAbstractSyntax::TypeDeclaration")
JavaAbstractSyntax_BlockComment = Class(name="JavaAbstractSyntax::BlockComment")
JavaAbstractSyntax_Javadoc = Class(name="JavaAbstractSyntax::Javadoc")
TagElement = Class(name="TagElement")
JavaAbstractSyntax_ArrayCreation = Class(name="JavaAbstractSyntax::ArrayCreation")
ArrayInitializer = Class(name="ArrayInitializer")
ArrayType = Class(name="ArrayType")
JavaAbstractSyntax_ArrayInitializer = Class(name="JavaAbstractSyntax::ArrayInitializer")
JavaAbstractSyntax_Assignment = Class(name="JavaAbstractSyntax::Assignment")
JavaAbstractSyntax_BooleanLiteral = Class(name="JavaAbstractSyntax::BooleanLiteral")
JavaAbstractSyntax_CastExpression = Class(name="JavaAbstractSyntax::CastExpression")
JavaAbstractSyntax_CharacterLiteral = Class(name="JavaAbstractSyntax::CharacterLiteral")
JavaAbstractSyntax_ClassInstanceCreation = Class(name="JavaAbstractSyntax::ClassInstanceCreation")
JavaAbstractSyntax_ConditionalExpression = Class(name="JavaAbstractSyntax::ConditionalExpression")
JavaAbstractSyntax_FieldAccess = Class(name="JavaAbstractSyntax::FieldAccess")
JavaAbstractSyntax_InfixExpression = Class(name="JavaAbstractSyntax::InfixExpression")
JavaAbstractSyntax_MethodInvocation = Class(name="JavaAbstractSyntax::MethodInvocation")
JavaAbstractSyntax_InstanceofExpression = Class(name="JavaAbstractSyntax::InstanceofExpression")
JavaAbstractSyntax_PostfixExpression = Class(name="JavaAbstractSyntax::PostfixExpression")
JavaAbstractSyntax_Name = Class(name="JavaAbstractSyntax::Name", is_abstract=True)
JavaAbstractSyntax_NullLiteral = Class(name="JavaAbstractSyntax::NullLiteral")
JavaAbstractSyntax_NumberLiteral = Class(name="JavaAbstractSyntax::NumberLiteral")
JavaAbstractSyntax_ParenthesizedExpression = Class(name="JavaAbstractSyntax::ParenthesizedExpression")
JavaAbstractSyntax_SuperMethodInvocation = Class(name="JavaAbstractSyntax::SuperMethodInvocation")
JavaAbstractSyntax_PrefixExpression = Class(name="JavaAbstractSyntax::PrefixExpression")
JavaAbstractSyntax_StringLiteral = Class(name="JavaAbstractSyntax::StringLiteral")
JavaAbstractSyntax_SuperFieldAccess = Class(name="JavaAbstractSyntax::SuperFieldAccess")
JavaAbstractSyntax_AssertStatement = Class(name="JavaAbstractSyntax::AssertStatement")
Statement = Class(name="Statement")
JavaAbstractSyntax_ThisExpression = Class(name="JavaAbstractSyntax::ThisExpression")
JavaAbstractSyntax_TypeLiteral = Class(name="JavaAbstractSyntax::TypeLiteral")
JavaAbstractSyntax_VariableDeclarationExpression = Class(name="JavaAbstractSyntax::VariableDeclarationExpression")
JavaAbstractSyntax_Block = Class(name="JavaAbstractSyntax::Block")
JavaAbstractSyntax_BreakStatement = Class(name="JavaAbstractSyntax::BreakStatement")
JavaAbstractSyntax_ConstructorInvocation = Class(name="JavaAbstractSyntax::ConstructorInvocation")
JavaAbstractSyntax_ContinueStatement = Class(name="JavaAbstractSyntax::ContinueStatement")
JavaAbstractSyntax_DoStatement = Class(name="JavaAbstractSyntax::DoStatement")
JavaAbstractSyntax_EmptyStatement = Class(name="JavaAbstractSyntax::EmptyStatement")
JavaAbstractSyntax_EnhancedForStatement = Class(name="JavaAbstractSyntax::EnhancedForStatement")
JavaAbstractSyntax_ExpressionStatement = Class(name="JavaAbstractSyntax::ExpressionStatement")
JavaAbstractSyntax_ForStatement = Class(name="JavaAbstractSyntax::ForStatement")
JavaAbstractSyntax_IfStatement = Class(name="JavaAbstractSyntax::IfStatement")
JavaAbstractSyntax_LabeledStatement = Class(name="JavaAbstractSyntax::LabeledStatement")
JavaAbstractSyntax_ReturnStatement = Class(name="JavaAbstractSyntax::ReturnStatement")
JavaAbstractSyntax_SuperConstructorInvocation = Class(name="JavaAbstractSyntax::SuperConstructorInvocation")
JavaAbstractSyntax_TryStatement = Class(name="JavaAbstractSyntax::TryStatement")
CatchClause = Class(name="CatchClause")
JavaAbstractSyntax_SwitchCase = Class(name="JavaAbstractSyntax::SwitchCase")
JavaAbstractSyntax_SwitchStatement = Class(name="JavaAbstractSyntax::SwitchStatement")
JavaAbstractSyntax_SynchronizedStatement = Class(name="JavaAbstractSyntax::SynchronizedStatement")
JavaAbstractSyntax_ThrowStatement = Class(name="JavaAbstractSyntax::ThrowStatement")
JavaAbstractSyntax_ParameterizedType = Class(name="JavaAbstractSyntax::ParameterizedType")
JavaAbstractSyntax_TypeDeclarationStatement = Class(name="JavaAbstractSyntax::TypeDeclarationStatement")
JavaAbstractSyntax_VariableDeclarationStatement = Class(name="JavaAbstractSyntax::VariableDeclarationStatement")
JavaAbstractSyntax_WhileStatement = Class(name="JavaAbstractSyntax::WhileStatement")
JavaAbstractSyntax_ArrayType = Class(name="JavaAbstractSyntax::ArrayType")
JavaAbstractSyntax_VariableDeclarationFragment = Class(name="JavaAbstractSyntax::VariableDeclarationFragment")
JavaAbstractSyntax_QualifiedName = Class(name="JavaAbstractSyntax::QualifiedName")
JavaAbstractSyntax_PrimitiveType = Class(name="JavaAbstractSyntax::PrimitiveType")
JavaAbstractSyntax_QualifiedType = Class(name="JavaAbstractSyntax::QualifiedType")
JavaAbstractSyntax_SimpleType = Class(name="JavaAbstractSyntax::SimpleType")
JavaAbstractSyntax_WildcardType = Class(name="JavaAbstractSyntax::WildcardType")
JavaAbstractSyntax_SingleVariableDeclaration = Class(name="JavaAbstractSyntax::SingleVariableDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
JavaAbstractSyntax_SimpleName = Class(name="JavaAbstractSyntax::SimpleName")
JavaAbstractSyntax_MarkerAnnotation = Class(name="JavaAbstractSyntax::MarkerAnnotation")
JavaAbstractSyntax_NormalAnnotation = Class(name="JavaAbstractSyntax::NormalAnnotation")
MemberValuePair = Class(name="MemberValuePair")
JavaAbstractSyntax_SingleMemberAnnotation = Class(name="JavaAbstractSyntax::SingleMemberAnnotation")

# Javadoc class attributes and methods

# JavaAbstractSyntax_CatchClause class attributes and methods

# Block class attributes and methods

# JavaAbstractSyntax_AST class attributes and methods

# ASTNode class attributes and methods

# JavaAbstractSyntax_ASTNode class attributes and methods

# JavaAbstractSyntax_AnonymousClassDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# JavaAbstractSyntax_BodyDeclaration class attributes and methods

# ExtendedModifier class attributes and methods

# JavaAbstractSyntax_Expression class attributes and methods
JavaAbstractSyntax_Expression_resolveBoxing: Property = Property(name="resolveBoxing", type=StringType)
JavaAbstractSyntax_Expression_resolveUnboxing: Property = Property(name="resolveUnboxing", type=StringType)
JavaAbstractSyntax_Expression.attributes={JavaAbstractSyntax_Expression_resolveBoxing, JavaAbstractSyntax_Expression_resolveUnboxing}

# JavaAbstractSyntax_ImportDeclaration class attributes and methods
JavaAbstractSyntax_ImportDeclaration_onDemand: Property = Property(name="onDemand", type=StringType)
JavaAbstractSyntax_ImportDeclaration_static: Property = Property(name="static", type=StringType)
JavaAbstractSyntax_ImportDeclaration.attributes={JavaAbstractSyntax_ImportDeclaration_onDemand, JavaAbstractSyntax_ImportDeclaration_static}

# SingleVariableDeclaration class attributes and methods

# JavaAbstractSyntax_Comment class attributes and methods

# JavaAbstractSyntax_CompilationUnit class attributes and methods

# Comment class attributes and methods

# PackageDeclaration class attributes and methods

# ImportDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# JavaAbstractSyntax_MemberRef class attributes and methods

# SimpleName class attributes and methods

# Name class attributes and methods

# JavaAbstractSyntax_MemberValuePair class attributes and methods

# Expression class attributes and methods

# JavaAbstractSyntax_MethodRef class attributes and methods

# MethodRefParameter class attributes and methods

# JavaAbstractSyntax_MethodRefParameter class attributes and methods
JavaAbstractSyntax_MethodRefParameter_varargs: Property = Property(name="varargs", type=StringType)
JavaAbstractSyntax_MethodRefParameter.attributes={JavaAbstractSyntax_MethodRefParameter_varargs}

# Type class attributes and methods

# JavaAbstractSyntax_ExtendedModifier class attributes and methods

# JavaAbstractSyntax_Modifier class attributes and methods
JavaAbstractSyntax_Modifier_abstract: Property = Property(name="abstract", type=StringType)
JavaAbstractSyntax_Modifier_final: Property = Property(name="final", type=StringType)
JavaAbstractSyntax_Modifier_native: Property = Property(name="native", type=StringType)
JavaAbstractSyntax_Modifier_none: Property = Property(name="none", type=StringType)
JavaAbstractSyntax_Modifier_private: Property = Property(name="private", type=StringType)
JavaAbstractSyntax_Modifier_protected: Property = Property(name="protected", type=StringType)
JavaAbstractSyntax_Modifier_public: Property = Property(name="public", type=StringType)
JavaAbstractSyntax_Modifier_static: Property = Property(name="static", type=StringType)
JavaAbstractSyntax_Modifier_strictfp: Property = Property(name="strictfp", type=StringType)
JavaAbstractSyntax_Modifier_synchronized: Property = Property(name="synchronized", type=StringType)
JavaAbstractSyntax_Modifier_transient: Property = Property(name="transient", type=StringType)
JavaAbstractSyntax_Modifier_volatile: Property = Property(name="volatile", type=StringType)
JavaAbstractSyntax_Modifier.attributes={JavaAbstractSyntax_Modifier_final, JavaAbstractSyntax_Modifier_strictfp, JavaAbstractSyntax_Modifier_none, JavaAbstractSyntax_Modifier_public, JavaAbstractSyntax_Modifier_synchronized, JavaAbstractSyntax_Modifier_transient, JavaAbstractSyntax_Modifier_volatile, JavaAbstractSyntax_Modifier_native, JavaAbstractSyntax_Modifier_abstract, JavaAbstractSyntax_Modifier_static, JavaAbstractSyntax_Modifier_private, JavaAbstractSyntax_Modifier_protected}

# JavaAbstractSyntax_TypeParameter class attributes and methods

# JavaAbstractSyntax_PackageDeclaration class attributes and methods

# Annotation class attributes and methods

# JavaAbstractSyntax_Statement class attributes and methods

# JavaAbstractSyntax_TagElement class attributes and methods
JavaAbstractSyntax_TagElement_tagName: Property = Property(name="tagName", type=StringType)
JavaAbstractSyntax_TagElement_nested: Property = Property(name="nested", type=StringType)
JavaAbstractSyntax_TagElement.attributes={JavaAbstractSyntax_TagElement_nested, JavaAbstractSyntax_TagElement_tagName}

# JavaAbstractSyntax_TextElement class attributes and methods
JavaAbstractSyntax_TextElement_text: Property = Property(name="text", type=StringType)
JavaAbstractSyntax_TextElement.attributes={JavaAbstractSyntax_TextElement_text}

# JavaAbstractSyntax_Type class attributes and methods

# JavaAbstractSyntax_VariableDeclaration class attributes and methods
JavaAbstractSyntax_VariableDeclaration_extraDimensions: Property = Property(name="extraDimensions", type=StringType)
JavaAbstractSyntax_VariableDeclaration.attributes={JavaAbstractSyntax_VariableDeclaration_extraDimensions}

# JavaAbstractSyntax_AbstractTypeDeclaration class attributes and methods
JavaAbstractSyntax_AbstractTypeDeclaration_localTypeDeclaration: Property = Property(name="localTypeDeclaration", type=StringType)
JavaAbstractSyntax_AbstractTypeDeclaration_memberTypeDeclaration: Property = Property(name="memberTypeDeclaration", type=StringType)
JavaAbstractSyntax_AbstractTypeDeclaration_packageMemberTypeDeclaration: Property = Property(name="packageMemberTypeDeclaration", type=StringType)
JavaAbstractSyntax_AbstractTypeDeclaration.attributes={JavaAbstractSyntax_AbstractTypeDeclaration_memberTypeDeclaration, JavaAbstractSyntax_AbstractTypeDeclaration_packageMemberTypeDeclaration, JavaAbstractSyntax_AbstractTypeDeclaration_localTypeDeclaration}

# JavaAbstractSyntax_AnnotationTypeMemberDeclaration class attributes and methods

# JavaAbstractSyntax_EnumConstantDeclaration class attributes and methods

# AnonymousClassDeclaration class attributes and methods

# JavaAbstractSyntax_FieldDeclaration class attributes and methods

# VariableDeclarationFragment class attributes and methods

# JavaAbstractSyntax_Initializer class attributes and methods

# JavaAbstractSyntax_MethodDeclaration class attributes and methods
JavaAbstractSyntax_MethodDeclaration_extraDimensions: Property = Property(name="extraDimensions", type=StringType)
JavaAbstractSyntax_MethodDeclaration_constructor: Property = Property(name="constructor", type=StringType)
JavaAbstractSyntax_MethodDeclaration_varargs: Property = Property(name="varargs", type=StringType)
JavaAbstractSyntax_MethodDeclaration.attributes={JavaAbstractSyntax_MethodDeclaration_varargs, JavaAbstractSyntax_MethodDeclaration_constructor, JavaAbstractSyntax_MethodDeclaration_extraDimensions}

# JavaAbstractSyntax_LineComment class attributes and methods

# JavaAbstractSyntax_Annotation class attributes and methods

# JavaAbstractSyntax_ArrayAccess class attributes and methods

# TypeParameter class attributes and methods

# JavaAbstractSyntax_AnnotationTypeDeclaration class attributes and methods

# JavaAbstractSyntax_EnumDeclaration class attributes and methods

# EnumConstantDeclaration class attributes and methods

# JavaAbstractSyntax_TypeDeclaration class attributes and methods
JavaAbstractSyntax_TypeDeclaration_interface: Property = Property(name="interface", type=StringType)
JavaAbstractSyntax_TypeDeclaration.attributes={JavaAbstractSyntax_TypeDeclaration_interface}

# JavaAbstractSyntax_BlockComment class attributes and methods

# JavaAbstractSyntax_Javadoc class attributes and methods

# TagElement class attributes and methods

# JavaAbstractSyntax_ArrayCreation class attributes and methods

# ArrayInitializer class attributes and methods

# ArrayType class attributes and methods

# JavaAbstractSyntax_ArrayInitializer class attributes and methods

# JavaAbstractSyntax_Assignment class attributes and methods
JavaAbstractSyntax_Assignment_operator: Property = Property(name="operator", type=StringType)
JavaAbstractSyntax_Assignment.attributes={JavaAbstractSyntax_Assignment_operator}

# JavaAbstractSyntax_BooleanLiteral class attributes and methods
JavaAbstractSyntax_BooleanLiteral_booleanValue: Property = Property(name="booleanValue", type=StringType)
JavaAbstractSyntax_BooleanLiteral.attributes={JavaAbstractSyntax_BooleanLiteral_booleanValue}

# JavaAbstractSyntax_CastExpression class attributes and methods

# JavaAbstractSyntax_CharacterLiteral class attributes and methods
JavaAbstractSyntax_CharacterLiteral_charValue: Property = Property(name="charValue", type=StringType)
JavaAbstractSyntax_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
JavaAbstractSyntax_CharacterLiteral.attributes={JavaAbstractSyntax_CharacterLiteral_escapedValue, JavaAbstractSyntax_CharacterLiteral_charValue}

# JavaAbstractSyntax_ClassInstanceCreation class attributes and methods

# JavaAbstractSyntax_ConditionalExpression class attributes and methods

# JavaAbstractSyntax_FieldAccess class attributes and methods

# JavaAbstractSyntax_InfixExpression class attributes and methods
JavaAbstractSyntax_InfixExpression_operator: Property = Property(name="operator", type=StringType)
JavaAbstractSyntax_InfixExpression.attributes={JavaAbstractSyntax_InfixExpression_operator}

# JavaAbstractSyntax_MethodInvocation class attributes and methods

# JavaAbstractSyntax_InstanceofExpression class attributes and methods

# JavaAbstractSyntax_PostfixExpression class attributes and methods
JavaAbstractSyntax_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
JavaAbstractSyntax_PostfixExpression.attributes={JavaAbstractSyntax_PostfixExpression_operator}

# JavaAbstractSyntax_Name class attributes and methods
JavaAbstractSyntax_Name_fullyQualifiedName: Property = Property(name="fullyQualifiedName", type=StringType)
JavaAbstractSyntax_Name.attributes={JavaAbstractSyntax_Name_fullyQualifiedName}

# JavaAbstractSyntax_NullLiteral class attributes and methods

# JavaAbstractSyntax_NumberLiteral class attributes and methods
JavaAbstractSyntax_NumberLiteral_token: Property = Property(name="token", type=StringType)
JavaAbstractSyntax_NumberLiteral.attributes={JavaAbstractSyntax_NumberLiteral_token}

# JavaAbstractSyntax_ParenthesizedExpression class attributes and methods

# JavaAbstractSyntax_SuperMethodInvocation class attributes and methods

# JavaAbstractSyntax_PrefixExpression class attributes and methods
JavaAbstractSyntax_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
JavaAbstractSyntax_PrefixExpression.attributes={JavaAbstractSyntax_PrefixExpression_operator}

# JavaAbstractSyntax_StringLiteral class attributes and methods
JavaAbstractSyntax_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
JavaAbstractSyntax_StringLiteral_literalValue: Property = Property(name="literalValue", type=StringType)
JavaAbstractSyntax_StringLiteral.attributes={JavaAbstractSyntax_StringLiteral_literalValue, JavaAbstractSyntax_StringLiteral_escapedValue}

# JavaAbstractSyntax_SuperFieldAccess class attributes and methods

# JavaAbstractSyntax_AssertStatement class attributes and methods

# Statement class attributes and methods

# JavaAbstractSyntax_ThisExpression class attributes and methods

# JavaAbstractSyntax_TypeLiteral class attributes and methods

# JavaAbstractSyntax_VariableDeclarationExpression class attributes and methods

# JavaAbstractSyntax_Block class attributes and methods

# JavaAbstractSyntax_BreakStatement class attributes and methods

# JavaAbstractSyntax_ConstructorInvocation class attributes and methods

# JavaAbstractSyntax_ContinueStatement class attributes and methods

# JavaAbstractSyntax_DoStatement class attributes and methods

# JavaAbstractSyntax_EmptyStatement class attributes and methods

# JavaAbstractSyntax_EnhancedForStatement class attributes and methods

# JavaAbstractSyntax_ExpressionStatement class attributes and methods

# JavaAbstractSyntax_ForStatement class attributes and methods

# JavaAbstractSyntax_IfStatement class attributes and methods

# JavaAbstractSyntax_LabeledStatement class attributes and methods

# JavaAbstractSyntax_ReturnStatement class attributes and methods

# JavaAbstractSyntax_SuperConstructorInvocation class attributes and methods

# JavaAbstractSyntax_TryStatement class attributes and methods

# CatchClause class attributes and methods

# JavaAbstractSyntax_SwitchCase class attributes and methods
JavaAbstractSyntax_SwitchCase_default: Property = Property(name="default", type=StringType)
JavaAbstractSyntax_SwitchCase.attributes={JavaAbstractSyntax_SwitchCase_default}

# JavaAbstractSyntax_SwitchStatement class attributes and methods

# JavaAbstractSyntax_SynchronizedStatement class attributes and methods

# JavaAbstractSyntax_ThrowStatement class attributes and methods

# JavaAbstractSyntax_ParameterizedType class attributes and methods

# JavaAbstractSyntax_TypeDeclarationStatement class attributes and methods

# JavaAbstractSyntax_VariableDeclarationStatement class attributes and methods

# JavaAbstractSyntax_WhileStatement class attributes and methods

# JavaAbstractSyntax_ArrayType class attributes and methods
JavaAbstractSyntax_ArrayType_dimensions: Property = Property(name="dimensions", type=StringType)
JavaAbstractSyntax_ArrayType.attributes={JavaAbstractSyntax_ArrayType_dimensions}

# JavaAbstractSyntax_VariableDeclarationFragment class attributes and methods

# JavaAbstractSyntax_QualifiedName class attributes and methods

# JavaAbstractSyntax_PrimitiveType class attributes and methods
JavaAbstractSyntax_PrimitiveType_code: Property = Property(name="code", type=StringType)
JavaAbstractSyntax_PrimitiveType.attributes={JavaAbstractSyntax_PrimitiveType_code}

# JavaAbstractSyntax_QualifiedType class attributes and methods

# JavaAbstractSyntax_SimpleType class attributes and methods

# JavaAbstractSyntax_WildcardType class attributes and methods
JavaAbstractSyntax_WildcardType_upperBound: Property = Property(name="upperBound", type=StringType)
JavaAbstractSyntax_WildcardType.attributes={JavaAbstractSyntax_WildcardType_upperBound}

# JavaAbstractSyntax_SingleVariableDeclaration class attributes and methods
JavaAbstractSyntax_SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=StringType)
JavaAbstractSyntax_SingleVariableDeclaration.attributes={JavaAbstractSyntax_SingleVariableDeclaration_varargs}

# VariableDeclaration class attributes and methods

# JavaAbstractSyntax_SimpleName class attributes and methods
JavaAbstractSyntax_SimpleName_identifier: Property = Property(name="identifier", type=StringType)
JavaAbstractSyntax_SimpleName_declaration: Property = Property(name="declaration", type=StringType)
JavaAbstractSyntax_SimpleName.attributes={JavaAbstractSyntax_SimpleName_identifier, JavaAbstractSyntax_SimpleName_declaration}

# JavaAbstractSyntax_MarkerAnnotation class attributes and methods

# JavaAbstractSyntax_NormalAnnotation class attributes and methods

# MemberValuePair class attributes and methods

# JavaAbstractSyntax_SingleMemberAnnotation class attributes and methods

# Relationships
javadoc3: BinaryAssociation = BinaryAssociation(
    name="javadoc3",
    ends={
        Property(name="Javadoc", type=JavaAbstractSyntax_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_BodyDeclaration4", type=Javadoc, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body5: BinaryAssociation = BinaryAssociation(
    name="body5",
    ends={
        Property(name="Block", type=JavaAbstractSyntax_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_CatchClause", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="ASTNode", type=JavaAbstractSyntax_AST, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AST", type=ASTNode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyDeclarations1: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations1",
    ends={
        Property(name="BodyDeclaration", type=JavaAbstractSyntax_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AnonymousClassDeclaration", type=BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers2: BinaryAssociation = BinaryAssociation(
    name="modifiers2",
    ends={
        Property(name="ExtendedModifier", type=JavaAbstractSyntax_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_BodyDeclaration", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception6: BinaryAssociation = BinaryAssociation(
    name="exception6",
    ends={
        Property(name="SingleVariableDeclaration", type=JavaAbstractSyntax_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_CatchClause7", type=SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alternateRoot8: BinaryAssociation = BinaryAssociation(
    name="alternateRoot8",
    ends={
        Property(name="ASTNode9", type=JavaAbstractSyntax_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Comment", type=ASTNode, multiplicity=Multiplicity(1, 1))
    }
)
comments10: BinaryAssociation = BinaryAssociation(
    name="comments10",
    ends={
        Property(name="Comment", type=JavaAbstractSyntax_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_CompilationUnit", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package11: BinaryAssociation = BinaryAssociation(
    name="package11",
    ends={
        Property(name="PackageDeclaration", type=JavaAbstractSyntax_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_CompilationUnit12", type=PackageDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imports13: BinaryAssociation = BinaryAssociation(
    name="imports13",
    ends={
        Property(name="ImportDeclaration", type=JavaAbstractSyntax_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_CompilationUnit14", type=ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types15: BinaryAssociation = BinaryAssociation(
    name="types15",
    ends={
        Property(name="AbstractTypeDeclaration", type=JavaAbstractSyntax_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_CompilationUnit16", type=AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name18: BinaryAssociation = BinaryAssociation(
    name="name18",
    ends={
        Property(name="SimpleName", type=JavaAbstractSyntax_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MemberRef", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name17: BinaryAssociation = BinaryAssociation(
    name="name17",
    ends={
        Property(name="Name", type=JavaAbstractSyntax_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ImportDeclaration", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier19: BinaryAssociation = BinaryAssociation(
    name="qualifier19",
    ends={
        Property(name="Name21", type=JavaAbstractSyntax_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MemberRef20", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name22: BinaryAssociation = BinaryAssociation(
    name="name22",
    ends={
        Property(name="SimpleName23", type=JavaAbstractSyntax_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MemberValuePair", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value24: BinaryAssociation = BinaryAssociation(
    name="value24",
    ends={
        Property(name="Expression", type=JavaAbstractSyntax_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MemberValuePair25", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name26: BinaryAssociation = BinaryAssociation(
    name="name26",
    ends={
        Property(name="SimpleName27", type=JavaAbstractSyntax_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodRef", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier28: BinaryAssociation = BinaryAssociation(
    name="qualifier28",
    ends={
        Property(name="Name30", type=JavaAbstractSyntax_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodRef29", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters31: BinaryAssociation = BinaryAssociation(
    name="parameters31",
    ends={
        Property(name="MethodRefParameter", type=JavaAbstractSyntax_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodRef32", type=MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name33: BinaryAssociation = BinaryAssociation(
    name="name33",
    ends={
        Property(name="SimpleName34", type=JavaAbstractSyntax_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodRefParameter", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="Type", type=JavaAbstractSyntax_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodRefParameter36", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name46: BinaryAssociation = BinaryAssociation(
    name="name46",
    ends={
        Property(name="SimpleName47", type=JavaAbstractSyntax_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeParameter", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeBounds48: BinaryAssociation = BinaryAssociation(
    name="typeBounds48",
    ends={
        Property(name="Type50", type=JavaAbstractSyntax_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeParameter49", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations37: BinaryAssociation = BinaryAssociation(
    name="annotations37",
    ends={
        Property(name="Annotation", type=JavaAbstractSyntax_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_PackageDeclaration", type=Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc38: BinaryAssociation = BinaryAssociation(
    name="javadoc38",
    ends={
        Property(name="Javadoc40", type=JavaAbstractSyntax_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_PackageDeclaration39", type=Javadoc, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name41: BinaryAssociation = BinaryAssociation(
    name="name41",
    ends={
        Property(name="Name43", type=JavaAbstractSyntax_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_PackageDeclaration42", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments44: BinaryAssociation = BinaryAssociation(
    name="fragments44",
    ends={
        Property(name="ASTNode45", type=JavaAbstractSyntax_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TagElement", type=ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer51: BinaryAssociation = BinaryAssociation(
    name="initializer51",
    ends={
        Property(name="Expression52", type=JavaAbstractSyntax_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclaration", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name53: BinaryAssociation = BinaryAssociation(
    name="name53",
    ends={
        Property(name="SimpleName55", type=JavaAbstractSyntax_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclaration54", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyDeclarations56: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations56",
    ends={
        Property(name="BodyDeclaration57", type=JavaAbstractSyntax_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AbstractTypeDeclaration", type=BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name58: BinaryAssociation = BinaryAssociation(
    name="name58",
    ends={
        Property(name="SimpleName60", type=JavaAbstractSyntax_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AbstractTypeDeclaration59", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name84: BinaryAssociation = BinaryAssociation(
    name="name84",
    ends={
        Property(name="SimpleName86", type=JavaAbstractSyntax_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodDeclaration85", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType87: BinaryAssociation = BinaryAssociation(
    name="returnType87",
    ends={
        Property(name="Type89", type=JavaAbstractSyntax_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodDeclaration88", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
default61: BinaryAssociation = BinaryAssociation(
    name="default61",
    ends={
        Property(name="Expression62", type=JavaAbstractSyntax_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AnnotationTypeMemberDeclaration", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name63: BinaryAssociation = BinaryAssociation(
    name="name63",
    ends={
        Property(name="SimpleName65", type=JavaAbstractSyntax_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AnnotationTypeMemberDeclaration64", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type66: BinaryAssociation = BinaryAssociation(
    name="type66",
    ends={
        Property(name="Type68", type=JavaAbstractSyntax_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AnnotationTypeMemberDeclaration67", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments69: BinaryAssociation = BinaryAssociation(
    name="arguments69",
    ends={
        Property(name="Expression70", type=JavaAbstractSyntax_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnumConstantDeclaration", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration71: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration71",
    ends={
        Property(name="AnonymousClassDeclaration", type=JavaAbstractSyntax_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnumConstantDeclaration72", type=AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name73: BinaryAssociation = BinaryAssociation(
    name="name73",
    ends={
        Property(name="SimpleName75", type=JavaAbstractSyntax_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnumConstantDeclaration74", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments76: BinaryAssociation = BinaryAssociation(
    name="fragments76",
    ends={
        Property(name="VariableDeclarationFragment", type=JavaAbstractSyntax_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_FieldDeclaration", type=VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type77: BinaryAssociation = BinaryAssociation(
    name="type77",
    ends={
        Property(name="Type79", type=JavaAbstractSyntax_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_FieldDeclaration78", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body80: BinaryAssociation = BinaryAssociation(
    name="body80",
    ends={
        Property(name="Block81", type=JavaAbstractSyntax_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Initializer", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body82: BinaryAssociation = BinaryAssociation(
    name="body82",
    ends={
        Property(name="Block83", type=JavaAbstractSyntax_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodDeclaration", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tags110: BinaryAssociation = BinaryAssociation(
    name="tags110",
    ends={
        Property(name="TagElement", type=JavaAbstractSyntax_Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Javadoc", type=TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeName111: BinaryAssociation = BinaryAssociation(
    name="typeName111",
    ends={
        Property(name="Name112", type=JavaAbstractSyntax_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Annotation", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters90: BinaryAssociation = BinaryAssociation(
    name="parameters90",
    ends={
        Property(name="SingleVariableDeclaration92", type=JavaAbstractSyntax_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodDeclaration91", type=SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thrownExceptions93: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions93",
    ends={
        Property(name="Name95", type=JavaAbstractSyntax_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodDeclaration94", type=Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters96: BinaryAssociation = BinaryAssociation(
    name="typeParameters96",
    ends={
        Property(name="TypeParameter", type=JavaAbstractSyntax_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodDeclaration97", type=TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaceTypes98: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes98",
    ends={
        Property(name="Type99", type=JavaAbstractSyntax_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnumDeclaration", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumConstants100: BinaryAssociation = BinaryAssociation(
    name="enumConstants100",
    ends={
        Property(name="EnumConstantDeclaration", type=JavaAbstractSyntax_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnumDeclaration101", type=EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclassType102: BinaryAssociation = BinaryAssociation(
    name="superclassType102",
    ends={
        Property(name="Type103", type=JavaAbstractSyntax_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeDeclaration", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superInterfaceTypes104: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes104",
    ends={
        Property(name="Type106", type=JavaAbstractSyntax_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeDeclaration105", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters107: BinaryAssociation = BinaryAssociation(
    name="typeParameters107",
    ends={
        Property(name="TypeParameter109", type=JavaAbstractSyntax_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeDeclaration108", type=TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightHandSide128: BinaryAssociation = BinaryAssociation(
    name="rightHandSide128",
    ends={
        Property(name="Expression130", type=JavaAbstractSyntax_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Assignment129", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array113: BinaryAssociation = BinaryAssociation(
    name="array113",
    ends={
        Property(name="Expression114", type=JavaAbstractSyntax_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayAccess", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index115: BinaryAssociation = BinaryAssociation(
    name="index115",
    ends={
        Property(name="Expression117", type=JavaAbstractSyntax_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayAccess116", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions118: BinaryAssociation = BinaryAssociation(
    name="dimensions118",
    ends={
        Property(name="Expression119", type=JavaAbstractSyntax_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayCreation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer120: BinaryAssociation = BinaryAssociation(
    name="initializer120",
    ends={
        Property(name="ArrayInitializer", type=JavaAbstractSyntax_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayCreation121", type=ArrayInitializer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type122: BinaryAssociation = BinaryAssociation(
    name="type122",
    ends={
        Property(name="ArrayType", type=JavaAbstractSyntax_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayCreation123", type=ArrayType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions124: BinaryAssociation = BinaryAssociation(
    name="expressions124",
    ends={
        Property(name="Expression125", type=JavaAbstractSyntax_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayInitializer", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftHandSide126: BinaryAssociation = BinaryAssociation(
    name="leftHandSide126",
    ends={
        Property(name="Expression127", type=JavaAbstractSyntax_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Assignment", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anonymousClassDeclaration138: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration138",
    ends={
        Property(name="AnonymousClassDeclaration140", type=JavaAbstractSyntax_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ClassInstanceCreation139", type=AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression141: BinaryAssociation = BinaryAssociation(
    name="expression141",
    ends={
        Property(name="Expression143", type=JavaAbstractSyntax_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ClassInstanceCreation142", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type144: BinaryAssociation = BinaryAssociation(
    name="type144",
    ends={
        Property(name="Type146", type=JavaAbstractSyntax_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ClassInstanceCreation145", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments147: BinaryAssociation = BinaryAssociation(
    name="typeArguments147",
    ends={
        Property(name="Type149", type=JavaAbstractSyntax_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ClassInstanceCreation148", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression131: BinaryAssociation = BinaryAssociation(
    name="expression131",
    ends={
        Property(name="Expression132", type=JavaAbstractSyntax_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_CastExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type133: BinaryAssociation = BinaryAssociation(
    name="type133",
    ends={
        Property(name="Type135", type=JavaAbstractSyntax_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_CastExpression134", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments136: BinaryAssociation = BinaryAssociation(
    name="arguments136",
    ends={
        Property(name="Expression137", type=JavaAbstractSyntax_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ClassInstanceCreation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedOperands163: BinaryAssociation = BinaryAssociation(
    name="extendedOperands163",
    ends={
        Property(name="JavaAbstractSyntax_InfixExpression", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Expression164", type=JavaAbstractSyntax_InfixExpression, multiplicity=Multiplicity(1, 1))
    }
)
leftOperand165: BinaryAssociation = BinaryAssociation(
    name="leftOperand165",
    ends={
        Property(name="Expression167", type=JavaAbstractSyntax_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_InfixExpression166", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression150: BinaryAssociation = BinaryAssociation(
    name="elseExpression150",
    ends={
        Property(name="Expression151", type=JavaAbstractSyntax_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ConditionalExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression152: BinaryAssociation = BinaryAssociation(
    name="expression152",
    ends={
        Property(name="Expression154", type=JavaAbstractSyntax_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ConditionalExpression153", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression155: BinaryAssociation = BinaryAssociation(
    name="thenExpression155",
    ends={
        Property(name="Expression157", type=JavaAbstractSyntax_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ConditionalExpression156", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression158: BinaryAssociation = BinaryAssociation(
    name="expression158",
    ends={
        Property(name="Expression159", type=JavaAbstractSyntax_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_FieldAccess", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name160: BinaryAssociation = BinaryAssociation(
    name="name160",
    ends={
        Property(name="SimpleName162", type=JavaAbstractSyntax_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_FieldAccess161", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand173: BinaryAssociation = BinaryAssociation(
    name="rightOperand173",
    ends={
        Property(name="JavaAbstractSyntax_InstanceofExpression174", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Type175", type=JavaAbstractSyntax_InstanceofExpression, multiplicity=Multiplicity(1, 1))
    }
)
arguments176: BinaryAssociation = BinaryAssociation(
    name="arguments176",
    ends={
        Property(name="Expression177", type=JavaAbstractSyntax_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightOperand168: BinaryAssociation = BinaryAssociation(
    name="rightOperand168",
    ends={
        Property(name="Expression170", type=JavaAbstractSyntax_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_InfixExpression169", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand171: BinaryAssociation = BinaryAssociation(
    name="leftOperand171",
    ends={
        Property(name="Expression172", type=JavaAbstractSyntax_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_InstanceofExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand189: BinaryAssociation = BinaryAssociation(
    name="operand189",
    ends={
        Property(name="Expression190", type=JavaAbstractSyntax_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_PostfixExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression178: BinaryAssociation = BinaryAssociation(
    name="expression178",
    ends={
        Property(name="Expression180", type=JavaAbstractSyntax_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodInvocation179", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name181: BinaryAssociation = BinaryAssociation(
    name="name181",
    ends={
        Property(name="SimpleName183", type=JavaAbstractSyntax_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodInvocation182", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments184: BinaryAssociation = BinaryAssociation(
    name="typeArguments184",
    ends={
        Property(name="Type186", type=JavaAbstractSyntax_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodInvocation185", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression187: BinaryAssociation = BinaryAssociation(
    name="expression187",
    ends={
        Property(name="Expression188", type=JavaAbstractSyntax_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ParenthesizedExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier195: BinaryAssociation = BinaryAssociation(
    name="qualifier195",
    ends={
        Property(name="Name197", type=JavaAbstractSyntax_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperFieldAccess196", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments198: BinaryAssociation = BinaryAssociation(
    name="arguments198",
    ends={
        Property(name="Expression199", type=JavaAbstractSyntax_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperMethodInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand191: BinaryAssociation = BinaryAssociation(
    name="operand191",
    ends={
        Property(name="Expression192", type=JavaAbstractSyntax_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_PrefixExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name193: BinaryAssociation = BinaryAssociation(
    name="name193",
    ends={
        Property(name="SimpleName194", type=JavaAbstractSyntax_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperFieldAccess", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifiers215: BinaryAssociation = BinaryAssociation(
    name="modifiers215",
    ends={
        Property(name="ExtendedModifier217", type=JavaAbstractSyntax_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationExpression216", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type218: BinaryAssociation = BinaryAssociation(
    name="type218",
    ends={
        Property(name="Type220", type=JavaAbstractSyntax_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationExpression219", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression221: BinaryAssociation = BinaryAssociation(
    name="expression221",
    ends={
        Property(name="Expression222", type=JavaAbstractSyntax_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AssertStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name200: BinaryAssociation = BinaryAssociation(
    name="name200",
    ends={
        Property(name="Name202", type=JavaAbstractSyntax_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperMethodInvocation201", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier203: BinaryAssociation = BinaryAssociation(
    name="qualifier203",
    ends={
        Property(name="Name205", type=JavaAbstractSyntax_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperMethodInvocation204", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments206: BinaryAssociation = BinaryAssociation(
    name="typeArguments206",
    ends={
        Property(name="Type208", type=JavaAbstractSyntax_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperMethodInvocation207", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier209: BinaryAssociation = BinaryAssociation(
    name="qualifier209",
    ends={
        Property(name="Name210", type=JavaAbstractSyntax_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ThisExpression", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type211: BinaryAssociation = BinaryAssociation(
    name="type211",
    ends={
        Property(name="Type212", type=JavaAbstractSyntax_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeLiteral", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments213: BinaryAssociation = BinaryAssociation(
    name="fragments213",
    ends={
        Property(name="VariableDeclarationFragment214", type=JavaAbstractSyntax_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationExpression", type=VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message223: BinaryAssociation = BinaryAssociation(
    name="message223",
    ends={
        Property(name="Expression225", type=JavaAbstractSyntax_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AssertStatement224", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements226: BinaryAssociation = BinaryAssociation(
    name="statements226",
    ends={
        Property(name="Statement", type=JavaAbstractSyntax_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Block", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label227: BinaryAssociation = BinaryAssociation(
    name="label227",
    ends={
        Property(name="SimpleName228", type=JavaAbstractSyntax_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_BreakStatement", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments229: BinaryAssociation = BinaryAssociation(
    name="arguments229",
    ends={
        Property(name="Expression230", type=JavaAbstractSyntax_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ConstructorInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression243: BinaryAssociation = BinaryAssociation(
    name="expression243",
    ends={
        Property(name="Expression245", type=JavaAbstractSyntax_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnhancedForStatement244", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments231: BinaryAssociation = BinaryAssociation(
    name="typeArguments231",
    ends={
        Property(name="Type233", type=JavaAbstractSyntax_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ConstructorInvocation232", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label234: BinaryAssociation = BinaryAssociation(
    name="label234",
    ends={
        Property(name="SimpleName235", type=JavaAbstractSyntax_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ContinueStatement", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body236: BinaryAssociation = BinaryAssociation(
    name="body236",
    ends={
        Property(name="Statement237", type=JavaAbstractSyntax_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_DoStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression238: BinaryAssociation = BinaryAssociation(
    name="expression238",
    ends={
        Property(name="Expression240", type=JavaAbstractSyntax_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_DoStatement239", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body241: BinaryAssociation = BinaryAssociation(
    name="body241",
    ends={
        Property(name="Statement242", type=JavaAbstractSyntax_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnhancedForStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression253: BinaryAssociation = BinaryAssociation(
    name="expression253",
    ends={
        Property(name="Expression255", type=JavaAbstractSyntax_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ForStatement254", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter246: BinaryAssociation = BinaryAssociation(
    name="parameter246",
    ends={
        Property(name="SingleVariableDeclaration248", type=JavaAbstractSyntax_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnhancedForStatement247", type=SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression249: BinaryAssociation = BinaryAssociation(
    name="expression249",
    ends={
        Property(name="Expression250", type=JavaAbstractSyntax_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body251: BinaryAssociation = BinaryAssociation(
    name="body251",
    ends={
        Property(name="Statement252", type=JavaAbstractSyntax_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ForStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement262: BinaryAssociation = BinaryAssociation(
    name="elseStatement262",
    ends={
        Property(name="Statement263", type=JavaAbstractSyntax_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_IfStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression264: BinaryAssociation = BinaryAssociation(
    name="expression264",
    ends={
        Property(name="Expression266", type=JavaAbstractSyntax_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_IfStatement265", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializers256: BinaryAssociation = BinaryAssociation(
    name="initializers256",
    ends={
        Property(name="Expression258", type=JavaAbstractSyntax_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ForStatement257", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updaters259: BinaryAssociation = BinaryAssociation(
    name="updaters259",
    ends={
        Property(name="Expression261", type=JavaAbstractSyntax_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ForStatement260", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments282: BinaryAssociation = BinaryAssociation(
    name="typeArguments282",
    ends={
        Property(name="Type284", type=JavaAbstractSyntax_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperConstructorInvocation283", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenStatement267: BinaryAssociation = BinaryAssociation(
    name="thenStatement267",
    ends={
        Property(name="Statement269", type=JavaAbstractSyntax_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_IfStatement268", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body270: BinaryAssociation = BinaryAssociation(
    name="body270",
    ends={
        Property(name="Statement271", type=JavaAbstractSyntax_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_LabeledStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label272: BinaryAssociation = BinaryAssociation(
    name="label272",
    ends={
        Property(name="SimpleName274", type=JavaAbstractSyntax_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_LabeledStatement273", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression275: BinaryAssociation = BinaryAssociation(
    name="expression275",
    ends={
        Property(name="Expression276", type=JavaAbstractSyntax_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ReturnStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments277: BinaryAssociation = BinaryAssociation(
    name="arguments277",
    ends={
        Property(name="Expression278", type=JavaAbstractSyntax_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperConstructorInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchClauses299: BinaryAssociation = BinaryAssociation(
    name="catchClauses299",
    ends={
        Property(name="CatchClause", type=JavaAbstractSyntax_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TryStatement", type=CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression279: BinaryAssociation = BinaryAssociation(
    name="expression279",
    ends={
        Property(name="Expression281", type=JavaAbstractSyntax_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperConstructorInvocation280", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body300: BinaryAssociation = BinaryAssociation(
    name="body300",
    ends={
        Property(name="Block302", type=JavaAbstractSyntax_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TryStatement301", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression285: BinaryAssociation = BinaryAssociation(
    name="expression285",
    ends={
        Property(name="Expression286", type=JavaAbstractSyntax_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SwitchCase", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression287: BinaryAssociation = BinaryAssociation(
    name="expression287",
    ends={
        Property(name="Expression288", type=JavaAbstractSyntax_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SwitchStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements289: BinaryAssociation = BinaryAssociation(
    name="statements289",
    ends={
        Property(name="Statement291", type=JavaAbstractSyntax_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SwitchStatement290", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body292: BinaryAssociation = BinaryAssociation(
    name="body292",
    ends={
        Property(name="Block293", type=JavaAbstractSyntax_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SynchronizedStatement", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression294: BinaryAssociation = BinaryAssociation(
    name="expression294",
    ends={
        Property(name="Expression296", type=JavaAbstractSyntax_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SynchronizedStatement295", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression297: BinaryAssociation = BinaryAssociation(
    name="expression297",
    ends={
        Property(name="Expression298", type=JavaAbstractSyntax_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ThrowStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType323: BinaryAssociation = BinaryAssociation(
    name="elementType323",
    ends={
        Property(name="Type325", type=JavaAbstractSyntax_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayType324", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally303: BinaryAssociation = BinaryAssociation(
    name="finally303",
    ends={
        Property(name="Block305", type=JavaAbstractSyntax_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TryStatement304", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration306: BinaryAssociation = BinaryAssociation(
    name="declaration306",
    ends={
        Property(name="AbstractTypeDeclaration307", type=JavaAbstractSyntax_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeDeclarationStatement", type=AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments308: BinaryAssociation = BinaryAssociation(
    name="fragments308",
    ends={
        Property(name="VariableDeclarationFragment309", type=JavaAbstractSyntax_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationStatement", type=VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers310: BinaryAssociation = BinaryAssociation(
    name="modifiers310",
    ends={
        Property(name="ExtendedModifier312", type=JavaAbstractSyntax_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationStatement311", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type313: BinaryAssociation = BinaryAssociation(
    name="type313",
    ends={
        Property(name="Type315", type=JavaAbstractSyntax_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationStatement314", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body316: BinaryAssociation = BinaryAssociation(
    name="body316",
    ends={
        Property(name="Statement317", type=JavaAbstractSyntax_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_WhileStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression318: BinaryAssociation = BinaryAssociation(
    name="expression318",
    ends={
        Property(name="Expression320", type=JavaAbstractSyntax_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_WhileStatement319", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
componentType321: BinaryAssociation = BinaryAssociation(
    name="componentType321",
    ends={
        Property(name="Type322", type=JavaAbstractSyntax_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifiers342: BinaryAssociation = BinaryAssociation(
    name="modifiers342",
    ends={
        Property(name="ExtendedModifier344", type=JavaAbstractSyntax_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SingleVariableDeclaration343", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type326: BinaryAssociation = BinaryAssociation(
    name="type326",
    ends={
        Property(name="Type327", type=JavaAbstractSyntax_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ParameterizedType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments328: BinaryAssociation = BinaryAssociation(
    name="typeArguments328",
    ends={
        Property(name="Type330", type=JavaAbstractSyntax_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ParameterizedType329", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name331: BinaryAssociation = BinaryAssociation(
    name="name331",
    ends={
        Property(name="SimpleName332", type=JavaAbstractSyntax_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_QualifiedType", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier333: BinaryAssociation = BinaryAssociation(
    name="qualifier333",
    ends={
        Property(name="Type335", type=JavaAbstractSyntax_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_QualifiedType334", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name336: BinaryAssociation = BinaryAssociation(
    name="name336",
    ends={
        Property(name="Name337", type=JavaAbstractSyntax_SimpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SimpleType", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bound338: BinaryAssociation = BinaryAssociation(
    name="bound338",
    ends={
        Property(name="Type339", type=JavaAbstractSyntax_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_WildcardType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type340: BinaryAssociation = BinaryAssociation(
    name="type340",
    ends={
        Property(name="Type341", type=JavaAbstractSyntax_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SingleVariableDeclaration", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name345: BinaryAssociation = BinaryAssociation(
    name="name345",
    ends={
        Property(name="SimpleName346", type=JavaAbstractSyntax_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_QualifiedName", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier347: BinaryAssociation = BinaryAssociation(
    name="qualifier347",
    ends={
        Property(name="Name349", type=JavaAbstractSyntax_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_QualifiedName348", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values350: BinaryAssociation = BinaryAssociation(
    name="values350",
    ends={
        Property(name="MemberValuePair", type=JavaAbstractSyntax_NormalAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_NormalAnnotation", type=MemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value351: BinaryAssociation = BinaryAssociation(
    name="value351",
    ends={
        Property(name="Expression352", type=JavaAbstractSyntax_SingleMemberAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SingleMemberAnnotation", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_JavaAbstractSyntax_CatchClause_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_CatchClause)
gen_JavaAbstractSyntax_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_AnonymousClassDeclaration)
gen_JavaAbstractSyntax_BodyDeclaration_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_BodyDeclaration)
gen_JavaAbstractSyntax_Expression_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_Expression)
gen_JavaAbstractSyntax_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_ImportDeclaration)
gen_JavaAbstractSyntax_Comment_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_Comment)
gen_JavaAbstractSyntax_CompilationUnit_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_CompilationUnit)
gen_JavaAbstractSyntax_MemberRef_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_MemberRef)
gen_JavaAbstractSyntax_Modifier_ExtendedModifier = Generalization(general=ExtendedModifier, specific=JavaAbstractSyntax_Modifier)
gen_JavaAbstractSyntax_MemberValuePair_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_MemberValuePair)
gen_JavaAbstractSyntax_MethodRef_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_MethodRef)
gen_JavaAbstractSyntax_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_MethodRefParameter)
gen_JavaAbstractSyntax_Modifier_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_Modifier)
gen_JavaAbstractSyntax_TypeParameter_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_TypeParameter)
gen_JavaAbstractSyntax_PackageDeclaration_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_PackageDeclaration)
gen_JavaAbstractSyntax_Statement_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_Statement)
gen_JavaAbstractSyntax_TagElement_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_TagElement)
gen_JavaAbstractSyntax_TextElement_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_TextElement)
gen_JavaAbstractSyntax_Type_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_Type)
gen_JavaAbstractSyntax_VariableDeclaration_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_VariableDeclaration)
gen_JavaAbstractSyntax_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_AbstractTypeDeclaration)
gen_JavaAbstractSyntax_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_AnnotationTypeMemberDeclaration)
gen_JavaAbstractSyntax_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_EnumConstantDeclaration)
gen_JavaAbstractSyntax_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_FieldDeclaration)
gen_JavaAbstractSyntax_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_Initializer)
gen_JavaAbstractSyntax_MethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_MethodDeclaration)
gen_JavaAbstractSyntax_LineComment_Comment = Generalization(general=Comment, specific=JavaAbstractSyntax_LineComment)
gen_JavaAbstractSyntax_Annotation_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_Annotation)
gen_JavaAbstractSyntax_Annotation_ExtendedModifier = Generalization(general=ExtendedModifier, specific=JavaAbstractSyntax_Annotation)
gen_JavaAbstractSyntax_ArrayAccess_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ArrayAccess)
gen_JavaAbstractSyntax_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JavaAbstractSyntax_AnnotationTypeDeclaration)
gen_JavaAbstractSyntax_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JavaAbstractSyntax_EnumDeclaration)
gen_JavaAbstractSyntax_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JavaAbstractSyntax_TypeDeclaration)
gen_JavaAbstractSyntax_BlockComment_Comment = Generalization(general=Comment, specific=JavaAbstractSyntax_BlockComment)
gen_JavaAbstractSyntax_Javadoc_Comment = Generalization(general=Comment, specific=JavaAbstractSyntax_Javadoc)
gen_JavaAbstractSyntax_ArrayCreation_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ArrayCreation)
gen_JavaAbstractSyntax_ArrayInitializer_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ArrayInitializer)
gen_JavaAbstractSyntax_Assignment_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_Assignment)
gen_JavaAbstractSyntax_BooleanLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_BooleanLiteral)
gen_JavaAbstractSyntax_CastExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_CastExpression)
gen_JavaAbstractSyntax_CharacterLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_CharacterLiteral)
gen_JavaAbstractSyntax_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ClassInstanceCreation)
gen_JavaAbstractSyntax_ConditionalExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ConditionalExpression)
gen_JavaAbstractSyntax_FieldAccess_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_FieldAccess)
gen_JavaAbstractSyntax_InfixExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_InfixExpression)
gen_JavaAbstractSyntax_MethodInvocation_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_MethodInvocation)
gen_JavaAbstractSyntax_InstanceofExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_InstanceofExpression)
gen_JavaAbstractSyntax_PostfixExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_PostfixExpression)
gen_JavaAbstractSyntax_Name_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_Name)
gen_JavaAbstractSyntax_NullLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_NullLiteral)
gen_JavaAbstractSyntax_NumberLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_NumberLiteral)
gen_JavaAbstractSyntax_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ParenthesizedExpression)
gen_JavaAbstractSyntax_SuperMethodInvocation_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_SuperMethodInvocation)
gen_JavaAbstractSyntax_PrefixExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_PrefixExpression)
gen_JavaAbstractSyntax_StringLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_StringLiteral)
gen_JavaAbstractSyntax_SuperFieldAccess_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_SuperFieldAccess)
gen_JavaAbstractSyntax_AssertStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_AssertStatement)
gen_JavaAbstractSyntax_ThisExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ThisExpression)
gen_JavaAbstractSyntax_TypeLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_TypeLiteral)
gen_JavaAbstractSyntax_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_VariableDeclarationExpression)
gen_JavaAbstractSyntax_Block_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_Block)
gen_JavaAbstractSyntax_BreakStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_BreakStatement)
gen_JavaAbstractSyntax_ConstructorInvocation_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ConstructorInvocation)
gen_JavaAbstractSyntax_ContinueStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ContinueStatement)
gen_JavaAbstractSyntax_DoStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_DoStatement)
gen_JavaAbstractSyntax_EmptyStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_EmptyStatement)
gen_JavaAbstractSyntax_EnhancedForStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_EnhancedForStatement)
gen_JavaAbstractSyntax_ExpressionStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ExpressionStatement)
gen_JavaAbstractSyntax_ForStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ForStatement)
gen_JavaAbstractSyntax_IfStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_IfStatement)
gen_JavaAbstractSyntax_LabeledStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_LabeledStatement)
gen_JavaAbstractSyntax_ReturnStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ReturnStatement)
gen_JavaAbstractSyntax_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_SuperConstructorInvocation)
gen_JavaAbstractSyntax_TryStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_TryStatement)
gen_JavaAbstractSyntax_SwitchCase_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_SwitchCase)
gen_JavaAbstractSyntax_SwitchStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_SwitchStatement)
gen_JavaAbstractSyntax_SynchronizedStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_SynchronizedStatement)
gen_JavaAbstractSyntax_ThrowStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ThrowStatement)
gen_JavaAbstractSyntax_ParameterizedType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_ParameterizedType)
gen_JavaAbstractSyntax_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_TypeDeclarationStatement)
gen_JavaAbstractSyntax_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_VariableDeclarationStatement)
gen_JavaAbstractSyntax_WhileStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_WhileStatement)
gen_JavaAbstractSyntax_ArrayType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_ArrayType)
gen_JavaAbstractSyntax_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=JavaAbstractSyntax_VariableDeclarationFragment)
gen_JavaAbstractSyntax_QualifiedName_Name = Generalization(general=Name, specific=JavaAbstractSyntax_QualifiedName)
gen_JavaAbstractSyntax_PrimitiveType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_PrimitiveType)
gen_JavaAbstractSyntax_QualifiedType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_QualifiedType)
gen_JavaAbstractSyntax_SimpleType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_SimpleType)
gen_JavaAbstractSyntax_WildcardType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_WildcardType)
gen_JavaAbstractSyntax_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=JavaAbstractSyntax_SingleVariableDeclaration)
gen_JavaAbstractSyntax_SimpleName_Name = Generalization(general=Name, specific=JavaAbstractSyntax_SimpleName)
gen_JavaAbstractSyntax_MarkerAnnotation_Annotation = Generalization(general=Annotation, specific=JavaAbstractSyntax_MarkerAnnotation)
gen_JavaAbstractSyntax_NormalAnnotation_Annotation = Generalization(general=Annotation, specific=JavaAbstractSyntax_NormalAnnotation)
gen_JavaAbstractSyntax_SingleMemberAnnotation_Annotation = Generalization(general=Annotation, specific=JavaAbstractSyntax_SingleMemberAnnotation)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Javadoc, JavaAbstractSyntax_CatchClause, Block, JavaAbstractSyntax_AST, ASTNode, JavaAbstractSyntax_ASTNode, JavaAbstractSyntax_AnonymousClassDeclaration, BodyDeclaration, JavaAbstractSyntax_BodyDeclaration, ExtendedModifier, JavaAbstractSyntax_Expression, JavaAbstractSyntax_ImportDeclaration, SingleVariableDeclaration, JavaAbstractSyntax_Comment, JavaAbstractSyntax_CompilationUnit, Comment, PackageDeclaration, ImportDeclaration, AbstractTypeDeclaration, JavaAbstractSyntax_MemberRef, SimpleName, Name, JavaAbstractSyntax_MemberValuePair, Expression, JavaAbstractSyntax_MethodRef, MethodRefParameter, JavaAbstractSyntax_MethodRefParameter, Type, JavaAbstractSyntax_ExtendedModifier, JavaAbstractSyntax_Modifier, JavaAbstractSyntax_TypeParameter, JavaAbstractSyntax_PackageDeclaration, Annotation, JavaAbstractSyntax_Statement, JavaAbstractSyntax_TagElement, JavaAbstractSyntax_TextElement, JavaAbstractSyntax_Type, JavaAbstractSyntax_VariableDeclaration, JavaAbstractSyntax_AbstractTypeDeclaration, JavaAbstractSyntax_AnnotationTypeMemberDeclaration, JavaAbstractSyntax_EnumConstantDeclaration, AnonymousClassDeclaration, JavaAbstractSyntax_FieldDeclaration, VariableDeclarationFragment, JavaAbstractSyntax_Initializer, JavaAbstractSyntax_MethodDeclaration, JavaAbstractSyntax_LineComment, JavaAbstractSyntax_Annotation, JavaAbstractSyntax_ArrayAccess, TypeParameter, JavaAbstractSyntax_AnnotationTypeDeclaration, JavaAbstractSyntax_EnumDeclaration, EnumConstantDeclaration, JavaAbstractSyntax_TypeDeclaration, JavaAbstractSyntax_BlockComment, JavaAbstractSyntax_Javadoc, TagElement, JavaAbstractSyntax_ArrayCreation, ArrayInitializer, ArrayType, JavaAbstractSyntax_ArrayInitializer, JavaAbstractSyntax_Assignment, JavaAbstractSyntax_BooleanLiteral, JavaAbstractSyntax_CastExpression, JavaAbstractSyntax_CharacterLiteral, JavaAbstractSyntax_ClassInstanceCreation, JavaAbstractSyntax_ConditionalExpression, JavaAbstractSyntax_FieldAccess, JavaAbstractSyntax_InfixExpression, JavaAbstractSyntax_MethodInvocation, JavaAbstractSyntax_InstanceofExpression, JavaAbstractSyntax_PostfixExpression, JavaAbstractSyntax_Name, JavaAbstractSyntax_NullLiteral, JavaAbstractSyntax_NumberLiteral, JavaAbstractSyntax_ParenthesizedExpression, JavaAbstractSyntax_SuperMethodInvocation, JavaAbstractSyntax_PrefixExpression, JavaAbstractSyntax_StringLiteral, JavaAbstractSyntax_SuperFieldAccess, JavaAbstractSyntax_AssertStatement, Statement, JavaAbstractSyntax_ThisExpression, JavaAbstractSyntax_TypeLiteral, JavaAbstractSyntax_VariableDeclarationExpression, JavaAbstractSyntax_Block, JavaAbstractSyntax_BreakStatement, JavaAbstractSyntax_ConstructorInvocation, JavaAbstractSyntax_ContinueStatement, JavaAbstractSyntax_DoStatement, JavaAbstractSyntax_EmptyStatement, JavaAbstractSyntax_EnhancedForStatement, JavaAbstractSyntax_ExpressionStatement, JavaAbstractSyntax_ForStatement, JavaAbstractSyntax_IfStatement, JavaAbstractSyntax_LabeledStatement, JavaAbstractSyntax_ReturnStatement, JavaAbstractSyntax_SuperConstructorInvocation, JavaAbstractSyntax_TryStatement, CatchClause, JavaAbstractSyntax_SwitchCase, JavaAbstractSyntax_SwitchStatement, JavaAbstractSyntax_SynchronizedStatement, JavaAbstractSyntax_ThrowStatement, JavaAbstractSyntax_ParameterizedType, JavaAbstractSyntax_TypeDeclarationStatement, JavaAbstractSyntax_VariableDeclarationStatement, JavaAbstractSyntax_WhileStatement, JavaAbstractSyntax_ArrayType, JavaAbstractSyntax_VariableDeclarationFragment, JavaAbstractSyntax_QualifiedName, JavaAbstractSyntax_PrimitiveType, JavaAbstractSyntax_QualifiedType, JavaAbstractSyntax_SimpleType, JavaAbstractSyntax_WildcardType, JavaAbstractSyntax_SingleVariableDeclaration, VariableDeclaration, JavaAbstractSyntax_SimpleName, JavaAbstractSyntax_MarkerAnnotation, JavaAbstractSyntax_NormalAnnotation, MemberValuePair, JavaAbstractSyntax_SingleMemberAnnotation, AssignementOperatorKind, InfixExpressionOperatorKind, PostfixExpresssionOperatorKind, PrefixExpresssionOperatorKind},
    associations={javadoc3, body5, root0, bodyDeclarations1, modifiers2, exception6, alternateRoot8, comments10, package11, imports13, types15, name18, name17, qualifier19, name22, value24, name26, qualifier28, parameters31, name33, type35, name46, typeBounds48, annotations37, javadoc38, name41, fragments44, initializer51, name53, bodyDeclarations56, name58, name84, returnType87, default61, name63, type66, arguments69, anonymousClassDeclaration71, name73, fragments76, type77, body80, body82, tags110, typeName111, parameters90, thrownExceptions93, typeParameters96, superInterfaceTypes98, enumConstants100, superclassType102, superInterfaceTypes104, typeParameters107, rightHandSide128, array113, index115, dimensions118, initializer120, type122, expressions124, leftHandSide126, anonymousClassDeclaration138, expression141, type144, typeArguments147, expression131, type133, arguments136, extendedOperands163, leftOperand165, elseExpression150, expression152, thenExpression155, expression158, name160, rightOperand173, arguments176, rightOperand168, leftOperand171, operand189, expression178, name181, typeArguments184, expression187, qualifier195, arguments198, operand191, name193, modifiers215, type218, expression221, name200, qualifier203, typeArguments206, qualifier209, type211, fragments213, message223, statements226, label227, arguments229, expression243, typeArguments231, label234, body236, expression238, body241, expression253, parameter246, expression249, body251, elseStatement262, expression264, initializers256, updaters259, typeArguments282, thenStatement267, body270, label272, expression275, arguments277, catchClauses299, expression279, body300, expression285, expression287, statements289, body292, expression294, expression297, elementType323, finally303, declaration306, fragments308, modifiers310, type313, body316, expression318, componentType321, modifiers342, type326, typeArguments328, name331, qualifier333, name336, bound338, type340, name345, qualifier347, values350, value351},
    generalizations={gen_JavaAbstractSyntax_CatchClause_ASTNode, gen_JavaAbstractSyntax_AnonymousClassDeclaration_ASTNode, gen_JavaAbstractSyntax_BodyDeclaration_ASTNode, gen_JavaAbstractSyntax_Expression_ASTNode, gen_JavaAbstractSyntax_ImportDeclaration_ASTNode, gen_JavaAbstractSyntax_Comment_ASTNode, gen_JavaAbstractSyntax_CompilationUnit_ASTNode, gen_JavaAbstractSyntax_MemberRef_ASTNode, gen_JavaAbstractSyntax_Modifier_ExtendedModifier, gen_JavaAbstractSyntax_MemberValuePair_ASTNode, gen_JavaAbstractSyntax_MethodRef_ASTNode, gen_JavaAbstractSyntax_MethodRefParameter_ASTNode, gen_JavaAbstractSyntax_Modifier_ASTNode, gen_JavaAbstractSyntax_TypeParameter_ASTNode, gen_JavaAbstractSyntax_PackageDeclaration_ASTNode, gen_JavaAbstractSyntax_Statement_ASTNode, gen_JavaAbstractSyntax_TagElement_ASTNode, gen_JavaAbstractSyntax_TextElement_ASTNode, gen_JavaAbstractSyntax_Type_ASTNode, gen_JavaAbstractSyntax_VariableDeclaration_ASTNode, gen_JavaAbstractSyntax_AbstractTypeDeclaration_BodyDeclaration, gen_JavaAbstractSyntax_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_JavaAbstractSyntax_EnumConstantDeclaration_BodyDeclaration, gen_JavaAbstractSyntax_FieldDeclaration_BodyDeclaration, gen_JavaAbstractSyntax_Initializer_BodyDeclaration, gen_JavaAbstractSyntax_MethodDeclaration_BodyDeclaration, gen_JavaAbstractSyntax_LineComment_Comment, gen_JavaAbstractSyntax_Annotation_Expression, gen_JavaAbstractSyntax_Annotation_ExtendedModifier, gen_JavaAbstractSyntax_ArrayAccess_Expression, gen_JavaAbstractSyntax_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_JavaAbstractSyntax_EnumDeclaration_AbstractTypeDeclaration, gen_JavaAbstractSyntax_TypeDeclaration_AbstractTypeDeclaration, gen_JavaAbstractSyntax_BlockComment_Comment, gen_JavaAbstractSyntax_Javadoc_Comment, gen_JavaAbstractSyntax_ArrayCreation_Expression, gen_JavaAbstractSyntax_ArrayInitializer_Expression, gen_JavaAbstractSyntax_Assignment_Expression, gen_JavaAbstractSyntax_BooleanLiteral_Expression, gen_JavaAbstractSyntax_CastExpression_Expression, gen_JavaAbstractSyntax_CharacterLiteral_Expression, gen_JavaAbstractSyntax_ClassInstanceCreation_Expression, gen_JavaAbstractSyntax_ConditionalExpression_Expression, gen_JavaAbstractSyntax_FieldAccess_Expression, gen_JavaAbstractSyntax_InfixExpression_Expression, gen_JavaAbstractSyntax_MethodInvocation_Expression, gen_JavaAbstractSyntax_InstanceofExpression_Expression, gen_JavaAbstractSyntax_PostfixExpression_Expression, gen_JavaAbstractSyntax_Name_Expression, gen_JavaAbstractSyntax_NullLiteral_Expression, gen_JavaAbstractSyntax_NumberLiteral_Expression, gen_JavaAbstractSyntax_ParenthesizedExpression_Expression, gen_JavaAbstractSyntax_SuperMethodInvocation_Expression, gen_JavaAbstractSyntax_PrefixExpression_Expression, gen_JavaAbstractSyntax_StringLiteral_Expression, gen_JavaAbstractSyntax_SuperFieldAccess_Expression, gen_JavaAbstractSyntax_AssertStatement_Statement, gen_JavaAbstractSyntax_ThisExpression_Expression, gen_JavaAbstractSyntax_TypeLiteral_Expression, gen_JavaAbstractSyntax_VariableDeclarationExpression_Expression, gen_JavaAbstractSyntax_Block_Statement, gen_JavaAbstractSyntax_BreakStatement_Statement, gen_JavaAbstractSyntax_ConstructorInvocation_Statement, gen_JavaAbstractSyntax_ContinueStatement_Statement, gen_JavaAbstractSyntax_DoStatement_Statement, gen_JavaAbstractSyntax_EmptyStatement_Statement, gen_JavaAbstractSyntax_EnhancedForStatement_Statement, gen_JavaAbstractSyntax_ExpressionStatement_Statement, gen_JavaAbstractSyntax_ForStatement_Statement, gen_JavaAbstractSyntax_IfStatement_Statement, gen_JavaAbstractSyntax_LabeledStatement_Statement, gen_JavaAbstractSyntax_ReturnStatement_Statement, gen_JavaAbstractSyntax_SuperConstructorInvocation_Statement, gen_JavaAbstractSyntax_TryStatement_Statement, gen_JavaAbstractSyntax_SwitchCase_Statement, gen_JavaAbstractSyntax_SwitchStatement_Statement, gen_JavaAbstractSyntax_SynchronizedStatement_Statement, gen_JavaAbstractSyntax_ThrowStatement_Statement, gen_JavaAbstractSyntax_ParameterizedType_Type, gen_JavaAbstractSyntax_TypeDeclarationStatement_Statement, gen_JavaAbstractSyntax_VariableDeclarationStatement_Statement, gen_JavaAbstractSyntax_WhileStatement_Statement, gen_JavaAbstractSyntax_ArrayType_Type, gen_JavaAbstractSyntax_VariableDeclarationFragment_VariableDeclaration, gen_JavaAbstractSyntax_QualifiedName_Name, gen_JavaAbstractSyntax_PrimitiveType_Type, gen_JavaAbstractSyntax_QualifiedType_Type, gen_JavaAbstractSyntax_SimpleType_Type, gen_JavaAbstractSyntax_WildcardType_Type, gen_JavaAbstractSyntax_SingleVariableDeclaration_VariableDeclaration, gen_JavaAbstractSyntax_SimpleName_Name, gen_JavaAbstractSyntax_MarkerAnnotation_Annotation, gen_JavaAbstractSyntax_NormalAnnotation_Annotation, gen_JavaAbstractSyntax_SingleMemberAnnotation_Annotation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)