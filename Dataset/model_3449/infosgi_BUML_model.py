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
Country: Enumeration = Enumeration(
    name="Country",
    literals={
            EnumerationLiteral(name="USA"),
			EnumerationLiteral(name="CAN"),
			EnumerationLiteral(name="MEX"),
			EnumerationLiteral(name="PR")
    }
)

Language: Enumeration = Enumeration(
    name="Language",
    literals={
            EnumerationLiteral(name="CHINESE"),
			EnumerationLiteral(name="KOREAN"),
			EnumerationLiteral(name="VIETNAMESE"),
			EnumerationLiteral(name="THAI"),
			EnumerationLiteral(name="OTHER"),
			EnumerationLiteral(name="ENGLISH"),
			EnumerationLiteral(name="SPANISH"),
			EnumerationLiteral(name="FRENCH"),
			EnumerationLiteral(name="ITALIAN"),
			EnumerationLiteral(name="GERMAN"),
			EnumerationLiteral(name="PORTUGUESE"),
			EnumerationLiteral(name="JAPANESE")
    }
)

PhoneNumberType: Enumeration = Enumeration(
    name="PhoneNumberType",
    literals={
            EnumerationLiteral(name="HOME"),
			EnumerationLiteral(name="WORK"),
			EnumerationLiteral(name="CELL"),
			EnumerationLiteral(name="FAX"),
			EnumerationLiteral(name="OTHER")
    }
)

RoleType: Enumeration = Enumeration(
    name="RoleType",
    literals={
            EnumerationLiteral(name="MANAGER"),
			EnumerationLiteral(name="USER"),
			EnumerationLiteral(name="HOST")
    }
)

State: Enumeration = Enumeration(
    name="State",
    literals={
            EnumerationLiteral(name="AL"),
			EnumerationLiteral(name="AK"),
			EnumerationLiteral(name="AZ"),
			EnumerationLiteral(name="AR"),
			EnumerationLiteral(name="CA"),
			EnumerationLiteral(name="CO"),
			EnumerationLiteral(name="CT"),
			EnumerationLiteral(name="DE"),
			EnumerationLiteral(name="FL"),
			EnumerationLiteral(name="GA"),
			EnumerationLiteral(name="HI"),
			EnumerationLiteral(name="ID"),
			EnumerationLiteral(name="IL"),
			EnumerationLiteral(name="ND"),
			EnumerationLiteral(name="OH"),
			EnumerationLiteral(name="OK"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="PA"),
			EnumerationLiteral(name="RI"),
			EnumerationLiteral(name="SC"),
			EnumerationLiteral(name="SD"),
			EnumerationLiteral(name="TN"),
			EnumerationLiteral(name="TX"),
			EnumerationLiteral(name="UT"),
			EnumerationLiteral(name="VT"),
			EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="IA"),
			EnumerationLiteral(name="KS"),
			EnumerationLiteral(name="KY"),
			EnumerationLiteral(name="LA"),
			EnumerationLiteral(name="ME"),
			EnumerationLiteral(name="MD"),
			EnumerationLiteral(name="MA"),
			EnumerationLiteral(name="MI"),
			EnumerationLiteral(name="MN"),
			EnumerationLiteral(name="MS"),
			EnumerationLiteral(name="MO"),
			EnumerationLiteral(name="MT"),
			EnumerationLiteral(name="NE"),
			EnumerationLiteral(name="NV"),
			EnumerationLiteral(name="NH"),
			EnumerationLiteral(name="NJ"),
			EnumerationLiteral(name="NM"),
			EnumerationLiteral(name="NY"),
			EnumerationLiteral(name="NC"),
			EnumerationLiteral(name="VA"),
			EnumerationLiteral(name="WA"),
			EnumerationLiteral(name="WV"),
			EnumerationLiteral(name="WI"),
			EnumerationLiteral(name="WY")
    }
)

Status: Enumeration = Enumeration(
    name="Status",
    literals={
            EnumerationLiteral(name="INFO"),
			EnumerationLiteral(name="PROMPT"),
			EnumerationLiteral(name="WARNING"),
			EnumerationLiteral(name="ERROR")
    }
)

ActivityGroup: Enumeration = Enumeration(
    name="ActivityGroup",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="YOUTHMUSICCORP"),
			EnumerationLiteral(name="FIFEANDDRUMCORP"),
			EnumerationLiteral(name="BYAKUREN"),
			EnumerationLiteral(name="SOKAGROUP"),
			EnumerationLiteral(name="GAJOKAI"),
			EnumerationLiteral(name="CHORUSGROUP"),
			EnumerationLiteral(name="STUDYGROUP"),
			EnumerationLiteral(name="PHONETOBAN"),
			EnumerationLiteral(name="BOOKSTORETOBAN"),
			EnumerationLiteral(name="CLEANUPCOMMITTEE"),
			EnumerationLiteral(name="BUILDINGCOMMITTEE"),
			EnumerationLiteral(name="WELCOMINGCOMMITTEE"),
			EnumerationLiteral(name="GOLDENSTAGECREW"),
			EnumerationLiteral(name="YOUTHPEACEGROUP"),
			EnumerationLiteral(name="YOUTHSUPPORTGROUP"),
			EnumerationLiteral(name="SOKASPIRITGROUP"),
			EnumerationLiteral(name="CULTUREDEPT"),
			EnumerationLiteral(name="SECRETARIET"),
			EnumerationLiteral(name="CENTRALEXECUTIVECOMMITTEE")
    }
)

ActivityGroupName: Enumeration = Enumeration(
    name="ActivityGroupName",
    literals={
            EnumerationLiteral(name="ChorusGroup"),
			EnumerationLiteral(name="StudyGroup"),
			EnumerationLiteral(name="PhoneToban"),
			EnumerationLiteral(name="BookstoreToban"),
			EnumerationLiteral(name="CleanupCommittee"),
			EnumerationLiteral(name="BuildingCommittee"),
			EnumerationLiteral(name="WelcomingCommittee"),
			EnumerationLiteral(name="GoldenStageCrew"),
			EnumerationLiteral(name="YouthPeaceGroup"),
			EnumerationLiteral(name="YouthSupportGroup"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="YouthMusicCorp"),
			EnumerationLiteral(name="FifeAndDrumCorp"),
			EnumerationLiteral(name="Byakuren"),
			EnumerationLiteral(name="SokaGroup"),
			EnumerationLiteral(name="Gajokai"),
			EnumerationLiteral(name="SokaSpiritGroup"),
			EnumerationLiteral(name="CultureDept"),
			EnumerationLiteral(name="Secretariet"),
			EnumerationLiteral(name="CentralExecutiveCommittee")
    }
)

Division: Enumeration = Enumeration(
    name="Division",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="YWD"),
			EnumerationLiteral(name="YMD"),
			EnumerationLiteral(name="YD"),
			EnumerationLiteral(name="WD"),
			EnumerationLiteral(name="MD"),
			EnumerationLiteral(name="ALL")
    }
)

DivisionName: Enumeration = Enumeration(
    name="DivisionName",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="YoungWomenSDivision"),
			EnumerationLiteral(name="YoungMenSDivision"),
			EnumerationLiteral(name="YouthDivision"),
			EnumerationLiteral(name="WomanSDivision"),
			EnumerationLiteral(name="MenSDivision"),
			EnumerationLiteral(name="AllDivisions")
    }
)

Capability: Enumeration = Enumeration(
    name="Capability",
    literals={
            EnumerationLiteral(name="ALL"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="READ"),
			EnumerationLiteral(name="CREATE"),
			EnumerationLiteral(name="UPDATE"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="EXPORT"),
			EnumerationLiteral(name="EMAIL"),
			EnumerationLiteral(name="PRINT")
    }
)

FamilyRelation: Enumeration = Enumeration(
    name="FamilyRelation",
    literals={
            EnumerationLiteral(name="MOTHER"),
			EnumerationLiteral(name="FATHER"),
			EnumerationLiteral(name="SISTER"),
			EnumerationLiteral(name="BROTHER"),
			EnumerationLiteral(name="STEPSISTER"),
			EnumerationLiteral(name="STEPBROTHER"),
			EnumerationLiteral(name="HUSBAND"),
			EnumerationLiteral(name="WIFE"),
			EnumerationLiteral(name="SON"),
			EnumerationLiteral(name="DAUGHTER"),
			EnumerationLiteral(name="GRANDMOTHER"),
			EnumerationLiteral(name="GRANDFATHER"),
			EnumerationLiteral(name="GRANDSON"),
			EnumerationLiteral(name="GRANDDAUGHTER"),
			EnumerationLiteral(name="MOTHERINLAW"),
			EnumerationLiteral(name="FATHERINLAW"),
			EnumerationLiteral(name="SONINLAW"),
			EnumerationLiteral(name="DAUGHTERINLAW"),
			EnumerationLiteral(name="AUNT"),
			EnumerationLiteral(name="UNCLE"),
			EnumerationLiteral(name="COUSIN"),
			EnumerationLiteral(name="NIECE"),
			EnumerationLiteral(name="NEPHEW"),
			EnumerationLiteral(name="EXHUSBAND"),
			EnumerationLiteral(name="EXWIFE"),
			EnumerationLiteral(name="OTHER")
    }
)

EventStatus: Enumeration = Enumeration(
    name="EventStatus",
    literals={
            EnumerationLiteral(name="MANAGER"),
			EnumerationLiteral(name="USER"),
			EnumerationLiteral(name="HOST")
    }
)

GohonzonType: Enumeration = Enumeration(
    name="GohonzonType",
    literals={
            EnumerationLiteral(name="REGULAR"),
			EnumerationLiteral(name="SMALL"),
			EnumerationLiteral(name="LARGE"),
			EnumerationLiteral(name="FAMILY"),
			EnumerationLiteral(name="OMOMORI"),
			EnumerationLiteral(name="OKATAGI")
    }
)

OrganizationLevel: Enumeration = Enumeration(
    name="OrganizationLevel",
    literals={
            EnumerationLiteral(name="SGIUSA"),
			EnumerationLiteral(name="TEAM"),
			EnumerationLiteral(name="ZONE"),
			EnumerationLiteral(name="REGION"),
			EnumerationLiteral(name="AREA"),
			EnumerationLiteral(name="CHAPTER"),
			EnumerationLiteral(name="DISTRICT"),
			EnumerationLiteral(name="GROUP"),
			EnumerationLiteral(name="UNIT")
    }
)

Position: Enumeration = Enumeration(
    name="Position",
    literals={
            EnumerationLiteral(name="LEADER"),
			EnumerationLiteral(name="VICELEADER"),
			EnumerationLiteral(name="GUIDANCE"),
			EnumerationLiteral(name="ADVISOR"),
			EnumerationLiteral(name="SENIORVICELEADER"),
			EnumerationLiteral(name="GENERALDIRECTOR"),
			EnumerationLiteral(name="VICEGENERALDIRECTOR"),
			EnumerationLiteral(name="SENIORVICEGENERALDIRECTOR"),
			EnumerationLiteral(name="SOKASPIRITCOORDINATOR"),
			EnumerationLiteral(name="CULTUREDEPTCOORDINATOR"),
			EnumerationLiteral(name="MEMBERCAREADVISOR"),
			EnumerationLiteral(name="MEMBERSHIPSTATISTICSADMINISTRATOR"),
			EnumerationLiteral(name="MEMBERSHIPDATABASEADMINISTRATOR"),
			EnumerationLiteral(name="PUBLICATIONSREPRESENTATIVE")
    }
)

PositionName: Enumeration = Enumeration(
    name="PositionName",
    literals={
            EnumerationLiteral(name="Leader"),
			EnumerationLiteral(name="ViceLeader"),
			EnumerationLiteral(name="Guidance"),
			EnumerationLiteral(name="Advisor"),
			EnumerationLiteral(name="SeniorViceLeader"),
			EnumerationLiteral(name="GeneralDirector"),
			EnumerationLiteral(name="ViceGeneralDirector"),
			EnumerationLiteral(name="SeniorViceGeneralDirector"),
			EnumerationLiteral(name="SokaSpiritCoordinator"),
			EnumerationLiteral(name="CultureDeptCoordinator"),
			EnumerationLiteral(name="MemberCareAdvisor"),
			EnumerationLiteral(name="MembershipStatisticsAdministrator"),
			EnumerationLiteral(name="MembershipDatabaseAdministrator"),
			EnumerationLiteral(name="PublicationsRepresentative")
    }
)

Role: Enumeration = Enumeration(
    name="Role",
    literals={
            EnumerationLiteral(name="MANAGER"),
			EnumerationLiteral(name="USER"),
			EnumerationLiteral(name="HOST")
    }
)

SchoolType: Enumeration = Enumeration(
    name="SchoolType",
    literals={
            EnumerationLiteral(name="OTHER"),
			EnumerationLiteral(name="ELEMENTARY"),
			EnumerationLiteral(name="GRAMMER"),
			EnumerationLiteral(name="JRHIGHSCHOOL"),
			EnumerationLiteral(name="HIGHSCHOOL"),
			EnumerationLiteral(name="COLLEGE"),
			EnumerationLiteral(name="GRADUATE")
    }
)

StudyDeptExamLevel: Enumeration = Enumeration(
    name="StudyDeptExamLevel",
    literals={
            EnumerationLiteral(name="ENTRANCE"),
			EnumerationLiteral(name="ELEMENTARY"),
			EnumerationLiteral(name="INTERMEDIATE"),
			EnumerationLiteral(name="ADVANCED"),
			EnumerationLiteral(name="GRADUATE"),
			EnumerationLiteral(name="POSTGRADUATE"),
			EnumerationLiteral(name="OTHER")
    }
)

StudyDeptLanguage: Enumeration = Enumeration(
    name="StudyDeptLanguage",
    literals={
            EnumerationLiteral(name="ENGLISH"),
			EnumerationLiteral(name="SPANISH"),
			EnumerationLiteral(name="FRENCH"),
			EnumerationLiteral(name="ITALIAN"),
			EnumerationLiteral(name="GERMAN"),
			EnumerationLiteral(name="PORTUGUESE"),
			EnumerationLiteral(name="JAPANESE"),
			EnumerationLiteral(name="CHINESE"),
			EnumerationLiteral(name="KOREAN"),
			EnumerationLiteral(name="VIETNAMESE"),
			EnumerationLiteral(name="THAI"),
			EnumerationLiteral(name="OTHER")
    }
)

SubDivisionName: Enumeration = Enumeration(
    name="SubDivisionName",
    literals={
            EnumerationLiteral(name="StudentDivision"),
			EnumerationLiteral(name="HighSchoolDivision"),
			EnumerationLiteral(name="JrHighSchoolDivision"),
			EnumerationLiteral(name="ElementarySchoolDivision"),
			EnumerationLiteral(name="ChildrenSDivision"),
			EnumerationLiteral(name="ALLSubDivisions")
    }
)

SubDivision: Enumeration = Enumeration(
    name="SubDivision",
    literals={
            EnumerationLiteral(name="STUDENT"),
			EnumerationLiteral(name="HIGHSCHOOL"),
			EnumerationLiteral(name="JRHIGHSCHOOL"),
			EnumerationLiteral(name="ELEMENTARYSCHOOL"),
			EnumerationLiteral(name="CHILDREN"),
			EnumerationLiteral(name="ALL")
    }
)

ViewType: Enumeration = Enumeration(
    name="ViewType",
    literals={
            EnumerationLiteral(name="USERLIST"),
			EnumerationLiteral(name="MEMBERLIST"),
			EnumerationLiteral(name="ORGANIZATIONNODE")
    }
)

# Classes
org_aries_common_Attachment = Class(name="org::aries::common::Attachment")
org_aries_common_DocumentRoot = Class(name="org::aries::common::DocumentRoot")
Attachment = Class(name="Attachment")
EmailAccount = Class(name="EmailAccount")
EmailAddress = Class(name="EmailAddress")
org_aries_common_EStringToStringMapEntry = Class(name="org::aries::common::EStringToStringMapEntry")
EmailBox = Class(name="EmailBox")
EmailMessage = Class(name="EmailMessage")
Event = Class(name="Event")
Map = Class(name="Map")
EmailAddressList = Class(name="EmailAddressList")
Note = Class(name="Note")
Person = Class(name="Person")
PersonName = Class(name="PersonName")
MapEntry = Class(name="MapEntry")
Properties = Class(name="Properties")
Property_ = Class(name="Property")
StreetAddress = Class(name="StreetAddress")
User = Class(name="User")
PhoneNumber = Class(name="PhoneNumber")
org_aries_common_EmailAccount = Class(name="org::aries::common::EmailAccount")
ZipCode = Class(name="ZipCode")
org_aries_common_EmailAddress = Class(name="org::aries::common::EmailAddress")
org_aries_common_EmailAddressList = Class(name="org::aries::common::EmailAddressList")
org_aries_common_EmailBox = Class(name="org::aries::common::EmailBox")
org_aries_common_EmailMessage = Class(name="org::aries::common::EmailMessage")
org_aries_common_Event = Class(name="org::aries::common::Event")
org_aries_common_Map = Class(name="org::aries::common::Map")
org_aries_common_EObject = Class(name="org::aries::common::EObject")
org_aries_common_MapEntry = Class(name="org::aries::common::MapEntry")
org_aries_common_Person = Class(name="org::aries::common::Person")
org_aries_common_Note = Class(name="org::aries::common::Note")
org_aries_common_PersonName = Class(name="org::aries::common::PersonName")
org_aries_common_PhoneNumber = Class(name="org::aries::common::PhoneNumber")
org_aries_common_Property = Class(name="org::aries::common::Property")
org_aries_common_Properties = Class(name="org::aries::common::Properties")
org_aries_common_StreetAddress = Class(name="org::aries::common::StreetAddress")
org_aries_common_User = Class(name="org::aries::common::User")
org_aries_common_ZipCode = Class(name="org::aries::common::ZipCode")
org_sgiusa_model_EStringToStringMapEntry = Class(name="org::sgiusa::model::EStringToStringMapEntry")
org_sgiusa_model_DocumentRoot = Class(name="org::sgiusa::model::DocumentRoot")
FamilyMember = Class(name="FamilyMember")
EmailList = Class(name="EmailList")
Member = Class(name="Member")
GohonzonInfo = Class(name="GohonzonInfo")
LeadershipInfo = Class(name="LeadershipInfo")
LeadershipRole = Class(name="LeadershipRole")
MembershipInfo = Class(name="MembershipInfo")
Organization = Class(name="Organization")
Members = Class(name="Members")
MemberSearchCriteria = Class(name="MemberSearchCriteria")
StudyDeptInfo = Class(name="StudyDeptInfo")
Users = Class(name="Users")
View = Class(name="View")
Permission = Class(name="Permission")
Preferences = Class(name="Preferences")
Registration = Class(name="Registration")
SchoolInfo = Class(name="SchoolInfo")
StudyDeptExam = Class(name="StudyDeptExam")
org_sgiusa_model_Event = Class(name="org::sgiusa::model::Event")
org_sgiusa_model_EmailList = Class(name="org::sgiusa::model::EmailList")
org_sgiusa_model_FamilyMember = Class(name="org::sgiusa::model::FamilyMember")
org_sgiusa_model_GohonzonInfo = Class(name="org::sgiusa::model::GohonzonInfo")
org_sgiusa_model_LeadershipRole = Class(name="org::sgiusa::model::LeadershipRole")
org_sgiusa_model_LeadershipInfo = Class(name="org::sgiusa::model::LeadershipInfo")
org_sgiusa_model_Member = Class(name="org::sgiusa::model::Member")
org_sgiusa_model_Members = Class(name="org::sgiusa::model::Members")
org_sgiusa_model_MemberSearchCriteria = Class(name="org::sgiusa::model::MemberSearchCriteria")
org_sgiusa_model_Note = Class(name="org::sgiusa::model::Note")
org_sgiusa_model_MembershipInfo = Class(name="org::sgiusa::model::MembershipInfo")
org_sgiusa_model_Organization = Class(name="org::sgiusa::model::Organization")
org_sgiusa_model_Permission = Class(name="org::sgiusa::model::Permission")
org_sgiusa_model_Preferences = Class(name="org::sgiusa::model::Preferences")
org_sgiusa_model_Registration = Class(name="org::sgiusa::model::Registration")
org_sgiusa_model_SchoolInfo = Class(name="org::sgiusa::model::SchoolInfo")
org_sgiusa_model_StudyDeptExam = Class(name="org::sgiusa::model::StudyDeptExam")
org_sgiusa_model_StudyDeptInfo = Class(name="org::sgiusa::model::StudyDeptInfo")
org_sgiusa_model_User = Class(name="org::sgiusa::model::User")
org_sgiusa_model_Users = Class(name="org::sgiusa::model::Users")
org_sgiusa_model_View = Class(name="org::sgiusa::model::View")

# org_aries_common_Attachment class attributes and methods
org_aries_common_Attachment_id: Property = Property(name="id", type=StringType)
org_aries_common_Attachment_name: Property = Property(name="name", type=StringType)
org_aries_common_Attachment_size: Property = Property(name="size", type=StringType)
org_aries_common_Attachment_fileName: Property = Property(name="fileName", type=StringType)
org_aries_common_Attachment_fileData: Property = Property(name="fileData", type=StringType)
org_aries_common_Attachment_contentType: Property = Property(name="contentType", type=StringType)
org_aries_common_Attachment.attributes={org_aries_common_Attachment_id, org_aries_common_Attachment_name, org_aries_common_Attachment_fileData, org_aries_common_Attachment_contentType, org_aries_common_Attachment_size, org_aries_common_Attachment_fileName}

# org_aries_common_DocumentRoot class attributes and methods
org_aries_common_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
org_aries_common_DocumentRoot.attributes={org_aries_common_DocumentRoot_mixed}

# Attachment class attributes and methods

# EmailAccount class attributes and methods

# EmailAddress class attributes and methods

# org_aries_common_EStringToStringMapEntry class attributes and methods

# EmailBox class attributes and methods

# EmailMessage class attributes and methods

# Event class attributes and methods

# Map class attributes and methods

# EmailAddressList class attributes and methods

# Note class attributes and methods

# Person class attributes and methods

# PersonName class attributes and methods

# MapEntry class attributes and methods

# Properties class attributes and methods

# Property class attributes and methods

# StreetAddress class attributes and methods

# User class attributes and methods

# PhoneNumber class attributes and methods

# org_aries_common_EmailAccount class attributes and methods
org_aries_common_EmailAccount_id: Property = Property(name="id", type=StringType)
org_aries_common_EmailAccount_userId: Property = Property(name="userId", type=StringType)
org_aries_common_EmailAccount_password: Property = Property(name="password", type=StringType)
org_aries_common_EmailAccount_firstName: Property = Property(name="firstName", type=StringType)
org_aries_common_EmailAccount_lastName: Property = Property(name="lastName", type=StringType)
org_aries_common_EmailAccount_enabled: Property = Property(name="enabled", type=StringType)
org_aries_common_EmailAccount.attributes={org_aries_common_EmailAccount_password, org_aries_common_EmailAccount_userId, org_aries_common_EmailAccount_enabled, org_aries_common_EmailAccount_id, org_aries_common_EmailAccount_firstName, org_aries_common_EmailAccount_lastName}

# ZipCode class attributes and methods

# org_aries_common_EmailAddress class attributes and methods
org_aries_common_EmailAddress_id: Property = Property(name="id", type=StringType)
org_aries_common_EmailAddress_url: Property = Property(name="url", type=StringType)
org_aries_common_EmailAddress_userId: Property = Property(name="userId", type=StringType)
org_aries_common_EmailAddress_firstName: Property = Property(name="firstName", type=StringType)
org_aries_common_EmailAddress_lastName: Property = Property(name="lastName", type=StringType)
org_aries_common_EmailAddress_organization: Property = Property(name="organization", type=StringType)
org_aries_common_EmailAddress_creationDate: Property = Property(name="creationDate", type=StringType)
org_aries_common_EmailAddress_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_aries_common_EmailAddress_enabled: Property = Property(name="enabled", type=StringType)
org_aries_common_EmailAddress.attributes={org_aries_common_EmailAddress_url, org_aries_common_EmailAddress_firstName, org_aries_common_EmailAddress_organization, org_aries_common_EmailAddress_id, org_aries_common_EmailAddress_lastUpdate, org_aries_common_EmailAddress_enabled, org_aries_common_EmailAddress_creationDate, org_aries_common_EmailAddress_userId, org_aries_common_EmailAddress_lastName}

# org_aries_common_EmailAddressList class attributes and methods
org_aries_common_EmailAddressList_name: Property = Property(name="name", type=StringType)
org_aries_common_EmailAddressList_emailAddress: Property = Property(name="emailAddress", type=StringType)
org_aries_common_EmailAddressList.attributes={org_aries_common_EmailAddressList_emailAddress, org_aries_common_EmailAddressList_name}

# org_aries_common_EmailBox class attributes and methods
org_aries_common_EmailBox_id: Property = Property(name="id", type=StringType)
org_aries_common_EmailBox_type: Property = Property(name="type", type=StringType)
org_aries_common_EmailBox_name: Property = Property(name="name", type=StringType)
org_aries_common_EmailBox_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_aries_common_EmailBox_creationDate: Property = Property(name="creationDate", type=StringType)
org_aries_common_EmailBox.attributes={org_aries_common_EmailBox_lastUpdate, org_aries_common_EmailBox_type, org_aries_common_EmailBox_id, org_aries_common_EmailBox_name, org_aries_common_EmailBox_creationDate}

# org_aries_common_EmailMessage class attributes and methods
org_aries_common_EmailMessage_id: Property = Property(name="id", type=StringType)
org_aries_common_EmailMessage_content: Property = Property(name="content", type=StringType)
org_aries_common_EmailMessage_subject: Property = Property(name="subject", type=StringType)
org_aries_common_EmailMessage_timestamp: Property = Property(name="timestamp", type=StringType)
org_aries_common_EmailMessage_smtpPort: Property = Property(name="smtpPort", type=StringType)
org_aries_common_EmailMessage_sourceId: Property = Property(name="sourceId", type=StringType)
org_aries_common_EmailMessage_smtpHost: Property = Property(name="smtpHost", type=StringType)
org_aries_common_EmailMessage_sendAsHtml: Property = Property(name="sendAsHtml", type=StringType)
org_aries_common_EmailMessage.attributes={org_aries_common_EmailMessage_id, org_aries_common_EmailMessage_sendAsHtml, org_aries_common_EmailMessage_content, org_aries_common_EmailMessage_subject, org_aries_common_EmailMessage_smtpPort, org_aries_common_EmailMessage_sourceId, org_aries_common_EmailMessage_smtpHost, org_aries_common_EmailMessage_timestamp}

# org_aries_common_Event class attributes and methods
org_aries_common_Event_id: Property = Property(name="id", type=StringType)
org_aries_common_Event.attributes={org_aries_common_Event_id}

# org_aries_common_Map class attributes and methods

# org_aries_common_EObject class attributes and methods

# org_aries_common_MapEntry class attributes and methods

# org_aries_common_Person class attributes and methods
org_aries_common_Person_id: Property = Property(name="id", type=StringType)
org_aries_common_Person_userId: Property = Property(name="userId", type=StringType)
org_aries_common_Person.attributes={org_aries_common_Person_userId, org_aries_common_Person_id}

# org_aries_common_Note class attributes and methods
org_aries_common_Note_id: Property = Property(name="id", type=StringType)
org_aries_common_Note_creationDate: Property = Property(name="creationDate", type=StringType)
org_aries_common_Note_text: Property = Property(name="text", type=StringType)
org_aries_common_Note_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_aries_common_Note.attributes={org_aries_common_Note_creationDate, org_aries_common_Note_id, org_aries_common_Note_text, org_aries_common_Note_lastUpdate}

# org_aries_common_PersonName class attributes and methods
org_aries_common_PersonName_lastName: Property = Property(name="lastName", type=StringType)
org_aries_common_PersonName_firstName: Property = Property(name="firstName", type=StringType)
org_aries_common_PersonName_middleInitial: Property = Property(name="middleInitial", type=StringType)
org_aries_common_PersonName.attributes={org_aries_common_PersonName_middleInitial, org_aries_common_PersonName_firstName, org_aries_common_PersonName_lastName}

# org_aries_common_PhoneNumber class attributes and methods
org_aries_common_PhoneNumber_country: Property = Property(name="country", type=StringType)
org_aries_common_PhoneNumber_extension: Property = Property(name="extension", type=StringType)
org_aries_common_PhoneNumber_number: Property = Property(name="number", type=StringType)
org_aries_common_PhoneNumber_id: Property = Property(name="id", type=StringType)
org_aries_common_PhoneNumber_type: Property = Property(name="type", type=StringType)
org_aries_common_PhoneNumber_area: Property = Property(name="area", type=StringType)
org_aries_common_PhoneNumber_value: Property = Property(name="value", type=StringType)
org_aries_common_PhoneNumber.attributes={org_aries_common_PhoneNumber_value, org_aries_common_PhoneNumber_extension, org_aries_common_PhoneNumber_country, org_aries_common_PhoneNumber_type, org_aries_common_PhoneNumber_number, org_aries_common_PhoneNumber_area, org_aries_common_PhoneNumber_id}

# org_aries_common_Property class attributes and methods
org_aries_common_Property_mixed: Property = Property(name="mixed", type=StringType)
org_aries_common_Property_id: Property = Property(name="id", type=StringType)
org_aries_common_Property_name: Property = Property(name="name", type=StringType)
org_aries_common_Property_value: Property = Property(name="value", type=StringType)
org_aries_common_Property.attributes={org_aries_common_Property_id, org_aries_common_Property_value, org_aries_common_Property_name, org_aries_common_Property_mixed}

# org_aries_common_Properties class attributes and methods

# org_aries_common_StreetAddress class attributes and methods
org_aries_common_StreetAddress_city: Property = Property(name="city", type=StringType)
org_aries_common_StreetAddress_country: Property = Property(name="country", type=StringType)
org_aries_common_StreetAddress_id: Property = Property(name="id", type=StringType)
org_aries_common_StreetAddress_latitude: Property = Property(name="latitude", type=StringType)
org_aries_common_StreetAddress_longitude: Property = Property(name="longitude", type=StringType)
org_aries_common_StreetAddress_state: Property = Property(name="state", type=StringType)
org_aries_common_StreetAddress_street: Property = Property(name="street", type=StringType)
org_aries_common_StreetAddress.attributes={org_aries_common_StreetAddress_longitude, org_aries_common_StreetAddress_id, org_aries_common_StreetAddress_latitude, org_aries_common_StreetAddress_street, org_aries_common_StreetAddress_city, org_aries_common_StreetAddress_country, org_aries_common_StreetAddress_state}

# org_aries_common_User class attributes and methods
org_aries_common_User_id: Property = Property(name="id", type=StringType)
org_aries_common_User_userId: Property = Property(name="userId", type=StringType)
org_aries_common_User_password: Property = Property(name="password", type=StringType)
org_aries_common_User_firstName: Property = Property(name="firstName", type=StringType)
org_aries_common_User_lastName: Property = Property(name="lastName", type=StringType)
org_aries_common_User_enabled: Property = Property(name="enabled", type=StringType)
org_aries_common_User.attributes={org_aries_common_User_enabled, org_aries_common_User_id, org_aries_common_User_firstName, org_aries_common_User_lastName, org_aries_common_User_password, org_aries_common_User_userId}

# org_aries_common_ZipCode class attributes and methods
org_aries_common_ZipCode_country: Property = Property(name="country", type=StringType)
org_aries_common_ZipCode_extension: Property = Property(name="extension", type=StringType)
org_aries_common_ZipCode_number: Property = Property(name="number", type=StringType)
org_aries_common_ZipCode.attributes={org_aries_common_ZipCode_extension, org_aries_common_ZipCode_number, org_aries_common_ZipCode_country}

# org_sgiusa_model_EStringToStringMapEntry class attributes and methods

# org_sgiusa_model_DocumentRoot class attributes and methods
org_sgiusa_model_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
org_sgiusa_model_DocumentRoot.attributes={org_sgiusa_model_DocumentRoot_mixed}

# FamilyMember class attributes and methods

# EmailList class attributes and methods

# Member class attributes and methods

# GohonzonInfo class attributes and methods

# LeadershipInfo class attributes and methods

# LeadershipRole class attributes and methods

# MembershipInfo class attributes and methods

# Organization class attributes and methods

# Members class attributes and methods

# MemberSearchCriteria class attributes and methods

# StudyDeptInfo class attributes and methods

# Users class attributes and methods

# View class attributes and methods

# Permission class attributes and methods

# Preferences class attributes and methods

# Registration class attributes and methods

# SchoolInfo class attributes and methods

# StudyDeptExam class attributes and methods

# org_sgiusa_model_Event class attributes and methods
org_sgiusa_model_Event_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_Event_userId: Property = Property(name="userId", type=StringType)
org_sgiusa_model_Event_status: Property = Property(name="status", type=StringType)
org_sgiusa_model_Event_divisions: Property = Property(name="divisions", type=StringType)
org_sgiusa_model_Event_subDivisions: Property = Property(name="subDivisions", type=StringType)
org_sgiusa_model_Event.attributes={org_sgiusa_model_Event_id, org_sgiusa_model_Event_status, org_sgiusa_model_Event_subDivisions, org_sgiusa_model_Event_divisions, org_sgiusa_model_Event_userId}

# org_sgiusa_model_EmailList class attributes and methods
org_sgiusa_model_EmailList_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_EmailList_enabled: Property = Property(name="enabled", type=StringType)
org_sgiusa_model_EmailList_divisions: Property = Property(name="divisions", type=StringType)
org_sgiusa_model_EmailList_subDivisions: Property = Property(name="subDivisions", type=StringType)
org_sgiusa_model_EmailList_activityGroups: Property = Property(name="activityGroups", type=StringType)
org_sgiusa_model_EmailList.attributes={org_sgiusa_model_EmailList_id, org_sgiusa_model_EmailList_divisions, org_sgiusa_model_EmailList_enabled, org_sgiusa_model_EmailList_subDivisions, org_sgiusa_model_EmailList_activityGroups}

# org_sgiusa_model_FamilyMember class attributes and methods
org_sgiusa_model_FamilyMember_familyRelation: Property = Property(name="familyRelation", type=StringType)
org_sgiusa_model_FamilyMember_personName: Property = Property(name="personName", type=StringType)
org_sgiusa_model_FamilyMember_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_sgiusa_model_FamilyMember_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_FamilyMember_sgiMember: Property = Property(name="sgiMember", type=StringType)
org_sgiusa_model_FamilyMember.attributes={org_sgiusa_model_FamilyMember_lastUpdate, org_sgiusa_model_FamilyMember_personName, org_sgiusa_model_FamilyMember_sgiMember, org_sgiusa_model_FamilyMember_familyRelation, org_sgiusa_model_FamilyMember_id}

# org_sgiusa_model_GohonzonInfo class attributes and methods
org_sgiusa_model_GohonzonInfo_gohonzonType: Property = Property(name="gohonzonType", type=StringType)
org_sgiusa_model_GohonzonInfo_receiveDate: Property = Property(name="receiveDate", type=StringType)
org_sgiusa_model_GohonzonInfo_returned: Property = Property(name="returned", type=StringType)
org_sgiusa_model_GohonzonInfo_returnDate: Property = Property(name="returnDate", type=StringType)
org_sgiusa_model_GohonzonInfo_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_sgiusa_model_GohonzonInfo_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_GohonzonInfo.attributes={org_sgiusa_model_GohonzonInfo_gohonzonType, org_sgiusa_model_GohonzonInfo_lastUpdate, org_sgiusa_model_GohonzonInfo_id, org_sgiusa_model_GohonzonInfo_receiveDate, org_sgiusa_model_GohonzonInfo_returnDate, org_sgiusa_model_GohonzonInfo_returned}

# org_sgiusa_model_LeadershipRole class attributes and methods
org_sgiusa_model_LeadershipRole_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_LeadershipRole_startDate: Property = Property(name="startDate", type=StringType)
org_sgiusa_model_LeadershipRole_endDate: Property = Property(name="endDate", type=StringType)
org_sgiusa_model_LeadershipRole_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_sgiusa_model_LeadershipRole_active: Property = Property(name="active", type=StringType)
org_sgiusa_model_LeadershipRole_level: Property = Property(name="level", type=StringType)
org_sgiusa_model_LeadershipRole_position: Property = Property(name="position", type=StringType)
org_sgiusa_model_LeadershipRole_division: Property = Property(name="division", type=StringType)
org_sgiusa_model_LeadershipRole_subDivision: Property = Property(name="subDivision", type=StringType)
org_sgiusa_model_LeadershipRole_activityGroup: Property = Property(name="activityGroup", type=StringType)
org_sgiusa_model_LeadershipRole.attributes={org_sgiusa_model_LeadershipRole_startDate, org_sgiusa_model_LeadershipRole_level, org_sgiusa_model_LeadershipRole_subDivision, org_sgiusa_model_LeadershipRole_division, org_sgiusa_model_LeadershipRole_endDate, org_sgiusa_model_LeadershipRole_lastUpdate, org_sgiusa_model_LeadershipRole_id, org_sgiusa_model_LeadershipRole_active, org_sgiusa_model_LeadershipRole_activityGroup, org_sgiusa_model_LeadershipRole_position}

# org_sgiusa_model_LeadershipInfo class attributes and methods
org_sgiusa_model_LeadershipInfo_manualSignedDate: Property = Property(name="manualSignedDate", type=StringType)
org_sgiusa_model_LeadershipInfo_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_sgiusa_model_LeadershipInfo_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_LeadershipInfo_examPassed: Property = Property(name="examPassed", type=StringType)
org_sgiusa_model_LeadershipInfo_examPassedDate: Property = Property(name="examPassedDate", type=StringType)
org_sgiusa_model_LeadershipInfo_manualSigned: Property = Property(name="manualSigned", type=StringType)
org_sgiusa_model_LeadershipInfo.attributes={org_sgiusa_model_LeadershipInfo_examPassedDate, org_sgiusa_model_LeadershipInfo_manualSigned, org_sgiusa_model_LeadershipInfo_lastUpdate, org_sgiusa_model_LeadershipInfo_manualSignedDate, org_sgiusa_model_LeadershipInfo_id, org_sgiusa_model_LeadershipInfo_examPassed}

# org_sgiusa_model_Member class attributes and methods
org_sgiusa_model_Member_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_Member_division: Property = Property(name="division", type=StringType)
org_sgiusa_model_Member_firstName: Property = Property(name="firstName", type=StringType)
org_sgiusa_model_Member_lastName: Property = Property(name="lastName", type=StringType)
org_sgiusa_model_Member_middleInitial: Property = Property(name="middleInitial", type=StringType)
org_sgiusa_model_Member_interests: Property = Property(name="interests", type=StringType)
org_sgiusa_model_Member_languages: Property = Property(name="languages", type=StringType)
org_sgiusa_model_Member_joinDate: Property = Property(name="joinDate", type=StringType)
org_sgiusa_model_Member_birthDate: Property = Property(name="birthDate", type=StringType)
org_sgiusa_model_Member_subDivision: Property = Property(name="subDivision", type=StringType)
org_sgiusa_model_Member_activityGroups: Property = Property(name="activityGroups", type=StringType)
org_sgiusa_model_Member_statusProfile: Property = Property(name="statusProfile", type=StringType)
org_sgiusa_model_Member_archived: Property = Property(name="archived", type=StringType)
org_sgiusa_model_Member_employer: Property = Property(name="employer", type=StringType)
org_sgiusa_model_Member_occupation: Property = Property(name="occupation", type=StringType)
org_sgiusa_model_Member_extraField1: Property = Property(name="extraField1", type=StringType)
org_sgiusa_model_Member_extraField2: Property = Property(name="extraField2", type=StringType)
org_sgiusa_model_Member_visible: Property = Property(name="visible", type=StringType)
org_sgiusa_model_Member_locatable: Property = Property(name="locatable", type=StringType)
org_sgiusa_model_Member.attributes={org_sgiusa_model_Member_visible, org_sgiusa_model_Member_middleInitial, org_sgiusa_model_Member_archived, org_sgiusa_model_Member_birthDate, org_sgiusa_model_Member_interests, org_sgiusa_model_Member_languages, org_sgiusa_model_Member_locatable, org_sgiusa_model_Member_employer, org_sgiusa_model_Member_extraField1, org_sgiusa_model_Member_occupation, org_sgiusa_model_Member_joinDate, org_sgiusa_model_Member_subDivision, org_sgiusa_model_Member_extraField2, org_sgiusa_model_Member_division, org_sgiusa_model_Member_statusProfile, org_sgiusa_model_Member_lastName, org_sgiusa_model_Member_firstName, org_sgiusa_model_Member_id, org_sgiusa_model_Member_activityGroups}

# org_sgiusa_model_Members class attributes and methods

# org_sgiusa_model_MemberSearchCriteria class attributes and methods
org_sgiusa_model_MemberSearchCriteria_divisions: Property = Property(name="divisions", type=StringType)
org_sgiusa_model_MemberSearchCriteria_subDivisions: Property = Property(name="subDivisions", type=StringType)
org_sgiusa_model_MemberSearchCriteria_activityGroups: Property = Property(name="activityGroups", type=StringType)
org_sgiusa_model_MemberSearchCriteria.attributes={org_sgiusa_model_MemberSearchCriteria_activityGroups, org_sgiusa_model_MemberSearchCriteria_subDivisions, org_sgiusa_model_MemberSearchCriteria_divisions}

# org_sgiusa_model_Note class attributes and methods
org_sgiusa_model_Note_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_Note_text: Property = Property(name="text", type=StringType)
org_sgiusa_model_Note_creationDate: Property = Property(name="creationDate", type=StringType)
org_sgiusa_model_Note_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_sgiusa_model_Note.attributes={org_sgiusa_model_Note_creationDate, org_sgiusa_model_Note_id, org_sgiusa_model_Note_text, org_sgiusa_model_Note_lastUpdate}

# org_sgiusa_model_MembershipInfo class attributes and methods
org_sgiusa_model_MembershipInfo_receivedCertificate: Property = Property(name="receivedCertificate", type=StringType)
org_sgiusa_model_MembershipInfo_notActivated: Property = Property(name="notActivated", type=StringType)
org_sgiusa_model_MembershipInfo_notLocatable: Property = Property(name="notLocatable", type=StringType)
org_sgiusa_model_MembershipInfo_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_sgiusa_model_MembershipInfo_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_MembershipInfo_friendOfSgi: Property = Property(name="friendOfSgi", type=StringType)
org_sgiusa_model_MembershipInfo.attributes={org_sgiusa_model_MembershipInfo_notLocatable, org_sgiusa_model_MembershipInfo_friendOfSgi, org_sgiusa_model_MembershipInfo_notActivated, org_sgiusa_model_MembershipInfo_receivedCertificate, org_sgiusa_model_MembershipInfo_id, org_sgiusa_model_MembershipInfo_lastUpdate}

# org_sgiusa_model_Organization class attributes and methods
org_sgiusa_model_Organization_organizationId: Property = Property(name="organizationId", type=StringType)
org_sgiusa_model_Organization_permissionId: Property = Property(name="permissionId", type=StringType)
org_sgiusa_model_Organization_type: Property = Property(name="type", type=StringType)
org_sgiusa_model_Organization_level: Property = Property(name="level", type=StringType)
org_sgiusa_model_Organization_name: Property = Property(name="name", type=StringType)
org_sgiusa_model_Organization_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_Organization_zipCodes: Property = Property(name="zipCodes", type=StringType)
org_sgiusa_model_Organization_creationDate: Property = Property(name="creationDate", type=StringType)
org_sgiusa_model_Organization_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_sgiusa_model_Organization_abbrv: Property = Property(name="abbrv", type=StringType)
org_sgiusa_model_Organization_label: Property = Property(name="label", type=StringType)
org_sgiusa_model_Organization.attributes={org_sgiusa_model_Organization_lastUpdate, org_sgiusa_model_Organization_label, org_sgiusa_model_Organization_level, org_sgiusa_model_Organization_abbrv, org_sgiusa_model_Organization_permissionId, org_sgiusa_model_Organization_type, org_sgiusa_model_Organization_id, org_sgiusa_model_Organization_zipCodes, org_sgiusa_model_Organization_creationDate, org_sgiusa_model_Organization_organizationId, org_sgiusa_model_Organization_name}

# org_sgiusa_model_Permission class attributes and methods
org_sgiusa_model_Permission_divisions: Property = Property(name="divisions", type=StringType)
org_sgiusa_model_Permission_subDivisions: Property = Property(name="subDivisions", type=StringType)
org_sgiusa_model_Permission_activityGroups: Property = Property(name="activityGroups", type=StringType)
org_sgiusa_model_Permission_capabilities: Property = Property(name="capabilities", type=StringType)
org_sgiusa_model_Permission_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_Permission_userId: Property = Property(name="userId", type=StringType)
org_sgiusa_model_Permission_enabled: Property = Property(name="enabled", type=StringType)
org_sgiusa_model_Permission.attributes={org_sgiusa_model_Permission_enabled, org_sgiusa_model_Permission_activityGroups, org_sgiusa_model_Permission_divisions, org_sgiusa_model_Permission_capabilities, org_sgiusa_model_Permission_id, org_sgiusa_model_Permission_subDivisions, org_sgiusa_model_Permission_userId}

# org_sgiusa_model_Preferences class attributes and methods
org_sgiusa_model_Preferences_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_Preferences_userId: Property = Property(name="userId", type=StringType)
org_sgiusa_model_Preferences_themeId: Property = Property(name="themeId", type=StringType)
org_sgiusa_model_Preferences_selectedView: Property = Property(name="selectedView", type=StringType)
org_sgiusa_model_Preferences_selectedNode: Property = Property(name="selectedNode", type=StringType)
org_sgiusa_model_Preferences_openViews: Property = Property(name="openViews", type=StringType)
org_sgiusa_model_Preferences_openNodes: Property = Property(name="openNodes", type=StringType)
org_sgiusa_model_Preferences_enableTooltips: Property = Property(name="enableTooltips", type=StringType)
org_sgiusa_model_Preferences.attributes={org_sgiusa_model_Preferences_id, org_sgiusa_model_Preferences_userId, org_sgiusa_model_Preferences_enableTooltips, org_sgiusa_model_Preferences_selectedView, org_sgiusa_model_Preferences_selectedNode, org_sgiusa_model_Preferences_openViews, org_sgiusa_model_Preferences_openNodes, org_sgiusa_model_Preferences_themeId}

# org_sgiusa_model_Registration class attributes and methods
org_sgiusa_model_Registration_date: Property = Property(name="date", type=StringType)
org_sgiusa_model_Registration_cancelled: Property = Property(name="cancelled", type=StringType)
org_sgiusa_model_Registration_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_Registration_aborted: Property = Property(name="aborted", type=StringType)
org_sgiusa_model_Registration.attributes={org_sgiusa_model_Registration_cancelled, org_sgiusa_model_Registration_date, org_sgiusa_model_Registration_id, org_sgiusa_model_Registration_aborted}

# org_sgiusa_model_SchoolInfo class attributes and methods
org_sgiusa_model_SchoolInfo_schoolName: Property = Property(name="schoolName", type=StringType)
org_sgiusa_model_SchoolInfo_schoolType: Property = Property(name="schoolType", type=StringType)
org_sgiusa_model_SchoolInfo_fieldOfStudy: Property = Property(name="fieldOfStudy", type=StringType)
org_sgiusa_model_SchoolInfo_startDate: Property = Property(name="startDate", type=StringType)
org_sgiusa_model_SchoolInfo_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_SchoolInfo_endDate: Property = Property(name="endDate", type=StringType)
org_sgiusa_model_SchoolInfo_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_sgiusa_model_SchoolInfo.attributes={org_sgiusa_model_SchoolInfo_endDate, org_sgiusa_model_SchoolInfo_lastUpdate, org_sgiusa_model_SchoolInfo_id, org_sgiusa_model_SchoolInfo_schoolName, org_sgiusa_model_SchoolInfo_startDate, org_sgiusa_model_SchoolInfo_fieldOfStudy, org_sgiusa_model_SchoolInfo_schoolType}

# org_sgiusa_model_StudyDeptExam class attributes and methods
org_sgiusa_model_StudyDeptExam_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_StudyDeptExam_current: Property = Property(name="current", type=StringType)
org_sgiusa_model_StudyDeptExam_examDate: Property = Property(name="examDate", type=StringType)
org_sgiusa_model_StudyDeptExam_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_sgiusa_model_StudyDeptExam_examLevel: Property = Property(name="examLevel", type=StringType)
org_sgiusa_model_StudyDeptExam_examLanguage: Property = Property(name="examLanguage", type=StringType)
org_sgiusa_model_StudyDeptExam_examLocation: Property = Property(name="examLocation", type=StringType)
org_sgiusa_model_StudyDeptExam.attributes={org_sgiusa_model_StudyDeptExam_current, org_sgiusa_model_StudyDeptExam_examLocation, org_sgiusa_model_StudyDeptExam_lastUpdate, org_sgiusa_model_StudyDeptExam_examDate, org_sgiusa_model_StudyDeptExam_id, org_sgiusa_model_StudyDeptExam_examLanguage, org_sgiusa_model_StudyDeptExam_examLevel}

# org_sgiusa_model_StudyDeptInfo class attributes and methods
org_sgiusa_model_StudyDeptInfo_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_StudyDeptInfo_lastUpdate: Property = Property(name="lastUpdate", type=StringType)
org_sgiusa_model_StudyDeptInfo.attributes={org_sgiusa_model_StudyDeptInfo_lastUpdate, org_sgiusa_model_StudyDeptInfo_id}

# org_sgiusa_model_User class attributes and methods
org_sgiusa_model_User_password: Property = Property(name="password", type=StringType)
org_sgiusa_model_User_enabled: Property = Property(name="enabled", type=StringType)
org_sgiusa_model_User_firstName: Property = Property(name="firstName", type=StringType)
org_sgiusa_model_User_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_User_userId: Property = Property(name="userId", type=StringType)
org_sgiusa_model_User_lastName: Property = Property(name="lastName", type=StringType)
org_sgiusa_model_User_role: Property = Property(name="role", type=StringType)
org_sgiusa_model_User.attributes={org_sgiusa_model_User_userId, org_sgiusa_model_User_id, org_sgiusa_model_User_firstName, org_sgiusa_model_User_enabled, org_sgiusa_model_User_password, org_sgiusa_model_User_role, org_sgiusa_model_User_lastName}

# org_sgiusa_model_Users class attributes and methods

# org_sgiusa_model_View class attributes and methods
org_sgiusa_model_View_id: Property = Property(name="id", type=StringType)
org_sgiusa_model_View_userId: Property = Property(name="userId", type=StringType)
org_sgiusa_model_View_viewType: Property = Property(name="viewType", type=StringType)
org_sgiusa_model_View.attributes={org_sgiusa_model_View_userId, org_sgiusa_model_View_viewType, org_sgiusa_model_View_id}

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="org_aries_common_EStringToStringMapEntry", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot", type=org_aries_common_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="org_aries_common_EStringToStringMapEntry3", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot2", type=org_aries_common_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attachment4: BinaryAssociation = BinaryAssociation(
    name="attachment4",
    ends={
        Property(name="Attachment", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot5", type=Attachment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emailAccount6: BinaryAssociation = BinaryAssociation(
    name="emailAccount6",
    ends={
        Property(name="EmailAccount", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot7", type=EmailAccount, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emailAddress8: BinaryAssociation = BinaryAssociation(
    name="emailAddress8",
    ends={
        Property(name="EmailAddress", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot9", type=EmailAddress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emailBox12: BinaryAssociation = BinaryAssociation(
    name="emailBox12",
    ends={
        Property(name="EmailBox", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot13", type=EmailBox, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emailMessage14: BinaryAssociation = BinaryAssociation(
    name="emailMessage14",
    ends={
        Property(name="EmailMessage", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot15", type=EmailMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event16: BinaryAssociation = BinaryAssociation(
    name="event16",
    ends={
        Property(name="Event", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot17", type=Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
map18: BinaryAssociation = BinaryAssociation(
    name="map18",
    ends={
        Property(name="Map", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot19", type=Map, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emailAddressList10: BinaryAssociation = BinaryAssociation(
    name="emailAddressList10",
    ends={
        Property(name="EmailAddressList", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot11", type=EmailAddressList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
note22: BinaryAssociation = BinaryAssociation(
    name="note22",
    ends={
        Property(name="Note", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot23", type=Note, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person24: BinaryAssociation = BinaryAssociation(
    name="person24",
    ends={
        Property(name="Person", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot25", type=Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
personName26: BinaryAssociation = BinaryAssociation(
    name="personName26",
    ends={
        Property(name="PersonName", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot27", type=PersonName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapEntry20: BinaryAssociation = BinaryAssociation(
    name="mapEntry20",
    ends={
        Property(name="MapEntry", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot21", type=MapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties30: BinaryAssociation = BinaryAssociation(
    name="properties30",
    ends={
        Property(name="Properties", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot31", type=Properties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property32: BinaryAssociation = BinaryAssociation(
    name="property32",
    ends={
        Property(name="Property", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot33", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
streetAddress34: BinaryAssociation = BinaryAssociation(
    name="streetAddress34",
    ends={
        Property(name="StreetAddress", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot35", type=StreetAddress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user36: BinaryAssociation = BinaryAssociation(
    name="user36",
    ends={
        Property(name="User", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot37", type=User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phoneNumber28: BinaryAssociation = BinaryAssociation(
    name="phoneNumber28",
    ends={
        Property(name="PhoneNumber", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot29", type=PhoneNumber, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zipCode38: BinaryAssociation = BinaryAssociation(
    name="zipCode38",
    ends={
        Property(name="ZipCode", type=org_aries_common_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_DocumentRoot39", type=ZipCode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emailBoxes40: BinaryAssociation = BinaryAssociation(
    name="emailBoxes40",
    ends={
        Property(name="EmailBox41", type=org_aries_common_EmailAccount, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailAccount", type=EmailBox, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phoneNumber42: BinaryAssociation = BinaryAssociation(
    name="phoneNumber42",
    ends={
        Property(name="PhoneNumber43", type=org_aries_common_EmailAddress, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailAddress", type=PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emailAccount44: BinaryAssociation = BinaryAssociation(
    name="emailAccount44",
    ends={
        Property(name="EmailAccount45", type=org_aries_common_EmailBox, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailBox", type=EmailAccount, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentBox46: BinaryAssociation = BinaryAssociation(
    name="parentBox46",
    ends={
        Property(name="EmailBox48", type=org_aries_common_EmailBox, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailBox47", type=EmailBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageList49: BinaryAssociation = BinaryAssociation(
    name="messageList49",
    ends={
        Property(name="EmailMessage51", type=org_aries_common_EmailBox, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailBox50", type=EmailMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromAddress52: BinaryAssociation = BinaryAssociation(
    name="fromAddress52",
    ends={
        Property(name="EmailAddress53", type=org_aries_common_EmailMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailMessage", type=EmailAddress, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
toAddressList54: BinaryAssociation = BinaryAssociation(
    name="toAddressList54",
    ends={
        Property(name="EmailAddressList56", type=org_aries_common_EmailMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailMessage55", type=EmailAddressList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bccAddressList57: BinaryAssociation = BinaryAssociation(
    name="bccAddressList57",
    ends={
        Property(name="EmailAddressList59", type=org_aries_common_EmailMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailMessage58", type=EmailAddressList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ccAddressList60: BinaryAssociation = BinaryAssociation(
    name="ccAddressList60",
    ends={
        Property(name="EmailAddressList62", type=org_aries_common_EmailMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailMessage61", type=EmailAddressList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adminAddressList66: BinaryAssociation = BinaryAssociation(
    name="adminAddressList66",
    ends={
        Property(name="EmailAddressList68", type=org_aries_common_EmailMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailMessage67", type=EmailAddressList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attachments69: BinaryAssociation = BinaryAssociation(
    name="attachments69",
    ends={
        Property(name="Attachment71", type=org_aries_common_EmailMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailMessage70", type=Attachment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replytoAddressList63: BinaryAssociation = BinaryAssociation(
    name="replytoAddressList63",
    ends={
        Property(name="EmailAddressList65", type=org_aries_common_EmailMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_EmailMessage64", type=EmailAddressList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user72: BinaryAssociation = BinaryAssociation(
    name="user72",
    ends={
        Property(name="User73", type=org_aries_common_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_Event", type=User, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
key76: BinaryAssociation = BinaryAssociation(
    name="key76",
    ends={
        Property(name="org_aries_common_EObject", type=org_aries_common_MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_MapEntry", type=org_aries_common_EObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapEntry74: BinaryAssociation = BinaryAssociation(
    name="mapEntry74",
    ends={
        Property(name="MapEntry75", type=org_aries_common_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_Map", type=MapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value77: BinaryAssociation = BinaryAssociation(
    name="value77",
    ends={
        Property(name="org_aries_common_EObject79", type=org_aries_common_MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_MapEntry78", type=org_aries_common_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author80: BinaryAssociation = BinaryAssociation(
    name="author80",
    ends={
        Property(name="User81", type=org_aries_common_Note, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_Note", type=User, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name82: BinaryAssociation = BinaryAssociation(
    name="name82",
    ends={
        Property(name="PersonName83", type=org_aries_common_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_Person", type=PersonName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
phoneNumber84: BinaryAssociation = BinaryAssociation(
    name="phoneNumber84",
    ends={
        Property(name="PhoneNumber86", type=org_aries_common_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_Person85", type=PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emailAddress87: BinaryAssociation = BinaryAssociation(
    name="emailAddress87",
    ends={
        Property(name="EmailAddress89", type=org_aries_common_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_Person88", type=EmailAddress, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
streetAddress90: BinaryAssociation = BinaryAssociation(
    name="streetAddress90",
    ends={
        Property(name="StreetAddress92", type=org_aries_common_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_Person91", type=StreetAddress, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property93: BinaryAssociation = BinaryAssociation(
    name="property93",
    ends={
        Property(name="Property94", type=org_aries_common_Properties, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_Properties", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zip95: BinaryAssociation = BinaryAssociation(
    name="zip95",
    ends={
        Property(name="ZipCode96", type=org_aries_common_StreetAddress, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_StreetAddress", type=ZipCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phoneNumber97: BinaryAssociation = BinaryAssociation(
    name="phoneNumber97",
    ends={
        Property(name="PhoneNumber98", type=org_aries_common_User, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_User", type=PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emailAddress99: BinaryAssociation = BinaryAssociation(
    name="emailAddress99",
    ends={
        Property(name="EmailAddress101", type=org_aries_common_User, multiplicity=Multiplicity(1, 1)),
        Property(name="org_aries_common_User100", type=EmailAddress, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xMLNSPrefixMap102: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap102",
    ends={
        Property(name="org_sgiusa_model_EStringToStringMapEntry", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot", type=org_sgiusa_model_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation103: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation103",
    ends={
        Property(name="org_sgiusa_model_EStringToStringMapEntry105", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot104", type=org_sgiusa_model_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
familyMember111: BinaryAssociation = BinaryAssociation(
    name="familyMember111",
    ends={
        Property(name="FamilyMember", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot112", type=FamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
emailList106: BinaryAssociation = BinaryAssociation(
    name="emailList106",
    ends={
        Property(name="EmailList", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot107", type=EmailList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event108: BinaryAssociation = BinaryAssociation(
    name="event108",
    ends={
        Property(name="Event110", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot109", type=Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member119: BinaryAssociation = BinaryAssociation(
    name="member119",
    ends={
        Property(name="Member", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot120", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gohonzonInfo113: BinaryAssociation = BinaryAssociation(
    name="gohonzonInfo113",
    ends={
        Property(name="GohonzonInfo", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot114", type=GohonzonInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leadershipInfo115: BinaryAssociation = BinaryAssociation(
    name="leadershipInfo115",
    ends={
        Property(name="LeadershipInfo", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot116", type=LeadershipInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leadershipRole117: BinaryAssociation = BinaryAssociation(
    name="leadershipRole117",
    ends={
        Property(name="LeadershipRole", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot118", type=LeadershipRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
membershipInfo125: BinaryAssociation = BinaryAssociation(
    name="membershipInfo125",
    ends={
        Property(name="MembershipInfo", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot126", type=MembershipInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
note127: BinaryAssociation = BinaryAssociation(
    name="note127",
    ends={
        Property(name="Note129", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot128", type=Note, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organization130: BinaryAssociation = BinaryAssociation(
    name="organization130",
    ends={
        Property(name="Organization", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot131", type=Organization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members121: BinaryAssociation = BinaryAssociation(
    name="members121",
    ends={
        Property(name="Members", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot122", type=Members, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberSearchCriteria123: BinaryAssociation = BinaryAssociation(
    name="memberSearchCriteria123",
    ends={
        Property(name="MemberSearchCriteria", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot124", type=MemberSearchCriteria, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyDeptInfo142: BinaryAssociation = BinaryAssociation(
    name="studyDeptInfo142",
    ends={
        Property(name="StudyDeptInfo", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot143", type=StudyDeptInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user144: BinaryAssociation = BinaryAssociation(
    name="user144",
    ends={
        Property(name="User146", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot145", type=User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users147: BinaryAssociation = BinaryAssociation(
    name="users147",
    ends={
        Property(name="Users", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot148", type=Users, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
view149: BinaryAssociation = BinaryAssociation(
    name="view149",
    ends={
        Property(name="View", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot150", type=View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
permission132: BinaryAssociation = BinaryAssociation(
    name="permission132",
    ends={
        Property(name="Permission", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot133", type=Permission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preferences134: BinaryAssociation = BinaryAssociation(
    name="preferences134",
    ends={
        Property(name="Preferences", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot135", type=Preferences, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
registration136: BinaryAssociation = BinaryAssociation(
    name="registration136",
    ends={
        Property(name="Registration", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot137", type=Registration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schoolInfo138: BinaryAssociation = BinaryAssociation(
    name="schoolInfo138",
    ends={
        Property(name="SchoolInfo", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot139", type=SchoolInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyDeptExam140: BinaryAssociation = BinaryAssociation(
    name="studyDeptExam140",
    ends={
        Property(name="StudyDeptExam", type=org_sgiusa_model_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_DocumentRoot141", type=StudyDeptExam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organization151: BinaryAssociation = BinaryAssociation(
    name="organization151",
    ends={
        Property(name="Organization152", type=org_sgiusa_model_EmailList, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_EmailList", type=Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emailAddressList153: BinaryAssociation = BinaryAssociation(
    name="emailAddressList153",
    ends={
        Property(name="User155", type=org_sgiusa_model_EmailList, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_EmailList154", type=User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organization156: BinaryAssociation = BinaryAssociation(
    name="organization156",
    ends={
        Property(name="Organization157", type=org_sgiusa_model_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Event", type=Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leadershipRoles158: BinaryAssociation = BinaryAssociation(
    name="leadershipRoles158",
    ends={
        Property(name="LeadershipRole159", type=org_sgiusa_model_LeadershipInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_LeadershipInfo", type=LeadershipRole, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workPhone171: BinaryAssociation = BinaryAssociation(
    name="workPhone171",
    ends={
        Property(name="PhoneNumber173", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member172", type=PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
otherPhone174: BinaryAssociation = BinaryAssociation(
    name="otherPhone174",
    ends={
        Property(name="PhoneNumber176", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member175", type=PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization177: BinaryAssociation = BinaryAssociation(
    name="organization177",
    ends={
        Property(name="Organization179", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member178", type=Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emailAddress160: BinaryAssociation = BinaryAssociation(
    name="emailAddress160",
    ends={
        Property(name="EmailAddress161", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member", type=EmailAddress, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
streetAddress162: BinaryAssociation = BinaryAssociation(
    name="streetAddress162",
    ends={
        Property(name="StreetAddress164", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member163", type=StreetAddress, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
homePhone165: BinaryAssociation = BinaryAssociation(
    name="homePhone165",
    ends={
        Property(name="PhoneNumber167", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member166", type=PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cellPhone168: BinaryAssociation = BinaryAssociation(
    name="cellPhone168",
    ends={
        Property(name="PhoneNumber170", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member169", type=PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leadershipInfo180: BinaryAssociation = BinaryAssociation(
    name="leadershipInfo180",
    ends={
        Property(name="LeadershipInfo182", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member181", type=LeadershipInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
studyDeptInfo183: BinaryAssociation = BinaryAssociation(
    name="studyDeptInfo183",
    ends={
        Property(name="StudyDeptInfo185", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member184", type=StudyDeptInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notes186: BinaryAssociation = BinaryAssociation(
    name="notes186",
    ends={
        Property(name="Note188", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member187", type=Note, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
record192: BinaryAssociation = BinaryAssociation(
    name="record192",
    ends={
        Property(name="Member193", type=org_sgiusa_model_Members, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Members", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organization194: BinaryAssociation = BinaryAssociation(
    name="organization194",
    ends={
        Property(name="Organization195", type=org_sgiusa_model_MemberSearchCriteria, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_MemberSearchCriteria", type=Organization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
familyInfo189: BinaryAssociation = BinaryAssociation(
    name="familyInfo189",
    ends={
        Property(name="FamilyMember191", type=org_sgiusa_model_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Member190", type=FamilyMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gohonzons196: BinaryAssociation = BinaryAssociation(
    name="gohonzons196",
    ends={
        Property(name="GohonzonInfo197", type=org_sgiusa_model_MembershipInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_MembershipInfo", type=GohonzonInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author198: BinaryAssociation = BinaryAssociation(
    name="author198",
    ends={
        Property(name="User199", type=org_sgiusa_model_Note, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Note", type=User, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessors211: BinaryAssociation = BinaryAssociation(
    name="accessors211",
    ends={
        Property(name="User213", type=org_sgiusa_model_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Organization212", type=User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent200: BinaryAssociation = BinaryAssociation(
    name="parent200",
    ends={
        Property(name="Organization201", type=org_sgiusa_model_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Organization", type=Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children202: BinaryAssociation = BinaryAssociation(
    name="children202",
    ends={
        Property(name="Organization204", type=org_sgiusa_model_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Organization203", type=Organization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
creator205: BinaryAssociation = BinaryAssociation(
    name="creator205",
    ends={
        Property(name="User207", type=org_sgiusa_model_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Organization206", type=User, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
provider208: BinaryAssociation = BinaryAssociation(
    name="provider208",
    ends={
        Property(name="User210", type=org_sgiusa_model_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Organization209", type=User, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization214: BinaryAssociation = BinaryAssociation(
    name="organization214",
    ends={
        Property(name="Organization215", type=org_sgiusa_model_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Permission", type=Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
user216: BinaryAssociation = BinaryAssociation(
    name="user216",
    ends={
        Property(name="User217", type=org_sgiusa_model_Registration, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Registration", type=User, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
studyDeptExams218: BinaryAssociation = BinaryAssociation(
    name="studyDeptExams218",
    ends={
        Property(name="StudyDeptExam219", type=org_sgiusa_model_StudyDeptInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_StudyDeptInfo", type=StudyDeptExam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
streetAddress225: BinaryAssociation = BinaryAssociation(
    name="streetAddress225",
    ends={
        Property(name="StreetAddress227", type=org_sgiusa_model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_User226", type=StreetAddress, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cellPhone228: BinaryAssociation = BinaryAssociation(
    name="cellPhone228",
    ends={
        Property(name="PhoneNumber230", type=org_sgiusa_model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_User229", type=PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
homePhone231: BinaryAssociation = BinaryAssociation(
    name="homePhone231",
    ends={
        Property(name="PhoneNumber233", type=org_sgiusa_model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_User232", type=PhoneNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emailAccount220: BinaryAssociation = BinaryAssociation(
    name="emailAccount220",
    ends={
        Property(name="EmailAccount221", type=org_sgiusa_model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_User", type=EmailAccount, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emailAddress222: BinaryAssociation = BinaryAssociation(
    name="emailAddress222",
    ends={
        Property(name="EmailAddress224", type=org_sgiusa_model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_User223", type=EmailAddress, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record240: BinaryAssociation = BinaryAssociation(
    name="record240",
    ends={
        Property(name="User241", type=org_sgiusa_model_Users, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_Users", type=User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
permissions234: BinaryAssociation = BinaryAssociation(
    name="permissions234",
    ends={
        Property(name="Permission236", type=org_sgiusa_model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_User235", type=Permission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preferences237: BinaryAssociation = BinaryAssociation(
    name="preferences237",
    ends={
        Property(name="Preferences239", type=org_sgiusa_model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_User238", type=Preferences, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organization242: BinaryAssociation = BinaryAssociation(
    name="organization242",
    ends={
        Property(name="Organization243", type=org_sgiusa_model_View, multiplicity=Multiplicity(1, 1)),
        Property(name="org_sgiusa_model_View", type=Organization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="org_sgiusa_model",
    types={org_aries_common_Attachment, org_aries_common_DocumentRoot, Attachment, EmailAccount, EmailAddress, org_aries_common_EStringToStringMapEntry, EmailBox, EmailMessage, Event, Map, EmailAddressList, Note, Person, PersonName, MapEntry, Properties, Property_, StreetAddress, User, PhoneNumber, org_aries_common_EmailAccount, ZipCode, org_aries_common_EmailAddress, org_aries_common_EmailAddressList, org_aries_common_EmailBox, org_aries_common_EmailMessage, org_aries_common_Event, org_aries_common_Map, org_aries_common_EObject, org_aries_common_MapEntry, org_aries_common_Person, org_aries_common_Note, org_aries_common_PersonName, org_aries_common_PhoneNumber, org_aries_common_Property, org_aries_common_Properties, org_aries_common_StreetAddress, org_aries_common_User, org_aries_common_ZipCode, org_sgiusa_model_EStringToStringMapEntry, org_sgiusa_model_DocumentRoot, FamilyMember, EmailList, Member, GohonzonInfo, LeadershipInfo, LeadershipRole, MembershipInfo, Organization, Members, MemberSearchCriteria, StudyDeptInfo, Users, View, Permission, Preferences, Registration, SchoolInfo, StudyDeptExam, org_sgiusa_model_Event, org_sgiusa_model_EmailList, org_sgiusa_model_FamilyMember, org_sgiusa_model_GohonzonInfo, org_sgiusa_model_LeadershipRole, org_sgiusa_model_LeadershipInfo, org_sgiusa_model_Member, org_sgiusa_model_Members, org_sgiusa_model_MemberSearchCriteria, org_sgiusa_model_Note, org_sgiusa_model_MembershipInfo, org_sgiusa_model_Organization, org_sgiusa_model_Permission, org_sgiusa_model_Preferences, org_sgiusa_model_Registration, org_sgiusa_model_SchoolInfo, org_sgiusa_model_StudyDeptExam, org_sgiusa_model_StudyDeptInfo, org_sgiusa_model_User, org_sgiusa_model_Users, org_sgiusa_model_View, Country, Language, PhoneNumberType, RoleType, State, Status, ActivityGroup, ActivityGroupName, Division, DivisionName, Capability, FamilyRelation, EventStatus, GohonzonType, OrganizationLevel, Position, PositionName, Role, SchoolType, StudyDeptExamLevel, StudyDeptLanguage, SubDivisionName, SubDivision, ViewType},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, attachment4, emailAccount6, emailAddress8, emailBox12, emailMessage14, event16, map18, emailAddressList10, note22, person24, personName26, mapEntry20, properties30, property32, streetAddress34, user36, phoneNumber28, zipCode38, emailBoxes40, phoneNumber42, emailAccount44, parentBox46, messageList49, fromAddress52, toAddressList54, bccAddressList57, ccAddressList60, adminAddressList66, attachments69, replytoAddressList63, user72, key76, mapEntry74, value77, author80, name82, phoneNumber84, emailAddress87, streetAddress90, property93, zip95, phoneNumber97, emailAddress99, xMLNSPrefixMap102, xSISchemaLocation103, familyMember111, emailList106, event108, member119, gohonzonInfo113, leadershipInfo115, leadershipRole117, membershipInfo125, note127, organization130, members121, memberSearchCriteria123, studyDeptInfo142, user144, users147, view149, permission132, preferences134, registration136, schoolInfo138, studyDeptExam140, organization151, emailAddressList153, organization156, leadershipRoles158, workPhone171, otherPhone174, organization177, emailAddress160, streetAddress162, homePhone165, cellPhone168, leadershipInfo180, studyDeptInfo183, notes186, record192, organization194, familyInfo189, gohonzons196, author198, accessors211, parent200, children202, creator205, provider208, organization214, user216, studyDeptExams218, streetAddress225, cellPhone228, homePhone231, emailAccount220, emailAddress222, record240, permissions234, preferences237, organization242},
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