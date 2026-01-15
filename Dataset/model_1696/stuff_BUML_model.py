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
stuff_Thing = Class(name="stuff::Thing")
stuff_Property = Class(name="stuff::Property")
stuff_World = Class(name="stuff::World")

# stuff_Thing class attributes and methods
stuff_Thing_name: Property = Property(name="name", type=StringType)
stuff_Thing.attributes={stuff_Thing_name}

# stuff_Property class attributes and methods
stuff_Property_name: Property = Property(name="name", type=StringType)
stuff_Property_intrinsic: Property = Property(name="intrinsic", type=BooleanType)
stuff_Property.attributes={stuff_Property_intrinsic, stuff_Property_name}

# stuff_World class attributes and methods

# Relationships
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="stuff_Property", type=stuff_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="stuff_Thing", type=stuff_Property, multiplicity=Multiplicity(1, 9999))
    }
)
things1: BinaryAssociation = BinaryAssociation(
    name="things1",
    ends={
        Property(name="stuff_Thing2", type=stuff_World, multiplicity=Multiplicity(1, 1)),
        Property(name="stuff_World", type=stuff_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertiesOfThings3: BinaryAssociation = BinaryAssociation(
    name="propertiesOfThings3",
    ends={
        Property(name="stuff_Property5", type=stuff_World, multiplicity=Multiplicity(1, 1)),
        Property(name="stuff_World4", type=stuff_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="stuff",
    types={stuff_Thing, stuff_Property, stuff_World},
    associations={properties0, things1, propertiesOfThings3},
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