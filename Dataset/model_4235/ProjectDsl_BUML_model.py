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
taskType: Enumeration = Enumeration(
    name="taskType",
    literals={
            EnumerationLiteral(name="development"),
			EnumerationLiteral(name="documentation")
    }
)

# Classes
projectDsl_Company = Class(name="projectDsl::Company")
projectDsl_Employees = Class(name="projectDsl::Employees")
projectDsl_Project = Class(name="projectDsl::Project")
projectDsl_Employee = Class(name="projectDsl::Employee")
projectDsl_Task = Class(name="projectDsl::Task")

# projectDsl_Company class attributes and methods
projectDsl_Company_name: Property = Property(name="name", type=StringType)
projectDsl_Company.attributes={projectDsl_Company_name}

# projectDsl_Employees class attributes and methods

# projectDsl_Project class attributes and methods
projectDsl_Project_name: Property = Property(name="name", type=StringType)
projectDsl_Project_type: Property = Property(name="type", type=StringType)
projectDsl_Project.attributes={projectDsl_Project_type, projectDsl_Project_name}

# projectDsl_Employee class attributes and methods
projectDsl_Employee_name: Property = Property(name="name", type=StringType)
projectDsl_Employee_weight: Property = Property(name="weight", type=IntegerType)
projectDsl_Employee_height: Property = Property(name="height", type=IntegerType)
projectDsl_Employee.attributes={projectDsl_Employee_name, projectDsl_Employee_height, projectDsl_Employee_weight}

# projectDsl_Task class attributes and methods
projectDsl_Task_name: Property = Property(name="name", type=StringType)
projectDsl_Task_type: Property = Property(name="type", type=StringType)
projectDsl_Task.attributes={projectDsl_Task_type, projectDsl_Task_name}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="projectDsl_Employees", type=projectDsl_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="projectDsl_Company", type=projectDsl_Employees, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
project1: BinaryAssociation = BinaryAssociation(
    name="project1",
    ends={
        Property(name="projectDsl_Project", type=projectDsl_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="projectDsl_Company2", type=projectDsl_Project, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
employees3: BinaryAssociation = BinaryAssociation(
    name="employees3",
    ends={
        Property(name="projectDsl_Employee", type=projectDsl_Employees, multiplicity=Multiplicity(1, 1)),
        Property(name="projectDsl_Employees4", type=projectDsl_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasks5: BinaryAssociation = BinaryAssociation(
    name="tasks5",
    ends={
        Property(name="projectDsl_Project6", type=projectDsl_Task, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="projectDsl_Task", type=projectDsl_Project, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="projectDsl",
    types={projectDsl_Company, projectDsl_Employees, projectDsl_Project, projectDsl_Employee, projectDsl_Task, taskType},
    associations={employees0, project1, employees3, tasks5},
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