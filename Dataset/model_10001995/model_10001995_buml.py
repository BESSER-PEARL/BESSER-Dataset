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
Management_Director = Class(name="Management_Director")
Management_Manager = Class(name="Management_Manager")
Management_DirectorTest = Class(name="Management_DirectorTest")
Management_ManagerTest = Class(name="Management_ManagerTest")
Staff_Employee = Class(name="Staff_Employee", is_abstract=True)
techStaff_DatabaseAdmin = Class(name="techStaff_DatabaseAdmin")
techStaff_Developer = Class(name="techStaff_Developer")
techStaff_DatabaseAdminTest = Class(name="techStaff_DatabaseAdminTest")
techStaff_DeveloperTest = Class(name="techStaff_DeveloperTest")

# Management_Director class attributes and methods
Management_Director_budget: Property = Property(name="budget", type=FloatType)
Management_Director.attributes={Management_Director_budget}

# Management_Manager class attributes and methods
Management_Manager_deptName: Property = Property(name="deptName", type=StringType)
Management_Manager.attributes={Management_Manager_deptName}

# Management_DirectorTest class attributes and methods

# Management_ManagerTest class attributes and methods

# Staff_Employee class attributes and methods
Staff_Employee_name: Property = Property(name="name", type=StringType)
Staff_Employee_nationalInsurance: Property = Property(name="nationalInsurance", type=StringType)
Staff_Employee_salary: Property = Property(name="salary", type=FloatType)
Staff_Employee.attributes={Staff_Employee_name, Staff_Employee_nationalInsurance, Staff_Employee_salary}

# techStaff_DatabaseAdmin class attributes and methods

# techStaff_Developer class attributes and methods

# techStaff_DatabaseAdminTest class attributes and methods

# techStaff_DeveloperTest class attributes and methods

# Relationships
databaseAdmin_DatabaseAdminTest_DatabaseAdmin_2: BinaryAssociation = BinaryAssociation(
    name="databaseAdmin_DatabaseAdminTest_DatabaseAdmin_2",
    ends={
        Property(name="databaseadmintest0", type=techStaff_DatabaseAdminTest, multiplicity=Multiplicity(0, 1)),
        Property(name="databaseAdmin1", type=techStaff_DatabaseAdmin, multiplicity=Multiplicity(0, 1))
    }
)
developer_DeveloperTest_Developer_3: BinaryAssociation = BinaryAssociation(
    name="developer_DeveloperTest_Developer_3",
    ends={
        Property(name="developertest2", type=techStaff_DeveloperTest, multiplicity=Multiplicity(0, 1)),
        Property(name="developer3", type=techStaff_Developer, multiplicity=Multiplicity(0, 1))
    }
)
manager_ManagerTest_Manager_0: BinaryAssociation = BinaryAssociation(
    name="manager_ManagerTest_Manager_0",
    ends={
        Property(name="managertest4", type=Management_ManagerTest, multiplicity=Multiplicity(0, 1)),
        Property(name="manager5", type=Management_Manager, multiplicity=Multiplicity(0, 1))
    }
)
director_DirectorTest_Director_1: BinaryAssociation = BinaryAssociation(
    name="director_DirectorTest_Director_1",
    ends={
        Property(name="directortest6", type=Management_DirectorTest, multiplicity=Multiplicity(0, 1)),
        Property(name="director7", type=Management_Director, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_iUigMElqEemcCbHu8oEdZw",
    types={Management_Director, Management_Manager, Management_DirectorTest, Management_ManagerTest, Staff_Employee, techStaff_DatabaseAdmin, techStaff_Developer, techStaff_DatabaseAdminTest, techStaff_DeveloperTest},
    associations={databaseAdmin_DatabaseAdminTest_DatabaseAdmin_2, developer_DeveloperTest_Developer_3, manager_ManagerTest_Manager_0, director_DirectorTest_Director_1},
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