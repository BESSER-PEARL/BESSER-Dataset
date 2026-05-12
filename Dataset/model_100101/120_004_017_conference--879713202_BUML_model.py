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
TALK_TYPE: Enumeration = Enumeration(
    name="TALK_TYPE",
    literals={
            EnumerationLiteral(name="WORKSHOP"),
			EnumerationLiteral(name="DEMONSTRATION"),
			EnumerationLiteral(name="CONFERENCE")
    }
)

GENDER: Enumeration = Enumeration(
    name="GENDER",
    literals={
            EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="MALE"),
			EnumerationLiteral(name="FEMALE")
    }
)

# Classes
conference_Talk = Class(name="conference_Talk")
conference_Topic = Class(name="conference_Topic")
conference_Site = Class(name="conference_Site")
conference_Conference = Class(name="conference_Conference")
conference_Person = Class(name="conference_Person")
conference_Room = Class(name="conference_Room")

# conference_Talk class attributes and methods
conference_Talk_title: Property = Property(name="title", type=StringType)
conference_Talk_type: Property = Property(name="type", type=StringType)
conference_Talk_documentation: Property = Property(name="documentation", type=StringType)
conference_Talk.attributes={conference_Talk_type, conference_Talk_title, conference_Talk_documentation}

# conference_Topic class attributes and methods
conference_Topic_description: Property = Property(name="description", type=StringType)
conference_Topic_references: Property = Property(name="references", type=StringType)
conference_Topic_documentation: Property = Property(name="documentation", type=StringType)
conference_Topic.attributes={conference_Topic_description, conference_Topic_references, conference_Topic_documentation}

# conference_Site class attributes and methods
conference_Site_documentation: Property = Property(name="documentation", type=StringType)
conference_Site_name: Property = Property(name="name", type=StringType)
conference_Site.attributes={conference_Site_name, conference_Site_documentation}

# conference_Conference class attributes and methods
conference_Conference_name: Property = Property(name="name", type=StringType)
conference_Conference_overview: Property = Property(name="overview", type=StringType)
conference_Conference_place: Property = Property(name="place", type=StringType)
conference_Conference.attributes={conference_Conference_place, conference_Conference_name, conference_Conference_overview}

# conference_Person class attributes and methods
conference_Person_firstname: Property = Property(name="firstname", type=StringType)
conference_Person_lastname: Property = Property(name="lastname", type=StringType)
conference_Person_age: Property = Property(name="age", type=IntegerType)
conference_Person_eclipseCommiter: Property = Property(name="eclipseCommiter", type=BooleanType)
conference_Person_gender: Property = Property(name="gender", type=StringType)
conference_Person_isRegistered: Property = Property(name="isRegistered", type=BooleanType)
conference_Person.attributes={conference_Person_lastname, conference_Person_eclipseCommiter, conference_Person_isRegistered, conference_Person_firstname, conference_Person_age, conference_Person_gender}

# conference_Room class attributes and methods
conference_Room_name: Property = Property(name="name", type=StringType)
conference_Room_capacity: Property = Property(name="capacity", type=IntegerType)
conference_Room.attributes={conference_Room_name, conference_Room_capacity}

# Relationships
talks1: BinaryAssociation = BinaryAssociation(
    name="talks1",
    ends={
        Property(name="conference_Talk", type=conference_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Conference2", type=conference_Talk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topics3: BinaryAssociation = BinaryAssociation(
    name="topics3",
    ends={
        Property(name="conference_Topic", type=conference_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Conference4", type=conference_Topic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sites5: BinaryAssociation = BinaryAssociation(
    name="sites5",
    ends={
        Property(name="conference_Site", type=conference_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Conference6", type=conference_Site, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participants0: BinaryAssociation = BinaryAssociation(
    name="participants0",
    ends={
        Property(name="conference_Person", type=conference_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Conference", type=conference_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rooms19: BinaryAssociation = BinaryAssociation(
    name="rooms19",
    ends={
        Property(name="conference_Room", type=conference_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Site20", type=conference_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assists7: BinaryAssociation = BinaryAssociation(
    name="assists7",
    ends={
        Property(name="conference_Talk9", type=conference_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Person8", type=conference_Talk, multiplicity=Multiplicity(0, 9999))
    }
)
topic10: BinaryAssociation = BinaryAssociation(
    name="topic10",
    ends={
        Property(name="conference_Topic12", type=conference_Talk, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Talk11", type=conference_Topic, multiplicity=Multiplicity(1, 1))
    }
)
presenter13: BinaryAssociation = BinaryAssociation(
    name="presenter13",
    ends={
        Property(name="conference_Person15", type=conference_Talk, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Talk14", type=conference_Person, multiplicity=Multiplicity(1, 1))
    }
)
creator16: BinaryAssociation = BinaryAssociation(
    name="creator16",
    ends={
        Property(name="conference_Person18", type=conference_Talk, multiplicity=Multiplicity(1, 1)),
        Property(name="conference_Talk17", type=conference_Person, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="conference",
    types={conference_Talk, conference_Topic, conference_Site, conference_Conference, conference_Person, conference_Room, TALK_TYPE, GENDER},
    associations={talks1, topics3, sites5, participants0, rooms19, assists7, topic10, presenter13, creator16},
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