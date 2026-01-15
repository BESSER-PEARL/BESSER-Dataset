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
v125case5_D = Class(name="v125case5::D")
T = Class(name="T")
v125case5_N = Class(name="v125case5::N")
Named = Class(name="Named")
v125case5_T = Class(name="v125case5::T")
v125case5_E = Class(name="v125case5::E")
D = Class(name="D")
v125case5_A = Class(name="v125case5::A")
v125case5_B = Class(name="v125case5::B")
v125case5_Named = Class(name="v125case5::Named")

# v125case5_D class attributes and methods

# T class attributes and methods

# v125case5_N class attributes and methods

# Named class attributes and methods

# v125case5_T class attributes and methods

# v125case5_E class attributes and methods

# D class attributes and methods

# v125case5_A class attributes and methods

# v125case5_B class attributes and methods

# v125case5_Named class attributes and methods
v125case5_Named_name: Property = Property(name="name", type=StringType)
v125case5_Named.attributes={v125case5_Named_name}

# Relationships
ts0: BinaryAssociation = BinaryAssociation(
    name="ts0",
    ends={
        Property(name="v125case5_T", type=v125case5_N, multiplicity=Multiplicity(1, 1)),
        Property(name="v125case5_N", type=v125case5_T, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ds7: BinaryAssociation = BinaryAssociation(
    name="ds7",
    ends={
        Property(name="v125case5_D9", type=v125case5_B, multiplicity=Multiplicity(1, 1)),
        Property(name="v125case5_B8", type=v125case5_D, multiplicity=Multiplicity(0, 9999))
    }
)
as1: BinaryAssociation = BinaryAssociation(
    name="as1",
    ends={
        Property(name="v125case5_A", type=v125case5_N, multiplicity=Multiplicity(1, 1)),
        Property(name="v125case5_N2", type=v125case5_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs3: BinaryAssociation = BinaryAssociation(
    name="bs3",
    ends={
        Property(name="v125case5_B", type=v125case5_N, multiplicity=Multiplicity(1, 1)),
        Property(name="v125case5_N4", type=v125case5_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
d5: BinaryAssociation = BinaryAssociation(
    name="d5",
    ends={
        Property(name="v125case5_D", type=v125case5_A, multiplicity=Multiplicity(1, 1)),
        Property(name="v125case5_A6", type=v125case5_D, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_v125case5_D_T = Generalization(general=T, specific=v125case5_D)
gen_v125case5_N_Named = Generalization(general=Named, specific=v125case5_N)
gen_v125case5_E_Named = Generalization(general=Named, specific=v125case5_E)
gen_v125case5_E_D = Generalization(general=D, specific=v125case5_E)
gen_v125case5_T_Named = Generalization(general=Named, specific=v125case5_T)
gen_v125case5_A_Named = Generalization(general=Named, specific=v125case5_A)
gen_v125case5_B_Named = Generalization(general=Named, specific=v125case5_B)

# Domain Model
domain_model = DomainModel(
    name="v125case5",
    types={v125case5_D, T, v125case5_N, Named, v125case5_T, v125case5_E, D, v125case5_A, v125case5_B, v125case5_Named},
    associations={ts0, ds7, as1, bs3, d5},
    generalizations={gen_v125case5_D_T, gen_v125case5_N_Named, gen_v125case5_E_Named, gen_v125case5_E_D, gen_v125case5_T_Named, gen_v125case5_A_Named, gen_v125case5_B_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)