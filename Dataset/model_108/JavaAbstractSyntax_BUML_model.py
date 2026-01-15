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
            EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="CONDITIONAL_OR"),
			EnumerationLiteral(name="REMAINDER"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="RIGHT_SHIFT_SIGNED"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="LESS_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
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
BodyDeclaration = Class(name="BodyDeclaration")
JavaAbstractSyntax_BodyDeclaration = Class(name="JavaAbstractSyntax::BodyDeclaration", is_abstract=True)
ExtendedModifier = Class(name="ExtendedModifier")
JavaAbstractSyntax_AST = Class(name="JavaAbstractSyntax::AST")
ASTNode = Class(name="ASTNode")
JavaAbstractSyntax_ASTNode = Class(name="JavaAbstractSyntax::ASTNode", is_abstract=True)
JavaAbstractSyntax_AnonymousClassDeclaration = Class(name="JavaAbstractSyntax::AnonymousClassDeclaration")
JavaAbstractSyntax_MemberValuePair = Class(name="JavaAbstractSyntax::MemberValuePair")
Expression = Class(name="Expression")
Javadoc = Class(name="Javadoc")
JavaAbstractSyntax_CatchClause = Class(name="JavaAbstractSyntax::CatchClause")
Block = Class(name="Block")
SingleVariableDeclaration = Class(name="SingleVariableDeclaration")
JavaAbstractSyntax_Comment = Class(name="JavaAbstractSyntax::Comment", is_abstract=True)
JavaAbstractSyntax_CompilationUnit = Class(name="JavaAbstractSyntax::CompilationUnit")
Comment = Class(name="Comment")
PackageDeclaration = Class(name="PackageDeclaration")
ImportDeclaration = Class(name="ImportDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
JavaAbstractSyntax_Expression = Class(name="JavaAbstractSyntax::Expression", is_abstract=True)
JavaAbstractSyntax_ImportDeclaration = Class(name="JavaAbstractSyntax::ImportDeclaration")
Name = Class(name="Name")
JavaAbstractSyntax_MemberRef = Class(name="JavaAbstractSyntax::MemberRef")
SimpleName = Class(name="SimpleName")
JavaAbstractSyntax_Statement = Class(name="JavaAbstractSyntax::Statement", is_abstract=True)
JavaAbstractSyntax_TagElement = Class(name="JavaAbstractSyntax::TagElement")
JavaAbstractSyntax_MethodRef = Class(name="JavaAbstractSyntax::MethodRef")
MethodRefParameter = Class(name="MethodRefParameter")
JavaAbstractSyntax_MethodRefParameter = Class(name="JavaAbstractSyntax::MethodRefParameter")
Type = Class(name="Type")
JavaAbstractSyntax_ExtendedModifier = Class(name="JavaAbstractSyntax::ExtendedModifier", is_abstract=True)
JavaAbstractSyntax_Modifier = Class(name="JavaAbstractSyntax::Modifier")
JavaAbstractSyntax_PackageDeclaration = Class(name="JavaAbstractSyntax::PackageDeclaration")
Annotation = Class(name="Annotation")
JavaAbstractSyntax_TextElement = Class(name="JavaAbstractSyntax::TextElement")
JavaAbstractSyntax_Type = Class(name="JavaAbstractSyntax::Type", is_abstract=True)
JavaAbstractSyntax_TypeParameter = Class(name="JavaAbstractSyntax::TypeParameter")
JavaAbstractSyntax_VariableDeclaration = Class(name="JavaAbstractSyntax::VariableDeclaration", is_abstract=True)
JavaAbstractSyntax_AbstractTypeDeclaration = Class(name="JavaAbstractSyntax::AbstractTypeDeclaration", is_abstract=True)
JavaAbstractSyntax_AnnotationTypeMemberDeclaration = Class(name="JavaAbstractSyntax::AnnotationTypeMemberDeclaration")
JavaAbstractSyntax_EnumConstantDeclaration = Class(name="JavaAbstractSyntax::EnumConstantDeclaration")
AnonymousClassDeclaration = Class(name="AnonymousClassDeclaration")
JavaAbstractSyntax_FieldDeclaration = Class(name="JavaAbstractSyntax::FieldDeclaration")
VariableDeclarationFragment = Class(name="VariableDeclarationFragment")
JavaAbstractSyntax_Initializer = Class(name="JavaAbstractSyntax::Initializer")
JavaAbstractSyntax_MethodDeclaration = Class(name="JavaAbstractSyntax::MethodDeclaration")
JavaAbstractSyntax_BlockComment = Class(name="JavaAbstractSyntax::BlockComment")
JavaAbstractSyntax_Javadoc = Class(name="JavaAbstractSyntax::Javadoc")
TagElement = Class(name="TagElement")
TypeParameter = Class(name="TypeParameter")
JavaAbstractSyntax_AnnotationTypeDeclaration = Class(name="JavaAbstractSyntax::AnnotationTypeDeclaration")
JavaAbstractSyntax_EnumDeclaration = Class(name="JavaAbstractSyntax::EnumDeclaration")
EnumConstantDeclaration = Class(name="EnumConstantDeclaration")
JavaAbstractSyntax_TypeDeclaration = Class(name="JavaAbstractSyntax::TypeDeclaration")
JavaAbstractSyntax_LineComment = Class(name="JavaAbstractSyntax::LineComment")
JavaAbstractSyntax_Annotation = Class(name="JavaAbstractSyntax::Annotation", is_abstract=True)
JavaAbstractSyntax_ArrayAccess = Class(name="JavaAbstractSyntax::ArrayAccess")
JavaAbstractSyntax_ArrayCreation = Class(name="JavaAbstractSyntax::ArrayCreation")
ArrayInitializer = Class(name="ArrayInitializer")
ArrayType = Class(name="ArrayType")
JavaAbstractSyntax_ArrayInitializer = Class(name="JavaAbstractSyntax::ArrayInitializer")
JavaAbstractSyntax_Assignment = Class(name="JavaAbstractSyntax::Assignment")
JavaAbstractSyntax_BooleanLiteral = Class(name="JavaAbstractSyntax::BooleanLiteral")
JavaAbstractSyntax_CastExpression = Class(name="JavaAbstractSyntax::CastExpression")
JavaAbstractSyntax_CharacterLiteral = Class(name="JavaAbstractSyntax::CharacterLiteral")
JavaAbstractSyntax_FieldAccess = Class(name="JavaAbstractSyntax::FieldAccess")
JavaAbstractSyntax_ClassInstanceCreation = Class(name="JavaAbstractSyntax::ClassInstanceCreation")
JavaAbstractSyntax_ConditionalExpression = Class(name="JavaAbstractSyntax::ConditionalExpression")
JavaAbstractSyntax_InfixExpression = Class(name="JavaAbstractSyntax::InfixExpression")
JavaAbstractSyntax_InstanceofExpression = Class(name="JavaAbstractSyntax::InstanceofExpression")
JavaAbstractSyntax_MethodInvocation = Class(name="JavaAbstractSyntax::MethodInvocation")
JavaAbstractSyntax_PrefixExpression = Class(name="JavaAbstractSyntax::PrefixExpression")
JavaAbstractSyntax_Name = Class(name="JavaAbstractSyntax::Name", is_abstract=True)
JavaAbstractSyntax_NullLiteral = Class(name="JavaAbstractSyntax::NullLiteral")
JavaAbstractSyntax_NumberLiteral = Class(name="JavaAbstractSyntax::NumberLiteral")
JavaAbstractSyntax_ParenthesizedExpression = Class(name="JavaAbstractSyntax::ParenthesizedExpression")
JavaAbstractSyntax_PostfixExpression = Class(name="JavaAbstractSyntax::PostfixExpression")
JavaAbstractSyntax_StringLiteral = Class(name="JavaAbstractSyntax::StringLiteral")
JavaAbstractSyntax_SuperFieldAccess = Class(name="JavaAbstractSyntax::SuperFieldAccess")
JavaAbstractSyntax_SuperMethodInvocation = Class(name="JavaAbstractSyntax::SuperMethodInvocation")
JavaAbstractSyntax_TypeLiteral = Class(name="JavaAbstractSyntax::TypeLiteral")
JavaAbstractSyntax_ThisExpression = Class(name="JavaAbstractSyntax::ThisExpression")
JavaAbstractSyntax_VariableDeclarationExpression = Class(name="JavaAbstractSyntax::VariableDeclarationExpression")
JavaAbstractSyntax_AssertStatement = Class(name="JavaAbstractSyntax::AssertStatement")
Statement = Class(name="Statement")
JavaAbstractSyntax_ContinueStatement = Class(name="JavaAbstractSyntax::ContinueStatement")
JavaAbstractSyntax_DoStatement = Class(name="JavaAbstractSyntax::DoStatement")
JavaAbstractSyntax_Block = Class(name="JavaAbstractSyntax::Block")
JavaAbstractSyntax_EmptyStatement = Class(name="JavaAbstractSyntax::EmptyStatement")
JavaAbstractSyntax_EnhancedForStatement = Class(name="JavaAbstractSyntax::EnhancedForStatement")
JavaAbstractSyntax_BreakStatement = Class(name="JavaAbstractSyntax::BreakStatement")
JavaAbstractSyntax_ConstructorInvocation = Class(name="JavaAbstractSyntax::ConstructorInvocation")
JavaAbstractSyntax_ForStatement = Class(name="JavaAbstractSyntax::ForStatement")
JavaAbstractSyntax_ExpressionStatement = Class(name="JavaAbstractSyntax::ExpressionStatement")
JavaAbstractSyntax_IfStatement = Class(name="JavaAbstractSyntax::IfStatement")
JavaAbstractSyntax_LabeledStatement = Class(name="JavaAbstractSyntax::LabeledStatement")
JavaAbstractSyntax_ReturnStatement = Class(name="JavaAbstractSyntax::ReturnStatement")
JavaAbstractSyntax_SuperConstructorInvocation = Class(name="JavaAbstractSyntax::SuperConstructorInvocation")
JavaAbstractSyntax_SwitchCase = Class(name="JavaAbstractSyntax::SwitchCase")
JavaAbstractSyntax_SwitchStatement = Class(name="JavaAbstractSyntax::SwitchStatement")
JavaAbstractSyntax_SynchronizedStatement = Class(name="JavaAbstractSyntax::SynchronizedStatement")
JavaAbstractSyntax_ThrowStatement = Class(name="JavaAbstractSyntax::ThrowStatement")
JavaAbstractSyntax_TryStatement = Class(name="JavaAbstractSyntax::TryStatement")
CatchClause = Class(name="CatchClause")
JavaAbstractSyntax_TypeDeclarationStatement = Class(name="JavaAbstractSyntax::TypeDeclarationStatement")
JavaAbstractSyntax_VariableDeclarationStatement = Class(name="JavaAbstractSyntax::VariableDeclarationStatement")
JavaAbstractSyntax_WhileStatement = Class(name="JavaAbstractSyntax::WhileStatement")
JavaAbstractSyntax_ArrayType = Class(name="JavaAbstractSyntax::ArrayType")
JavaAbstractSyntax_ParameterizedType = Class(name="JavaAbstractSyntax::ParameterizedType")
JavaAbstractSyntax_PrimitiveType = Class(name="JavaAbstractSyntax::PrimitiveType")
JavaAbstractSyntax_QualifiedType = Class(name="JavaAbstractSyntax::QualifiedType")
JavaAbstractSyntax_SimpleType = Class(name="JavaAbstractSyntax::SimpleType")
JavaAbstractSyntax_WildcardType = Class(name="JavaAbstractSyntax::WildcardType")
JavaAbstractSyntax_SingleVariableDeclaration = Class(name="JavaAbstractSyntax::SingleVariableDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
JavaAbstractSyntax_VariableDeclarationFragment = Class(name="JavaAbstractSyntax::VariableDeclarationFragment")
JavaAbstractSyntax_QualifiedName = Class(name="JavaAbstractSyntax::QualifiedName")
JavaAbstractSyntax_SimpleName = Class(name="JavaAbstractSyntax::SimpleName")
JavaAbstractSyntax_MarkerAnnotation = Class(name="JavaAbstractSyntax::MarkerAnnotation")
JavaAbstractSyntax_NormalAnnotation = Class(name="JavaAbstractSyntax::NormalAnnotation")
MemberValuePair = Class(name="MemberValuePair")
JavaAbstractSyntax_SingleMemberAnnotation = Class(name="JavaAbstractSyntax::SingleMemberAnnotation")
JavaAbstractSyntax_StructuralPackage = Class(name="JavaAbstractSyntax::StructuralPackage")
StructuralPackage = Class(name="StructuralPackage")
CompilationUnit = Class(name="CompilationUnit")

# BodyDeclaration class attributes and methods

# JavaAbstractSyntax_BodyDeclaration class attributes and methods

# ExtendedModifier class attributes and methods

# JavaAbstractSyntax_AST class attributes and methods

# ASTNode class attributes and methods

# JavaAbstractSyntax_ASTNode class attributes and methods

# JavaAbstractSyntax_AnonymousClassDeclaration class attributes and methods

# JavaAbstractSyntax_MemberValuePair class attributes and methods

# Expression class attributes and methods

# Javadoc class attributes and methods

# JavaAbstractSyntax_CatchClause class attributes and methods

# Block class attributes and methods

# SingleVariableDeclaration class attributes and methods

# JavaAbstractSyntax_Comment class attributes and methods

# JavaAbstractSyntax_CompilationUnit class attributes and methods

# Comment class attributes and methods

# PackageDeclaration class attributes and methods

# ImportDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# JavaAbstractSyntax_Expression class attributes and methods
JavaAbstractSyntax_Expression_resolveBoxing: Property = Property(name="resolveBoxing", type=StringType)
JavaAbstractSyntax_Expression_resolveUnboxing: Property = Property(name="resolveUnboxing", type=StringType)
JavaAbstractSyntax_Expression.attributes={JavaAbstractSyntax_Expression_resolveBoxing, JavaAbstractSyntax_Expression_resolveUnboxing}

# JavaAbstractSyntax_ImportDeclaration class attributes and methods
JavaAbstractSyntax_ImportDeclaration_onDemand: Property = Property(name="onDemand", type=StringType)
JavaAbstractSyntax_ImportDeclaration_static: Property = Property(name="static", type=StringType)
JavaAbstractSyntax_ImportDeclaration.attributes={JavaAbstractSyntax_ImportDeclaration_onDemand, JavaAbstractSyntax_ImportDeclaration_static}

# Name class attributes and methods

# JavaAbstractSyntax_MemberRef class attributes and methods

# SimpleName class attributes and methods

# JavaAbstractSyntax_Statement class attributes and methods

# JavaAbstractSyntax_TagElement class attributes and methods
JavaAbstractSyntax_TagElement_tagName: Property = Property(name="tagName", type=StringType)
JavaAbstractSyntax_TagElement_nested: Property = Property(name="nested", type=StringType)
JavaAbstractSyntax_TagElement.attributes={JavaAbstractSyntax_TagElement_nested, JavaAbstractSyntax_TagElement_tagName}

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
JavaAbstractSyntax_Modifier.attributes={JavaAbstractSyntax_Modifier_strictfp, JavaAbstractSyntax_Modifier_static, JavaAbstractSyntax_Modifier_synchronized, JavaAbstractSyntax_Modifier_protected, JavaAbstractSyntax_Modifier_transient, JavaAbstractSyntax_Modifier_private, JavaAbstractSyntax_Modifier_volatile, JavaAbstractSyntax_Modifier_none, JavaAbstractSyntax_Modifier_abstract, JavaAbstractSyntax_Modifier_native, JavaAbstractSyntax_Modifier_public, JavaAbstractSyntax_Modifier_final}

# JavaAbstractSyntax_PackageDeclaration class attributes and methods

# Annotation class attributes and methods

# JavaAbstractSyntax_TextElement class attributes and methods
JavaAbstractSyntax_TextElement_text: Property = Property(name="text", type=StringType)
JavaAbstractSyntax_TextElement.attributes={JavaAbstractSyntax_TextElement_text}

# JavaAbstractSyntax_Type class attributes and methods

# JavaAbstractSyntax_TypeParameter class attributes and methods

# JavaAbstractSyntax_VariableDeclaration class attributes and methods
JavaAbstractSyntax_VariableDeclaration_extraDimensions: Property = Property(name="extraDimensions", type=StringType)
JavaAbstractSyntax_VariableDeclaration.attributes={JavaAbstractSyntax_VariableDeclaration_extraDimensions}

# JavaAbstractSyntax_AbstractTypeDeclaration class attributes and methods
JavaAbstractSyntax_AbstractTypeDeclaration_localTypeDeclaration: Property = Property(name="localTypeDeclaration", type=StringType)
JavaAbstractSyntax_AbstractTypeDeclaration_memberTypeDeclaration: Property = Property(name="memberTypeDeclaration", type=StringType)
JavaAbstractSyntax_AbstractTypeDeclaration_packageMemberTypeDeclaration: Property = Property(name="packageMemberTypeDeclaration", type=StringType)
JavaAbstractSyntax_AbstractTypeDeclaration.attributes={JavaAbstractSyntax_AbstractTypeDeclaration_localTypeDeclaration, JavaAbstractSyntax_AbstractTypeDeclaration_packageMemberTypeDeclaration, JavaAbstractSyntax_AbstractTypeDeclaration_memberTypeDeclaration}

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
JavaAbstractSyntax_MethodDeclaration.attributes={JavaAbstractSyntax_MethodDeclaration_varargs, JavaAbstractSyntax_MethodDeclaration_extraDimensions, JavaAbstractSyntax_MethodDeclaration_constructor}

# JavaAbstractSyntax_BlockComment class attributes and methods

# JavaAbstractSyntax_Javadoc class attributes and methods

# TagElement class attributes and methods

# TypeParameter class attributes and methods

# JavaAbstractSyntax_AnnotationTypeDeclaration class attributes and methods

# JavaAbstractSyntax_EnumDeclaration class attributes and methods

# EnumConstantDeclaration class attributes and methods

# JavaAbstractSyntax_TypeDeclaration class attributes and methods
JavaAbstractSyntax_TypeDeclaration_interface: Property = Property(name="interface", type=StringType)
JavaAbstractSyntax_TypeDeclaration.attributes={JavaAbstractSyntax_TypeDeclaration_interface}

# JavaAbstractSyntax_LineComment class attributes and methods

# JavaAbstractSyntax_Annotation class attributes and methods

# JavaAbstractSyntax_ArrayAccess class attributes and methods

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

# JavaAbstractSyntax_FieldAccess class attributes and methods

# JavaAbstractSyntax_ClassInstanceCreation class attributes and methods

# JavaAbstractSyntax_ConditionalExpression class attributes and methods

# JavaAbstractSyntax_InfixExpression class attributes and methods
JavaAbstractSyntax_InfixExpression_operator: Property = Property(name="operator", type=StringType)
JavaAbstractSyntax_InfixExpression.attributes={JavaAbstractSyntax_InfixExpression_operator}

# JavaAbstractSyntax_InstanceofExpression class attributes and methods

# JavaAbstractSyntax_MethodInvocation class attributes and methods

# JavaAbstractSyntax_PrefixExpression class attributes and methods
JavaAbstractSyntax_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
JavaAbstractSyntax_PrefixExpression.attributes={JavaAbstractSyntax_PrefixExpression_operator}

# JavaAbstractSyntax_Name class attributes and methods
JavaAbstractSyntax_Name_fullyQualifiedName: Property = Property(name="fullyQualifiedName", type=StringType)
JavaAbstractSyntax_Name.attributes={JavaAbstractSyntax_Name_fullyQualifiedName}

# JavaAbstractSyntax_NullLiteral class attributes and methods

# JavaAbstractSyntax_NumberLiteral class attributes and methods
JavaAbstractSyntax_NumberLiteral_token: Property = Property(name="token", type=StringType)
JavaAbstractSyntax_NumberLiteral.attributes={JavaAbstractSyntax_NumberLiteral_token}

# JavaAbstractSyntax_ParenthesizedExpression class attributes and methods

# JavaAbstractSyntax_PostfixExpression class attributes and methods
JavaAbstractSyntax_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
JavaAbstractSyntax_PostfixExpression.attributes={JavaAbstractSyntax_PostfixExpression_operator}

# JavaAbstractSyntax_StringLiteral class attributes and methods
JavaAbstractSyntax_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
JavaAbstractSyntax_StringLiteral_literalValue: Property = Property(name="literalValue", type=StringType)
JavaAbstractSyntax_StringLiteral.attributes={JavaAbstractSyntax_StringLiteral_escapedValue, JavaAbstractSyntax_StringLiteral_literalValue}

# JavaAbstractSyntax_SuperFieldAccess class attributes and methods

# JavaAbstractSyntax_SuperMethodInvocation class attributes and methods

# JavaAbstractSyntax_TypeLiteral class attributes and methods

# JavaAbstractSyntax_ThisExpression class attributes and methods

# JavaAbstractSyntax_VariableDeclarationExpression class attributes and methods

# JavaAbstractSyntax_AssertStatement class attributes and methods

# Statement class attributes and methods

# JavaAbstractSyntax_ContinueStatement class attributes and methods

# JavaAbstractSyntax_DoStatement class attributes and methods

# JavaAbstractSyntax_Block class attributes and methods

# JavaAbstractSyntax_EmptyStatement class attributes and methods

# JavaAbstractSyntax_EnhancedForStatement class attributes and methods

# JavaAbstractSyntax_BreakStatement class attributes and methods

# JavaAbstractSyntax_ConstructorInvocation class attributes and methods

# JavaAbstractSyntax_ForStatement class attributes and methods

# JavaAbstractSyntax_ExpressionStatement class attributes and methods

# JavaAbstractSyntax_IfStatement class attributes and methods

# JavaAbstractSyntax_LabeledStatement class attributes and methods

# JavaAbstractSyntax_ReturnStatement class attributes and methods

# JavaAbstractSyntax_SuperConstructorInvocation class attributes and methods

# JavaAbstractSyntax_SwitchCase class attributes and methods
JavaAbstractSyntax_SwitchCase_default: Property = Property(name="default", type=StringType)
JavaAbstractSyntax_SwitchCase.attributes={JavaAbstractSyntax_SwitchCase_default}

# JavaAbstractSyntax_SwitchStatement class attributes and methods

# JavaAbstractSyntax_SynchronizedStatement class attributes and methods

# JavaAbstractSyntax_ThrowStatement class attributes and methods

# JavaAbstractSyntax_TryStatement class attributes and methods

# CatchClause class attributes and methods

# JavaAbstractSyntax_TypeDeclarationStatement class attributes and methods

# JavaAbstractSyntax_VariableDeclarationStatement class attributes and methods

# JavaAbstractSyntax_WhileStatement class attributes and methods

# JavaAbstractSyntax_ArrayType class attributes and methods
JavaAbstractSyntax_ArrayType_dimensions: Property = Property(name="dimensions", type=StringType)
JavaAbstractSyntax_ArrayType.attributes={JavaAbstractSyntax_ArrayType_dimensions}

# JavaAbstractSyntax_ParameterizedType class attributes and methods

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

# JavaAbstractSyntax_VariableDeclarationFragment class attributes and methods

# JavaAbstractSyntax_QualifiedName class attributes and methods

# JavaAbstractSyntax_SimpleName class attributes and methods
JavaAbstractSyntax_SimpleName_identifier: Property = Property(name="identifier", type=StringType)
JavaAbstractSyntax_SimpleName_declaration: Property = Property(name="declaration", type=StringType)
JavaAbstractSyntax_SimpleName.attributes={JavaAbstractSyntax_SimpleName_declaration, JavaAbstractSyntax_SimpleName_identifier}

# JavaAbstractSyntax_MarkerAnnotation class attributes and methods

# JavaAbstractSyntax_NormalAnnotation class attributes and methods

# MemberValuePair class attributes and methods

# JavaAbstractSyntax_SingleMemberAnnotation class attributes and methods

# JavaAbstractSyntax_StructuralPackage class attributes and methods
JavaAbstractSyntax_StructuralPackage_name: Property = Property(name="name", type=StringType)
JavaAbstractSyntax_StructuralPackage.attributes={JavaAbstractSyntax_StructuralPackage_name}

# StructuralPackage class attributes and methods

# CompilationUnit class attributes and methods

# Relationships
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
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="ASTNode", type=JavaAbstractSyntax_AST, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AST", type=ASTNode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name22: BinaryAssociation = BinaryAssociation(
    name="name22",
    ends={
        Property(name="SimpleName23", type=JavaAbstractSyntax_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MemberValuePair", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
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
name17: BinaryAssociation = BinaryAssociation(
    name="name17",
    ends={
        Property(name="Name", type=JavaAbstractSyntax_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ImportDeclaration", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name18: BinaryAssociation = BinaryAssociation(
    name="name18",
    ends={
        Property(name="SimpleName", type=JavaAbstractSyntax_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MemberRef", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier19: BinaryAssociation = BinaryAssociation(
    name="qualifier19",
    ends={
        Property(name="Name21", type=JavaAbstractSyntax_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MemberRef20", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments44: BinaryAssociation = BinaryAssociation(
    name="fragments44",
    ends={
        Property(name="ASTNode45", type=JavaAbstractSyntax_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TagElement", type=ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
default61: BinaryAssociation = BinaryAssociation(
    name="default61",
    ends={
        Property(name="Expression62", type=JavaAbstractSyntax_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AnnotationTypeMemberDeclaration", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
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
tags113: BinaryAssociation = BinaryAssociation(
    name="tags113",
    ends={
        Property(name="TagElement", type=JavaAbstractSyntax_Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Javadoc", type=TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
constants102: BinaryAssociation = BinaryAssociation(
    name="constants102",
    ends={
        Property(name="EnumConstantDeclaration104", type=JavaAbstractSyntax_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnumDeclaration103", type=EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclassType105: BinaryAssociation = BinaryAssociation(
    name="superclassType105",
    ends={
        Property(name="Type106", type=JavaAbstractSyntax_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeDeclaration", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superInterfaceTypes107: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes107",
    ends={
        Property(name="Type109", type=JavaAbstractSyntax_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeDeclaration108", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters110: BinaryAssociation = BinaryAssociation(
    name="typeParameters110",
    ends={
        Property(name="TypeParameter112", type=JavaAbstractSyntax_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeDeclaration111", type=TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftHandSide129: BinaryAssociation = BinaryAssociation(
    name="leftHandSide129",
    ends={
        Property(name="Expression130", type=JavaAbstractSyntax_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Assignment", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeName114: BinaryAssociation = BinaryAssociation(
    name="typeName114",
    ends={
        Property(name="Name115", type=JavaAbstractSyntax_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Annotation", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array116: BinaryAssociation = BinaryAssociation(
    name="array116",
    ends={
        Property(name="Expression117", type=JavaAbstractSyntax_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayAccess", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index118: BinaryAssociation = BinaryAssociation(
    name="index118",
    ends={
        Property(name="Expression120", type=JavaAbstractSyntax_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayAccess119", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions121: BinaryAssociation = BinaryAssociation(
    name="dimensions121",
    ends={
        Property(name="Expression122", type=JavaAbstractSyntax_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayCreation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer123: BinaryAssociation = BinaryAssociation(
    name="initializer123",
    ends={
        Property(name="ArrayInitializer", type=JavaAbstractSyntax_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayCreation124", type=ArrayInitializer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type125: BinaryAssociation = BinaryAssociation(
    name="type125",
    ends={
        Property(name="ArrayType", type=JavaAbstractSyntax_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayCreation126", type=ArrayType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions127: BinaryAssociation = BinaryAssociation(
    name="expressions127",
    ends={
        Property(name="Expression128", type=JavaAbstractSyntax_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayInitializer", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightHandSide131: BinaryAssociation = BinaryAssociation(
    name="rightHandSide131",
    ends={
        Property(name="Expression133", type=JavaAbstractSyntax_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Assignment132", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression134: BinaryAssociation = BinaryAssociation(
    name="expression134",
    ends={
        Property(name="Expression135", type=JavaAbstractSyntax_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_CastExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type136: BinaryAssociation = BinaryAssociation(
    name="type136",
    ends={
        Property(name="Type138", type=JavaAbstractSyntax_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_CastExpression137", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments139: BinaryAssociation = BinaryAssociation(
    name="arguments139",
    ends={
        Property(name="Expression140", type=JavaAbstractSyntax_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ClassInstanceCreation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration141: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration141",
    ends={
        Property(name="AnonymousClassDeclaration143", type=JavaAbstractSyntax_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ClassInstanceCreation142", type=AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression144: BinaryAssociation = BinaryAssociation(
    name="expression144",
    ends={
        Property(name="Expression146", type=JavaAbstractSyntax_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ClassInstanceCreation145", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type147: BinaryAssociation = BinaryAssociation(
    name="type147",
    ends={
        Property(name="Type149", type=JavaAbstractSyntax_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ClassInstanceCreation148", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments150: BinaryAssociation = BinaryAssociation(
    name="typeArguments150",
    ends={
        Property(name="Type152", type=JavaAbstractSyntax_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ClassInstanceCreation151", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseExpression153: BinaryAssociation = BinaryAssociation(
    name="elseExpression153",
    ends={
        Property(name="Expression154", type=JavaAbstractSyntax_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ConditionalExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression155: BinaryAssociation = BinaryAssociation(
    name="expression155",
    ends={
        Property(name="Expression157", type=JavaAbstractSyntax_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ConditionalExpression156", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression158: BinaryAssociation = BinaryAssociation(
    name="thenExpression158",
    ends={
        Property(name="Expression160", type=JavaAbstractSyntax_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ConditionalExpression159", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression161: BinaryAssociation = BinaryAssociation(
    name="expression161",
    ends={
        Property(name="Expression162", type=JavaAbstractSyntax_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_FieldAccess", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name163: BinaryAssociation = BinaryAssociation(
    name="name163",
    ends={
        Property(name="SimpleName165", type=JavaAbstractSyntax_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_FieldAccess164", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands166: BinaryAssociation = BinaryAssociation(
    name="extendedOperands166",
    ends={
        Property(name="Expression167", type=JavaAbstractSyntax_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_InfixExpression", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand168: BinaryAssociation = BinaryAssociation(
    name="leftOperand168",
    ends={
        Property(name="Expression170", type=JavaAbstractSyntax_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_InfixExpression169", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand171: BinaryAssociation = BinaryAssociation(
    name="rightOperand171",
    ends={
        Property(name="Expression173", type=JavaAbstractSyntax_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_InfixExpression172", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments187: BinaryAssociation = BinaryAssociation(
    name="typeArguments187",
    ends={
        Property(name="Type189", type=JavaAbstractSyntax_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodInvocation188", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand174: BinaryAssociation = BinaryAssociation(
    name="leftOperand174",
    ends={
        Property(name="Expression175", type=JavaAbstractSyntax_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_InstanceofExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand176: BinaryAssociation = BinaryAssociation(
    name="rightOperand176",
    ends={
        Property(name="Type178", type=JavaAbstractSyntax_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_InstanceofExpression177", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments179: BinaryAssociation = BinaryAssociation(
    name="arguments179",
    ends={
        Property(name="Expression180", type=JavaAbstractSyntax_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression181: BinaryAssociation = BinaryAssociation(
    name="expression181",
    ends={
        Property(name="Expression183", type=JavaAbstractSyntax_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodInvocation182", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name184: BinaryAssociation = BinaryAssociation(
    name="name184",
    ends={
        Property(name="SimpleName186", type=JavaAbstractSyntax_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_MethodInvocation185", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand194: BinaryAssociation = BinaryAssociation(
    name="operand194",
    ends={
        Property(name="Expression195", type=JavaAbstractSyntax_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_PrefixExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression190: BinaryAssociation = BinaryAssociation(
    name="expression190",
    ends={
        Property(name="Expression191", type=JavaAbstractSyntax_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ParenthesizedExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand192: BinaryAssociation = BinaryAssociation(
    name="operand192",
    ends={
        Property(name="Expression193", type=JavaAbstractSyntax_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_PostfixExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name196: BinaryAssociation = BinaryAssociation(
    name="name196",
    ends={
        Property(name="SimpleName197", type=JavaAbstractSyntax_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperFieldAccess", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier198: BinaryAssociation = BinaryAssociation(
    name="qualifier198",
    ends={
        Property(name="Name200", type=JavaAbstractSyntax_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperFieldAccess199", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments201: BinaryAssociation = BinaryAssociation(
    name="arguments201",
    ends={
        Property(name="Expression202", type=JavaAbstractSyntax_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperMethodInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier212: BinaryAssociation = BinaryAssociation(
    name="qualifier212",
    ends={
        Property(name="Name213", type=JavaAbstractSyntax_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ThisExpression", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name203: BinaryAssociation = BinaryAssociation(
    name="name203",
    ends={
        Property(name="Name205", type=JavaAbstractSyntax_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperMethodInvocation204", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier206: BinaryAssociation = BinaryAssociation(
    name="qualifier206",
    ends={
        Property(name="Name208", type=JavaAbstractSyntax_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperMethodInvocation207", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments209: BinaryAssociation = BinaryAssociation(
    name="typeArguments209",
    ends={
        Property(name="Type211", type=JavaAbstractSyntax_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperMethodInvocation210", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression224: BinaryAssociation = BinaryAssociation(
    name="expression224",
    ends={
        Property(name="Expression225", type=JavaAbstractSyntax_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AssertStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type214: BinaryAssociation = BinaryAssociation(
    name="type214",
    ends={
        Property(name="Type215", type=JavaAbstractSyntax_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeLiteral", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments216: BinaryAssociation = BinaryAssociation(
    name="fragments216",
    ends={
        Property(name="VariableDeclarationFragment217", type=JavaAbstractSyntax_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationExpression", type=VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers218: BinaryAssociation = BinaryAssociation(
    name="modifiers218",
    ends={
        Property(name="ExtendedModifier220", type=JavaAbstractSyntax_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationExpression219", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type221: BinaryAssociation = BinaryAssociation(
    name="type221",
    ends={
        Property(name="Type223", type=JavaAbstractSyntax_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationExpression222", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments234: BinaryAssociation = BinaryAssociation(
    name="typeArguments234",
    ends={
        Property(name="Type236", type=JavaAbstractSyntax_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ConstructorInvocation235", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label237: BinaryAssociation = BinaryAssociation(
    name="label237",
    ends={
        Property(name="SimpleName238", type=JavaAbstractSyntax_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ContinueStatement", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message226: BinaryAssociation = BinaryAssociation(
    name="message226",
    ends={
        Property(name="Expression228", type=JavaAbstractSyntax_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_AssertStatement227", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body239: BinaryAssociation = BinaryAssociation(
    name="body239",
    ends={
        Property(name="Statement240", type=JavaAbstractSyntax_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_DoStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression241: BinaryAssociation = BinaryAssociation(
    name="expression241",
    ends={
        Property(name="Expression243", type=JavaAbstractSyntax_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_DoStatement242", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements229: BinaryAssociation = BinaryAssociation(
    name="statements229",
    ends={
        Property(name="Statement", type=JavaAbstractSyntax_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_Block", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label230: BinaryAssociation = BinaryAssociation(
    name="label230",
    ends={
        Property(name="SimpleName231", type=JavaAbstractSyntax_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_BreakStatement", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments232: BinaryAssociation = BinaryAssociation(
    name="arguments232",
    ends={
        Property(name="Expression233", type=JavaAbstractSyntax_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ConstructorInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression246: BinaryAssociation = BinaryAssociation(
    name="expression246",
    ends={
        Property(name="Expression248", type=JavaAbstractSyntax_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnhancedForStatement247", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body254: BinaryAssociation = BinaryAssociation(
    name="body254",
    ends={
        Property(name="Statement255", type=JavaAbstractSyntax_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ForStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body244: BinaryAssociation = BinaryAssociation(
    name="body244",
    ends={
        Property(name="Statement245", type=JavaAbstractSyntax_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnhancedForStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression256: BinaryAssociation = BinaryAssociation(
    name="expression256",
    ends={
        Property(name="Expression258", type=JavaAbstractSyntax_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ForStatement257", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter249: BinaryAssociation = BinaryAssociation(
    name="parameter249",
    ends={
        Property(name="SingleVariableDeclaration251", type=JavaAbstractSyntax_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_EnhancedForStatement250", type=SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression252: BinaryAssociation = BinaryAssociation(
    name="expression252",
    ends={
        Property(name="Expression253", type=JavaAbstractSyntax_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement265: BinaryAssociation = BinaryAssociation(
    name="elseStatement265",
    ends={
        Property(name="Statement266", type=JavaAbstractSyntax_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_IfStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression267: BinaryAssociation = BinaryAssociation(
    name="expression267",
    ends={
        Property(name="Expression269", type=JavaAbstractSyntax_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_IfStatement268", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializers259: BinaryAssociation = BinaryAssociation(
    name="initializers259",
    ends={
        Property(name="Expression261", type=JavaAbstractSyntax_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ForStatement260", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenStatement270: BinaryAssociation = BinaryAssociation(
    name="thenStatement270",
    ends={
        Property(name="Statement272", type=JavaAbstractSyntax_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_IfStatement271", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updaters262: BinaryAssociation = BinaryAssociation(
    name="updaters262",
    ends={
        Property(name="Expression264", type=JavaAbstractSyntax_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ForStatement263", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments280: BinaryAssociation = BinaryAssociation(
    name="arguments280",
    ends={
        Property(name="Expression281", type=JavaAbstractSyntax_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperConstructorInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body273: BinaryAssociation = BinaryAssociation(
    name="body273",
    ends={
        Property(name="Statement274", type=JavaAbstractSyntax_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_LabeledStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label275: BinaryAssociation = BinaryAssociation(
    name="label275",
    ends={
        Property(name="SimpleName277", type=JavaAbstractSyntax_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_LabeledStatement276", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression278: BinaryAssociation = BinaryAssociation(
    name="expression278",
    ends={
        Property(name="Expression279", type=JavaAbstractSyntax_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ReturnStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression282: BinaryAssociation = BinaryAssociation(
    name="expression282",
    ends={
        Property(name="Expression284", type=JavaAbstractSyntax_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperConstructorInvocation283", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments285: BinaryAssociation = BinaryAssociation(
    name="typeArguments285",
    ends={
        Property(name="Type287", type=JavaAbstractSyntax_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SuperConstructorInvocation286", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression288: BinaryAssociation = BinaryAssociation(
    name="expression288",
    ends={
        Property(name="Expression289", type=JavaAbstractSyntax_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SwitchCase", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression297: BinaryAssociation = BinaryAssociation(
    name="expression297",
    ends={
        Property(name="Expression299", type=JavaAbstractSyntax_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SynchronizedStatement298", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression290: BinaryAssociation = BinaryAssociation(
    name="expression290",
    ends={
        Property(name="Expression291", type=JavaAbstractSyntax_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SwitchStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements292: BinaryAssociation = BinaryAssociation(
    name="statements292",
    ends={
        Property(name="Statement294", type=JavaAbstractSyntax_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SwitchStatement293", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body295: BinaryAssociation = BinaryAssociation(
    name="body295",
    ends={
        Property(name="Block296", type=JavaAbstractSyntax_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SynchronizedStatement", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type316: BinaryAssociation = BinaryAssociation(
    name="type316",
    ends={
        Property(name="Type318", type=JavaAbstractSyntax_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationStatement317", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression300: BinaryAssociation = BinaryAssociation(
    name="expression300",
    ends={
        Property(name="Expression301", type=JavaAbstractSyntax_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ThrowStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catchClauses302: BinaryAssociation = BinaryAssociation(
    name="catchClauses302",
    ends={
        Property(name="CatchClause", type=JavaAbstractSyntax_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TryStatement", type=CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body303: BinaryAssociation = BinaryAssociation(
    name="body303",
    ends={
        Property(name="Block305", type=JavaAbstractSyntax_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TryStatement304", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally306: BinaryAssociation = BinaryAssociation(
    name="finally306",
    ends={
        Property(name="Block308", type=JavaAbstractSyntax_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TryStatement307", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration309: BinaryAssociation = BinaryAssociation(
    name="declaration309",
    ends={
        Property(name="AbstractTypeDeclaration310", type=JavaAbstractSyntax_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_TypeDeclarationStatement", type=AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments311: BinaryAssociation = BinaryAssociation(
    name="fragments311",
    ends={
        Property(name="VariableDeclarationFragment312", type=JavaAbstractSyntax_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationStatement", type=VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers313: BinaryAssociation = BinaryAssociation(
    name="modifiers313",
    ends={
        Property(name="ExtendedModifier315", type=JavaAbstractSyntax_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_VariableDeclarationStatement314", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body319: BinaryAssociation = BinaryAssociation(
    name="body319",
    ends={
        Property(name="Statement320", type=JavaAbstractSyntax_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_WhileStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression321: BinaryAssociation = BinaryAssociation(
    name="expression321",
    ends={
        Property(name="Expression323", type=JavaAbstractSyntax_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_WhileStatement322", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
componentType324: BinaryAssociation = BinaryAssociation(
    name="componentType324",
    ends={
        Property(name="Type325", type=JavaAbstractSyntax_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType326: BinaryAssociation = BinaryAssociation(
    name="elementType326",
    ends={
        Property(name="Type328", type=JavaAbstractSyntax_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ArrayType327", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type329: BinaryAssociation = BinaryAssociation(
    name="type329",
    ends={
        Property(name="Type330", type=JavaAbstractSyntax_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ParameterizedType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments331: BinaryAssociation = BinaryAssociation(
    name="typeArguments331",
    ends={
        Property(name="Type333", type=JavaAbstractSyntax_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_ParameterizedType332", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers345: BinaryAssociation = BinaryAssociation(
    name="modifiers345",
    ends={
        Property(name="ExtendedModifier347", type=JavaAbstractSyntax_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SingleVariableDeclaration346", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name334: BinaryAssociation = BinaryAssociation(
    name="name334",
    ends={
        Property(name="SimpleName335", type=JavaAbstractSyntax_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_QualifiedType", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier336: BinaryAssociation = BinaryAssociation(
    name="qualifier336",
    ends={
        Property(name="Type338", type=JavaAbstractSyntax_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_QualifiedType337", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name339: BinaryAssociation = BinaryAssociation(
    name="name339",
    ends={
        Property(name="Name340", type=JavaAbstractSyntax_SimpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SimpleType", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bound341: BinaryAssociation = BinaryAssociation(
    name="bound341",
    ends={
        Property(name="Type342", type=JavaAbstractSyntax_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_WildcardType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type343: BinaryAssociation = BinaryAssociation(
    name="type343",
    ends={
        Property(name="Type344", type=JavaAbstractSyntax_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SingleVariableDeclaration", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compilations357: BinaryAssociation = BinaryAssociation(
    name="compilations357",
    ends={
        Property(name="CompilationUnit", type=JavaAbstractSyntax_StructuralPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_StructuralPackage358", type=CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name348: BinaryAssociation = BinaryAssociation(
    name="name348",
    ends={
        Property(name="SimpleName349", type=JavaAbstractSyntax_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_QualifiedName", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier350: BinaryAssociation = BinaryAssociation(
    name="qualifier350",
    ends={
        Property(name="Name352", type=JavaAbstractSyntax_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_QualifiedName351", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values353: BinaryAssociation = BinaryAssociation(
    name="values353",
    ends={
        Property(name="MemberValuePair", type=JavaAbstractSyntax_NormalAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_NormalAnnotation", type=MemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value354: BinaryAssociation = BinaryAssociation(
    name="value354",
    ends={
        Property(name="Expression355", type=JavaAbstractSyntax_SingleMemberAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_SingleMemberAnnotation", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structuralPackages356: BinaryAssociation = BinaryAssociation(
    name="structuralPackages356",
    ends={
        Property(name="StructuralPackage", type=JavaAbstractSyntax_StructuralPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaAbstractSyntax_StructuralPackage", type=StructuralPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_JavaAbstractSyntax_BodyDeclaration_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_BodyDeclaration)
gen_JavaAbstractSyntax_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_AnonymousClassDeclaration)
gen_JavaAbstractSyntax_MemberValuePair_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_MemberValuePair)
gen_JavaAbstractSyntax_CatchClause_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_CatchClause)
gen_JavaAbstractSyntax_Comment_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_Comment)
gen_JavaAbstractSyntax_CompilationUnit_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_CompilationUnit)
gen_JavaAbstractSyntax_Expression_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_Expression)
gen_JavaAbstractSyntax_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_ImportDeclaration)
gen_JavaAbstractSyntax_MemberRef_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_MemberRef)
gen_JavaAbstractSyntax_Statement_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_Statement)
gen_JavaAbstractSyntax_TagElement_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_TagElement)
gen_JavaAbstractSyntax_MethodRef_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_MethodRef)
gen_JavaAbstractSyntax_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_MethodRefParameter)
gen_JavaAbstractSyntax_Modifier_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_Modifier)
gen_JavaAbstractSyntax_Modifier_ExtendedModifier = Generalization(general=ExtendedModifier, specific=JavaAbstractSyntax_Modifier)
gen_JavaAbstractSyntax_PackageDeclaration_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_PackageDeclaration)
gen_JavaAbstractSyntax_TextElement_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_TextElement)
gen_JavaAbstractSyntax_Type_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_Type)
gen_JavaAbstractSyntax_TypeParameter_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_TypeParameter)
gen_JavaAbstractSyntax_VariableDeclaration_ASTNode = Generalization(general=ASTNode, specific=JavaAbstractSyntax_VariableDeclaration)
gen_JavaAbstractSyntax_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_AbstractTypeDeclaration)
gen_JavaAbstractSyntax_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_AnnotationTypeMemberDeclaration)
gen_JavaAbstractSyntax_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_EnumConstantDeclaration)
gen_JavaAbstractSyntax_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_FieldDeclaration)
gen_JavaAbstractSyntax_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_Initializer)
gen_JavaAbstractSyntax_MethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JavaAbstractSyntax_MethodDeclaration)
gen_JavaAbstractSyntax_BlockComment_Comment = Generalization(general=Comment, specific=JavaAbstractSyntax_BlockComment)
gen_JavaAbstractSyntax_Javadoc_Comment = Generalization(general=Comment, specific=JavaAbstractSyntax_Javadoc)
gen_JavaAbstractSyntax_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JavaAbstractSyntax_AnnotationTypeDeclaration)
gen_JavaAbstractSyntax_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JavaAbstractSyntax_EnumDeclaration)
gen_JavaAbstractSyntax_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JavaAbstractSyntax_TypeDeclaration)
gen_JavaAbstractSyntax_LineComment_Comment = Generalization(general=Comment, specific=JavaAbstractSyntax_LineComment)
gen_JavaAbstractSyntax_Annotation_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_Annotation)
gen_JavaAbstractSyntax_Annotation_ExtendedModifier = Generalization(general=ExtendedModifier, specific=JavaAbstractSyntax_Annotation)
gen_JavaAbstractSyntax_ArrayAccess_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ArrayAccess)
gen_JavaAbstractSyntax_ArrayCreation_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ArrayCreation)
gen_JavaAbstractSyntax_ArrayInitializer_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ArrayInitializer)
gen_JavaAbstractSyntax_Assignment_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_Assignment)
gen_JavaAbstractSyntax_BooleanLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_BooleanLiteral)
gen_JavaAbstractSyntax_CastExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_CastExpression)
gen_JavaAbstractSyntax_CharacterLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_CharacterLiteral)
gen_JavaAbstractSyntax_FieldAccess_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_FieldAccess)
gen_JavaAbstractSyntax_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ClassInstanceCreation)
gen_JavaAbstractSyntax_ConditionalExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ConditionalExpression)
gen_JavaAbstractSyntax_InfixExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_InfixExpression)
gen_JavaAbstractSyntax_InstanceofExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_InstanceofExpression)
gen_JavaAbstractSyntax_MethodInvocation_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_MethodInvocation)
gen_JavaAbstractSyntax_PrefixExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_PrefixExpression)
gen_JavaAbstractSyntax_Name_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_Name)
gen_JavaAbstractSyntax_NullLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_NullLiteral)
gen_JavaAbstractSyntax_NumberLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_NumberLiteral)
gen_JavaAbstractSyntax_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ParenthesizedExpression)
gen_JavaAbstractSyntax_PostfixExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_PostfixExpression)
gen_JavaAbstractSyntax_StringLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_StringLiteral)
gen_JavaAbstractSyntax_SuperFieldAccess_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_SuperFieldAccess)
gen_JavaAbstractSyntax_SuperMethodInvocation_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_SuperMethodInvocation)
gen_JavaAbstractSyntax_TypeLiteral_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_TypeLiteral)
gen_JavaAbstractSyntax_ThisExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_ThisExpression)
gen_JavaAbstractSyntax_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=JavaAbstractSyntax_VariableDeclarationExpression)
gen_JavaAbstractSyntax_AssertStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_AssertStatement)
gen_JavaAbstractSyntax_ContinueStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ContinueStatement)
gen_JavaAbstractSyntax_DoStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_DoStatement)
gen_JavaAbstractSyntax_Block_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_Block)
gen_JavaAbstractSyntax_EmptyStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_EmptyStatement)
gen_JavaAbstractSyntax_EnhancedForStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_EnhancedForStatement)
gen_JavaAbstractSyntax_BreakStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_BreakStatement)
gen_JavaAbstractSyntax_ConstructorInvocation_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ConstructorInvocation)
gen_JavaAbstractSyntax_ForStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ForStatement)
gen_JavaAbstractSyntax_ExpressionStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ExpressionStatement)
gen_JavaAbstractSyntax_IfStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_IfStatement)
gen_JavaAbstractSyntax_LabeledStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_LabeledStatement)
gen_JavaAbstractSyntax_ReturnStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ReturnStatement)
gen_JavaAbstractSyntax_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_SuperConstructorInvocation)
gen_JavaAbstractSyntax_SwitchCase_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_SwitchCase)
gen_JavaAbstractSyntax_SwitchStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_SwitchStatement)
gen_JavaAbstractSyntax_SynchronizedStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_SynchronizedStatement)
gen_JavaAbstractSyntax_ThrowStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_ThrowStatement)
gen_JavaAbstractSyntax_TryStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_TryStatement)
gen_JavaAbstractSyntax_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_TypeDeclarationStatement)
gen_JavaAbstractSyntax_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_VariableDeclarationStatement)
gen_JavaAbstractSyntax_WhileStatement_Statement = Generalization(general=Statement, specific=JavaAbstractSyntax_WhileStatement)
gen_JavaAbstractSyntax_ArrayType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_ArrayType)
gen_JavaAbstractSyntax_ParameterizedType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_ParameterizedType)
gen_JavaAbstractSyntax_PrimitiveType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_PrimitiveType)
gen_JavaAbstractSyntax_QualifiedType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_QualifiedType)
gen_JavaAbstractSyntax_SimpleType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_SimpleType)
gen_JavaAbstractSyntax_WildcardType_Type = Generalization(general=Type, specific=JavaAbstractSyntax_WildcardType)
gen_JavaAbstractSyntax_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=JavaAbstractSyntax_SingleVariableDeclaration)
gen_JavaAbstractSyntax_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=JavaAbstractSyntax_VariableDeclarationFragment)
gen_JavaAbstractSyntax_QualifiedName_Name = Generalization(general=Name, specific=JavaAbstractSyntax_QualifiedName)
gen_JavaAbstractSyntax_SimpleName_Name = Generalization(general=Name, specific=JavaAbstractSyntax_SimpleName)
gen_JavaAbstractSyntax_MarkerAnnotation_Annotation = Generalization(general=Annotation, specific=JavaAbstractSyntax_MarkerAnnotation)
gen_JavaAbstractSyntax_NormalAnnotation_Annotation = Generalization(general=Annotation, specific=JavaAbstractSyntax_NormalAnnotation)
gen_JavaAbstractSyntax_SingleMemberAnnotation_Annotation = Generalization(general=Annotation, specific=JavaAbstractSyntax_SingleMemberAnnotation)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={BodyDeclaration, JavaAbstractSyntax_BodyDeclaration, ExtendedModifier, JavaAbstractSyntax_AST, ASTNode, JavaAbstractSyntax_ASTNode, JavaAbstractSyntax_AnonymousClassDeclaration, JavaAbstractSyntax_MemberValuePair, Expression, Javadoc, JavaAbstractSyntax_CatchClause, Block, SingleVariableDeclaration, JavaAbstractSyntax_Comment, JavaAbstractSyntax_CompilationUnit, Comment, PackageDeclaration, ImportDeclaration, AbstractTypeDeclaration, JavaAbstractSyntax_Expression, JavaAbstractSyntax_ImportDeclaration, Name, JavaAbstractSyntax_MemberRef, SimpleName, JavaAbstractSyntax_Statement, JavaAbstractSyntax_TagElement, JavaAbstractSyntax_MethodRef, MethodRefParameter, JavaAbstractSyntax_MethodRefParameter, Type, JavaAbstractSyntax_ExtendedModifier, JavaAbstractSyntax_Modifier, JavaAbstractSyntax_PackageDeclaration, Annotation, JavaAbstractSyntax_TextElement, JavaAbstractSyntax_Type, JavaAbstractSyntax_TypeParameter, JavaAbstractSyntax_VariableDeclaration, JavaAbstractSyntax_AbstractTypeDeclaration, JavaAbstractSyntax_AnnotationTypeMemberDeclaration, JavaAbstractSyntax_EnumConstantDeclaration, AnonymousClassDeclaration, JavaAbstractSyntax_FieldDeclaration, VariableDeclarationFragment, JavaAbstractSyntax_Initializer, JavaAbstractSyntax_MethodDeclaration, JavaAbstractSyntax_BlockComment, JavaAbstractSyntax_Javadoc, TagElement, TypeParameter, JavaAbstractSyntax_AnnotationTypeDeclaration, JavaAbstractSyntax_EnumDeclaration, EnumConstantDeclaration, JavaAbstractSyntax_TypeDeclaration, JavaAbstractSyntax_LineComment, JavaAbstractSyntax_Annotation, JavaAbstractSyntax_ArrayAccess, JavaAbstractSyntax_ArrayCreation, ArrayInitializer, ArrayType, JavaAbstractSyntax_ArrayInitializer, JavaAbstractSyntax_Assignment, JavaAbstractSyntax_BooleanLiteral, JavaAbstractSyntax_CastExpression, JavaAbstractSyntax_CharacterLiteral, JavaAbstractSyntax_FieldAccess, JavaAbstractSyntax_ClassInstanceCreation, JavaAbstractSyntax_ConditionalExpression, JavaAbstractSyntax_InfixExpression, JavaAbstractSyntax_InstanceofExpression, JavaAbstractSyntax_MethodInvocation, JavaAbstractSyntax_PrefixExpression, JavaAbstractSyntax_Name, JavaAbstractSyntax_NullLiteral, JavaAbstractSyntax_NumberLiteral, JavaAbstractSyntax_ParenthesizedExpression, JavaAbstractSyntax_PostfixExpression, JavaAbstractSyntax_StringLiteral, JavaAbstractSyntax_SuperFieldAccess, JavaAbstractSyntax_SuperMethodInvocation, JavaAbstractSyntax_TypeLiteral, JavaAbstractSyntax_ThisExpression, JavaAbstractSyntax_VariableDeclarationExpression, JavaAbstractSyntax_AssertStatement, Statement, JavaAbstractSyntax_ContinueStatement, JavaAbstractSyntax_DoStatement, JavaAbstractSyntax_Block, JavaAbstractSyntax_EmptyStatement, JavaAbstractSyntax_EnhancedForStatement, JavaAbstractSyntax_BreakStatement, JavaAbstractSyntax_ConstructorInvocation, JavaAbstractSyntax_ForStatement, JavaAbstractSyntax_ExpressionStatement, JavaAbstractSyntax_IfStatement, JavaAbstractSyntax_LabeledStatement, JavaAbstractSyntax_ReturnStatement, JavaAbstractSyntax_SuperConstructorInvocation, JavaAbstractSyntax_SwitchCase, JavaAbstractSyntax_SwitchStatement, JavaAbstractSyntax_SynchronizedStatement, JavaAbstractSyntax_ThrowStatement, JavaAbstractSyntax_TryStatement, CatchClause, JavaAbstractSyntax_TypeDeclarationStatement, JavaAbstractSyntax_VariableDeclarationStatement, JavaAbstractSyntax_WhileStatement, JavaAbstractSyntax_ArrayType, JavaAbstractSyntax_ParameterizedType, JavaAbstractSyntax_PrimitiveType, JavaAbstractSyntax_QualifiedType, JavaAbstractSyntax_SimpleType, JavaAbstractSyntax_WildcardType, JavaAbstractSyntax_SingleVariableDeclaration, VariableDeclaration, JavaAbstractSyntax_VariableDeclarationFragment, JavaAbstractSyntax_QualifiedName, JavaAbstractSyntax_SimpleName, JavaAbstractSyntax_MarkerAnnotation, JavaAbstractSyntax_NormalAnnotation, MemberValuePair, JavaAbstractSyntax_SingleMemberAnnotation, JavaAbstractSyntax_StructuralPackage, StructuralPackage, CompilationUnit, AssignementOperatorKind, InfixExpressionOperatorKind, PostfixExpresssionOperatorKind, PrefixExpresssionOperatorKind},
    associations={bodyDeclarations1, modifiers2, root0, name22, javadoc3, body5, exception6, alternateRoot8, comments10, package11, imports13, types15, name17, name18, qualifier19, fragments44, value24, name26, qualifier28, parameters31, name33, type35, annotations37, javadoc38, name41, default61, name46, typeBounds48, initializer51, name53, bodyDeclarations56, name58, name84, returnType87, name63, type66, arguments69, anonymousClassDeclaration71, name73, fragments76, type77, body80, body82, tags113, parameters90, thrownExceptions93, typeParameters96, superInterfaceTypes98, enumConstants100, constants102, superclassType105, superInterfaceTypes107, typeParameters110, leftHandSide129, typeName114, array116, index118, dimensions121, initializer123, type125, expressions127, rightHandSide131, expression134, type136, arguments139, anonymousClassDeclaration141, expression144, type147, typeArguments150, elseExpression153, expression155, thenExpression158, expression161, name163, extendedOperands166, leftOperand168, rightOperand171, typeArguments187, leftOperand174, rightOperand176, arguments179, expression181, name184, operand194, expression190, operand192, name196, qualifier198, arguments201, qualifier212, name203, qualifier206, typeArguments209, expression224, type214, fragments216, modifiers218, type221, typeArguments234, label237, message226, body239, expression241, statements229, label230, arguments232, expression246, body254, body244, expression256, parameter249, expression252, elseStatement265, expression267, initializers259, thenStatement270, updaters262, arguments280, body273, label275, expression278, expression282, typeArguments285, expression288, expression297, expression290, statements292, body295, type316, expression300, catchClauses302, body303, finally306, declaration309, fragments311, modifiers313, body319, expression321, componentType324, elementType326, type329, typeArguments331, modifiers345, name334, qualifier336, name339, bound341, type343, compilations357, name348, qualifier350, values353, value354, structuralPackages356},
    generalizations={gen_JavaAbstractSyntax_BodyDeclaration_ASTNode, gen_JavaAbstractSyntax_AnonymousClassDeclaration_ASTNode, gen_JavaAbstractSyntax_MemberValuePair_ASTNode, gen_JavaAbstractSyntax_CatchClause_ASTNode, gen_JavaAbstractSyntax_Comment_ASTNode, gen_JavaAbstractSyntax_CompilationUnit_ASTNode, gen_JavaAbstractSyntax_Expression_ASTNode, gen_JavaAbstractSyntax_ImportDeclaration_ASTNode, gen_JavaAbstractSyntax_MemberRef_ASTNode, gen_JavaAbstractSyntax_Statement_ASTNode, gen_JavaAbstractSyntax_TagElement_ASTNode, gen_JavaAbstractSyntax_MethodRef_ASTNode, gen_JavaAbstractSyntax_MethodRefParameter_ASTNode, gen_JavaAbstractSyntax_Modifier_ASTNode, gen_JavaAbstractSyntax_Modifier_ExtendedModifier, gen_JavaAbstractSyntax_PackageDeclaration_ASTNode, gen_JavaAbstractSyntax_TextElement_ASTNode, gen_JavaAbstractSyntax_Type_ASTNode, gen_JavaAbstractSyntax_TypeParameter_ASTNode, gen_JavaAbstractSyntax_VariableDeclaration_ASTNode, gen_JavaAbstractSyntax_AbstractTypeDeclaration_BodyDeclaration, gen_JavaAbstractSyntax_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_JavaAbstractSyntax_EnumConstantDeclaration_BodyDeclaration, gen_JavaAbstractSyntax_FieldDeclaration_BodyDeclaration, gen_JavaAbstractSyntax_Initializer_BodyDeclaration, gen_JavaAbstractSyntax_MethodDeclaration_BodyDeclaration, gen_JavaAbstractSyntax_BlockComment_Comment, gen_JavaAbstractSyntax_Javadoc_Comment, gen_JavaAbstractSyntax_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_JavaAbstractSyntax_EnumDeclaration_AbstractTypeDeclaration, gen_JavaAbstractSyntax_TypeDeclaration_AbstractTypeDeclaration, gen_JavaAbstractSyntax_LineComment_Comment, gen_JavaAbstractSyntax_Annotation_Expression, gen_JavaAbstractSyntax_Annotation_ExtendedModifier, gen_JavaAbstractSyntax_ArrayAccess_Expression, gen_JavaAbstractSyntax_ArrayCreation_Expression, gen_JavaAbstractSyntax_ArrayInitializer_Expression, gen_JavaAbstractSyntax_Assignment_Expression, gen_JavaAbstractSyntax_BooleanLiteral_Expression, gen_JavaAbstractSyntax_CastExpression_Expression, gen_JavaAbstractSyntax_CharacterLiteral_Expression, gen_JavaAbstractSyntax_FieldAccess_Expression, gen_JavaAbstractSyntax_ClassInstanceCreation_Expression, gen_JavaAbstractSyntax_ConditionalExpression_Expression, gen_JavaAbstractSyntax_InfixExpression_Expression, gen_JavaAbstractSyntax_InstanceofExpression_Expression, gen_JavaAbstractSyntax_MethodInvocation_Expression, gen_JavaAbstractSyntax_PrefixExpression_Expression, gen_JavaAbstractSyntax_Name_Expression, gen_JavaAbstractSyntax_NullLiteral_Expression, gen_JavaAbstractSyntax_NumberLiteral_Expression, gen_JavaAbstractSyntax_ParenthesizedExpression_Expression, gen_JavaAbstractSyntax_PostfixExpression_Expression, gen_JavaAbstractSyntax_StringLiteral_Expression, gen_JavaAbstractSyntax_SuperFieldAccess_Expression, gen_JavaAbstractSyntax_SuperMethodInvocation_Expression, gen_JavaAbstractSyntax_TypeLiteral_Expression, gen_JavaAbstractSyntax_ThisExpression_Expression, gen_JavaAbstractSyntax_VariableDeclarationExpression_Expression, gen_JavaAbstractSyntax_AssertStatement_Statement, gen_JavaAbstractSyntax_ContinueStatement_Statement, gen_JavaAbstractSyntax_DoStatement_Statement, gen_JavaAbstractSyntax_Block_Statement, gen_JavaAbstractSyntax_EmptyStatement_Statement, gen_JavaAbstractSyntax_EnhancedForStatement_Statement, gen_JavaAbstractSyntax_BreakStatement_Statement, gen_JavaAbstractSyntax_ConstructorInvocation_Statement, gen_JavaAbstractSyntax_ForStatement_Statement, gen_JavaAbstractSyntax_ExpressionStatement_Statement, gen_JavaAbstractSyntax_IfStatement_Statement, gen_JavaAbstractSyntax_LabeledStatement_Statement, gen_JavaAbstractSyntax_ReturnStatement_Statement, gen_JavaAbstractSyntax_SuperConstructorInvocation_Statement, gen_JavaAbstractSyntax_SwitchCase_Statement, gen_JavaAbstractSyntax_SwitchStatement_Statement, gen_JavaAbstractSyntax_SynchronizedStatement_Statement, gen_JavaAbstractSyntax_ThrowStatement_Statement, gen_JavaAbstractSyntax_TryStatement_Statement, gen_JavaAbstractSyntax_TypeDeclarationStatement_Statement, gen_JavaAbstractSyntax_VariableDeclarationStatement_Statement, gen_JavaAbstractSyntax_WhileStatement_Statement, gen_JavaAbstractSyntax_ArrayType_Type, gen_JavaAbstractSyntax_ParameterizedType_Type, gen_JavaAbstractSyntax_PrimitiveType_Type, gen_JavaAbstractSyntax_QualifiedType_Type, gen_JavaAbstractSyntax_SimpleType_Type, gen_JavaAbstractSyntax_WildcardType_Type, gen_JavaAbstractSyntax_SingleVariableDeclaration_VariableDeclaration, gen_JavaAbstractSyntax_VariableDeclarationFragment_VariableDeclaration, gen_JavaAbstractSyntax_QualifiedName_Name, gen_JavaAbstractSyntax_SimpleName_Name, gen_JavaAbstractSyntax_MarkerAnnotation_Annotation, gen_JavaAbstractSyntax_NormalAnnotation_Annotation, gen_JavaAbstractSyntax_SingleMemberAnnotation_Annotation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)