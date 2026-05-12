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
Executive_Director = Class(name="Executive_Director")
void = Class(name="void")
Normal_user = Class(name="Normal_user")
Admin = Class(name="Admin")
Volunteer = Class(name="Volunteer")
Calender_Event = Class(name="Calender_Event")
System_Login = Class(name="System_Login")
Attendance = Class(name="Attendance")
Logout = Class(name="Logout")
Donations = Class(name="Donations")
Mail = Class(name="Mail")
Volunteer_Forms = Class(name="Volunteer_Forms")

# Profile class attributes and methods
Profile_first_Name: Property = Property(name="first_Name", type=StringType)
Profile_last_Name: Property = Property(name="last_Name", type=StringType)
Profile_user_Name: Property = Property(name="user_Name", type=StringType)
Profile_password: Property = Property(name="password", type=StringType)
Profile_phone_Number: Property = Property(name="phone_Number", type=IntegerType)
Profile.attributes={Profile_last_Name, Profile_phone_Number, Profile_first_Name, Profile_password, Profile_user_Name}

# Executive_Director class attributes and methods
Executive_Director_userID: Property = Property(name="userID", type=IntegerType)
Executive_Director_userName: Property = Property(name="userName", type=StringType)
Executive_Director_password: Property = Property(name="password", type=StringType)
Executive_Director.attributes={Executive_Director_password, Executive_Director_userName, Executive_Director_userID}

# void class attributes and methods

# Normal_user class attributes and methods
Normal_user_userID: Property = Property(name="userID", type=IntegerType)
Normal_user_userName: Property = Property(name="userName", type=StringType)
Normal_user_password: Property = Property(name="password", type=StringType)
Normal_user.attributes={Normal_user_password, Normal_user_userID, Normal_user_userName}

# Admin class attributes and methods
Admin_userID: Property = Property(name="userID", type=IntegerType)
Admin_userName: Property = Property(name="userName", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin.attributes={Admin_userName, Admin_password, Admin_userID}

# Volunteer class attributes and methods
Volunteer_userID: Property = Property(name="userID", type=IntegerType)
Volunteer_userName: Property = Property(name="userName", type=StringType)
Volunteer_password: Property = Property(name="password", type=StringType)
Volunteer.attributes={Volunteer_password, Volunteer_userID, Volunteer_userName}

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
Calender_Event.attributes={Calender_Event_eventType, Calender_Event_participantAmount, Calender_Event_nomarlUser, Calender_Event_date, Calender_Event_volunteer, Calender_Event_category, Calender_Event_admin, Calender_Event_time, Calender_Event_description}

# System_Login class attributes and methods
System_Login_userID: Property = Property(name="userID", type=Profile)
System_Login_loggedinTime: Property = Property(name="loggedinTime", type=StringType)
System_Login_loggedoutTime: Property = Property(name="loggedoutTime", type=StringType)
System_Login.attributes={System_Login_userID, System_Login_loggedoutTime, System_Login_loggedinTime}

# Attendance class attributes and methods
Attendance_attendanceID: Property = Property(name="attendanceID", type=IntegerType)
Attendance_checkInTime: Property = Property(name="checkInTime", type=StringType)
Attendance_checkOutTime: Property = Property(name="checkOutTime", type=StringType)
Attendance.attributes={Attendance_attendanceID, Attendance_checkOutTime, Attendance_checkInTime}

# Logout class attributes and methods

# Donations class attributes and methods
Donations_amount: Property = Property(name="amount", type=IntegerType)
Donations_cardType: Property = Property(name="cardType", type=StringType)
Donations_cardNumber: Property = Property(name="cardNumber", type=IntegerType)
Donations_issuerName: Property = Property(name="issuerName", type=StringType)
Donations_expirationDate: Property = Property(name="expirationDate", type=IntegerType)
Donations.attributes={Donations_expirationDate, Donations_issuerName, Donations_amount, Donations_cardType, Donations_cardNumber}

# Mail class attributes and methods
Mail_emailID: Property = Property(name="emailID", type=StringType)
Mail_sendTo: Property = Property(name="sendTo", type=StringType)
Mail_sendBy: Property = Property(name="sendBy", type=StringType)
Mail_subject: Property = Property(name="subject", type=StringType)
Mail.attributes={Mail_sendTo, Mail_sendBy, Mail_emailID, Mail_subject}

# Volunteer_Forms class attributes and methods
Volunteer_Forms_userName: Property = Property(name="userName", type=StringType)
Volunteer_Forms_password: Property = Property(name="password", type=StringType)
Volunteer_Forms_userID: Property = Property(name="userID", type=IntegerType)
Volunteer_Forms.attributes={Volunteer_Forms_password, Volunteer_Forms_userName, Volunteer_Forms_userID}

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
        Property(name="Add_Edit_Vew7", type=Executive_Director, multiplicity=Multiplicity(0, 9999))
    }
)
Profile_Attendance: BinaryAssociation = BinaryAssociation(
    name="Profile_Attendance",
    ends={
        Property(name="Track_Attendance8", type=Attendance, multiplicity=Multiplicity(0, 1)),
        Property(name="profile9", type=Profile, multiplicity=Multiplicity(0, 1))
    }
)
SuperAdmin_Donations: BinaryAssociation = BinaryAssociation(
    name="SuperAdmin_Donations",
    ends={
        Property(name="payment10", type=Donations, multiplicity=Multiplicity(0, 1)),
        Property(name="superAdmin11", type=Executive_Director, multiplicity=Multiplicity(0, 9999))
    }
)
Volunteer_Donations: BinaryAssociation = BinaryAssociation(
    name="Volunteer_Donations",
    ends={
        Property(name="payment12", type=Donations, multiplicity=Multiplicity(0, 1)),
        Property(name="volunteer13", type=Volunteer, multiplicity=Multiplicity(0, 9999))
    }
)
Admin_Donations: BinaryAssociation = BinaryAssociation(
    name="Admin_Donations",
    ends={
        Property(name="donation14", type=Donations, multiplicity=Multiplicity(0, 1)),
        Property(name="admin15", type=Admin, multiplicity=Multiplicity(0, 9999))
    }
)
Normal_user_Donations: BinaryAssociation = BinaryAssociation(
    name="Normal_user_Donations",
    ends={
        Property(name="donation216", type=Donations, multiplicity=Multiplicity(0, 1)),
        Property(name="normal_user17", type=Normal_user, multiplicity=Multiplicity(0, 9999))
    }
)
SuperAdmin_Mail: BinaryAssociation = BinaryAssociation(
    name="SuperAdmin_Mail",
    ends={
        Property(name="mail18", type=Mail, multiplicity=Multiplicity(0, 9999)),
        Property(name="superAdmin19", type=Executive_Director, multiplicity=Multiplicity(0, 1))
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
    name="d3006d70_595e_40d5_9665_55e81efa333f",
    types={Profile, Executive_Director, void, Normal_user, Admin, Volunteer, Calender_Event, System_Login, Attendance, Logout, Donations, Mail, Volunteer_Forms},
    associations={Volunteer_Calender_Event, Admin_Calender_Event, Normal_user_Calender_Event, SuperAdmin_Calender_Event, Profile_Attendance, SuperAdmin_Donations, Volunteer_Donations, Admin_Donations, Normal_user_Donations, SuperAdmin_Mail, Admin_Mail},
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