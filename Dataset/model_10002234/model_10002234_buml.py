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
Supervisor_Actor = Class(name="Supervisor_Actor")
Pr_fungsplaner_Component = Class(name="Pr_fungsplaner_Component")
ExaminationDate = Class(name="ExaminationDate")
Pr_funungen_einsehen_external = Class(name="Pr_funungen_einsehen_external")
Im_LTS_anmelden_external = Class(name="Im_LTS_anmelden_external")
Pr_fungsplaner_einsehen_external = Class(name="Pr_fungsplaner_einsehen_external")
Pr_fungstermine_verschieben_external = Class(name="Pr_fungstermine_verschieben_external")
Pr_fungen_sehen_external = Class(name="Pr_fungen_sehen_external")
PDF_Datei_erstellen_external = Class(name="PDF_Datei_erstellen_external")
Kalendarische_Ansicht_ver_ndern_external = Class(name="Kalendarische_Ansicht_ver_ndern_external")
Benutzer_Actor = Class(name="Benutzer_Actor")

# Supervisor_Actor class attributes and methods

# Pr_fungsplaner_Component class attributes and methods

# ExaminationDate class attributes and methods
ExaminationDate_attribute: Property = Property(name="attribute", type=StringType)
ExaminationDate_attribute2: Property = Property(name="attribute2", type=StringType)
ExaminationDate.attributes={ExaminationDate_attribute, ExaminationDate_attribute2}

# Pr_funungen_einsehen_external class attributes and methods

# Im_LTS_anmelden_external class attributes and methods

# Pr_fungsplaner_einsehen_external class attributes and methods

# Pr_fungstermine_verschieben_external class attributes and methods

# Pr_fungen_sehen_external class attributes and methods

# PDF_Datei_erstellen_external class attributes and methods

# Kalendarische_Ansicht_ver_ndern_external class attributes and methods

# Benutzer_Actor class attributes and methods

# Relationships
Im_LTS_anmelden_Pr_funungen_einsehen: BinaryAssociation = BinaryAssociation(
    name="Im_LTS_anmelden_Pr_funungen_einsehen",
    ends={
        Property(name="pr_funungen_einsehen0", type=Pr_funungen_einsehen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="im_LTS_anmelden1", type=Im_LTS_anmelden_external, multiplicity=Multiplicity(0, 1))
    }
)
Im_LTS_anmelden_Pr_fungsplaner_einsehen: BinaryAssociation = BinaryAssociation(
    name="Im_LTS_anmelden_Pr_fungsplaner_einsehen",
    ends={
        Property(name="pr_fungsplaner_einsehen2", type=Pr_fungsplaner_einsehen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="im_LTS_anmelden3", type=Im_LTS_anmelden_external, multiplicity=Multiplicity(0, 1))
    }
)
Pr_fungsplaner_einsehen_Pr_fungstermine_verschieben: BinaryAssociation = BinaryAssociation(
    name="Pr_fungsplaner_einsehen_Pr_fungstermine_verschieben",
    ends={
        Property(name="pr_fungstermine_verschieben4", type=Pr_fungstermine_verschieben_external, multiplicity=Multiplicity(0, 1)),
        Property(name="pr_fungsplaner_einsehen5", type=Pr_fungsplaner_einsehen_external, multiplicity=Multiplicity(0, 1))
    }
)
Pr_fungsplaner_einsehen_Pr_fungen_sehen: BinaryAssociation = BinaryAssociation(
    name="Pr_fungsplaner_einsehen_Pr_fungen_sehen",
    ends={
        Property(name="pr_fungen_sehen6", type=Pr_fungen_sehen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="pr_fungsplaner_einsehen7", type=Pr_fungsplaner_einsehen_external, multiplicity=Multiplicity(0, 1))
    }
)
Pr_fungsplaner_einsehen_PDF_Datei_erstellen: BinaryAssociation = BinaryAssociation(
    name="Pr_fungsplaner_einsehen_PDF_Datei_erstellen",
    ends={
        Property(name="pDF_Datei_erstellen8", type=PDF_Datei_erstellen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="pr_fungsplaner_einsehen9", type=Pr_fungsplaner_einsehen_external, multiplicity=Multiplicity(0, 1))
    }
)
Pr_fungsplaner_einsehen_Kalendarische_Ansicht_ver_ndern: BinaryAssociation = BinaryAssociation(
    name="Pr_fungsplaner_einsehen_Kalendarische_Ansicht_ver_ndern",
    ends={
        Property(name="kalendarische_Ansicht_ver_ndern10", type=Kalendarische_Ansicht_ver_ndern_external, multiplicity=Multiplicity(0, 1)),
        Property(name="pr_fungsplaner_einsehen11", type=Pr_fungsplaner_einsehen_external, multiplicity=Multiplicity(0, 1))
    }
)
Benutzer_Im_LTS_anmelden: BinaryAssociation = BinaryAssociation(
    name="Benutzer_Im_LTS_anmelden",
    ends={
        Property(name="im_LTS_anmelden12", type=Im_LTS_anmelden_external, multiplicity=Multiplicity(0, 1)),
        Property(name="benutzer13", type=Benutzer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Supervisor_Im_LTS_anmelden: BinaryAssociation = BinaryAssociation(
    name="Supervisor_Im_LTS_anmelden",
    ends={
        Property(name="im_LTS_anmelden14", type=Im_LTS_anmelden_external, multiplicity=Multiplicity(0, 1)),
        Property(name="supervisor15", type=Supervisor_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_yMS34Eb0EeiOybRP6Wy3kg",
    types={Supervisor_Actor, Pr_fungsplaner_Component, ExaminationDate, Pr_funungen_einsehen_external, Im_LTS_anmelden_external, Pr_fungsplaner_einsehen_external, Pr_fungstermine_verschieben_external, Pr_fungen_sehen_external, PDF_Datei_erstellen_external, Kalendarische_Ansicht_ver_ndern_external, Benutzer_Actor},
    associations={Im_LTS_anmelden_Pr_funungen_einsehen, Im_LTS_anmelden_Pr_fungsplaner_einsehen, Pr_fungsplaner_einsehen_Pr_fungstermine_verschieben, Pr_fungsplaner_einsehen_Pr_fungen_sehen, Pr_fungsplaner_einsehen_PDF_Datei_erstellen, Pr_fungsplaner_einsehen_Kalendarische_Ansicht_ver_ndern, Benutzer_Im_LTS_anmelden, Supervisor_Im_LTS_anmelden},
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