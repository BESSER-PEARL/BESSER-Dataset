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
addressbook_Contact = Class(name="addressbook::Contact", is_abstract=True)
addressbook_Electronic = Class(name="addressbook::Electronic")
Contact = Class(name="Contact")
addressbook_Office = Class(name="addressbook::Office")
addressbook_People = Class(name="addressbook::People")
addressbook_AddressBook = Class(name="addressbook::AddressBook")
addressbook_Repository = Class(name="addressbook::Repository")
addressbook_BookVersion = Class(name="addressbook::BookVersion")

# addressbook_Contact class attributes and methods

# addressbook_Electronic class attributes and methods
addressbook_Electronic_email: Property = Property(name="email", type=StringType)
addressbook_Electronic_website: Property = Property(name="website", type=StringType)
addressbook_Electronic.attributes={addressbook_Electronic_website, addressbook_Electronic_email}

# Contact class attributes and methods

# addressbook_Office class attributes and methods
addressbook_Office_company: Property = Property(name="company", type=StringType)
addressbook_Office.attributes={addressbook_Office_company}

# addressbook_People class attributes and methods
addressbook_People_name: Property = Property(name="name", type=StringType)
addressbook_People.attributes={addressbook_People_name}

# addressbook_AddressBook class attributes and methods

# addressbook_Repository class attributes and methods
addressbook_Repository_m_checkin: Method = Method(name="checkin", parameters={})
addressbook_Repository_m_checkout: Method = Method(name="checkout", parameters={Parameter(name='id')}, type=StringType)
addressbook_Repository.methods={addressbook_Repository_m_checkout, addressbook_Repository_m_checkin}

# addressbook_BookVersion class attributes and methods
addressbook_BookVersion_id: Property = Property(name="id", type=IntegerType)
addressbook_BookVersion.attributes={addressbook_BookVersion_id}

# Relationships
contacts0: BinaryAssociation = BinaryAssociation(
    name="contacts0",
    ends={
        Property(name="addressbook_Contact", type=addressbook_People, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_People", type=addressbook_Contact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
peoples1: BinaryAssociation = BinaryAssociation(
    name="peoples1",
    ends={
        Property(name="addressbook_People2", type=addressbook_AddressBook, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_AddressBook", type=addressbook_People, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
head3: BinaryAssociation = BinaryAssociation(
    name="head3",
    ends={
        Property(name="addressbook_AddressBook4", type=addressbook_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_Repository", type=addressbook_AddressBook, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
history5: BinaryAssociation = BinaryAssociation(
    name="history5",
    ends={
        Property(name="addressbook_BookVersion", type=addressbook_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_Repository6", type=addressbook_BookVersion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book7: BinaryAssociation = BinaryAssociation(
    name="book7",
    ends={
        Property(name="addressbook_AddressBook9", type=addressbook_BookVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_BookVersion8", type=addressbook_AddressBook, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_addressbook_Electronic_Contact = Generalization(general=Contact, specific=addressbook_Electronic)
gen_addressbook_Office_Contact = Generalization(general=Contact, specific=addressbook_Office)

# Domain Model
domain_model = DomainModel(
    name="addressbook",
    types={addressbook_Contact, addressbook_Electronic, Contact, addressbook_Office, addressbook_People, addressbook_AddressBook, addressbook_Repository, addressbook_BookVersion},
    associations={contacts0, peoples1, head3, history5, book7},
    generalizations={gen_addressbook_Electronic_Contact, gen_addressbook_Office_Contact},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)