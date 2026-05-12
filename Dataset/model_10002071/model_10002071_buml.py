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
DossierPatient = Class(name="DossierPatient")
Patient = Class(name="Patient")
Rendez_Vous = Class(name="Rendez_Vous")
Consultion = Class(name="Consultion")
Examen = Class(name="Examen")
Medecin = Class(name="Medecin")
Service = Class(name="Service")
Programme = Class(name="Programme")
CentreHospitalier = Class(name="CentreHospitalier")
ResultatExamen = Class(name="ResultatExamen")
Secretaire_external = Class(name="Secretaire_external")

# DossierPatient class attributes and methods
DossierPatient_numeroPatient: Property = Property(name="numeroPatient", type=IntegerType)
DossierPatient_nomDossier: Property = Property(name="nomDossier", type=StringType)
DossierPatient_dateCreation: Property = Property(name="dateCreation", type=IntegerType)
DossierPatient_heure: Property = Property(name="heure", type=IntegerType)
DossierPatient_infoAntecedant: Property = Property(name="infoAntecedant", type=StringType)
DossierPatient.attributes={DossierPatient_nomDossier, DossierPatient_dateCreation, DossierPatient_numeroPatient, DossierPatient_infoAntecedant, DossierPatient_heure}

# Patient class attributes and methods
Patient_numeroPatien: Property = Property(name="numeroPatien", type=IntegerType)
Patient_nomPatient: Property = Property(name="nomPatient", type=StringType)
Patient_prenomPatien: Property = Property(name="prenomPatien", type=StringType)
Patient_agePatient: Property = Property(name="agePatient", type=IntegerType)
Patient_lieuResidence: Property = Property(name="lieuResidence", type=StringType)
Patient_profession: Property = Property(name="profession", type=StringType)
Patient.attributes={Patient_nomPatient, Patient_lieuResidence, Patient_prenomPatien, Patient_numeroPatien, Patient_profession, Patient_agePatient}

# Rendez_Vous class attributes and methods
Rendez_Vous_numeroRdV: Property = Property(name="numeroRdV", type=IntegerType)
Rendez_Vous_dateRDV: Property = Property(name="dateRDV", type=StringType)
Rendez_Vous_heure: Property = Property(name="heure", type=StringType)
Rendez_Vous_lieuRDV: Property = Property(name="lieuRDV", type=StringType)
Rendez_Vous.attributes={Rendez_Vous_lieuRDV, Rendez_Vous_heure, Rendez_Vous_numeroRdV, Rendez_Vous_dateRDV}

# Consultion class attributes and methods
Consultion_numeroConsultation: Property = Property(name="numeroConsultation", type=IntegerType)
Consultion_dateConsultation: Property = Property(name="dateConsultation", type=StringType)
Consultion_heure: Property = Property(name="heure", type=StringType)
Consultion_description: Property = Property(name="description", type=StringType)
Consultion.attributes={Consultion_heure, Consultion_numeroConsultation, Consultion_description, Consultion_dateConsultation}

# Examen class attributes and methods
Examen_numeroExamen: Property = Property(name="numeroExamen", type=IntegerType)
Examen_dateProvisoir: Property = Property(name="dateProvisoir", type=StringType)
Examen_heure: Property = Property(name="heure", type=StringType)
Examen_motif: Property = Property(name="motif", type=StringType)
Examen.attributes={Examen_numeroExamen, Examen_heure, Examen_motif, Examen_dateProvisoir}

# Medecin class attributes and methods
Medecin_numeroMedecin: Property = Property(name="numeroMedecin", type=IntegerType)
Medecin_nomMedecin: Property = Property(name="nomMedecin", type=StringType)
Medecin_prenomMedecin: Property = Property(name="prenomMedecin", type=StringType)
Medecin_dateNaissance: Property = Property(name="dateNaissance", type=StringType)
Medecin_specialite: Property = Property(name="specialite", type=StringType)
Medecin.attributes={Medecin_numeroMedecin, Medecin_dateNaissance, Medecin_specialite, Medecin_nomMedecin, Medecin_prenomMedecin}

# Service class attributes and methods
Service_numeroService: Property = Property(name="numeroService", type=IntegerType)
Service_nomService: Property = Property(name="nomService", type=StringType)
Service_descriptionService: Property = Property(name="descriptionService", type=StringType)
Service.attributes={Service_numeroService, Service_nomService, Service_descriptionService}

# Programme class attributes and methods
Programme_numeroProgramme: Property = Property(name="numeroProgramme", type=StringType)
Programme_date: Property = Property(name="date", type=StringType)
Programme_heure: Property = Property(name="heure", type=StringType)
Programme.attributes={Programme_heure, Programme_numeroProgramme, Programme_date}

# CentreHospitalier class attributes and methods
CentreHospitalier_numeroCentre: Property = Property(name="numeroCentre", type=IntegerType)
CentreHospitalier_nomCentre: Property = Property(name="nomCentre", type=StringType)
CentreHospitalier_descriptionCentre: Property = Property(name="descriptionCentre", type=StringType)
CentreHospitalier.attributes={CentreHospitalier_numeroCentre, CentreHospitalier_descriptionCentre, CentreHospitalier_nomCentre}

# ResultatExamen class attributes and methods
ResultatExamen_numeroResultat: Property = Property(name="numeroResultat", type=IntegerType)
ResultatExamen_infoResultat: Property = Property(name="infoResultat", type=StringType)
ResultatExamen.attributes={ResultatExamen_infoResultat, ResultatExamen_numeroResultat}

# Secretaire_external class attributes and methods

# Relationships
DossierPatient_Patient: BinaryAssociation = BinaryAssociation(
    name="DossierPatient_Patient",
    ends={
        Property(name="patient0", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="dossierPatient1", type=DossierPatient, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_Rendez_Vous: BinaryAssociation = BinaryAssociation(
    name="Patient_Rendez_Vous",
    ends={
        Property(name="rendez_Vous2", type=Rendez_Vous, multiplicity=Multiplicity(1, 9999)),
        Property(name="patient3", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
Rendez_Vous_Consultion: BinaryAssociation = BinaryAssociation(
    name="Rendez_Vous_Consultion",
    ends={
        Property(name="consultion4", type=Consultion, multiplicity=Multiplicity(0, 1)),
        Property(name="rendez_Vous5", type=Rendez_Vous, multiplicity=Multiplicity(0, 1))
    }
)
Rendez_Vous_Examen: BinaryAssociation = BinaryAssociation(
    name="Rendez_Vous_Examen",
    ends={
        Property(name="examen6", type=Examen, multiplicity=Multiplicity(0, 1)),
        Property(name="rendez_Vous7", type=Rendez_Vous, multiplicity=Multiplicity(0, 1))
    }
)
Rendez_Vous_Medecin: BinaryAssociation = BinaryAssociation(
    name="Rendez_Vous_Medecin",
    ends={
        Property(name="medecin8", type=Medecin, multiplicity=Multiplicity(0, 1)),
        Property(name="rendez_Vous9", type=Rendez_Vous, multiplicity=Multiplicity(0, 1))
    }
)
Programme_Medecin: BinaryAssociation = BinaryAssociation(
    name="Programme_Medecin",
    ends={
        Property(name="medecin10", type=Medecin, multiplicity=Multiplicity(0, 1)),
        Property(name="programme11", type=Programme, multiplicity=Multiplicity(0, 1))
    }
)
Medecin_Service: BinaryAssociation = BinaryAssociation(
    name="Medecin_Service",
    ends={
        Property(name="service12", type=Service, multiplicity=Multiplicity(0, 1)),
        Property(name="medecin13", type=Medecin, multiplicity=Multiplicity(0, 1))
    }
)
Service_CentreHospitalier: BinaryAssociation = BinaryAssociation(
    name="Service_CentreHospitalier",
    ends={
        Property(name="centreHospitalier14", type=CentreHospitalier, multiplicity=Multiplicity(1, 1)),
        Property(name="service15", type=Service, multiplicity=Multiplicity(1, 9999))
    }
)
Secretaire_ResultatExamen: BinaryAssociation = BinaryAssociation(
    name="Secretaire_ResultatExamen",
    ends={
        Property(name="resultatExamen16", type=ResultatExamen, multiplicity=Multiplicity(0, 9999)),
        Property(name="secretaire17", type=Secretaire_external, multiplicity=Multiplicity(1, 1))
    }
)
ResultatExamen_Medecin: BinaryAssociation = BinaryAssociation(
    name="ResultatExamen_Medecin",
    ends={
        Property(name="medecin18", type=Medecin, multiplicity=Multiplicity(0, 1)),
        Property(name="resultatExamen19", type=ResultatExamen, multiplicity=Multiplicity(0, 1))
    }
)
Patient_ResultatExamen: BinaryAssociation = BinaryAssociation(
    name="Patient_ResultatExamen",
    ends={
        Property(name="resultatExamen20", type=ResultatExamen, multiplicity=Multiplicity(0, 1)),
        Property(name="patient21", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_mjAyMHnbEeqeQcxm9hmzHw",
    types={DossierPatient, Patient, Rendez_Vous, Consultion, Examen, Medecin, Service, Programme, CentreHospitalier, ResultatExamen, Secretaire_external},
    associations={DossierPatient_Patient, Patient_Rendez_Vous, Rendez_Vous_Consultion, Rendez_Vous_Examen, Rendez_Vous_Medecin, Programme_Medecin, Medecin_Service, Service_CentreHospitalier, Secretaire_ResultatExamen, ResultatExamen_Medecin, Patient_ResultatExamen},
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