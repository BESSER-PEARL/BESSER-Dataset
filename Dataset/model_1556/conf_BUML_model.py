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
conf_System = Class(name="conf::System")
conf_Admin = Class(name="conf::Admin")
conf_Laboratory = Class(name="conf::Laboratory")
conf_Conference = Class(name="conf::Conference")
conf_RevisionProcess = Class(name="conf::RevisionProcess")
conf_Session = Class(name="conf::Session")
conf_Location = Class(name="conf::Location")
conf_ProgramComitee = Class(name="conf::ProgramComitee")
conf_SteeringComitee = Class(name="conf::SteeringComitee")
conf_Contribution = Class(name="conf::Contribution")
conf_Researcher = Class(name="conf::Researcher")
conf_Publication = Class(name="conf::Publication")
Person = Class(name="Person")
conf_Evaluation = Class(name="conf::Evaluation")
conf_Chapter = Class(name="conf::Chapter")
conf_RevisionNote = Class(name="conf::RevisionNote")
conf_Person = Class(name="conf::Person")

# conf_System class attributes and methods

# conf_Admin class attributes and methods

# conf_Laboratory class attributes and methods

# conf_Conference class attributes and methods

# conf_RevisionProcess class attributes and methods

# conf_Session class attributes and methods
conf_Session_year: Property = Property(name="year", type=StringType)
conf_Session.attributes={conf_Session_year}

# conf_Location class attributes and methods
conf_Location_name: Property = Property(name="name", type=StringType)
conf_Location.attributes={conf_Location_name}

# conf_ProgramComitee class attributes and methods

# conf_SteeringComitee class attributes and methods

# conf_Contribution class attributes and methods

# conf_Researcher class attributes and methods

# conf_Publication class attributes and methods

# Person class attributes and methods

# conf_Evaluation class attributes and methods

# conf_Chapter class attributes and methods

# conf_RevisionNote class attributes and methods

# conf_Person class attributes and methods

# Relationships
admin0: BinaryAssociation = BinaryAssociation(
    name="admin0",
    ends={
        Property(name="conf_Admin", type=conf_System, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_System", type=conf_Admin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
laboratories1: BinaryAssociation = BinaryAssociation(
    name="laboratories1",
    ends={
        Property(name="conf_Laboratory", type=conf_System, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_System2", type=conf_Laboratory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conferences3: BinaryAssociation = BinaryAssociation(
    name="conferences3",
    ends={
        Property(name="conf_Conference", type=conf_System, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_System4", type=conf_Conference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
revisionProcess5: BinaryAssociation = BinaryAssociation(
    name="revisionProcess5",
    ends={
        Property(name="conf_RevisionProcess", type=conf_System, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_System6", type=conf_RevisionProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location7: BinaryAssociation = BinaryAssociation(
    name="location7",
    ends={
        Property(name="conf_Location", type=conf_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Session", type=conf_Location, multiplicity=Multiplicity(0, 1))
    }
)
progcomit8: BinaryAssociation = BinaryAssociation(
    name="progcomit8",
    ends={
        Property(name="conf_ProgramComitee", type=conf_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Session9", type=conf_ProgramComitee, multiplicity=Multiplicity(0, 1))
    }
)
steercomit10: BinaryAssociation = BinaryAssociation(
    name="steercomit10",
    ends={
        Property(name="conf_SteeringComitee", type=conf_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Session11", type=conf_SteeringComitee, multiplicity=Multiplicity(0, 1))
    }
)
contributions12: BinaryAssociation = BinaryAssociation(
    name="contributions12",
    ends={
        Property(name="conf_Contribution", type=conf_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Session13", type=conf_Contribution, multiplicity=Multiplicity(0, 1))
    }
)
locations14: BinaryAssociation = BinaryAssociation(
    name="locations14",
    ends={
        Property(name="conf_Location16", type=conf_Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Admin15", type=conf_Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sessions17: BinaryAssociation = BinaryAssociation(
    name="sessions17",
    ends={
        Property(name="conf_Session19", type=conf_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Conference18", type=conf_Session, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
researchers20: BinaryAssociation = BinaryAssociation(
    name="researchers20",
    ends={
        Property(name="conf_Researcher", type=conf_Laboratory, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Laboratory21", type=conf_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publications22: BinaryAssociation = BinaryAssociation(
    name="publications22",
    ends={
        Property(name="conf_Publication", type=conf_Laboratory, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Laboratory23", type=conf_Publication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
evaluations24: BinaryAssociation = BinaryAssociation(
    name="evaluations24",
    ends={
        Property(name="conf_Evaluation", type=conf_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Researcher25", type=conf_Evaluation, multiplicity=Multiplicity(0, 1))
    }
)
writes26: BinaryAssociation = BinaryAssociation(
    name="writes26",
    ends={
        Property(name="conf_Chapter", type=conf_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Researcher27", type=conf_Chapter, multiplicity=Multiplicity(0, 1))
    }
)
reviews28: BinaryAssociation = BinaryAssociation(
    name="reviews28",
    ends={
        Property(name="conf_RevisionNote", type=conf_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Researcher29", type=conf_RevisionNote, multiplicity=Multiplicity(0, 1))
    }
)
chapters30: BinaryAssociation = BinaryAssociation(
    name="chapters30",
    ends={
        Property(name="conf_Chapter32", type=conf_Publication, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Publication31", type=conf_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
revisonNotes33: BinaryAssociation = BinaryAssociation(
    name="revisonNotes33",
    ends={
        Property(name="conf_RevisionNote35", type=conf_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Chapter34", type=conf_RevisionNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scPerson36: BinaryAssociation = BinaryAssociation(
    name="scPerson36",
    ends={
        Property(name="conf_Person", type=conf_SteeringComitee, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_SteeringComitee37", type=conf_Person, multiplicity=Multiplicity(0, 1))
    }
)
pcPerson38: BinaryAssociation = BinaryAssociation(
    name="pcPerson38",
    ends={
        Property(name="conf_Person40", type=conf_ProgramComitee, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_ProgramComitee39", type=conf_Person, multiplicity=Multiplicity(0, 1))
    }
)
publication41: BinaryAssociation = BinaryAssociation(
    name="publication41",
    ends={
        Property(name="conf_Publication43", type=conf_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Contribution42", type=conf_Publication, multiplicity=Multiplicity(0, 1))
    }
)
evPubli44: BinaryAssociation = BinaryAssociation(
    name="evPubli44",
    ends={
        Property(name="conf_Publication46", type=conf_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="conf_Evaluation45", type=conf_Publication, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_conf_Researcher_Person = Generalization(general=Person, specific=conf_Researcher)

# Domain Model
domain_model = DomainModel(
    name="conf",
    types={conf_System, conf_Admin, conf_Laboratory, conf_Conference, conf_RevisionProcess, conf_Session, conf_Location, conf_ProgramComitee, conf_SteeringComitee, conf_Contribution, conf_Researcher, conf_Publication, Person, conf_Evaluation, conf_Chapter, conf_RevisionNote, conf_Person},
    associations={admin0, laboratories1, conferences3, revisionProcess5, location7, progcomit8, steercomit10, contributions12, locations14, sessions17, researchers20, publications22, evaluations24, writes26, reviews28, chapters30, revisonNotes33, scPerson36, pcPerson38, publication41, evPubli44},
    generalizations={gen_conf_Researcher_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)