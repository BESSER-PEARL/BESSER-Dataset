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
Attitude: Enumeration = Enumeration(
    name="Attitude",
    literals={
            EnumerationLiteral(name="serious"),
			EnumerationLiteral(name="cool"),
			EnumerationLiteral(name="disgraceful")
    }
)

# Classes
conference_Conference = Class(name="conference_Conference")
conference_Track = Class(name="conference_Track")
conference_Person = Class(name="conference_Person")
conference_Day = Class(name="conference_Day")
conference_Location = Class(name="conference_Location")
conference_Talk = Class(name="conference_Talk")
Story = Class(name="Story")
conference_makingOf_Day = Class(name="conference_makingOf_Day")
Task = Class(name="Task")
conference_Subject = Class(name="conference_Subject")
conference_makingOf_Story = Class(name="conference_makingOf_Story")
Day = Class(name="Day")
conference_makingOf_Task = Class(name="conference_makingOf_Task")
conference_makingOf_Participant = Class(name="conference_makingOf_Participant")
makingOf_conference_Person = Class(name="makingOf_conference_Person")
Participant = Class(name="Participant")

# conference_Conference class attributes and methods
conference_Conference_name: Property = Property(name="name", type=StringType)
conference_Conference.attributes={conference_Conference_name}

# conference_Track class attributes and methods
conference_Track_name: Property = Property(name="name", type=StringType)
conference_Track.attributes={conference_Track_name}

# conference_Person class attributes and methods
conference_Person_name: Property = Property(name="name", type=StringType)
conference_Person_organisation: Property = Property(name="organisation", type=StringType)
conference_Person.attributes={conference_Person_organisation, conference_Person_name}

# conference_Day class attributes and methods
conference_Day_name: Property = Property(name="name", type=StringType)
conference_Day.attributes={conference_Day_name}

# conference_Location class attributes and methods
conference_Location_name: Property = Property(name="name", type=StringType)
conference_Location.attributes={conference_Location_name}

# conference_Talk class attributes and methods
conference_Talk_time: Property = Property(name="time", type=StringType)
conference_Talk_name: Property = Property(name="name", type=StringType)
conference_Talk_abstract: Property = Property(name="abstract", type=StringType)
conference_Talk_duration: Property = Property(name="duration", type=IntegerType)
conference_Talk.attributes={conference_Talk_abstract, conference_Talk_name, conference_Talk_duration, conference_Talk_time}

# Story class attributes and methods

# conference_makingOf_Day class attributes and methods
conference_makingOf_Day_name: Property = Property(name="name", type=StringType)
conference_makingOf_Day.attributes={conference_makingOf_Day_name}

# Task class attributes and methods

# conference_Subject class attributes and methods
conference_Subject_description: Property = Property(name="description", type=StringType)
conference_Subject_isDone: Property = Property(name="isDone", type=BooleanType)
conference_Subject.attributes={conference_Subject_description, conference_Subject_isDone}

# conference_makingOf_Story class attributes and methods
conference_makingOf_Story_name: Property = Property(name="name", type=StringType)
conference_makingOf_Story.attributes={conference_makingOf_Story_name}

# Day class attributes and methods

# conference_makingOf_Task class attributes and methods
conference_makingOf_Task_name: Property = Property(name="name", type=StringType)
conference_makingOf_Task.attributes={conference_makingOf_Task_name}

# conference_makingOf_Participant class attributes and methods
conference_makingOf_Participant_age: Property = Property(name="age", type=IntegerType)
conference_makingOf_Participant_attitude: Property = Property(name="attitude", type=StringType)
conference_makingOf_Participant.attributes={conference_makingOf_Participant_age, conference_makingOf_Participant_attitude}

# makingOf_conference_Person class attributes and methods

# Participant class attributes and methods

# Relationships
tracks0: BinaryAssociation = BinaryAssociation(
    name="tracks0",
    ends={
        Property(name="conference_Track", type=conference_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Conference", type=conference_Track, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
speakers1: BinaryAssociation = BinaryAssociation(
    name="speakers1",
    ends={
        Property(name="conference_Person", type=conference_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Conference2", type=conference_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
days3: BinaryAssociation = BinaryAssociation(
    name="days3",
    ends={
        Property(name="conference_Day", type=conference_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Conference4", type=conference_Day, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locations5: BinaryAssociation = BinaryAssociation(
    name="locations5",
    ends={
        Property(name="conference_Location", type=conference_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Conference6", type=conference_Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
speakers7: BinaryAssociation = BinaryAssociation(
    name="speakers7",
    ends={
        Property(name="Person", type=conference_Talk, multiplicity=Multiplicity(1, 1)),
        Property(name="talks", type=conference_Person, multiplicity=Multiplicity(0, 9999))
    }
)
subjects8: BinaryAssociation = BinaryAssociation(
    name="subjects8",
    ends={
        Property(name="conference_Subject", type=conference_Talk, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Talk", type=conference_Subject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
makingOfStories9: BinaryAssociation = BinaryAssociation(
    name="makingOfStories9",
    ends={
        Property(name="Story", type=conference_Talk, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Talk10", type=Story, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
day11: BinaryAssociation = BinaryAssociation(
    name="day11",
    ends={
        Property(name="Day", type=conference_Talk, multiplicity=Multiplicity(1, 1)),
        Property(name="talks12", type=conference_Day, multiplicity=Multiplicity(0, 1))
    }
)
location13: BinaryAssociation = BinaryAssociation(
    name="location13",
    ends={
        Property(name="Location", type=conference_Talk, multiplicity=Multiplicity(1, 1)),
        Property(name="talks14", type=conference_Location, multiplicity=Multiplicity(0, 1))
    }
)
talks15: BinaryAssociation = BinaryAssociation(
    name="talks15",
    ends={
        Property(name="Talk", type=conference_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="speakers", type=conference_Talk, multiplicity=Multiplicity(0, 9999))
    }
)
tracks16: BinaryAssociation = BinaryAssociation(
    name="tracks16",
    ends={
        Property(name="Track", type=conference_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="animators", type=conference_Track, multiplicity=Multiplicity(0, 9999))
    }
)
talks17: BinaryAssociation = BinaryAssociation(
    name="talks17",
    ends={
        Property(name="conference_Talk19", type=conference_Track, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Track18", type=conference_Talk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
animators20: BinaryAssociation = BinaryAssociation(
    name="animators20",
    ends={
        Property(name="Person21", type=conference_Track, multiplicity=Multiplicity(1, 1)),
        Property(name="tracks", type=conference_Person, multiplicity=Multiplicity(0, 9999))
    }
)
talks22: BinaryAssociation = BinaryAssociation(
    name="talks22",
    ends={
        Property(name="Talk23", type=conference_Day, multiplicity=Multiplicity(1, 1)),
        Property(name="day", type=conference_Talk, multiplicity=Multiplicity(0, 9999))
    }
)
talks24: BinaryAssociation = BinaryAssociation(
    name="talks24",
    ends={
        Property(name="Talk25", type=conference_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=conference_Talk, multiplicity=Multiplicity(0, 9999))
    }
)
tasks26: BinaryAssociation = BinaryAssociation(
    name="tasks26",
    ends={
        Property(name="Task", type=conference_makingOf_Day, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_makingOf_Day", type=Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participants30: BinaryAssociation = BinaryAssociation(
    name="participants30",
    ends={
        Property(name="conference_makingOf_Day31", type=Participant, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Participant", type=conference_makingOf_Day, multiplicity=Multiplicity(1, 1))
    }
)
days32: BinaryAssociation = BinaryAssociation(
    name="days32",
    ends={
        Property(name="Day33", type=conference_makingOf_Story, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_makingOf_Story", type=Day, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isInvolved34: BinaryAssociation = BinaryAssociation(
    name="isInvolved34",
    ends={
        Property(name="Participant35", type=conference_makingOf_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_makingOf_Task", type=Participant, multiplicity=Multiplicity(0, 9999))
    }
)
person36: BinaryAssociation = BinaryAssociation(
    name="person36",
    ends={
        Property(name="makingOf_conference_Person", type=conference_makingOf_Participant, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_makingOf_Participant", type=makingOf_conference_Person, multiplicity=Multiplicity(0, 1))
    }
)
ideas27: BinaryAssociation = BinaryAssociation(
    name="ideas27",
    ends={
        Property(name="Task29", type=conference_makingOf_Day, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_makingOf_Day28", type=Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="conference",
    types={conference_Conference, conference_Track, conference_Person, conference_Day, conference_Location, conference_Talk, Story, conference_makingOf_Day, Task, conference_Subject, conference_makingOf_Story, Day, conference_makingOf_Task, conference_makingOf_Participant, makingOf_conference_Person, Participant, Attitude},
    associations={tracks0, speakers1, days3, locations5, speakers7, subjects8, makingOfStories9, day11, location13, talks15, tracks16, talks17, animators20, talks22, talks24, tasks26, participants30, days32, isInvolved34, person36, ideas27},
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