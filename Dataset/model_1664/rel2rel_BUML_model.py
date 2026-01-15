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
rel2rel_Thing = Class(name="rel2rel::Thing")
NamedElement = Class(name="NamedElement")
rel2rel_World = Class(name="rel2rel::World")
rel2rel_RelatedTo = Class(name="rel2rel::RelatedTo")
rel2rel_NamedElement = Class(name="rel2rel::NamedElement", is_abstract=True)
Thing = Class(name="Thing")

# rel2rel_Thing class attributes and methods
rel2rel_Thing_id: Property = Property(name="id", type=IntegerType)
rel2rel_Thing.attributes={rel2rel_Thing_id}

# NamedElement class attributes and methods

# rel2rel_World class attributes and methods

# rel2rel_RelatedTo class attributes and methods
rel2rel_RelatedTo_since: Property = Property(name="since", type=StringType)
rel2rel_RelatedTo.attributes={rel2rel_RelatedTo_since}

# rel2rel_NamedElement class attributes and methods
rel2rel_NamedElement_name: Property = Property(name="name", type=StringType)
rel2rel_NamedElement.attributes={rel2rel_NamedElement_name}

# Thing class attributes and methods

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="rel2rel_Thing", type=rel2rel_World, multiplicity=Multiplicity(1, 1)),
        Property(name="rel2rel_World", type=rel2rel_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=rel2rel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=rel2rel_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing2: BinaryAssociation = BinaryAssociation(
    name="fromThing2",
    ends={
        Property(name="Thing", type=rel2rel_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=rel2rel_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing3: BinaryAssociation = BinaryAssociation(
    name="toThing3",
    ends={
        Property(name="rel2rel_Thing4", type=rel2rel_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="rel2rel_RelatedTo", type=rel2rel_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toRelation6: BinaryAssociation = BinaryAssociation(
    name="toRelation6",
    ends={
        Property(name="rel2rel_RelatedTo7", type=rel2rel_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="rel2rel_RelatedTo5", type=rel2rel_RelatedTo, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_rel2rel_Thing_NamedElement = Generalization(general=NamedElement, specific=rel2rel_Thing)
gen_rel2rel_RelatedTo_Thing = Generalization(general=Thing, specific=rel2rel_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="rel2rel",
    types={rel2rel_Thing, NamedElement, rel2rel_World, rel2rel_RelatedTo, rel2rel_NamedElement, Thing},
    associations={things0, relations1, fromThing2, toThing3, toRelation6},
    generalizations={gen_rel2rel_Thing_NamedElement, gen_rel2rel_RelatedTo_Thing},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)