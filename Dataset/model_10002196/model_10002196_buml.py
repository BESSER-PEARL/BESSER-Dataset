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
online_shopping_chart_system_Component = Class(name="online_shopping_chart_system_Component")
admin_portal_Component = Class(name="admin_portal_Component")
online_shopping_portal_Component = Class(name="online_shopping_portal_Component")
admin_Actor = Class(name="admin_Actor")
online_client_Actor = Class(name="online_client_Actor")
registered_client_Actor = Class(name="registered_client_Actor")
Product_catalog_Component = Class(name="Product_catalog_Component")
search_UseCase = Class(name="search_UseCase")
Customer = Class(name="Customer")
ShoppingCart = Class(name="ShoppingCart")
Product = Class(name="Product")
CartItem = Class(name="CartItem")
keyWord = Class(name="keyWord")
Order = Class(name="Order")

# online_shopping_chart_system_Component class attributes and methods

# admin_portal_Component class attributes and methods

# online_shopping_portal_Component class attributes and methods

# admin_Actor class attributes and methods

# online_client_Actor class attributes and methods

# registered_client_Actor class attributes and methods

# Product_catalog_Component class attributes and methods

# search_UseCase class attributes and methods

# Customer class attributes and methods
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_adress: Property = Property(name="adress", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer_phone: Property = Property(name="phone", type=StringType)
Customer_cardId: Property = Property(name="cardId", type=IntegerType)
Customer.attributes={Customer_Name, Customer_adress, Customer_phone, Customer_email, Customer_cardId}

# ShoppingCart class attributes and methods
ShoppingCart_cartID: Property = Property(name="cartID", type=IntegerType)
ShoppingCart_productID: Property = Property(name="productID", type=IntegerType)
ShoppingCart_quantity: Property = Property(name="quantity", type=IntegerType)
ShoppingCart_dateAdded: Property = Property(name="dateAdded", type=StringType)
ShoppingCart.attributes={ShoppingCart_quantity, ShoppingCart_cartID, ShoppingCart_productID, ShoppingCart_dateAdded}

# Product class attributes and methods
Product_ProductID: Property = Property(name="ProductID", type=IntegerType)
Product_Name: Property = Property(name="Name", type=StringType)
Product_Price: Property = Property(name="Price", type=StringType)
Product_fileName: Property = Property(name="fileName", type=StringType)
Product_cardId: Property = Property(name="cardId", type=IntegerType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_fileName, Product_cardId, Product_description, Product_ProductID, Product_Price, Product_Name}

# CartItem class attributes and methods
CartItem_cartID: Property = Property(name="cartID", type=IntegerType)
CartItem_Name: Property = Property(name="Name", type=StringType)
CartItem_ProductID: Property = Property(name="ProductID", type=IntegerType)
CartItem_quantity: Property = Property(name="quantity", type=IntegerType)
CartItem_Price: Property = Property(name="Price", type=StringType)
CartItem_fileName: Property = Property(name="fileName", type=StringType)
CartItem_subtotal: Property = Property(name="subtotal", type=StringType)
CartItem.attributes={CartItem_fileName, CartItem_quantity, CartItem_Price, CartItem_subtotal, CartItem_ProductID, CartItem_Name, CartItem_cartID}

# keyWord class attributes and methods
keyWord_keyword: Property = Property(name="keyword", type=StringType)
keyWord.attributes={keyWord_keyword}

# Order class attributes and methods
Order_OrderID: Property = Property(name="OrderID", type=IntegerType)
Order_customerID: Property = Property(name="customerID", type=StringType)
Order_shippingID: Property = Property(name="shippingID", type=StringType)
Order_dateCreated: Property = Property(name="dateCreated", type=StringType)
Order_dateShipped: Property = Property(name="dateShipped", type=StringType)
Order_status: Property = Property(name="status", type=StringType)
Order.attributes={Order_shippingID, Order_status, Order_dateCreated, Order_customerID, Order_OrderID, Order_dateShipped}

# Relationships
ShoppingCart_Customer: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Customer",
    ends={
        Property(name="customer0", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="ShoppingCart_Customer_11", type=ShoppingCart, multiplicity=Multiplicity(0, 1))
    }
)
ShoppingCart_CartItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_CartItem",
    ends={
        Property(name="cartItem2", type=CartItem, multiplicity=Multiplicity(0, 1)),
        Property(name="shoppingCart3", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Product_CartItem: BinaryAssociation = BinaryAssociation(
    name="Product_CartItem",
    ends={
        Property(name="cartItem4", type=CartItem, multiplicity=Multiplicity(1, 1)),
        Property(name="product5", type=Product, multiplicity=Multiplicity(1, 9999))
    }
)
keyWord_Product: BinaryAssociation = BinaryAssociation(
    name="keyWord_Product",
    ends={
        Property(name="product6", type=Product, multiplicity=Multiplicity(1, 1)),
        Property(name="keyWord7", type=keyWord, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order8", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer9", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_vXlREN9YEeeAyLDAJ12_fg",
    types={online_shopping_chart_system_Component, admin_portal_Component, online_shopping_portal_Component, admin_Actor, online_client_Actor, registered_client_Actor, Product_catalog_Component, search_UseCase, Customer, ShoppingCart, Product, CartItem, keyWord, Order},
    associations={ShoppingCart_Customer, ShoppingCart_CartItem, Product_CartItem, keyWord_Product, Customer_Order},
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