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
ProjectType: Enumeration = Enumeration(
    name="ProjectType",
    literals={
            EnumerationLiteral(name="Development"),
			EnumerationLiteral(name="Regie")
    }
)

# Classes
chartDsl_Company = Class(name="chartDsl::Company")
chartDsl_Employee = Class(name="chartDsl::Employee")
chartDsl_Project = Class(name="chartDsl::Project")
chartDsl_Task = Class(name="chartDsl::Task")

# chartDsl_Company class attributes and methods
chartDsl_Company_name: Property = Property(name="name", type=StringType)
chartDsl_Company.attributes={chartDsl_Company_name}

# chartDsl_Employee class attributes and methods
chartDsl_Employee_name: Property = Property(name="name", type=StringType)
chartDsl_Employee.attributes={chartDsl_Employee_name}

# chartDsl_Project class attributes and methods
chartDsl_Project_name: Property = Property(name="name", type=StringType)
chartDsl_Project_projectType: Property = Property(name="projectType", type=StringType)
chartDsl_Project.attributes={chartDsl_Project_name, chartDsl_Project_projectType}

# chartDsl_Task class attributes and methods
chartDsl_Task_name: Property = Property(name="name", type=StringType)
chartDsl_Task.attributes={chartDsl_Task_name}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="chartDsl_Employee", type=chartDsl_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="chartDsl_Company", type=chartDsl_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects1: BinaryAssociation = BinaryAssociation(
    name="projects1",
    ends={
        Property(name="chartDsl_Project", type=chartDsl_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="chartDsl_Company2", type=chartDsl_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasks3: BinaryAssociation = BinaryAssociation(
    name="tasks3",
    ends={
        Property(name="chartDsl_Task", type=chartDsl_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="chartDsl_Project4", type=chartDsl_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
responsable5: BinaryAssociation = BinaryAssociation(
    name="responsable5",
    ends={
        Property(name="chartDsl_Employee7", type=chartDsl_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="chartDsl_Task6", type=chartDsl_Employee, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="chartDsl",
    types={chartDsl_Company, chartDsl_Employee, chartDsl_Project, chartDsl_Task, ProjectType},
    associations={employees0, projects1, tasks3, responsable5},
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