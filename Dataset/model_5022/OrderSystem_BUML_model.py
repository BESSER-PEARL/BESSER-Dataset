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
ordersystem_Order = Class(name="ordersystem::Order")
ordersystem_Customer = Class(name="ordersystem::Customer")
ordersystem_LineItem = Class(name="ordersystem::LineItem")
ordersystem_Product = Class(name="ordersystem::Product")
ordersystem_OrderSystem = Class(name="ordersystem::OrderSystem")
ordersystem_Warehouse = Class(name="ordersystem::Warehouse")
ordersystem_InventoryItem = Class(name="ordersystem::InventoryItem")
ordersystem_Account = Class(name="ordersystem::Account")
ordersystem_Address = Class(name="ordersystem::Address")
ordersystem_special_PreferredCustomer = Class(name="ordersystem::special::PreferredCustomer")
Customer = Class(name="Customer")
ordersystem_special_LimitedEditionProduct = Class(name="ordersystem::special::LimitedEditionProduct")
Product = Class(name="Product")

# ordersystem_Order class attributes and methods
ordersystem_Order_placedOn: Property = Property(name="placedOn", type=StringType)
ordersystem_Order_filledOn: Property = Property(name="filledOn", type=StringType)
ordersystem_Order_completed: Property = Property(name="completed", type=BooleanType)
ordersystem_Order_id: Property = Property(name="id", type=StringType)
ordersystem_Order.attributes={ordersystem_Order_id, ordersystem_Order_filledOn, ordersystem_Order_placedOn, ordersystem_Order_completed}

# ordersystem_Customer class attributes and methods
ordersystem_Customer_lastName: Property = Property(name="lastName", type=StringType)
ordersystem_Customer_firstName: Property = Property(name="firstName", type=StringType)
ordersystem_Customer.attributes={ordersystem_Customer_lastName, ordersystem_Customer_firstName}

# ordersystem_LineItem class attributes and methods
ordersystem_LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
ordersystem_LineItem_discount: Property = Property(name="discount", type=FloatType)
ordersystem_LineItem_m_getCost: Method = Method(name="getCost", parameters={}, type=FloatType)
ordersystem_LineItem.attributes={ordersystem_LineItem_quantity, ordersystem_LineItem_discount}
ordersystem_LineItem.methods={ordersystem_LineItem_m_getCost}

# ordersystem_Product class attributes and methods
ordersystem_Product_name: Property = Property(name="name", type=StringType)
ordersystem_Product_sku: Property = Property(name="sku", type=StringType)
ordersystem_Product_price: Property = Property(name="price", type=FloatType)
ordersystem_Product.attributes={ordersystem_Product_name, ordersystem_Product_price, ordersystem_Product_sku}

# ordersystem_OrderSystem class attributes and methods
ordersystem_OrderSystem_version: Property = Property(name="version", type=IntegerType)
ordersystem_OrderSystem.attributes={ordersystem_OrderSystem_version}

# ordersystem_Warehouse class attributes and methods
ordersystem_Warehouse_name: Property = Property(name="name", type=StringType)
ordersystem_Warehouse.attributes={ordersystem_Warehouse_name}

# ordersystem_InventoryItem class attributes and methods
ordersystem_InventoryItem_inStock: Property = Property(name="inStock", type=IntegerType)
ordersystem_InventoryItem_restockThreshold: Property = Property(name="restockThreshold", type=IntegerType)
ordersystem_InventoryItem_nextStockDate: Property = Property(name="nextStockDate", type=StringType)
ordersystem_InventoryItem.attributes={ordersystem_InventoryItem_nextStockDate, ordersystem_InventoryItem_inStock, ordersystem_InventoryItem_restockThreshold}

# ordersystem_Account class attributes and methods
ordersystem_Account_paymentMethod: Property = Property(name="paymentMethod", type=StringType)
ordersystem_Account_accountNumber: Property = Property(name="accountNumber", type=StringType)
ordersystem_Account.attributes={ordersystem_Account_accountNumber, ordersystem_Account_paymentMethod}

# ordersystem_Address class attributes and methods
ordersystem_Address_number: Property = Property(name="number", type=StringType)
ordersystem_Address_street: Property = Property(name="street", type=StringType)
ordersystem_Address_apartment: Property = Property(name="apartment", type=StringType)
ordersystem_Address_city: Property = Property(name="city", type=StringType)
ordersystem_Address_province: Property = Property(name="province", type=StringType)
ordersystem_Address_postalCode: Property = Property(name="postalCode", type=StringType)
ordersystem_Address_country: Property = Property(name="country", type=StringType)
ordersystem_Address.attributes={ordersystem_Address_number, ordersystem_Address_apartment, ordersystem_Address_country, ordersystem_Address_city, ordersystem_Address_postalCode, ordersystem_Address_street, ordersystem_Address_province}

# ordersystem_special_PreferredCustomer class attributes and methods
ordersystem_special_PreferredCustomer_since: Property = Property(name="since", type=StringType)
ordersystem_special_PreferredCustomer.attributes={ordersystem_special_PreferredCustomer_since}

# Customer class attributes and methods

# ordersystem_special_LimitedEditionProduct class attributes and methods
ordersystem_special_LimitedEditionProduct_availableUntil: Property = Property(name="availableUntil", type=StringType)
ordersystem_special_LimitedEditionProduct.attributes={ordersystem_special_LimitedEditionProduct_availableUntil}

# Product class attributes and methods

# Relationships
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="Customer", type=ordersystem_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=ordersystem_Customer, multiplicity=Multiplicity(0, 1))
    }
)
item1: BinaryAssociation = BinaryAssociation(
    name="item1",
    ends={
        Property(name="LineItem", type=ordersystem_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=ordersystem_LineItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner2: BinaryAssociation = BinaryAssociation(
    name="owner2",
    ends={
        Property(name="OrderSystem", type=ordersystem_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="product", type=ordersystem_OrderSystem, multiplicity=Multiplicity(0, 1))
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="OrderSystem4", type=ordersystem_Warehouse, multiplicity=Multiplicity(1, 1)),
        Property(name="warehouse", type=ordersystem_OrderSystem, multiplicity=Multiplicity(0, 1))
    }
)
owner15: BinaryAssociation = BinaryAssociation(
    name="owner15",
    ends={
        Property(name="Order", type=ordersystem_LineItem, multiplicity=Multiplicity(1, 1)),
        Property(name="item", type=ordersystem_Order, multiplicity=Multiplicity(0, 1))
    }
)
product16: BinaryAssociation = BinaryAssociation(
    name="product16",
    ends={
        Property(name="ordersystem_Product", type=ordersystem_LineItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ordersystem_LineItem", type=ordersystem_Product, multiplicity=Multiplicity(1, 1))
    }
)
Warehouse17: BinaryAssociation = BinaryAssociation(
    name="Warehouse17",
    ends={
        Property(name="Warehouse19", type=ordersystem_InventoryItem, multiplicity=Multiplicity(1, 1)),
        Property(name="item18", type=ordersystem_Warehouse, multiplicity=Multiplicity(0, 1))
    }
)
product20: BinaryAssociation = BinaryAssociation(
    name="product20",
    ends={
        Property(name="ordersystem_Product21", type=ordersystem_InventoryItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ordersystem_InventoryItem", type=ordersystem_Product, multiplicity=Multiplicity(1, 1))
    }
)
owner22: BinaryAssociation = BinaryAssociation(
    name="owner22",
    ends={
        Property(name="OrderSystem23", type=ordersystem_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=ordersystem_OrderSystem, multiplicity=Multiplicity(0, 1))
    }
)
account24: BinaryAssociation = BinaryAssociation(
    name="account24",
    ends={
        Property(name="Account", type=ordersystem_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="owner25", type=ordersystem_Account, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
order26: BinaryAssociation = BinaryAssociation(
    name="order26",
    ends={
        Property(name="Order28", type=ordersystem_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="owner27", type=ordersystem_Order, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
item5: BinaryAssociation = BinaryAssociation(
    name="item5",
    ends={
        Property(name="InventoryItem", type=ordersystem_Warehouse, multiplicity=Multiplicity(1, 1)),
        Property(name="Warehouse", type=ordersystem_InventoryItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location6: BinaryAssociation = BinaryAssociation(
    name="location6",
    ends={
        Property(name="ordersystem_Address", type=ordersystem_Warehouse, multiplicity=Multiplicity(1, 1)),
        Property(name="ordersystem_Warehouse", type=ordersystem_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
customer7: BinaryAssociation = BinaryAssociation(
    name="customer7",
    ends={
        Property(name="Customer9", type=ordersystem_OrderSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="owner8", type=ordersystem_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
product10: BinaryAssociation = BinaryAssociation(
    name="product10",
    ends={
        Property(name="Product", type=ordersystem_OrderSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="owner11", type=ordersystem_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
warehouse12: BinaryAssociation = BinaryAssociation(
    name="warehouse12",
    ends={
        Property(name="Warehouse14", type=ordersystem_OrderSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="owner13", type=ordersystem_Warehouse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner29: BinaryAssociation = BinaryAssociation(
    name="owner29",
    ends={
        Property(name="Customer30", type=ordersystem_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="account", type=ordersystem_Customer, multiplicity=Multiplicity(0, 1))
    }
)
billingAddress31: BinaryAssociation = BinaryAssociation(
    name="billingAddress31",
    ends={
        Property(name="ordersystem_Address32", type=ordersystem_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="ordersystem_Account", type=ordersystem_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
shippingAddress33: BinaryAssociation = BinaryAssociation(
    name="shippingAddress33",
    ends={
        Property(name="ordersystem_Address35", type=ordersystem_Account, multiplicity=Multiplicity(1, 1)),
        Property(name="ordersystem_Account34", type=ordersystem_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_ordersystem_special_PreferredCustomer_Customer = Generalization(general=Customer, specific=ordersystem_special_PreferredCustomer)
gen_ordersystem_special_LimitedEditionProduct_Product = Generalization(general=Product, specific=ordersystem_special_LimitedEditionProduct)

# Domain Model
domain_model = DomainModel(
    name="ordersystem",
    types={ordersystem_Order, ordersystem_Customer, ordersystem_LineItem, ordersystem_Product, ordersystem_OrderSystem, ordersystem_Warehouse, ordersystem_InventoryItem, ordersystem_Account, ordersystem_Address, ordersystem_special_PreferredCustomer, Customer, ordersystem_special_LimitedEditionProduct, Product},
    associations={owner0, item1, owner2, owner3, owner15, product16, Warehouse17, product20, owner22, account24, order26, item5, location6, customer7, product10, warehouse12, owner29, billingAddress31, shippingAddress33},
    generalizations={gen_ordersystem_special_PreferredCustomer_Customer, gen_ordersystem_special_LimitedEditionProduct_Product},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)