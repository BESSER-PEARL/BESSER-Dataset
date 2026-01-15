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
epo_Item = Class(name="epo::Item")
epo_PurchaseOrder = Class(name="epo::PurchaseOrder")
epo_USAddress = Class(name="epo::USAddress")
Address = Class(name="Address")
epo_Address = Class(name="epo::Address", is_abstract=True)
epo_Customer = Class(name="epo::Customer")
epo_Supplier = Class(name="epo::Supplier")
epo_GlobalAddress = Class(name="epo::GlobalAddress")
GlobalLocation = Class(name="GlobalLocation")
epo_GlobalLocation = Class(name="epo::GlobalLocation")
epo_CanadianAddress = Class(name="epo::CanadianAddress")

# epo_Item class attributes and methods
epo_Item_productName: Property = Property(name="productName", type=StringType)
epo_Item_quantity: Property = Property(name="quantity", type=IntegerType)
epo_Item_USPrice: Property = Property(name="USPrice", type=IntegerType)
epo_Item_comment: Property = Property(name="comment", type=StringType)
epo_Item_shipDate: Property = Property(name="shipDate", type=StringType)
epo_Item_partNum: Property = Property(name="partNum", type=StringType)
epo_Item.attributes={epo_Item_partNum, epo_Item_productName, epo_Item_quantity, epo_Item_comment, epo_Item_shipDate, epo_Item_USPrice}

# epo_PurchaseOrder class attributes and methods
epo_PurchaseOrder_comment: Property = Property(name="comment", type=StringType)
epo_PurchaseOrder_orderDate: Property = Property(name="orderDate", type=StringType)
epo_PurchaseOrder_status: Property = Property(name="status", type=StringType)
epo_PurchaseOrder_totalAmount: Property = Property(name="totalAmount", type=IntegerType)
epo_PurchaseOrder.attributes={epo_PurchaseOrder_comment, epo_PurchaseOrder_totalAmount, epo_PurchaseOrder_status, epo_PurchaseOrder_orderDate}

# epo_USAddress class attributes and methods
epo_USAddress_street: Property = Property(name="street", type=StringType)
epo_USAddress_city: Property = Property(name="city", type=StringType)
epo_USAddress_state: Property = Property(name="state", type=StringType)
epo_USAddress_zip: Property = Property(name="zip", type=IntegerType)
epo_USAddress.attributes={epo_USAddress_city, epo_USAddress_zip, epo_USAddress_state, epo_USAddress_street}

# Address class attributes and methods

# epo_Address class attributes and methods
epo_Address_name: Property = Property(name="name", type=StringType)
epo_Address_country: Property = Property(name="country", type=StringType)
epo_Address.attributes={epo_Address_country, epo_Address_name}

# epo_Customer class attributes and methods
epo_Customer_customerID: Property = Property(name="customerID", type=IntegerType)
epo_Customer.attributes={epo_Customer_customerID}

# epo_Supplier class attributes and methods
epo_Supplier_name: Property = Property(name="name", type=StringType)
epo_Supplier.attributes={epo_Supplier_name}

# epo_GlobalAddress class attributes and methods
epo_GlobalAddress_location: Property = Property(name="location", type=StringType)
epo_GlobalAddress.attributes={epo_GlobalAddress_location}

# GlobalLocation class attributes and methods

# epo_GlobalLocation class attributes and methods
epo_GlobalLocation_countryCode: Property = Property(name="countryCode", type=IntegerType)
epo_GlobalLocation.attributes={epo_GlobalLocation_countryCode}

# epo_CanadianAddress class attributes and methods
epo_CanadianAddress_street: Property = Property(name="street", type=StringType)
epo_CanadianAddress_city: Property = Property(name="city", type=StringType)
epo_CanadianAddress_province: Property = Property(name="province", type=StringType)
epo_CanadianAddress_postalCode: Property = Property(name="postalCode", type=StringType)
epo_CanadianAddress.attributes={epo_CanadianAddress_province, epo_CanadianAddress_postalCode, epo_CanadianAddress_city, epo_CanadianAddress_street}

# Relationships
order0: BinaryAssociation = BinaryAssociation(
    name="order0",
    ends={
        Property(name="PurchaseOrder", type=epo_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="items", type=epo_PurchaseOrder, multiplicity=Multiplicity(1, 1))
    }
)
orders11: BinaryAssociation = BinaryAssociation(
    name="orders11",
    ends={
        Property(name="epo_PurchaseOrder13", type=epo_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo_Supplier12", type=epo_PurchaseOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pendingOrders14: BinaryAssociation = BinaryAssociation(
    name="pendingOrders14",
    ends={
        Property(name="epo_PurchaseOrder16", type=epo_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo_Supplier15", type=epo_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
shippedOrders17: BinaryAssociation = BinaryAssociation(
    name="shippedOrders17",
    ends={
        Property(name="epo_PurchaseOrder19", type=epo_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo_Supplier18", type=epo_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
items1: BinaryAssociation = BinaryAssociation(
    name="items1",
    ends={
        Property(name="Item", type=epo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=epo_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
billTo2: BinaryAssociation = BinaryAssociation(
    name="billTo2",
    ends={
        Property(name="epo_Address", type=epo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="epo_PurchaseOrder", type=epo_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
shipTo3: BinaryAssociation = BinaryAssociation(
    name="shipTo3",
    ends={
        Property(name="epo_Address5", type=epo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="epo_PurchaseOrder4", type=epo_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
customer6: BinaryAssociation = BinaryAssociation(
    name="customer6",
    ends={
        Property(name="Customer", type=epo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="orders", type=epo_Customer, multiplicity=Multiplicity(1, 1))
    }
)
previousOrder8: BinaryAssociation = BinaryAssociation(
    name="previousOrder8",
    ends={
        Property(name="epo_PurchaseOrder9", type=epo_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="epo_PurchaseOrder7", type=epo_PurchaseOrder, multiplicity=Multiplicity(0, 1))
    }
)
customers10: BinaryAssociation = BinaryAssociation(
    name="customers10",
    ends={
        Property(name="epo_Customer", type=epo_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="epo_Supplier", type=epo_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orders20: BinaryAssociation = BinaryAssociation(
    name="orders20",
    ends={
        Property(name="PurchaseOrder21", type=epo_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=epo_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_epo_USAddress_Address = Generalization(general=Address, specific=epo_USAddress)
gen_epo_GlobalAddress_Address = Generalization(general=Address, specific=epo_GlobalAddress)
gen_epo_GlobalAddress_GlobalLocation = Generalization(general=GlobalLocation, specific=epo_GlobalAddress)
gen_epo_CanadianAddress_Address = Generalization(general=Address, specific=epo_CanadianAddress)

# Domain Model
domain_model = DomainModel(
    name="epo",
    types={epo_Item, epo_PurchaseOrder, epo_USAddress, Address, epo_Address, epo_Customer, epo_Supplier, epo_GlobalAddress, GlobalLocation, epo_GlobalLocation, epo_CanadianAddress, OrderStatus},
    associations={order0, orders11, pendingOrders14, shippedOrders17, items1, billTo2, shipTo3, customer6, previousOrder8, customers10, orders20},
    generalizations={gen_epo_USAddress_Address, gen_epo_GlobalAddress_Address, gen_epo_GlobalAddress_GlobalLocation, gen_epo_CanadianAddress_Address},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)