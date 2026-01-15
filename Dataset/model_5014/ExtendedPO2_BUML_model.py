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

# Enumerations
OrderStatus: Enumeration = Enumeration(
    name="OrderStatus",
    literals={
            EnumerationLiteral(name="Pending"),
			EnumerationLiteral(name="BackOrder"),
			EnumerationLiteral(name="Complete")
    }
)

# Classes
extendedPO2_Item = Class(name="extendedPO2::Item")
extendedPO2_Address = Class(name="extendedPO2::Address", is_abstract=True)
extendedPO2_Customer = Class(name="extendedPO2::Customer")
extendedPO2_USAddress = Class(name="extendedPO2::USAddress")
Address = Class(name="Address")
extendedPO2_PurchaseOrder = Class(name="extendedPO2::PurchaseOrder")
extendedPO2_Supplier = Class(name="extendedPO2::Supplier")
extendedPO2_GlobalAddress = Class(name="extendedPO2::GlobalAddress")

# extendedPO2_Item class attributes and methods
extendedPO2_Item_productName: Property = Property(name="productName", type=StringType)
extendedPO2_Item_quantity: Property = Property(name="quantity", type=IntegerType)
extendedPO2_Item_USPrice: Property = Property(name="USPrice", type=IntegerType)
extendedPO2_Item_comment: Property = Property(name="comment", type=StringType)
extendedPO2_Item_shipDate: Property = Property(name="shipDate", type=StringType)
extendedPO2_Item_partNum: Property = Property(name="partNum", type=StringType)
extendedPO2_Item.attributes={extendedPO2_Item_partNum, extendedPO2_Item_USPrice, extendedPO2_Item_quantity, extendedPO2_Item_shipDate, extendedPO2_Item_productName, extendedPO2_Item_comment}

# extendedPO2_Address class attributes and methods
extendedPO2_Address_name: Property = Property(name="name", type=StringType)
extendedPO2_Address_country: Property = Property(name="country", type=StringType)
extendedPO2_Address.attributes={extendedPO2_Address_country, extendedPO2_Address_name}

# extendedPO2_Customer class attributes and methods
extendedPO2_Customer_customerID: Property = Property(name="customerID", type=IntegerType)
extendedPO2_Customer.attributes={extendedPO2_Customer_customerID}

# extendedPO2_USAddress class attributes and methods
extendedPO2_USAddress_street: Property = Property(name="street", type=StringType)
extendedPO2_USAddress_city: Property = Property(name="city", type=StringType)
extendedPO2_USAddress_state: Property = Property(name="state", type=StringType)
extendedPO2_USAddress_zip: Property = Property(name="zip", type=IntegerType)
extendedPO2_USAddress.attributes={extendedPO2_USAddress_city, extendedPO2_USAddress_zip, extendedPO2_USAddress_state, extendedPO2_USAddress_street}

# Address class attributes and methods

# extendedPO2_PurchaseOrder class attributes and methods
extendedPO2_PurchaseOrder_totalAmount: Property = Property(name="totalAmount", type=IntegerType)
extendedPO2_PurchaseOrder_comment: Property = Property(name="comment", type=StringType)
extendedPO2_PurchaseOrder_orderDate: Property = Property(name="orderDate", type=StringType)
extendedPO2_PurchaseOrder_status: Property = Property(name="status", type=StringType)
extendedPO2_PurchaseOrder.attributes={extendedPO2_PurchaseOrder_orderDate, extendedPO2_PurchaseOrder_totalAmount, extendedPO2_PurchaseOrder_status, extendedPO2_PurchaseOrder_comment}

# extendedPO2_Supplier class attributes and methods
extendedPO2_Supplier_name: Property = Property(name="name", type=StringType)
extendedPO2_Supplier.attributes={extendedPO2_Supplier_name}

# extendedPO2_GlobalAddress class attributes and methods
extendedPO2_GlobalAddress_location: Property = Property(name="location", type=StringType)
extendedPO2_GlobalAddress.attributes={extendedPO2_GlobalAddress_location}

# Relationships
items0: BinaryAssociation = BinaryAssociation(
    name="items0",
    ends={
        Property(name="Item", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=extendedPO2_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
billTo1: BinaryAssociation = BinaryAssociation(
    name="billTo1",
    ends={
        Property(name="extendedPO2_Address", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPO2_PurchaseOrder", type=extendedPO2_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
shipTo2: BinaryAssociation = BinaryAssociation(
    name="shipTo2",
    ends={
        Property(name="extendedPO2_Address4", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPO2_PurchaseOrder3", type=extendedPO2_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
previousOrder6: BinaryAssociation = BinaryAssociation(
    name="previousOrder6",
    ends={
        Property(name="extendedPO2_PurchaseOrder7", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPO2_PurchaseOrder5", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(0, 1))
    }
)
customer8: BinaryAssociation = BinaryAssociation(
    name="customer8",
    ends={
        Property(name="Customer", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="orders", type=extendedPO2_Customer, multiplicity=Multiplicity(1, 1))
    }
)
order9: BinaryAssociation = BinaryAssociation(
    name="order9",
    ends={
        Property(name="PurchaseOrder", type=extendedPO2_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="items", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(0, 1))
    }
)
orders12: BinaryAssociation = BinaryAssociation(
    name="orders12",
    ends={
        Property(name="extendedPO2_PurchaseOrder13", type=extendedPO2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPO2_Supplier", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customers14: BinaryAssociation = BinaryAssociation(
    name="customers14",
    ends={
        Property(name="extendedPO2_Customer", type=extendedPO2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPO2_Supplier15", type=extendedPO2_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pendingOrders16: BinaryAssociation = BinaryAssociation(
    name="pendingOrders16",
    ends={
        Property(name="extendedPO2_PurchaseOrder18", type=extendedPO2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPO2_Supplier17", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
shippedOrders19: BinaryAssociation = BinaryAssociation(
    name="shippedOrders19",
    ends={
        Property(name="extendedPO2_PurchaseOrder21", type=extendedPO2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPO2_Supplier20", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
orders10: BinaryAssociation = BinaryAssociation(
    name="orders10",
    ends={
        Property(name="PurchaseOrder11", type=extendedPO2_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=extendedPO2_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_extendedPO2_USAddress_Address = Generalization(general=Address, specific=extendedPO2_USAddress)
gen_extendedPO2_GlobalAddress_Address = Generalization(general=Address, specific=extendedPO2_GlobalAddress)

# Domain Model
domain_model = DomainModel(
    name="extendedPO2",
    types={extendedPO2_Item, extendedPO2_Address, extendedPO2_Customer, extendedPO2_USAddress, Address, extendedPO2_PurchaseOrder, extendedPO2_Supplier, extendedPO2_GlobalAddress, OrderStatus},
    associations={items0, billTo1, shipTo2, previousOrder6, customer8, order9, orders12, customers14, pendingOrders16, shippedOrders19, orders10},
    generalizations={gen_extendedPO2_USAddress_Address, gen_extendedPO2_GlobalAddress_Address},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)