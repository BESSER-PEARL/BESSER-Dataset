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
AssignmentOperatorType: Enumeration = Enumeration(
    name="AssignmentOperatorType",
    literals={
            EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="PLUS_ASSIGN")
    }
)

InfixOperatorType: Enumeration = Enumeration(
    name="InfixOperatorType",
    literals={
            EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="CONDITIONAL_AND"),
			EnumerationLiteral(name="CONDITIONAL_OR")
    }
)

LiteralType: Enumeration = Enumeration(
    name="LiteralType",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="NULL")
    }
)

VisibilityType: Enumeration = Enumeration(
    name="VisibilityType",
    literals={
            EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PACKAGE"),
			EnumerationLiteral(name="PRIVATE")
    }
)

# Classes
JavaSimplified_Assignment = Class(name="JavaSimplified::Assignment")
Expression = Class(name="Expression")
JavaSimplified_Expression = Class(name="JavaSimplified::Expression", is_abstract=True)
JavaSimplified_CastExpression = Class(name="JavaSimplified::CastExpression")
JavaSimplified_Type = Class(name="JavaSimplified::Type")
JavaSimplified_ClassInstanceCreation = Class(name="JavaSimplified::ClassInstanceCreation")
JavaSimplified_Comment = Class(name="JavaSimplified::Comment")
JavaSimplified_CommentStatement = Class(name="JavaSimplified::CommentStatement")
Statement = Class(name="Statement")
JavaSimplified_ExpressionStatement = Class(name="JavaSimplified::ExpressionStatement")
JavaSimplified_Feature = Class(name="JavaSimplified::Feature")
CommentedElement = Class(name="CommentedElement")
NamedElement = Class(name="NamedElement")
StringElement = Class(name="StringElement")
JavaSimplified_CommentedElement = Class(name="JavaSimplified::CommentedElement", is_abstract=True)
JavaSimplified_FieldAccess = Class(name="JavaSimplified::FieldAccess")
JavaSimplified_Name = Class(name="JavaSimplified::Name")
JavaSimplified_IfStatement = Class(name="JavaSimplified::IfStatement")
JavaSimplified_Statement = Class(name="JavaSimplified::Statement")
JavaSimplified_InfixExpression = Class(name="JavaSimplified::InfixExpression")
JavaSimplified_Field = Class(name="JavaSimplified::Field")
TypedElement = Class(name="TypedElement")
Feature = Class(name="Feature")
JavaSimplified_JavaClass = Class(name="JavaSimplified::JavaClass")
JavaSimplified_Method = Class(name="JavaSimplified::Method")
JavaSimplified_JavaModel = Class(name="JavaSimplified::JavaModel")
JavaSimplified_Parameter = Class(name="JavaSimplified::Parameter")
JavaSimplified_MethodCall = Class(name="JavaSimplified::MethodCall")
JavaSimplified_Literal = Class(name="JavaSimplified::Literal")
JavaSimplified_MethodInvocation = Class(name="JavaSimplified::MethodInvocation")
JavaSimplified_NamedElement = Class(name="JavaSimplified::NamedElement", is_abstract=True)
JavaSimplified_ReturnStatement = Class(name="JavaSimplified::ReturnStatement")
JavaSimplified_TypedElement = Class(name="JavaSimplified::TypedElement", is_abstract=True)
JavaSimplified_VariableDeclarationStatement = Class(name="JavaSimplified::VariableDeclarationStatement")
JavaSimplified_StringElement = Class(name="JavaSimplified::StringElement", is_abstract=True)
JavaSimplified_ThisExpression = Class(name="JavaSimplified::ThisExpression")

# JavaSimplified_Assignment class attributes and methods
JavaSimplified_Assignment_operator: Property = Property(name="operator", type=StringType)
JavaSimplified_Assignment.attributes={JavaSimplified_Assignment_operator}

# Expression class attributes and methods

# JavaSimplified_Expression class attributes and methods

# JavaSimplified_CastExpression class attributes and methods

# JavaSimplified_Type class attributes and methods
JavaSimplified_Type_type: Property = Property(name="type", type=StringType)
JavaSimplified_Type.attributes={JavaSimplified_Type_type}

# JavaSimplified_ClassInstanceCreation class attributes and methods

# JavaSimplified_Comment class attributes and methods
JavaSimplified_Comment_isJavadoc: Property = Property(name="isJavadoc", type=BooleanType)
JavaSimplified_Comment.attributes={JavaSimplified_Comment_isJavadoc}

# JavaSimplified_CommentStatement class attributes and methods

# Statement class attributes and methods

# JavaSimplified_ExpressionStatement class attributes and methods

# JavaSimplified_Feature class attributes and methods
JavaSimplified_Feature_visibility: Property = Property(name="visibility", type=StringType)
JavaSimplified_Feature.attributes={JavaSimplified_Feature_visibility}

# CommentedElement class attributes and methods

# NamedElement class attributes and methods

# StringElement class attributes and methods

# JavaSimplified_CommentedElement class attributes and methods

# JavaSimplified_FieldAccess class attributes and methods

# JavaSimplified_Name class attributes and methods
JavaSimplified_Name_identifier: Property = Property(name="identifier", type=StringType)
JavaSimplified_Name.attributes={JavaSimplified_Name_identifier}

# JavaSimplified_IfStatement class attributes and methods

# JavaSimplified_Statement class attributes and methods

# JavaSimplified_InfixExpression class attributes and methods
JavaSimplified_InfixExpression_operator: Property = Property(name="operator", type=StringType)
JavaSimplified_InfixExpression.attributes={JavaSimplified_InfixExpression_operator}

# JavaSimplified_Field class attributes and methods

# TypedElement class attributes and methods

# Feature class attributes and methods

# JavaSimplified_JavaClass class attributes and methods
JavaSimplified_JavaClass_imports: Property = Property(name="imports", type=StringType)
JavaSimplified_JavaClass.attributes={JavaSimplified_JavaClass_imports}

# JavaSimplified_Method class attributes and methods
JavaSimplified_Method_exceptions: Property = Property(name="exceptions", type=StringType)
JavaSimplified_Method.attributes={JavaSimplified_Method_exceptions}

# JavaSimplified_JavaModel class attributes and methods

# JavaSimplified_Parameter class attributes and methods

# JavaSimplified_MethodCall class attributes and methods

# JavaSimplified_Literal class attributes and methods
JavaSimplified_Literal_type: Property = Property(name="type", type=StringType)
JavaSimplified_Literal_value: Property = Property(name="value", type=StringType)
JavaSimplified_Literal.attributes={JavaSimplified_Literal_type, JavaSimplified_Literal_value}

# JavaSimplified_MethodInvocation class attributes and methods

# JavaSimplified_NamedElement class attributes and methods

# JavaSimplified_ReturnStatement class attributes and methods

# JavaSimplified_TypedElement class attributes and methods

# JavaSimplified_VariableDeclarationStatement class attributes and methods

# JavaSimplified_StringElement class attributes and methods
JavaSimplified_StringElement_strValue: Property = Property(name="strValue", type=StringType)
JavaSimplified_StringElement.attributes={JavaSimplified_StringElement_strValue}

# JavaSimplified_ThisExpression class attributes and methods

# Relationships
expr10: BinaryAssociation = BinaryAssociation(
    name="expr10",
    ends={
        Property(name="JavaSimplified_Expression", type=JavaSimplified_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Assignment", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr4: BinaryAssociation = BinaryAssociation(
    name="expr4",
    ends={
        Property(name="JavaSimplified_Expression5", type=JavaSimplified_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_CastExpression", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="JavaSimplified_Type", type=JavaSimplified_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_CastExpression7", type=JavaSimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)
arguments8: BinaryAssociation = BinaryAssociation(
    name="arguments8",
    ends={
        Property(name="JavaSimplified_Expression9", type=JavaSimplified_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_ClassInstanceCreation", type=JavaSimplified_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
className10: BinaryAssociation = BinaryAssociation(
    name="className10",
    ends={
        Property(name="JavaSimplified_Type12", type=JavaSimplified_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_ClassInstanceCreation11", type=JavaSimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)
expr21: BinaryAssociation = BinaryAssociation(
    name="expr21",
    ends={
        Property(name="JavaSimplified_Expression3", type=JavaSimplified_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Assignment2", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comment13: BinaryAssociation = BinaryAssociation(
    name="comment13",
    ends={
        Property(name="JavaSimplified_Comment", type=JavaSimplified_CommentedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_CommentedElement", type=JavaSimplified_Comment, multiplicity=Multiplicity(0, 1))
    }
)
comment14: BinaryAssociation = BinaryAssociation(
    name="comment14",
    ends={
        Property(name="JavaSimplified_Comment15", type=JavaSimplified_CommentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_CommentStatement", type=JavaSimplified_Comment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr16: BinaryAssociation = BinaryAssociation(
    name="expr16",
    ends={
        Property(name="JavaSimplified_Expression17", type=JavaSimplified_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_ExpressionStatement", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr18: BinaryAssociation = BinaryAssociation(
    name="expr18",
    ends={
        Property(name="JavaSimplified_Expression19", type=JavaSimplified_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Field", type=JavaSimplified_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr20: BinaryAssociation = BinaryAssociation(
    name="expr20",
    ends={
        Property(name="JavaSimplified_Expression21", type=JavaSimplified_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_FieldAccess", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name22: BinaryAssociation = BinaryAssociation(
    name="name22",
    ends={
        Property(name="JavaSimplified_Name", type=JavaSimplified_FieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_FieldAccess23", type=JavaSimplified_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr24: BinaryAssociation = BinaryAssociation(
    name="expr24",
    ends={
        Property(name="JavaSimplified_Expression25", type=JavaSimplified_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_IfStatement", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifst26: BinaryAssociation = BinaryAssociation(
    name="ifst26",
    ends={
        Property(name="JavaSimplified_Statement", type=JavaSimplified_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_IfStatement27", type=JavaSimplified_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elsest28: BinaryAssociation = BinaryAssociation(
    name="elsest28",
    ends={
        Property(name="JavaSimplified_Statement30", type=JavaSimplified_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_IfStatement29", type=JavaSimplified_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr233: BinaryAssociation = BinaryAssociation(
    name="expr233",
    ends={
        Property(name="JavaSimplified_Expression35", type=JavaSimplified_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_InfixExpression34", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fields36: BinaryAssociation = BinaryAssociation(
    name="fields36",
    ends={
        Property(name="JavaSimplified_Field37", type=JavaSimplified_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_JavaClass", type=JavaSimplified_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods38: BinaryAssociation = BinaryAssociation(
    name="methods38",
    ends={
        Property(name="JavaSimplified_Method", type=JavaSimplified_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_JavaClass39", type=JavaSimplified_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes40: BinaryAssociation = BinaryAssociation(
    name="classes40",
    ends={
        Property(name="JavaSimplified_JavaClass41", type=JavaSimplified_JavaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_JavaModel", type=JavaSimplified_JavaClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr131: BinaryAssociation = BinaryAssociation(
    name="expr131",
    ends={
        Property(name="JavaSimplified_Expression32", type=JavaSimplified_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_InfixExpression", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters45: BinaryAssociation = BinaryAssociation(
    name="parameters45",
    ends={
        Property(name="JavaSimplified_Parameter", type=JavaSimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Method46", type=JavaSimplified_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements47: BinaryAssociation = BinaryAssociation(
    name="statements47",
    ends={
        Property(name="JavaSimplified_Statement49", type=JavaSimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Method48", type=JavaSimplified_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType50: BinaryAssociation = BinaryAssociation(
    name="returnType50",
    ends={
        Property(name="JavaSimplified_Type52", type=JavaSimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Method51", type=JavaSimplified_Type, multiplicity=Multiplicity(0, 1))
    }
)
arguments53: BinaryAssociation = BinaryAssociation(
    name="arguments53",
    ends={
        Property(name="JavaSimplified_Expression54", type=JavaSimplified_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_MethodCall", type=JavaSimplified_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types42: BinaryAssociation = BinaryAssociation(
    name="types42",
    ends={
        Property(name="JavaSimplified_Type44", type=JavaSimplified_JavaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_JavaModel43", type=JavaSimplified_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object61: BinaryAssociation = BinaryAssociation(
    name="object61",
    ends={
        Property(name="JavaSimplified_Name62", type=JavaSimplified_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_MethodInvocation", type=JavaSimplified_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method63: BinaryAssociation = BinaryAssociation(
    name="method63",
    ends={
        Property(name="JavaSimplified_MethodCall65", type=JavaSimplified_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_MethodInvocation64", type=JavaSimplified_MethodCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name66: BinaryAssociation = BinaryAssociation(
    name="name66",
    ends={
        Property(name="JavaSimplified_Name67", type=JavaSimplified_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_NamedElement", type=JavaSimplified_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr68: BinaryAssociation = BinaryAssociation(
    name="expr68",
    ends={
        Property(name="JavaSimplified_Expression69", type=JavaSimplified_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_ReturnStatement", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
childCall56: BinaryAssociation = BinaryAssociation(
    name="childCall56",
    ends={
        Property(name="JavaSimplified_MethodCall57", type=JavaSimplified_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_MethodCall55", type=JavaSimplified_MethodCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodName58: BinaryAssociation = BinaryAssociation(
    name="methodName58",
    ends={
        Property(name="JavaSimplified_Name60", type=JavaSimplified_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_MethodCall59", type=JavaSimplified_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="JavaSimplified_Type71", type=JavaSimplified_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_TypedElement", type=JavaSimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)
expr72: BinaryAssociation = BinaryAssociation(
    name="expr72",
    ends={
        Property(name="JavaSimplified_Expression73", type=JavaSimplified_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_VariableDeclarationStatement", type=JavaSimplified_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_JavaSimplified_Assignment_Expression = Generalization(general=Expression, specific=JavaSimplified_Assignment)
gen_JavaSimplified_CastExpression_Expression = Generalization(general=Expression, specific=JavaSimplified_CastExpression)
gen_JavaSimplified_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=JavaSimplified_ClassInstanceCreation)
gen_JavaSimplified_CommentStatement_Statement = Generalization(general=Statement, specific=JavaSimplified_CommentStatement)
gen_JavaSimplified_Expression_StringElement = Generalization(general=StringElement, specific=JavaSimplified_Expression)
gen_JavaSimplified_ExpressionStatement_Statement = Generalization(general=Statement, specific=JavaSimplified_ExpressionStatement)
gen_JavaSimplified_Feature_CommentedElement = Generalization(general=CommentedElement, specific=JavaSimplified_Feature)
gen_JavaSimplified_Feature_NamedElement = Generalization(general=NamedElement, specific=JavaSimplified_Feature)
gen_JavaSimplified_Comment_StringElement = Generalization(general=StringElement, specific=JavaSimplified_Comment)
gen_JavaSimplified_FieldAccess_Expression = Generalization(general=Expression, specific=JavaSimplified_FieldAccess)
gen_JavaSimplified_IfStatement_Statement = Generalization(general=Statement, specific=JavaSimplified_IfStatement)
gen_JavaSimplified_Feature_StringElement = Generalization(general=StringElement, specific=JavaSimplified_Feature)
gen_JavaSimplified_Field_TypedElement = Generalization(general=TypedElement, specific=JavaSimplified_Field)
gen_JavaSimplified_Field_Feature = Generalization(general=Feature, specific=JavaSimplified_Field)
gen_JavaSimplified_JavaClass_CommentedElement = Generalization(general=CommentedElement, specific=JavaSimplified_JavaClass)
gen_JavaSimplified_JavaClass_NamedElement = Generalization(general=NamedElement, specific=JavaSimplified_JavaClass)
gen_JavaSimplified_InfixExpression_Expression = Generalization(general=Expression, specific=JavaSimplified_InfixExpression)
gen_JavaSimplified_Method_Feature = Generalization(general=Feature, specific=JavaSimplified_Method)
gen_JavaSimplified_Literal_Expression = Generalization(general=Expression, specific=JavaSimplified_Literal)
gen_JavaSimplified_MethodInvocation_Expression = Generalization(general=Expression, specific=JavaSimplified_MethodInvocation)
gen_JavaSimplified_Name_Expression = Generalization(general=Expression, specific=JavaSimplified_Name)
gen_JavaSimplified_Parameter_NamedElement = Generalization(general=NamedElement, specific=JavaSimplified_Parameter)
gen_JavaSimplified_Parameter_TypedElement = Generalization(general=TypedElement, specific=JavaSimplified_Parameter)
gen_JavaSimplified_ReturnStatement_Statement = Generalization(general=Statement, specific=JavaSimplified_ReturnStatement)
gen_JavaSimplified_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=JavaSimplified_VariableDeclarationStatement)
gen_JavaSimplified_VariableDeclarationStatement_TypedElement = Generalization(general=TypedElement, specific=JavaSimplified_VariableDeclarationStatement)
gen_JavaSimplified_VariableDeclarationStatement_NamedElement = Generalization(general=NamedElement, specific=JavaSimplified_VariableDeclarationStatement)
gen_JavaSimplified_Statement_StringElement = Generalization(general=StringElement, specific=JavaSimplified_Statement)
gen_JavaSimplified_ThisExpression_Expression = Generalization(general=Expression, specific=JavaSimplified_ThisExpression)

# Domain Model
domain_model = DomainModel(
    name="JavaSimplified",
    types={JavaSimplified_Assignment, Expression, JavaSimplified_Expression, JavaSimplified_CastExpression, JavaSimplified_Type, JavaSimplified_ClassInstanceCreation, JavaSimplified_Comment, JavaSimplified_CommentStatement, Statement, JavaSimplified_ExpressionStatement, JavaSimplified_Feature, CommentedElement, NamedElement, StringElement, JavaSimplified_CommentedElement, JavaSimplified_FieldAccess, JavaSimplified_Name, JavaSimplified_IfStatement, JavaSimplified_Statement, JavaSimplified_InfixExpression, JavaSimplified_Field, TypedElement, Feature, JavaSimplified_JavaClass, JavaSimplified_Method, JavaSimplified_JavaModel, JavaSimplified_Parameter, JavaSimplified_MethodCall, JavaSimplified_Literal, JavaSimplified_MethodInvocation, JavaSimplified_NamedElement, JavaSimplified_ReturnStatement, JavaSimplified_TypedElement, JavaSimplified_VariableDeclarationStatement, JavaSimplified_StringElement, JavaSimplified_ThisExpression, AssignmentOperatorType, InfixOperatorType, LiteralType, VisibilityType},
    associations={expr10, expr4, type6, arguments8, className10, expr21, comment13, comment14, expr16, expr18, expr20, name22, expr24, ifst26, elsest28, expr233, fields36, methods38, classes40, expr131, parameters45, statements47, returnType50, arguments53, types42, object61, method63, name66, expr68, childCall56, methodName58, type70, expr72},
    generalizations={gen_JavaSimplified_Assignment_Expression, gen_JavaSimplified_CastExpression_Expression, gen_JavaSimplified_ClassInstanceCreation_Expression, gen_JavaSimplified_CommentStatement_Statement, gen_JavaSimplified_Expression_StringElement, gen_JavaSimplified_ExpressionStatement_Statement, gen_JavaSimplified_Feature_CommentedElement, gen_JavaSimplified_Feature_NamedElement, gen_JavaSimplified_Comment_StringElement, gen_JavaSimplified_FieldAccess_Expression, gen_JavaSimplified_IfStatement_Statement, gen_JavaSimplified_Feature_StringElement, gen_JavaSimplified_Field_TypedElement, gen_JavaSimplified_Field_Feature, gen_JavaSimplified_JavaClass_CommentedElement, gen_JavaSimplified_JavaClass_NamedElement, gen_JavaSimplified_InfixExpression_Expression, gen_JavaSimplified_Method_Feature, gen_JavaSimplified_Literal_Expression, gen_JavaSimplified_MethodInvocation_Expression, gen_JavaSimplified_Name_Expression, gen_JavaSimplified_Parameter_NamedElement, gen_JavaSimplified_Parameter_TypedElement, gen_JavaSimplified_ReturnStatement_Statement, gen_JavaSimplified_VariableDeclarationStatement_Statement, gen_JavaSimplified_VariableDeclarationStatement_TypedElement, gen_JavaSimplified_VariableDeclarationStatement_NamedElement, gen_JavaSimplified_Statement_StringElement, gen_JavaSimplified_ThisExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)