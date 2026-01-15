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
Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female"),
			EnumerationLiteral(name="unknown")
    }
)

TeamPersonKind: Enumeration = Enumeration(
    name="TeamPersonKind",
    literals={
            EnumerationLiteral(name="captain"),
			EnumerationLiteral(name="member")
    }
)

# Classes
grudi_Person = Class(name="grudi::Person")
grudi_Team = Class(name="grudi::Team")
grudi_TeamLine = Class(name="grudi::TeamLine")
grudi_PersonInfo = Class(name="grudi::PersonInfo")

# grudi_Person class attributes and methods
grudi_Person_id: Property = Property(name="id", type=StringType)
grudi_Person_username: Property = Property(name="username", type=StringType)
grudi_Person_email: Property = Property(name="email", type=StringType)
grudi_Person_password: Property = Property(name="password", type=StringType)
grudi_Person_name: Property = Property(name="name", type=StringType)
grudi_Person_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
grudi_Person_gender: Property = Property(name="gender", type=StringType)
grudi_Person_address: Property = Property(name="address", type=StringType)
grudi_Person_versionNumber: Property = Property(name="versionNumber", type=StringType)
grudi_Person.attributes={grudi_Person_gender, grudi_Person_versionNumber, grudi_Person_password, grudi_Person_phoneNumber, grudi_Person_name, grudi_Person_email, grudi_Person_username, grudi_Person_address, grudi_Person_id}

# grudi_Team class attributes and methods
grudi_Team_versionNumber: Property = Property(name="versionNumber", type=StringType)
grudi_Team_id: Property = Property(name="id", type=StringType)
grudi_Team_name: Property = Property(name="name", type=StringType)
grudi_Team.attributes={grudi_Team_versionNumber, grudi_Team_name, grudi_Team_id}

# grudi_TeamLine class attributes and methods
grudi_TeamLine_id: Property = Property(name="id", type=StringType)
grudi_TeamLine_kind: Property = Property(name="kind", type=StringType)
grudi_TeamLine_versionNumber: Property = Property(name="versionNumber", type=StringType)
grudi_TeamLine.attributes={grudi_TeamLine_kind, grudi_TeamLine_id, grudi_TeamLine_versionNumber}

# grudi_PersonInfo class attributes and methods
grudi_PersonInfo_gender: Property = Property(name="gender", type=StringType)
grudi_PersonInfo_id: Property = Property(name="id", type=StringType)
grudi_PersonInfo_userName: Property = Property(name="userName", type=StringType)
grudi_PersonInfo_name: Property = Property(name="name", type=StringType)
grudi_PersonInfo_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
grudi_PersonInfo.attributes={grudi_PersonInfo_gender, grudi_PersonInfo_id, grudi_PersonInfo_userName, grudi_PersonInfo_phoneNumber, grudi_PersonInfo_name}

# Relationships
lines0: BinaryAssociation = BinaryAssociation(
    name="lines0",
    ends={
        Property(name="TeamLine", type=grudi_Team, multiplicity=Multiplicity(1, 1)),
        Property(name="team", type=grudi_TeamLine, multiplicity=Multiplicity(0, 9999))
    }
)
team1: BinaryAssociation = BinaryAssociation(
    name="team1",
    ends={
        Property(name="Team", type=grudi_TeamLine, multiplicity=Multiplicity(1, 1)),
        Property(name="lines", type=grudi_Team, multiplicity=Multiplicity(0, 1))
    }
)
person2: BinaryAssociation = BinaryAssociation(
    name="person2",
    ends={
        Property(name="grudi_PersonInfo", type=grudi_TeamLine, multiplicity=Multiplicity(1, 1)),
        Property(name="grudi_TeamLine", type=grudi_PersonInfo, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="grudi",
    types={grudi_Person, grudi_Team, grudi_TeamLine, grudi_PersonInfo, Gender, TeamPersonKind},
    associations={lines0, team1, person2},
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