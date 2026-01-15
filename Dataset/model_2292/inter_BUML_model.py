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
zlvp_Geschlecht = Class(name="zlvp::Geschlecht")
zlvp_Person = Class(name="zlvp::Person")
zlvp_Anrede = Class(name="zlvp::Anrede")
zlvp_Stab = Class(name="zlvp::Stab")
zlvp_Funktion = Class(name="zlvp::Funktion")
zlvp_Leiter = Class(name="zlvp::Leiter")
zlvp_Gruppen = Class(name="zlvp::Gruppen")
zlvp_Teilnehmer = Class(name="zlvp::Teilnehmer")
zlvp_Lager = Class(name="zlvp::Lager")
zlvp_Jahr = Class(name="zlvp::Jahr")
zlvp_Essen = Class(name="zlvp::Essen")
zlvp_Programm = Class(name="zlvp::Programm")
zlvp_Lagerort = Class(name="zlvp::Lagerort")
zlvp_Zelt = Class(name="zlvp::Zelt")
zlvp_ZeltDetail = Class(name="zlvp::ZeltDetail")
zlvp_Schaeden = Class(name="zlvp::Schaeden")
zlvp_Verleih = Class(name="zlvp::Verleih")
zlvp_ZeltDetailBezeichnung = Class(name="zlvp::ZeltDetailBezeichnung")
zlvp_Legenda = Class(name="zlvp::Legenda")
zlvp_LegendaTyp = Class(name="zlvp::LegendaTyp")

# zlvp_Geschlecht class attributes and methods
zlvp_Geschlecht_id: Property = Property(name="id", type=IntegerType)
zlvp_Geschlecht_name: Property = Property(name="name", type=StringType)
zlvp_Geschlecht.attributes={zlvp_Geschlecht_name, zlvp_Geschlecht_id}

# zlvp_Person class attributes and methods
zlvp_Person_id: Property = Property(name="id", type=IntegerType)
zlvp_Person_nachname: Property = Property(name="nachname", type=StringType)
zlvp_Person_vorname: Property = Property(name="vorname", type=StringType)
zlvp_Person_strasse: Property = Property(name="strasse", type=StringType)
zlvp_Person_plz: Property = Property(name="plz", type=StringType)
zlvp_Person_ort: Property = Property(name="ort", type=StringType)
zlvp_Person_telNr: Property = Property(name="telNr", type=StringType)
zlvp_Person_handyNr: Property = Property(name="handyNr", type=StringType)
zlvp_Person_email: Property = Property(name="email", type=StringType)
zlvp_Person_gebDat: Property = Property(name="gebDat", type=DateType)
zlvp_Person_notTelNr: Property = Property(name="notTelNr", type=StringType)
zlvp_Person_version: Property = Property(name="version", type=StringType)
zlvp_Person.attributes={zlvp_Person_version, zlvp_Person_id, zlvp_Person_email, zlvp_Person_strasse, zlvp_Person_ort, zlvp_Person_gebDat, zlvp_Person_nachname, zlvp_Person_plz, zlvp_Person_handyNr, zlvp_Person_vorname, zlvp_Person_notTelNr, zlvp_Person_telNr}

# zlvp_Anrede class attributes and methods
zlvp_Anrede_id: Property = Property(name="id", type=IntegerType)
zlvp_Anrede_name: Property = Property(name="name", type=StringType)
zlvp_Anrede.attributes={zlvp_Anrede_id, zlvp_Anrede_name}

# zlvp_Stab class attributes and methods
zlvp_Stab_id: Property = Property(name="id", type=IntegerType)
zlvp_Stab.attributes={zlvp_Stab_id}

# zlvp_Funktion class attributes and methods
zlvp_Funktion_id: Property = Property(name="id", type=IntegerType)
zlvp_Funktion_name: Property = Property(name="name", type=StringType)
zlvp_Funktion.attributes={zlvp_Funktion_id, zlvp_Funktion_name}

# zlvp_Leiter class attributes and methods
zlvp_Leiter_id: Property = Property(name="id", type=IntegerType)
zlvp_Leiter.attributes={zlvp_Leiter_id}

# zlvp_Gruppen class attributes and methods
zlvp_Gruppen_id: Property = Property(name="id", type=IntegerType)
zlvp_Gruppen_name: Property = Property(name="name", type=StringType)
zlvp_Gruppen_spruch: Property = Property(name="spruch", type=StringType)
zlvp_Gruppen.attributes={zlvp_Gruppen_name, zlvp_Gruppen_id, zlvp_Gruppen_spruch}

# zlvp_Teilnehmer class attributes and methods
zlvp_Teilnehmer_id: Property = Property(name="id", type=IntegerType)
zlvp_Teilnehmer.attributes={zlvp_Teilnehmer_id}

# zlvp_Lager class attributes and methods
zlvp_Lager_id: Property = Property(name="id", type=IntegerType)
zlvp_Lager_name: Property = Property(name="name", type=StringType)
zlvp_Lager_start: Property = Property(name="start", type=DateType)
zlvp_Lager_stop: Property = Property(name="stop", type=DateType)
zlvp_Lager_thema: Property = Property(name="thema", type=StringType)
zlvp_Lager_ort: Property = Property(name="ort", type=StringType)
zlvp_Lager.attributes={zlvp_Lager_ort, zlvp_Lager_stop, zlvp_Lager_thema, zlvp_Lager_id, zlvp_Lager_start, zlvp_Lager_name}

# zlvp_Jahr class attributes and methods
zlvp_Jahr_id: Property = Property(name="id", type=IntegerType)
zlvp_Jahr_name: Property = Property(name="name", type=StringType)
zlvp_Jahr.attributes={zlvp_Jahr_name, zlvp_Jahr_id}

# zlvp_Essen class attributes and methods
zlvp_Essen_vormittag: Property = Property(name="vormittag", type=StringType)
zlvp_Essen_nachmittag: Property = Property(name="nachmittag", type=StringType)
zlvp_Essen_nacht: Property = Property(name="nacht", type=StringType)
zlvp_Essen_id: Property = Property(name="id", type=IntegerType)
zlvp_Essen_datum: Property = Property(name="datum", type=DateType)
zlvp_Essen.attributes={zlvp_Essen_datum, zlvp_Essen_nachmittag, zlvp_Essen_nacht, zlvp_Essen_vormittag, zlvp_Essen_id}

# zlvp_Programm class attributes and methods
zlvp_Programm_id: Property = Property(name="id", type=IntegerType)
zlvp_Programm_datum: Property = Property(name="datum", type=DateType)
zlvp_Programm_vormittag: Property = Property(name="vormittag", type=StringType)
zlvp_Programm_nachmittag: Property = Property(name="nachmittag", type=StringType)
zlvp_Programm_nacht: Property = Property(name="nacht", type=StringType)
zlvp_Programm.attributes={zlvp_Programm_nachmittag, zlvp_Programm_datum, zlvp_Programm_nacht, zlvp_Programm_id, zlvp_Programm_vormittag}

# zlvp_Lagerort class attributes and methods
zlvp_Lagerort_id: Property = Property(name="id", type=IntegerType)
zlvp_Lagerort_name: Property = Property(name="name", type=StringType)
zlvp_Lagerort.attributes={zlvp_Lagerort_id, zlvp_Lagerort_name}

# zlvp_Zelt class attributes and methods
zlvp_Zelt_id: Property = Property(name="id", type=IntegerType)
zlvp_Zelt_name: Property = Property(name="name", type=StringType)
zlvp_Zelt.attributes={zlvp_Zelt_name, zlvp_Zelt_id}

# zlvp_ZeltDetail class attributes and methods
zlvp_ZeltDetail_id: Property = Property(name="id", type=IntegerType)
zlvp_ZeltDetail_name: Property = Property(name="name", type=StringType)
zlvp_ZeltDetail.attributes={zlvp_ZeltDetail_name, zlvp_ZeltDetail_id}

# zlvp_Schaeden class attributes and methods
zlvp_Schaeden_id: Property = Property(name="id", type=IntegerType)
zlvp_Schaeden_datum: Property = Property(name="datum", type=DateType)
zlvp_Schaeden_bezeichnung: Property = Property(name="bezeichnung", type=StringType)
zlvp_Schaeden.attributes={zlvp_Schaeden_id, zlvp_Schaeden_bezeichnung, zlvp_Schaeden_datum}

# zlvp_Verleih class attributes and methods
zlvp_Verleih_id: Property = Property(name="id", type=IntegerType)
zlvp_Verleih_datum: Property = Property(name="datum", type=DateType)
zlvp_Verleih_person: Property = Property(name="person", type=StringType)
zlvp_Verleih_bemerkung: Property = Property(name="bemerkung", type=StringType)
zlvp_Verleih.attributes={zlvp_Verleih_bemerkung, zlvp_Verleih_datum, zlvp_Verleih_person, zlvp_Verleih_id}

# zlvp_ZeltDetailBezeichnung class attributes and methods
zlvp_ZeltDetailBezeichnung_name: Property = Property(name="name", type=StringType)
zlvp_ZeltDetailBezeichnung_id: Property = Property(name="id", type=IntegerType)
zlvp_ZeltDetailBezeichnung.attributes={zlvp_ZeltDetailBezeichnung_name, zlvp_ZeltDetailBezeichnung_id}

# zlvp_Legenda class attributes and methods
zlvp_Legenda_id: Property = Property(name="id", type=IntegerType)
zlvp_Legenda_nachname: Property = Property(name="nachname", type=StringType)
zlvp_Legenda_vorname: Property = Property(name="vorname", type=StringType)
zlvp_Legenda_strasse: Property = Property(name="strasse", type=StringType)
zlvp_Legenda_plz: Property = Property(name="plz", type=StringType)
zlvp_Legenda_handyNr: Property = Property(name="handyNr", type=StringType)
zlvp_Legenda_faxNr: Property = Property(name="faxNr", type=StringType)
zlvp_Legenda_email: Property = Property(name="email", type=StringType)
zlvp_Legenda_firma: Property = Property(name="firma", type=StringType)
zlvp_Legenda_bemerkung: Property = Property(name="bemerkung", type=StringType)
zlvp_Legenda_ort: Property = Property(name="ort", type=StringType)
zlvp_Legenda_telNr: Property = Property(name="telNr", type=StringType)
zlvp_Legenda.attributes={zlvp_Legenda_handyNr, zlvp_Legenda_strasse, zlvp_Legenda_bemerkung, zlvp_Legenda_telNr, zlvp_Legenda_nachname, zlvp_Legenda_id, zlvp_Legenda_vorname, zlvp_Legenda_email, zlvp_Legenda_ort, zlvp_Legenda_faxNr, zlvp_Legenda_plz, zlvp_Legenda_firma}

# zlvp_LegendaTyp class attributes and methods
zlvp_LegendaTyp_name: Property = Property(name="name", type=StringType)
zlvp_LegendaTyp_id: Property = Property(name="id", type=IntegerType)
zlvp_LegendaTyp.attributes={zlvp_LegendaTyp_name, zlvp_LegendaTyp_id}

# Relationships
anrede1: BinaryAssociation = BinaryAssociation(
    name="anrede1",
    ends={
        Property(name="zlvp_Anrede", type=zlvp_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Person2", type=zlvp_Anrede, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
geschlecht0: BinaryAssociation = BinaryAssociation(
    name="geschlecht0",
    ends={
        Property(name="zlvp_Geschlecht", type=zlvp_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Person", type=zlvp_Geschlecht, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
person4: BinaryAssociation = BinaryAssociation(
    name="person4",
    ends={
        Property(name="zlvp_Person6", type=zlvp_Stab, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Stab5", type=zlvp_Person, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
funktion7: BinaryAssociation = BinaryAssociation(
    name="funktion7",
    ends={
        Property(name="zlvp_Funktion", type=zlvp_Stab, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Stab8", type=zlvp_Funktion, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
gruppen9: BinaryAssociation = BinaryAssociation(
    name="gruppen9",
    ends={
        Property(name="zlvp_Gruppen", type=zlvp_Leiter, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Leiter", type=zlvp_Gruppen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person10: BinaryAssociation = BinaryAssociation(
    name="person10",
    ends={
        Property(name="zlvp_Person12", type=zlvp_Leiter, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Leiter11", type=zlvp_Person, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lager3: BinaryAssociation = BinaryAssociation(
    name="lager3",
    ends={
        Property(name="zlvp_Lager", type=zlvp_Stab, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Stab", type=zlvp_Lager, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gruppen13: BinaryAssociation = BinaryAssociation(
    name="gruppen13",
    ends={
        Property(name="zlvp_Gruppen14", type=zlvp_Teilnehmer, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Teilnehmer", type=zlvp_Gruppen, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
person15: BinaryAssociation = BinaryAssociation(
    name="person15",
    ends={
        Property(name="zlvp_Person17", type=zlvp_Teilnehmer, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Teilnehmer16", type=zlvp_Person, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lager18: BinaryAssociation = BinaryAssociation(
    name="lager18",
    ends={
        Property(name="zlvp_Lager19", type=zlvp_Jahr, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Jahr", type=zlvp_Lager, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gruppen20: BinaryAssociation = BinaryAssociation(
    name="gruppen20",
    ends={
        Property(name="zlvp_Gruppen22", type=zlvp_Lager, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Lager21", type=zlvp_Gruppen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stab23: BinaryAssociation = BinaryAssociation(
    name="stab23",
    ends={
        Property(name="zlvp_Stab25", type=zlvp_Lager, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Lager24", type=zlvp_Stab, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
essen26: BinaryAssociation = BinaryAssociation(
    name="essen26",
    ends={
        Property(name="zlvp_Essen", type=zlvp_Lager, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Lager27", type=zlvp_Essen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programm28: BinaryAssociation = BinaryAssociation(
    name="programm28",
    ends={
        Property(name="zlvp_Programm", type=zlvp_Lager, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Lager29", type=zlvp_Programm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
materialwart32: BinaryAssociation = BinaryAssociation(
    name="materialwart32",
    ends={
        Property(name="zlvp_Person34", type=zlvp_Lager, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Lager33", type=zlvp_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lagerort35: BinaryAssociation = BinaryAssociation(
    name="lagerort35",
    ends={
        Property(name="zlvp_Lagerort", type=zlvp_Lager, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Lager36", type=zlvp_Lagerort, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leiter37: BinaryAssociation = BinaryAssociation(
    name="leiter37",
    ends={
        Property(name="zlvp_Leiter39", type=zlvp_Gruppen, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Gruppen38", type=zlvp_Leiter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
teilnehmer40: BinaryAssociation = BinaryAssociation(
    name="teilnehmer40",
    ends={
        Property(name="zlvp_Teilnehmer42", type=zlvp_Gruppen, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Gruppen41", type=zlvp_Teilnehmer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
zelt30: BinaryAssociation = BinaryAssociation(
    name="zelt30",
    ends={
        Property(name="zlvp_Zelt", type=zlvp_Lager, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Lager31", type=zlvp_Zelt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zeltDetail43: BinaryAssociation = BinaryAssociation(
    name="zeltDetail43",
    ends={
        Property(name="zlvp_ZeltDetail", type=zlvp_Zelt, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Zelt44", type=zlvp_ZeltDetail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schaeden45: BinaryAssociation = BinaryAssociation(
    name="schaeden45",
    ends={
        Property(name="zlvp_Schaeden", type=zlvp_Zelt, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Zelt46", type=zlvp_Schaeden, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
verleih47: BinaryAssociation = BinaryAssociation(
    name="verleih47",
    ends={
        Property(name="zlvp_Verleih", type=zlvp_Zelt, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Zelt48", type=zlvp_Verleih, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zeltDetailBezeichnung52: BinaryAssociation = BinaryAssociation(
    name="zeltDetailBezeichnung52",
    ends={
        Property(name="zlvp_ZeltDetailBezeichnung", type=zlvp_ZeltDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_ZeltDetail53", type=zlvp_ZeltDetailBezeichnung, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anrede54: BinaryAssociation = BinaryAssociation(
    name="anrede54",
    ends={
        Property(name="zlvp_Anrede55", type=zlvp_Legenda, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Legenda", type=zlvp_Anrede, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Lager49: BinaryAssociation = BinaryAssociation(
    name="Lager49",
    ends={
        Property(name="zlvp_Lager51", type=zlvp_Zelt, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Zelt50", type=zlvp_Lager, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
legendaTyp56: BinaryAssociation = BinaryAssociation(
    name="legendaTyp56",
    ends={
        Property(name="zlvp_LegendaTyp", type=zlvp_Legenda, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Legenda57", type=zlvp_LegendaTyp, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
legenda58: BinaryAssociation = BinaryAssociation(
    name="legenda58",
    ends={
        Property(name="zlvp_Legenda60", type=zlvp_Lagerort, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Lagerort59", type=zlvp_Legenda, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lager61: BinaryAssociation = BinaryAssociation(
    name="lager61",
    ends={
        Property(name="zlvp_Lager63", type=zlvp_Lagerort, multiplicity=Multiplicity(1, 1)),
        Property(name="zlvp_Lagerort62", type=zlvp_Lager, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="zlvp",
    types={zlvp_Geschlecht, zlvp_Person, zlvp_Anrede, zlvp_Stab, zlvp_Funktion, zlvp_Leiter, zlvp_Gruppen, zlvp_Teilnehmer, zlvp_Lager, zlvp_Jahr, zlvp_Essen, zlvp_Programm, zlvp_Lagerort, zlvp_Zelt, zlvp_ZeltDetail, zlvp_Schaeden, zlvp_Verleih, zlvp_ZeltDetailBezeichnung, zlvp_Legenda, zlvp_LegendaTyp},
    associations={anrede1, geschlecht0, person4, funktion7, gruppen9, person10, lager3, gruppen13, person15, lager18, gruppen20, stab23, essen26, programm28, materialwart32, lagerort35, leiter37, teilnehmer40, zelt30, zeltDetail43, schaeden45, verleih47, zeltDetailBezeichnung52, anrede54, Lager49, legendaTyp56, legenda58, lager61},
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