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
            
    }
)

real: Enumeration = Enumeration(
    name="real",
    literals={
            
    }
)

# Classes
Portal = Class(name="Portal")
Customer = Class(name="Customer")
Order = Class(name="Order")
OrderDetail = Class(name="OrderDetail")
Product = Class(name="Product")
PremiumCustomer = Class(name="PremiumCustomer")

# Portal class attributes and methods
Portal_portalId: Property = Property(name="portalId", type=StringType)
Portal_name: Property = Property(name="name", type=StringType)
Portal_url: Property = Property(name="url", type=StringType)
Portal.attributes={Portal_portalId, Portal_url, Portal_name}

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer_phone: Property = Property(name="phone", type=IntegerType)
Customer_creditCardInfo: Property = Property(name="creditCardInfo", type=StringType)
Customer_shippingInfo: Property = Property(name="shippingInfo", type=StringType)
Customer.attributes={Customer_address, Customer_shippingInfo, Customer_creditCardInfo, Customer_name, Customer_phone, Customer_email}

# Order class attributes and methods
Order_orderId: Property = Property(name="orderId", type=IntegerType)
Order_creationDate: Property = Property(name="creationDate", type=StringType)
Order_dateShipped: Property = Property(name="dateShipped", type=StringType)
Order_customerId: Property = Property(name="customerId", type=IntegerType)
Order_status: Property = Property(name="status", type=OrderStatus)
Order_shippingId: Property = Property(name="shippingId", type=IntegerType)
Order_totalPrice: Property = Property(name="totalPrice", type=FloatType)
Order.attributes={Order_customerId, Order_creationDate, Order_shippingId, Order_dateShipped, Order_totalPrice, Order_orderId, Order_status}

# OrderDetail class attributes and methods
OrderDetail_ordrId: Property = Property(name="ordrId", type=IntegerType)
OrderDetail_productId: Property = Property(name="productId", type=IntegerType)
OrderDetail_productName: Property = Property(name="productName", type=StringType)
OrderDetail_quantity: Property = Property(name="quantity", type=IntegerType)
OrderDetail_unitCost: Property = Property(name="unitCost", type=FloatType)
OrderDetail_subtotal: Property = Property(name="subtotal", type=FloatType)
OrderDetail.attributes={OrderDetail_productName, OrderDetail_unitCost, OrderDetail_subtotal, OrderDetail_quantity, OrderDetail_productId, OrderDetail_ordrId}

# Product class attributes and methods
Product_productId: Property = Property(name="productId", type=IntegerType)
Product_description: Property = Property(name="description", type=StringType)
Product_productName: Property = Property(name="productName", type=StringType)
Product_price: Property = Property(name="price", type=FloatType)
Product_imageFileName: Property = Property(name="imageFileName", type=StringType)
Product_stock: Property = Property(name="stock", type=IntegerType)
Product.attributes={Product_stock, Product_productId, Product_description, Product_imageFileName, Product_productName, Product_price}

# PremiumCustomer class attributes and methods
PremiumCustomer_subscriptionExpires: Property = Property(name="subscriptionExpires", type=StringType)
PremiumCustomer.attributes={PremiumCustomer_subscriptionExpires}

# Relationships
Order_OrderDetail: BinaryAssociation = BinaryAssociation(
    name="Order_OrderDetail",
    ends={
        Property(name="orderDetails0", type=OrderDetail, multiplicity=Multiplicity(1, 9999)),
        Property(name="order1", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Product_OrderDetail: BinaryAssociation = BinaryAssociation(
    name="Product_OrderDetail",
    ends={
        Property(name="orderDetails2", type=OrderDetail, multiplicity=Multiplicity(0, 9999)),
        Property(name="product3", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="orders4", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Portal: BinaryAssociation = BinaryAssociation(
    name="Customer_Portal",
    ends={
        Property(name="portal6", type=Portal, multiplicity=Multiplicity(1, 1)),
        Property(name="users7", type=Customer, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5zi_0IqFEemopIBfncy06w",
    types={Portal, Customer, Order, OrderDetail, Product, PremiumCustomer, OrderStatus, real},
    associations={Order_OrderDetail, Product_OrderDetail, Customer_Order, Customer_Portal},
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