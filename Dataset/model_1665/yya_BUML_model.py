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
yya_Thing = Class(name="yya::Thing")
NamedElement = Class(name="NamedElement")
yya_RelatedTo = Class(name="yya::RelatedTo")
yya_NamedElement = Class(name="yya::NamedElement", is_abstract=True)
yya_Alias = Class(name="yya::Alias")

# yya_Thing class attributes and methods
yya_Thing_id: Property = Property(name="id", type=IntegerType)
yya_Thing.attributes={yya_Thing_id}

# NamedElement class attributes and methods

# yya_RelatedTo class attributes and methods
yya_RelatedTo_since: Property = Property(name="since", type=StringType)
yya_RelatedTo.attributes={yya_RelatedTo_since}

# yya_NamedElement class attributes and methods
yya_NamedElement_name: Property = Property(name="name", type=StringType)
yya_NamedElement.attributes={yya_NamedElement_name}

# yya_Alias class attributes and methods
yya_Alias_id: Property = Property(name="id", type=StringType)
yya_Alias.attributes={yya_Alias_id}

# Relationships
toThing3: BinaryAssociation = BinaryAssociation(
    name="toThing3",
    ends={
        Property(name="yya_Thing", type=yya_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="yya_RelatedTo", type=yya_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="RelatedTo", type=yya_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=yya_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases1: BinaryAssociation = BinaryAssociation(
    name="aliases1",
    ends={
        Property(name="yya_Alias", type=yya_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yya_NamedElement", type=yya_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing2: BinaryAssociation = BinaryAssociation(
    name="fromThing2",
    ends={
        Property(name="Thing", type=yya_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=yya_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_yya_Thing_NamedElement = Generalization(general=NamedElement, specific=yya_Thing)
gen_yya_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=yya_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="yya",
    types={yya_Thing, NamedElement, yya_RelatedTo, yya_NamedElement, yya_Alias},
    associations={toThing3, relations0, aliases1, fromThing2},
    generalizations={gen_yya_Thing_NamedElement, gen_yya_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)