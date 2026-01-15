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
ProjectSize: Enumeration = Enumeration(
    name="ProjectSize",
    literals={
            EnumerationLiteral(name="small"),
			EnumerationLiteral(name="medium"),
			EnumerationLiteral(name="big")
    }
)

ProjectStatus: Enumeration = Enumeration(
    name="ProjectStatus",
    literals={
            EnumerationLiteral(name="planned"),
			EnumerationLiteral(name="active"),
			EnumerationLiteral(name="finished"),
			EnumerationLiteral(name="suspended")
    }
)

# Classes
Projects_Project = Class(name="Projects::Project")
Projects_Company = Class(name="Projects::Company")
Projects_Qualification = Class(name="Projects::Qualification")
Projects_Worker = Class(name="Projects::Worker")
Projects_Training = Class(name="Projects::Training")
Project = Class(name="Project")

# Projects_Project class attributes and methods
Projects_Project_name: Property = Property(name="name", type=StringType)
Projects_Project_size: Property = Property(name="size", type=StringType)
Projects_Project_status: Property = Property(name="status", type=StringType)
Projects_Project_m_missingQualifications: Method = Method(name="missingQualifications", parameters={}, type=StringType)
Projects_Project_m_isHelpful: Method = Method(name="isHelpful", parameters={Parameter(name='w')}, type=BooleanType)
Projects_Project.attributes={Projects_Project_name, Projects_Project_size, Projects_Project_status}
Projects_Project.methods={Projects_Project_m_missingQualifications, Projects_Project_m_isHelpful}

# Projects_Company class attributes and methods
Projects_Company_name: Property = Property(name="name", type=StringType)
Projects_Company_m_start: Method = Method(name="start", parameters={Parameter(name='p')})
Projects_Company_m_finish: Method = Method(name="finish", parameters={Parameter(name='p')})
Projects_Company_m_createWorker: Method = Method(name="createWorker", parameters={Parameter(name='qs')}, type=StringType)
Projects_Company_m_createProject: Method = Method(name="createProject", parameters={Parameter(name='ws'), Parameter(name='n'), Parameter(name='qs'), Parameter(name='s')}, type=StringType)
Projects_Company_m_fire: Method = Method(name="fire", parameters={Parameter(name='w')})
Projects_Company_m_hire: Method = Method(name="hire", parameters={Parameter(name='w')})
Projects_Company.attributes={Projects_Company_name}
Projects_Company.methods={Projects_Company_m_hire, Projects_Company_m_start, Projects_Company_m_createProject, Projects_Company_m_createWorker, Projects_Company_m_finish, Projects_Company_m_fire}

# Projects_Qualification class attributes and methods
Projects_Qualification_description: Property = Property(name="description", type=StringType)
Projects_Qualification.attributes={Projects_Qualification_description}

# Projects_Worker class attributes and methods
Projects_Worker_nickname: Property = Property(name="nickname", type=StringType)
Projects_Worker_salary: Property = Property(name="salary", type=IntegerType)
Projects_Worker_m_isOverloaded: Method = Method(name="isOverloaded", parameters={}, type=BooleanType)
Projects_Worker.attributes={Projects_Worker_salary, Projects_Worker_nickname}
Projects_Worker.methods={Projects_Worker_m_isOverloaded}

# Projects_Training class attributes and methods

# Project class attributes and methods

# Relationships
projects0: BinaryAssociation = BinaryAssociation(
    name="projects0",
    ends={
        Property(name="Project", type=Projects_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company", type=Projects_Project, multiplicity=Multiplicity(0, 9999))
    }
)
employer2: BinaryAssociation = BinaryAssociation(
    name="employer2",
    ends={
        Property(name="Company", type=Projects_Worker, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=Projects_Company, multiplicity=Multiplicity(0, 1))
    }
)
qualifications3: BinaryAssociation = BinaryAssociation(
    name="qualifications3",
    ends={
        Property(name="Qualification", type=Projects_Worker, multiplicity=Multiplicity(1, 1)),
        Property(name="workers", type=Projects_Qualification, multiplicity=Multiplicity(1, 9999))
    }
)
projects4: BinaryAssociation = BinaryAssociation(
    name="projects4",
    ends={
        Property(name="Project5", type=Projects_Worker, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=Projects_Project, multiplicity=Multiplicity(0, 9999))
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="Worker", type=Projects_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="employer", type=Projects_Worker, multiplicity=Multiplicity(1, 9999))
    }
)
requirements11: BinaryAssociation = BinaryAssociation(
    name="requirements11",
    ends={
        Property(name="Qualification13", type=Projects_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projects12", type=Projects_Qualification, multiplicity=Multiplicity(1, 9999))
    }
)
predecessors15: BinaryAssociation = BinaryAssociation(
    name="predecessors15",
    ends={
        Property(name="Project16", type=Projects_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="successors", type=Projects_Project, multiplicity=Multiplicity(0, 9999))
    }
)
successors18: BinaryAssociation = BinaryAssociation(
    name="successors18",
    ends={
        Property(name="Project19", type=Projects_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessors", type=Projects_Project, multiplicity=Multiplicity(0, 9999))
    }
)
workers20: BinaryAssociation = BinaryAssociation(
    name="workers20",
    ends={
        Property(name="Worker21", type=Projects_Qualification, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifications", type=Projects_Worker, multiplicity=Multiplicity(0, 9999))
    }
)
projects22: BinaryAssociation = BinaryAssociation(
    name="projects22",
    ends={
        Property(name="Project23", type=Projects_Qualification, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements", type=Projects_Project, multiplicity=Multiplicity(0, 9999))
    }
)
trainings24: BinaryAssociation = BinaryAssociation(
    name="trainings24",
    ends={
        Property(name="Training", type=Projects_Qualification, multiplicity=Multiplicity(1, 1)),
        Property(name="trained", type=Projects_Training, multiplicity=Multiplicity(0, 1))
    }
)
company6: BinaryAssociation = BinaryAssociation(
    name="company6",
    ends={
        Property(name="Company7", type=Projects_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projects", type=Projects_Company, multiplicity=Multiplicity(1, 1))
    }
)
members8: BinaryAssociation = BinaryAssociation(
    name="members8",
    ends={
        Property(name="Worker10", type=Projects_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projects9", type=Projects_Worker, multiplicity=Multiplicity(0, 9999))
    }
)
trained25: BinaryAssociation = BinaryAssociation(
    name="trained25",
    ends={
        Property(name="Qualification26", type=Projects_Training, multiplicity=Multiplicity(1, 1)),
        Property(name="trainings", type=Projects_Qualification, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_Projects_Training_Project = Generalization(general=Project, specific=Projects_Training)

# Domain Model
domain_model = DomainModel(
    name="Projects",
    types={Projects_Project, Projects_Company, Projects_Qualification, Projects_Worker, Projects_Training, Project, ProjectSize, ProjectStatus},
    associations={projects0, employer2, qualifications3, projects4, employees1, requirements11, predecessors15, successors18, workers20, projects22, trainings24, company6, members8, trained25},
    generalizations={gen_Projects_Training_Project},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)