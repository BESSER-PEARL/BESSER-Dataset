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
helloworld123_Thing = Class(name="helloworld123::Thing")
NamedElement = Class(name="NamedElement")
helloworld123_World = Class(name="helloworld123::World")
helloworld123_RelatedTo = Class(name="helloworld123::RelatedTo")
helloworld123_NamedElement = Class(name="helloworld123::NamedElement", is_abstract=True)
helloworld123_Alias = Class(name="helloworld123::Alias")

# helloworld123_Thing class attributes and methods
helloworld123_Thing_id: Property = Property(name="id", type=IntegerType)
helloworld123_Thing.attributes={helloworld123_Thing_id}

# NamedElement class attributes and methods

# helloworld123_World class attributes and methods

# helloworld123_RelatedTo class attributes and methods
helloworld123_RelatedTo_since: Property = Property(name="since", type=StringType)
helloworld123_RelatedTo.attributes={helloworld123_RelatedTo_since}

# helloworld123_NamedElement class attributes and methods
helloworld123_NamedElement_name: Property = Property(name="name", type=StringType)
helloworld123_NamedElement.attributes={helloworld123_NamedElement_name}

# helloworld123_Alias class attributes and methods
helloworld123_Alias_id: Property = Property(name="id", type=StringType)
helloworld123_Alias.attributes={helloworld123_Alias_id}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="helloworld123_Thing", type=helloworld123_World, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld123_World", type=helloworld123_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases3: BinaryAssociation = BinaryAssociation(
    name="aliases3",
    ends={
        Property(name="helloworld123_NamedElement", type=helloworld123_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="helloworld123_Alias", type=helloworld123_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="2", type=helloworld123_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=helloworld123_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing4: BinaryAssociation = BinaryAssociation(
    name="fromThing4",
    ends={
        Property(name="6", type=helloworld123_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="5", type=helloworld123_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing7: BinaryAssociation = BinaryAssociation(
    name="toThing7",
    ends={
        Property(name="helloworld123_Thing8", type=helloworld123_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld123_RelatedTo", type=helloworld123_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_helloworld123_Thing_NamedElement = Generalization(general=NamedElement, specific=helloworld123_Thing)
gen_helloworld123_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=helloworld123_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="helloworld123",
    types={helloworld123_Thing, NamedElement, helloworld123_World, helloworld123_RelatedTo, helloworld123_NamedElement, helloworld123_Alias},
    associations={things0, aliases3, relations1, fromThing4, toThing7},
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