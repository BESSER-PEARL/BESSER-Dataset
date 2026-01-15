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
PersonCompany_Person = Class(name="PersonCompany::Person")
PersonCompany_Job = Class(name="PersonCompany::Job")
PersonCompany_Company = Class(name="PersonCompany::Company")

# PersonCompany_Person class attributes and methods
PersonCompany_Person_name: Property = Property(name="name", type=StringType)
PersonCompany_Person_m_employer: Method = Method(name="employer", parameters={}, type=StringType)
PersonCompany_Person.attributes={PersonCompany_Person_name}
PersonCompany_Person.methods={PersonCompany_Person_m_employer}

# PersonCompany_Job class attributes and methods
PersonCompany_Job_salary: Property = Property(name="salary", type=IntegerType)
PersonCompany_Job_m_bossPlus: Method = Method(name="bossPlus", parameters={}, type=StringType)
PersonCompany_Job_m_workerPlus: Method = Method(name="workerPlus", parameters={}, type=StringType)
PersonCompany_Job_m_workerPlusOnSet: Method = Method(name="workerPlusOnSet", parameters={Parameter(name='s')}, type=StringType)
PersonCompany_Job.attributes={PersonCompany_Job_salary}
PersonCompany_Job.methods={PersonCompany_Job_m_workerPlusOnSet, PersonCompany_Job_m_bossPlus, PersonCompany_Job_m_workerPlus}

# PersonCompany_Company class attributes and methods
PersonCompany_Company_name: Property = Property(name="name", type=StringType)
PersonCompany_Company_m_employee: Method = Method(name="employee", parameters={}, type=StringType)
PersonCompany_Company.attributes={PersonCompany_Company_name}
PersonCompany_Company.methods={PersonCompany_Company_m_employee}

# Relationships
PersonJob_Job_role_job0: BinaryAssociation = BinaryAssociation(
    name="PersonJob_Job_role_job0",
    ends={
        Property(name="Job", type=PersonCompany_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="PersonJob_Person_role_employee", type=PersonCompany_Job, multiplicity=Multiplicity(0, 9999))
    }
)
CompanyJob_Job_role_job1: BinaryAssociation = BinaryAssociation(
    name="CompanyJob_Job_role_job1",
    ends={
        Property(name="Job2", type=PersonCompany_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="CompanyJob_Company_role_employer", type=PersonCompany_Job, multiplicity=Multiplicity(0, 9999))
    }
)
PersonJob_Person_role_employee3: BinaryAssociation = BinaryAssociation(
    name="PersonJob_Person_role_employee3",
    ends={
        Property(name="Person", type=PersonCompany_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="PersonJob_Job_role_job", type=PersonCompany_Person, multiplicity=Multiplicity(1, 1))
    }
)
CompanyJob_Company_role_employer4: BinaryAssociation = BinaryAssociation(
    name="CompanyJob_Company_role_employer4",
    ends={
        Property(name="Company", type=PersonCompany_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="CompanyJob_Job_role_job", type=PersonCompany_Company, multiplicity=Multiplicity(1, 1))
    }
)
BossWorker_Job_role_worker6: BinaryAssociation = BinaryAssociation(
    name="BossWorker_Job_role_worker6",
    ends={
        Property(name="Job7", type=PersonCompany_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="BossWorker_Job_role_boss", type=PersonCompany_Job, multiplicity=Multiplicity(0, 9999))
    }
)
BossWorker_Job_role_boss9: BinaryAssociation = BinaryAssociation(
    name="BossWorker_Job_role_boss9",
    ends={
        Property(name="Job10", type=PersonCompany_Job, multiplicity=Multiplicity(1, 1)),
        Property(name="BossWorker_Job_role_worker", type=PersonCompany_Job, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PersonCompany",
    types={PersonCompany_Person, PersonCompany_Job, PersonCompany_Company},
    associations={PersonJob_Job_role_job0, CompanyJob_Job_role_job1, PersonJob_Person_role_employee3, CompanyJob_Company_role_employer4, BossWorker_Job_role_worker6, BossWorker_Job_role_boss9},
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