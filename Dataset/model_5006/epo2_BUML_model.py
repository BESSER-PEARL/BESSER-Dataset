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
epo2_Item = Class(name="epo2::Item")
epo2_Address = Class(name="epo2::Address", is_abstract=True)
epo2_Supplier = Class(name="epo2::Supplier")
epo2_PurchaseOrder = Class(name="epo2::PurchaseOrder")
epo2_Customer = Class(name="epo2::Customer")
epo2_USAddress = Class(name="epo2::USAddress")
Address = Class(name="Address")
epo2_GlobalAddress = Class(name="epo2::GlobalAddress")
GlobalLocation = Class(name="GlobalLocation")
epo2_GlobalLocation = Class(name="epo2::GlobalLocation")

# epo2_Item class attributes and methods
epo2_Item_productName: Property = Property(name="productName", type=StringType)
epo2_Item_quantity: Property = Property(name="quantity", type=IntegerType)
epo2_Item_usPrice: Property = Property(name="usPrice", type=IntegerType)
epo2_Item_comment: Property = Property(name="comment", type=StringType)
epo2_Item_shipDate: Property = Property(name="shipDate", type=DateType)
epo2_Item_partNum: Property = Property(name="partNum", type=StringType)
epo2_Item.attributes={epo2_Item_productName, epo2_Item_shipDate, epo2_Item_quantity, epo2_Item_partNum, epo2_Item_usPrice, epo2_Item_comment}

# epo2_Address class attributes and methods
epo2_Address_name: Property = Property(name="name", type=StringType)
epo2_Address_country: Property = Property(name="country", type=StringType)
epo2_Address.attributes={epo2_Address_country, epo2_Address_name}

# epo2_Supplier class attributes and methods
epo2_Supplier_name: Property = Property(name="name", type=StringType)
epo2_Supplier.attributes={epo2_Supplier_name}

# epo2_PurchaseOrder class attributes and methods
epo2_PurchaseOrder_comment: Property = Property(name="comment", type=StringType)
epo2_PurchaseOrder_orderDate: Property = Property(name="orderDate", type=DateType)
epo2_PurchaseOrder_status: Property = Property(name="status", type=StringType)
epo2_PurchaseOrder_totalAmount: Property = Property(name="totalAmount", type=IntegerType)
epo2_PurchaseOrder.attributes={epo2_PurchaseOrder_orderDate, epo2_PurchaseOrder_comment, epo2_PurchaseOrder_status, epo2_PurchaseOrder_totalAmount}

# epo2_Customer class attributes and methods
epo2_Customer_customerID: Property = Property(name="customerID", type=IntegerType)
epo2_Customer.attributes={epo2_Customer_customerID}

# epo2_USAddress class attributes and methods
epo2_USAddress_street: Property = Property(name="street", type=StringType)
epo2_USAddress_city: Property = Property(name="city", type=StringType)
epo2_USAddress_state: Property = Property(name="state", type=StringType)
epo2_USAddress_zip: Property = Property(name="zip", type=StringType)
epo2_USAddress.attributes={epo2_USAddress_street, epo2_USAddress_zip, epo2_USAddress_state, epo2_USAddress_city}

# Address class attributes and methods

# epo2_GlobalAddress class attributes and methods
epo2_GlobalAddress_location: Property = Property(name="location", type=StringType)
epo2_GlobalAddress.attributes={epo2_GlobalAddress_location}

# GlobalLocation class attributes and methods

# epo2_GlobalLocation class attributes and methods
epo2_GlobalLocation_countryCode: Property = Property(name="countryCode", type=IntegerType)
epo2_GlobalLocation.attributes={epo2_GlobalLocation_countryCode}

# Relationships
previousOrder11: BinaryAssociation = BinaryAssociation(
    name="previousOrder11",
    ends={
        Property(name="epo2_PurchaseOrder10", type=epo2_PurchaseOrder, multiplicity=Multiplicity(0, 1)),
        Property(name="epo2_PurchaseOrder12", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1))
    }
)
items13: BinaryAssociation = BinaryAssociation(
    name="items13",
    ends={
        Property(name="Item", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=epo2_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
billTo14: BinaryAssociation = BinaryAssociation(
    name="billTo14",
    ends={
        Property(name="epo2_Address", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_PurchaseOrder15", type=epo2_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
shipTo16: BinaryAssociation = BinaryAssociation(
    name="shipTo16",
    ends={
        Property(name="epo2_Address18", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_PurchaseOrder17", type=epo2_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
orders19: BinaryAssociation = BinaryAssociation(
    name="orders19",
    ends={
        Property(name="PurchaseOrder", type=epo2_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=epo2_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
order20: BinaryAssociation = BinaryAssociation(
    name="order20",
    ends={
        Property(name="PurchaseOrder21", type=epo2_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="items", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1))
    }
)
orders0: BinaryAssociation = BinaryAssociation(
    name="orders0",
    ends={
        Property(name="epo2_PurchaseOrder", type=epo2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_Supplier", type=epo2_PurchaseOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pendingOrders1: BinaryAssociation = BinaryAssociation(
    name="pendingOrders1",
    ends={
        Property(name="epo2_PurchaseOrder3", type=epo2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_Supplier2", type=epo2_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
shippedOrders4: BinaryAssociation = BinaryAssociation(
    name="shippedOrders4",
    ends={
        Property(name="epo2_PurchaseOrder6", type=epo2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_Supplier5", type=epo2_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
customers7: BinaryAssociation = BinaryAssociation(
    name="customers7",
    ends={
        Property(name="epo2_Customer", type=epo2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_Supplier8", type=epo2_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customer9: BinaryAssociation = BinaryAssociation(
    name="customer9",
    ends={
        Property(name="Customer", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="orders", type=epo2_Customer, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_epo2_USAddress_Address = Generalization(general=Address, specific=epo2_USAddress)
gen_epo2_GlobalAddress_Address = Generalization(general=Address, specific=epo2_GlobalAddress)
gen_epo2_GlobalAddress_GlobalLocation = Generalization(general=GlobalLocation, specific=epo2_GlobalAddress)

# Domain Model
domain_model = DomainModel(
    name="epo2",
    types={epo2_Item, epo2_Address, epo2_Supplier, epo2_PurchaseOrder, epo2_Customer, epo2_USAddress, Address, epo2_GlobalAddress, GlobalLocation, epo2_GlobalLocation, OrderStatus},
    associations={previousOrder11, items13, billTo14, shipTo16, orders19, order20, orders0, pendingOrders1, shippedOrders4, customers7, customer9},
    generalizations={gen_epo2_USAddress_Address, gen_epo2_GlobalAddress_Address, gen_epo2_GlobalAddress_GlobalLocation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)