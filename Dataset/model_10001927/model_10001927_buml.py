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
Products = Class(name="Products")
Shopping_Cart = Class(name="Shopping_Cart")
Payment = Class(name="Payment")
Order = Class(name="Order")
Account = Class(name="Account")
Warehouse = Class(name="Warehouse")
Items = Class(name="Items")

# Customer class attributes and methods
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_Customer_ID: Property = Property(name="Customer_ID", type=IntegerType)
Customer.attributes={Customer_Name, Customer_Customer_ID}

# Products class attributes and methods
Products_Product_ID: Property = Property(name="Product_ID", type=IntegerType)
Products.attributes={Products_Product_ID}

# Shopping_Cart class attributes and methods
Shopping_Cart_Date: Property = Property(name="Date", type=IntegerType)
Shopping_Cart.attributes={Shopping_Cart_Date}

# Payment class attributes and methods
Payment_Payment_ID: Property = Property(name="Payment_ID", type=IntegerType)
Payment_Date: Property = Property(name="Date", type=IntegerType)
Payment.attributes={Payment_Payment_ID, Payment_Date}

# Order class attributes and methods
Order_Order_ID: Property = Property(name="Order_ID", type=IntegerType)
Order.attributes={Order_Order_ID}

# Account class attributes and methods
Account_Address: Property = Property(name="Address", type=StringType)
Account_Test_attr: Property = Property(name="Test_attr", type=IntegerType)
Account.attributes={Account_Address, Account_Test_attr}

# Warehouse class attributes and methods
Warehouse_Warehouse_branch: Property = Property(name="Warehouse_branch", type=StringType)
Warehouse.attributes={Warehouse_Warehouse_branch}

# Items class attributes and methods
Items_Description: Property = Property(name="Description", type=StringType)
Items.attributes={Items_Description}

# Relationships
Customer_Products: BinaryAssociation = BinaryAssociation(
    name="Customer_Products",
    ends={
        Property(name="products0", type=Products, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order2", type=Order, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer3", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Shopping_Cart",
    ends={
        Property(name="shopping_Cart4", type=Shopping_Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Payment",
    ends={
        Property(name="payment6", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Account_Customer: BinaryAssociation = BinaryAssociation(
    name="Account_Customer",
    ends={
        Property(name="customer8", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="account9", type=Account, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account10", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="customer11", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Warehouse_Products: BinaryAssociation = BinaryAssociation(
    name="Warehouse_Products",
    ends={
        Property(name="products12", type=Products, multiplicity=Multiplicity(1, 9999)),
        Property(name="warehouse13", type=Warehouse, multiplicity=Multiplicity(1, 9999))
    }
)
Payment__Order: BinaryAssociation = BinaryAssociation(
    name="Payment__Order",
    ends={
        Property(name="order14", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment15", type=Payment, multiplicity=Multiplicity(1, 1))
    }
)
Shopping_Cart_Items: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Items",
    ends={
        Property(name="items16", type=Items, multiplicity=Multiplicity(1, 9999)),
        Property(name="shopping_Cart17", type=Shopping_Cart, multiplicity=Multiplicity(1, 1))
    }
)
Order_Account: BinaryAssociation = BinaryAssociation(
    name="Order_Account",
    ends={
        Property(name="account18", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="order19", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_Account2: BinaryAssociation = BinaryAssociation(
    name="Order_Account2",
    ends={
        Property(name="account20", type=Account, multiplicity=Multiplicity(0, 1)),
        Property(name="order21", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order22", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="account23", type=Account, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_dzxiQDfREeqTDpmqRhKD9Q",
    types={Customer, Products, Shopping_Cart, Payment, Order, Account, Warehouse, Items},
    associations={Customer_Products, Customer_Order, Customer_Shopping_Cart, Customer_Payment, Account_Customer, Customer_Account, Warehouse_Products, Payment__Order, Shopping_Cart_Items, Order_Account, Order_Account2, Account_Order},
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