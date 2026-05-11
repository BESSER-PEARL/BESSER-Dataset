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
OrderChannel: Enumeration = Enumeration(
    name="OrderChannel",
    literals={
            EnumerationLiteral(name="WEB"),
			EnumerationLiteral(name="MAIL"),
			EnumerationLiteral(name="PHONE")
    }
)

# Classes
customerDsl_CustomerDb = Class(name="customerDsl_CustomerDb")
customerDsl_Customer = Class(name="customerDsl_Customer")
customerDsl_Order = Class(name="customerDsl_Order")
customerDsl_Product = Class(name="customerDsl_Product")
customerDsl_Address = Class(name="customerDsl_Address")
customerDsl_StreetAddress = Class(name="customerDsl_StreetAddress")
Address = Class(name="Address")
customerDsl_POBox = Class(name="customerDsl_POBox")

# customerDsl_CustomerDb class attributes and methods

# customerDsl_Customer class attributes and methods
customerDsl_Customer_name: Property = Property(name="name", type=StringType)
customerDsl_Customer_fullName: Property = Property(name="fullName", type=StringType)
customerDsl_Customer.attributes={customerDsl_Customer_fullName, customerDsl_Customer_name}

# customerDsl_Order class attributes and methods
customerDsl_Order_name: Property = Property(name="name", type=StringType)
customerDsl_Order_channel: Property = Property(name="channel", type=StringType)
customerDsl_Order.attributes={customerDsl_Order_channel, customerDsl_Order_name}

# customerDsl_Product class attributes and methods
customerDsl_Product_name: Property = Property(name="name", type=StringType)
customerDsl_Product_price: Property = Property(name="price", type=IntegerType)
customerDsl_Product.attributes={customerDsl_Product_price, customerDsl_Product_name}

# customerDsl_Address class attributes and methods
customerDsl_Address_name: Property = Property(name="name", type=StringType)
customerDsl_Address_zip: Property = Property(name="zip", type=StringType)
customerDsl_Address.attributes={customerDsl_Address_name, customerDsl_Address_zip}

# customerDsl_StreetAddress class attributes and methods
customerDsl_StreetAddress_street: Property = Property(name="street", type=StringType)
customerDsl_StreetAddress_city: Property = Property(name="city", type=StringType)
customerDsl_StreetAddress.attributes={customerDsl_StreetAddress_city, customerDsl_StreetAddress_street}

# Address class attributes and methods

# customerDsl_POBox class attributes and methods
customerDsl_POBox_number: Property = Property(name="number", type=IntegerType)
customerDsl_POBox.attributes={customerDsl_POBox_number}

# Relationships
customers0: BinaryAssociation = BinaryAssociation(
    name="customers0",
    ends={
        Property(name="customerDsl_Customer", type=customerDsl_CustomerDb, multiplicity=Multiplicity(1, 1)),
        Property(name="customerDsl_CustomerDb", type=customerDsl_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orders1: BinaryAssociation = BinaryAssociation(
    name="orders1",
    ends={
        Property(name="customerDsl_Order", type=customerDsl_CustomerDb, multiplicity=Multiplicity(1, 1)),
        Property(name="customerDsl_CustomerDb2", type=customerDsl_Order, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
products3: BinaryAssociation = BinaryAssociation(
    name="products3",
    ends={
        Property(name="customerDsl_Product", type=customerDsl_CustomerDb, multiplicity=Multiplicity(1, 1)),
        Property(name="customerDsl_CustomerDb4", type=customerDsl_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addresses5: BinaryAssociation = BinaryAssociation(
    name="addresses5",
    ends={
        Property(name="customerDsl_Address", type=customerDsl_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customerDsl_Customer6", type=customerDsl_Address, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customer7: BinaryAssociation = BinaryAssociation(
    name="customer7",
    ends={
        Property(name="customerDsl_Customer9", type=customerDsl_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="customerDsl_Order8", type=customerDsl_Customer, multiplicity=Multiplicity(0, 1))
    }
)
address10: BinaryAssociation = BinaryAssociation(
    name="address10",
    ends={
        Property(name="customerDsl_Address12", type=customerDsl_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="customerDsl_Order11", type=customerDsl_Address, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_customerDsl_StreetAddress_Address = Generalization(general=Address, specific=customerDsl_StreetAddress)
gen_customerDsl_POBox_Address = Generalization(general=Address, specific=customerDsl_POBox)

# Domain Model
domain_model = DomainModel(
    name="customerDsl",
    types={customerDsl_CustomerDb, customerDsl_Customer, customerDsl_Order, customerDsl_Product, customerDsl_Address, customerDsl_StreetAddress, Address, customerDsl_POBox, OrderChannel},
    associations={customers0, orders1, products3, addresses5, customer7, address10},
    generalizations={gen_customerDsl_StreetAddress_Address, gen_customerDsl_POBox_Address},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)