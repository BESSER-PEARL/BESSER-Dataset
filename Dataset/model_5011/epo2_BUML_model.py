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
epo2_PurchaseOrder = Class(name="epo2::PurchaseOrder")
epo2_USAddress = Class(name="epo2::USAddress")
Address = Class(name="Address")
epo2_Address = Class(name="epo2::Address", is_abstract=True)
epo2_Customer = Class(name="epo2::Customer")
epo2_Supplier = Class(name="epo2::Supplier")
epo2_GlobalAddress = Class(name="epo2::GlobalAddress")
GlobalLocation = Class(name="GlobalLocation")
epo2_GlobalLocation = Class(name="epo2::GlobalLocation")

# epo2_Item class attributes and methods
epo2_Item_productName: Property = Property(name="productName", type=StringType)
epo2_Item_quantity: Property = Property(name="quantity", type=IntegerType)
epo2_Item_USPrice: Property = Property(name="USPrice", type=IntegerType)
epo2_Item_comment: Property = Property(name="comment", type=StringType)
epo2_Item_shipDate: Property = Property(name="shipDate", type=StringType)
epo2_Item_partNum: Property = Property(name="partNum", type=StringType)
epo2_Item.attributes={epo2_Item_productName, epo2_Item_quantity, epo2_Item_USPrice, epo2_Item_comment, epo2_Item_partNum, epo2_Item_shipDate}

# epo2_PurchaseOrder class attributes and methods
epo2_PurchaseOrder_comment: Property = Property(name="comment", type=StringType)
epo2_PurchaseOrder_orderDate: Property = Property(name="orderDate", type=StringType)
epo2_PurchaseOrder_status: Property = Property(name="status", type=StringType)
epo2_PurchaseOrder_totalAmount: Property = Property(name="totalAmount", type=IntegerType)
epo2_PurchaseOrder.attributes={epo2_PurchaseOrder_status, epo2_PurchaseOrder_comment, epo2_PurchaseOrder_totalAmount, epo2_PurchaseOrder_orderDate}

# epo2_USAddress class attributes and methods
epo2_USAddress_street: Property = Property(name="street", type=StringType)
epo2_USAddress_city: Property = Property(name="city", type=StringType)
epo2_USAddress_state: Property = Property(name="state", type=StringType)
epo2_USAddress_zip: Property = Property(name="zip", type=IntegerType)
epo2_USAddress.attributes={epo2_USAddress_state, epo2_USAddress_city, epo2_USAddress_street, epo2_USAddress_zip}

# Address class attributes and methods

# epo2_Address class attributes and methods
epo2_Address_name: Property = Property(name="name", type=StringType)
epo2_Address_country: Property = Property(name="country", type=StringType)
epo2_Address.attributes={epo2_Address_name, epo2_Address_country}

# epo2_Customer class attributes and methods
epo2_Customer_customerID: Property = Property(name="customerID", type=IntegerType)
epo2_Customer.attributes={epo2_Customer_customerID}

# epo2_Supplier class attributes and methods
epo2_Supplier_name: Property = Property(name="name", type=StringType)
epo2_Supplier.attributes={epo2_Supplier_name}

# epo2_GlobalAddress class attributes and methods
epo2_GlobalAddress_location: Property = Property(name="location", type=StringType)
epo2_GlobalAddress.attributes={epo2_GlobalAddress_location}

# GlobalLocation class attributes and methods

# epo2_GlobalLocation class attributes and methods
epo2_GlobalLocation_countryCode: Property = Property(name="countryCode", type=IntegerType)
epo2_GlobalLocation.attributes={epo2_GlobalLocation_countryCode}

# Relationships
order0: BinaryAssociation = BinaryAssociation(
    name="order0",
    ends={
        Property(name="PurchaseOrder", type=epo2_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="items", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1))
    }
)
items1: BinaryAssociation = BinaryAssociation(
    name="items1",
    ends={
        Property(name="Item", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=epo2_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
billTo2: BinaryAssociation = BinaryAssociation(
    name="billTo2",
    ends={
        Property(name="epo2_Address", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_PurchaseOrder", type=epo2_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
shipTo3: BinaryAssociation = BinaryAssociation(
    name="shipTo3",
    ends={
        Property(name="epo2_Address5", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_PurchaseOrder4", type=epo2_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
customer6: BinaryAssociation = BinaryAssociation(
    name="customer6",
    ends={
        Property(name="Customer", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="orders", type=epo2_Customer, multiplicity=Multiplicity(1, 1))
    }
)
previousOrder8: BinaryAssociation = BinaryAssociation(
    name="previousOrder8",
    ends={
        Property(name="epo2_PurchaseOrder9", type=epo2_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_PurchaseOrder7", type=epo2_PurchaseOrder, multiplicity=Multiplicity(0, 1))
    }
)
customers10: BinaryAssociation = BinaryAssociation(
    name="customers10",
    ends={
        Property(name="epo2_Customer", type=epo2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_Supplier", type=epo2_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orders11: BinaryAssociation = BinaryAssociation(
    name="orders11",
    ends={
        Property(name="epo2_PurchaseOrder13", type=epo2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_Supplier12", type=epo2_PurchaseOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pendingOrders14: BinaryAssociation = BinaryAssociation(
    name="pendingOrders14",
    ends={
        Property(name="epo2_PurchaseOrder16", type=epo2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_Supplier15", type=epo2_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
shippedOrders17: BinaryAssociation = BinaryAssociation(
    name="shippedOrders17",
    ends={
        Property(name="epo2_PurchaseOrder19", type=epo2_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo2_Supplier18", type=epo2_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
orders20: BinaryAssociation = BinaryAssociation(
    name="orders20",
    ends={
        Property(name="PurchaseOrder21", type=epo2_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=epo2_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_epo2_USAddress_Address = Generalization(general=Address, specific=epo2_USAddress)
gen_epo2_GlobalAddress_Address = Generalization(general=Address, specific=epo2_GlobalAddress)
gen_epo2_GlobalAddress_GlobalLocation = Generalization(general=GlobalLocation, specific=epo2_GlobalAddress)

# Domain Model
domain_model = DomainModel(
    name="epo2",
    types={epo2_Item, epo2_PurchaseOrder, epo2_USAddress, Address, epo2_Address, epo2_Customer, epo2_Supplier, epo2_GlobalAddress, GlobalLocation, epo2_GlobalLocation, OrderStatus},
    associations={order0, items1, billTo2, shipTo3, customer6, previousOrder8, customers10, orders11, pendingOrders14, shippedOrders17, orders20},
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