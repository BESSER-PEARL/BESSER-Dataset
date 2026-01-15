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
InfixOperatorType: Enumeration = Enumeration(
    name="InfixOperatorType",
    literals={
            EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="CONDITIONAL_AND"),
			EnumerationLiteral(name="CONDITIONAL_OR")
    }
)

AssignmentOperatorType: Enumeration = Enumeration(
    name="AssignmentOperatorType",
    literals={
            EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="PLUS_ASSIGN")
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
JavaSimplified_Comment = Class(name="JavaSimplified::Comment")
StringElement = Class(name="StringElement")
JavaSimplified_CommentedElement = Class(name="JavaSimplified::CommentedElement", is_abstract=True)
JavaSimplified_StringElement = Class(name="JavaSimplified::StringElement", is_abstract=True)
JavaSimplified_NamedElement = Class(name="JavaSimplified::NamedElement", is_abstract=True)
JavaSimplified_Name = Class(name="JavaSimplified::Name")
JavaSimplified_TypedElement = Class(name="JavaSimplified::TypedElement", is_abstract=True)
JavaSimplified_Type = Class(name="JavaSimplified::Type")
JavaSimplified_CommentStatement = Class(name="JavaSimplified::CommentStatement")
Statement = Class(name="Statement")
JavaSimplified_ExpressionStatement = Class(name="JavaSimplified::ExpressionStatement")
JavaSimplified_IfStatement = Class(name="JavaSimplified::IfStatement")
JavaSimplified_JavaClass = Class(name="JavaSimplified::JavaClass", is_abstract=True)
CommentedElement = Class(name="CommentedElement")
NamedElement = Class(name="NamedElement")
JavaSimplified_Field = Class(name="JavaSimplified::Field")
JavaSimplified_Method = Class(name="JavaSimplified::Method")
TypedElement = Class(name="TypedElement")
JavaSimplified_Expression = Class(name="JavaSimplified::Expression", is_abstract=True)
JavaSimplified_Parameter = Class(name="JavaSimplified::Parameter")
JavaSimplified_Statement = Class(name="JavaSimplified::Statement")
Expression = Class(name="Expression")
JavaSimplified_VariableDeclarationStatement = Class(name="JavaSimplified::VariableDeclarationStatement")
JavaSimplified_ReturnStatement = Class(name="JavaSimplified::ReturnStatement")
JavaSimplified_Assignment = Class(name="JavaSimplified::Assignment")
JavaSimplified_CastExpression = Class(name="JavaSimplified::CastExpression")
JavaSimplified_MethodInvocation = Class(name="JavaSimplified::MethodInvocation")
JavaSimplified_MethodCall = Class(name="JavaSimplified::MethodCall")
JavaSimplified_InfixExpression = Class(name="JavaSimplified::InfixExpression")
JavaSimplified_Literal = Class(name="JavaSimplified::Literal")
JavaSimplified_ClassInstanceCreation = Class(name="JavaSimplified::ClassInstanceCreation")

# JavaSimplified_Comment class attributes and methods
JavaSimplified_Comment_isJavadoc: Property = Property(name="isJavadoc", type=BooleanType)
JavaSimplified_Comment.attributes={JavaSimplified_Comment_isJavadoc}

# StringElement class attributes and methods

# JavaSimplified_CommentedElement class attributes and methods

# JavaSimplified_StringElement class attributes and methods
JavaSimplified_StringElement_strValue: Property = Property(name="strValue", type=StringType)
JavaSimplified_StringElement.attributes={JavaSimplified_StringElement_strValue}

# JavaSimplified_NamedElement class attributes and methods

# JavaSimplified_Name class attributes and methods
JavaSimplified_Name_identifier: Property = Property(name="identifier", type=StringType)
JavaSimplified_Name.attributes={JavaSimplified_Name_identifier}

# JavaSimplified_TypedElement class attributes and methods

# JavaSimplified_Type class attributes and methods
JavaSimplified_Type_type: Property = Property(name="type", type=StringType)
JavaSimplified_Type.attributes={JavaSimplified_Type_type}

# JavaSimplified_CommentStatement class attributes and methods

# Statement class attributes and methods

# JavaSimplified_ExpressionStatement class attributes and methods

# JavaSimplified_IfStatement class attributes and methods

# JavaSimplified_JavaClass class attributes and methods
JavaSimplified_JavaClass_imports: Property = Property(name="imports", type=StringType)
JavaSimplified_JavaClass.attributes={JavaSimplified_JavaClass_imports}

# CommentedElement class attributes and methods

# NamedElement class attributes and methods

# JavaSimplified_Field class attributes and methods
JavaSimplified_Field_visibility: Property = Property(name="visibility", type=StringType)
JavaSimplified_Field.attributes={JavaSimplified_Field_visibility}

# JavaSimplified_Method class attributes and methods
JavaSimplified_Method_exceptions: Property = Property(name="exceptions", type=StringType)
JavaSimplified_Method.attributes={JavaSimplified_Method_exceptions}

# TypedElement class attributes and methods

# JavaSimplified_Expression class attributes and methods

# JavaSimplified_Parameter class attributes and methods

# JavaSimplified_Statement class attributes and methods

# Expression class attributes and methods

# JavaSimplified_VariableDeclarationStatement class attributes and methods

# JavaSimplified_ReturnStatement class attributes and methods

# JavaSimplified_Assignment class attributes and methods
JavaSimplified_Assignment_operator: Property = Property(name="operator", type=StringType)
JavaSimplified_Assignment.attributes={JavaSimplified_Assignment_operator}

# JavaSimplified_CastExpression class attributes and methods

# JavaSimplified_MethodInvocation class attributes and methods

# JavaSimplified_MethodCall class attributes and methods

# JavaSimplified_InfixExpression class attributes and methods
JavaSimplified_InfixExpression_operator: Property = Property(name="operator", type=StringType)
JavaSimplified_InfixExpression.attributes={JavaSimplified_InfixExpression_operator}

# JavaSimplified_Literal class attributes and methods
JavaSimplified_Literal_type: Property = Property(name="type", type=StringType)
JavaSimplified_Literal_value: Property = Property(name="value", type=StringType)
JavaSimplified_Literal.attributes={JavaSimplified_Literal_type, JavaSimplified_Literal_value}

# JavaSimplified_ClassInstanceCreation class attributes and methods

# Relationships
comment2: BinaryAssociation = BinaryAssociation(
    name="comment2",
    ends={
        Property(name="JavaSimplified_Comment", type=JavaSimplified_CommentedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_CommentedElement", type=JavaSimplified_Comment, multiplicity=Multiplicity(0, 1))
    }
)
name0: BinaryAssociation = BinaryAssociation(
    name="name0",
    ends={
        Property(name="JavaSimplified_Name", type=JavaSimplified_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_NamedElement", type=JavaSimplified_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="JavaSimplified_Type", type=JavaSimplified_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_TypedElement", type=JavaSimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)
comment15: BinaryAssociation = BinaryAssociation(
    name="comment15",
    ends={
        Property(name="JavaSimplified_Comment16", type=JavaSimplified_CommentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_CommentStatement", type=JavaSimplified_Comment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr17: BinaryAssociation = BinaryAssociation(
    name="expr17",
    ends={
        Property(name="JavaSimplified_Expression18", type=JavaSimplified_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_ExpressionStatement", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr19: BinaryAssociation = BinaryAssociation(
    name="expr19",
    ends={
        Property(name="JavaSimplified_Expression20", type=JavaSimplified_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_IfStatement", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fields3: BinaryAssociation = BinaryAssociation(
    name="fields3",
    ends={
        Property(name="JavaSimplified_Field", type=JavaSimplified_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_JavaClass", type=JavaSimplified_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods4: BinaryAssociation = BinaryAssociation(
    name="methods4",
    ends={
        Property(name="JavaSimplified_Method", type=JavaSimplified_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_JavaClass5", type=JavaSimplified_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr6: BinaryAssociation = BinaryAssociation(
    name="expr6",
    ends={
        Property(name="JavaSimplified_Expression", type=JavaSimplified_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Field7", type=JavaSimplified_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters8: BinaryAssociation = BinaryAssociation(
    name="parameters8",
    ends={
        Property(name="JavaSimplified_Parameter", type=JavaSimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Method9", type=JavaSimplified_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements10: BinaryAssociation = BinaryAssociation(
    name="statements10",
    ends={
        Property(name="JavaSimplified_Statement", type=JavaSimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Method11", type=JavaSimplified_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType12: BinaryAssociation = BinaryAssociation(
    name="returnType12",
    ends={
        Property(name="JavaSimplified_Type14", type=JavaSimplified_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Method13", type=JavaSimplified_Type, multiplicity=Multiplicity(0, 1))
    }
)
ifst21: BinaryAssociation = BinaryAssociation(
    name="ifst21",
    ends={
        Property(name="JavaSimplified_Statement23", type=JavaSimplified_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_IfStatement22", type=JavaSimplified_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elsest24: BinaryAssociation = BinaryAssociation(
    name="elsest24",
    ends={
        Property(name="JavaSimplified_Statement26", type=JavaSimplified_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_IfStatement25", type=JavaSimplified_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr27: BinaryAssociation = BinaryAssociation(
    name="expr27",
    ends={
        Property(name="JavaSimplified_Expression28", type=JavaSimplified_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_VariableDeclarationStatement", type=JavaSimplified_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr29: BinaryAssociation = BinaryAssociation(
    name="expr29",
    ends={
        Property(name="JavaSimplified_Expression30", type=JavaSimplified_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_ReturnStatement", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr154: BinaryAssociation = BinaryAssociation(
    name="expr154",
    ends={
        Property(name="JavaSimplified_Expression55", type=JavaSimplified_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Assignment", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
var31: BinaryAssociation = BinaryAssociation(
    name="var31",
    ends={
        Property(name="JavaSimplified_Name32", type=JavaSimplified_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_CastExpression", type=JavaSimplified_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="JavaSimplified_Type35", type=JavaSimplified_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_CastExpression34", type=JavaSimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)
object36: BinaryAssociation = BinaryAssociation(
    name="object36",
    ends={
        Property(name="JavaSimplified_Name37", type=JavaSimplified_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_MethodInvocation", type=JavaSimplified_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method38: BinaryAssociation = BinaryAssociation(
    name="method38",
    ends={
        Property(name="JavaSimplified_MethodCall", type=JavaSimplified_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_MethodInvocation39", type=JavaSimplified_MethodCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments40: BinaryAssociation = BinaryAssociation(
    name="arguments40",
    ends={
        Property(name="JavaSimplified_Expression42", type=JavaSimplified_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_MethodCall41", type=JavaSimplified_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childCall44: BinaryAssociation = BinaryAssociation(
    name="childCall44",
    ends={
        Property(name="JavaSimplified_MethodCall45", type=JavaSimplified_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_MethodCall43", type=JavaSimplified_MethodCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodName46: BinaryAssociation = BinaryAssociation(
    name="methodName46",
    ends={
        Property(name="JavaSimplified_Name48", type=JavaSimplified_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_MethodCall47", type=JavaSimplified_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr149: BinaryAssociation = BinaryAssociation(
    name="expr149",
    ends={
        Property(name="JavaSimplified_Expression50", type=JavaSimplified_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_InfixExpression", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr251: BinaryAssociation = BinaryAssociation(
    name="expr251",
    ends={
        Property(name="JavaSimplified_Expression53", type=JavaSimplified_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_InfixExpression52", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr256: BinaryAssociation = BinaryAssociation(
    name="expr256",
    ends={
        Property(name="JavaSimplified_Expression58", type=JavaSimplified_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_Assignment57", type=JavaSimplified_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments59: BinaryAssociation = BinaryAssociation(
    name="arguments59",
    ends={
        Property(name="JavaSimplified_Expression60", type=JavaSimplified_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_ClassInstanceCreation", type=JavaSimplified_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
className61: BinaryAssociation = BinaryAssociation(
    name="className61",
    ends={
        Property(name="JavaSimplified_Type63", type=JavaSimplified_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="JavaSimplified_ClassInstanceCreation62", type=JavaSimplified_Type, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_JavaSimplified_Comment_StringElement = Generalization(general=StringElement, specific=JavaSimplified_Comment)
gen_JavaSimplified_Statement_StringElement = Generalization(general=StringElement, specific=JavaSimplified_Statement)
gen_JavaSimplified_CommentStatement_Statement = Generalization(general=Statement, specific=JavaSimplified_CommentStatement)
gen_JavaSimplified_ExpressionStatement_Statement = Generalization(general=Statement, specific=JavaSimplified_ExpressionStatement)
gen_JavaSimplified_IfStatement_Statement = Generalization(general=Statement, specific=JavaSimplified_IfStatement)
gen_JavaSimplified_JavaClass_CommentedElement = Generalization(general=CommentedElement, specific=JavaSimplified_JavaClass)
gen_JavaSimplified_JavaClass_NamedElement = Generalization(general=NamedElement, specific=JavaSimplified_JavaClass)
gen_JavaSimplified_Field_StringElement = Generalization(general=StringElement, specific=JavaSimplified_Field)
gen_JavaSimplified_Field_CommentedElement = Generalization(general=CommentedElement, specific=JavaSimplified_Field)
gen_JavaSimplified_Field_NamedElement = Generalization(general=NamedElement, specific=JavaSimplified_Field)
gen_JavaSimplified_Field_TypedElement = Generalization(general=TypedElement, specific=JavaSimplified_Field)
gen_JavaSimplified_Method_StringElement = Generalization(general=StringElement, specific=JavaSimplified_Method)
gen_JavaSimplified_Method_CommentedElement = Generalization(general=CommentedElement, specific=JavaSimplified_Method)
gen_JavaSimplified_Method_NamedElement = Generalization(general=NamedElement, specific=JavaSimplified_Method)
gen_JavaSimplified_Parameter_NamedElement = Generalization(general=NamedElement, specific=JavaSimplified_Parameter)
gen_JavaSimplified_Parameter_TypedElement = Generalization(general=TypedElement, specific=JavaSimplified_Parameter)
gen_JavaSimplified_Name_Expression = Generalization(general=Expression, specific=JavaSimplified_Name)
gen_JavaSimplified_VariableDeclarationStatement_Statement = Generalization(general=Statement, specific=JavaSimplified_VariableDeclarationStatement)
gen_JavaSimplified_VariableDeclarationStatement_TypedElement = Generalization(general=TypedElement, specific=JavaSimplified_VariableDeclarationStatement)
gen_JavaSimplified_VariableDeclarationStatement_NamedElement = Generalization(general=NamedElement, specific=JavaSimplified_VariableDeclarationStatement)
gen_JavaSimplified_ReturnStatement_Statement = Generalization(general=Statement, specific=JavaSimplified_ReturnStatement)
gen_JavaSimplified_Assignment_Expression = Generalization(general=Expression, specific=JavaSimplified_Assignment)
gen_JavaSimplified_Expression_StringElement = Generalization(general=StringElement, specific=JavaSimplified_Expression)
gen_JavaSimplified_CastExpression_Expression = Generalization(general=Expression, specific=JavaSimplified_CastExpression)
gen_JavaSimplified_MethodInvocation_Expression = Generalization(general=Expression, specific=JavaSimplified_MethodInvocation)
gen_JavaSimplified_InfixExpression_Expression = Generalization(general=Expression, specific=JavaSimplified_InfixExpression)
gen_JavaSimplified_Literal_Expression = Generalization(general=Expression, specific=JavaSimplified_Literal)
gen_JavaSimplified_ClassInstanceCreation_Expression = Generalization(general=Expression, specific=JavaSimplified_ClassInstanceCreation)

# Domain Model
domain_model = DomainModel(
    name="JavaSimplified",
    types={JavaSimplified_Comment, StringElement, JavaSimplified_CommentedElement, JavaSimplified_StringElement, JavaSimplified_NamedElement, JavaSimplified_Name, JavaSimplified_TypedElement, JavaSimplified_Type, JavaSimplified_CommentStatement, Statement, JavaSimplified_ExpressionStatement, JavaSimplified_IfStatement, JavaSimplified_JavaClass, CommentedElement, NamedElement, JavaSimplified_Field, JavaSimplified_Method, TypedElement, JavaSimplified_Expression, JavaSimplified_Parameter, JavaSimplified_Statement, Expression, JavaSimplified_VariableDeclarationStatement, JavaSimplified_ReturnStatement, JavaSimplified_Assignment, JavaSimplified_CastExpression, JavaSimplified_MethodInvocation, JavaSimplified_MethodCall, JavaSimplified_InfixExpression, JavaSimplified_Literal, JavaSimplified_ClassInstanceCreation, InfixOperatorType, AssignmentOperatorType, LiteralType, VisibilityType},
    associations={comment2, name0, type1, comment15, expr17, expr19, fields3, methods4, expr6, parameters8, statements10, returnType12, ifst21, elsest24, expr27, expr29, expr154, var31, type33, object36, method38, arguments40, childCall44, methodName46, expr149, expr251, expr256, arguments59, className61},
    generalizations={gen_JavaSimplified_Comment_StringElement, gen_JavaSimplified_Statement_StringElement, gen_JavaSimplified_CommentStatement_Statement, gen_JavaSimplified_ExpressionStatement_Statement, gen_JavaSimplified_IfStatement_Statement, gen_JavaSimplified_JavaClass_CommentedElement, gen_JavaSimplified_JavaClass_NamedElement, gen_JavaSimplified_Field_StringElement, gen_JavaSimplified_Field_CommentedElement, gen_JavaSimplified_Field_NamedElement, gen_JavaSimplified_Field_TypedElement, gen_JavaSimplified_Method_StringElement, gen_JavaSimplified_Method_CommentedElement, gen_JavaSimplified_Method_NamedElement, gen_JavaSimplified_Parameter_NamedElement, gen_JavaSimplified_Parameter_TypedElement, gen_JavaSimplified_Name_Expression, gen_JavaSimplified_VariableDeclarationStatement_Statement, gen_JavaSimplified_VariableDeclarationStatement_TypedElement, gen_JavaSimplified_VariableDeclarationStatement_NamedElement, gen_JavaSimplified_ReturnStatement_Statement, gen_JavaSimplified_Assignment_Expression, gen_JavaSimplified_Expression_StringElement, gen_JavaSimplified_CastExpression_Expression, gen_JavaSimplified_MethodInvocation_Expression, gen_JavaSimplified_InfixExpression_Expression, gen_JavaSimplified_Literal_Expression, gen_JavaSimplified_ClassInstanceCreation_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)