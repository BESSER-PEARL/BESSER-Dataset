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
Employee = Class(name="Employee", is_abstract=True)
Payable_Interface = Class(name="Payable_Interface")
SalariedEmployee = Class(name="SalariedEmployee")
Invoice = Class(name="Invoice")

# Employee class attributes and methods
Employee_firstname: Property = Property(name="firstname", type=StringType)
Employee_lastname: Property = Property(name="lastname", type=StringType)
Employee_ssn: Property = Property(name="ssn", type=StringType)
Employee.attributes={Employee_firstname, Employee_ssn, Employee_lastname}

# Payable_Interface class attributes and methods

# SalariedEmployee class attributes and methods
SalariedEmployee_salary: Property = Property(name="salary", type=FloatType)
SalariedEmployee.attributes={SalariedEmployee_salary}

# Invoice class attributes and methods
Invoice_num: Property = Property(name="num", type=StringType)
Invoice_product: Property = Property(name="product", type=StringType)
Invoice_quantity: Property = Property(name="quantity", type=IntegerType)
Invoice_amount: Property = Property(name="amount", type=FloatType)
Invoice.attributes={Invoice_quantity, Invoice_num, Invoice_amount, Invoice_product}

# Domain Model
domain_model = DomainModel(
    name="_NHMXEMMqEeeWu_SLkciAbg",
    types={Employee, Payable_Interface, SalariedEmployee, Invoice},
    associations={},
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