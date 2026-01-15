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
esof_homework4_q2_PurchaseOrder = Class(name="esof::homework4::q2::PurchaseOrder")
esof_homework4_q2_Item = Class(name="esof::homework4::q2::Item")
esof_homework4_q2_USAddress = Class(name="esof::homework4::q2::USAddress")

# esof_homework4_q2_PurchaseOrder class attributes and methods
esof_homework4_q2_PurchaseOrder_comment: Property = Property(name="comment", type=StringType)
esof_homework4_q2_PurchaseOrder_orderDate: Property = Property(name="orderDate", type=StringType)
esof_homework4_q2_PurchaseOrder.attributes={esof_homework4_q2_PurchaseOrder_comment, esof_homework4_q2_PurchaseOrder_orderDate}

# esof_homework4_q2_Item class attributes and methods
esof_homework4_q2_Item_productName: Property = Property(name="productName", type=StringType)
esof_homework4_q2_Item_quantity: Property = Property(name="quantity", type=IntegerType)
esof_homework4_q2_Item_USPrice: Property = Property(name="USPrice", type=IntegerType)
esof_homework4_q2_Item_comment: Property = Property(name="comment", type=StringType)
esof_homework4_q2_Item_shipDate: Property = Property(name="shipDate", type=StringType)
esof_homework4_q2_Item_partNum: Property = Property(name="partNum", type=StringType)
esof_homework4_q2_Item.attributes={esof_homework4_q2_Item_quantity, esof_homework4_q2_Item_partNum, esof_homework4_q2_Item_productName, esof_homework4_q2_Item_shipDate, esof_homework4_q2_Item_comment, esof_homework4_q2_Item_USPrice}

# esof_homework4_q2_USAddress class attributes and methods
esof_homework4_q2_USAddress_name: Property = Property(name="name", type=StringType)
esof_homework4_q2_USAddress_street: Property = Property(name="street", type=StringType)
esof_homework4_q2_USAddress_city: Property = Property(name="city", type=StringType)
esof_homework4_q2_USAddress_zip: Property = Property(name="zip", type=IntegerType)
esof_homework4_q2_USAddress_state: Property = Property(name="state", type=StringType)
esof_homework4_q2_USAddress_country: Property = Property(name="country", type=StringType)
esof_homework4_q2_USAddress.attributes={esof_homework4_q2_USAddress_state, esof_homework4_q2_USAddress_street, esof_homework4_q2_USAddress_city, esof_homework4_q2_USAddress_country, esof_homework4_q2_USAddress_name, esof_homework4_q2_USAddress_zip}

# Relationships
items0: BinaryAssociation = BinaryAssociation(
    name="items0",
    ends={
        Property(name="esof_homework4_q2_Item", type=esof_homework4_q2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="esof_homework4_q2_PurchaseOrder", type=esof_homework4_q2_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shipTo1: BinaryAssociation = BinaryAssociation(
    name="shipTo1",
    ends={
        Property(name="esof_homework4_q2_USAddress", type=esof_homework4_q2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="esof_homework4_q2_PurchaseOrder2", type=esof_homework4_q2_USAddress, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
billTo3: BinaryAssociation = BinaryAssociation(
    name="billTo3",
    ends={
        Property(name="esof_homework4_q2_USAddress5", type=esof_homework4_q2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="esof_homework4_q2_PurchaseOrder4", type=esof_homework4_q2_USAddress, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="esof_homework4_q2",
    types={esof_homework4_q2_PurchaseOrder, esof_homework4_q2_Item, esof_homework4_q2_USAddress},
    associations={items0, shipTo1, billTo3},
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