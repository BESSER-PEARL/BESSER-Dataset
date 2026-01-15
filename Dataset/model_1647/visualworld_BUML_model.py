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
visualworld_World = Class(name="visualworld::World")
visualworld_RelatedTo = Class(name="visualworld::RelatedTo")
visualworld_Thing = Class(name="visualworld::Thing")
NamedElement = Class(name="NamedElement")
visualworld_NamedElement = Class(name="visualworld::NamedElement", is_abstract=True)

# visualworld_World class attributes and methods

# visualworld_RelatedTo class attributes and methods
visualworld_RelatedTo_since: Property = Property(name="since", type=StringType)
visualworld_RelatedTo.attributes={visualworld_RelatedTo_since}

# visualworld_Thing class attributes and methods
visualworld_Thing_id: Property = Property(name="id", type=IntegerType)
visualworld_Thing.attributes={visualworld_Thing_id}

# NamedElement class attributes and methods

# visualworld_NamedElement class attributes and methods
visualworld_NamedElement_name: Property = Property(name="name", type=StringType)
visualworld_NamedElement.attributes={visualworld_NamedElement_name}

# Relationships
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=visualworld_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=visualworld_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="visualworld_Thing", type=visualworld_World, multiplicity=Multiplicity(1, 1)),
        Property(name="visualworld_World", type=visualworld_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toThing3: BinaryAssociation = BinaryAssociation(
    name="toThing3",
    ends={
        Property(name="visualworld_Thing4", type=visualworld_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="visualworld_RelatedTo", type=visualworld_Thing, multiplicity=Multiplicity(0, 1))
    }
)
fromThing2: BinaryAssociation = BinaryAssociation(
    name="fromThing2",
    ends={
        Property(name="Thing", type=visualworld_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=visualworld_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_visualworld_Thing_NamedElement = Generalization(general=NamedElement, specific=visualworld_Thing)
gen_visualworld_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=visualworld_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="visualworld",
    types={visualworld_World, visualworld_RelatedTo, visualworld_Thing, NamedElement, visualworld_NamedElement},
    associations={relations1, things0, toThing3, fromThing2},
    generalizations={gen_visualworld_Thing_NamedElement, gen_visualworld_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)