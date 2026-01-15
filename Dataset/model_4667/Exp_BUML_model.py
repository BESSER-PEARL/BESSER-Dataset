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
exp_Exp = Class(name="exp::Exp", is_abstract=True)
exp_Lit = Class(name="exp::Lit")
Exp = Class(name="Exp")
exp_Add = Class(name="exp::Add")

# exp_Exp class attributes and methods

# exp_Lit class attributes and methods
exp_Lit_value: Property = Property(name="value", type=IntegerType)
exp_Lit.attributes={exp_Lit_value}

# Exp class attributes and methods

# exp_Add class attributes and methods

# Relationships
lhs0: BinaryAssociation = BinaryAssociation(
    name="lhs0",
    ends={
        Property(name="exp_Exp", type=exp_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="exp_Add", type=exp_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs1: BinaryAssociation = BinaryAssociation(
    name="rhs1",
    ends={
        Property(name="exp_Exp3", type=exp_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="exp_Add2", type=exp_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_exp_Lit_Exp = Generalization(general=Exp, specific=exp_Lit)
gen_exp_Add_Exp = Generalization(general=Exp, specific=exp_Add)

# Domain Model
domain_model = DomainModel(
    name="exp",
    types={exp_Exp, exp_Lit, Exp, exp_Add},
    associations={lhs0, rhs1},
    generalizations={gen_exp_Lit_Exp, gen_exp_Add_Exp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)