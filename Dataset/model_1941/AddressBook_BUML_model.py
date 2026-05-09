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
addressbook_AddressBook = Class(name="addressbook_AddressBook")
NamedElement = Class(name="NamedElement")
addressbook_Category = Class(name="addressbook_Category")
addressbook_NamedElement = Class(name="addressbook_NamedElement", is_abstract=True)
addressbook_Entry = Class(name="addressbook_Entry", is_abstract=True)
addressbook_Contact = Class(name="addressbook_Contact")
Entry = Class(name="Entry")
addressbook_Organization = Class(name="addressbook_Organization")

# addressbook_AddressBook class attributes and methods

# NamedElement class attributes and methods

# addressbook_Category class attributes and methods

# addressbook_NamedElement class attributes and methods
addressbook_NamedElement_name: Property = Property(name="name", type=StringType)
addressbook_NamedElement.attributes={addressbook_NamedElement_name}

# addressbook_Entry class attributes and methods
addressbook_Entry_id: Property = Property(name="id", type=IntegerType)
addressbook_Entry.attributes={addressbook_Entry_id}

# addressbook_Contact class attributes and methods
addressbook_Contact_firstName: Property = Property(name="firstName", type=StringType)
addressbook_Contact_lastName: Property = Property(name="lastName", type=StringType)
addressbook_Contact_email: Property = Property(name="email", type=StringType)
addressbook_Contact.attributes={addressbook_Contact_firstName, addressbook_Contact_lastName, addressbook_Contact_email}

# Entry class attributes and methods

# addressbook_Organization class attributes and methods
addressbook_Organization_homepage: Property = Property(name="homepage", type=StringType)
addressbook_Organization.attributes={addressbook_Organization_homepage}

# Relationships
categories0: BinaryAssociation = BinaryAssociation(
    name="categories0",
    ends={
        Property(name="Category", type=addressbook_AddressBook, multiplicity=Multiplicity(1, 1)),
        Property(name="addressBook", type=addressbook_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressBook1: BinaryAssociation = BinaryAssociation(
    name="addressBook1",
    ends={
        Property(name="AddressBook", type=addressbook_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="categories", type=addressbook_AddressBook, multiplicity=Multiplicity(0, 1))
    }
)
entries2: BinaryAssociation = BinaryAssociation(
    name="entries2",
    ends={
        Property(name="Entry", type=addressbook_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=addressbook_Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
category3: BinaryAssociation = BinaryAssociation(
    name="category3",
    ends={
        Property(name="Category4", type=addressbook_Entry, multiplicity=Multiplicity(1, 1)),
        Property(name="entries", type=addressbook_Category, multiplicity=Multiplicity(0, 1))
    }
)
employers5: BinaryAssociation = BinaryAssociation(
    name="employers5",
    ends={
        Property(name="Organization", type=addressbook_Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=addressbook_Organization, multiplicity=Multiplicity(0, 9999))
    }
)
employees6: BinaryAssociation = BinaryAssociation(
    name="employees6",
    ends={
        Property(name="Contact", type=addressbook_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="employers", type=addressbook_Contact, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_addressbook_AddressBook_NamedElement = Generalization(general=NamedElement, specific=addressbook_AddressBook)
gen_addressbook_Category_NamedElement = Generalization(general=NamedElement, specific=addressbook_Category)
gen_addressbook_Contact_Entry = Generalization(general=Entry, specific=addressbook_Contact)
gen_addressbook_Organization_Entry = Generalization(general=Entry, specific=addressbook_Organization)
gen_addressbook_Organization_NamedElement = Generalization(general=NamedElement, specific=addressbook_Organization)

# Domain Model
domain_model = DomainModel(
    name="addressbook",
    types={addressbook_AddressBook, NamedElement, addressbook_Category, addressbook_NamedElement, addressbook_Entry, addressbook_Contact, Entry, addressbook_Organization},
    associations={categories0, addressBook1, entries2, category3, employers5, employees6},
    generalizations={gen_addressbook_AddressBook_NamedElement, gen_addressbook_Category_NamedElement, gen_addressbook_Contact_Entry, gen_addressbook_Organization_Entry, gen_addressbook_Organization_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)