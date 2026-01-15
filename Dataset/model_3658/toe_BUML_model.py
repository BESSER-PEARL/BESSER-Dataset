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
toe_AllHolder = Class(name="toe::AllHolder")
toe_AllBase = Class(name="toe::AllBase", is_abstract=True)
toe_Employee = Class(name="toe::Employee")
AllBase = Class(name="AllBase")
toe_Project = Class(name="toe::Project")
toe_Department = Class(name="toe::Department")
toe_Contribution = Class(name="toe::Contribution")
toe_Manager = Class(name="toe::Manager")
Employee = Class(name="Employee")

# toe_AllHolder class attributes and methods

# toe_AllBase class attributes and methods

# toe_Employee class attributes and methods
toe_Employee_name: Property = Property(name="name", type=StringType)
toe_Employee_salary: Property = Property(name="salary", type=IntegerType)
toe_Employee.attributes={toe_Employee_salary, toe_Employee_name}

# AllBase class attributes and methods

# toe_Project class attributes and methods
toe_Project_name: Property = Property(name="name", type=StringType)
toe_Project_departmentWide: Property = Property(name="departmentWide", type=BooleanType)
toe_Project.attributes={toe_Project_departmentWide, toe_Project_name}

# toe_Department class attributes and methods
toe_Department_name: Property = Property(name="name", type=StringType)
toe_Department_m_allSubDepartments: Method = Method(name="allSubDepartments", parameters={}, type=StringType)
toe_Department.attributes={toe_Department_name}
toe_Department.methods={toe_Department_m_allSubDepartments}

# toe_Contribution class attributes and methods
toe_Contribution_description: Property = Property(name="description", type=StringType)
toe_Contribution.attributes={toe_Contribution_description}

# toe_Manager class attributes and methods

# Employee class attributes and methods

# Relationships
all0: BinaryAssociation = BinaryAssociation(
    name="all0",
    ends={
        Property(name="toe_AllBase", type=toe_AllHolder, multiplicity=Multiplicity(1, 1)),
        Property(name="toe_AllHolder", type=toe_AllBase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects1: BinaryAssociation = BinaryAssociation(
    name="projects1",
    ends={
        Property(name="Project", type=toe_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="projectTeam", type=toe_Project, multiplicity=Multiplicity(0, 9999))
    }
)
department2: BinaryAssociation = BinaryAssociation(
    name="department2",
    ends={
        Property(name="Department", type=toe_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=toe_Department, multiplicity=Multiplicity(0, 1))
    }
)
contributions3: BinaryAssociation = BinaryAssociation(
    name="contributions3",
    ends={
        Property(name="Contribution", type=toe_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee", type=toe_Contribution, multiplicity=Multiplicity(0, 9999))
    }
)
leads4: BinaryAssociation = BinaryAssociation(
    name="leads4",
    ends={
        Property(name="Project5", type=toe_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="lead", type=toe_Project, multiplicity=Multiplicity(0, 9999))
    }
)
managedDepartment6: BinaryAssociation = BinaryAssociation(
    name="managedDepartment6",
    ends={
        Property(name="Department7", type=toe_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="manager", type=toe_Department, multiplicity=Multiplicity(0, 1))
    }
)
employees15: BinaryAssociation = BinaryAssociation(
    name="employees15",
    ends={
        Property(name="department", type=toe_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Employee16", type=toe_Department, multiplicity=Multiplicity(1, 1))
    }
)
parentDepartment18: BinaryAssociation = BinaryAssociation(
    name="parentDepartment18",
    ends={
        Property(name="Department19", type=toe_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="subDepartments", type=toe_Department, multiplicity=Multiplicity(0, 1))
    }
)
manager20: BinaryAssociation = BinaryAssociation(
    name="manager20",
    ends={
        Property(name="Manager", type=toe_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="managedDepartment", type=toe_Manager, multiplicity=Multiplicity(1, 1))
    }
)
projectTeam21: BinaryAssociation = BinaryAssociation(
    name="projectTeam21",
    ends={
        Property(name="Employee22", type=toe_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projects", type=toe_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
lead23: BinaryAssociation = BinaryAssociation(
    name="lead23",
    ends={
        Property(name="Manager24", type=toe_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="leads", type=toe_Manager, multiplicity=Multiplicity(0, 1))
    }
)
contributions25: BinaryAssociation = BinaryAssociation(
    name="contributions25",
    ends={
        Property(name="Contribution26", type=toe_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project", type=toe_Contribution, multiplicity=Multiplicity(0, 9999))
    }
)
employee8: BinaryAssociation = BinaryAssociation(
    name="employee8",
    ends={
        Property(name="Employee", type=toe_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="contributions", type=toe_Employee, multiplicity=Multiplicity(0, 1))
    }
)
project9: BinaryAssociation = BinaryAssociation(
    name="project9",
    ends={
        Property(name="Project11", type=toe_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="contributions10", type=toe_Project, multiplicity=Multiplicity(0, 1))
    }
)
subDepartments13: BinaryAssociation = BinaryAssociation(
    name="subDepartments13",
    ends={
        Property(name="Department14", type=toe_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="parentDepartment", type=toe_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_toe_Employee_AllBase = Generalization(general=AllBase, specific=toe_Employee)
gen_toe_Manager_Employee = Generalization(general=Employee, specific=toe_Manager)
gen_toe_Contribution_AllBase = Generalization(general=AllBase, specific=toe_Contribution)
gen_toe_Project_AllBase = Generalization(general=AllBase, specific=toe_Project)
gen_toe_Department_AllBase = Generalization(general=AllBase, specific=toe_Department)

# Domain Model
domain_model = DomainModel(
    name="toe",
    types={toe_AllHolder, toe_AllBase, toe_Employee, AllBase, toe_Project, toe_Department, toe_Contribution, toe_Manager, Employee},
    associations={all0, projects1, department2, contributions3, leads4, managedDepartment6, employees15, parentDepartment18, manager20, projectTeam21, lead23, contributions25, employee8, project9, subDepartments13},
    generalizations={gen_toe_Employee_AllBase, gen_toe_Manager_Employee, gen_toe_Contribution_AllBase, gen_toe_Project_AllBase, gen_toe_Department_AllBase},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)