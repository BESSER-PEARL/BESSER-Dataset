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
case4_D = Class(name="case4::D")
T = Class(name="T")
case4_N = Class(name="case4::N")
Named = Class(name="Named")
case4_A = Class(name="case4::A")
case4_B = Class(name="case4::B")
case4_T = Class(name="case4::T")
case4_Named = Class(name="case4::Named")
case4_E = Class(name="case4::E")
D = Class(name="D")

# case4_D class attributes and methods

# T class attributes and methods

# case4_N class attributes and methods

# Named class attributes and methods

# case4_A class attributes and methods

# case4_B class attributes and methods

# case4_T class attributes and methods

# case4_Named class attributes and methods
case4_Named_name: Property = Property(name="name", type=StringType)
case4_Named.attributes={case4_Named_name}

# case4_E class attributes and methods

# D class attributes and methods

# Relationships
ts0: BinaryAssociation = BinaryAssociation(
    name="ts0",
    ends={
        Property(name="case4_N", type=case4_T, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="case4_T", type=case4_N, multiplicity=Multiplicity(1, 1))
    }
)
as1: BinaryAssociation = BinaryAssociation(
    name="as1",
    ends={
        Property(name="case4_A", type=case4_N, multiplicity=Multiplicity(1, 1)),
        Property(name="case4_N2", type=case4_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs3: BinaryAssociation = BinaryAssociation(
    name="bs3",
    ends={
        Property(name="case4_B", type=case4_N, multiplicity=Multiplicity(1, 1)),
        Property(name="case4_N4", type=case4_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
d5: BinaryAssociation = BinaryAssociation(
    name="d5",
    ends={
        Property(name="case4_D", type=case4_A, multiplicity=Multiplicity(1, 1)),
        Property(name="case4_A6", type=case4_D, multiplicity=Multiplicity(0, 1))
    }
)
ds7: BinaryAssociation = BinaryAssociation(
    name="ds7",
    ends={
        Property(name="case4_D9", type=case4_B, multiplicity=Multiplicity(1, 1)),
        Property(name="case4_B8", type=case4_D, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_case4_D_T = Generalization(general=T, specific=case4_D)
gen_case4_N_Named = Generalization(general=Named, specific=case4_N)
gen_case4_T_Named = Generalization(general=Named, specific=case4_T)
gen_case4_A_Named = Generalization(general=Named, specific=case4_A)
gen_case4_E_Named = Generalization(general=Named, specific=case4_E)
gen_case4_E_D = Generalization(general=D, specific=case4_E)
gen_case4_B_Named = Generalization(general=Named, specific=case4_B)

# Domain Model
domain_model = DomainModel(
    name="case4",
    types={case4_D, T, case4_N, Named, case4_A, case4_B, case4_T, case4_Named, case4_E, D},
    associations={ts0, as1, bs3, d5, ds7},
    generalizations={gen_case4_D_T, gen_case4_N_Named, gen_case4_T_Named, gen_case4_A_Named, gen_case4_E_Named, gen_case4_E_D, gen_case4_B_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)