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
Personne = Class(name="Personne", is_abstract=True)
Employe = Class(name="Employe", is_abstract=True)
EmployeAdministratif = Class(name="EmployeAdministratif")
Medecin = Class(name="Medecin")
RDV = Class(name="RDV")
AgendaPartage = Class(name="AgendaPartage")
Agenda = Class(name="Agenda")
Patient = Class(name="Patient")
Compte = Class(name="Compte")
Test = Class(name="Test")

# Personne class attributes and methods
Personne_nom: Property = Property(name="nom", type=StringType)
Personne_prenom: Property = Property(name="prenom", type=StringType)
Personne_adresse: Property = Property(name="adresse", type=StringType)
Personne_email: Property = Property(name="email", type=StringType)
Personne_telPrive: Property = Property(name="telPrive", type=StringType)
Personne_dateNaissance: Property = Property(name="dateNaissance", type=StringType)
Personne.attributes={Personne_telPrive, Personne_nom, Personne_prenom, Personne_adresse, Personne_email, Personne_dateNaissance}

# Employe class attributes and methods
Employe_salaire: Property = Property(name="salaire", type=IntegerType)
Employe_dateDebut: Property = Property(name="dateDebut", type=StringType)
Employe_dateFin: Property = Property(name="dateFin", type=StringType)
Employe_joursVacance: Property = Property(name="joursVacance", type=IntegerType)
Employe.attributes={Employe_joursVacance, Employe_dateDebut, Employe_salaire, Employe_dateFin}

# EmployeAdministratif class attributes and methods
EmployeAdministratif_formation: Property = Property(name="formation", type=StringType)
EmployeAdministratif.attributes={EmployeAdministratif_formation}

# Medecin class attributes and methods
Medecin_specialisation: Property = Property(name="specialisation", type=StringType)
Medecin.attributes={Medecin_specialisation}

# RDV class attributes and methods
RDV_date: Property = Property(name="date", type=StringType)
RDV_heure: Property = Property(name="heure", type=StringType)
RDV_duree: Property = Property(name="duree", type=IntegerType)
RDV.attributes={RDV_duree, RDV_date, RDV_heure}

# AgendaPartage class attributes and methods

# Agenda class attributes and methods
Agenda_annee: Property = Property(name="annee", type=StringType)
Agenda.attributes={Agenda_annee}

# Patient class attributes and methods
Patient_antecedent: Property = Property(name="antecedent", type=StringType)
Patient_traitement: Property = Property(name="traitement", type=StringType)
Patient_allergies: Property = Property(name="allergies", type=StringType)
Patient.attributes={Patient_antecedent, Patient_traitement, Patient_allergies}

# Compte class attributes and methods
Compte_login: Property = Property(name="login", type=StringType)
Compte_password: Property = Property(name="password", type=StringType)
Compte_typeCompte: Property = Property(name="typeCompte", type=StringType)
Compte.attributes={Compte_typeCompte, Compte_login, Compte_password}

# Test class attributes and methods
Test_Prenom: Property = Property(name="Prenom", type=StringType)
Test.attributes={Test_Prenom}

# Relationships
Agenda_RDV: BinaryAssociation = BinaryAssociation(
    name="Agenda_RDV",
    ends={
        Property(name="rDV0", type=RDV, multiplicity=Multiplicity(0, 9999)),
        Property(name="agenda1", type=Agenda, multiplicity=Multiplicity(1, 1))
    }
)
AgendaPartage_Agenda: BinaryAssociation = BinaryAssociation(
    name="AgendaPartage_Agenda",
    ends={
        Property(name="agenda2", type=Agenda, multiplicity=Multiplicity(1, 9999)),
        Property(name="agendaPartage3", type=AgendaPartage, multiplicity=Multiplicity(1, 1))
    }
)
Employe_Compte: BinaryAssociation = BinaryAssociation(
    name="Employe_Compte",
    ends={
        Property(name="compte4", type=Compte, multiplicity=Multiplicity(1, 2)),
        Property(name="employe5", type=Employe, multiplicity=Multiplicity(1, 1))
    }
)
Medecin_Agenda: BinaryAssociation = BinaryAssociation(
    name="Medecin_Agenda",
    ends={
        Property(name="agenda6", type=Agenda, multiplicity=Multiplicity(1, 1)),
        Property(name="medecin7", type=Medecin, multiplicity=Multiplicity(1, 1))
    }
)
EmployeAdministratif_AgendaPartage: BinaryAssociation = BinaryAssociation(
    name="EmployeAdministratif_AgendaPartage",
    ends={
        Property(name="agendaPartage8", type=AgendaPartage, multiplicity=Multiplicity(1, 1)),
        Property(name="employeAdministratif9", type=EmployeAdministratif, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_Compte: BinaryAssociation = BinaryAssociation(
    name="Patient_Compte",
    ends={
        Property(name="compte10", type=Compte, multiplicity=Multiplicity(0, 1)),
        Property(name="patient11", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
RDV_Patient: BinaryAssociation = BinaryAssociation(
    name="RDV_Patient",
    ends={
        Property(name="patient12", type=Patient, multiplicity=Multiplicity(1, 1)),
        Property(name="rDV13", type=RDV, multiplicity=Multiplicity(0, 9999))
    }
)
Medecin_Patient: BinaryAssociation = BinaryAssociation(
    name="Medecin_Patient",
    ends={
        Property(name="patient14", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="medecin15", type=Medecin, multiplicity=Multiplicity(1, 1))
    }
)
EmployeAdministratif_RDV: BinaryAssociation = BinaryAssociation(
    name="EmployeAdministratif_RDV",
    ends={
        Property(name="rDV16", type=RDV, multiplicity=Multiplicity(0, 9999)),
        Property(name="employeAdministratif17", type=EmployeAdministratif, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3maM4HxjEemZdOOrcag7Wg",
    types={Personne, Employe, EmployeAdministratif, Medecin, RDV, AgendaPartage, Agenda, Patient, Compte, Test},
    associations={Agenda_RDV, AgendaPartage_Agenda, Employe_Compte, Medecin_Agenda, EmployeAdministratif_AgendaPartage, Patient_Compte, RDV_Patient, Medecin_Patient, EmployeAdministratif_RDV},
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