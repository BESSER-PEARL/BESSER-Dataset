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
Customer1 = Class(name="Customer1")
Products = Class(name="Products")
Guest = Class(name="Guest")
Payment = Class(name="Payment")
Order = Class(name="Order")
OrderProduct = Class(name="OrderProduct")
CustomerProduct = Class(name="CustomerProduct")
Address = Class(name="Address")
OrderCustomer = Class(name="OrderCustomer")

# Customer class attributes and methods
Customer_attribute: Property = Property(name="attribute", type=StringType)
Customer_attribute2: Property = Property(name="attribute2", type=StringType)
Customer_attribute3: Property = Property(name="attribute3", type=StringType)
Customer.attributes={Customer_attribute2, Customer_attribute, Customer_attribute3}

# Customer1 class attributes and methods
Customer1_ID: Property = Property(name="ID", type=StringType)
Customer1_Name: Property = Property(name="Name", type=StringType)
Customer1_Email: Property = Property(name="Email", type=StringType)
Customer1_attribute: Property = Property(name="attribute", type=StringType)
Customer1_Password: Property = Property(name="Password", type=StringType)
Customer1.attributes={Customer1_Password, Customer1_attribute, Customer1_Email, Customer1_Name, Customer1_ID}

# Products class attributes and methods
Products_ID: Property = Property(name="ID", type=IntegerType)
Products_Name: Property = Property(name="Name", type=StringType)
Products_Description: Property = Property(name="Description", type=StringType)
Products.attributes={Products_ID, Products_Name, Products_Description}

# Guest class attributes and methods

# Payment class attributes and methods
Payment_ID: Property = Property(name="ID", type=IntegerType)
Payment_Customer: Property = Property(name="Customer", type=Customer)
Payment_Details: Property = Property(name="Details", type=StringType)
Payment_Amount: Property = Property(name="Amount", type=IntegerType)
Payment.attributes={Payment_Details, Payment_Amount, Payment_Customer, Payment_ID}

# Order class attributes and methods
Order_id: Property = Property(name="id", type=IntegerType)
Order_Date: Property = Property(name="Date", type=StringType)
Order_ProductID: Property = Property(name="ProductID", type=Products)
Order.attributes={Order_ProductID, Order_Date, Order_id}

# OrderProduct class attributes and methods
OrderProduct_ID: Property = Property(name="ID", type=IntegerType)
OrderProduct_Oid: Property = Property(name="Oid", type=Order)
OrderProduct_Pid: Property = Property(name="Pid", type=Products)
OrderProduct.attributes={OrderProduct_ID, OrderProduct_Pid, OrderProduct_Oid}

# CustomerProduct class attributes and methods
CustomerProduct_ID: Property = Property(name="ID", type=IntegerType)
CustomerProduct_Customer: Property = Property(name="Customer", type=Customer)
CustomerProduct_Product: Property = Property(name="Product", type=Products)
CustomerProduct.attributes={CustomerProduct_Product, CustomerProduct_Customer, CustomerProduct_ID}

# Address class attributes and methods
Address_House: Property = Property(name="House", type=StringType)
Address_Street: Property = Property(name="Street", type=StringType)
Address_City: Property = Property(name="City", type=StringType)
Address.attributes={Address_City, Address_Street, Address_House}

# OrderCustomer class attributes and methods
OrderCustomer_id: Property = Property(name="id", type=IntegerType)
OrderCustomer_Customer: Property = Property(name="Customer", type=Customer)
OrderCustomer_Order: Property = Property(name="Order", type=Order)
OrderCustomer.attributes={OrderCustomer_id, OrderCustomer_Customer, OrderCustomer_Order}

# Relationships
Products_OrderProduct: BinaryAssociation = BinaryAssociation(
    name="Products_OrderProduct",
    ends={
        Property(name="products9", type=Products, multiplicity=Multiplicity(1, 1)),
        Property(name="orderProduct8", type=OrderProduct, multiplicity=Multiplicity(1, 9999))
    }
)
Order_OrderProduct: BinaryAssociation = BinaryAssociation(
    name="Order_OrderProduct",
    ends={
        Property(name="orderProduct10", type=OrderProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="order11", type=Order, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Payment",
    ends={
        Property(name="payment12", type=Payment, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer13", type=Customer1, multiplicity=Multiplicity(1, 1))
    }
)
Address_Customer: BinaryAssociation = BinaryAssociation(
    name="Address_Customer",
    ends={
        Property(name="customer14", type=Customer1, multiplicity=Multiplicity(1, 1)),
        Property(name="address15", type=Address, multiplicity=Multiplicity(1, 1))
    }
)
Address_Order: BinaryAssociation = BinaryAssociation(
    name="Address_Order",
    ends={
        Property(name="order16", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="address17", type=Address, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Customer: BinaryAssociation = BinaryAssociation(
    name="Customer_Customer",
    ends={
        Property(name="customer0", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Customer2: BinaryAssociation = BinaryAssociation(
    name="Customer_Customer2",
    ends={
        Property(name="customer2", type=Customer, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer3", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_CustomerProduct: BinaryAssociation = BinaryAssociation(
    name="Customer_CustomerProduct",
    ends={
        Property(name="customerProduct4", type=CustomerProduct, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer5", type=Customer1, multiplicity=Multiplicity(1, 1))
    }
)
CustomerProduct_Products: BinaryAssociation = BinaryAssociation(
    name="CustomerProduct_Products",
    ends={
        Property(name="products6", type=Products, multiplicity=Multiplicity(1, 1)),
        Property(name="customerProduct7", type=CustomerProduct, multiplicity=Multiplicity(1, 9999))
    }
)
Order_OrderCustomer: BinaryAssociation = BinaryAssociation(
    name="Order_OrderCustomer",
    ends={
        Property(name="orderCustomer18", type=OrderCustomer, multiplicity=Multiplicity(1, 9999)),
        Property(name="order19", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Customer_OrderCustomer: BinaryAssociation = BinaryAssociation(
    name="Customer_OrderCustomer",
    ends={
        Property(name="orderCustomer20", type=OrderCustomer, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer21", type=Customer1, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_PKbbIMskEemfA78eeeotcQ",
    types={Customer, Customer1, Products, Guest, Payment, Order, OrderProduct, CustomerProduct, Address, OrderCustomer},
    associations={Products_OrderProduct, Order_OrderProduct, Customer_Payment, Address_Customer, Address_Order, Customer_Customer, Customer_Customer2, Customer_CustomerProduct, CustomerProduct_Products, Order_OrderCustomer, Customer_OrderCustomer},
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