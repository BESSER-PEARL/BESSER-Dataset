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
linkinher_E = Class(name="linkinher::E", is_abstract=True)
Named = Class(name="Named")
linkinher_N = Class(name="linkinher::N")
linkinher_Named = Class(name="linkinher::Named", is_abstract=True)
T = Class(name="T")
S = Class(name="S")
linkinher_K = Class(name="linkinher::K")
linkinher_X = Class(name="linkinher::X")
linkinher_T = Class(name="linkinher::T", is_abstract=True)
linkinher_S = Class(name="linkinher::S", is_abstract=True)
linkinher_C = Class(name="linkinher::C", is_abstract=True)
linkinher_L = Class(name="linkinher::L")
C = Class(name="C")
linkinher_M = Class(name="linkinher::M")
E = Class(name="E")

# linkinher_E class attributes and methods

# Named class attributes and methods

# linkinher_N class attributes and methods

# linkinher_Named class attributes and methods
linkinher_Named_name: Property = Property(name="name", type=StringType)
linkinher_Named.attributes={linkinher_Named_name}

# T class attributes and methods

# S class attributes and methods

# linkinher_K class attributes and methods

# linkinher_X class attributes and methods

# linkinher_T class attributes and methods

# linkinher_S class attributes and methods

# linkinher_C class attributes and methods

# linkinher_L class attributes and methods

# C class attributes and methods

# linkinher_M class attributes and methods

# E class attributes and methods

# Relationships
net0: BinaryAssociation = BinaryAssociation(
    name="net0",
    ends={
        Property(name="linkinher_N", type=linkinher_E, multiplicity=Multiplicity(1, 1)),
        Property(name="linkinher_E", type=linkinher_N, multiplicity=Multiplicity(0, 1))
    }
)
nes1: BinaryAssociation = BinaryAssociation(
    name="nes1",
    ends={
        Property(name="linkinher_N3", type=linkinher_E, multiplicity=Multiplicity(1, 1)),
        Property(name="linkinher_E2", type=linkinher_N, multiplicity=Multiplicity(0, 1))
    }
)
nameds7: BinaryAssociation = BinaryAssociation(
    name="nameds7",
    ends={
        Property(name="linkinher_Named", type=linkinher_X, multiplicity=Multiplicity(1, 1)),
        Property(name="linkinher_X", type=linkinher_Named, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nx8: BinaryAssociation = BinaryAssociation(
    name="nx8",
    ends={
        Property(name="linkinher_N10", type=linkinher_X, multiplicity=Multiplicity(1, 1)),
        Property(name="linkinher_X9", type=linkinher_N, multiplicity=Multiplicity(1, 1))
    }
)
ns11: BinaryAssociation = BinaryAssociation(
    name="ns11",
    ends={
        Property(name="linkinher_N12", type=linkinher_S, multiplicity=Multiplicity(1, 1)),
        Property(name="linkinher_S", type=linkinher_N, multiplicity=Multiplicity(0, 1))
    }
)
es4: BinaryAssociation = BinaryAssociation(
    name="es4",
    ends={
        Property(name="linkinher_E6", type=linkinher_N, multiplicity=Multiplicity(1, 1)),
        Property(name="linkinher_N5", type=linkinher_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_linkinher_E_Named = Generalization(general=Named, specific=linkinher_E)
gen_linkinher_N_Named = Generalization(general=Named, specific=linkinher_N)
gen_linkinher_N_T = Generalization(general=T, specific=linkinher_N)
gen_linkinher_K_C = Generalization(general=C, specific=linkinher_K)
gen_linkinher_S_Named = Generalization(general=Named, specific=linkinher_S)
gen_linkinher_C_S = Generalization(general=S, specific=linkinher_C)
gen_linkinher_C_E = Generalization(general=E, specific=linkinher_C)
gen_linkinher_N_S = Generalization(general=S, specific=linkinher_N)
gen_linkinher_L_C = Generalization(general=C, specific=linkinher_L)
gen_linkinher_L_T = Generalization(general=T, specific=linkinher_L)
gen_linkinher_M_E = Generalization(general=E, specific=linkinher_M)

# Domain Model
domain_model = DomainModel(
    name="linkinher",
    types={linkinher_E, Named, linkinher_N, linkinher_Named, T, S, linkinher_K, linkinher_X, linkinher_T, linkinher_S, linkinher_C, linkinher_L, C, linkinher_M, E},
    associations={net0, nes1, nameds7, nx8, ns11, es4},
    generalizations={gen_linkinher_E_Named, gen_linkinher_N_Named, gen_linkinher_N_T, gen_linkinher_K_C, gen_linkinher_S_Named, gen_linkinher_C_S, gen_linkinher_C_E, gen_linkinher_N_S, gen_linkinher_L_C, gen_linkinher_L_T, gen_linkinher_M_E},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)