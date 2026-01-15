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
shop_Product = Class(name="shop::Product")
shop_ProductCategory = Class(name="shop::ProductCategory")
shop_PriceCategory = Class(name="shop::PriceCategory")
shop_Customer = Class(name="shop::Customer")
shop_Order = Class(name="shop::Order")
shop_Transaction = Class(name="shop::Transaction")

# shop_Product class attributes and methods
shop_Product_name: Property = Property(name="name", type=StringType)
shop_Product_number: Property = Property(name="number", type=StringType)
shop_Product_description: Property = Property(name="description", type=StringType)
shop_Product.attributes={shop_Product_description, shop_Product_name, shop_Product_number}

# shop_ProductCategory class attributes and methods
shop_ProductCategory_name: Property = Property(name="name", type=StringType)
shop_ProductCategory.attributes={shop_ProductCategory_name}

# shop_PriceCategory class attributes and methods
shop_PriceCategory_name: Property = Property(name="name", type=StringType)
shop_PriceCategory_prices: Property = Property(name="prices", type=FloatType)
shop_PriceCategory.attributes={shop_PriceCategory_prices, shop_PriceCategory_name}

# shop_Customer class attributes and methods
shop_Customer_hotel: Property = Property(name="hotel", type=StringType)
shop_Customer_comments: Property = Property(name="comments", type=StringType)
shop_Customer_surname: Property = Property(name="surname", type=StringType)
shop_Customer_familyName: Property = Property(name="familyName", type=StringType)
shop_Customer_telephoneNr: Property = Property(name="telephoneNr", type=StringType)
shop_Customer_address: Property = Property(name="address", type=StringType)
shop_Customer.attributes={shop_Customer_address, shop_Customer_comments, shop_Customer_telephoneNr, shop_Customer_hotel, shop_Customer_surname, shop_Customer_familyName}

# shop_Order class attributes and methods
shop_Order_number: Property = Property(name="number", type=StringType)
shop_Order_comments: Property = Property(name="comments", type=StringType)
shop_Order.attributes={shop_Order_comments, shop_Order_number}

# shop_Transaction class attributes and methods
shop_Transaction_number: Property = Property(name="number", type=StringType)
shop_Transaction_startDate: Property = Property(name="startDate", type=DateType)
shop_Transaction_endDate: Property = Property(name="endDate", type=DateType)
shop_Transaction_price: Property = Property(name="price", type=FloatType)
shop_Transaction_paidDate: Property = Property(name="paidDate", type=DateType)
shop_Transaction.attributes={shop_Transaction_startDate, shop_Transaction_number, shop_Transaction_paidDate, shop_Transaction_endDate, shop_Transaction_price}

# Relationships
products2: BinaryAssociation = BinaryAssociation(
    name="products2",
    ends={
        Property(name="Product", type=shop_ProductCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="productCategory", type=shop_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
productCategory0: BinaryAssociation = BinaryAssociation(
    name="productCategory0",
    ends={
        Property(name="ProductCategory", type=shop_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="products", type=shop_ProductCategory, multiplicity=Multiplicity(0, 1))
    }
)
priceCategory1: BinaryAssociation = BinaryAssociation(
    name="priceCategory1",
    ends={
        Property(name="shop_PriceCategory", type=shop_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="shop_Product", type=shop_PriceCategory, multiplicity=Multiplicity(0, 1))
    }
)
subCategorys4: BinaryAssociation = BinaryAssociation(
    name="subCategorys4",
    ends={
        Property(name="ProductCategory5", type=shop_ProductCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=shop_ProductCategory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="ProductCategory8", type=shop_ProductCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="subCategorys", type=shop_ProductCategory, multiplicity=Multiplicity(0, 1))
    }
)
transactions9: BinaryAssociation = BinaryAssociation(
    name="transactions9",
    ends={
        Property(name="Transaction", type=shop_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=shop_Transaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customer10: BinaryAssociation = BinaryAssociation(
    name="customer10",
    ends={
        Property(name="shop_Customer", type=shop_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="shop_Order", type=shop_Customer, multiplicity=Multiplicity(0, 1))
    }
)
order11: BinaryAssociation = BinaryAssociation(
    name="order11",
    ends={
        Property(name="Order", type=shop_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="transactions", type=shop_Order, multiplicity=Multiplicity(0, 1))
    }
)
product12: BinaryAssociation = BinaryAssociation(
    name="product12",
    ends={
        Property(name="shop_Product13", type=shop_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="shop_Transaction", type=shop_Product, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="shop",
    types={shop_Product, shop_ProductCategory, shop_PriceCategory, shop_Customer, shop_Order, shop_Transaction},
    associations={products2, productCategory0, priceCategory1, subCategorys4, parent7, transactions9, customer10, order11, product12},
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