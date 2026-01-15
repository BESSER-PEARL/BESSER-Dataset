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
genealogy_Genealogy = Class(name="genealogy::Genealogy")
genealogy_Person = Class(name="genealogy::Person")

# genealogy_Genealogy class attributes and methods

# genealogy_Person class attributes and methods
genealogy_Person_name: Property = Property(name="name", type=StringType)
genealogy_Person_age: Property = Property(name="age", type=IntegerType)
genealogy_Person_alive: Property = Property(name="alive", type=BooleanType)
genealogy_Person.attributes={genealogy_Person_age, genealogy_Person_name, genealogy_Person_alive}

# Relationships
parents2: BinaryAssociation = BinaryAssociation(
    name="parents2",
    ends={
        Property(name="Person", type=genealogy_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=genealogy_Person, multiplicity=Multiplicity(0, 2))
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="Person5", type=genealogy_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=genealogy_Person, multiplicity=Multiplicity(0, 9999))
    }
)
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="genealogy_Person", type=genealogy_Genealogy, multiplicity=Multiplicity(1, 1)),
        Property(name="genealogy_Genealogy", type=genealogy_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="genealogy",
    types={genealogy_Genealogy, genealogy_Person},
    associations={parents2, children4, persons0},
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