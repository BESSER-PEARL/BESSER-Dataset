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
workbench101_Thing = Class(name="workbench101::Thing")
workbench101_Thoughts = Class(name="workbench101::Thoughts")
NamedElement = Class(name="NamedElement")
workbench101_RelatedTo = Class(name="workbench101::RelatedTo")
workbench101_Workbench = Class(name="workbench101::Workbench")
workbench101_NamedElement = Class(name="workbench101::NamedElement", is_abstract=True)

# workbench101_Thing class attributes and methods
workbench101_Thing_id: Property = Property(name="id", type=IntegerType)
workbench101_Thing.attributes={workbench101_Thing_id}

# workbench101_Thoughts class attributes and methods

# NamedElement class attributes and methods

# workbench101_RelatedTo class attributes and methods
workbench101_RelatedTo_since: Property = Property(name="since", type=StringType)
workbench101_RelatedTo.attributes={workbench101_RelatedTo_since}

# workbench101_Workbench class attributes and methods
workbench101_Workbench_aprop: Property = Property(name="aprop", type=StringType)
workbench101_Workbench.attributes={workbench101_Workbench_aprop}

# workbench101_NamedElement class attributes and methods
workbench101_NamedElement_name: Property = Property(name="name", type=StringType)
workbench101_NamedElement.attributes={workbench101_NamedElement_name}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="workbench101_Thing", type=workbench101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="workbench101_Workbench", type=workbench101_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoughts1: BinaryAssociation = BinaryAssociation(
    name="thoughts1",
    ends={
        Property(name="workbench101_Thoughts", type=workbench101_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="workbench101_Workbench2", type=workbench101_Thoughts, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toThing5: BinaryAssociation = BinaryAssociation(
    name="toThing5",
    ends={
        Property(name="workbench101_Thing6", type=workbench101_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="workbench101_RelatedTo", type=workbench101_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relatedTo7: BinaryAssociation = BinaryAssociation(
    name="relatedTo7",
    ends={
        Property(name="workbench101_Thing9", type=workbench101_Thoughts, multiplicity=Multiplicity(1, 1)),
        Property(name="workbench101_Thoughts8", type=workbench101_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
relations3: BinaryAssociation = BinaryAssociation(
    name="relations3",
    ends={
        Property(name="RelatedTo", type=workbench101_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=workbench101_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing4: BinaryAssociation = BinaryAssociation(
    name="fromThing4",
    ends={
        Property(name="Thing", type=workbench101_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=workbench101_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_workbench101_Thing_NamedElement = Generalization(general=NamedElement, specific=workbench101_Thing)
gen_workbench101_Thoughts_NamedElement = Generalization(general=NamedElement, specific=workbench101_Thoughts)
gen_workbench101_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=workbench101_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="workbench101",
    types={workbench101_Thing, workbench101_Thoughts, NamedElement, workbench101_RelatedTo, workbench101_Workbench, workbench101_NamedElement},
    associations={things0, thoughts1, toThing5, relatedTo7, relations3, fromThing4},
    generalizations={gen_workbench101_Thing_NamedElement, gen_workbench101_Thoughts_NamedElement, gen_workbench101_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)