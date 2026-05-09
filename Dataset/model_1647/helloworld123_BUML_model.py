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
NamedElement = Class(name="NamedElement")
helloworld123_RelatedTo = Class(name="helloworld123_RelatedTo")
helloworld123_NamedElement = Class(name="helloworld123_NamedElement", is_abstract=True)
helloworld123_World = Class(name="helloworld123_World")
helloworld123_Thing = Class(name="helloworld123_Thing")
helloworld123_Alias = Class(name="helloworld123_Alias")

# NamedElement class attributes and methods

# helloworld123_RelatedTo class attributes and methods
helloworld123_RelatedTo_since: Property = Property(name="since", type=StringType)
helloworld123_RelatedTo.attributes={helloworld123_RelatedTo_since}

# helloworld123_NamedElement class attributes and methods
helloworld123_NamedElement_name: Property = Property(name="name", type=StringType)
helloworld123_NamedElement.attributes={helloworld123_NamedElement_name}

# helloworld123_World class attributes and methods

# helloworld123_Thing class attributes and methods
helloworld123_Thing_id: Property = Property(name="id", type=IntegerType)
helloworld123_Thing.attributes={helloworld123_Thing_id}

# helloworld123_Alias class attributes and methods
helloworld123_Alias_id: Property = Property(name="id", type=StringType)
helloworld123_Alias.attributes={helloworld123_Alias_id}

# Relationships
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=helloworld123_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=helloworld123_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="helloworld123_Thing", type=helloworld123_World, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld123_World", type=helloworld123_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases2: BinaryAssociation = BinaryAssociation(
    name="aliases2",
    ends={
        Property(name="helloworld123_Alias", type=helloworld123_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld123_NamedElement", type=helloworld123_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing3: BinaryAssociation = BinaryAssociation(
    name="fromThing3",
    ends={
        Property(name="Thing", type=helloworld123_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=helloworld123_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing4: BinaryAssociation = BinaryAssociation(
    name="toThing4",
    ends={
        Property(name="helloworld123_Thing5", type=helloworld123_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld123_RelatedTo", type=helloworld123_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_helloworld123_Thing_NamedElement = Generalization(general=NamedElement, specific=helloworld123_Thing)
gen_helloworld123_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=helloworld123_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="helloworld123",
    types={NamedElement, helloworld123_RelatedTo, helloworld123_NamedElement, helloworld123_World, helloworld123_Thing, helloworld123_Alias},
    associations={relations1, things0, aliases2, fromThing3, toThing4},
    generalizations={gen_helloworld123_Thing_NamedElement, gen_helloworld123_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)