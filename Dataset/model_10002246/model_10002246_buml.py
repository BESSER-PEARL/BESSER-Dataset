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
Manager = Class(name="Manager")
void = Class(name="void")
Normal_user = Class(name="Normal_user")
Admin = Class(name="Admin")
Volunteer = Class(name="Volunteer")
Calender_Event = Class(name="Calender_Event")
Login = Class(name="Login")
Logout = Class(name="Logout")
Payment = Class(name="Payment")
Mail = Class(name="Mail")
Profile = Class(name="Profile")

# Manager class attributes and methods
Manager_userID: Property = Property(name="userID", type=IntegerType)
Manager_userName: Property = Property(name="userName", type=StringType)
Manager_password: Property = Property(name="password", type=StringType)
Manager.attributes={Manager_password, Manager_userID, Manager_userName}

# void class attributes and methods

# Normal_user class attributes and methods
Normal_user_userID: Property = Property(name="userID", type=IntegerType)
Normal_user_userName: Property = Property(name="userName", type=StringType)
Normal_user_password: Property = Property(name="password", type=StringType)
Normal_user.attributes={Normal_user_userName, Normal_user_userID, Normal_user_password}

# Admin class attributes and methods
Admin_userID: Property = Property(name="userID", type=IntegerType)
Admin_userName: Property = Property(name="userName", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin.attributes={Admin_password, Admin_userName, Admin_userID}

# Volunteer class attributes and methods
Volunteer_userID: Property = Property(name="userID", type=IntegerType)
Volunteer_userName: Property = Property(name="userName", type=StringType)
Volunteer_password: Property = Property(name="password", type=StringType)
Volunteer.attributes={Volunteer_userID, Volunteer_password, Volunteer_userName}

# Calender_Event class attributes and methods
Calender_Event_category: Property = Property(name="category", type=StringType)
Calender_Event_date: Property = Property(name="date", type=StringType)
Calender_Event_time: Property = Property(name="time", type=StringType)
Calender_Event_description: Property = Property(name="description", type=StringType)
Calender_Event_eventType: Property = Property(name="eventType", type=StringType)
Calender_Event_participantAmount: Property = Property(name="participantAmount", type=StringType)
Calender_Event_volunteer: Property = Property(name="volunteer", type=Volunteer)
Calender_Event_nomarlUser: Property = Property(name="nomarlUser", type=Normal_user)
Calender_Event_admin: Property = Property(name="admin", type=Admin)
Calender_Event.attributes={Calender_Event_description, Calender_Event_participantAmount, Calender_Event_date, Calender_Event_category, Calender_Event_eventType, Calender_Event_time, Calender_Event_volunteer, Calender_Event_admin, Calender_Event_nomarlUser}

# Login class attributes and methods
Login_userID: Property = Property(name="userID", type=Profile)
Login_loggedinTime: Property = Property(name="loggedinTime", type=StringType)
Login_loggedoutTime: Property = Property(name="loggedoutTime", type=StringType)
Login.attributes={Login_userID, Login_loggedinTime, Login_loggedoutTime}

# Logout class attributes and methods

# Payment class attributes and methods
Payment_amount: Property = Property(name="amount", type=IntegerType)
Payment_cardType: Property = Property(name="cardType", type=StringType)
Payment_cardNumber: Property = Property(name="cardNumber", type=IntegerType)
Payment_issuerName: Property = Property(name="issuerName", type=StringType)
Payment_expiryDate: Property = Property(name="expiryDate", type=StringType)
Payment.attributes={Payment_cardNumber, Payment_amount, Payment_issuerName, Payment_cardType, Payment_expiryDate}

# Mail class attributes and methods
Mail_emailID: Property = Property(name="emailID", type=StringType)
Mail_sendTo: Property = Property(name="sendTo", type=StringType)
Mail_sendBy: Property = Property(name="sendBy", type=StringType)
Mail_subject: Property = Property(name="subject", type=StringType)
Mail.attributes={Mail_sendBy, Mail_sendTo, Mail_subject, Mail_emailID}

# Profile class attributes and methods
Profile_f_Name: Property = Property(name="f_Name", type=StringType)
Profile_l_Name: Property = Property(name="l_Name", type=StringType)
Profile_user_Name: Property = Property(name="user_Name", type=StringType)
Profile_password: Property = Property(name="password", type=StringType)
Profile.attributes={Profile_l_Name, Profile_user_Name, Profile_f_Name, Profile_password}

# Relationships
SuperAdmin_Payment: BinaryAssociation = BinaryAssociation(
    name="SuperAdmin_Payment",
    ends={
        Property(name="payment0", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="superAdmin1", type=Manager, multiplicity=Multiplicity(0, 9999))
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
Normal_user_Payment: BinaryAssociation = BinaryAssociation(
    name="Normal_user_Payment",
    ends={
        Property(name="payment26", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="normal_user7", type=Normal_user, multiplicity=Multiplicity(0, 9999))
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
    name="_z9rnQCg8EeqqcaoAsxFIeg",
    types={Manager, void, Normal_user, Admin, Volunteer, Calender_Event, Login, Logout, Payment, Mail, Profile},
    associations={SuperAdmin_Payment, Volunteer_Payment, Admin_Payment, Normal_user_Payment, Admin_Mail},
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