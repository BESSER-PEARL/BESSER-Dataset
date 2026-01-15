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
ContactType: Enumeration = Enumeration(
    name="ContactType",
    literals={
            EnumerationLiteral(name="PHONE"),
			EnumerationLiteral(name="EMAIL")
    }
)

# Classes
test_Person = Class(name="test::Person")
test_Contact = Class(name="test::Contact")
test_Address = Class(name="test::Address")

# test_Person class attributes and methods
test_Person_firstname: Property = Property(name="firstname", type=StringType)
test_Person_lastname: Property = Property(name="lastname", type=StringType)
test_Person.attributes={test_Person_lastname, test_Person_firstname}

# test_Contact class attributes and methods
test_Contact_value: Property = Property(name="value", type=StringType)
test_Contact_type: Property = Property(name="type", type=StringType)
test_Contact.attributes={test_Contact_value, test_Contact_type}

# test_Address class attributes and methods
test_Address_street: Property = Property(name="street", type=StringType)
test_Address_city: Property = Property(name="city", type=StringType)
test_Address.attributes={test_Address_city, test_Address_street}

# Relationships
contacts1: BinaryAssociation = BinaryAssociation(
    name="contacts1",
    ends={
        Property(name="test_Contact", type=test_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Person2", type=test_Contact, multiplicity=Multiplicity(0, 9999))
    }
)
address0: BinaryAssociation = BinaryAssociation(
    name="address0",
    ends={
        Property(name="test_Address", type=test_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Person", type=test_Address, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_Person, test_Contact, test_Address, ContactType},
    associations={contacts1, address0},
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