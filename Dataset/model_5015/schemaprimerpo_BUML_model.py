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
schemaprimerpo_DocumentRoot = Class(name="schemaprimerpo::DocumentRoot")
schemaprimerpo_EStringToStringMapEntry = Class(name="schemaprimerpo::EStringToStringMapEntry")
schemaprimerpo_PurchaseOrder = Class(name="schemaprimerpo::PurchaseOrder")
schemaprimerpo_Item = Class(name="schemaprimerpo::Item")
schemaprimerpo_USAddress = Class(name="schemaprimerpo::USAddress")

# schemaprimerpo_DocumentRoot class attributes and methods
schemaprimerpo_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
schemaprimerpo_DocumentRoot_comment: Property = Property(name="comment", type=StringType)
schemaprimerpo_DocumentRoot.attributes={schemaprimerpo_DocumentRoot_mixed, schemaprimerpo_DocumentRoot_comment}

# schemaprimerpo_EStringToStringMapEntry class attributes and methods

# schemaprimerpo_PurchaseOrder class attributes and methods
schemaprimerpo_PurchaseOrder_comment: Property = Property(name="comment", type=StringType)
schemaprimerpo_PurchaseOrder_orderDate: Property = Property(name="orderDate", type=StringType)
schemaprimerpo_PurchaseOrder.attributes={schemaprimerpo_PurchaseOrder_orderDate, schemaprimerpo_PurchaseOrder_comment}

# schemaprimerpo_Item class attributes and methods
schemaprimerpo_Item_productName: Property = Property(name="productName", type=StringType)
schemaprimerpo_Item_quantity: Property = Property(name="quantity", type=StringType)
schemaprimerpo_Item_partNum: Property = Property(name="partNum", type=StringType)
schemaprimerpo_Item_uSPrice: Property = Property(name="uSPrice", type=StringType)
schemaprimerpo_Item_comment: Property = Property(name="comment", type=StringType)
schemaprimerpo_Item_shipDate: Property = Property(name="shipDate", type=StringType)
schemaprimerpo_Item.attributes={schemaprimerpo_Item_partNum, schemaprimerpo_Item_productName, schemaprimerpo_Item_shipDate, schemaprimerpo_Item_uSPrice, schemaprimerpo_Item_quantity, schemaprimerpo_Item_comment}

# schemaprimerpo_USAddress class attributes and methods
schemaprimerpo_USAddress_name: Property = Property(name="name", type=StringType)
schemaprimerpo_USAddress_street: Property = Property(name="street", type=StringType)
schemaprimerpo_USAddress_city: Property = Property(name="city", type=StringType)
schemaprimerpo_USAddress_state: Property = Property(name="state", type=StringType)
schemaprimerpo_USAddress_zip: Property = Property(name="zip", type=StringType)
schemaprimerpo_USAddress_country: Property = Property(name="country", type=StringType)
schemaprimerpo_USAddress.attributes={schemaprimerpo_USAddress_zip, schemaprimerpo_USAddress_state, schemaprimerpo_USAddress_name, schemaprimerpo_USAddress_city, schemaprimerpo_USAddress_street, schemaprimerpo_USAddress_country}

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="schemaprimerpo_EStringToStringMapEntry", type=schemaprimerpo_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="schemaprimerpo_DocumentRoot", type=schemaprimerpo_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="schemaprimerpo_EStringToStringMapEntry3", type=schemaprimerpo_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="schemaprimerpo_DocumentRoot2", type=schemaprimerpo_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
order4: BinaryAssociation = BinaryAssociation(
    name="order4",
    ends={
        Property(name="schemaprimerpo_PurchaseOrder", type=schemaprimerpo_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="schemaprimerpo_DocumentRoot5", type=schemaprimerpo_PurchaseOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shipTo6: BinaryAssociation = BinaryAssociation(
    name="shipTo6",
    ends={
        Property(name="schemaprimerpo_USAddress", type=schemaprimerpo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="schemaprimerpo_PurchaseOrder7", type=schemaprimerpo_USAddress, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
billTo8: BinaryAssociation = BinaryAssociation(
    name="billTo8",
    ends={
        Property(name="schemaprimerpo_USAddress10", type=schemaprimerpo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="schemaprimerpo_PurchaseOrder9", type=schemaprimerpo_USAddress, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
items11: BinaryAssociation = BinaryAssociation(
    name="items11",
    ends={
        Property(name="schemaprimerpo_Item", type=schemaprimerpo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="schemaprimerpo_PurchaseOrder12", type=schemaprimerpo_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="schemaprimerpo",
    types={schemaprimerpo_DocumentRoot, schemaprimerpo_EStringToStringMapEntry, schemaprimerpo_PurchaseOrder, schemaprimerpo_Item, schemaprimerpo_USAddress},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, order4, shipTo6, billTo8, items11},
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