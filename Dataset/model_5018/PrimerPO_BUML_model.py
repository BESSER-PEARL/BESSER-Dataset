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
ppo_PurchaseOrder = Class(name="ppo::PurchaseOrder")
ppo_USAddress = Class(name="ppo::USAddress")
ppo_Item = Class(name="ppo::Item")

# ppo_PurchaseOrder class attributes and methods
ppo_PurchaseOrder_comment: Property = Property(name="comment", type=StringType)
ppo_PurchaseOrder_orderDate: Property = Property(name="orderDate", type=StringType)
ppo_PurchaseOrder.attributes={ppo_PurchaseOrder_orderDate, ppo_PurchaseOrder_comment}

# ppo_USAddress class attributes and methods
ppo_USAddress_name: Property = Property(name="name", type=StringType)
ppo_USAddress_street: Property = Property(name="street", type=StringType)
ppo_USAddress_city: Property = Property(name="city", type=StringType)
ppo_USAddress_state: Property = Property(name="state", type=StringType)
ppo_USAddress_zip: Property = Property(name="zip", type=IntegerType)
ppo_USAddress_country: Property = Property(name="country", type=StringType)
ppo_USAddress.attributes={ppo_USAddress_country, ppo_USAddress_zip, ppo_USAddress_state, ppo_USAddress_city, ppo_USAddress_street, ppo_USAddress_name}

# ppo_Item class attributes and methods
ppo_Item_productName: Property = Property(name="productName", type=StringType)
ppo_Item_quantity: Property = Property(name="quantity", type=IntegerType)
ppo_Item_USPrice: Property = Property(name="USPrice", type=IntegerType)
ppo_Item_comment: Property = Property(name="comment", type=StringType)
ppo_Item_shipDate: Property = Property(name="shipDate", type=StringType)
ppo_Item_partNum: Property = Property(name="partNum", type=StringType)
ppo_Item.attributes={ppo_Item_quantity, ppo_Item_partNum, ppo_Item_comment, ppo_Item_USPrice, ppo_Item_shipDate, ppo_Item_productName}

# Relationships
shipTo0: BinaryAssociation = BinaryAssociation(
    name="shipTo0",
    ends={
        Property(name="ppo_USAddress", type=ppo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="ppo_PurchaseOrder", type=ppo_USAddress, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
billTo1: BinaryAssociation = BinaryAssociation(
    name="billTo1",
    ends={
        Property(name="ppo_USAddress3", type=ppo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="ppo_PurchaseOrder2", type=ppo_USAddress, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
items4: BinaryAssociation = BinaryAssociation(
    name="items4",
    ends={
        Property(name="ppo_Item", type=ppo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="ppo_PurchaseOrder5", type=ppo_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ppo",
    types={ppo_PurchaseOrder, ppo_USAddress, ppo_Item},
    associations={shipTo0, billTo1, items4},
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