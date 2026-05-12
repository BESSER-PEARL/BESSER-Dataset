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
Bank = Class(name="Bank")
ATM = Class(name="ATM")
Account = Class(name="Account")
Customer = Class(name="Customer")

# Bank class attributes and methods
Bank_code: Property = Property(name="code", type=IntegerType)
Bank_address: Property = Property(name="address", type=StringType)
Bank.attributes={Bank_address, Bank_code}

# ATM class attributes and methods
ATM_location: Property = Property(name="location", type=StringType)
ATM_managedby: Property = Property(name="managedby", type=StringType)
ATM.attributes={ATM_location, ATM_managedby}

# Account class attributes and methods
Account_number: Property = Property(name="number", type=IntegerType)
Account_balance: Property = Property(name="balance", type=IntegerType)
Account.attributes={Account_balance, Account_number}

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_dob: Property = Property(name="dob", type=StringType)
Customer_cardnumber: Property = Property(name="cardnumber", type=IntegerType)
Customer_pin: Property = Property(name="pin", type=IntegerType)
Customer.attributes={Customer_name, Customer_address, Customer_cardnumber, Customer_pin, Customer_dob}

# Relationships
Bank_ATM: BinaryAssociation = BinaryAssociation(
    name="Bank_ATM",
    ends={
        Property(name="aTM0", type=ATM, multiplicity=Multiplicity(0, 1)),
        Property(name="bank1", type=Bank, multiplicity=Multiplicity(0, 1))
    }
)
Bank_Account: BinaryAssociation = BinaryAssociation(
    name="Bank_Account",
    ends={
        Property(name="account2", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="bank3", type=Bank, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account4", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_is0EgLOdEemcsc4aPpxbEQ",
    types={Bank, ATM, Account, Customer},
    associations={Bank_ATM, Bank_Account, Customer_Account},
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