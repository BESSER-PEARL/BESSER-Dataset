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
login_UseCase = Class(name="login_UseCase")
client_Actor = Class(name="client_Actor")
register_complaint_UseCase = Class(name="register_complaint_UseCase")
view_status_UseCase = Class(name="view_status_UseCase")
logout_UseCase = Class(name="logout_UseCase")
administrator_Actor = Class(name="administrator_Actor")
create_user_UseCase = Class(name="create_user_UseCase")
search_user_UseCase = Class(name="search_user_UseCase")
technical_team_Actor = Class(name="technical_team_Actor")
login_technical_UseCase = Class(name="login_technical_UseCase")
new_complaint_details_UseCase = Class(name="new_complaint_details_UseCase")
find_out_fault_UseCase = Class(name="find_out_fault_UseCase")
send_to_admin_UseCase = Class(name="send_to_admin_UseCase")
logout_technician_UseCase = Class(name="logout_technician_UseCase")
customer = Class(name="customer")
monitor_complaint = Class(name="monitor_complaint")
administrator = Class(name="administrator")
update_status = Class(name="update_status")
register_complaint = Class(name="register_complaint")
check_status = Class(name="check_status")
logout = Class(name="logout")
D_B_details = Class(name="D_B_details")
login = Class(name="login")
Customer = Class(name="Customer")
MonitorComplaint = Class(name="MonitorComplaint")
RegisterComplaint = Class(name="RegisterComplaint")
Administrator = Class(name="Administrator")
UpdateStatus = Class(name="UpdateStatus")
Logout = Class(name="Logout")
CheckStatus = Class(name="CheckStatus")
DbDetails = Class(name="DbDetails")
Login = Class(name="Login")

# login_UseCase class attributes and methods

# client_Actor class attributes and methods

# register_complaint_UseCase class attributes and methods

# view_status_UseCase class attributes and methods

# logout_UseCase class attributes and methods

# administrator_Actor class attributes and methods

# create_user_UseCase class attributes and methods

# search_user_UseCase class attributes and methods

# technical_team_Actor class attributes and methods

# login_technical_UseCase class attributes and methods

# new_complaint_details_UseCase class attributes and methods

# find_out_fault_UseCase class attributes and methods

# send_to_admin_UseCase class attributes and methods

# logout_technician_UseCase class attributes and methods

# customer class attributes and methods
customer_product_id: Property = Property(name="product_id", type=StringType)
customer_email_id: Property = Property(name="email_id", type=IntegerType)
customer_name: Property = Property(name="name", type=StringType)
customer_address: Property = Property(name="address", type=StringType)
customer.attributes={customer_product_id, customer_address, customer_email_id, customer_name}

# monitor_complaint class attributes and methods
monitor_complaint_complaintid: Property = Property(name="complaintid", type=IntegerType)
monitor_complaint_complaint_type: Property = Property(name="complaint_type", type=StringType)
monitor_complaint_date: Property = Property(name="date", type=StringType)
monitor_complaint.attributes={monitor_complaint_complaint_type, monitor_complaint_complaintid, monitor_complaint_date}

# administrator class attributes and methods
administrator_username: Property = Property(name="username", type=StringType)
administrator_password: Property = Property(name="password", type=StringType)
administrator.attributes={administrator_password, administrator_username}

# update_status class attributes and methods
update_status_supdate: Property = Property(name="supdate", type=StringType)
update_status.attributes={update_status_supdate}

# register_complaint class attributes and methods
register_complaint_complaint_type: Property = Property(name="complaint_type", type=StringType)
register_complaint_description: Property = Property(name="description", type=StringType)
register_complaint.attributes={register_complaint_description, register_complaint_complaint_type}

# check_status class attributes and methods
check_status_complaint: Property = Property(name="complaint", type=StringType)
check_status.attributes={check_status_complaint}

# logout class attributes and methods
logout_session_out: Property = Property(name="session_out", type=StringType)
logout.attributes={logout_session_out}

# D_B_details class attributes and methods
D_B_details_logged_in: Property = Property(name="logged_in", type=StringType)
D_B_details_session_out: Property = Property(name="session_out", type=StringType)
D_B_details.attributes={D_B_details_logged_in, D_B_details_session_out}

# login class attributes and methods
login_username: Property = Property(name="username", type=StringType)
login_password: Property = Property(name="password", type=StringType)
login.attributes={login_password, login_username}

# Customer class attributes and methods

# MonitorComplaint class attributes and methods

# RegisterComplaint class attributes and methods

# Administrator class attributes and methods
Administrator_password: Property = Property(name="password", type=StringType)
Administrator.attributes={Administrator_password}

# UpdateStatus class attributes and methods

# Logout class attributes and methods

# CheckStatus class attributes and methods

# DbDetails class attributes and methods

# Login class attributes and methods

# Relationships
client_register_complaint: BinaryAssociation = BinaryAssociation(
    name="client_register_complaint",
    ends={
        Property(name="register_complaint0", type=register_complaint_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client1", type=client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
client_login: BinaryAssociation = BinaryAssociation(
    name="client_login",
    ends={
        Property(name="login2", type=login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client3", type=client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
client_view_status: BinaryAssociation = BinaryAssociation(
    name="client_view_status",
    ends={
        Property(name="view_status4", type=view_status_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client5", type=client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
client_logout: BinaryAssociation = BinaryAssociation(
    name="client_logout",
    ends={
        Property(name="logout6", type=logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client7", type=client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
administrator_login: BinaryAssociation = BinaryAssociation(
    name="administrator_login",
    ends={
        Property(name="login8", type=login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator9", type=administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
administrator_logout: BinaryAssociation = BinaryAssociation(
    name="administrator_logout",
    ends={
        Property(name="logout10", type=logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator11", type=administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
administrator_create_user: BinaryAssociation = BinaryAssociation(
    name="administrator_create_user",
    ends={
        Property(name="create_user12", type=create_user_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator13", type=administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
administrator_search_user: BinaryAssociation = BinaryAssociation(
    name="administrator_search_user",
    ends={
        Property(name="search_user14", type=search_user_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator15", type=administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
technical_team_login_technical: BinaryAssociation = BinaryAssociation(
    name="technical_team_login_technical",
    ends={
        Property(name="login_technical16", type=login_technical_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="technical_team17", type=technical_team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
technical_team_new_complaint_details: BinaryAssociation = BinaryAssociation(
    name="technical_team_new_complaint_details",
    ends={
        Property(name="new_complaint_details18", type=new_complaint_details_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="technical_team19", type=technical_team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
technical_team_find_out_fault: BinaryAssociation = BinaryAssociation(
    name="technical_team_find_out_fault",
    ends={
        Property(name="find_out_fault20", type=find_out_fault_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="technical_team21", type=technical_team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
technical_team_send_to_admin: BinaryAssociation = BinaryAssociation(
    name="technical_team_send_to_admin",
    ends={
        Property(name="send_to_admin22", type=send_to_admin_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="technical_team23", type=technical_team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
technical_team_logout_technician: BinaryAssociation = BinaryAssociation(
    name="technical_team_logout_technician",
    ends={
        Property(name="logout_technician24", type=logout_technician_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="technical_team25", type=technical_team_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_lssegE5HEeqesv9gci_YTQ",
    types={login_UseCase, client_Actor, register_complaint_UseCase, view_status_UseCase, logout_UseCase, administrator_Actor, create_user_UseCase, search_user_UseCase, technical_team_Actor, login_technical_UseCase, new_complaint_details_UseCase, find_out_fault_UseCase, send_to_admin_UseCase, logout_technician_UseCase, customer, monitor_complaint, administrator, update_status, register_complaint, check_status, logout, D_B_details, login, Customer, MonitorComplaint, RegisterComplaint, Administrator, UpdateStatus, Logout, CheckStatus, DbDetails, Login},
    associations={client_register_complaint, client_login, client_view_status, client_logout, administrator_login, administrator_logout, administrator_create_user, administrator_search_user, technical_team_login_technical, technical_team_new_complaint_details, technical_team_find_out_fault, technical_team_send_to_admin, technical_team_logout_technician},
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