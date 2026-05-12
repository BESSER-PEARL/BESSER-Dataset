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
Car_Rental_Component = Class(name="Car_Rental_Component")
Customer_Actor = Class(name="Customer_Actor")
Insurance_company_Actor = Class(name="Insurance_company_Actor")
Employee_Actor = Class(name="Employee_Actor")
Manager_Actor = Class(name="Manager_Actor")
MyClass = Class(name="MyClass")
UseCase_UseCase = Class(name="UseCase_UseCase")
Pay_bill_external = Class(name="Pay_bill_external")
Login_external = Class(name="Login_external")
Register_external = Class(name="Register_external")
Search_car_external = Class(name="Search_car_external")
Select_car_external = Class(name="Select_car_external")
Book_external = Class(name="Book_external")
View_monthly_rental_reports_external = Class(name="View_monthly_rental_reports_external")
View_daily_rental_reports_external = Class(name="View_daily_rental_reports_external")
Maintain_car_information_external = Class(name="Maintain_car_information_external")
Generate_bill_external = Class(name="Generate_bill_external")

# Car_Rental_Component class attributes and methods

# Customer_Actor class attributes and methods

# Insurance_company_Actor class attributes and methods

# Employee_Actor class attributes and methods

# Manager_Actor class attributes and methods

# MyClass class attributes and methods

# UseCase_UseCase class attributes and methods

# Pay_bill_external class attributes and methods

# Login_external class attributes and methods

# Register_external class attributes and methods

# Search_car_external class attributes and methods

# Select_car_external class attributes and methods

# Book_external class attributes and methods

# View_monthly_rental_reports_external class attributes and methods

# View_daily_rental_reports_external class attributes and methods

# Maintain_car_information_external class attributes and methods

# Generate_bill_external class attributes and methods

# Relationships
Insurance_company_Pay_bill: BinaryAssociation = BinaryAssociation(
    name="Insurance_company_Pay_bill",
    ends={
        Property(name="pay_bill0", type=Pay_bill_external, multiplicity=Multiplicity(0, 1)),
        Property(name="insurance_company1", type=Insurance_company_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Pay_bill: BinaryAssociation = BinaryAssociation(
    name="Customer_Pay_bill",
    ends={
        Property(name="pay_bill2", type=Pay_bill_external, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login4", type=Login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Register: BinaryAssociation = BinaryAssociation(
    name="Customer_Register",
    ends={
        Property(name="register6", type=Register_external, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Search_car: BinaryAssociation = BinaryAssociation(
    name="Customer_Search_car",
    ends={
        Property(name="search_car8", type=Search_car_external, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Select_car: BinaryAssociation = BinaryAssociation(
    name="Customer_Select_car",
    ends={
        Property(name="select_car10", type=Select_car_external, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Book: BinaryAssociation = BinaryAssociation(
    name="Customer_Book",
    ends={
        Property(name="book12", type=Book_external, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
View_monthly_rental_reports_Manager: BinaryAssociation = BinaryAssociation(
    name="View_monthly_rental_reports_Manager",
    ends={
        Property(name="manager14", type=Manager_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_monthly_rental_reports15", type=View_monthly_rental_reports_external, multiplicity=Multiplicity(0, 1))
    }
)
View_daily_rental_reports_Employee: BinaryAssociation = BinaryAssociation(
    name="View_daily_rental_reports_Employee",
    ends={
        Property(name="employee16", type=Employee_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_daily_rental_reports17", type=View_daily_rental_reports_external, multiplicity=Multiplicity(0, 1))
    }
)
Maintain_car_information_Employee: BinaryAssociation = BinaryAssociation(
    name="Maintain_car_information_Employee",
    ends={
        Property(name="employee18", type=Employee_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="maintain_car_information19", type=Maintain_car_information_external, multiplicity=Multiplicity(0, 1))
    }
)
Login_Employee: BinaryAssociation = BinaryAssociation(
    name="Login_Employee",
    ends={
        Property(name="employee20", type=Employee_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login21", type=Login_external, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Generate_bill: BinaryAssociation = BinaryAssociation(
    name="Employee_Generate_bill",
    ends={
        Property(name="generate_bill22", type=Generate_bill_external, multiplicity=Multiplicity(0, 1)),
        Property(name="employee23", type=Employee_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c98062ff_e57c_4e18_b5e2_b8e9ad97a62b",
    types={Car_Rental_Component, Customer_Actor, Insurance_company_Actor, Employee_Actor, Manager_Actor, MyClass, UseCase_UseCase, Pay_bill_external, Login_external, Register_external, Search_car_external, Select_car_external, Book_external, View_monthly_rental_reports_external, View_daily_rental_reports_external, Maintain_car_information_external, Generate_bill_external},
    associations={Insurance_company_Pay_bill, Customer_Pay_bill, Customer_Login, Customer_Register, Customer_Search_car, Customer_Select_car, Customer_Book, View_monthly_rental_reports_Manager, View_daily_rental_reports_Employee, Maintain_car_information_Employee, Login_Employee, Employee_Generate_bill},
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