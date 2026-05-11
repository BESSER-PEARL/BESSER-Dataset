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
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="INTEGER")
    }
)

# Classes
simple_csp_TypedElement = Class(name="simple_csp_TypedElement", is_abstract=True)
simple_csp_Problem = Class(name="simple_csp_Problem")
NamedElement = Class(name="NamedElement")
simple_csp_Domain = Class(name="simple_csp_Domain", is_abstract=True)
simple_csp_Variable = Class(name="simple_csp_Variable")
simple_csp_Constraint = Class(name="simple_csp_Constraint")
simple_csp_Goal = Class(name="simple_csp_Goal", is_abstract=True)
simple_csp_BinaryOp = Class(name="simple_csp_BinaryOp", is_abstract=True)
simple_csp_IntegerDomain = Class(name="simple_csp_IntegerDomain")
Domain = Class(name="Domain")
DescribedElement = Class(name="DescribedElement")
TypedElement = Class(name="TypedElement")
simple_csp_Expression = Class(name="simple_csp_Expression", is_abstract=True)
simple_csp_Operator = Class(name="simple_csp_Operator", is_abstract=True)
Expression = Class(name="Expression")
simple_csp_SetOp = Class(name="simple_csp_SetOp", is_abstract=True)
Operator = Class(name="Operator")
simple_csp_Minus = Class(name="simple_csp_Minus")
simple_csp_Plus = Class(name="simple_csp_Plus")
simple_csp_Times = Class(name="simple_csp_Times")
simple_csp_Power = Class(name="simple_csp_Power")
simple_csp_UnaryOp = Class(name="simple_csp_UnaryOp", is_abstract=True)
simple_csp_Not = Class(name="simple_csp_Not")
UnaryOp = Class(name="UnaryOp")
simple_csp_And = Class(name="simple_csp_And")
BinaryOp = Class(name="BinaryOp")
simple_csp_Or = Class(name="simple_csp_Or")
simple_csp_Implies = Class(name="simple_csp_Implies")
simple_csp_Equal = Class(name="simple_csp_Equal")
simple_csp_UnEqual = Class(name="simple_csp_UnEqual")
simple_csp_Less = Class(name="simple_csp_Less")
simple_csp_LessEqual = Class(name="simple_csp_LessEqual")
simple_csp_Greater = Class(name="simple_csp_Greater")
simple_csp_GreaterEqual = Class(name="simple_csp_GreaterEqual")
simple_csp_MinimizeGoal = Class(name="simple_csp_MinimizeGoal")
simple_csp_NamedElement = Class(name="simple_csp_NamedElement", is_abstract=True)
simple_csp_Sum = Class(name="simple_csp_Sum")
SetOp = Class(name="SetOp")
simple_csp_Min = Class(name="simple_csp_Min")
simple_csp_Max = Class(name="simple_csp_Max")
simple_csp_VarOccurence = Class(name="simple_csp_VarOccurence")
simple_csp_BooleanLiteral = Class(name="simple_csp_BooleanLiteral", is_abstract=True)
simple_csp_TrueValue = Class(name="simple_csp_TrueValue")
BooleanLiteral = Class(name="BooleanLiteral")
simple_csp_FalseValue = Class(name="simple_csp_FalseValue")
simple_csp_MaximizeGoal = Class(name="simple_csp_MaximizeGoal")
Goal = Class(name="Goal")
simple_csp_DescribedElement = Class(name="simple_csp_DescribedElement", is_abstract=True)

# simple_csp_TypedElement class attributes and methods
simple_csp_TypedElement_type: Property = Property(name="type", type=StringType)
simple_csp_TypedElement.attributes={simple_csp_TypedElement_type}

# simple_csp_Problem class attributes and methods

# NamedElement class attributes and methods

# simple_csp_Domain class attributes and methods

# simple_csp_Variable class attributes and methods

# simple_csp_Constraint class attributes and methods

# simple_csp_Goal class attributes and methods

# simple_csp_BinaryOp class attributes and methods

# simple_csp_IntegerDomain class attributes and methods
simple_csp_IntegerDomain_minValue: Property = Property(name="minValue", type=StringType)
simple_csp_IntegerDomain_maxValue: Property = Property(name="maxValue", type=StringType)
simple_csp_IntegerDomain.attributes={simple_csp_IntegerDomain_minValue, simple_csp_IntegerDomain_maxValue}

# Domain class attributes and methods

# DescribedElement class attributes and methods

# TypedElement class attributes and methods

# simple_csp_Expression class attributes and methods

# simple_csp_Operator class attributes and methods

# Expression class attributes and methods

# simple_csp_SetOp class attributes and methods

# Operator class attributes and methods

# simple_csp_Minus class attributes and methods

# simple_csp_Plus class attributes and methods

# simple_csp_Times class attributes and methods

# simple_csp_Power class attributes and methods

# simple_csp_UnaryOp class attributes and methods

# simple_csp_Not class attributes and methods

# UnaryOp class attributes and methods

# simple_csp_And class attributes and methods

# BinaryOp class attributes and methods

# simple_csp_Or class attributes and methods

# simple_csp_Implies class attributes and methods

# simple_csp_Equal class attributes and methods

# simple_csp_UnEqual class attributes and methods

# simple_csp_Less class attributes and methods

# simple_csp_LessEqual class attributes and methods

# simple_csp_Greater class attributes and methods

# simple_csp_GreaterEqual class attributes and methods

# simple_csp_MinimizeGoal class attributes and methods

# simple_csp_NamedElement class attributes and methods
simple_csp_NamedElement_name: Property = Property(name="name", type=StringType)
simple_csp_NamedElement.attributes={simple_csp_NamedElement_name}

# simple_csp_Sum class attributes and methods

# SetOp class attributes and methods

# simple_csp_Min class attributes and methods

# simple_csp_Max class attributes and methods

# simple_csp_VarOccurence class attributes and methods

# simple_csp_BooleanLiteral class attributes and methods

# simple_csp_TrueValue class attributes and methods

# BooleanLiteral class attributes and methods

# simple_csp_FalseValue class attributes and methods

# simple_csp_MaximizeGoal class attributes and methods

# Goal class attributes and methods

# simple_csp_DescribedElement class attributes and methods
simple_csp_DescribedElement_description: Property = Property(name="description", type=StringType)
simple_csp_DescribedElement.attributes={simple_csp_DescribedElement_description}

# Relationships
goals5: BinaryAssociation = BinaryAssociation(
    name="goals5",
    ends={
        Property(name="simple_csp_Goal", type=simple_csp_Problem, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_Problem6", type=simple_csp_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain7: BinaryAssociation = BinaryAssociation(
    name="domain7",
    ends={
        Property(name="simple_csp_Domain8", type=simple_csp_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_TypedElement", type=simple_csp_Domain, multiplicity=Multiplicity(0, 1))
    }
)
domains0: BinaryAssociation = BinaryAssociation(
    name="domains0",
    ends={
        Property(name="simple_csp_Domain", type=simple_csp_Problem, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_Problem", type=simple_csp_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables1: BinaryAssociation = BinaryAssociation(
    name="variables1",
    ends={
        Property(name="simple_csp_Variable", type=simple_csp_Problem, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_Problem2", type=simple_csp_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraint3: BinaryAssociation = BinaryAssociation(
    name="constraint3",
    ends={
        Property(name="simple_csp_Constraint", type=simple_csp_Problem, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_Problem4", type=simple_csp_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exps11: BinaryAssociation = BinaryAssociation(
    name="exps11",
    ends={
        Property(name="simple_csp_Expression12", type=simple_csp_SetOp, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_SetOp", type=simple_csp_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftExp13: BinaryAssociation = BinaryAssociation(
    name="leftExp13",
    ends={
        Property(name="simple_csp_Expression14", type=simple_csp_BinaryOp, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_BinaryOp", type=simple_csp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp9: BinaryAssociation = BinaryAssociation(
    name="exp9",
    ends={
        Property(name="simple_csp_Expression", type=simple_csp_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_Constraint10", type=simple_csp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightExp15: BinaryAssociation = BinaryAssociation(
    name="rightExp15",
    ends={
        Property(name="simple_csp_Expression17", type=simple_csp_BinaryOp, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_BinaryOp16", type=simple_csp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp18: BinaryAssociation = BinaryAssociation(
    name="exp18",
    ends={
        Property(name="simple_csp_Expression19", type=simple_csp_UnaryOp, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_UnaryOp", type=simple_csp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable20: BinaryAssociation = BinaryAssociation(
    name="variable20",
    ends={
        Property(name="simple_csp_Variable21", type=simple_csp_VarOccurence, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_VarOccurence", type=simple_csp_Variable, multiplicity=Multiplicity(0, 1))
    }
)
exp22: BinaryAssociation = BinaryAssociation(
    name="exp22",
    ends={
        Property(name="simple_csp_Expression24", type=simple_csp_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_csp_Goal23", type=simple_csp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_simple_csp_Problem_NamedElement = Generalization(general=NamedElement, specific=simple_csp_Problem)
gen_simple_csp_BinaryOp_Operator = Generalization(general=Operator, specific=simple_csp_BinaryOp)
gen_simple_csp_IntegerDomain_Domain = Generalization(general=Domain, specific=simple_csp_IntegerDomain)
gen_simple_csp_Variable_NamedElement = Generalization(general=NamedElement, specific=simple_csp_Variable)
gen_simple_csp_Variable_DescribedElement = Generalization(general=DescribedElement, specific=simple_csp_Variable)
gen_simple_csp_Variable_TypedElement = Generalization(general=TypedElement, specific=simple_csp_Variable)
gen_simple_csp_Constraint_NamedElement = Generalization(general=NamedElement, specific=simple_csp_Constraint)
gen_simple_csp_Operator_Expression = Generalization(general=Expression, specific=simple_csp_Operator)
gen_simple_csp_SetOp_Operator = Generalization(general=Operator, specific=simple_csp_SetOp)
gen_simple_csp_Minus_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_Minus)
gen_simple_csp_Plus_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_Plus)
gen_simple_csp_Times_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_Times)
gen_simple_csp_Power_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_Power)
gen_simple_csp_UnaryOp_Operator = Generalization(general=Operator, specific=simple_csp_UnaryOp)
gen_simple_csp_Not_UnaryOp = Generalization(general=UnaryOp, specific=simple_csp_Not)
gen_simple_csp_And_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_And)
gen_simple_csp_Or_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_Or)
gen_simple_csp_Implies_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_Implies)
gen_simple_csp_Equal_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_Equal)
gen_simple_csp_UnEqual_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_UnEqual)
gen_simple_csp_Less_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_Less)
gen_simple_csp_LessEqual_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_LessEqual)
gen_simple_csp_Greater_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_Greater)
gen_simple_csp_GreaterEqual_BinaryOp = Generalization(general=BinaryOp, specific=simple_csp_GreaterEqual)
gen_simple_csp_MinimizeGoal_Goal = Generalization(general=Goal, specific=simple_csp_MinimizeGoal)
gen_simple_csp_Sum_SetOp = Generalization(general=SetOp, specific=simple_csp_Sum)
gen_simple_csp_Min_SetOp = Generalization(general=SetOp, specific=simple_csp_Min)
gen_simple_csp_Max_SetOp = Generalization(general=SetOp, specific=simple_csp_Max)
gen_simple_csp_VarOccurence_Expression = Generalization(general=Expression, specific=simple_csp_VarOccurence)
gen_simple_csp_BooleanLiteral_Expression = Generalization(general=Expression, specific=simple_csp_BooleanLiteral)
gen_simple_csp_TrueValue_BooleanLiteral = Generalization(general=BooleanLiteral, specific=simple_csp_TrueValue)
gen_simple_csp_FalseValue_BooleanLiteral = Generalization(general=BooleanLiteral, specific=simple_csp_FalseValue)
gen_simple_csp_Goal_NamedElement = Generalization(general=NamedElement, specific=simple_csp_Goal)
gen_simple_csp_MaximizeGoal_Goal = Generalization(general=Goal, specific=simple_csp_MaximizeGoal)

# Domain Model
domain_model = DomainModel(
    name="simple_csp",
    types={simple_csp_TypedElement, simple_csp_Problem, NamedElement, simple_csp_Domain, simple_csp_Variable, simple_csp_Constraint, simple_csp_Goal, simple_csp_BinaryOp, simple_csp_IntegerDomain, Domain, DescribedElement, TypedElement, simple_csp_Expression, simple_csp_Operator, Expression, simple_csp_SetOp, Operator, simple_csp_Minus, simple_csp_Plus, simple_csp_Times, simple_csp_Power, simple_csp_UnaryOp, simple_csp_Not, UnaryOp, simple_csp_And, BinaryOp, simple_csp_Or, simple_csp_Implies, simple_csp_Equal, simple_csp_UnEqual, simple_csp_Less, simple_csp_LessEqual, simple_csp_Greater, simple_csp_GreaterEqual, simple_csp_MinimizeGoal, simple_csp_NamedElement, simple_csp_Sum, SetOp, simple_csp_Min, simple_csp_Max, simple_csp_VarOccurence, simple_csp_BooleanLiteral, simple_csp_TrueValue, BooleanLiteral, simple_csp_FalseValue, simple_csp_MaximizeGoal, Goal, simple_csp_DescribedElement, Type},
    associations={goals5, domain7, domains0, variables1, constraint3, exps11, leftExp13, exp9, rightExp15, exp18, variable20, exp22},
    generalizations={gen_simple_csp_Problem_NamedElement, gen_simple_csp_BinaryOp_Operator, gen_simple_csp_IntegerDomain_Domain, gen_simple_csp_Variable_NamedElement, gen_simple_csp_Variable_DescribedElement, gen_simple_csp_Variable_TypedElement, gen_simple_csp_Constraint_NamedElement, gen_simple_csp_Operator_Expression, gen_simple_csp_SetOp_Operator, gen_simple_csp_Minus_BinaryOp, gen_simple_csp_Plus_BinaryOp, gen_simple_csp_Times_BinaryOp, gen_simple_csp_Power_BinaryOp, gen_simple_csp_UnaryOp_Operator, gen_simple_csp_Not_UnaryOp, gen_simple_csp_And_BinaryOp, gen_simple_csp_Or_BinaryOp, gen_simple_csp_Implies_BinaryOp, gen_simple_csp_Equal_BinaryOp, gen_simple_csp_UnEqual_BinaryOp, gen_simple_csp_Less_BinaryOp, gen_simple_csp_LessEqual_BinaryOp, gen_simple_csp_Greater_BinaryOp, gen_simple_csp_GreaterEqual_BinaryOp, gen_simple_csp_MinimizeGoal_Goal, gen_simple_csp_Sum_SetOp, gen_simple_csp_Min_SetOp, gen_simple_csp_Max_SetOp, gen_simple_csp_VarOccurence_Expression, gen_simple_csp_BooleanLiteral_Expression, gen_simple_csp_TrueValue_BooleanLiteral, gen_simple_csp_FalseValue_BooleanLiteral, gen_simple_csp_Goal_NamedElement, gen_simple_csp_MaximizeGoal_Goal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)