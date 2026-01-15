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
simpleworld_World = Class(name="simpleworld::World")
simpleworld_Thing = Class(name="simpleworld::Thing")
NamedElement = Class(name="NamedElement")
simpleworld_RelatedTo = Class(name="simpleworld::RelatedTo")
simpleworld_NamedElement = Class(name="simpleworld::NamedElement", is_abstract=True)

# simpleworld_World class attributes and methods

# simpleworld_Thing class attributes and methods
simpleworld_Thing_id: Property = Property(name="id", type=IntegerType)
simpleworld_Thing.attributes={simpleworld_Thing_id}

# NamedElement class attributes and methods

# simpleworld_RelatedTo class attributes and methods
simpleworld_RelatedTo_since: Property = Property(name="since", type=StringType)
simpleworld_RelatedTo.attributes={simpleworld_RelatedTo_since}

# simpleworld_NamedElement class attributes and methods
simpleworld_NamedElement_name: Property = Property(name="name", type=StringType)
simpleworld_NamedElement.attributes={simpleworld_NamedElement_name}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="simpleworld_Thing", type=simpleworld_World, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld_World", type=simpleworld_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing2: BinaryAssociation = BinaryAssociation(
    name="fromThing2",
    ends={
        Property(name="Thing", type=simpleworld_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=simpleworld_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing3: BinaryAssociation = BinaryAssociation(
    name="toThing3",
    ends={
        Property(name="simpleworld_Thing4", type=simpleworld_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld_RelatedTo", type=simpleworld_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=simpleworld_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=simpleworld_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_simpleworld_Thing_NamedElement = Generalization(general=NamedElement, specific=simpleworld_Thing)
gen_simpleworld_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=simpleworld_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="simpleworld",
    types={simpleworld_World, simpleworld_Thing, NamedElement, simpleworld_RelatedTo, simpleworld_NamedElement},
    associations={things0, fromThing2, toThing3, relations1},
    generalizations={gen_simpleworld_Thing_NamedElement, gen_simpleworld_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)