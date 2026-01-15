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
Axis: Enumeration = Enumeration(
    name="Axis",
    literals={
            EnumerationLiteral(name="component"),
			EnumerationLiteral(name="internalinterface"),
			EnumerationLiteral(name="interface"),
			EnumerationLiteral(name="attribute"),
			EnumerationLiteral(name="binding"),
			EnumerationLiteral(name="child"),
			EnumerationLiteral(name="parent"),
			EnumerationLiteral(name="descendant"),
			EnumerationLiteral(name="ancestor"),
			EnumerationLiteral(name="sibling"),
			EnumerationLiteral(name="descendantorself"),
			EnumerationLiteral(name="ancestororself"),
			EnumerationLiteral(name="siblingorself")
    }
)

# Classes
FPath_LocatedElement = Class(name="FPath::LocatedElement", is_abstract=True)
FPath_Expression = Class(name="FPath::Expression", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
FPath_ContextExp = Class(name="FPath::ContextExp")
Expression = Class(name="Expression")
FPath_VariableExp = Class(name="FPath::VariableExp")
FPath_FunctionCallExp = Class(name="FPath::FunctionCallExp")
FPath_NumberExp = Class(name="FPath::NumberExp")
FPath_StringExp = Class(name="FPath::StringExp")
FPath_UnaryOperatorExp = Class(name="FPath::UnaryOperatorExp")
FPath_Test = Class(name="FPath::Test", is_abstract=True)
FPath_WildcardTest = Class(name="FPath::WildcardTest")
Test = Class(name="Test")
FPath_NameTest = Class(name="FPath::NameTest")
FPath_PathExp = Class(name="FPath::PathExp")
FPath_Step = Class(name="FPath::Step")
FPath_OperatorExp = Class(name="FPath::OperatorExp", is_abstract=True)
FPath_BinaryOperatorExp = Class(name="FPath::BinaryOperatorExp")
OperatorExp = Class(name="OperatorExp")

# FPath_LocatedElement class attributes and methods
FPath_LocatedElement_location: Property = Property(name="location", type=StringType)
FPath_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
FPath_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
FPath_LocatedElement.attributes={FPath_LocatedElement_commentsAfter, FPath_LocatedElement_location, FPath_LocatedElement_commentsBefore}

# FPath_Expression class attributes and methods

# LocatedElement class attributes and methods

# FPath_ContextExp class attributes and methods

# Expression class attributes and methods

# FPath_VariableExp class attributes and methods
FPath_VariableExp_name: Property = Property(name="name", type=StringType)
FPath_VariableExp.attributes={FPath_VariableExp_name}

# FPath_FunctionCallExp class attributes and methods
FPath_FunctionCallExp_name: Property = Property(name="name", type=StringType)
FPath_FunctionCallExp.attributes={FPath_FunctionCallExp_name}

# FPath_NumberExp class attributes and methods
FPath_NumberExp_value: Property = Property(name="value", type=StringType)
FPath_NumberExp.attributes={FPath_NumberExp_value}

# FPath_StringExp class attributes and methods
FPath_StringExp_value: Property = Property(name="value", type=StringType)
FPath_StringExp.attributes={FPath_StringExp_value}

# FPath_UnaryOperatorExp class attributes and methods

# FPath_Test class attributes and methods

# FPath_WildcardTest class attributes and methods

# Test class attributes and methods

# FPath_NameTest class attributes and methods
FPath_NameTest_name: Property = Property(name="name", type=StringType)
FPath_NameTest.attributes={FPath_NameTest_name}

# FPath_PathExp class attributes and methods

# FPath_Step class attributes and methods
FPath_Step_axis: Property = Property(name="axis", type=StringType)
FPath_Step.attributes={FPath_Step_axis}

# FPath_OperatorExp class attributes and methods
FPath_OperatorExp_operator: Property = Property(name="operator", type=StringType)
FPath_OperatorExp.attributes={FPath_OperatorExp_operator}

# FPath_BinaryOperatorExp class attributes and methods

# OperatorExp class attributes and methods

# Relationships
arguments0: BinaryAssociation = BinaryAssociation(
    name="arguments0",
    ends={
        Property(name="FPath_Expression", type=FPath_FunctionCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FPath_FunctionCallExp", type=FPath_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left5: BinaryAssociation = BinaryAssociation(
    name="left5",
    ends={
        Property(name="FPath_Expression6", type=FPath_BinaryOperatorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FPath_BinaryOperatorExp", type=FPath_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right7: BinaryAssociation = BinaryAssociation(
    name="right7",
    ends={
        Property(name="FPath_Expression9", type=FPath_BinaryOperatorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FPath_BinaryOperatorExp8", type=FPath_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand10: BinaryAssociation = BinaryAssociation(
    name="operand10",
    ends={
        Property(name="FPath_Expression11", type=FPath_UnaryOperatorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FPath_UnaryOperatorExp", type=FPath_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
test12: BinaryAssociation = BinaryAssociation(
    name="test12",
    ends={
        Property(name="FPath_Test", type=FPath_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="FPath_Step13", type=FPath_Test, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predicates14: BinaryAssociation = BinaryAssociation(
    name="predicates14",
    ends={
        Property(name="FPath_Expression16", type=FPath_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="FPath_Step15", type=FPath_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialNodeSet1: BinaryAssociation = BinaryAssociation(
    name="initialNodeSet1",
    ends={
        Property(name="FPath_Expression2", type=FPath_PathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FPath_PathExp", type=FPath_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
steps3: BinaryAssociation = BinaryAssociation(
    name="steps3",
    ends={
        Property(name="FPath_Step", type=FPath_PathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FPath_PathExp4", type=FPath_Step, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_FPath_Expression_LocatedElement = Generalization(general=LocatedElement, specific=FPath_Expression)
gen_FPath_ContextExp_Expression = Generalization(general=Expression, specific=FPath_ContextExp)
gen_FPath_VariableExp_Expression = Generalization(general=Expression, specific=FPath_VariableExp)
gen_FPath_FunctionCallExp_Expression = Generalization(general=Expression, specific=FPath_FunctionCallExp)
gen_FPath_NumberExp_Expression = Generalization(general=Expression, specific=FPath_NumberExp)
gen_FPath_StringExp_Expression = Generalization(general=Expression, specific=FPath_StringExp)
gen_FPath_UnaryOperatorExp_OperatorExp = Generalization(general=OperatorExp, specific=FPath_UnaryOperatorExp)
gen_FPath_Step_LocatedElement = Generalization(general=LocatedElement, specific=FPath_Step)
gen_FPath_Test_LocatedElement = Generalization(general=LocatedElement, specific=FPath_Test)
gen_FPath_WildcardTest_Test = Generalization(general=Test, specific=FPath_WildcardTest)
gen_FPath_NameTest_Test = Generalization(general=Test, specific=FPath_NameTest)
gen_FPath_PathExp_Expression = Generalization(general=Expression, specific=FPath_PathExp)
gen_FPath_OperatorExp_Expression = Generalization(general=Expression, specific=FPath_OperatorExp)
gen_FPath_BinaryOperatorExp_OperatorExp = Generalization(general=OperatorExp, specific=FPath_BinaryOperatorExp)

# Domain Model
domain_model = DomainModel(
    name="FPath",
    types={FPath_LocatedElement, FPath_Expression, LocatedElement, FPath_ContextExp, Expression, FPath_VariableExp, FPath_FunctionCallExp, FPath_NumberExp, FPath_StringExp, FPath_UnaryOperatorExp, FPath_Test, FPath_WildcardTest, Test, FPath_NameTest, FPath_PathExp, FPath_Step, FPath_OperatorExp, FPath_BinaryOperatorExp, OperatorExp, Axis},
    associations={arguments0, left5, right7, operand10, test12, predicates14, initialNodeSet1, steps3},
    generalizations={gen_FPath_Expression_LocatedElement, gen_FPath_ContextExp_Expression, gen_FPath_VariableExp_Expression, gen_FPath_FunctionCallExp_Expression, gen_FPath_NumberExp_Expression, gen_FPath_StringExp_Expression, gen_FPath_UnaryOperatorExp_OperatorExp, gen_FPath_Step_LocatedElement, gen_FPath_Test_LocatedElement, gen_FPath_WildcardTest_Test, gen_FPath_NameTest_Test, gen_FPath_PathExp_Expression, gen_FPath_OperatorExp_Expression, gen_FPath_BinaryOperatorExp_OperatorExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)