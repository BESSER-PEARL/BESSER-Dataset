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
OrgType: Enumeration = Enumeration(
    name="OrgType",
    literals={
            EnumerationLiteral(name="department"),
			EnumerationLiteral(name="school"),
			EnumerationLiteral(name="major"),
			EnumerationLiteral(name="Misc"),
			EnumerationLiteral(name="Discipline"),
			EnumerationLiteral(name="Specjalization")
    }
)

Role: Enumeration = Enumeration(
    name="Role",
    literals={
            EnumerationLiteral(name="student"),
			EnumerationLiteral(name="teacher")
    }
)

# Classes
dXP_OneRoster = Class(name="dXP::OneRoster")
dXP_AcademicSession = Class(name="dXP::AcademicSession")
dXP_Org = Class(name="dXP::Org")
dXP_Enrolment = Class(name="dXP::Enrolment")
dXP_Course = Class(name="dXP::Course")
Base = Class(name="Base")
dXP_Class = Class(name="dXP::Class")
dXP_Base = Class(name="dXP::Base", is_abstract=True)
dXP_Metadata = Class(name="dXP::Metadata")
dXP_UserId = Class(name="dXP::UserId")
dXP_User = Class(name="dXP::User")
dXP_OrgUnit = Class(name="dXP::OrgUnit")
Org = Class(name="Org")

# dXP_OneRoster class attributes and methods

# dXP_AcademicSession class attributes and methods
dXP_AcademicSession_title: Property = Property(name="title", type=StringType)
dXP_AcademicSession_startDate: Property = Property(name="startDate", type=StringType)
dXP_AcademicSession_endDate: Property = Property(name="endDate", type=StringType)
dXP_AcademicSession_schoolYear: Property = Property(name="schoolYear", type=StringType)
dXP_AcademicSession_type: Property = Property(name="type", type=StringType)
dXP_AcademicSession.attributes={dXP_AcademicSession_title, dXP_AcademicSession_schoolYear, dXP_AcademicSession_type, dXP_AcademicSession_startDate, dXP_AcademicSession_endDate}

# dXP_Org class attributes and methods
dXP_Org_name: Property = Property(name="name", type=StringType)
dXP_Org_type: Property = Property(name="type", type=StringType)
dXP_Org.attributes={dXP_Org_type, dXP_Org_name}

# dXP_Enrolment class attributes and methods
dXP_Enrolment_role: Property = Property(name="role", type=StringType)
dXP_Enrolment_primary: Property = Property(name="primary", type=StringType)
dXP_Enrolment.attributes={dXP_Enrolment_primary, dXP_Enrolment_role}

# dXP_Course class attributes and methods
dXP_Course_title: Property = Property(name="title", type=StringType)
dXP_Course_courseCode: Property = Property(name="courseCode", type=StringType)
dXP_Course.attributes={dXP_Course_courseCode, dXP_Course_title}

# Base class attributes and methods

# dXP_Class class attributes and methods
dXP_Class_title: Property = Property(name="title", type=StringType)
dXP_Class_classCode: Property = Property(name="classCode", type=StringType)
dXP_Class_classType: Property = Property(name="classType", type=StringType)
dXP_Class_location: Property = Property(name="location", type=StringType)
dXP_Class.attributes={dXP_Class_location, dXP_Class_title, dXP_Class_classType, dXP_Class_classCode}

# dXP_Base class attributes and methods
dXP_Base_sourceId: Property = Property(name="sourceId", type=StringType)
dXP_Base_status: Property = Property(name="status", type=StringType)
dXP_Base_dateLastModified: Property = Property(name="dateLastModified", type=StringType)
dXP_Base.attributes={dXP_Base_status, dXP_Base_dateLastModified, dXP_Base_sourceId}

# dXP_Metadata class attributes and methods
dXP_Metadata_key: Property = Property(name="key", type=StringType)
dXP_Metadata_value: Property = Property(name="value", type=StringType)
dXP_Metadata.attributes={dXP_Metadata_value, dXP_Metadata_key}

# dXP_UserId class attributes and methods
dXP_UserId_type: Property = Property(name="type", type=StringType)
dXP_UserId_identifier: Property = Property(name="identifier", type=StringType)
dXP_UserId.attributes={dXP_UserId_identifier, dXP_UserId_type}

# dXP_User class attributes and methods
dXP_User_userName: Property = Property(name="userName", type=StringType)
dXP_User_enabledUser: Property = Property(name="enabledUser", type=StringType)
dXP_User_role: Property = Property(name="role", type=StringType)
dXP_User_identifier: Property = Property(name="identifier", type=StringType)
dXP_User.attributes={dXP_User_role, dXP_User_identifier, dXP_User_userName, dXP_User_enabledUser}

# dXP_OrgUnit class attributes and methods

# Org class attributes and methods

# Relationships
academicsession0: BinaryAssociation = BinaryAssociation(
    name="academicsession0",
    ends={
        Property(name="dXP_AcademicSession", type=dXP_OneRoster, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_OneRoster", type=dXP_AcademicSession, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
org1: BinaryAssociation = BinaryAssociation(
    name="org1",
    ends={
        Property(name="dXP_Org", type=dXP_OneRoster, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_OneRoster2", type=dXP_Org, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class5: BinaryAssociation = BinaryAssociation(
    name="class5",
    ends={
        Property(name="dXP_Class", type=dXP_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_Course", type=dXP_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metadata6: BinaryAssociation = BinaryAssociation(
    name="metadata6",
    ends={
        Property(name="dXP_Metadata", type=dXP_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_Base", type=dXP_Metadata, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enrolment3: BinaryAssociation = BinaryAssociation(
    name="enrolment3",
    ends={
        Property(name="dXP_Enrolment", type=dXP_OneRoster, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_OneRoster4", type=dXP_Enrolment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user10: BinaryAssociation = BinaryAssociation(
    name="user10",
    ends={
        Property(name="dXP_User", type=dXP_AcademicSession, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_AcademicSession11", type=dXP_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userid12: BinaryAssociation = BinaryAssociation(
    name="userid12",
    ends={
        Property(name="dXP_UserId", type=dXP_User, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_User13", type=dXP_UserId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course7: BinaryAssociation = BinaryAssociation(
    name="course7",
    ends={
        Property(name="dXP_Course9", type=dXP_AcademicSession, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_AcademicSession8", type=dXP_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orgunit14: BinaryAssociation = BinaryAssociation(
    name="orgunit14",
    ends={
        Property(name="dXP_OrgUnit", type=dXP_Org, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_Org15", type=dXP_OrgUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user16: BinaryAssociation = BinaryAssociation(
    name="user16",
    ends={
        Property(name="dXP_User18", type=dXP_Enrolment, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_Enrolment17", type=dXP_User, multiplicity=Multiplicity(0, 1))
    }
)
class19: BinaryAssociation = BinaryAssociation(
    name="class19",
    ends={
        Property(name="dXP_Class21", type=dXP_Enrolment, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_Enrolment20", type=dXP_Class, multiplicity=Multiplicity(0, 1))
    }
)
orgunit22: BinaryAssociation = BinaryAssociation(
    name="orgunit22",
    ends={
        Property(name="dXP_OrgUnit24", type=dXP_Enrolment, multiplicity=Multiplicity(1, 1)),
        Property(name="dXP_Enrolment23", type=dXP_OrgUnit, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_dXP_Course_Base = Generalization(general=Base, specific=dXP_Course)
gen_dXP_AcademicSession_Base = Generalization(general=Base, specific=dXP_AcademicSession)
gen_dXP_Class_Base = Generalization(general=Base, specific=dXP_Class)
gen_dXP_User_Base = Generalization(general=Base, specific=dXP_User)
gen_dXP_Org_Base = Generalization(general=Base, specific=dXP_Org)
gen_dXP_OrgUnit_Org = Generalization(general=Org, specific=dXP_OrgUnit)
gen_dXP_Enrolment_Base = Generalization(general=Base, specific=dXP_Enrolment)

# Domain Model
domain_model = DomainModel(
    name="dXP",
    types={dXP_OneRoster, dXP_AcademicSession, dXP_Org, dXP_Enrolment, dXP_Course, Base, dXP_Class, dXP_Base, dXP_Metadata, dXP_UserId, dXP_User, dXP_OrgUnit, Org, OrgType, Role},
    associations={academicsession0, org1, class5, metadata6, enrolment3, user10, userid12, course7, orgunit14, user16, class19, orgunit22},
    generalizations={gen_dXP_Course_Base, gen_dXP_AcademicSession_Base, gen_dXP_Class_Base, gen_dXP_User_Base, gen_dXP_Org_Base, gen_dXP_OrgUnit_Org, gen_dXP_Enrolment_Base},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)