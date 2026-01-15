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
basic_World = Class(name="basic::World")
basic_Thing = Class(name="basic::Thing")
basic_RelatedTo = Class(name="basic::RelatedTo")

# basic_World class attributes and methods

# basic_Thing class attributes and methods
basic_Thing_id: Property = Property(name="id", type=IntegerType)
basic_Thing.attributes={basic_Thing_id}

# basic_RelatedTo class attributes and methods
basic_RelatedTo_since: Property = Property(name="since", type=StringType)
basic_RelatedTo.attributes={basic_RelatedTo_since}

# Relationships
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=basic_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=basic_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing2: BinaryAssociation = BinaryAssociation(
    name="fromThing2",
    ends={
        Property(name="Thing", type=basic_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=basic_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing3: BinaryAssociation = BinaryAssociation(
    name="toThing3",
    ends={
        Property(name="basic_Thing4", type=basic_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_RelatedTo", type=basic_Thing, multiplicity=Multiplicity(0, 1))
    }
)
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="basic_Thing", type=basic_World, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_World", type=basic_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="basic",
    types={basic_World, basic_Thing, basic_RelatedTo},
    associations={relations1, fromThing2, toThing3, things0},
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