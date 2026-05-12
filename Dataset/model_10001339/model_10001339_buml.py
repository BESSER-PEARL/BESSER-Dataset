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
C1 = Class(name="C1")
C2 = Class(name="C2")
C3 = Class(name="C3")

# C1 class attributes and methods
C1_i3: Property = Property(name="i3", type=IntegerType)
C1.attributes={C1_i3}

# C2 class attributes and methods
C2_b1: Property = Property(name="b1", type=BooleanType)
C2.attributes={C2_b1}

# C3 class attributes and methods
C3_i3: Property = Property(name="i3", type=IntegerType)
C3.attributes={C3_i3}

# Relationships
C1_C2: BinaryAssociation = BinaryAssociation(
    name="C1_C2",
    ends={
        Property(name="c20", type=C2, multiplicity=Multiplicity(0, 1)),
        Property(name="c11", type=C1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0mMLYNK1EeiczqJWtOPN4Q",
    types={C1, C2, C3},
    associations={C1_C2},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)