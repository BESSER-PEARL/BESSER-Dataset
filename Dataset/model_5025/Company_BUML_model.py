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
company_Addressable = Class(name="company::Addressable", is_abstract=True)
company_Order = Class(name="company::Order")
company_OrderDetail = Class(name="company::OrderDetail")
company_Product = Class(name="company::Product")
Order = Class(name="Order")
company_Company = Class(name="company::Company")
Addressable = Class(name="Addressable")
company_Category = Class(name="company::Category")
company_Supplier = Class(name="company::Supplier")
company_Customer = Class(name="company::Customer")
company_PurchaseOrder = Class(name="company::PurchaseOrder")
company_SalesOrder = Class(name="company::SalesOrder")

# company_Addressable class attributes and methods
company_Addressable_name: Property = Property(name="name", type=StringType)
company_Addressable_street: Property = Property(name="street", type=StringType)
company_Addressable_city: Property = Property(name="city", type=StringType)
company_Addressable.attributes={company_Addressable_street, company_Addressable_name, company_Addressable_city}

# company_Order class attributes and methods

# company_OrderDetail class attributes and methods
company_OrderDetail_price: Property = Property(name="price", type=FloatType)
company_OrderDetail.attributes={company_OrderDetail_price}

# company_Product class attributes and methods
company_Product_name: Property = Property(name="name", type=StringType)
company_Product_vat: Property = Property(name="vat", type=StringType)
company_Product_description: Property = Property(name="description", type=StringType)
company_Product_price: Property = Property(name="price", type=FloatType)
company_Product.attributes={company_Product_vat, company_Product_description, company_Product_name, company_Product_price}

# Order class attributes and methods

# company_Company class attributes and methods

# Addressable class attributes and methods

# company_Category class attributes and methods
company_Category_name: Property = Property(name="name", type=StringType)
company_Category.attributes={company_Category_name}

# company_Supplier class attributes and methods
company_Supplier_preferred: Property = Property(name="preferred", type=BooleanType)
company_Supplier.attributes={company_Supplier_preferred}

# company_Customer class attributes and methods

# company_PurchaseOrder class attributes and methods
company_PurchaseOrder_date: Property = Property(name="date", type=DateType)
company_PurchaseOrder.attributes={company_PurchaseOrder_date}

# company_SalesOrder class attributes and methods
company_SalesOrder_id: Property = Property(name="id", type=IntegerType)
company_SalesOrder.attributes={company_SalesOrder_id}

# Relationships
purchaseOrders9: BinaryAssociation = BinaryAssociation(
    name="purchaseOrders9",
    ends={
        Property(name="PurchaseOrder", type=company_Supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="supplier", type=company_PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
salesOrders10: BinaryAssociation = BinaryAssociation(
    name="salesOrders10",
    ends={
        Property(name="SalesOrder", type=company_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=company_SalesOrder, multiplicity=Multiplicity(0, 9999))
    }
)
orderDetails11: BinaryAssociation = BinaryAssociation(
    name="orderDetails11",
    ends={
        Property(name="OrderDetail", type=company_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="order", type=company_OrderDetail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
order12: BinaryAssociation = BinaryAssociation(
    name="order12",
    ends={
        Property(name="Order", type=company_OrderDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="orderDetails", type=company_Order, multiplicity=Multiplicity(1, 1))
    }
)
product13: BinaryAssociation = BinaryAssociation(
    name="product13",
    ends={
        Property(name="Product", type=company_OrderDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="orderDetails14", type=company_Product, multiplicity=Multiplicity(0, 1))
    }
)
supplier15: BinaryAssociation = BinaryAssociation(
    name="supplier15",
    ends={
        Property(name="Supplier", type=company_PurchaseOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="purchaseOrders", type=company_Supplier, multiplicity=Multiplicity(1, 1))
    }
)
customer16: BinaryAssociation = BinaryAssociation(
    name="customer16",
    ends={
        Property(name="Customer", type=company_SalesOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="salesOrders", type=company_Customer, multiplicity=Multiplicity(1, 1))
    }
)
categories18: BinaryAssociation = BinaryAssociation(
    name="categories18",
    ends={
        Property(name="company_Category19", type=company_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Category17", type=company_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
products20: BinaryAssociation = BinaryAssociation(
    name="products20",
    ends={
        Property(name="company_Product", type=company_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Category21", type=company_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categories0: BinaryAssociation = BinaryAssociation(
    name="categories0",
    ends={
        Property(name="company_Category", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company", type=company_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
suppliers1: BinaryAssociation = BinaryAssociation(
    name="suppliers1",
    ends={
        Property(name="company_Supplier", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company2", type=company_Supplier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customers3: BinaryAssociation = BinaryAssociation(
    name="customers3",
    ends={
        Property(name="company_Customer", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company4", type=company_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
purchaseOrders5: BinaryAssociation = BinaryAssociation(
    name="purchaseOrders5",
    ends={
        Property(name="company_PurchaseOrder", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company6", type=company_PurchaseOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
salesOrders7: BinaryAssociation = BinaryAssociation(
    name="salesOrders7",
    ends={
        Property(name="company_SalesOrder", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company8", type=company_SalesOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orderDetails22: BinaryAssociation = BinaryAssociation(
    name="orderDetails22",
    ends={
        Property(name="OrderDetail23", type=company_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="product", type=company_OrderDetail, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_company_Supplier_Addressable = Generalization(general=Addressable, specific=company_Supplier)
gen_company_Customer_Addressable = Generalization(general=Addressable, specific=company_Customer)
gen_company_PurchaseOrder_Order = Generalization(general=Order, specific=company_PurchaseOrder)
gen_company_SalesOrder_Order = Generalization(general=Order, specific=company_SalesOrder)
gen_company_Company_Addressable = Generalization(general=Addressable, specific=company_Company)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Addressable, company_Order, company_OrderDetail, company_Product, Order, company_Company, Addressable, company_Category, company_Supplier, company_Customer, company_PurchaseOrder, company_SalesOrder, VAT},
    associations={purchaseOrders9, salesOrders10, orderDetails11, order12, product13, supplier15, customer16, categories18, products20, categories0, suppliers1, customers3, purchaseOrders5, salesOrders7, orderDetails22},
    generalizations={gen_company_Supplier_Addressable, gen_company_Customer_Addressable, gen_company_PurchaseOrder_Order, gen_company_SalesOrder_Order, gen_company_Company_Addressable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)