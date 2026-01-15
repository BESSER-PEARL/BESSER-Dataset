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
AddressType: Enumeration = Enumeration(
    name="AddressType",
    literals={
            EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="BUSINESS"),
			EnumerationLiteral(name="DELIVERY")
    }
)

# Classes
addressbook_AddressBook = Class(name="addressbook::AddressBook")
addressbook_Person = Class(name="addressbook::Person")
addressbook_Country = Class(name="addressbook::Country")
addressbook_Address = Class(name="addressbook::Address")
addressbook_FederalState = Class(name="addressbook::FederalState")

# addressbook_AddressBook class attributes and methods

# addressbook_Person class attributes and methods
addressbook_Person_firstname: Property = Property(name="firstname", type=StringType)
addressbook_Person_lastname: Property = Property(name="lastname", type=StringType)
addressbook_Person.attributes={addressbook_Person_firstname, addressbook_Person_lastname}

# addressbook_Country class attributes and methods
addressbook_Country_name: Property = Property(name="name", type=StringType)
addressbook_Country.attributes={addressbook_Country_name}

# addressbook_Address class attributes and methods
addressbook_Address_zip: Property = Property(name="zip", type=StringType)
addressbook_Address_city: Property = Property(name="city", type=StringType)
addressbook_Address_street: Property = Property(name="street", type=StringType)
addressbook_Address_type: Property = Property(name="type", type=StringType)
addressbook_Address.attributes={addressbook_Address_street, addressbook_Address_zip, addressbook_Address_city, addressbook_Address_type}

# addressbook_FederalState class attributes and methods
addressbook_FederalState_name: Property = Property(name="name", type=StringType)
addressbook_FederalState.attributes={addressbook_FederalState_name}

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="Person", type=addressbook_AddressBook, multiplicity=Multiplicity(1, 1)),
        Property(name="addressBook", type=addressbook_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
countries1: BinaryAssociation = BinaryAssociation(
    name="countries1",
    ends={
        Property(name="addressbook_Country", type=addressbook_AddressBook, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_AddressBook", type=addressbook_Country, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addresses2: BinaryAssociation = BinaryAssociation(
    name="addresses2",
    ends={
        Property(name="Address", type=addressbook_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="person", type=addressbook_Address, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressBook3: BinaryAssociation = BinaryAssociation(
    name="addressBook3",
    ends={
        Property(name="AddressBook", type=addressbook_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=addressbook_AddressBook, multiplicity=Multiplicity(0, 1))
    }
)
country4: BinaryAssociation = BinaryAssociation(
    name="country4",
    ends={
        Property(name="addressbook_Country5", type=addressbook_Address, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_Address", type=addressbook_Country, multiplicity=Multiplicity(0, 1))
    }
)
federalState6: BinaryAssociation = BinaryAssociation(
    name="federalState6",
    ends={
        Property(name="addressbook_FederalState", type=addressbook_Address, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_Address7", type=addressbook_FederalState, multiplicity=Multiplicity(0, 1))
    }
)
person8: BinaryAssociation = BinaryAssociation(
    name="person8",
    ends={
        Property(name="Person9", type=addressbook_Address, multiplicity=Multiplicity(1, 1)),
        Property(name="addresses", type=addressbook_Person, multiplicity=Multiplicity(0, 1))
    }
)
federalStates10: BinaryAssociation = BinaryAssociation(
    name="federalStates10",
    ends={
        Property(name="FederalState", type=addressbook_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="country", type=addressbook_FederalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addressBook11: BinaryAssociation = BinaryAssociation(
    name="addressBook11",
    ends={
        Property(name="addressbook_AddressBook13", type=addressbook_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="addressbook_Country12", type=addressbook_AddressBook, multiplicity=Multiplicity(0, 1))
    }
)
country14: BinaryAssociation = BinaryAssociation(
    name="country14",
    ends={
        Property(name="Country", type=addressbook_FederalState, multiplicity=Multiplicity(1, 1)),
        Property(name="federalStates", type=addressbook_Country, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="addressbook",
    types={addressbook_AddressBook, addressbook_Person, addressbook_Country, addressbook_Address, addressbook_FederalState, AddressType},
    associations={persons0, countries1, addresses2, addressBook3, country4, federalState6, person8, federalStates10, addressBook11, country14},
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