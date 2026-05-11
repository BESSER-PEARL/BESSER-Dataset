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
training_Session = Class(name="training_Session")
training_Person = Class(name="training_Person", is_abstract=True)
training_TrainingOrganization = Class(name="training_TrainingOrganization")
training_Training = Class(name="training_Training")
training_Trainer = Class(name="training_Trainer")
Person = Class(name="Person")
training_Trainee = Class(name="training_Trainee")

# training_Session class attributes and methods
training_Session_name: Property = Property(name="name", type=StringType)
training_Session_date: Property = Property(name="date", type=DateType)
training_Session.attributes={training_Session_name, training_Session_date}

# training_Person class attributes and methods
training_Person_firstname: Property = Property(name="firstname", type=StringType)
training_Person_lastname: Property = Property(name="lastname", type=StringType)
training_Person.attributes={training_Person_firstname, training_Person_lastname}

# training_TrainingOrganization class attributes and methods
training_TrainingOrganization_name: Property = Property(name="name", type=StringType)
training_TrainingOrganization.attributes={training_TrainingOrganization_name}

# training_Training class attributes and methods
training_Training_title: Property = Property(name="title", type=StringType)
training_Training.attributes={training_Training_title}

# training_Trainer class attributes and methods

# Person class attributes and methods

# training_Trainee class attributes and methods

# Relationships
trainer1: BinaryAssociation = BinaryAssociation(
    name="trainer1",
    ends={
        Property(name="training_Trainer", type=training_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="training_Session", type=training_Trainer, multiplicity=Multiplicity(1, 1))
    }
)
Trainees2: BinaryAssociation = BinaryAssociation(
    name="Trainees2",
    ends={
        Property(name="training_Person", type=training_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="training_Session3", type=training_Person, multiplicity=Multiplicity(1, 9999))
    }
)
training0: BinaryAssociation = BinaryAssociation(
    name="training0",
    ends={
        Property(name="Training", type=training_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="session", type=training_Training, multiplicity=Multiplicity(1, 1))
    }
)
canBeProvidedBy11: BinaryAssociation = BinaryAssociation(
    name="canBeProvidedBy11",
    ends={
        Property(name="Trainer", type=training_Training, multiplicity=Multiplicity(1, 1)),
        Property(name="canProvide", type=training_Trainer, multiplicity=Multiplicity(1, 9999))
    }
)
session12: BinaryAssociation = BinaryAssociation(
    name="session12",
    ends={
        Property(name="Session", type=training_Training, multiplicity=Multiplicity(1, 1)),
        Property(name="training", type=training_Session, multiplicity=Multiplicity(0, 1))
    }
)
canProvide13: BinaryAssociation = BinaryAssociation(
    name="canProvide13",
    ends={
        Property(name="Training14", type=training_Trainer, multiplicity=Multiplicity(1, 1)),
        Property(name="canBeProvidedBy", type=training_Training, multiplicity=Multiplicity(1, 9999))
    }
)
people4: BinaryAssociation = BinaryAssociation(
    name="people4",
    ends={
        Property(name="training_Person5", type=training_TrainingOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="training_TrainingOrganization", type=training_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sessions6: BinaryAssociation = BinaryAssociation(
    name="sessions6",
    ends={
        Property(name="training_Session8", type=training_TrainingOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="training_TrainingOrganization7", type=training_Session, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
training9: BinaryAssociation = BinaryAssociation(
    name="training9",
    ends={
        Property(name="training_Training", type=training_TrainingOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="training_TrainingOrganization10", type=training_Training, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_training_Trainer_Person = Generalization(general=Person, specific=training_Trainer)
gen_training_Trainee_Person = Generalization(general=Person, specific=training_Trainee)

# Domain Model
domain_model = DomainModel(
    name="training",
    types={training_Session, training_Person, training_TrainingOrganization, training_Training, training_Trainer, Person, training_Trainee},
    associations={trainer1, Trainees2, training0, canBeProvidedBy11, session12, canProvide13, people4, sessions6, training9},
    generalizations={gen_training_Trainer_Person, gen_training_Trainee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)