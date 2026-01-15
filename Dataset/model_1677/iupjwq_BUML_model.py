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
iupjwq_World = Class(name="iupjwq::World")
iupjwq_Thing = Class(name="iupjwq::Thing")
iupjwq_RelatedTo = Class(name="iupjwq::RelatedTo")

# iupjwq_World class attributes and methods

# iupjwq_Thing class attributes and methods
iupjwq_Thing_id: Property = Property(name="id", type=IntegerType)
iupjwq_Thing.attributes={iupjwq_Thing_id}

# iupjwq_RelatedTo class attributes and methods
iupjwq_RelatedTo_since: Property = Property(name="since", type=StringType)
iupjwq_RelatedTo.attributes={iupjwq_RelatedTo_since}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="iupjwq_Thing", type=iupjwq_World, multiplicity=Multiplicity(1, 1)),
        Property(name="iupjwq_World", type=iupjwq_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=iupjwq_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=iupjwq_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing2: BinaryAssociation = BinaryAssociation(
    name="fromThing2",
    ends={
        Property(name="Thing", type=iupjwq_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=iupjwq_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing3: BinaryAssociation = BinaryAssociation(
    name="toThing3",
    ends={
        Property(name="iupjwq_Thing4", type=iupjwq_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="iupjwq_RelatedTo", type=iupjwq_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="iupjwq",
    types={iupjwq_World, iupjwq_Thing, iupjwq_RelatedTo},
    associations={things0, relations1, fromThing2, toThing3},
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