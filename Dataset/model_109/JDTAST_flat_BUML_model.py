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
			EnumerationLiteral(name="volatile"),
			EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="annotation"),
			EnumerationLiteral(name="bridge"),
			EnumerationLiteral(name="default"),
			EnumerationLiteral(name="deprecated")
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
            EnumerationLiteral(name="less_equals"),
			EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="not_equals"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="conditional_or"),
			EnumerationLiteral(name="remainder"),
			EnumerationLiteral(name="less"),
			EnumerationLiteral(name="left_shift"),
			EnumerationLiteral(name="right_shift_unsigned"),
			EnumerationLiteral(name="conditional_and"),
			EnumerationLiteral(name="times"),
			EnumerationLiteral(name="divide"),
			EnumerationLiteral(name="greater_equals"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="right_shift_signed"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="xor")
    }
)

PrefixExpressionOperatorKind: Enumeration = Enumeration(
    name="PrefixExpressionOperatorKind",
    literals={
            EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="not"),
			EnumerationLiteral(name="decrement"),
			EnumerationLiteral(name="complement"),
			EnumerationLiteral(name="increment"),
			EnumerationLiteral(name="plus")
    }
)

PostfixExpressionOperatorKind: Enumeration = Enumeration(
    name="PostfixExpressionOperatorKind",
    literals={
            EnumerationLiteral(name="increment"),
			EnumerationLiteral(name="decrement")
    }
)

# Classes
JDTAST_PhysicalElement = Class(name="JDTAST::PhysicalElement", is_abstract=True)
JDTAST_IJavaModel = Class(name="JDTAST::IJavaModel")
PhysicalElement = Class(name="PhysicalElement")
JDTAST_IJavaProject = Class(name="JDTAST::IJavaProject")
JDTAST_IJavaElement = Class(name="JDTAST::IJavaElement", is_abstract=True)
JDTAST_IPackageFragment = Class(name="JDTAST::IPackageFragment")
JDTAST_BinaryPackageFragmentRoot = Class(name="JDTAST::BinaryPackageFragmentRoot")
IPackageFragmentRoot = Class(name="IPackageFragmentRoot")
JDTAST_SourcePackageFragmentRoot = Class(name="JDTAST::SourcePackageFragmentRoot")
JDTAST_IPackageFragmentRoot = Class(name="JDTAST::IPackageFragmentRoot", is_abstract=True)
IJavaElement = Class(name="IJavaElement")
ITypeRoot = Class(name="ITypeRoot")
JDTAST_IType = Class(name="JDTAST::IType")
JDTAST_IImportDeclaration = Class(name="JDTAST::IImportDeclaration")
JDTAST_CompilationUnit = Class(name="JDTAST::CompilationUnit")
JDTAST_IClassFile = Class(name="JDTAST::IClassFile")
JDTAST_ICompilationUnit = Class(name="JDTAST::ICompilationUnit")
JDTAST_ITypeRoot = Class(name="JDTAST::ITypeRoot", is_abstract=True)
ISourceReference = Class(name="ISourceReference")
JDTAST_ISourceReference = Class(name="JDTAST::ISourceReference", is_abstract=True)
JDTAST_ISourceRange = Class(name="JDTAST::ISourceRange")
JDTAST_IMember = Class(name="JDTAST::IMember", is_abstract=True)
JDTAST_IInitializer = Class(name="JDTAST::IInitializer")
JDTAST_IField = Class(name="JDTAST::IField")
JDTAST_IMethod = Class(name="JDTAST::IMethod")
JDTAST_ITypeParameter = Class(name="JDTAST::ITypeParameter")
IMember = Class(name="IMember")
JDTAST_Parameter = Class(name="JDTAST::Parameter")
JDTAST_AST = Class(name="JDTAST::AST")
JDTAST_ExtendedModifier = Class(name="JDTAST::ExtendedModifier", is_abstract=True)
JDTAST_Javadoc = Class(name="JDTAST::Javadoc")
JDTAST_CatchClause = Class(name="JDTAST::CatchClause")
JDTAST_Block = Class(name="JDTAST::Block")
JDTAST_SingleVariableDeclaration = Class(name="JDTAST::SingleVariableDeclaration")
JDTAST_ASTNode = Class(name="JDTAST::ASTNode", is_abstract=True)
JDTAST_AnonymousClassDeclaration = Class(name="JDTAST::AnonymousClassDeclaration")
ASTNode = Class(name="ASTNode")
JDTAST_BodyDeclaration = Class(name="JDTAST::BodyDeclaration", is_abstract=True)
JDTAST_PackageDeclaration = Class(name="JDTAST::PackageDeclaration")
JDTAST_ImportDeclaration = Class(name="JDTAST::ImportDeclaration")
JDTAST_AbstractTypeDeclaration = Class(name="JDTAST::AbstractTypeDeclaration", is_abstract=True)
JDTAST_Expression = Class(name="JDTAST::Expression", is_abstract=True)
JDTAST_Comment = Class(name="JDTAST::Comment", is_abstract=True)
JDTAST_Name = Class(name="JDTAST::Name", is_abstract=True)
JDTAST_MemberRef = Class(name="JDTAST::MemberRef")
JDTAST_SimpleName = Class(name="JDTAST::SimpleName")
JDTAST_MethodRef = Class(name="JDTAST::MethodRef")
JDTAST_MethodRefParameter = Class(name="JDTAST::MethodRefParameter")
JDTAST_MemberValuePair = Class(name="JDTAST::MemberValuePair")
JDTAST_Modifier = Class(name="JDTAST::Modifier")
ExtendedModifier = Class(name="ExtendedModifier")
JDTAST_Type = Class(name="JDTAST::Type", is_abstract=True)
JDTAST_Annotation = Class(name="JDTAST::Annotation", is_abstract=True)
JDTAST_Statement = Class(name="JDTAST::Statement", is_abstract=True)
JDTAST_TextElement = Class(name="JDTAST::TextElement")
JDTAST_TypeParameter = Class(name="JDTAST::TypeParameter")
JDTAST_VariableDeclaration = Class(name="JDTAST::VariableDeclaration", is_abstract=True)
JDTAST_TagElement = Class(name="JDTAST::TagElement")
BodyDeclaration = Class(name="BodyDeclaration")
JDTAST_AnnotationTypeMemberDeclaration = Class(name="JDTAST::AnnotationTypeMemberDeclaration")
JDTAST_EnumConstantDeclaration = Class(name="JDTAST::EnumConstantDeclaration")
JDTAST_FieldDeclaration = Class(name="JDTAST::FieldDeclaration")
JDTAST_VariableDeclarationFragment = Class(name="JDTAST::VariableDeclarationFragment")
JDTAST_MethodDeclaration = Class(name="JDTAST::MethodDeclaration")
JDTAST_Initializer = Class(name="JDTAST::Initializer")
JDTAST_AnnotationTypeDeclaration = Class(name="JDTAST::AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
JDTAST_EnumDeclaration = Class(name="JDTAST::EnumDeclaration")
JDTAST_BlockComment = Class(name="JDTAST::BlockComment")
Comment = Class(name="Comment")
JDTAST_TypeDeclaration = Class(name="JDTAST::TypeDeclaration")
JDTAST_ArrayCreation = Class(name="JDTAST::ArrayCreation")
JDTAST_ArrayInitializer = Class(name="JDTAST::ArrayInitializer")
JDTAST_ArrayType = Class(name="JDTAST::ArrayType")
JDTAST_LineComment = Class(name="JDTAST::LineComment")
Expression = Class(name="Expression")
JDTAST_ArrayAccess = Class(name="JDTAST::ArrayAccess")
JDTAST_BooleanLiteral = Class(name="JDTAST::BooleanLiteral")
JDTAST_CastExpression = Class(name="JDTAST::CastExpression")
JDTAST_Assignment = Class(name="JDTAST::Assignment")
JDTAST_ClassInstanceCreation = Class(name="JDTAST::ClassInstanceCreation")
JDTAST_ConditionalExpression = Class(name="JDTAST::ConditionalExpression")
JDTAST_CharacterLiteral = Class(name="JDTAST::CharacterLiteral")
JDTAST_FieldAccess = Class(name="JDTAST::FieldAccess")
JDTAST_InfixExpression = Class(name="JDTAST::InfixExpression")
JDTAST_InstanceofExpression = Class(name="JDTAST::InstanceofExpression")
JDTAST_MethodInvocation = Class(name="JDTAST::MethodInvocation")
JDTAST_NullLiteral = Class(name="JDTAST::NullLiteral")
JDTAST_NumberLiteral = Class(name="JDTAST::NumberLiteral")
JDTAST_ParenthesizedExpression = Class(name="JDTAST::ParenthesizedExpression")
JDTAST_PostfixExpression = Class(name="JDTAST::PostfixExpression")
JDTAST_PrefixExpression = Class(name="JDTAST::PrefixExpression")
JDTAST_StringLiteral = Class(name="JDTAST::StringLiteral")
JDTAST_SuperFieldAccess = Class(name="JDTAST::SuperFieldAccess")
JDTAST_SuperMethodInvocation = Class(name="JDTAST::SuperMethodInvocation")
JDTAST_TypeLiteral = Class(name="JDTAST::TypeLiteral")
JDTAST_VariableDeclarationExpression = Class(name="JDTAST::VariableDeclarationExpression")
JDTAST_ThisExpression = Class(name="JDTAST::ThisExpression")
JDTAST_BreakStatement = Class(name="JDTAST::BreakStatement")
JDTAST_AssertStatement = Class(name="JDTAST::AssertStatement")
Statement = Class(name="Statement")
JDTAST_ContinueStatement = Class(name="JDTAST::ContinueStatement")
JDTAST_DoStatement = Class(name="JDTAST::DoStatement")
JDTAST_ConstructorInvocation = Class(name="JDTAST::ConstructorInvocation")
JDTAST_ExpressionStatement = Class(name="JDTAST::ExpressionStatement")
JDTAST_EmptyStatement = Class(name="JDTAST::EmptyStatement")
JDTAST_EnhancedForStatement = Class(name="JDTAST::EnhancedForStatement")
JDTAST_ForStatement = Class(name="JDTAST::ForStatement")
JDTAST_IfStatement = Class(name="JDTAST::IfStatement")
JDTAST_LabeledStatement = Class(name="JDTAST::LabeledStatement")
JDTAST_ReturnStatement = Class(name="JDTAST::ReturnStatement")
JDTAST_SuperConstructorInvocation = Class(name="JDTAST::SuperConstructorInvocation")
JDTAST_SwitchCase = Class(name="JDTAST::SwitchCase")
JDTAST_SwitchStatement = Class(name="JDTAST::SwitchStatement")
JDTAST_SynchronizedStatement = Class(name="JDTAST::SynchronizedStatement")
JDTAST_ThrowStatement = Class(name="JDTAST::ThrowStatement")
JDTAST_TryStatement = Class(name="JDTAST::TryStatement")
JDTAST_TypeDeclarationStatement = Class(name="JDTAST::TypeDeclarationStatement")
JDTAST_VariableDeclarationStatement = Class(name="JDTAST::VariableDeclarationStatement")
JDTAST_WhileStatement = Class(name="JDTAST::WhileStatement")
Type = Class(name="Type")
JDTAST_ParameterizedType = Class(name="JDTAST::ParameterizedType")
JDTAST_QualifiedName = Class(name="JDTAST::QualifiedName")
Name = Class(name="Name")
JDTAST_PrimitiveType = Class(name="JDTAST::PrimitiveType")
JDTAST_QualifiedType = Class(name="JDTAST::QualifiedType")
JDTAST_SimpleType = Class(name="JDTAST::SimpleType")
JDTAST_WildcardType = Class(name="JDTAST::WildcardType")
VariableDeclaration = Class(name="VariableDeclaration")
JDTAST_MarkerAnnotation = Class(name="JDTAST::MarkerAnnotation")
Annotation = Class(name="Annotation")
JDTAST_NormalAnnotation = Class(name="JDTAST::NormalAnnotation")
JDTAST_SingleMemberAnnotation = Class(name="JDTAST::SingleMemberAnnotation")

# JDTAST_PhysicalElement class attributes and methods
JDTAST_PhysicalElement_path: Property = Property(name="path", type=StringType)
JDTAST_PhysicalElement_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
JDTAST_PhysicalElement.attributes={JDTAST_PhysicalElement_isReadOnly, JDTAST_PhysicalElement_path}

# JDTAST_IJavaModel class attributes and methods

# PhysicalElement class attributes and methods

# JDTAST_IJavaProject class attributes and methods

# JDTAST_IJavaElement class attributes and methods
JDTAST_IJavaElement_elementName: Property = Property(name="elementName", type=StringType)
JDTAST_IJavaElement.attributes={JDTAST_IJavaElement_elementName}

# JDTAST_IPackageFragment class attributes and methods
JDTAST_IPackageFragment_isDefaultPackage: Property = Property(name="isDefaultPackage", type=StringType)
JDTAST_IPackageFragment.attributes={JDTAST_IPackageFragment_isDefaultPackage}

# JDTAST_BinaryPackageFragmentRoot class attributes and methods

# IPackageFragmentRoot class attributes and methods

# JDTAST_SourcePackageFragmentRoot class attributes and methods

# JDTAST_IPackageFragmentRoot class attributes and methods

# IJavaElement class attributes and methods

# ITypeRoot class attributes and methods

# JDTAST_IType class attributes and methods
JDTAST_IType_fullyQualifiedParametrizedName: Property = Property(name="fullyQualifiedParametrizedName", type=StringType)
JDTAST_IType_fullyQualifiedName: Property = Property(name="fullyQualifiedName", type=StringType)
JDTAST_IType.attributes={JDTAST_IType_fullyQualifiedParametrizedName, JDTAST_IType_fullyQualifiedName}

# JDTAST_IImportDeclaration class attributes and methods
JDTAST_IImportDeclaration_isOnDemand: Property = Property(name="isOnDemand", type=StringType)
JDTAST_IImportDeclaration_isStatic: Property = Property(name="isStatic", type=StringType)
JDTAST_IImportDeclaration.attributes={JDTAST_IImportDeclaration_isStatic, JDTAST_IImportDeclaration_isOnDemand}

# JDTAST_CompilationUnit class attributes and methods

# JDTAST_IClassFile class attributes and methods
JDTAST_IClassFile_isClass: Property = Property(name="isClass", type=StringType)
JDTAST_IClassFile_isInterface: Property = Property(name="isInterface", type=StringType)
JDTAST_IClassFile.attributes={JDTAST_IClassFile_isInterface, JDTAST_IClassFile_isClass}

# JDTAST_ICompilationUnit class attributes and methods

# JDTAST_ITypeRoot class attributes and methods

# ISourceReference class attributes and methods

# JDTAST_ISourceReference class attributes and methods
JDTAST_ISourceReference_source: Property = Property(name="source", type=StringType)
JDTAST_ISourceReference.attributes={JDTAST_ISourceReference_source}

# JDTAST_ISourceRange class attributes and methods
JDTAST_ISourceRange_length: Property = Property(name="length", type=StringType)
JDTAST_ISourceRange_offset: Property = Property(name="offset", type=StringType)
JDTAST_ISourceRange.attributes={JDTAST_ISourceRange_length, JDTAST_ISourceRange_offset}

# JDTAST_IMember class attributes and methods

# JDTAST_IInitializer class attributes and methods

# JDTAST_IField class attributes and methods
JDTAST_IField_isTransient: Property = Property(name="isTransient", type=StringType)
JDTAST_IField_constant: Property = Property(name="constant", type=StringType)
JDTAST_IField_isEnumConstant: Property = Property(name="isEnumConstant", type=StringType)
JDTAST_IField_typeSignature: Property = Property(name="typeSignature", type=StringType)
JDTAST_IField_isVolatile: Property = Property(name="isVolatile", type=StringType)
JDTAST_IField.attributes={JDTAST_IField_isTransient, JDTAST_IField_typeSignature, JDTAST_IField_constant, JDTAST_IField_isVolatile, JDTAST_IField_isEnumConstant}

# JDTAST_IMethod class attributes and methods
JDTAST_IMethod_returnType: Property = Property(name="returnType", type=StringType)
JDTAST_IMethod_isConstructor: Property = Property(name="isConstructor", type=StringType)
JDTAST_IMethod_isMainMethod: Property = Property(name="isMainMethod", type=StringType)
JDTAST_IMethod_exceptionTypes: Property = Property(name="exceptionTypes", type=StringType)
JDTAST_IMethod.attributes={JDTAST_IMethod_returnType, JDTAST_IMethod_isConstructor, JDTAST_IMethod_isMainMethod, JDTAST_IMethod_exceptionTypes}

# JDTAST_ITypeParameter class attributes and methods
JDTAST_ITypeParameter_bounds: Property = Property(name="bounds", type=StringType)
JDTAST_ITypeParameter.attributes={JDTAST_ITypeParameter_bounds}

# IMember class attributes and methods

# JDTAST_Parameter class attributes and methods
JDTAST_Parameter_name: Property = Property(name="name", type=StringType)
JDTAST_Parameter_type: Property = Property(name="type", type=StringType)
JDTAST_Parameter.attributes={JDTAST_Parameter_type, JDTAST_Parameter_name}

# JDTAST_AST class attributes and methods

# JDTAST_ExtendedModifier class attributes and methods

# JDTAST_Javadoc class attributes and methods

# JDTAST_CatchClause class attributes and methods

# JDTAST_Block class attributes and methods

# JDTAST_SingleVariableDeclaration class attributes and methods
JDTAST_SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=StringType)
JDTAST_SingleVariableDeclaration.attributes={JDTAST_SingleVariableDeclaration_varargs}

# JDTAST_ASTNode class attributes and methods

# JDTAST_AnonymousClassDeclaration class attributes and methods

# ASTNode class attributes and methods

# JDTAST_BodyDeclaration class attributes and methods

# JDTAST_PackageDeclaration class attributes and methods

# JDTAST_ImportDeclaration class attributes and methods
JDTAST_ImportDeclaration_onDemand: Property = Property(name="onDemand", type=StringType)
JDTAST_ImportDeclaration_static: Property = Property(name="static", type=StringType)
JDTAST_ImportDeclaration.attributes={JDTAST_ImportDeclaration_onDemand, JDTAST_ImportDeclaration_static}

# JDTAST_AbstractTypeDeclaration class attributes and methods
JDTAST_AbstractTypeDeclaration_localTypeDeclaration: Property = Property(name="localTypeDeclaration", type=StringType)
JDTAST_AbstractTypeDeclaration_memberTypeDeclaration: Property = Property(name="memberTypeDeclaration", type=StringType)
JDTAST_AbstractTypeDeclaration_packageMemberTypeDeclaration: Property = Property(name="packageMemberTypeDeclaration", type=StringType)
JDTAST_AbstractTypeDeclaration.attributes={JDTAST_AbstractTypeDeclaration_packageMemberTypeDeclaration, JDTAST_AbstractTypeDeclaration_localTypeDeclaration, JDTAST_AbstractTypeDeclaration_memberTypeDeclaration}

# JDTAST_Expression class attributes and methods
JDTAST_Expression_resolveBoxing: Property = Property(name="resolveBoxing", type=StringType)
JDTAST_Expression_resolveUnboxing: Property = Property(name="resolveUnboxing", type=StringType)
JDTAST_Expression.attributes={JDTAST_Expression_resolveUnboxing, JDTAST_Expression_resolveBoxing}

# JDTAST_Comment class attributes and methods

# JDTAST_Name class attributes and methods
JDTAST_Name_fullyQualifiedName: Property = Property(name="fullyQualifiedName", type=StringType)
JDTAST_Name.attributes={JDTAST_Name_fullyQualifiedName}

# JDTAST_MemberRef class attributes and methods

# JDTAST_SimpleName class attributes and methods
JDTAST_SimpleName_identifier: Property = Property(name="identifier", type=StringType)
JDTAST_SimpleName_declaration: Property = Property(name="declaration", type=StringType)
JDTAST_SimpleName.attributes={JDTAST_SimpleName_declaration, JDTAST_SimpleName_identifier}

# JDTAST_MethodRef class attributes and methods

# JDTAST_MethodRefParameter class attributes and methods
JDTAST_MethodRefParameter_varargs: Property = Property(name="varargs", type=StringType)
JDTAST_MethodRefParameter.attributes={JDTAST_MethodRefParameter_varargs}

# JDTAST_MemberValuePair class attributes and methods

# JDTAST_Modifier class attributes and methods
JDTAST_Modifier_abstract: Property = Property(name="abstract", type=StringType)
JDTAST_Modifier_final: Property = Property(name="final", type=StringType)
JDTAST_Modifier_native: Property = Property(name="native", type=StringType)
JDTAST_Modifier_none: Property = Property(name="none", type=StringType)
JDTAST_Modifier_private: Property = Property(name="private", type=StringType)
JDTAST_Modifier_protected: Property = Property(name="protected", type=StringType)
JDTAST_Modifier_public: Property = Property(name="public", type=StringType)
JDTAST_Modifier_static: Property = Property(name="static", type=StringType)
JDTAST_Modifier_strictfp: Property = Property(name="strictfp", type=StringType)
JDTAST_Modifier_synchronized: Property = Property(name="synchronized", type=StringType)
JDTAST_Modifier_transient: Property = Property(name="transient", type=StringType)
JDTAST_Modifier_volatile: Property = Property(name="volatile", type=StringType)
JDTAST_Modifier.attributes={JDTAST_Modifier_strictfp, JDTAST_Modifier_volatile, JDTAST_Modifier_native, JDTAST_Modifier_none, JDTAST_Modifier_synchronized, JDTAST_Modifier_static, JDTAST_Modifier_protected, JDTAST_Modifier_private, JDTAST_Modifier_abstract, JDTAST_Modifier_transient, JDTAST_Modifier_final, JDTAST_Modifier_public}

# ExtendedModifier class attributes and methods

# JDTAST_Type class attributes and methods

# JDTAST_Annotation class attributes and methods

# JDTAST_Statement class attributes and methods

# JDTAST_TextElement class attributes and methods
JDTAST_TextElement_text: Property = Property(name="text", type=StringType)
JDTAST_TextElement.attributes={JDTAST_TextElement_text}

# JDTAST_TypeParameter class attributes and methods

# JDTAST_VariableDeclaration class attributes and methods
JDTAST_VariableDeclaration_extraDimensions: Property = Property(name="extraDimensions", type=StringType)
JDTAST_VariableDeclaration.attributes={JDTAST_VariableDeclaration_extraDimensions}

# JDTAST_TagElement class attributes and methods
JDTAST_TagElement_nested: Property = Property(name="nested", type=StringType)
JDTAST_TagElement_tagName: Property = Property(name="tagName", type=StringType)
JDTAST_TagElement.attributes={JDTAST_TagElement_nested, JDTAST_TagElement_tagName}

# BodyDeclaration class attributes and methods

# JDTAST_AnnotationTypeMemberDeclaration class attributes and methods

# JDTAST_EnumConstantDeclaration class attributes and methods

# JDTAST_FieldDeclaration class attributes and methods

# JDTAST_VariableDeclarationFragment class attributes and methods

# JDTAST_MethodDeclaration class attributes and methods
JDTAST_MethodDeclaration_extraDimensions: Property = Property(name="extraDimensions", type=StringType)
JDTAST_MethodDeclaration_constructor: Property = Property(name="constructor", type=StringType)
JDTAST_MethodDeclaration_varargs: Property = Property(name="varargs", type=StringType)
JDTAST_MethodDeclaration.attributes={JDTAST_MethodDeclaration_extraDimensions, JDTAST_MethodDeclaration_constructor, JDTAST_MethodDeclaration_varargs}

# JDTAST_Initializer class attributes and methods

# JDTAST_AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# JDTAST_EnumDeclaration class attributes and methods

# JDTAST_BlockComment class attributes and methods

# Comment class attributes and methods

# JDTAST_TypeDeclaration class attributes and methods
JDTAST_TypeDeclaration_interface: Property = Property(name="interface", type=StringType)
JDTAST_TypeDeclaration.attributes={JDTAST_TypeDeclaration_interface}

# JDTAST_ArrayCreation class attributes and methods

# JDTAST_ArrayInitializer class attributes and methods

# JDTAST_ArrayType class attributes and methods
JDTAST_ArrayType_dimensions: Property = Property(name="dimensions", type=StringType)
JDTAST_ArrayType.attributes={JDTAST_ArrayType_dimensions}

# JDTAST_LineComment class attributes and methods

# Expression class attributes and methods

# JDTAST_ArrayAccess class attributes and methods

# JDTAST_BooleanLiteral class attributes and methods
JDTAST_BooleanLiteral_booleanValue: Property = Property(name="booleanValue", type=StringType)
JDTAST_BooleanLiteral.attributes={JDTAST_BooleanLiteral_booleanValue}

# JDTAST_CastExpression class attributes and methods

# JDTAST_Assignment class attributes and methods
JDTAST_Assignment_operator: Property = Property(name="operator", type=StringType)
JDTAST_Assignment.attributes={JDTAST_Assignment_operator}

# JDTAST_ClassInstanceCreation class attributes and methods

# JDTAST_ConditionalExpression class attributes and methods

# JDTAST_CharacterLiteral class attributes and methods
JDTAST_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
JDTAST_CharacterLiteral_charValue: Property = Property(name="charValue", type=StringType)
JDTAST_CharacterLiteral.attributes={JDTAST_CharacterLiteral_charValue, JDTAST_CharacterLiteral_escapedValue}

# JDTAST_FieldAccess class attributes and methods

# JDTAST_InfixExpression class attributes and methods
JDTAST_InfixExpression_operator: Property = Property(name="operator", type=StringType)
JDTAST_InfixExpression.attributes={JDTAST_InfixExpression_operator}

# JDTAST_InstanceofExpression class attributes and methods

# JDTAST_MethodInvocation class attributes and methods

# JDTAST_NullLiteral class attributes and methods

# JDTAST_NumberLiteral class attributes and methods
JDTAST_NumberLiteral_token: Property = Property(name="token", type=StringType)
JDTAST_NumberLiteral.attributes={JDTAST_NumberLiteral_token}

# JDTAST_ParenthesizedExpression class attributes and methods

# JDTAST_PostfixExpression class attributes and methods
JDTAST_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
JDTAST_PostfixExpression.attributes={JDTAST_PostfixExpression_operator}

# JDTAST_PrefixExpression class attributes and methods
JDTAST_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
JDTAST_PrefixExpression.attributes={JDTAST_PrefixExpression_operator}

# JDTAST_StringLiteral class attributes and methods
JDTAST_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
JDTAST_StringLiteral_literalValue: Property = Property(name="literalValue", type=StringType)
JDTAST_StringLiteral.attributes={JDTAST_StringLiteral_literalValue, JDTAST_StringLiteral_escapedValue}

# JDTAST_SuperFieldAccess class attributes and methods

# JDTAST_SuperMethodInvocation class attributes and methods

# JDTAST_TypeLiteral class attributes and methods

# JDTAST_VariableDeclarationExpression class attributes and methods

# JDTAST_ThisExpression class attributes and methods

# JDTAST_BreakStatement class attributes and methods

# JDTAST_AssertStatement class attributes and methods

# Statement class attributes and methods

# JDTAST_ContinueStatement class attributes and methods

# JDTAST_DoStatement class attributes and methods

# JDTAST_ConstructorInvocation class attributes and methods

# JDTAST_ExpressionStatement class attributes and methods

# JDTAST_EmptyStatement class attributes and methods

# JDTAST_EnhancedForStatement class attributes and methods

# JDTAST_ForStatement class attributes and methods

# JDTAST_IfStatement class attributes and methods

# JDTAST_LabeledStatement class attributes and methods

# JDTAST_ReturnStatement class attributes and methods

# JDTAST_SuperConstructorInvocation class attributes and methods

# JDTAST_SwitchCase class attributes and methods
JDTAST_SwitchCase_default: Property = Property(name="default", type=StringType)
JDTAST_SwitchCase.attributes={JDTAST_SwitchCase_default}

# JDTAST_SwitchStatement class attributes and methods

# JDTAST_SynchronizedStatement class attributes and methods

# JDTAST_ThrowStatement class attributes and methods

# JDTAST_TryStatement class attributes and methods

# JDTAST_TypeDeclarationStatement class attributes and methods

# JDTAST_VariableDeclarationStatement class attributes and methods

# JDTAST_WhileStatement class attributes and methods

# Type class attributes and methods

# JDTAST_ParameterizedType class attributes and methods

# JDTAST_QualifiedName class attributes and methods

# Name class attributes and methods

# JDTAST_PrimitiveType class attributes and methods
JDTAST_PrimitiveType_code: Property = Property(name="code", type=StringType)
JDTAST_PrimitiveType.attributes={JDTAST_PrimitiveType_code}

# JDTAST_QualifiedType class attributes and methods

# JDTAST_SimpleType class attributes and methods

# JDTAST_WildcardType class attributes and methods
JDTAST_WildcardType_upperBound: Property = Property(name="upperBound", type=StringType)
JDTAST_WildcardType.attributes={JDTAST_WildcardType_upperBound}

# VariableDeclaration class attributes and methods

# JDTAST_MarkerAnnotation class attributes and methods

# Annotation class attributes and methods

# JDTAST_NormalAnnotation class attributes and methods

# JDTAST_SingleMemberAnnotation class attributes and methods

# Relationships
javaProjects0: BinaryAssociation = BinaryAssociation(
    name="javaProjects0",
    ends={
        Property(name="JDTAST_IJavaProject", type=JDTAST_IJavaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IJavaModel", type=JDTAST_IJavaProject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalPackageFragmentRoots6: BinaryAssociation = BinaryAssociation(
    name="externalPackageFragmentRoots6",
    ends={
        Property(name="JDTAST_IPackageFragmentRoot8", type=JDTAST_IJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IJavaProject7", type=JDTAST_IPackageFragmentRoot, multiplicity=Multiplicity(0, 9999))
    }
)
requiredProjects10: BinaryAssociation = BinaryAssociation(
    name="requiredProjects10",
    ends={
        Property(name="JDTAST_IJavaProject11", type=JDTAST_IJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IJavaProject9", type=JDTAST_IJavaProject, multiplicity=Multiplicity(0, 9999))
    }
)
packageFragments12: BinaryAssociation = BinaryAssociation(
    name="packageFragments12",
    ends={
        Property(name="IPackageFragment", type=JDTAST_IPackageFragmentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="packageFragmentRoot", type=JDTAST_IPackageFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageFragmentRoot13: BinaryAssociation = BinaryAssociation(
    name="packageFragmentRoot13",
    ends={
        Property(name="IPackageFragmentRoot", type=JDTAST_IPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="packageFragments", type=JDTAST_IPackageFragmentRoot, multiplicity=Multiplicity(1, 1))
    }
)
externalPackageFragmentRoots1: BinaryAssociation = BinaryAssociation(
    name="externalPackageFragmentRoots1",
    ends={
        Property(name="JDTAST_IPackageFragmentRoot", type=JDTAST_IJavaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IJavaModel2", type=JDTAST_IPackageFragmentRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageFragmentRoots3: BinaryAssociation = BinaryAssociation(
    name="packageFragmentRoots3",
    ends={
        Property(name="JDTAST_IPackageFragmentRoot5", type=JDTAST_IJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IJavaProject4", type=JDTAST_IPackageFragmentRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allType17: BinaryAssociation = BinaryAssociation(
    name="allType17",
    ends={
        Property(name="JDTAST_IType", type=JDTAST_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ICompilationUnit18", type=JDTAST_IType, multiplicity=Multiplicity(0, 9999))
    }
)
imports19: BinaryAssociation = BinaryAssociation(
    name="imports19",
    ends={
        Property(name="JDTAST_IImportDeclaration", type=JDTAST_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ICompilationUnit20", type=JDTAST_IImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types21: BinaryAssociation = BinaryAssociation(
    name="types21",
    ends={
        Property(name="JDTAST_IType23", type=JDTAST_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ICompilationUnit22", type=JDTAST_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primary25: BinaryAssociation = BinaryAssociation(
    name="primary25",
    ends={
        Property(name="JDTAST_ICompilationUnit26", type=JDTAST_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ICompilationUnit24", type=JDTAST_ICompilationUnit, multiplicity=Multiplicity(1, 1))
    }
)
ast27: BinaryAssociation = BinaryAssociation(
    name="ast27",
    ends={
        Property(name="JDTAST_CompilationUnit", type=JDTAST_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ICompilationUnit28", type=JDTAST_CompilationUnit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classFiles14: BinaryAssociation = BinaryAssociation(
    name="classFiles14",
    ends={
        Property(name="JDTAST_IClassFile", type=JDTAST_IPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IPackageFragment", type=JDTAST_IClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits15: BinaryAssociation = BinaryAssociation(
    name="compilationUnits15",
    ends={
        Property(name="JDTAST_ICompilationUnit", type=JDTAST_IPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IPackageFragment16", type=JDTAST_ICompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="JDTAST_IType31", type=JDTAST_IClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IClassFile30", type=JDTAST_IType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceRange32: BinaryAssociation = BinaryAssociation(
    name="sourceRange32",
    ends={
        Property(name="JDTAST_ISourceRange", type=JDTAST_ISourceReference, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ISourceReference", type=JDTAST_ISourceRange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializers38: BinaryAssociation = BinaryAssociation(
    name="initializers38",
    ends={
        Property(name="JDTAST_IInitializer", type=JDTAST_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IType39", type=JDTAST_IInitializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields40: BinaryAssociation = BinaryAssociation(
    name="fields40",
    ends={
        Property(name="JDTAST_IField", type=JDTAST_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IType41", type=JDTAST_IField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods42: BinaryAssociation = BinaryAssociation(
    name="methods42",
    ends={
        Property(name="JDTAST_IMethod", type=JDTAST_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IType43", type=JDTAST_IMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types45: BinaryAssociation = BinaryAssociation(
    name="types45",
    ends={
        Property(name="JDTAST_IType46", type=JDTAST_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IType44", type=JDTAST_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters47: BinaryAssociation = BinaryAssociation(
    name="typeParameters47",
    ends={
        Property(name="JDTAST_ITypeParameter", type=JDTAST_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IType48", type=JDTAST_ITypeParameter, multiplicity=Multiplicity(0, 9999))
    }
)
javadocRange33: BinaryAssociation = BinaryAssociation(
    name="javadocRange33",
    ends={
        Property(name="JDTAST_ISourceRange34", type=JDTAST_IMember, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IMember", type=JDTAST_ISourceRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameRange35: BinaryAssociation = BinaryAssociation(
    name="nameRange35",
    ends={
        Property(name="JDTAST_ISourceRange37", type=JDTAST_IMember, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IMember36", type=JDTAST_ISourceRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters49: BinaryAssociation = BinaryAssociation(
    name="parameters49",
    ends={
        Property(name="JDTAST_Parameter", type=JDTAST_IMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IMethod50", type=JDTAST_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations52: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations52",
    ends={
        Property(name="JDTAST_AnonymousClassDeclaration", type=JDTAST_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="JDTAST_BodyDeclaration", type=JDTAST_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
modifiers53: BinaryAssociation = BinaryAssociation(
    name="modifiers53",
    ends={
        Property(name="JDTAST_ExtendedModifier", type=JDTAST_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_BodyDeclaration54", type=JDTAST_ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc55: BinaryAssociation = BinaryAssociation(
    name="javadoc55",
    ends={
        Property(name="JDTAST_Javadoc", type=JDTAST_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_BodyDeclaration56", type=JDTAST_Javadoc, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body57: BinaryAssociation = BinaryAssociation(
    name="body57",
    ends={
        Property(name="JDTAST_Block", type=JDTAST_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_CatchClause", type=JDTAST_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compilationUnits51: BinaryAssociation = BinaryAssociation(
    name="compilationUnits51",
    ends={
        Property(name="JDTAST_ASTNode", type=JDTAST_AST, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_AST", type=JDTAST_ASTNode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comments62: BinaryAssociation = BinaryAssociation(
    name="comments62",
    ends={
        Property(name="JDTAST_Comment64", type=JDTAST_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_CompilationUnit63", type=JDTAST_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package65: BinaryAssociation = BinaryAssociation(
    name="package65",
    ends={
        Property(name="JDTAST_PackageDeclaration", type=JDTAST_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_CompilationUnit66", type=JDTAST_PackageDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imports67: BinaryAssociation = BinaryAssociation(
    name="imports67",
    ends={
        Property(name="JDTAST_ImportDeclaration", type=JDTAST_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_CompilationUnit68", type=JDTAST_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types69: BinaryAssociation = BinaryAssociation(
    name="types69",
    ends={
        Property(name="JDTAST_AbstractTypeDeclaration", type=JDTAST_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_CompilationUnit70", type=JDTAST_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception58: BinaryAssociation = BinaryAssociation(
    name="exception58",
    ends={
        Property(name="JDTAST_SingleVariableDeclaration", type=JDTAST_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_CatchClause59", type=JDTAST_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alternateRoot60: BinaryAssociation = BinaryAssociation(
    name="alternateRoot60",
    ends={
        Property(name="JDTAST_ASTNode61", type=JDTAST_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_Comment", type=JDTAST_ASTNode, multiplicity=Multiplicity(1, 1))
    }
)
name73: BinaryAssociation = BinaryAssociation(
    name="name73",
    ends={
        Property(name="JDTAST_Name", type=JDTAST_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ImportDeclaration74", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name75: BinaryAssociation = BinaryAssociation(
    name="name75",
    ends={
        Property(name="JDTAST_SimpleName", type=JDTAST_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MemberRef", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier76: BinaryAssociation = BinaryAssociation(
    name="qualifier76",
    ends={
        Property(name="JDTAST_Name78", type=JDTAST_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MemberRef77", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeBinding71: BinaryAssociation = BinaryAssociation(
    name="typeBinding71",
    ends={
        Property(name="JDTAST_IType72", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_Expression", type=JDTAST_IType, multiplicity=Multiplicity(1, 1))
    }
)
name84: BinaryAssociation = BinaryAssociation(
    name="name84",
    ends={
        Property(name="JDTAST_SimpleName85", type=JDTAST_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodRef", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier86: BinaryAssociation = BinaryAssociation(
    name="qualifier86",
    ends={
        Property(name="JDTAST_Name88", type=JDTAST_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodRef87", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters89: BinaryAssociation = BinaryAssociation(
    name="parameters89",
    ends={
        Property(name="JDTAST_MethodRefParameter", type=JDTAST_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodRef90", type=JDTAST_MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name91: BinaryAssociation = BinaryAssociation(
    name="name91",
    ends={
        Property(name="JDTAST_SimpleName93", type=JDTAST_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodRefParameter92", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name79: BinaryAssociation = BinaryAssociation(
    name="name79",
    ends={
        Property(name="JDTAST_SimpleName80", type=JDTAST_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MemberValuePair", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value81: BinaryAssociation = BinaryAssociation(
    name="value81",
    ends={
        Property(name="JDTAST_Expression83", type=JDTAST_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MemberValuePair82", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type94: BinaryAssociation = BinaryAssociation(
    name="type94",
    ends={
        Property(name="JDTAST_Type", type=JDTAST_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodRefParameter95", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations96: BinaryAssociation = BinaryAssociation(
    name="annotations96",
    ends={
        Property(name="JDTAST_Annotation", type=JDTAST_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_PackageDeclaration97", type=JDTAST_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc98: BinaryAssociation = BinaryAssociation(
    name="javadoc98",
    ends={
        Property(name="JDTAST_Javadoc100", type=JDTAST_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_PackageDeclaration99", type=JDTAST_Javadoc, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name101: BinaryAssociation = BinaryAssociation(
    name="name101",
    ends={
        Property(name="JDTAST_Name103", type=JDTAST_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_PackageDeclaration102", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
binding104: BinaryAssociation = BinaryAssociation(
    name="binding104",
    ends={
        Property(name="JDTAST_IPackageFragment106", type=JDTAST_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_PackageDeclaration105", type=JDTAST_IPackageFragment, multiplicity=Multiplicity(1, 1))
    }
)
name109: BinaryAssociation = BinaryAssociation(
    name="name109",
    ends={
        Property(name="JDTAST_SimpleName110", type=JDTAST_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TypeParameter", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeBounds111: BinaryAssociation = BinaryAssociation(
    name="typeBounds111",
    ends={
        Property(name="JDTAST_Type113", type=JDTAST_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TypeParameter112", type=JDTAST_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments107: BinaryAssociation = BinaryAssociation(
    name="fragments107",
    ends={
        Property(name="JDTAST_ASTNode108", type=JDTAST_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TagElement", type=JDTAST_ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations119: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations119",
    ends={
        Property(name="JDTAST_BodyDeclaration121", type=JDTAST_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_AbstractTypeDeclaration120", type=JDTAST_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name122: BinaryAssociation = BinaryAssociation(
    name="name122",
    ends={
        Property(name="JDTAST_SimpleName124", type=JDTAST_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_AbstractTypeDeclaration123", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer114: BinaryAssociation = BinaryAssociation(
    name="initializer114",
    ends={
        Property(name="JDTAST_Expression115", type=JDTAST_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_VariableDeclaration", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name116: BinaryAssociation = BinaryAssociation(
    name="name116",
    ends={
        Property(name="JDTAST_SimpleName118", type=JDTAST_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_VariableDeclaration117", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type130: BinaryAssociation = BinaryAssociation(
    name="type130",
    ends={
        Property(name="JDTAST_Type132", type=JDTAST_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_AnnotationTypeMemberDeclaration131", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments133: BinaryAssociation = BinaryAssociation(
    name="arguments133",
    ends={
        Property(name="JDTAST_Expression134", type=JDTAST_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_EnumConstantDeclaration", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration135: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration135",
    ends={
        Property(name="JDTAST_AnonymousClassDeclaration137", type=JDTAST_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_EnumConstantDeclaration136", type=JDTAST_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name138: BinaryAssociation = BinaryAssociation(
    name="name138",
    ends={
        Property(name="JDTAST_SimpleName140", type=JDTAST_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_EnumConstantDeclaration139", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments141: BinaryAssociation = BinaryAssociation(
    name="fragments141",
    ends={
        Property(name="JDTAST_VariableDeclarationFragment", type=JDTAST_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_FieldDeclaration", type=JDTAST_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default125: BinaryAssociation = BinaryAssociation(
    name="default125",
    ends={
        Property(name="JDTAST_Expression126", type=JDTAST_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_AnnotationTypeMemberDeclaration", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name127: BinaryAssociation = BinaryAssociation(
    name="name127",
    ends={
        Property(name="JDTAST_SimpleName129", type=JDTAST_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_AnnotationTypeMemberDeclaration128", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body145: BinaryAssociation = BinaryAssociation(
    name="body145",
    ends={
        Property(name="JDTAST_Block146", type=JDTAST_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_Initializer", type=JDTAST_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body147: BinaryAssociation = BinaryAssociation(
    name="body147",
    ends={
        Property(name="JDTAST_Block148", type=JDTAST_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodDeclaration", type=JDTAST_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name149: BinaryAssociation = BinaryAssociation(
    name="name149",
    ends={
        Property(name="JDTAST_SimpleName151", type=JDTAST_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodDeclaration150", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType152: BinaryAssociation = BinaryAssociation(
    name="returnType152",
    ends={
        Property(name="JDTAST_Type154", type=JDTAST_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodDeclaration153", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type142: BinaryAssociation = BinaryAssociation(
    name="type142",
    ends={
        Property(name="JDTAST_Type144", type=JDTAST_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_FieldDeclaration143", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thrownExceptions158: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions158",
    ends={
        Property(name="JDTAST_Name160", type=JDTAST_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodDeclaration159", type=JDTAST_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters161: BinaryAssociation = BinaryAssociation(
    name="typeParameters161",
    ends={
        Property(name="JDTAST_TypeParameter163", type=JDTAST_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodDeclaration162", type=JDTAST_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
binding164: BinaryAssociation = BinaryAssociation(
    name="binding164",
    ends={
        Property(name="JDTAST_IMethod166", type=JDTAST_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodDeclaration165", type=JDTAST_IMethod, multiplicity=Multiplicity(1, 1))
    }
)
superclassType172: BinaryAssociation = BinaryAssociation(
    name="superclassType172",
    ends={
        Property(name="JDTAST_Type173", type=JDTAST_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TypeDeclaration", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters155: BinaryAssociation = BinaryAssociation(
    name="parameters155",
    ends={
        Property(name="JDTAST_SingleVariableDeclaration157", type=JDTAST_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodDeclaration156", type=JDTAST_SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaceTypes174: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes174",
    ends={
        Property(name="JDTAST_Type176", type=JDTAST_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TypeDeclaration175", type=JDTAST_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters177: BinaryAssociation = BinaryAssociation(
    name="typeParameters177",
    ends={
        Property(name="JDTAST_TypeParameter179", type=JDTAST_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TypeDeclaration178", type=JDTAST_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaceTypes167: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes167",
    ends={
        Property(name="JDTAST_Type168", type=JDTAST_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_EnumDeclaration", type=JDTAST_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumConstants169: BinaryAssociation = BinaryAssociation(
    name="enumConstants169",
    ends={
        Property(name="JDTAST_EnumConstantDeclaration171", type=JDTAST_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_EnumDeclaration170", type=JDTAST_EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
array186: BinaryAssociation = BinaryAssociation(
    name="array186",
    ends={
        Property(name="JDTAST_Expression187", type=JDTAST_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ArrayAccess", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index188: BinaryAssociation = BinaryAssociation(
    name="index188",
    ends={
        Property(name="JDTAST_Expression190", type=JDTAST_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ArrayAccess189", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions191: BinaryAssociation = BinaryAssociation(
    name="dimensions191",
    ends={
        Property(name="JDTAST_Expression192", type=JDTAST_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ArrayCreation", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer193: BinaryAssociation = BinaryAssociation(
    name="initializer193",
    ends={
        Property(name="JDTAST_ArrayInitializer", type=JDTAST_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ArrayCreation194", type=JDTAST_ArrayInitializer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type195: BinaryAssociation = BinaryAssociation(
    name="type195",
    ends={
        Property(name="JDTAST_ArrayType", type=JDTAST_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ArrayCreation196", type=JDTAST_ArrayType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tags180: BinaryAssociation = BinaryAssociation(
    name="tags180",
    ends={
        Property(name="JDTAST_TagElement182", type=JDTAST_Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_Javadoc181", type=JDTAST_TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions197: BinaryAssociation = BinaryAssociation(
    name="expressions197",
    ends={
        Property(name="JDTAST_Expression199", type=JDTAST_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ArrayInitializer198", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeName183: BinaryAssociation = BinaryAssociation(
    name="typeName183",
    ends={
        Property(name="JDTAST_Name185", type=JDTAST_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_Annotation184", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide202: BinaryAssociation = BinaryAssociation(
    name="rightHandSide202",
    ends={
        Property(name="JDTAST_Expression204", type=JDTAST_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_Assignment203", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide200: BinaryAssociation = BinaryAssociation(
    name="leftHandSide200",
    ends={
        Property(name="JDTAST_Expression201", type=JDTAST_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_Assignment", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments210: BinaryAssociation = BinaryAssociation(
    name="arguments210",
    ends={
        Property(name="JDTAST_Expression211", type=JDTAST_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ClassInstanceCreation", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration212: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration212",
    ends={
        Property(name="JDTAST_AnonymousClassDeclaration214", type=JDTAST_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ClassInstanceCreation213", type=JDTAST_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression215: BinaryAssociation = BinaryAssociation(
    name="expression215",
    ends={
        Property(name="JDTAST_Expression217", type=JDTAST_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ClassInstanceCreation216", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type218: BinaryAssociation = BinaryAssociation(
    name="type218",
    ends={
        Property(name="JDTAST_Type220", type=JDTAST_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ClassInstanceCreation219", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments221: BinaryAssociation = BinaryAssociation(
    name="typeArguments221",
    ends={
        Property(name="JDTAST_Type223", type=JDTAST_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ClassInstanceCreation222", type=JDTAST_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression205: BinaryAssociation = BinaryAssociation(
    name="expression205",
    ends={
        Property(name="JDTAST_Expression206", type=JDTAST_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_CastExpression", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type207: BinaryAssociation = BinaryAssociation(
    name="type207",
    ends={
        Property(name="JDTAST_Type209", type=JDTAST_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_CastExpression208", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression232: BinaryAssociation = BinaryAssociation(
    name="expression232",
    ends={
        Property(name="JDTAST_Expression233", type=JDTAST_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_FieldAccess", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name234: BinaryAssociation = BinaryAssociation(
    name="name234",
    ends={
        Property(name="JDTAST_SimpleName236", type=JDTAST_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_FieldAccess235", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands237: BinaryAssociation = BinaryAssociation(
    name="extendedOperands237",
    ends={
        Property(name="JDTAST_Expression238", type=JDTAST_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_InfixExpression", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand239: BinaryAssociation = BinaryAssociation(
    name="leftOperand239",
    ends={
        Property(name="JDTAST_Expression241", type=JDTAST_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_InfixExpression240", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression224: BinaryAssociation = BinaryAssociation(
    name="elseExpression224",
    ends={
        Property(name="JDTAST_Expression225", type=JDTAST_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ConditionalExpression", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression226: BinaryAssociation = BinaryAssociation(
    name="expression226",
    ends={
        Property(name="JDTAST_Expression228", type=JDTAST_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ConditionalExpression227", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression229: BinaryAssociation = BinaryAssociation(
    name="thenExpression229",
    ends={
        Property(name="JDTAST_Expression231", type=JDTAST_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ConditionalExpression230", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand245: BinaryAssociation = BinaryAssociation(
    name="leftOperand245",
    ends={
        Property(name="JDTAST_Expression246", type=JDTAST_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_InstanceofExpression", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand247: BinaryAssociation = BinaryAssociation(
    name="rightOperand247",
    ends={
        Property(name="JDTAST_Type249", type=JDTAST_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_InstanceofExpression248", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand242: BinaryAssociation = BinaryAssociation(
    name="rightOperand242",
    ends={
        Property(name="JDTAST_Expression244", type=JDTAST_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_InfixExpression243", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments250: BinaryAssociation = BinaryAssociation(
    name="arguments250",
    ends={
        Property(name="JDTAST_Expression251", type=JDTAST_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodInvocation", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression252: BinaryAssociation = BinaryAssociation(
    name="expression252",
    ends={
        Property(name="JDTAST_Expression254", type=JDTAST_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodInvocation253", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name255: BinaryAssociation = BinaryAssociation(
    name="name255",
    ends={
        Property(name="JDTAST_SimpleName257", type=JDTAST_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodInvocation256", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments258: BinaryAssociation = BinaryAssociation(
    name="typeArguments258",
    ends={
        Property(name="JDTAST_Type260", type=JDTAST_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodInvocation259", type=JDTAST_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodBinding261: BinaryAssociation = BinaryAssociation(
    name="methodBinding261",
    ends={
        Property(name="JDTAST_IMethod263", type=JDTAST_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_MethodInvocation262", type=JDTAST_IMethod, multiplicity=Multiplicity(1, 1))
    }
)
expression264: BinaryAssociation = BinaryAssociation(
    name="expression264",
    ends={
        Property(name="JDTAST_Expression265", type=JDTAST_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ParenthesizedExpression", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand266: BinaryAssociation = BinaryAssociation(
    name="operand266",
    ends={
        Property(name="JDTAST_Expression267", type=JDTAST_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_PostfixExpression", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand268: BinaryAssociation = BinaryAssociation(
    name="operand268",
    ends={
        Property(name="JDTAST_Expression269", type=JDTAST_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_PrefixExpression", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name270: BinaryAssociation = BinaryAssociation(
    name="name270",
    ends={
        Property(name="JDTAST_SimpleName271", type=JDTAST_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SuperFieldAccess", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier272: BinaryAssociation = BinaryAssociation(
    name="qualifier272",
    ends={
        Property(name="JDTAST_Name274", type=JDTAST_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SuperFieldAccess273", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments275: BinaryAssociation = BinaryAssociation(
    name="arguments275",
    ends={
        Property(name="JDTAST_Expression276", type=JDTAST_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SuperMethodInvocation", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name277: BinaryAssociation = BinaryAssociation(
    name="name277",
    ends={
        Property(name="JDTAST_Name279", type=JDTAST_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SuperMethodInvocation278", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier280: BinaryAssociation = BinaryAssociation(
    name="qualifier280",
    ends={
        Property(name="JDTAST_Name282", type=JDTAST_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SuperMethodInvocation281", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier286: BinaryAssociation = BinaryAssociation(
    name="qualifier286",
    ends={
        Property(name="JDTAST_Name287", type=JDTAST_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ThisExpression", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type288: BinaryAssociation = BinaryAssociation(
    name="type288",
    ends={
        Property(name="JDTAST_Type289", type=JDTAST_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TypeLiteral", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments290: BinaryAssociation = BinaryAssociation(
    name="fragments290",
    ends={
        Property(name="JDTAST_VariableDeclarationFragment291", type=JDTAST_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_VariableDeclarationExpression", type=JDTAST_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers292: BinaryAssociation = BinaryAssociation(
    name="modifiers292",
    ends={
        Property(name="JDTAST_ExtendedModifier294", type=JDTAST_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_VariableDeclarationExpression293", type=JDTAST_ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments283: BinaryAssociation = BinaryAssociation(
    name="typeArguments283",
    ends={
        Property(name="JDTAST_Type285", type=JDTAST_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SuperMethodInvocation284", type=JDTAST_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression298: BinaryAssociation = BinaryAssociation(
    name="expression298",
    ends={
        Property(name="JDTAST_Expression299", type=JDTAST_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_AssertStatement", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message300: BinaryAssociation = BinaryAssociation(
    name="message300",
    ends={
        Property(name="JDTAST_Expression302", type=JDTAST_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_AssertStatement301", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements303: BinaryAssociation = BinaryAssociation(
    name="statements303",
    ends={
        Property(name="JDTAST_Statement", type=JDTAST_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_Block304", type=JDTAST_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label305: BinaryAssociation = BinaryAssociation(
    name="label305",
    ends={
        Property(name="JDTAST_SimpleName306", type=JDTAST_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_BreakStatement", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type295: BinaryAssociation = BinaryAssociation(
    name="type295",
    ends={
        Property(name="JDTAST_Type297", type=JDTAST_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_VariableDeclarationExpression296", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments309: BinaryAssociation = BinaryAssociation(
    name="typeArguments309",
    ends={
        Property(name="JDTAST_Type311", type=JDTAST_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ConstructorInvocation310", type=JDTAST_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label312: BinaryAssociation = BinaryAssociation(
    name="label312",
    ends={
        Property(name="JDTAST_SimpleName313", type=JDTAST_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ContinueStatement", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body314: BinaryAssociation = BinaryAssociation(
    name="body314",
    ends={
        Property(name="JDTAST_Statement315", type=JDTAST_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_DoStatement", type=JDTAST_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression316: BinaryAssociation = BinaryAssociation(
    name="expression316",
    ends={
        Property(name="JDTAST_Expression318", type=JDTAST_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_DoStatement317", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments307: BinaryAssociation = BinaryAssociation(
    name="arguments307",
    ends={
        Property(name="JDTAST_Expression308", type=JDTAST_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ConstructorInvocation", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body319: BinaryAssociation = BinaryAssociation(
    name="body319",
    ends={
        Property(name="JDTAST_Statement320", type=JDTAST_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_EnhancedForStatement", type=JDTAST_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression321: BinaryAssociation = BinaryAssociation(
    name="expression321",
    ends={
        Property(name="JDTAST_Expression323", type=JDTAST_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_EnhancedForStatement322", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter324: BinaryAssociation = BinaryAssociation(
    name="parameter324",
    ends={
        Property(name="JDTAST_SingleVariableDeclaration326", type=JDTAST_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_EnhancedForStatement325", type=JDTAST_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression327: BinaryAssociation = BinaryAssociation(
    name="expression327",
    ends={
        Property(name="JDTAST_Expression328", type=JDTAST_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ExpressionStatement", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body329: BinaryAssociation = BinaryAssociation(
    name="body329",
    ends={
        Property(name="JDTAST_Statement330", type=JDTAST_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ForStatement", type=JDTAST_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression331: BinaryAssociation = BinaryAssociation(
    name="expression331",
    ends={
        Property(name="JDTAST_Expression333", type=JDTAST_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ForStatement332", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializers334: BinaryAssociation = BinaryAssociation(
    name="initializers334",
    ends={
        Property(name="JDTAST_Expression336", type=JDTAST_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ForStatement335", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatement340: BinaryAssociation = BinaryAssociation(
    name="elseStatement340",
    ends={
        Property(name="JDTAST_Statement341", type=JDTAST_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IfStatement", type=JDTAST_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression342: BinaryAssociation = BinaryAssociation(
    name="expression342",
    ends={
        Property(name="JDTAST_Expression344", type=JDTAST_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IfStatement343", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement345: BinaryAssociation = BinaryAssociation(
    name="thenStatement345",
    ends={
        Property(name="JDTAST_Statement347", type=JDTAST_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_IfStatement346", type=JDTAST_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body348: BinaryAssociation = BinaryAssociation(
    name="body348",
    ends={
        Property(name="JDTAST_Statement349", type=JDTAST_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_LabeledStatement", type=JDTAST_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label350: BinaryAssociation = BinaryAssociation(
    name="label350",
    ends={
        Property(name="JDTAST_SimpleName352", type=JDTAST_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_LabeledStatement351", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression353: BinaryAssociation = BinaryAssociation(
    name="expression353",
    ends={
        Property(name="JDTAST_Expression354", type=JDTAST_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ReturnStatement", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updaters337: BinaryAssociation = BinaryAssociation(
    name="updaters337",
    ends={
        Property(name="JDTAST_Expression339", type=JDTAST_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ForStatement338", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body370: BinaryAssociation = BinaryAssociation(
    name="body370",
    ends={
        Property(name="JDTAST_Block371", type=JDTAST_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SynchronizedStatement", type=JDTAST_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression357: BinaryAssociation = BinaryAssociation(
    name="expression357",
    ends={
        Property(name="JDTAST_Expression359", type=JDTAST_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SuperConstructorInvocation358", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments360: BinaryAssociation = BinaryAssociation(
    name="typeArguments360",
    ends={
        Property(name="JDTAST_Type362", type=JDTAST_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SuperConstructorInvocation361", type=JDTAST_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression363: BinaryAssociation = BinaryAssociation(
    name="expression363",
    ends={
        Property(name="JDTAST_Expression364", type=JDTAST_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SwitchCase", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression365: BinaryAssociation = BinaryAssociation(
    name="expression365",
    ends={
        Property(name="JDTAST_Expression366", type=JDTAST_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SwitchStatement", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements367: BinaryAssociation = BinaryAssociation(
    name="statements367",
    ends={
        Property(name="JDTAST_Statement369", type=JDTAST_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SwitchStatement368", type=JDTAST_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments355: BinaryAssociation = BinaryAssociation(
    name="arguments355",
    ends={
        Property(name="JDTAST_Expression356", type=JDTAST_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SuperConstructorInvocation", type=JDTAST_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type392: BinaryAssociation = BinaryAssociation(
    name="type392",
    ends={
        Property(name="JDTAST_Type394", type=JDTAST_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_VariableDeclarationStatement393", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression372: BinaryAssociation = BinaryAssociation(
    name="expression372",
    ends={
        Property(name="JDTAST_Expression374", type=JDTAST_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SynchronizedStatement373", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression375: BinaryAssociation = BinaryAssociation(
    name="expression375",
    ends={
        Property(name="JDTAST_Expression376", type=JDTAST_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ThrowStatement", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catchClauses377: BinaryAssociation = BinaryAssociation(
    name="catchClauses377",
    ends={
        Property(name="JDTAST_CatchClause378", type=JDTAST_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TryStatement", type=JDTAST_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body379: BinaryAssociation = BinaryAssociation(
    name="body379",
    ends={
        Property(name="JDTAST_Block381", type=JDTAST_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TryStatement380", type=JDTAST_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally382: BinaryAssociation = BinaryAssociation(
    name="finally382",
    ends={
        Property(name="JDTAST_Block384", type=JDTAST_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TryStatement383", type=JDTAST_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration385: BinaryAssociation = BinaryAssociation(
    name="declaration385",
    ends={
        Property(name="JDTAST_AbstractTypeDeclaration386", type=JDTAST_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_TypeDeclarationStatement", type=JDTAST_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments387: BinaryAssociation = BinaryAssociation(
    name="fragments387",
    ends={
        Property(name="JDTAST_VariableDeclarationFragment388", type=JDTAST_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_VariableDeclarationStatement", type=JDTAST_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers389: BinaryAssociation = BinaryAssociation(
    name="modifiers389",
    ends={
        Property(name="JDTAST_ExtendedModifier391", type=JDTAST_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_VariableDeclarationStatement390", type=JDTAST_ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body395: BinaryAssociation = BinaryAssociation(
    name="body395",
    ends={
        Property(name="JDTAST_Statement396", type=JDTAST_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_WhileStatement", type=JDTAST_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression397: BinaryAssociation = BinaryAssociation(
    name="expression397",
    ends={
        Property(name="JDTAST_Expression399", type=JDTAST_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_WhileStatement398", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
componentType400: BinaryAssociation = BinaryAssociation(
    name="componentType400",
    ends={
        Property(name="JDTAST_Type402", type=JDTAST_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ArrayType401", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType403: BinaryAssociation = BinaryAssociation(
    name="elementType403",
    ends={
        Property(name="JDTAST_Type405", type=JDTAST_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ArrayType404", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type406: BinaryAssociation = BinaryAssociation(
    name="type406",
    ends={
        Property(name="JDTAST_Type407", type=JDTAST_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ParameterizedType", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name411: BinaryAssociation = BinaryAssociation(
    name="name411",
    ends={
        Property(name="JDTAST_SimpleName412", type=JDTAST_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_QualifiedType", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier413: BinaryAssociation = BinaryAssociation(
    name="qualifier413",
    ends={
        Property(name="JDTAST_Type415", type=JDTAST_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_QualifiedType414", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name416: BinaryAssociation = BinaryAssociation(
    name="name416",
    ends={
        Property(name="JDTAST_Name417", type=JDTAST_SimpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SimpleType", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bound418: BinaryAssociation = BinaryAssociation(
    name="bound418",
    ends={
        Property(name="JDTAST_Type419", type=JDTAST_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_WildcardType", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type420: BinaryAssociation = BinaryAssociation(
    name="type420",
    ends={
        Property(name="JDTAST_Type422", type=JDTAST_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SingleVariableDeclaration421", type=JDTAST_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifiers423: BinaryAssociation = BinaryAssociation(
    name="modifiers423",
    ends={
        Property(name="JDTAST_ExtendedModifier425", type=JDTAST_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SingleVariableDeclaration424", type=JDTAST_ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments408: BinaryAssociation = BinaryAssociation(
    name="typeArguments408",
    ends={
        Property(name="JDTAST_Type410", type=JDTAST_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_ParameterizedType409", type=JDTAST_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name426: BinaryAssociation = BinaryAssociation(
    name="name426",
    ends={
        Property(name="JDTAST_SimpleName427", type=JDTAST_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_QualifiedName", type=JDTAST_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier428: BinaryAssociation = BinaryAssociation(
    name="qualifier428",
    ends={
        Property(name="JDTAST_Name430", type=JDTAST_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_QualifiedName429", type=JDTAST_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values431: BinaryAssociation = BinaryAssociation(
    name="values431",
    ends={
        Property(name="JDTAST_MemberValuePair432", type=JDTAST_NormalAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_NormalAnnotation", type=JDTAST_MemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value433: BinaryAssociation = BinaryAssociation(
    name="value433",
    ends={
        Property(name="JDTAST_Expression434", type=JDTAST_SingleMemberAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="JDTAST_SingleMemberAnnotation", type=JDTAST_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_JDTAST_IJavaModel_PhysicalElement = Generalization(general=PhysicalElement, specific=JDTAST_IJavaModel)
gen_JDTAST_IPackageFragmentRoot_IJavaElement = Generalization(general=IJavaElement, specific=JDTAST_IPackageFragmentRoot)
gen_JDTAST_IPackageFragmentRoot_PhysicalElement = Generalization(general=PhysicalElement, specific=JDTAST_IPackageFragmentRoot)
gen_JDTAST_BinaryPackageFragmentRoot_IPackageFragmentRoot = Generalization(general=IPackageFragmentRoot, specific=JDTAST_BinaryPackageFragmentRoot)
gen_JDTAST_SourcePackageFragmentRoot_IPackageFragmentRoot = Generalization(general=IPackageFragmentRoot, specific=JDTAST_SourcePackageFragmentRoot)
gen_JDTAST_IPackageFragment_IJavaElement = Generalization(general=IJavaElement, specific=JDTAST_IPackageFragment)
gen_JDTAST_IPackageFragment_PhysicalElement = Generalization(general=PhysicalElement, specific=JDTAST_IPackageFragment)
gen_JDTAST_IJavaProject_IJavaElement = Generalization(general=IJavaElement, specific=JDTAST_IJavaProject)
gen_JDTAST_IJavaProject_PhysicalElement = Generalization(general=PhysicalElement, specific=JDTAST_IJavaProject)
gen_JDTAST_ITypeRoot_PhysicalElement = Generalization(general=PhysicalElement, specific=JDTAST_ITypeRoot)
gen_JDTAST_ICompilationUnit_ITypeRoot = Generalization(general=ITypeRoot, specific=JDTAST_ICompilationUnit)
gen_JDTAST_ITypeRoot_IJavaElement = Generalization(general=IJavaElement, specific=JDTAST_ITypeRoot)
gen_JDTAST_ITypeRoot_ISourceReference = Generalization(general=ISourceReference, specific=JDTAST_ITypeRoot)
gen_JDTAST_IImportDeclaration_IJavaElement = Generalization(general=IJavaElement, specific=JDTAST_IImportDeclaration)
gen_JDTAST_IImportDeclaration_ISourceReference = Generalization(general=ISourceReference, specific=JDTAST_IImportDeclaration)
gen_JDTAST_IMember_IJavaElement = Generalization(general=IJavaElement, specific=JDTAST_IMember)
gen_JDTAST_IMember_ISourceReference = Generalization(general=ISourceReference, specific=JDTAST_IMember)
gen_JDTAST_IClassFile_ITypeRoot = Generalization(general=ITypeRoot, specific=JDTAST_IClassFile)
gen_JDTAST_ITypeParameter_IJavaElement = Generalization(general=IJavaElement, specific=JDTAST_ITypeParameter)
gen_JDTAST_ITypeParameter_ISourceReference = Generalization(general=ISourceReference, specific=JDTAST_ITypeParameter)
gen_JDTAST_IInitializer_IMember = Generalization(general=IMember, specific=JDTAST_IInitializer)
gen_JDTAST_IType_IMember = Generalization(general=IMember, specific=JDTAST_IType)
gen_JDTAST_IMethod_IMember = Generalization(general=IMember, specific=JDTAST_IMethod)
gen_JDTAST_IField_IMember = Generalization(general=IMember, specific=JDTAST_IField)
gen_JDTAST_BodyDeclaration_ASTNode = Generalization(general=ASTNode, specific=JDTAST_BodyDeclaration)
gen_JDTAST_CatchClause_ASTNode = Generalization(general=ASTNode, specific=JDTAST_CatchClause)
gen_JDTAST_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=JDTAST_AnonymousClassDeclaration)
gen_JDTAST_CompilationUnit_ASTNode = Generalization(general=ASTNode, specific=JDTAST_CompilationUnit)
gen_JDTAST_Expression_ASTNode = Generalization(general=ASTNode, specific=JDTAST_Expression)
gen_JDTAST_Comment_ASTNode = Generalization(general=ASTNode, specific=JDTAST_Comment)
gen_JDTAST_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=JDTAST_ImportDeclaration)
gen_JDTAST_MemberRef_ASTNode = Generalization(general=ASTNode, specific=JDTAST_MemberRef)
gen_JDTAST_MethodRef_ASTNode = Generalization(general=ASTNode, specific=JDTAST_MethodRef)
gen_JDTAST_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=JDTAST_MethodRefParameter)
gen_JDTAST_MemberValuePair_ASTNode = Generalization(general=ASTNode, specific=JDTAST_MemberValuePair)
gen_JDTAST_Modifier_ASTNode = Generalization(general=ASTNode, specific=JDTAST_Modifier)
gen_JDTAST_Modifier_ExtendedModifier = Generalization(general=ExtendedModifier, specific=JDTAST_Modifier)
gen_JDTAST_PackageDeclaration_ASTNode = Generalization(general=ASTNode, specific=JDTAST_PackageDeclaration)
gen_JDTAST_Statement_ASTNode = Generalization(general=ASTNode, specific=JDTAST_Statement)
gen_JDTAST_TextElement_ASTNode = Generalization(general=ASTNode, specific=JDTAST_TextElement)
gen_JDTAST_Type_ASTNode = Generalization(general=ASTNode, specific=JDTAST_Type)
gen_JDTAST_TypeParameter_ASTNode = Generalization(general=ASTNode, specific=JDTAST_TypeParameter)
gen_JDTAST_VariableDeclaration_ASTNode = Generalization(general=ASTNode, specific=JDTAST_VariableDeclaration)
gen_JDTAST_TagElement_ASTNode = Generalization(general=ASTNode, specific=JDTAST_TagElement)
gen_JDTAST_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JDTAST_AbstractTypeDeclaration)
gen_JDTAST_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JDTAST_AnnotationTypeMemberDeclaration)
gen_JDTAST_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JDTAST_EnumConstantDeclaration)
gen_JDTAST_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JDTAST_FieldDeclaration)
gen_JDTAST_MethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JDTAST_MethodDeclaration)
gen_JDTAST_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JDTAST_Initializer)
gen_JDTAST_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JDTAST_AnnotationTypeDeclaration)
gen_JDTAST_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JDTAST_EnumDeclaration)
gen_JDTAST_BlockComment_Comment = Generalization(general=Comment, specific=JDTAST_BlockComment)
gen_JDTAST_Javadoc_Comment = Generalization(general=Comment, specific=JDTAST_Javadoc)
gen_JDTAST_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JDTAST_TypeDeclaration)
gen_JDTAST_ArrayCreation_Expression = Generalization(general=Expression, specific=JDTAST_ArrayCreation)
gen_JDTAST_ArrayInitializer_Expression = Generalization(general=Expression, specific=JDTAST_ArrayInitializer)
gen_JDTAST_LineComment_Comment = Generalization(general=Comment, specific=JDTAST_LineComment)
gen_JDTAST_Annotation_Expression = Generalization(general=Expression, specific=JDTAST_Annotation)
gen_JDTAST_Annotation_ExtendedModifier = Generalization(general=ExtendedModifier, specific=JDTAST_Annotation)
gen_JDTAST_ArrayAccess_Expression = Generalization(general=Expression, specific=JDTAST_ArrayAccess)
gen_JDTAST_BooleanLiteral_Expression = Generalization(general=Expression, specific=JDTAST_BooleanLiteral)
gen_JDTAST_CastExpression_Expression = Generalization(general=Expression, specific=JDTAST_CastExpression)
gen_JDTAST_Assignment_Expression = Generalization(general=Expression, specific=JDTAST_Assignment)
gen_JDTAST_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=JDTAST_ClassInstanceCreation)
gen_JDTAST_ConditionalExpression_Expression = Generalization(general=Expression, specific=JDTAST_ConditionalExpression)
gen_JDTAST_CharacterLiteral_Expression = Generalization(general=Expression, specific=JDTAST_CharacterLiteral)
gen_JDTAST_FieldAccess_Expression = Generalization(general=Expression, specific=JDTAST_FieldAccess)
gen_JDTAST_InfixExpression_Expression = Generalization(general=Expression, specific=JDTAST_InfixExpression)
gen_JDTAST_InstanceofExpression_Expression = Generalization(general=Expression, specific=JDTAST_InstanceofExpression)
gen_JDTAST_MethodInvocation_Expression = Generalization(general=Expression, specific=JDTAST_MethodInvocation)
gen_JDTAST_NullLiteral_Expression = Generalization(general=Expression, specific=JDTAST_NullLiteral)
gen_JDTAST_NumberLiteral_Expression = Generalization(general=Expression, specific=JDTAST_NumberLiteral)
gen_JDTAST_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=JDTAST_ParenthesizedExpression)
gen_JDTAST_PostfixExpression_Expression = Generalization(general=Expression, specific=JDTAST_PostfixExpression)
gen_JDTAST_Name_Expression = Generalization(general=Expression, specific=JDTAST_Name)
gen_JDTAST_PrefixExpression_Expression = Generalization(general=Expression, specific=JDTAST_PrefixExpression)
gen_JDTAST_StringLiteral_Expression = Generalization(general=Expression, specific=JDTAST_StringLiteral)
gen_JDTAST_SuperFieldAccess_Expression = Generalization(general=Expression, specific=JDTAST_SuperFieldAccess)
gen_JDTAST_SuperMethodInvocation_Expression = Generalization(general=Expression, specific=JDTAST_SuperMethodInvocation)
gen_JDTAST_ThisExpression_Expression = Generalization(general=Expression, specific=JDTAST_ThisExpression)
gen_JDTAST_TypeLiteral_Expression = Generalization(general=Expression, specific=JDTAST_TypeLiteral)
gen_JDTAST_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=JDTAST_VariableDeclarationExpression)
gen_JDTAST_Block_Statement = Generalization(general=Statement, specific=JDTAST_Block)
gen_JDTAST_BreakStatement_Statement = Generalization(general=Statement, specific=JDTAST_BreakStatement)
gen_JDTAST_AssertStatement_Statement = Generalization(general=Statement, specific=JDTAST_AssertStatement)
gen_JDTAST_ContinueStatement_Statement = Generalization(general=Statement, specific=JDTAST_ContinueStatement)
gen_JDTAST_DoStatement_Statement = Generalization(general=Statement, specific=JDTAST_DoStatement)
gen_JDTAST_ConstructorInvocation_Statement = Generalization(general=Statement, specific=JDTAST_ConstructorInvocation)
gen_JDTAST_ExpressionStatement_Statement = Generalization(general=Statement, specific=JDTAST_ExpressionStatement)
gen_JDTAST_EmptyStatement_Statement = Generalization(general=Statement, specific=JDTAST_EmptyStatement)
gen_JDTAST_EnhancedForStatement_Statement = Generalization(general=Statement, specific=JDTAST_EnhancedForStatement)
gen_JDTAST_ForStatement_Statement = Generalization(general=Statement, specific=JDTAST_ForStatement)
gen_JDTAST_IfStatement_Statement = Generalization(general=Statement, specific=JDTAST_IfStatement)
gen_JDTAST_LabeledStatement_Statement = Generalization(general=Statement, specific=JDTAST_LabeledStatement)
gen_JDTAST_ReturnStatement_Statement = Generalization(general=Statement, specific=JDTAST_ReturnStatement)
gen_JDTAST_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=JDTAST_SuperConstructorInvocation)
gen_JDTAST_SwitchCase_Statement = Generalization(general=Statement, specific=JDTAST_SwitchCase)
gen_JDTAST_SwitchStatement_Statement = Generalization(general=Statement, specific=JDTAST_SwitchStatement)
gen_JDTAST_SynchronizedStatement_Statement = Generalization(general=Statement, specific=JDTAST_SynchronizedStatement)
gen_JDTAST_ThrowStatement_Statement = Generalization(general=Statement, specific=JDTAST_ThrowStatement)
gen_JDTAST_TryStatement_Statement = Generalization(general=Statement, specific=JDTAST_TryStatement)
gen_JDTAST_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=JDTAST_TypeDeclarationStatement)
gen_JDTAST_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=JDTAST_VariableDeclarationStatement)
gen_JDTAST_WhileStatement_Statement = Generalization(general=Statement, specific=JDTAST_WhileStatement)
gen_JDTAST_ArrayType_Type = Generalization(general=Type, specific=JDTAST_ArrayType)
gen_JDTAST_ParameterizedType_Type = Generalization(general=Type, specific=JDTAST_ParameterizedType)
gen_JDTAST_PrimitiveType_Type = Generalization(general=Type, specific=JDTAST_PrimitiveType)
gen_JDTAST_QualifiedType_Type = Generalization(general=Type, specific=JDTAST_QualifiedType)
gen_JDTAST_SimpleType_Type = Generalization(general=Type, specific=JDTAST_SimpleType)
gen_JDTAST_WildcardType_Type = Generalization(general=Type, specific=JDTAST_WildcardType)
gen_JDTAST_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=JDTAST_SingleVariableDeclaration)
gen_JDTAST_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=JDTAST_VariableDeclarationFragment)
gen_JDTAST_QualifiedName_Name = Generalization(general=Name, specific=JDTAST_QualifiedName)
gen_JDTAST_SimpleName_Name = Generalization(general=Name, specific=JDTAST_SimpleName)
gen_JDTAST_MarkerAnnotation_Annotation = Generalization(general=Annotation, specific=JDTAST_MarkerAnnotation)
gen_JDTAST_NormalAnnotation_Annotation = Generalization(general=Annotation, specific=JDTAST_NormalAnnotation)
gen_JDTAST_SingleMemberAnnotation_Annotation = Generalization(general=Annotation, specific=JDTAST_SingleMemberAnnotation)

# Domain Model
domain_model = DomainModel(
    name="JDTAST",
    types={JDTAST_PhysicalElement, JDTAST_IJavaModel, PhysicalElement, JDTAST_IJavaProject, JDTAST_IJavaElement, JDTAST_IPackageFragment, JDTAST_BinaryPackageFragmentRoot, IPackageFragmentRoot, JDTAST_SourcePackageFragmentRoot, JDTAST_IPackageFragmentRoot, IJavaElement, ITypeRoot, JDTAST_IType, JDTAST_IImportDeclaration, JDTAST_CompilationUnit, JDTAST_IClassFile, JDTAST_ICompilationUnit, JDTAST_ITypeRoot, ISourceReference, JDTAST_ISourceReference, JDTAST_ISourceRange, JDTAST_IMember, JDTAST_IInitializer, JDTAST_IField, JDTAST_IMethod, JDTAST_ITypeParameter, IMember, JDTAST_Parameter, JDTAST_AST, JDTAST_ExtendedModifier, JDTAST_Javadoc, JDTAST_CatchClause, JDTAST_Block, JDTAST_SingleVariableDeclaration, JDTAST_ASTNode, JDTAST_AnonymousClassDeclaration, ASTNode, JDTAST_BodyDeclaration, JDTAST_PackageDeclaration, JDTAST_ImportDeclaration, JDTAST_AbstractTypeDeclaration, JDTAST_Expression, JDTAST_Comment, JDTAST_Name, JDTAST_MemberRef, JDTAST_SimpleName, JDTAST_MethodRef, JDTAST_MethodRefParameter, JDTAST_MemberValuePair, JDTAST_Modifier, ExtendedModifier, JDTAST_Type, JDTAST_Annotation, JDTAST_Statement, JDTAST_TextElement, JDTAST_TypeParameter, JDTAST_VariableDeclaration, JDTAST_TagElement, BodyDeclaration, JDTAST_AnnotationTypeMemberDeclaration, JDTAST_EnumConstantDeclaration, JDTAST_FieldDeclaration, JDTAST_VariableDeclarationFragment, JDTAST_MethodDeclaration, JDTAST_Initializer, JDTAST_AnnotationTypeDeclaration, AbstractTypeDeclaration, JDTAST_EnumDeclaration, JDTAST_BlockComment, Comment, JDTAST_TypeDeclaration, JDTAST_ArrayCreation, JDTAST_ArrayInitializer, JDTAST_ArrayType, JDTAST_LineComment, Expression, JDTAST_ArrayAccess, JDTAST_BooleanLiteral, JDTAST_CastExpression, JDTAST_Assignment, JDTAST_ClassInstanceCreation, JDTAST_ConditionalExpression, JDTAST_CharacterLiteral, JDTAST_FieldAccess, JDTAST_InfixExpression, JDTAST_InstanceofExpression, JDTAST_MethodInvocation, JDTAST_NullLiteral, JDTAST_NumberLiteral, JDTAST_ParenthesizedExpression, JDTAST_PostfixExpression, JDTAST_PrefixExpression, JDTAST_StringLiteral, JDTAST_SuperFieldAccess, JDTAST_SuperMethodInvocation, JDTAST_TypeLiteral, JDTAST_VariableDeclarationExpression, JDTAST_ThisExpression, JDTAST_BreakStatement, JDTAST_AssertStatement, Statement, JDTAST_ContinueStatement, JDTAST_DoStatement, JDTAST_ConstructorInvocation, JDTAST_ExpressionStatement, JDTAST_EmptyStatement, JDTAST_EnhancedForStatement, JDTAST_ForStatement, JDTAST_IfStatement, JDTAST_LabeledStatement, JDTAST_ReturnStatement, JDTAST_SuperConstructorInvocation, JDTAST_SwitchCase, JDTAST_SwitchStatement, JDTAST_SynchronizedStatement, JDTAST_ThrowStatement, JDTAST_TryStatement, JDTAST_TypeDeclarationStatement, JDTAST_VariableDeclarationStatement, JDTAST_WhileStatement, Type, JDTAST_ParameterizedType, JDTAST_QualifiedName, Name, JDTAST_PrimitiveType, JDTAST_QualifiedType, JDTAST_SimpleType, JDTAST_WildcardType, VariableDeclaration, JDTAST_MarkerAnnotation, Annotation, JDTAST_NormalAnnotation, JDTAST_SingleMemberAnnotation, Modifiers, AssignmentOperatorKind, InfixExpressionOperatorKind, PrefixExpressionOperatorKind, PostfixExpressionOperatorKind},
    associations={javaProjects0, externalPackageFragmentRoots6, requiredProjects10, packageFragments12, packageFragmentRoot13, externalPackageFragmentRoots1, packageFragmentRoots3, allType17, imports19, types21, primary25, ast27, classFiles14, compilationUnits15, type29, sourceRange32, initializers38, fields40, methods42, types45, typeParameters47, javadocRange33, nameRange35, parameters49, bodyDeclarations52, modifiers53, javadoc55, body57, compilationUnits51, comments62, package65, imports67, types69, exception58, alternateRoot60, name73, name75, qualifier76, typeBinding71, name84, qualifier86, parameters89, name91, name79, value81, type94, annotations96, javadoc98, name101, binding104, name109, typeBounds111, fragments107, bodyDeclarations119, name122, initializer114, name116, type130, arguments133, anonymousClassDeclaration135, name138, fragments141, default125, name127, body145, body147, name149, returnType152, type142, thrownExceptions158, typeParameters161, binding164, superclassType172, parameters155, superInterfaceTypes174, typeParameters177, superInterfaceTypes167, enumConstants169, array186, index188, dimensions191, initializer193, type195, tags180, expressions197, typeName183, rightHandSide202, leftHandSide200, arguments210, anonymousClassDeclaration212, expression215, type218, typeArguments221, expression205, type207, expression232, name234, extendedOperands237, leftOperand239, elseExpression224, expression226, thenExpression229, leftOperand245, rightOperand247, rightOperand242, arguments250, expression252, name255, typeArguments258, methodBinding261, expression264, operand266, operand268, name270, qualifier272, arguments275, name277, qualifier280, qualifier286, type288, fragments290, modifiers292, typeArguments283, expression298, message300, statements303, label305, type295, typeArguments309, label312, body314, expression316, arguments307, body319, expression321, parameter324, expression327, body329, expression331, initializers334, elseStatement340, expression342, thenStatement345, body348, label350, expression353, updaters337, body370, expression357, typeArguments360, expression363, expression365, statements367, arguments355, type392, expression372, expression375, catchClauses377, body379, finally382, declaration385, fragments387, modifiers389, body395, expression397, componentType400, elementType403, type406, name411, qualifier413, name416, bound418, type420, modifiers423, typeArguments408, name426, qualifier428, values431, value433},
    generalizations={gen_JDTAST_IJavaModel_PhysicalElement, gen_JDTAST_IPackageFragmentRoot_IJavaElement, gen_JDTAST_IPackageFragmentRoot_PhysicalElement, gen_JDTAST_BinaryPackageFragmentRoot_IPackageFragmentRoot, gen_JDTAST_SourcePackageFragmentRoot_IPackageFragmentRoot, gen_JDTAST_IPackageFragment_IJavaElement, gen_JDTAST_IPackageFragment_PhysicalElement, gen_JDTAST_IJavaProject_IJavaElement, gen_JDTAST_IJavaProject_PhysicalElement, gen_JDTAST_ITypeRoot_PhysicalElement, gen_JDTAST_ICompilationUnit_ITypeRoot, gen_JDTAST_ITypeRoot_IJavaElement, gen_JDTAST_ITypeRoot_ISourceReference, gen_JDTAST_IImportDeclaration_IJavaElement, gen_JDTAST_IImportDeclaration_ISourceReference, gen_JDTAST_IMember_IJavaElement, gen_JDTAST_IMember_ISourceReference, gen_JDTAST_IClassFile_ITypeRoot, gen_JDTAST_ITypeParameter_IJavaElement, gen_JDTAST_ITypeParameter_ISourceReference, gen_JDTAST_IInitializer_IMember, gen_JDTAST_IType_IMember, gen_JDTAST_IMethod_IMember, gen_JDTAST_IField_IMember, gen_JDTAST_BodyDeclaration_ASTNode, gen_JDTAST_CatchClause_ASTNode, gen_JDTAST_AnonymousClassDeclaration_ASTNode, gen_JDTAST_CompilationUnit_ASTNode, gen_JDTAST_Expression_ASTNode, gen_JDTAST_Comment_ASTNode, gen_JDTAST_ImportDeclaration_ASTNode, gen_JDTAST_MemberRef_ASTNode, gen_JDTAST_MethodRef_ASTNode, gen_JDTAST_MethodRefParameter_ASTNode, gen_JDTAST_MemberValuePair_ASTNode, gen_JDTAST_Modifier_ASTNode, gen_JDTAST_Modifier_ExtendedModifier, gen_JDTAST_PackageDeclaration_ASTNode, gen_JDTAST_Statement_ASTNode, gen_JDTAST_TextElement_ASTNode, gen_JDTAST_Type_ASTNode, gen_JDTAST_TypeParameter_ASTNode, gen_JDTAST_VariableDeclaration_ASTNode, gen_JDTAST_TagElement_ASTNode, gen_JDTAST_AbstractTypeDeclaration_BodyDeclaration, gen_JDTAST_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_JDTAST_EnumConstantDeclaration_BodyDeclaration, gen_JDTAST_FieldDeclaration_BodyDeclaration, gen_JDTAST_MethodDeclaration_BodyDeclaration, gen_JDTAST_Initializer_BodyDeclaration, gen_JDTAST_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_JDTAST_EnumDeclaration_AbstractTypeDeclaration, gen_JDTAST_BlockComment_Comment, gen_JDTAST_Javadoc_Comment, gen_JDTAST_TypeDeclaration_AbstractTypeDeclaration, gen_JDTAST_ArrayCreation_Expression, gen_JDTAST_ArrayInitializer_Expression, gen_JDTAST_LineComment_Comment, gen_JDTAST_Annotation_Expression, gen_JDTAST_Annotation_ExtendedModifier, gen_JDTAST_ArrayAccess_Expression, gen_JDTAST_BooleanLiteral_Expression, gen_JDTAST_CastExpression_Expression, gen_JDTAST_Assignment_Expression, gen_JDTAST_ClassInstanceCreation_Expression, gen_JDTAST_ConditionalExpression_Expression, gen_JDTAST_CharacterLiteral_Expression, gen_JDTAST_FieldAccess_Expression, gen_JDTAST_InfixExpression_Expression, gen_JDTAST_InstanceofExpression_Expression, gen_JDTAST_MethodInvocation_Expression, gen_JDTAST_NullLiteral_Expression, gen_JDTAST_NumberLiteral_Expression, gen_JDTAST_ParenthesizedExpression_Expression, gen_JDTAST_PostfixExpression_Expression, gen_JDTAST_Name_Expression, gen_JDTAST_PrefixExpression_Expression, gen_JDTAST_StringLiteral_Expression, gen_JDTAST_SuperFieldAccess_Expression, gen_JDTAST_SuperMethodInvocation_Expression, gen_JDTAST_ThisExpression_Expression, gen_JDTAST_TypeLiteral_Expression, gen_JDTAST_VariableDeclarationExpression_Expression, gen_JDTAST_Block_Statement, gen_JDTAST_BreakStatement_Statement, gen_JDTAST_AssertStatement_Statement, gen_JDTAST_ContinueStatement_Statement, gen_JDTAST_DoStatement_Statement, gen_JDTAST_ConstructorInvocation_Statement, gen_JDTAST_ExpressionStatement_Statement, gen_JDTAST_EmptyStatement_Statement, gen_JDTAST_EnhancedForStatement_Statement, gen_JDTAST_ForStatement_Statement, gen_JDTAST_IfStatement_Statement, gen_JDTAST_LabeledStatement_Statement, gen_JDTAST_ReturnStatement_Statement, gen_JDTAST_SuperConstructorInvocation_Statement, gen_JDTAST_SwitchCase_Statement, gen_JDTAST_SwitchStatement_Statement, gen_JDTAST_SynchronizedStatement_Statement, gen_JDTAST_ThrowStatement_Statement, gen_JDTAST_TryStatement_Statement, gen_JDTAST_TypeDeclarationStatement_Statement, gen_JDTAST_VariableDeclarationStatement_Statement, gen_JDTAST_WhileStatement_Statement, gen_JDTAST_ArrayType_Type, gen_JDTAST_ParameterizedType_Type, gen_JDTAST_PrimitiveType_Type, gen_JDTAST_QualifiedType_Type, gen_JDTAST_SimpleType_Type, gen_JDTAST_WildcardType_Type, gen_JDTAST_SingleVariableDeclaration_VariableDeclaration, gen_JDTAST_VariableDeclarationFragment_VariableDeclaration, gen_JDTAST_QualifiedName_Name, gen_JDTAST_SimpleName_Name, gen_JDTAST_MarkerAnnotation_Annotation, gen_JDTAST_NormalAnnotation_Annotation, gen_JDTAST_SingleMemberAnnotation_Annotation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)