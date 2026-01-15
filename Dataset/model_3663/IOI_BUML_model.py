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
iOI_Employee = Class(name="iOI::Employee")
iOI_Position = Class(name="iOI::Position")
iOI_Model = Class(name="iOI::Model")
iOI_Company = Class(name="iOI::Company")
iOI_Department = Class(name="iOI::Department")
iOI_Manager = Class(name="iOI::Manager")
Employee = Class(name="Employee")

# iOI_Employee class attributes and methods
iOI_Employee_name: Property = Property(name="name", type=StringType)
iOI_Employee_salary: Property = Property(name="salary", type=IntegerType)
iOI_Employee.attributes={iOI_Employee_name, iOI_Employee_salary}

# iOI_Position class attributes and methods
iOI_Position_name: Property = Property(name="name", type=StringType)
iOI_Position.attributes={iOI_Position_name}

# iOI_Model class attributes and methods
iOI_Model_name: Property = Property(name="name", type=StringType)
iOI_Model.attributes={iOI_Model_name}

# iOI_Company class attributes and methods
iOI_Company_name: Property = Property(name="name", type=StringType)
iOI_Company.attributes={iOI_Company_name}

# iOI_Department class attributes and methods
iOI_Department_name: Property = Property(name="name", type=StringType)
iOI_Department.attributes={iOI_Department_name}

# iOI_Manager class attributes and methods

# Employee class attributes and methods

# Relationships
companies0: BinaryAssociation = BinaryAssociation(
    name="companies0",
    ends={
        Property(name="iOI_Company", type=iOI_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="iOI_Model", type=iOI_Company, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub_department13: BinaryAssociation = BinaryAssociation(
    name="sub_department13",
    ends={
        Property(name="iOI_Department14", type=iOI_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="iOI_Department12", type=iOI_Department, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
works_on1: BinaryAssociation = BinaryAssociation(
    name="works_on1",
    ends={
        Property(name="iOI_Position", type=iOI_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="iOI_Employee", type=iOI_Position, multiplicity=Multiplicity(0, 1))
    }
)
positions2: BinaryAssociation = BinaryAssociation(
    name="positions2",
    ends={
        Property(name="iOI_Position4", type=iOI_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="iOI_Company3", type=iOI_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
departments5: BinaryAssociation = BinaryAssociation(
    name="departments5",
    ends={
        Property(name="iOI_Department", type=iOI_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="iOI_Company6", type=iOI_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manager7: BinaryAssociation = BinaryAssociation(
    name="manager7",
    ends={
        Property(name="iOI_Manager", type=iOI_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="iOI_Department8", type=iOI_Manager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
employees9: BinaryAssociation = BinaryAssociation(
    name="employees9",
    ends={
        Property(name="iOI_Employee11", type=iOI_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="iOI_Department10", type=iOI_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_iOI_Manager_Employee = Generalization(general=Employee, specific=iOI_Manager)

# Domain Model
domain_model = DomainModel(
    name="iOI",
    types={iOI_Employee, iOI_Position, iOI_Model, iOI_Company, iOI_Department, iOI_Manager, Employee},
    associations={companies0, sub_department13, works_on1, positions2, departments5, manager7, employees9},
    generalizations={gen_iOI_Manager_Employee},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)