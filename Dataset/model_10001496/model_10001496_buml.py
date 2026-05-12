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
Mitarbeiter_verwalten_external = Class(name="Mitarbeiter_verwalten_external")
Patienten_aufnehmen_entlassen_external = Class(name="Patienten_aufnehmen_entlassen_external")
Auswahl_der_Fahrkartenkategorie_external = Class(name="Auswahl_der_Fahrkartenkategorie_external")
Abbrechen_external = Class(name="Abbrechen_external")
Hilfe_rufen_external = Class(name="Hilfe_rufen_external")
Wartung_external = Class(name="Wartung_external")
Schwimmbad_Eintritt_Component = Class(name="Schwimmbad_Eintritt_Component")
Gast_Actor = Class(name="Gast_Actor")
Automat_Actor = Class(name="Automat_Actor")
Kino_besuch_Component = Class(name="Kino_besuch_Component")
Gast_Actor1 = Class(name="Gast_Actor1")
Krankenhaus_System_Component = Class(name="Krankenhaus_System_Component")
Herr_M_ller_Actor = Class(name="Herr_M_ller_Actor")
Herr_Maier_Actor = Class(name="Herr_Maier_Actor")
Fahrkarte_kaufen_Component = Class(name="Fahrkarte_kaufen_Component")
Wechselgeldbeh_lter_leeren_UseCase = Class(name="Wechselgeldbeh_lter_leeren_UseCase")
Kunde_Actor = Class(name="Kunde_Actor")
Automat_Actor1 = Class(name="Automat_Actor1")
Servicetechniker_Actor = Class(name="Servicetechniker_Actor")
Person = Class(name="Person")
_Interface = Class(name="_Interface")
Name_Interface = Class(name="Name_Interface")
Wohnadresse = Class(name="Wohnadresse")
Student = Class(name="Student")
Professor = Class(name="Professor")
_2_Stunden_Ticket_kaufen_external = Class(name="_2_Stunden_Ticket_kaufen_external")
Tagesticket_kaufen_external = Class(name="Tagesticket_kaufen_external")
Kinokarten_kaufen_external = Class(name="Kinokarten_kaufen_external")
angestellt_in_der_Verwaltung_external = Class(name="angestellt_in_der_Verwaltung_external")

# Mitarbeiter_verwalten_external class attributes and methods

# Patienten_aufnehmen_entlassen_external class attributes and methods

# Auswahl_der_Fahrkartenkategorie_external class attributes and methods

# Abbrechen_external class attributes and methods

# Hilfe_rufen_external class attributes and methods

# Wartung_external class attributes and methods

# Schwimmbad_Eintritt_Component class attributes and methods

# Gast_Actor class attributes and methods

# Automat_Actor class attributes and methods

# Kino_besuch_Component class attributes and methods

# Gast_Actor1 class attributes and methods

# Krankenhaus_System_Component class attributes and methods

# Herr_M_ller_Actor class attributes and methods

# Herr_Maier_Actor class attributes and methods

# Fahrkarte_kaufen_Component class attributes and methods

# Wechselgeldbeh_lter_leeren_UseCase class attributes and methods

# Kunde_Actor class attributes and methods

# Automat_Actor1 class attributes and methods

# Servicetechniker_Actor class attributes and methods

# Person class attributes and methods
Person_Name: Property = Property(name="Name", type=StringType)
Person_Name1: Property = Property(name="Name1", type=StringType)
Person_Telefonnummer: Property = Property(name="Telefonnummer", type=IntegerType)
Person_E_mail: Property = Property(name="E_mail", type=StringType)
Person.attributes={Person_Name, Person_Telefonnummer, Person_Name1, Person_E_mail}

# _Interface class attributes and methods

# Name_Interface class attributes and methods

# Wohnadresse class attributes and methods
Wohnadresse_Strasse: Property = Property(name="Strasse", type=StringType)
Wohnadresse_Stadt: Property = Property(name="Stadt", type=StringType)
Wohnadresse_PLZ: Property = Property(name="PLZ", type=IntegerType)
Wohnadresse_Land: Property = Property(name="Land", type=StringType)
Wohnadresse.attributes={Wohnadresse_Stadt, Wohnadresse_Land, Wohnadresse_Strasse, Wohnadresse_PLZ}

# Student class attributes and methods
Student_Martikelnummer: Property = Property(name="Martikelnummer", type=IntegerType)
Student_Durchschnittsnote: Property = Property(name="Durchschnittsnote", type=IntegerType)
Student.attributes={Student_Martikelnummer, Student_Durchschnittsnote}

# Professor class attributes and methods
Professor_Lohn: Property = Property(name="Lohn", type=IntegerType)
Professor_attribute2: Property = Property(name="attribute2", type=StringType)
Professor.attributes={Professor_Lohn, Professor_attribute2}

# _2_Stunden_Ticket_kaufen_external class attributes and methods

# Tagesticket_kaufen_external class attributes and methods

# Kinokarten_kaufen_external class attributes and methods

# angestellt_in_der_Verwaltung_external class attributes and methods

# Relationships
Herr_M_ller_angestellt_in_der_Verwaltung: BinaryAssociation = BinaryAssociation(
    name="Herr_M_ller_angestellt_in_der_Verwaltung",
    ends={
        Property(name="herr_M_ller13", type=Herr_M_ller_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="angestellt_in_der_Verwaltung12", type=angestellt_in_der_Verwaltung_external, multiplicity=Multiplicity(0, 1))
    }
)
Herr_M_ller_Mitarbeiter_verwalten: BinaryAssociation = BinaryAssociation(
    name="Herr_M_ller_Mitarbeiter_verwalten",
    ends={
        Property(name="mitarbeiter_verwalten14", type=Mitarbeiter_verwalten_external, multiplicity=Multiplicity(0, 1)),
        Property(name="herr_M_ller15", type=Herr_M_ller_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Herr_Maier_Patienten_aufnehmen_entlassen: BinaryAssociation = BinaryAssociation(
    name="Herr_Maier_Patienten_aufnehmen_entlassen",
    ends={
        Property(name="patienten_aufnehmen_entlassen16", type=Patienten_aufnehmen_entlassen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="herr_Maier17", type=Herr_Maier_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Herr_M_ller_Patienten_aufnehmen_entlassen: BinaryAssociation = BinaryAssociation(
    name="Herr_M_ller_Patienten_aufnehmen_entlassen",
    ends={
        Property(name="patienten_aufnehmen_entlassen18", type=Patienten_aufnehmen_entlassen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="herr_M_ller19", type=Herr_M_ller_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Kunde_Auswahl_der_Fahrkartenkategorie: BinaryAssociation = BinaryAssociation(
    name="Kunde_Auswahl_der_Fahrkartenkategorie",
    ends={
        Property(name="auswahl_der_Fahrkartenkategorie20", type=Auswahl_der_Fahrkartenkategorie_external, multiplicity=Multiplicity(0, 1)),
        Property(name="kunde21", type=Kunde_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Automat_Abbruchtaste_wird_gedr_ckt: BinaryAssociation = BinaryAssociation(
    name="Automat_Abbruchtaste_wird_gedr_ckt",
    ends={
        Property(name="abbruchtaste_wird_gedr_ckt22", type=Abbrechen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="automat23", type=Automat_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Kunde_Hilfe_rufen: BinaryAssociation = BinaryAssociation(
    name="Kunde_Hilfe_rufen",
    ends={
        Property(name="hilfe_rufen24", type=Hilfe_rufen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="kunde25", type=Kunde_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Servicetechniker_Wartung: BinaryAssociation = BinaryAssociation(
    name="Servicetechniker_Wartung",
    ends={
        Property(name="wartung26", type=Wartung_external, multiplicity=Multiplicity(0, 1)),
        Property(name="servicetechniker27", type=Servicetechniker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Servicetechniker_Hilfe_rufen: BinaryAssociation = BinaryAssociation(
    name="Servicetechniker_Hilfe_rufen",
    ends={
        Property(name="hilfe_rufen28", type=Hilfe_rufen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="servicetechniker29", type=Servicetechniker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Servicetechniker_Auswahl_der_Fahrkartenkategorie: BinaryAssociation = BinaryAssociation(
    name="Servicetechniker_Auswahl_der_Fahrkartenkategorie",
    ends={
        Property(name="auswahl_der_Fahrkartenkategorie30", type=Auswahl_der_Fahrkartenkategorie_external, multiplicity=Multiplicity(0, 1)),
        Property(name="servicetechniker31", type=Servicetechniker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Servicetechniker_Kunde: BinaryAssociation = BinaryAssociation(
    name="Servicetechniker_Kunde",
    ends={
        Property(name="kunde32", type=Kunde_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="servicetechniker33", type=Servicetechniker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Wohnadresse_Person: BinaryAssociation = BinaryAssociation(
    name="Wohnadresse_Person",
    ends={
        Property(name="person34", type=Person, multiplicity=Multiplicity(0, 1)),
        Property(name="wohnadresse35", type=Wohnadresse, multiplicity=Multiplicity(0, 1))
    }
)
Gast_2_Stunden_Ticket_kaufen: BinaryAssociation = BinaryAssociation(
    name="Gast_2_Stunden_Ticket_kaufen",
    ends={
        Property(name="_2_Stunden_Ticket_kaufen0", type=_2_Stunden_Ticket_kaufen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="gast1", type=Gast_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Automat_2_Stunden_Ticket_kaufen: BinaryAssociation = BinaryAssociation(
    name="Automat_2_Stunden_Ticket_kaufen",
    ends={
        Property(name="_2_Stunden_Ticket_kaufen2", type=_2_Stunden_Ticket_kaufen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="automat3", type=Automat_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gast_Tagesticket_kaufen: BinaryAssociation = BinaryAssociation(
    name="Gast_Tagesticket_kaufen",
    ends={
        Property(name="tagesticket_kaufen4", type=Tagesticket_kaufen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="gast5", type=Gast_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Automat_Tagesticket_kaufen: BinaryAssociation = BinaryAssociation(
    name="Automat_Tagesticket_kaufen",
    ends={
        Property(name="tagesticket_kaufen6", type=Tagesticket_kaufen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="automat7", type=Automat_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gast_Kinokarten_kaufen: BinaryAssociation = BinaryAssociation(
    name="Gast_Kinokarten_kaufen",
    ends={
        Property(name="kinokarten_kaufen8", type=Kinokarten_kaufen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="gast9", type=Gast_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Herr_Maier_angestellt_in_der_Verwaltung: BinaryAssociation = BinaryAssociation(
    name="Herr_Maier_angestellt_in_der_Verwaltung",
    ends={
        Property(name="angestellt_in_der_Verwaltung10", type=angestellt_in_der_Verwaltung_external, multiplicity=Multiplicity(0, 1)),
        Property(name="herr_Maier11", type=Herr_Maier_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Atc00HfNEemeYMb8Sxp8Zg",
    types={Mitarbeiter_verwalten_external, Patienten_aufnehmen_entlassen_external, Auswahl_der_Fahrkartenkategorie_external, Abbrechen_external, Hilfe_rufen_external, Wartung_external, Schwimmbad_Eintritt_Component, Gast_Actor, Automat_Actor, Kino_besuch_Component, Gast_Actor1, Krankenhaus_System_Component, Herr_M_ller_Actor, Herr_Maier_Actor, Fahrkarte_kaufen_Component, Wechselgeldbeh_lter_leeren_UseCase, Kunde_Actor, Automat_Actor1, Servicetechniker_Actor, Person, _Interface, Name_Interface, Wohnadresse, Student, Professor, _2_Stunden_Ticket_kaufen_external, Tagesticket_kaufen_external, Kinokarten_kaufen_external, angestellt_in_der_Verwaltung_external},
    associations={Herr_M_ller_angestellt_in_der_Verwaltung, Herr_M_ller_Mitarbeiter_verwalten, Herr_Maier_Patienten_aufnehmen_entlassen, Herr_M_ller_Patienten_aufnehmen_entlassen, Kunde_Auswahl_der_Fahrkartenkategorie, Automat_Abbruchtaste_wird_gedr_ckt, Kunde_Hilfe_rufen, Servicetechniker_Wartung, Servicetechniker_Hilfe_rufen, Servicetechniker_Auswahl_der_Fahrkartenkategorie, Servicetechniker_Kunde, Wohnadresse_Person, Gast_2_Stunden_Ticket_kaufen, Automat_2_Stunden_Ticket_kaufen, Gast_Tagesticket_kaufen, Automat_Tagesticket_kaufen, Gast_Kinokarten_kaufen, Herr_Maier_angestellt_in_der_Verwaltung},
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