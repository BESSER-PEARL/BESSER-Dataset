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
Class_ = Class(name="Class")
Location = Class(name="Location")
Packet = Class(name="Packet")
Neighbor = Class(name="Neighbor")
Transportation = Class(name="Transportation")
Sistema_Actor = Class(name="Sistema_Actor")
Base_de_datos_Actor = Class(name="Base_de_datos_Actor")
Cliente_Actor = Class(name="Cliente_Actor")
Sistema2 = Class(name="Sistema2")
Operario_Actor = Class(name="Operario_Actor")

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

# Class class attributes and methods
Class__attribute: Property = Property(name="attribute", type=StringType)
Class_.attributes={Class__attribute}

# Location class attributes and methods

# Packet class attributes and methods

# Neighbor class attributes and methods

# Transportation class attributes and methods

# Sistema_Actor class attributes and methods

# Base_de_datos_Actor class attributes and methods

# Cliente_Actor class attributes and methods

# Sistema2 class attributes and methods

# Operario_Actor class attributes and methods

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
    name="_IILT8F6eEeqK2M3E1LfZ7Q",
    types={ShoppingCartExample_ShoppingCart, ShoppingCartExample_Order, ShoppingCartExample_LineItem, ShoppingCartExample_Account, ShoppingCartExample_Customer, Class_, Location, Packet, Neighbor, Transportation, Sistema_Actor, Base_de_datos_Actor, Cliente_Actor, Sistema2, Operario_Actor},
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