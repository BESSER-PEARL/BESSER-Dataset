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
binDsl_B = Class(name="binDsl::B")
binDsl_N = Class(name="binDsl::N")
binDsl_L = Class(name="binDsl::L")

# binDsl_B class attributes and methods
binDsl_B_b: Property = Property(name="b", type=StringType)
binDsl_B.attributes={binDsl_B_b}

# binDsl_N class attributes and methods
binDsl_N_cond: Property = Property(name="cond", type=BooleanType)
binDsl_N.attributes={binDsl_N_cond}

# binDsl_L class attributes and methods

# Relationships
v21: BinaryAssociation = BinaryAssociation(
    name="v21",
    ends={
        Property(name="binDsl_L3", type=binDsl_N, multiplicity=Multiplicity(1, 1)),
        Property(name="binDsl_N2", type=binDsl_L, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
v4: BinaryAssociation = BinaryAssociation(
    name="v4",
    ends={
        Property(name="binDsl_B", type=binDsl_L, multiplicity=Multiplicity(1, 1)),
        Property(name="binDsl_L5", type=binDsl_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
v10: BinaryAssociation = BinaryAssociation(
    name="v10",
    ends={
        Property(name="binDsl_L", type=binDsl_N, multiplicity=Multiplicity(1, 1)),
        Property(name="binDsl_N", type=binDsl_L, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="binDsl",
    types={binDsl_B, binDsl_N, binDsl_L},
    associations={v21, v4, v10},
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