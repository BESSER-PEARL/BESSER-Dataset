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
Patient = Class(name="Patient")
Examen = Class(name="Examen")
Medecin = Class(name="Medecin")
Service = Class(name="Service")
Programme = Class(name="Programme")
CentreHospitalier = Class(name="CentreHospitalier")
ResultatExamen = Class(name="ResultatExamen")
Laboratoire = Class(name="Laboratoire")
Personne = Class(name="Personne")
Contact = Class(name="Contact")
Rendez_vous = Class(name="Rendez_vous")
Ordonance = Class(name="Ordonance")
Produit = Class(name="Produit")
Rendez_vous_Laboratoire_Patient_external = Class(name="Rendez_vous_Laboratoire_Patient_external")
Rendez_vous_Medecin_Patient_external = Class(name="Rendez_vous_Medecin_Patient_external")

# Patient class attributes and methods
Patient_numeroPatien: Property = Property(name="numeroPatien", type=IntegerType)
Patient_nomPatient: Property = Property(name="nomPatient", type=StringType)
Patient_prenomPatien: Property = Property(name="prenomPatien", type=StringType)
Patient_agePatient: Property = Property(name="agePatient", type=IntegerType)
Patient_lieuResidence: Property = Property(name="lieuResidence", type=StringType)
Patient_profession: Property = Property(name="profession", type=StringType)
Patient.attributes={Patient_nomPatient, Patient_prenomPatien, Patient_agePatient, Patient_lieuResidence, Patient_numeroPatien, Patient_profession}

# Examen class attributes and methods
Examen_numeroExamen: Property = Property(name="numeroExamen", type=IntegerType)
Examen_dateProvisoir: Property = Property(name="dateProvisoir", type=StringType)
Examen_heure: Property = Property(name="heure", type=StringType)
Examen_motif: Property = Property(name="motif", type=StringType)
Examen.attributes={Examen_dateProvisoir, Examen_numeroExamen, Examen_motif, Examen_heure}

# Medecin class attributes and methods
Medecin_nomMedecin: Property = Property(name="nomMedecin", type=StringType)
Medecin_prenomMedecin: Property = Property(name="prenomMedecin", type=StringType)
Medecin_dateNaissance: Property = Property(name="dateNaissance", type=StringType)
Medecin_specialite: Property = Property(name="specialite", type=StringType)
Medecin.attributes={Medecin_specialite, Medecin_dateNaissance, Medecin_nomMedecin, Medecin_prenomMedecin}

# Service class attributes and methods
Service_numeroService: Property = Property(name="numeroService", type=IntegerType)
Service_nomService: Property = Property(name="nomService", type=StringType)
Service_descriptionService: Property = Property(name="descriptionService", type=StringType)
Service.attributes={Service_descriptionService, Service_nomService, Service_numeroService}

# Programme class attributes and methods
Programme_numeroProgramme: Property = Property(name="numeroProgramme", type=StringType)
Programme_date: Property = Property(name="date", type=StringType)
Programme_heure: Property = Property(name="heure", type=StringType)
Programme.attributes={Programme_date, Programme_numeroProgramme, Programme_heure}

# CentreHospitalier class attributes and methods
CentreHospitalier_numeroCentre: Property = Property(name="numeroCentre", type=IntegerType)
CentreHospitalier_nomCentre: Property = Property(name="nomCentre", type=StringType)
CentreHospitalier_descriptionCentre: Property = Property(name="descriptionCentre", type=StringType)
CentreHospitalier.attributes={CentreHospitalier_numeroCentre, CentreHospitalier_descriptionCentre, CentreHospitalier_nomCentre}

# ResultatExamen class attributes and methods
ResultatExamen_numeroResultat: Property = Property(name="numeroResultat", type=IntegerType)
ResultatExamen_infoResultat: Property = Property(name="infoResultat", type=StringType)
ResultatExamen.attributes={ResultatExamen_infoResultat, ResultatExamen_numeroResultat}

# Laboratoire class attributes and methods
Laboratoire_id: Property = Property(name="id", type=IntegerType)
Laboratoire_numero: Property = Property(name="numero", type=StringType)
Laboratoire_nom: Property = Property(name="nom", type=StringType)
Laboratoire.attributes={Laboratoire_numero, Laboratoire_nom, Laboratoire_id}

# Personne class attributes and methods
Personne_id: Property = Property(name="id", type=IntegerType)
Personne_numero: Property = Property(name="numero", type=StringType)
Personne_nom: Property = Property(name="nom", type=StringType)
Personne_prenom: Property = Property(name="prenom", type=StringType)
Personne_attribute: Property = Property(name="attribute", type=StringType)
Personne_numeroMedecin: Property = Property(name="numeroMedecin", type=IntegerType)
Personne.attributes={Personne_numeroMedecin, Personne_prenom, Personne_attribute, Personne_nom, Personne_numero, Personne_id}

# Contact class attributes and methods
Contact_id: Property = Property(name="id", type=IntegerType)
Contact_telephone: Property = Property(name="telephone", type=IntegerType)
Contact_mail: Property = Property(name="mail", type=StringType)
Contact.attributes={Contact_mail, Contact_telephone, Contact_id}

# Rendez_vous class attributes and methods
Rendez_vous_numero: Property = Property(name="numero", type=StringType)
Rendez_vous_date: Property = Property(name="date", type=StringType)
Rendez_vous_id: Property = Property(name="id", type=IntegerType)
Rendez_vous.attributes={Rendez_vous_numero, Rendez_vous_date, Rendez_vous_id}

# Ordonance class attributes and methods
Ordonance_id: Property = Property(name="id", type=IntegerType)
Ordonance_date: Property = Property(name="date", type=StringType)
Ordonance.attributes={Ordonance_id, Ordonance_date}

# Produit class attributes and methods
Produit_id: Property = Property(name="id", type=IntegerType)
Produit_nom: Property = Property(name="nom", type=StringType)
Produit_dose: Property = Property(name="dose", type=StringType)
Produit_posologie: Property = Property(name="posologie", type=StringType)
Produit.attributes={Produit_posologie, Produit_nom, Produit_dose, Produit_id}

# Rendez_vous_Laboratoire_Patient_external class attributes and methods

# Rendez_vous_Medecin_Patient_external class attributes and methods

# Relationships
Medecin_Service: BinaryAssociation = BinaryAssociation(
    name="Medecin_Service",
    ends={
        Property(name="service0", type=Service, multiplicity=Multiplicity(0, 1)),
        Property(name="medecin1", type=Medecin, multiplicity=Multiplicity(0, 1))
    }
)
Service_CentreHospitalier: BinaryAssociation = BinaryAssociation(
    name="Service_CentreHospitalier",
    ends={
        Property(name="centreHospitalier2", type=CentreHospitalier, multiplicity=Multiplicity(1, 1)),
        Property(name="service3", type=Service, multiplicity=Multiplicity(1, 9999))
    }
)
Personne_Contact: BinaryAssociation = BinaryAssociation(
    name="Personne_Contact",
    ends={
        Property(name="personne4", type=Personne, multiplicity=Multiplicity(1, 1)),
        Property(name="contact5", type=Contact, multiplicity=Multiplicity(0, 9999))
    }
)
Rendez_vous_Laboratoire_Patient_Examen: BinaryAssociation = BinaryAssociation(
    name="Rendez_vous_Laboratoire_Patient_Examen",
    ends={
        Property(name="rendez_vous_Laboratoire_Patient6", type=Rendez_vous_Laboratoire_Patient_external, multiplicity=Multiplicity(0, 1)),
        Property(name="examen7", type=Examen, multiplicity=Multiplicity(0, 1))
    }
)
Examen_ResultatExamen: BinaryAssociation = BinaryAssociation(
    name="Examen_ResultatExamen",
    ends={
        Property(name="examen8", type=Examen, multiplicity=Multiplicity(0, 1)),
        Property(name="resultatExamen9", type=ResultatExamen, multiplicity=Multiplicity(0, 1))
    }
)
Rendez_vous_Medecin_Patient_Ordonance: BinaryAssociation = BinaryAssociation(
    name="Rendez_vous_Medecin_Patient_Ordonance",
    ends={
        Property(name="rendez_vous_Medecin_Patient10", type=Rendez_vous_Medecin_Patient_external, multiplicity=Multiplicity(0, 1)),
        Property(name="ordonance11", type=Ordonance, multiplicity=Multiplicity(0, 1))
    }
)
Programme_Examen: BinaryAssociation = BinaryAssociation(
    name="Programme_Examen",
    ends={
        Property(name="programme12", type=Programme, multiplicity=Multiplicity(0, 1)),
        Property(name="examen13", type=Examen, multiplicity=Multiplicity(0, 1))
    }
)
Ordonance_Produit: BinaryAssociation = BinaryAssociation(
    name="Ordonance_Produit",
    ends={
        Property(name="ordonance14", type=Ordonance, multiplicity=Multiplicity(0, 1)),
        Property(name="produit15", type=Produit, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_KEC1EHt5EeqeQcxm9hmzHw",
    types={Patient, Examen, Medecin, Service, Programme, CentreHospitalier, ResultatExamen, Laboratoire, Personne, Contact, Rendez_vous, Ordonance, Produit, Rendez_vous_Laboratoire_Patient_external, Rendez_vous_Medecin_Patient_external},
    associations={Medecin_Service, Service_CentreHospitalier, Personne_Contact, Rendez_vous_Laboratoire_Patient_Examen, Examen_ResultatExamen, Rendez_vous_Medecin_Patient_Ordonance, Programme_Examen, Ordonance_Produit},
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