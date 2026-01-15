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
family_Model = Class(name="family::Model")
family_Family = Class(name="family::Family")
family_Person = Class(name="family::Person")
family_Pet = Class(name="family::Pet")

# family_Model class attributes and methods

# family_Family class attributes and methods

# family_Person class attributes and methods
family_Person_name: Property = Property(name="name", type=StringType)
family_Person.attributes={family_Person_name}

# family_Pet class attributes and methods
family_Pet_name: Property = Property(name="name", type=StringType)
family_Pet.attributes={family_Pet_name}

# Relationships
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="family_Family", type=family_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Model", type=family_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members1: BinaryAssociation = BinaryAssociation(
    name="members1",
    ends={
        Property(name="family_Person", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family2", type=family_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pets3: BinaryAssociation = BinaryAssociation(
    name="pets3",
    ends={
        Property(name="family_Pet", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family4", type=family_Pet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="Person", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=family_Person, multiplicity=Multiplicity(0, 9999))
    }
)
partner8: BinaryAssociation = BinaryAssociation(
    name="partner8",
    ends={
        Property(name="family_Person9", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Person7", type=family_Person, multiplicity=Multiplicity(0, 1))
    }
)
parents11: BinaryAssociation = BinaryAssociation(
    name="parents11",
    ends={
        Property(name="Person12", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=family_Person, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_Model, family_Family, family_Person, family_Pet},
    associations={families0, members1, pets3, children6, partner8, parents11},
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