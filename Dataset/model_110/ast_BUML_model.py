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

# Classes
IExtendedModifier = Class(name="IExtendedModifier")
ast_ASTNode = Class(name="ast::ASTNode")
ast_MarkerAnnotation = Class(name="ast::MarkerAnnotation")
Annotation = Class(name="Annotation")
ast_Name = Class(name="ast::Name")
ast_Annotation = Class(name="ast::Annotation")
Expression = Class(name="Expression")
ast_Expression = Class(name="ast::Expression")
ast_NormalAnnotation = Class(name="ast::NormalAnnotation")
ast_IExtendedModifier = Class(name="ast::IExtendedModifier")
ast_Modifier = Class(name="ast::Modifier")
ASTNode = Class(name="ASTNode")
ast_IDocElement = Class(name="ast::IDocElement")
ast_MemberRef = Class(name="ast::MemberRef")
IDocElement = Class(name="IDocElement")
ast_SimpleName = Class(name="ast::SimpleName")
ast_MethodRef = Class(name="ast::MethodRef")
ast_MethodRefParameter = Class(name="ast::MethodRefParameter")
ast_MemberValuePair = Class(name="ast::MemberValuePair")
ast_SingleMemberAnnotation = Class(name="ast::SingleMemberAnnotation")
ast_TextElement = Class(name="ast::TextElement")
ast_AnonymousClassDeclaration = Class(name="ast::AnonymousClassDeclaration")
ast_BodyDeclaration = Class(name="ast::BodyDeclaration")
ast_ArrayAccess = Class(name="ast::ArrayAccess")
ast_ArrayCreation = Class(name="ast::ArrayCreation")
ast_ArrayType = Class(name="ast::ArrayType")
ast_TagElement = Class(name="ast::TagElement")
Type = Class(name="Type")
ast_Statement = Class(name="ast::Statement")
ast_Assignment = Class(name="ast::Assignment")
ast_ArrayInitializer = Class(name="ast::ArrayInitializer")
ast_Type = Class(name="ast::Type")
ast_Dimension = Class(name="ast::Dimension")
ast_AssertStatement = Class(name="ast::AssertStatement")
Statement = Class(name="Statement")
ast_CastExpression = Class(name="ast::CastExpression")
ast_CatchClause = Class(name="ast::CatchClause")
ast_SingleVariableDeclaration = Class(name="ast::SingleVariableDeclaration")
ast_CharacterLiteral = Class(name="ast::CharacterLiteral")
ast_ClassInstanceCreation = Class(name="ast::ClassInstanceCreation")
ast_Block = Class(name="ast::Block")
ast_BooleanLiteral = Class(name="ast::BooleanLiteral")
ast_BreakStatement = Class(name="ast::BreakStatement")
ast_CompilationUnit = Class(name="ast::CompilationUnit")
ast_PackageDeclaration = Class(name="ast::PackageDeclaration")
ast_ImportDeclaration = Class(name="ast::ImportDeclaration")
ast_AbstractTypeDeclaration = Class(name="ast::AbstractTypeDeclaration")
ast_ConditionalExpression = Class(name="ast::ConditionalExpression")
ast_ContinueStatement = Class(name="ast::ContinueStatement")
ast_DoStatement = Class(name="ast::DoStatement")
ast_ConstructorInvocation = Class(name="ast::ConstructorInvocation")
ast_FieldDeclaration = Class(name="ast::FieldDeclaration")
BodyDeclaration = Class(name="BodyDeclaration")
ast_Javadoc = Class(name="ast::Javadoc")
ast_VariableDeclarationFragment = Class(name="ast::VariableDeclarationFragment")
ast_ForStatement = Class(name="ast::ForStatement")
ast_EmptyStatement = Class(name="ast::EmptyStatement")
ast_ExpressionStatement = Class(name="ast::ExpressionStatement")
ast_FieldAccess = Class(name="ast::FieldAccess")
ast_InfixExpression = Class(name="ast::InfixExpression")
ast_IfStatement = Class(name="ast::IfStatement")
Comment = Class(name="Comment")
ast_Comment = Class(name="ast::Comment")
ast_LabeledStatement = Class(name="ast::LabeledStatement")
ast_MethodDeclaration = Class(name="ast::MethodDeclaration")
ast_Initializer = Class(name="ast::Initializer")
ast_MethodInvocation = Class(name="ast::MethodInvocation")
ast_TypeParameter = Class(name="ast::TypeParameter")
ast_NullLiteral = Class(name="ast::NullLiteral")
ast_NumberLiteral = Class(name="ast::NumberLiteral")
ast_ParenthesizedExpression = Class(name="ast::ParenthesizedExpression")
ast_PrimitiveType = Class(name="ast::PrimitiveType")
AnnotatableType = Class(name="AnnotatableType")
ast_AnnotatableType = Class(name="ast::AnnotatableType")
ast_QualifiedName = Class(name="ast::QualifiedName")
Name = Class(name="Name")
ast_PostfixExpression = Class(name="ast::PostfixExpression")
ast_PrefixExpression = Class(name="ast::PrefixExpression")
VariableDeclaration = Class(name="VariableDeclaration")
ast_ReturnStatement = Class(name="ast::ReturnStatement")
ast_SimpleType = Class(name="ast::SimpleType")
ast_SuperConstructorInvocation = Class(name="ast::SuperConstructorInvocation")
ast_SuperFieldAccess = Class(name="ast::SuperFieldAccess")
ast_VariableDeclaration = Class(name="ast::VariableDeclaration")
ast_StringLiteral = Class(name="ast::StringLiteral")
ast_SwitchCase = Class(name="ast::SwitchCase")
ast_SwitchStatement = Class(name="ast::SwitchStatement")
ast_SuperMethodInvocation = Class(name="ast::SuperMethodInvocation")
ast_ThrowStatement = Class(name="ast::ThrowStatement")
ast_TryStatement = Class(name="ast::TryStatement")
ast_VariableDeclarationExpression = Class(name="ast::VariableDeclarationExpression")
ast_SynchronizedStatement = Class(name="ast::SynchronizedStatement")
ast_ThisExpression = Class(name="ast::ThisExpression")
ast_TypeDeclarationStatement = Class(name="ast::TypeDeclarationStatement")
ast_TypeDeclaration = Class(name="ast::TypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
ast_TypeLiteral = Class(name="ast::TypeLiteral")
ast_WhileStatement = Class(name="ast::WhileStatement")
ast_InstanceofExpression = Class(name="ast::InstanceofExpression")
ast_VariableDeclarationStatement = Class(name="ast::VariableDeclarationStatement")
ast_EnhancedForStatement = Class(name="ast::EnhancedForStatement")
ast_EnumDeclaration = Class(name="ast::EnumDeclaration")
ast_LineComment = Class(name="ast::LineComment")
ast_BlockComment = Class(name="ast::BlockComment")
ast_ParameterizedType = Class(name="ast::ParameterizedType")
ast_EnumConstantDeclaration = Class(name="ast::EnumConstantDeclaration")
ast_AnnotationTypeDeclaration = Class(name="ast::AnnotationTypeDeclaration")
ast_AnnotationTypeMemberDeclaration = Class(name="ast::AnnotationTypeMemberDeclaration")
ast_QualifiedType = Class(name="ast::QualifiedType")
ast_WildcardType = Class(name="ast::WildcardType")
ast_LambdaExpression = Class(name="ast::LambdaExpression")
ast_IntersectionType = Class(name="ast::IntersectionType")
ast_NameQualifiedType = Class(name="ast::NameQualifiedType")
ast_UnionType = Class(name="ast::UnionType")
ast_SuperMethodReference = Class(name="ast::SuperMethodReference")
ast_CreationReference = Class(name="ast::CreationReference")
MethodReference = Class(name="MethodReference")
ast_MethodReference = Class(name="ast::MethodReference")
ast_ExpressionMethodReference = Class(name="ast::ExpressionMethodReference")
ast_TypeMethodReference = Class(name="ast::TypeMethodReference")

# IExtendedModifier class attributes and methods

# ast_ASTNode class attributes and methods

# ast_MarkerAnnotation class attributes and methods

# Annotation class attributes and methods

# ast_Name class attributes and methods

# ast_Annotation class attributes and methods

# Expression class attributes and methods

# ast_Expression class attributes and methods

# ast_NormalAnnotation class attributes and methods

# ast_IExtendedModifier class attributes and methods

# ast_Modifier class attributes and methods
ast_Modifier_keyword: Property = Property(name="keyword", type=StringType)
ast_Modifier.attributes={ast_Modifier_keyword}

# ASTNode class attributes and methods

# ast_IDocElement class attributes and methods

# ast_MemberRef class attributes and methods

# IDocElement class attributes and methods

# ast_SimpleName class attributes and methods
ast_SimpleName_identifier: Property = Property(name="identifier", type=StringType)
ast_SimpleName.attributes={ast_SimpleName_identifier}

# ast_MethodRef class attributes and methods

# ast_MethodRefParameter class attributes and methods
ast_MethodRefParameter_varargs: Property = Property(name="varargs", type=BooleanType)
ast_MethodRefParameter.attributes={ast_MethodRefParameter_varargs}

# ast_MemberValuePair class attributes and methods

# ast_SingleMemberAnnotation class attributes and methods

# ast_TextElement class attributes and methods
ast_TextElement_text: Property = Property(name="text", type=StringType)
ast_TextElement.attributes={ast_TextElement_text}

# ast_AnonymousClassDeclaration class attributes and methods

# ast_BodyDeclaration class attributes and methods

# ast_ArrayAccess class attributes and methods

# ast_ArrayCreation class attributes and methods

# ast_ArrayType class attributes and methods

# ast_TagElement class attributes and methods
ast_TagElement_tagName: Property = Property(name="tagName", type=StringType)
ast_TagElement.attributes={ast_TagElement_tagName}

# Type class attributes and methods

# ast_Statement class attributes and methods

# ast_Assignment class attributes and methods
ast_Assignment_operator: Property = Property(name="operator", type=StringType)
ast_Assignment.attributes={ast_Assignment_operator}

# ast_ArrayInitializer class attributes and methods

# ast_Type class attributes and methods

# ast_Dimension class attributes and methods

# ast_AssertStatement class attributes and methods

# Statement class attributes and methods

# ast_CastExpression class attributes and methods

# ast_CatchClause class attributes and methods

# ast_SingleVariableDeclaration class attributes and methods
ast_SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=BooleanType)
ast_SingleVariableDeclaration.attributes={ast_SingleVariableDeclaration_varargs}

# ast_CharacterLiteral class attributes and methods
ast_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
ast_CharacterLiteral.attributes={ast_CharacterLiteral_escapedValue}

# ast_ClassInstanceCreation class attributes and methods

# ast_Block class attributes and methods

# ast_BooleanLiteral class attributes and methods
ast_BooleanLiteral_booleanValue: Property = Property(name="booleanValue", type=BooleanType)
ast_BooleanLiteral.attributes={ast_BooleanLiteral_booleanValue}

# ast_BreakStatement class attributes and methods

# ast_CompilationUnit class attributes and methods

# ast_PackageDeclaration class attributes and methods

# ast_ImportDeclaration class attributes and methods
ast_ImportDeclaration_static: Property = Property(name="static", type=BooleanType)
ast_ImportDeclaration_onDemand: Property = Property(name="onDemand", type=BooleanType)
ast_ImportDeclaration.attributes={ast_ImportDeclaration_static, ast_ImportDeclaration_onDemand}

# ast_AbstractTypeDeclaration class attributes and methods

# ast_ConditionalExpression class attributes and methods

# ast_ContinueStatement class attributes and methods

# ast_DoStatement class attributes and methods

# ast_ConstructorInvocation class attributes and methods

# ast_FieldDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# ast_Javadoc class attributes and methods

# ast_VariableDeclarationFragment class attributes and methods

# ast_ForStatement class attributes and methods

# ast_EmptyStatement class attributes and methods

# ast_ExpressionStatement class attributes and methods

# ast_FieldAccess class attributes and methods

# ast_InfixExpression class attributes and methods
ast_InfixExpression_operator: Property = Property(name="operator", type=StringType)
ast_InfixExpression.attributes={ast_InfixExpression_operator}

# ast_IfStatement class attributes and methods

# Comment class attributes and methods

# ast_Comment class attributes and methods

# ast_LabeledStatement class attributes and methods

# ast_MethodDeclaration class attributes and methods
ast_MethodDeclaration_constructor: Property = Property(name="constructor", type=BooleanType)
ast_MethodDeclaration.attributes={ast_MethodDeclaration_constructor}

# ast_Initializer class attributes and methods

# ast_MethodInvocation class attributes and methods

# ast_TypeParameter class attributes and methods

# ast_NullLiteral class attributes and methods

# ast_NumberLiteral class attributes and methods
ast_NumberLiteral_token: Property = Property(name="token", type=StringType)
ast_NumberLiteral.attributes={ast_NumberLiteral_token}

# ast_ParenthesizedExpression class attributes and methods

# ast_PrimitiveType class attributes and methods
ast_PrimitiveType_primitiveTypeCode: Property = Property(name="primitiveTypeCode", type=StringType)
ast_PrimitiveType.attributes={ast_PrimitiveType_primitiveTypeCode}

# AnnotatableType class attributes and methods

# ast_AnnotatableType class attributes and methods

# ast_QualifiedName class attributes and methods

# Name class attributes and methods

# ast_PostfixExpression class attributes and methods
ast_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
ast_PostfixExpression.attributes={ast_PostfixExpression_operator}

# ast_PrefixExpression class attributes and methods
ast_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
ast_PrefixExpression.attributes={ast_PrefixExpression_operator}

# VariableDeclaration class attributes and methods

# ast_ReturnStatement class attributes and methods

# ast_SimpleType class attributes and methods

# ast_SuperConstructorInvocation class attributes and methods

# ast_SuperFieldAccess class attributes and methods

# ast_VariableDeclaration class attributes and methods

# ast_StringLiteral class attributes and methods
ast_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
ast_StringLiteral.attributes={ast_StringLiteral_escapedValue}

# ast_SwitchCase class attributes and methods

# ast_SwitchStatement class attributes and methods

# ast_SuperMethodInvocation class attributes and methods

# ast_ThrowStatement class attributes and methods

# ast_TryStatement class attributes and methods

# ast_VariableDeclarationExpression class attributes and methods

# ast_SynchronizedStatement class attributes and methods

# ast_ThisExpression class attributes and methods

# ast_TypeDeclarationStatement class attributes and methods

# ast_TypeDeclaration class attributes and methods
ast_TypeDeclaration_interface: Property = Property(name="interface", type=BooleanType)
ast_TypeDeclaration.attributes={ast_TypeDeclaration_interface}

# AbstractTypeDeclaration class attributes and methods

# ast_TypeLiteral class attributes and methods

# ast_WhileStatement class attributes and methods

# ast_InstanceofExpression class attributes and methods

# ast_VariableDeclarationStatement class attributes and methods

# ast_EnhancedForStatement class attributes and methods

# ast_EnumDeclaration class attributes and methods

# ast_LineComment class attributes and methods

# ast_BlockComment class attributes and methods

# ast_ParameterizedType class attributes and methods

# ast_EnumConstantDeclaration class attributes and methods

# ast_AnnotationTypeDeclaration class attributes and methods

# ast_AnnotationTypeMemberDeclaration class attributes and methods

# ast_QualifiedType class attributes and methods

# ast_WildcardType class attributes and methods
ast_WildcardType_upperBound: Property = Property(name="upperBound", type=BooleanType)
ast_WildcardType.attributes={ast_WildcardType_upperBound}

# ast_LambdaExpression class attributes and methods
ast_LambdaExpression_parentheses: Property = Property(name="parentheses", type=BooleanType)
ast_LambdaExpression.attributes={ast_LambdaExpression_parentheses}

# ast_IntersectionType class attributes and methods

# ast_NameQualifiedType class attributes and methods

# ast_UnionType class attributes and methods

# ast_SuperMethodReference class attributes and methods

# ast_CreationReference class attributes and methods

# MethodReference class attributes and methods

# ast_MethodReference class attributes and methods

# ast_ExpressionMethodReference class attributes and methods

# ast_TypeMethodReference class attributes and methods

# Relationships
typeName0: BinaryAssociation = BinaryAssociation(
    name="typeName0",
    ends={
        Property(name="ast_Name", type=ast_MarkerAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MarkerAnnotation", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName1: BinaryAssociation = BinaryAssociation(
    name="typeName1",
    ends={
        Property(name="ast_Name2", type=ast_NormalAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NormalAnnotation", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier9: BinaryAssociation = BinaryAssociation(
    name="qualifier9",
    ends={
        Property(name="ast_Name10", type=ast_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MemberRef", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name11: BinaryAssociation = BinaryAssociation(
    name="name11",
    ends={
        Property(name="ast_SimpleName", type=ast_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MemberRef12", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier13: BinaryAssociation = BinaryAssociation(
    name="qualifier13",
    ends={
        Property(name="ast_Name14", type=ast_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodRef", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name15: BinaryAssociation = BinaryAssociation(
    name="name15",
    ends={
        Property(name="ast_SimpleName17", type=ast_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodRef16", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values3: BinaryAssociation = BinaryAssociation(
    name="values3",
    ends={
        Property(name="ast_MemberValuePair", type=ast_NormalAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NormalAnnotation4", type=ast_MemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeName5: BinaryAssociation = BinaryAssociation(
    name="typeName5",
    ends={
        Property(name="ast_Name6", type=ast_SingleMemberAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SingleMemberAnnotation", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="ast_Expression", type=ast_SingleMemberAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SingleMemberAnnotation8", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments20: BinaryAssociation = BinaryAssociation(
    name="fragments20",
    ends={
        Property(name="ast_IDocElement", type=ast_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TagElement", type=ast_IDocElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations21: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations21",
    ends={
        Property(name="ast_BodyDeclaration", type=ast_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AnonymousClassDeclaration", type=ast_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
array22: BinaryAssociation = BinaryAssociation(
    name="array22",
    ends={
        Property(name="ast_Expression23", type=ast_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayAccess", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index24: BinaryAssociation = BinaryAssociation(
    name="index24",
    ends={
        Property(name="ast_Expression26", type=ast_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayAccess25", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="ast_ArrayType", type=ast_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayCreation", type=ast_ArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters18: BinaryAssociation = BinaryAssociation(
    name="parameters18",
    ends={
        Property(name="ast_MethodRefParameter", type=ast_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodRef19", type=ast_MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer31: BinaryAssociation = BinaryAssociation(
    name="initializer31",
    ends={
        Property(name="ast_ArrayInitializer", type=ast_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayCreation32", type=ast_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions33: BinaryAssociation = BinaryAssociation(
    name="expressions33",
    ends={
        Property(name="ast_Expression35", type=ast_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayInitializer34", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimensions28: BinaryAssociation = BinaryAssociation(
    name="dimensions28",
    ends={
        Property(name="ast_Expression30", type=ast_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayCreation29", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftHandSide45: BinaryAssociation = BinaryAssociation(
    name="leftHandSide45",
    ends={
        Property(name="ast_Expression46", type=ast_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Assignment", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightHandSide47: BinaryAssociation = BinaryAssociation(
    name="rightHandSide47",
    ends={
        Property(name="ast_Expression49", type=ast_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Assignment48", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType36: BinaryAssociation = BinaryAssociation(
    name="elementType36",
    ends={
        Property(name="ast_Type", type=ast_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayType37", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimensions38: BinaryAssociation = BinaryAssociation(
    name="dimensions38",
    ends={
        Property(name="ast_Dimension", type=ast_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayType39", type=ast_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression40: BinaryAssociation = BinaryAssociation(
    name="expression40",
    ends={
        Property(name="ast_Expression41", type=ast_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AssertStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message42: BinaryAssociation = BinaryAssociation(
    name="message42",
    ends={
        Property(name="ast_Expression44", type=ast_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AssertStatement43", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label51: BinaryAssociation = BinaryAssociation(
    name="label51",
    ends={
        Property(name="ast_SimpleName52", type=ast_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_BreakStatement", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type53: BinaryAssociation = BinaryAssociation(
    name="type53",
    ends={
        Property(name="ast_Type54", type=ast_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CastExpression", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression55: BinaryAssociation = BinaryAssociation(
    name="expression55",
    ends={
        Property(name="ast_Expression57", type=ast_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CastExpression56", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception58: BinaryAssociation = BinaryAssociation(
    name="exception58",
    ends={
        Property(name="ast_SingleVariableDeclaration", type=ast_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CatchClause", type=ast_SingleVariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body59: BinaryAssociation = BinaryAssociation(
    name="body59",
    ends={
        Property(name="ast_Block61", type=ast_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CatchClause60", type=ast_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements50: BinaryAssociation = BinaryAssociation(
    name="statements50",
    ends={
        Property(name="ast_Statement", type=ast_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Block", type=ast_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package76: BinaryAssociation = BinaryAssociation(
    name="package76",
    ends={
        Property(name="ast_PackageDeclaration", type=ast_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CompilationUnit", type=ast_PackageDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports77: BinaryAssociation = BinaryAssociation(
    name="imports77",
    ends={
        Property(name="ast_ImportDeclaration", type=ast_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CompilationUnit78", type=ast_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types79: BinaryAssociation = BinaryAssociation(
    name="types79",
    ends={
        Property(name="ast_AbstractTypeDeclaration", type=ast_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CompilationUnit80", type=ast_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression62: BinaryAssociation = BinaryAssociation(
    name="expression62",
    ends={
        Property(name="ast_Expression63", type=ast_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassInstanceCreation", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments64: BinaryAssociation = BinaryAssociation(
    name="typeArguments64",
    ends={
        Property(name="ast_Type66", type=ast_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassInstanceCreation65", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type67: BinaryAssociation = BinaryAssociation(
    name="type67",
    ends={
        Property(name="ast_Type69", type=ast_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassInstanceCreation68", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments70: BinaryAssociation = BinaryAssociation(
    name="arguments70",
    ends={
        Property(name="ast_Expression72", type=ast_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassInstanceCreation71", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments89: BinaryAssociation = BinaryAssociation(
    name="typeArguments89",
    ends={
        Property(name="ast_Type90", type=ast_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ConstructorInvocation", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration73: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration73",
    ends={
        Property(name="ast_AnonymousClassDeclaration75", type=ast_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ClassInstanceCreation74", type=ast_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments91: BinaryAssociation = BinaryAssociation(
    name="arguments91",
    ends={
        Property(name="ast_Expression93", type=ast_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ConstructorInvocation92", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label94: BinaryAssociation = BinaryAssociation(
    name="label94",
    ends={
        Property(name="ast_SimpleName95", type=ast_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ContinueStatement", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body96: BinaryAssociation = BinaryAssociation(
    name="body96",
    ends={
        Property(name="ast_Statement97", type=ast_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_DoStatement", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression98: BinaryAssociation = BinaryAssociation(
    name="expression98",
    ends={
        Property(name="ast_Expression100", type=ast_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_DoStatement99", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression81: BinaryAssociation = BinaryAssociation(
    name="expression81",
    ends={
        Property(name="ast_Expression82", type=ast_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ConditionalExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression83: BinaryAssociation = BinaryAssociation(
    name="thenExpression83",
    ends={
        Property(name="ast_Expression85", type=ast_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ConditionalExpression84", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression86: BinaryAssociation = BinaryAssociation(
    name="elseExpression86",
    ends={
        Property(name="ast_Expression88", type=ast_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ConditionalExpression87", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
javadoc108: BinaryAssociation = BinaryAssociation(
    name="javadoc108",
    ends={
        Property(name="ast_Javadoc", type=ast_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FieldDeclaration", type=ast_Javadoc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers109: BinaryAssociation = BinaryAssociation(
    name="modifiers109",
    ends={
        Property(name="ast_IExtendedModifier", type=ast_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FieldDeclaration110", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type111: BinaryAssociation = BinaryAssociation(
    name="type111",
    ends={
        Property(name="ast_Type113", type=ast_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FieldDeclaration112", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments114: BinaryAssociation = BinaryAssociation(
    name="fragments114",
    ends={
        Property(name="ast_VariableDeclarationFragment", type=ast_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FieldDeclaration115", type=ast_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializers116: BinaryAssociation = BinaryAssociation(
    name="initializers116",
    ends={
        Property(name="ast_Expression117", type=ast_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForStatement", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression118: BinaryAssociation = BinaryAssociation(
    name="expression118",
    ends={
        Property(name="ast_Expression120", type=ast_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForStatement119", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression101: BinaryAssociation = BinaryAssociation(
    name="expression101",
    ends={
        Property(name="ast_Expression102", type=ast_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ExpressionStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression103: BinaryAssociation = BinaryAssociation(
    name="expression103",
    ends={
        Property(name="ast_Expression104", type=ast_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FieldAccess", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name105: BinaryAssociation = BinaryAssociation(
    name="name105",
    ends={
        Property(name="ast_SimpleName107", type=ast_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FieldAccess106", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement132: BinaryAssociation = BinaryAssociation(
    name="elseStatement132",
    ends={
        Property(name="ast_Statement134", type=ast_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfStatement133", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name135: BinaryAssociation = BinaryAssociation(
    name="name135",
    ends={
        Property(name="ast_Name137", type=ast_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ImportDeclaration136", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand138: BinaryAssociation = BinaryAssociation(
    name="leftOperand138",
    ends={
        Property(name="ast_Expression139", type=ast_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_InfixExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand140: BinaryAssociation = BinaryAssociation(
    name="rightOperand140",
    ends={
        Property(name="ast_Expression142", type=ast_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_InfixExpression141", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedOperands143: BinaryAssociation = BinaryAssociation(
    name="extendedOperands143",
    ends={
        Property(name="ast_Expression145", type=ast_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_InfixExpression144", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updaters121: BinaryAssociation = BinaryAssociation(
    name="updaters121",
    ends={
        Property(name="ast_Expression123", type=ast_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForStatement122", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body124: BinaryAssociation = BinaryAssociation(
    name="body124",
    ends={
        Property(name="ast_Statement126", type=ast_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForStatement125", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression127: BinaryAssociation = BinaryAssociation(
    name="expression127",
    ends={
        Property(name="ast_Expression128", type=ast_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenStatement129: BinaryAssociation = BinaryAssociation(
    name="thenStatement129",
    ends={
        Property(name="ast_Statement131", type=ast_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfStatement130", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tags154: BinaryAssociation = BinaryAssociation(
    name="tags154",
    ends={
        Property(name="ast_TagElement156", type=ast_Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Javadoc155", type=ast_TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label157: BinaryAssociation = BinaryAssociation(
    name="label157",
    ends={
        Property(name="ast_SimpleName158", type=ast_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LabeledStatement", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body159: BinaryAssociation = BinaryAssociation(
    name="body159",
    ends={
        Property(name="ast_Statement161", type=ast_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LabeledStatement160", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
javadoc162: BinaryAssociation = BinaryAssociation(
    name="javadoc162",
    ends={
        Property(name="ast_Javadoc163", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration", type=ast_Javadoc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers164: BinaryAssociation = BinaryAssociation(
    name="modifiers164",
    ends={
        Property(name="ast_IExtendedModifier166", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration165", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc146: BinaryAssociation = BinaryAssociation(
    name="javadoc146",
    ends={
        Property(name="ast_Javadoc147", type=ast_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Initializer", type=ast_Javadoc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers148: BinaryAssociation = BinaryAssociation(
    name="modifiers148",
    ends={
        Property(name="ast_IExtendedModifier150", type=ast_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Initializer149", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body151: BinaryAssociation = BinaryAssociation(
    name="body151",
    ends={
        Property(name="ast_Block153", type=ast_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Initializer152", type=ast_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiverType175: BinaryAssociation = BinaryAssociation(
    name="receiverType175",
    ends={
        Property(name="ast_Type177", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration176", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiverQualifier178: BinaryAssociation = BinaryAssociation(
    name="receiverQualifier178",
    ends={
        Property(name="ast_SimpleName180", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration179", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters181: BinaryAssociation = BinaryAssociation(
    name="parameters181",
    ends={
        Property(name="ast_SingleVariableDeclaration183", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration182", type=ast_SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extraDimensions2184: BinaryAssociation = BinaryAssociation(
    name="extraDimensions2184",
    ends={
        Property(name="ast_Dimension186", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration185", type=ast_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thrownExceptionTypes187: BinaryAssociation = BinaryAssociation(
    name="thrownExceptionTypes187",
    ends={
        Property(name="ast_Type189", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration188", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body190: BinaryAssociation = BinaryAssociation(
    name="body190",
    ends={
        Property(name="ast_Block192", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration191", type=ast_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters167: BinaryAssociation = BinaryAssociation(
    name="typeParameters167",
    ends={
        Property(name="ast_TypeParameter", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration168", type=ast_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType2169: BinaryAssociation = BinaryAssociation(
    name="returnType2169",
    ends={
        Property(name="ast_Type171", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration170", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name172: BinaryAssociation = BinaryAssociation(
    name="name172",
    ends={
        Property(name="ast_SimpleName174", type=ast_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodDeclaration173", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments201: BinaryAssociation = BinaryAssociation(
    name="arguments201",
    ends={
        Property(name="ast_Expression203", type=ast_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodInvocation202", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc204: BinaryAssociation = BinaryAssociation(
    name="javadoc204",
    ends={
        Property(name="ast_Javadoc206", type=ast_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PackageDeclaration205", type=ast_Javadoc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations207: BinaryAssociation = BinaryAssociation(
    name="annotations207",
    ends={
        Property(name="ast_Annotation", type=ast_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PackageDeclaration208", type=ast_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name209: BinaryAssociation = BinaryAssociation(
    name="name209",
    ends={
        Property(name="ast_Name211", type=ast_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PackageDeclaration210", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression193: BinaryAssociation = BinaryAssociation(
    name="expression193",
    ends={
        Property(name="ast_Expression194", type=ast_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodInvocation", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments195: BinaryAssociation = BinaryAssociation(
    name="typeArguments195",
    ends={
        Property(name="ast_Type197", type=ast_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodInvocation196", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name198: BinaryAssociation = BinaryAssociation(
    name="name198",
    ends={
        Property(name="ast_SimpleName200", type=ast_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodInvocation199", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand216: BinaryAssociation = BinaryAssociation(
    name="operand216",
    ends={
        Property(name="ast_Expression217", type=ast_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PrefixExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations218: BinaryAssociation = BinaryAssociation(
    name="annotations218",
    ends={
        Property(name="ast_Annotation219", type=ast_PrimitiveType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PrimitiveType", type=ast_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier220: BinaryAssociation = BinaryAssociation(
    name="qualifier220",
    ends={
        Property(name="ast_Name221", type=ast_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_QualifiedName", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name222: BinaryAssociation = BinaryAssociation(
    name="name222",
    ends={
        Property(name="ast_SimpleName224", type=ast_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_QualifiedName223", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression212: BinaryAssociation = BinaryAssociation(
    name="expression212",
    ends={
        Property(name="ast_Expression213", type=ast_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ParenthesizedExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand214: BinaryAssociation = BinaryAssociation(
    name="operand214",
    ends={
        Property(name="ast_Expression215", type=ast_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PostfixExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations227: BinaryAssociation = BinaryAssociation(
    name="annotations227",
    ends={
        Property(name="ast_Annotation228", type=ast_SimpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SimpleType", type=ast_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name229: BinaryAssociation = BinaryAssociation(
    name="name229",
    ends={
        Property(name="ast_Name231", type=ast_SimpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SimpleType230", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers232: BinaryAssociation = BinaryAssociation(
    name="modifiers232",
    ends={
        Property(name="ast_IExtendedModifier234", type=ast_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SingleVariableDeclaration233", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type235: BinaryAssociation = BinaryAssociation(
    name="type235",
    ends={
        Property(name="ast_Type237", type=ast_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SingleVariableDeclaration236", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varargsAnnotations238: BinaryAssociation = BinaryAssociation(
    name="varargsAnnotations238",
    ends={
        Property(name="ast_Annotation240", type=ast_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SingleVariableDeclaration239", type=ast_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name241: BinaryAssociation = BinaryAssociation(
    name="name241",
    ends={
        Property(name="ast_SimpleName243", type=ast_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SingleVariableDeclaration242", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression225: BinaryAssociation = BinaryAssociation(
    name="expression225",
    ends={
        Property(name="ast_Expression226", type=ast_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ReturnStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression250: BinaryAssociation = BinaryAssociation(
    name="expression250",
    ends={
        Property(name="ast_Expression251", type=ast_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperConstructorInvocation", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments252: BinaryAssociation = BinaryAssociation(
    name="typeArguments252",
    ends={
        Property(name="ast_Type254", type=ast_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperConstructorInvocation253", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments255: BinaryAssociation = BinaryAssociation(
    name="arguments255",
    ends={
        Property(name="ast_Expression257", type=ast_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperConstructorInvocation256", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extraDimensions2244: BinaryAssociation = BinaryAssociation(
    name="extraDimensions2244",
    ends={
        Property(name="ast_Dimension246", type=ast_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SingleVariableDeclaration245", type=ast_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer247: BinaryAssociation = BinaryAssociation(
    name="initializer247",
    ends={
        Property(name="ast_Expression249", type=ast_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SingleVariableDeclaration248", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name268: BinaryAssociation = BinaryAssociation(
    name="name268",
    ends={
        Property(name="ast_SuperMethodInvocation269", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ast_SimpleName270", type=ast_SuperMethodInvocation, multiplicity=Multiplicity(1, 1))
    }
)
arguments271: BinaryAssociation = BinaryAssociation(
    name="arguments271",
    ends={
        Property(name="ast_Expression273", type=ast_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperMethodInvocation272", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression274: BinaryAssociation = BinaryAssociation(
    name="expression274",
    ends={
        Property(name="ast_Expression275", type=ast_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchCase", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression276: BinaryAssociation = BinaryAssociation(
    name="expression276",
    ends={
        Property(name="ast_Expression277", type=ast_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier258: BinaryAssociation = BinaryAssociation(
    name="qualifier258",
    ends={
        Property(name="ast_Name259", type=ast_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperFieldAccess", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements278: BinaryAssociation = BinaryAssociation(
    name="statements278",
    ends={
        Property(name="ast_Statement280", type=ast_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchStatement279", type=ast_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name260: BinaryAssociation = BinaryAssociation(
    name="name260",
    ends={
        Property(name="ast_SimpleName262", type=ast_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperFieldAccess261", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier263: BinaryAssociation = BinaryAssociation(
    name="qualifier263",
    ends={
        Property(name="ast_Name264", type=ast_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperMethodInvocation", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments265: BinaryAssociation = BinaryAssociation(
    name="typeArguments265",
    ends={
        Property(name="ast_Type267", type=ast_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperMethodInvocation266", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier286: BinaryAssociation = BinaryAssociation(
    name="qualifier286",
    ends={
        Property(name="ast_Name287", type=ast_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ThisExpression", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression288: BinaryAssociation = BinaryAssociation(
    name="expression288",
    ends={
        Property(name="ast_Expression289", type=ast_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ThrowStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resources290: BinaryAssociation = BinaryAssociation(
    name="resources290",
    ends={
        Property(name="ast_VariableDeclarationExpression", type=ast_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TryStatement", type=ast_VariableDeclarationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body291: BinaryAssociation = BinaryAssociation(
    name="body291",
    ends={
        Property(name="ast_Block293", type=ast_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TryStatement292", type=ast_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses294: BinaryAssociation = BinaryAssociation(
    name="catchClauses294",
    ends={
        Property(name="ast_CatchClause296", type=ast_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TryStatement295", type=ast_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression281: BinaryAssociation = BinaryAssociation(
    name="expression281",
    ends={
        Property(name="ast_Expression282", type=ast_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SynchronizedStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body283: BinaryAssociation = BinaryAssociation(
    name="body283",
    ends={
        Property(name="ast_Block285", type=ast_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SynchronizedStatement284", type=ast_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name305: BinaryAssociation = BinaryAssociation(
    name="name305",
    ends={
        Property(name="ast_SimpleName307", type=ast_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeDeclaration306", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters308: BinaryAssociation = BinaryAssociation(
    name="typeParameters308",
    ends={
        Property(name="ast_TypeParameter310", type=ast_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeDeclaration309", type=ast_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclassType311: BinaryAssociation = BinaryAssociation(
    name="superclassType311",
    ends={
        Property(name="ast_Type313", type=ast_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeDeclaration312", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superInterfaceTypes314: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes314",
    ends={
        Property(name="ast_Type316", type=ast_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeDeclaration315", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations317: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations317",
    ends={
        Property(name="ast_BodyDeclaration319", type=ast_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeDeclaration318", type=ast_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration320: BinaryAssociation = BinaryAssociation(
    name="declaration320",
    ends={
        Property(name="ast_AbstractTypeDeclaration321", type=ast_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeDeclarationStatement", type=ast_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finally297: BinaryAssociation = BinaryAssociation(
    name="finally297",
    ends={
        Property(name="ast_Block299", type=ast_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TryStatement298", type=ast_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
javadoc300: BinaryAssociation = BinaryAssociation(
    name="javadoc300",
    ends={
        Property(name="ast_Javadoc301", type=ast_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeDeclaration", type=ast_Javadoc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers302: BinaryAssociation = BinaryAssociation(
    name="modifiers302",
    ends={
        Property(name="ast_IExtendedModifier304", type=ast_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeDeclaration303", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers324: BinaryAssociation = BinaryAssociation(
    name="modifiers324",
    ends={
        Property(name="ast_IExtendedModifier326", type=ast_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_VariableDeclarationExpression325", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type327: BinaryAssociation = BinaryAssociation(
    name="type327",
    ends={
        Property(name="ast_Type329", type=ast_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_VariableDeclarationExpression328", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments330: BinaryAssociation = BinaryAssociation(
    name="fragments330",
    ends={
        Property(name="ast_VariableDeclarationFragment332", type=ast_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_VariableDeclarationExpression331", type=ast_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name333: BinaryAssociation = BinaryAssociation(
    name="name333",
    ends={
        Property(name="ast_SimpleName335", type=ast_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_VariableDeclarationFragment334", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments347: BinaryAssociation = BinaryAssociation(
    name="fragments347",
    ends={
        Property(name="ast_VariableDeclarationStatement348", type=ast_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ast_VariableDeclarationFragment349", type=ast_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1))
    }
)
type322: BinaryAssociation = BinaryAssociation(
    name="type322",
    ends={
        Property(name="ast_Type323", type=ast_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeLiteral", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression350: BinaryAssociation = BinaryAssociation(
    name="expression350",
    ends={
        Property(name="ast_Expression351", type=ast_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_WhileStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body352: BinaryAssociation = BinaryAssociation(
    name="body352",
    ends={
        Property(name="ast_Statement354", type=ast_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_WhileStatement353", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand355: BinaryAssociation = BinaryAssociation(
    name="leftOperand355",
    ends={
        Property(name="ast_Expression356", type=ast_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_InstanceofExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extraDimensions2336: BinaryAssociation = BinaryAssociation(
    name="extraDimensions2336",
    ends={
        Property(name="ast_Dimension338", type=ast_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_VariableDeclarationFragment337", type=ast_Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer339: BinaryAssociation = BinaryAssociation(
    name="initializer339",
    ends={
        Property(name="ast_Expression341", type=ast_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_VariableDeclarationFragment340", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers342: BinaryAssociation = BinaryAssociation(
    name="modifiers342",
    ends={
        Property(name="ast_IExtendedModifier343", type=ast_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_VariableDeclarationStatement", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type344: BinaryAssociation = BinaryAssociation(
    name="type344",
    ends={
        Property(name="ast_Type346", type=ast_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_VariableDeclarationStatement345", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter366: BinaryAssociation = BinaryAssociation(
    name="parameter366",
    ends={
        Property(name="ast_SingleVariableDeclaration367", type=ast_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnhancedForStatement", type=ast_SingleVariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression368: BinaryAssociation = BinaryAssociation(
    name="expression368",
    ends={
        Property(name="ast_Expression370", type=ast_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnhancedForStatement369", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body371: BinaryAssociation = BinaryAssociation(
    name="body371",
    ends={
        Property(name="ast_Statement373", type=ast_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnhancedForStatement372", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
javadoc374: BinaryAssociation = BinaryAssociation(
    name="javadoc374",
    ends={
        Property(name="ast_Javadoc375", type=ast_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumDeclaration", type=ast_Javadoc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand357: BinaryAssociation = BinaryAssociation(
    name="rightOperand357",
    ends={
        Property(name="ast_Type359", type=ast_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_InstanceofExpression358", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type360: BinaryAssociation = BinaryAssociation(
    name="type360",
    ends={
        Property(name="ast_Type362", type=ast_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodRefParameter361", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name363: BinaryAssociation = BinaryAssociation(
    name="name363",
    ends={
        Property(name="ast_SimpleName365", type=ast_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MethodRefParameter364", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers393: BinaryAssociation = BinaryAssociation(
    name="modifiers393",
    ends={
        Property(name="ast_IExtendedModifier395", type=ast_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumConstantDeclaration394", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name396: BinaryAssociation = BinaryAssociation(
    name="name396",
    ends={
        Property(name="ast_SimpleName398", type=ast_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumConstantDeclaration397", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments399: BinaryAssociation = BinaryAssociation(
    name="arguments399",
    ends={
        Property(name="ast_Expression401", type=ast_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumConstantDeclaration400", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration402: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration402",
    ends={
        Property(name="ast_AnonymousClassDeclaration404", type=ast_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumConstantDeclaration403", type=ast_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers405: BinaryAssociation = BinaryAssociation(
    name="modifiers405",
    ends={
        Property(name="ast_IExtendedModifier407", type=ast_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeParameter406", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name408: BinaryAssociation = BinaryAssociation(
    name="name408",
    ends={
        Property(name="ast_SimpleName410", type=ast_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeParameter409", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeBounds411: BinaryAssociation = BinaryAssociation(
    name="typeBounds411",
    ends={
        Property(name="ast_Type413", type=ast_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeParameter412", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers376: BinaryAssociation = BinaryAssociation(
    name="modifiers376",
    ends={
        Property(name="ast_IExtendedModifier378", type=ast_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumDeclaration377", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type414: BinaryAssociation = BinaryAssociation(
    name="type414",
    ends={
        Property(name="ast_Type415", type=ast_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ParameterizedType", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments416: BinaryAssociation = BinaryAssociation(
    name="typeArguments416",
    ends={
        Property(name="ast_Type418", type=ast_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ParameterizedType417", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name379: BinaryAssociation = BinaryAssociation(
    name="name379",
    ends={
        Property(name="ast_SimpleName381", type=ast_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumDeclaration380", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superInterfaceTypes382: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes382",
    ends={
        Property(name="ast_Type384", type=ast_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumDeclaration383", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumConstants385: BinaryAssociation = BinaryAssociation(
    name="enumConstants385",
    ends={
        Property(name="ast_EnumConstantDeclaration", type=ast_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumDeclaration386", type=ast_EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations387: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations387",
    ends={
        Property(name="ast_BodyDeclaration389", type=ast_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumDeclaration388", type=ast_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc390: BinaryAssociation = BinaryAssociation(
    name="javadoc390",
    ends={
        Property(name="ast_Javadoc392", type=ast_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumConstantDeclaration391", type=ast_Javadoc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name432: BinaryAssociation = BinaryAssociation(
    name="name432",
    ends={
        Property(name="ast_SimpleName434", type=ast_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MemberValuePair433", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value435: BinaryAssociation = BinaryAssociation(
    name="value435",
    ends={
        Property(name="ast_Expression437", type=ast_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MemberValuePair436", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
javadoc438: BinaryAssociation = BinaryAssociation(
    name="javadoc438",
    ends={
        Property(name="ast_Javadoc439", type=ast_AnnotationTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AnnotationTypeDeclaration", type=ast_Javadoc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers440: BinaryAssociation = BinaryAssociation(
    name="modifiers440",
    ends={
        Property(name="ast_IExtendedModifier442", type=ast_AnnotationTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AnnotationTypeDeclaration441", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name443: BinaryAssociation = BinaryAssociation(
    name="name443",
    ends={
        Property(name="ast_SimpleName445", type=ast_AnnotationTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AnnotationTypeDeclaration444", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyDeclarations446: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations446",
    ends={
        Property(name="ast_BodyDeclaration448", type=ast_AnnotationTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AnnotationTypeDeclaration447", type=ast_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc449: BinaryAssociation = BinaryAssociation(
    name="javadoc449",
    ends={
        Property(name="ast_Javadoc450", type=ast_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AnnotationTypeMemberDeclaration", type=ast_Javadoc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers451: BinaryAssociation = BinaryAssociation(
    name="modifiers451",
    ends={
        Property(name="ast_IExtendedModifier453", type=ast_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AnnotationTypeMemberDeclaration452", type=ast_IExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type454: BinaryAssociation = BinaryAssociation(
    name="type454",
    ends={
        Property(name="ast_Type456", type=ast_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AnnotationTypeMemberDeclaration455", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name457: BinaryAssociation = BinaryAssociation(
    name="name457",
    ends={
        Property(name="ast_SimpleName459", type=ast_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AnnotationTypeMemberDeclaration458", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier419: BinaryAssociation = BinaryAssociation(
    name="qualifier419",
    ends={
        Property(name="ast_Type420", type=ast_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_QualifiedType", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations421: BinaryAssociation = BinaryAssociation(
    name="annotations421",
    ends={
        Property(name="ast_Annotation423", type=ast_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_QualifiedType422", type=ast_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name424: BinaryAssociation = BinaryAssociation(
    name="name424",
    ends={
        Property(name="ast_SimpleName426", type=ast_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_QualifiedType425", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations427: BinaryAssociation = BinaryAssociation(
    name="annotations427",
    ends={
        Property(name="ast_Annotation428", type=ast_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_WildcardType", type=ast_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bound429: BinaryAssociation = BinaryAssociation(
    name="bound429",
    ends={
        Property(name="ast_Type431", type=ast_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_WildcardType430", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters468: BinaryAssociation = BinaryAssociation(
    name="parameters468",
    ends={
        Property(name="ast_VariableDeclaration", type=ast_LambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LambdaExpression", type=ast_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body469: BinaryAssociation = BinaryAssociation(
    name="body469",
    ends={
        Property(name="ast_ASTNode", type=ast_LambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LambdaExpression470", type=ast_ASTNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types471: BinaryAssociation = BinaryAssociation(
    name="types471",
    ends={
        Property(name="ast_Type472", type=ast_IntersectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IntersectionType", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier473: BinaryAssociation = BinaryAssociation(
    name="qualifier473",
    ends={
        Property(name="ast_Name474", type=ast_NameQualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NameQualifiedType", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations475: BinaryAssociation = BinaryAssociation(
    name="annotations475",
    ends={
        Property(name="ast_Annotation477", type=ast_NameQualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NameQualifiedType476", type=ast_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name478: BinaryAssociation = BinaryAssociation(
    name="name478",
    ends={
        Property(name="ast_SimpleName480", type=ast_NameQualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NameQualifiedType479", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default460: BinaryAssociation = BinaryAssociation(
    name="default460",
    ends={
        Property(name="ast_Expression462", type=ast_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AnnotationTypeMemberDeclaration461", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types463: BinaryAssociation = BinaryAssociation(
    name="types463",
    ends={
        Property(name="ast_Type464", type=ast_UnionType, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_UnionType", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations465: BinaryAssociation = BinaryAssociation(
    name="annotations465",
    ends={
        Property(name="ast_Annotation467", type=ast_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Dimension466", type=ast_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression486: BinaryAssociation = BinaryAssociation(
    name="expression486",
    ends={
        Property(name="ast_Expression487", type=ast_ExpressionMethodReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ExpressionMethodReference", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments488: BinaryAssociation = BinaryAssociation(
    name="typeArguments488",
    ends={
        Property(name="ast_Type490", type=ast_ExpressionMethodReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ExpressionMethodReference489", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name491: BinaryAssociation = BinaryAssociation(
    name="name491",
    ends={
        Property(name="ast_SimpleName493", type=ast_ExpressionMethodReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ExpressionMethodReference492", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier494: BinaryAssociation = BinaryAssociation(
    name="qualifier494",
    ends={
        Property(name="ast_Name495", type=ast_SuperMethodReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperMethodReference", type=ast_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments496: BinaryAssociation = BinaryAssociation(
    name="typeArguments496",
    ends={
        Property(name="ast_Type498", type=ast_SuperMethodReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperMethodReference497", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name499: BinaryAssociation = BinaryAssociation(
    name="name499",
    ends={
        Property(name="ast_SimpleName501", type=ast_SuperMethodReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SuperMethodReference500", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type481: BinaryAssociation = BinaryAssociation(
    name="type481",
    ends={
        Property(name="ast_Type482", type=ast_CreationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CreationReference", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments483: BinaryAssociation = BinaryAssociation(
    name="typeArguments483",
    ends={
        Property(name="ast_Type485", type=ast_CreationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_CreationReference484", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type502: BinaryAssociation = BinaryAssociation(
    name="type502",
    ends={
        Property(name="ast_Type503", type=ast_TypeMethodReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeMethodReference", type=ast_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments504: BinaryAssociation = BinaryAssociation(
    name="typeArguments504",
    ends={
        Property(name="ast_Type506", type=ast_TypeMethodReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeMethodReference505", type=ast_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name507: BinaryAssociation = BinaryAssociation(
    name="name507",
    ends={
        Property(name="ast_SimpleName509", type=ast_TypeMethodReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeMethodReference508", type=ast_SimpleName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_ast_Modifier_IExtendedModifier = Generalization(general=IExtendedModifier, specific=ast_Modifier)
gen_ast_MarkerAnnotation_Annotation = Generalization(general=Annotation, specific=ast_MarkerAnnotation)
gen_ast_Annotation_Expression = Generalization(general=Expression, specific=ast_Annotation)
gen_ast_Annotation_IExtendedModifier = Generalization(general=IExtendedModifier, specific=ast_Annotation)
gen_ast_Expression_ASTNode = Generalization(general=ASTNode, specific=ast_Expression)
gen_ast_NormalAnnotation_Annotation = Generalization(general=Annotation, specific=ast_NormalAnnotation)
gen_ast_Modifier_ASTNode = Generalization(general=ASTNode, specific=ast_Modifier)
gen_ast_MemberRef_ASTNode = Generalization(general=ASTNode, specific=ast_MemberRef)
gen_ast_MemberRef_IDocElement = Generalization(general=IDocElement, specific=ast_MemberRef)
gen_ast_MethodRef_ASTNode = Generalization(general=ASTNode, specific=ast_MethodRef)
gen_ast_MethodRef_IDocElement = Generalization(general=IDocElement, specific=ast_MethodRef)
gen_ast_SingleMemberAnnotation_Annotation = Generalization(general=Annotation, specific=ast_SingleMemberAnnotation)
gen_ast_TextElement_ASTNode = Generalization(general=ASTNode, specific=ast_TextElement)
gen_ast_TextElement_IDocElement = Generalization(general=IDocElement, specific=ast_TextElement)
gen_ast_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=ast_AnonymousClassDeclaration)
gen_ast_ArrayAccess_Expression = Generalization(general=Expression, specific=ast_ArrayAccess)
gen_ast_ArrayCreation_Expression = Generalization(general=Expression, specific=ast_ArrayCreation)
gen_ast_Name_Expression = Generalization(general=Expression, specific=ast_Name)
gen_ast_Name_IDocElement = Generalization(general=IDocElement, specific=ast_Name)
gen_ast_TagElement_ASTNode = Generalization(general=ASTNode, specific=ast_TagElement)
gen_ast_TagElement_IDocElement = Generalization(general=IDocElement, specific=ast_TagElement)
gen_ast_ArrayInitializer_Expression = Generalization(general=Expression, specific=ast_ArrayInitializer)
gen_ast_ArrayType_Type = Generalization(general=Type, specific=ast_ArrayType)
gen_ast_Statement_ASTNode = Generalization(general=ASTNode, specific=ast_Statement)
gen_ast_Assignment_Expression = Generalization(general=Expression, specific=ast_Assignment)
gen_ast_Type_ASTNode = Generalization(general=ASTNode, specific=ast_Type)
gen_ast_AssertStatement_Statement = Generalization(general=Statement, specific=ast_AssertStatement)
gen_ast_CastExpression_Expression = Generalization(general=Expression, specific=ast_CastExpression)
gen_ast_CatchClause_ASTNode = Generalization(general=ASTNode, specific=ast_CatchClause)
gen_ast_CharacterLiteral_Expression = Generalization(general=Expression, specific=ast_CharacterLiteral)
gen_ast_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=ast_ClassInstanceCreation)
gen_ast_Block_Statement = Generalization(general=Statement, specific=ast_Block)
gen_ast_BooleanLiteral_Expression = Generalization(general=Expression, specific=ast_BooleanLiteral)
gen_ast_BreakStatement_Statement = Generalization(general=Statement, specific=ast_BreakStatement)
gen_ast_CompilationUnit_ASTNode = Generalization(general=ASTNode, specific=ast_CompilationUnit)
gen_ast_ConditionalExpression_Expression = Generalization(general=Expression, specific=ast_ConditionalExpression)
gen_ast_ContinueStatement_Statement = Generalization(general=Statement, specific=ast_ContinueStatement)
gen_ast_DoStatement_Statement = Generalization(general=Statement, specific=ast_DoStatement)
gen_ast_ConstructorInvocation_Statement = Generalization(general=Statement, specific=ast_ConstructorInvocation)
gen_ast_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=ast_FieldDeclaration)
gen_ast_BodyDeclaration_ASTNode = Generalization(general=ASTNode, specific=ast_BodyDeclaration)
gen_ast_ForStatement_Statement = Generalization(general=Statement, specific=ast_ForStatement)
gen_ast_EmptyStatement_Statement = Generalization(general=Statement, specific=ast_EmptyStatement)
gen_ast_ExpressionStatement_Statement = Generalization(general=Statement, specific=ast_ExpressionStatement)
gen_ast_FieldAccess_Expression = Generalization(general=Expression, specific=ast_FieldAccess)
gen_ast_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=ast_ImportDeclaration)
gen_ast_InfixExpression_Expression = Generalization(general=Expression, specific=ast_InfixExpression)
gen_ast_IfStatement_Statement = Generalization(general=Statement, specific=ast_IfStatement)
gen_ast_Javadoc_Comment = Generalization(general=Comment, specific=ast_Javadoc)
gen_ast_Comment_ASTNode = Generalization(general=ASTNode, specific=ast_Comment)
gen_ast_LabeledStatement_Statement = Generalization(general=Statement, specific=ast_LabeledStatement)
gen_ast_MethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=ast_MethodDeclaration)
gen_ast_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=ast_Initializer)
gen_ast_MethodInvocation_Expression = Generalization(general=Expression, specific=ast_MethodInvocation)
gen_ast_NullLiteral_Expression = Generalization(general=Expression, specific=ast_NullLiteral)
gen_ast_NumberLiteral_Expression = Generalization(general=Expression, specific=ast_NumberLiteral)
gen_ast_PackageDeclaration_ASTNode = Generalization(general=ASTNode, specific=ast_PackageDeclaration)
gen_ast_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=ast_ParenthesizedExpression)
gen_ast_PrimitiveType_AnnotatableType = Generalization(general=AnnotatableType, specific=ast_PrimitiveType)
gen_ast_AnnotatableType_Type = Generalization(general=Type, specific=ast_AnnotatableType)
gen_ast_QualifiedName_Name = Generalization(general=Name, specific=ast_QualifiedName)
gen_ast_PostfixExpression_Expression = Generalization(general=Expression, specific=ast_PostfixExpression)
gen_ast_PrefixExpression_Expression = Generalization(general=Expression, specific=ast_PrefixExpression)
gen_ast_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=ast_SingleVariableDeclaration)
gen_ast_ReturnStatement_Statement = Generalization(general=Statement, specific=ast_ReturnStatement)
gen_ast_SimpleName_Name = Generalization(general=Name, specific=ast_SimpleName)
gen_ast_SimpleType_AnnotatableType = Generalization(general=AnnotatableType, specific=ast_SimpleType)
gen_ast_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=ast_SuperConstructorInvocation)
gen_ast_SuperFieldAccess_Expression = Generalization(general=Expression, specific=ast_SuperFieldAccess)
gen_ast_VariableDeclaration_ASTNode = Generalization(general=ASTNode, specific=ast_VariableDeclaration)
gen_ast_StringLiteral_Expression = Generalization(general=Expression, specific=ast_StringLiteral)
gen_ast_SwitchCase_Statement = Generalization(general=Statement, specific=ast_SwitchCase)
gen_ast_SwitchStatement_Statement = Generalization(general=Statement, specific=ast_SwitchStatement)
gen_ast_SuperMethodInvocation_Expression = Generalization(general=Expression, specific=ast_SuperMethodInvocation)
gen_ast_ThrowStatement_Statement = Generalization(general=Statement, specific=ast_ThrowStatement)
gen_ast_TryStatement_Statement = Generalization(general=Statement, specific=ast_TryStatement)
gen_ast_SynchronizedStatement_Statement = Generalization(general=Statement, specific=ast_SynchronizedStatement)
gen_ast_ThisExpression_Expression = Generalization(general=Expression, specific=ast_ThisExpression)
gen_ast_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=ast_AbstractTypeDeclaration)
gen_ast_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=ast_TypeDeclarationStatement)
gen_ast_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=ast_TypeDeclaration)
gen_ast_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=ast_VariableDeclarationExpression)
gen_ast_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=ast_VariableDeclarationFragment)
gen_ast_TypeLiteral_Expression = Generalization(general=Expression, specific=ast_TypeLiteral)
gen_ast_WhileStatement_Statement = Generalization(general=Statement, specific=ast_WhileStatement)
gen_ast_InstanceofExpression_Expression = Generalization(general=Expression, specific=ast_InstanceofExpression)
gen_ast_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=ast_VariableDeclarationStatement)
gen_ast_EnhancedForStatement_Statement = Generalization(general=Statement, specific=ast_EnhancedForStatement)
gen_ast_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=ast_EnumDeclaration)
gen_ast_LineComment_Comment = Generalization(general=Comment, specific=ast_LineComment)
gen_ast_BlockComment_Comment = Generalization(general=Comment, specific=ast_BlockComment)
gen_ast_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=ast_MethodRefParameter)
gen_ast_TypeParameter_ASTNode = Generalization(general=ASTNode, specific=ast_TypeParameter)
gen_ast_ParameterizedType_Type = Generalization(general=Type, specific=ast_ParameterizedType)
gen_ast_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=ast_EnumConstantDeclaration)
gen_ast_MemberValuePair_ASTNode = Generalization(general=ASTNode, specific=ast_MemberValuePair)
gen_ast_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=ast_AnnotationTypeDeclaration)
gen_ast_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=ast_AnnotationTypeMemberDeclaration)
gen_ast_QualifiedType_AnnotatableType = Generalization(general=AnnotatableType, specific=ast_QualifiedType)
gen_ast_WildcardType_AnnotatableType = Generalization(general=AnnotatableType, specific=ast_WildcardType)
gen_ast_LambdaExpression_Expression = Generalization(general=Expression, specific=ast_LambdaExpression)
gen_ast_IntersectionType_Type = Generalization(general=Type, specific=ast_IntersectionType)
gen_ast_NameQualifiedType_AnnotatableType = Generalization(general=AnnotatableType, specific=ast_NameQualifiedType)
gen_ast_UnionType_Type = Generalization(general=Type, specific=ast_UnionType)
gen_ast_Dimension_ASTNode = Generalization(general=ASTNode, specific=ast_Dimension)
gen_ast_SuperMethodReference_MethodReference = Generalization(general=MethodReference, specific=ast_SuperMethodReference)
gen_ast_CreationReference_MethodReference = Generalization(general=MethodReference, specific=ast_CreationReference)
gen_ast_MethodReference_Expression = Generalization(general=Expression, specific=ast_MethodReference)
gen_ast_ExpressionMethodReference_MethodReference = Generalization(general=MethodReference, specific=ast_ExpressionMethodReference)
gen_ast_TypeMethodReference_MethodReference = Generalization(general=MethodReference, specific=ast_TypeMethodReference)

# Domain Model
domain_model = DomainModel(
    name="ast",
    types={IExtendedModifier, ast_ASTNode, ast_MarkerAnnotation, Annotation, ast_Name, ast_Annotation, Expression, ast_Expression, ast_NormalAnnotation, ast_IExtendedModifier, ast_Modifier, ASTNode, ast_IDocElement, ast_MemberRef, IDocElement, ast_SimpleName, ast_MethodRef, ast_MethodRefParameter, ast_MemberValuePair, ast_SingleMemberAnnotation, ast_TextElement, ast_AnonymousClassDeclaration, ast_BodyDeclaration, ast_ArrayAccess, ast_ArrayCreation, ast_ArrayType, ast_TagElement, Type, ast_Statement, ast_Assignment, ast_ArrayInitializer, ast_Type, ast_Dimension, ast_AssertStatement, Statement, ast_CastExpression, ast_CatchClause, ast_SingleVariableDeclaration, ast_CharacterLiteral, ast_ClassInstanceCreation, ast_Block, ast_BooleanLiteral, ast_BreakStatement, ast_CompilationUnit, ast_PackageDeclaration, ast_ImportDeclaration, ast_AbstractTypeDeclaration, ast_ConditionalExpression, ast_ContinueStatement, ast_DoStatement, ast_ConstructorInvocation, ast_FieldDeclaration, BodyDeclaration, ast_Javadoc, ast_VariableDeclarationFragment, ast_ForStatement, ast_EmptyStatement, ast_ExpressionStatement, ast_FieldAccess, ast_InfixExpression, ast_IfStatement, Comment, ast_Comment, ast_LabeledStatement, ast_MethodDeclaration, ast_Initializer, ast_MethodInvocation, ast_TypeParameter, ast_NullLiteral, ast_NumberLiteral, ast_ParenthesizedExpression, ast_PrimitiveType, AnnotatableType, ast_AnnotatableType, ast_QualifiedName, Name, ast_PostfixExpression, ast_PrefixExpression, VariableDeclaration, ast_ReturnStatement, ast_SimpleType, ast_SuperConstructorInvocation, ast_SuperFieldAccess, ast_VariableDeclaration, ast_StringLiteral, ast_SwitchCase, ast_SwitchStatement, ast_SuperMethodInvocation, ast_ThrowStatement, ast_TryStatement, ast_VariableDeclarationExpression, ast_SynchronizedStatement, ast_ThisExpression, ast_TypeDeclarationStatement, ast_TypeDeclaration, AbstractTypeDeclaration, ast_TypeLiteral, ast_WhileStatement, ast_InstanceofExpression, ast_VariableDeclarationStatement, ast_EnhancedForStatement, ast_EnumDeclaration, ast_LineComment, ast_BlockComment, ast_ParameterizedType, ast_EnumConstantDeclaration, ast_AnnotationTypeDeclaration, ast_AnnotationTypeMemberDeclaration, ast_QualifiedType, ast_WildcardType, ast_LambdaExpression, ast_IntersectionType, ast_NameQualifiedType, ast_UnionType, ast_SuperMethodReference, ast_CreationReference, MethodReference, ast_MethodReference, ast_ExpressionMethodReference, ast_TypeMethodReference},
    associations={typeName0, typeName1, qualifier9, name11, qualifier13, name15, values3, typeName5, value7, fragments20, bodyDeclarations21, array22, index24, type27, parameters18, initializer31, expressions33, dimensions28, leftHandSide45, rightHandSide47, elementType36, dimensions38, expression40, message42, label51, type53, expression55, exception58, body59, statements50, package76, imports77, types79, expression62, typeArguments64, type67, arguments70, typeArguments89, anonymousClassDeclaration73, arguments91, label94, body96, expression98, expression81, thenExpression83, elseExpression86, javadoc108, modifiers109, type111, fragments114, initializers116, expression118, expression101, expression103, name105, elseStatement132, name135, leftOperand138, rightOperand140, extendedOperands143, updaters121, body124, expression127, thenStatement129, tags154, label157, body159, javadoc162, modifiers164, javadoc146, modifiers148, body151, receiverType175, receiverQualifier178, parameters181, extraDimensions2184, thrownExceptionTypes187, body190, typeParameters167, returnType2169, name172, arguments201, javadoc204, annotations207, name209, expression193, typeArguments195, name198, operand216, annotations218, qualifier220, name222, expression212, operand214, annotations227, name229, modifiers232, type235, varargsAnnotations238, name241, expression225, expression250, typeArguments252, arguments255, extraDimensions2244, initializer247, name268, arguments271, expression274, expression276, qualifier258, statements278, name260, qualifier263, typeArguments265, qualifier286, expression288, resources290, body291, catchClauses294, expression281, body283, name305, typeParameters308, superclassType311, superInterfaceTypes314, bodyDeclarations317, declaration320, finally297, javadoc300, modifiers302, modifiers324, type327, fragments330, name333, fragments347, type322, expression350, body352, leftOperand355, extraDimensions2336, initializer339, modifiers342, type344, parameter366, expression368, body371, javadoc374, rightOperand357, type360, name363, modifiers393, name396, arguments399, anonymousClassDeclaration402, modifiers405, name408, typeBounds411, modifiers376, type414, typeArguments416, name379, superInterfaceTypes382, enumConstants385, bodyDeclarations387, javadoc390, name432, value435, javadoc438, modifiers440, name443, bodyDeclarations446, javadoc449, modifiers451, type454, name457, qualifier419, annotations421, name424, annotations427, bound429, parameters468, body469, types471, qualifier473, annotations475, name478, default460, types463, annotations465, expression486, typeArguments488, name491, qualifier494, typeArguments496, name499, type481, typeArguments483, type502, typeArguments504, name507},
    generalizations={gen_ast_Modifier_IExtendedModifier, gen_ast_MarkerAnnotation_Annotation, gen_ast_Annotation_Expression, gen_ast_Annotation_IExtendedModifier, gen_ast_Expression_ASTNode, gen_ast_NormalAnnotation_Annotation, gen_ast_Modifier_ASTNode, gen_ast_MemberRef_ASTNode, gen_ast_MemberRef_IDocElement, gen_ast_MethodRef_ASTNode, gen_ast_MethodRef_IDocElement, gen_ast_SingleMemberAnnotation_Annotation, gen_ast_TextElement_ASTNode, gen_ast_TextElement_IDocElement, gen_ast_AnonymousClassDeclaration_ASTNode, gen_ast_ArrayAccess_Expression, gen_ast_ArrayCreation_Expression, gen_ast_Name_Expression, gen_ast_Name_IDocElement, gen_ast_TagElement_ASTNode, gen_ast_TagElement_IDocElement, gen_ast_ArrayInitializer_Expression, gen_ast_ArrayType_Type, gen_ast_Statement_ASTNode, gen_ast_Assignment_Expression, gen_ast_Type_ASTNode, gen_ast_AssertStatement_Statement, gen_ast_CastExpression_Expression, gen_ast_CatchClause_ASTNode, gen_ast_CharacterLiteral_Expression, gen_ast_ClassInstanceCreation_Expression, gen_ast_Block_Statement, gen_ast_BooleanLiteral_Expression, gen_ast_BreakStatement_Statement, gen_ast_CompilationUnit_ASTNode, gen_ast_ConditionalExpression_Expression, gen_ast_ContinueStatement_Statement, gen_ast_DoStatement_Statement, gen_ast_ConstructorInvocation_Statement, gen_ast_FieldDeclaration_BodyDeclaration, gen_ast_BodyDeclaration_ASTNode, gen_ast_ForStatement_Statement, gen_ast_EmptyStatement_Statement, gen_ast_ExpressionStatement_Statement, gen_ast_FieldAccess_Expression, gen_ast_ImportDeclaration_ASTNode, gen_ast_InfixExpression_Expression, gen_ast_IfStatement_Statement, gen_ast_Javadoc_Comment, gen_ast_Comment_ASTNode, gen_ast_LabeledStatement_Statement, gen_ast_MethodDeclaration_BodyDeclaration, gen_ast_Initializer_BodyDeclaration, gen_ast_MethodInvocation_Expression, gen_ast_NullLiteral_Expression, gen_ast_NumberLiteral_Expression, gen_ast_PackageDeclaration_ASTNode, gen_ast_ParenthesizedExpression_Expression, gen_ast_PrimitiveType_AnnotatableType, gen_ast_AnnotatableType_Type, gen_ast_QualifiedName_Name, gen_ast_PostfixExpression_Expression, gen_ast_PrefixExpression_Expression, gen_ast_SingleVariableDeclaration_VariableDeclaration, gen_ast_ReturnStatement_Statement, gen_ast_SimpleName_Name, gen_ast_SimpleType_AnnotatableType, gen_ast_SuperConstructorInvocation_Statement, gen_ast_SuperFieldAccess_Expression, gen_ast_VariableDeclaration_ASTNode, gen_ast_StringLiteral_Expression, gen_ast_SwitchCase_Statement, gen_ast_SwitchStatement_Statement, gen_ast_SuperMethodInvocation_Expression, gen_ast_ThrowStatement_Statement, gen_ast_TryStatement_Statement, gen_ast_SynchronizedStatement_Statement, gen_ast_ThisExpression_Expression, gen_ast_AbstractTypeDeclaration_BodyDeclaration, gen_ast_TypeDeclarationStatement_Statement, gen_ast_TypeDeclaration_AbstractTypeDeclaration, gen_ast_VariableDeclarationExpression_Expression, gen_ast_VariableDeclarationFragment_VariableDeclaration, gen_ast_TypeLiteral_Expression, gen_ast_WhileStatement_Statement, gen_ast_InstanceofExpression_Expression, gen_ast_VariableDeclarationStatement_Statement, gen_ast_EnhancedForStatement_Statement, gen_ast_EnumDeclaration_AbstractTypeDeclaration, gen_ast_LineComment_Comment, gen_ast_BlockComment_Comment, gen_ast_MethodRefParameter_ASTNode, gen_ast_TypeParameter_ASTNode, gen_ast_ParameterizedType_Type, gen_ast_EnumConstantDeclaration_BodyDeclaration, gen_ast_MemberValuePair_ASTNode, gen_ast_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_ast_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_ast_QualifiedType_AnnotatableType, gen_ast_WildcardType_AnnotatableType, gen_ast_LambdaExpression_Expression, gen_ast_IntersectionType_Type, gen_ast_NameQualifiedType_AnnotatableType, gen_ast_UnionType_Type, gen_ast_Dimension_ASTNode, gen_ast_SuperMethodReference_MethodReference, gen_ast_CreationReference_MethodReference, gen_ast_MethodReference_Expression, gen_ast_ExpressionMethodReference_MethodReference, gen_ast_TypeMethodReference_MethodReference},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)