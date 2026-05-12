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
User = Class(name="User")
Administrator = Class(name="Administrator")
Order = Class(name="Order")
Pets = Class(name="Pets")
Employee = Class(name="Employee")
Manager = Class(name="Manager")
Payment = Class(name="Payment")
Shopping_Cart = Class(name="Shopping_Cart")
Doctor = Class(name="Doctor")

# Customer class attributes and methods
Customer_CusID: Property = Property(name="CusID", type=IntegerType)
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_ContactNo: Property = Property(name="ContactNo", type=StringType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer_Email: Property = Property(name="Email", type=StringType)
Customer.attributes={Customer_ContactNo, Customer_Address, Customer_Email, Customer_CusID, Customer_Name}

# User class attributes and methods
User_UserID: Property = Property(name="UserID", type=StringType)
User_Password: Property = Property(name="Password", type=StringType)
User.attributes={User_UserID, User_Password}

# Administrator class attributes and methods
Administrator_adminID: Property = Property(name="adminID", type=StringType)
Administrator_Name: Property = Property(name="Name", type=StringType)
Administrator.attributes={Administrator_Name, Administrator_adminID}

# Order class attributes and methods
Order_OrderID: Property = Property(name="OrderID", type=IntegerType)
Order_DateCreated: Property = Property(name="DateCreated", type=StringType)
Order_CusID: Property = Property(name="CusID", type=IntegerType)
Order.attributes={Order_DateCreated, Order_OrderID, Order_CusID}

# Pets class attributes and methods
Pets_PetID: Property = Property(name="PetID", type=IntegerType)
Pets_PetType: Property = Property(name="PetType", type=StringType)
Pets_PetName: Property = Property(name="PetName", type=StringType)
Pets_Age: Property = Property(name="Age", type=IntegerType)
Pets.attributes={Pets_Age, Pets_PetName, Pets_PetID, Pets_PetType}

# Employee class attributes and methods
Employee_EmpID: Property = Property(name="EmpID", type=IntegerType)
Employee_Name: Property = Property(name="Name", type=StringType)
Employee_ContactNo: Property = Property(name="ContactNo", type=StringType)
Employee_Department: Property = Property(name="Department", type=StringType)
Employee.attributes={Employee_EmpID, Employee_Department, Employee_Name, Employee_ContactNo}

# Manager class attributes and methods
Manager_ManagerID: Property = Property(name="ManagerID", type=IntegerType)
Manager_Name: Property = Property(name="Name", type=StringType)
Manager_ContatctNo: Property = Property(name="ContatctNo", type=StringType)
Manager_Email: Property = Property(name="Email", type=StringType)
Manager.attributes={Manager_Name, Manager_ContatctNo, Manager_ManagerID, Manager_Email}

# Payment class attributes and methods
Payment_PaymentID: Property = Property(name="PaymentID", type=IntegerType)
Payment_Method: Property = Property(name="Method", type=StringType)
Payment_OrderID: Property = Property(name="OrderID", type=IntegerType)
Payment.attributes={Payment_OrderID, Payment_PaymentID, Payment_Method}

# Shopping_Cart class attributes and methods
Shopping_Cart_CartID: Property = Property(name="CartID", type=IntegerType)
Shopping_Cart_OrderID: Property = Property(name="OrderID", type=IntegerType)
Shopping_Cart_Quantity: Property = Property(name="Quantity", type=IntegerType)
Shopping_Cart.attributes={Shopping_Cart_Quantity, Shopping_Cart_CartID, Shopping_Cart_OrderID}

# Doctor class attributes and methods
Doctor_DoctorID: Property = Property(name="DoctorID", type=IntegerType)
Doctor_Name: Property = Property(name="Name", type=StringType)
Doctor_ContactNo: Property = Property(name="ContactNo", type=StringType)
Doctor_Email: Property = Property(name="Email", type=StringType)
Doctor.attributes={Doctor_Name, Doctor_Email, Doctor_ContactNo, Doctor_DoctorID}

# Relationships
Customer_OrderPet: BinaryAssociation = BinaryAssociation(
    name="Customer_OrderPet",
    ends={
        Property(name="_0__0", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Order_Payment: BinaryAssociation = BinaryAssociation(
    name="Order_Payment",
    ends={
        Property(name="payment2", type=Payment, multiplicity=Multiplicity(1, 9999)),
        Property(name="order3", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Order_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Order_Shopping_Cart",
    ends={
        Property(name="_0__4", type=Shopping_Cart, multiplicity=Multiplicity(0, 9999)),
        Property(name="order5", type=Order, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_lL9bAIPZEeeveJPbhFhy_g",
    types={Customer, User, Administrator, Order, Pets, Employee, Manager, Payment, Shopping_Cart, Doctor},
    associations={Customer_OrderPet, Order_Payment, Order_Shopping_Cart},
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