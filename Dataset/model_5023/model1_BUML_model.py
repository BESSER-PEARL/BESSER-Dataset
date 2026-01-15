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
VAT: Enumeration = Enumeration(
    name="VAT",
    literals={
            EnumerationLiteral(name="vat0"),
			EnumerationLiteral(name="vat7"),
			EnumerationLiteral(name="vat15")
    }
)

# Classes
model1_Product1 = Class(name="model1::Product1")
model1_Address = Class(name="model1::Address")
model1_Company = Class(name="model1::Company")
Address = Class(name="Address")
model1_Category = Class(name="model1::Category")
model1_Supplier = Class(name="model1::Supplier")
model1_Customer = Class(name="model1::Customer")
model1_PurchaseOrder = Class(name="model1::PurchaseOrder")
model1_SalesOrder = Class(name="model1::SalesOrder")
model1_ProductToOrder = Class(name="model1::ProductToOrder")
model1_Order = Class(name="model1::Order", is_abstract=True)
model1_OrderDetail = Class(name="model1::OrderDetail")
Order = Class(name="Order")
model1_OrderAddress = Class(name="model1::OrderAddress")
OrderDetail = Class(name="OrderDetail")

# model1_Product1 class attributes and methods
model1_Product1_name: Property = Property(name="name", type=StringType)
model1_Product1_vat: Property = Property(name="vat", type=StringType)
model1_Product1_otherVATs: Property = Property(name="otherVATs", type=StringType)
model1_Product1_description: Property = Property(name="description", type=StringType)
model1_Product1.attributes={model1_Product1_vat, model1_Product1_description, model1_Product1_otherVATs, model1_Product1_name}

# model1_Address class attributes and methods
model1_Address_name: Property = Property(name="name", type=StringType)
model1_Address_street: Property = Property(name="street", type=StringType)
model1_Address_city: Property = Property(name="city", type=StringType)
model1_Address.attributes={model1_Address_name, model1_Address_city, model1_Address_street}

# model1_Company class attributes and methods

# Address class attributes and methods

# model1_Category class attributes and methods
model1_Category_name: Property = Property(name="name", type=StringType)
model1_Category.attributes={model1_Category_name}

# model1_Supplier class attributes and methods
model1_Supplier_preferred: Property = Property(name="preferred", type=BooleanType)
model1_Supplier.attributes={model1_Supplier_preferred}

# model1_Customer class attributes and methods

# model1_PurchaseOrder class attributes and methods
model1_PurchaseOrder_date: Property = Property(name="date", type=DateType)
model1_PurchaseOrder.attributes={model1_PurchaseOrder_date}

# model1_SalesOrder class attributes and methods
model1_SalesOrder_id: Property = Property(name="id", type=IntegerType)
model1_SalesOrder.attributes={model1_SalesOrder_id}

# model1_ProductToOrder class attributes and methods

# model1_Order class attributes and methods

# model1_OrderDetail class attributes and methods
model1_OrderDetail_price: Property = Property(name="price", type=FloatType)
model1_OrderDetail.attributes={model1_OrderDetail_price}

# Order class attributes and methods

# model1_OrderAddress class attributes and methods
model1_OrderAddress_testAttribute: Property = Property(name="testAttribute", type=BooleanType)
model1_OrderAddress.attributes={model1_OrderAddress_testAttribute}

# OrderDetail class attributes and methods

# Relationships
order14: BinaryAssociation = BinaryAssociation(
    name="order14",
    ends={
        Property(name="Order", type=model1_OrderDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="orderDetails", type=model1_Order, multiplicity=Multiplicity(1, 1))
    }
)
categories0: BinaryAssociation = BinaryAssociation(
    name="categories0",
    ends={
        Property(name="model1_Category", type=model1_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="model1_Company", type=model1_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
suppliers1: BinaryAssociation = BinaryAssociation(
    name="suppliers1",
    ends={
        Property(name="model1_Supplier", type=model1_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="model1_Company2", type=model1_Supplier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customers3: BinaryAssociation = BinaryAssociation(
    name="customers3",
    ends={
        Property(name="model1_Customer", type=model1_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="model1_Company4", type=model1_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
purchaseOrders5: BinaryAssociation = BinaryAssociation(
    name="purchaseOrders5",
    ends={
        Property(name="model1_PurchaseOrder", type=model1_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="model1_Company6", type=model1_PurchaseOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
salesOrders7: BinaryAssociation = BinaryAssociation(
    name="salesOrders7",
    ends={
        Property(name="model1_SalesOrder", type=model1_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="model1_Company8", type=model1_SalesOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
purchaseOrders9: BinaryAssociation = BinaryAssociation(
    name="purchaseOrders9",
    ends={
        Property(name="PurchaseOrder", type=model1_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="supplier", type=model1_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
salesOrders10: BinaryAssociation = BinaryAssociation(
    name="salesOrders10",
    ends={
        Property(name="SalesOrder", type=model1_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=model1_SalesOrder, multiplicity=Multiplicity(0, 9999))
    }
)
orderByProduct11: BinaryAssociation = BinaryAssociation(
    name="orderByProduct11",
    ends={
        Property(name="model1_ProductToOrder", type=model1_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="model1_Customer12", type=model1_ProductToOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orderDetails13: BinaryAssociation = BinaryAssociation(
    name="orderDetails13",
    ends={
        Property(name="OrderDetail", type=model1_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=model1_OrderDetail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key32: BinaryAssociation = BinaryAssociation(
    name="key32",
    ends={
        Property(name="model1_Product134", type=model1_ProductToOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="model1_ProductToOrder33", type=model1_Product1, multiplicity=Multiplicity(0, 1))
    }
)
product15: BinaryAssociation = BinaryAssociation(
    name="product15",
    ends={
        Property(name="Product1", type=model1_OrderDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="orderDetails16", type=model1_Product1, multiplicity=Multiplicity(0, 1))
    }
)
supplier17: BinaryAssociation = BinaryAssociation(
    name="supplier17",
    ends={
        Property(name="Supplier", type=model1_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="purchaseOrders", type=model1_Supplier, multiplicity=Multiplicity(1, 1))
    }
)
salesOrders18: BinaryAssociation = BinaryAssociation(
    name="salesOrders18",
    ends={
        Property(name="SalesOrder20", type=model1_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="purchaseOrders19", type=model1_SalesOrder, multiplicity=Multiplicity(0, 9999))
    }
)
customer21: BinaryAssociation = BinaryAssociation(
    name="customer21",
    ends={
        Property(name="Customer", type=model1_SalesOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="salesOrders", type=model1_Customer, multiplicity=Multiplicity(1, 1))
    }
)
purchaseOrders22: BinaryAssociation = BinaryAssociation(
    name="purchaseOrders22",
    ends={
        Property(name="PurchaseOrder24", type=model1_SalesOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="salesOrders23", type=model1_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
categories26: BinaryAssociation = BinaryAssociation(
    name="categories26",
    ends={
        Property(name="model1_Category27", type=model1_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="model1_Category25", type=model1_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
products28: BinaryAssociation = BinaryAssociation(
    name="products28",
    ends={
        Property(name="model1_Product1", type=model1_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="model1_Category29", type=model1_Product1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orderDetails30: BinaryAssociation = BinaryAssociation(
    name="orderDetails30",
    ends={
        Property(name="OrderDetail31", type=model1_Product1, multiplicity=Multiplicity(1, 1)),
        Property(name="product", type=model1_OrderDetail, multiplicity=Multiplicity(0, 9999))
    }
)
value35: BinaryAssociation = BinaryAssociation(
    name="value35",
    ends={
        Property(name="model1_SalesOrder37", type=model1_ProductToOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="model1_ProductToOrder36", type=model1_SalesOrder, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model1_Company_Address = Generalization(general=Address, specific=model1_Company)
gen_model1_Supplier_Address = Generalization(general=Address, specific=model1_Supplier)
gen_model1_Customer_Address = Generalization(general=Address, specific=model1_Customer)
gen_model1_PurchaseOrder_Order = Generalization(general=Order, specific=model1_PurchaseOrder)
gen_model1_SalesOrder_Order = Generalization(general=Order, specific=model1_SalesOrder)
gen_model1_OrderAddress_Address = Generalization(general=Address, specific=model1_OrderAddress)
gen_model1_OrderAddress_Order = Generalization(general=Order, specific=model1_OrderAddress)
gen_model1_OrderAddress_OrderDetail = Generalization(general=OrderDetail, specific=model1_OrderAddress)

# Domain Model
domain_model = DomainModel(
    name="model1",
    types={model1_Product1, model1_Address, model1_Company, Address, model1_Category, model1_Supplier, model1_Customer, model1_PurchaseOrder, model1_SalesOrder, model1_ProductToOrder, model1_Order, model1_OrderDetail, Order, model1_OrderAddress, OrderDetail, VAT},
    associations={order14, categories0, suppliers1, customers3, purchaseOrders5, salesOrders7, purchaseOrders9, salesOrders10, orderByProduct11, orderDetails13, key32, product15, supplier17, salesOrders18, customer21, purchaseOrders22, categories26, products28, orderDetails30, value35},
    generalizations={gen_model1_Company_Address, gen_model1_Supplier_Address, gen_model1_Customer_Address, gen_model1_PurchaseOrder_Order, gen_model1_SalesOrder_Order, gen_model1_OrderAddress_Address, gen_model1_OrderAddress_Order, gen_model1_OrderAddress_OrderDetail},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)