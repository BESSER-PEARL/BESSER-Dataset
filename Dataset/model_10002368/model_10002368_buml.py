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
ShoppingCartExample_ShoppingCart = Class(name="ShoppingCartExample_ShoppingCart")
ShoppingCartExample_Order = Class(name="ShoppingCartExample_Order")
ShoppingCartExample_LineItem = Class(name="ShoppingCartExample_LineItem")
ShoppingCartExample_Account = Class(name="ShoppingCartExample_Account")
ShoppingCartExample_Customer = Class(name="ShoppingCartExample_Customer")

# ShoppingCartExample_ShoppingCart class attributes and methods
ShoppingCartExample_ShoppingCart_creationDate: Property = Property(name="creationDate", type=DateType)
ShoppingCartExample_ShoppingCart.attributes={ShoppingCartExample_ShoppingCart_creationDate}

# ShoppingCartExample_Order class attributes and methods
ShoppingCartExample_Order_id: Property = Property(name="id", type=IntegerType)
ShoppingCartExample_Order.attributes={ShoppingCartExample_Order_id}

# ShoppingCartExample_LineItem class attributes and methods
ShoppingCartExample_LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
ShoppingCartExample_LineItem_price: Property = Property(name="price", type=IntegerType)
ShoppingCartExample_LineItem.attributes={ShoppingCartExample_LineItem_price, ShoppingCartExample_LineItem_quantity}

# ShoppingCartExample_Account class attributes and methods
ShoppingCartExample_Account_id: Property = Property(name="id", type=IntegerType)
ShoppingCartExample_Account.attributes={ShoppingCartExample_Account_id}

# ShoppingCartExample_Customer class attributes and methods

# Relationships
Order_Line: BinaryAssociation = BinaryAssociation(
    name="Order_Line",
    ends={
        Property(name="items0", type=ShoppingCartExample_LineItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="order1", type=ShoppingCartExample_Order, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_Order: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_Order",
    ends={
        Property(name="order2", type=ShoppingCartExample_Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="c3", type=ShoppingCartExample_ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart4", type=ShoppingCartExample_ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account5", type=ShoppingCartExample_Account, multiplicity=Multiplicity(1, 1))
    }
)
Account_Customer: BinaryAssociation = BinaryAssociation(
    name="Account_Customer",
    ends={
        Property(name="customer6", type=ShoppingCartExample_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="account7", type=ShoppingCartExample_Account, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ac2bd1cf_0780_46a3_b691_131d75be9260",
    types={ShoppingCartExample_ShoppingCart, ShoppingCartExample_Order, ShoppingCartExample_LineItem, ShoppingCartExample_Account, ShoppingCartExample_Customer},
    associations={Order_Line, ShoppingCart_Order, Account_ShoppingCart, Account_Customer},
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