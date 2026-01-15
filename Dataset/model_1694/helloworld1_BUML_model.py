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
helloworld1_World = Class(name="helloworld1::World")
helloworld1_Thing = Class(name="helloworld1::Thing")

# helloworld1_World class attributes and methods

# helloworld1_Thing class attributes and methods
helloworld1_Thing_id: Property = Property(name="id", type=IntegerType)
helloworld1_Thing.attributes={helloworld1_Thing_id}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="helloworld1_Thing", type=helloworld1_World, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld1_World", type=helloworld1_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things2: BinaryAssociation = BinaryAssociation(
    name="things2",
    ends={
        Property(name="helloworld1_Thing3", type=helloworld1_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld1_Thing1", type=helloworld1_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="helloworld1",
    types={helloworld1_World, helloworld1_Thing},
    associations={things0, things2},
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