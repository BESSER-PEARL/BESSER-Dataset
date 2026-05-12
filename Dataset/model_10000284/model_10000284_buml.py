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
Property_ = Class(name="Property")
User = Class(name="User")
customer = Class(name="customer")
owner = Class(name="owner")
Administrator = Class(name="Administrator")
operation_or_contract = Class(name="operation_or_contract")

# Property class attributes and methods
Property__property_id: Property = Property(name="property_id", type=StringType)
Property__property_type: Property = Property(name="property_type", type=StringType)
Property__address: Property = Property(name="address", type=StringType)
Property__location: Property = Property(name="location", type=StringType)
Property__size: Property = Property(name="size", type=StringType)
Property__Available: Property = Property(name="Available", type=BooleanType)
Property_.attributes={Property__property_id, Property__address, Property__location, Property__Available, Property__property_type, Property__size}

# User class attributes and methods
User_Id: Property = Property(name="Id", type=IntegerType)
User_email: Property = Property(name="email", type=StringType)
User_Address: Property = Property(name="Address", type=StringType)
User_phone: Property = Property(name="phone", type=IntegerType)
User_password: Property = Property(name="password", type=StringType)
User.attributes={User_password, User_email, User_Address, User_Id, User_phone}

# customer class attributes and methods

# owner class attributes and methods

# Administrator class attributes and methods
Administrator_admin_name: Property = Property(name="admin_name", type=StringType)
Administrator_password: Property = Property(name="password", type=StringType)
Administrator.attributes={Administrator_admin_name, Administrator_password}

# operation_or_contract class attributes and methods
operation_or_contract_operation_id: Property = Property(name="operation_id", type=IntegerType)
operation_or_contract_customer_id: Property = Property(name="customer_id", type=StringType)
operation_or_contract_owner_id: Property = Property(name="owner_id", type=StringType)
operation_or_contract_operation_type: Property = Property(name="operation_type", type=StringType)
operation_or_contract_Property_id: Property = Property(name="Property_id", type=IntegerType)
operation_or_contract.attributes={operation_or_contract_Property_id, operation_or_contract_customer_id, operation_or_contract_owner_id, operation_or_contract_operation_type, operation_or_contract_operation_id}

# Relationships
User_Administrator: BinaryAssociation = BinaryAssociation(
    name="User_Administrator",
    ends={
        Property(name="administrator0", type=Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="employee1", type=User, multiplicity=Multiplicity(1, 9999))
    }
)
Property_Seller: BinaryAssociation = BinaryAssociation(
    name="Property_Seller",
    ends={
        Property(name="owner2", type=owner, multiplicity=Multiplicity(1, 1)),
        Property(name="property3", type=Property_, multiplicity=Multiplicity(1, 9999))
    }
)
owner_operation_or_contract: BinaryAssociation = BinaryAssociation(
    name="owner_operation_or_contract",
    ends={
        Property(name="operation_or_contract4", type=operation_or_contract, multiplicity=Multiplicity(0, 1)),
        Property(name="owner5", type=owner, multiplicity=Multiplicity(1, 1))
    }
)
customer_Property: BinaryAssociation = BinaryAssociation(
    name="customer_Property",
    ends={
        Property(name="property6", type=Property_, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=customer, multiplicity=Multiplicity(0, 9999))
    }
)
operation_or_contract_Property: BinaryAssociation = BinaryAssociation(
    name="operation_or_contract_Property",
    ends={
        Property(name="property8", type=Property_, multiplicity=Multiplicity(1, 1)),
        Property(name="operation_or_contract9", type=operation_or_contract, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_23567908_1301_4fe2_ab95_93b21d1e5c4d",
    types={Property_, User, customer, owner, Administrator, operation_or_contract},
    associations={User_Administrator, Property_Seller, owner_operation_or_contract, customer_Property, operation_or_contract_Property},
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