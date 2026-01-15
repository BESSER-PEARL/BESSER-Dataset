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
timetrack_Library = Class(name="timetrack::Library")
timetrack_User = Class(name="timetrack::User")
timetrack_Project = Class(name="timetrack::Project")
timetrack_TimeEntry = Class(name="timetrack::TimeEntry")

# timetrack_Library class attributes and methods

# timetrack_User class attributes and methods
timetrack_User_name: Property = Property(name="name", type=StringType)
timetrack_User_password: Property = Property(name="password", type=StringType)
timetrack_User_sap_name: Property = Property(name="sap_name", type=StringType)
timetrack_User_sap_password: Property = Property(name="sap_password", type=StringType)
timetrack_User.attributes={timetrack_User_name, timetrack_User_password, timetrack_User_sap_name, timetrack_User_sap_password}

# timetrack_Project class attributes and methods
timetrack_Project_number: Property = Property(name="number", type=StringType)
timetrack_Project_name: Property = Property(name="name", type=StringType)
timetrack_Project.attributes={timetrack_Project_name, timetrack_Project_number}

# timetrack_TimeEntry class attributes and methods
timetrack_TimeEntry_duration: Property = Property(name="duration", type=DateType)
timetrack_TimeEntry_factured: Property = Property(name="factured", type=BooleanType)
timetrack_TimeEntry_notes: Property = Property(name="notes", type=StringType)
timetrack_TimeEntry_sync_date: Property = Property(name="sync_date", type=DateType)
timetrack_TimeEntry_day: Property = Property(name="day", type=DateType)
timetrack_TimeEntry_from: Property = Property(name="from", type=DateType)
timetrack_TimeEntry_till: Property = Property(name="till", type=DateType)
timetrack_TimeEntry.attributes={timetrack_TimeEntry_from, timetrack_TimeEntry_till, timetrack_TimeEntry_duration, timetrack_TimeEntry_notes, timetrack_TimeEntry_day, timetrack_TimeEntry_factured, timetrack_TimeEntry_sync_date}

# Relationships
listBook3: BinaryAssociation = BinaryAssociation(
    name="listBook3",
    ends={
        Property(name="timetrack_User4", type=timetrack_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="timetrack_Library", type=timetrack_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listTimeEntry5: BinaryAssociation = BinaryAssociation(
    name="listTimeEntry5",
    ends={
        Property(name="timetrack_TimeEntry7", type=timetrack_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="timetrack_Library6", type=timetrack_TimeEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user0: BinaryAssociation = BinaryAssociation(
    name="user0",
    ends={
        Property(name="timetrack_User", type=timetrack_TimeEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="timetrack_TimeEntry", type=timetrack_User, multiplicity=Multiplicity(1, 1))
    }
)
project1: BinaryAssociation = BinaryAssociation(
    name="project1",
    ends={
        Property(name="timetrack_Project", type=timetrack_TimeEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="timetrack_TimeEntry2", type=timetrack_Project, multiplicity=Multiplicity(1, 1))
    }
)
listProject8: BinaryAssociation = BinaryAssociation(
    name="listProject8",
    ends={
        Property(name="timetrack_Project10", type=timetrack_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="timetrack_Library9", type=timetrack_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="timetrack",
    types={timetrack_Library, timetrack_User, timetrack_Project, timetrack_TimeEntry},
    associations={listBook3, listTimeEntry5, user0, project1, listProject8},
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