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
Customer = Class(name="Customer")
Payment = Class(name="Payment")
Product = Class(name="Product")
Inventory = Class(name="Inventory")

# Customer class attributes and methods
Customer_type: Property = Property(name="type", type=StringType)
Customer_royalty: Property = Property(name="royalty", type=BooleanType)
Customer.attributes={Customer_royalty, Customer_type}

# Payment class attributes and methods
Payment_quantity: Property = Property(name="quantity", type=IntegerType)
Payment_ID: Property = Property(name="ID", type=IntegerType)
Payment_list: Property = Property(name="list", type=StringType)
Payment_totalamount: Property = Property(name="totalamount", type=StringType)
Payment_finalamount: Property = Property(name="finalamount", type=StringType)
Payment_discountamount: Property = Property(name="discountamount", type=StringType)
Payment_amount__: Property = Property(name="amount__", type=StringType)
Payment_Imtiaz: Property = Property(name="Imtiaz", type=StringType)
Payment.attributes={Payment_finalamount, Payment_ID, Payment_discountamount, Payment_amount__, Payment_list, Payment_quantity, Payment_Imtiaz, Payment_totalamount}

# Product class attributes and methods
Product_ID: Property = Property(name="ID", type=IntegerType)
Product_qty: Property = Property(name="qty", type=IntegerType)
Product_Name: Property = Property(name="Name", type=StringType)
Product_type: Property = Property(name="type", type=StringType)
Product_price: Property = Property(name="price", type=StringType)
Product_amount: Property = Property(name="amount", type=StringType)
Product_blgl: Property = Property(name="blgl", type=BooleanType)
Product_attribute: Property = Property(name="attribute", type=StringType)
Product.attributes={Product_price, Product_attribute, Product_ID, Product_qty, Product_type, Product_Name, Product_amount, Product_blgl}

# Inventory class attributes and methods
Inventory_SuperMarket: Property = Property(name="SuperMarket", type=StringType)
Inventory_list: Property = Property(name="list", type=StringType)
Inventory.attributes={Inventory_SuperMarket, Inventory_list}

# Relationships
Customer_Payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Payment",
    ends={
        Property(name="payment0", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Inventory_Product: BinaryAssociation = BinaryAssociation(
    name="Inventory_Product",
    ends={
        Property(name="product2", type=Product, multiplicity=Multiplicity(1, 9999)),
        Property(name="inventory3", type=Inventory, multiplicity=Multiplicity(1, 9999))
    }
)
Product_Customer: BinaryAssociation = BinaryAssociation(
    name="Product_Customer",
    ends={
        Property(name="customer4", type=Customer, multiplicity=Multiplicity(0, 9999)),
        Property(name="product5", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
Product_Payment: BinaryAssociation = BinaryAssociation(
    name="Product_Payment",
    ends={
        Property(name="payment6", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="product7", type=Product, multiplicity=Multiplicity(1, 9999))
    }
)
Payment_Inventory: BinaryAssociation = BinaryAssociation(
    name="Payment_Inventory",
    ends={
        Property(name="inventory8", type=Inventory, multiplicity=Multiplicity(1, 1)),
        Property(name="payment9", type=Payment, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Ni_I4Fk5Eem2zdxW8Rsq_g",
    types={Customer, Payment, Product, Inventory},
    associations={Customer_Payment, Inventory_Product, Product_Customer, Product_Payment, Payment_Inventory},
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