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
ref3_D = Class(name="ref3::D")
T = Class(name="T")
ref3_N = Class(name="ref3::N")
Named = Class(name="Named")
ref3_T = Class(name="ref3::T")
ref3_Named = Class(name="ref3::Named")
ref3_A = Class(name="ref3::A")
ref3_B = Class(name="ref3::B")
D = Class(name="D")
ref3_E = Class(name="ref3::E")

# ref3_D class attributes and methods

# T class attributes and methods

# ref3_N class attributes and methods

# Named class attributes and methods

# ref3_T class attributes and methods

# ref3_Named class attributes and methods
ref3_Named_name: Property = Property(name="name", type=StringType)
ref3_Named.attributes={ref3_Named_name}

# ref3_A class attributes and methods

# ref3_B class attributes and methods

# D class attributes and methods

# ref3_E class attributes and methods

# Relationships
ts0: BinaryAssociation = BinaryAssociation(
    name="ts0",
    ends={
        Property(name="ref3_T", type=ref3_N, multiplicity=Multiplicity(1, 1)),
        Property(name="ref3_N", type=ref3_T, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ds5: BinaryAssociation = BinaryAssociation(
    name="ds5",
    ends={
        Property(name="ref3_D", type=ref3_A, multiplicity=Multiplicity(1, 1)),
        Property(name="ref3_A6", type=ref3_D, multiplicity=Multiplicity(0, 9999))
    }
)
as1: BinaryAssociation = BinaryAssociation(
    name="as1",
    ends={
        Property(name="ref3_A", type=ref3_N, multiplicity=Multiplicity(1, 1)),
        Property(name="ref3_N2", type=ref3_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs3: BinaryAssociation = BinaryAssociation(
    name="bs3",
    ends={
        Property(name="ref3_B", type=ref3_N, multiplicity=Multiplicity(1, 1)),
        Property(name="ref3_N4", type=ref3_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ds10: BinaryAssociation = BinaryAssociation(
    name="ds10",
    ends={
        Property(name="ref3_D11", type=ref3_E, multiplicity=Multiplicity(1, 1)),
        Property(name="ref3_E", type=ref3_D, multiplicity=Multiplicity(0, 1))
    }
)
ds7: BinaryAssociation = BinaryAssociation(
    name="ds7",
    ends={
        Property(name="ref3_D9", type=ref3_B, multiplicity=Multiplicity(1, 1)),
        Property(name="ref3_B8", type=ref3_D, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ref3_D_T = Generalization(general=T, specific=ref3_D)
gen_ref3_N_Named = Generalization(general=Named, specific=ref3_N)
gen_ref3_T_Named = Generalization(general=Named, specific=ref3_T)
gen_ref3_A_Named = Generalization(general=Named, specific=ref3_A)
gen_ref3_E_D = Generalization(general=D, specific=ref3_E)
gen_ref3_B_Named = Generalization(general=Named, specific=ref3_B)
gen_ref3_E_Named = Generalization(general=Named, specific=ref3_E)

# Domain Model
domain_model = DomainModel(
    name="ref3",
    types={ref3_D, T, ref3_N, Named, ref3_T, ref3_Named, ref3_A, ref3_B, D, ref3_E},
    associations={ts0, ds5, as1, bs3, ds10, ds7},
    generalizations={gen_ref3_D_T, gen_ref3_N_Named, gen_ref3_T_Named, gen_ref3_A_Named, gen_ref3_E_D, gen_ref3_B_Named, gen_ref3_E_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)