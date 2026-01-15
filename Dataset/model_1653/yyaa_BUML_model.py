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
yyaa_World = Class(name="yyaa::World")
yyaa_Thing = Class(name="yyaa::Thing")
NamedElement = Class(name="NamedElement")
yyaa_RelatedTo = Class(name="yyaa::RelatedTo")
yyaa_NamedElement = Class(name="yyaa::NamedElement", is_abstract=True)
yyaa_Alias = Class(name="yyaa::Alias")

# yyaa_World class attributes and methods

# yyaa_Thing class attributes and methods
yyaa_Thing_id: Property = Property(name="id", type=IntegerType)
yyaa_Thing.attributes={yyaa_Thing_id}

# NamedElement class attributes and methods

# yyaa_RelatedTo class attributes and methods
yyaa_RelatedTo_since: Property = Property(name="since", type=StringType)
yyaa_RelatedTo.attributes={yyaa_RelatedTo_since}

# yyaa_NamedElement class attributes and methods
yyaa_NamedElement_name: Property = Property(name="name", type=StringType)
yyaa_NamedElement.attributes={yyaa_NamedElement_name}

# yyaa_Alias class attributes and methods
yyaa_Alias_id: Property = Property(name="id", type=StringType)
yyaa_Alias.attributes={yyaa_Alias_id}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="yyaa_Thing", type=yyaa_World, multiplicity=Multiplicity(1, 1)),
        Property(name="yyaa_World", type=yyaa_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="2", type=yyaa_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=yyaa_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases3: BinaryAssociation = BinaryAssociation(
    name="aliases3",
    ends={
        Property(name="yyaa_Alias", type=yyaa_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyaa_NamedElement", type=yyaa_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing4: BinaryAssociation = BinaryAssociation(
    name="fromThing4",
    ends={
        Property(name="6", type=yyaa_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="5", type=yyaa_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing7: BinaryAssociation = BinaryAssociation(
    name="toThing7",
    ends={
        Property(name="yyaa_Thing8", type=yyaa_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="yyaa_RelatedTo", type=yyaa_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_yyaa_Thing_NamedElement = Generalization(general=NamedElement, specific=yyaa_Thing)
gen_yyaa_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=yyaa_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="yyaa",
    types={yyaa_World, yyaa_Thing, NamedElement, yyaa_RelatedTo, yyaa_NamedElement, yyaa_Alias},
    associations={things0, relations1, aliases3, fromThing4, toThing7},
    generalizations={gen_yyaa_Thing_NamedElement, gen_yyaa_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)