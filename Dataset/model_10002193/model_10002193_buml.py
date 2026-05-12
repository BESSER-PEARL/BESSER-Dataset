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
Bibliothek_Component = Class(name="Bibliothek_Component")
Selbstbedienungsterminal_Actor = Class(name="Selbstbedienungsterminal_Actor")
Kunde_Actor1 = Class(name="Kunde_Actor1")
Lieferant_Actor = Class(name="Lieferant_Actor")
Adresse = Class(name="Adresse")
Geld_abheben_external = Class(name="Geld_abheben_external")
ausstehende_Mahnung_versenden_external = Class(name="ausstehende_Mahnung_versenden_external")
Kunde_Actor = Class(name="Kunde_Actor")
Terminal_Actor = Class(name="Terminal_Actor")
Banksystem_Component = Class(name="Banksystem_Component")
Verwaltung_Actor = Class(name="Verwaltung_Actor")
Bibliothekar_Actor = Class(name="Bibliothekar_Actor")
Leser_Actor = Class(name="Leser_Actor")
Medienr_ckgabe_external = Class(name="Medienr_ckgabe_external")
Medien_ausleihen_external = Class(name="Medien_ausleihen_external")
Buch_suchen_external = Class(name="Buch_suchen_external")
Adresse__ndern_external = Class(name="Adresse__ndern_external")

# Bibliothek_Component class attributes and methods

# Selbstbedienungsterminal_Actor class attributes and methods

# Kunde_Actor1 class attributes and methods

# Lieferant_Actor class attributes and methods

# Adresse class attributes and methods

# Geld_abheben_external class attributes and methods

# ausstehende_Mahnung_versenden_external class attributes and methods

# Kunde_Actor class attributes and methods

# Terminal_Actor class attributes and methods

# Banksystem_Component class attributes and methods

# Verwaltung_Actor class attributes and methods

# Bibliothekar_Actor class attributes and methods

# Leser_Actor class attributes and methods

# Medienr_ckgabe_external class attributes and methods

# Medien_ausleihen_external class attributes and methods

# Buch_suchen_external class attributes and methods

# Adresse__ndern_external class attributes and methods

# Relationships
Kunde_Geld_abheben: BinaryAssociation = BinaryAssociation(
    name="Kunde_Geld_abheben",
    ends={
        Property(name="geld_abheben0", type=Geld_abheben_external, multiplicity=Multiplicity(0, 1)),
        Property(name="kunde1", type=Kunde_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Terminal_Geld_abheben: BinaryAssociation = BinaryAssociation(
    name="Terminal_Geld_abheben",
    ends={
        Property(name="geld_abheben2", type=Geld_abheben_external, multiplicity=Multiplicity(0, 1)),
        Property(name="terminal3", type=Terminal_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Verwaltung_ausstehende_Mahnung_versenden: BinaryAssociation = BinaryAssociation(
    name="Verwaltung_ausstehende_Mahnung_versenden",
    ends={
        Property(name="ausstehende_Mahnung_versenden4", type=ausstehende_Mahnung_versenden_external, multiplicity=Multiplicity(0, 1)),
        Property(name="verwaltung5", type=Verwaltung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Bibliothekar_Medienr_ckgabe: BinaryAssociation = BinaryAssociation(
    name="Bibliothekar_Medienr_ckgabe",
    ends={
        Property(name="medienr_ckgabe6", type=Medienr_ckgabe_external, multiplicity=Multiplicity(0, 1)),
        Property(name="bibliothekar7", type=Bibliothekar_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Bibliothekar_Medien_ausleihen: BinaryAssociation = BinaryAssociation(
    name="Bibliothekar_Medien_ausleihen",
    ends={
        Property(name="medien_ausleihen8", type=Medien_ausleihen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="bibliothekar9", type=Bibliothekar_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Leser_Medienr_ckgabe: BinaryAssociation = BinaryAssociation(
    name="Leser_Medienr_ckgabe",
    ends={
        Property(name="medienr_ckgabe10", type=Medienr_ckgabe_external, multiplicity=Multiplicity(0, 1)),
        Property(name="leser11", type=Leser_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Leser_Medien_ausleihen: BinaryAssociation = BinaryAssociation(
    name="Leser_Medien_ausleihen",
    ends={
        Property(name="medien_ausleihen12", type=Medien_ausleihen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="leser13", type=Leser_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Leser_Buch_suchen: BinaryAssociation = BinaryAssociation(
    name="Leser_Buch_suchen",
    ends={
        Property(name="buch_suchen14", type=Buch_suchen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="leser15", type=Leser_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Leser_Adresse__ndern: BinaryAssociation = BinaryAssociation(
    name="Leser_Adresse__ndern",
    ends={
        Property(name="adresse__ndern16", type=Adresse__ndern_external, multiplicity=Multiplicity(0, 1)),
        Property(name="leser17", type=Leser_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Selbstbedienungsterminal_Adresse__ndern: BinaryAssociation = BinaryAssociation(
    name="Selbstbedienungsterminal_Adresse__ndern",
    ends={
        Property(name="adresse__ndern18", type=Adresse__ndern_external, multiplicity=Multiplicity(0, 1)),
        Property(name="selbstbedienungsterminal19", type=Selbstbedienungsterminal_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Selbstbedienungsterminal_Buch_suchen: BinaryAssociation = BinaryAssociation(
    name="Selbstbedienungsterminal_Buch_suchen",
    ends={
        Property(name="buch_suchen20", type=Buch_suchen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="selbstbedienungsterminal21", type=Selbstbedienungsterminal_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_vQ6uMENjEemwEfmno6HCkg",
    types={Bibliothek_Component, Selbstbedienungsterminal_Actor, Kunde_Actor1, Lieferant_Actor, Adresse, Geld_abheben_external, ausstehende_Mahnung_versenden_external, Kunde_Actor, Terminal_Actor, Banksystem_Component, Verwaltung_Actor, Bibliothekar_Actor, Leser_Actor, Medienr_ckgabe_external, Medien_ausleihen_external, Buch_suchen_external, Adresse__ndern_external},
    associations={Kunde_Geld_abheben, Terminal_Geld_abheben, Verwaltung_ausstehende_Mahnung_versenden, Bibliothekar_Medienr_ckgabe, Bibliothekar_Medien_ausleihen, Leser_Medienr_ckgabe, Leser_Medien_ausleihen, Leser_Buch_suchen, Leser_Adresse__ndern, Selbstbedienungsterminal_Adresse__ndern, Selbstbedienungsterminal_Buch_suchen},
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