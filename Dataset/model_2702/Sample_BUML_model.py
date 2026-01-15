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
sample_A = Class(name="sample::A", is_abstract=True)
sample_B = Class(name="sample::B")
A = Class(name="A")
sample_C = Class(name="sample::C")

# sample_A class attributes and methods
sample_A_name: Property = Property(name="name", type=StringType)
sample_A_valid: Property = Property(name="valid", type=BooleanType)
sample_A_quantity: Property = Property(name="quantity", type=IntegerType)
sample_A.attributes={sample_A_quantity, sample_A_name, sample_A_valid}

# sample_B class attributes and methods
sample_B_label: Property = Property(name="label", type=StringType)
sample_B.attributes={sample_B_label}

# A class attributes and methods

# sample_C class attributes and methods

# Relationships
c0: BinaryAssociation = BinaryAssociation(
    name="c0",
    ends={
        Property(name="sample_C", type=sample_B, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_B", type=sample_C, multiplicity=Multiplicity(0, 9999))
    }
)
a1: BinaryAssociation = BinaryAssociation(
    name="a1",
    ends={
        Property(name="sample_A", type=sample_C, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_C2", type=sample_A, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sample_B_A = Generalization(general=A, specific=sample_B)

# Domain Model
domain_model = DomainModel(
    name="sample",
    types={sample_A, sample_B, A, sample_C},
    associations={c0, a1},
    generalizations={gen_sample_B_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)