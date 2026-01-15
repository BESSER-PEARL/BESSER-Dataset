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
detachelist_Contacts = Class(name="detachelist::Contacts")
detachelist_Person = Class(name="detachelist::Person")

# detachelist_Contacts class attributes and methods

# detachelist_Person class attributes and methods
detachelist_Person_name: Property = Property(name="name", type=StringType)
detachelist_Person.attributes={detachelist_Person_name}

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="detachelist_Person", type=detachelist_Contacts, multiplicity=Multiplicity(1, 1)),
        Property(name="detachelist_Contacts", type=detachelist_Person, multiplicity=Multiplicity(0, 9999))
    }
)
containedPersons1: BinaryAssociation = BinaryAssociation(
    name="containedPersons1",
    ends={
        Property(name="detachelist_Person3", type=detachelist_Contacts, multiplicity=Multiplicity(1, 1)),
        Property(name="detachelist_Contacts2", type=detachelist_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="detachelist_Person6", type=detachelist_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="detachelist_Person4", type=detachelist_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="detachelist",
    types={detachelist_Contacts, detachelist_Person},
    associations={persons0, containedPersons1, children5},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)