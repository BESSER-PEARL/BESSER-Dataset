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
AssignmentOperatorKind: Enumeration = Enumeration(
    name="AssignmentOperatorKind",
    literals={
            EnumerationLiteral(name="plus_assign"),
			EnumerationLiteral(name="assign"),
			EnumerationLiteral(name="right_shift_unsigned_assign"),
			EnumerationLiteral(name="remainder_assign"),
			EnumerationLiteral(name="bit_and_assign"),
			EnumerationLiteral(name="left_shift_assign"),
			EnumerationLiteral(name="right_shift_signed_assign"),
			EnumerationLiteral(name="bit_xor_assign"),
			EnumerationLiteral(name="times_assign"),
			EnumerationLiteral(name="divide_assign"),
			EnumerationLiteral(name="minus_assign"),
			EnumerationLiteral(name="bit_or_assign")
    }
)

InfixExpressionOperatorKind: Enumeration = Enumeration(
    name="InfixExpressionOperatorKind",
    literals={
            EnumerationLiteral(name="or"),
			EnumerationLiteral(name="right_shift_signed"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="xor"),
			EnumerationLiteral(name="less_equals"),
			EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="not_equals"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="greater_equals"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="conditional_or"),
			EnumerationLiteral(name="remainder"),
			EnumerationLiteral(name="less"),
			EnumerationLiteral(name="left_shift"),
			EnumerationLiteral(name="right_shift_unsigned"),
			EnumerationLiteral(name="conditional_and"),
			EnumerationLiteral(name="times"),
			EnumerationLiteral(name="divide")
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
DOM_AnonymousClassDeclaration = Class(name="DOM::AnonymousClassDeclaration")
ASTNode = Class(name="ASTNode")
DOM_BodyDeclaration = Class(name="DOM::BodyDeclaration", is_abstract=True)
DOM_ExtendedModifier = Class(name="DOM::ExtendedModifier", is_abstract=True)
DOM_AST = Class(name="DOM::AST")
DOM_ASTNode = Class(name="DOM::ASTNode", is_abstract=True)
DOM_CompilationUnit = Class(name="DOM::CompilationUnit")
DOM_PackageDeclaration = Class(name="DOM::PackageDeclaration")
DOM_ImportDeclaration = Class(name="DOM::ImportDeclaration")
DOM_Javadoc = Class(name="DOM::Javadoc")
DOM_AbstractTypeDeclaration = Class(name="DOM::AbstractTypeDeclaration", is_abstract=True)
DOM_CatchClause = Class(name="DOM::CatchClause")
DOM_Block = Class(name="DOM::Block")
DOM_SingleVariableDeclaration = Class(name="DOM::SingleVariableDeclaration")
DOM_Comment = Class(name="DOM::Comment", is_abstract=True)
DOM_Name = Class(name="DOM::Name", is_abstract=True)
DOM_MemberRef = Class(name="DOM::MemberRef")
DOM_SimpleName = Class(name="DOM::SimpleName")
DOM_MemberValuePair = Class(name="DOM::MemberValuePair")
DOM_Expression = Class(name="DOM::Expression", is_abstract=True)
DOM_IType = Class(name="DOM::IType")
DOM_MethodRefParameter = Class(name="DOM::MethodRefParameter")
DOM_Type = Class(name="DOM::Type", is_abstract=True)
DOM_MethodRef = Class(name="DOM::MethodRef")
DOM_Annotation = Class(name="DOM::Annotation", is_abstract=True)
DOM_Modifier = Class(name="DOM::Modifier")
ExtendedModifier = Class(name="ExtendedModifier")
DOM_TagElement = Class(name="DOM::TagElement")
DOM_TextElement = Class(name="DOM::TextElement")
DOM_TypeParameter = Class(name="DOM::TypeParameter")
DOM_IPackageFragment = Class(name="DOM::IPackageFragment")
DOM_Statement = Class(name="DOM::Statement", is_abstract=True)
BodyDeclaration = Class(name="BodyDeclaration")
DOM_VariableDeclaration = Class(name="DOM::VariableDeclaration", is_abstract=True)
DOM_EnumConstantDeclaration = Class(name="DOM::EnumConstantDeclaration")
DOM_FieldDeclaration = Class(name="DOM::FieldDeclaration")
DOM_VariableDeclarationFragment = Class(name="DOM::VariableDeclarationFragment")
DOM_AnnotationTypeMemberDeclaration = Class(name="DOM::AnnotationTypeMemberDeclaration")
DOM_MethodDeclaration = Class(name="DOM::MethodDeclaration")
DOM_Initializer = Class(name="DOM::Initializer")
DOM_AnnotationTypeDeclaration = Class(name="DOM::AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
DOM_EnumDeclaration = Class(name="DOM::EnumDeclaration")
DOM_TypeDeclaration = Class(name="DOM::TypeDeclaration")
DOM_IMethod = Class(name="DOM::IMethod")
DOM_LineComment = Class(name="DOM::LineComment")
Expression = Class(name="Expression")
DOM_ArrayAccess = Class(name="DOM::ArrayAccess")
DOM_BlockComment = Class(name="DOM::BlockComment")
Comment = Class(name="Comment")
DOM_ArrayType = Class(name="DOM::ArrayType")
DOM_Assignment = Class(name="DOM::Assignment")
DOM_ArrayCreation = Class(name="DOM::ArrayCreation")
DOM_ArrayInitializer = Class(name="DOM::ArrayInitializer")
DOM_BooleanLiteral = Class(name="DOM::BooleanLiteral")
DOM_CastExpression = Class(name="DOM::CastExpression")
DOM_CharacterLiteral = Class(name="DOM::CharacterLiteral")
DOM_ClassInstanceCreation = Class(name="DOM::ClassInstanceCreation")
DOM_FieldAccess = Class(name="DOM::FieldAccess")
DOM_InfixExpression = Class(name="DOM::InfixExpression")
DOM_ConditionalExpression = Class(name="DOM::ConditionalExpression")
DOM_MethodInvocation = Class(name="DOM::MethodInvocation")
DOM_InstanceofExpression = Class(name="DOM::InstanceofExpression")
DOM_NumberLiteral = Class(name="DOM::NumberLiteral")
DOM_ParenthesizedExpression = Class(name="DOM::ParenthesizedExpression")
DOM_NullLiteral = Class(name="DOM::NullLiteral")
DOM_PostfixExpression = Class(name="DOM::PostfixExpression")
DOM_PrefixExpression = Class(name="DOM::PrefixExpression")
DOM_StringLiteral = Class(name="DOM::StringLiteral")
DOM_SuperFieldAccess = Class(name="DOM::SuperFieldAccess")
DOM_SuperMethodInvocation = Class(name="DOM::SuperMethodInvocation")
DOM_ThisExpression = Class(name="DOM::ThisExpression")
DOM_TypeLiteral = Class(name="DOM::TypeLiteral")
DOM_VariableDeclarationExpression = Class(name="DOM::VariableDeclarationExpression")
DOM_ConstructorInvocation = Class(name="DOM::ConstructorInvocation")
DOM_AssertStatement = Class(name="DOM::AssertStatement")
Statement = Class(name="Statement")
DOM_BreakStatement = Class(name="DOM::BreakStatement")
DOM_EnhancedForStatement = Class(name="DOM::EnhancedForStatement")
DOM_ContinueStatement = Class(name="DOM::ContinueStatement")
DOM_DoStatement = Class(name="DOM::DoStatement")
DOM_EmptyStatement = Class(name="DOM::EmptyStatement")
DOM_ExpressionStatement = Class(name="DOM::ExpressionStatement")
DOM_ForStatement = Class(name="DOM::ForStatement")
DOM_LabeledStatement = Class(name="DOM::LabeledStatement")
DOM_IfStatement = Class(name="DOM::IfStatement")
DOM_ReturnStatement = Class(name="DOM::ReturnStatement")
DOM_SuperConstructorInvocation = Class(name="DOM::SuperConstructorInvocation")
DOM_SwitchCase = Class(name="DOM::SwitchCase")
DOM_SwitchStatement = Class(name="DOM::SwitchStatement")
DOM_SynchronizedStatement = Class(name="DOM::SynchronizedStatement")
DOM_ThrowStatement = Class(name="DOM::ThrowStatement")
DOM_TryStatement = Class(name="DOM::TryStatement")
DOM_TypeDeclarationStatement = Class(name="DOM::TypeDeclarationStatement")
DOM_VariableDeclarationStatement = Class(name="DOM::VariableDeclarationStatement")
DOM_ParameterizedType = Class(name="DOM::ParameterizedType")
DOM_WhileStatement = Class(name="DOM::WhileStatement")
Type = Class(name="Type")
VariableDeclaration = Class(name="VariableDeclaration")
DOM_PrimitiveType = Class(name="DOM::PrimitiveType")
DOM_QualifiedType = Class(name="DOM::QualifiedType")
DOM_SimpleType = Class(name="DOM::SimpleType")
DOM_WildcardType = Class(name="DOM::WildcardType")
DOM_MarkerAnnotation = Class(name="DOM::MarkerAnnotation")
Annotation = Class(name="Annotation")
DOM_NormalAnnotation = Class(name="DOM::NormalAnnotation")
DOM_SingleMemberAnnotation = Class(name="DOM::SingleMemberAnnotation")
DOM_QualifiedName = Class(name="DOM::QualifiedName")
Name = Class(name="Name")

# DOM_AnonymousClassDeclaration class attributes and methods

# ASTNode class attributes and methods

# DOM_BodyDeclaration class attributes and methods

# DOM_ExtendedModifier class attributes and methods

# DOM_AST class attributes and methods

# DOM_ASTNode class attributes and methods

# DOM_CompilationUnit class attributes and methods

# DOM_PackageDeclaration class attributes and methods

# DOM_ImportDeclaration class attributes and methods
DOM_ImportDeclaration_onDemand: Property = Property(name="onDemand", type=StringType)
DOM_ImportDeclaration_static: Property = Property(name="static", type=StringType)
DOM_ImportDeclaration.attributes={DOM_ImportDeclaration_static, DOM_ImportDeclaration_onDemand}

# DOM_Javadoc class attributes and methods

# DOM_AbstractTypeDeclaration class attributes and methods
DOM_AbstractTypeDeclaration_localTypeDeclaration: Property = Property(name="localTypeDeclaration", type=StringType)
DOM_AbstractTypeDeclaration_memberTypeDeclaration: Property = Property(name="memberTypeDeclaration", type=StringType)
DOM_AbstractTypeDeclaration_packageMemberTypeDeclaration: Property = Property(name="packageMemberTypeDeclaration", type=StringType)
DOM_AbstractTypeDeclaration.attributes={DOM_AbstractTypeDeclaration_packageMemberTypeDeclaration, DOM_AbstractTypeDeclaration_memberTypeDeclaration, DOM_AbstractTypeDeclaration_localTypeDeclaration}

# DOM_CatchClause class attributes and methods

# DOM_Block class attributes and methods

# DOM_SingleVariableDeclaration class attributes and methods
DOM_SingleVariableDeclaration_varargs: Property = Property(name="varargs", type=StringType)
DOM_SingleVariableDeclaration.attributes={DOM_SingleVariableDeclaration_varargs}

# DOM_Comment class attributes and methods

# DOM_Name class attributes and methods
DOM_Name_fullyQualifiedName: Property = Property(name="fullyQualifiedName", type=StringType)
DOM_Name.attributes={DOM_Name_fullyQualifiedName}

# DOM_MemberRef class attributes and methods

# DOM_SimpleName class attributes and methods
DOM_SimpleName_identifier: Property = Property(name="identifier", type=StringType)
DOM_SimpleName_declaration: Property = Property(name="declaration", type=StringType)
DOM_SimpleName.attributes={DOM_SimpleName_identifier, DOM_SimpleName_declaration}

# DOM_MemberValuePair class attributes and methods

# DOM_Expression class attributes and methods
DOM_Expression_resolveBoxing: Property = Property(name="resolveBoxing", type=StringType)
DOM_Expression_resolveUnboxing: Property = Property(name="resolveUnboxing", type=StringType)
DOM_Expression.attributes={DOM_Expression_resolveBoxing, DOM_Expression_resolveUnboxing}

# DOM_IType class attributes and methods

# DOM_MethodRefParameter class attributes and methods
DOM_MethodRefParameter_varargs: Property = Property(name="varargs", type=StringType)
DOM_MethodRefParameter.attributes={DOM_MethodRefParameter_varargs}

# DOM_Type class attributes and methods

# DOM_MethodRef class attributes and methods

# DOM_Annotation class attributes and methods

# DOM_Modifier class attributes and methods
DOM_Modifier_protected: Property = Property(name="protected", type=StringType)
DOM_Modifier_public: Property = Property(name="public", type=StringType)
DOM_Modifier_static: Property = Property(name="static", type=StringType)
DOM_Modifier_strictfp: Property = Property(name="strictfp", type=StringType)
DOM_Modifier_synchronized: Property = Property(name="synchronized", type=StringType)
DOM_Modifier_transient: Property = Property(name="transient", type=StringType)
DOM_Modifier_volatile: Property = Property(name="volatile", type=StringType)
DOM_Modifier_abstract: Property = Property(name="abstract", type=StringType)
DOM_Modifier_final: Property = Property(name="final", type=StringType)
DOM_Modifier_native: Property = Property(name="native", type=StringType)
DOM_Modifier_none: Property = Property(name="none", type=StringType)
DOM_Modifier_private: Property = Property(name="private", type=StringType)
DOM_Modifier.attributes={DOM_Modifier_none, DOM_Modifier_final, DOM_Modifier_native, DOM_Modifier_public, DOM_Modifier_static, DOM_Modifier_protected, DOM_Modifier_strictfp, DOM_Modifier_transient, DOM_Modifier_synchronized, DOM_Modifier_private, DOM_Modifier_volatile, DOM_Modifier_abstract}

# ExtendedModifier class attributes and methods

# DOM_TagElement class attributes and methods
DOM_TagElement_tagName: Property = Property(name="tagName", type=StringType)
DOM_TagElement_nested: Property = Property(name="nested", type=StringType)
DOM_TagElement.attributes={DOM_TagElement_nested, DOM_TagElement_tagName}

# DOM_TextElement class attributes and methods
DOM_TextElement_text: Property = Property(name="text", type=StringType)
DOM_TextElement.attributes={DOM_TextElement_text}

# DOM_TypeParameter class attributes and methods

# DOM_IPackageFragment class attributes and methods

# DOM_Statement class attributes and methods

# BodyDeclaration class attributes and methods

# DOM_VariableDeclaration class attributes and methods
DOM_VariableDeclaration_extraDimensions: Property = Property(name="extraDimensions", type=StringType)
DOM_VariableDeclaration.attributes={DOM_VariableDeclaration_extraDimensions}

# DOM_EnumConstantDeclaration class attributes and methods

# DOM_FieldDeclaration class attributes and methods

# DOM_VariableDeclarationFragment class attributes and methods

# DOM_AnnotationTypeMemberDeclaration class attributes and methods

# DOM_MethodDeclaration class attributes and methods
DOM_MethodDeclaration_extraDimensions: Property = Property(name="extraDimensions", type=StringType)
DOM_MethodDeclaration_constructor: Property = Property(name="constructor", type=StringType)
DOM_MethodDeclaration_varargs: Property = Property(name="varargs", type=StringType)
DOM_MethodDeclaration.attributes={DOM_MethodDeclaration_extraDimensions, DOM_MethodDeclaration_constructor, DOM_MethodDeclaration_varargs}

# DOM_Initializer class attributes and methods

# DOM_AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# DOM_EnumDeclaration class attributes and methods

# DOM_TypeDeclaration class attributes and methods
DOM_TypeDeclaration_interface: Property = Property(name="interface", type=StringType)
DOM_TypeDeclaration.attributes={DOM_TypeDeclaration_interface}

# DOM_IMethod class attributes and methods

# DOM_LineComment class attributes and methods

# Expression class attributes and methods

# DOM_ArrayAccess class attributes and methods

# DOM_BlockComment class attributes and methods

# Comment class attributes and methods

# DOM_ArrayType class attributes and methods
DOM_ArrayType_dimensions: Property = Property(name="dimensions", type=StringType)
DOM_ArrayType.attributes={DOM_ArrayType_dimensions}

# DOM_Assignment class attributes and methods
DOM_Assignment_operator: Property = Property(name="operator", type=StringType)
DOM_Assignment.attributes={DOM_Assignment_operator}

# DOM_ArrayCreation class attributes and methods

# DOM_ArrayInitializer class attributes and methods

# DOM_BooleanLiteral class attributes and methods
DOM_BooleanLiteral_booleanValue: Property = Property(name="booleanValue", type=StringType)
DOM_BooleanLiteral.attributes={DOM_BooleanLiteral_booleanValue}

# DOM_CastExpression class attributes and methods

# DOM_CharacterLiteral class attributes and methods
DOM_CharacterLiteral_charValue: Property = Property(name="charValue", type=StringType)
DOM_CharacterLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
DOM_CharacterLiteral.attributes={DOM_CharacterLiteral_escapedValue, DOM_CharacterLiteral_charValue}

# DOM_ClassInstanceCreation class attributes and methods

# DOM_FieldAccess class attributes and methods

# DOM_InfixExpression class attributes and methods
DOM_InfixExpression_operator: Property = Property(name="operator", type=StringType)
DOM_InfixExpression.attributes={DOM_InfixExpression_operator}

# DOM_ConditionalExpression class attributes and methods

# DOM_MethodInvocation class attributes and methods

# DOM_InstanceofExpression class attributes and methods

# DOM_NumberLiteral class attributes and methods
DOM_NumberLiteral_token: Property = Property(name="token", type=StringType)
DOM_NumberLiteral.attributes={DOM_NumberLiteral_token}

# DOM_ParenthesizedExpression class attributes and methods

# DOM_NullLiteral class attributes and methods

# DOM_PostfixExpression class attributes and methods
DOM_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
DOM_PostfixExpression.attributes={DOM_PostfixExpression_operator}

# DOM_PrefixExpression class attributes and methods
DOM_PrefixExpression_operator: Property = Property(name="operator", type=StringType)
DOM_PrefixExpression.attributes={DOM_PrefixExpression_operator}

# DOM_StringLiteral class attributes and methods
DOM_StringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
DOM_StringLiteral_literalValue: Property = Property(name="literalValue", type=StringType)
DOM_StringLiteral.attributes={DOM_StringLiteral_escapedValue, DOM_StringLiteral_literalValue}

# DOM_SuperFieldAccess class attributes and methods

# DOM_SuperMethodInvocation class attributes and methods

# DOM_ThisExpression class attributes and methods

# DOM_TypeLiteral class attributes and methods

# DOM_VariableDeclarationExpression class attributes and methods

# DOM_ConstructorInvocation class attributes and methods

# DOM_AssertStatement class attributes and methods

# Statement class attributes and methods

# DOM_BreakStatement class attributes and methods

# DOM_EnhancedForStatement class attributes and methods

# DOM_ContinueStatement class attributes and methods

# DOM_DoStatement class attributes and methods

# DOM_EmptyStatement class attributes and methods

# DOM_ExpressionStatement class attributes and methods

# DOM_ForStatement class attributes and methods

# DOM_LabeledStatement class attributes and methods

# DOM_IfStatement class attributes and methods

# DOM_ReturnStatement class attributes and methods

# DOM_SuperConstructorInvocation class attributes and methods

# DOM_SwitchCase class attributes and methods
DOM_SwitchCase_default: Property = Property(name="default", type=StringType)
DOM_SwitchCase.attributes={DOM_SwitchCase_default}

# DOM_SwitchStatement class attributes and methods

# DOM_SynchronizedStatement class attributes and methods

# DOM_ThrowStatement class attributes and methods

# DOM_TryStatement class attributes and methods

# DOM_TypeDeclarationStatement class attributes and methods

# DOM_VariableDeclarationStatement class attributes and methods

# DOM_ParameterizedType class attributes and methods

# DOM_WhileStatement class attributes and methods

# Type class attributes and methods

# VariableDeclaration class attributes and methods

# DOM_PrimitiveType class attributes and methods
DOM_PrimitiveType_code: Property = Property(name="code", type=StringType)
DOM_PrimitiveType.attributes={DOM_PrimitiveType_code}

# DOM_QualifiedType class attributes and methods

# DOM_SimpleType class attributes and methods

# DOM_WildcardType class attributes and methods
DOM_WildcardType_upperBound: Property = Property(name="upperBound", type=StringType)
DOM_WildcardType.attributes={DOM_WildcardType_upperBound}

# DOM_MarkerAnnotation class attributes and methods

# Annotation class attributes and methods

# DOM_NormalAnnotation class attributes and methods

# DOM_SingleMemberAnnotation class attributes and methods

# DOM_QualifiedName class attributes and methods

# Name class attributes and methods

# Relationships
bodyDeclarations1: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations1",
    ends={
        Property(name="DOM_BodyDeclaration", type=DOM_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AnonymousClassDeclaration", type=DOM_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers2: BinaryAssociation = BinaryAssociation(
    name="modifiers2",
    ends={
        Property(name="DOM_ExtendedModifier", type=DOM_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_BodyDeclaration3", type=DOM_ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits0: BinaryAssociation = BinaryAssociation(
    name="compilationUnits0",
    ends={
        Property(name="DOM_ASTNode", type=DOM_AST, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AST", type=DOM_ASTNode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alternateRoot9: BinaryAssociation = BinaryAssociation(
    name="alternateRoot9",
    ends={
        Property(name="DOM_Comment", type=DOM_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ASTNode10", type=DOM_Comment, multiplicity=Multiplicity(1, 1))
    }
)
comments11: BinaryAssociation = BinaryAssociation(
    name="comments11",
    ends={
        Property(name="DOM_Comment12", type=DOM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CompilationUnit", type=DOM_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package13: BinaryAssociation = BinaryAssociation(
    name="package13",
    ends={
        Property(name="DOM_PackageDeclaration", type=DOM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CompilationUnit14", type=DOM_PackageDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
imports15: BinaryAssociation = BinaryAssociation(
    name="imports15",
    ends={
        Property(name="DOM_ImportDeclaration", type=DOM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CompilationUnit16", type=DOM_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc4: BinaryAssociation = BinaryAssociation(
    name="javadoc4",
    ends={
        Property(name="DOM_Javadoc", type=DOM_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_BodyDeclaration5", type=DOM_Javadoc, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types17: BinaryAssociation = BinaryAssociation(
    name="types17",
    ends={
        Property(name="DOM_AbstractTypeDeclaration", type=DOM_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CompilationUnit18", type=DOM_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body6: BinaryAssociation = BinaryAssociation(
    name="body6",
    ends={
        Property(name="DOM_Block", type=DOM_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CatchClause", type=DOM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception7: BinaryAssociation = BinaryAssociation(
    name="exception7",
    ends={
        Property(name="DOM_SingleVariableDeclaration", type=DOM_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CatchClause8", type=DOM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name20: BinaryAssociation = BinaryAssociation(
    name="name20",
    ends={
        Property(name="DOM_Name", type=DOM_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ImportDeclaration21", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name22: BinaryAssociation = BinaryAssociation(
    name="name22",
    ends={
        Property(name="DOM_SimpleName", type=DOM_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MemberRef", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier23: BinaryAssociation = BinaryAssociation(
    name="qualifier23",
    ends={
        Property(name="DOM_Name25", type=DOM_MemberRef, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MemberRef24", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeBinding19: BinaryAssociation = BinaryAssociation(
    name="typeBinding19",
    ends={
        Property(name="DOM_IType", type=DOM_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Expression", type=DOM_IType, multiplicity=Multiplicity(1, 1))
    }
)
qualifier33: BinaryAssociation = BinaryAssociation(
    name="qualifier33",
    ends={
        Property(name="DOM_MethodRef34", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="DOM_Name35", type=DOM_MethodRef, multiplicity=Multiplicity(1, 1))
    }
)
parameters36: BinaryAssociation = BinaryAssociation(
    name="parameters36",
    ends={
        Property(name="DOM_MethodRefParameter", type=DOM_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodRef37", type=DOM_MethodRefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name38: BinaryAssociation = BinaryAssociation(
    name="name38",
    ends={
        Property(name="DOM_SimpleName40", type=DOM_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodRefParameter39", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type41: BinaryAssociation = BinaryAssociation(
    name="type41",
    ends={
        Property(name="DOM_Type", type=DOM_MethodRefParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodRefParameter42", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name26: BinaryAssociation = BinaryAssociation(
    name="name26",
    ends={
        Property(name="DOM_SimpleName27", type=DOM_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MemberValuePair", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value28: BinaryAssociation = BinaryAssociation(
    name="value28",
    ends={
        Property(name="DOM_Expression30", type=DOM_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MemberValuePair29", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name31: BinaryAssociation = BinaryAssociation(
    name="name31",
    ends={
        Property(name="DOM_SimpleName32", type=DOM_MethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodRef", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations43: BinaryAssociation = BinaryAssociation(
    name="annotations43",
    ends={
        Property(name="DOM_Annotation", type=DOM_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PackageDeclaration44", type=DOM_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments53: BinaryAssociation = BinaryAssociation(
    name="fragments53",
    ends={
        Property(name="DOM_ASTNode54", type=DOM_TagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TagElement", type=DOM_ASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javadoc45: BinaryAssociation = BinaryAssociation(
    name="javadoc45",
    ends={
        Property(name="DOM_Javadoc47", type=DOM_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PackageDeclaration46", type=DOM_Javadoc, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name48: BinaryAssociation = BinaryAssociation(
    name="name48",
    ends={
        Property(name="DOM_Name50", type=DOM_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PackageDeclaration49", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
binding51: BinaryAssociation = BinaryAssociation(
    name="binding51",
    ends={
        Property(name="DOM_IPackageFragment", type=DOM_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PackageDeclaration52", type=DOM_IPackageFragment, multiplicity=Multiplicity(1, 1))
    }
)
name62: BinaryAssociation = BinaryAssociation(
    name="name62",
    ends={
        Property(name="DOM_SimpleName64", type=DOM_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclaration63", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bodyDeclarations65: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations65",
    ends={
        Property(name="DOM_BodyDeclaration67", type=DOM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AbstractTypeDeclaration66", type=DOM_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name55: BinaryAssociation = BinaryAssociation(
    name="name55",
    ends={
        Property(name="DOM_SimpleName56", type=DOM_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeParameter", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeBounds57: BinaryAssociation = BinaryAssociation(
    name="typeBounds57",
    ends={
        Property(name="DOM_Type59", type=DOM_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeParameter58", type=DOM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer60: BinaryAssociation = BinaryAssociation(
    name="initializer60",
    ends={
        Property(name="DOM_Expression61", type=DOM_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclaration", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name68: BinaryAssociation = BinaryAssociation(
    name="name68",
    ends={
        Property(name="DOM_SimpleName70", type=DOM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AbstractTypeDeclaration69", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments79: BinaryAssociation = BinaryAssociation(
    name="arguments79",
    ends={
        Property(name="DOM_Expression80", type=DOM_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnumConstantDeclaration", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration81: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration81",
    ends={
        Property(name="DOM_AnonymousClassDeclaration83", type=DOM_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnumConstantDeclaration82", type=DOM_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name84: BinaryAssociation = BinaryAssociation(
    name="name84",
    ends={
        Property(name="DOM_SimpleName86", type=DOM_EnumConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnumConstantDeclaration85", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
default71: BinaryAssociation = BinaryAssociation(
    name="default71",
    ends={
        Property(name="DOM_Expression72", type=DOM_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AnnotationTypeMemberDeclaration", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name73: BinaryAssociation = BinaryAssociation(
    name="name73",
    ends={
        Property(name="DOM_SimpleName75", type=DOM_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AnnotationTypeMemberDeclaration74", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type76: BinaryAssociation = BinaryAssociation(
    name="type76",
    ends={
        Property(name="DOM_Type78", type=DOM_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AnnotationTypeMemberDeclaration77", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body93: BinaryAssociation = BinaryAssociation(
    name="body93",
    ends={
        Property(name="DOM_Block94", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration", type=DOM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name95: BinaryAssociation = BinaryAssociation(
    name="name95",
    ends={
        Property(name="DOM_SimpleName97", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration96", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType98: BinaryAssociation = BinaryAssociation(
    name="returnType98",
    ends={
        Property(name="DOM_Type100", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration99", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments87: BinaryAssociation = BinaryAssociation(
    name="fragments87",
    ends={
        Property(name="DOM_VariableDeclarationFragment", type=DOM_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_FieldDeclaration", type=DOM_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type88: BinaryAssociation = BinaryAssociation(
    name="type88",
    ends={
        Property(name="DOM_Type90", type=DOM_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_FieldDeclaration89", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body91: BinaryAssociation = BinaryAssociation(
    name="body91",
    ends={
        Property(name="DOM_Block92", type=DOM_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Initializer", type=DOM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
binding110: BinaryAssociation = BinaryAssociation(
    name="binding110",
    ends={
        Property(name="DOM_IMethod", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration111", type=DOM_IMethod, multiplicity=Multiplicity(1, 1))
    }
)
superInterfaceTypes112: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes112",
    ends={
        Property(name="DOM_Type113", type=DOM_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnumDeclaration", type=DOM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumConstants114: BinaryAssociation = BinaryAssociation(
    name="enumConstants114",
    ends={
        Property(name="DOM_EnumConstantDeclaration116", type=DOM_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnumDeclaration115", type=DOM_EnumConstantDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters101: BinaryAssociation = BinaryAssociation(
    name="parameters101",
    ends={
        Property(name="DOM_SingleVariableDeclaration103", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration102", type=DOM_SingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thrownExceptions104: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions104",
    ends={
        Property(name="DOM_Name106", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration105", type=DOM_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters107: BinaryAssociation = BinaryAssociation(
    name="typeParameters107",
    ends={
        Property(name="DOM_TypeParameter109", type=DOM_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodDeclaration108", type=DOM_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags125: BinaryAssociation = BinaryAssociation(
    name="tags125",
    ends={
        Property(name="DOM_TagElement127", type=DOM_Javadoc, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Javadoc126", type=DOM_TagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeName128: BinaryAssociation = BinaryAssociation(
    name="typeName128",
    ends={
        Property(name="DOM_Name130", type=DOM_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Annotation129", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superclassType117: BinaryAssociation = BinaryAssociation(
    name="superclassType117",
    ends={
        Property(name="DOM_Type118", type=DOM_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeDeclaration", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superInterfaceTypes119: BinaryAssociation = BinaryAssociation(
    name="superInterfaceTypes119",
    ends={
        Property(name="DOM_Type121", type=DOM_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeDeclaration120", type=DOM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters122: BinaryAssociation = BinaryAssociation(
    name="typeParameters122",
    ends={
        Property(name="DOM_TypeParameter124", type=DOM_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeDeclaration123", type=DOM_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer138: BinaryAssociation = BinaryAssociation(
    name="initializer138",
    ends={
        Property(name="DOM_ArrayInitializer", type=DOM_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayCreation139", type=DOM_ArrayInitializer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type140: BinaryAssociation = BinaryAssociation(
    name="type140",
    ends={
        Property(name="DOM_ArrayType", type=DOM_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayCreation141", type=DOM_ArrayType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions142: BinaryAssociation = BinaryAssociation(
    name="expressions142",
    ends={
        Property(name="DOM_Expression144", type=DOM_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayInitializer143", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftHandSide145: BinaryAssociation = BinaryAssociation(
    name="leftHandSide145",
    ends={
        Property(name="DOM_Expression146", type=DOM_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Assignment", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array131: BinaryAssociation = BinaryAssociation(
    name="array131",
    ends={
        Property(name="DOM_Expression132", type=DOM_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayAccess", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index133: BinaryAssociation = BinaryAssociation(
    name="index133",
    ends={
        Property(name="DOM_Expression135", type=DOM_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayAccess134", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions136: BinaryAssociation = BinaryAssociation(
    name="dimensions136",
    ends={
        Property(name="DOM_Expression137", type=DOM_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayCreation", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression150: BinaryAssociation = BinaryAssociation(
    name="expression150",
    ends={
        Property(name="DOM_Expression151", type=DOM_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CastExpression", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide147: BinaryAssociation = BinaryAssociation(
    name="rightHandSide147",
    ends={
        Property(name="DOM_Expression149", type=DOM_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Assignment148", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments155: BinaryAssociation = BinaryAssociation(
    name="arguments155",
    ends={
        Property(name="DOM_Expression156", type=DOM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ClassInstanceCreation", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClassDeclaration157: BinaryAssociation = BinaryAssociation(
    name="anonymousClassDeclaration157",
    ends={
        Property(name="DOM_AnonymousClassDeclaration159", type=DOM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ClassInstanceCreation158", type=DOM_AnonymousClassDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression160: BinaryAssociation = BinaryAssociation(
    name="expression160",
    ends={
        Property(name="DOM_Expression162", type=DOM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ClassInstanceCreation161", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type163: BinaryAssociation = BinaryAssociation(
    name="type163",
    ends={
        Property(name="DOM_Type165", type=DOM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ClassInstanceCreation164", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments166: BinaryAssociation = BinaryAssociation(
    name="typeArguments166",
    ends={
        Property(name="DOM_Type168", type=DOM_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ClassInstanceCreation167", type=DOM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type152: BinaryAssociation = BinaryAssociation(
    name="type152",
    ends={
        Property(name="DOM_Type154", type=DOM_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_CastExpression153", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression177: BinaryAssociation = BinaryAssociation(
    name="expression177",
    ends={
        Property(name="DOM_Expression178", type=DOM_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_FieldAccess", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name179: BinaryAssociation = BinaryAssociation(
    name="name179",
    ends={
        Property(name="DOM_SimpleName181", type=DOM_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_FieldAccess180", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedOperands182: BinaryAssociation = BinaryAssociation(
    name="extendedOperands182",
    ends={
        Property(name="DOM_Expression183", type=DOM_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_InfixExpression", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseExpression169: BinaryAssociation = BinaryAssociation(
    name="elseExpression169",
    ends={
        Property(name="DOM_Expression170", type=DOM_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ConditionalExpression", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression171: BinaryAssociation = BinaryAssociation(
    name="expression171",
    ends={
        Property(name="DOM_Expression173", type=DOM_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ConditionalExpression172", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression174: BinaryAssociation = BinaryAssociation(
    name="thenExpression174",
    ends={
        Property(name="DOM_Expression176", type=DOM_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ConditionalExpression175", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand192: BinaryAssociation = BinaryAssociation(
    name="rightOperand192",
    ends={
        Property(name="DOM_Type194", type=DOM_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_InstanceofExpression193", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand184: BinaryAssociation = BinaryAssociation(
    name="leftOperand184",
    ends={
        Property(name="DOM_Expression186", type=DOM_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_InfixExpression185", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments195: BinaryAssociation = BinaryAssociation(
    name="arguments195",
    ends={
        Property(name="DOM_Expression196", type=DOM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodInvocation", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightOperand187: BinaryAssociation = BinaryAssociation(
    name="rightOperand187",
    ends={
        Property(name="DOM_Expression189", type=DOM_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_InfixExpression188", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand190: BinaryAssociation = BinaryAssociation(
    name="leftOperand190",
    ends={
        Property(name="DOM_Expression191", type=DOM_InstanceofExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_InstanceofExpression", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression197: BinaryAssociation = BinaryAssociation(
    name="expression197",
    ends={
        Property(name="DOM_Expression199", type=DOM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodInvocation198", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name200: BinaryAssociation = BinaryAssociation(
    name="name200",
    ends={
        Property(name="DOM_SimpleName202", type=DOM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodInvocation201", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments203: BinaryAssociation = BinaryAssociation(
    name="typeArguments203",
    ends={
        Property(name="DOM_Type205", type=DOM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodInvocation204", type=DOM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodBinding206: BinaryAssociation = BinaryAssociation(
    name="methodBinding206",
    ends={
        Property(name="DOM_IMethod208", type=DOM_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_MethodInvocation207", type=DOM_IMethod, multiplicity=Multiplicity(1, 1))
    }
)
expression209: BinaryAssociation = BinaryAssociation(
    name="expression209",
    ends={
        Property(name="DOM_Expression210", type=DOM_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ParenthesizedExpression", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand211: BinaryAssociation = BinaryAssociation(
    name="operand211",
    ends={
        Property(name="DOM_Expression212", type=DOM_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PostfixExpression", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand213: BinaryAssociation = BinaryAssociation(
    name="operand213",
    ends={
        Property(name="DOM_Expression214", type=DOM_PrefixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_PrefixExpression", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name222: BinaryAssociation = BinaryAssociation(
    name="name222",
    ends={
        Property(name="DOM_Name224", type=DOM_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperMethodInvocation223", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier225: BinaryAssociation = BinaryAssociation(
    name="qualifier225",
    ends={
        Property(name="DOM_Name227", type=DOM_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperMethodInvocation226", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name215: BinaryAssociation = BinaryAssociation(
    name="name215",
    ends={
        Property(name="DOM_SimpleName216", type=DOM_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperFieldAccess", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier217: BinaryAssociation = BinaryAssociation(
    name="qualifier217",
    ends={
        Property(name="DOM_Name219", type=DOM_SuperFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperFieldAccess218", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments220: BinaryAssociation = BinaryAssociation(
    name="arguments220",
    ends={
        Property(name="DOM_Expression221", type=DOM_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperMethodInvocation", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers237: BinaryAssociation = BinaryAssociation(
    name="modifiers237",
    ends={
        Property(name="DOM_ExtendedModifier239", type=DOM_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationExpression238", type=DOM_ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type240: BinaryAssociation = BinaryAssociation(
    name="type240",
    ends={
        Property(name="DOM_Type242", type=DOM_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationExpression241", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments228: BinaryAssociation = BinaryAssociation(
    name="typeArguments228",
    ends={
        Property(name="DOM_Type230", type=DOM_SuperMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperMethodInvocation229", type=DOM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier231: BinaryAssociation = BinaryAssociation(
    name="qualifier231",
    ends={
        Property(name="DOM_Name232", type=DOM_ThisExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ThisExpression", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type233: BinaryAssociation = BinaryAssociation(
    name="type233",
    ends={
        Property(name="DOM_Type234", type=DOM_TypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeLiteral", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments235: BinaryAssociation = BinaryAssociation(
    name="fragments235",
    ends={
        Property(name="DOM_VariableDeclarationFragment236", type=DOM_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationExpression", type=DOM_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label250: BinaryAssociation = BinaryAssociation(
    name="label250",
    ends={
        Property(name="DOM_BreakStatement", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="DOM_SimpleName251", type=DOM_BreakStatement, multiplicity=Multiplicity(1, 1))
    }
)
arguments252: BinaryAssociation = BinaryAssociation(
    name="arguments252",
    ends={
        Property(name="DOM_Expression253", type=DOM_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ConstructorInvocation", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression243: BinaryAssociation = BinaryAssociation(
    name="expression243",
    ends={
        Property(name="DOM_Expression244", type=DOM_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AssertStatement", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message245: BinaryAssociation = BinaryAssociation(
    name="message245",
    ends={
        Property(name="DOM_Expression247", type=DOM_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_AssertStatement246", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements248: BinaryAssociation = BinaryAssociation(
    name="statements248",
    ends={
        Property(name="DOM_Statement", type=DOM_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_Block249", type=DOM_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments254: BinaryAssociation = BinaryAssociation(
    name="typeArguments254",
    ends={
        Property(name="DOM_Type256", type=DOM_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ConstructorInvocation255", type=DOM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label257: BinaryAssociation = BinaryAssociation(
    name="label257",
    ends={
        Property(name="DOM_SimpleName258", type=DOM_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ContinueStatement", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body259: BinaryAssociation = BinaryAssociation(
    name="body259",
    ends={
        Property(name="DOM_Statement260", type=DOM_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_DoStatement", type=DOM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression261: BinaryAssociation = BinaryAssociation(
    name="expression261",
    ends={
        Property(name="DOM_Expression263", type=DOM_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_DoStatement262", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializers279: BinaryAssociation = BinaryAssociation(
    name="initializers279",
    ends={
        Property(name="DOM_Expression281", type=DOM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ForStatement280", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body264: BinaryAssociation = BinaryAssociation(
    name="body264",
    ends={
        Property(name="DOM_Statement265", type=DOM_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnhancedForStatement", type=DOM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression266: BinaryAssociation = BinaryAssociation(
    name="expression266",
    ends={
        Property(name="DOM_Expression268", type=DOM_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnhancedForStatement267", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter269: BinaryAssociation = BinaryAssociation(
    name="parameter269",
    ends={
        Property(name="DOM_SingleVariableDeclaration271", type=DOM_EnhancedForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_EnhancedForStatement270", type=DOM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression272: BinaryAssociation = BinaryAssociation(
    name="expression272",
    ends={
        Property(name="DOM_Expression273", type=DOM_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ExpressionStatement", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body274: BinaryAssociation = BinaryAssociation(
    name="body274",
    ends={
        Property(name="DOM_Statement275", type=DOM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ForStatement", type=DOM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression276: BinaryAssociation = BinaryAssociation(
    name="expression276",
    ends={
        Property(name="DOM_Expression278", type=DOM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ForStatement277", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body293: BinaryAssociation = BinaryAssociation(
    name="body293",
    ends={
        Property(name="DOM_Statement294", type=DOM_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_LabeledStatement", type=DOM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updaters282: BinaryAssociation = BinaryAssociation(
    name="updaters282",
    ends={
        Property(name="DOM_Expression284", type=DOM_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ForStatement283", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatement285: BinaryAssociation = BinaryAssociation(
    name="elseStatement285",
    ends={
        Property(name="DOM_Statement286", type=DOM_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_IfStatement", type=DOM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression287: BinaryAssociation = BinaryAssociation(
    name="expression287",
    ends={
        Property(name="DOM_Expression289", type=DOM_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_IfStatement288", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement290: BinaryAssociation = BinaryAssociation(
    name="thenStatement290",
    ends={
        Property(name="DOM_Statement292", type=DOM_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_IfStatement291", type=DOM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments305: BinaryAssociation = BinaryAssociation(
    name="typeArguments305",
    ends={
        Property(name="DOM_Type307", type=DOM_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperConstructorInvocation306", type=DOM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label295: BinaryAssociation = BinaryAssociation(
    name="label295",
    ends={
        Property(name="DOM_SimpleName297", type=DOM_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_LabeledStatement296", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression298: BinaryAssociation = BinaryAssociation(
    name="expression298",
    ends={
        Property(name="DOM_Expression299", type=DOM_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ReturnStatement", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments300: BinaryAssociation = BinaryAssociation(
    name="arguments300",
    ends={
        Property(name="DOM_Expression301", type=DOM_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperConstructorInvocation", type=DOM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression302: BinaryAssociation = BinaryAssociation(
    name="expression302",
    ends={
        Property(name="DOM_Expression304", type=DOM_SuperConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SuperConstructorInvocation303", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression317: BinaryAssociation = BinaryAssociation(
    name="expression317",
    ends={
        Property(name="DOM_Expression319", type=DOM_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SynchronizedStatement318", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression308: BinaryAssociation = BinaryAssociation(
    name="expression308",
    ends={
        Property(name="DOM_Expression309", type=DOM_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SwitchCase", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression310: BinaryAssociation = BinaryAssociation(
    name="expression310",
    ends={
        Property(name="DOM_Expression311", type=DOM_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SwitchStatement", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements312: BinaryAssociation = BinaryAssociation(
    name="statements312",
    ends={
        Property(name="DOM_Statement314", type=DOM_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SwitchStatement313", type=DOM_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments332: BinaryAssociation = BinaryAssociation(
    name="fragments332",
    ends={
        Property(name="DOM_VariableDeclarationFragment333", type=DOM_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationStatement", type=DOM_VariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body315: BinaryAssociation = BinaryAssociation(
    name="body315",
    ends={
        Property(name="DOM_Block316", type=DOM_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SynchronizedStatement", type=DOM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifiers334: BinaryAssociation = BinaryAssociation(
    name="modifiers334",
    ends={
        Property(name="DOM_ExtendedModifier336", type=DOM_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationStatement335", type=DOM_ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type337: BinaryAssociation = BinaryAssociation(
    name="type337",
    ends={
        Property(name="DOM_Type339", type=DOM_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_VariableDeclarationStatement338", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression320: BinaryAssociation = BinaryAssociation(
    name="expression320",
    ends={
        Property(name="DOM_Expression321", type=DOM_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ThrowStatement", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catchClauses322: BinaryAssociation = BinaryAssociation(
    name="catchClauses322",
    ends={
        Property(name="DOM_CatchClause323", type=DOM_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TryStatement", type=DOM_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body324: BinaryAssociation = BinaryAssociation(
    name="body324",
    ends={
        Property(name="DOM_Block326", type=DOM_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TryStatement325", type=DOM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finally327: BinaryAssociation = BinaryAssociation(
    name="finally327",
    ends={
        Property(name="DOM_Block329", type=DOM_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TryStatement328", type=DOM_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaration330: BinaryAssociation = BinaryAssociation(
    name="declaration330",
    ends={
        Property(name="DOM_AbstractTypeDeclaration331", type=DOM_TypeDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_TypeDeclarationStatement", type=DOM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type351: BinaryAssociation = BinaryAssociation(
    name="type351",
    ends={
        Property(name="DOM_Type352", type=DOM_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ParameterizedType", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments353: BinaryAssociation = BinaryAssociation(
    name="typeArguments353",
    ends={
        Property(name="DOM_Type355", type=DOM_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ParameterizedType354", type=DOM_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body340: BinaryAssociation = BinaryAssociation(
    name="body340",
    ends={
        Property(name="DOM_Statement341", type=DOM_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_WhileStatement", type=DOM_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression342: BinaryAssociation = BinaryAssociation(
    name="expression342",
    ends={
        Property(name="DOM_Expression344", type=DOM_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_WhileStatement343", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
componentType345: BinaryAssociation = BinaryAssociation(
    name="componentType345",
    ends={
        Property(name="DOM_Type347", type=DOM_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayType346", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType348: BinaryAssociation = BinaryAssociation(
    name="elementType348",
    ends={
        Property(name="DOM_Type350", type=DOM_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_ArrayType349", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name356: BinaryAssociation = BinaryAssociation(
    name="name356",
    ends={
        Property(name="DOM_SimpleName357", type=DOM_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_QualifiedType", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier358: BinaryAssociation = BinaryAssociation(
    name="qualifier358",
    ends={
        Property(name="DOM_Type360", type=DOM_QualifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_QualifiedType359", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name361: BinaryAssociation = BinaryAssociation(
    name="name361",
    ends={
        Property(name="DOM_Name362", type=DOM_SimpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SimpleType", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bound363: BinaryAssociation = BinaryAssociation(
    name="bound363",
    ends={
        Property(name="DOM_Type364", type=DOM_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_WildcardType", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values376: BinaryAssociation = BinaryAssociation(
    name="values376",
    ends={
        Property(name="DOM_MemberValuePair377", type=DOM_NormalAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_NormalAnnotation", type=DOM_MemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type365: BinaryAssociation = BinaryAssociation(
    name="type365",
    ends={
        Property(name="DOM_Type367", type=DOM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SingleVariableDeclaration366", type=DOM_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifiers368: BinaryAssociation = BinaryAssociation(
    name="modifiers368",
    ends={
        Property(name="DOM_ExtendedModifier370", type=DOM_SingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SingleVariableDeclaration369", type=DOM_ExtendedModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name371: BinaryAssociation = BinaryAssociation(
    name="name371",
    ends={
        Property(name="DOM_SimpleName372", type=DOM_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_QualifiedName", type=DOM_SimpleName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier373: BinaryAssociation = BinaryAssociation(
    name="qualifier373",
    ends={
        Property(name="DOM_Name375", type=DOM_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_QualifiedName374", type=DOM_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value378: BinaryAssociation = BinaryAssociation(
    name="value378",
    ends={
        Property(name="DOM_Expression379", type=DOM_SingleMemberAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="DOM_SingleMemberAnnotation", type=DOM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_DOM_AnonymousClassDeclaration_ASTNode = Generalization(general=ASTNode, specific=DOM_AnonymousClassDeclaration)
gen_DOM_BodyDeclaration_ASTNode = Generalization(general=ASTNode, specific=DOM_BodyDeclaration)
gen_DOM_CompilationUnit_ASTNode = Generalization(general=ASTNode, specific=DOM_CompilationUnit)
gen_DOM_CatchClause_ASTNode = Generalization(general=ASTNode, specific=DOM_CatchClause)
gen_DOM_Comment_ASTNode = Generalization(general=ASTNode, specific=DOM_Comment)
gen_DOM_MemberRef_ASTNode = Generalization(general=ASTNode, specific=DOM_MemberRef)
gen_DOM_MemberValuePair_ASTNode = Generalization(general=ASTNode, specific=DOM_MemberValuePair)
gen_DOM_Expression_ASTNode = Generalization(general=ASTNode, specific=DOM_Expression)
gen_DOM_ImportDeclaration_ASTNode = Generalization(general=ASTNode, specific=DOM_ImportDeclaration)
gen_DOM_MethodRefParameter_ASTNode = Generalization(general=ASTNode, specific=DOM_MethodRefParameter)
gen_DOM_MethodRef_ASTNode = Generalization(general=ASTNode, specific=DOM_MethodRef)
gen_DOM_PackageDeclaration_ASTNode = Generalization(general=ASTNode, specific=DOM_PackageDeclaration)
gen_DOM_Modifier_ASTNode = Generalization(general=ASTNode, specific=DOM_Modifier)
gen_DOM_Modifier_ExtendedModifier = Generalization(general=ExtendedModifier, specific=DOM_Modifier)
gen_DOM_TagElement_ASTNode = Generalization(general=ASTNode, specific=DOM_TagElement)
gen_DOM_TextElement_ASTNode = Generalization(general=ASTNode, specific=DOM_TextElement)
gen_DOM_Type_ASTNode = Generalization(general=ASTNode, specific=DOM_Type)
gen_DOM_TypeParameter_ASTNode = Generalization(general=ASTNode, specific=DOM_TypeParameter)
gen_DOM_Statement_ASTNode = Generalization(general=ASTNode, specific=DOM_Statement)
gen_DOM_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_AbstractTypeDeclaration)
gen_DOM_VariableDeclaration_ASTNode = Generalization(general=ASTNode, specific=DOM_VariableDeclaration)
gen_DOM_EnumConstantDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_EnumConstantDeclaration)
gen_DOM_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_FieldDeclaration)
gen_DOM_AnnotationTypeMemberDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_AnnotationTypeMemberDeclaration)
gen_DOM_MethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_MethodDeclaration)
gen_DOM_Initializer_BodyDeclaration = Generalization(general=BodyDeclaration, specific=DOM_Initializer)
gen_DOM_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=DOM_AnnotationTypeDeclaration)
gen_DOM_EnumDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=DOM_EnumDeclaration)
gen_DOM_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=DOM_TypeDeclaration)
gen_DOM_Javadoc_Comment = Generalization(general=Comment, specific=DOM_Javadoc)
gen_DOM_LineComment_Comment = Generalization(general=Comment, specific=DOM_LineComment)
gen_DOM_Annotation_Expression = Generalization(general=Expression, specific=DOM_Annotation)
gen_DOM_Annotation_ExtendedModifier = Generalization(general=ExtendedModifier, specific=DOM_Annotation)
gen_DOM_ArrayAccess_Expression = Generalization(general=Expression, specific=DOM_ArrayAccess)
gen_DOM_BlockComment_Comment = Generalization(general=Comment, specific=DOM_BlockComment)
gen_DOM_ArrayInitializer_Expression = Generalization(general=Expression, specific=DOM_ArrayInitializer)
gen_DOM_Assignment_Expression = Generalization(general=Expression, specific=DOM_Assignment)
gen_DOM_ArrayCreation_Expression = Generalization(general=Expression, specific=DOM_ArrayCreation)
gen_DOM_BooleanLiteral_Expression = Generalization(general=Expression, specific=DOM_BooleanLiteral)
gen_DOM_CastExpression_Expression = Generalization(general=Expression, specific=DOM_CastExpression)
gen_DOM_CharacterLiteral_Expression = Generalization(general=Expression, specific=DOM_CharacterLiteral)
gen_DOM_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=DOM_ClassInstanceCreation)
gen_DOM_FieldAccess_Expression = Generalization(general=Expression, specific=DOM_FieldAccess)
gen_DOM_InfixExpression_Expression = Generalization(general=Expression, specific=DOM_InfixExpression)
gen_DOM_ConditionalExpression_Expression = Generalization(general=Expression, specific=DOM_ConditionalExpression)
gen_DOM_MethodInvocation_Expression = Generalization(general=Expression, specific=DOM_MethodInvocation)
gen_DOM_InstanceofExpression_Expression = Generalization(general=Expression, specific=DOM_InstanceofExpression)
gen_DOM_NumberLiteral_Expression = Generalization(general=Expression, specific=DOM_NumberLiteral)
gen_DOM_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=DOM_ParenthesizedExpression)
gen_DOM_Name_Expression = Generalization(general=Expression, specific=DOM_Name)
gen_DOM_NullLiteral_Expression = Generalization(general=Expression, specific=DOM_NullLiteral)
gen_DOM_PostfixExpression_Expression = Generalization(general=Expression, specific=DOM_PostfixExpression)
gen_DOM_PrefixExpression_Expression = Generalization(general=Expression, specific=DOM_PrefixExpression)
gen_DOM_StringLiteral_Expression = Generalization(general=Expression, specific=DOM_StringLiteral)
gen_DOM_SuperFieldAccess_Expression = Generalization(general=Expression, specific=DOM_SuperFieldAccess)
gen_DOM_SuperMethodInvocation_Expression = Generalization(general=Expression, specific=DOM_SuperMethodInvocation)
gen_DOM_ThisExpression_Expression = Generalization(general=Expression, specific=DOM_ThisExpression)
gen_DOM_TypeLiteral_Expression = Generalization(general=Expression, specific=DOM_TypeLiteral)
gen_DOM_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=DOM_VariableDeclarationExpression)
gen_DOM_ConstructorInvocation_Statement = Generalization(general=Statement, specific=DOM_ConstructorInvocation)
gen_DOM_AssertStatement_Statement = Generalization(general=Statement, specific=DOM_AssertStatement)
gen_DOM_Block_Statement = Generalization(general=Statement, specific=DOM_Block)
gen_DOM_BreakStatement_Statement = Generalization(general=Statement, specific=DOM_BreakStatement)
gen_DOM_EmptyStatement_Statement = Generalization(general=Statement, specific=DOM_EmptyStatement)
gen_DOM_EnhancedForStatement_Statement = Generalization(general=Statement, specific=DOM_EnhancedForStatement)
gen_DOM_ContinueStatement_Statement = Generalization(general=Statement, specific=DOM_ContinueStatement)
gen_DOM_DoStatement_Statement = Generalization(general=Statement, specific=DOM_DoStatement)
gen_DOM_ExpressionStatement_Statement = Generalization(general=Statement, specific=DOM_ExpressionStatement)
gen_DOM_ForStatement_Statement = Generalization(general=Statement, specific=DOM_ForStatement)
gen_DOM_LabeledStatement_Statement = Generalization(general=Statement, specific=DOM_LabeledStatement)
gen_DOM_IfStatement_Statement = Generalization(general=Statement, specific=DOM_IfStatement)
gen_DOM_ReturnStatement_Statement = Generalization(general=Statement, specific=DOM_ReturnStatement)
gen_DOM_SuperConstructorInvocation_Statement = Generalization(general=Statement, specific=DOM_SuperConstructorInvocation)
gen_DOM_SwitchCase_Statement = Generalization(general=Statement, specific=DOM_SwitchCase)
gen_DOM_SwitchStatement_Statement = Generalization(general=Statement, specific=DOM_SwitchStatement)
gen_DOM_SynchronizedStatement_Statement = Generalization(general=Statement, specific=DOM_SynchronizedStatement)
gen_DOM_ThrowStatement_Statement = Generalization(general=Statement, specific=DOM_ThrowStatement)
gen_DOM_TryStatement_Statement = Generalization(general=Statement, specific=DOM_TryStatement)
gen_DOM_TypeDeclarationStatement_Statement = Generalization(general=Statement, specific=DOM_TypeDeclarationStatement)
gen_DOM_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=DOM_VariableDeclarationStatement)
gen_DOM_ParameterizedType_Type = Generalization(general=Type, specific=DOM_ParameterizedType)
gen_DOM_WhileStatement_Statement = Generalization(general=Statement, specific=DOM_WhileStatement)
gen_DOM_ArrayType_Type = Generalization(general=Type, specific=DOM_ArrayType)
gen_DOM_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=DOM_SingleVariableDeclaration)
gen_DOM_PrimitiveType_Type = Generalization(general=Type, specific=DOM_PrimitiveType)
gen_DOM_QualifiedType_Type = Generalization(general=Type, specific=DOM_QualifiedType)
gen_DOM_SimpleType_Type = Generalization(general=Type, specific=DOM_SimpleType)
gen_DOM_WildcardType_Type = Generalization(general=Type, specific=DOM_WildcardType)
gen_DOM_MarkerAnnotation_Annotation = Generalization(general=Annotation, specific=DOM_MarkerAnnotation)
gen_DOM_NormalAnnotation_Annotation = Generalization(general=Annotation, specific=DOM_NormalAnnotation)
gen_DOM_VariableDeclarationFragment_VariableDeclaration = Generalization(general=VariableDeclaration, specific=DOM_VariableDeclarationFragment)
gen_DOM_QualifiedName_Name = Generalization(general=Name, specific=DOM_QualifiedName)
gen_DOM_SimpleName_Name = Generalization(general=Name, specific=DOM_SimpleName)
gen_DOM_SingleMemberAnnotation_Annotation = Generalization(general=Annotation, specific=DOM_SingleMemberAnnotation)

# Domain Model
domain_model = DomainModel(
    name="DOM",
    types={DOM_AnonymousClassDeclaration, ASTNode, DOM_BodyDeclaration, DOM_ExtendedModifier, DOM_AST, DOM_ASTNode, DOM_CompilationUnit, DOM_PackageDeclaration, DOM_ImportDeclaration, DOM_Javadoc, DOM_AbstractTypeDeclaration, DOM_CatchClause, DOM_Block, DOM_SingleVariableDeclaration, DOM_Comment, DOM_Name, DOM_MemberRef, DOM_SimpleName, DOM_MemberValuePair, DOM_Expression, DOM_IType, DOM_MethodRefParameter, DOM_Type, DOM_MethodRef, DOM_Annotation, DOM_Modifier, ExtendedModifier, DOM_TagElement, DOM_TextElement, DOM_TypeParameter, DOM_IPackageFragment, DOM_Statement, BodyDeclaration, DOM_VariableDeclaration, DOM_EnumConstantDeclaration, DOM_FieldDeclaration, DOM_VariableDeclarationFragment, DOM_AnnotationTypeMemberDeclaration, DOM_MethodDeclaration, DOM_Initializer, DOM_AnnotationTypeDeclaration, AbstractTypeDeclaration, DOM_EnumDeclaration, DOM_TypeDeclaration, DOM_IMethod, DOM_LineComment, Expression, DOM_ArrayAccess, DOM_BlockComment, Comment, DOM_ArrayType, DOM_Assignment, DOM_ArrayCreation, DOM_ArrayInitializer, DOM_BooleanLiteral, DOM_CastExpression, DOM_CharacterLiteral, DOM_ClassInstanceCreation, DOM_FieldAccess, DOM_InfixExpression, DOM_ConditionalExpression, DOM_MethodInvocation, DOM_InstanceofExpression, DOM_NumberLiteral, DOM_ParenthesizedExpression, DOM_NullLiteral, DOM_PostfixExpression, DOM_PrefixExpression, DOM_StringLiteral, DOM_SuperFieldAccess, DOM_SuperMethodInvocation, DOM_ThisExpression, DOM_TypeLiteral, DOM_VariableDeclarationExpression, DOM_ConstructorInvocation, DOM_AssertStatement, Statement, DOM_BreakStatement, DOM_EnhancedForStatement, DOM_ContinueStatement, DOM_DoStatement, DOM_EmptyStatement, DOM_ExpressionStatement, DOM_ForStatement, DOM_LabeledStatement, DOM_IfStatement, DOM_ReturnStatement, DOM_SuperConstructorInvocation, DOM_SwitchCase, DOM_SwitchStatement, DOM_SynchronizedStatement, DOM_ThrowStatement, DOM_TryStatement, DOM_TypeDeclarationStatement, DOM_VariableDeclarationStatement, DOM_ParameterizedType, DOM_WhileStatement, Type, VariableDeclaration, DOM_PrimitiveType, DOM_QualifiedType, DOM_SimpleType, DOM_WildcardType, DOM_MarkerAnnotation, Annotation, DOM_NormalAnnotation, DOM_SingleMemberAnnotation, DOM_QualifiedName, Name, AssignmentOperatorKind, InfixExpressionOperatorKind, PrefixExpressionOperatorKind, PostfixExpressionOperatorKind},
    associations={bodyDeclarations1, modifiers2, compilationUnits0, alternateRoot9, comments11, package13, imports15, javadoc4, types17, body6, exception7, name20, name22, qualifier23, typeBinding19, qualifier33, parameters36, name38, type41, name26, value28, name31, annotations43, fragments53, javadoc45, name48, binding51, name62, bodyDeclarations65, name55, typeBounds57, initializer60, name68, arguments79, anonymousClassDeclaration81, name84, default71, name73, type76, body93, name95, returnType98, fragments87, type88, body91, binding110, superInterfaceTypes112, enumConstants114, parameters101, thrownExceptions104, typeParameters107, tags125, typeName128, superclassType117, superInterfaceTypes119, typeParameters122, initializer138, type140, expressions142, leftHandSide145, array131, index133, dimensions136, expression150, rightHandSide147, arguments155, anonymousClassDeclaration157, expression160, type163, typeArguments166, type152, expression177, name179, extendedOperands182, elseExpression169, expression171, thenExpression174, rightOperand192, leftOperand184, arguments195, rightOperand187, leftOperand190, expression197, name200, typeArguments203, methodBinding206, expression209, operand211, operand213, name222, qualifier225, name215, qualifier217, arguments220, modifiers237, type240, typeArguments228, qualifier231, type233, fragments235, label250, arguments252, expression243, message245, statements248, typeArguments254, label257, body259, expression261, initializers279, body264, expression266, parameter269, expression272, body274, expression276, body293, updaters282, elseStatement285, expression287, thenStatement290, typeArguments305, label295, expression298, arguments300, expression302, expression317, expression308, expression310, statements312, fragments332, body315, modifiers334, type337, expression320, catchClauses322, body324, finally327, declaration330, type351, typeArguments353, body340, expression342, componentType345, elementType348, name356, qualifier358, name361, bound363, values376, type365, modifiers368, name371, qualifier373, value378},
    generalizations={gen_DOM_AnonymousClassDeclaration_ASTNode, gen_DOM_BodyDeclaration_ASTNode, gen_DOM_CompilationUnit_ASTNode, gen_DOM_CatchClause_ASTNode, gen_DOM_Comment_ASTNode, gen_DOM_MemberRef_ASTNode, gen_DOM_MemberValuePair_ASTNode, gen_DOM_Expression_ASTNode, gen_DOM_ImportDeclaration_ASTNode, gen_DOM_MethodRefParameter_ASTNode, gen_DOM_MethodRef_ASTNode, gen_DOM_PackageDeclaration_ASTNode, gen_DOM_Modifier_ASTNode, gen_DOM_Modifier_ExtendedModifier, gen_DOM_TagElement_ASTNode, gen_DOM_TextElement_ASTNode, gen_DOM_Type_ASTNode, gen_DOM_TypeParameter_ASTNode, gen_DOM_Statement_ASTNode, gen_DOM_AbstractTypeDeclaration_BodyDeclaration, gen_DOM_VariableDeclaration_ASTNode, gen_DOM_EnumConstantDeclaration_BodyDeclaration, gen_DOM_FieldDeclaration_BodyDeclaration, gen_DOM_AnnotationTypeMemberDeclaration_BodyDeclaration, gen_DOM_MethodDeclaration_BodyDeclaration, gen_DOM_Initializer_BodyDeclaration, gen_DOM_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_DOM_EnumDeclaration_AbstractTypeDeclaration, gen_DOM_TypeDeclaration_AbstractTypeDeclaration, gen_DOM_Javadoc_Comment, gen_DOM_LineComment_Comment, gen_DOM_Annotation_Expression, gen_DOM_Annotation_ExtendedModifier, gen_DOM_ArrayAccess_Expression, gen_DOM_BlockComment_Comment, gen_DOM_ArrayInitializer_Expression, gen_DOM_Assignment_Expression, gen_DOM_ArrayCreation_Expression, gen_DOM_BooleanLiteral_Expression, gen_DOM_CastExpression_Expression, gen_DOM_CharacterLiteral_Expression, gen_DOM_ClassInstanceCreation_Expression, gen_DOM_FieldAccess_Expression, gen_DOM_InfixExpression_Expression, gen_DOM_ConditionalExpression_Expression, gen_DOM_MethodInvocation_Expression, gen_DOM_InstanceofExpression_Expression, gen_DOM_NumberLiteral_Expression, gen_DOM_ParenthesizedExpression_Expression, gen_DOM_Name_Expression, gen_DOM_NullLiteral_Expression, gen_DOM_PostfixExpression_Expression, gen_DOM_PrefixExpression_Expression, gen_DOM_StringLiteral_Expression, gen_DOM_SuperFieldAccess_Expression, gen_DOM_SuperMethodInvocation_Expression, gen_DOM_ThisExpression_Expression, gen_DOM_TypeLiteral_Expression, gen_DOM_VariableDeclarationExpression_Expression, gen_DOM_ConstructorInvocation_Statement, gen_DOM_AssertStatement_Statement, gen_DOM_Block_Statement, gen_DOM_BreakStatement_Statement, gen_DOM_EmptyStatement_Statement, gen_DOM_EnhancedForStatement_Statement, gen_DOM_ContinueStatement_Statement, gen_DOM_DoStatement_Statement, gen_DOM_ExpressionStatement_Statement, gen_DOM_ForStatement_Statement, gen_DOM_LabeledStatement_Statement, gen_DOM_IfStatement_Statement, gen_DOM_ReturnStatement_Statement, gen_DOM_SuperConstructorInvocation_Statement, gen_DOM_SwitchCase_Statement, gen_DOM_SwitchStatement_Statement, gen_DOM_SynchronizedStatement_Statement, gen_DOM_ThrowStatement_Statement, gen_DOM_TryStatement_Statement, gen_DOM_TypeDeclarationStatement_Statement, gen_DOM_VariableDeclarationStatement_Statement, gen_DOM_ParameterizedType_Type, gen_DOM_WhileStatement_Statement, gen_DOM_ArrayType_Type, gen_DOM_SingleVariableDeclaration_VariableDeclaration, gen_DOM_PrimitiveType_Type, gen_DOM_QualifiedType_Type, gen_DOM_SimpleType_Type, gen_DOM_WildcardType_Type, gen_DOM_MarkerAnnotation_Annotation, gen_DOM_NormalAnnotation_Annotation, gen_DOM_VariableDeclarationFragment_VariableDeclaration, gen_DOM_QualifiedName_Name, gen_DOM_SimpleName_Name, gen_DOM_SingleMemberAnnotation_Annotation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)