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
Modifiers: Enumeration = Enumeration(
    name="Modifiers",
    literals={
            EnumerationLiteral(name="annotation"),
			EnumerationLiteral(name="bridge"),
			EnumerationLiteral(name="default"),
			EnumerationLiteral(name="deprecated"),
			EnumerationLiteral(name="enum"),
			EnumerationLiteral(name="final"),
			EnumerationLiteral(name="interface"),
			EnumerationLiteral(name="native"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="static"),
			EnumerationLiteral(name="strictfp"),
			EnumerationLiteral(name="super"),
			EnumerationLiteral(name="synchronized"),
			EnumerationLiteral(name="synthetic"),
			EnumerationLiteral(name="transient"),
			EnumerationLiteral(name="varargs"),
			EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="volatile")
    }
)

AssignmentOperatorKind: Enumeration = Enumeration(
    name="AssignmentOperatorKind",
    literals={
            EnumerationLiteral(name="right_shift_signed_assign"),
			EnumerationLiteral(name="bit_xor_assign"),
			EnumerationLiteral(name="times_assign"),
			EnumerationLiteral(name="divide_assign"),
			EnumerationLiteral(name="minus_assign"),
			EnumerationLiteral(name="bit_or_assign"),
			EnumerationLiteral(name="plus_assign"),
			EnumerationLiteral(name="assign"),
			EnumerationLiteral(name="right_shift_unsigned_assign"),
			EnumerationLiteral(name="remainder_assign"),
			EnumerationLiteral(name="bit_and_assign"),
			EnumerationLiteral(name="left_shift_assign")
    }
)

InfixExpressionOperatorKind: Enumeration = Enumeration(
    name="InfixExpressionOperatorKind",
    literals={
            EnumerationLiteral(name="greater_equals"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="right_shift_signed"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="xor"),
			EnumerationLiteral(name="less_equals"),
			EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="not_equals"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="conditional_or"),
			EnumerationLiteral(name="right_shift_unsigned"),
			EnumerationLiteral(name="remainder"),
			EnumerationLiteral(name="conditional_and"),
			EnumerationLiteral(name="times"),
			EnumerationLiteral(name="divide"),
			EnumerationLiteral(name="less"),
			EnumerationLiteral(name="left_shift")
    }
)

PostfixExpressionOperatorKind: Enumeration = Enumeration(
    name="PostfixExpressionOperatorKind",
    literals={
            EnumerationLiteral(name="increment"),
			EnumerationLiteral(name="decrement")
    }
)

PrefixExpressionOperatorKind: Enumeration = Enumeration(
    name="PrefixExpressionOperatorKind",
    literals={
            EnumerationLiteral(name="decrement"),
			EnumerationLiteral(name="complement"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="not"),
			EnumerationLiteral(name="increment"),
			EnumerationLiteral(name="plus")
    }
)

# Classes
Core_PhysicalElement = Class(name="Core::PhysicalElement", is_abstract=True)
Core_IJavaModel = Class(name="Core::IJavaModel")
PhysicalElement = Class(name="PhysicalElement")
IJavaProject = Class(name="IJavaProject")
Core_IJavaElement = Class(name="Core::IJavaElement", is_abstract=True)
Core_BinaryPackageFragmentRoot = Class(name="Core::BinaryPackageFragmentRoot")
Core_SourcePackageFragmentRoot = Class(name="Core::SourcePackageFragmentRoot")
Core_IPackageFragment = Class(name="Core::IPackageFragment")
IPackageFragmentRoot = Class(name="IPackageFragmentRoot")
Core_IJavaProject = Class(name="Core::IJavaProject")
IJavaElement = Class(name="IJavaElement")
Core_IPackageFragmentRoot = Class(name="Core::IPackageFragmentRoot", is_abstract=True)
IPackageFragment = Class(name="IPackageFragment")
CompilationUnit = Class(name="CompilationUnit")
Core_IClassFile = Class(name="Core::IClassFile")
IClassFile = Class(name="IClassFile")
ICompilationUnit = Class(name="ICompilationUnit")
Core_ITypeRoot = Class(name="Core::ITypeRoot", is_abstract=True)
ISourceReference = Class(name="ISourceReference")
Core_ICompilationUnit = Class(name="Core::ICompilationUnit")
ITypeRoot = Class(name="ITypeRoot")
IType = Class(name="IType")
IImportDeclaration = Class(name="IImportDeclaration")
Core_IMember = Class(name="Core::IMember", is_abstract=True)
Core_IType = Class(name="Core::IType")
IMember = Class(name="IMember")
IInitializer = Class(name="IInitializer")
Core_ISourceReference = Class(name="Core::ISourceReference", is_abstract=True)
ISourceRange = Class(name="ISourceRange")
Core_IImportDeclaration = Class(name="Core::IImportDeclaration")
Core_ISourceRange = Class(name="Core::ISourceRange")
Core_IInitializer = Class(name="Core::IInitializer")
Core_IField = Class(name="Core::IField")
Core_IMethod = Class(name="Core::IMethod")
IField = Class(name="IField")
IMethod = Class(name="IMethod")
ITypeParameter = Class(name="ITypeParameter")
Core_ITypeParameter = Class(name="Core::ITypeParameter")
Parameter_ = Class(name="Parameter")
Core_Parameter = Class(name="Core::Parameter")
ExtendedModifier = Class(name="ExtendedModifier")
Javadoc = Class(name="Javadoc")
DOM_CatchClause = Class(name="DOM::CatchClause")
Block = Class(name="Block")
SingleVariableDeclaration = Class(name="SingleVariableDeclaration")
DOM_Comment = Class(name="DOM::Comment", is_abstract=True)
DOM_AST = Class(name="DOM::AST")
ASTNode = Class(name="ASTNode")
DOM_ASTNode = Class(name="DOM::ASTNode", is_abstract=True)
DOM_AnonymousClassDeclaration = Class(name="DOM::AnonymousClassDeclaration")
BodyDeclaration = Class(name="BodyDeclaration")
DOM_BodyDeclaration = Class(name="DOM::BodyDeclaration", is_abstract=True)
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
DOM_Expression = Class(name="DOM::Expression", is_abstract=True)
DOM_ImportDeclaration = Class(name="DOM::ImportDeclaration")
DOM_CompilationUnit = Class(name="DOM::CompilationUnit")
Comment = Class(name="Comment")
PackageDeclaration = Class(name="PackageDeclaration")
ImportDeclaration = Class(name="ImportDeclaration")
Expression = Class(name="Expression")
DOM_MethodRef = Class(name="DOM::MethodRef")
MethodRefParameter = Class(name="MethodRefParameter")
Name = Class(name="Name")
DOM_MemberRef = Class(name="DOM::MemberRef")
SimpleName = Class(name="SimpleName")
DOM_MemberValuePair = Class(name="DOM::MemberValuePair")
DOM_MethodRefParameter = Class(name="DOM::MethodRefParameter")
Type = Class(name="Type")
DOM_ExtendedModifier = Class(name="DOM::ExtendedModifier", is_abstract=True)
DOM_Modifier = Class(name="DOM::Modifier")
DOM_Statement = Class(name="DOM::Statement", is_abstract=True)
DOM_TagElement = Class(name="DOM::TagElement")
DOM_TextElement = Class(name="DOM::TextElement")
DOM_PackageDeclaration = Class(name="DOM::PackageDeclaration")
Annotation = Class(name="Annotation")
DOM_AbstractTypeDeclaration = Class(name="DOM::AbstractTypeDeclaration", is_abstract=True)
DOM_Type = Class(name="DOM::Type", is_abstract=True)
DOM_TypeParameter = Class(name="DOM::TypeParameter")
DOM_VariableDeclaration = Class(name="DOM::VariableDeclaration", is_abstract=True)
AnonymousClassDeclaration = Class(name="AnonymousClassDeclaration")
DOM_FieldDeclaration = Class(name="DOM::FieldDeclaration")
VariableDeclarationFragment = Class(name="VariableDeclarationFragment")
DOM_AnnotationTypeMemberDeclaration = Class(name="DOM::AnnotationTypeMemberDeclaration")
DOM_EnumConstantDeclaration = Class(name="DOM::EnumConstantDeclaration")
TypeParameter = Class(name="TypeParameter")
DOM_Initializer = Class(name="DOM::Initializer")
DOM_MethodDeclaration = Class(name="DOM::MethodDeclaration")
DOM_BlockComment = Class(name="DOM::BlockComment")
DOM_Javadoc = Class(name="DOM::Javadoc")
TagElement = Class(name="TagElement")
DOM_AnnotationTypeDeclaration = Class(name="DOM::AnnotationTypeDeclaration")
DOM_EnumDeclaration = Class(name="DOM::EnumDeclaration")
EnumConstantDeclaration = Class(name="EnumConstantDeclaration")
DOM_TypeDeclaration = Class(name="DOM::TypeDeclaration")
DOM_ArrayCreation = Class(name="DOM::ArrayCreation")
ArrayInitializer = Class(name="ArrayInitializer")
ArrayType = Class(name="ArrayType")
DOM_LineComment = Class(name="DOM::LineComment")
DOM_Annotation = Class(name="DOM::Annotation", is_abstract=True)
DOM_ArrayAccess = Class(name="DOM::ArrayAccess")
DOM_ArrayInitializer = Class(name="DOM::ArrayInitializer")
DOM_BooleanLiteral = Class(name="DOM::BooleanLiteral")
DOM_Assignment = Class(name="DOM::Assignment")
DOM_CastExpression = Class(name="DOM::CastExpression")
DOM_ConditionalExpression = Class(name="DOM::ConditionalExpression")
DOM_CharacterLiteral = Class(name="DOM::CharacterLiteral")
DOM_ClassInstanceCreation = Class(name="DOM::ClassInstanceCreation")
DOM_FieldAccess = Class(name="DOM::FieldAccess")
DOM_InfixExpression = Class(name="DOM::InfixExpression")
DOM_InstanceofExpression = Class(name="DOM::InstanceofExpression")
DOM_MethodInvocation = Class(name="DOM::MethodInvocation")
DOM_Name = Class(name="DOM::Name", is_abstract=True)
DOM_NullLiteral = Class(name="DOM::NullLiteral")
DOM_NumberLiteral = Class(name="DOM::NumberLiteral")
DOM_ParenthesizedExpression = Class(name="DOM::ParenthesizedExpression")
DOM_PostfixExpression = Class(name="DOM::PostfixExpression")
DOM_PrefixExpression = Class(name="DOM::PrefixExpression")
DOM_StringLiteral = Class(name="DOM::StringLiteral")
DOM_SuperFieldAccess = Class(name="DOM::SuperFieldAccess")
DOM_SuperMethodInvocation = Class(name="DOM::SuperMethodInvocation")
DOM_ThisExpression = Class(name="DOM::ThisExpression")
DOM_TypeLiteral = Class(name="DOM::TypeLiteral")
DOM_VariableDeclarationExpression = Class(name="DOM::VariableDeclarationExpression")
DOM_AssertStatement = Class(name="DOM::AssertStatement")
Statement = Class(name="Statement")
DOM_Block = Class(name="DOM::Block")
DOM_BreakStatement = Class(name="DOM::BreakStatement")
DOM_EnhancedForStatement = Class(name="DOM::EnhancedForStatement")
DOM_ConstructorInvocation = Class(name="DOM::ConstructorInvocation")
DOM_ContinueStatement = Class(name="DOM::ContinueStatement")
DOM_DoStatement = Class(name="DOM::DoStatement")
DOM_EmptyStatement = Class(name="DOM::EmptyStatement")
DOM_ExpressionStatement = Class(name="DOM::ExpressionStatement")
DOM_ForStatement = Class(name="DOM::ForStatement")
DOM_IfStatement = Class(name="DOM::IfStatement")
DOM_LabeledStatement = Class(name="DOM::LabeledStatement")
DOM_ReturnStatement = Class(name="DOM::ReturnStatement")
DOM_SuperConstructorInvocation = Class(name="DOM::SuperConstructorInvocation")
DOM_SwitchCase = Class(name="DOM::SwitchCase")
DOM_SwitchStatement = Class(name="DOM::SwitchStatement")
DOM_SynchronizedStatement = Class(name="DOM::SynchronizedStatement")
DOM_ThrowStatement = Class(name="DOM::ThrowStatement")
DOM_TryStatement = Class(name="DOM::TryStatement")
CatchClause = Class(name="CatchClause")
DOM_TypeDeclarationStatement = Class(name="DOM::TypeDeclarationStatement")
DOM_VariableDeclarationStatement = Class(name="DOM::VariableDeclarationStatement")
DOM_WhileStatement = Class(name="DOM::WhileStatement")
DOM_ArrayType = Class(name="DOM::ArrayType")
DOM_ParameterizedType = Class(name="DOM::ParameterizedType")
DOM_PrimitiveType = Class(name="DOM::PrimitiveType")
DOM_QualifiedType = Class(name="DOM::QualifiedType")
DOM_SimpleType = Class(name="DOM::SimpleType")
DOM_WildcardType = Class(name="DOM::WildcardType")
DOM_SingleVariableDeclaration = Class(name="DOM::SingleVariableDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
DOM_VariableDeclarationFragment = Class(name="DOM::VariableDeclarationFragment")
DOM_QualifiedName = Class(name="DOM::QualifiedName")
DOM_SimpleName = Class(name="DOM::SimpleName")
DOM_MarkerAnnotation = Class(name="DOM::MarkerAnnotation")
DOM_NormalAnnotation = Class(name="DOM::NormalAnnotation")
MemberValuePair = Class(name="MemberValuePair")
DOM_SingleMemberAnnotation = Class(name="DOM::SingleMemberAnnotation")

# Core_PhysicalElement class attributes and methods
Core_PhysicalElement_path: Property = Property(name="path", type=StringType)
Core_PhysicalElement_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
Core_PhysicalElement.attributes={Core_PhysicalElement_isReadOnly, Core_PhysicalElement_path}

# Core_IJavaModel class attributes and methods

# PhysicalElement class attributes and methods

# IJavaProject class attributes and methods

# Core_IJavaElement class attributes and methods
Core_IJavaElement_elementName: Property = Property(name="elementName", type=StringType)
Core_IJavaElement.attributes={Core_IJavaElement_elementName}

# Core_BinaryPackageFragmentRoot class attributes and methods

# Core_SourcePackageFragmentRoot class attributes and methods

# Core_IPackageFragment class attributes and methods
Core_IPackageFragment_isDefaultPackage: Property = Property(name="isDefaultPackage", type=StringType)
Core_IPackageFragment.attributes={Core_IPackageFragment_isDefaultPackage}

# IPackageFragmentRoot class attributes and methods

# Core_IJavaProject class attributes and methods

# IJavaElement class attributes and methods

# Core_IPackageFragmentRoot class attributes and methods

# IPackageFragment class attributes and methods

# CompilationUnit class attributes and methods

# Core_IClassFile class attributes and methods
Core_IClassFile_isClass: Property = Property(name="isClass", type=StringType)
Core_IClassFile_isInterface: Property = Property(name="isInterface", type=StringType)
Core_IClassFile.attributes={Core_IClassFile_isInterface, Core_IClassFile_isClass}

# IClassFile class attributes and methods

# ICompilationUnit class attributes and methods

# Core_ITypeRoot class attributes and methods

# ISourceReference class attributes and methods

# Core_ICompilationUnit class attributes and methods

# ITypeRoot class attributes and methods

# IType class attributes and methods

# IImportDeclaration class attributes and methods

# Core_IMember class attributes and methods

# Core_IType class attributes and methods
Core_IType_fullyQualifiedName: Property = Property(name="fullyQualifiedName", type=StringType)
Core_IType_fullyQualifiedParametrizedName: Property = Property(name="fullyQualifiedParametrizedName", type=StringType)
Core_IType.attributes={Core_IType_fullyQualifiedName, Core_IType_fullyQualifiedParametrizedName}

# IMember class attributes and methods

# IInitializer class attributes and methods

# Core_ISourceReference class attributes and methods
Core_ISourceReference_source: Property = Property(name="source", type=StringType)
Core_ISourceReference.attributes={Core_ISourceReference_source}

# ISourceRange class attributes and methods

# Core_IImportDeclaration class attributes and methods
Core_IImportDeclaration_isOnDemand: Property = Property(name="isOnDemand", type=StringType)
Core_IImportDeclaration_isStatic: Property = Property(name="isStatic", type=StringType)
Core_IImportDeclaration.attributes={Core_IImportDeclaration_isOnDemand, Core_IImportDeclaration_isStatic}

# Core_ISourceRange class attributes and methods
Core_ISourceRange_length: Property = Property(name="length", type=StringType)
Core_ISourceRange_offset: Property = Property(name="offset", type=StringType)
Core_ISourceRange.attributes={Core_ISourceRange_length, Core_ISourceRange_offset}

# Core_IInitializer class attributes and methods

# Core_IField class attributes and methods
Core_IField_constant: Property = Property(name="constant", type=StringType)
Core_IField_isEnumConstant: Property = Property(name="isEnumConstant", type=StringType)
Core_IField_typeSignature: Property = Property(name="typeSignature", type=StringType)
Core_IField_isVolatile: Property = Property(name="isVolatile", type=StringType)
Core_IField_isTransient: Property = Property(name="isTransient", type=StringType)
Core_IField.attributes={Core_IField_constant, Core_IField_isVolatile, Core_IField_typeSignature, Core_IField_isTransient, Core_IField_isEnumConstant}

# Core_IMethod class attributes and methods
Core_IMethod_returnType: Property = Property(name="returnType", type=StringType)
Core_IMethod_isConstructor: Property = Property(name="isConstructor", type=StringType)
Core_IMethod_isMainMethod: Property = Property(name="isMainMethod", type=StringType)
Core_IMethod_exceptionTypes: Property = Property(name="exceptionTypes", type=StringType)
Core_IMethod.attributes={Core_IMethod_exceptionTypes, Core_IMethod_returnType, Core_IMethod_isMainMethod, Core_IMethod_isConstructor}

# IField class attributes and methods

# IMethod class attributes and methods

# ITypeParameter class attributes and methods

# Core_ITypeParameter class attributes and methods
Core_ITypeParameter_bounds: Property = Property(name="bounds", type=StringType)
Core_ITypeParameter.attributes={Core_ITypeParameter_bounds}

# Parameter class attributes and methods

# Core_Parameter class attributes and methods
Core_Parameter_name: Property = Property(name="name", type=StringType)
Core_Parameter_type: Property = Property(name="type", type=StringType)
Core_Parameter.attributes={Core_Parameter_type, Core_Parameter_name}

# ExtendedModifier class attributes and methods

# Javadoc class attributes and methods

# DOM_CatchClause class attributes and methods

# Block class attributes and methods

# SingleVariableDeclaration class attributes and methods

# DOM_Comment class attributes and methods

# DOM_AST class attributes and methods

# ASTNode class attributes and methods

# DOM_ASTNode class attributes and methods

# DOM_AnonymousClassDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# DOM_BodyDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# DOM_Expression class attributes and methods
DOM_Expression_resolveBoxing: Property = Property(name="resolveBoxing", type=StringType)
DOM_Expression_resolveUnboxing: Property = Property(name="resolveUnboxing", type=StringType)
DOM_Expression.attributes={DOM_Expression_resolveBoxing, DOM_Expression_resolveUnboxing}

# DOM_ImportDeclaration class attributes and methods
DOM_ImportDeclaration_onDemand: Property = Property(name="onDemand", type=StringType)
DOM_ImportDeclaration_static: Property = Property(name="static", type=StringType)
DOM_ImportDeclaration.attributes={DOM_ImportDeclaration_static, DOM_ImportDeclaration_onDemand}

# DOM_CompilationUnit class attributes and methods

# Comment class attributes and methods

# PackageDeclaration class attributes and methods

# ImportDeclaration class attributes and methods

# Expression class attributes and methods

# DOM_MethodRef class attributes and methods

# MethodRefParameter class attributes and methods

# Name class attributes and methods

# DOM_MemberRef class attributes and methods

# SimpleName class attributes and methods

# DOM_MemberValuePair class attributes and methods

# DOM_MethodRefParameter class attributes and methods
DOM_MethodRefParameter_varargs: Property = Property(name="varargs", type=StringType)
DOM_MethodRefParameter.attributes={DOM_MethodRefParameter_varargs}

# Type class attributes and methods

# DOM_ExtendedModifier class attributes and methods

# DOM_Modifier class attributes and methods
DOM_Modifier_final: Property = Property(name="final", type=StringType)
DOM_Modifier_native: Property = Property(name="native", type=StringType)
DOM_Modifier_none: Property = Property(name="none", type=StringType)
DOM_Modifier_private: Property = Property(name="private", type=StringType)
DOM_Modifier_protected: Property = Property(name="protected", type=StringType)
DOM_Modifier_public: Property = Property(name="public", type=StringType)
DOM_Modifier_static: Property = Property(name="static", type=StringType)
DOM_Modifier_strictfp: Property = Property(name="strictfp", type=StringType)
DOM_Modifier_synchronized: Property = Property(name="synchronized", type=StringType)
DOM_Modifier_abstract: Property = Property(name="abstract", type=StringType)
DOM_Modifier_transient: Property = Property(name="transient", type=StringType)
DOM_Modifier_volatile: Property = Property(name="volatile", type=StringType)
DOM_Modifier.attributes={DOM_Modifier_final, DOM_Modifier_private, DOM_Modifier_native, DOM_Modifier_strictfp, DOM_Modifier_none, DOM_Modifier_abstract, DOM_Modifier_public, DOM_Modifier_transient, DOM_Modifier_synchronized, DOM_Modifier_protected, DOM_Modifier_volatile, DOM_Modifier_static}

# DOM_Statement class attributes and methods

# DOM_TagElement class attributes and methods
DOM_TagElement_tagName: Property = Property(name="tagName", type=StringType)
DOM_TagElement_nested: Property = Property(name="nested", type=StringType)
DOM_TagElement.attributes={DOM_TagElement_tagName, DOM_TagElement_nested}

# DOM_TextElement class attributes and methods
DOM_TextElement_text: Property = Property(name="text", type=StringType)
DOM_TextElement.attributes={DOM_TextElement_text}

# DOM_PackageDeclaration class attributes and methods

# Annotation class attributes and methods

# DOM_AbstractTypeDeclaration class attributes and methods
DOM_AbstractTypeDeclaration_localTypeDeclaration: Property = Property(name="localTypeDeclaration", type=StringType)
DOM_AbstractTypeDeclaration_memberTypeDeclaration: Property = Property(name="memberTypeDeclaration", type=StringType)
DOM_AbstractTypeDeclaration_packageMemberTypeDeclaration: Property = Property(name="packageMemberTypeDeclaration", type=StringType)
DOM_AbstractTypeDeclaration.attributes={DOM_AbstractTypeDeclaration_memberTypeDeclaration, DOM_AbstractTypeDeclaration_packageMemberTypeDeclaration, DOM_AbstractTypeDeclaration_localTypeDeclaration}

# DOM_Type class attributes and methods

# DOM_TypeParameter class attributes and methods

# DOM_VariableDeclaration class attributes and methods
DOM_VariableDeclaration_extraDimensions: Property = Property(name="extraDimensions", type=StringType)
DOM_VariableDeclaration.attributes={DOM_VariableDeclaration_extraDimensions}

# AnonymousClassDeclaration class attributes and methods

# DOM_FieldDeclaration class attributes and methods

# VariableDeclarationFragment class attributes and methods

# DOM_AnnotationTypeMemberDeclaration class attributes and methods

# DOM_EnumConstantDeclaration class attributes and methods

# TypeParameter class attributes and methods

# DOM_Initializer class attributes and methods

# DOM_MethodDeclaration class attributes and methods
DOM_MethodDeclaration_constructor: Property = Property(name="constructor", type=StringType)
DOM_MethodDeclaration_varargs: Property = Property(name="varargs", type=StringType)
DOM_MethodDeclaration_extraDimensions: Property = Property(name="extraDimensions", type=StringType)
DOM_MethodDeclaration.attributes={DOM_MethodDeclaration_varargs, DOM_MethodDeclaration_constructor, DOM_MethodDeclaration_extraDimensions}

# DOM_BlockComment class attributes and methods

# DOM_Javadoc class attributes and methods

# TagElement class attributes and methods

# DOM_AnnotationTypeDeclaration class attributes and methods

# DOM_EnumDeclaration class attributes and methods

# EnumConstantDeclaration class attributes and methods

# DOM_TypeDeclaration class attributes and methods
DOM_TypeDeclaration_interface: Property = Property(name="interface", type=StringType)
DOM_TypeDeclaration.attributes={DOM_TypeDeclaration_interface}

# DOM_ArrayCreation class attributes and methods

# ArrayInitializer class attributes and methods

# ArrayType class attributes and methods

# DOM_LineComment class attributes and methods

# DOM_Annotation class attributes and methods

# DOM_ArrayAccess class attributes and methods

# DOM_ArrayInitializer class attributes and methods

# DOM_BooleanLiteral class attributes and methods
DOM_BooleanLiteral_booleanValue: Property = Property(name="booleanValue", type=StringType)
DOM_BooleanLiteral.attributes={DOM_BooleanLiteral_booleanValue}

# DOM_Assignment class attributes and methods
DOM_Assignment_operator: Property = Property(name="operator", type=StringType)
DOM_Assignment.attributes={DOM_Assignment_operator}

# DOM_CastExpression class attributes and methods

# DOM_ConditionalExpression class attributes and methods

# DOM_CharacterLiteral class attributes and methods
DOM_CharacterLiteral_charValue: Property = Property(name="charValue", type=StringType)
DOM_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
DOM_CharacterLiteral.attributes={DOM_CharacterLiteral_charValue, DOM_CharacterLiteral_escapedValue}

# DOM_ClassInstanceCreation class attributes and methods

# DOM_FieldAccess class attributes and methods

# DOM_InfixExpression class attributes and methods
DOM_InfixExpression_operator: Property = Property(name="operator", type=StringType)
DOM_InfixExpression.attributes={DOM_InfixExpression_operator}

# DOM_InstanceofExpression class attributes and methods

# DOM_MethodInvocation class attributes and methods

# DOM_Name class attributes and methods
DOM_Name_fullyQualifiedName: Property = Property(name="fullyQualifiedName", type=StringType)
DOM_Name.attributes={DOM_Name_fullyQualifiedName}

# DOM_NullLiteral class attributes and methods

# DOM_NumberLiteral class attributes and methods
DOM_NumberLiteral_token: Property = Property(name="token", type=StringType)
DOM_NumberLiteral.attributes={DOM_NumberLiteral_token}

# DOM_ParenthesizedExpression class attributes and methods

# DOM_PostfixExpression class attributes and methods
DOM_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
DOM_PostfixExpression.attributes={DOM_PostfixExpression_operator}

# DOM_PrefixExpression class attributes and methods
DOM_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
DOM_PrefixExpression.attributes={DOM_PrefixExpression_operator}

# DOM_StringLiteral class attributes and methods
DOM_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
DOM_StringLiteral_literalValue: Property = Property(name="literalValue", type=StringType)
DOM_StringLiteral.attributes={DOM_StringLiteral_literalValue, DOM_StringLiteral_escapedValue}

# DOM_SuperFieldAccess class attributes and methods

# DOM_SuperMethodInvocation class attributes and methods

# DOM_ThisExpression class attributes and methods

# DOM_TypeLiteral class attributes and methods

# DOM_VariableDeclarationExpression class attributes and methods

# DOM_AssertStatement class attributes and methods

# Statement class attributes and methods

# DOM_Block class attributes and methods

# DOM_BreakStatement class attributes and methods

# DOM_EnhancedForStatement class attributes and methods

# DOM_ConstructorInvocation class attributes and methods

# DOM_ContinueStatement class attributes and methods

# DOM_DoStatement class attributes and methods

# DOM_EmptyStatement class attributes and methods

# DOM_ExpressionStatement class attributes and methods

# DOM_ForStatement class attributes and methods

# DOM_IfStatement class attributes and methods

# DOM_LabeledStatement class attributes and methods

# DOM_ReturnStatement class attributes and methods

# DOM_SuperConstructorInvocation class attributes and methods

# DOM_SwitchCase class attributes and methods
DOM_SwitchCase_default: Property = Property(name="default", type=StringType)
DOM_SwitchCase.attributes={DOM_SwitchCase_default}

# DOM_SwitchStatement class attributes and methods

# DOM_SynchronizedStatement class attributes and methods

# DOM_ThrowStatement class attributes and methods

# DOM_TryStatement class attributes and methods

# CatchClause class attributes and methods

# DOM_TypeDeclarationStatement class attributes and methods

# DOM_VariableDeclarationStatement class attributes and methods

# DOM_WhileStatement class attributes and methods

# DOM_ArrayType class attributes and methods
DOM_ArrayType_dimensions: Property = Property(name="dimensions", type=StringType)
DOM_ArrayType.attributes={DOM_ArrayType_dimensions}

# DOM_ParameterizedType class attributes and methods

# DOM_PrimitiveType class attributes and methods
DOM_PrimitiveType_code: Property = Property(name="code", type=StringType)
DOM_PrimitiveType.attributes={DOM_PrimitiveType_code}

# DOM_QualifiedType class attributes and methods

# DOM_SimpleType class attributes and methods

# DOM_WildcardType class attributes and methods
DOM_WildcardType_upperBound: Property = Property(name="upperBound", type=StringType)
DOM_WildcardType.attributes={DOM_WildcardType_upperBound}

# DOM_SingleVariableDeclaration class attributes and methods
DOM_SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=StringType)
DOM_SingleVariableDeclaration.attributes={DOM_SingleVariableDeclaration_varargs}

# VariableDeclaration class attributes and methods

# DOM_VariableDeclarationFragment class attributes and methods

# DOM_QualifiedName class attributes and methods

# DOM_SimpleName class attributes and methods
DOM_SimpleName_identifier: Property = Property(name="identifier", type=StringType)
DOM_SimpleName_declaration: Property = Property(name="declaration", type=StringType)
DOM_SimpleName.attributes={DOM_SimpleName_declaration, DOM_SimpleName_identifier}

# DOM_MarkerAnnotation class attributes and methods

# DOM_NormalAnnotation class attributes and methods

# MemberValuePair class attributes and methods

# DOM_SingleMemberAnnotation class attributes and methods

# Relationships
javaProjects0: BinaryAssociation = BinaryAssociation(
    name="javaProjects0",
    ends={
        Property(name="IJavaProject", type=Core_IJavaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IJavaModel", type=IJavaProject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageFragmentRoot12: BinaryAssociation = BinaryAssociation(
    name="packageFragmentRoot12",
    ends={
        Property(name="#14", type=Core_IPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="013", type=IPackageFragmentRoot, multiplicity=Multiplicity(1, 1))
    }
)
externalPackageFragmentRoots1: BinaryAssociation = BinaryAssociation(
    name="externalPackageFragmentRoots1",
    ends={
        Property(name="IPackageFragmentRoot", type=Core_IJavaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IJavaModel2", type=IPackageFragmentRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageFragmentRoots3: BinaryAssociation = BinaryAssociation(
    name="packageFragmentRoots3",
    ends={
        Property(name="IPackageFragmentRoot4", type=Core_IJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IJavaProject", type=IPackageFragmentRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalPackageFragmentRoots5: BinaryAssociation = BinaryAssociation(
    name="externalPackageFragmentRoots5",
    ends={
        Property(name="IPackageFragmentRoot7", type=Core_IJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IJavaProject6", type=IPackageFragmentRoot, multiplicity=Multiplicity(0, 9999))
    }
)
requiredProjects8: BinaryAssociation = BinaryAssociation(
    name="requiredProjects8",
    ends={
        Property(name="IJavaProject10", type=Core_IJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IJavaProject9", type=IJavaProject, multiplicity=Multiplicity(0, 9999))
    }
)
packageFragments11: BinaryAssociation = BinaryAssociation(
    name="packageFragments11",
    ends={
        Property(name="#", type=Core_IPackageFragmentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=IPackageFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primary24: BinaryAssociation = BinaryAssociation(
    name="primary24",
    ends={
        Property(name="ICompilationUnit26", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ICompilationUnit25", type=ICompilationUnit, multiplicity=Multiplicity(1, 1))
    }
)
ast27: BinaryAssociation = BinaryAssociation(
    name="ast27",
    ends={
        Property(name="CompilationUnit", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ICompilationUnit28", type=CompilationUnit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classFiles15: BinaryAssociation = BinaryAssociation(
    name="classFiles15",
    ends={
        Property(name="IClassFile", type=Core_IPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IPackageFragment", type=IClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits16: BinaryAssociation = BinaryAssociation(
    name="compilationUnits16",
    ends={
        Property(name="ICompilationUnit", type=Core_IPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IPackageFragment17", type=ICompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allType18: BinaryAssociation = BinaryAssociation(
    name="allType18",
    ends={
        Property(name="IType", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ICompilationUnit", type=IType, multiplicity=Multiplicity(0, 9999))
    }
)
imports19: BinaryAssociation = BinaryAssociation(
    name="imports19",
    ends={
        Property(name="IImportDeclaration", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ICompilationUnit20", type=IImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types21: BinaryAssociation = BinaryAssociation(
    name="types21",
    ends={
        Property(name="IType23", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ICompilationUnit22", type=IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadocRange32: BinaryAssociation = BinaryAssociation(
    name="javadocRange32",
    ends={
        Property(name="ISourceRange33", type=Core_IMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IMember", type=ISourceRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameRange34: BinaryAssociation = BinaryAssociation(
    name="nameRange34",
    ends={
        Property(name="ISourceRange36", type=Core_IMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IMember35", type=ISourceRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="IType30", type=Core_IClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IClassFile", type=IType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializers37: BinaryAssociation = BinaryAssociation(
    name="initializers37",
    ends={
        Property(name="IInitializer", type=Core_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IType", type=IInitializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceRange31: BinaryAssociation = BinaryAssociation(
    name="sourceRange31",
    ends={
        Property(name="ISourceRange", type=Core_ISourceReference, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ISourceReference", type=ISourceRange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fields38: BinaryAssociation = BinaryAssociation(
    name="fields38",
    ends={
        Property(name="IField", type=Core_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IType39", type=IField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods40: BinaryAssociation = BinaryAssociation(
    name="methods40",
    ends={
        Property(name="IMethod", type=Core_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IType41", type=IMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types42: BinaryAssociation = BinaryAssociation(
    name="types42",
    ends={
        Property(name="IType44", type=Core_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IType43", type=IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters45: BinaryAssociation = BinaryAssociation(
    name="typeParameters45",
    ends={
        Property(name="ITypeParameter", type=Core_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IType46", type=ITypeParameter, multiplicity=Multiplicity(0, 9999))
    }
)
parameters47: BinaryAssociation = BinaryAssociation(
    name="parameters47",
    ends={
        Property(name="Parameter", type=Core_IMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IMethod", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers50: BinaryAssociation = BinaryAssociation(
    name="modifiers50",
    ends={
        Property(name="ExtendedModifier", type=DOM_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_BodyDeclaration", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc51: BinaryAssociation = BinaryAssociation(
    name="javadoc51",
    ends={
        Property(name="Javadoc", type=DOM_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_BodyDeclaration52", type=Javadoc, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body53: BinaryAssociation = BinaryAssociation(
    name="body53",
    ends={
        Property(name="Block", type=DOM_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CatchClause", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception54: BinaryAssociation = BinaryAssociation(
    name="exception54",
    ends={
        Property(name="SingleVariableDeclaration", type=DOM_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CatchClause55", type=SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compilationUnits48: BinaryAssociation = BinaryAssociation(
    name="compilationUnits48",
    ends={
        Property(name="ASTNode", type=DOM_AST, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AST", type=ASTNode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyDeclarations49: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations49",
    ends={
        Property(name="BodyDeclaration", type=DOM_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AnonymousClassDeclaration", type=BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports61: BinaryAssociation = BinaryAssociation(
    name="imports61",
    ends={
        Property(name="ImportDeclaration", type=DOM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CompilationUnit62", type=ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types63: BinaryAssociation = BinaryAssociation(
    name="types63",
    ends={
        Property(name="AbstractTypeDeclaration", type=DOM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CompilationUnit64", type=AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeBinding65: BinaryAssociation = BinaryAssociation(
    name="typeBinding65",
    ends={
        Property(name="IType66", type=DOM_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Expression", type=IType, multiplicity=Multiplicity(1, 1))
    }
)
alternateRoot56: BinaryAssociation = BinaryAssociation(
    name="alternateRoot56",
    ends={
        Property(name="ASTNode57", type=DOM_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Comment", type=ASTNode, multiplicity=Multiplicity(1, 1))
    }
)
comments58: BinaryAssociation = BinaryAssociation(
    name="comments58",
    ends={
        Property(name="Comment", type=DOM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CompilationUnit", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package59: BinaryAssociation = BinaryAssociation(
    name="package59",
    ends={
        Property(name="PackageDeclaration", type=DOM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CompilationUnit60", type=PackageDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name72: BinaryAssociation = BinaryAssociation(
    name="name72",
    ends={
        Property(name="SimpleName73", type=DOM_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MemberValuePair", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value74: BinaryAssociation = BinaryAssociation(
    name="value74",
    ends={
        Property(name="Expression", type=DOM_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MemberValuePair75", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name76: BinaryAssociation = BinaryAssociation(
    name="name76",
    ends={
        Property(name="SimpleName77", type=DOM_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodRef", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier78: BinaryAssociation = BinaryAssociation(
    name="qualifier78",
    ends={
        Property(name="Name80", type=DOM_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodRef79", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters81: BinaryAssociation = BinaryAssociation(
    name="parameters81",
    ends={
        Property(name="MethodRefParameter", type=DOM_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodRef82", type=MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name67: BinaryAssociation = BinaryAssociation(
    name="name67",
    ends={
        Property(name="Name", type=DOM_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ImportDeclaration", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name68: BinaryAssociation = BinaryAssociation(
    name="name68",
    ends={
        Property(name="SimpleName", type=DOM_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MemberRef", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier69: BinaryAssociation = BinaryAssociation(
    name="qualifier69",
    ends={
        Property(name="Name71", type=DOM_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MemberRef70", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name83: BinaryAssociation = BinaryAssociation(
    name="name83",
    ends={
        Property(name="SimpleName84", type=DOM_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodRefParameter", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type85: BinaryAssociation = BinaryAssociation(
    name="type85",
    ends={
        Property(name="Type", type=DOM_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodRefParameter86", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
binding94: BinaryAssociation = BinaryAssociation(
    name="binding94",
    ends={
        Property(name="DOM_PackageDeclaration95", type=IPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="IPackageFragment", type=DOM_PackageDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
fragments96: BinaryAssociation = BinaryAssociation(
    name="fragments96",
    ends={
        Property(name="ASTNode97", type=DOM_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TagElement", type=ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations87: BinaryAssociation = BinaryAssociation(
    name="annotations87",
    ends={
        Property(name="Annotation", type=DOM_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PackageDeclaration", type=Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc88: BinaryAssociation = BinaryAssociation(
    name="javadoc88",
    ends={
        Property(name="Javadoc90", type=DOM_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PackageDeclaration89", type=Javadoc, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name91: BinaryAssociation = BinaryAssociation(
    name="name91",
    ends={
        Property(name="Name93", type=DOM_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PackageDeclaration92", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer103: BinaryAssociation = BinaryAssociation(
    name="initializer103",
    ends={
        Property(name="Expression104", type=DOM_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclaration", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name105: BinaryAssociation = BinaryAssociation(
    name="name105",
    ends={
        Property(name="SimpleName107", type=DOM_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclaration106", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyDeclarations108: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations108",
    ends={
        Property(name="BodyDeclaration109", type=DOM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AbstractTypeDeclaration", type=BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name110: BinaryAssociation = BinaryAssociation(
    name="name110",
    ends={
        Property(name="SimpleName112", type=DOM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AbstractTypeDeclaration111", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name98: BinaryAssociation = BinaryAssociation(
    name="name98",
    ends={
        Property(name="SimpleName99", type=DOM_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeParameter", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeBounds100: BinaryAssociation = BinaryAssociation(
    name="typeBounds100",
    ends={
        Property(name="Type102", type=DOM_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeParameter101", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments121: BinaryAssociation = BinaryAssociation(
    name="arguments121",
    ends={
        Property(name="Expression122", type=DOM_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnumConstantDeclaration", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration123: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration123",
    ends={
        Property(name="AnonymousClassDeclaration", type=DOM_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnumConstantDeclaration124", type=AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name125: BinaryAssociation = BinaryAssociation(
    name="name125",
    ends={
        Property(name="SimpleName127", type=DOM_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnumConstantDeclaration126", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments128: BinaryAssociation = BinaryAssociation(
    name="fragments128",
    ends={
        Property(name="VariableDeclarationFragment", type=DOM_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_FieldDeclaration", type=VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type129: BinaryAssociation = BinaryAssociation(
    name="type129",
    ends={
        Property(name="Type131", type=DOM_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_FieldDeclaration130", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
default113: BinaryAssociation = BinaryAssociation(
    name="default113",
    ends={
        Property(name="Expression114", type=DOM_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AnnotationTypeMemberDeclaration", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name115: BinaryAssociation = BinaryAssociation(
    name="name115",
    ends={
        Property(name="SimpleName117", type=DOM_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AnnotationTypeMemberDeclaration116", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type118: BinaryAssociation = BinaryAssociation(
    name="type118",
    ends={
        Property(name="Type120", type=DOM_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AnnotationTypeMemberDeclaration119", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType139: BinaryAssociation = BinaryAssociation(
    name="returnType139",
    ends={
        Property(name="Type141", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration140", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters142: BinaryAssociation = BinaryAssociation(
    name="parameters142",
    ends={
        Property(name="SingleVariableDeclaration144", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration143", type=SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thrownExceptions145: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions145",
    ends={
        Property(name="Name147", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration146", type=Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters148: BinaryAssociation = BinaryAssociation(
    name="typeParameters148",
    ends={
        Property(name="TypeParameter", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration149", type=TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body132: BinaryAssociation = BinaryAssociation(
    name="body132",
    ends={
        Property(name="Block133", type=DOM_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Initializer", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body134: BinaryAssociation = BinaryAssociation(
    name="body134",
    ends={
        Property(name="Block135", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name136: BinaryAssociation = BinaryAssociation(
    name="name136",
    ends={
        Property(name="SimpleName138", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration137", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superclassType157: BinaryAssociation = BinaryAssociation(
    name="superclassType157",
    ends={
        Property(name="Type158", type=DOM_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeDeclaration", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superInterfaceTypes159: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes159",
    ends={
        Property(name="Type161", type=DOM_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeDeclaration160", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters162: BinaryAssociation = BinaryAssociation(
    name="typeParameters162",
    ends={
        Property(name="TypeParameter164", type=DOM_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeDeclaration163", type=TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
binding150: BinaryAssociation = BinaryAssociation(
    name="binding150",
    ends={
        Property(name="IMethod152", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration151", type=IMethod, multiplicity=Multiplicity(1, 1))
    }
)
superInterfaceTypes153: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes153",
    ends={
        Property(name="Type154", type=DOM_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnumDeclaration", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumConstants155: BinaryAssociation = BinaryAssociation(
    name="enumConstants155",
    ends={
        Property(name="EnumConstantDeclaration", type=DOM_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnumDeclaration156", type=EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
index170: BinaryAssociation = BinaryAssociation(
    name="index170",
    ends={
        Property(name="Expression172", type=DOM_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayAccess171", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions173: BinaryAssociation = BinaryAssociation(
    name="dimensions173",
    ends={
        Property(name="Expression174", type=DOM_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayCreation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer175: BinaryAssociation = BinaryAssociation(
    name="initializer175",
    ends={
        Property(name="ArrayInitializer", type=DOM_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayCreation176", type=ArrayInitializer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tags165: BinaryAssociation = BinaryAssociation(
    name="tags165",
    ends={
        Property(name="TagElement", type=DOM_Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Javadoc", type=TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeName166: BinaryAssociation = BinaryAssociation(
    name="typeName166",
    ends={
        Property(name="Name167", type=DOM_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Annotation", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array168: BinaryAssociation = BinaryAssociation(
    name="array168",
    ends={
        Property(name="Expression169", type=DOM_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayAccess", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide181: BinaryAssociation = BinaryAssociation(
    name="leftHandSide181",
    ends={
        Property(name="Expression182", type=DOM_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Assignment", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide183: BinaryAssociation = BinaryAssociation(
    name="rightHandSide183",
    ends={
        Property(name="Expression185", type=DOM_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Assignment184", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type177: BinaryAssociation = BinaryAssociation(
    name="type177",
    ends={
        Property(name="ArrayType", type=DOM_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayCreation178", type=ArrayType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions179: BinaryAssociation = BinaryAssociation(
    name="expressions179",
    ends={
        Property(name="Expression180", type=DOM_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayInitializer", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression186: BinaryAssociation = BinaryAssociation(
    name="expression186",
    ends={
        Property(name="Expression187", type=DOM_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CastExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type188: BinaryAssociation = BinaryAssociation(
    name="type188",
    ends={
        Property(name="Type190", type=DOM_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CastExpression189", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments191: BinaryAssociation = BinaryAssociation(
    name="arguments191",
    ends={
        Property(name="Expression192", type=DOM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ClassInstanceCreation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration193: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration193",
    ends={
        Property(name="AnonymousClassDeclaration195", type=DOM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ClassInstanceCreation194", type=AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression196: BinaryAssociation = BinaryAssociation(
    name="expression196",
    ends={
        Property(name="Expression198", type=DOM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ClassInstanceCreation197", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type199: BinaryAssociation = BinaryAssociation(
    name="type199",
    ends={
        Property(name="Type201", type=DOM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ClassInstanceCreation200", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments202: BinaryAssociation = BinaryAssociation(
    name="typeArguments202",
    ends={
        Property(name="Type204", type=DOM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ClassInstanceCreation203", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseExpression205: BinaryAssociation = BinaryAssociation(
    name="elseExpression205",
    ends={
        Property(name="Expression206", type=DOM_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ConditionalExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression207: BinaryAssociation = BinaryAssociation(
    name="expression207",
    ends={
        Property(name="Expression209", type=DOM_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ConditionalExpression208", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression210: BinaryAssociation = BinaryAssociation(
    name="thenExpression210",
    ends={
        Property(name="Expression212", type=DOM_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ConditionalExpression211", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression213: BinaryAssociation = BinaryAssociation(
    name="expression213",
    ends={
        Property(name="Expression214", type=DOM_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_FieldAccess", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name215: BinaryAssociation = BinaryAssociation(
    name="name215",
    ends={
        Property(name="SimpleName217", type=DOM_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_FieldAccess216", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands218: BinaryAssociation = BinaryAssociation(
    name="extendedOperands218",
    ends={
        Property(name="Expression219", type=DOM_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_InfixExpression", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand220: BinaryAssociation = BinaryAssociation(
    name="leftOperand220",
    ends={
        Property(name="Expression222", type=DOM_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_InfixExpression221", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand223: BinaryAssociation = BinaryAssociation(
    name="rightOperand223",
    ends={
        Property(name="Expression225", type=DOM_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_InfixExpression224", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand226: BinaryAssociation = BinaryAssociation(
    name="leftOperand226",
    ends={
        Property(name="Expression227", type=DOM_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_InstanceofExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand228: BinaryAssociation = BinaryAssociation(
    name="rightOperand228",
    ends={
        Property(name="Type230", type=DOM_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_InstanceofExpression229", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments231: BinaryAssociation = BinaryAssociation(
    name="arguments231",
    ends={
        Property(name="Expression232", type=DOM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression245: BinaryAssociation = BinaryAssociation(
    name="expression245",
    ends={
        Property(name="Expression246", type=DOM_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ParenthesizedExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name236: BinaryAssociation = BinaryAssociation(
    name="name236",
    ends={
        Property(name="SimpleName238", type=DOM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodInvocation237", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments239: BinaryAssociation = BinaryAssociation(
    name="typeArguments239",
    ends={
        Property(name="Type241", type=DOM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodInvocation240", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodBinding242: BinaryAssociation = BinaryAssociation(
    name="methodBinding242",
    ends={
        Property(name="IMethod244", type=DOM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodInvocation243", type=IMethod, multiplicity=Multiplicity(1, 1))
    }
)
expression233: BinaryAssociation = BinaryAssociation(
    name="expression233",
    ends={
        Property(name="Expression235", type=DOM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodInvocation234", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand247: BinaryAssociation = BinaryAssociation(
    name="operand247",
    ends={
        Property(name="Expression248", type=DOM_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PostfixExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand249: BinaryAssociation = BinaryAssociation(
    name="operand249",
    ends={
        Property(name="Expression250", type=DOM_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PrefixExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name258: BinaryAssociation = BinaryAssociation(
    name="name258",
    ends={
        Property(name="Name260", type=DOM_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperMethodInvocation259", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name251: BinaryAssociation = BinaryAssociation(
    name="name251",
    ends={
        Property(name="SimpleName252", type=DOM_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperFieldAccess", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier253: BinaryAssociation = BinaryAssociation(
    name="qualifier253",
    ends={
        Property(name="Name255", type=DOM_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperFieldAccess254", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments256: BinaryAssociation = BinaryAssociation(
    name="arguments256",
    ends={
        Property(name="Expression257", type=DOM_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperMethodInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers273: BinaryAssociation = BinaryAssociation(
    name="modifiers273",
    ends={
        Property(name="ExtendedModifier275", type=DOM_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationExpression274", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier261: BinaryAssociation = BinaryAssociation(
    name="qualifier261",
    ends={
        Property(name="Name263", type=DOM_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperMethodInvocation262", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments264: BinaryAssociation = BinaryAssociation(
    name="typeArguments264",
    ends={
        Property(name="Type266", type=DOM_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperMethodInvocation265", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier267: BinaryAssociation = BinaryAssociation(
    name="qualifier267",
    ends={
        Property(name="Name268", type=DOM_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ThisExpression", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type269: BinaryAssociation = BinaryAssociation(
    name="type269",
    ends={
        Property(name="Type270", type=DOM_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeLiteral", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments271: BinaryAssociation = BinaryAssociation(
    name="fragments271",
    ends={
        Property(name="VariableDeclarationFragment272", type=DOM_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationExpression", type=VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type276: BinaryAssociation = BinaryAssociation(
    name="type276",
    ends={
        Property(name="Type278", type=DOM_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationExpression277", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression279: BinaryAssociation = BinaryAssociation(
    name="expression279",
    ends={
        Property(name="Expression280", type=DOM_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AssertStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message281: BinaryAssociation = BinaryAssociation(
    name="message281",
    ends={
        Property(name="Expression283", type=DOM_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AssertStatement282", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements284: BinaryAssociation = BinaryAssociation(
    name="statements284",
    ends={
        Property(name="Statement", type=DOM_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Block", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label285: BinaryAssociation = BinaryAssociation(
    name="label285",
    ends={
        Property(name="SimpleName286", type=DOM_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_BreakStatement", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments287: BinaryAssociation = BinaryAssociation(
    name="arguments287",
    ends={
        Property(name="Expression288", type=DOM_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ConstructorInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments289: BinaryAssociation = BinaryAssociation(
    name="typeArguments289",
    ends={
        Property(name="Type291", type=DOM_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ConstructorInvocation290", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label292: BinaryAssociation = BinaryAssociation(
    name="label292",
    ends={
        Property(name="SimpleName293", type=DOM_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ContinueStatement", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body294: BinaryAssociation = BinaryAssociation(
    name="body294",
    ends={
        Property(name="Statement295", type=DOM_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_DoStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression296: BinaryAssociation = BinaryAssociation(
    name="expression296",
    ends={
        Property(name="Expression298", type=DOM_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_DoStatement297", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression311: BinaryAssociation = BinaryAssociation(
    name="expression311",
    ends={
        Property(name="Expression313", type=DOM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ForStatement312", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body299: BinaryAssociation = BinaryAssociation(
    name="body299",
    ends={
        Property(name="Statement300", type=DOM_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnhancedForStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression301: BinaryAssociation = BinaryAssociation(
    name="expression301",
    ends={
        Property(name="Expression303", type=DOM_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnhancedForStatement302", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter304: BinaryAssociation = BinaryAssociation(
    name="parameter304",
    ends={
        Property(name="SingleVariableDeclaration306", type=DOM_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnhancedForStatement305", type=SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression307: BinaryAssociation = BinaryAssociation(
    name="expression307",
    ends={
        Property(name="Expression308", type=DOM_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body309: BinaryAssociation = BinaryAssociation(
    name="body309",
    ends={
        Property(name="Statement310", type=DOM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ForStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializers314: BinaryAssociation = BinaryAssociation(
    name="initializers314",
    ends={
        Property(name="Expression316", type=DOM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ForStatement315", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updaters317: BinaryAssociation = BinaryAssociation(
    name="updaters317",
    ends={
        Property(name="Expression319", type=DOM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ForStatement318", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatement320: BinaryAssociation = BinaryAssociation(
    name="elseStatement320",
    ends={
        Property(name="Statement321", type=DOM_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_IfStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression322: BinaryAssociation = BinaryAssociation(
    name="expression322",
    ends={
        Property(name="Expression324", type=DOM_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_IfStatement323", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement325: BinaryAssociation = BinaryAssociation(
    name="thenStatement325",
    ends={
        Property(name="Statement327", type=DOM_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_IfStatement326", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body328: BinaryAssociation = BinaryAssociation(
    name="body328",
    ends={
        Property(name="Statement329", type=DOM_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_LabeledStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label330: BinaryAssociation = BinaryAssociation(
    name="label330",
    ends={
        Property(name="SimpleName332", type=DOM_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_LabeledStatement331", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression333: BinaryAssociation = BinaryAssociation(
    name="expression333",
    ends={
        Property(name="Expression334", type=DOM_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ReturnStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments335: BinaryAssociation = BinaryAssociation(
    name="arguments335",
    ends={
        Property(name="Expression336", type=DOM_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperConstructorInvocation", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression337: BinaryAssociation = BinaryAssociation(
    name="expression337",
    ends={
        Property(name="Expression339", type=DOM_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperConstructorInvocation338", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments340: BinaryAssociation = BinaryAssociation(
    name="typeArguments340",
    ends={
        Property(name="Type342", type=DOM_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperConstructorInvocation341", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression343: BinaryAssociation = BinaryAssociation(
    name="expression343",
    ends={
        Property(name="Expression344", type=DOM_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SwitchCase", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression345: BinaryAssociation = BinaryAssociation(
    name="expression345",
    ends={
        Property(name="Expression346", type=DOM_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SwitchStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements347: BinaryAssociation = BinaryAssociation(
    name="statements347",
    ends={
        Property(name="Statement349", type=DOM_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SwitchStatement348", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body350: BinaryAssociation = BinaryAssociation(
    name="body350",
    ends={
        Property(name="Block351", type=DOM_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SynchronizedStatement", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression352: BinaryAssociation = BinaryAssociation(
    name="expression352",
    ends={
        Property(name="Expression354", type=DOM_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SynchronizedStatement353", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression355: BinaryAssociation = BinaryAssociation(
    name="expression355",
    ends={
        Property(name="Expression356", type=DOM_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ThrowStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catchClauses357: BinaryAssociation = BinaryAssociation(
    name="catchClauses357",
    ends={
        Property(name="CatchClause", type=DOM_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TryStatement", type=CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body358: BinaryAssociation = BinaryAssociation(
    name="body358",
    ends={
        Property(name="Block360", type=DOM_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TryStatement359", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally361: BinaryAssociation = BinaryAssociation(
    name="finally361",
    ends={
        Property(name="Block363", type=DOM_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TryStatement362", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration364: BinaryAssociation = BinaryAssociation(
    name="declaration364",
    ends={
        Property(name="AbstractTypeDeclaration365", type=DOM_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeDeclarationStatement", type=AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments366: BinaryAssociation = BinaryAssociation(
    name="fragments366",
    ends={
        Property(name="VariableDeclarationFragment367", type=DOM_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationStatement", type=VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers368: BinaryAssociation = BinaryAssociation(
    name="modifiers368",
    ends={
        Property(name="ExtendedModifier370", type=DOM_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationStatement369", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type371: BinaryAssociation = BinaryAssociation(
    name="type371",
    ends={
        Property(name="Type373", type=DOM_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationStatement372", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body374: BinaryAssociation = BinaryAssociation(
    name="body374",
    ends={
        Property(name="Statement375", type=DOM_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_WhileStatement", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression376: BinaryAssociation = BinaryAssociation(
    name="expression376",
    ends={
        Property(name="Expression378", type=DOM_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_WhileStatement377", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
componentType379: BinaryAssociation = BinaryAssociation(
    name="componentType379",
    ends={
        Property(name="Type380", type=DOM_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType381: BinaryAssociation = BinaryAssociation(
    name="elementType381",
    ends={
        Property(name="Type383", type=DOM_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayType382", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type384: BinaryAssociation = BinaryAssociation(
    name="type384",
    ends={
        Property(name="Type385", type=DOM_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ParameterizedType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments386: BinaryAssociation = BinaryAssociation(
    name="typeArguments386",
    ends={
        Property(name="Type388", type=DOM_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ParameterizedType387", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name389: BinaryAssociation = BinaryAssociation(
    name="name389",
    ends={
        Property(name="SimpleName390", type=DOM_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_QualifiedType", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier391: BinaryAssociation = BinaryAssociation(
    name="qualifier391",
    ends={
        Property(name="Type393", type=DOM_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_QualifiedType392", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name394: BinaryAssociation = BinaryAssociation(
    name="name394",
    ends={
        Property(name="Name395", type=DOM_SimpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SimpleType", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bound396: BinaryAssociation = BinaryAssociation(
    name="bound396",
    ends={
        Property(name="Type397", type=DOM_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_WildcardType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type398: BinaryAssociation = BinaryAssociation(
    name="type398",
    ends={
        Property(name="Type399", type=DOM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SingleVariableDeclaration", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name403: BinaryAssociation = BinaryAssociation(
    name="name403",
    ends={
        Property(name="SimpleName404", type=DOM_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_QualifiedName", type=SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier405: BinaryAssociation = BinaryAssociation(
    name="qualifier405",
    ends={
        Property(name="Name407", type=DOM_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_QualifiedName406", type=Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values408: BinaryAssociation = BinaryAssociation(
    name="values408",
    ends={
        Property(name="MemberValuePair", type=DOM_NormalAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_NormalAnnotation", type=MemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers400: BinaryAssociation = BinaryAssociation(
    name="modifiers400",
    ends={
        Property(name="ExtendedModifier402", type=DOM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SingleVariableDeclaration401", type=ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value409: BinaryAssociation = BinaryAssociation(
    name="value409",
    ends={
        Property(name="Expression410", type=DOM_SingleMemberAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SingleMemberAnnotation", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Core_IJavaModel_PhysicalElement = Generalization(general=PhysicalElement, specific=Core_IJavaModel)
gen_Core_BinaryPackageFragmentRoot_IPackageFragmentRoot = Generalization(general=IPackageFragmentRoot, specific=Core_BinaryPackageFragmentRoot)
gen_Core_SourcePackageFragmentRoot_IPackageFragmentRoot = Generalization(general=IPackageFragmentRoot, specific=Core_SourcePackageFragmentRoot)
gen_Core_IPackageFragment_IJavaElement = Generalization(general=IJavaElement, specific=Core_IPackageFragment)
gen_Core_IPackageFragment_PhysicalElement = Generalization(general=PhysicalElement, specific=Core_IPackageFragment)
gen_Core_IJavaProject_IJavaElement = Generalization(general=IJavaElement, specific=Core_IJavaProject)
gen_Core_IJavaProject_PhysicalElement = Generalization(general=PhysicalElement, specific=Core_IJavaProject)
gen_Core_IPackageFragmentRoot_IJavaElement = Generalization(general=IJavaElement, specific=Core_IPackageFragmentRoot)
gen_Core_IPackageFragmentRoot_PhysicalElement = Generalization(general=PhysicalElement, specific=Core_IPackageFragmentRoot)
gen_Core_IClassFile_ITypeRoot = Generalization(general=ITypeRoot, specific=Core_IClassFile)
gen_Core_ITypeRoot_IJavaElement = Generalization(general=IJavaElement, specific=Core_ITypeRoot)
gen_Core_ITypeRoot_ISourceReference = Generalization(general=ISourceReference, specific=Core_ITypeRoot)
gen_Core_ITypeRoot_PhysicalElement = Generalization(general=PhysicalElement, specific=Core_ITypeRoot)
gen_Core_ICompilationUnit_ITypeRoot = Generalization(general=ITypeRoot, specific=Core_ICompilationUnit)
gen_Core_IMember_IJavaElement = Generalization(general=IJavaElement, specific=Core_IMember)
gen_Core_IMember_ISourceReference = Generalization(general=ISourceReference, specific=Core_IMember)
gen_Core_IType_IMember = Generalization(general=IMember, specific=Core_IType)
gen_Core_IImportDeclaration_IJavaElement = Generalization(general=IJavaElement, specific=Core_IImportDeclaration)
gen_Core_IImportDeclaration_ISourceReference = Generalization(general=ISourceReference, specific=Core_IImportDeclaration)
gen_Core_IInitializer_IMember = Generalization(general=IMember, specific=Core_IInitializer)
gen_Core_IField_IMember = Generalization(general=IMember, specific=Core_IField)
gen_Core_IMethod_IMember = Generalization(general=IMember, specific=Core_IMethod)
gen_Core_ITypeParameter_IJavaElement = Generalization(general=IJavaElement, specific=Core_ITypeParameter)
gen_Core_ITypeParameter_ISourceReference = Generalization(general=ISourceReference, specific=Core_ITypeParameter)
gen_DOM_CatchClause_ASTNode = Generalization(general=ASTNode, specific=DOM_CatchClause)
gen_DOM_Comment_ASTNode = Generalization(general=ASTNode, specific=DOM_Comment)
gen_DOM_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=DOM_AnonymousClassDeclaration)
gen_DOM_BodyDeclaration_ASTNode = Generalization(general=ASTNode, specific=DOM_BodyDeclaration)
gen_DOM_Expression_ASTNode = Generalization(general=ASTNode, specific=DOM_Expression)
gen_DOM_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=DOM_ImportDeclaration)
gen_DOM_CompilationUnit_ASTNode = Generalization(general=ASTNode, specific=DOM_CompilationUnit)
gen_DOM_MethodRef_ASTNode = Generalization(general=ASTNode, specific=DOM_MethodRef)
gen_DOM_MemberRef_ASTNode = Generalization(general=ASTNode, specific=DOM_MemberRef)
gen_DOM_MemberValuePair_ASTNode = Generalization(general=ASTNode, specific=DOM_MemberValuePair)
gen_DOM_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=DOM_MethodRefParameter)
gen_DOM_Modifier_ASTNode = Generalization(general=ASTNode, specific=DOM_Modifier)
gen_DOM_Modifier_ExtendedModifier = Generalization(general=ExtendedModifier, specific=DOM_Modifier)
gen_DOM_Statement_ASTNode = Generalization(general=ASTNode, specific=DOM_Statement)
gen_DOM_TagElement_ASTNode = Generalization(general=ASTNode, specific=DOM_TagElement)
gen_DOM_TextElement_ASTNode = Generalization(general=ASTNode, specific=DOM_TextElement)
gen_DOM_PackageDeclaration_ASTNode = Generalization(general=ASTNode, specific=DOM_PackageDeclaration)
gen_DOM_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_AbstractTypeDeclaration)
gen_DOM_Type_ASTNode = Generalization(general=ASTNode, specific=DOM_Type)
gen_DOM_TypeParameter_ASTNode = Generalization(general=ASTNode, specific=DOM_TypeParameter)
gen_DOM_VariableDeclaration_ASTNode = Generalization(general=ASTNode, specific=DOM_VariableDeclaration)
gen_DOM_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_FieldDeclaration)
gen_DOM_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_AnnotationTypeMemberDeclaration)
gen_DOM_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_EnumConstantDeclaration)
gen_DOM_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_Initializer)
gen_DOM_MethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_MethodDeclaration)
gen_DOM_BlockComment_Comment = Generalization(general=Comment, specific=DOM_BlockComment)
gen_DOM_Javadoc_Comment = Generalization(general=Comment, specific=DOM_Javadoc)
gen_DOM_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=DOM_AnnotationTypeDeclaration)
gen_DOM_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=DOM_EnumDeclaration)
gen_DOM_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=DOM_TypeDeclaration)
gen_DOM_ArrayCreation_Expression = Generalization(general=Expression, specific=DOM_ArrayCreation)
gen_DOM_LineComment_Comment = Generalization(general=Comment, specific=DOM_LineComment)
gen_DOM_Annotation_Expression = Generalization(general=Expression, specific=DOM_Annotation)
gen_DOM_Annotation_ExtendedModifier = Generalization(general=ExtendedModifier, specific=DOM_Annotation)
gen_DOM_ArrayAccess_Expression = Generalization(general=Expression, specific=DOM_ArrayAccess)
gen_DOM_ArrayInitializer_Expression = Generalization(general=Expression, specific=DOM_ArrayInitializer)
gen_DOM_BooleanLiteral_Expression = Generalization(general=Expression, specific=DOM_BooleanLiteral)
gen_DOM_Assignment_Expression = Generalization(general=Expression, specific=DOM_Assignment)
gen_DOM_CharacterLiteral_Expression = Generalization(general=Expression, specific=DOM_CharacterLiteral)
gen_DOM_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=DOM_ClassInstanceCreation)
gen_DOM_CastExpression_Expression = Generalization(general=Expression, specific=DOM_CastExpression)
gen_DOM_ConditionalExpression_Expression = Generalization(general=Expression, specific=DOM_ConditionalExpression)
gen_DOM_FieldAccess_Expression = Generalization(general=Expression, specific=DOM_FieldAccess)
gen_DOM_InfixExpression_Expression = Generalization(general=Expression, specific=DOM_InfixExpression)
gen_DOM_InstanceofExpression_Expression = Generalization(general=Expression, specific=DOM_InstanceofExpression)
gen_DOM_MethodInvocation_Expression = Generalization(general=Expression, specific=DOM_MethodInvocation)
gen_DOM_Name_Expression = Generalization(general=Expression, specific=DOM_Name)
gen_DOM_NullLiteral_Expression = Generalization(general=Expression, specific=DOM_NullLiteral)
gen_DOM_NumberLiteral_Expression = Generalization(general=Expression, specific=DOM_NumberLiteral)
gen_DOM_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=DOM_ParenthesizedExpression)
gen_DOM_PostfixExpression_Expression = Generalization(general=Expression, specific=DOM_PostfixExpression)
gen_DOM_PrefixExpression_Expression = Generalization(general=Expression, specific=DOM_PrefixExpression)
gen_DOM_StringLiteral_Expression = Generalization(general=Expression, specific=DOM_StringLiteral)
gen_DOM_SuperFieldAccess_Expression = Generalization(general=Expression, specific=DOM_SuperFieldAccess)
gen_DOM_SuperMethodInvocation_Expression = Generalization(general=Expression, specific=DOM_SuperMethodInvocation)
gen_DOM_ThisExpression_Expression = Generalization(general=Expression, specific=DOM_ThisExpression)
gen_DOM_TypeLiteral_Expression = Generalization(general=Expression, specific=DOM_TypeLiteral)
gen_DOM_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=DOM_VariableDeclarationExpression)
gen_DOM_AssertStatement_Statement = Generalization(general=Statement, specific=DOM_AssertStatement)
gen_DOM_Block_Statement = Generalization(general=Statement, specific=DOM_Block)
gen_DOM_BreakStatement_Statement = Generalization(general=Statement, specific=DOM_BreakStatement)
gen_DOM_EnhancedForStatement_Statement = Generalization(general=Statement, specific=DOM_EnhancedForStatement)
gen_DOM_ConstructorInvocation_Statement = Generalization(general=Statement, specific=DOM_ConstructorInvocation)
gen_DOM_ContinueStatement_Statement = Generalization(general=Statement, specific=DOM_ContinueStatement)
gen_DOM_DoStatement_Statement = Generalization(general=Statement, specific=DOM_DoStatement)
gen_DOM_EmptyStatement_Statement = Generalization(general=Statement, specific=DOM_EmptyStatement)
gen_DOM_ExpressionStatement_Statement = Generalization(general=Statement, specific=DOM_ExpressionStatement)
gen_DOM_ForStatement_Statement = Generalization(general=Statement, specific=DOM_ForStatement)
gen_DOM_IfStatement_Statement = Generalization(general=Statement, specific=DOM_IfStatement)
gen_DOM_LabeledStatement_Statement = Generalization(general=Statement, specific=DOM_LabeledStatement)
gen_DOM_ReturnStatement_Statement = Generalization(general=Statement, specific=DOM_ReturnStatement)
gen_DOM_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=DOM_SuperConstructorInvocation)
gen_DOM_SwitchCase_Statement = Generalization(general=Statement, specific=DOM_SwitchCase)
gen_DOM_SwitchStatement_Statement = Generalization(general=Statement, specific=DOM_SwitchStatement)
gen_DOM_SynchronizedStatement_Statement = Generalization(general=Statement, specific=DOM_SynchronizedStatement)
gen_DOM_ThrowStatement_Statement = Generalization(general=Statement, specific=DOM_ThrowStatement)
gen_DOM_TryStatement_Statement = Generalization(general=Statement, specific=DOM_TryStatement)
gen_DOM_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=DOM_TypeDeclarationStatement)
gen_DOM_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=DOM_VariableDeclarationStatement)
gen_DOM_WhileStatement_Statement = Generalization(general=Statement, specific=DOM_WhileStatement)
gen_DOM_ArrayType_Type = Generalization(general=Type, specific=DOM_ArrayType)
gen_DOM_ParameterizedType_Type = Generalization(general=Type, specific=DOM_ParameterizedType)
gen_DOM_PrimitiveType_Type = Generalization(general=Type, specific=DOM_PrimitiveType)
gen_DOM_QualifiedType_Type = Generalization(general=Type, specific=DOM_QualifiedType)
gen_DOM_SimpleType_Type = Generalization(general=Type, specific=DOM_SimpleType)
gen_DOM_WildcardType_Type = Generalization(general=Type, specific=DOM_WildcardType)
gen_DOM_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=DOM_SingleVariableDeclaration)
gen_DOM_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=DOM_VariableDeclarationFragment)
gen_DOM_QualifiedName_Name = Generalization(general=Name, specific=DOM_QualifiedName)
gen_DOM_SimpleName_Name = Generalization(general=Name, specific=DOM_SimpleName)
gen_DOM_MarkerAnnotation_Annotation = Generalization(general=Annotation, specific=DOM_MarkerAnnotation)
gen_DOM_NormalAnnotation_Annotation = Generalization(general=Annotation, specific=DOM_NormalAnnotation)
gen_DOM_SingleMemberAnnotation_Annotation = Generalization(general=Annotation, specific=DOM_SingleMemberAnnotation)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Core_PhysicalElement, Core_IJavaModel, PhysicalElement, IJavaProject, Core_IJavaElement, Core_BinaryPackageFragmentRoot, Core_SourcePackageFragmentRoot, Core_IPackageFragment, IPackageFragmentRoot, Core_IJavaProject, IJavaElement, Core_IPackageFragmentRoot, IPackageFragment, CompilationUnit, Core_IClassFile, IClassFile, ICompilationUnit, Core_ITypeRoot, ISourceReference, Core_ICompilationUnit, ITypeRoot, IType, IImportDeclaration, Core_IMember, Core_IType, IMember, IInitializer, Core_ISourceReference, ISourceRange, Core_IImportDeclaration, Core_ISourceRange, Core_IInitializer, Core_IField, Core_IMethod, IField, IMethod, ITypeParameter, Core_ITypeParameter, Parameter_, Core_Parameter, ExtendedModifier, Javadoc, DOM_CatchClause, Block, SingleVariableDeclaration, DOM_Comment, DOM_AST, ASTNode, DOM_ASTNode, DOM_AnonymousClassDeclaration, BodyDeclaration, DOM_BodyDeclaration, AbstractTypeDeclaration, DOM_Expression, DOM_ImportDeclaration, DOM_CompilationUnit, Comment, PackageDeclaration, ImportDeclaration, Expression, DOM_MethodRef, MethodRefParameter, Name, DOM_MemberRef, SimpleName, DOM_MemberValuePair, DOM_MethodRefParameter, Type, DOM_ExtendedModifier, DOM_Modifier, DOM_Statement, DOM_TagElement, DOM_TextElement, DOM_PackageDeclaration, Annotation, DOM_AbstractTypeDeclaration, DOM_Type, DOM_TypeParameter, DOM_VariableDeclaration, AnonymousClassDeclaration, DOM_FieldDeclaration, VariableDeclarationFragment, DOM_AnnotationTypeMemberDeclaration, DOM_EnumConstantDeclaration, TypeParameter, DOM_Initializer, DOM_MethodDeclaration, DOM_BlockComment, DOM_Javadoc, TagElement, DOM_AnnotationTypeDeclaration, DOM_EnumDeclaration, EnumConstantDeclaration, DOM_TypeDeclaration, DOM_ArrayCreation, ArrayInitializer, ArrayType, DOM_LineComment, DOM_Annotation, DOM_ArrayAccess, DOM_ArrayInitializer, DOM_BooleanLiteral, DOM_Assignment, DOM_CastExpression, DOM_ConditionalExpression, DOM_CharacterLiteral, DOM_ClassInstanceCreation, DOM_FieldAccess, DOM_InfixExpression, DOM_InstanceofExpression, DOM_MethodInvocation, DOM_Name, DOM_NullLiteral, DOM_NumberLiteral, DOM_ParenthesizedExpression, DOM_PostfixExpression, DOM_PrefixExpression, DOM_StringLiteral, DOM_SuperFieldAccess, DOM_SuperMethodInvocation, DOM_ThisExpression, DOM_TypeLiteral, DOM_VariableDeclarationExpression, DOM_AssertStatement, Statement, DOM_Block, DOM_BreakStatement, DOM_EnhancedForStatement, DOM_ConstructorInvocation, DOM_ContinueStatement, DOM_DoStatement, DOM_EmptyStatement, DOM_ExpressionStatement, DOM_ForStatement, DOM_IfStatement, DOM_LabeledStatement, DOM_ReturnStatement, DOM_SuperConstructorInvocation, DOM_SwitchCase, DOM_SwitchStatement, DOM_SynchronizedStatement, DOM_ThrowStatement, DOM_TryStatement, CatchClause, DOM_TypeDeclarationStatement, DOM_VariableDeclarationStatement, DOM_WhileStatement, DOM_ArrayType, DOM_ParameterizedType, DOM_PrimitiveType, DOM_QualifiedType, DOM_SimpleType, DOM_WildcardType, DOM_SingleVariableDeclaration, VariableDeclaration, DOM_VariableDeclarationFragment, DOM_QualifiedName, DOM_SimpleName, DOM_MarkerAnnotation, DOM_NormalAnnotation, MemberValuePair, DOM_SingleMemberAnnotation, Modifiers, AssignmentOperatorKind, InfixExpressionOperatorKind, PostfixExpressionOperatorKind, PrefixExpressionOperatorKind},
    associations={javaProjects0, packageFragmentRoot12, externalPackageFragmentRoots1, packageFragmentRoots3, externalPackageFragmentRoots5, requiredProjects8, packageFragments11, primary24, ast27, classFiles15, compilationUnits16, allType18, imports19, types21, javadocRange32, nameRange34, type29, initializers37, sourceRange31, fields38, methods40, types42, typeParameters45, parameters47, modifiers50, javadoc51, body53, exception54, compilationUnits48, bodyDeclarations49, imports61, types63, typeBinding65, alternateRoot56, comments58, package59, name72, value74, name76, qualifier78, parameters81, name67, name68, qualifier69, name83, type85, binding94, fragments96, annotations87, javadoc88, name91, initializer103, name105, bodyDeclarations108, name110, name98, typeBounds100, arguments121, anonymousClassDeclaration123, name125, fragments128, type129, default113, name115, type118, returnType139, parameters142, thrownExceptions145, typeParameters148, body132, body134, name136, superclassType157, superInterfaceTypes159, typeParameters162, binding150, superInterfaceTypes153, enumConstants155, index170, dimensions173, initializer175, tags165, typeName166, array168, leftHandSide181, rightHandSide183, type177, expressions179, expression186, type188, arguments191, anonymousClassDeclaration193, expression196, type199, typeArguments202, elseExpression205, expression207, thenExpression210, expression213, name215, extendedOperands218, leftOperand220, rightOperand223, leftOperand226, rightOperand228, arguments231, expression245, name236, typeArguments239, methodBinding242, expression233, operand247, operand249, name258, name251, qualifier253, arguments256, modifiers273, qualifier261, typeArguments264, qualifier267, type269, fragments271, type276, expression279, message281, statements284, label285, arguments287, typeArguments289, label292, body294, expression296, expression311, body299, expression301, parameter304, expression307, body309, initializers314, updaters317, elseStatement320, expression322, thenStatement325, body328, label330, expression333, arguments335, expression337, typeArguments340, expression343, expression345, statements347, body350, expression352, expression355, catchClauses357, body358, finally361, declaration364, fragments366, modifiers368, type371, body374, expression376, componentType379, elementType381, type384, typeArguments386, name389, qualifier391, name394, bound396, type398, name403, qualifier405, values408, modifiers400, value409},
    generalizations={gen_Core_IJavaModel_PhysicalElement, gen_Core_BinaryPackageFragmentRoot_IPackageFragmentRoot, gen_Core_SourcePackageFragmentRoot_IPackageFragmentRoot, gen_Core_IPackageFragment_IJavaElement, gen_Core_IPackageFragment_PhysicalElement, gen_Core_IJavaProject_IJavaElement, gen_Core_IJavaProject_PhysicalElement, gen_Core_IPackageFragmentRoot_IJavaElement, gen_Core_IPackageFragmentRoot_PhysicalElement, gen_Core_IClassFile_ITypeRoot, gen_Core_ITypeRoot_IJavaElement, gen_Core_ITypeRoot_ISourceReference, gen_Core_ITypeRoot_PhysicalElement, gen_Core_ICompilationUnit_ITypeRoot, gen_Core_IMember_IJavaElement, gen_Core_IMember_ISourceReference, gen_Core_IType_IMember, gen_Core_IImportDeclaration_IJavaElement, gen_Core_IImportDeclaration_ISourceReference, gen_Core_IInitializer_IMember, gen_Core_IField_IMember, gen_Core_IMethod_IMember, gen_Core_ITypeParameter_IJavaElement, gen_Core_ITypeParameter_ISourceReference, gen_DOM_CatchClause_ASTNode, gen_DOM_Comment_ASTNode, gen_DOM_AnonymousClassDeclaration_ASTNode, gen_DOM_BodyDeclaration_ASTNode, gen_DOM_Expression_ASTNode, gen_DOM_ImportDeclaration_ASTNode, gen_DOM_CompilationUnit_ASTNode, gen_DOM_MethodRef_ASTNode, gen_DOM_MemberRef_ASTNode, gen_DOM_MemberValuePair_ASTNode, gen_DOM_MethodRefParameter_ASTNode, gen_DOM_Modifier_ASTNode, gen_DOM_Modifier_ExtendedModifier, gen_DOM_Statement_ASTNode, gen_DOM_TagElement_ASTNode, gen_DOM_TextElement_ASTNode, gen_DOM_PackageDeclaration_ASTNode, gen_DOM_AbstractTypeDeclaration_BodyDeclaration, gen_DOM_Type_ASTNode, gen_DOM_TypeParameter_ASTNode, gen_DOM_VariableDeclaration_ASTNode, gen_DOM_FieldDeclaration_BodyDeclaration, gen_DOM_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_DOM_EnumConstantDeclaration_BodyDeclaration, gen_DOM_Initializer_BodyDeclaration, gen_DOM_MethodDeclaration_BodyDeclaration, gen_DOM_BlockComment_Comment, gen_DOM_Javadoc_Comment, gen_DOM_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_DOM_EnumDeclaration_AbstractTypeDeclaration, gen_DOM_TypeDeclaration_AbstractTypeDeclaration, gen_DOM_ArrayCreation_Expression, gen_DOM_LineComment_Comment, gen_DOM_Annotation_Expression, gen_DOM_Annotation_ExtendedModifier, gen_DOM_ArrayAccess_Expression, gen_DOM_ArrayInitializer_Expression, gen_DOM_BooleanLiteral_Expression, gen_DOM_Assignment_Expression, gen_DOM_CharacterLiteral_Expression, gen_DOM_ClassInstanceCreation_Expression, gen_DOM_CastExpression_Expression, gen_DOM_ConditionalExpression_Expression, gen_DOM_FieldAccess_Expression, gen_DOM_InfixExpression_Expression, gen_DOM_InstanceofExpression_Expression, gen_DOM_MethodInvocation_Expression, gen_DOM_Name_Expression, gen_DOM_NullLiteral_Expression, gen_DOM_NumberLiteral_Expression, gen_DOM_ParenthesizedExpression_Expression, gen_DOM_PostfixExpression_Expression, gen_DOM_PrefixExpression_Expression, gen_DOM_StringLiteral_Expression, gen_DOM_SuperFieldAccess_Expression, gen_DOM_SuperMethodInvocation_Expression, gen_DOM_ThisExpression_Expression, gen_DOM_TypeLiteral_Expression, gen_DOM_VariableDeclarationExpression_Expression, gen_DOM_AssertStatement_Statement, gen_DOM_Block_Statement, gen_DOM_BreakStatement_Statement, gen_DOM_EnhancedForStatement_Statement, gen_DOM_ConstructorInvocation_Statement, gen_DOM_ContinueStatement_Statement, gen_DOM_DoStatement_Statement, gen_DOM_EmptyStatement_Statement, gen_DOM_ExpressionStatement_Statement, gen_DOM_ForStatement_Statement, gen_DOM_IfStatement_Statement, gen_DOM_LabeledStatement_Statement, gen_DOM_ReturnStatement_Statement, gen_DOM_SuperConstructorInvocation_Statement, gen_DOM_SwitchCase_Statement, gen_DOM_SwitchStatement_Statement, gen_DOM_SynchronizedStatement_Statement, gen_DOM_ThrowStatement_Statement, gen_DOM_TryStatement_Statement, gen_DOM_TypeDeclarationStatement_Statement, gen_DOM_VariableDeclarationStatement_Statement, gen_DOM_WhileStatement_Statement, gen_DOM_ArrayType_Type, gen_DOM_ParameterizedType_Type, gen_DOM_PrimitiveType_Type, gen_DOM_QualifiedType_Type, gen_DOM_SimpleType_Type, gen_DOM_WildcardType_Type, gen_DOM_SingleVariableDeclaration_VariableDeclaration, gen_DOM_VariableDeclarationFragment_VariableDeclaration, gen_DOM_QualifiedName_Name, gen_DOM_SimpleName_Name, gen_DOM_MarkerAnnotation_Annotation, gen_DOM_NormalAnnotation_Annotation, gen_DOM_SingleMemberAnnotation_Annotation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)