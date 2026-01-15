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
Sexus: Enumeration = Enumeration(
    name="Sexus",
    literals={
            EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female"),
			EnumerationLiteral(name="undefined")
    }
)

# Classes
gedcoml_Projectdescription = Class(name="gedcoml::Projectdescription")
gedcoml_FamilyImport = Class(name="gedcoml::FamilyImport")
gedcoml_Author = Class(name="gedcoml::Author")
gedcoml_Family = Class(name="gedcoml::Family")
gedcoml_Person = Class(name="gedcoml::Person", is_abstract=True)
gedcoml_BekanntePerson = Class(name="gedcoml::BekanntePerson")
Person = Class(name="Person")
gedcoml_Others = Class(name="gedcoml::Others")
Source = Class(name="Source")
gedcoml_PersonRef = Class(name="gedcoml::PersonRef")
gedcoml_UnbekanntePerson = Class(name="gedcoml::UnbekanntePerson")
gedcoml_Married = Class(name="gedcoml::Married")
gedcoml_Note = Class(name="gedcoml::Note")
gedcoml_Source = Class(name="gedcoml::Source", is_abstract=True)
gedcoml_FamilyBook = Class(name="gedcoml::FamilyBook")
gedcoml_PostAddress = Class(name="gedcoml::PostAddress")
Address = Class(name="Address")
gedcoml_Address = Class(name="gedcoml::Address", is_abstract=True)

# gedcoml_Projectdescription class attributes and methods
gedcoml_Projectdescription_groupId: Property = Property(name="groupId", type=StringType)
gedcoml_Projectdescription_artifactId: Property = Property(name="artifactId", type=StringType)
gedcoml_Projectdescription_version: Property = Property(name="version", type=StringType)
gedcoml_Projectdescription_publishingDate: Property = Property(name="publishingDate", type=StringType)
gedcoml_Projectdescription.attributes={gedcoml_Projectdescription_groupId, gedcoml_Projectdescription_publishingDate, gedcoml_Projectdescription_version, gedcoml_Projectdescription_artifactId}

# gedcoml_FamilyImport class attributes and methods

# gedcoml_Author class attributes and methods
gedcoml_Author_firstName: Property = Property(name="firstName", type=StringType)
gedcoml_Author_lastName: Property = Property(name="lastName", type=StringType)
gedcoml_Author.attributes={gedcoml_Author_firstName, gedcoml_Author_lastName}

# gedcoml_Family class attributes and methods
gedcoml_Family_name: Property = Property(name="name", type=StringType)
gedcoml_Family.attributes={gedcoml_Family_name}

# gedcoml_Person class attributes and methods
gedcoml_Person_id: Property = Property(name="id", type=StringType)
gedcoml_Person_sex: Property = Property(name="sex", type=StringType)
gedcoml_Person.attributes={gedcoml_Person_id, gedcoml_Person_sex}

# gedcoml_BekanntePerson class attributes and methods
gedcoml_BekanntePerson_firstName: Property = Property(name="firstName", type=StringType)
gedcoml_BekanntePerson_lastName: Property = Property(name="lastName", type=StringType)
gedcoml_BekanntePerson_middleName: Property = Property(name="middleName", type=StringType)
gedcoml_BekanntePerson_birthDay: Property = Property(name="birthDay", type=StringType)
gedcoml_BekanntePerson_deathDay: Property = Property(name="deathDay", type=StringType)
gedcoml_BekanntePerson_birthName: Property = Property(name="birthName", type=StringType)
gedcoml_BekanntePerson.attributes={gedcoml_BekanntePerson_firstName, gedcoml_BekanntePerson_birthName, gedcoml_BekanntePerson_lastName, gedcoml_BekanntePerson_birthDay, gedcoml_BekanntePerson_deathDay, gedcoml_BekanntePerson_middleName}

# Person class attributes and methods

# gedcoml_Others class attributes and methods
gedcoml_Others_description: Property = Property(name="description", type=StringType)
gedcoml_Others.attributes={gedcoml_Others_description}

# Source class attributes and methods

# gedcoml_PersonRef class attributes and methods

# gedcoml_UnbekanntePerson class attributes and methods

# gedcoml_Married class attributes and methods
gedcoml_Married_weddingDay: Property = Property(name="weddingDay", type=StringType)
gedcoml_Married_separationDay: Property = Property(name="separationDay", type=StringType)
gedcoml_Married.attributes={gedcoml_Married_weddingDay, gedcoml_Married_separationDay}

# gedcoml_Note class attributes and methods
gedcoml_Note_content: Property = Property(name="content", type=StringType)
gedcoml_Note.attributes={gedcoml_Note_content}

# gedcoml_Source class attributes and methods

# gedcoml_FamilyBook class attributes and methods

# gedcoml_PostAddress class attributes and methods
gedcoml_PostAddress_street: Property = Property(name="street", type=StringType)
gedcoml_PostAddress_postcode: Property = Property(name="postcode", type=StringType)
gedcoml_PostAddress_city: Property = Property(name="city", type=StringType)
gedcoml_PostAddress.attributes={gedcoml_PostAddress_postcode, gedcoml_PostAddress_street, gedcoml_PostAddress_city}

# Address class attributes and methods

# gedcoml_Address class attributes and methods
gedcoml_Address_entry: Property = Property(name="entry", type=StringType)
gedcoml_Address_exodus: Property = Property(name="exodus", type=StringType)
gedcoml_Address.attributes={gedcoml_Address_exodus, gedcoml_Address_entry}

# Relationships
biologicalParentOf7: BinaryAssociation = BinaryAssociation(
    name="biologicalParentOf7",
    ends={
        Property(name="gedcoml_Person8", type=gedcoml_BekanntePerson, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_BekanntePerson", type=gedcoml_Person, multiplicity=Multiplicity(0, 9999))
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="gedcoml_FamilyImport", type=gedcoml_Projectdescription, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_Projectdescription", type=gedcoml_FamilyImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author1: BinaryAssociation = BinaryAssociation(
    name="author1",
    ends={
        Property(name="gedcoml_Author", type=gedcoml_Projectdescription, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_Projectdescription2", type=gedcoml_Author, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
members3: BinaryAssociation = BinaryAssociation(
    name="members3",
    ends={
        Property(name="gedcoml_Person", type=gedcoml_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_Family", type=gedcoml_Person, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
imports4: BinaryAssociation = BinaryAssociation(
    name="imports4",
    ends={
        Property(name="gedcoml_FamilyImport6", type=gedcoml_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_Family5", type=gedcoml_FamilyImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberId29: BinaryAssociation = BinaryAssociation(
    name="memberId29",
    ends={
        Property(name="gedcoml_BekanntePerson31", type=gedcoml_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_Author30", type=gedcoml_BekanntePerson, multiplicity=Multiplicity(0, 1))
    }
)
personID32: BinaryAssociation = BinaryAssociation(
    name="personID32",
    ends={
        Property(name="gedcoml_BekanntePerson33", type=gedcoml_PersonRef, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_PersonRef", type=gedcoml_BekanntePerson, multiplicity=Multiplicity(1, 1))
    }
)
biologicalFatherIs9: BinaryAssociation = BinaryAssociation(
    name="biologicalFatherIs9",
    ends={
        Property(name="gedcoml_Person11", type=gedcoml_BekanntePerson, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_BekanntePerson10", type=gedcoml_Person, multiplicity=Multiplicity(1, 1))
    }
)
biologicalMotherIs12: BinaryAssociation = BinaryAssociation(
    name="biologicalMotherIs12",
    ends={
        Property(name="gedcoml_Person14", type=gedcoml_BekanntePerson, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_BekanntePerson13", type=gedcoml_Person, multiplicity=Multiplicity(1, 1))
    }
)
marriedWith15: BinaryAssociation = BinaryAssociation(
    name="marriedWith15",
    ends={
        Property(name="gedcoml_Married", type=gedcoml_BekanntePerson, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_BekanntePerson16", type=gedcoml_Married, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
notes17: BinaryAssociation = BinaryAssociation(
    name="notes17",
    ends={
        Property(name="gedcoml_Note", type=gedcoml_BekanntePerson, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_BekanntePerson18", type=gedcoml_Note, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sources19: BinaryAssociation = BinaryAssociation(
    name="sources19",
    ends={
        Property(name="gedcoml_Source", type=gedcoml_BekanntePerson, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_BekanntePerson20", type=gedcoml_Source, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
project21: BinaryAssociation = BinaryAssociation(
    name="project21",
    ends={
        Property(name="gedcoml_Projectdescription22", type=gedcoml_FamilyBook, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_FamilyBook", type=gedcoml_Projectdescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedResource23: BinaryAssociation = BinaryAssociation(
    name="importedResource23",
    ends={
        Property(name="gedcoml_Family25", type=gedcoml_FamilyImport, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_FamilyImport24", type=gedcoml_Family, multiplicity=Multiplicity(1, 1))
    }
)
partner26: BinaryAssociation = BinaryAssociation(
    name="partner26",
    ends={
        Property(name="gedcoml_Person28", type=gedcoml_Married, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_Married27", type=gedcoml_Person, multiplicity=Multiplicity(1, 1))
    }
)
addresses34: BinaryAssociation = BinaryAssociation(
    name="addresses34",
    ends={
        Property(name="gedcoml_Address", type=gedcoml_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="gedcoml_Person35", type=gedcoml_Address, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_gedcoml_BekanntePerson_Person = Generalization(general=Person, specific=gedcoml_BekanntePerson)
gen_gedcoml_Others_Source = Generalization(general=Source, specific=gedcoml_Others)
gen_gedcoml_PersonRef_Source = Generalization(general=Source, specific=gedcoml_PersonRef)
gen_gedcoml_UnbekanntePerson_Person = Generalization(general=Person, specific=gedcoml_UnbekanntePerson)
gen_gedcoml_PostAddress_Address = Generalization(general=Address, specific=gedcoml_PostAddress)

# Domain Model
domain_model = DomainModel(
    name="gedcoml",
    types={gedcoml_Projectdescription, gedcoml_FamilyImport, gedcoml_Author, gedcoml_Family, gedcoml_Person, gedcoml_BekanntePerson, Person, gedcoml_Others, Source, gedcoml_PersonRef, gedcoml_UnbekanntePerson, gedcoml_Married, gedcoml_Note, gedcoml_Source, gedcoml_FamilyBook, gedcoml_PostAddress, Address, gedcoml_Address, Sexus},
    associations={biologicalParentOf7, imports0, author1, members3, imports4, memberId29, personID32, biologicalFatherIs9, biologicalMotherIs12, marriedWith15, notes17, sources19, project21, importedResource23, partner26, addresses34},
    generalizations={gen_gedcoml_BekanntePerson_Person, gen_gedcoml_Others_Source, gen_gedcoml_PersonRef_Source, gen_gedcoml_UnbekanntePerson_Person, gen_gedcoml_PostAddress_Address},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)