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
javaDsl_Head = Class(name="javaDsl::Head")
javaDsl_CompilationUnit = Class(name="javaDsl::CompilationUnit")
javaDsl_PackageStatement = Class(name="javaDsl::PackageStatement")
javaDsl_EObject = Class(name="javaDsl::EObject")
javaDsl_ClassDeclaration = Class(name="javaDsl::ClassDeclaration")
javaDsl_ImportStatement = Class(name="javaDsl::ImportStatement")
javaDsl_TypeDeclaration = Class(name="javaDsl::TypeDeclaration")
javaDsl_ClassBody = Class(name="javaDsl::ClassBody")
javaDsl_ClassBodyDeclaration = Class(name="javaDsl::ClassBodyDeclaration")
javaDsl_Interfaces = Class(name="javaDsl::Interfaces")
javaDsl_MethodDeclaration = Class(name="javaDsl::MethodDeclaration")
javaDsl_StaticInitializer = Class(name="javaDsl::StaticInitializer")
ClassBodyDeclaration = Class(name="ClassBodyDeclaration")
javaDsl_Block = Class(name="javaDsl::Block")
javaDsl_ConstructorDeclaration = Class(name="javaDsl::ConstructorDeclaration")
javaDsl_ConstructorDeclarator = Class(name="javaDsl::ConstructorDeclarator")
javaDsl_Exceptions = Class(name="javaDsl::Exceptions")
javaDsl_ConstructorBody = Class(name="javaDsl::ConstructorBody")
javaDsl_ClassMemberDeclaration = Class(name="javaDsl::ClassMemberDeclaration")
javaDsl_FieldDeclaration = Class(name="javaDsl::FieldDeclaration")
javaDsl_ExplicitConstructorInvocation = Class(name="javaDsl::ExplicitConstructorInvocation")
javaDsl_BlockStatement = Class(name="javaDsl::BlockStatement")
javaDsl_ArgumentList = Class(name="javaDsl::ArgumentList")
javaDsl_VariableDeclarator = Class(name="javaDsl::VariableDeclarator")
javaDsl_FormalParameter = Class(name="javaDsl::FormalParameter")
javaDsl_Type = Class(name="javaDsl::Type")
javaDsl_ResultType = Class(name="javaDsl::ResultType")
javaDsl_MethodDeclarator = Class(name="javaDsl::MethodDeclarator")
javaDsl_VariableInitializer = Class(name="javaDsl::VariableInitializer")
javaDsl_Expression = Class(name="javaDsl::Expression")
javaDsl_MethodHeader = Class(name="javaDsl::MethodHeader")
javaDsl_InterfaceMemberDeclaration = Class(name="javaDsl::InterfaceMemberDeclaration")
javaDsl_ConstantDeclaration = Class(name="javaDsl::ConstantDeclaration")
InterfaceMemberDeclaration = Class(name="InterfaceMemberDeclaration")
javaDsl_AbstractMethodDeclaration = Class(name="javaDsl::AbstractMethodDeclaration")
javaDsl_ArrayInitializer = Class(name="javaDsl::ArrayInitializer")
VariableInitializer = Class(name="VariableInitializer")
javaDsl_InterfaceDeclaration = Class(name="javaDsl::InterfaceDeclaration")
javaDsl_ExtendsInterfaces = Class(name="javaDsl::ExtendsInterfaces")
javaDsl_StatementExpression = Class(name="javaDsl::StatementExpression")
javaDsl_InterfaceBody = Class(name="javaDsl::InterfaceBody")
javaDsl_IfStatement = Class(name="javaDsl::IfStatement")
javaDsl_SwitchStatement = Class(name="javaDsl::SwitchStatement")
javaDsl_ConstantExpression = Class(name="javaDsl::ConstantExpression")
javaDsl_WhileStatement = Class(name="javaDsl::WhileStatement")
javaDsl_DoStatement = Class(name="javaDsl::DoStatement")
javaDsl_ForStatement = Class(name="javaDsl::ForStatement")
javaDsl_ForInit = Class(name="javaDsl::ForInit")
Statement = Class(name="Statement")
javaDsl_LocalVariableDeclaration = Class(name="javaDsl::LocalVariableDeclaration")
BlockStatement = Class(name="BlockStatement")
javaDsl_Statement = Class(name="javaDsl::Statement")
javaDsl_LabeledStatement = Class(name="javaDsl::LabeledStatement")
javaDsl_ThrowsStatement = Class(name="javaDsl::ThrowsStatement")
javaDsl_SynchronizedStatement = Class(name="javaDsl::SynchronizedStatement")
javaDsl_TryStatement = Class(name="javaDsl::TryStatement")
ConstantExpression = Class(name="ConstantExpression")
PrimaryNoNewArray = Class(name="PrimaryNoNewArray")
javaDsl_AssignmentExpression = Class(name="javaDsl::AssignmentExpression")
Expression = Class(name="Expression")
javaDsl_Assignment = Class(name="javaDsl::Assignment")
StatementExpression = Class(name="StatementExpression")
AssignmentExpression = Class(name="AssignmentExpression")
javaDsl_LeftHandSide = Class(name="javaDsl::LeftHandSide")
javaDsl_ForUpdate = Class(name="javaDsl::ForUpdate")
javaDsl_BreakStatement = Class(name="javaDsl::BreakStatement")
javaDsl_ContinueStatement = Class(name="javaDsl::ContinueStatement")
javaDsl_ReturnStatement = Class(name="javaDsl::ReturnStatement")
javaDsl_ExclusiveOrExpression = Class(name="javaDsl::ExclusiveOrExpression")
javaDsl_AndExpression = Class(name="javaDsl::AndExpression")
javaDsl_EqualityExpression = Class(name="javaDsl::EqualityExpression")
javaDsl_RelationalExpression = Class(name="javaDsl::RelationalExpression")
javaDsl_ShiftExpression = Class(name="javaDsl::ShiftExpression")
javaDsl_AdditiveExpression = Class(name="javaDsl::AdditiveExpression")
javaDsl_MultiplicativeExpression = Class(name="javaDsl::MultiplicativeExpression")
javaDsl_ConditionalExpression = Class(name="javaDsl::ConditionalExpression")
javaDsl_ConditionalOrExpression = Class(name="javaDsl::ConditionalOrExpression")
javaDsl_ConditionalAndExpression = Class(name="javaDsl::ConditionalAndExpression")
javaDsl_InclusiveOrExpression = Class(name="javaDsl::InclusiveOrExpression")
javaDsl_PreIncrementExpression = Class(name="javaDsl::PreIncrementExpression")
javaDsl_NoArrayExpressionWithoutMinus = Class(name="javaDsl::NoArrayExpressionWithoutMinus")
javaDsl_PostfixExpression = Class(name="javaDsl::PostfixExpression")
javaDsl_Primary = Class(name="javaDsl::Primary")
javaDsl_MethodInvocation = Class(name="javaDsl::MethodInvocation")
javaDsl_FieldAccess = Class(name="javaDsl::FieldAccess")
LeftHandSide = Class(name="LeftHandSide")
javaDsl_NoArrayExpression = Class(name="javaDsl::NoArrayExpression")
javaDsl_CastExpression = Class(name="javaDsl::CastExpression")
NoArrayExpressionWithoutMinus = Class(name="NoArrayExpressionWithoutMinus")
javaDsl_PreDecrementExpression = Class(name="javaDsl::PreDecrementExpression")
NoArrayExpression = Class(name="NoArrayExpression")
javaDsl_PrimaryNewArray = Class(name="javaDsl::PrimaryNewArray")
javaDsl_ArrayCreationExpression = Class(name="javaDsl::ArrayCreationExpression")
javaDsl_ArrayExpression = Class(name="javaDsl::ArrayExpression")
javaDsl_PrimaryNoNewArray = Class(name="javaDsl::PrimaryNoNewArray")
Primary = Class(name="Primary")
javaDsl_ClassInstanceCreationExpression = Class(name="javaDsl::ClassInstanceCreationExpression")
javaDsl_ArrayAccess = Class(name="javaDsl::ArrayAccess")

# javaDsl_Head class attributes and methods

# javaDsl_CompilationUnit class attributes and methods

# javaDsl_PackageStatement class attributes and methods
javaDsl_PackageStatement_name: Property = Property(name="name", type=StringType)
javaDsl_PackageStatement.attributes={javaDsl_PackageStatement_name}

# javaDsl_EObject class attributes and methods

# javaDsl_ClassDeclaration class attributes and methods
javaDsl_ClassDeclaration_modifiers: Property = Property(name="modifiers", type=StringType)
javaDsl_ClassDeclaration_className: Property = Property(name="className", type=StringType)
javaDsl_ClassDeclaration_extend: Property = Property(name="extend", type=StringType)
javaDsl_ClassDeclaration.attributes={javaDsl_ClassDeclaration_modifiers, javaDsl_ClassDeclaration_className, javaDsl_ClassDeclaration_extend}

# javaDsl_ImportStatement class attributes and methods
javaDsl_ImportStatement_package: Property = Property(name="package", type=StringType)
javaDsl_ImportStatement_object: Property = Property(name="object", type=StringType)
javaDsl_ImportStatement.attributes={javaDsl_ImportStatement_package, javaDsl_ImportStatement_object}

# javaDsl_TypeDeclaration class attributes and methods
javaDsl_TypeDeclaration_doc: Property = Property(name="doc", type=StringType)
javaDsl_TypeDeclaration.attributes={javaDsl_TypeDeclaration_doc}

# javaDsl_ClassBody class attributes and methods

# javaDsl_ClassBodyDeclaration class attributes and methods

# javaDsl_Interfaces class attributes and methods
javaDsl_Interfaces_keyword: Property = Property(name="keyword", type=StringType)
javaDsl_Interfaces_interfaces: Property = Property(name="interfaces", type=StringType)
javaDsl_Interfaces.attributes={javaDsl_Interfaces_keyword, javaDsl_Interfaces_interfaces}

# javaDsl_MethodDeclaration class attributes and methods

# javaDsl_StaticInitializer class attributes and methods

# ClassBodyDeclaration class attributes and methods

# javaDsl_Block class attributes and methods

# javaDsl_ConstructorDeclaration class attributes and methods
javaDsl_ConstructorDeclaration_modifiers: Property = Property(name="modifiers", type=StringType)
javaDsl_ConstructorDeclaration.attributes={javaDsl_ConstructorDeclaration_modifiers}

# javaDsl_ConstructorDeclarator class attributes and methods
javaDsl_ConstructorDeclarator_name: Property = Property(name="name", type=StringType)
javaDsl_ConstructorDeclarator.attributes={javaDsl_ConstructorDeclarator_name}

# javaDsl_Exceptions class attributes and methods
javaDsl_Exceptions_exceptions: Property = Property(name="exceptions", type=StringType)
javaDsl_Exceptions.attributes={javaDsl_Exceptions_exceptions}

# javaDsl_ConstructorBody class attributes and methods

# javaDsl_ClassMemberDeclaration class attributes and methods

# javaDsl_FieldDeclaration class attributes and methods
javaDsl_FieldDeclaration_modifiers: Property = Property(name="modifiers", type=StringType)
javaDsl_FieldDeclaration.attributes={javaDsl_FieldDeclaration_modifiers}

# javaDsl_ExplicitConstructorInvocation class attributes and methods
javaDsl_ExplicitConstructorInvocation_keyword: Property = Property(name="keyword", type=StringType)
javaDsl_ExplicitConstructorInvocation.attributes={javaDsl_ExplicitConstructorInvocation_keyword}

# javaDsl_BlockStatement class attributes and methods

# javaDsl_ArgumentList class attributes and methods

# javaDsl_VariableDeclarator class attributes and methods
javaDsl_VariableDeclarator_name: Property = Property(name="name", type=StringType)
javaDsl_VariableDeclarator.attributes={javaDsl_VariableDeclarator_name}

# javaDsl_FormalParameter class attributes and methods
javaDsl_FormalParameter_variable: Property = Property(name="variable", type=StringType)
javaDsl_FormalParameter.attributes={javaDsl_FormalParameter_variable}

# javaDsl_Type class attributes and methods
javaDsl_Type_name: Property = Property(name="name", type=StringType)
javaDsl_Type.attributes={javaDsl_Type_name}

# javaDsl_ResultType class attributes and methods

# javaDsl_MethodDeclarator class attributes and methods
javaDsl_MethodDeclarator_name: Property = Property(name="name", type=StringType)
javaDsl_MethodDeclarator.attributes={javaDsl_MethodDeclarator_name}

# javaDsl_VariableInitializer class attributes and methods

# javaDsl_Expression class attributes and methods

# javaDsl_MethodHeader class attributes and methods
javaDsl_MethodHeader_modifiers: Property = Property(name="modifiers", type=StringType)
javaDsl_MethodHeader.attributes={javaDsl_MethodHeader_modifiers}

# javaDsl_InterfaceMemberDeclaration class attributes and methods
javaDsl_InterfaceMemberDeclaration_modifiers: Property = Property(name="modifiers", type=StringType)
javaDsl_InterfaceMemberDeclaration.attributes={javaDsl_InterfaceMemberDeclaration_modifiers}

# javaDsl_ConstantDeclaration class attributes and methods

# InterfaceMemberDeclaration class attributes and methods

# javaDsl_AbstractMethodDeclaration class attributes and methods

# javaDsl_ArrayInitializer class attributes and methods

# VariableInitializer class attributes and methods

# javaDsl_InterfaceDeclaration class attributes and methods
javaDsl_InterfaceDeclaration_modifiers: Property = Property(name="modifiers", type=StringType)
javaDsl_InterfaceDeclaration_name: Property = Property(name="name", type=StringType)
javaDsl_InterfaceDeclaration.attributes={javaDsl_InterfaceDeclaration_name, javaDsl_InterfaceDeclaration_modifiers}

# javaDsl_ExtendsInterfaces class attributes and methods
javaDsl_ExtendsInterfaces_keyword: Property = Property(name="keyword", type=StringType)
javaDsl_ExtendsInterfaces_interfaces: Property = Property(name="interfaces", type=StringType)
javaDsl_ExtendsInterfaces.attributes={javaDsl_ExtendsInterfaces_keyword, javaDsl_ExtendsInterfaces_interfaces}

# javaDsl_StatementExpression class attributes and methods

# javaDsl_InterfaceBody class attributes and methods

# javaDsl_IfStatement class attributes and methods
javaDsl_IfStatement_condition: Property = Property(name="condition", type=BooleanType)
javaDsl_IfStatement.attributes={javaDsl_IfStatement_condition}

# javaDsl_SwitchStatement class attributes and methods

# javaDsl_ConstantExpression class attributes and methods

# javaDsl_WhileStatement class attributes and methods
javaDsl_WhileStatement_condition: Property = Property(name="condition", type=BooleanType)
javaDsl_WhileStatement.attributes={javaDsl_WhileStatement_condition}

# javaDsl_DoStatement class attributes and methods
javaDsl_DoStatement_condition: Property = Property(name="condition", type=BooleanType)
javaDsl_DoStatement.attributes={javaDsl_DoStatement_condition}

# javaDsl_ForStatement class attributes and methods
javaDsl_ForStatement_condition: Property = Property(name="condition", type=BooleanType)
javaDsl_ForStatement.attributes={javaDsl_ForStatement_condition}

# javaDsl_ForInit class attributes and methods

# Statement class attributes and methods

# javaDsl_LocalVariableDeclaration class attributes and methods

# BlockStatement class attributes and methods

# javaDsl_Statement class attributes and methods

# javaDsl_LabeledStatement class attributes and methods
javaDsl_LabeledStatement_label: Property = Property(name="label", type=StringType)
javaDsl_LabeledStatement.attributes={javaDsl_LabeledStatement_label}

# javaDsl_ThrowsStatement class attributes and methods

# javaDsl_SynchronizedStatement class attributes and methods

# javaDsl_TryStatement class attributes and methods

# ConstantExpression class attributes and methods

# PrimaryNoNewArray class attributes and methods

# javaDsl_AssignmentExpression class attributes and methods

# Expression class attributes and methods

# javaDsl_Assignment class attributes and methods
javaDsl_Assignment_operator: Property = Property(name="operator", type=StringType)
javaDsl_Assignment.attributes={javaDsl_Assignment_operator}

# StatementExpression class attributes and methods

# AssignmentExpression class attributes and methods

# javaDsl_LeftHandSide class attributes and methods

# javaDsl_ForUpdate class attributes and methods

# javaDsl_BreakStatement class attributes and methods
javaDsl_BreakStatement_reference: Property = Property(name="reference", type=StringType)
javaDsl_BreakStatement.attributes={javaDsl_BreakStatement_reference}

# javaDsl_ContinueStatement class attributes and methods
javaDsl_ContinueStatement_reference: Property = Property(name="reference", type=StringType)
javaDsl_ContinueStatement.attributes={javaDsl_ContinueStatement_reference}

# javaDsl_ReturnStatement class attributes and methods

# javaDsl_ExclusiveOrExpression class attributes and methods
javaDsl_ExclusiveOrExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_ExclusiveOrExpression.attributes={javaDsl_ExclusiveOrExpression_operators}

# javaDsl_AndExpression class attributes and methods
javaDsl_AndExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_AndExpression.attributes={javaDsl_AndExpression_operators}

# javaDsl_EqualityExpression class attributes and methods
javaDsl_EqualityExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_EqualityExpression.attributes={javaDsl_EqualityExpression_operators}

# javaDsl_RelationalExpression class attributes and methods
javaDsl_RelationalExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_RelationalExpression_classes: Property = Property(name="classes", type=StringType)
javaDsl_RelationalExpression.attributes={javaDsl_RelationalExpression_classes, javaDsl_RelationalExpression_operators}

# javaDsl_ShiftExpression class attributes and methods
javaDsl_ShiftExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_ShiftExpression.attributes={javaDsl_ShiftExpression_operators}

# javaDsl_AdditiveExpression class attributes and methods
javaDsl_AdditiveExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_AdditiveExpression.attributes={javaDsl_AdditiveExpression_operators}

# javaDsl_MultiplicativeExpression class attributes and methods
javaDsl_MultiplicativeExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_MultiplicativeExpression.attributes={javaDsl_MultiplicativeExpression_operators}

# javaDsl_ConditionalExpression class attributes and methods

# javaDsl_ConditionalOrExpression class attributes and methods
javaDsl_ConditionalOrExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_ConditionalOrExpression.attributes={javaDsl_ConditionalOrExpression_operators}

# javaDsl_ConditionalAndExpression class attributes and methods
javaDsl_ConditionalAndExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_ConditionalAndExpression.attributes={javaDsl_ConditionalAndExpression_operators}

# javaDsl_InclusiveOrExpression class attributes and methods
javaDsl_InclusiveOrExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_InclusiveOrExpression.attributes={javaDsl_InclusiveOrExpression_operators}

# javaDsl_PreIncrementExpression class attributes and methods

# javaDsl_NoArrayExpressionWithoutMinus class attributes and methods

# javaDsl_PostfixExpression class attributes and methods
javaDsl_PostfixExpression_reference: Property = Property(name="reference", type=StringType)
javaDsl_PostfixExpression_operators: Property = Property(name="operators", type=StringType)
javaDsl_PostfixExpression.attributes={javaDsl_PostfixExpression_operators, javaDsl_PostfixExpression_reference}

# javaDsl_Primary class attributes and methods
javaDsl_Primary_fields: Property = Property(name="fields", type=StringType)
javaDsl_Primary.attributes={javaDsl_Primary_fields}

# javaDsl_MethodInvocation class attributes and methods
javaDsl_MethodInvocation_method: Property = Property(name="method", type=StringType)
javaDsl_MethodInvocation_keyword: Property = Property(name="keyword", type=StringType)
javaDsl_MethodInvocation.attributes={javaDsl_MethodInvocation_method, javaDsl_MethodInvocation_keyword}

# javaDsl_FieldAccess class attributes and methods
javaDsl_FieldAccess_field: Property = Property(name="field", type=StringType)
javaDsl_FieldAccess_keyword: Property = Property(name="keyword", type=StringType)
javaDsl_FieldAccess.attributes={javaDsl_FieldAccess_keyword, javaDsl_FieldAccess_field}

# LeftHandSide class attributes and methods

# javaDsl_NoArrayExpression class attributes and methods
javaDsl_NoArrayExpression_operator: Property = Property(name="operator", type=StringType)
javaDsl_NoArrayExpression.attributes={javaDsl_NoArrayExpression_operator}

# javaDsl_CastExpression class attributes and methods
javaDsl_CastExpression_type: Property = Property(name="type", type=StringType)
javaDsl_CastExpression.attributes={javaDsl_CastExpression_type}

# NoArrayExpressionWithoutMinus class attributes and methods

# javaDsl_PreDecrementExpression class attributes and methods

# NoArrayExpression class attributes and methods

# javaDsl_PrimaryNewArray class attributes and methods

# javaDsl_ArrayCreationExpression class attributes and methods
javaDsl_ArrayCreationExpression_type: Property = Property(name="type", type=StringType)
javaDsl_ArrayCreationExpression_layers: Property = Property(name="layers", type=StringType)
javaDsl_ArrayCreationExpression.attributes={javaDsl_ArrayCreationExpression_type, javaDsl_ArrayCreationExpression_layers}

# javaDsl_ArrayExpression class attributes and methods

# javaDsl_PrimaryNoNewArray class attributes and methods
javaDsl_PrimaryNoNewArray_reference: Property = Property(name="reference", type=StringType)
javaDsl_PrimaryNoNewArray_literal: Property = Property(name="literal", type=StringType)
javaDsl_PrimaryNoNewArray_keyword: Property = Property(name="keyword", type=StringType)
javaDsl_PrimaryNoNewArray_method: Property = Property(name="method", type=StringType)
javaDsl_PrimaryNoNewArray.attributes={javaDsl_PrimaryNoNewArray_literal, javaDsl_PrimaryNoNewArray_method, javaDsl_PrimaryNoNewArray_reference, javaDsl_PrimaryNoNewArray_keyword}

# Primary class attributes and methods

# javaDsl_ClassInstanceCreationExpression class attributes and methods
javaDsl_ClassInstanceCreationExpression_type: Property = Property(name="type", type=StringType)
javaDsl_ClassInstanceCreationExpression.attributes={javaDsl_ClassInstanceCreationExpression_type}

# javaDsl_ArrayAccess class attributes and methods
javaDsl_ArrayAccess_reference: Property = Property(name="reference", type=StringType)
javaDsl_ArrayAccess.attributes={javaDsl_ArrayAccess_reference}

# Relationships
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="javaDsl_CompilationUnit", type=javaDsl_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_Head", type=javaDsl_CompilationUnit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
package1: BinaryAssociation = BinaryAssociation(
    name="package1",
    ends={
        Property(name="javaDsl_PackageStatement", type=javaDsl_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_CompilationUnit2", type=javaDsl_PackageStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name7: BinaryAssociation = BinaryAssociation(
    name="name7",
    ends={
        Property(name="javaDsl_EObject", type=javaDsl_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_TypeDeclaration8", type=javaDsl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports3: BinaryAssociation = BinaryAssociation(
    name="imports3",
    ends={
        Property(name="javaDsl_ImportStatement", type=javaDsl_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_CompilationUnit4", type=javaDsl_ImportStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDeclarations5: BinaryAssociation = BinaryAssociation(
    name="typeDeclarations5",
    ends={
        Property(name="javaDsl_TypeDeclaration", type=javaDsl_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_CompilationUnit6", type=javaDsl_TypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body10: BinaryAssociation = BinaryAssociation(
    name="body10",
    ends={
        Property(name="javaDsl_ClassBody", type=javaDsl_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ClassDeclaration11", type=javaDsl_ClassBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations12: BinaryAssociation = BinaryAssociation(
    name="declarations12",
    ends={
        Property(name="javaDsl_ClassBodyDeclaration", type=javaDsl_ClassBody, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ClassBody13", type=javaDsl_ClassBodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements9: BinaryAssociation = BinaryAssociation(
    name="implements9",
    ends={
        Property(name="javaDsl_Interfaces", type=javaDsl_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ClassDeclaration", type=javaDsl_Interfaces, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method18: BinaryAssociation = BinaryAssociation(
    name="method18",
    ends={
        Property(name="javaDsl_MethodDeclaration", type=javaDsl_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ClassMemberDeclaration19", type=javaDsl_MethodDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
code20: BinaryAssociation = BinaryAssociation(
    name="code20",
    ends={
        Property(name="javaDsl_Block", type=javaDsl_StaticInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_StaticInitializer", type=javaDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
header21: BinaryAssociation = BinaryAssociation(
    name="header21",
    ends={
        Property(name="javaDsl_ConstructorDeclarator", type=javaDsl_ConstructorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConstructorDeclaration", type=javaDsl_ConstructorDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throws22: BinaryAssociation = BinaryAssociation(
    name="throws22",
    ends={
        Property(name="javaDsl_Exceptions", type=javaDsl_ConstructorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConstructorDeclaration23", type=javaDsl_Exceptions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body24: BinaryAssociation = BinaryAssociation(
    name="body24",
    ends={
        Property(name="javaDsl_ConstructorBody", type=javaDsl_ConstructorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConstructorDeclaration25", type=javaDsl_ConstructorBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member14: BinaryAssociation = BinaryAssociation(
    name="member14",
    ends={
        Property(name="javaDsl_ClassMemberDeclaration", type=javaDsl_ClassBodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ClassBodyDeclaration15", type=javaDsl_ClassMemberDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field16: BinaryAssociation = BinaryAssociation(
    name="field16",
    ends={
        Property(name="javaDsl_FieldDeclaration", type=javaDsl_ClassMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ClassMemberDeclaration17", type=javaDsl_FieldDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invocation30: BinaryAssociation = BinaryAssociation(
    name="invocation30",
    ends={
        Property(name="javaDsl_ExplicitConstructorInvocation", type=javaDsl_ConstructorBody, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConstructorBody31", type=javaDsl_ExplicitConstructorInvocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations32: BinaryAssociation = BinaryAssociation(
    name="declarations32",
    ends={
        Property(name="javaDsl_BlockStatement", type=javaDsl_ConstructorBody, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConstructorBody33", type=javaDsl_BlockStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args34: BinaryAssociation = BinaryAssociation(
    name="args34",
    ends={
        Property(name="javaDsl_ArgumentList", type=javaDsl_ExplicitConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ExplicitConstructorInvocation35", type=javaDsl_ArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type36: BinaryAssociation = BinaryAssociation(
    name="type36",
    ends={
        Property(name="javaDsl_Type38", type=javaDsl_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_FieldDeclaration37", type=javaDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables39: BinaryAssociation = BinaryAssociation(
    name="variables39",
    ends={
        Property(name="javaDsl_VariableDeclarator", type=javaDsl_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_FieldDeclaration40", type=javaDsl_VariableDeclarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params26: BinaryAssociation = BinaryAssociation(
    name="params26",
    ends={
        Property(name="javaDsl_FormalParameter", type=javaDsl_ConstructorDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConstructorDeclarator27", type=javaDsl_FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="javaDsl_Type", type=javaDsl_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_FormalParameter29", type=javaDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body47: BinaryAssociation = BinaryAssociation(
    name="body47",
    ends={
        Property(name="javaDsl_MethodDeclaration48", type=javaDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="javaDsl_Block49", type=javaDsl_MethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
returnType50: BinaryAssociation = BinaryAssociation(
    name="returnType50",
    ends={
        Property(name="javaDsl_ResultType", type=javaDsl_MethodHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_MethodHeader51", type=javaDsl_ResultType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
header52: BinaryAssociation = BinaryAssociation(
    name="header52",
    ends={
        Property(name="javaDsl_MethodDeclarator", type=javaDsl_MethodHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_MethodHeader53", type=javaDsl_MethodDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throws54: BinaryAssociation = BinaryAssociation(
    name="throws54",
    ends={
        Property(name="javaDsl_Exceptions56", type=javaDsl_MethodHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_MethodHeader55", type=javaDsl_Exceptions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type57: BinaryAssociation = BinaryAssociation(
    name="type57",
    ends={
        Property(name="javaDsl_Type59", type=javaDsl_ResultType, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ResultType58", type=javaDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params60: BinaryAssociation = BinaryAssociation(
    name="params60",
    ends={
        Property(name="javaDsl_FormalParameter62", type=javaDsl_MethodDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_MethodDeclarator61", type=javaDsl_FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value41: BinaryAssociation = BinaryAssociation(
    name="value41",
    ends={
        Property(name="javaDsl_VariableInitializer", type=javaDsl_VariableDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_VariableDeclarator42", type=javaDsl_VariableInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp43: BinaryAssociation = BinaryAssociation(
    name="exp43",
    ends={
        Property(name="javaDsl_Expression", type=javaDsl_VariableInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_VariableInitializer44", type=javaDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature45: BinaryAssociation = BinaryAssociation(
    name="signature45",
    ends={
        Property(name="javaDsl_MethodHeader", type=javaDsl_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_MethodDeclaration46", type=javaDsl_MethodHeader, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations66: BinaryAssociation = BinaryAssociation(
    name="declarations66",
    ends={
        Property(name="javaDsl_InterfaceMemberDeclaration", type=javaDsl_InterfaceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_InterfaceBody67", type=javaDsl_InterfaceMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type68: BinaryAssociation = BinaryAssociation(
    name="type68",
    ends={
        Property(name="javaDsl_Type69", type=javaDsl_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConstantDeclaration", type=javaDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant70: BinaryAssociation = BinaryAssociation(
    name="constant70",
    ends={
        Property(name="javaDsl_VariableDeclarator72", type=javaDsl_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConstantDeclaration71", type=javaDsl_VariableDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType73: BinaryAssociation = BinaryAssociation(
    name="returnType73",
    ends={
        Property(name="javaDsl_ResultType74", type=javaDsl_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_AbstractMethodDeclaration", type=javaDsl_ResultType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
header75: BinaryAssociation = BinaryAssociation(
    name="header75",
    ends={
        Property(name="javaDsl_MethodDeclarator77", type=javaDsl_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_AbstractMethodDeclaration76", type=javaDsl_MethodDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throws78: BinaryAssociation = BinaryAssociation(
    name="throws78",
    ends={
        Property(name="javaDsl_Exceptions80", type=javaDsl_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_AbstractMethodDeclaration79", type=javaDsl_Exceptions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends63: BinaryAssociation = BinaryAssociation(
    name="extends63",
    ends={
        Property(name="javaDsl_ExtendsInterfaces", type=javaDsl_InterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_InterfaceDeclaration", type=javaDsl_ExtendsInterfaces, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body64: BinaryAssociation = BinaryAssociation(
    name="body64",
    ends={
        Property(name="javaDsl_InterfaceBody", type=javaDsl_InterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_InterfaceDeclaration65", type=javaDsl_InterfaceBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then92: BinaryAssociation = BinaryAssociation(
    name="then92",
    ends={
        Property(name="javaDsl_Statement93", type=javaDsl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_IfStatement", type=javaDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else94: BinaryAssociation = BinaryAssociation(
    name="else94",
    ends={
        Property(name="javaDsl_Statement96", type=javaDsl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_IfStatement95", type=javaDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression97: BinaryAssociation = BinaryAssociation(
    name="expression97",
    ends={
        Property(name="javaDsl_Expression98", type=javaDsl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_SwitchStatement", type=javaDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constants99: BinaryAssociation = BinaryAssociation(
    name="constants99",
    ends={
        Property(name="javaDsl_ConstantExpression", type=javaDsl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_SwitchStatement100", type=javaDsl_ConstantExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements101: BinaryAssociation = BinaryAssociation(
    name="statements101",
    ends={
        Property(name="javaDsl_BlockStatement103", type=javaDsl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_SwitchStatement102", type=javaDsl_BlockStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement104: BinaryAssociation = BinaryAssociation(
    name="statement104",
    ends={
        Property(name="javaDsl_Statement105", type=javaDsl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_WhileStatement", type=javaDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement106: BinaryAssociation = BinaryAssociation(
    name="statement106",
    ends={
        Property(name="javaDsl_Statement107", type=javaDsl_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_DoStatement", type=javaDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values81: BinaryAssociation = BinaryAssociation(
    name="values81",
    ends={
        Property(name="javaDsl_VariableInitializer82", type=javaDsl_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ArrayInitializer", type=javaDsl_VariableInitializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initExpr108: BinaryAssociation = BinaryAssociation(
    name="initExpr108",
    ends={
        Property(name="javaDsl_ForInit", type=javaDsl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ForStatement", type=javaDsl_ForInit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations83: BinaryAssociation = BinaryAssociation(
    name="declarations83",
    ends={
        Property(name="javaDsl_BlockStatement85", type=javaDsl_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_Block84", type=javaDsl_BlockStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type86: BinaryAssociation = BinaryAssociation(
    name="type86",
    ends={
        Property(name="javaDsl_Type87", type=javaDsl_LocalVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_LocalVariableDeclaration", type=javaDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables88: BinaryAssociation = BinaryAssociation(
    name="variables88",
    ends={
        Property(name="javaDsl_VariableDeclarator90", type=javaDsl_LocalVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_LocalVariableDeclaration89", type=javaDsl_VariableDeclarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement91: BinaryAssociation = BinaryAssociation(
    name="statement91",
    ends={
        Property(name="javaDsl_Statement", type=javaDsl_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_LabeledStatement", type=javaDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression122: BinaryAssociation = BinaryAssociation(
    name="expression122",
    ends={
        Property(name="javaDsl_Expression123", type=javaDsl_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ReturnStatement", type=javaDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression124: BinaryAssociation = BinaryAssociation(
    name="expression124",
    ends={
        Property(name="javaDsl_Expression125", type=javaDsl_ThrowsStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ThrowsStatement", type=javaDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="javaDsl_Expression127", type=javaDsl_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_SynchronizedStatement", type=javaDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body128: BinaryAssociation = BinaryAssociation(
    name="body128",
    ends={
        Property(name="javaDsl_Block130", type=javaDsl_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_SynchronizedStatement129", type=javaDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryBody131: BinaryAssociation = BinaryAssociation(
    name="tryBody131",
    ends={
        Property(name="javaDsl_Block132", type=javaDsl_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_TryStatement", type=javaDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params133: BinaryAssociation = BinaryAssociation(
    name="params133",
    ends={
        Property(name="javaDsl_FormalParameter135", type=javaDsl_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_TryStatement134", type=javaDsl_FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchesBody136: BinaryAssociation = BinaryAssociation(
    name="catchesBody136",
    ends={
        Property(name="javaDsl_Block138", type=javaDsl_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_TryStatement137", type=javaDsl_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finallyBody139: BinaryAssociation = BinaryAssociation(
    name="finallyBody139",
    ends={
        Property(name="javaDsl_Block141", type=javaDsl_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_TryStatement140", type=javaDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object142: BinaryAssociation = BinaryAssociation(
    name="object142",
    ends={
        Property(name="javaDsl_LeftHandSide", type=javaDsl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_Assignment", type=javaDsl_LeftHandSide, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateExpr109: BinaryAssociation = BinaryAssociation(
    name="updateExpr109",
    ends={
        Property(name="javaDsl_ForUpdate", type=javaDsl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ForStatement110", type=javaDsl_ForUpdate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement111: BinaryAssociation = BinaryAssociation(
    name="statement111",
    ends={
        Property(name="javaDsl_Statement113", type=javaDsl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ForStatement112", type=javaDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions114: BinaryAssociation = BinaryAssociation(
    name="expressions114",
    ends={
        Property(name="javaDsl_StatementExpression", type=javaDsl_ForInit, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ForInit115", type=javaDsl_StatementExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariable116: BinaryAssociation = BinaryAssociation(
    name="localVariable116",
    ends={
        Property(name="javaDsl_LocalVariableDeclaration118", type=javaDsl_ForInit, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ForInit117", type=javaDsl_LocalVariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions119: BinaryAssociation = BinaryAssociation(
    name="expressions119",
    ends={
        Property(name="javaDsl_StatementExpression121", type=javaDsl_ForUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ForUpdate120", type=javaDsl_StatementExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands156: BinaryAssociation = BinaryAssociation(
    name="operands156",
    ends={
        Property(name="javaDsl_ExclusiveOrExpression", type=javaDsl_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_InclusiveOrExpression157", type=javaDsl_ExclusiveOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands158: BinaryAssociation = BinaryAssociation(
    name="operands158",
    ends={
        Property(name="javaDsl_AndExpression", type=javaDsl_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ExclusiveOrExpression159", type=javaDsl_AndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands160: BinaryAssociation = BinaryAssociation(
    name="operands160",
    ends={
        Property(name="javaDsl_EqualityExpression", type=javaDsl_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_AndExpression161", type=javaDsl_EqualityExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands162: BinaryAssociation = BinaryAssociation(
    name="operands162",
    ends={
        Property(name="javaDsl_RelationalExpression", type=javaDsl_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_EqualityExpression163", type=javaDsl_RelationalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands164: BinaryAssociation = BinaryAssociation(
    name="operands164",
    ends={
        Property(name="javaDsl_ShiftExpression", type=javaDsl_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_RelationalExpression165", type=javaDsl_ShiftExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands166: BinaryAssociation = BinaryAssociation(
    name="operands166",
    ends={
        Property(name="javaDsl_AdditiveExpression", type=javaDsl_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ShiftExpression167", type=javaDsl_AdditiveExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands168: BinaryAssociation = BinaryAssociation(
    name="operands168",
    ends={
        Property(name="javaDsl_MultiplicativeExpression", type=javaDsl_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_AdditiveExpression169", type=javaDsl_MultiplicativeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value143: BinaryAssociation = BinaryAssociation(
    name="value143",
    ends={
        Property(name="javaDsl_AssignmentExpression", type=javaDsl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_Assignment144", type=javaDsl_AssignmentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition145: BinaryAssociation = BinaryAssociation(
    name="condition145",
    ends={
        Property(name="javaDsl_ConditionalOrExpression", type=javaDsl_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConditionalExpression", type=javaDsl_ConditionalOrExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then146: BinaryAssociation = BinaryAssociation(
    name="then146",
    ends={
        Property(name="javaDsl_Expression148", type=javaDsl_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConditionalExpression147", type=javaDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else150: BinaryAssociation = BinaryAssociation(
    name="else150",
    ends={
        Property(name="javaDsl_ConditionalExpression151", type=javaDsl_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConditionalExpression149", type=javaDsl_ConditionalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operands152: BinaryAssociation = BinaryAssociation(
    name="operands152",
    ends={
        Property(name="javaDsl_ConditionalAndExpression", type=javaDsl_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConditionalOrExpression153", type=javaDsl_ConditionalAndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operands154: BinaryAssociation = BinaryAssociation(
    name="operands154",
    ends={
        Property(name="javaDsl_InclusiveOrExpression", type=javaDsl_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ConditionalAndExpression155", type=javaDsl_InclusiveOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object175: BinaryAssociation = BinaryAssociation(
    name="object175",
    ends={
        Property(name="javaDsl_Primary", type=javaDsl_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_PostfixExpression", type=javaDsl_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args176: BinaryAssociation = BinaryAssociation(
    name="args176",
    ends={
        Property(name="javaDsl_ArgumentList177", type=javaDsl_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_MethodInvocation", type=javaDsl_ArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object178: BinaryAssociation = BinaryAssociation(
    name="object178",
    ends={
        Property(name="javaDsl_Primary180", type=javaDsl_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_MethodInvocation179", type=javaDsl_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object181: BinaryAssociation = BinaryAssociation(
    name="object181",
    ends={
        Property(name="javaDsl_Primary182", type=javaDsl_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_FieldAccess", type=javaDsl_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operands170: BinaryAssociation = BinaryAssociation(
    name="operands170",
    ends={
        Property(name="javaDsl_NoArrayExpression", type=javaDsl_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_MultiplicativeExpression171", type=javaDsl_NoArrayExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand173: BinaryAssociation = BinaryAssociation(
    name="operand173",
    ends={
        Property(name="javaDsl_NoArrayExpression174", type=javaDsl_NoArrayExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_NoArrayExpression172", type=javaDsl_NoArrayExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array189: BinaryAssociation = BinaryAssociation(
    name="array189",
    ends={
        Property(name="javaDsl_ArrayCreationExpression", type=javaDsl_PrimaryNewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_PrimaryNewArray", type=javaDsl_ArrayCreationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args190: BinaryAssociation = BinaryAssociation(
    name="args190",
    ends={
        Property(name="javaDsl_ArgumentList192", type=javaDsl_ClassInstanceCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ClassInstanceCreationExpression191", type=javaDsl_ArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations193: BinaryAssociation = BinaryAssociation(
    name="declarations193",
    ends={
        Property(name="javaDsl_Expression195", type=javaDsl_ArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ArgumentList194", type=javaDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimensions196: BinaryAssociation = BinaryAssociation(
    name="dimensions196",
    ends={
        Property(name="javaDsl_ArrayExpression198", type=javaDsl_ArrayCreationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ArrayCreationExpression197", type=javaDsl_ArrayExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
index199: BinaryAssociation = BinaryAssociation(
    name="index199",
    ends={
        Property(name="javaDsl_Expression201", type=javaDsl_ArrayExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ArrayExpression200", type=javaDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args183: BinaryAssociation = BinaryAssociation(
    name="args183",
    ends={
        Property(name="javaDsl_ArgumentList185", type=javaDsl_Primary, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_Primary184", type=javaDsl_ArgumentList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimensions186: BinaryAssociation = BinaryAssociation(
    name="dimensions186",
    ends={
        Property(name="javaDsl_ArrayExpression", type=javaDsl_Primary, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_Primary187", type=javaDsl_ArrayExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class188: BinaryAssociation = BinaryAssociation(
    name="class188",
    ends={
        Property(name="javaDsl_ClassInstanceCreationExpression", type=javaDsl_PrimaryNoNewArray, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_PrimaryNoNewArray", type=javaDsl_ClassInstanceCreationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array202: BinaryAssociation = BinaryAssociation(
    name="array202",
    ends={
        Property(name="javaDsl_PrimaryNoNewArray203", type=javaDsl_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ArrayAccess", type=javaDsl_PrimaryNoNewArray, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field204: BinaryAssociation = BinaryAssociation(
    name="field204",
    ends={
        Property(name="javaDsl_ArrayExpression206", type=javaDsl_ArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="javaDsl_ArrayAccess205", type=javaDsl_ArrayExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_javaDsl_StaticInitializer_ClassBodyDeclaration = Generalization(general=ClassBodyDeclaration, specific=javaDsl_StaticInitializer)
gen_javaDsl_ConstructorDeclaration_ClassBodyDeclaration = Generalization(general=ClassBodyDeclaration, specific=javaDsl_ConstructorDeclaration)
gen_javaDsl_ConstantDeclaration_InterfaceMemberDeclaration = Generalization(general=InterfaceMemberDeclaration, specific=javaDsl_ConstantDeclaration)
gen_javaDsl_AbstractMethodDeclaration_InterfaceMemberDeclaration = Generalization(general=InterfaceMemberDeclaration, specific=javaDsl_AbstractMethodDeclaration)
gen_javaDsl_StatementExpression_Statement = Generalization(general=Statement, specific=javaDsl_StatementExpression)
gen_javaDsl_IfStatement_Statement = Generalization(general=Statement, specific=javaDsl_IfStatement)
gen_javaDsl_SwitchStatement_Statement = Generalization(general=Statement, specific=javaDsl_SwitchStatement)
gen_javaDsl_WhileStatement_Statement = Generalization(general=Statement, specific=javaDsl_WhileStatement)
gen_javaDsl_DoStatement_Statement = Generalization(general=Statement, specific=javaDsl_DoStatement)
gen_javaDsl_ArrayInitializer_VariableInitializer = Generalization(general=VariableInitializer, specific=javaDsl_ArrayInitializer)
gen_javaDsl_ForStatement_Statement = Generalization(general=Statement, specific=javaDsl_ForStatement)
gen_javaDsl_Block_Statement = Generalization(general=Statement, specific=javaDsl_Block)
gen_javaDsl_LocalVariableDeclaration_BlockStatement = Generalization(general=BlockStatement, specific=javaDsl_LocalVariableDeclaration)
gen_javaDsl_Statement_BlockStatement = Generalization(general=BlockStatement, specific=javaDsl_Statement)
gen_javaDsl_LabeledStatement_Statement = Generalization(general=Statement, specific=javaDsl_LabeledStatement)
gen_javaDsl_ThrowsStatement_Statement = Generalization(general=Statement, specific=javaDsl_ThrowsStatement)
gen_javaDsl_SynchronizedStatement_Statement = Generalization(general=Statement, specific=javaDsl_SynchronizedStatement)
gen_javaDsl_TryStatement_Statement = Generalization(general=Statement, specific=javaDsl_TryStatement)
gen_javaDsl_Expression_ConstantExpression = Generalization(general=ConstantExpression, specific=javaDsl_Expression)
gen_javaDsl_Expression_PrimaryNoNewArray = Generalization(general=PrimaryNoNewArray, specific=javaDsl_Expression)
gen_javaDsl_AssignmentExpression_Expression = Generalization(general=Expression, specific=javaDsl_AssignmentExpression)
gen_javaDsl_Assignment_StatementExpression = Generalization(general=StatementExpression, specific=javaDsl_Assignment)
gen_javaDsl_Assignment_AssignmentExpression = Generalization(general=AssignmentExpression, specific=javaDsl_Assignment)
gen_javaDsl_BreakStatement_Statement = Generalization(general=Statement, specific=javaDsl_BreakStatement)
gen_javaDsl_ContinueStatement_Statement = Generalization(general=Statement, specific=javaDsl_ContinueStatement)
gen_javaDsl_ReturnStatement_Statement = Generalization(general=Statement, specific=javaDsl_ReturnStatement)
gen_javaDsl_ConditionalExpression_AssignmentExpression = Generalization(general=AssignmentExpression, specific=javaDsl_ConditionalExpression)
gen_javaDsl_PreIncrementExpression_StatementExpression = Generalization(general=StatementExpression, specific=javaDsl_PreIncrementExpression)
gen_javaDsl_PreIncrementExpression_NoArrayExpression = Generalization(general=NoArrayExpression, specific=javaDsl_PreIncrementExpression)
gen_javaDsl_NoArrayExpressionWithoutMinus_NoArrayExpression = Generalization(general=NoArrayExpression, specific=javaDsl_NoArrayExpressionWithoutMinus)
gen_javaDsl_PostfixExpression_StatementExpression = Generalization(general=StatementExpression, specific=javaDsl_PostfixExpression)
gen_javaDsl_PostfixExpression_NoArrayExpressionWithoutMinus = Generalization(general=NoArrayExpressionWithoutMinus, specific=javaDsl_PostfixExpression)
gen_javaDsl_MethodInvocation_StatementExpression = Generalization(general=StatementExpression, specific=javaDsl_MethodInvocation)
gen_javaDsl_FieldAccess_LeftHandSide = Generalization(general=LeftHandSide, specific=javaDsl_FieldAccess)
gen_javaDsl_CastExpression_NoArrayExpressionWithoutMinus = Generalization(general=NoArrayExpressionWithoutMinus, specific=javaDsl_CastExpression)
gen_javaDsl_PreDecrementExpression_StatementExpression = Generalization(general=StatementExpression, specific=javaDsl_PreDecrementExpression)
gen_javaDsl_PreDecrementExpression_NoArrayExpression = Generalization(general=NoArrayExpression, specific=javaDsl_PreDecrementExpression)
gen_javaDsl_PrimaryNewArray_Primary = Generalization(general=Primary, specific=javaDsl_PrimaryNewArray)
gen_javaDsl_ClassInstanceCreationExpression_StatementExpression = Generalization(general=StatementExpression, specific=javaDsl_ClassInstanceCreationExpression)
gen_javaDsl_PrimaryNoNewArray_Primary = Generalization(general=Primary, specific=javaDsl_PrimaryNoNewArray)
gen_javaDsl_ArrayAccess_LeftHandSide = Generalization(general=LeftHandSide, specific=javaDsl_ArrayAccess)

# Domain Model
domain_model = DomainModel(
    name="javaDsl",
    types={javaDsl_Head, javaDsl_CompilationUnit, javaDsl_PackageStatement, javaDsl_EObject, javaDsl_ClassDeclaration, javaDsl_ImportStatement, javaDsl_TypeDeclaration, javaDsl_ClassBody, javaDsl_ClassBodyDeclaration, javaDsl_Interfaces, javaDsl_MethodDeclaration, javaDsl_StaticInitializer, ClassBodyDeclaration, javaDsl_Block, javaDsl_ConstructorDeclaration, javaDsl_ConstructorDeclarator, javaDsl_Exceptions, javaDsl_ConstructorBody, javaDsl_ClassMemberDeclaration, javaDsl_FieldDeclaration, javaDsl_ExplicitConstructorInvocation, javaDsl_BlockStatement, javaDsl_ArgumentList, javaDsl_VariableDeclarator, javaDsl_FormalParameter, javaDsl_Type, javaDsl_ResultType, javaDsl_MethodDeclarator, javaDsl_VariableInitializer, javaDsl_Expression, javaDsl_MethodHeader, javaDsl_InterfaceMemberDeclaration, javaDsl_ConstantDeclaration, InterfaceMemberDeclaration, javaDsl_AbstractMethodDeclaration, javaDsl_ArrayInitializer, VariableInitializer, javaDsl_InterfaceDeclaration, javaDsl_ExtendsInterfaces, javaDsl_StatementExpression, javaDsl_InterfaceBody, javaDsl_IfStatement, javaDsl_SwitchStatement, javaDsl_ConstantExpression, javaDsl_WhileStatement, javaDsl_DoStatement, javaDsl_ForStatement, javaDsl_ForInit, Statement, javaDsl_LocalVariableDeclaration, BlockStatement, javaDsl_Statement, javaDsl_LabeledStatement, javaDsl_ThrowsStatement, javaDsl_SynchronizedStatement, javaDsl_TryStatement, ConstantExpression, PrimaryNoNewArray, javaDsl_AssignmentExpression, Expression, javaDsl_Assignment, StatementExpression, AssignmentExpression, javaDsl_LeftHandSide, javaDsl_ForUpdate, javaDsl_BreakStatement, javaDsl_ContinueStatement, javaDsl_ReturnStatement, javaDsl_ExclusiveOrExpression, javaDsl_AndExpression, javaDsl_EqualityExpression, javaDsl_RelationalExpression, javaDsl_ShiftExpression, javaDsl_AdditiveExpression, javaDsl_MultiplicativeExpression, javaDsl_ConditionalExpression, javaDsl_ConditionalOrExpression, javaDsl_ConditionalAndExpression, javaDsl_InclusiveOrExpression, javaDsl_PreIncrementExpression, javaDsl_NoArrayExpressionWithoutMinus, javaDsl_PostfixExpression, javaDsl_Primary, javaDsl_MethodInvocation, javaDsl_FieldAccess, LeftHandSide, javaDsl_NoArrayExpression, javaDsl_CastExpression, NoArrayExpressionWithoutMinus, javaDsl_PreDecrementExpression, NoArrayExpression, javaDsl_PrimaryNewArray, javaDsl_ArrayCreationExpression, javaDsl_ArrayExpression, javaDsl_PrimaryNoNewArray, Primary, javaDsl_ClassInstanceCreationExpression, javaDsl_ArrayAccess},
    associations={program0, package1, name7, imports3, typeDeclarations5, body10, declarations12, implements9, method18, code20, header21, throws22, body24, member14, field16, invocation30, declarations32, args34, type36, variables39, params26, type28, body47, returnType50, header52, throws54, type57, params60, value41, exp43, signature45, declarations66, type68, constant70, returnType73, header75, throws78, extends63, body64, then92, else94, expression97, constants99, statements101, statement104, statement106, values81, initExpr108, declarations83, type86, variables88, statement91, expression122, expression124, expression126, body128, tryBody131, params133, catchesBody136, finallyBody139, object142, updateExpr109, statement111, expressions114, localVariable116, expressions119, operands156, operands158, operands160, operands162, operands164, operands166, operands168, value143, condition145, then146, else150, operands152, operands154, object175, args176, object178, object181, operands170, operand173, array189, args190, declarations193, dimensions196, index199, args183, dimensions186, class188, array202, field204},
    generalizations={gen_javaDsl_StaticInitializer_ClassBodyDeclaration, gen_javaDsl_ConstructorDeclaration_ClassBodyDeclaration, gen_javaDsl_ConstantDeclaration_InterfaceMemberDeclaration, gen_javaDsl_AbstractMethodDeclaration_InterfaceMemberDeclaration, gen_javaDsl_StatementExpression_Statement, gen_javaDsl_IfStatement_Statement, gen_javaDsl_SwitchStatement_Statement, gen_javaDsl_WhileStatement_Statement, gen_javaDsl_DoStatement_Statement, gen_javaDsl_ArrayInitializer_VariableInitializer, gen_javaDsl_ForStatement_Statement, gen_javaDsl_Block_Statement, gen_javaDsl_LocalVariableDeclaration_BlockStatement, gen_javaDsl_Statement_BlockStatement, gen_javaDsl_LabeledStatement_Statement, gen_javaDsl_ThrowsStatement_Statement, gen_javaDsl_SynchronizedStatement_Statement, gen_javaDsl_TryStatement_Statement, gen_javaDsl_Expression_ConstantExpression, gen_javaDsl_Expression_PrimaryNoNewArray, gen_javaDsl_AssignmentExpression_Expression, gen_javaDsl_Assignment_StatementExpression, gen_javaDsl_Assignment_AssignmentExpression, gen_javaDsl_BreakStatement_Statement, gen_javaDsl_ContinueStatement_Statement, gen_javaDsl_ReturnStatement_Statement, gen_javaDsl_ConditionalExpression_AssignmentExpression, gen_javaDsl_PreIncrementExpression_StatementExpression, gen_javaDsl_PreIncrementExpression_NoArrayExpression, gen_javaDsl_NoArrayExpressionWithoutMinus_NoArrayExpression, gen_javaDsl_PostfixExpression_StatementExpression, gen_javaDsl_PostfixExpression_NoArrayExpressionWithoutMinus, gen_javaDsl_MethodInvocation_StatementExpression, gen_javaDsl_FieldAccess_LeftHandSide, gen_javaDsl_CastExpression_NoArrayExpressionWithoutMinus, gen_javaDsl_PreDecrementExpression_StatementExpression, gen_javaDsl_PreDecrementExpression_NoArrayExpression, gen_javaDsl_PrimaryNewArray_Primary, gen_javaDsl_ClassInstanceCreationExpression_StatementExpression, gen_javaDsl_PrimaryNoNewArray_Primary, gen_javaDsl_ArrayAccess_LeftHandSide},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)