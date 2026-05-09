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
errya_World = Class(name="errya_World")
errya_Thing = Class(name="errya_Thing")
NamedElement = Class(name="NamedElement")
errya_RelatedTo = Class(name="errya_RelatedTo")
errya_NamedElement = Class(name="errya_NamedElement", is_abstract=True)
errya_Alias = Class(name="errya_Alias")

# errya_World class attributes and methods

# errya_Thing class attributes and methods
errya_Thing_id: Property = Property(name="id", type=IntegerType)
errya_Thing.attributes={errya_Thing_id}

# NamedElement class attributes and methods

# errya_RelatedTo class attributes and methods
errya_RelatedTo_since: Property = Property(name="since", type=StringType)
errya_RelatedTo.attributes={errya_RelatedTo_since}

# errya_NamedElement class attributes and methods
errya_NamedElement_name: Property = Property(name="name", type=StringType)
errya_NamedElement.attributes={errya_NamedElement_name}

# errya_Alias class attributes and methods
errya_Alias_id: Property = Property(name="id", type=StringType)
errya_Alias.attributes={errya_Alias_id}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="errya_Thing", type=errya_World, multiplicity=Multiplicity(1, 1)),
        Property(name="errya_World", type=errya_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=errya_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=errya_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases2: BinaryAssociation = BinaryAssociation(
    name="aliases2",
    ends={
        Property(name="errya_Alias", type=errya_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="errya_NamedElement", type=errya_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing3: BinaryAssociation = BinaryAssociation(
    name="fromThing3",
    ends={
        Property(name="Thing", type=errya_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=errya_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing4: BinaryAssociation = BinaryAssociation(
    name="toThing4",
    ends={
        Property(name="errya_Thing5", type=errya_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="errya_RelatedTo", type=errya_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_errya_Thing_NamedElement = Generalization(general=NamedElement, specific=errya_Thing)
gen_errya_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=errya_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="errya",
    types={errya_World, errya_Thing, NamedElement, errya_RelatedTo, errya_NamedElement, errya_Alias},
    associations={things0, relations1, aliases2, fromThing3, toThing4},
    generalizations={gen_errya_Thing_NamedElement, gen_errya_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)