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
Nationality: Enumeration = Enumeration(
    name="Nationality",
    literals={
            EnumerationLiteral(name="French"),
			EnumerationLiteral(name="German"),
			EnumerationLiteral(name="Spanish"),
			EnumerationLiteral(name="English"),
			EnumerationLiteral(name="other")
    }
)

Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="Male"),
			EnumerationLiteral(name="Female")
    }
)

Subject: Enumeration = Enumeration(
    name="Subject",
    literals={
            EnumerationLiteral(name="CES"),
			EnumerationLiteral(name="BusinessEngineering"),
			EnumerationLiteral(name="ComputerScience"),
			EnumerationLiteral(name="MechanicalEngineering"),
			EnumerationLiteral(name="Physics"),
			EnumerationLiteral(name="Mathematics"),
			EnumerationLiteral(name="AppliedGeographics")
    }
)

OperatingSystem: Enumeration = Enumeration(
    name="OperatingSystem",
    literals={
            EnumerationLiteral(name="Windows"),
			EnumerationLiteral(name="Linux_Unix"),
			EnumerationLiteral(name="MacOS"),
			EnumerationLiteral(name="other")
    }
)

ProgrammingLanguage: Enumeration = Enumeration(
    name="ProgrammingLanguage",
    literals={
            EnumerationLiteral(name="other"),
			EnumerationLiteral(name="C_CPP"),
			EnumerationLiteral(name="Java"),
			EnumerationLiteral(name="Pascal_Delphi")
    }
)

# Classes
VorkursModel_RegistrationSystem = Class(name="VorkursModel::RegistrationSystem")
VorkursModel_Person = Class(name="VorkursModel::Person", is_abstract=True)
VorkursModel_Contact = Class(name="VorkursModel::Contact")
VorkursModel_Notebook = Class(name="VorkursModel::Notebook")
VorkursModel_Student = Class(name="VorkursModel::Student")
VorkursModel_TeachingAssistant = Class(name="VorkursModel::TeachingAssistant")
VorkursModel_Address = Class(name="VorkursModel::Address")
VorkursModel_Qualification = Class(name="VorkursModel::Qualification")
Person = Class(name="Person")
VorkursModel_Room = Class(name="VorkursModel::Room")

# VorkursModel_RegistrationSystem class attributes and methods

# VorkursModel_Person class attributes and methods
VorkursModel_Person_firstname: Property = Property(name="firstname", type=StringType)
VorkursModel_Person_lastname: Property = Property(name="lastname", type=StringType)
VorkursModel_Person_subject: Property = Property(name="subject", type=StringType)
VorkursModel_Person_gender: Property = Property(name="gender", type=StringType)
VorkursModel_Person.attributes={VorkursModel_Person_gender, VorkursModel_Person_firstname, VorkursModel_Person_subject, VorkursModel_Person_lastname}

# VorkursModel_Contact class attributes and methods
VorkursModel_Contact_phonenumber: Property = Property(name="phonenumber", type=StringType)
VorkursModel_Contact_Email: Property = Property(name="Email", type=StringType)
VorkursModel_Contact.attributes={VorkursModel_Contact_Email, VorkursModel_Contact_phonenumber}

# VorkursModel_Notebook class attributes and methods
VorkursModel_Notebook_OperatingSystem: Property = Property(name="OperatingSystem", type=StringType)
VorkursModel_Notebook_hasWLAN: Property = Property(name="hasWLAN", type=BooleanType)
VorkursModel_Notebook.attributes={VorkursModel_Notebook_OperatingSystem, VorkursModel_Notebook_hasWLAN}

# VorkursModel_Student class attributes and methods

# VorkursModel_TeachingAssistant class attributes and methods

# VorkursModel_Address class attributes and methods
VorkursModel_Address_city: Property = Property(name="city", type=StringType)
VorkursModel_Address_state: Property = Property(name="state", type=StringType)
VorkursModel_Address_zip: Property = Property(name="zip", type=StringType)
VorkursModel_Address_street: Property = Property(name="street", type=StringType)
VorkursModel_Address.attributes={VorkursModel_Address_zip, VorkursModel_Address_street, VorkursModel_Address_city, VorkursModel_Address_state}

# VorkursModel_Qualification class attributes and methods
VorkursModel_Qualification_hasPCExperience: Property = Property(name="hasPCExperience", type=BooleanType)
VorkursModel_Qualification_hasProgrammingExperience: Property = Property(name="hasProgrammingExperience", type=BooleanType)
VorkursModel_Qualification_Language: Property = Property(name="Language", type=StringType)
VorkursModel_Qualification_programminLanguage: Property = Property(name="programminLanguage", type=StringType)
VorkursModel_Qualification.attributes={VorkursModel_Qualification_hasPCExperience, VorkursModel_Qualification_hasProgrammingExperience, VorkursModel_Qualification_programminLanguage, VorkursModel_Qualification_Language}

# Person class attributes and methods

# VorkursModel_Room class attributes and methods
VorkursModel_Room_roomNr: Property = Property(name="roomNr", type=IntegerType)
VorkursModel_Room_sockets: Property = Property(name="sockets", type=BooleanType)
VorkursModel_Room_seats: Property = Property(name="seats", type=IntegerType)
VorkursModel_Room_hasComputers: Property = Property(name="hasComputers", type=BooleanType)
VorkursModel_Room.attributes={VorkursModel_Room_seats, VorkursModel_Room_hasComputers, VorkursModel_Room_sockets, VorkursModel_Room_roomNr}

# Relationships
contactinfo3: BinaryAssociation = BinaryAssociation(
    name="contactinfo3",
    ends={
        Property(name="VorkursModel_Contact", type=VorkursModel_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="VorkursModel_Person", type=VorkursModel_Contact, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
notebook4: BinaryAssociation = BinaryAssociation(
    name="notebook4",
    ends={
        Property(name="VorkursModel_Notebook", type=VorkursModel_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="VorkursModel_Person5", type=VorkursModel_Notebook, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
students0: BinaryAssociation = BinaryAssociation(
    name="students0",
    ends={
        Property(name="VorkursModel_Student", type=VorkursModel_RegistrationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="VorkursModel_RegistrationSystem", type=VorkursModel_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teachingAssistants1: BinaryAssociation = BinaryAssociation(
    name="teachingAssistants1",
    ends={
        Property(name="VorkursModel_TeachingAssistant", type=VorkursModel_RegistrationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="VorkursModel_RegistrationSystem2", type=VorkursModel_TeachingAssistant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualification6: BinaryAssociation = BinaryAssociation(
    name="qualification6",
    ends={
        Property(name="VorkursModel_Qualification", type=VorkursModel_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="VorkursModel_Person7", type=VorkursModel_Qualification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
address8: BinaryAssociation = BinaryAssociation(
    name="address8",
    ends={
        Property(name="VorkursModel_Address", type=VorkursModel_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="VorkursModel_Contact9", type=VorkursModel_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
room10: BinaryAssociation = BinaryAssociation(
    name="room10",
    ends={
        Property(name="VorkursModel_Room", type=VorkursModel_TeachingAssistant, multiplicity=Multiplicity(1, 1)),
        Property(name="VorkursModel_TeachingAssistant11", type=VorkursModel_Room, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_VorkursModel_TeachingAssistant_Person = Generalization(general=Person, specific=VorkursModel_TeachingAssistant)
gen_VorkursModel_Student_Person = Generalization(general=Person, specific=VorkursModel_Student)

# Domain Model
domain_model = DomainModel(
    name="VorkursModel",
    types={VorkursModel_RegistrationSystem, VorkursModel_Person, VorkursModel_Contact, VorkursModel_Notebook, VorkursModel_Student, VorkursModel_TeachingAssistant, VorkursModel_Address, VorkursModel_Qualification, Person, VorkursModel_Room, Nationality, Gender, Subject, OperatingSystem, ProgrammingLanguage},
    associations={contactinfo3, notebook4, students0, teachingAssistants1, qualification6, address8, room10},
    generalizations={gen_VorkursModel_TeachingAssistant_Person, gen_VorkursModel_Student_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)