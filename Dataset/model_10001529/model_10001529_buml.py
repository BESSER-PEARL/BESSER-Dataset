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
Person = Class(name="Person")
Product = Class(name="Product")
Order = Class(name="Order")
Admin = Class(name="Admin")
Customer = Class(name="Customer")
Medicine = Class(name="Medicine")
Cart = Class(name="Cart")
MediDevices = Class(name="MediDevices")
ExerciseMachine = Class(name="ExerciseMachine")
PaymentMethod = Class(name="PaymentMethod")
Registration = Class(name="Registration")

# Person class attributes and methods
Person_Name: Property = Property(name="Name", type=StringType)
Person_LastName: Property = Property(name="LastName", type=StringType)
Person_DOB: Property = Property(name="DOB", type=StringType)
Person_Address: Property = Property(name="Address", type=StringType)
Person_Phone: Property = Property(name="Phone", type=IntegerType)
Person_Email: Property = Property(name="Email", type=StringType)
Person.attributes={Person_DOB, Person_LastName, Person_Name, Person_Phone, Person_Email, Person_Address}

# Product class attributes and methods
Product_pID: Property = Property(name="pID", type=StringType)
Product_name: Property = Property(name="name", type=StringType)
Product_price: Property = Property(name="price", type=IntegerType)
Product_manufecturer: Property = Property(name="manufecturer", type=StringType)
Product_manufecturedDate: Property = Property(name="manufecturedDate", type=StringType)
Product_expiry: Property = Property(name="expiry", type=StringType)
Product_color: Property = Property(name="color", type=StringType)
Product.attributes={Product_name, Product_manufecturer, Product_expiry, Product_pID, Product_color, Product_manufecturedDate, Product_price}

# Order class attributes and methods
Order_id: Property = Property(name="id", type=IntegerType)
Order_orderDate: Property = Property(name="orderDate", type=StringType)
Order_quantity: Property = Property(name="quantity", type=IntegerType)
Order_orderStatus: Property = Property(name="orderStatus", type=StringType)
Order.attributes={Order_id, Order_quantity, Order_orderStatus, Order_orderDate}

# Admin class attributes and methods
Admin_id: Property = Property(name="id", type=IntegerType)
Admin_userName: Property = Property(name="userName", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin.attributes={Admin_userName, Admin_id, Admin_password}

# Customer class attributes and methods
Customer_id: Property = Property(name="id", type=IntegerType)
Customer_userName: Property = Property(name="userName", type=StringType)
Customer_password: Property = Property(name="password", type=StringType)
Customer.attributes={Customer_id, Customer_password, Customer_userName}

# Medicine class attributes and methods
Medicine_id: Property = Property(name="id", type=IntegerType)
Medicine_name: Property = Property(name="name", type=StringType)
Medicine_formula: Property = Property(name="formula", type=StringType)
Medicine_potency: Property = Property(name="potency", type=StringType)
Medicine.attributes={Medicine_potency, Medicine_formula, Medicine_id, Medicine_name}

# Cart class attributes and methods
Cart_id: Property = Property(name="id", type=IntegerType)
Cart_TotalBill: Property = Property(name="TotalBill", type=IntegerType)
Cart.attributes={Cart_TotalBill, Cart_id}

# MediDevices class attributes and methods
MediDevices_id: Property = Property(name="id", type=StringType)
MediDevices_name: Property = Property(name="name", type=StringType)
MediDevices_type: Property = Property(name="type", type=StringType)
MediDevices.attributes={MediDevices_id, MediDevices_name, MediDevices_type}

# ExerciseMachine class attributes and methods
ExerciseMachine_id: Property = Property(name="id", type=IntegerType)
ExerciseMachine_name: Property = Property(name="name", type=StringType)
ExerciseMachine_type: Property = Property(name="type", type=StringType)
ExerciseMachine_size: Property = Property(name="size", type=IntegerType)
ExerciseMachine.attributes={ExerciseMachine_type, ExerciseMachine_size, ExerciseMachine_name, ExerciseMachine_id}

# PaymentMethod class attributes and methods
PaymentMethod_paymentType: Property = Property(name="paymentType", type=StringType)
PaymentMethod_online: Property = Property(name="online", type=StringType)
PaymentMethod_cashOnDelievery: Property = Property(name="cashOnDelievery", type=StringType)
PaymentMethod.attributes={PaymentMethod_cashOnDelievery, PaymentMethod_paymentType, PaymentMethod_online}

# Registration class attributes and methods
Registration_name: Property = Property(name="name", type=StringType)
Registration_LastName: Property = Property(name="LastName", type=StringType)
Registration_DOB: Property = Property(name="DOB", type=StringType)
Registration_UserName: Property = Property(name="UserName", type=StringType)
Registration_Password: Property = Property(name="Password", type=StringType)
Registration_Address: Property = Property(name="Address", type=StringType)
Registration_Phone: Property = Property(name="Phone", type=IntegerType)
Registration_Email: Property = Property(name="Email", type=StringType)
Registration.attributes={Registration_name, Registration_Email, Registration_UserName, Registration_Address, Registration_Phone, Registration_LastName, Registration_Password, Registration_DOB}

# Relationships
Product_Medicine: BinaryAssociation = BinaryAssociation(
    name="Product_Medicine",
    ends={
        Property(name="medicine0", type=Medicine, multiplicity=Multiplicity(0, 1)),
        Property(name="product1", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Product_MediDevices: BinaryAssociation = BinaryAssociation(
    name="Product_MediDevices",
    ends={
        Property(name="mediDevices2", type=MediDevices, multiplicity=Multiplicity(0, 1)),
        Property(name="product3", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Product_ExerciseMachine: BinaryAssociation = BinaryAssociation(
    name="Product_ExerciseMachine",
    ends={
        Property(name="exerciseMachine4", type=ExerciseMachine, multiplicity=Multiplicity(0, 1)),
        Property(name="product5", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Order_Cart: BinaryAssociation = BinaryAssociation(
    name="Order_Cart",
    ends={
        Property(name="cart6", type=Cart, multiplicity=Multiplicity(0, 1)),
        Property(name="order7", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Cart_PaymentMethod: BinaryAssociation = BinaryAssociation(
    name="Cart_PaymentMethod",
    ends={
        Property(name="paymentMethod8", type=PaymentMethod, multiplicity=Multiplicity(0, 1)),
        Property(name="cart9", type=Cart, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Registration: BinaryAssociation = BinaryAssociation(
    name="Admin_Registration",
    ends={
        Property(name="registration10", type=Registration, multiplicity=Multiplicity(0, 1)),
        Property(name="admin11", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Person_Product: BinaryAssociation = BinaryAssociation(
    name="Person_Product",
    ends={
        Property(name="product12", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="person13", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Product: BinaryAssociation = BinaryAssociation(
    name="Admin_Product",
    ends={
        Property(name="product14", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="admin15", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Product_Order: BinaryAssociation = BinaryAssociation(
    name="Product_Order",
    ends={
        Property(name="order16", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="product17", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Person_Registration: BinaryAssociation = BinaryAssociation(
    name="Person_Registration",
    ends={
        Property(name="registration18", type=Registration, multiplicity=Multiplicity(0, 1)),
        Property(name="person19", type=Person, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Du7DoBphEeqPCsas7676rw",
    types={Person, Product, Order, Admin, Customer, Medicine, Cart, MediDevices, ExerciseMachine, PaymentMethod, Registration},
    associations={Product_Medicine, Product_MediDevices, Product_ExerciseMachine, Order_Cart, Cart_PaymentMethod, Admin_Registration, Person_Product, Admin_Product, Product_Order, Person_Registration},
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