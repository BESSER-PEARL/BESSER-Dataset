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
model_PersonList = Class(name="model::PersonList")
model_Root = Class(name="model::Root")
model_Person = Class(name="model::Person")

# model_PersonList class attributes and methods

# model_Root class attributes and methods

# model_Person class attributes and methods
model_Person_firstName: Property = Property(name="firstName", type=StringType)
model_Person.attributes={model_Person_firstName}

# Relationships
person0: BinaryAssociation = BinaryAssociation(
    name="person0",
    ends={
        Property(name="model_Person", type=model_PersonList, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PersonList", type=model_Person, multiplicity=Multiplicity(1, 1))
    }
)
persons1: BinaryAssociation = BinaryAssociation(
    name="persons1",
    ends={
        Property(name="model_Person2", type=model_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Root", type=model_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
personList3: BinaryAssociation = BinaryAssociation(
    name="personList3",
    ends={
        Property(name="model_PersonList5", type=model_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Root4", type=model_PersonList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_PersonList, model_Root, model_Person},
    associations={person0, persons1, personList3},
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