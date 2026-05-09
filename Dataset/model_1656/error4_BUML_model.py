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
error4_Thing = Class(name="error4_Thing")
NamedElement = Class(name="NamedElement")
error4_RelatedTo = Class(name="error4_RelatedTo")
error4_Component = Class(name="error4_Component")
error4_World = Class(name="error4_World")
error4_NamedElement = Class(name="error4_NamedElement", is_abstract=True)

# error4_Thing class attributes and methods
error4_Thing_id: Property = Property(name="id", type=IntegerType)
error4_Thing.attributes={error4_Thing_id}

# NamedElement class attributes and methods

# error4_RelatedTo class attributes and methods
error4_RelatedTo_since: Property = Property(name="since", type=StringType)
error4_RelatedTo.attributes={error4_RelatedTo_since}

# error4_Component class attributes and methods

# error4_World class attributes and methods

# error4_NamedElement class attributes and methods
error4_NamedElement_name: Property = Property(name="name", type=StringType)
error4_NamedElement.attributes={error4_NamedElement_name}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="error4_Thing", type=error4_World, multiplicity=Multiplicity(1, 1)),
        Property(name="error4_World", type=error4_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=error4_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=error4_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components2: BinaryAssociation = BinaryAssociation(
    name="components2",
    ends={
        Property(name="error4_Component", type=error4_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="error4_Thing3", type=error4_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toComponent7: BinaryAssociation = BinaryAssociation(
    name="toComponent7",
    ends={
        Property(name="error4_Component9", type=error4_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="error4_RelatedTo8", type=error4_Component, multiplicity=Multiplicity(0, 1))
    }
)
fromThing4: BinaryAssociation = BinaryAssociation(
    name="fromThing4",
    ends={
        Property(name="Thing", type=error4_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=error4_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing5: BinaryAssociation = BinaryAssociation(
    name="toThing5",
    ends={
        Property(name="error4_Thing6", type=error4_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="error4_RelatedTo", type=error4_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_error4_Thing_NamedElement = Generalization(general=NamedElement, specific=error4_Thing)
gen_error4_Component_NamedElement = Generalization(general=NamedElement, specific=error4_Component)
gen_error4_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=error4_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="error4",
    types={error4_Thing, NamedElement, error4_RelatedTo, error4_Component, error4_World, error4_NamedElement},
    associations={things0, relations1, components2, toComponent7, fromThing4, toThing5},
    generalizations={gen_error4_Thing_NamedElement, gen_error4_Component_NamedElement, gen_error4_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)