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
            EnumerationLiteral(name="active"),
			EnumerationLiteral(name="finished"),
			EnumerationLiteral(name="suspended"),
			EnumerationLiteral(name="planned")
    }
)

# Classes
Projects_Company = Class(name="Projects_Company")
Projects_Project = Class(name="Projects_Project")
Projects_Worker = Class(name="Projects_Worker")
Projects_Qualification = Class(name="Projects_Qualification")

# Projects_Company class attributes and methods
Projects_Company_m_hire: Method = Method(name="hire", parameters={Parameter(name='Projects_w', type=StringType)})
Projects_Company_m_start: Method = Method(name="start", parameters={Parameter(name='Projects_p', type=StringType)})
Projects_Company_m_finish: Method = Method(name="finish", parameters={Parameter(name='Projects_p', type=StringType)})
Projects_Company_m_fire: Method = Method(name="fire", parameters={Parameter(name='Projects_w', type=StringType)})
Projects_Company.methods={Projects_Company_m_finish, Projects_Company_m_hire, Projects_Company_m_start, Projects_Company_m_fire}

# Projects_Project class attributes and methods
Projects_Project_size: Property = Property(name="size", type=StringType)
Projects_Project_status: Property = Property(name="status", type=StringType)
Projects_Project.attributes={Projects_Project_size, Projects_Project_status}

# Projects_Worker class attributes and methods

# Projects_Qualification class attributes and methods

# Relationships
company8: BinaryAssociation = BinaryAssociation(
    name="company8",
    ends={
        Property(name="Projects_Project9", type=Projects_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="Projects_Company10", type=Projects_Project, multiplicity=Multiplicity(1, 1))
    }
)
members11: BinaryAssociation = BinaryAssociation(
    name="members11",
    ends={
        Property(name="Projects_Worker13", type=Projects_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Projects_Project12", type=Projects_Worker, multiplicity=Multiplicity(0, 9999))
    }
)
requirements14: BinaryAssociation = BinaryAssociation(
    name="requirements14",
    ends={
        Property(name="Projects_Qualification16", type=Projects_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Projects_Project15", type=Projects_Qualification, multiplicity=Multiplicity(1, 9999))
    }
)
predecessors18: BinaryAssociation = BinaryAssociation(
    name="predecessors18",
    ends={
        Property(name="Projects_Project19", type=Projects_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Projects_Project17", type=Projects_Project, multiplicity=Multiplicity(0, 9999))
    }
)
projects0: BinaryAssociation = BinaryAssociation(
    name="projects0",
    ends={
        Property(name="Projects_Project", type=Projects_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="Projects_Company", type=Projects_Project, multiplicity=Multiplicity(0, 9999))
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="Projects_Worker", type=Projects_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="Projects_Company2", type=Projects_Worker, multiplicity=Multiplicity(1, 9999))
    }
)
qualifications3: BinaryAssociation = BinaryAssociation(
    name="qualifications3",
    ends={
        Property(name="Projects_Qualification", type=Projects_Worker, multiplicity=Multiplicity(1, 1)),
        Property(name="Projects_Worker4", type=Projects_Qualification, multiplicity=Multiplicity(1, 9999))
    }
)
projects5: BinaryAssociation = BinaryAssociation(
    name="projects5",
    ends={
        Property(name="Projects_Project7", type=Projects_Worker, multiplicity=Multiplicity(1, 1)),
        Property(name="Projects_Worker6", type=Projects_Project, multiplicity=Multiplicity(0, 9999))
    }
)


# OCL Constraints
notOverloaded: Constraint = Constraint(
    name="notOverloaded",
    context=Projects_Worker,
    expression="context Worker inv: not (projects->select(p|p.status = ProjectStatus_active)->select(p|p.size=ProjectSize_big)->size() * 2 + projects->select(p|p.status = ProjectStatus_active)->select(p|p.size=ProjectSize_medium)->size() > 3)",
    language="OCL"
)
OnlyOwnEmployeesInProjects: Constraint = Constraint(
    name="OnlyOwnEmployeesInProjects",
    context=Projects_Company,
    expression="context Company inv: employees->includesAll(projects.members->asSet())",
    language="OCL"
)
AllQualificationsForActiveProject: Constraint = Constraint(
    name="AllQualificationsForActiveProject",
    context=Projects_Project,
    expression="context Project inv: status = ProjectStatus_active implies (requirements->select(q|not members->exists(m | m.qualifications->includes(q))))->isEmpty()",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="Projects",
    types={Projects_Company, Projects_Project, Projects_Worker, Projects_Qualification, ProjectSize, ProjectStatus},
    associations={company8, members11, requirements14, predecessors18, projects0, employees1, qualifications3, projects5},
    constraints={notOverloaded, OnlyOwnEmployeesInProjects, AllQualificationsForActiveProject},
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