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
Profile = Class(name="Profile")
SuperAdmin = Class(name="SuperAdmin")
void = Class(name="void")
Admin = Class(name="Admin")
Volunteer = Class(name="Volunteer")
Login = Class(name="Login")
Logout = Class(name="Logout")
Payment = Class(name="Payment")
Mail = Class(name="Mail")

# Profile class attributes and methods
Profile_l_Name: Property = Property(name="l_Name", type=StringType)
Profile_user_Name: Property = Property(name="user_Name", type=StringType)
Profile_password: Property = Property(name="password", type=StringType)
Profile_f_Name: Property = Property(name="f_Name", type=StringType)
Profile.attributes={Profile_user_Name, Profile_password, Profile_l_Name, Profile_f_Name}

# SuperAdmin class attributes and methods
SuperAdmin_userID: Property = Property(name="userID", type=IntegerType)
SuperAdmin_userName: Property = Property(name="userName", type=StringType)
SuperAdmin_password: Property = Property(name="password", type=StringType)
SuperAdmin.attributes={SuperAdmin_password, SuperAdmin_userName, SuperAdmin_userID}

# void class attributes and methods

# Admin class attributes and methods
Admin_userID: Property = Property(name="userID", type=IntegerType)
Admin_userName: Property = Property(name="userName", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin.attributes={Admin_userID, Admin_userName, Admin_password}

# Volunteer class attributes and methods
Volunteer_userID: Property = Property(name="userID", type=IntegerType)
Volunteer_userName: Property = Property(name="userName", type=StringType)
Volunteer_password: Property = Property(name="password", type=StringType)
Volunteer.attributes={Volunteer_userID, Volunteer_password, Volunteer_userName}

# Login class attributes and methods
Login_userID: Property = Property(name="userID", type=Profile)
Login_loggedinTime: Property = Property(name="loggedinTime", type=StringType)
Login_loggedoutTime: Property = Property(name="loggedoutTime", type=StringType)
Login.attributes={Login_loggedoutTime, Login_loggedinTime, Login_userID}

# Logout class attributes and methods

# Payment class attributes and methods
Payment_amount: Property = Property(name="amount", type=IntegerType)
Payment_cardType: Property = Property(name="cardType", type=StringType)
Payment_cardNumber: Property = Property(name="cardNumber", type=IntegerType)
Payment_issuerName: Property = Property(name="issuerName", type=StringType)
Payment_expiryDate: Property = Property(name="expiryDate", type=StringType)
Payment.attributes={Payment_amount, Payment_expiryDate, Payment_cardNumber, Payment_cardType, Payment_issuerName}

# Mail class attributes and methods
Mail_emailID: Property = Property(name="emailID", type=StringType)
Mail_sendTo: Property = Property(name="sendTo", type=StringType)
Mail_sendBy: Property = Property(name="sendBy", type=StringType)
Mail_subject: Property = Property(name="subject", type=StringType)
Mail.attributes={Mail_emailID, Mail_subject, Mail_sendTo, Mail_sendBy}

# Relationships
SuperAdmin_Payment: BinaryAssociation = BinaryAssociation(
    name="SuperAdmin_Payment",
    ends={
        Property(name="payment0", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="superAdmin1", type=SuperAdmin, multiplicity=Multiplicity(0, 9999))
    }
)
Volunteer_Payment: BinaryAssociation = BinaryAssociation(
    name="Volunteer_Payment",
    ends={
        Property(name="payment2", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="volunteer3", type=Volunteer, multiplicity=Multiplicity(0, 9999))
    }
)
Admin_Payment: BinaryAssociation = BinaryAssociation(
    name="Admin_Payment",
    ends={
        Property(name="payment4", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="admin5", type=Admin, multiplicity=Multiplicity(0, 9999))
    }
)
SuperAdmin_Mail: BinaryAssociation = BinaryAssociation(
    name="SuperAdmin_Mail",
    ends={
        Property(name="mail6", type=Mail, multiplicity=Multiplicity(0, 9999)),
        Property(name="superAdmin7", type=SuperAdmin, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Mail: BinaryAssociation = BinaryAssociation(
    name="Admin_Mail",
    ends={
        Property(name="mail8", type=Mail, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin9", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_70b7a514_91e6_4094_8409_dabb7b13d18a",
    types={Profile, SuperAdmin, void, Admin, Volunteer, Login, Logout, Payment, Mail},
    associations={SuperAdmin_Payment, Volunteer_Payment, Admin_Payment, SuperAdmin_Mail, Admin_Mail},
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