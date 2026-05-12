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
admission_receptionist_Actor = Class(name="admission_receptionist_Actor")
patient_Actor = Class(name="patient_Actor")
release_receptionist_Actor = Class(name="release_receptionist_Actor")
floor_nurse_Actor = Class(name="floor_nurse_Actor")
physicians_Actor = Class(name="physicians_Actor")
medical_technologist_Actor = Class(name="medical_technologist_Actor")
hospital_admission_system_Component = Class(name="hospital_admission_system_Component")
student_Actor = Class(name="student_Actor")
Part = Class(name="Part")
Storage = Class(name="Storage")
_supplier = Class(name="_supplier")
price_quote = Class(name="price_quote")
Routing_number = Class(name="Routing_number")
enter_lab_notes_external = Class(name="enter_lab_notes_external")
enter_patient_notes_external = Class(name="enter_patient_notes_external")
check_in_external = Class(name="check_in_external")
check_out_external = Class(name="check_out_external")
receive_patient_records_external = Class(name="receive_patient_records_external")
receive_records_external = Class(name="receive_records_external")
list_of_patients_external = Class(name="list_of_patients_external")

# admission_receptionist_Actor class attributes and methods

# patient_Actor class attributes and methods

# release_receptionist_Actor class attributes and methods

# floor_nurse_Actor class attributes and methods

# physicians_Actor class attributes and methods

# medical_technologist_Actor class attributes and methods

# hospital_admission_system_Component class attributes and methods

# student_Actor class attributes and methods

# Part class attributes and methods
Part__part_number: Property = Property(name="_part_number", type=StringType)
Part__description: Property = Property(name="_description", type=StringType)
Part.attributes={Part__description, Part__part_number}

# Storage class attributes and methods
Storage_instruction_ID: Property = Property(name="instruction_ID", type=StringType)
Storage.attributes={Storage_instruction_ID}

# _supplier class attributes and methods
_supplier__supplier_ID: Property = Property(name="_supplier_ID", type=StringType)
_supplier.attributes={_supplier__supplier_ID}

# price_quote class attributes and methods
price_quote__bulk_rate_price: Property = Property(name="_bulk_rate_price", type=StringType)
price_quote.attributes={price_quote__bulk_rate_price}

# Routing_number class attributes and methods

# enter_lab_notes_external class attributes and methods

# enter_patient_notes_external class attributes and methods

# check_in_external class attributes and methods

# check_out_external class attributes and methods

# receive_patient_records_external class attributes and methods

# receive_records_external class attributes and methods

# list_of_patients_external class attributes and methods

# Relationships
enter_lab_notes_medical_technologist: BinaryAssociation = BinaryAssociation(
    name="enter_lab_notes_medical_technologist",
    ends={
        Property(name="medical_technologist0", type=medical_technologist_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="enter_lab_notes1", type=enter_lab_notes_external, multiplicity=Multiplicity(0, 1))
    }
)
enter_patient_notes_physicians: BinaryAssociation = BinaryAssociation(
    name="enter_patient_notes_physicians",
    ends={
        Property(name="physicians2", type=physicians_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="enter_patient_notes3", type=enter_patient_notes_external, multiplicity=Multiplicity(0, 1))
    }
)
admission_receptionist_check_in: BinaryAssociation = BinaryAssociation(
    name="admission_receptionist_check_in",
    ends={
        Property(name="check_in4", type=check_in_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admission_receptionist5", type=admission_receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admission_receptionist_patient: BinaryAssociation = BinaryAssociation(
    name="admission_receptionist_patient",
    ends={
        Property(name="patient6", type=patient_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="admission_receptionist7", type=admission_receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
patient_release_receptionist: BinaryAssociation = BinaryAssociation(
    name="patient_release_receptionist",
    ends={
        Property(name="release_receptionist8", type=release_receptionist_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="patient9", type=patient_Actor, multiplicity=Multiplicity(0, 1))
    }
)
release_receptionist_check_out: BinaryAssociation = BinaryAssociation(
    name="release_receptionist_check_out",
    ends={
        Property(name="check_out10", type=check_out_external, multiplicity=Multiplicity(0, 1)),
        Property(name="release_receptionist11", type=release_receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
medical_technologist_receive_patient_records: BinaryAssociation = BinaryAssociation(
    name="medical_technologist_receive_patient_records",
    ends={
        Property(name="receive_patient_records12", type=receive_patient_records_external, multiplicity=Multiplicity(0, 1)),
        Property(name="medical_technologist13", type=medical_technologist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
physicians_receive_records: BinaryAssociation = BinaryAssociation(
    name="physicians_receive_records",
    ends={
        Property(name="receive_records14", type=receive_records_external, multiplicity=Multiplicity(0, 1)),
        Property(name="physicians15", type=physicians_Actor, multiplicity=Multiplicity(0, 1))
    }
)
floor_nurse_enter_patient_notes: BinaryAssociation = BinaryAssociation(
    name="floor_nurse_enter_patient_notes",
    ends={
        Property(name="enter_patient_notes16", type=enter_patient_notes_external, multiplicity=Multiplicity(0, 1)),
        Property(name="floor_nurse17", type=floor_nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
floor_nurse_list_of_patients: BinaryAssociation = BinaryAssociation(
    name="floor_nurse_list_of_patients",
    ends={
        Property(name="list_of_patients18", type=list_of_patients_external, multiplicity=Multiplicity(0, 1)),
        Property(name="floor_nurse19", type=floor_nurse_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Part_Storage: BinaryAssociation = BinaryAssociation(
    name="Part_Storage",
    ends={
        Property(name="storage20", type=Storage, multiplicity=Multiplicity(1, 9999)),
        Property(name="part21", type=Part, multiplicity=Multiplicity(0, 9999))
    }
)
Part_Part: BinaryAssociation = BinaryAssociation(
    name="Part_Part",
    ends={
        Property(name="subpart22", type=Part, multiplicity=Multiplicity(0, 9999)),
        Property(name="part23", type=Part, multiplicity=Multiplicity(1, 9999))
    }
)
Part__supplier: BinaryAssociation = BinaryAssociation(
    name="Part__supplier",
    ends={
        Property(name="_supplier24", type=_supplier, multiplicity=Multiplicity(1, 9999)),
        Property(name="part25", type=Part, multiplicity=Multiplicity(0, 9999))
    }
)
price_quote__supplier: BinaryAssociation = BinaryAssociation(
    name="price_quote__supplier",
    ends={
        Property(name="_supplier26", type=_supplier, multiplicity=Multiplicity(1, 1)),
        Property(name="price_quote27", type=price_quote, multiplicity=Multiplicity(1, 1))
    }
)
Part_price_quote: BinaryAssociation = BinaryAssociation(
    name="Part_price_quote",
    ends={
        Property(name="price_quote28", type=price_quote, multiplicity=Multiplicity(1, 1)),
        Property(name="part29", type=Part, multiplicity=Multiplicity(1, 1))
    }
)
Routing_number_Part: BinaryAssociation = BinaryAssociation(
    name="Routing_number_Part",
    ends={
        Property(name="part30", type=Part, multiplicity=Multiplicity(1, 1)),
        Property(name="routing_number31", type=Routing_number, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_QSy1kNQvEeehRMl7r1_c5g",
    types={admission_receptionist_Actor, patient_Actor, release_receptionist_Actor, floor_nurse_Actor, physicians_Actor, medical_technologist_Actor, hospital_admission_system_Component, student_Actor, Part, Storage, _supplier, price_quote, Routing_number, enter_lab_notes_external, enter_patient_notes_external, check_in_external, check_out_external, receive_patient_records_external, receive_records_external, list_of_patients_external},
    associations={enter_lab_notes_medical_technologist, enter_patient_notes_physicians, admission_receptionist_check_in, admission_receptionist_patient, patient_release_receptionist, release_receptionist_check_out, medical_technologist_receive_patient_records, physicians_receive_records, floor_nurse_enter_patient_notes, floor_nurse_list_of_patients, Part_Storage, Part_Part, Part__supplier, price_quote__supplier, Part_price_quote, Routing_number_Part},
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