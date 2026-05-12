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
Job_Seeker_Actor = Class(name="Job_Seeker_Actor")
Employer_Actor = Class(name="Employer_Actor")
Registration_UseCase = Class(name="Registration_UseCase")
Admin_Actor = Class(name="Admin_Actor")
Login_UseCase = Class(name="Login_UseCase")
Apply_for_Job_UseCase = Class(name="Apply_for_Job_UseCase")
Post_Job_UseCase = Class(name="Post_Job_UseCase")
Send_Mail_UseCase = Class(name="Send_Mail_UseCase")
Manage_Accounts_UseCase = Class(name="Manage_Accounts_UseCase")
Logout_UseCase = Class(name="Logout_UseCase")
Delete_Profile_UseCase = Class(name="Delete_Profile_UseCase")
Update_Profile_UseCase = Class(name="Update_Profile_UseCase")
MyClass = Class(name="MyClass")
Actor_Actor = Class(name="Actor_Actor")

# Job_Seeker_Actor class attributes and methods

# Employer_Actor class attributes and methods

# Registration_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# Login_UseCase class attributes and methods

# Apply_for_Job_UseCase class attributes and methods

# Post_Job_UseCase class attributes and methods

# Send_Mail_UseCase class attributes and methods

# Manage_Accounts_UseCase class attributes and methods

# Logout_UseCase class attributes and methods

# Delete_Profile_UseCase class attributes and methods

# Update_Profile_UseCase class attributes and methods

# MyClass class attributes and methods

# Actor_Actor class attributes and methods

# Relationships
Job_Seeker_Registration: BinaryAssociation = BinaryAssociation(
    name="Job_Seeker_Registration",
    ends={
        Property(name="registration0", type=Registration_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="job_Seeker1", type=Job_Seeker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Job_Seeker_Login: BinaryAssociation = BinaryAssociation(
    name="Job_Seeker_Login",
    ends={
        Property(name="login2", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="job_Seeker3", type=Job_Seeker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Post_Job_Admin: BinaryAssociation = BinaryAssociation(
    name="Post_Job_Admin",
    ends={
        Property(name="admin4", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="post_Job5", type=Post_Job_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Send_Mail_Admin: BinaryAssociation = BinaryAssociation(
    name="Send_Mail_Admin",
    ends={
        Property(name="admin6", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="send_Mail7", type=Send_Mail_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Logout_Employer: BinaryAssociation = BinaryAssociation(
    name="Logout_Employer",
    ends={
        Property(name="employer8", type=Employer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="logout9", type=Logout_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Logout_Admin: BinaryAssociation = BinaryAssociation(
    name="Logout_Admin",
    ends={
        Property(name="admin10", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="logout11", type=Logout_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Manage_Accounts: BinaryAssociation = BinaryAssociation(
    name="Admin_Manage_Accounts",
    ends={
        Property(name="manage_Accounts12", type=Manage_Accounts_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin13", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employer_Send_Mail: BinaryAssociation = BinaryAssociation(
    name="Employer_Send_Mail",
    ends={
        Property(name="send_Mail14", type=Send_Mail_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employer15", type=Employer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Update_Profile_Job_Seeker: BinaryAssociation = BinaryAssociation(
    name="Update_Profile_Job_Seeker",
    ends={
        Property(name="job_Seeker16", type=Job_Seeker_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="update_Profile17", type=Update_Profile_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Employer_Login: BinaryAssociation = BinaryAssociation(
    name="Employer_Login",
    ends={
        Property(name="login18", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employer19", type=Employer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employer_Registration: BinaryAssociation = BinaryAssociation(
    name="Employer_Registration",
    ends={
        Property(name="registration20", type=Registration_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employer21", type=Employer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Employer_Post_Job: BinaryAssociation = BinaryAssociation(
    name="Employer_Post_Job",
    ends={
        Property(name="post_Job22", type=Post_Job_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employer23", type=Employer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Apply_for_Job_Job_Seeker: BinaryAssociation = BinaryAssociation(
    name="Apply_for_Job_Job_Seeker",
    ends={
        Property(name="job_Seeker24", type=Job_Seeker_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="apply_for_Job25", type=Apply_for_Job_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Employer_Update_Profile: BinaryAssociation = BinaryAssociation(
    name="Employer_Update_Profile",
    ends={
        Property(name="update_Profile26", type=Update_Profile_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="employer27", type=Employer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Job_Seeker_Delete_Profile: BinaryAssociation = BinaryAssociation(
    name="Job_Seeker_Delete_Profile",
    ends={
        Property(name="delete_Profile28", type=Delete_Profile_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="job_Seeker29", type=Job_Seeker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Login_Admin: BinaryAssociation = BinaryAssociation(
    name="Login_Admin",
    ends={
        Property(name="admin30", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login31", type=Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Logout_Job_Seeker: BinaryAssociation = BinaryAssociation(
    name="Logout_Job_Seeker",
    ends={
        Property(name="job_Seeker32", type=Job_Seeker_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="logout33", type=Logout_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_17b8865c_68e1_42ee_befd_d898357dcc1c",
    types={Job_Seeker_Actor, Employer_Actor, Registration_UseCase, Admin_Actor, Login_UseCase, Apply_for_Job_UseCase, Post_Job_UseCase, Send_Mail_UseCase, Manage_Accounts_UseCase, Logout_UseCase, Delete_Profile_UseCase, Update_Profile_UseCase, MyClass, Actor_Actor},
    associations={Job_Seeker_Registration, Job_Seeker_Login, Post_Job_Admin, Send_Mail_Admin, Logout_Employer, Logout_Admin, Admin_Manage_Accounts, Employer_Send_Mail, Update_Profile_Job_Seeker, Employer_Login, Employer_Registration, Employer_Post_Job, Apply_for_Job_Job_Seeker, Employer_Update_Profile, Job_Seeker_Delete_Profile, Login_Admin, Logout_Job_Seeker},
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