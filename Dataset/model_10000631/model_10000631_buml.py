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
EnrollPatient_Controller = Class(name="EnrollPatient_Controller")
StateDAO = Class(name="StateDAO")
PatientTO = Class(name="PatientTO")
StateDAO1 = Class(name="StateDAO1")
PatientBO = Class(name="PatientBO")
PatientDAO = Class(name="PatientDAO")
PlanDAO = Class(name="PlanDAO")
Class_ = Class(name="Class")

# EnrollPatient_Controller class attributes and methods

# StateDAO class attributes and methods

# PatientTO class attributes and methods
PatientTO_patient_id: Property = Property(name="patient_id", type=IntegerType)
PatientTO_first_name: Property = Property(name="first_name", type=StringType)
PatientTO_last_name: Property = Property(name="last_name", type=StringType)
PatientTO_password: Property = Property(name="password", type=StringType)
PatientTO_date_of_birth: Property = Property(name="date_of_birth", type=DateType)
PatientTO_email: Property = Property(name="email", type=StringType)
PatientTO_contact_no: Property = Property(name="contact_no", type=IntegerType)
PatientTO_state_id: Property = Property(name="state_id", type=IntegerType)
PatientTO_plan_id: Property = Property(name="plan_id", type=IntegerType)
PatientTO.attributes={PatientTO_first_name, PatientTO_state_id, PatientTO_email, PatientTO_date_of_birth, PatientTO_plan_id, PatientTO_contact_no, PatientTO_patient_id, PatientTO_last_name, PatientTO_password}

# StateDAO1 class attributes and methods

# PatientBO class attributes and methods

# PatientDAO class attributes and methods

# PlanDAO class attributes and methods

# Class class attributes and methods

# Relationships
EnrollPatient_Controller_PatientBO: BinaryAssociation = BinaryAssociation(
    name="EnrollPatient_Controller_PatientBO",
    ends={
        Property(name="patientBO0", type=PatientBO, multiplicity=Multiplicity(0, 1)),
        Property(name="enrollPatient_Controller1", type=EnrollPatient_Controller, multiplicity=Multiplicity(0, 1))
    }
)
PatientDAO_StateDAO: BinaryAssociation = BinaryAssociation(
    name="PatientDAO_StateDAO",
    ends={
        Property(name="stateDAO2", type=StateDAO1, multiplicity=Multiplicity(0, 1)),
        Property(name="patientDAO3", type=PatientDAO, multiplicity=Multiplicity(0, 1))
    }
)
PatientBO_PatientDAO: BinaryAssociation = BinaryAssociation(
    name="PatientBO_PatientDAO",
    ends={
        Property(name="patientDAO4", type=PatientDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="patientBO5", type=PatientBO, multiplicity=Multiplicity(0, 1))
    }
)
PatientDAO_PlanDAO: BinaryAssociation = BinaryAssociation(
    name="PatientDAO_PlanDAO",
    ends={
        Property(name="planDAO6", type=PlanDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="patientDAO7", type=PatientDAO, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4d96bb58_c194_4b0b_8872_7533dc8b0e56",
    types={EnrollPatient_Controller, StateDAO, PatientTO, StateDAO1, PatientBO, PatientDAO, PlanDAO, Class_},
    associations={EnrollPatient_Controller_PatientBO, PatientDAO_StateDAO, PatientBO_PatientDAO, PatientDAO_PlanDAO},
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