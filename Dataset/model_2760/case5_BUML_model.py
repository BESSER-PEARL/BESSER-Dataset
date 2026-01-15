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
case5_A = Class(name="case5::A")
case5_B = Class(name="case5::B")
case5_D = Class(name="case5::D")
T = Class(name="T")
case5_N = Class(name="case5::N")
case5_T = Class(name="case5::T")
case5_E = Class(name="case5::E")
D = Class(name="D")

# case5_A class attributes and methods

# case5_B class attributes and methods

# case5_D class attributes and methods

# T class attributes and methods

# case5_N class attributes and methods

# case5_T class attributes and methods

# case5_E class attributes and methods

# D class attributes and methods

# Relationships
as1: BinaryAssociation = BinaryAssociation(
    name="as1",
    ends={
        Property(name="case5_A", type=case5_N, multiplicity=Multiplicity(1, 1)),
        Property(name="case5_N2", type=case5_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs3: BinaryAssociation = BinaryAssociation(
    name="bs3",
    ends={
        Property(name="case5_B", type=case5_N, multiplicity=Multiplicity(1, 1)),
        Property(name="case5_N4", type=case5_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ts0: BinaryAssociation = BinaryAssociation(
    name="ts0",
    ends={
        Property(name="case5_T", type=case5_N, multiplicity=Multiplicity(1, 1)),
        Property(name="case5_N", type=case5_T, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
d5: BinaryAssociation = BinaryAssociation(
    name="d5",
    ends={
        Property(name="case5_D", type=case5_A, multiplicity=Multiplicity(1, 1)),
        Property(name="case5_A6", type=case5_D, multiplicity=Multiplicity(0, 1))
    }
)
ds7: BinaryAssociation = BinaryAssociation(
    name="ds7",
    ends={
        Property(name="case5_D9", type=case5_B, multiplicity=Multiplicity(1, 1)),
        Property(name="case5_B8", type=case5_D, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_case5_D_T = Generalization(general=T, specific=case5_D)
gen_case5_E_D = Generalization(general=D, specific=case5_E)

# Domain Model
domain_model = DomainModel(
    name="case5",
    types={case5_A, case5_B, case5_D, T, case5_N, case5_T, case5_E, D},
    associations={as1, bs3, ts0, d5, ds7},
    generalizations={gen_case5_D_T, gen_case5_E_D},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)