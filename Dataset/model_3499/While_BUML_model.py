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
while_While = Class(name="while::While")
Statement = Class(name="Statement")
while_BoolExp = Class(name="while::BoolExp")
while_If = Class(name="while::If")
while_Program = Class(name="while::Program")
while_Statement = Class(name="while::Statement", is_abstract=True)
while_Var = Class(name="while::Var")
while_Val = Class(name="while::Val")
while_NEqExp = Class(name="while::NEqExp")
while_BinaryExp = Class(name="while::BinaryExp", is_abstract=True)
Exp = Class(name="Exp")
while_Exp = Class(name="while::Exp", is_abstract=True)
while_AndExp = Class(name="while::AndExp")
while_EqExp = Class(name="while::EqExp")
BinaryExp = Class(name="BinaryExp")
BoolExp = Class(name="BoolExp")
while_Ret = Class(name="while::Ret")
while_VarExp = Class(name="while::VarExp")
while_Assignment = Class(name="while::Assignment")

# while_While class attributes and methods

# Statement class attributes and methods

# while_BoolExp class attributes and methods

# while_If class attributes and methods

# while_Program class attributes and methods

# while_Statement class attributes and methods

# while_Var class attributes and methods
while_Var_id: Property = Property(name="id", type=StringType)
while_Var.attributes={while_Var_id}

# while_Val class attributes and methods
while_Val_id: Property = Property(name="id", type=StringType)
while_Val.attributes={while_Val_id}

# while_NEqExp class attributes and methods

# while_BinaryExp class attributes and methods

# Exp class attributes and methods

# while_Exp class attributes and methods

# while_AndExp class attributes and methods

# while_EqExp class attributes and methods

# BinaryExp class attributes and methods

# BoolExp class attributes and methods

# while_Ret class attributes and methods

# while_VarExp class attributes and methods

# while_Assignment class attributes and methods

# Relationships
literals3: BinaryAssociation = BinaryAssociation(
    name="literals3",
    ends={
        Property(name="while_Val", type=while_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="while_Program4", type=while_Val, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition5: BinaryAssociation = BinaryAssociation(
    name="condition5",
    ends={
        Property(name="while_BoolExp", type=while_While, multiplicity=Multiplicity(1, 1)),
        Property(name="while_While", type=while_BoolExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then6: BinaryAssociation = BinaryAssociation(
    name="then6",
    ends={
        Property(name="while_Statement8", type=while_While, multiplicity=Multiplicity(1, 1)),
        Property(name="while_While7", type=while_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next10: BinaryAssociation = BinaryAssociation(
    name="next10",
    ends={
        Property(name="while_Statement11", type=while_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="while_Statement9", type=while_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first0: BinaryAssociation = BinaryAssociation(
    name="first0",
    ends={
        Property(name="while_Statement", type=while_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="while_Program", type=while_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables1: BinaryAssociation = BinaryAssociation(
    name="variables1",
    ends={
        Property(name="while_Var", type=while_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="while_Program2", type=while_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs20: BinaryAssociation = BinaryAssociation(
    name="lhs20",
    ends={
        Property(name="while_Exp", type=while_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="while_BinaryExp", type=while_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs21: BinaryAssociation = BinaryAssociation(
    name="rhs21",
    ends={
        Property(name="while_Exp23", type=while_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="while_BinaryExp22", type=while_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition12: BinaryAssociation = BinaryAssociation(
    name="condition12",
    ends={
        Property(name="while_BoolExp13", type=while_If, multiplicity=Multiplicity(1, 1)),
        Property(name="while_If", type=while_BoolExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then14: BinaryAssociation = BinaryAssociation(
    name="then14",
    ends={
        Property(name="while_Statement16", type=while_If, multiplicity=Multiplicity(1, 1)),
        Property(name="while_If15", type=while_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else17: BinaryAssociation = BinaryAssociation(
    name="else17",
    ends={
        Property(name="while_Statement19", type=while_If, multiplicity=Multiplicity(1, 1)),
        Property(name="while_If18", type=while_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var26: BinaryAssociation = BinaryAssociation(
    name="var26",
    ends={
        Property(name="while_Assignment", type=while_Var, multiplicity=Multiplicity(0, 1)),
        Property(name="while_Var27", type=while_Assignment, multiplicity=Multiplicity(1, 1))
    }
)
exp28: BinaryAssociation = BinaryAssociation(
    name="exp28",
    ends={
        Property(name="while_Exp30", type=while_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="while_Assignment29", type=while_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp31: BinaryAssociation = BinaryAssociation(
    name="exp31",
    ends={
        Property(name="while_Exp32", type=while_Ret, multiplicity=Multiplicity(1, 1)),
        Property(name="while_Ret", type=while_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var24: BinaryAssociation = BinaryAssociation(
    name="var24",
    ends={
        Property(name="while_Var25", type=while_VarExp, multiplicity=Multiplicity(1, 1)),
        Property(name="while_VarExp", type=while_Var, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_while_While_Statement = Generalization(general=Statement, specific=while_While)
gen_while_If_Statement = Generalization(general=Statement, specific=while_If)
gen_while_NEqExp_BinaryExp = Generalization(general=BinaryExp, specific=while_NEqExp)
gen_while_NEqExp_BoolExp = Generalization(general=BoolExp, specific=while_NEqExp)
gen_while_BinaryExp_Exp = Generalization(general=Exp, specific=while_BinaryExp)
gen_while_BoolExp_Exp = Generalization(general=Exp, specific=while_BoolExp)
gen_while_AndExp_BinaryExp = Generalization(general=BinaryExp, specific=while_AndExp)
gen_while_AndExp_BoolExp = Generalization(general=BoolExp, specific=while_AndExp)
gen_while_EqExp_BinaryExp = Generalization(general=BinaryExp, specific=while_EqExp)
gen_while_EqExp_BoolExp = Generalization(general=BoolExp, specific=while_EqExp)
gen_while_Ret_Statement = Generalization(general=Statement, specific=while_Ret)
gen_while_Val_Exp = Generalization(general=Exp, specific=while_Val)
gen_while_VarExp_Exp = Generalization(general=Exp, specific=while_VarExp)
gen_while_Assignment_Statement = Generalization(general=Statement, specific=while_Assignment)

# Domain Model
domain_model = DomainModel(
    name="while",
    types={while_While, Statement, while_BoolExp, while_If, while_Program, while_Statement, while_Var, while_Val, while_NEqExp, while_BinaryExp, Exp, while_Exp, while_AndExp, while_EqExp, BinaryExp, BoolExp, while_Ret, while_VarExp, while_Assignment},
    associations={literals3, condition5, then6, next10, first0, variables1, lhs20, rhs21, condition12, then14, else17, var26, exp28, exp31, var24},
    generalizations={gen_while_While_Statement, gen_while_If_Statement, gen_while_NEqExp_BinaryExp, gen_while_NEqExp_BoolExp, gen_while_BinaryExp_Exp, gen_while_BoolExp_Exp, gen_while_AndExp_BinaryExp, gen_while_AndExp_BoolExp, gen_while_EqExp_BinaryExp, gen_while_EqExp_BoolExp, gen_while_Ret_Statement, gen_while_Val_Exp, gen_while_VarExp_Exp, gen_while_Assignment_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)