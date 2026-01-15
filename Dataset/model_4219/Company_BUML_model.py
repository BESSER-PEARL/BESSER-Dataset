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
CompanyModel_Company = Class(name="CompanyModel::Company")
CompanyModel_Department = Class(name="CompanyModel::Department")
CompanyModel_Employee = Class(name="CompanyModel::Employee")
CompanyModel_Product = Class(name="CompanyModel::Product")

# CompanyModel_Company class attributes and methods
CompanyModel_Company_name: Property = Property(name="name", type=StringType)
CompanyModel_Company.attributes={CompanyModel_Company_name}

# CompanyModel_Department class attributes and methods
CompanyModel_Department_number: Property = Property(name="number", type=IntegerType)
CompanyModel_Department.attributes={CompanyModel_Department_number}

# CompanyModel_Employee class attributes and methods
CompanyModel_Employee_isManager: Property = Property(name="isManager", type=BooleanType)
CompanyModel_Employee_name: Property = Property(name="name", type=StringType)
CompanyModel_Employee.attributes={CompanyModel_Employee_name, CompanyModel_Employee_isManager}

# CompanyModel_Product class attributes and methods
CompanyModel_Product_name: Property = Property(name="name", type=StringType)
CompanyModel_Product_productID: Property = Property(name="productID", type=IntegerType)
CompanyModel_Product.attributes={CompanyModel_Product_name, CompanyModel_Product_productID}

# Relationships
departments0: BinaryAssociation = BinaryAssociation(
    name="departments0",
    ends={
        Property(name="CompanyModel_Department", type=CompanyModel_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="CompanyModel_Company", type=CompanyModel_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="CompanyModel_Employee", type=CompanyModel_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="CompanyModel_Department2", type=CompanyModel_Employee, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
products3: BinaryAssociation = BinaryAssociation(
    name="products3",
    ends={
        Property(name="CompanyModel_Product", type=CompanyModel_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="CompanyModel_Department4", type=CompanyModel_Product, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="CompanyModel",
    types={CompanyModel_Company, CompanyModel_Department, CompanyModel_Employee, CompanyModel_Product},
    associations={departments0, employees1, products3},
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