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
purchaseOrder_PurchaseOrder = Class(name="purchaseOrder::PurchaseOrder")
purchaseOrder_USAddress = Class(name="purchaseOrder::USAddress")
purchaseOrder_Item = Class(name="purchaseOrder::Item")

# purchaseOrder_PurchaseOrder class attributes and methods
purchaseOrder_PurchaseOrder_comment: Property = Property(name="comment", type=StringType)
purchaseOrder_PurchaseOrder_orderDate: Property = Property(name="orderDate", type=StringType)
purchaseOrder_PurchaseOrder.attributes={purchaseOrder_PurchaseOrder_comment, purchaseOrder_PurchaseOrder_orderDate}

# purchaseOrder_USAddress class attributes and methods
purchaseOrder_USAddress_name: Property = Property(name="name", type=StringType)
purchaseOrder_USAddress_street: Property = Property(name="street", type=StringType)
purchaseOrder_USAddress_city: Property = Property(name="city", type=StringType)
purchaseOrder_USAddress_state: Property = Property(name="state", type=StringType)
purchaseOrder_USAddress_zip: Property = Property(name="zip", type=IntegerType)
purchaseOrder_USAddress_country: Property = Property(name="country", type=StringType)
purchaseOrder_USAddress.attributes={purchaseOrder_USAddress_country, purchaseOrder_USAddress_zip, purchaseOrder_USAddress_state, purchaseOrder_USAddress_street, purchaseOrder_USAddress_name, purchaseOrder_USAddress_city}

# purchaseOrder_Item class attributes and methods
purchaseOrder_Item_productName: Property = Property(name="productName", type=StringType)
purchaseOrder_Item_quantity: Property = Property(name="quantity", type=IntegerType)
purchaseOrder_Item_USPrice: Property = Property(name="USPrice", type=IntegerType)
purchaseOrder_Item_comment: Property = Property(name="comment", type=StringType)
purchaseOrder_Item_shipDate: Property = Property(name="shipDate", type=StringType)
purchaseOrder_Item_partNum: Property = Property(name="partNum", type=StringType)
purchaseOrder_Item.attributes={purchaseOrder_Item_comment, purchaseOrder_Item_productName, purchaseOrder_Item_USPrice, purchaseOrder_Item_shipDate, purchaseOrder_Item_partNum, purchaseOrder_Item_quantity}

# Relationships
shipTo0: BinaryAssociation = BinaryAssociation(
    name="shipTo0",
    ends={
        Property(name="purchaseOrder_USAddress", type=purchaseOrder_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="purchaseOrder_PurchaseOrder", type=purchaseOrder_USAddress, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
billTo1: BinaryAssociation = BinaryAssociation(
    name="billTo1",
    ends={
        Property(name="purchaseOrder_USAddress3", type=purchaseOrder_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="purchaseOrder_PurchaseOrder2", type=purchaseOrder_USAddress, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
items4: BinaryAssociation = BinaryAssociation(
    name="items4",
    ends={
        Property(name="purchaseOrder_Item", type=purchaseOrder_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="purchaseOrder_PurchaseOrder5", type=purchaseOrder_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="purchaseOrder",
    types={purchaseOrder_PurchaseOrder, purchaseOrder_USAddress, purchaseOrder_Item},
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