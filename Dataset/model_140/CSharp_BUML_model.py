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
cSharp_UsingDirective = Class(name="cSharp::UsingDirective")
cSharp_GlobalAttributes = Class(name="cSharp::GlobalAttributes")
cSharp_NamespaceMemberDeclaration = Class(name="cSharp::NamespaceMemberDeclaration")
cSharp_Identifier = Class(name="cSharp::Identifier")
cSharp_QualifiedIdentifier = Class(name="cSharp::QualifiedIdentifier")
cSharp_CompilationUnit = Class(name="cSharp::CompilationUnit")
cSharp_Attributes = Class(name="cSharp::Attributes")
cSharp_AttributeSection = Class(name="cSharp::AttributeSection")
AttributeSection = Class(name="AttributeSection")
cSharp_Attribute = Class(name="cSharp::Attribute")
cSharp_AttributeName = Class(name="cSharp::AttributeName")
cSharp_ArrayType = Class(name="cSharp::ArrayType")
cSharp_GlobalAttributeSection = Class(name="cSharp::GlobalAttributeSection")
cSharp_AttributeList = Class(name="cSharp::AttributeList")
cSharp_ExpressionList = Class(name="cSharp::ExpressionList")
cSharp_Expression = Class(name="cSharp::Expression")
VariableInitializer = Class(name="VariableInitializer")
Argument = Class(name="Argument")
ResourceAquisition = Class(name="ResourceAquisition")
cSharp_UnaryExpression = Class(name="cSharp::UnaryExpression")
cSharp_Expression2 = Class(name="cSharp::Expression2")
cSharp_AttributeArguments = Class(name="cSharp::AttributeArguments")
cSharp_BuiltInType = Class(name="cSharp::BuiltInType")
cSharp_ArrayInitializer = Class(name="cSharp::ArrayInitializer")
cSharp_ArgumentList = Class(name="cSharp::ArgumentList")
cSharp_TypeOrVoid = Class(name="cSharp::TypeOrVoid")
cSharp_PrimaryExpression2 = Class(name="cSharp::PrimaryExpression2")
cSharp_Type = Class(name="cSharp::Type")
cSharp_PrimaryExpression = Class(name="cSharp::PrimaryExpression")
cSharp_NonArrayType = Class(name="cSharp::NonArrayType")
cSharp_VariableInitializer = Class(name="cSharp::VariableInitializer")
EventDeclaration = Class(name="EventDeclaration")
PropertyDeclaration = Class(name="PropertyDeclaration")
FieldDeclaration = Class(name="FieldDeclaration")
ConstantDeclaration = Class(name="ConstantDeclaration")
cSharp_VariableDeclarator = Class(name="cSharp::VariableDeclarator")
cSharp_ConstantDeclarator = Class(name="cSharp::ConstantDeclarator")
cSharp_IntegralType = Class(name="cSharp::IntegralType")
BuiltInType = Class(name="BuiltInType")
ArrayType = Class(name="ArrayType")
cSharp_BuiltInClassType = Class(name="cSharp::BuiltInClassType")
ClassBase = Class(name="ClassBase")
cSharp_QualifiedIdentifierList = Class(name="cSharp::QualifiedIdentifierList")
cSharp_EventAccessorDeclarations = Class(name="cSharp::EventAccessorDeclarations")
cSharp_AccessorDeclarations = Class(name="cSharp::AccessorDeclarations")
cSharp_ClassDeclaration = Class(name="cSharp::ClassDeclaration")
cSharp_InterfaceDeclaration = Class(name="cSharp::InterfaceDeclaration")
cSharp_EnumDeclaration = Class(name="cSharp::EnumDeclaration")
cSharp_DelegateDeclaration = Class(name="cSharp::DelegateDeclaration")
cSharp_EnumBody = Class(name="cSharp::EnumBody")
cSharp_NamespaceDeclaration = Class(name="cSharp::NamespaceDeclaration")
cSharp_TypeDeclaration = Class(name="cSharp::TypeDeclaration")
cSharp_NamespaceBody = Class(name="cSharp::NamespaceBody")
cSharp_InterfaceBody = Class(name="cSharp::InterfaceBody")
cSharp_InterfaceMemberDeclaration = Class(name="cSharp::InterfaceMemberDeclaration")
cSharp_InterfaceMethodDeclaration = Class(name="cSharp::InterfaceMethodDeclaration")
cSharp_InterfaceEventDeclaration = Class(name="cSharp::InterfaceEventDeclaration")
cSharp_InterfaceIndexerDeclaration = Class(name="cSharp::InterfaceIndexerDeclaration")
cSharp_InterfacePropertyDeclaration = Class(name="cSharp::InterfacePropertyDeclaration")
cSharp_EnumMemberDeclaration = Class(name="cSharp::EnumMemberDeclaration")
cSharp_FormalParameterList = Class(name="cSharp::FormalParameterList")
cSharp_InterfaceAccessors = Class(name="cSharp::InterfaceAccessors")
cSharp_FieldDeclaration = Class(name="cSharp::FieldDeclaration")
cSharp_MethodDeclaration = Class(name="cSharp::MethodDeclaration")
cSharp_ConstantDeclaration = Class(name="cSharp::ConstantDeclaration")
cSharp_PropertyDeclaration = Class(name="cSharp::PropertyDeclaration")
cSharp_EventDeclaration = Class(name="cSharp::EventDeclaration")
cSharp_IndexerDeclaration = Class(name="cSharp::IndexerDeclaration")
cSharp_OperatorDeclaration = Class(name="cSharp::OperatorDeclaration")
cSharp_ConstructorDeclaration = Class(name="cSharp::ConstructorDeclaration")
cSharp_DestructorDeclaration = Class(name="cSharp::DestructorDeclaration")
cSharp_ClassBase = Class(name="cSharp::ClassBase")
cSharp_ClassBody = Class(name="cSharp::ClassBody")
cSharp_ClassMemberDeclaration = Class(name="cSharp::ClassMemberDeclaration")
cSharp_ConstructorDeclarator = Class(name="cSharp::ConstructorDeclarator")
cSharp_ConstructorInitializer = Class(name="cSharp::ConstructorInitializer")
ConstructorInitializer = Class(name="ConstructorInitializer")
cSharp_Argument = Class(name="cSharp::Argument")
cSharp_StaticConstructorDeclaration = Class(name="cSharp::StaticConstructorDeclaration")
cSharp_MaybeEmptyBlock = Class(name="cSharp::MaybeEmptyBlock")
cSharp_ConversionOperatorDeclarator = Class(name="cSharp::ConversionOperatorDeclarator")
OperatorDeclarator = Class(name="OperatorDeclarator")
cSharp_BinaryOperatorDeclarator = Class(name="cSharp::BinaryOperatorDeclarator")
cSharp_UnaryOperatorDeclarator = Class(name="cSharp::UnaryOperatorDeclarator")
cSharp_OperatorDeclarator = Class(name="cSharp::OperatorDeclarator")
cSharp_IndexerDeclarator = Class(name="cSharp::IndexerDeclarator")
cSharp_RemoveAccessorDeclaration = Class(name="cSharp::RemoveAccessorDeclaration")
cSharp_GetAccessorDeclaration = Class(name="cSharp::GetAccessorDeclaration")
cSharp_SetAccessorDeclaration = Class(name="cSharp::SetAccessorDeclaration")
cSharp_MethodHeader = Class(name="cSharp::MethodHeader")
cSharp_AddAccessorDeclaration = Class(name="cSharp::AddAccessorDeclaration")
cSharp_ParameterArray = Class(name="cSharp::ParameterArray")
cSharp_FixedParameters = Class(name="cSharp::FixedParameters")
FormalParameterList = Class(name="FormalParameterList")
cSharp_FixedParameter = Class(name="cSharp::FixedParameter")
DelegateDeclaration = Class(name="DelegateDeclaration")
cSharp_Statement = Class(name="cSharp::Statement")
cSharp_LabeledStatement = Class(name="cSharp::LabeledStatement")
cSharp_DeclarationStatment = Class(name="cSharp::DeclarationStatment")
cSharp_EmbeddedStatement = Class(name="cSharp::EmbeddedStatement")
cSharp_LocalVariableDeclaration = Class(name="cSharp::LocalVariableDeclaration")
cSharp_LocalconstantDeclaration = Class(name="cSharp::LocalconstantDeclaration")
cSharp_StatementExpression = Class(name="cSharp::StatementExpression")
cSharp_SelectionStatement = Class(name="cSharp::SelectionStatement")
cSharp_ResourceAquisition = Class(name="cSharp::ResourceAquisition")
cSharp_IterationStatement = Class(name="cSharp::IterationStatement")
cSharp_JumpStatement = Class(name="cSharp::JumpStatement")
cSharp_CatchClauses = Class(name="cSharp::CatchClauses")
cSharp_FinallyClause = Class(name="cSharp::FinallyClause")
cSharp_TryStatement = Class(name="cSharp::TryStatement")
cSharp_Block = Class(name="cSharp::Block")
cSharp_LockStatement = Class(name="cSharp::LockStatement")
cSharp_UsingStatement = Class(name="cSharp::UsingStatement")
cSharp_BreakStatement = Class(name="cSharp::BreakStatement")
cSharp_ContinueStatement = Class(name="cSharp::ContinueStatement")
cSharp_GotoStatement = Class(name="cSharp::GotoStatement")
cSharp_ReturnStatement = Class(name="cSharp::ReturnStatement")
cSharp_ThrowStatement = Class(name="cSharp::ThrowStatement")
cSharp_SpecificCatchClause = Class(name="cSharp::SpecificCatchClause")
cSharp_GeneralCatchclause = Class(name="cSharp::GeneralCatchclause")
cSharp_WhileStatement = Class(name="cSharp::WhileStatement")
cSharp_DoStatement = Class(name="cSharp::DoStatement")
cSharp_ForStatement = Class(name="cSharp::ForStatement")
cSharp_ForeachStatement = Class(name="cSharp::ForeachStatement")
cSharp_ForInitializer = Class(name="cSharp::ForInitializer")
cSharp_StatementExpressionList = Class(name="cSharp::StatementExpressionList")
cSharp_IfStatement = Class(name="cSharp::IfStatement")
cSharp_SwitchStatement = Class(name="cSharp::SwitchStatement")
cSharp_SwitchSection = Class(name="cSharp::SwitchSection")
cSharp_SwitchLabel = Class(name="cSharp::SwitchLabel")
cSharp_ElsePart = Class(name="cSharp::ElsePart")
RemoveAccessorDeclaration = Class(name="RemoveAccessorDeclaration")
AddAccessorDeclaration = Class(name="AddAccessorDeclaration")
MaybeEmptyBlock = Class(name="MaybeEmptyBlock")
SetAccessorDeclaration = Class(name="SetAccessorDeclaration")
GetAccessorDeclaration = Class(name="GetAccessorDeclaration")
cSharp_SByte = Class(name="cSharp::SByte")
IntegralType = Class(name="IntegralType")
cSharp_Byte = Class(name="cSharp::Byte")
cSharp_Double = Class(name="cSharp::Double")
cSharp_Object = Class(name="cSharp::Object")
BuiltInClassType = Class(name="BuiltInClassType")
cSharp_String = Class(name="cSharp::String")
cSharp_Void = Class(name="cSharp::Void")
TypeOrVoid = Class(name="TypeOrVoid")
cSharp_Short = Class(name="cSharp::Short")
cSharp_UShort = Class(name="cSharp::UShort")
cSharp_Int = Class(name="cSharp::Int")
cSharp_UInt = Class(name="cSharp::UInt")
cSharp_Long = Class(name="cSharp::Long")
cSharp_ULong = Class(name="cSharp::ULong")
cSharp_Char = Class(name="cSharp::Char")
cSharp_Bool = Class(name="cSharp::Bool")
cSharp_Decimal = Class(name="cSharp::Decimal")
cSharp_Float = Class(name="cSharp::Float")

# cSharp_UsingDirective class attributes and methods

# cSharp_GlobalAttributes class attributes and methods

# cSharp_NamespaceMemberDeclaration class attributes and methods

# cSharp_Identifier class attributes and methods

# cSharp_QualifiedIdentifier class attributes and methods

# cSharp_CompilationUnit class attributes and methods

# cSharp_Attributes class attributes and methods

# cSharp_AttributeSection class attributes and methods

# AttributeSection class attributes and methods

# cSharp_Attribute class attributes and methods

# cSharp_AttributeName class attributes and methods

# cSharp_ArrayType class attributes and methods

# cSharp_GlobalAttributeSection class attributes and methods

# cSharp_AttributeList class attributes and methods

# cSharp_ExpressionList class attributes and methods

# cSharp_Expression class attributes and methods

# VariableInitializer class attributes and methods

# Argument class attributes and methods

# ResourceAquisition class attributes and methods

# cSharp_UnaryExpression class attributes and methods
cSharp_UnaryExpression_expUnaryOperator: Property = Property(name="expUnaryOperator", type=StringType)
cSharp_UnaryExpression.attributes={cSharp_UnaryExpression_expUnaryOperator}

# cSharp_Expression2 class attributes and methods

# cSharp_AttributeArguments class attributes and methods

# cSharp_BuiltInType class attributes and methods

# cSharp_ArrayInitializer class attributes and methods

# cSharp_ArgumentList class attributes and methods

# cSharp_TypeOrVoid class attributes and methods

# cSharp_PrimaryExpression2 class attributes and methods
cSharp_PrimaryExpression2_incrementeDecrement: Property = Property(name="incrementeDecrement", type=StringType)
cSharp_PrimaryExpression2.attributes={cSharp_PrimaryExpression2_incrementeDecrement}

# cSharp_Type class attributes and methods

# cSharp_PrimaryExpression class attributes and methods
cSharp_PrimaryExpression_rankSpecifier: Property = Property(name="rankSpecifier", type=StringType)
cSharp_PrimaryExpression_literal: Property = Property(name="literal", type=StringType)
cSharp_PrimaryExpression_predefinedType: Property = Property(name="predefinedType", type=StringType)
cSharp_PrimaryExpression.attributes={cSharp_PrimaryExpression_literal, cSharp_PrimaryExpression_rankSpecifier, cSharp_PrimaryExpression_predefinedType}

# cSharp_NonArrayType class attributes and methods

# cSharp_VariableInitializer class attributes and methods

# EventDeclaration class attributes and methods

# PropertyDeclaration class attributes and methods

# FieldDeclaration class attributes and methods

# ConstantDeclaration class attributes and methods

# cSharp_VariableDeclarator class attributes and methods

# cSharp_ConstantDeclarator class attributes and methods

# cSharp_IntegralType class attributes and methods

# BuiltInType class attributes and methods

# ArrayType class attributes and methods

# cSharp_BuiltInClassType class attributes and methods

# ClassBase class attributes and methods

# cSharp_QualifiedIdentifierList class attributes and methods

# cSharp_EventAccessorDeclarations class attributes and methods

# cSharp_AccessorDeclarations class attributes and methods

# cSharp_ClassDeclaration class attributes and methods
cSharp_ClassDeclaration_classModifier: Property = Property(name="classModifier", type=StringType)
cSharp_ClassDeclaration.attributes={cSharp_ClassDeclaration_classModifier}

# cSharp_InterfaceDeclaration class attributes and methods

# cSharp_EnumDeclaration class attributes and methods

# cSharp_DelegateDeclaration class attributes and methods

# cSharp_EnumBody class attributes and methods

# cSharp_NamespaceDeclaration class attributes and methods

# cSharp_TypeDeclaration class attributes and methods

# cSharp_NamespaceBody class attributes and methods

# cSharp_InterfaceBody class attributes and methods

# cSharp_InterfaceMemberDeclaration class attributes and methods

# cSharp_InterfaceMethodDeclaration class attributes and methods

# cSharp_InterfaceEventDeclaration class attributes and methods

# cSharp_InterfaceIndexerDeclaration class attributes and methods

# cSharp_InterfacePropertyDeclaration class attributes and methods

# cSharp_EnumMemberDeclaration class attributes and methods

# cSharp_FormalParameterList class attributes and methods

# cSharp_InterfaceAccessors class attributes and methods

# cSharp_FieldDeclaration class attributes and methods

# cSharp_MethodDeclaration class attributes and methods

# cSharp_ConstantDeclaration class attributes and methods

# cSharp_PropertyDeclaration class attributes and methods

# cSharp_EventDeclaration class attributes and methods

# cSharp_IndexerDeclaration class attributes and methods
cSharp_IndexerDeclaration_idModifier: Property = Property(name="idModifier", type=StringType)
cSharp_IndexerDeclaration.attributes={cSharp_IndexerDeclaration_idModifier}

# cSharp_OperatorDeclaration class attributes and methods
cSharp_OperatorDeclaration_opModifier: Property = Property(name="opModifier", type=StringType)
cSharp_OperatorDeclaration.attributes={cSharp_OperatorDeclaration_opModifier}

# cSharp_ConstructorDeclaration class attributes and methods
cSharp_ConstructorDeclaration_constModifier: Property = Property(name="constModifier", type=StringType)
cSharp_ConstructorDeclaration.attributes={cSharp_ConstructorDeclaration_constModifier}

# cSharp_DestructorDeclaration class attributes and methods

# cSharp_ClassBase class attributes and methods

# cSharp_ClassBody class attributes and methods

# cSharp_ClassMemberDeclaration class attributes and methods

# cSharp_ConstructorDeclarator class attributes and methods

# cSharp_ConstructorInitializer class attributes and methods

# ConstructorInitializer class attributes and methods

# cSharp_Argument class attributes and methods

# cSharp_StaticConstructorDeclaration class attributes and methods
cSharp_StaticConstructorDeclaration_staticCosntModifier: Property = Property(name="staticCosntModifier", type=StringType)
cSharp_StaticConstructorDeclaration.attributes={cSharp_StaticConstructorDeclaration_staticCosntModifier}

# cSharp_MaybeEmptyBlock class attributes and methods

# cSharp_ConversionOperatorDeclarator class attributes and methods

# OperatorDeclarator class attributes and methods

# cSharp_BinaryOperatorDeclarator class attributes and methods
cSharp_BinaryOperatorDeclarator_overBinOperator: Property = Property(name="overBinOperator", type=StringType)
cSharp_BinaryOperatorDeclarator.attributes={cSharp_BinaryOperatorDeclarator_overBinOperator}

# cSharp_UnaryOperatorDeclarator class attributes and methods

# cSharp_OperatorDeclarator class attributes and methods

# cSharp_IndexerDeclarator class attributes and methods

# cSharp_RemoveAccessorDeclaration class attributes and methods

# cSharp_GetAccessorDeclaration class attributes and methods

# cSharp_SetAccessorDeclaration class attributes and methods

# cSharp_MethodHeader class attributes and methods
cSharp_MethodHeader_modifier: Property = Property(name="modifier", type=StringType)
cSharp_MethodHeader.attributes={cSharp_MethodHeader_modifier}

# cSharp_AddAccessorDeclaration class attributes and methods

# cSharp_ParameterArray class attributes and methods

# cSharp_FixedParameters class attributes and methods

# FormalParameterList class attributes and methods

# cSharp_FixedParameter class attributes and methods

# DelegateDeclaration class attributes and methods

# cSharp_Statement class attributes and methods

# cSharp_LabeledStatement class attributes and methods

# cSharp_DeclarationStatment class attributes and methods

# cSharp_EmbeddedStatement class attributes and methods

# cSharp_LocalVariableDeclaration class attributes and methods

# cSharp_LocalconstantDeclaration class attributes and methods

# cSharp_StatementExpression class attributes and methods
cSharp_StatementExpression_incrimentDecrement: Property = Property(name="incrimentDecrement", type=StringType)
cSharp_StatementExpression_assignementOperator: Property = Property(name="assignementOperator", type=StringType)
cSharp_StatementExpression.attributes={cSharp_StatementExpression_assignementOperator, cSharp_StatementExpression_incrimentDecrement}

# cSharp_SelectionStatement class attributes and methods

# cSharp_ResourceAquisition class attributes and methods

# cSharp_IterationStatement class attributes and methods

# cSharp_JumpStatement class attributes and methods

# cSharp_CatchClauses class attributes and methods

# cSharp_FinallyClause class attributes and methods

# cSharp_TryStatement class attributes and methods

# cSharp_Block class attributes and methods

# cSharp_LockStatement class attributes and methods

# cSharp_UsingStatement class attributes and methods

# cSharp_BreakStatement class attributes and methods

# cSharp_ContinueStatement class attributes and methods

# cSharp_GotoStatement class attributes and methods

# cSharp_ReturnStatement class attributes and methods

# cSharp_ThrowStatement class attributes and methods

# cSharp_SpecificCatchClause class attributes and methods

# cSharp_GeneralCatchclause class attributes and methods

# cSharp_WhileStatement class attributes and methods

# cSharp_DoStatement class attributes and methods

# cSharp_ForStatement class attributes and methods

# cSharp_ForeachStatement class attributes and methods

# cSharp_ForInitializer class attributes and methods

# cSharp_StatementExpressionList class attributes and methods

# cSharp_IfStatement class attributes and methods

# cSharp_SwitchStatement class attributes and methods

# cSharp_SwitchSection class attributes and methods

# cSharp_SwitchLabel class attributes and methods

# cSharp_ElsePart class attributes and methods

# RemoveAccessorDeclaration class attributes and methods

# AddAccessorDeclaration class attributes and methods

# MaybeEmptyBlock class attributes and methods

# SetAccessorDeclaration class attributes and methods

# GetAccessorDeclaration class attributes and methods

# cSharp_SByte class attributes and methods

# IntegralType class attributes and methods

# cSharp_Byte class attributes and methods

# cSharp_Double class attributes and methods

# cSharp_Object class attributes and methods

# BuiltInClassType class attributes and methods

# cSharp_String class attributes and methods

# cSharp_Void class attributes and methods

# TypeOrVoid class attributes and methods

# cSharp_Short class attributes and methods

# cSharp_UShort class attributes and methods

# cSharp_Int class attributes and methods

# cSharp_UInt class attributes and methods

# cSharp_Long class attributes and methods

# cSharp_ULong class attributes and methods

# cSharp_Char class attributes and methods

# cSharp_Bool class attributes and methods

# cSharp_Decimal class attributes and methods

# cSharp_Float class attributes and methods

# Relationships
usingDirectives0: BinaryAssociation = BinaryAssociation(
    name="usingDirectives0",
    ends={
        Property(name="cSharp_UsingDirective", type=cSharp_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_CompilationUnit", type=cSharp_UsingDirective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalAtt1: BinaryAssociation = BinaryAssociation(
    name="globalAtt1",
    ends={
        Property(name="cSharp_GlobalAttributes", type=cSharp_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_CompilationUnit2", type=cSharp_GlobalAttributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameSpaces3: BinaryAssociation = BinaryAssociation(
    name="nameSpaces3",
    ends={
        Property(name="cSharp_NamespaceMemberDeclaration", type=cSharp_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_CompilationUnit4", type=cSharp_NamespaceMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name5: BinaryAssociation = BinaryAssociation(
    name="name5",
    ends={
        Property(name="cSharp_Identifier", type=cSharp_UsingDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_UsingDirective6", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes11: BinaryAssociation = BinaryAssociation(
    name="attributes11",
    ends={
        Property(name="cSharp_GlobalAttributeSection12", type=cSharp_AttributeList, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="cSharp_AttributeList", type=cSharp_GlobalAttributeSection, multiplicity=Multiplicity(1, 1))
    }
)
attributes13: BinaryAssociation = BinaryAssociation(
    name="attributes13",
    ends={
        Property(name="cSharp_AttributeSection", type=cSharp_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Attributes", type=cSharp_AttributeSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute14: BinaryAssociation = BinaryAssociation(
    name="attribute14",
    ends={
        Property(name="cSharp_Attribute", type=cSharp_AttributeList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_AttributeList15", type=cSharp_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes16: BinaryAssociation = BinaryAssociation(
    name="attributes16",
    ends={
        Property(name="cSharp_Attribute18", type=cSharp_AttributeList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_AttributeList17", type=cSharp_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name19: BinaryAssociation = BinaryAssociation(
    name="name19",
    ends={
        Property(name="cSharp_AttributeName", type=cSharp_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Attribute20", type=cSharp_AttributeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usings7: BinaryAssociation = BinaryAssociation(
    name="usings7",
    ends={
        Property(name="cSharp_QualifiedIdentifier", type=cSharp_UsingDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_UsingDirective8", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
globalAttSections9: BinaryAssociation = BinaryAssociation(
    name="globalAttSections9",
    ends={
        Property(name="cSharp_GlobalAttributeSection", type=cSharp_GlobalAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_GlobalAttributes10", type=cSharp_GlobalAttributeSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expresionList23: BinaryAssociation = BinaryAssociation(
    name="expresionList23",
    ends={
        Property(name="cSharp_ExpressionList", type=cSharp_AttributeArguments, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_AttributeArguments24", type=cSharp_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression25: BinaryAssociation = BinaryAssociation(
    name="expression25",
    ends={
        Property(name="cSharp_Expression", type=cSharp_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ExpressionList26", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions27: BinaryAssociation = BinaryAssociation(
    name="expressions27",
    ends={
        Property(name="cSharp_Expression29", type=cSharp_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ExpressionList28", type=cSharp_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unary30: BinaryAssociation = BinaryAssociation(
    name="unary30",
    ends={
        Property(name="cSharp_UnaryExpression", type=cSharp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression31", type=cSharp_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp33: BinaryAssociation = BinaryAssociation(
    name="exp33",
    ends={
        Property(name="cSharp_Expression34", type=cSharp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression32", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp235: BinaryAssociation = BinaryAssociation(
    name="exp235",
    ends={
        Property(name="cSharp_Expression2", type=cSharp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression36", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interExp37: BinaryAssociation = BinaryAssociation(
    name="interExp37",
    ends={
        Property(name="cSharp_Expression39", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression238", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interExp241: BinaryAssociation = BinaryAssociation(
    name="interExp241",
    ends={
        Property(name="cSharp_Expression242", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression240", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pipelineExp43: BinaryAssociation = BinaryAssociation(
    name="pipelineExp43",
    ends={
        Property(name="cSharp_Expression45", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression244", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pipelineExp247: BinaryAssociation = BinaryAssociation(
    name="pipelineExp247",
    ends={
        Property(name="cSharp_Expression248", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression246", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attArguments21: BinaryAssociation = BinaryAssociation(
    name="attArguments21",
    ends={
        Property(name="cSharp_AttributeArguments", type=cSharp_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Attribute22", type=cSharp_AttributeArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equalityExp73: BinaryAssociation = BinaryAssociation(
    name="equalityExp73",
    ends={
        Property(name="cSharp_Expression75", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression274", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equalityExp277: BinaryAssociation = BinaryAssociation(
    name="equalityExp277",
    ends={
        Property(name="cSharp_Expression278", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression276", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relopExp79: BinaryAssociation = BinaryAssociation(
    name="relopExp79",
    ends={
        Property(name="cSharp_Expression81", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression280", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relopExp283: BinaryAssociation = BinaryAssociation(
    name="relopExp283",
    ends={
        Property(name="cSharp_Expression284", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression282", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buildInType85: BinaryAssociation = BinaryAssociation(
    name="buildInType85",
    ends={
        Property(name="cSharp_BuiltInType", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression286", type=cSharp_BuiltInType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shiftExp87: BinaryAssociation = BinaryAssociation(
    name="shiftExp87",
    ends={
        Property(name="cSharp_Expression89", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression288", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shiftExp291: BinaryAssociation = BinaryAssociation(
    name="shiftExp291",
    ends={
        Property(name="cSharp_Expression292", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression290", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operatorExp93: BinaryAssociation = BinaryAssociation(
    name="operatorExp93",
    ends={
        Property(name="cSharp_Expression95", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression294", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operatorExp297: BinaryAssociation = BinaryAssociation(
    name="operatorExp297",
    ends={
        Property(name="cSharp_Expression298", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression296", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multipExp99: BinaryAssociation = BinaryAssociation(
    name="multipExp99",
    ends={
        Property(name="cSharp_Expression101", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression2100", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multipExp2103: BinaryAssociation = BinaryAssociation(
    name="multipExp2103",
    ends={
        Property(name="cSharp_Expression2104", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression2102", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
divExp105: BinaryAssociation = BinaryAssociation(
    name="divExp105",
    ends={
        Property(name="cSharp_Expression107", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression2106", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inExp49: BinaryAssociation = BinaryAssociation(
    name="inExp49",
    ends={
        Property(name="cSharp_Expression51", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression250", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
divExp2109: BinaryAssociation = BinaryAssociation(
    name="divExp2109",
    ends={
        Property(name="cSharp_Expression2110", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression2108", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inExp253: BinaryAssociation = BinaryAssociation(
    name="inExp253",
    ends={
        Property(name="cSharp_Expression254", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression252", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
barExp55: BinaryAssociation = BinaryAssociation(
    name="barExp55",
    ends={
        Property(name="cSharp_Expression57", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression256", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
barExp259: BinaryAssociation = BinaryAssociation(
    name="barExp259",
    ends={
        Property(name="cSharp_Expression260", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression258", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp61: BinaryAssociation = BinaryAssociation(
    name="exp61",
    ends={
        Property(name="cSharp_Expression63", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression262", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp265: BinaryAssociation = BinaryAssociation(
    name="exp265",
    ends={
        Property(name="cSharp_Expression266", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression264", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ampExp67: BinaryAssociation = BinaryAssociation(
    name="ampExp67",
    ends={
        Property(name="cSharp_Expression69", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression268", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ampExp271: BinaryAssociation = BinaryAssociation(
    name="ampExp271",
    ends={
        Property(name="cSharp_Expression272", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression270", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nonArrayType124: BinaryAssociation = BinaryAssociation(
    name="nonArrayType124",
    ends={
        Property(name="cSharp_NonArrayType", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression125", type=cSharp_NonArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList126: BinaryAssociation = BinaryAssociation(
    name="expressionList126",
    ends={
        Property(name="cSharp_ExpressionList128", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression127", type=cSharp_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayInitializer129: BinaryAssociation = BinaryAssociation(
    name="arrayInitializer129",
    ends={
        Property(name="cSharp_ArrayInitializer", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression130", type=cSharp_ArrayInitializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayType131: BinaryAssociation = BinaryAssociation(
    name="arrayType131",
    ends={
        Property(name="cSharp_ArrayType", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression132", type=cSharp_ArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayInitializer2133: BinaryAssociation = BinaryAssociation(
    name="arrayInitializer2133",
    ends={
        Property(name="cSharp_ArrayInitializer135", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression134", type=cSharp_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipo136: BinaryAssociation = BinaryAssociation(
    name="tipo136",
    ends={
        Property(name="cSharp_Type138", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression137", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argumentList139: BinaryAssociation = BinaryAssociation(
    name="argumentList139",
    ends={
        Property(name="cSharp_ArgumentList", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression140", type=cSharp_ArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id141: BinaryAssociation = BinaryAssociation(
    name="id141",
    ends={
        Property(name="cSharp_Identifier143", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression142", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression144: BinaryAssociation = BinaryAssociation(
    name="expression144",
    ends={
        Property(name="cSharp_Expression146", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression145", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeOrVoid147: BinaryAssociation = BinaryAssociation(
    name="typeOrVoid147",
    ends={
        Property(name="cSharp_TypeOrVoid", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression148", type=cSharp_TypeOrVoid, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExoression2149: BinaryAssociation = BinaryAssociation(
    name="primaryExoression2149",
    ends={
        Property(name="cSharp_PrimaryExpression2", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression150", type=cSharp_PrimaryExpression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modExp111: BinaryAssociation = BinaryAssociation(
    name="modExp111",
    ends={
        Property(name="cSharp_Expression113", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression2112", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modExp2115: BinaryAssociation = BinaryAssociation(
    name="modExp2115",
    ends={
        Property(name="cSharp_Expression2116", type=cSharp_Expression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Expression2114", type=cSharp_Expression2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type117: BinaryAssociation = BinaryAssociation(
    name="type117",
    ends={
        Property(name="cSharp_Type", type=cSharp_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_UnaryExpression118", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExp120: BinaryAssociation = BinaryAssociation(
    name="unaryExp120",
    ends={
        Property(name="cSharp_UnaryExpression121", type=cSharp_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_UnaryExpression119", type=cSharp_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExp122: BinaryAssociation = BinaryAssociation(
    name="primaryExp122",
    ends={
        Property(name="cSharp_PrimaryExpression", type=cSharp_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_UnaryExpression123", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableInitalizer163: BinaryAssociation = BinaryAssociation(
    name="variableInitalizer163",
    ends={
        Property(name="cSharp_VariableInitializer", type=cSharp_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ArrayInitializer164", type=cSharp_VariableInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableInitalizers165: BinaryAssociation = BinaryAssociation(
    name="variableInitalizers165",
    ends={
        Property(name="cSharp_VariableInitializer167", type=cSharp_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ArrayInitializer166", type=cSharp_VariableInitializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifiedId168: BinaryAssociation = BinaryAssociation(
    name="qualifiedId168",
    ends={
        Property(name="cSharp_QualifiedIdentifier170", type=cSharp_AttributeName, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_AttributeName169", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nonArray171: BinaryAssociation = BinaryAssociation(
    name="nonArray171",
    ends={
        Property(name="cSharp_NonArrayType173", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type172", type=cSharp_NonArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDeclarator174: BinaryAssociation = BinaryAssociation(
    name="variableDeclarator174",
    ends={
        Property(name="cSharp_VariableDeclarator", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type175", type=cSharp_VariableDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDeclarators176: BinaryAssociation = BinaryAssociation(
    name="variableDeclarators176",
    ends={
        Property(name="cSharp_VariableDeclarator178", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type177", type=cSharp_VariableDeclarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qIdent179: BinaryAssociation = BinaryAssociation(
    name="qIdent179",
    ends={
        Property(name="cSharp_QualifiedIdentifier181", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type180", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id151: BinaryAssociation = BinaryAssociation(
    name="id151",
    ends={
        Property(name="cSharp_Identifier153", type=cSharp_PrimaryExpression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression2152", type=cSharp_Identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argumentList154: BinaryAssociation = BinaryAssociation(
    name="argumentList154",
    ends={
        Property(name="cSharp_ArgumentList156", type=cSharp_PrimaryExpression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression2155", type=cSharp_ArgumentList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionList157: BinaryAssociation = BinaryAssociation(
    name="expressionList157",
    ends={
        Property(name="cSharp_ExpressionList159", type=cSharp_PrimaryExpression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression2158", type=cSharp_ExpressionList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryExpression2161: BinaryAssociation = BinaryAssociation(
    name="primaryExpression2161",
    ends={
        Property(name="cSharp_PrimaryExpression2162", type=cSharp_PrimaryExpression2, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_PrimaryExpression2160", type=cSharp_PrimaryExpression2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constDeclarator195: BinaryAssociation = BinaryAssociation(
    name="constDeclarator195",
    ends={
        Property(name="cSharp_ConstantDeclarator", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type196", type=cSharp_ConstantDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constDeclarators197: BinaryAssociation = BinaryAssociation(
    name="constDeclarators197",
    ends={
        Property(name="cSharp_ConstantDeclarator199", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type198", type=cSharp_ConstantDeclarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
builtType200: BinaryAssociation = BinaryAssociation(
    name="builtType200",
    ends={
        Property(name="cSharp_BuiltInType202", type=cSharp_NonArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_NonArrayType201", type=cSharp_BuiltInType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualified203: BinaryAssociation = BinaryAssociation(
    name="qualified203",
    ends={
        Property(name="cSharp_QualifiedIdentifier205", type=cSharp_NonArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_NonArrayType204", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qID2206: BinaryAssociation = BinaryAssociation(
    name="qID2206",
    ends={
        Property(name="cSharp_QualifiedIdentifierList", type=cSharp_BuiltInClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_BuiltInClassType", type=cSharp_QualifiedIdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id207: BinaryAssociation = BinaryAssociation(
    name="id207",
    ends={
        Property(name="cSharp_Identifier209", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_QualifiedIdentifier208", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ids210: BinaryAssociation = BinaryAssociation(
    name="ids210",
    ends={
        Property(name="cSharp_Identifier212", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_QualifiedIdentifier211", type=cSharp_Identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventAccessorDeclarations182: BinaryAssociation = BinaryAssociation(
    name="eventAccessorDeclarations182",
    ends={
        Property(name="cSharp_EventAccessorDeclarations", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type183", type=cSharp_EventAccessorDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedId184: BinaryAssociation = BinaryAssociation(
    name="qualifiedId184",
    ends={
        Property(name="cSharp_QualifiedIdentifier186", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type185", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accDeclarate187: BinaryAssociation = BinaryAssociation(
    name="accDeclarate187",
    ends={
        Property(name="cSharp_AccessorDeclarations", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type188", type=cSharp_AccessorDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable189: BinaryAssociation = BinaryAssociation(
    name="variable189",
    ends={
        Property(name="cSharp_VariableDeclarator191", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type190", type=cSharp_VariableDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables192: BinaryAssociation = BinaryAssociation(
    name="variables192",
    ends={
        Property(name="cSharp_VariableDeclarator194", type=cSharp_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Type193", type=cSharp_VariableDeclarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usingDirectives222: BinaryAssociation = BinaryAssociation(
    name="usingDirectives222",
    ends={
        Property(name="cSharp_UsingDirective224", type=cSharp_NamespaceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_NamespaceBody223", type=cSharp_UsingDirective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameSpaces225: BinaryAssociation = BinaryAssociation(
    name="nameSpaces225",
    ends={
        Property(name="cSharp_NamespaceMemberDeclaration227", type=cSharp_NamespaceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_NamespaceBody226", type=cSharp_NamespaceMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classDeclaration228: BinaryAssociation = BinaryAssociation(
    name="classDeclaration228",
    ends={
        Property(name="cSharp_ClassDeclaration", type=cSharp_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TypeDeclaration229", type=cSharp_ClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceDeclaration230: BinaryAssociation = BinaryAssociation(
    name="interfaceDeclaration230",
    ends={
        Property(name="cSharp_InterfaceDeclaration", type=cSharp_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TypeDeclaration231", type=cSharp_InterfaceDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumDeclaration232: BinaryAssociation = BinaryAssociation(
    name="enumDeclaration232",
    ends={
        Property(name="cSharp_EnumDeclaration", type=cSharp_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TypeDeclaration233", type=cSharp_EnumDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delegateDeclaration234: BinaryAssociation = BinaryAssociation(
    name="delegateDeclaration234",
    ends={
        Property(name="cSharp_DelegateDeclaration", type=cSharp_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TypeDeclaration235", type=cSharp_DelegateDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name236: BinaryAssociation = BinaryAssociation(
    name="name236",
    ends={
        Property(name="cSharp_Identifier238", type=cSharp_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EnumDeclaration237", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
intType239: BinaryAssociation = BinaryAssociation(
    name="intType239",
    ends={
        Property(name="cSharp_IntegralType", type=cSharp_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EnumDeclaration240", type=cSharp_IntegralType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumBody241: BinaryAssociation = BinaryAssociation(
    name="enumBody241",
    ends={
        Property(name="cSharp_EnumBody", type=cSharp_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EnumDeclaration242", type=cSharp_EnumBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameDeclaretion213: BinaryAssociation = BinaryAssociation(
    name="nameDeclaretion213",
    ends={
        Property(name="cSharp_NamespaceDeclaration", type=cSharp_NamespaceMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_NamespaceMemberDeclaration214", type=cSharp_NamespaceDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDeclaration215: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration215",
    ends={
        Property(name="cSharp_TypeDeclaration", type=cSharp_NamespaceMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_NamespaceMemberDeclaration216", type=cSharp_TypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qId217: BinaryAssociation = BinaryAssociation(
    name="qId217",
    ends={
        Property(name="cSharp_QualifiedIdentifier219", type=cSharp_NamespaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_NamespaceDeclaration218", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameBody220: BinaryAssociation = BinaryAssociation(
    name="nameBody220",
    ends={
        Property(name="cSharp_NamespaceBody", type=cSharp_NamespaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_NamespaceDeclaration221", type=cSharp_NamespaceBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name257: BinaryAssociation = BinaryAssociation(
    name="name257",
    ends={
        Property(name="cSharp_Identifier259", type=cSharp_InterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceDeclaration258", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qIdentifiers260: BinaryAssociation = BinaryAssociation(
    name="qIdentifiers260",
    ends={
        Property(name="cSharp_QualifiedIdentifierList262", type=cSharp_InterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceDeclaration261", type=cSharp_QualifiedIdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interBody263: BinaryAssociation = BinaryAssociation(
    name="interBody263",
    ends={
        Property(name="cSharp_InterfaceBody", type=cSharp_InterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceDeclaration264", type=cSharp_InterfaceBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceMemberDeclarations265: BinaryAssociation = BinaryAssociation(
    name="interfaceMemberDeclarations265",
    ends={
        Property(name="cSharp_InterfaceMemberDeclaration", type=cSharp_InterfaceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceBody266", type=cSharp_InterfaceMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermethodDeclaration267: BinaryAssociation = BinaryAssociation(
    name="intermethodDeclaration267",
    ends={
        Property(name="cSharp_InterfaceMethodDeclaration", type=cSharp_InterfaceMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceMemberDeclaration268", type=cSharp_InterfaceMethodDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interEventDeclaration269: BinaryAssociation = BinaryAssociation(
    name="interEventDeclaration269",
    ends={
        Property(name="cSharp_InterfaceEventDeclaration", type=cSharp_InterfaceMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceMemberDeclaration270", type=cSharp_InterfaceEventDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type1271: BinaryAssociation = BinaryAssociation(
    name="type1271",
    ends={
        Property(name="cSharp_Type273", type=cSharp_InterfaceMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceMemberDeclaration272", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceIndexerDecla274: BinaryAssociation = BinaryAssociation(
    name="interfaceIndexerDecla274",
    ends={
        Property(name="cSharp_InterfaceIndexerDeclaration", type=cSharp_InterfaceMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceMemberDeclaration275", type=cSharp_InterfaceIndexerDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interProperty276: BinaryAssociation = BinaryAssociation(
    name="interProperty276",
    ends={
        Property(name="cSharp_InterfacePropertyDeclaration", type=cSharp_InterfaceMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceMemberDeclaration277", type=cSharp_InterfacePropertyDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumDeclaration243: BinaryAssociation = BinaryAssociation(
    name="enumDeclaration243",
    ends={
        Property(name="cSharp_EnumMemberDeclaration", type=cSharp_EnumBody, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EnumBody244", type=cSharp_EnumMemberDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumDeclarations245: BinaryAssociation = BinaryAssociation(
    name="enumDeclarations245",
    ends={
        Property(name="cSharp_EnumMemberDeclaration247", type=cSharp_EnumBody, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EnumBody246", type=cSharp_EnumMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
att248: BinaryAssociation = BinaryAssociation(
    name="att248",
    ends={
        Property(name="cSharp_Attributes250", type=cSharp_EnumMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EnumMemberDeclaration249", type=cSharp_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name251: BinaryAssociation = BinaryAssociation(
    name="name251",
    ends={
        Property(name="cSharp_Identifier253", type=cSharp_EnumMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EnumMemberDeclaration252", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp254: BinaryAssociation = BinaryAssociation(
    name="exp254",
    ends={
        Property(name="cSharp_Expression256", type=cSharp_EnumMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EnumMemberDeclaration255", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name288: BinaryAssociation = BinaryAssociation(
    name="name288",
    ends={
        Property(name="cSharp_Identifier290", type=cSharp_InterfacePropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfacePropertyDeclaration289", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interAccessor291: BinaryAssociation = BinaryAssociation(
    name="interAccessor291",
    ends={
        Property(name="cSharp_InterfaceAccessors293", type=cSharp_InterfacePropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfacePropertyDeclaration292", type=cSharp_InterfaceAccessors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
att294: BinaryAssociation = BinaryAssociation(
    name="att294",
    ends={
        Property(name="cSharp_Attributes296", type=cSharp_InterfaceAccessors, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceAccessors295", type=cSharp_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newAtt297: BinaryAssociation = BinaryAssociation(
    name="newAtt297",
    ends={
        Property(name="cSharp_Attributes299", type=cSharp_InterfaceAccessors, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceAccessors298", type=cSharp_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
otherAtt300: BinaryAssociation = BinaryAssociation(
    name="otherAtt300",
    ends={
        Property(name="cSharp_Attributes302", type=cSharp_InterfaceAccessors, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceAccessors301", type=cSharp_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type303: BinaryAssociation = BinaryAssociation(
    name="type303",
    ends={
        Property(name="cSharp_TypeOrVoid305", type=cSharp_InterfaceMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceMethodDeclaration304", type=cSharp_TypeOrVoid, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name306: BinaryAssociation = BinaryAssociation(
    name="name306",
    ends={
        Property(name="cSharp_Identifier308", type=cSharp_InterfaceMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceMethodDeclaration307", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterList309: BinaryAssociation = BinaryAssociation(
    name="parameterList309",
    ends={
        Property(name="cSharp_FormalParameterList311", type=cSharp_InterfaceMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceMethodDeclaration310", type=cSharp_FormalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className312: BinaryAssociation = BinaryAssociation(
    name="className312",
    ends={
        Property(name="cSharp_Identifier314", type=cSharp_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassDeclaration313", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterList278: BinaryAssociation = BinaryAssociation(
    name="parameterList278",
    ends={
        Property(name="cSharp_FormalParameterList", type=cSharp_InterfaceIndexerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceIndexerDeclaration279", type=cSharp_FormalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interAccessors280: BinaryAssociation = BinaryAssociation(
    name="interAccessors280",
    ends={
        Property(name="cSharp_InterfaceAccessors", type=cSharp_InterfaceIndexerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceIndexerDeclaration281", type=cSharp_InterfaceAccessors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type282: BinaryAssociation = BinaryAssociation(
    name="type282",
    ends={
        Property(name="cSharp_Type284", type=cSharp_InterfaceEventDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceEventDeclaration283", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name285: BinaryAssociation = BinaryAssociation(
    name="name285",
    ends={
        Property(name="cSharp_Identifier287", type=cSharp_InterfaceEventDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_InterfaceEventDeclaration286", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldDeclaration324: BinaryAssociation = BinaryAssociation(
    name="fieldDeclaration324",
    ends={
        Property(name="cSharp_FieldDeclaration", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration325", type=cSharp_FieldDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodDeclaration326: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration326",
    ends={
        Property(name="cSharp_MethodDeclaration", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration327", type=cSharp_MethodDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constDeclaration328: BinaryAssociation = BinaryAssociation(
    name="constDeclaration328",
    ends={
        Property(name="cSharp_ConstantDeclaration", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration329", type=cSharp_ConstantDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyDeclaration330: BinaryAssociation = BinaryAssociation(
    name="propertyDeclaration330",
    ends={
        Property(name="cSharp_PropertyDeclaration", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration331", type=cSharp_PropertyDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventDeclaration332: BinaryAssociation = BinaryAssociation(
    name="eventDeclaration332",
    ends={
        Property(name="cSharp_EventDeclaration", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration333", type=cSharp_EventDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexDeclaration334: BinaryAssociation = BinaryAssociation(
    name="indexDeclaration334",
    ends={
        Property(name="cSharp_IndexerDeclaration", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration335", type=cSharp_IndexerDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDeclaration336: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration336",
    ends={
        Property(name="cSharp_TypeDeclaration338", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration337", type=cSharp_TypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opDeclaration339: BinaryAssociation = BinaryAssociation(
    name="opDeclaration339",
    ends={
        Property(name="cSharp_OperatorDeclaration", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration340", type=cSharp_OperatorDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constructorDeclaration341: BinaryAssociation = BinaryAssociation(
    name="constructorDeclaration341",
    ends={
        Property(name="cSharp_ConstructorDeclaration", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration342", type=cSharp_ConstructorDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destructorDeclaration343: BinaryAssociation = BinaryAssociation(
    name="destructorDeclaration343",
    ends={
        Property(name="cSharp_DestructorDeclaration", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration344", type=cSharp_DestructorDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classBase315: BinaryAssociation = BinaryAssociation(
    name="classBase315",
    ends={
        Property(name="cSharp_ClassBase", type=cSharp_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassDeclaration316", type=cSharp_ClassBase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classBody317: BinaryAssociation = BinaryAssociation(
    name="classBody317",
    ends={
        Property(name="cSharp_ClassBody", type=cSharp_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassDeclaration318", type=cSharp_ClassBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classAtt319: BinaryAssociation = BinaryAssociation(
    name="classAtt319",
    ends={
        Property(name="cSharp_Attributes321", type=cSharp_ClassBody, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassBody320", type=cSharp_Attributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classDeclaration322: BinaryAssociation = BinaryAssociation(
    name="classDeclaration322",
    ends={
        Property(name="cSharp_ClassMemberDeclaration", type=cSharp_ClassBody, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassBody323", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name352: BinaryAssociation = BinaryAssociation(
    name="name352",
    ends={
        Property(name="cSharp_Identifier354", type=cSharp_DestructorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_DestructorDeclaration353", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emptyBlock355: BinaryAssociation = BinaryAssociation(
    name="emptyBlock355",
    ends={
        Property(name="cSharp_MaybeEmptyBlock357", type=cSharp_DestructorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_DestructorDeclaration356", type=cSharp_MaybeEmptyBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constrDeclarator358: BinaryAssociation = BinaryAssociation(
    name="constrDeclarator358",
    ends={
        Property(name="cSharp_ConstructorDeclarator", type=cSharp_ConstructorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ConstructorDeclaration359", type=cSharp_ConstructorDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emptyBlock360: BinaryAssociation = BinaryAssociation(
    name="emptyBlock360",
    ends={
        Property(name="cSharp_MaybeEmptyBlock362", type=cSharp_ConstructorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ConstructorDeclaration361", type=cSharp_MaybeEmptyBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
className363: BinaryAssociation = BinaryAssociation(
    name="className363",
    ends={
        Property(name="cSharp_Identifier365", type=cSharp_ConstructorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ConstructorDeclarator364", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalList366: BinaryAssociation = BinaryAssociation(
    name="formalList366",
    ends={
        Property(name="cSharp_FormalParameterList368", type=cSharp_ConstructorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ConstructorDeclarator367", type=cSharp_FormalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constInitializer369: BinaryAssociation = BinaryAssociation(
    name="constInitializer369",
    ends={
        Property(name="cSharp_ConstructorInitializer", type=cSharp_ConstructorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ConstructorDeclarator370", type=cSharp_ConstructorInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg371: BinaryAssociation = BinaryAssociation(
    name="arg371",
    ends={
        Property(name="cSharp_Argument", type=cSharp_ArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ArgumentList372", type=cSharp_Argument, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
staticDeclaration345: BinaryAssociation = BinaryAssociation(
    name="staticDeclaration345",
    ends={
        Property(name="cSharp_StaticConstructorDeclaration", type=cSharp_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassMemberDeclaration346", type=cSharp_StaticConstructorDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name347: BinaryAssociation = BinaryAssociation(
    name="name347",
    ends={
        Property(name="cSharp_Identifier349", type=cSharp_StaticConstructorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_StaticConstructorDeclaration348", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emptyBlock350: BinaryAssociation = BinaryAssociation(
    name="emptyBlock350",
    ends={
        Property(name="cSharp_MaybeEmptyBlock", type=cSharp_StaticConstructorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_StaticConstructorDeclaration351", type=cSharp_MaybeEmptyBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opDeclarator376: BinaryAssociation = BinaryAssociation(
    name="opDeclarator376",
    ends={
        Property(name="cSharp_OperatorDeclarator", type=cSharp_OperatorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_OperatorDeclaration377", type=cSharp_OperatorDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emptyBlock378: BinaryAssociation = BinaryAssociation(
    name="emptyBlock378",
    ends={
        Property(name="cSharp_MaybeEmptyBlock380", type=cSharp_OperatorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_OperatorDeclaration379", type=cSharp_MaybeEmptyBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type381: BinaryAssociation = BinaryAssociation(
    name="type381",
    ends={
        Property(name="cSharp_Type383", type=cSharp_OperatorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_OperatorDeclarator382", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstType384: BinaryAssociation = BinaryAssociation(
    name="firstType384",
    ends={
        Property(name="cSharp_Type385", type=cSharp_ConversionOperatorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ConversionOperatorDeclarator", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conversionName386: BinaryAssociation = BinaryAssociation(
    name="conversionName386",
    ends={
        Property(name="cSharp_Identifier388", type=cSharp_ConversionOperatorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ConversionOperatorDeclarator387", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
binType389: BinaryAssociation = BinaryAssociation(
    name="binType389",
    ends={
        Property(name="cSharp_Type390", type=cSharp_BinaryOperatorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_BinaryOperatorDeclarator", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
otherName391: BinaryAssociation = BinaryAssociation(
    name="otherName391",
    ends={
        Property(name="cSharp_Identifier393", type=cSharp_BinaryOperatorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_BinaryOperatorDeclarator392", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
secondType394: BinaryAssociation = BinaryAssociation(
    name="secondType394",
    ends={
        Property(name="cSharp_Type396", type=cSharp_BinaryOperatorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_BinaryOperatorDeclarator395", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args373: BinaryAssociation = BinaryAssociation(
    name="args373",
    ends={
        Property(name="cSharp_Argument375", type=cSharp_ArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ArgumentList374", type=cSharp_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
secondName397: BinaryAssociation = BinaryAssociation(
    name="secondName397",
    ends={
        Property(name="cSharp_Identifier399", type=cSharp_BinaryOperatorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_BinaryOperatorDeclarator398", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
otherType400: BinaryAssociation = BinaryAssociation(
    name="otherType400",
    ends={
        Property(name="cSharp_Type401", type=cSharp_UnaryOperatorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_UnaryOperatorDeclarator", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name402: BinaryAssociation = BinaryAssociation(
    name="name402",
    ends={
        Property(name="cSharp_Identifier404", type=cSharp_UnaryOperatorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_UnaryOperatorDeclarator403", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexerDeclarator405: BinaryAssociation = BinaryAssociation(
    name="indexerDeclarator405",
    ends={
        Property(name="cSharp_IndexerDeclarator", type=cSharp_IndexerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IndexerDeclaration406", type=cSharp_IndexerDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accDeclaration407: BinaryAssociation = BinaryAssociation(
    name="accDeclaration407",
    ends={
        Property(name="cSharp_AccessorDeclarations409", type=cSharp_IndexerDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IndexerDeclaration408", type=cSharp_AccessorDeclarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type410: BinaryAssociation = BinaryAssociation(
    name="type410",
    ends={
        Property(name="cSharp_Type412", type=cSharp_IndexerDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IndexerDeclarator411", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalList413: BinaryAssociation = BinaryAssociation(
    name="formalList413",
    ends={
        Property(name="cSharp_FormalParameterList415", type=cSharp_IndexerDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IndexerDeclarator414", type=cSharp_FormalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedId416: BinaryAssociation = BinaryAssociation(
    name="qualifiedId416",
    ends={
        Property(name="cSharp_QualifiedIdentifier418", type=cSharp_IndexerDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IndexerDeclarator417", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
att1419: BinaryAssociation = BinaryAssociation(
    name="att1419",
    ends={
        Property(name="cSharp_Attributes421", type=cSharp_EventAccessorDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EventAccessorDeclarations420", type=cSharp_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
att424: BinaryAssociation = BinaryAssociation(
    name="att424",
    ends={
        Property(name="cSharp_Attributes426", type=cSharp_EventAccessorDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EventAccessorDeclarations425", type=cSharp_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removAccessor427: BinaryAssociation = BinaryAssociation(
    name="removAccessor427",
    ends={
        Property(name="cSharp_RemoveAccessorDeclaration", type=cSharp_EventAccessorDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EventAccessorDeclarations428", type=cSharp_RemoveAccessorDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
att429: BinaryAssociation = BinaryAssociation(
    name="att429",
    ends={
        Property(name="cSharp_Attributes431", type=cSharp_AccessorDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_AccessorDeclarations430", type=cSharp_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
getAcc432: BinaryAssociation = BinaryAssociation(
    name="getAcc432",
    ends={
        Property(name="cSharp_GetAccessorDeclaration", type=cSharp_AccessorDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_AccessorDeclarations433", type=cSharp_GetAccessorDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
att2434: BinaryAssociation = BinaryAssociation(
    name="att2434",
    ends={
        Property(name="cSharp_Attributes436", type=cSharp_AccessorDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_AccessorDeclarations435", type=cSharp_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setAcc437: BinaryAssociation = BinaryAssociation(
    name="setAcc437",
    ends={
        Property(name="cSharp_SetAccessorDeclaration", type=cSharp_AccessorDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_AccessorDeclarations438", type=cSharp_SetAccessorDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodHeader439: BinaryAssociation = BinaryAssociation(
    name="methodHeader439",
    ends={
        Property(name="cSharp_MethodHeader", type=cSharp_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_MethodDeclaration440", type=cSharp_MethodHeader, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maybeEmpty441: BinaryAssociation = BinaryAssociation(
    name="maybeEmpty441",
    ends={
        Property(name="cSharp_MaybeEmptyBlock443", type=cSharp_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_MethodDeclaration442", type=cSharp_MaybeEmptyBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeOrVoid444: BinaryAssociation = BinaryAssociation(
    name="typeOrVoid444",
    ends={
        Property(name="cSharp_TypeOrVoid446", type=cSharp_MethodHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_MethodHeader445", type=cSharp_TypeOrVoid, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addAccessor422: BinaryAssociation = BinaryAssociation(
    name="addAccessor422",
    ends={
        Property(name="cSharp_AddAccessorDeclaration", type=cSharp_EventAccessorDeclarations, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EventAccessorDeclarations423", type=cSharp_AddAccessorDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters450: BinaryAssociation = BinaryAssociation(
    name="formalParameters450",
    ends={
        Property(name="cSharp_FormalParameterList452", type=cSharp_MethodHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_MethodHeader451", type=cSharp_FormalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterArray453: BinaryAssociation = BinaryAssociation(
    name="parameterArray453",
    ends={
        Property(name="cSharp_ParameterArray", type=cSharp_FormalParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_FormalParameterList454", type=cSharp_ParameterArray, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
att455: BinaryAssociation = BinaryAssociation(
    name="att455",
    ends={
        Property(name="cSharp_Attributes457", type=cSharp_ParameterArray, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ParameterArray456", type=cSharp_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array458: BinaryAssociation = BinaryAssociation(
    name="array458",
    ends={
        Property(name="cSharp_ArrayType460", type=cSharp_ParameterArray, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ParameterArray459", type=cSharp_ArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name461: BinaryAssociation = BinaryAssociation(
    name="name461",
    ends={
        Property(name="cSharp_Identifier463", type=cSharp_ParameterArray, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ParameterArray462", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fixParameter464: BinaryAssociation = BinaryAssociation(
    name="fixParameter464",
    ends={
        Property(name="cSharp_FixedParameter", type=cSharp_FixedParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_FixedParameters", type=cSharp_FixedParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fixParameters465: BinaryAssociation = BinaryAssociation(
    name="fixParameters465",
    ends={
        Property(name="cSharp_FixedParameter467", type=cSharp_FixedParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_FixedParameters466", type=cSharp_FixedParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Att468: BinaryAssociation = BinaryAssociation(
    name="Att468",
    ends={
        Property(name="cSharp_Attributes470", type=cSharp_FixedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_FixedParameter469", type=cSharp_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type471: BinaryAssociation = BinaryAssociation(
    name="type471",
    ends={
        Property(name="cSharp_Type473", type=cSharp_FixedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_FixedParameter472", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifiedIdentifier447: BinaryAssociation = BinaryAssociation(
    name="qualifiedIdentifier447",
    ends={
        Property(name="cSharp_QualifiedIdentifier449", type=cSharp_MethodHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_MethodHeader448", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name474: BinaryAssociation = BinaryAssociation(
    name="name474",
    ends={
        Property(name="cSharp_FixedParameter475", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="cSharp_Identifier476", type=cSharp_FixedParameter, multiplicity=Multiplicity(1, 1))
    }
)
name477: BinaryAssociation = BinaryAssociation(
    name="name477",
    ends={
        Property(name="cSharp_Identifier479", type=cSharp_TypeOrVoid, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TypeOrVoid478", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters480: BinaryAssociation = BinaryAssociation(
    name="formalParameters480",
    ends={
        Property(name="cSharp_FormalParameterList482", type=cSharp_TypeOrVoid, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TypeOrVoid481", type=cSharp_FormalParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type483: BinaryAssociation = BinaryAssociation(
    name="type483",
    ends={
        Property(name="cSharp_Type485", type=cSharp_TypeOrVoid, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TypeOrVoid484", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableName486: BinaryAssociation = BinaryAssociation(
    name="variableName486",
    ends={
        Property(name="cSharp_Identifier488", type=cSharp_VariableDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_VariableDeclarator487", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable489: BinaryAssociation = BinaryAssociation(
    name="variable489",
    ends={
        Property(name="cSharp_VariableInitializer491", type=cSharp_VariableDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_VariableDeclarator490", type=cSharp_VariableInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name492: BinaryAssociation = BinaryAssociation(
    name="name492",
    ends={
        Property(name="cSharp_Identifier494", type=cSharp_ConstantDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ConstantDeclarator493", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp495: BinaryAssociation = BinaryAssociation(
    name="exp495",
    ends={
        Property(name="cSharp_Expression497", type=cSharp_ConstantDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ConstantDeclarator496", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipo516: BinaryAssociation = BinaryAssociation(
    name="tipo516",
    ends={
        Property(name="cSharp_Type518", type=cSharp_LocalconstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_LocalconstantDeclaration517", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constDeclarator519: BinaryAssociation = BinaryAssociation(
    name="constDeclarator519",
    ends={
        Property(name="cSharp_ConstantDeclarator521", type=cSharp_LocalconstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_LocalconstantDeclaration520", type=cSharp_ConstantDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qIDs498: BinaryAssociation = BinaryAssociation(
    name="qIDs498",
    ends={
        Property(name="cSharp_QualifiedIdentifierList500", type=cSharp_ClassBase, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ClassBase499", type=cSharp_QualifiedIdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constDeclarators522: BinaryAssociation = BinaryAssociation(
    name="constDeclarators522",
    ends={
        Property(name="cSharp_ConstantDeclarator524", type=cSharp_LocalconstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_LocalconstantDeclaration523", type=cSharp_ConstantDeclarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id501: BinaryAssociation = BinaryAssociation(
    name="id501",
    ends={
        Property(name="cSharp_QualifiedIdentifier503", type=cSharp_QualifiedIdentifierList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_QualifiedIdentifierList502", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ids504: BinaryAssociation = BinaryAssociation(
    name="ids504",
    ends={
        Property(name="cSharp_QualifiedIdentifier506", type=cSharp_QualifiedIdentifierList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_QualifiedIdentifierList505", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelStat507: BinaryAssociation = BinaryAssociation(
    name="labelStat507",
    ends={
        Property(name="cSharp_LabeledStatement", type=cSharp_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Statement", type=cSharp_LabeledStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declareStat508: BinaryAssociation = BinaryAssociation(
    name="declareStat508",
    ends={
        Property(name="cSharp_DeclarationStatment", type=cSharp_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Statement509", type=cSharp_DeclarationStatment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStat510: BinaryAssociation = BinaryAssociation(
    name="embeddedStat510",
    ends={
        Property(name="cSharp_EmbeddedStatement", type=cSharp_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Statement511", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariableDeclaration512: BinaryAssociation = BinaryAssociation(
    name="localVariableDeclaration512",
    ends={
        Property(name="cSharp_LocalVariableDeclaration", type=cSharp_DeclarationStatment, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_DeclarationStatment513", type=cSharp_LocalVariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localCOnstant514: BinaryAssociation = BinaryAssociation(
    name="localCOnstant514",
    ends={
        Property(name="cSharp_LocalconstantDeclaration", type=cSharp_DeclarationStatment, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_DeclarationStatment515", type=cSharp_LocalconstantDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id525: BinaryAssociation = BinaryAssociation(
    name="id525",
    ends={
        Property(name="cSharp_Identifier527", type=cSharp_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_LabeledStatement526", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stat528: BinaryAssociation = BinaryAssociation(
    name="stat528",
    ends={
        Property(name="cSharp_Statement530", type=cSharp_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_LabeledStatement529", type=cSharp_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maybeEmpty531: BinaryAssociation = BinaryAssociation(
    name="maybeEmpty531",
    ends={
        Property(name="cSharp_MaybeEmptyBlock533", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EmbeddedStatement532", type=cSharp_MaybeEmptyBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statExp534: BinaryAssociation = BinaryAssociation(
    name="statExp534",
    ends={
        Property(name="cSharp_StatementExpression", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EmbeddedStatement535", type=cSharp_StatementExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectionStat536: BinaryAssociation = BinaryAssociation(
    name="selectionStat536",
    ends={
        Property(name="cSharp_SelectionStatement", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EmbeddedStatement537", type=cSharp_SelectionStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourcAquisition550: BinaryAssociation = BinaryAssociation(
    name="resourcAquisition550",
    ends={
        Property(name="cSharp_ResourceAquisition", type=cSharp_UsingStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_UsingStatement551", type=cSharp_ResourceAquisition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationStat538: BinaryAssociation = BinaryAssociation(
    name="iterationStat538",
    ends={
        Property(name="cSharp_IterationStatement", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EmbeddedStatement539", type=cSharp_IterationStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStat552: BinaryAssociation = BinaryAssociation(
    name="embeddedStat552",
    ends={
        Property(name="cSharp_EmbeddedStatement554", type=cSharp_UsingStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_UsingStatement553", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipo555: BinaryAssociation = BinaryAssociation(
    name="tipo555",
    ends={
        Property(name="cSharp_Type557", type=cSharp_LocalVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_LocalVariableDeclaration556", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable558: BinaryAssociation = BinaryAssociation(
    name="variable558",
    ends={
        Property(name="cSharp_VariableDeclarator560", type=cSharp_LocalVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_LocalVariableDeclaration559", type=cSharp_VariableDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables561: BinaryAssociation = BinaryAssociation(
    name="variables561",
    ends={
        Property(name="cSharp_VariableDeclarator563", type=cSharp_LocalVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_LocalVariableDeclaration562", type=cSharp_VariableDeclarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp564: BinaryAssociation = BinaryAssociation(
    name="exp564",
    ends={
        Property(name="cSharp_Expression566", type=cSharp_LockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_LockStatement565", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStat567: BinaryAssociation = BinaryAssociation(
    name="embeddedStat567",
    ends={
        Property(name="cSharp_EmbeddedStatement569", type=cSharp_LockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_LockStatement568", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block570: BinaryAssociation = BinaryAssociation(
    name="block570",
    ends={
        Property(name="cSharp_Block572", type=cSharp_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TryStatement571", type=cSharp_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses573: BinaryAssociation = BinaryAssociation(
    name="catchClauses573",
    ends={
        Property(name="cSharp_CatchClauses", type=cSharp_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TryStatement574", type=cSharp_CatchClauses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finally575: BinaryAssociation = BinaryAssociation(
    name="finally575",
    ends={
        Property(name="cSharp_FinallyClause", type=cSharp_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TryStatement576", type=cSharp_FinallyClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jumpStat540: BinaryAssociation = BinaryAssociation(
    name="jumpStat540",
    ends={
        Property(name="cSharp_JumpStatement", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EmbeddedStatement541", type=cSharp_JumpStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryStat542: BinaryAssociation = BinaryAssociation(
    name="tryStat542",
    ends={
        Property(name="cSharp_TryStatement", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EmbeddedStatement543", type=cSharp_TryStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block544: BinaryAssociation = BinaryAssociation(
    name="block544",
    ends={
        Property(name="cSharp_Block", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EmbeddedStatement545", type=cSharp_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lockStat546: BinaryAssociation = BinaryAssociation(
    name="lockStat546",
    ends={
        Property(name="cSharp_LockStatement", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EmbeddedStatement547", type=cSharp_LockStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usingStat548: BinaryAssociation = BinaryAssociation(
    name="usingStat548",
    ends={
        Property(name="cSharp_UsingStatement", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_EmbeddedStatement549", type=cSharp_UsingStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specCatchClause587: BinaryAssociation = BinaryAssociation(
    name="specCatchClause587",
    ends={
        Property(name="cSharp_SpecificCatchClause589", type=cSharp_CatchClauses, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_CatchClauses588", type=cSharp_SpecificCatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block590: BinaryAssociation = BinaryAssociation(
    name="block590",
    ends={
        Property(name="cSharp_Block592", type=cSharp_GeneralCatchclause, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_GeneralCatchclause591", type=cSharp_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classType593: BinaryAssociation = BinaryAssociation(
    name="classType593",
    ends={
        Property(name="cSharp_BuiltInClassType595", type=cSharp_SpecificCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SpecificCatchClause594", type=cSharp_BuiltInClassType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualiId596: BinaryAssociation = BinaryAssociation(
    name="qualiId596",
    ends={
        Property(name="cSharp_QualifiedIdentifier598", type=cSharp_SpecificCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SpecificCatchClause597", type=cSharp_QualifiedIdentifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id599: BinaryAssociation = BinaryAssociation(
    name="id599",
    ends={
        Property(name="cSharp_Identifier601", type=cSharp_SpecificCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SpecificCatchClause600", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block602: BinaryAssociation = BinaryAssociation(
    name="block602",
    ends={
        Property(name="cSharp_Block604", type=cSharp_SpecificCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SpecificCatchClause603", type=cSharp_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
breakStat605: BinaryAssociation = BinaryAssociation(
    name="breakStat605",
    ends={
        Property(name="cSharp_BreakStatement", type=cSharp_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_JumpStatement606", type=cSharp_BreakStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
continueStat607: BinaryAssociation = BinaryAssociation(
    name="continueStat607",
    ends={
        Property(name="cSharp_ContinueStatement", type=cSharp_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_JumpStatement608", type=cSharp_ContinueStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gotoStat609: BinaryAssociation = BinaryAssociation(
    name="gotoStat609",
    ends={
        Property(name="cSharp_GotoStatement", type=cSharp_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_JumpStatement610", type=cSharp_GotoStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnStat611: BinaryAssociation = BinaryAssociation(
    name="returnStat611",
    ends={
        Property(name="cSharp_ReturnStatement", type=cSharp_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_JumpStatement612", type=cSharp_ReturnStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throwStat613: BinaryAssociation = BinaryAssociation(
    name="throwStat613",
    ends={
        Property(name="cSharp_ThrowStatement", type=cSharp_JumpStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_JumpStatement614", type=cSharp_ThrowStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression615: BinaryAssociation = BinaryAssociation(
    name="expression615",
    ends={
        Property(name="cSharp_Expression617", type=cSharp_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ThrowStatement616", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finallyClause577: BinaryAssociation = BinaryAssociation(
    name="finallyClause577",
    ends={
        Property(name="cSharp_FinallyClause579", type=cSharp_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_TryStatement578", type=cSharp_FinallyClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block580: BinaryAssociation = BinaryAssociation(
    name="block580",
    ends={
        Property(name="cSharp_Block582", type=cSharp_FinallyClause, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_FinallyClause581", type=cSharp_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
speciCatchClause583: BinaryAssociation = BinaryAssociation(
    name="speciCatchClause583",
    ends={
        Property(name="cSharp_SpecificCatchClause", type=cSharp_CatchClauses, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_CatchClauses584", type=cSharp_SpecificCatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
genCatchClause585: BinaryAssociation = BinaryAssociation(
    name="genCatchClause585",
    ends={
        Property(name="cSharp_GeneralCatchclause", type=cSharp_CatchClauses, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_CatchClauses586", type=cSharp_GeneralCatchclause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whileStatement627: BinaryAssociation = BinaryAssociation(
    name="whileStatement627",
    ends={
        Property(name="cSharp_WhileStatement", type=cSharp_IterationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IterationStatement628", type=cSharp_WhileStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doStatement629: BinaryAssociation = BinaryAssociation(
    name="doStatement629",
    ends={
        Property(name="cSharp_DoStatement", type=cSharp_IterationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IterationStatement630", type=cSharp_DoStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forStatement631: BinaryAssociation = BinaryAssociation(
    name="forStatement631",
    ends={
        Property(name="cSharp_ForStatement", type=cSharp_IterationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IterationStatement632", type=cSharp_ForStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foreachStatement633: BinaryAssociation = BinaryAssociation(
    name="foreachStatement633",
    ends={
        Property(name="cSharp_ForeachStatement", type=cSharp_IterationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IterationStatement634", type=cSharp_ForeachStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression618: BinaryAssociation = BinaryAssociation(
    name="expression618",
    ends={
        Property(name="cSharp_Expression620", type=cSharp_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ReturnStatement619", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id621: BinaryAssociation = BinaryAssociation(
    name="id621",
    ends={
        Property(name="cSharp_Identifier623", type=cSharp_GotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_GotoStatement622", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression624: BinaryAssociation = BinaryAssociation(
    name="expression624",
    ends={
        Property(name="cSharp_Expression626", type=cSharp_GotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_GotoStatement625", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression641: BinaryAssociation = BinaryAssociation(
    name="expression641",
    ends={
        Property(name="cSharp_ForeachStatement642", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="cSharp_Expression643", type=cSharp_ForeachStatement, multiplicity=Multiplicity(1, 1))
    }
)
embeddedStatement644: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement644",
    ends={
        Property(name="cSharp_EmbeddedStatement646", type=cSharp_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ForeachStatement645", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forInitializer647: BinaryAssociation = BinaryAssociation(
    name="forInitializer647",
    ends={
        Property(name="cSharp_ForInitializer", type=cSharp_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ForStatement648", type=cSharp_ForInitializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression649: BinaryAssociation = BinaryAssociation(
    name="expression649",
    ends={
        Property(name="cSharp_Expression651", type=cSharp_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ForStatement650", type=cSharp_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statementExpressionList652: BinaryAssociation = BinaryAssociation(
    name="statementExpressionList652",
    ends={
        Property(name="cSharp_StatementExpressionList", type=cSharp_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ForStatement653", type=cSharp_StatementExpressionList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
embeddedStatement654: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement654",
    ends={
        Property(name="cSharp_EmbeddedStatement656", type=cSharp_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ForStatement655", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariableDeclaration657: BinaryAssociation = BinaryAssociation(
    name="localVariableDeclaration657",
    ends={
        Property(name="cSharp_LocalVariableDeclaration659", type=cSharp_ForInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ForInitializer658", type=cSharp_LocalVariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipo635: BinaryAssociation = BinaryAssociation(
    name="tipo635",
    ends={
        Property(name="cSharp_Type637", type=cSharp_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ForeachStatement636", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id638: BinaryAssociation = BinaryAssociation(
    name="id638",
    ends={
        Property(name="cSharp_Identifier640", type=cSharp_ForeachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ForeachStatement639", type=cSharp_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipo669: BinaryAssociation = BinaryAssociation(
    name="tipo669",
    ends={
        Property(name="cSharp_Type671", type=cSharp_StatementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_StatementExpression670", type=cSharp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argumentList672: BinaryAssociation = BinaryAssociation(
    name="argumentList672",
    ends={
        Property(name="cSharp_ArgumentList674", type=cSharp_StatementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_StatementExpression673", type=cSharp_ArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExpression675: BinaryAssociation = BinaryAssociation(
    name="primaryExpression675",
    ends={
        Property(name="cSharp_PrimaryExpression677", type=cSharp_StatementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_StatementExpression676", type=cSharp_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpression678: BinaryAssociation = BinaryAssociation(
    name="unaryExpression678",
    ends={
        Property(name="cSharp_UnaryExpression680", type=cSharp_StatementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_StatementExpression679", type=cSharp_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression681: BinaryAssociation = BinaryAssociation(
    name="expression681",
    ends={
        Property(name="cSharp_Expression683", type=cSharp_StatementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_StatementExpression682", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStatement684: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement684",
    ends={
        Property(name="cSharp_EmbeddedStatement686", type=cSharp_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_DoStatement685", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression687: BinaryAssociation = BinaryAssociation(
    name="expression687",
    ends={
        Property(name="cSharp_Expression689", type=cSharp_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_DoStatement688", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementExpressionList660: BinaryAssociation = BinaryAssociation(
    name="statementExpressionList660",
    ends={
        Property(name="cSharp_StatementExpressionList662", type=cSharp_ForInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ForInitializer661", type=cSharp_StatementExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression690: BinaryAssociation = BinaryAssociation(
    name="expression690",
    ends={
        Property(name="cSharp_Expression692", type=cSharp_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_WhileStatement691", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list663: BinaryAssociation = BinaryAssociation(
    name="list663",
    ends={
        Property(name="cSharp_StatementExpression665", type=cSharp_StatementExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_StatementExpressionList664", type=cSharp_StatementExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lists666: BinaryAssociation = BinaryAssociation(
    name="lists666",
    ends={
        Property(name="cSharp_StatementExpression668", type=cSharp_StatementExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_StatementExpressionList667", type=cSharp_StatementExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifStatement696: BinaryAssociation = BinaryAssociation(
    name="ifStatement696",
    ends={
        Property(name="cSharp_IfStatement", type=cSharp_SelectionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SelectionStatement697", type=cSharp_IfStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchStatement698: BinaryAssociation = BinaryAssociation(
    name="switchStatement698",
    ends={
        Property(name="cSharp_SwitchStatement", type=cSharp_SelectionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SelectionStatement699", type=cSharp_SwitchStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression700: BinaryAssociation = BinaryAssociation(
    name="expression700",
    ends={
        Property(name="cSharp_Expression702", type=cSharp_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SwitchStatement701", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchSection703: BinaryAssociation = BinaryAssociation(
    name="switchSection703",
    ends={
        Property(name="cSharp_SwitchSection", type=cSharp_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SwitchStatement704", type=cSharp_SwitchSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
switchlabel705: BinaryAssociation = BinaryAssociation(
    name="switchlabel705",
    ends={
        Property(name="cSharp_SwitchLabel", type=cSharp_SwitchSection, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SwitchSection706", type=cSharp_SwitchLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement707: BinaryAssociation = BinaryAssociation(
    name="statement707",
    ends={
        Property(name="cSharp_Statement709", type=cSharp_SwitchSection, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SwitchSection708", type=cSharp_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression710: BinaryAssociation = BinaryAssociation(
    name="expression710",
    ends={
        Property(name="cSharp_Expression712", type=cSharp_SwitchLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_SwitchLabel711", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStatement693: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement693",
    ends={
        Property(name="cSharp_EmbeddedStatement695", type=cSharp_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_WhileStatement694", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression713: BinaryAssociation = BinaryAssociation(
    name="expression713",
    ends={
        Property(name="cSharp_Expression715", type=cSharp_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IfStatement714", type=cSharp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStatement716: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement716",
    ends={
        Property(name="cSharp_EmbeddedStatement718", type=cSharp_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IfStatement717", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsePart719: BinaryAssociation = BinaryAssociation(
    name="elsePart719",
    ends={
        Property(name="cSharp_ElsePart", type=cSharp_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_IfStatement720", type=cSharp_ElsePart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedStatement721: BinaryAssociation = BinaryAssociation(
    name="embeddedStatement721",
    ends={
        Property(name="cSharp_EmbeddedStatement723", type=cSharp_ElsePart, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_ElsePart722", type=cSharp_EmbeddedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement724: BinaryAssociation = BinaryAssociation(
    name="statement724",
    ends={
        Property(name="cSharp_Statement726", type=cSharp_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharp_Block725", type=cSharp_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cSharp_AttributeList_AttributeSection = Generalization(general=AttributeSection, specific=cSharp_AttributeList)
gen_cSharp_Expression_VariableInitializer = Generalization(general=VariableInitializer, specific=cSharp_Expression)
gen_cSharp_Expression_Argument = Generalization(general=Argument, specific=cSharp_Expression)
gen_cSharp_Expression_ResourceAquisition = Generalization(general=ResourceAquisition, specific=cSharp_Expression)
gen_cSharp_Type_EventDeclaration = Generalization(general=EventDeclaration, specific=cSharp_Type)
gen_cSharp_Type_PropertyDeclaration = Generalization(general=PropertyDeclaration, specific=cSharp_Type)
gen_cSharp_Type_FieldDeclaration = Generalization(general=FieldDeclaration, specific=cSharp_Type)
gen_cSharp_Type_ConstantDeclaration = Generalization(general=ConstantDeclaration, specific=cSharp_Type)
gen_cSharp_ArrayInitializer_VariableInitializer = Generalization(general=VariableInitializer, specific=cSharp_ArrayInitializer)
gen_cSharp_IntegralType_BuiltInType = Generalization(general=BuiltInType, specific=cSharp_IntegralType)
gen_cSharp_NonArrayType_ArrayType = Generalization(general=ArrayType, specific=cSharp_NonArrayType)
gen_cSharp_BuiltInClassType_BuiltInType = Generalization(general=BuiltInType, specific=cSharp_BuiltInClassType)
gen_cSharp_BuiltInClassType_ClassBase = Generalization(general=ClassBase, specific=cSharp_BuiltInClassType)
gen_cSharp_ArgumentList_ConstructorInitializer = Generalization(general=ConstructorInitializer, specific=cSharp_ArgumentList)
gen_cSharp_ConversionOperatorDeclarator_OperatorDeclarator = Generalization(general=OperatorDeclarator, specific=cSharp_ConversionOperatorDeclarator)
gen_cSharp_BinaryOperatorDeclarator_OperatorDeclarator = Generalization(general=OperatorDeclarator, specific=cSharp_BinaryOperatorDeclarator)
gen_cSharp_UnaryOperatorDeclarator_OperatorDeclarator = Generalization(general=OperatorDeclarator, specific=cSharp_UnaryOperatorDeclarator)
gen_cSharp_FixedParameters_FormalParameterList = Generalization(general=FormalParameterList, specific=cSharp_FixedParameters)
gen_cSharp_TypeOrVoid_DelegateDeclaration = Generalization(general=DelegateDeclaration, specific=cSharp_TypeOrVoid)
gen_cSharp_LocalVariableDeclaration_ResourceAquisition = Generalization(general=ResourceAquisition, specific=cSharp_LocalVariableDeclaration)
gen_cSharp_Block_RemoveAccessorDeclaration = Generalization(general=RemoveAccessorDeclaration, specific=cSharp_Block)
gen_cSharp_Block_AddAccessorDeclaration = Generalization(general=AddAccessorDeclaration, specific=cSharp_Block)
gen_cSharp_Block_MaybeEmptyBlock = Generalization(general=MaybeEmptyBlock, specific=cSharp_Block)
gen_cSharp_MaybeEmptyBlock_SetAccessorDeclaration = Generalization(general=SetAccessorDeclaration, specific=cSharp_MaybeEmptyBlock)
gen_cSharp_MaybeEmptyBlock_GetAccessorDeclaration = Generalization(general=GetAccessorDeclaration, specific=cSharp_MaybeEmptyBlock)
gen_cSharp_SByte_IntegralType = Generalization(general=IntegralType, specific=cSharp_SByte)
gen_cSharp_Byte_IntegralType = Generalization(general=IntegralType, specific=cSharp_Byte)
gen_cSharp_Double_BuiltInType = Generalization(general=BuiltInType, specific=cSharp_Double)
gen_cSharp_Object_BuiltInClassType = Generalization(general=BuiltInClassType, specific=cSharp_Object)
gen_cSharp_String_BuiltInClassType = Generalization(general=BuiltInClassType, specific=cSharp_String)
gen_cSharp_Void_TypeOrVoid = Generalization(general=TypeOrVoid, specific=cSharp_Void)
gen_cSharp_Short_IntegralType = Generalization(general=IntegralType, specific=cSharp_Short)
gen_cSharp_UShort_IntegralType = Generalization(general=IntegralType, specific=cSharp_UShort)
gen_cSharp_Int_IntegralType = Generalization(general=IntegralType, specific=cSharp_Int)
gen_cSharp_UInt_IntegralType = Generalization(general=IntegralType, specific=cSharp_UInt)
gen_cSharp_Long_IntegralType = Generalization(general=IntegralType, specific=cSharp_Long)
gen_cSharp_ULong_IntegralType = Generalization(general=IntegralType, specific=cSharp_ULong)
gen_cSharp_Char_IntegralType = Generalization(general=IntegralType, specific=cSharp_Char)
gen_cSharp_Bool_BuiltInType = Generalization(general=BuiltInType, specific=cSharp_Bool)
gen_cSharp_Decimal_BuiltInType = Generalization(general=BuiltInType, specific=cSharp_Decimal)
gen_cSharp_Float_BuiltInType = Generalization(general=BuiltInType, specific=cSharp_Float)

# Domain Model
domain_model = DomainModel(
    name="cSharp",
    types={cSharp_UsingDirective, cSharp_GlobalAttributes, cSharp_NamespaceMemberDeclaration, cSharp_Identifier, cSharp_QualifiedIdentifier, cSharp_CompilationUnit, cSharp_Attributes, cSharp_AttributeSection, AttributeSection, cSharp_Attribute, cSharp_AttributeName, cSharp_ArrayType, cSharp_GlobalAttributeSection, cSharp_AttributeList, cSharp_ExpressionList, cSharp_Expression, VariableInitializer, Argument, ResourceAquisition, cSharp_UnaryExpression, cSharp_Expression2, cSharp_AttributeArguments, cSharp_BuiltInType, cSharp_ArrayInitializer, cSharp_ArgumentList, cSharp_TypeOrVoid, cSharp_PrimaryExpression2, cSharp_Type, cSharp_PrimaryExpression, cSharp_NonArrayType, cSharp_VariableInitializer, EventDeclaration, PropertyDeclaration, FieldDeclaration, ConstantDeclaration, cSharp_VariableDeclarator, cSharp_ConstantDeclarator, cSharp_IntegralType, BuiltInType, ArrayType, cSharp_BuiltInClassType, ClassBase, cSharp_QualifiedIdentifierList, cSharp_EventAccessorDeclarations, cSharp_AccessorDeclarations, cSharp_ClassDeclaration, cSharp_InterfaceDeclaration, cSharp_EnumDeclaration, cSharp_DelegateDeclaration, cSharp_EnumBody, cSharp_NamespaceDeclaration, cSharp_TypeDeclaration, cSharp_NamespaceBody, cSharp_InterfaceBody, cSharp_InterfaceMemberDeclaration, cSharp_InterfaceMethodDeclaration, cSharp_InterfaceEventDeclaration, cSharp_InterfaceIndexerDeclaration, cSharp_InterfacePropertyDeclaration, cSharp_EnumMemberDeclaration, cSharp_FormalParameterList, cSharp_InterfaceAccessors, cSharp_FieldDeclaration, cSharp_MethodDeclaration, cSharp_ConstantDeclaration, cSharp_PropertyDeclaration, cSharp_EventDeclaration, cSharp_IndexerDeclaration, cSharp_OperatorDeclaration, cSharp_ConstructorDeclaration, cSharp_DestructorDeclaration, cSharp_ClassBase, cSharp_ClassBody, cSharp_ClassMemberDeclaration, cSharp_ConstructorDeclarator, cSharp_ConstructorInitializer, ConstructorInitializer, cSharp_Argument, cSharp_StaticConstructorDeclaration, cSharp_MaybeEmptyBlock, cSharp_ConversionOperatorDeclarator, OperatorDeclarator, cSharp_BinaryOperatorDeclarator, cSharp_UnaryOperatorDeclarator, cSharp_OperatorDeclarator, cSharp_IndexerDeclarator, cSharp_RemoveAccessorDeclaration, cSharp_GetAccessorDeclaration, cSharp_SetAccessorDeclaration, cSharp_MethodHeader, cSharp_AddAccessorDeclaration, cSharp_ParameterArray, cSharp_FixedParameters, FormalParameterList, cSharp_FixedParameter, DelegateDeclaration, cSharp_Statement, cSharp_LabeledStatement, cSharp_DeclarationStatment, cSharp_EmbeddedStatement, cSharp_LocalVariableDeclaration, cSharp_LocalconstantDeclaration, cSharp_StatementExpression, cSharp_SelectionStatement, cSharp_ResourceAquisition, cSharp_IterationStatement, cSharp_JumpStatement, cSharp_CatchClauses, cSharp_FinallyClause, cSharp_TryStatement, cSharp_Block, cSharp_LockStatement, cSharp_UsingStatement, cSharp_BreakStatement, cSharp_ContinueStatement, cSharp_GotoStatement, cSharp_ReturnStatement, cSharp_ThrowStatement, cSharp_SpecificCatchClause, cSharp_GeneralCatchclause, cSharp_WhileStatement, cSharp_DoStatement, cSharp_ForStatement, cSharp_ForeachStatement, cSharp_ForInitializer, cSharp_StatementExpressionList, cSharp_IfStatement, cSharp_SwitchStatement, cSharp_SwitchSection, cSharp_SwitchLabel, cSharp_ElsePart, RemoveAccessorDeclaration, AddAccessorDeclaration, MaybeEmptyBlock, SetAccessorDeclaration, GetAccessorDeclaration, cSharp_SByte, IntegralType, cSharp_Byte, cSharp_Double, cSharp_Object, BuiltInClassType, cSharp_String, cSharp_Void, TypeOrVoid, cSharp_Short, cSharp_UShort, cSharp_Int, cSharp_UInt, cSharp_Long, cSharp_ULong, cSharp_Char, cSharp_Bool, cSharp_Decimal, cSharp_Float},
    associations={usingDirectives0, globalAtt1, nameSpaces3, name5, attributes11, attributes13, attribute14, attributes16, name19, usings7, globalAttSections9, expresionList23, expression25, expressions27, unary30, exp33, exp235, interExp37, interExp241, pipelineExp43, pipelineExp247, attArguments21, equalityExp73, equalityExp277, relopExp79, relopExp283, buildInType85, shiftExp87, shiftExp291, operatorExp93, operatorExp297, multipExp99, multipExp2103, divExp105, inExp49, divExp2109, inExp253, barExp55, barExp259, exp61, exp265, ampExp67, ampExp271, nonArrayType124, expressionList126, arrayInitializer129, arrayType131, arrayInitializer2133, tipo136, argumentList139, id141, expression144, typeOrVoid147, primaryExoression2149, modExp111, modExp2115, type117, unaryExp120, primaryExp122, variableInitalizer163, variableInitalizers165, qualifiedId168, nonArray171, variableDeclarator174, variableDeclarators176, qIdent179, id151, argumentList154, expressionList157, primaryExpression2161, constDeclarator195, constDeclarators197, builtType200, qualified203, qID2206, id207, ids210, eventAccessorDeclarations182, qualifiedId184, accDeclarate187, variable189, variables192, usingDirectives222, nameSpaces225, classDeclaration228, interfaceDeclaration230, enumDeclaration232, delegateDeclaration234, name236, intType239, enumBody241, nameDeclaretion213, typeDeclaration215, qId217, nameBody220, name257, qIdentifiers260, interBody263, interfaceMemberDeclarations265, intermethodDeclaration267, interEventDeclaration269, type1271, interfaceIndexerDecla274, interProperty276, enumDeclaration243, enumDeclarations245, att248, name251, exp254, name288, interAccessor291, att294, newAtt297, otherAtt300, type303, name306, parameterList309, className312, parameterList278, interAccessors280, type282, name285, fieldDeclaration324, methodDeclaration326, constDeclaration328, propertyDeclaration330, eventDeclaration332, indexDeclaration334, typeDeclaration336, opDeclaration339, constructorDeclaration341, destructorDeclaration343, classBase315, classBody317, classAtt319, classDeclaration322, name352, emptyBlock355, constrDeclarator358, emptyBlock360, className363, formalList366, constInitializer369, arg371, staticDeclaration345, name347, emptyBlock350, opDeclarator376, emptyBlock378, type381, firstType384, conversionName386, binType389, otherName391, secondType394, args373, secondName397, otherType400, name402, indexerDeclarator405, accDeclaration407, type410, formalList413, qualifiedId416, att1419, att424, removAccessor427, att429, getAcc432, att2434, setAcc437, methodHeader439, maybeEmpty441, typeOrVoid444, addAccessor422, formalParameters450, parameterArray453, att455, array458, name461, fixParameter464, fixParameters465, Att468, type471, qualifiedIdentifier447, name474, name477, formalParameters480, type483, variableName486, variable489, name492, exp495, tipo516, constDeclarator519, qIDs498, constDeclarators522, id501, ids504, labelStat507, declareStat508, embeddedStat510, localVariableDeclaration512, localCOnstant514, id525, stat528, maybeEmpty531, statExp534, selectionStat536, resourcAquisition550, iterationStat538, embeddedStat552, tipo555, variable558, variables561, exp564, embeddedStat567, block570, catchClauses573, finally575, jumpStat540, tryStat542, block544, lockStat546, usingStat548, specCatchClause587, block590, classType593, qualiId596, id599, block602, breakStat605, continueStat607, gotoStat609, returnStat611, throwStat613, expression615, finallyClause577, block580, speciCatchClause583, genCatchClause585, whileStatement627, doStatement629, forStatement631, foreachStatement633, expression618, id621, expression624, expression641, embeddedStatement644, forInitializer647, expression649, statementExpressionList652, embeddedStatement654, localVariableDeclaration657, tipo635, id638, tipo669, argumentList672, primaryExpression675, unaryExpression678, expression681, embeddedStatement684, expression687, statementExpressionList660, expression690, list663, lists666, ifStatement696, switchStatement698, expression700, switchSection703, switchlabel705, statement707, expression710, embeddedStatement693, expression713, embeddedStatement716, elsePart719, embeddedStatement721, statement724},
    generalizations={gen_cSharp_AttributeList_AttributeSection, gen_cSharp_Expression_VariableInitializer, gen_cSharp_Expression_Argument, gen_cSharp_Expression_ResourceAquisition, gen_cSharp_Type_EventDeclaration, gen_cSharp_Type_PropertyDeclaration, gen_cSharp_Type_FieldDeclaration, gen_cSharp_Type_ConstantDeclaration, gen_cSharp_ArrayInitializer_VariableInitializer, gen_cSharp_IntegralType_BuiltInType, gen_cSharp_NonArrayType_ArrayType, gen_cSharp_BuiltInClassType_BuiltInType, gen_cSharp_BuiltInClassType_ClassBase, gen_cSharp_ArgumentList_ConstructorInitializer, gen_cSharp_ConversionOperatorDeclarator_OperatorDeclarator, gen_cSharp_BinaryOperatorDeclarator_OperatorDeclarator, gen_cSharp_UnaryOperatorDeclarator_OperatorDeclarator, gen_cSharp_FixedParameters_FormalParameterList, gen_cSharp_TypeOrVoid_DelegateDeclaration, gen_cSharp_LocalVariableDeclaration_ResourceAquisition, gen_cSharp_Block_RemoveAccessorDeclaration, gen_cSharp_Block_AddAccessorDeclaration, gen_cSharp_Block_MaybeEmptyBlock, gen_cSharp_MaybeEmptyBlock_SetAccessorDeclaration, gen_cSharp_MaybeEmptyBlock_GetAccessorDeclaration, gen_cSharp_SByte_IntegralType, gen_cSharp_Byte_IntegralType, gen_cSharp_Double_BuiltInType, gen_cSharp_Object_BuiltInClassType, gen_cSharp_String_BuiltInClassType, gen_cSharp_Void_TypeOrVoid, gen_cSharp_Short_IntegralType, gen_cSharp_UShort_IntegralType, gen_cSharp_Int_IntegralType, gen_cSharp_UInt_IntegralType, gen_cSharp_Long_IntegralType, gen_cSharp_ULong_IntegralType, gen_cSharp_Char_IntegralType, gen_cSharp_Bool_BuiltInType, gen_cSharp_Decimal_BuiltInType, gen_cSharp_Float_BuiltInType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)