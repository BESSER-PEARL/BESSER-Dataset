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
NamedElement = Class(name="NamedElement")
tbase_A = Class(name="tbase::A")
tbase_B = Class(name="tbase::B")
tbase_C = Class(name="tbase::C")
tbase_TRoot = Class(name="tbase::TRoot")
tbase_NamedElement = Class(name="tbase::NamedElement")

# NamedElement class attributes and methods

# tbase_A class attributes and methods

# tbase_B class attributes and methods

# tbase_C class attributes and methods

# tbase_TRoot class attributes and methods

# tbase_NamedElement class attributes and methods
tbase_NamedElement_name: Property = Property(name="name", type=StringType)
tbase_NamedElement.attributes={tbase_NamedElement_name}

# Relationships
ownsB0: BinaryAssociation = BinaryAssociation(
    name="ownsB0",
    ends={
        Property(name="tbase_B", type=tbase_A, multiplicity=Multiplicity(1, 1)),
        Property(name="tbase_A", type=tbase_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownsC1: BinaryAssociation = BinaryAssociation(
    name="ownsC1",
    ends={
        Property(name="tbase_C", type=tbase_B, multiplicity=Multiplicity(1, 1)),
        Property(name="tbase_B2", type=tbase_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedA3: BinaryAssociation = BinaryAssociation(
    name="ownedA3",
    ends={
        Property(name="tbase_A4", type=tbase_TRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="tbase_TRoot", type=tbase_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tbase_A_NamedElement = Generalization(general=NamedElement, specific=tbase_A)
gen_tbase_B_NamedElement = Generalization(general=NamedElement, specific=tbase_B)

# Domain Model
domain_model = DomainModel(
    name="tbase",
    types={NamedElement, tbase_A, tbase_B, tbase_C, tbase_TRoot, tbase_NamedElement},
    associations={ownsB0, ownsC1, ownedA3},
    generalizations={gen_tbase_A_NamedElement, gen_tbase_B_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)