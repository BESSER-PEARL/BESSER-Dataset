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
InheritanceKind: Enumeration = Enumeration(
    name="InheritanceKind",
    literals={
            EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="final")
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
Java5_BodyDeclaration = Class(name="Java5::BodyDeclaration", is_abstract=True)
Java5_ImportDeclaration = Class(name="Java5::ImportDeclaration")
Java5_PackageDeclaration = Class(name="Java5::PackageDeclaration")
Java5_AbstractTypeDeclaration = Class(name="Java5::AbstractTypeDeclaration", is_abstract=True)
BodyDeclaration = Class(name="BodyDeclaration")
NamedElement = Class(name="NamedElement")
Java5_Expression = Class(name="Java5::Expression", is_abstract=True)
Java5_AnnotationTypeDeclaration = Class(name="Java5::AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
Java5_AnnotationTypeMemberDeclaration = Class(name="Java5::AnnotationTypeMemberDeclaration")
Java5_NamedElementRef = Class(name="Java5::NamedElementRef")
Java5_Annotation = Class(name="Java5::Annotation")
Expression = Class(name="Expression")
Java5_AnnotationMemberValuePair = Class(name="Java5::AnnotationMemberValuePair")
Java5_ArrayCreation = Class(name="Java5::ArrayCreation")
Java5_ArrayInitializer = Class(name="Java5::ArrayInitializer")
Java5_AnonymousClassDeclaration = Class(name="Java5::AnonymousClassDeclaration")
ASTNode = Class(name="ASTNode")
Java5_ClassInstanceCreation = Class(name="Java5::ClassInstanceCreation")
Java5_ArrayAccess = Class(name="Java5::ArrayAccess")
Java5_AssertStatement = Class(name="Java5::AssertStatement")
Statement = Class(name="Statement")
Java5_Assignment = Class(name="Java5::Assignment")
Java5_ASTNode = Class(name="Java5::ASTNode", is_abstract=True)
Java5_Block = Class(name="Java5::Block")
Java5_Statement = Class(name="Java5::Statement", is_abstract=True)
Java5_ArrayLengthAccess = Class(name="Java5::ArrayLengthAccess")
Java5_ArrayType = Class(name="Java5::ArrayType")
OrphanType = Class(name="OrphanType")
Java5_CastExpression = Class(name="Java5::CastExpression")
Java5_CatchClause = Class(name="Java5::CatchClause")
Java5_SingleVariableDeclaration = Class(name="Java5::SingleVariableDeclaration")
Java5_CharacterLiteral = Class(name="Java5::CharacterLiteral")
Java5_ClassDeclaration = Class(name="Java5::ClassDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
Java5_Modifier = Class(name="Java5::Modifier")
Java5_BooleanLiteral = Class(name="Java5::BooleanLiteral")
Java5_BreakStatement = Class(name="Java5::BreakStatement")
Java5_CompilationUnit = Class(name="Java5::CompilationUnit")
Java5_ConstructorInvocation = Class(name="Java5::ConstructorInvocation")
Java5_ContinueStatement = Class(name="Java5::ContinueStatement")
Java5_ConditionalExpression = Class(name="Java5::ConditionalExpression")
Java5_EmptyStatement = Class(name="Java5::EmptyStatement")
Java5_EnumDeclaration = Class(name="Java5::EnumDeclaration")
Java5_EnumConstantDeclaration = Class(name="Java5::EnumConstantDeclaration")
Java5_EnhancedForStatement = Class(name="Java5::EnhancedForStatement")
Java5_DoStatement = Class(name="Java5::DoStatement")
Java5_ExpressionStatement = Class(name="Java5::ExpressionStatement")
Java5_FieldAccess = Class(name="Java5::FieldAccess")
Java5_ForStatement = Class(name="Java5::ForStatement")
Java5_FieldDeclaration = Class(name="Java5::FieldDeclaration")
Java5_VariableDeclarationFragment = Class(name="Java5::VariableDeclarationFragment")
Java5_InfixExpression = Class(name="Java5::InfixExpression")
Java5_IfStatement = Class(name="Java5::IfStatement")
Java5_Initializer = Class(name="Java5::Initializer")
Java5_InstanceofExpression = Class(name="Java5::InstanceofExpression")
Java5_InterfaceDeclaration = Class(name="Java5::InterfaceDeclaration")
Java5_LabeledStatement = Class(name="Java5::LabeledStatement")
Java5_MethodDeclaration = Class(name="Java5::MethodDeclaration")
Java5_MemberRef = Class(name="Java5::MemberRef")
Java5_MethodInvocation = Class(name="Java5::MethodInvocation")
Java5_TypeParameter = Class(name="Java5::TypeParameter")
Java5_MethodRefParameter = Class(name="Java5::MethodRefParameter")
Java5_Model = Class(name="Java5::Model")
Java5_MethodRef = Class(name="Java5::MethodRef")
Java5_OrphanType = Class(name="Java5::OrphanType")
Java5_UnresolvedItem = Class(name="Java5::UnresolvedItem")
Java5_NullLiteral = Class(name="Java5::NullLiteral")
Java5_NumberLiteral = Class(name="Java5::NumberLiteral")
Java5_VariableDeclarationStatement = Class(name="Java5::VariableDeclarationStatement")
Java5_VariableDeclarationExpression = Class(name="Java5::VariableDeclarationExpression")
Java5_NamedElement = Class(name="Java5::NamedElement", is_abstract=True)
Java5_ParameterizedType = Class(name="Java5::ParameterizedType")
Java5_PostfixExpression = Class(name="Java5::PostfixExpression")
Java5_ParenthesizedExpression = Class(name="Java5::ParenthesizedExpression")
Java5_PrimitiveType = Class(name="Java5::PrimitiveType")
Java5_PrimitiveTypeBoolean = Class(name="Java5::PrimitiveTypeBoolean")
PrimitiveType = Class(name="PrimitiveType")
Java5_PrimitiveTypeByte = Class(name="Java5::PrimitiveTypeByte")
Java5_PrefixExpression = Class(name="Java5::PrefixExpression")
Java5_PrimitiveTypeFloat = Class(name="Java5::PrimitiveTypeFloat")
Java5_PrimitiveTypeInt = Class(name="Java5::PrimitiveTypeInt")
Java5_PrimitiveTypeLong = Class(name="Java5::PrimitiveTypeLong")
Java5_PrimitiveTypeVoid = Class(name="Java5::PrimitiveTypeVoid")
Java5_ReturnStatement = Class(name="Java5::ReturnStatement")
Java5_PrimitiveTypeChar = Class(name="Java5::PrimitiveTypeChar")
Java5_PrimitiveTypeDouble = Class(name="Java5::PrimitiveTypeDouble")
Java5_PrimitiveTypeShort = Class(name="Java5::PrimitiveTypeShort")
Java5_SuperFieldAccess = Class(name="Java5::SuperFieldAccess")
VariableDeclaration = Class(name="VariableDeclaration")
Java5_StringLiteral = Class(name="Java5::StringLiteral")
Java5_SuperConstructorInvocation = Class(name="Java5::SuperConstructorInvocation")
Java5_SwitchStatement = Class(name="Java5::SwitchStatement")
Java5_SuperMethodInvocation = Class(name="Java5::SuperMethodInvocation")
Java5_SwitchCase = Class(name="Java5::SwitchCase")
Java5_SynchronizedStatement = Class(name="Java5::SynchronizedStatement")
Java5_ThrowStatement = Class(name="Java5::ThrowStatement")
Java5_TagElement = Class(name="Java5::TagElement")
Java5_TextElement = Class(name="Java5::TextElement")
Java5_ThisExpression = Class(name="Java5::ThisExpression")
Java5_TryStatement = Class(name="Java5::TryStatement")
Java5_TypeDeclaration = Class(name="Java5::TypeDeclaration", is_abstract=True)
Java5_TypeDeclarationStatement = Class(name="Java5::TypeDeclarationStatement")
Java5_TypeLiteral = Class(name="Java5::TypeLiteral")
Java5_VariableDeclaration = Class(name="Java5::VariableDeclaration", is_abstract=True)
Java5_WhileStatement = Class(name="Java5::WhileStatement")
Java5_WildCardType = Class(name="Java5::WildCardType")

# Java5_BodyDeclaration class attributes and methods

# Java5_ImportDeclaration class attributes and methods
Java5_ImportDeclaration_static: Property = Property(name="static", type=BooleanType)
Java5_ImportDeclaration.attributes={Java5_ImportDeclaration_static}

# Java5_PackageDeclaration class attributes and methods
Java5_PackageDeclaration_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
Java5_PackageDeclaration.attributes={Java5_PackageDeclaration_qualifiedName}

# Java5_AbstractTypeDeclaration class attributes and methods
Java5_AbstractTypeDeclaration_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
Java5_AbstractTypeDeclaration.attributes={Java5_AbstractTypeDeclaration_qualifiedName}

# BodyDeclaration class attributes and methods

# NamedElement class attributes and methods

# Java5_Expression class attributes and methods

# Java5_AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# Java5_AnnotationTypeMemberDeclaration class attributes and methods

# Java5_NamedElementRef class attributes and methods

# Java5_Annotation class attributes and methods

# Expression class attributes and methods

# Java5_AnnotationMemberValuePair class attributes and methods

# Java5_ArrayCreation class attributes and methods

# Java5_ArrayInitializer class attributes and methods

# Java5_AnonymousClassDeclaration class attributes and methods

# ASTNode class attributes and methods

# Java5_ClassInstanceCreation class attributes and methods

# Java5_ArrayAccess class attributes and methods

# Java5_AssertStatement class attributes and methods

# Statement class attributes and methods

# Java5_Assignment class attributes and methods
Java5_Assignment_operator: Property = Property(name="operator", type=StringType)
Java5_Assignment.attributes={Java5_Assignment_operator}

# Java5_ASTNode class attributes and methods

# Java5_Block class attributes and methods

# Java5_Statement class attributes and methods

# Java5_ArrayLengthAccess class attributes and methods

# Java5_ArrayType class attributes and methods
Java5_ArrayType_originalName: Property = Property(name="originalName", type=StringType)
Java5_ArrayType_dimensions: Property = Property(name="dimensions", type=IntegerType)
Java5_ArrayType.attributes={Java5_ArrayType_originalName, Java5_ArrayType_dimensions}

# OrphanType class attributes and methods

# Java5_CastExpression class attributes and methods

# Java5_CatchClause class attributes and methods

# Java5_SingleVariableDeclaration class attributes and methods
Java5_SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=BooleanType)
Java5_SingleVariableDeclaration.attributes={Java5_SingleVariableDeclaration_varargs}

# Java5_CharacterLiteral class attributes and methods
Java5_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
Java5_CharacterLiteral_value: Property = Property(name="value", type=StringType)
Java5_CharacterLiteral.attributes={Java5_CharacterLiteral_value, Java5_CharacterLiteral_escapedValue}

# Java5_ClassDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# Java5_Modifier class attributes and methods
Java5_Modifier_visibility: Property = Property(name="visibility", type=StringType)
Java5_Modifier_inheritance: Property = Property(name="inheritance", type=StringType)
Java5_Modifier_static: Property = Property(name="static", type=BooleanType)
Java5_Modifier_transient: Property = Property(name="transient", type=BooleanType)
Java5_Modifier_volatile: Property = Property(name="volatile", type=BooleanType)
Java5_Modifier_native: Property = Property(name="native", type=BooleanType)
Java5_Modifier_strictfp: Property = Property(name="strictfp", type=BooleanType)
Java5_Modifier_synchronized: Property = Property(name="synchronized", type=BooleanType)
Java5_Modifier.attributes={Java5_Modifier_strictfp, Java5_Modifier_static, Java5_Modifier_native, Java5_Modifier_inheritance, Java5_Modifier_synchronized, Java5_Modifier_volatile, Java5_Modifier_transient, Java5_Modifier_visibility}

# Java5_BooleanLiteral class attributes and methods
Java5_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
Java5_BooleanLiteral.attributes={Java5_BooleanLiteral_value}

# Java5_BreakStatement class attributes and methods

# Java5_CompilationUnit class attributes and methods
Java5_CompilationUnit_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
Java5_CompilationUnit.attributes={Java5_CompilationUnit_originalFilePath}

# Java5_ConstructorInvocation class attributes and methods

# Java5_ContinueStatement class attributes and methods

# Java5_ConditionalExpression class attributes and methods

# Java5_EmptyStatement class attributes and methods

# Java5_EnumDeclaration class attributes and methods

# Java5_EnumConstantDeclaration class attributes and methods

# Java5_EnhancedForStatement class attributes and methods

# Java5_DoStatement class attributes and methods

# Java5_ExpressionStatement class attributes and methods

# Java5_FieldAccess class attributes and methods

# Java5_ForStatement class attributes and methods

# Java5_FieldDeclaration class attributes and methods

# Java5_VariableDeclarationFragment class attributes and methods

# Java5_InfixExpression class attributes and methods
Java5_InfixExpression_operator: Property = Property(name="operator", type=StringType)
Java5_InfixExpression.attributes={Java5_InfixExpression_operator}

# Java5_IfStatement class attributes and methods

# Java5_Initializer class attributes and methods

# Java5_InstanceofExpression class attributes and methods

# Java5_InterfaceDeclaration class attributes and methods

# Java5_LabeledStatement class attributes and methods

# Java5_MethodDeclaration class attributes and methods
Java5_MethodDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
Java5_MethodDeclaration_constructor: Property = Property(name="constructor", type=BooleanType)
Java5_MethodDeclaration_varargs: Property = Property(name="varargs", type=BooleanType)
Java5_MethodDeclaration.attributes={Java5_MethodDeclaration_constructor, Java5_MethodDeclaration_extraArrayDimensions, Java5_MethodDeclaration_varargs}

# Java5_MemberRef class attributes and methods

# Java5_MethodInvocation class attributes and methods

# Java5_TypeParameter class attributes and methods

# Java5_MethodRefParameter class attributes and methods
Java5_MethodRefParameter_name: Property = Property(name="name", type=StringType)
Java5_MethodRefParameter_isVarargs: Property = Property(name="isVarargs", type=StringType)
Java5_MethodRefParameter.attributes={Java5_MethodRefParameter_isVarargs, Java5_MethodRefParameter_name}

# Java5_Model class attributes and methods
Java5_Model_name: Property = Property(name="name", type=StringType)
Java5_Model.attributes={Java5_Model_name}

# Java5_MethodRef class attributes and methods

# Java5_OrphanType class attributes and methods

# Java5_UnresolvedItem class attributes and methods

# Java5_NullLiteral class attributes and methods

# Java5_NumberLiteral class attributes and methods
Java5_NumberLiteral_tokenValue: Property = Property(name="tokenValue", type=StringType)
Java5_NumberLiteral.attributes={Java5_NumberLiteral_tokenValue}

# Java5_VariableDeclarationStatement class attributes and methods
Java5_VariableDeclarationStatement_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
Java5_VariableDeclarationStatement.attributes={Java5_VariableDeclarationStatement_extraArrayDimensions}

# Java5_VariableDeclarationExpression class attributes and methods

# Java5_NamedElement class attributes and methods
Java5_NamedElement_proxy: Property = Property(name="proxy", type=BooleanType)
Java5_NamedElement_name: Property = Property(name="name", type=StringType)
Java5_NamedElement.attributes={Java5_NamedElement_name, Java5_NamedElement_proxy}

# Java5_ParameterizedType class attributes and methods

# Java5_PostfixExpression class attributes and methods
Java5_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
Java5_PostfixExpression.attributes={Java5_PostfixExpression_operator}

# Java5_ParenthesizedExpression class attributes and methods

# Java5_PrimitiveType class attributes and methods

# Java5_PrimitiveTypeBoolean class attributes and methods

# PrimitiveType class attributes and methods

# Java5_PrimitiveTypeByte class attributes and methods

# Java5_PrefixExpression class attributes and methods
Java5_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
Java5_PrefixExpression.attributes={Java5_PrefixExpression_operator}

# Java5_PrimitiveTypeFloat class attributes and methods

# Java5_PrimitiveTypeInt class attributes and methods

# Java5_PrimitiveTypeLong class attributes and methods

# Java5_PrimitiveTypeVoid class attributes and methods

# Java5_ReturnStatement class attributes and methods

# Java5_PrimitiveTypeChar class attributes and methods

# Java5_PrimitiveTypeDouble class attributes and methods

# Java5_PrimitiveTypeShort class attributes and methods

# Java5_SuperFieldAccess class attributes and methods

# VariableDeclaration class attributes and methods

# Java5_StringLiteral class attributes and methods
Java5_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
Java5_StringLiteral_value: Property = Property(name="value", type=StringType)
Java5_StringLiteral.attributes={Java5_StringLiteral_value, Java5_StringLiteral_escapedValue}

# Java5_SuperConstructorInvocation class attributes and methods

# Java5_SwitchStatement class attributes and methods

# Java5_SuperMethodInvocation class attributes and methods

# Java5_SwitchCase class attributes and methods
Java5_SwitchCase_default: Property = Property(name="default", type=BooleanType)
Java5_SwitchCase.attributes={Java5_SwitchCase_default}

# Java5_SynchronizedStatement class attributes and methods

# Java5_ThrowStatement class attributes and methods

# Java5_TagElement class attributes and methods
Java5_TagElement_tagName: Property = Property(name="tagName", type=StringType)
Java5_TagElement.attributes={Java5_TagElement_tagName}

# Java5_TextElement class attributes and methods
Java5_TextElement_text: Property = Property(name="text", type=StringType)
Java5_TextElement.attributes={Java5_TextElement_text}

# Java5_ThisExpression class attributes and methods

# Java5_TryStatement class attributes and methods

# Java5_TypeDeclaration class attributes and methods

# Java5_TypeDeclarationStatement class attributes and methods

# Java5_TypeLiteral class attributes and methods

# Java5_VariableDeclaration class attributes and methods
Java5_VariableDeclaration_extraArrayDimensions: Property = Property(name="extraArrayDimensions", type=IntegerType)
Java5_VariableDeclaration.attributes={Java5_VariableDeclaration_extraArrayDimensions}

# Java5_WhileStatement class attributes and methods

# Java5_WildCardType class attributes and methods
Java5_WildCardType_isUpperBound: Property = Property(name="isUpperBound", type=StringType)
Java5_WildCardType.attributes={Java5_WildCardType_isUpperBound}

# Relationships
bodyDeclarations0: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations0",
    ends={
        Property(name="BodyDeclaration", type=Java5_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractTypeDeclaration", type=Java5_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="Java5_ImportDeclaration", type=Java5_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_AbstractTypeDeclaration", type=Java5_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package2: BinaryAssociation = BinaryAssociation(
    name="package2",
    ends={
        Property(name="PackageDeclaration", type=Java5_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements", type=Java5_PackageDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
member9: BinaryAssociation = BinaryAssociation(
    name="member9",
    ends={
        Property(name="Java5_NamedElementRef11", type=Java5_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_AnnotationMemberValuePair10", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value12: BinaryAssociation = BinaryAssociation(
    name="value12",
    ends={
        Property(name="Java5_Expression", type=Java5_AnnotationMemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_AnnotationMemberValuePair13", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
default14: BinaryAssociation = BinaryAssociation(
    name="default14",
    ends={
        Property(name="Java5_Expression15", type=Java5_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_AnnotationTypeMemberDeclaration", type=Java5_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="Java5_NamedElementRef18", type=Java5_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_AnnotationTypeMemberDeclaration17", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superInterfaces3: BinaryAssociation = BinaryAssociation(
    name="superInterfaces3",
    ends={
        Property(name="Java5_NamedElementRef", type=Java5_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_AbstractTypeDeclaration4", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="Java5_NamedElementRef6", type=Java5_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_Annotation", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values7: BinaryAssociation = BinaryAssociation(
    name="values7",
    ends={
        Property(name="Java5_AnnotationMemberValuePair", type=Java5_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_Annotation8", type=Java5_AnnotationMemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
index24: BinaryAssociation = BinaryAssociation(
    name="index24",
    ends={
        Property(name="Java5_Expression26", type=Java5_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ArrayAccess25", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions27: BinaryAssociation = BinaryAssociation(
    name="dimensions27",
    ends={
        Property(name="Java5_Expression28", type=Java5_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ArrayCreation", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer29: BinaryAssociation = BinaryAssociation(
    name="initializer29",
    ends={
        Property(name="Java5_ArrayInitializer", type=Java5_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ArrayCreation30", type=Java5_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type31: BinaryAssociation = BinaryAssociation(
    name="type31",
    ends={
        Property(name="Java5_NamedElementRef33", type=Java5_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ArrayCreation32", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyDeclarations19: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations19",
    ends={
        Property(name="BodyDeclaration20", type=Java5_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclarationOwner", type=Java5_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classInstanceCreation21: BinaryAssociation = BinaryAssociation(
    name="classInstanceCreation21",
    ends={
        Property(name="ClassInstanceCreation", type=Java5_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="anonymousClassDeclaration", type=Java5_ClassInstanceCreation, multiplicity=Multiplicity(0, 1))
    }
)
array22: BinaryAssociation = BinaryAssociation(
    name="array22",
    ends={
        Property(name="Java5_Expression23", type=Java5_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ArrayAccess", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType39: BinaryAssociation = BinaryAssociation(
    name="elementType39",
    ends={
        Property(name="Java5_NamedElementRef40", type=Java5_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ArrayType", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message41: BinaryAssociation = BinaryAssociation(
    name="message41",
    ends={
        Property(name="Java5_Expression42", type=Java5_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_AssertStatement", type=Java5_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression43: BinaryAssociation = BinaryAssociation(
    name="expression43",
    ends={
        Property(name="Java5_Expression45", type=Java5_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_AssertStatement44", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide46: BinaryAssociation = BinaryAssociation(
    name="leftHandSide46",
    ends={
        Property(name="Java5_Expression47", type=Java5_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_Assignment", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide48: BinaryAssociation = BinaryAssociation(
    name="rightHandSide48",
    ends={
        Property(name="Java5_Expression50", type=Java5_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_Assignment49", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements51: BinaryAssociation = BinaryAssociation(
    name="statements51",
    ends={
        Property(name="Java5_Statement", type=Java5_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_Block", type=Java5_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions34: BinaryAssociation = BinaryAssociation(
    name="expressions34",
    ends={
        Property(name="Java5_Expression36", type=Java5_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ArrayInitializer35", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
array37: BinaryAssociation = BinaryAssociation(
    name="array37",
    ends={
        Property(name="Java5_Expression38", type=Java5_ArrayLengthAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ArrayLengthAccess", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression61: BinaryAssociation = BinaryAssociation(
    name="expression61",
    ends={
        Property(name="Java5_Expression62", type=Java5_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_CastExpression", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type63: BinaryAssociation = BinaryAssociation(
    name="type63",
    ends={
        Property(name="Java5_NamedElementRef65", type=Java5_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_CastExpression64", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception66: BinaryAssociation = BinaryAssociation(
    name="exception66",
    ends={
        Property(name="SingleVariableDeclaration", type=Java5_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="catchClause", type=Java5_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body67: BinaryAssociation = BinaryAssociation(
    name="body67",
    ends={
        Property(name="Java5_Block68", type=Java5_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_CatchClause", type=Java5_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superClass69: BinaryAssociation = BinaryAssociation(
    name="superClass69",
    ends={
        Property(name="Java5_NamedElementRef70", type=Java5_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ClassDeclaration", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstractTypeDeclaration52: BinaryAssociation = BinaryAssociation(
    name="abstractTypeDeclaration52",
    ends={
        Property(name="AbstractTypeDeclaration", type=Java5_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations", type=Java5_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
annotations53: BinaryAssociation = BinaryAssociation(
    name="annotations53",
    ends={
        Property(name="Java5_Annotation54", type=Java5_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_BodyDeclaration", type=Java5_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclarationOwner55: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclarationOwner55",
    ends={
        Property(name="AnonymousClassDeclaration", type=Java5_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclarations56", type=Java5_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
modifiers57: BinaryAssociation = BinaryAssociation(
    name="modifiers57",
    ends={
        Property(name="Modifier", type=Java5_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="BodyDeclaration58", type=Java5_Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label59: BinaryAssociation = BinaryAssociation(
    name="label59",
    ends={
        Property(name="Java5_NamedElementRef60", type=Java5_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_BreakStatement", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method78: BinaryAssociation = BinaryAssociation(
    name="method78",
    ends={
        Property(name="Java5_NamedElementRef80", type=Java5_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ClassInstanceCreation79", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type81: BinaryAssociation = BinaryAssociation(
    name="type81",
    ends={
        Property(name="Java5_NamedElementRef83", type=Java5_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ClassInstanceCreation82", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imports84: BinaryAssociation = BinaryAssociation(
    name="imports84",
    ends={
        Property(name="Java5_ImportDeclaration85", type=Java5_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_CompilationUnit", type=Java5_ImportDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
anonymousClassDeclaration71: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration71",
    ends={
        Property(name="AnonymousClassDeclaration72", type=Java5_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="classInstanceCreation", type=Java5_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments73: BinaryAssociation = BinaryAssociation(
    name="arguments73",
    ends={
        Property(name="Java5_Expression74", type=Java5_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ClassInstanceCreation", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression75: BinaryAssociation = BinaryAssociation(
    name="expression75",
    ends={
        Property(name="Java5_Expression77", type=Java5_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ClassInstanceCreation76", type=Java5_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression93: BinaryAssociation = BinaryAssociation(
    name="expression93",
    ends={
        Property(name="Java5_Expression95", type=Java5_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ConditionalExpression94", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression96: BinaryAssociation = BinaryAssociation(
    name="thenExpression96",
    ends={
        Property(name="Java5_Expression98", type=Java5_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ConditionalExpression97", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments99: BinaryAssociation = BinaryAssociation(
    name="arguments99",
    ends={
        Property(name="Java5_Expression100", type=Java5_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ConstructorInvocation", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method101: BinaryAssociation = BinaryAssociation(
    name="method101",
    ends={
        Property(name="Java5_NamedElementRef103", type=Java5_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ConstructorInvocation102", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
package86: BinaryAssociation = BinaryAssociation(
    name="package86",
    ends={
        Property(name="Java5_PackageDeclaration", type=Java5_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_CompilationUnit87", type=Java5_PackageDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
types88: BinaryAssociation = BinaryAssociation(
    name="types88",
    ends={
        Property(name="Java5_AbstractTypeDeclaration90", type=Java5_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_CompilationUnit89", type=Java5_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
elseExpression91: BinaryAssociation = BinaryAssociation(
    name="elseExpression91",
    ends={
        Property(name="Java5_Expression92", type=Java5_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ConditionalExpression", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumConstants111: BinaryAssociation = BinaryAssociation(
    name="enumConstants111",
    ends={
        Property(name="Java5_EnumConstantDeclaration", type=Java5_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_EnumDeclaration", type=Java5_EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration112: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration112",
    ends={
        Property(name="Java5_AnonymousClassDeclaration", type=Java5_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_EnumConstantDeclaration113", type=Java5_AnonymousClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments114: BinaryAssociation = BinaryAssociation(
    name="arguments114",
    ends={
        Property(name="Java5_Expression116", type=Java5_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_EnumConstantDeclaration115", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label104: BinaryAssociation = BinaryAssociation(
    name="label104",
    ends={
        Property(name="Java5_NamedElementRef105", type=Java5_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ContinueStatement", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression106: BinaryAssociation = BinaryAssociation(
    name="expression106",
    ends={
        Property(name="Java5_Expression107", type=Java5_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_DoStatement", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body108: BinaryAssociation = BinaryAssociation(
    name="body108",
    ends={
        Property(name="Java5_Statement110", type=Java5_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_DoStatement109", type=Java5_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression124: BinaryAssociation = BinaryAssociation(
    name="expression124",
    ends={
        Property(name="Java5_Expression125", type=Java5_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ExpressionStatement", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
field126: BinaryAssociation = BinaryAssociation(
    name="field126",
    ends={
        Property(name="Java5_NamedElementRef127", type=Java5_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_FieldAccess", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression128: BinaryAssociation = BinaryAssociation(
    name="expression128",
    ends={
        Property(name="Java5_Expression130", type=Java5_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_FieldAccess129", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body117: BinaryAssociation = BinaryAssociation(
    name="body117",
    ends={
        Property(name="Java5_Statement118", type=Java5_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_EnhancedForStatement", type=Java5_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression119: BinaryAssociation = BinaryAssociation(
    name="expression119",
    ends={
        Property(name="Java5_Expression121", type=Java5_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_EnhancedForStatement120", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter122: BinaryAssociation = BinaryAssociation(
    name="parameter122",
    ends={
        Property(name="SingleVariableDeclaration123", type=Java5_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="enhancedForStatement", type=Java5_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments133: BinaryAssociation = BinaryAssociation(
    name="fragments133",
    ends={
        Property(name="VariableDeclarationFragment", type=Java5_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fieldDeclaration", type=Java5_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression134: BinaryAssociation = BinaryAssociation(
    name="expression134",
    ends={
        Property(name="Java5_Expression135", type=Java5_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ForStatement", type=Java5_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updaters136: BinaryAssociation = BinaryAssociation(
    name="updaters136",
    ends={
        Property(name="Java5_Expression138", type=Java5_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ForStatement137", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializers139: BinaryAssociation = BinaryAssociation(
    name="initializers139",
    ends={
        Property(name="Java5_Expression141", type=Java5_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ForStatement140", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type131: BinaryAssociation = BinaryAssociation(
    name="type131",
    ends={
        Property(name="Java5_NamedElementRef132", type=Java5_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_FieldDeclaration", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement147: BinaryAssociation = BinaryAssociation(
    name="thenStatement147",
    ends={
        Property(name="Java5_Statement149", type=Java5_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_IfStatement148", type=Java5_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement150: BinaryAssociation = BinaryAssociation(
    name="elseStatement150",
    ends={
        Property(name="Java5_Statement152", type=Java5_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_IfStatement151", type=Java5_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedElement153: BinaryAssociation = BinaryAssociation(
    name="importedElement153",
    ends={
        Property(name="Java5_NamedElementRef155", type=Java5_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ImportDeclaration154", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand156: BinaryAssociation = BinaryAssociation(
    name="rightOperand156",
    ends={
        Property(name="Java5_Expression157", type=Java5_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_InfixExpression", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body142: BinaryAssociation = BinaryAssociation(
    name="body142",
    ends={
        Property(name="Java5_Statement144", type=Java5_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ForStatement143", type=Java5_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression145: BinaryAssociation = BinaryAssociation(
    name="expression145",
    ends={
        Property(name="Java5_Expression146", type=Java5_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_IfStatement", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body164: BinaryAssociation = BinaryAssociation(
    name="body164",
    ends={
        Property(name="Java5_Block165", type=Java5_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_Initializer", type=Java5_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand166: BinaryAssociation = BinaryAssociation(
    name="rightOperand166",
    ends={
        Property(name="Java5_NamedElementRef167", type=Java5_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_InstanceofExpression", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand168: BinaryAssociation = BinaryAssociation(
    name="leftOperand168",
    ends={
        Property(name="Java5_Expression170", type=Java5_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_InstanceofExpression169", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand158: BinaryAssociation = BinaryAssociation(
    name="leftOperand158",
    ends={
        Property(name="Java5_Expression160", type=Java5_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_InfixExpression159", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands161: BinaryAssociation = BinaryAssociation(
    name="extendedOperands161",
    ends={
        Property(name="Java5_Expression163", type=Java5_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_InfixExpression162", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier175: BinaryAssociation = BinaryAssociation(
    name="qualifier175",
    ends={
        Property(name="Java5_NamedElementRef177", type=Java5_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MemberRef176", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body178: BinaryAssociation = BinaryAssociation(
    name="body178",
    ends={
        Property(name="Java5_Block179", type=Java5_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodDeclaration", type=Java5_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thrownExceptions180: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions180",
    ends={
        Property(name="Java5_NamedElementRef182", type=Java5_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodDeclaration181", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType183: BinaryAssociation = BinaryAssociation(
    name="returnType183",
    ends={
        Property(name="Java5_NamedElementRef185", type=Java5_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodDeclaration184", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body171: BinaryAssociation = BinaryAssociation(
    name="body171",
    ends={
        Property(name="Java5_Statement172", type=Java5_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_LabeledStatement", type=Java5_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member173: BinaryAssociation = BinaryAssociation(
    name="member173",
    ends={
        Property(name="Java5_NamedElementRef174", type=Java5_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MemberRef", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters193: BinaryAssociation = BinaryAssociation(
    name="parameters193",
    ends={
        Property(name="SingleVariableDeclaration194", type=Java5_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methodDeclaration", type=Java5_SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method195: BinaryAssociation = BinaryAssociation(
    name="method195",
    ends={
        Property(name="Java5_NamedElementRef196", type=Java5_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodInvocation", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments197: BinaryAssociation = BinaryAssociation(
    name="arguments197",
    ends={
        Property(name="Java5_Expression199", type=Java5_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodInvocation198", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression200: BinaryAssociation = BinaryAssociation(
    name="expression200",
    ends={
        Property(name="Java5_Expression202", type=Java5_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodInvocation201", type=Java5_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters186: BinaryAssociation = BinaryAssociation(
    name="typeParameters186",
    ends={
        Property(name="Java5_TypeParameter", type=Java5_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodDeclaration187", type=Java5_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedMethodDeclaration189: BinaryAssociation = BinaryAssociation(
    name="redefinedMethodDeclaration189",
    ends={
        Property(name="MethodDeclaration", type=Java5_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinitions", type=Java5_MethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
redefinitions191: BinaryAssociation = BinaryAssociation(
    name="redefinitions191",
    ends={
        Property(name="MethodDeclaration192", type=Java5_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redefinedMethodDeclaration", type=Java5_MethodDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
qualifier205: BinaryAssociation = BinaryAssociation(
    name="qualifier205",
    ends={
        Property(name="Java5_NamedElementRef207", type=Java5_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodRef206", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters208: BinaryAssociation = BinaryAssociation(
    name="parameters208",
    ends={
        Property(name="Java5_MethodRefParameter", type=Java5_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodRef209", type=Java5_MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type210: BinaryAssociation = BinaryAssociation(
    name="type210",
    ends={
        Property(name="Java5_NamedElementRef212", type=Java5_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodRefParameter211", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method203: BinaryAssociation = BinaryAssociation(
    name="method203",
    ends={
        Property(name="Java5_NamedElementRef204", type=Java5_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_MethodRef", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
BodyDeclaration222: BinaryAssociation = BinaryAssociation(
    name="BodyDeclaration222",
    ends={
        Property(name="BodyDeclaration223", type=Java5_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifiers", type=Java5_BodyDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
SingleVariableDeclaration224: BinaryAssociation = BinaryAssociation(
    name="SingleVariableDeclaration224",
    ends={
        Property(name="SingleVariableDeclaration226", type=Java5_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifiers225", type=Java5_SingleVariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ownedElements213: BinaryAssociation = BinaryAssociation(
    name="ownedElements213",
    ends={
        Property(name="Java5_PackageDeclaration214", type=Java5_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_Model", type=Java5_PackageDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orphanTypes215: BinaryAssociation = BinaryAssociation(
    name="orphanTypes215",
    ends={
        Property(name="Java5_OrphanType", type=Java5_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_Model216", type=Java5_OrphanType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unresolvedItems217: BinaryAssociation = BinaryAssociation(
    name="unresolvedItems217",
    ends={
        Property(name="Java5_UnresolvedItem", type=Java5_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_Model218", type=Java5_UnresolvedItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits219: BinaryAssociation = BinaryAssociation(
    name="compilationUnits219",
    ends={
        Property(name="Java5_CompilationUnit221", type=Java5_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_Model220", type=Java5_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier232: BinaryAssociation = BinaryAssociation(
    name="qualifier232",
    ends={
        Property(name="Java5_NamedElementRef233", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_NamedElementRef231", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element234: BinaryAssociation = BinaryAssociation(
    name="element234",
    ends={
        Property(name="Java5_NamedElement", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_NamedElementRef235", type=Java5_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
VariableDeclarationStatement227: BinaryAssociation = BinaryAssociation(
    name="VariableDeclarationStatement227",
    ends={
        Property(name="VariableDeclarationStatement", type=Java5_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifiers228", type=Java5_VariableDeclarationStatement, multiplicity=Multiplicity(0, 1))
    }
)
VariableDeclarationExpression229: BinaryAssociation = BinaryAssociation(
    name="VariableDeclarationExpression229",
    ends={
        Property(name="VariableDeclarationExpression", type=Java5_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifiers230", type=Java5_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1))
    }
)
type241: BinaryAssociation = BinaryAssociation(
    name="type241",
    ends={
        Property(name="Java5_NamedElementRef242", type=Java5_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ParameterizedType", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments243: BinaryAssociation = BinaryAssociation(
    name="typeArguments243",
    ends={
        Property(name="Java5_NamedElementRef245", type=Java5_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ParameterizedType244", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElements236: BinaryAssociation = BinaryAssociation(
    name="ownedElements236",
    ends={
        Property(name="AbstractTypeDeclaration237", type=Java5_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=Java5_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPackages239: BinaryAssociation = BinaryAssociation(
    name="ownedPackages239",
    ends={
        Property(name="Java5_PackageDeclaration240", type=Java5_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_PackageDeclaration238", type=Java5_PackageDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand248: BinaryAssociation = BinaryAssociation(
    name="operand248",
    ends={
        Property(name="Java5_Expression249", type=Java5_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_PostfixExpression", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression246: BinaryAssociation = BinaryAssociation(
    name="expression246",
    ends={
        Property(name="Java5_Expression247", type=Java5_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ParenthesizedExpression", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand250: BinaryAssociation = BinaryAssociation(
    name="operand250",
    ends={
        Property(name="Java5_PrefixExpression", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Java5_Expression251", type=Java5_PrefixExpression, multiplicity=Multiplicity(1, 1))
    }
)
expression252: BinaryAssociation = BinaryAssociation(
    name="expression252",
    ends={
        Property(name="Java5_Expression253", type=Java5_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ReturnStatement", type=Java5_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type257: BinaryAssociation = BinaryAssociation(
    name="type257",
    ends={
        Property(name="Java5_SingleVariableDeclaration", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Java5_NamedElementRef258", type=Java5_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
method268: BinaryAssociation = BinaryAssociation(
    name="method268",
    ends={
        Property(name="Java5_NamedElementRef270", type=Java5_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SuperConstructorInvocation269", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodDeclaration259: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration259",
    ends={
        Property(name="MethodDeclaration260", type=Java5_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Java5_MethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
catchClause261: BinaryAssociation = BinaryAssociation(
    name="catchClause261",
    ends={
        Property(name="CatchClause", type=Java5_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="exception", type=Java5_CatchClause, multiplicity=Multiplicity(0, 1))
    }
)
modifiers254: BinaryAssociation = BinaryAssociation(
    name="modifiers254",
    ends={
        Property(name="Modifier256", type=Java5_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="SingleVariableDeclaration255", type=Java5_Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enhancedForStatement262: BinaryAssociation = BinaryAssociation(
    name="enhancedForStatement262",
    ends={
        Property(name="EnhancedForStatement", type=Java5_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=Java5_EnhancedForStatement, multiplicity=Multiplicity(0, 1))
    }
)
expression263: BinaryAssociation = BinaryAssociation(
    name="expression263",
    ends={
        Property(name="Java5_Expression264", type=Java5_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SuperConstructorInvocation", type=Java5_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments265: BinaryAssociation = BinaryAssociation(
    name="arguments265",
    ends={
        Property(name="Java5_Expression267", type=Java5_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SuperConstructorInvocation266", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression284: BinaryAssociation = BinaryAssociation(
    name="expression284",
    ends={
        Property(name="Java5_Expression285", type=Java5_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SwitchCase", type=Java5_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field271: BinaryAssociation = BinaryAssociation(
    name="field271",
    ends={
        Property(name="Java5_NamedElementRef272", type=Java5_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SuperFieldAccess", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier273: BinaryAssociation = BinaryAssociation(
    name="qualifier273",
    ends={
        Property(name="Java5_NamedElementRef275", type=Java5_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SuperFieldAccess274", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments276: BinaryAssociation = BinaryAssociation(
    name="arguments276",
    ends={
        Property(name="Java5_Expression277", type=Java5_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SuperMethodInvocation", type=Java5_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method278: BinaryAssociation = BinaryAssociation(
    name="method278",
    ends={
        Property(name="Java5_NamedElementRef280", type=Java5_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SuperMethodInvocation279", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier281: BinaryAssociation = BinaryAssociation(
    name="qualifier281",
    ends={
        Property(name="Java5_NamedElementRef283", type=Java5_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SuperMethodInvocation282", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body291: BinaryAssociation = BinaryAssociation(
    name="body291",
    ends={
        Property(name="Java5_Block292", type=Java5_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SynchronizedStatement", type=Java5_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression286: BinaryAssociation = BinaryAssociation(
    name="expression286",
    ends={
        Property(name="Java5_Expression287", type=Java5_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SwitchStatement", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements288: BinaryAssociation = BinaryAssociation(
    name="statements288",
    ends={
        Property(name="Java5_Statement290", type=Java5_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SwitchStatement289", type=Java5_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression299: BinaryAssociation = BinaryAssociation(
    name="expression299",
    ends={
        Property(name="Java5_Expression300", type=Java5_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ThrowStatement", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression293: BinaryAssociation = BinaryAssociation(
    name="expression293",
    ends={
        Property(name="Java5_Expression295", type=Java5_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_SynchronizedStatement294", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments296: BinaryAssociation = BinaryAssociation(
    name="fragments296",
    ends={
        Property(name="Java5_ASTNode", type=Java5_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_TagElement", type=Java5_ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier297: BinaryAssociation = BinaryAssociation(
    name="qualifier297",
    ends={
        Property(name="Java5_NamedElementRef298", type=Java5_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_ThisExpression", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body310: BinaryAssociation = BinaryAssociation(
    name="body310",
    ends={
        Property(name="Java5_Block311", type=Java5_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_TryStatement", type=Java5_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally312: BinaryAssociation = BinaryAssociation(
    name="finally312",
    ends={
        Property(name="Java5_Block314", type=Java5_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_TryStatement313", type=Java5_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters301: BinaryAssociation = BinaryAssociation(
    name="typeParameters301",
    ends={
        Property(name="Java5_TypeParameter302", type=Java5_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_TypeDeclaration", type=Java5_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration303: BinaryAssociation = BinaryAssociation(
    name="declaration303",
    ends={
        Property(name="Java5_AbstractTypeDeclaration304", type=Java5_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_TypeDeclarationStatement", type=Java5_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type305: BinaryAssociation = BinaryAssociation(
    name="type305",
    ends={
        Property(name="Java5_NamedElementRef306", type=Java5_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_TypeLiteral", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bounds307: BinaryAssociation = BinaryAssociation(
    name="bounds307",
    ends={
        Property(name="Java5_NamedElementRef309", type=Java5_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_TypeParameter308", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers324: BinaryAssociation = BinaryAssociation(
    name="modifiers324",
    ends={
        Property(name="Modifier326", type=Java5_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclarationExpression325", type=Java5_Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldDeclaration327: BinaryAssociation = BinaryAssociation(
    name="fieldDeclaration327",
    ends={
        Property(name="FieldDeclaration", type=Java5_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=Java5_FieldDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
catchClauses315: BinaryAssociation = BinaryAssociation(
    name="catchClauses315",
    ends={
        Property(name="Java5_CatchClause317", type=Java5_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_TryStatement316", type=Java5_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer318: BinaryAssociation = BinaryAssociation(
    name="initializer318",
    ends={
        Property(name="Java5_Expression319", type=Java5_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_VariableDeclaration", type=Java5_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type320: BinaryAssociation = BinaryAssociation(
    name="type320",
    ends={
        Property(name="Java5_NamedElementRef321", type=Java5_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_VariableDeclarationExpression", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments322: BinaryAssociation = BinaryAssociation(
    name="fragments322",
    ends={
        Property(name="VariableDeclarationFragment323", type=Java5_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationExpression", type=Java5_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression341: BinaryAssociation = BinaryAssociation(
    name="expression341",
    ends={
        Property(name="Java5_Expression342", type=Java5_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_WhileStatement", type=Java5_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableDeclarationStatement328: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationStatement328",
    ends={
        Property(name="VariableDeclarationStatement330", type=Java5_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments329", type=Java5_VariableDeclarationStatement, multiplicity=Multiplicity(0, 1))
    }
)
variableDeclarationExpression331: BinaryAssociation = BinaryAssociation(
    name="variableDeclarationExpression331",
    ends={
        Property(name="VariableDeclarationExpression333", type=Java5_VariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments332", type=Java5_VariableDeclarationExpression, multiplicity=Multiplicity(0, 1))
    }
)
type334: BinaryAssociation = BinaryAssociation(
    name="type334",
    ends={
        Property(name="Java5_NamedElementRef335", type=Java5_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_VariableDeclarationStatement", type=Java5_NamedElementRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments336: BinaryAssociation = BinaryAssociation(
    name="fragments336",
    ends={
        Property(name="VariableDeclarationFragment337", type=Java5_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="variableDeclarationStatement", type=Java5_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers338: BinaryAssociation = BinaryAssociation(
    name="modifiers338",
    ends={
        Property(name="Modifier340", type=Java5_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableDeclarationStatement339", type=Java5_Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body343: BinaryAssociation = BinaryAssociation(
    name="body343",
    ends={
        Property(name="Java5_Statement345", type=Java5_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_WhileStatement344", type=Java5_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bound346: BinaryAssociation = BinaryAssociation(
    name="bound346",
    ends={
        Property(name="Java5_NamedElementRef347", type=Java5_WildCardType, multiplicity=Multiplicity(1, 1)),
        Property(name="Java5_WildCardType", type=Java5_NamedElementRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_Java5_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java5_AbstractTypeDeclaration)
gen_Java5_AnnotationMemberValuePair_NamedElement = Generalization(general=NamedElement, specific=Java5_AnnotationMemberValuePair)
gen_Java5_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=Java5_AnnotationTypeDeclaration)
gen_Java5_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java5_AnnotationTypeMemberDeclaration)
gen_Java5_Annotation_Expression = Generalization(general=Expression, specific=Java5_Annotation)
gen_Java5_ArrayCreation_Expression = Generalization(general=Expression, specific=Java5_ArrayCreation)
gen_Java5_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=Java5_AnonymousClassDeclaration)
gen_Java5_ArrayAccess_Expression = Generalization(general=Expression, specific=Java5_ArrayAccess)
gen_Java5_AssertStatement_Statement = Generalization(general=Statement, specific=Java5_AssertStatement)
gen_Java5_Assignment_Expression = Generalization(general=Expression, specific=Java5_Assignment)
gen_Java5_Block_Statement = Generalization(general=Statement, specific=Java5_Block)
gen_Java5_BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=Java5_BodyDeclaration)
gen_Java5_ArrayInitializer_Expression = Generalization(general=Expression, specific=Java5_ArrayInitializer)
gen_Java5_ArrayLengthAccess_Expression = Generalization(general=Expression, specific=Java5_ArrayLengthAccess)
gen_Java5_ArrayType_OrphanType = Generalization(general=OrphanType, specific=Java5_ArrayType)
gen_Java5_CastExpression_Expression = Generalization(general=Expression, specific=Java5_CastExpression)
gen_Java5_CatchClause_Statement = Generalization(general=Statement, specific=Java5_CatchClause)
gen_Java5_CharacterLiteral_Expression = Generalization(general=Expression, specific=Java5_CharacterLiteral)
gen_Java5_ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=Java5_ClassDeclaration)
gen_Java5_BooleanLiteral_Expression = Generalization(general=Expression, specific=Java5_BooleanLiteral)
gen_Java5_BreakStatement_Statement = Generalization(general=Statement, specific=Java5_BreakStatement)
gen_Java5_CompilationUnit_NamedElement = Generalization(general=NamedElement, specific=Java5_CompilationUnit)
gen_Java5_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=Java5_ClassInstanceCreation)
gen_Java5_ConstructorInvocation_Statement = Generalization(general=Statement, specific=Java5_ConstructorInvocation)
gen_Java5_ContinueStatement_Statement = Generalization(general=Statement, specific=Java5_ContinueStatement)
gen_Java5_ConditionalExpression_Expression = Generalization(general=Expression, specific=Java5_ConditionalExpression)
gen_Java5_EmptyStatement_Statement = Generalization(general=Statement, specific=Java5_EmptyStatement)
gen_Java5_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=Java5_EnumDeclaration)
gen_Java5_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java5_EnumConstantDeclaration)
gen_Java5_EnhancedForStatement_Statement = Generalization(general=Statement, specific=Java5_EnhancedForStatement)
gen_Java5_DoStatement_Statement = Generalization(general=Statement, specific=Java5_DoStatement)
gen_Java5_Expression_ASTNode = Generalization(general=ASTNode, specific=Java5_Expression)
gen_Java5_ExpressionStatement_Statement = Generalization(general=Statement, specific=Java5_ExpressionStatement)
gen_Java5_FieldAccess_Expression = Generalization(general=Expression, specific=Java5_FieldAccess)
gen_Java5_ForStatement_Statement = Generalization(general=Statement, specific=Java5_ForStatement)
gen_Java5_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java5_FieldDeclaration)
gen_Java5_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=Java5_ImportDeclaration)
gen_Java5_InfixExpression_Expression = Generalization(general=Expression, specific=Java5_InfixExpression)
gen_Java5_IfStatement_Statement = Generalization(general=Statement, specific=Java5_IfStatement)
gen_Java5_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java5_Initializer)
gen_Java5_InstanceofExpression_Expression = Generalization(general=Expression, specific=Java5_InstanceofExpression)
gen_Java5_InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=Java5_InterfaceDeclaration)
gen_Java5_MethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=Java5_MethodDeclaration)
gen_Java5_LabeledStatement_NamedElement = Generalization(general=NamedElement, specific=Java5_LabeledStatement)
gen_Java5_LabeledStatement_Statement = Generalization(general=Statement, specific=Java5_LabeledStatement)
gen_Java5_MemberRef_ASTNode = Generalization(general=ASTNode, specific=Java5_MemberRef)
gen_Java5_MethodInvocation_Expression = Generalization(general=Expression, specific=Java5_MethodInvocation)
gen_Java5_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=Java5_MethodRefParameter)
gen_Java5_MethodRef_ASTNode = Generalization(general=ASTNode, specific=Java5_MethodRef)
gen_Java5_Modifier_ASTNode = Generalization(general=ASTNode, specific=Java5_Modifier)
gen_Java5_NamedElementRef_Expression = Generalization(general=Expression, specific=Java5_NamedElementRef)
gen_Java5_NullLiteral_Expression = Generalization(general=Expression, specific=Java5_NullLiteral)
gen_Java5_NumberLiteral_Expression = Generalization(general=Expression, specific=Java5_NumberLiteral)
gen_Java5_OrphanType_NamedElement = Generalization(general=NamedElement, specific=Java5_OrphanType)
gen_Java5_PackageDeclaration_NamedElement = Generalization(general=NamedElement, specific=Java5_PackageDeclaration)
gen_Java5_NamedElement_ASTNode = Generalization(general=ASTNode, specific=Java5_NamedElement)
gen_Java5_ParameterizedType_OrphanType = Generalization(general=OrphanType, specific=Java5_ParameterizedType)
gen_Java5_PostfixExpression_Expression = Generalization(general=Expression, specific=Java5_PostfixExpression)
gen_Java5_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=Java5_ParenthesizedExpression)
gen_Java5_PrimitiveType_OrphanType = Generalization(general=OrphanType, specific=Java5_PrimitiveType)
gen_Java5_PrimitiveTypeBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=Java5_PrimitiveTypeBoolean)
gen_Java5_PrimitiveTypeByte_PrimitiveType = Generalization(general=PrimitiveType, specific=Java5_PrimitiveTypeByte)
gen_Java5_PrefixExpression_Expression = Generalization(general=Expression, specific=Java5_PrefixExpression)
gen_Java5_PrimitiveTypeFloat_PrimitiveType = Generalization(general=PrimitiveType, specific=Java5_PrimitiveTypeFloat)
gen_Java5_PrimitiveTypeInt_PrimitiveType = Generalization(general=PrimitiveType, specific=Java5_PrimitiveTypeInt)
gen_Java5_PrimitiveTypeLong_PrimitiveType = Generalization(general=PrimitiveType, specific=Java5_PrimitiveTypeLong)
gen_Java5_PrimitiveTypeVoid_PrimitiveType = Generalization(general=PrimitiveType, specific=Java5_PrimitiveTypeVoid)
gen_Java5_ReturnStatement_Statement = Generalization(general=Statement, specific=Java5_ReturnStatement)
gen_Java5_PrimitiveTypeChar_PrimitiveType = Generalization(general=PrimitiveType, specific=Java5_PrimitiveTypeChar)
gen_Java5_PrimitiveTypeDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=Java5_PrimitiveTypeDouble)
gen_Java5_PrimitiveTypeShort_PrimitiveType = Generalization(general=PrimitiveType, specific=Java5_PrimitiveTypeShort)
gen_Java5_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=Java5_SingleVariableDeclaration)
gen_Java5_Statement_ASTNode = Generalization(general=ASTNode, specific=Java5_Statement)
gen_Java5_StringLiteral_Expression = Generalization(general=Expression, specific=Java5_StringLiteral)
gen_Java5_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=Java5_SuperConstructorInvocation)
gen_Java5_SwitchCase_Statement = Generalization(general=Statement, specific=Java5_SwitchCase)
gen_Java5_SuperFieldAccess_Expression = Generalization(general=Expression, specific=Java5_SuperFieldAccess)
gen_Java5_SwitchStatement_Statement = Generalization(general=Statement, specific=Java5_SwitchStatement)
gen_Java5_SuperMethodInvocation_Expression = Generalization(general=Expression, specific=Java5_SuperMethodInvocation)
gen_Java5_SynchronizedStatement_Statement = Generalization(general=Statement, specific=Java5_SynchronizedStatement)
gen_Java5_ThrowStatement_Statement = Generalization(general=Statement, specific=Java5_ThrowStatement)
gen_Java5_TagElement_ASTNode = Generalization(general=ASTNode, specific=Java5_TagElement)
gen_Java5_TextElement_ASTNode = Generalization(general=ASTNode, specific=Java5_TextElement)
gen_Java5_ThisExpression_Expression = Generalization(general=Expression, specific=Java5_ThisExpression)
gen_Java5_TryStatement_Statement = Generalization(general=Statement, specific=Java5_TryStatement)
gen_Java5_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=Java5_TypeDeclaration)
gen_Java5_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=Java5_TypeDeclarationStatement)
gen_Java5_TypeLiteral_Expression = Generalization(general=Expression, specific=Java5_TypeLiteral)
gen_Java5_TypeParameter_NamedElement = Generalization(general=NamedElement, specific=Java5_TypeParameter)
gen_Java5_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=Java5_VariableDeclarationFragment)
gen_Java5_UnresolvedItem_NamedElement = Generalization(general=NamedElement, specific=Java5_UnresolvedItem)
gen_Java5_VariableDeclaration_NamedElement = Generalization(general=NamedElement, specific=Java5_VariableDeclaration)
gen_Java5_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=Java5_VariableDeclarationExpression)
gen_Java5_WhileStatement_Statement = Generalization(general=Statement, specific=Java5_WhileStatement)
gen_Java5_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=Java5_VariableDeclarationStatement)
gen_Java5_WildCardType_OrphanType = Generalization(general=OrphanType, specific=Java5_WildCardType)

# Domain Model
domain_model = DomainModel(
    name="Java5",
    types={Java5_BodyDeclaration, Java5_ImportDeclaration, Java5_PackageDeclaration, Java5_AbstractTypeDeclaration, BodyDeclaration, NamedElement, Java5_Expression, Java5_AnnotationTypeDeclaration, AbstractTypeDeclaration, Java5_AnnotationTypeMemberDeclaration, Java5_NamedElementRef, Java5_Annotation, Expression, Java5_AnnotationMemberValuePair, Java5_ArrayCreation, Java5_ArrayInitializer, Java5_AnonymousClassDeclaration, ASTNode, Java5_ClassInstanceCreation, Java5_ArrayAccess, Java5_AssertStatement, Statement, Java5_Assignment, Java5_ASTNode, Java5_Block, Java5_Statement, Java5_ArrayLengthAccess, Java5_ArrayType, OrphanType, Java5_CastExpression, Java5_CatchClause, Java5_SingleVariableDeclaration, Java5_CharacterLiteral, Java5_ClassDeclaration, TypeDeclaration, Java5_Modifier, Java5_BooleanLiteral, Java5_BreakStatement, Java5_CompilationUnit, Java5_ConstructorInvocation, Java5_ContinueStatement, Java5_ConditionalExpression, Java5_EmptyStatement, Java5_EnumDeclaration, Java5_EnumConstantDeclaration, Java5_EnhancedForStatement, Java5_DoStatement, Java5_ExpressionStatement, Java5_FieldAccess, Java5_ForStatement, Java5_FieldDeclaration, Java5_VariableDeclarationFragment, Java5_InfixExpression, Java5_IfStatement, Java5_Initializer, Java5_InstanceofExpression, Java5_InterfaceDeclaration, Java5_LabeledStatement, Java5_MethodDeclaration, Java5_MemberRef, Java5_MethodInvocation, Java5_TypeParameter, Java5_MethodRefParameter, Java5_Model, Java5_MethodRef, Java5_OrphanType, Java5_UnresolvedItem, Java5_NullLiteral, Java5_NumberLiteral, Java5_VariableDeclarationStatement, Java5_VariableDeclarationExpression, Java5_NamedElement, Java5_ParameterizedType, Java5_PostfixExpression, Java5_ParenthesizedExpression, Java5_PrimitiveType, Java5_PrimitiveTypeBoolean, PrimitiveType, Java5_PrimitiveTypeByte, Java5_PrefixExpression, Java5_PrimitiveTypeFloat, Java5_PrimitiveTypeInt, Java5_PrimitiveTypeLong, Java5_PrimitiveTypeVoid, Java5_ReturnStatement, Java5_PrimitiveTypeChar, Java5_PrimitiveTypeDouble, Java5_PrimitiveTypeShort, Java5_SuperFieldAccess, VariableDeclaration, Java5_StringLiteral, Java5_SuperConstructorInvocation, Java5_SwitchStatement, Java5_SuperMethodInvocation, Java5_SwitchCase, Java5_SynchronizedStatement, Java5_ThrowStatement, Java5_TagElement, Java5_TextElement, Java5_ThisExpression, Java5_TryStatement, Java5_TypeDeclaration, Java5_TypeDeclarationStatement, Java5_TypeLiteral, Java5_VariableDeclaration, Java5_WhileStatement, Java5_WildCardType, InheritanceKind, VisibilityKind},
    associations={bodyDeclarations0, imports1, package2, member9, value12, default14, type16, superInterfaces3, type5, values7, index24, dimensions27, initializer29, type31, bodyDeclarations19, classInstanceCreation21, array22, elementType39, message41, expression43, leftHandSide46, rightHandSide48, statements51, expressions34, array37, expression61, type63, exception66, body67, superClass69, abstractTypeDeclaration52, annotations53, anonymousClassDeclarationOwner55, modifiers57, label59, method78, type81, imports84, anonymousClassDeclaration71, arguments73, expression75, expression93, thenExpression96, arguments99, method101, package86, types88, elseExpression91, enumConstants111, anonymousClassDeclaration112, arguments114, label104, expression106, body108, expression124, field126, expression128, body117, expression119, parameter122, fragments133, expression134, updaters136, initializers139, type131, thenStatement147, elseStatement150, importedElement153, rightOperand156, body142, expression145, body164, rightOperand166, leftOperand168, leftOperand158, extendedOperands161, qualifier175, body178, thrownExceptions180, returnType183, body171, member173, parameters193, method195, arguments197, expression200, typeParameters186, redefinedMethodDeclaration189, redefinitions191, qualifier205, parameters208, type210, method203, BodyDeclaration222, SingleVariableDeclaration224, ownedElements213, orphanTypes215, unresolvedItems217, compilationUnits219, qualifier232, element234, VariableDeclarationStatement227, VariableDeclarationExpression229, type241, typeArguments243, ownedElements236, ownedPackages239, operand248, expression246, operand250, expression252, type257, method268, methodDeclaration259, catchClause261, modifiers254, enhancedForStatement262, expression263, arguments265, expression284, field271, qualifier273, arguments276, method278, qualifier281, body291, expression286, statements288, expression299, expression293, fragments296, qualifier297, body310, finally312, typeParameters301, declaration303, type305, bounds307, modifiers324, fieldDeclaration327, catchClauses315, initializer318, type320, fragments322, expression341, variableDeclarationStatement328, variableDeclarationExpression331, type334, fragments336, modifiers338, body343, bound346},
    generalizations={gen_Java5_AbstractTypeDeclaration_BodyDeclaration, gen_Java5_AnnotationMemberValuePair_NamedElement, gen_Java5_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_Java5_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_Java5_Annotation_Expression, gen_Java5_ArrayCreation_Expression, gen_Java5_AnonymousClassDeclaration_ASTNode, gen_Java5_ArrayAccess_Expression, gen_Java5_AssertStatement_Statement, gen_Java5_Assignment_Expression, gen_Java5_Block_Statement, gen_Java5_BodyDeclaration_NamedElement, gen_Java5_ArrayInitializer_Expression, gen_Java5_ArrayLengthAccess_Expression, gen_Java5_ArrayType_OrphanType, gen_Java5_CastExpression_Expression, gen_Java5_CatchClause_Statement, gen_Java5_CharacterLiteral_Expression, gen_Java5_ClassDeclaration_TypeDeclaration, gen_Java5_BooleanLiteral_Expression, gen_Java5_BreakStatement_Statement, gen_Java5_CompilationUnit_NamedElement, gen_Java5_ClassInstanceCreation_Expression, gen_Java5_ConstructorInvocation_Statement, gen_Java5_ContinueStatement_Statement, gen_Java5_ConditionalExpression_Expression, gen_Java5_EmptyStatement_Statement, gen_Java5_EnumDeclaration_AbstractTypeDeclaration, gen_Java5_EnumConstantDeclaration_BodyDeclaration, gen_Java5_EnhancedForStatement_Statement, gen_Java5_DoStatement_Statement, gen_Java5_Expression_ASTNode, gen_Java5_ExpressionStatement_Statement, gen_Java5_FieldAccess_Expression, gen_Java5_ForStatement_Statement, gen_Java5_FieldDeclaration_BodyDeclaration, gen_Java5_ImportDeclaration_ASTNode, gen_Java5_InfixExpression_Expression, gen_Java5_IfStatement_Statement, gen_Java5_Initializer_BodyDeclaration, gen_Java5_InstanceofExpression_Expression, gen_Java5_InterfaceDeclaration_TypeDeclaration, gen_Java5_MethodDeclaration_BodyDeclaration, gen_Java5_LabeledStatement_NamedElement, gen_Java5_LabeledStatement_Statement, gen_Java5_MemberRef_ASTNode, gen_Java5_MethodInvocation_Expression, gen_Java5_MethodRefParameter_ASTNode, gen_Java5_MethodRef_ASTNode, gen_Java5_Modifier_ASTNode, gen_Java5_NamedElementRef_Expression, gen_Java5_NullLiteral_Expression, gen_Java5_NumberLiteral_Expression, gen_Java5_OrphanType_NamedElement, gen_Java5_PackageDeclaration_NamedElement, gen_Java5_NamedElement_ASTNode, gen_Java5_ParameterizedType_OrphanType, gen_Java5_PostfixExpression_Expression, gen_Java5_ParenthesizedExpression_Expression, gen_Java5_PrimitiveType_OrphanType, gen_Java5_PrimitiveTypeBoolean_PrimitiveType, gen_Java5_PrimitiveTypeByte_PrimitiveType, gen_Java5_PrefixExpression_Expression, gen_Java5_PrimitiveTypeFloat_PrimitiveType, gen_Java5_PrimitiveTypeInt_PrimitiveType, gen_Java5_PrimitiveTypeLong_PrimitiveType, gen_Java5_PrimitiveTypeVoid_PrimitiveType, gen_Java5_ReturnStatement_Statement, gen_Java5_PrimitiveTypeChar_PrimitiveType, gen_Java5_PrimitiveTypeDouble_PrimitiveType, gen_Java5_PrimitiveTypeShort_PrimitiveType, gen_Java5_SingleVariableDeclaration_VariableDeclaration, gen_Java5_Statement_ASTNode, gen_Java5_StringLiteral_Expression, gen_Java5_SuperConstructorInvocation_Statement, gen_Java5_SwitchCase_Statement, gen_Java5_SuperFieldAccess_Expression, gen_Java5_SwitchStatement_Statement, gen_Java5_SuperMethodInvocation_Expression, gen_Java5_SynchronizedStatement_Statement, gen_Java5_ThrowStatement_Statement, gen_Java5_TagElement_ASTNode, gen_Java5_TextElement_ASTNode, gen_Java5_ThisExpression_Expression, gen_Java5_TryStatement_Statement, gen_Java5_TypeDeclaration_AbstractTypeDeclaration, gen_Java5_TypeDeclarationStatement_Statement, gen_Java5_TypeLiteral_Expression, gen_Java5_TypeParameter_NamedElement, gen_Java5_VariableDeclarationFragment_VariableDeclaration, gen_Java5_UnresolvedItem_NamedElement, gen_Java5_VariableDeclaration_NamedElement, gen_Java5_VariableDeclarationExpression_Expression, gen_Java5_WhileStatement_Statement, gen_Java5_VariableDeclarationStatement_Statement, gen_Java5_WildCardType_OrphanType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)