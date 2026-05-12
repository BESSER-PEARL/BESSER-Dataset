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
Customer = Class(name="Customer")
Cart = Class(name="Cart")
Orders = Class(name="Orders")
User = Class(name="User")
Transport = Class(name="Transport")
Admin = Class(name="Admin")
Payment = Class(name="Payment")
Meals = Class(name="Meals")
OrderDetails = Class(name="OrderDetails")
Employee = Class(name="Employee")
Guest = Class(name="Guest")

# Customer class attributes and methods
Customer_CustomerName: Property = Property(name="CustomerName", type=StringType)
Customer_CutsomerAddress: Property = Property(name="CutsomerAddress", type=StringType)
Customer_PhoneNumber: Property = Property(name="PhoneNumber", type=IntegerType)
Customer_Email: Property = Property(name="Email", type=StringType)
Customer.attributes={Customer_CustomerName, Customer_Email, Customer_PhoneNumber, Customer_CutsomerAddress}

# Cart class attributes and methods
Cart_cartID: Property = Property(name="cartID", type=IntegerType)
Cart_ProductID: Property = Property(name="ProductID", type=StringType)
Cart_Quantity: Property = Property(name="Quantity", type=IntegerType)
Cart_date: Property = Property(name="date", type=StringType)
Cart.attributes={Cart_ProductID, Cart_date, Cart_Quantity, Cart_cartID}

# Orders class attributes and methods
Orders_OrderID: Property = Property(name="OrderID", type=IntegerType)
Orders_dateOrdered: Property = Property(name="dateOrdered", type=StringType)
Orders_status: Property = Property(name="status", type=StringType)
Orders_dateFinished: Property = Property(name="dateFinished", type=StringType)
Orders.attributes={Orders_status, Orders_dateOrdered, Orders_OrderID, Orders_dateFinished}

# User class attributes and methods
User_userID: Property = Property(name="userID", type=StringType)
User_Password: Property = Property(name="Password", type=StringType)
User_loginStatus: Property = Property(name="loginStatus", type=StringType)
User.attributes={User_userID, User_loginStatus, User_Password}

# Transport class attributes and methods
Transport_TransportID: Property = Property(name="TransportID", type=IntegerType)
Transport_location: Property = Property(name="location", type=StringType)
Transport_transportCost: Property = Property(name="transportCost", type=StringType)
Transport.attributes={Transport_transportCost, Transport_location, Transport_TransportID}

# Admin class attributes and methods

# Payment class attributes and methods
Payment_paymentID: Property = Property(name="paymentID", type=StringType)
Payment_PaymentType: Property = Property(name="PaymentType", type=StringType)
Payment_PaymentStatus: Property = Property(name="PaymentStatus", type=StringType)
Payment_paymentAmount: Property = Property(name="paymentAmount", type=StringType)
Payment_paymentDate: Property = Property(name="paymentDate", type=StringType)
Payment.attributes={Payment_paymentID, Payment_paymentAmount, Payment_paymentDate, Payment_PaymentType, Payment_PaymentStatus}

# Meals class attributes and methods
Meals_unitPrice: Property = Property(name="unitPrice", type=StringType)
Meals_Portion: Property = Property(name="Portion", type=StringType)
Meals_supplier: Property = Property(name="supplier", type=StringType)
Meals_MealID: Property = Property(name="MealID", type=StringType)
Meals_MealName: Property = Property(name="MealName", type=StringType)
Meals_MealType: Property = Property(name="MealType", type=StringType)
Meals.attributes={Meals_supplier, Meals_MealID, Meals_MealName, Meals_MealType, Meals_Portion, Meals_unitPrice}

# OrderDetails class attributes and methods
OrderDetails_OrderID: Property = Property(name="OrderID", type=IntegerType)
OrderDetails_quantity: Property = Property(name="quantity", type=IntegerType)
OrderDetails_MealID: Property = Property(name="MealID", type=StringType)
OrderDetails_totPrice: Property = Property(name="totPrice", type=StringType)
OrderDetails_orderTime: Property = Property(name="orderTime", type=StringType)
OrderDetails_status: Property = Property(name="status", type=StringType)
OrderDetails.attributes={OrderDetails_status, OrderDetails_quantity, OrderDetails_MealID, OrderDetails_orderTime, OrderDetails_OrderID, OrderDetails_totPrice}

# Employee class attributes and methods
Employee_EmployeeID: Property = Property(name="EmployeeID", type=StringType)
Employee_EmpPassword: Property = Property(name="EmpPassword", type=StringType)
Employee_EmpName: Property = Property(name="EmpName", type=StringType)
Employee.attributes={Employee_EmpPassword, Employee_EmployeeID, Employee_EmpName}

# Guest class attributes and methods
Guest_guestID: Property = Property(name="guestID", type=StringType)
Guest.attributes={Guest_guestID}

# Relationships
Customer_Payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Payment",
    ends={
        Property(name="payment0", type=Payment, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Orders: BinaryAssociation = BinaryAssociation(
    name="Customer_Orders",
    ends={
        Property(name="orders2", type=Orders, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer3", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Employee_Orders: BinaryAssociation = BinaryAssociation(
    name="Employee_Orders",
    ends={
        Property(name="orders4", type=Orders, multiplicity=Multiplicity(0, 1)),
        Property(name="employee5", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)
Orders_OrderDetails: BinaryAssociation = BinaryAssociation(
    name="Orders_OrderDetails",
    ends={
        Property(name="orderDetails6", type=OrderDetails, multiplicity=Multiplicity(1, 9999)),
        Property(name="orders7", type=Orders, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Cart",
    ends={
        Property(name="cart8", type=Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="customer9", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
OrderDetails_Cart: BinaryAssociation = BinaryAssociation(
    name="OrderDetails_Cart",
    ends={
        Property(name="cart10", type=Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="orderDetails11", type=OrderDetails, multiplicity=Multiplicity(0, 1))
    }
)
Orders_Transport2: BinaryAssociation = BinaryAssociation(
    name="Orders_Transport2",
    ends={
        Property(name="transport12", type=Transport, multiplicity=Multiplicity(1, 1)),
        Property(name="orders13", type=Orders, multiplicity=Multiplicity(1, 1))
    }
)
Orders_Payment: BinaryAssociation = BinaryAssociation(
    name="Orders_Payment",
    ends={
        Property(name="payment14", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="orders15", type=Orders, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8ZzEgIPiEeeveJPbhFhy_g",
    types={Customer, Cart, Orders, User, Transport, Admin, Payment, Meals, OrderDetails, Employee, Guest},
    associations={Customer_Payment, Customer_Orders, Employee_Orders, Orders_OrderDetails, Customer_Cart, OrderDetails_Cart, Orders_Transport2, Orders_Payment},
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