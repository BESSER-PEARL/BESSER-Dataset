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
hutnArticleFamilies_Family = Class(name="hutnArticleFamilies::Family")
hutnArticleFamilies_Person = Class(name="hutnArticleFamilies::Person")

# hutnArticleFamilies_Family class attributes and methods
hutnArticleFamilies_Family_name: Property = Property(name="name", type=StringType)
hutnArticleFamilies_Family_nuclear: Property = Property(name="nuclear", type=BooleanType)
hutnArticleFamilies_Family_migrant: Property = Property(name="migrant", type=BooleanType)
hutnArticleFamilies_Family_lotteryNumbers: Property = Property(name="lotteryNumbers", type=IntegerType)
hutnArticleFamilies_Family.attributes={hutnArticleFamilies_Family_migrant, hutnArticleFamilies_Family_nuclear, hutnArticleFamilies_Family_name, hutnArticleFamilies_Family_lotteryNumbers}

# hutnArticleFamilies_Person class attributes and methods
hutnArticleFamilies_Person_name: Property = Property(name="name", type=StringType)
hutnArticleFamilies_Person.attributes={hutnArticleFamilies_Person_name}

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="hutnArticleFamilies_Family", type=hutnArticleFamilies_Person, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="hutnArticleFamilies_Person", type=hutnArticleFamilies_Family, multiplicity=Multiplicity(1, 1))
    }
)
familyFriends2: BinaryAssociation = BinaryAssociation(
    name="familyFriends2",
    ends={
        Property(name="hutnArticleFamilies_Family3", type=hutnArticleFamilies_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="hutnArticleFamilies_Family1", type=hutnArticleFamilies_Family, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="hutnArticleFamilies",
    types={hutnArticleFamilies_Family, hutnArticleFamilies_Person},
    associations={members0, familyFriends2},
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