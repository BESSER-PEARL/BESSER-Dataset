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
Mitarbeiterprovision_einsehen_UseCase = Class(name="Mitarbeiterprovision_einsehen_UseCase")
Gesch_ftsf_hrer_Actor1 = Class(name="Gesch_ftsf_hrer_Actor1")
Lagerverwaltung_Component = Class(name="Lagerverwaltung_Component")
Verkaufte_Mobilfunkger_te_einsehen_UseCase = Class(name="Verkaufte_Mobilfunkger_te_einsehen_UseCase")
Systemverwaltung_Component = Class(name="Systemverwaltung_Component")
Benutzer_anlegen_und_verwalten_UseCase = Class(name="Benutzer_anlegen_und_verwalten_UseCase")
Benutzer_deaktivieren_UseCase = Class(name="Benutzer_deaktivieren_UseCase")
Benutzer_authentifizieren_und_autorisieren_UseCase = Class(name="Benutzer_authentifizieren_und_autorisieren_UseCase")
Benutzername_und_Passwort_eingeben_UseCase = Class(name="Benutzername_und_Passwort_eingeben_UseCase")
Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase = Class(name="Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Gesch_ftsf_hrer_Actor2 = Class(name="Gesch_ftsf_hrer_Actor2")
Administrator_Actor1 = Class(name="Administrator_Actor1")
Component_Component = Class(name="Component_Component")
Anwendungssystem_Component = Class(name="Anwendungssystem_Component")
Systemverwaltung_Component1 = Class(name="Systemverwaltung_Component1")
Benutzer_anlegen_und_verwalten_UseCase1 = Class(name="Benutzer_anlegen_und_verwalten_UseCase1")
Benutzer_deaktivieren_UseCase1 = Class(name="Benutzer_deaktivieren_UseCase1")
Benutzer_authentifizieren_und_autorisieren_UseCase1 = Class(name="Benutzer_authentifizieren_und_autorisieren_UseCase1")
Benutzername_und_Passwort_eingeben_UseCase1 = Class(name="Benutzername_und_Passwort_eingeben_UseCase1")
Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase1 = Class(name="Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase1")
Provisionlisten_verwalten_Component1 = Class(name="Provisionlisten_verwalten_Component1")
Tarife_einsehen_UseCase1 = Class(name="Tarife_einsehen_UseCase1")
Mitarbeiterprovision_einsehen_UseCase1 = Class(name="Mitarbeiterprovision_einsehen_UseCase1")
Lagerverwaltung_Component1 = Class(name="Lagerverwaltung_Component1")
Verkaufte_Mobilfunkger_te_einsehen_UseCase1 = Class(name="Verkaufte_Mobilfunkger_te_einsehen_UseCase1")
Mobilfunkger_t_einbuchen_Component1 = Class(name="Mobilfunkger_t_einbuchen_Component1")
T1 = Class(name="T1")
Information_hinterlegen_UseCase1 = Class(name="Information_hinterlegen_UseCase1")
Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase1 = Class(name="Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase1")
Hinweis_anzeigen__falsche_EAN_UseCase1 = Class(name="Hinweis_anzeigen__falsche_EAN_UseCase1")
Mobilfunkger_t_verkauft_Component1 = Class(name="Mobilfunkger_t_verkauft_Component1")
Mobilfunkger_t_ausbuchen_UseCase1 = Class(name="Mobilfunkger_t_ausbuchen_UseCase1")
Verkaufspreis_eintragen_UseCase1 = Class(name="Verkaufspreis_eintragen_UseCase1")
Verkaufstyp_ausw_hlen_UseCase1 = Class(name="Verkaufstyp_ausw_hlen_UseCase1")
Tarif_hintelegen_UseCase1 = Class(name="Tarif_hintelegen_UseCase1")
Mitarbeiterprovision_hinterlegen_UseCase1 = Class(name="Mitarbeiterprovision_hinterlegen_UseCase1")
Mobilfunkger_t_freigeben_UseCase2 = Class(name="Mobilfunkger_t_freigeben_UseCase2")
Mobilfunkger_t_reservieren_UseCase2 = Class(name="Mobilfunkger_t_reservieren_UseCase2")
Mobilfunkger_t = Class(name="Mobilfunkger_t")
Lager = Class(name="Lager")
Mitarbeiter = Class(name="Mitarbeiter")
Tarif = Class(name="Tarif")
Gesch_ftsf_herer = Class(name="Gesch_ftsf_herer")
vef_gbare_Ger_te = Class(name="vef_gbare_Ger_te")
verkaufte_Ger_te = Class(name="verkaufte_Ger_te")
Class_ = Class(name="Class")
Gesch_ftsf_hrer_Actor = Class(name="Gesch_ftsf_hrer_Actor")
Mitarbeiter_Actor = Class(name="Mitarbeiter_Actor")
Mobilfunkger_t_einbuchen_Component = Class(name="Mobilfunkger_t_einbuchen_Component")
T = Class(name="T")
Information_hinterlegen_UseCase = Class(name="Information_hinterlegen_UseCase")
Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase = Class(name="Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase")
Hinweis_anzeigen__falsche_EAN_UseCase = Class(name="Hinweis_anzeigen__falsche_EAN_UseCase")
Lager_einsehen_UseCase = Class(name="Lager_einsehen_UseCase")
Lager_verwalten_Component = Class(name="Lager_verwalten_Component")
Lager_einsehen_UseCase1 = Class(name="Lager_einsehen_UseCase1")
Mobilfunkger_t_reservieren_UseCase = Class(name="Mobilfunkger_t_reservieren_UseCase")
Mobilfunkger_t_umbuchen_UseCase = Class(name="Mobilfunkger_t_umbuchen_UseCase")
Mobilfunkger_t_l_schen_UseCase = Class(name="Mobilfunkger_t_l_schen_UseCase")
Mobilfunkger_t_freigeben_UseCase = Class(name="Mobilfunkger_t_freigeben_UseCase")
Mobilfunkger_t_verkauft_Component = Class(name="Mobilfunkger_t_verkauft_Component")
Mobilfunkger_t_ausbuchen_UseCase = Class(name="Mobilfunkger_t_ausbuchen_UseCase")
Verkaufspreis_eintragen_UseCase = Class(name="Verkaufspreis_eintragen_UseCase")
Verkaufstyp_ausw_hlen_UseCase = Class(name="Verkaufstyp_ausw_hlen_UseCase")
Lager_einsehen_UseCase2 = Class(name="Lager_einsehen_UseCase2")
Tarif_hintelegen_UseCase = Class(name="Tarif_hintelegen_UseCase")
Mitarbeiterprovision_hinterlegen_UseCase = Class(name="Mitarbeiterprovision_hinterlegen_UseCase")
Mobilfunkger_t_freigeben_UseCase1 = Class(name="Mobilfunkger_t_freigeben_UseCase1")
Mobilfunkger_t_reservieren_UseCase1 = Class(name="Mobilfunkger_t_reservieren_UseCase1")
Provisionlisten_verwalten_Component = Class(name="Provisionlisten_verwalten_Component")
Tarife_einsehen_UseCase = Class(name="Tarife_einsehen_UseCase")
Mobilfunkger_t_einbuchen_external = Class(name="Mobilfunkger_t_einbuchen_external")
Mobilfunkger_t_l_schen_external = Class(name="Mobilfunkger_t_l_schen_external")
Lager_einsehen_und_verwalten_external = Class(name="Lager_einsehen_und_verwalten_external")
Tarif_anlegen_external = Class(name="Tarif_anlegen_external")
Mobilfunkger_t_umbuchen_external = Class(name="Mobilfunkger_t_umbuchen_external")

# Mitarbeiterprovision_einsehen_UseCase class attributes and methods

# Gesch_ftsf_hrer_Actor1 class attributes and methods

# Lagerverwaltung_Component class attributes and methods

# Verkaufte_Mobilfunkger_te_einsehen_UseCase class attributes and methods

# Systemverwaltung_Component class attributes and methods

# Benutzer_anlegen_und_verwalten_UseCase class attributes and methods

# Benutzer_deaktivieren_UseCase class attributes and methods

# Benutzer_authentifizieren_und_autorisieren_UseCase class attributes and methods

# Benutzername_und_Passwort_eingeben_UseCase class attributes and methods

# Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Gesch_ftsf_hrer_Actor2 class attributes and methods

# Administrator_Actor1 class attributes and methods

# Component_Component class attributes and methods

# Anwendungssystem_Component class attributes and methods

# Systemverwaltung_Component1 class attributes and methods

# Benutzer_anlegen_und_verwalten_UseCase1 class attributes and methods

# Benutzer_deaktivieren_UseCase1 class attributes and methods

# Benutzer_authentifizieren_und_autorisieren_UseCase1 class attributes and methods

# Benutzername_und_Passwort_eingeben_UseCase1 class attributes and methods

# Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase1 class attributes and methods

# Provisionlisten_verwalten_Component1 class attributes and methods

# Tarife_einsehen_UseCase1 class attributes and methods

# Mitarbeiterprovision_einsehen_UseCase1 class attributes and methods

# Lagerverwaltung_Component1 class attributes and methods

# Verkaufte_Mobilfunkger_te_einsehen_UseCase1 class attributes and methods

# Mobilfunkger_t_einbuchen_Component1 class attributes and methods

# T1 class attributes and methods

# Information_hinterlegen_UseCase1 class attributes and methods

# Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase1 class attributes and methods

# Hinweis_anzeigen__falsche_EAN_UseCase1 class attributes and methods

# Mobilfunkger_t_verkauft_Component1 class attributes and methods

# Mobilfunkger_t_ausbuchen_UseCase1 class attributes and methods

# Verkaufspreis_eintragen_UseCase1 class attributes and methods

# Verkaufstyp_ausw_hlen_UseCase1 class attributes and methods

# Tarif_hintelegen_UseCase1 class attributes and methods

# Mitarbeiterprovision_hinterlegen_UseCase1 class attributes and methods

# Mobilfunkger_t_freigeben_UseCase2 class attributes and methods

# Mobilfunkger_t_reservieren_UseCase2 class attributes and methods

# Mobilfunkger_t class attributes and methods

# Lager class attributes and methods

# Mitarbeiter class attributes and methods

# Tarif class attributes and methods

# Gesch_ftsf_herer class attributes and methods

# vef_gbare_Ger_te class attributes and methods

# verkaufte_Ger_te class attributes and methods

# Class class attributes and methods

# Gesch_ftsf_hrer_Actor class attributes and methods

# Mitarbeiter_Actor class attributes and methods

# Mobilfunkger_t_einbuchen_Component class attributes and methods

# T class attributes and methods

# Information_hinterlegen_UseCase class attributes and methods

# Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase class attributes and methods

# Hinweis_anzeigen__falsche_EAN_UseCase class attributes and methods

# Lager_einsehen_UseCase class attributes and methods

# Lager_verwalten_Component class attributes and methods

# Lager_einsehen_UseCase1 class attributes and methods

# Mobilfunkger_t_reservieren_UseCase class attributes and methods

# Mobilfunkger_t_umbuchen_UseCase class attributes and methods

# Mobilfunkger_t_l_schen_UseCase class attributes and methods

# Mobilfunkger_t_freigeben_UseCase class attributes and methods

# Mobilfunkger_t_verkauft_Component class attributes and methods

# Mobilfunkger_t_ausbuchen_UseCase class attributes and methods

# Verkaufspreis_eintragen_UseCase class attributes and methods

# Verkaufstyp_ausw_hlen_UseCase class attributes and methods

# Lager_einsehen_UseCase2 class attributes and methods

# Tarif_hintelegen_UseCase class attributes and methods

# Mitarbeiterprovision_hinterlegen_UseCase class attributes and methods

# Mobilfunkger_t_freigeben_UseCase1 class attributes and methods

# Mobilfunkger_t_reservieren_UseCase1 class attributes and methods

# Provisionlisten_verwalten_Component class attributes and methods

# Tarife_einsehen_UseCase class attributes and methods

# Mobilfunkger_t_einbuchen_external class attributes and methods

# Mobilfunkger_t_l_schen_external class attributes and methods

# Lager_einsehen_und_verwalten_external class attributes and methods

# Tarif_anlegen_external class attributes and methods

# Mobilfunkger_t_umbuchen_external class attributes and methods

# Relationships
Gesch_ftsf_hrer_Lager_einsehen: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Lager_einsehen",
    ends={
        Property(name="lager_einsehen8", type=Lager_einsehen_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer9", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Mobilfunkger_t_reservieren: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Mobilfunkger_t_reservieren",
    ends={
        Property(name="mobilfunkger_t_reservieren10", type=Mobilfunkger_t_reservieren_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer11", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Mobilfunkger_t_umbuchen: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Mobilfunkger_t_umbuchen",
    ends={
        Property(name="mobilfunkger_t_umbuchen12", type=Mobilfunkger_t_umbuchen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer13", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Mobilfunkger_t_einbuchen: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Mobilfunkger_t_einbuchen",
    ends={
        Property(name="mobilfunkger_t_einbuchen0", type=Mobilfunkger_t_einbuchen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer1", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Lager_einsehen_Mitarbeiter: BinaryAssociation = BinaryAssociation(
    name="Lager_einsehen_Mitarbeiter",
    ends={
        Property(name="mitarbeiter2", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="lager_einsehen3", type=Lager_einsehen_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Mobilfunkger_t_reservieren_Mitarbeiter: BinaryAssociation = BinaryAssociation(
    name="Mobilfunkger_t_reservieren_Mitarbeiter",
    ends={
        Property(name="mitarbeiter4", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mobilfunkger_t_reservieren5", type=Mobilfunkger_t_reservieren_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Mobilfunkger_t_umbuchen_Mitarbeiter: BinaryAssociation = BinaryAssociation(
    name="Mobilfunkger_t_umbuchen_Mitarbeiter",
    ends={
        Property(name="mitarbeiter6", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mobilfunkger_t_umbuchen7", type=Mobilfunkger_t_umbuchen_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Benutzer_anlegen_und_verwalten2: BinaryAssociation = BinaryAssociation(
    name="Administrator_Benutzer_anlegen_und_verwalten2",
    ends={
        Property(name="administrator47", type=Administrator_Actor1, multiplicity=Multiplicity(0, 1)),
        Property(name="benutzer_anlegen_und_verwalten46", type=_external_unnamed_46, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Benutzer_deaktivieren2: BinaryAssociation = BinaryAssociation(
    name="Administrator_Benutzer_deaktivieren2",
    ends={
        Property(name="benutzer_deaktivieren48", type=_external_unnamed_48, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator49", type=Administrator_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Benutzer_deaktivieren_Administrator: BinaryAssociation = BinaryAssociation(
    name="Benutzer_deaktivieren_Administrator",
    ends={
        Property(name="administrator50", type=Administrator_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="benutzer_deaktivieren51", type=Benutzer_deaktivieren_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Mobilfunkger_t_l_schen_Gesch_ftsf_hrer: BinaryAssociation = BinaryAssociation(
    name="Mobilfunkger_t_l_schen_Gesch_ftsf_hrer",
    ends={
        Property(name="gesch_ftsf_hrer52", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mobilfunkger_t_l_schen53", type=Mobilfunkger_t_l_schen_external, multiplicity=Multiplicity(0, 1))
    }
)
Lager_einsehen_und_verwalten_Mitarbeiter: BinaryAssociation = BinaryAssociation(
    name="Lager_einsehen_und_verwalten_Mitarbeiter",
    ends={
        Property(name="mitarbeiter54", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="lager_einsehen_und_verwalten55", type=Lager_einsehen_und_verwalten_external, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Benutzer_authentifizieren_und_autorisieren: BinaryAssociation = BinaryAssociation(
    name="Administrator_Benutzer_authentifizieren_und_autorisieren",
    ends={
        Property(name="benutzer_authentifizieren_und_autorisieren56", type=Benutzer_authentifizieren_und_autorisieren_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator57", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Benutzer_anlegen_und_verwalten3: BinaryAssociation = BinaryAssociation(
    name="Administrator_Benutzer_anlegen_und_verwalten3",
    ends={
        Property(name="benutzer_anlegen_und_verwalten58", type=Benutzer_anlegen_und_verwalten_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator59", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Mobilfunkvertrag_freigeben: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Mobilfunkvertrag_freigeben",
    ends={
        Property(name="mobilfunkvertrag_freigeben14", type=Mobilfunkger_t_freigeben_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer15", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Mobilfunkger_t_l_schen: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Mobilfunkger_t_l_schen",
    ends={
        Property(name="mobilfunkger_t_l_schen16", type=Mobilfunkger_t_l_schen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer17", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Tarif_anlegen: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Tarif_anlegen",
    ends={
        Property(name="tarif_anlegen18", type=Tarif_anlegen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer19", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Benutzer_authentifizieren_und_autorisieren_Gesch_ftsf_hrer: BinaryAssociation = BinaryAssociation(
    name="Benutzer_authentifizieren_und_autorisieren_Gesch_ftsf_hrer",
    ends={
        Property(name="gesch_ftsf_hrer20", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="benutzer_authentifizieren_und_autorisieren21", type=Benutzer_authentifizieren_und_autorisieren_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Benutzer_authentifizieren_und_autorisieren_Mitarbeiter: BinaryAssociation = BinaryAssociation(
    name="Benutzer_authentifizieren_und_autorisieren_Mitarbeiter",
    ends={
        Property(name="mitarbeiter22", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="benutzer_authentifizieren_und_autorisieren23", type=Benutzer_authentifizieren_und_autorisieren_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Tarife_einsehen: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Tarife_einsehen",
    ends={
        Property(name="tarife_einsehen24", type=Tarife_einsehen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer25", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mitarbeiter_Tarife_einsehen: BinaryAssociation = BinaryAssociation(
    name="Mitarbeiter_Tarife_einsehen",
    ends={
        Property(name="tarife_einsehen26", type=Tarife_einsehen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="mitarbeiter27", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Mitarbeiterprovision_einsehen: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Mitarbeiterprovision_einsehen",
    ends={
        Property(name="mitarbeiterprovision_einsehen28", type=Mitarbeiterprovision_einsehen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer29", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mitarbeiter_Mitarbeiterprovision_einsehen: BinaryAssociation = BinaryAssociation(
    name="Mitarbeiter_Mitarbeiterprovision_einsehen",
    ends={
        Property(name="mitarbeiterprovision_einsehen30", type=Mitarbeiterprovision_einsehen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="mitarbeiter31", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Benutzer_anlegen_und_verwalten: BinaryAssociation = BinaryAssociation(
    name="Administrator_Benutzer_anlegen_und_verwalten",
    ends={
        Property(name="benutzer_anlegen_und_verwalten32", type=Benutzer_anlegen_und_verwalten_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator33", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Benutzer_deaktivieren: BinaryAssociation = BinaryAssociation(
    name="Administrator_Benutzer_deaktivieren",
    ends={
        Property(name="benutzer_deaktivieren34", type=Benutzer_deaktivieren_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator35", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Verkaufte_Mobilfunkger_te_einsehen: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Verkaufte_Mobilfunkger_te_einsehen",
    ends={
        Property(name="verkaufte_Mobilfunkger_te_einsehen36", type=Verkaufte_Mobilfunkger_te_einsehen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer37", type=Gesch_ftsf_hrer_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Mitarbeiter_Mobilfunkger_t_ausbuchen: BinaryAssociation = BinaryAssociation(
    name="Mitarbeiter_Mobilfunkger_t_ausbuchen",
    ends={
        Property(name="mobilfunkger_t_ausbuchen38", type=Mobilfunkger_t_ausbuchen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="mitarbeiter39", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mitarbeiter_Lager_einsehen: BinaryAssociation = BinaryAssociation(
    name="Mitarbeiter_Lager_einsehen",
    ends={
        Property(name="lager_einsehen40", type=Lager_einsehen_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="mitarbeiter41", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mitarbeiter_Mobilfunkger_t_reservieren: BinaryAssociation = BinaryAssociation(
    name="Mitarbeiter_Mobilfunkger_t_reservieren",
    ends={
        Property(name="mobilfunkger_t_reservieren42", type=Mobilfunkger_t_reservieren_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="mitarbeiter43", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Mobilfunkger_t_freigeben: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Mobilfunkger_t_freigeben",
    ends={
        Property(name="mobilfunkger_t_freigeben44", type=Mobilfunkger_t_freigeben_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer45", type=Gesch_ftsf_hrer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Gesch_ftsf_hrer_Tarif_anlegen2: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_hrer_Tarif_anlegen2",
    ends={
        Property(name="tarif_anlegen60", type=Tarif_anlegen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="gesch_ftsf_hrer61", type=Gesch_ftsf_hrer_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
Mitarbeiter_Verkaufte_Mobilfunkger_te_einsehen: BinaryAssociation = BinaryAssociation(
    name="Mitarbeiter_Verkaufte_Mobilfunkger_te_einsehen",
    ends={
        Property(name="verkaufte_Mobilfunkger_te_einsehen62", type=Verkaufte_Mobilfunkger_te_einsehen_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="mitarbeiter63", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mitarbeiter_Mobilfunkger_t_umbuchen: BinaryAssociation = BinaryAssociation(
    name="Mitarbeiter_Mobilfunkger_t_umbuchen",
    ends={
        Property(name="mobilfunkger_t_umbuchen64", type=Mobilfunkger_t_umbuchen_external, multiplicity=Multiplicity(0, 1)),
        Property(name="mitarbeiter65", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mitarbeiter_Mitarbeiterprovision_einsehen2: BinaryAssociation = BinaryAssociation(
    name="Mitarbeiter_Mitarbeiterprovision_einsehen2",
    ends={
        Property(name="mitarbeiterprovision_einsehen66", type=Mitarbeiterprovision_einsehen_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="mitarbeiter67", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mitarbeiter_Tarife_einsehen2: BinaryAssociation = BinaryAssociation(
    name="Mitarbeiter_Tarife_einsehen2",
    ends={
        Property(name="tarife_einsehen68", type=Tarife_einsehen_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="mitarbeiter69", type=Mitarbeiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Lager_Mitarbeiter: BinaryAssociation = BinaryAssociation(
    name="Lager_Mitarbeiter",
    ends={
        Property(name="verwalten70", type=Mitarbeiter, multiplicity=Multiplicity(1, 9999)),
        Property(name="Lager_Mitarbeiter_171", type=Lager, multiplicity=Multiplicity(1, 1))
    }
)
Gesch_ftsf_herer_Tarif: BinaryAssociation = BinaryAssociation(
    name="Gesch_ftsf_herer_Tarif",
    ends={
        Property(name="tarif72", type=Tarif, multiplicity=Multiplicity(0, 9999)),
        Property(name="verwalten73", type=Gesch_ftsf_herer, multiplicity=Multiplicity(1, 1))
    }
)
Mobilfunkger_te_Tarif: BinaryAssociation = BinaryAssociation(
    name="Mobilfunkger_te_Tarif",
    ends={
        Property(name="tarif74", type=Tarif, multiplicity=Multiplicity(0, 1)),
        Property(name="mobilfunkger_te75", type=Mobilfunkger_t, multiplicity=Multiplicity(1, 1))
    }
)
Mobilfunkger_te_Mitarbeiter: BinaryAssociation = BinaryAssociation(
    name="Mobilfunkger_te_Mitarbeiter",
    ends={
        Property(name="buchen76", type=Mitarbeiter, multiplicity=Multiplicity(1, 1)),
        Property(name="mobilfunkger_te77", type=Mobilfunkger_t, multiplicity=Multiplicity(1, 1))
    }
)
Lager__vef_gbare_Ger_te_Mobilfunkger_te: BinaryAssociation = BinaryAssociation(
    name="Lager__vef_gbare_Ger_te_Mobilfunkger_te",
    ends={
        Property(name="mobilfunkger_te78", type=Mobilfunkger_t, multiplicity=Multiplicity(0, 9999)),
        Property(name="lager__vef_gbare_Ger_te79", type=vef_gbare_Ger_te, multiplicity=Multiplicity(1, 1))
    }
)
Lager_verkaufte_Ger_te_Mobilfunkger_te: BinaryAssociation = BinaryAssociation(
    name="Lager_verkaufte_Ger_te_Mobilfunkger_te",
    ends={
        Property(name="mobilfunkger_te80", type=Mobilfunkger_t, multiplicity=Multiplicity(0, 9999)),
        Property(name="lager_verkaufte_Ger_te81", type=verkaufte_Ger_te, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ec57c6cd_d448_4dad_8cf7_c8166682ece8",
    types={Mitarbeiterprovision_einsehen_UseCase, Gesch_ftsf_hrer_Actor1, Lagerverwaltung_Component, Verkaufte_Mobilfunkger_te_einsehen_UseCase, Systemverwaltung_Component, Benutzer_anlegen_und_verwalten_UseCase, Benutzer_deaktivieren_UseCase, Benutzer_authentifizieren_und_autorisieren_UseCase, Benutzername_und_Passwort_eingeben_UseCase, Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase, Administrator_Actor, Gesch_ftsf_hrer_Actor2, Administrator_Actor1, Component_Component, Anwendungssystem_Component, Systemverwaltung_Component1, Benutzer_anlegen_und_verwalten_UseCase1, Benutzer_deaktivieren_UseCase1, Benutzer_authentifizieren_und_autorisieren_UseCase1, Benutzername_und_Passwort_eingeben_UseCase1, Hinweis_anzeigen__Benutzername_oder_Passwort_falsch_UseCase1, Provisionlisten_verwalten_Component1, Tarife_einsehen_UseCase1, Mitarbeiterprovision_einsehen_UseCase1, Lagerverwaltung_Component1, Verkaufte_Mobilfunkger_te_einsehen_UseCase1, Mobilfunkger_t_einbuchen_Component1, T1, Information_hinterlegen_UseCase1, Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase1, Hinweis_anzeigen__falsche_EAN_UseCase1, Mobilfunkger_t_verkauft_Component1, Mobilfunkger_t_ausbuchen_UseCase1, Verkaufspreis_eintragen_UseCase1, Verkaufstyp_ausw_hlen_UseCase1, Tarif_hintelegen_UseCase1, Mitarbeiterprovision_hinterlegen_UseCase1, Mobilfunkger_t_freigeben_UseCase2, Mobilfunkger_t_reservieren_UseCase2, Mobilfunkger_t, Lager, Mitarbeiter, Tarif, Gesch_ftsf_herer, vef_gbare_Ger_te, verkaufte_Ger_te, Class_, Gesch_ftsf_hrer_Actor, Mitarbeiter_Actor, Mobilfunkger_t_einbuchen_Component, T, Information_hinterlegen_UseCase, Hinweis_anzeigen__falsche_oder_doppelte_IMEI_UseCase, Hinweis_anzeigen__falsche_EAN_UseCase, Lager_einsehen_UseCase, Lager_verwalten_Component, Lager_einsehen_UseCase1, Mobilfunkger_t_reservieren_UseCase, Mobilfunkger_t_umbuchen_UseCase, Mobilfunkger_t_l_schen_UseCase, Mobilfunkger_t_freigeben_UseCase, Mobilfunkger_t_verkauft_Component, Mobilfunkger_t_ausbuchen_UseCase, Verkaufspreis_eintragen_UseCase, Verkaufstyp_ausw_hlen_UseCase, Lager_einsehen_UseCase2, Tarif_hintelegen_UseCase, Mitarbeiterprovision_hinterlegen_UseCase, Mobilfunkger_t_freigeben_UseCase1, Mobilfunkger_t_reservieren_UseCase1, Provisionlisten_verwalten_Component, Tarife_einsehen_UseCase, Mobilfunkger_t_einbuchen_external, Mobilfunkger_t_l_schen_external, Lager_einsehen_und_verwalten_external, Tarif_anlegen_external, Mobilfunkger_t_umbuchen_external},
    associations={Gesch_ftsf_hrer_Lager_einsehen, Gesch_ftsf_hrer_Mobilfunkger_t_reservieren, Gesch_ftsf_hrer_Mobilfunkger_t_umbuchen, Gesch_ftsf_hrer_Mobilfunkger_t_einbuchen, Lager_einsehen_Mitarbeiter, Mobilfunkger_t_reservieren_Mitarbeiter, Mobilfunkger_t_umbuchen_Mitarbeiter, Administrator_Benutzer_anlegen_und_verwalten2, Administrator_Benutzer_deaktivieren2, Benutzer_deaktivieren_Administrator, Mobilfunkger_t_l_schen_Gesch_ftsf_hrer, Lager_einsehen_und_verwalten_Mitarbeiter, Administrator_Benutzer_authentifizieren_und_autorisieren, Administrator_Benutzer_anlegen_und_verwalten3, Gesch_ftsf_hrer_Mobilfunkvertrag_freigeben, Gesch_ftsf_hrer_Mobilfunkger_t_l_schen, Gesch_ftsf_hrer_Tarif_anlegen, Benutzer_authentifizieren_und_autorisieren_Gesch_ftsf_hrer, Benutzer_authentifizieren_und_autorisieren_Mitarbeiter, Gesch_ftsf_hrer_Tarife_einsehen, Mitarbeiter_Tarife_einsehen, Gesch_ftsf_hrer_Mitarbeiterprovision_einsehen, Mitarbeiter_Mitarbeiterprovision_einsehen, Administrator_Benutzer_anlegen_und_verwalten, Administrator_Benutzer_deaktivieren, Gesch_ftsf_hrer_Verkaufte_Mobilfunkger_te_einsehen, Mitarbeiter_Mobilfunkger_t_ausbuchen, Mitarbeiter_Lager_einsehen, Mitarbeiter_Mobilfunkger_t_reservieren, Gesch_ftsf_hrer_Mobilfunkger_t_freigeben, Gesch_ftsf_hrer_Tarif_anlegen2, Mitarbeiter_Verkaufte_Mobilfunkger_te_einsehen, Mitarbeiter_Mobilfunkger_t_umbuchen, Mitarbeiter_Mitarbeiterprovision_einsehen2, Mitarbeiter_Tarife_einsehen2, Lager_Mitarbeiter, Gesch_ftsf_herer_Tarif, Mobilfunkger_te_Tarif, Mobilfunkger_te_Mitarbeiter, Lager__vef_gbare_Ger_te_Mobilfunkger_te, Lager_verkaufte_Ger_te_Mobilfunkger_te},
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