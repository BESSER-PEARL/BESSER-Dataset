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
helloworldsaved_NamedElement = Class(name="helloworldsaved::NamedElement", is_abstract=True)
helloworldsaved_World = Class(name="helloworldsaved::World")
helloworldsaved_Thing = Class(name="helloworldsaved::Thing")
NamedElement = Class(name="NamedElement")
helloworldsaved_RelatedTo = Class(name="helloworldsaved::RelatedTo")
helloworldsaved_Alias = Class(name="helloworldsaved::Alias")

# helloworldsaved_NamedElement class attributes and methods
helloworldsaved_NamedElement_name: Property = Property(name="name", type=StringType)
helloworldsaved_NamedElement.attributes={helloworldsaved_NamedElement_name}

# helloworldsaved_World class attributes and methods

# helloworldsaved_Thing class attributes and methods
helloworldsaved_Thing_id: Property = Property(name="id", type=IntegerType)
helloworldsaved_Thing.attributes={helloworldsaved_Thing_id}

# NamedElement class attributes and methods

# helloworldsaved_RelatedTo class attributes and methods
helloworldsaved_RelatedTo_since: Property = Property(name="since", type=StringType)
helloworldsaved_RelatedTo.attributes={helloworldsaved_RelatedTo_since}

# helloworldsaved_Alias class attributes and methods
helloworldsaved_Alias_id: Property = Property(name="id", type=StringType)
helloworldsaved_Alias.attributes={helloworldsaved_Alias_id}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="helloworldsaved_Thing", type=helloworldsaved_World, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworldsaved_World", type=helloworldsaved_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=helloworldsaved_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=helloworldsaved_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases2: BinaryAssociation = BinaryAssociation(
    name="aliases2",
    ends={
        Property(name="helloworldsaved_Alias", type=helloworldsaved_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworldsaved_NamedElement", type=helloworldsaved_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing3: BinaryAssociation = BinaryAssociation(
    name="fromThing3",
    ends={
        Property(name="Thing", type=helloworldsaved_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=helloworldsaved_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing4: BinaryAssociation = BinaryAssociation(
    name="toThing4",
    ends={
        Property(name="helloworldsaved_Thing5", type=helloworldsaved_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworldsaved_RelatedTo", type=helloworldsaved_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_helloworldsaved_Thing_NamedElement = Generalization(general=NamedElement, specific=helloworldsaved_Thing)
gen_helloworldsaved_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=helloworldsaved_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="helloworldsaved",
    types={helloworldsaved_NamedElement, helloworldsaved_World, helloworldsaved_Thing, NamedElement, helloworldsaved_RelatedTo, helloworldsaved_Alias},
    associations={things0, relations1, aliases2, fromThing3, toThing4},
    generalizations={gen_helloworldsaved_Thing_NamedElement, gen_helloworldsaved_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)