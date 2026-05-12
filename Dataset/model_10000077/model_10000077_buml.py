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
User = Class(name="User")
Buyer = Class(name="Buyer")
Seller = Class(name="Seller")
Basket = Class(name="Basket")
Position = Class(name="Position")
Address = Class(name="Address")
Store = Class(name="Store")
Order = Class(name="Order")
Product = Class(name="Product")
Offer = Class(name="Offer")
Category = Class(name="Category")

# User class attributes and methods
User_id: Property = Property(name="id", type=StringType)
User_attribute: Property = Property(name="attribute", type=StringType)
User_username: Property = Property(name="username", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_firstname: Property = Property(name="firstname", type=StringType)
User_lastname: Property = Property(name="lastname", type=StringType)
User.attributes={User_lastname, User_id, User_firstname, User_username, User_attribute, User_password}

# Buyer class attributes and methods
Buyer_email: Property = Property(name="email", type=StringType)
Buyer.attributes={Buyer_email}

# Seller class attributes and methods
Seller_registerNumber: Property = Property(name="registerNumber", type=StringType)
Seller.attributes={Seller_registerNumber}

# Basket class attributes and methods
Basket_id: Property = Property(name="id", type=IntegerType)
Basket_updatedAt: Property = Property(name="updatedAt", type=StringType)
Basket.attributes={Basket_updatedAt, Basket_id}

# Position class attributes and methods
Position_longitude: Property = Property(name="longitude", type=StringType)
Position_latitude: Property = Property(name="latitude", type=StringType)
Position_createdAt: Property = Property(name="createdAt", type=StringType)
Position_id: Property = Property(name="id", type=IntegerType)
Position.attributes={Position_id, Position_createdAt, Position_latitude, Position_longitude}

# Address class attributes and methods
Address_id: Property = Property(name="id", type=IntegerType)
Address_street: Property = Property(name="street", type=StringType)
Address_zipCode: Property = Property(name="zipCode", type=StringType)
Address_city: Property = Property(name="city", type=StringType)
Address_country: Property = Property(name="country", type=StringType)
Address.attributes={Address_zipCode, Address_street, Address_city, Address_id, Address_country}

# Store class attributes and methods
Store_id: Property = Property(name="id", type=IntegerType)
Store_name: Property = Property(name="name", type=StringType)
Store_photoPath: Property = Property(name="photoPath", type=StringType)
Store.attributes={Store_id, Store_photoPath, Store_name}

# Order class attributes and methods
Order_id: Property = Property(name="id", type=IntegerType)
Order_createdAt: Property = Property(name="createdAt", type=StringType)
Order_amount: Property = Property(name="amount", type=IntegerType)
Order.attributes={Order_createdAt, Order_amount, Order_id}

# Product class attributes and methods
Product_id: Property = Property(name="id", type=IntegerType)
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product_price: Property = Property(name="price", type=IntegerType)
Product_photoPath: Property = Property(name="photoPath", type=StringType)
Product.attributes={Product_name, Product_price, Product_description, Product_id, Product_photoPath}

# Offer class attributes and methods
Offer_id: Property = Property(name="id", type=IntegerType)
Offer_discount: Property = Property(name="discount", type=IntegerType)
Offer_beginDate: Property = Property(name="beginDate", type=StringType)
Offer_endDate: Property = Property(name="endDate", type=StringType)
Offer.attributes={Offer_endDate, Offer_id, Offer_beginDate, Offer_discount}

# Category class attributes and methods
Category_id: Property = Property(name="id", type=IntegerType)
Category_name: Property = Property(name="name", type=StringType)
Category_photoPath: Property = Property(name="photoPath", type=StringType)
Category.attributes={Category_id, Category_photoPath, Category_name}

# Relationships
Buyer_Basket: BinaryAssociation = BinaryAssociation(
    name="Buyer_Basket",
    ends={
        Property(name="basket0", type=Basket, multiplicity=Multiplicity(1, 1)),
        Property(name="buyer1", type=Buyer, multiplicity=Multiplicity(1, 1))
    }
)
Buyer_Position: BinaryAssociation = BinaryAssociation(
    name="Buyer_Position",
    ends={
        Property(name="position2", type=Position, multiplicity=Multiplicity(1, 1)),
        Property(name="buyer3", type=Buyer, multiplicity=Multiplicity(1, 1))
    }
)
Address_Position: BinaryAssociation = BinaryAssociation(
    name="Address_Position",
    ends={
        Property(name="position4", type=Position, multiplicity=Multiplicity(1, 1)),
        Property(name="address5", type=Address, multiplicity=Multiplicity(1, 1))
    }
)
Store_Address: BinaryAssociation = BinaryAssociation(
    name="Store_Address",
    ends={
        Property(name="address6", type=Address, multiplicity=Multiplicity(1, 1)),
        Property(name="store7", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Seller_Store: BinaryAssociation = BinaryAssociation(
    name="Seller_Store",
    ends={
        Property(name="store8", type=Store, multiplicity=Multiplicity(1, 1)),
        Property(name="seller9", type=Seller, multiplicity=Multiplicity(1, 1))
    }
)
Buyer_Order: BinaryAssociation = BinaryAssociation(
    name="Buyer_Order",
    ends={
        Property(name="order10", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="buyer11", type=Buyer, multiplicity=Multiplicity(1, 1))
    }
)
Product_Offer: BinaryAssociation = BinaryAssociation(
    name="Product_Offer",
    ends={
        Property(name="offer12", type=Offer, multiplicity=Multiplicity(0, 9999)),
        Property(name="product13", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Category_Product: BinaryAssociation = BinaryAssociation(
    name="Category_Product",
    ends={
        Property(name="product14", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="category15", type=Category, multiplicity=Multiplicity(1, 1))
    }
)
Store_Product: BinaryAssociation = BinaryAssociation(
    name="Store_Product",
    ends={
        Property(name="product16", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="store17", type=Store, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0b321e9a_e5b3_4d42_b3c1_a0e9ba8f8adc",
    types={User, Buyer, Seller, Basket, Position, Address, Store, Order, Product, Offer, Category},
    associations={Buyer_Basket, Buyer_Position, Address_Position, Store_Address, Seller_Store, Buyer_Order, Product_Offer, Category_Product, Store_Product},
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