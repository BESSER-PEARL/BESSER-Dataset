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
nocollectionowner_Order = Class(name="nocollectionowner::Order")
nocollectionowner_Transaction = Class(name="nocollectionowner::Transaction")
nocollectionowner_Product = Class(name="nocollectionowner::Product")
nocollectionowner_ProductCategory = Class(name="nocollectionowner::ProductCategory")
nocollectionowner_PriceCategory = Class(name="nocollectionowner::PriceCategory")
nocollectionowner_Customer = Class(name="nocollectionowner::Customer")

# nocollectionowner_Order class attributes and methods
nocollectionowner_Order_number: Property = Property(name="number", type=StringType)
nocollectionowner_Order_comments: Property = Property(name="comments", type=StringType)
nocollectionowner_Order.attributes={nocollectionowner_Order_number, nocollectionowner_Order_comments}

# nocollectionowner_Transaction class attributes and methods
nocollectionowner_Transaction_number: Property = Property(name="number", type=StringType)
nocollectionowner_Transaction_startDate: Property = Property(name="startDate", type=DateType)
nocollectionowner_Transaction_endDate: Property = Property(name="endDate", type=DateType)
nocollectionowner_Transaction_price: Property = Property(name="price", type=FloatType)
nocollectionowner_Transaction_paidDate: Property = Property(name="paidDate", type=DateType)
nocollectionowner_Transaction.attributes={nocollectionowner_Transaction_startDate, nocollectionowner_Transaction_endDate, nocollectionowner_Transaction_price, nocollectionowner_Transaction_paidDate, nocollectionowner_Transaction_number}

# nocollectionowner_Product class attributes and methods
nocollectionowner_Product_name: Property = Property(name="name", type=StringType)
nocollectionowner_Product_number: Property = Property(name="number", type=StringType)
nocollectionowner_Product_description: Property = Property(name="description", type=StringType)
nocollectionowner_Product.attributes={nocollectionowner_Product_description, nocollectionowner_Product_name, nocollectionowner_Product_number}

# nocollectionowner_ProductCategory class attributes and methods
nocollectionowner_ProductCategory_name: Property = Property(name="name", type=StringType)
nocollectionowner_ProductCategory.attributes={nocollectionowner_ProductCategory_name}

# nocollectionowner_PriceCategory class attributes and methods
nocollectionowner_PriceCategory_name: Property = Property(name="name", type=StringType)
nocollectionowner_PriceCategory_prices: Property = Property(name="prices", type=FloatType)
nocollectionowner_PriceCategory.attributes={nocollectionowner_PriceCategory_name, nocollectionowner_PriceCategory_prices}

# nocollectionowner_Customer class attributes and methods
nocollectionowner_Customer_surname: Property = Property(name="surname", type=StringType)
nocollectionowner_Customer_familyName: Property = Property(name="familyName", type=StringType)
nocollectionowner_Customer_telephoneNr: Property = Property(name="telephoneNr", type=StringType)
nocollectionowner_Customer_address: Property = Property(name="address", type=StringType)
nocollectionowner_Customer_hotel: Property = Property(name="hotel", type=StringType)
nocollectionowner_Customer_comments: Property = Property(name="comments", type=StringType)
nocollectionowner_Customer.attributes={nocollectionowner_Customer_familyName, nocollectionowner_Customer_surname, nocollectionowner_Customer_comments, nocollectionowner_Customer_hotel, nocollectionowner_Customer_address, nocollectionowner_Customer_telephoneNr}

# Relationships
products2: BinaryAssociation = BinaryAssociation(
    name="products2",
    ends={
        Property(name="Product", type=nocollectionowner_ProductCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="productCategory", type=nocollectionowner_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subCategorys4: BinaryAssociation = BinaryAssociation(
    name="subCategorys4",
    ends={
        Property(name="ProductCategory5", type=nocollectionowner_ProductCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=nocollectionowner_ProductCategory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="ProductCategory8", type=nocollectionowner_ProductCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="subCategorys", type=nocollectionowner_ProductCategory, multiplicity=Multiplicity(0, 1))
    }
)
transactions9: BinaryAssociation = BinaryAssociation(
    name="transactions9",
    ends={
        Property(name="Transaction", type=nocollectionowner_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=nocollectionowner_Transaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
productCategory0: BinaryAssociation = BinaryAssociation(
    name="productCategory0",
    ends={
        Property(name="ProductCategory", type=nocollectionowner_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="products", type=nocollectionowner_ProductCategory, multiplicity=Multiplicity(0, 1))
    }
)
priceCategory1: BinaryAssociation = BinaryAssociation(
    name="priceCategory1",
    ends={
        Property(name="nocollectionowner_PriceCategory", type=nocollectionowner_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="nocollectionowner_Product", type=nocollectionowner_PriceCategory, multiplicity=Multiplicity(0, 1))
    }
)
customer10: BinaryAssociation = BinaryAssociation(
    name="customer10",
    ends={
        Property(name="nocollectionowner_Customer", type=nocollectionowner_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="nocollectionowner_Order", type=nocollectionowner_Customer, multiplicity=Multiplicity(0, 1))
    }
)
order11: BinaryAssociation = BinaryAssociation(
    name="order11",
    ends={
        Property(name="Order", type=nocollectionowner_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="transactions", type=nocollectionowner_Order, multiplicity=Multiplicity(0, 1))
    }
)
product12: BinaryAssociation = BinaryAssociation(
    name="product12",
    ends={
        Property(name="nocollectionowner_Product13", type=nocollectionowner_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="nocollectionowner_Transaction", type=nocollectionowner_Product, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="nocollectionowner",
    types={nocollectionowner_Order, nocollectionowner_Transaction, nocollectionowner_Product, nocollectionowner_ProductCategory, nocollectionowner_PriceCategory, nocollectionowner_Customer},
    associations={products2, subCategorys4, parent7, transactions9, productCategory0, priceCategory1, customer10, order11, product12},
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