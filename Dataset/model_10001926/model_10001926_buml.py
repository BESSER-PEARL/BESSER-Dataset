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
Users = Class(name="Users")
Auditorium = Class(name="Auditorium")
TimeInterval = Class(name="TimeInterval")
Group = Class(name="Group")
Specialty = Class(name="Specialty")
EducationalPlan = Class(name="EducationalPlan")
TimeCreditForEducationalSemester = Class(name="TimeCreditForEducationalSemester")
DocumentStorage = Class(name="DocumentStorage")
SubjectShedule = Class(name="SubjectShedule")
Subject = Class(name="Subject")
ActivityType = Class(name="ActivityType")
SubjectSheduleController = Class(name="SubjectSheduleController")

# Users class attributes and methods
Users_id: Property = Property(name="id", type=IntegerType)
Users_residentName: Property = Property(name="residentName", type=StringType)
Users_residentSurname: Property = Property(name="residentSurname", type=StringType)
Users_residentPatronymic: Property = Property(name="residentPatronymic", type=StringType)
Users_residentBirthday: Property = Property(name="residentBirthday", type=StringType)
Users_residentPassword: Property = Property(name="residentPassword", type=StringType)
Users_registrationCertificateCode: Property = Property(name="registrationCertificateCode", type=IntegerType)
Users_residentUserType: Property = Property(name="residentUserType", type=StringType)
Users_universityStructureUnit: Property = Property(name="universityStructureUnit", type=StringType)
Users_residentPosition: Property = Property(name="residentPosition", type=StringType)
Users_residentDepartment: Property = Property(name="residentDepartment", type=StringType)
Users_residentEmail: Property = Property(name="residentEmail", type=StringType)
Users_individuadIdentificationCode: Property = Property(name="individuadIdentificationCode", type=IntegerType)
Users.attributes={Users_universityStructureUnit, Users_residentSurname, Users_residentPatronymic, Users_residentDepartment, Users_registrationCertificateCode, Users_residentPassword, Users_residentPosition, Users_id, Users_residentUserType, Users_individuadIdentificationCode, Users_residentEmail, Users_residentBirthday, Users_residentName}

# Auditorium class attributes and methods
Auditorium_id: Property = Property(name="id", type=IntegerType)
Auditorium_educationalBuilding: Property = Property(name="educationalBuilding", type=StringType)
Auditorium_auditoriumNumber: Property = Property(name="auditoriumNumber", type=IntegerType)
Auditorium_is_busy: Property = Property(name="is_busy", type=BooleanType)
Auditorium.attributes={Auditorium_educationalBuilding, Auditorium_auditoriumNumber, Auditorium_is_busy, Auditorium_id}

# TimeInterval class attributes and methods
TimeInterval_id: Property = Property(name="id", type=IntegerType)
TimeInterval_date: Property = Property(name="date", type=StringType)
TimeInterval_weekIdentifier: Property = Property(name="weekIdentifier", type=IntegerType)
TimeInterval_weekday: Property = Property(name="weekday", type=IntegerType)
TimeInterval_classOrder: Property = Property(name="classOrder", type=IntegerType)
TimeInterval.attributes={TimeInterval_weekIdentifier, TimeInterval_date, TimeInterval_weekday, TimeInterval_id, TimeInterval_classOrder}

# Group class attributes and methods
Group_id: Property = Property(name="id", type=IntegerType)
Group_groupNumber: Property = Property(name="groupNumber", type=IntegerType)
Group_educationalYear: Property = Property(name="educationalYear", type=IntegerType)
Group_specialtyCode: Property = Property(name="specialtyCode", type=IntegerType)
Group.attributes={Group_specialtyCode, Group_educationalYear, Group_groupNumber, Group_id}

# Specialty class attributes and methods
Specialty_id: Property = Property(name="id", type=IntegerType)
Specialty_specialtyCode: Property = Property(name="specialtyCode", type=IntegerType)
Specialty_specialtyName: Property = Property(name="specialtyName", type=StringType)
Specialty_subjectCode: Property = Property(name="subjectCode", type=IntegerType)
Specialty.attributes={Specialty_subjectCode, Specialty_id, Specialty_specialtyCode, Specialty_specialtyName}

# EducationalPlan class attributes and methods
EducationalPlan_id: Property = Property(name="id", type=IntegerType)
EducationalPlan_individualIdentificationCode: Property = Property(name="individualIdentificationCode", type=IntegerType)
EducationalPlan_subjectCode: Property = Property(name="subjectCode", type=IntegerType)
EducationalPlan.attributes={EducationalPlan_id, EducationalPlan_individualIdentificationCode, EducationalPlan_subjectCode}

# TimeCreditForEducationalSemester class attributes and methods
TimeCreditForEducationalSemester_id: Property = Property(name="id", type=IntegerType)
TimeCreditForEducationalSemester_groupNumber: Property = Property(name="groupNumber", type=IntegerType)
TimeCreditForEducationalSemester_subjectCode: Property = Property(name="subjectCode", type=IntegerType)
TimeCreditForEducationalSemester_activityTypeCode: Property = Property(name="activityTypeCode", type=IntegerType)
TimeCreditForEducationalSemester_totalHours: Property = Property(name="totalHours", type=IntegerType)
TimeCreditForEducationalSemester.attributes={TimeCreditForEducationalSemester_id, TimeCreditForEducationalSemester_totalHours, TimeCreditForEducationalSemester_subjectCode, TimeCreditForEducationalSemester_groupNumber, TimeCreditForEducationalSemester_activityTypeCode}

# DocumentStorage class attributes and methods
DocumentStorage_documentPath: Property = Property(name="documentPath", type=StringType)
DocumentStorage_documentCode: Property = Property(name="documentCode", type=IntegerType)
DocumentStorage_is_exist: Property = Property(name="is_exist", type=BooleanType)
DocumentStorage_id: Property = Property(name="id", type=IntegerType)
DocumentStorage.attributes={DocumentStorage_is_exist, DocumentStorage_id, DocumentStorage_documentPath, DocumentStorage_documentCode}

# SubjectShedule class attributes and methods
SubjectShedule_id: Property = Property(name="id", type=IntegerType)
SubjectShedule_subjectCode: Property = Property(name="subjectCode", type=IntegerType)
SubjectShedule_groupNumber: Property = Property(name="groupNumber", type=IntegerType)
SubjectShedule_activityTypeCode: Property = Property(name="activityTypeCode", type=IntegerType)
SubjectShedule_date: Property = Property(name="date", type=StringType)
SubjectShedule_individualIdentificationCode: Property = Property(name="individualIdentificationCode", type=IntegerType)
SubjectShedule_auditoriumNumber: Property = Property(name="auditoriumNumber", type=IntegerType)
SubjectShedule.attributes={SubjectShedule_id, SubjectShedule_auditoriumNumber, SubjectShedule_activityTypeCode, SubjectShedule_groupNumber, SubjectShedule_date, SubjectShedule_individualIdentificationCode, SubjectShedule_subjectCode}

# Subject class attributes and methods
Subject_id: Property = Property(name="id", type=IntegerType)
Subject_subjectCode: Property = Property(name="subjectCode", type=IntegerType)
Subject_subjectName: Property = Property(name="subjectName", type=StringType)
Subject.attributes={Subject_subjectCode, Subject_subjectName, Subject_id}

# ActivityType class attributes and methods
ActivityType_id: Property = Property(name="id", type=IntegerType)
ActivityType_activityTypeCode: Property = Property(name="activityTypeCode", type=IntegerType)
ActivityType_activityTypeName: Property = Property(name="activityTypeName", type=StringType)
ActivityType_subjectCode: Property = Property(name="subjectCode", type=IntegerType)
ActivityType.attributes={ActivityType_activityTypeCode, ActivityType_id, ActivityType_subjectCode, ActivityType_activityTypeName}

# SubjectSheduleController class attributes and methods
SubjectSheduleController_subjectCodeService: Property = Property(name="subjectCodeService", type=StringType)
SubjectSheduleController_groupNumberService: Property = Property(name="groupNumberService", type=IntegerType)
SubjectSheduleController_activityTypeCodeService: Property = Property(name="activityTypeCodeService", type=IntegerType)
SubjectSheduleController_dateService: Property = Property(name="dateService", type=StringType)
SubjectSheduleController_individualIdentificationCodeService: Property = Property(name="individualIdentificationCodeService", type=IntegerType)
SubjectSheduleController_auditoriumNumberService: Property = Property(name="auditoriumNumberService", type=IntegerType)
SubjectSheduleController.attributes={SubjectSheduleController_subjectCodeService, SubjectSheduleController_auditoriumNumberService, SubjectSheduleController_individualIdentificationCodeService, SubjectSheduleController_dateService, SubjectSheduleController_groupNumberService, SubjectSheduleController_activityTypeCodeService}

# Relationships
assoc__JGODfZfZEeqEM7mFKilpXw: BinaryAssociation = BinaryAssociation(
    name="assoc__JGODfZfZEeqEM7mFKilpXw",
    ends={
        Property(name="assoc_00", type=ActivityType, multiplicity=Multiplicity(0, 9999)),
        Property(name="assoc_11", type=Subject, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_dwj4oJE9Eemqpd237shV0A",
    types={Users, Auditorium, TimeInterval, Group, Specialty, EducationalPlan, TimeCreditForEducationalSemester, DocumentStorage, SubjectShedule, Subject, ActivityType, SubjectSheduleController},
    associations={assoc__JGODfZfZEeqEM7mFKilpXw},
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