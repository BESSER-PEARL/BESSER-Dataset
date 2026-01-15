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
yyb_Thing = Class(name="yyb::Thing")
NamedElement = Class(name="NamedElement")
yyb_RelatedTo = Class(name="yyb::RelatedTo")
yyb_NamedElement = Class(name="yyb::NamedElement", is_abstract=True)
yyb_Alias = Class(name="yyb::Alias")

# yyb_Thing class attributes and methods
yyb_Thing_id: Property = Property(name="id", type=IntegerType)
yyb_Thing.attributes={yyb_Thing_id}

# NamedElement class attributes and methods

# yyb_RelatedTo class attributes and methods
yyb_RelatedTo_since: Property = Property(name="since", type=StringType)
yyb_RelatedTo.attributes={yyb_RelatedTo_since}

# yyb_NamedElement class attributes and methods
yyb_NamedElement_name: Property = Property(name="name", type=StringType)
yyb_NamedElement.attributes={yyb_NamedElement_name}

# yyb_Alias class attributes and methods
yyb_Alias_id: Property = Property(name="id", type=StringType)
yyb_Alias.attributes={yyb_Alias_id}

# Relationships
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="RelatedTo", type=yyb_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=yyb_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing1: BinaryAssociation = BinaryAssociation(
    name="fromThing1",
    ends={
        Property(name="Thing", type=yyb_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=yyb_Thing, multiplicity=Multiplicity(0, 1))
    }
)
aliases2: BinaryAssociation = BinaryAssociation(
    name="aliases2",
    ends={
        Property(name="yyb_Alias", type=yyb_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="yyb_RelatedTo", type=yyb_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_yyb_Thing_NamedElement = Generalization(general=NamedElement, specific=yyb_Thing)
gen_yyb_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=yyb_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="yyb",
    types={yyb_Thing, NamedElement, yyb_RelatedTo, yyb_NamedElement, yyb_Alias},
    associations={relations0, fromThing1, aliases2},
    generalizations={gen_yyb_Thing_NamedElement, gen_yyb_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)