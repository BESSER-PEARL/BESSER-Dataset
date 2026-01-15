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
UML_14_Einschraenkung = Class(name="UML::14::Einschraenkung")
UML_14_InstanzAnzahl = Class(name="UML::14::InstanzAnzahl")
UML_14_Verhalten = Class(name="UML::14::Verhalten")
UML_14_Eigenschaft = Class(name="UML::14::Eigenschaft")
UML_14_MethodenWert = Class(name="UML::14::MethodenWert")
Benanntes = Class(name="Benanntes")
UML_14_Aufzaehlung = Class(name="UML::14::Aufzaehlung")
UML_14_Einfach = Class(name="UML::14::Einfach")
UML_14_Vererbung = Class(name="UML::14::Vererbung")
UML_14_Konzept = Class(name="UML::14::Konzept")
UML_14_Verbindung = Class(name="UML::14::Verbindung")
UML_14_Verbindungsende = Class(name="UML::14::Verbindungsende")
UML_14_Aufzaehlungswert = Class(name="UML::14::Aufzaehlungswert")
UML_14_Kommentar = Class(name="UML::14::Kommentar")
UML_14_root = Class(name="UML::14::root")
UML_14_Schachtel = Class(name="UML::14::Schachtel")
UML_14_Benanntes = Class(name="UML::14::Benanntes", is_abstract=True)

# UML_14_Einschraenkung class attributes and methods
UML_14_Einschraenkung_beschreibung: Property = Property(name="beschreibung", type=StringType)
UML_14_Einschraenkung.attributes={UML_14_Einschraenkung_beschreibung}

# UML_14_InstanzAnzahl class attributes and methods
UML_14_InstanzAnzahl_untergrenze: Property = Property(name="untergrenze", type=StringType)
UML_14_InstanzAnzahl_obergrenze: Property = Property(name="obergrenze", type=StringType)
UML_14_InstanzAnzahl.attributes={UML_14_InstanzAnzahl_untergrenze, UML_14_InstanzAnzahl_obergrenze}

# UML_14_Verhalten class attributes and methods
UML_14_Verhalten_inhlat: Property = Property(name="inhlat", type=StringType)
UML_14_Verhalten_sichtbarkeit: Property = Property(name="sichtbarkeit", type=StringType)
UML_14_Verhalten.attributes={UML_14_Verhalten_inhlat, UML_14_Verhalten_sichtbarkeit}

# UML_14_Eigenschaft class attributes and methods
UML_14_Eigenschaft_initialWert: Property = Property(name="initialWert", type=StringType)
UML_14_Eigenschaft_sichtbarkeit: Property = Property(name="sichtbarkeit", type=StringType)
UML_14_Eigenschaft.attributes={UML_14_Eigenschaft_sichtbarkeit, UML_14_Eigenschaft_initialWert}

# UML_14_MethodenWert class attributes and methods
UML_14_MethodenWert_art: Property = Property(name="art", type=StringType)
UML_14_MethodenWert_standartWert: Property = Property(name="standartWert", type=StringType)
UML_14_MethodenWert.attributes={UML_14_MethodenWert_art, UML_14_MethodenWert_standartWert}

# Benanntes class attributes and methods

# UML_14_Aufzaehlung class attributes and methods

# UML_14_Einfach class attributes and methods

# UML_14_Vererbung class attributes and methods
UML_14_Vererbung_unterscheidung: Property = Property(name="unterscheidung", type=StringType)
UML_14_Vererbung.attributes={UML_14_Vererbung_unterscheidung}

# UML_14_Konzept class attributes and methods
UML_14_Konzept_istAktiev: Property = Property(name="istAktiev", type=StringType)
UML_14_Konzept.attributes={UML_14_Konzept_istAktiev}

# UML_14_Verbindung class attributes and methods

# UML_14_Verbindungsende class attributes and methods
UML_14_Verbindungsende_istNavigierbar: Property = Property(name="istNavigierbar", type=StringType)
UML_14_Verbindungsende_sichtbarkeit: Property = Property(name="sichtbarkeit", type=StringType)
UML_14_Verbindungsende.attributes={UML_14_Verbindungsende_istNavigierbar, UML_14_Verbindungsende_sichtbarkeit}

# UML_14_Aufzaehlungswert class attributes and methods
UML_14_Aufzaehlungswert_wert: Property = Property(name="wert", type=StringType)
UML_14_Aufzaehlungswert.attributes={UML_14_Aufzaehlungswert_wert}

# UML_14_Kommentar class attributes and methods
UML_14_Kommentar_inhalt: Property = Property(name="inhalt", type=StringType)
UML_14_Kommentar.attributes={UML_14_Kommentar_inhalt}

# UML_14_root class attributes and methods

# UML_14_Schachtel class attributes and methods

# UML_14_Benanntes class attributes and methods
UML_14_Benanntes_beschreibung: Property = Property(name="beschreibung", type=StringType)
UML_14_Benanntes.attributes={UML_14_Benanntes_beschreibung}

# Relationships
verhaltensWerte3: BinaryAssociation = BinaryAssociation(
    name="verhaltensWerte3",
    ends={
        Property(name="UML_14_MethodenWert4", type=UML_14_Verhalten, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Verhalten", type=UML_14_MethodenWert, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aufzaehlungsTyp0: BinaryAssociation = BinaryAssociation(
    name="aufzaehlungsTyp0",
    ends={
        Property(name="UML_14_Aufzaehlung", type=UML_14_MethodenWert, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_MethodenWert", type=UML_14_Aufzaehlung, multiplicity=Multiplicity(0, 1))
    }
)
einfacherWert1: BinaryAssociation = BinaryAssociation(
    name="einfacherWert1",
    ends={
        Property(name="UML_14_Einfach", type=UML_14_MethodenWert, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_MethodenWert2", type=UML_14_Einfach, multiplicity=Multiplicity(0, 1))
    }
)
teilnehmer18: BinaryAssociation = BinaryAssociation(
    name="teilnehmer18",
    ends={
        Property(name="UML_14_Verbindungsende", type=UML_14_Konzept, multiplicity=Multiplicity(0, 1)),
        Property(name="UML_14_Konzept19", type=UML_14_Verbindungsende, multiplicity=Multiplicity(1, 1))
    }
)
anzahlInstanzen5: BinaryAssociation = BinaryAssociation(
    name="anzahlInstanzen5",
    ends={
        Property(name="UML_14_InstanzAnzahl", type=UML_14_Eigenschaft, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Eigenschaft", type=UML_14_InstanzAnzahl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aufzaehlungsTyp6: BinaryAssociation = BinaryAssociation(
    name="aufzaehlungsTyp6",
    ends={
        Property(name="UML_14_Aufzaehlung8", type=UML_14_Eigenschaft, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Eigenschaft7", type=UML_14_Aufzaehlung, multiplicity=Multiplicity(0, 1))
    }
)
anzahlInstanzen20: BinaryAssociation = BinaryAssociation(
    name="anzahlInstanzen20",
    ends={
        Property(name="UML_14_InstanzAnzahl22", type=UML_14_Verbindungsende, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Verbindungsende21", type=UML_14_InstanzAnzahl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
einfacherTyp9: BinaryAssociation = BinaryAssociation(
    name="einfacherTyp9",
    ends={
        Property(name="UML_14_Einfach11", type=UML_14_Eigenschaft, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Eigenschaft10", type=UML_14_Einfach, multiplicity=Multiplicity(0, 1))
    }
)
auszeichner23: BinaryAssociation = BinaryAssociation(
    name="auszeichner23",
    ends={
        Property(name="UML_14_Eigenschaft25", type=UML_14_Verbindungsende, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Verbindungsende24", type=UML_14_Eigenschaft, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
kind12: BinaryAssociation = BinaryAssociation(
    name="kind12",
    ends={
        Property(name="UML_14_Konzept", type=UML_14_Vererbung, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Vererbung", type=UML_14_Konzept, multiplicity=Multiplicity(0, 9999))
    }
)
eltern13: BinaryAssociation = BinaryAssociation(
    name="eltern13",
    ends={
        Property(name="UML_14_Konzept15", type=UML_14_Vererbung, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Vererbung14", type=UML_14_Konzept, multiplicity=Multiplicity(0, 9999))
    }
)
eigenschaften26: BinaryAssociation = BinaryAssociation(
    name="eigenschaften26",
    ends={
        Property(name="UML_14_Eigenschaft28", type=UML_14_Konzept, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Konzept27", type=UML_14_Eigenschaft, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
verhalten29: BinaryAssociation = BinaryAssociation(
    name="verhalten29",
    ends={
        Property(name="UML_14_Verhalten31", type=UML_14_Konzept, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Konzept30", type=UML_14_Verhalten, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
verbinder16: BinaryAssociation = BinaryAssociation(
    name="verbinder16",
    ends={
        Property(name="Verbindungsende", type=UML_14_Verbindung, multiplicity=Multiplicity(1, 1)),
        Property(name="link", type=UML_14_Verbindungsende, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
link17: BinaryAssociation = BinaryAssociation(
    name="link17",
    ends={
        Property(name="Verbindung", type=UML_14_Verbindungsende, multiplicity=Multiplicity(1, 1)),
        Property(name="verbinder", type=UML_14_Verbindung, multiplicity=Multiplicity(1, 1))
    }
)
zeichen32: BinaryAssociation = BinaryAssociation(
    name="zeichen32",
    ends={
        Property(name="UML_14_Aufzaehlungswert", type=UML_14_Aufzaehlung, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Aufzaehlung33", type=UML_14_Aufzaehlungswert, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
geschachtelt34: BinaryAssociation = BinaryAssociation(
    name="geschachtelt34",
    ends={
        Property(name="UML_14_Schachtel", type=UML_14_root, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_root", type=UML_14_Schachtel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seineKlassen35: BinaryAssociation = BinaryAssociation(
    name="seineKlassen35",
    ends={
        Property(name="UML_14_Konzept37", type=UML_14_Schachtel, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Schachtel36", type=UML_14_Konzept, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seinePakete39: BinaryAssociation = BinaryAssociation(
    name="seinePakete39",
    ends={
        Property(name="UML_14_Schachtel40", type=UML_14_Schachtel, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Schachtel38", type=UML_14_Schachtel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seineAufzaehlungen41: BinaryAssociation = BinaryAssociation(
    name="seineAufzaehlungen41",
    ends={
        Property(name="UML_14_Aufzaehlung43", type=UML_14_Schachtel, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Schachtel42", type=UML_14_Aufzaehlung, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seineVererbungen44: BinaryAssociation = BinaryAssociation(
    name="seineVererbungen44",
    ends={
        Property(name="UML_14_Vererbung46", type=UML_14_Schachtel, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Schachtel45", type=UML_14_Vererbung, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seineVerbindungen47: BinaryAssociation = BinaryAssociation(
    name="seineVerbindungen47",
    ends={
        Property(name="UML_14_Verbindung", type=UML_14_Schachtel, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Schachtel48", type=UML_14_Verbindung, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
seineEinfachenTypen49: BinaryAssociation = BinaryAssociation(
    name="seineEinfachenTypen49",
    ends={
        Property(name="UML_14_Einfach51", type=UML_14_Schachtel, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Schachtel50", type=UML_14_Einfach, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kommentare52: BinaryAssociation = BinaryAssociation(
    name="kommentare52",
    ends={
        Property(name="UML_14_Kommentar", type=UML_14_Benanntes, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Benanntes", type=UML_14_Kommentar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
einschraenkungen53: BinaryAssociation = BinaryAssociation(
    name="einschraenkungen53",
    ends={
        Property(name="UML_14_Einschraenkung", type=UML_14_Benanntes, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Benanntes54", type=UML_14_Einschraenkung, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML_14_Verhalten_Benanntes = Generalization(general=Benanntes, specific=UML_14_Verhalten)
gen_UML_14_Eigenschaft_Benanntes = Generalization(general=Benanntes, specific=UML_14_Eigenschaft)
gen_UML_14_MethodenWert_Benanntes = Generalization(general=Benanntes, specific=UML_14_MethodenWert)
gen_UML_14_Konzept_Benanntes = Generalization(general=Benanntes, specific=UML_14_Konzept)
gen_UML_14_Verbindung_Benanntes = Generalization(general=Benanntes, specific=UML_14_Verbindung)
gen_UML_14_Einfach_Benanntes = Generalization(general=Benanntes, specific=UML_14_Einfach)
gen_UML_14_Verbindungsende_Benanntes = Generalization(general=Benanntes, specific=UML_14_Verbindungsende)
gen_UML_14_Aufzaehlung_Benanntes = Generalization(general=Benanntes, specific=UML_14_Aufzaehlung)
gen_UML_14_Schachtel_Benanntes = Generalization(general=Benanntes, specific=UML_14_Schachtel)

# Domain Model
domain_model = DomainModel(
    name="UML_14",
    types={UML_14_Einschraenkung, UML_14_InstanzAnzahl, UML_14_Verhalten, UML_14_Eigenschaft, UML_14_MethodenWert, Benanntes, UML_14_Aufzaehlung, UML_14_Einfach, UML_14_Vererbung, UML_14_Konzept, UML_14_Verbindung, UML_14_Verbindungsende, UML_14_Aufzaehlungswert, UML_14_Kommentar, UML_14_root, UML_14_Schachtel, UML_14_Benanntes},
    associations={verhaltensWerte3, aufzaehlungsTyp0, einfacherWert1, teilnehmer18, anzahlInstanzen5, aufzaehlungsTyp6, anzahlInstanzen20, einfacherTyp9, auszeichner23, kind12, eltern13, eigenschaften26, verhalten29, verbinder16, link17, zeichen32, geschachtelt34, seineKlassen35, seinePakete39, seineAufzaehlungen41, seineVererbungen44, seineVerbindungen47, seineEinfachenTypen49, kommentare52, einschraenkungen53},
    generalizations={gen_UML_14_Verhalten_Benanntes, gen_UML_14_Eigenschaft_Benanntes, gen_UML_14_MethodenWert_Benanntes, gen_UML_14_Konzept_Benanntes, gen_UML_14_Verbindung_Benanntes, gen_UML_14_Einfach_Benanntes, gen_UML_14_Verbindungsende_Benanntes, gen_UML_14_Aufzaehlung_Benanntes, gen_UML_14_Schachtel_Benanntes},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)