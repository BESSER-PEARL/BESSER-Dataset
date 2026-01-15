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
RelationshipType: Enumeration = Enumeration(
    name="RelationshipType",
    literals={
            EnumerationLiteral(name="Boss"),
			EnumerationLiteral(name="Employee"),
			EnumerationLiteral(name="Subdivision"),
			EnumerationLiteral(name="CoWorker")
    }
)

NoteType: Enumeration = Enumeration(
    name="NoteType",
    literals={
            EnumerationLiteral(name="MEETING"),
			EnumerationLiteral(name="CALL"),
			EnumerationLiteral(name="EMAIL")
    }
)

# Classes
addressbook_Contact = Class(name="addressbook::Contact", is_abstract=True)
addressbook_Address = Class(name="addressbook::Address")
addressbook_Relationship = Class(name="addressbook::Relationship")
addressbook_Note = Class(name="addressbook::Note")
addressbook_Person = Class(name="addressbook::Person")
Contact = Class(name="Contact")
addressbook_Company = Class(name="addressbook::Company")
addressbook_AddressBook = Class(name="addressbook::AddressBook")

# addressbook_Contact class attributes and methods
addressbook_Contact_Name: Property = Property(name="Name", type=StringType)
addressbook_Contact_Phone: Property = Property(name="Phone", type=StringType)
addressbook_Contact_Website: Property = Property(name="Website", type=StringType)
addressbook_Contact_EMail: Property = Property(name="EMail", type=StringType)
addressbook_Contact.attributes={addressbook_Contact_Phone, addressbook_Contact_Website, addressbook_Contact_EMail, addressbook_Contact_Name}

# addressbook_Address class attributes and methods
addressbook_Address_City: Property = Property(name="City", type=StringType)
addressbook_Address_Street: Property = Property(name="Street", type=StringType)
addressbook_Address_HouseNr: Property = Property(name="HouseNr", type=StringType)
addressbook_Address.attributes={addressbook_Address_HouseNr, addressbook_Address_City, addressbook_Address_Street}

# addressbook_Relationship class attributes and methods
addressbook_Relationship_Type: Property = Property(name="Type", type=StringType)
addressbook_Relationship.attributes={addressbook_Relationship_Type}

# addressbook_Note class attributes and methods
addressbook_Note_Author: Property = Property(name="Author", type=StringType)
addressbook_Note_Time: Property = Property(name="Time", type=DateType)
addressbook_Note_Type: Property = Property(name="Type", type=StringType)
addressbook_Note_Comment: Property = Property(name="Comment", type=StringType)
addressbook_Note.attributes={addressbook_Note_Comment, addressbook_Note_Type, addressbook_Note_Author, addressbook_Note_Time}

# addressbook_Person class attributes and methods
addressbook_Person_Title: Property = Property(name="Title", type=StringType)
addressbook_Person.attributes={addressbook_Person_Title}

# Contact class attributes and methods

# addressbook_Company class attributes and methods
addressbook_Company_Industry: Property = Property(name="Industry", type=StringType)
addressbook_Company.attributes={addressbook_Company_Industry}

# addressbook_AddressBook class attributes and methods

# Relationships
Contact9: BinaryAssociation = BinaryAssociation(
    name="Contact9",
    ends={
        Property(name="addressbook_Contact10", type=addressbook_AddressBook, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_AddressBook", type=addressbook_Contact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="Contact", type=addressbook_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="isRelated", type=addressbook_Contact, multiplicity=Multiplicity(1, 1))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="Contact13", type=addressbook_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="relates", type=addressbook_Contact, multiplicity=Multiplicity(1, 1))
    }
)
address0: BinaryAssociation = BinaryAssociation(
    name="address0",
    ends={
        Property(name="addressbook_Address", type=addressbook_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_Contact", type=addressbook_Address, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inRelation2: BinaryAssociation = BinaryAssociation(
    name="inRelation2",
    ends={
        Property(name="addressbook_Contact3", type=addressbook_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_Contact1", type=addressbook_Contact, multiplicity=Multiplicity(0, 9999))
    }
)
relates4: BinaryAssociation = BinaryAssociation(
    name="relates4",
    ends={
        Property(name="Relationship", type=addressbook_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=addressbook_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isRelated5: BinaryAssociation = BinaryAssociation(
    name="isRelated5",
    ends={
        Property(name="Relationship6", type=addressbook_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=addressbook_Relationship, multiplicity=Multiplicity(0, 9999))
    }
)
Note7: BinaryAssociation = BinaryAssociation(
    name="Note7",
    ends={
        Property(name="addressbook_Note", type=addressbook_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_Contact8", type=addressbook_Note, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_addressbook_Person_Contact = Generalization(general=Contact, specific=addressbook_Person)
gen_addressbook_Company_Contact = Generalization(general=Contact, specific=addressbook_Company)

# Domain Model
domain_model = DomainModel(
    name="addressbook",
    types={addressbook_Contact, addressbook_Address, addressbook_Relationship, addressbook_Note, addressbook_Person, Contact, addressbook_Company, addressbook_AddressBook, RelationshipType, NoteType},
    associations={Contact9, target11, source12, address0, inRelation2, relates4, isRelated5, Note7},
    generalizations={gen_addressbook_Person_Contact, gen_addressbook_Company_Contact},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)