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
Administrator_Actor = Class(name="Administrator_Actor")
employer_Actor = Class(name="employer_Actor")
job_seeker_Actor = Class(name="job_seeker_Actor")
log_in_UseCase = Class(name="log_in_UseCase")
list_of_jobs_available_UseCase = Class(name="list_of_jobs_available_UseCase")
seeking_for_job_UseCase = Class(name="seeking_for_job_UseCase")
educational_qualification_UseCase = Class(name="educational_qualification_UseCase")
UseCase_UseCase = Class(name="UseCase_UseCase")
Actor_Actor = Class(name="Actor_Actor")
admin_Actor = Class(name="admin_Actor")
Actor2_Actor = Class(name="Actor2_Actor")
Actor3_Actor = Class(name="Actor3_Actor")
login_UseCase = Class(name="login_UseCase")
job_offer_UseCase = Class(name="job_offer_UseCase")
MyClass = Class(name="MyClass")
admin_Actor1 = Class(name="admin_Actor1")
job_seeker_Actor1 = Class(name="job_seeker_Actor1")
Actor4_Actor = Class(name="Actor4_Actor")
admin_Actor2 = Class(name="admin_Actor2")
job_seeker_Actor2 = Class(name="job_seeker_Actor2")
employer_Actor1 = Class(name="employer_Actor1")
login_UseCase1 = Class(name="login_UseCase1")
job_offers_UseCase = Class(name="job_offers_UseCase")
educational_qualification_UseCase1 = Class(name="educational_qualification_UseCase1")
list_of_jobs_related_to_graduation_UseCase = Class(name="list_of_jobs_related_to_graduation_UseCase")
job_vacancies_UseCase = Class(name="job_vacancies_UseCase")
logout_UseCase = Class(name="logout_UseCase")
Job_Seeker_Actor = Class(name="Job_Seeker_Actor")
Administrator_Actor1 = Class(name="Administrator_Actor1")
Employer_Actor = Class(name="Employer_Actor")
login_UseCase2 = Class(name="login_UseCase2")
apply_for_job_UseCase = Class(name="apply_for_job_UseCase")
post_resume_UseCase = Class(name="post_resume_UseCase")
search_jobs_UseCase = Class(name="search_jobs_UseCase")
Manage_database_UseCase = Class(name="Manage_database_UseCase")
Update_categories_UseCase = Class(name="Update_categories_UseCase")
Response_to_users_employee_to_job_seekers__UseCase = Class(name="Response_to_users_employee_to_job_seekers__UseCase")
search_job_UseCase = Class(name="search_job_UseCase")
post_job_UseCase = Class(name="post_job_UseCase")
add_update_and_delete_job_UseCase = Class(name="add_update_and_delete_job_UseCase")
User = Class(name="User")
Employer = Class(name="Employer")
Administrator = Class(name="Administrator")
JobSeeker = Class(name="JobSeeker")

# Administrator_Actor class attributes and methods

# employer_Actor class attributes and methods

# job_seeker_Actor class attributes and methods

# log_in_UseCase class attributes and methods

# list_of_jobs_available_UseCase class attributes and methods

# seeking_for_job_UseCase class attributes and methods

# educational_qualification_UseCase class attributes and methods

# UseCase_UseCase class attributes and methods

# Actor_Actor class attributes and methods

# admin_Actor class attributes and methods

# Actor2_Actor class attributes and methods

# Actor3_Actor class attributes and methods

# login_UseCase class attributes and methods

# job_offer_UseCase class attributes and methods

# MyClass class attributes and methods

# admin_Actor1 class attributes and methods

# job_seeker_Actor1 class attributes and methods

# Actor4_Actor class attributes and methods

# admin_Actor2 class attributes and methods

# job_seeker_Actor2 class attributes and methods

# employer_Actor1 class attributes and methods

# login_UseCase1 class attributes and methods

# job_offers_UseCase class attributes and methods

# educational_qualification_UseCase1 class attributes and methods

# list_of_jobs_related_to_graduation_UseCase class attributes and methods

# job_vacancies_UseCase class attributes and methods

# logout_UseCase class attributes and methods

# Job_Seeker_Actor class attributes and methods

# Administrator_Actor1 class attributes and methods

# Employer_Actor class attributes and methods

# login_UseCase2 class attributes and methods

# apply_for_job_UseCase class attributes and methods

# post_resume_UseCase class attributes and methods

# search_jobs_UseCase class attributes and methods

# Manage_database_UseCase class attributes and methods

# Update_categories_UseCase class attributes and methods

# Response_to_users_employee_to_job_seekers__UseCase class attributes and methods

# search_job_UseCase class attributes and methods

# post_job_UseCase class attributes and methods

# add_update_and_delete_job_UseCase class attributes and methods

# User class attributes and methods
User_Name: Property = Property(name="Name", type=StringType)
User_Address: Property = Property(name="Address", type=StringType)
User.attributes={User_Name, User_Address}

# Employer class attributes and methods
Employer_Name: Property = Property(name="Name", type=StringType)
Employer_Address: Property = Property(name="Address", type=StringType)
Employer.attributes={Employer_Name, Employer_Address}

# Administrator class attributes and methods
Administrator_Name: Property = Property(name="Name", type=StringType)
Administrator_Address: Property = Property(name="Address", type=StringType)
Administrator_Company: Property = Property(name="Company", type=StringType)
Administrator.attributes={Administrator_Name, Administrator_Company, Administrator_Address}

# JobSeeker class attributes and methods
JobSeeker_Name: Property = Property(name="Name", type=StringType)
JobSeeker_Qualification: Property = Property(name="Qualification", type=StringType)
JobSeeker_Experience: Property = Property(name="Experience", type=StringType)
JobSeeker.attributes={JobSeeker_Qualification, JobSeeker_Name, JobSeeker_Experience}

# Relationships
Employer_login: BinaryAssociation = BinaryAssociation(
    name="Employer_login",
    ends={
        Property(name="login14", type=login_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="employer15", type=Employer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_login: BinaryAssociation = BinaryAssociation(
    name="Administrator_login",
    ends={
        Property(name="login16", type=login_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator17", type=Administrator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Job_Seeker_search_jobs: BinaryAssociation = BinaryAssociation(
    name="Job_Seeker_search_jobs",
    ends={
        Property(name="search_jobs18", type=search_jobs_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="job_Seeker19", type=Job_Seeker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Job_Seeker_apply_for_job: BinaryAssociation = BinaryAssociation(
    name="Job_Seeker_apply_for_job",
    ends={
        Property(name="apply_for_job20", type=apply_for_job_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="job_Seeker21", type=Job_Seeker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Job_Seeker_post_resume: BinaryAssociation = BinaryAssociation(
    name="Job_Seeker_post_resume",
    ends={
        Property(name="post_resume22", type=post_resume_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="job_Seeker23", type=Job_Seeker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Manage_database: BinaryAssociation = BinaryAssociation(
    name="Administrator_Manage_database",
    ends={
        Property(name="manage_database24", type=Manage_database_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator25", type=Administrator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Update_categories: BinaryAssociation = BinaryAssociation(
    name="Administrator_Update_categories",
    ends={
        Property(name="update_categories26", type=Update_categories_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator27", type=Administrator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Response_to_users: BinaryAssociation = BinaryAssociation(
    name="Administrator_Response_to_users",
    ends={
        Property(name="response_to_users28", type=Response_to_users_employee_to_job_seekers__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator29", type=Administrator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Employer_search_job: BinaryAssociation = BinaryAssociation(
    name="Employer_search_job",
    ends={
        Property(name="search_job30", type=search_job_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employer31", type=Employer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employer_post_job: BinaryAssociation = BinaryAssociation(
    name="Employer_post_job",
    ends={
        Property(name="post_job32", type=post_job_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employer33", type=Employer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
job_seeker_login: BinaryAssociation = BinaryAssociation(
    name="job_seeker_login",
    ends={
        Property(name="login0", type=login_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="job_seeker1", type=job_seeker_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
admin_login: BinaryAssociation = BinaryAssociation(
    name="admin_login",
    ends={
        Property(name="login2", type=login_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="admin3", type=admin_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Actor5_logout: BinaryAssociation = BinaryAssociation(
    name="Actor5_logout",
    ends={
        Property(name="logout4", type=logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor55", type=employer_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Actor5_login: BinaryAssociation = BinaryAssociation(
    name="Actor5_login",
    ends={
        Property(name="login6", type=login_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="actor57", type=employer_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
admin_logout: BinaryAssociation = BinaryAssociation(
    name="admin_logout",
    ends={
        Property(name="logout8", type=logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin9", type=admin_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
job_seeker_logout: BinaryAssociation = BinaryAssociation(
    name="job_seeker_logout",
    ends={
        Property(name="logout10", type=logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="job_seeker11", type=job_seeker_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Job_Seeker_login: BinaryAssociation = BinaryAssociation(
    name="Job_Seeker_login",
    ends={
        Property(name="login12", type=login_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="job_Seeker13", type=Job_Seeker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employer_add_update_and_delete_job: BinaryAssociation = BinaryAssociation(
    name="Employer_add_update_and_delete_job",
    ends={
        Property(name="add_update_and_delete_job34", type=add_update_and_delete_job_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employer35", type=Employer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employer_Administrator: BinaryAssociation = BinaryAssociation(
    name="Employer_Administrator",
    ends={
        Property(name="administrator36", type=Administrator, multiplicity=Multiplicity(0, 1)),
        Property(name="employer37", type=Employer, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Job_seeker: BinaryAssociation = BinaryAssociation(
    name="Administrator_Job_seeker",
    ends={
        Property(name="jobseeker38", type=JobSeeker, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator39", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_378e7a2c_5b4b_4cc9_a6c1_28c30b3f4e9a",
    types={Administrator_Actor, employer_Actor, job_seeker_Actor, log_in_UseCase, list_of_jobs_available_UseCase, seeking_for_job_UseCase, educational_qualification_UseCase, UseCase_UseCase, Actor_Actor, admin_Actor, Actor2_Actor, Actor3_Actor, login_UseCase, job_offer_UseCase, MyClass, admin_Actor1, job_seeker_Actor1, Actor4_Actor, admin_Actor2, job_seeker_Actor2, employer_Actor1, login_UseCase1, job_offers_UseCase, educational_qualification_UseCase1, list_of_jobs_related_to_graduation_UseCase, job_vacancies_UseCase, logout_UseCase, Job_Seeker_Actor, Administrator_Actor1, Employer_Actor, login_UseCase2, apply_for_job_UseCase, post_resume_UseCase, search_jobs_UseCase, Manage_database_UseCase, Update_categories_UseCase, Response_to_users_employee_to_job_seekers__UseCase, search_job_UseCase, post_job_UseCase, add_update_and_delete_job_UseCase, User, Employer, Administrator, JobSeeker},
    associations={Employer_login, Administrator_login, Job_Seeker_search_jobs, Job_Seeker_apply_for_job, Job_Seeker_post_resume, Administrator_Manage_database, Administrator_Update_categories, Administrator_Response_to_users, Employer_search_job, Employer_post_job, job_seeker_login, admin_login, Actor5_logout, Actor5_login, admin_logout, job_seeker_logout, Job_Seeker_login, Employer_add_update_and_delete_job, Employer_Administrator, Administrator_Job_seeker},
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