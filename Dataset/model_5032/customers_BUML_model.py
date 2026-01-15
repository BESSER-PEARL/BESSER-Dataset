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
USStates: Enumeration = Enumeration(
    name="USStates",
    literals={
            EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="AL"),
			EnumerationLiteral(name="AK"),
			EnumerationLiteral(name="AS"),
			EnumerationLiteral(name="AZ"),
			EnumerationLiteral(name="AR"),
			EnumerationLiteral(name="CA"),
			EnumerationLiteral(name="CO")
    }
)

CanadaProvinces: Enumeration = Enumeration(
    name="CanadaProvinces",
    literals={
            EnumerationLiteral(name="NB"),
			EnumerationLiteral(name="NL"),
			EnumerationLiteral(name="NT"),
			EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="AB"),
			EnumerationLiteral(name="BC"),
			EnumerationLiteral(name="MB")
    }
)

# Classes
customers_Customer = Class(name="customers::Customer")
customers_CreditCard = Class(name="customers::CreditCard")
customers_Address = Class(name="customers::Address")
customers_USAddress = Class(name="customers::USAddress")
Address = Class(name="Address")
customers_CanadaAddress = Class(name="customers::CanadaAddress")
customers_CustomersDB = Class(name="customers::CustomersDB")

# customers_Customer class attributes and methods
customers_Customer_firstName: Property = Property(name="firstName", type=StringType)
customers_Customer_lastName: Property = Property(name="lastName", type=StringType)
customers_Customer_comment: Property = Property(name="comment", type=StringType)
customers_Customer_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
customers_Customer.attributes={customers_Customer_lastName, customers_Customer_comment, customers_Customer_firstName, customers_Customer_dateOfBirth}

# customers_CreditCard class attributes and methods
customers_CreditCard_ccNumber: Property = Property(name="ccNumber", type=StringType)
customers_CreditCard_expiresDate: Property = Property(name="expiresDate", type=DateType)
customers_CreditCard_type: Property = Property(name="type", type=StringType)
customers_CreditCard.attributes={customers_CreditCard_ccNumber, customers_CreditCard_expiresDate, customers_CreditCard_type}

# customers_Address class attributes and methods
customers_Address_street: Property = Property(name="street", type=StringType)
customers_Address_town: Property = Property(name="town", type=StringType)
customers_Address_zipCode: Property = Property(name="zipCode", type=StringType)
customers_Address.attributes={customers_Address_zipCode, customers_Address_street, customers_Address_town}

# customers_USAddress class attributes and methods
customers_USAddress_state: Property = Property(name="state", type=StringType)
customers_USAddress.attributes={customers_USAddress_state}

# Address class attributes and methods

# customers_CanadaAddress class attributes and methods
customers_CanadaAddress_province: Property = Property(name="province", type=StringType)
customers_CanadaAddress.attributes={customers_CanadaAddress_province}

# customers_CustomersDB class attributes and methods
customers_CustomersDB_comment: Property = Property(name="comment", type=StringType)
customers_CustomersDB.attributes={customers_CustomersDB_comment}

# Relationships
creditCard0: BinaryAssociation = BinaryAssociation(
    name="creditCard0",
    ends={
        Property(name="CreditCard", type=customers_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="holder", type=customers_CreditCard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address1: BinaryAssociation = BinaryAssociation(
    name="address1",
    ends={
        Property(name="customers_Address", type=customers_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customers_Customer", type=customers_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
holder2: BinaryAssociation = BinaryAssociation(
    name="holder2",
    ends={
        Property(name="Customer", type=customers_CreditCard, multiplicity=Multiplicity(1, 1)),
        Property(name="creditCard", type=customers_Customer, multiplicity=Multiplicity(1, 1))
    }
)
customers3: BinaryAssociation = BinaryAssociation(
    name="customers3",
    ends={
        Property(name="customers_Customer4", type=customers_CustomersDB, multiplicity=Multiplicity(1, 1)),
        Property(name="customers_CustomersDB", type=customers_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_customers_USAddress_Address = Generalization(general=Address, specific=customers_USAddress)
gen_customers_CanadaAddress_Address = Generalization(general=Address, specific=customers_CanadaAddress)

# Domain Model
domain_model = DomainModel(
    name="customers",
    types={customers_Customer, customers_CreditCard, customers_Address, customers_USAddress, Address, customers_CanadaAddress, customers_CustomersDB, USStates, CanadaProvinces},
    associations={creditCard0, address1, holder2, customers3},
    generalizations={gen_customers_USAddress_Address, gen_customers_CanadaAddress_Address},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)