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

# Enumerations
PetKind: Enumeration = Enumeration(
    name="PetKind",
    literals={
            EnumerationLiteral(name="FRIENDLY"),
			EnumerationLiteral(name="INDEPENDENT"),
			EnumerationLiteral(name="DANGEROUS")
    }
)

# Classes
people_Person = Class(name="people::Person")
people_Model = Class(name="people::Model")
people_Pet = Class(name="people::Pet")

# people_Person class attributes and methods
people_Person_name: Property = Property(name="name", type=StringType)
people_Person_nicknames: Property = Property(name="nicknames", type=StringType)
people_Person_age: Property = Property(name="age", type=IntegerType)
people_Person_alive: Property = Property(name="alive", type=BooleanType)
people_Person_luckyNumbers: Property = Property(name="luckyNumbers", type=IntegerType)
people_Person_lotteryChances: Property = Property(name="lotteryChances", type=StringType)
people_Person.attributes={people_Person_alive, people_Person_nicknames, people_Person_lotteryChances, people_Person_luckyNumbers, people_Person_name, people_Person_age}

# people_Model class attributes and methods

# people_Pet class attributes and methods
people_Pet_name: Property = Property(name="name", type=StringType)
people_Pet_kind: Property = Property(name="kind", type=StringType)
people_Pet.attributes={people_Pet_name, people_Pet_kind}

# Relationships
people0: BinaryAssociation = BinaryAssociation(
    name="people0",
    ends={
        Property(name="people_Person", type=people_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="people_Model", type=people_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bestFriend2: BinaryAssociation = BinaryAssociation(
    name="bestFriend2",
    ends={
        Property(name="people_Person3", type=people_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="people_Person1", type=people_Person, multiplicity=Multiplicity(0, 1))
    }
)
pets4: BinaryAssociation = BinaryAssociation(
    name="pets4",
    ends={
        Property(name="people_Pet", type=people_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="people_Person5", type=people_Pet, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="people",
    types={people_Person, people_Model, people_Pet, PetKind},
    associations={people0, bestFriend2, pets4},
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