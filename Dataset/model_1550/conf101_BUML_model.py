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
conf101_System = Class(name="conf101::System")
NamedElement = Class(name="NamedElement")
conf101_Admin = Class(name="conf101::Admin")
conf101_Laboratory = Class(name="conf101::Laboratory")
conf101_Conference = Class(name="conf101::Conference")
conf101_RevisionProcess = Class(name="conf101::RevisionProcess")
conf101_Session = Class(name="conf101::Session")
conf101_Location = Class(name="conf101::Location")
conf101_ProgramComitee = Class(name="conf101::ProgramComitee")
conf101_SteeringComitee = Class(name="conf101::SteeringComitee")
conf101_Contribution = Class(name="conf101::Contribution")
conf101_Researcher = Class(name="conf101::Researcher")
conf101_Publication = Class(name="conf101::Publication")
Person = Class(name="Person")
conf101_Evaluation = Class(name="conf101::Evaluation")
conf101_Chapter = Class(name="conf101::Chapter")
conf101_RevisionNote = Class(name="conf101::RevisionNote")
conf101_Person = Class(name="conf101::Person")
conf101_NamedElement = Class(name="conf101::NamedElement")

# conf101_System class attributes and methods

# NamedElement class attributes and methods

# conf101_Admin class attributes and methods

# conf101_Laboratory class attributes and methods

# conf101_Conference class attributes and methods

# conf101_RevisionProcess class attributes and methods

# conf101_Session class attributes and methods
conf101_Session_year: Property = Property(name="year", type=StringType)
conf101_Session.attributes={conf101_Session_year}

# conf101_Location class attributes and methods

# conf101_ProgramComitee class attributes and methods

# conf101_SteeringComitee class attributes and methods

# conf101_Contribution class attributes and methods

# conf101_Researcher class attributes and methods

# conf101_Publication class attributes and methods

# Person class attributes and methods

# conf101_Evaluation class attributes and methods

# conf101_Chapter class attributes and methods

# conf101_RevisionNote class attributes and methods

# conf101_Person class attributes and methods

# conf101_NamedElement class attributes and methods
conf101_NamedElement_name: Property = Property(name="name", type=StringType)
conf101_NamedElement.attributes={conf101_NamedElement_name}

# Relationships
laboratories1: BinaryAssociation = BinaryAssociation(
    name="laboratories1",
    ends={
        Property(name="conf101_Laboratory", type=conf101_System, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_System2", type=conf101_Laboratory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
admin0: BinaryAssociation = BinaryAssociation(
    name="admin0",
    ends={
        Property(name="conf101_Admin", type=conf101_System, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_System", type=conf101_Admin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sessions17: BinaryAssociation = BinaryAssociation(
    name="sessions17",
    ends={
        Property(name="conf101_Session19", type=conf101_Conference, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Conference18", type=conf101_Session, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conferences3: BinaryAssociation = BinaryAssociation(
    name="conferences3",
    ends={
        Property(name="conf101_Conference", type=conf101_System, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_System4", type=conf101_Conference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
revisionProcess5: BinaryAssociation = BinaryAssociation(
    name="revisionProcess5",
    ends={
        Property(name="conf101_RevisionProcess", type=conf101_System, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_System6", type=conf101_RevisionProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location7: BinaryAssociation = BinaryAssociation(
    name="location7",
    ends={
        Property(name="conf101_Location", type=conf101_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Session", type=conf101_Location, multiplicity=Multiplicity(0, 1))
    }
)
progcomit8: BinaryAssociation = BinaryAssociation(
    name="progcomit8",
    ends={
        Property(name="conf101_ProgramComitee", type=conf101_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Session9", type=conf101_ProgramComitee, multiplicity=Multiplicity(0, 1))
    }
)
steercomit10: BinaryAssociation = BinaryAssociation(
    name="steercomit10",
    ends={
        Property(name="conf101_SteeringComitee", type=conf101_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Session11", type=conf101_SteeringComitee, multiplicity=Multiplicity(0, 1))
    }
)
contributions12: BinaryAssociation = BinaryAssociation(
    name="contributions12",
    ends={
        Property(name="conf101_Contribution", type=conf101_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Session13", type=conf101_Contribution, multiplicity=Multiplicity(0, 1))
    }
)
locations14: BinaryAssociation = BinaryAssociation(
    name="locations14",
    ends={
        Property(name="conf101_Location16", type=conf101_Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Admin15", type=conf101_Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
researchers20: BinaryAssociation = BinaryAssociation(
    name="researchers20",
    ends={
        Property(name="conf101_Researcher", type=conf101_Laboratory, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Laboratory21", type=conf101_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publications22: BinaryAssociation = BinaryAssociation(
    name="publications22",
    ends={
        Property(name="conf101_Publication", type=conf101_Laboratory, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Laboratory23", type=conf101_Publication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
evaluations24: BinaryAssociation = BinaryAssociation(
    name="evaluations24",
    ends={
        Property(name="conf101_Evaluation", type=conf101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Researcher25", type=conf101_Evaluation, multiplicity=Multiplicity(0, 1))
    }
)
writes26: BinaryAssociation = BinaryAssociation(
    name="writes26",
    ends={
        Property(name="conf101_Chapter", type=conf101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Researcher27", type=conf101_Chapter, multiplicity=Multiplicity(0, 1))
    }
)
reviews28: BinaryAssociation = BinaryAssociation(
    name="reviews28",
    ends={
        Property(name="conf101_RevisionNote", type=conf101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Researcher29", type=conf101_RevisionNote, multiplicity=Multiplicity(0, 1))
    }
)
publications30: BinaryAssociation = BinaryAssociation(
    name="publications30",
    ends={
        Property(name="conf101_Publication32", type=conf101_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Researcher31", type=conf101_Publication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publication44: BinaryAssociation = BinaryAssociation(
    name="publication44",
    ends={
        Property(name="conf101_Publication46", type=conf101_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Contribution45", type=conf101_Publication, multiplicity=Multiplicity(0, 1))
    }
)
chapters33: BinaryAssociation = BinaryAssociation(
    name="chapters33",
    ends={
        Property(name="conf101_Chapter35", type=conf101_Publication, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Publication34", type=conf101_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
revisonNotes36: BinaryAssociation = BinaryAssociation(
    name="revisonNotes36",
    ends={
        Property(name="conf101_RevisionNote38", type=conf101_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Chapter37", type=conf101_RevisionNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scPerson39: BinaryAssociation = BinaryAssociation(
    name="scPerson39",
    ends={
        Property(name="conf101_Person", type=conf101_SteeringComitee, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_SteeringComitee40", type=conf101_Person, multiplicity=Multiplicity(0, 1))
    }
)
pcPerson41: BinaryAssociation = BinaryAssociation(
    name="pcPerson41",
    ends={
        Property(name="conf101_Person43", type=conf101_ProgramComitee, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_ProgramComitee42", type=conf101_Person, multiplicity=Multiplicity(0, 1))
    }
)
evPubli47: BinaryAssociation = BinaryAssociation(
    name="evPubli47",
    ends={
        Property(name="conf101_Publication49", type=conf101_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="conf101_Evaluation48", type=conf101_Publication, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_conf101_System_NamedElement = Generalization(general=NamedElement, specific=conf101_System)
gen_conf101_Session_NamedElement = Generalization(general=NamedElement, specific=conf101_Session)
gen_conf101_Location_NamedElement = Generalization(general=NamedElement, specific=conf101_Location)
gen_conf101_Admin_NamedElement = Generalization(general=NamedElement, specific=conf101_Admin)
gen_conf101_Conference_NamedElement = Generalization(general=NamedElement, specific=conf101_Conference)
gen_conf101_Publication_NamedElement = Generalization(general=NamedElement, specific=conf101_Publication)
gen_conf101_Laboratory_NamedElement = Generalization(general=NamedElement, specific=conf101_Laboratory)
gen_conf101_Researcher_Person = Generalization(general=Person, specific=conf101_Researcher)
gen_conf101_Contribution_NamedElement = Generalization(general=NamedElement, specific=conf101_Contribution)
gen_conf101_Person_NamedElement = Generalization(general=NamedElement, specific=conf101_Person)
gen_conf101_Chapter_NamedElement = Generalization(general=NamedElement, specific=conf101_Chapter)
gen_conf101_SteeringComitee_NamedElement = Generalization(general=NamedElement, specific=conf101_SteeringComitee)
gen_conf101_ProgramComitee_NamedElement = Generalization(general=NamedElement, specific=conf101_ProgramComitee)
gen_conf101_Evaluation_NamedElement = Generalization(general=NamedElement, specific=conf101_Evaluation)

# Domain Model
domain_model = DomainModel(
    name="conf101",
    types={conf101_System, NamedElement, conf101_Admin, conf101_Laboratory, conf101_Conference, conf101_RevisionProcess, conf101_Session, conf101_Location, conf101_ProgramComitee, conf101_SteeringComitee, conf101_Contribution, conf101_Researcher, conf101_Publication, Person, conf101_Evaluation, conf101_Chapter, conf101_RevisionNote, conf101_Person, conf101_NamedElement},
    associations={laboratories1, admin0, sessions17, conferences3, revisionProcess5, location7, progcomit8, steercomit10, contributions12, locations14, researchers20, publications22, evaluations24, writes26, reviews28, publications30, publication44, chapters33, revisonNotes36, scPerson39, pcPerson41, evPubli47},
    generalizations={gen_conf101_System_NamedElement, gen_conf101_Session_NamedElement, gen_conf101_Location_NamedElement, gen_conf101_Admin_NamedElement, gen_conf101_Conference_NamedElement, gen_conf101_Publication_NamedElement, gen_conf101_Laboratory_NamedElement, gen_conf101_Researcher_Person, gen_conf101_Contribution_NamedElement, gen_conf101_Person_NamedElement, gen_conf101_Chapter_NamedElement, gen_conf101_SteeringComitee_NamedElement, gen_conf101_ProgramComitee_NamedElement, gen_conf101_Evaluation_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)