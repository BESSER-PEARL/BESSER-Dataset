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
core_Rule = Class(name="core_Rule")
core_IntegerExpression = Class(name="core_IntegerExpression", is_abstract=True)
core_UnaryExpression = Class(name="core_UnaryExpression", is_abstract=True)
IntegerExpression = Class(name="IntegerExpression")
core_And = Class(name="core_And")
core_Or = Class(name="core_Or")
core_Not = Class(name="core_Not")
UnaryExpression = Class(name="UnaryExpression")
core_Greater = Class(name="core_Greater")
core_Lower = Class(name="core_Lower")
core_IntegerLiteral = Class(name="core_IntegerLiteral")
core_Filter = Class(name="core_Filter", is_abstract=True)
core_Add = Class(name="core_Add")
BinaryExpression = Class(name="BinaryExpression")
core_BinaryExpression = Class(name="core_BinaryExpression", is_abstract=True)
core_Mult = Class(name="core_Mult")
core_Conditional = Class(name="core_Conditional")
core_Div = Class(name="core_Div")
core_Mod = Class(name="core_Mod")
core_UMinus = Class(name="core_UMinus")
core_Minus = Class(name="core_Minus")
core_Equal = Class(name="core_Equal")

# core_Rule class attributes and methods

# core_IntegerExpression class attributes and methods

# core_UnaryExpression class attributes and methods

# IntegerExpression class attributes and methods

# core_And class attributes and methods

# core_Or class attributes and methods

# core_Not class attributes and methods

# UnaryExpression class attributes and methods

# core_Greater class attributes and methods

# core_Lower class attributes and methods

# core_IntegerLiteral class attributes and methods
core_IntegerLiteral_val: Property = Property(name="val", type=IntegerType)
core_IntegerLiteral.attributes={core_IntegerLiteral_val}

# core_Filter class attributes and methods

# core_Add class attributes and methods

# BinaryExpression class attributes and methods

# core_BinaryExpression class attributes and methods

# core_Mult class attributes and methods

# core_Conditional class attributes and methods

# core_Div class attributes and methods

# core_Mod class attributes and methods

# core_UMinus class attributes and methods

# core_Minus class attributes and methods

# core_Equal class attributes and methods

# Relationships
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="core_IntegerExpression4", type=core_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="core_UnaryExpression", type=core_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
evaluatedVal0: BinaryAssociation = BinaryAssociation(
    name="evaluatedVal0",
    ends={
        Property(name="core_IntegerExpression", type=core_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Rule", type=core_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
filter1: BinaryAssociation = BinaryAssociation(
    name="filter1",
    ends={
        Property(name="core_Filter", type=core_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Rule2", type=core_Filter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifTrueExpression7: BinaryAssociation = BinaryAssociation(
    name="ifTrueExpression7",
    ends={
        Property(name="core_IntegerExpression9", type=core_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Conditional8", type=core_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifFalseExpression10: BinaryAssociation = BinaryAssociation(
    name="ifFalseExpression10",
    ends={
        Property(name="core_IntegerExpression12", type=core_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Conditional11", type=core_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left13: BinaryAssociation = BinaryAssociation(
    name="left13",
    ends={
        Property(name="core_IntegerExpression14", type=core_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="core_BinaryExpression", type=core_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right15: BinaryAssociation = BinaryAssociation(
    name="right15",
    ends={
        Property(name="core_IntegerExpression17", type=core_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="core_BinaryExpression16", type=core_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition5: BinaryAssociation = BinaryAssociation(
    name="condition5",
    ends={
        Property(name="core_IntegerExpression6", type=core_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="core_Conditional", type=core_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_core_UnaryExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=core_UnaryExpression)
gen_core_And_BinaryExpression = Generalization(general=BinaryExpression, specific=core_And)
gen_core_Or_BinaryExpression = Generalization(general=BinaryExpression, specific=core_Or)
gen_core_Not_UnaryExpression = Generalization(general=UnaryExpression, specific=core_Not)
gen_core_Greater_BinaryExpression = Generalization(general=BinaryExpression, specific=core_Greater)
gen_core_Lower_BinaryExpression = Generalization(general=BinaryExpression, specific=core_Lower)
gen_core_IntegerLiteral_IntegerExpression = Generalization(general=IntegerExpression, specific=core_IntegerLiteral)
gen_core_Add_BinaryExpression = Generalization(general=BinaryExpression, specific=core_Add)
gen_core_BinaryExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=core_BinaryExpression)
gen_core_Mult_BinaryExpression = Generalization(general=BinaryExpression, specific=core_Mult)
gen_core_Conditional_IntegerExpression = Generalization(general=IntegerExpression, specific=core_Conditional)
gen_core_Div_BinaryExpression = Generalization(general=BinaryExpression, specific=core_Div)
gen_core_Mod_BinaryExpression = Generalization(general=BinaryExpression, specific=core_Mod)
gen_core_UMinus_UnaryExpression = Generalization(general=UnaryExpression, specific=core_UMinus)
gen_core_Minus_BinaryExpression = Generalization(general=BinaryExpression, specific=core_Minus)
gen_core_Equal_BinaryExpression = Generalization(general=BinaryExpression, specific=core_Equal)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={core_Rule, core_IntegerExpression, core_UnaryExpression, IntegerExpression, core_And, core_Or, core_Not, UnaryExpression, core_Greater, core_Lower, core_IntegerLiteral, core_Filter, core_Add, BinaryExpression, core_BinaryExpression, core_Mult, core_Conditional, core_Div, core_Mod, core_UMinus, core_Minus, core_Equal},
    associations={target3, evaluatedVal0, filter1, ifTrueExpression7, ifFalseExpression10, left13, right15, condition5},
    generalizations={gen_core_UnaryExpression_IntegerExpression, gen_core_And_BinaryExpression, gen_core_Or_BinaryExpression, gen_core_Not_UnaryExpression, gen_core_Greater_BinaryExpression, gen_core_Lower_BinaryExpression, gen_core_IntegerLiteral_IntegerExpression, gen_core_Add_BinaryExpression, gen_core_BinaryExpression_IntegerExpression, gen_core_Mult_BinaryExpression, gen_core_Conditional_IntegerExpression, gen_core_Div_BinaryExpression, gen_core_Mod_BinaryExpression, gen_core_UMinus_UnaryExpression, gen_core_Minus_BinaryExpression, gen_core_Equal_BinaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)