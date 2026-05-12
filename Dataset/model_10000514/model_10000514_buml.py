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
Normal_user = Class(name="Normal_user")
Admin = Class(name="Admin")
Volunteer = Class(name="Volunteer")
Calender_Event = Class(name="Calender_Event")
Login = Class(name="Login")
Attendance = Class(name="Attendance")
Logout = Class(name="Logout")
Payment = Class(name="Payment")
Mail = Class(name="Mail")

# Profile class attributes and methods
Profile_f_Name: Property = Property(name="f_Name", type=StringType)
Profile_l_Name: Property = Property(name="l_Name", type=StringType)
Profile_user_Name: Property = Property(name="user_Name", type=StringType)
Profile_password: Property = Property(name="password", type=StringType)
Profile.attributes={Profile_password, Profile_f_Name, Profile_user_Name, Profile_l_Name}

# SuperAdmin class attributes and methods
SuperAdmin_userID: Property = Property(name="userID", type=IntegerType)
SuperAdmin_userName: Property = Property(name="userName", type=StringType)
SuperAdmin_password: Property = Property(name="password", type=StringType)
SuperAdmin.attributes={SuperAdmin_userID, SuperAdmin_password, SuperAdmin_userName}

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
Admin.attributes={Admin_password, Admin_userID, Admin_userName}

# Volunteer class attributes and methods
Volunteer_userID: Property = Property(name="userID", type=IntegerType)
Volunteer_userName: Property = Property(name="userName", type=StringType)
Volunteer_password: Property = Property(name="password", type=StringType)
Volunteer.attributes={Volunteer_userID, Volunteer_userName, Volunteer_password}

# Calender_Event class attributes and methods
Calender_Event_eventType: Property = Property(name="eventType", type=StringType)
Calender_Event_participantAmount: Property = Property(name="participantAmount", type=StringType)
Calender_Event_volunteer: Property = Property(name="volunteer", type=Volunteer)
Calender_Event_nomarlUser: Property = Property(name="nomarlUser", type=Normal_user)
Calender_Event_admin: Property = Property(name="admin", type=Admin)
Calender_Event_category: Property = Property(name="category", type=StringType)
Calender_Event_date: Property = Property(name="date", type=StringType)
Calender_Event_time: Property = Property(name="time", type=StringType)
Calender_Event_description: Property = Property(name="description", type=StringType)
Calender_Event.attributes={Calender_Event_eventType, Calender_Event_nomarlUser, Calender_Event_description, Calender_Event_participantAmount, Calender_Event_date, Calender_Event_category, Calender_Event_volunteer, Calender_Event_admin, Calender_Event_time}

# Login class attributes and methods
Login_userID: Property = Property(name="userID", type=Profile)
Login_loggedinTime: Property = Property(name="loggedinTime", type=StringType)
Login_loggedoutTime: Property = Property(name="loggedoutTime", type=StringType)
Login.attributes={Login_userID, Login_loggedoutTime, Login_loggedinTime}

# Attendance class attributes and methods
Attendance_attendanceID: Property = Property(name="attendanceID", type=IntegerType)
Attendance_checkInTime: Property = Property(name="checkInTime", type=StringType)
Attendance_checkOutTime: Property = Property(name="checkOutTime", type=StringType)
Attendance.attributes={Attendance_checkInTime, Attendance_attendanceID, Attendance_checkOutTime}

# Logout class attributes and methods

# Payment class attributes and methods
Payment_amount: Property = Property(name="amount", type=IntegerType)
Payment_cardType: Property = Property(name="cardType", type=StringType)
Payment_cardNumber: Property = Property(name="cardNumber", type=IntegerType)
Payment_issuerName: Property = Property(name="issuerName", type=StringType)
Payment_expiryDate: Property = Property(name="expiryDate", type=StringType)
Payment.attributes={Payment_issuerName, Payment_expiryDate, Payment_amount, Payment_cardNumber, Payment_cardType}

# Mail class attributes and methods
Mail_emailID: Property = Property(name="emailID", type=StringType)
Mail_sendTo: Property = Property(name="sendTo", type=StringType)
Mail_sendBy: Property = Property(name="sendBy", type=StringType)
Mail_subject: Property = Property(name="subject", type=StringType)
Mail.attributes={Mail_emailID, Mail_sendTo, Mail_subject, Mail_sendBy}

# Relationships
Volunteer_Calender_Event: BinaryAssociation = BinaryAssociation(
    name="Volunteer_Calender_Event",
    ends={
        Property(name="calender_Event0", type=Calender_Event, multiplicity=Multiplicity(0, 9999)),
        Property(name="Add_Edit_View1", type=Volunteer, multiplicity=Multiplicity(0, 9999))
    }
)
Admin_Calender_Event: BinaryAssociation = BinaryAssociation(
    name="Admin_Calender_Event",
    ends={
        Property(name="calender_Event2", type=Calender_Event, multiplicity=Multiplicity(0, 9999)),
        Property(name="Add_Edit_View3", type=Admin, multiplicity=Multiplicity(0, 9999))
    }
)
Normal_user_Calender_Event: BinaryAssociation = BinaryAssociation(
    name="Normal_user_Calender_Event",
    ends={
        Property(name="calender_Event4", type=Calender_Event, multiplicity=Multiplicity(0, 9999)),
        Property(name="Add_Edit_View5", type=Normal_user, multiplicity=Multiplicity(0, 1))
    }
)
SuperAdmin_Calender_Event: BinaryAssociation = BinaryAssociation(
    name="SuperAdmin_Calender_Event",
    ends={
        Property(name="calender_Event6", type=Calender_Event, multiplicity=Multiplicity(0, 9999)),
        Property(name="Add_Edit_Vew7", type=SuperAdmin, multiplicity=Multiplicity(0, 9999))
    }
)
Profile_Attendance: BinaryAssociation = BinaryAssociation(
    name="Profile_Attendance",
    ends={
        Property(name="Track_Attendance8", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="profile9", type=Profile, multiplicity=Multiplicity(0, 1))
    }
)
SuperAdmin_Payment: BinaryAssociation = BinaryAssociation(
    name="SuperAdmin_Payment",
    ends={
        Property(name="payment10", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="superAdmin11", type=SuperAdmin, multiplicity=Multiplicity(0, 9999))
    }
)
Volunteer_Payment: BinaryAssociation = BinaryAssociation(
    name="Volunteer_Payment",
    ends={
        Property(name="payment12", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="volunteer13", type=Volunteer, multiplicity=Multiplicity(0, 9999))
    }
)
Admin_Payment: BinaryAssociation = BinaryAssociation(
    name="Admin_Payment",
    ends={
        Property(name="payment14", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="admin15", type=Admin, multiplicity=Multiplicity(0, 9999))
    }
)
Normal_user_Payment: BinaryAssociation = BinaryAssociation(
    name="Normal_user_Payment",
    ends={
        Property(name="payment216", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="normal_user17", type=Normal_user, multiplicity=Multiplicity(0, 9999))
    }
)
SuperAdmin_Mail: BinaryAssociation = BinaryAssociation(
    name="SuperAdmin_Mail",
    ends={
        Property(name="mail18", type=Mail, multiplicity=Multiplicity(0, 9999)),
        Property(name="superAdmin19", type=SuperAdmin, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Mail: BinaryAssociation = BinaryAssociation(
    name="Admin_Mail",
    ends={
        Property(name="mail20", type=Mail, multiplicity=Multiplicity(0, 9999)),
        Property(name="admin21", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3f4139b9_ed3c_49d2_a207_4ea0e37cc0ac",
    types={Profile, SuperAdmin, void, Normal_user, Admin, Volunteer, Calender_Event, Login, Attendance, Logout, Payment, Mail},
    associations={Volunteer_Calender_Event, Admin_Calender_Event, Normal_user_Calender_Event, SuperAdmin_Calender_Event, Profile_Attendance, SuperAdmin_Payment, Volunteer_Payment, Admin_Payment, Normal_user_Payment, SuperAdmin_Mail, Admin_Mail},
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