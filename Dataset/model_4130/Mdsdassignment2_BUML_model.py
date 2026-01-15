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
mdsdassignment2_ExpOp = Class(name="mdsdassignment2::ExpOp")
mdsdassignment2_Parenthesis = Class(name="mdsdassignment2::Parenthesis")
ExpOp = Class(name="ExpOp")
mdsdassignment2_MathExp = Class(name="mdsdassignment2::MathExp")
mdsdassignment2_Exp = Class(name="mdsdassignment2::Exp")
mdsdassignment2_Num = Class(name="mdsdassignment2::Num")
mdsdassignment2_Add = Class(name="mdsdassignment2::Add")
mdsdassignment2_Sub = Class(name="mdsdassignment2::Sub")
mdsdassignment2_Mult = Class(name="mdsdassignment2::Mult")
mdsdassignment2_Div = Class(name="mdsdassignment2::Div")

# mdsdassignment2_ExpOp class attributes and methods

# mdsdassignment2_Parenthesis class attributes and methods

# ExpOp class attributes and methods

# mdsdassignment2_MathExp class attributes and methods

# mdsdassignment2_Exp class attributes and methods

# mdsdassignment2_Num class attributes and methods
mdsdassignment2_Num_value: Property = Property(name="value", type=IntegerType)
mdsdassignment2_Num.attributes={mdsdassignment2_Num_value}

# mdsdassignment2_Add class attributes and methods

# mdsdassignment2_Sub class attributes and methods

# mdsdassignment2_Mult class attributes and methods

# mdsdassignment2_Div class attributes and methods

# Relationships
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="mdsdassignment2_ExpOp", type=mdsdassignment2_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Exp2", type=mdsdassignment2_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator3: BinaryAssociation = BinaryAssociation(
    name="operator3",
    ends={
        Property(name="mdsdassignment2_ExpOp5", type=mdsdassignment2_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Exp4", type=mdsdassignment2_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right7: BinaryAssociation = BinaryAssociation(
    name="right7",
    ends={
        Property(name="mdsdassignment2_Exp8", type=mdsdassignment2_Exp, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Exp6", type=mdsdassignment2_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp9: BinaryAssociation = BinaryAssociation(
    name="exp9",
    ends={
        Property(name="mdsdassignment2_Exp10", type=mdsdassignment2_Parenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Parenthesis", type=mdsdassignment2_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp0: BinaryAssociation = BinaryAssociation(
    name="exp0",
    ends={
        Property(name="mdsdassignment2_Exp", type=mdsdassignment2_MathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_MathExp", type=mdsdassignment2_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left11: BinaryAssociation = BinaryAssociation(
    name="left11",
    ends={
        Property(name="mdsdassignment2_ExpOp12", type=mdsdassignment2_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Add", type=mdsdassignment2_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right13: BinaryAssociation = BinaryAssociation(
    name="right13",
    ends={
        Property(name="mdsdassignment2_ExpOp15", type=mdsdassignment2_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Add14", type=mdsdassignment2_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left16: BinaryAssociation = BinaryAssociation(
    name="left16",
    ends={
        Property(name="mdsdassignment2_ExpOp17", type=mdsdassignment2_Sub, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Sub", type=mdsdassignment2_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right18: BinaryAssociation = BinaryAssociation(
    name="right18",
    ends={
        Property(name="mdsdassignment2_ExpOp20", type=mdsdassignment2_Sub, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Sub19", type=mdsdassignment2_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left21: BinaryAssociation = BinaryAssociation(
    name="left21",
    ends={
        Property(name="mdsdassignment2_ExpOp22", type=mdsdassignment2_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Mult", type=mdsdassignment2_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right23: BinaryAssociation = BinaryAssociation(
    name="right23",
    ends={
        Property(name="mdsdassignment2_ExpOp25", type=mdsdassignment2_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Mult24", type=mdsdassignment2_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left26: BinaryAssociation = BinaryAssociation(
    name="left26",
    ends={
        Property(name="mdsdassignment2_ExpOp27", type=mdsdassignment2_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Div", type=mdsdassignment2_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right28: BinaryAssociation = BinaryAssociation(
    name="right28",
    ends={
        Property(name="mdsdassignment2_ExpOp30", type=mdsdassignment2_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="mdsdassignment2_Div29", type=mdsdassignment2_ExpOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mdsdassignment2_Parenthesis_ExpOp = Generalization(general=ExpOp, specific=mdsdassignment2_Parenthesis)
gen_mdsdassignment2_Num_ExpOp = Generalization(general=ExpOp, specific=mdsdassignment2_Num)
gen_mdsdassignment2_Add_ExpOp = Generalization(general=ExpOp, specific=mdsdassignment2_Add)
gen_mdsdassignment2_Sub_ExpOp = Generalization(general=ExpOp, specific=mdsdassignment2_Sub)
gen_mdsdassignment2_Mult_ExpOp = Generalization(general=ExpOp, specific=mdsdassignment2_Mult)
gen_mdsdassignment2_Div_ExpOp = Generalization(general=ExpOp, specific=mdsdassignment2_Div)

# Domain Model
domain_model = DomainModel(
    name="mdsdassignment2",
    types={mdsdassignment2_ExpOp, mdsdassignment2_Parenthesis, ExpOp, mdsdassignment2_MathExp, mdsdassignment2_Exp, mdsdassignment2_Num, mdsdassignment2_Add, mdsdassignment2_Sub, mdsdassignment2_Mult, mdsdassignment2_Div},
    associations={left1, operator3, right7, exp9, exp0, left11, right13, left16, right18, left21, right23, left26, right28},
    generalizations={gen_mdsdassignment2_Parenthesis_ExpOp, gen_mdsdassignment2_Num_ExpOp, gen_mdsdassignment2_Add_ExpOp, gen_mdsdassignment2_Sub_ExpOp, gen_mdsdassignment2_Mult_ExpOp, gen_mdsdassignment2_Div_ExpOp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)