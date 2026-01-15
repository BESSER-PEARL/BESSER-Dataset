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
d_D = Class(name="d::D")

# d_D class attributes and methods
d_D_name: Property = Property(name="name", type=StringType)
d_D_atts: Property = Property(name="atts", type=StringType)
d_D.attributes={d_D_atts, d_D_name}

# Relationships
refs1: BinaryAssociation = BinaryAssociation(
    name="refs1",
    ends={
        Property(name="d_D", type=d_D, multiplicity=Multiplicity(1, 1)),
        Property(name="d_D0", type=d_D, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="d",
    types={d_D},
    associations={refs1},
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