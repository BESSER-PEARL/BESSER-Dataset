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
contacts_Address = Class(name="contacts::Address")
contacts_PhoneNumber = Class(name="contacts::PhoneNumber")
contacts_Contact = Class(name="contacts::Contact")
contacts_AddressBook = Class(name="contacts::AddressBook")
contacts_UoD = Class(name="contacts::UoD")

# contacts_Address class attributes and methods
contacts_Address_zipCode: Property = Property(name="zipCode", type=StringType)
contacts_Address_street: Property = Property(name="street", type=StringType)
contacts_Address_city: Property = Property(name="city", type=StringType)
contacts_Address_state: Property = Property(name="state", type=StringType)
contacts_Address_country: Property = Property(name="country", type=StringType)
contacts_Address.attributes={contacts_Address_country, contacts_Address_street, contacts_Address_zipCode, contacts_Address_city, contacts_Address_state}

# contacts_PhoneNumber class attributes and methods
contacts_PhoneNumber_number: Property = Property(name="number", type=StringType)
contacts_PhoneNumber_country: Property = Property(name="country", type=StringType)
contacts_PhoneNumber.attributes={contacts_PhoneNumber_country, contacts_PhoneNumber_number}

# contacts_Contact class attributes and methods
contacts_Contact_company: Property = Property(name="company", type=StringType)
contacts_Contact_jobTitle: Property = Property(name="jobTitle", type=StringType)
contacts_Contact_email: Property = Property(name="email", type=StringType)
contacts_Contact_webPage: Property = Property(name="webPage", type=StringType)
contacts_Contact_firstName: Property = Property(name="firstName", type=StringType)
contacts_Contact_middleName: Property = Property(name="middleName", type=StringType)
contacts_Contact_lastName: Property = Property(name="lastName", type=StringType)
contacts_Contact_title: Property = Property(name="title", type=StringType)
contacts_Contact_note: Property = Property(name="note", type=StringType)
contacts_Contact_image: Property = Property(name="image", type=StringType)
contacts_Contact.attributes={contacts_Contact_lastName, contacts_Contact_company, contacts_Contact_image, contacts_Contact_webPage, contacts_Contact_title, contacts_Contact_email, contacts_Contact_jobTitle, contacts_Contact_note, contacts_Contact_firstName, contacts_Contact_middleName}

# contacts_AddressBook class attributes and methods

# contacts_UoD class attributes and methods

# Relationships
workAddress0: BinaryAssociation = BinaryAssociation(
    name="workAddress0",
    ends={
        Property(name="contacts_Address", type=contacts_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="contacts_Contact", type=contacts_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phone1: BinaryAssociation = BinaryAssociation(
    name="phone1",
    ends={
        Property(name="contacts_PhoneNumber", type=contacts_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="contacts_Contact2", type=contacts_PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contacts9: BinaryAssociation = BinaryAssociation(
    name="contacts9",
    ends={
        Property(name="contacts_Contact10", type=contacts_AddressBook, multiplicity=Multiplicity(1, 1)),
        Property(name="contacts_AddressBook", type=contacts_Contact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mobile3: BinaryAssociation = BinaryAssociation(
    name="mobile3",
    ends={
        Property(name="contacts_PhoneNumber5", type=contacts_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="contacts_Contact4", type=contacts_PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
homeAddress6: BinaryAssociation = BinaryAssociation(
    name="homeAddress6",
    ends={
        Property(name="contacts_Address8", type=contacts_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="contacts_Contact7", type=contacts_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allAddressBooks11: BinaryAssociation = BinaryAssociation(
    name="allAddressBooks11",
    ends={
        Property(name="contacts_AddressBook12", type=contacts_UoD, multiplicity=Multiplicity(1, 1)),
        Property(name="contacts_UoD", type=contacts_AddressBook, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="contacts",
    types={contacts_Address, contacts_PhoneNumber, contacts_Contact, contacts_AddressBook, contacts_UoD},
    associations={workAddress0, phone1, contacts9, mobile3, homeAddress6, allAddressBooks11},
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