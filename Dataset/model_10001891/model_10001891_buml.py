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
admin = Class(name="admin")
customer = Class(name="customer")
char = Class(name="char")
Payment = Class(name="Payment")
product = Class(name="product")
cart = Class(name="cart")
gest = Class(name="gest")
supplier = Class(name="supplier")
delivery = Class(name="delivery")

# admin class attributes and methods
admin_user_type: Property = Property(name="user_type", type=IntegerType)
admin_user_name: Property = Property(name="user_name", type=StringType)
admin_user_mobile: Property = Property(name="user_mobile", type=IntegerType)
admin.attributes={admin_user_name, admin_user_type, admin_user_mobile}

# customer class attributes and methods
customer_name: Property = Property(name="name", type=char)
customer_address: Property = Property(name="address", type=char)
customer_phone: Property = Property(name="phone", type=IntegerType)
customer_email: Property = Property(name="email", type=char)
customer_password: Property = Property(name="password", type=IntegerType)
customer.attributes={customer_email, customer_password, customer_name, customer_address, customer_phone}

# char class attributes and methods

# Payment class attributes and methods
Payment_customerName: Property = Property(name="customerName", type=char)
Payment_cardType: Property = Property(name="cardType", type=char)
Payment_cardNo: Property = Property(name="cardNo", type=IntegerType)
Payment_customerName1: Property = Property(name="customerName1", type=char)
Payment.attributes={Payment_cardNo, Payment_cardType, Payment_customerName1, Payment_customerName}

# product class attributes and methods
product_name: Property = Property(name="name", type=char)
product_group: Property = Property(name="group", type=char)
product_subgroub: Property = Property(name="subgroub", type=char)
product_id: Property = Property(name="id", type=IntegerType)
product.attributes={product_subgroub, product_name, product_group, product_id}

# cart class attributes and methods
cart_NumberOfProduct: Property = Property(name="NumberOfProduct", type=IntegerType)
cart_product1: Property = Property(name="product1", type=char)
cart_product2: Property = Property(name="product2", type=char)
cart_productn: Property = Property(name="productn", type=char)
cart_price: Property = Property(name="price", type=StringType)
cart_total: Property = Property(name="total", type=StringType)
cart_id: Property = Property(name="id", type=IntegerType)
cart.attributes={cart_product2, cart_product1, cart_id, cart_total, cart_NumberOfProduct, cart_price, cart_productn}

# gest class attributes and methods

# supplier class attributes and methods
supplier_name: Property = Property(name="name", type=char)
supplier_password: Property = Property(name="password", type=IntegerType)
supplier.attributes={supplier_name, supplier_password}

# delivery class attributes and methods
delivery_name: Property = Property(name="name", type=char)
delivery_password: Property = Property(name="password", type=char)
delivery.attributes={delivery_password, delivery_name}

# Relationships
Payment_customer: BinaryAssociation = BinaryAssociation(
    name="Payment_customer",
    ends={
        Property(name="customer0", type=customer, multiplicity=Multiplicity(0, 1)),
        Property(name="payment1", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
customer_cart: BinaryAssociation = BinaryAssociation(
    name="customer_cart",
    ends={
        Property(name="cart2", type=cart, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=customer, multiplicity=Multiplicity(0, 1))
    }
)
customer_product: BinaryAssociation = BinaryAssociation(
    name="customer_product",
    ends={
        Property(name="product4", type=product, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=customer, multiplicity=Multiplicity(0, 1))
    }
)
product_gest: BinaryAssociation = BinaryAssociation(
    name="product_gest",
    ends={
        Property(name="gest6", type=gest, multiplicity=Multiplicity(0, 1)),
        Property(name="product7", type=product, multiplicity=Multiplicity(0, 1))
    }
)
admin_product: BinaryAssociation = BinaryAssociation(
    name="admin_product",
    ends={
        Property(name="product8", type=product, multiplicity=Multiplicity(0, 1)),
        Property(name="admin9", type=admin, multiplicity=Multiplicity(0, 1))
    }
)
supplier_product: BinaryAssociation = BinaryAssociation(
    name="supplier_product",
    ends={
        Property(name="product10", type=product, multiplicity=Multiplicity(0, 1)),
        Property(name="supplier11", type=supplier, multiplicity=Multiplicity(0, 1))
    }
)
delivery_product: BinaryAssociation = BinaryAssociation(
    name="delivery_product",
    ends={
        Property(name="product12", type=product, multiplicity=Multiplicity(0, 1)),
        Property(name="delivery13", type=delivery, multiplicity=Multiplicity(0, 1))
    }
)
delivery_Payment: BinaryAssociation = BinaryAssociation(
    name="delivery_Payment",
    ends={
        Property(name="payment14", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="delivery15", type=delivery, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_buSloHZbEeiFX4HwoivBqg",
    types={admin, customer, char, Payment, product, cart, gest, supplier, delivery},
    associations={Payment_customer, customer_cart, customer_product, product_gest, admin_product, supplier_product, delivery_product, delivery_Payment},
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