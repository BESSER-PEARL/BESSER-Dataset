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

# Enumerations
PL_Form: Enumeration = Enumeration(
    name="PL_Form",
    literals={
            
    }
)

PL_Groesse: Enumeration = Enumeration(
    name="PL_Groesse",
    literals={
            
    }
)

# Classes
Zutat = Class(name="Zutat")
PlaetzchenForm = Class(name="PlaetzchenForm")
Groesse = Class(name="Groesse")
GUI = Class(name="GUI")
GUIKeksform = Class(name="GUIKeksform")
KonfigDatei = Class(name="KonfigDatei")
KonfigDatei_ = Class(name="KonfigDatei_")
TeigRezept = Class(name="TeigRezept")
TeigRezept_ = Class(name="TeigRezept_")
Plaetzchen = Class(name="Plaetzchen")
Plaetzchen_ = Class(name="Plaetzchen_")
ComboBox = Class(name="ComboBox")
PlaetzchenForm_ = Class(name="PlaetzchenForm_")
String_ = Class(name="String_")
GUIRezept = Class(name="GUIRezept")
DekorRezept = Class(name="DekorRezept")
Rezept = Class(name="Rezept")
Zutat_ = Class(name="Zutat_")
GussRezept = Class(name="GussRezept")
List_Zutat___ = Class(name="List_Zutat___")
List_PlaetzchenForm___ = Class(name="List_PlaetzchenForm___")
List_DekorRezept___ = Class(name="List_DekorRezept___")
Array_Zutat___ = Class(name="Array_Zutat___")
List_TeigRezept___ = Class(name="List_TeigRezept___")
PL_Groesse_ = Class(name="PL_Groesse_")
PL_Form_ = Class(name="PL_Form_")
Groesse_ = Class(name="Groesse_")
App = Class(name="App")
Object_ = Class(name="Object_")
ThreadExceptionEventArgs_ = Class(name="ThreadExceptionEventArgs_")
Font_ = Class(name="Font_")
Font_2 = Class(name="Font_2")
myException = Class(name="myException")
KeyPressEventArgs_ = Class(name="KeyPressEventArgs_")

# Zutat class attributes and methods
Zutat_name: Property = Property(name="name", type=String_)
Zutat_menge: Property = Property(name="menge", type=IntegerType)
Zutat_einheit: Property = Property(name="einheit", type=String_)
Zutat.attributes={Zutat_einheit, Zutat_menge, Zutat_name}

# PlaetzchenForm class attributes and methods
PlaetzchenForm_pl_groesse: Property = Property(name="pl_groesse", type=Groesse_)
PlaetzchenForm_pl_form: Property = Property(name="pl_form", type=PL_Form_)
PlaetzchenForm_faktor: Property = Property(name="faktor", type=StringType)
PlaetzchenForm.attributes={PlaetzchenForm_pl_form, PlaetzchenForm_pl_groesse, PlaetzchenForm_faktor}

# Groesse class attributes and methods
Groesse_name: Property = Property(name="name", type=StringType)
Groesse_name1: Property = Property(name="name1", type=PL_Groesse_)
Groesse_breite: Property = Property(name="breite", type=IntegerType)
Groesse_laenge: Property = Property(name="laenge", type=IntegerType)
Groesse.attributes={Groesse_name, Groesse_breite, Groesse_laenge, Groesse_name1}

# GUI class attributes and methods
GUI_dateiname: Property = Property(name="dateiname", type=StringType)
GUI_plaetzchenname: Property = Property(name="plaetzchenname", type=StringType)
GUI_teigsorte: Property = Property(name="teigsorte", type=ComboBox)
GUI_form: Property = Property(name="form", type=ComboBox)
GUI_groesse: Property = Property(name="groesse", type=ComboBox)
GUI_guss: Property = Property(name="guss", type=ComboBox)
GUI_deko: Property = Property(name="deko", type=ComboBox)
GUI_stueckzahl: Property = Property(name="stueckzahl", type=StringType)
GUI_datei: Property = Property(name="datei", type=KonfigDatei_)
GUI_plaetzchen: Property = Property(name="plaetzchen", type=Plaetzchen_)
GUI_teigList: Property = Property(name="teigList", type=List_TeigRezept___)
GUI_plformList: Property = Property(name="plformList", type=List_PlaetzchenForm___)
GUI_gussList: Property = Property(name="gussList", type=List_DekorRezept___)
GUI_dekorList: Property = Property(name="dekorList", type=List_DekorRezept___)
GUI_attribute: Property = Property(name="attribute", type=StringType)
GUI_zutatenList: Property = Property(name="zutatenList", type=List_Zutat___)
GUI.attributes={GUI_datei, GUI_groesse, GUI_plformList, GUI_teigsorte, GUI_form, GUI_guss, GUI_plaetzchen, GUI_zutatenList, GUI_attribute, GUI_dekorList, GUI_gussList, GUI_teigList, GUI_plaetzchenname, GUI_stueckzahl, GUI_dateiname, GUI_deko}

# GUIKeksform class attributes and methods
GUIKeksform_name: Property = Property(name="name", type=StringType)
GUIKeksform_pl__f: Property = Property(name="pl__f", type=PL_Form_)
GUIKeksform_breite: Property = Property(name="breite", type=IntegerType)
GUIKeksform_laenge: Property = Property(name="laenge", type=IntegerType)
GUIKeksform.attributes={GUIKeksform_laenge, GUIKeksform_name, GUIKeksform_pl__f, GUIKeksform_breite}

# KonfigDatei class attributes and methods
KonfigDatei_name: Property = Property(name="name", type=String_)
KonfigDatei_menge: Property = Property(name="menge", type=IntegerType)
KonfigDatei_backzeit: Property = Property(name="backzeit", type=IntegerType)
KonfigDatei_backtemp: Property = Property(name="backtemp", type=IntegerType)
KonfigDatei_menge1: Property = Property(name="menge1", type=IntegerType)
KonfigDatei_plaetzchen: Property = Property(name="plaetzchen", type=Plaetzchen_)
KonfigDatei_attribute: Property = Property(name="attribute", type=StringType)
KonfigDatei_attribute2: Property = Property(name="attribute2", type=StringType)
KonfigDatei.attributes={KonfigDatei_plaetzchen, KonfigDatei_menge1, KonfigDatei_attribute2, KonfigDatei_attribute, KonfigDatei_backzeit, KonfigDatei_name, KonfigDatei_menge, KonfigDatei_backtemp}

# KonfigDatei_ class attributes and methods

# TeigRezept class attributes and methods
TeigRezept_backtemp: Property = Property(name="backtemp", type=IntegerType)
TeigRezept_backzeit: Property = Property(name="backzeit", type=IntegerType)
TeigRezept_zutaten: Property = Property(name="zutaten", type=List_Zutat___)
TeigRezept_basismenge: Property = Property(name="basismenge", type=IntegerType)
TeigRezept_basis: Property = Property(name="basis", type=PlaetzchenForm_)
TeigRezept.attributes={TeigRezept_backtemp, TeigRezept_basis, TeigRezept_zutaten, TeigRezept_basismenge, TeigRezept_backzeit}

# TeigRezept_ class attributes and methods

# Plaetzchen class attributes and methods
Plaetzchen_name: Property = Property(name="name", type=String_)
Plaetzchen_teig: Property = Property(name="teig", type=List_Zutat___)
Plaetzchen_form: Property = Property(name="form", type=PlaetzchenForm_)
Plaetzchen_guss: Property = Property(name="guss", type=Zutat_)
Plaetzchen_deko: Property = Property(name="deko", type=Zutat_)
Plaetzchen_menge: Property = Property(name="menge", type=IntegerType)
Plaetzchen_rezeptTeig: Property = Property(name="rezeptTeig", type=TeigRezept_)
Plaetzchen_rezeptGuss: Property = Property(name="rezeptGuss", type=StringType)
Plaetzchen_rezeptDeko: Property = Property(name="rezeptDeko", type=StringType)
Plaetzchen.attributes={Plaetzchen_name, Plaetzchen_teig, Plaetzchen_deko, Plaetzchen_menge, Plaetzchen_rezeptTeig, Plaetzchen_rezeptDeko, Plaetzchen_form, Plaetzchen_rezeptGuss, Plaetzchen_guss}

# Plaetzchen_ class attributes and methods

# ComboBox class attributes and methods

# PlaetzchenForm_ class attributes and methods

# String_ class attributes and methods

# GUIRezept class attributes and methods
GUIRezept_name: Property = Property(name="name", type=StringType)
GUIRezept.attributes={GUIRezept_name}

# DekorRezept class attributes and methods
DekorRezept_basismenge: Property = Property(name="basismenge", type=IntegerType)
DekorRezept_zutaten: Property = Property(name="zutaten", type=List_Zutat___)
DekorRezept_basis: Property = Property(name="basis", type=PlaetzchenForm_)
DekorRezept_dekor: Property = Property(name="dekor", type=Zutat_)
DekorRezept.attributes={DekorRezept_zutaten, DekorRezept_basismenge, DekorRezept_dekor, DekorRezept_basis}

# Rezept class attributes and methods
Rezept_rezeptname: Property = Property(name="rezeptname", type=String_)
Rezept_basis: Property = Property(name="basis", type=PlaetzchenForm_)
Rezept_basismenge: Property = Property(name="basismenge", type=IntegerType)
Rezept_attribute: Property = Property(name="attribute", type=StringType)
Rezept_attribute2: Property = Property(name="attribute2", type=StringType)
Rezept.attributes={Rezept_rezeptname, Rezept_basis, Rezept_attribute2, Rezept_basismenge, Rezept_attribute}

# Zutat_ class attributes and methods

# GussRezept class attributes and methods
GussRezept_basismenge: Property = Property(name="basismenge", type=IntegerType)
GussRezept_zutat: Property = Property(name="zutat", type=Zutat)
GussRezept_basis: Property = Property(name="basis", type=PlaetzchenForm_)
GussRezept.attributes={GussRezept_basis, GussRezept_zutat, GussRezept_basismenge}

# List_Zutat___ class attributes and methods

# List_PlaetzchenForm___ class attributes and methods

# List_DekorRezept___ class attributes and methods

# Array_Zutat___ class attributes and methods

# List_TeigRezept___ class attributes and methods

# PL_Groesse_ class attributes and methods

# PL_Form_ class attributes and methods

# Groesse_ class attributes and methods

# App class attributes and methods

# Object_ class attributes and methods

# ThreadExceptionEventArgs_ class attributes and methods

# Font_ class attributes and methods

# Font_2 class attributes and methods

# myException class attributes and methods

# KeyPressEventArgs_ class attributes and methods

# Relationships
Groesse_PlaetzchenForm: BinaryAssociation = BinaryAssociation(
    name="Groesse_PlaetzchenForm",
    ends={
        Property(name="plaetzchenForm0", type=PlaetzchenForm, multiplicity=Multiplicity(0, 1)),
        Property(name="groesse21", type=Groesse, multiplicity=Multiplicity(0, 1))
    }
)
PlaetzchenForm_Plaetzchen: BinaryAssociation = BinaryAssociation(
    name="PlaetzchenForm_Plaetzchen",
    ends={
        Property(name="plaetzchen2", type=Plaetzchen, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchenForm3", type=PlaetzchenForm, multiplicity=Multiplicity(0, 1))
    }
)
Zutat_TeigRezept: BinaryAssociation = BinaryAssociation(
    name="Zutat_TeigRezept",
    ends={
        Property(name="teigRezept4", type=TeigRezept, multiplicity=Multiplicity(0, 1)),
        Property(name="zutat5", type=Zutat, multiplicity=Multiplicity(0, 1))
    }
)
PlaetzchenForm_GUI: BinaryAssociation = BinaryAssociation(
    name="PlaetzchenForm_GUI",
    ends={
        Property(name="gUI6", type=GUI, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchenForm7", type=PlaetzchenForm, multiplicity=Multiplicity(0, 1))
    }
)
PlaetzchenForm_TeigRezept: BinaryAssociation = BinaryAssociation(
    name="PlaetzchenForm_TeigRezept",
    ends={
        Property(name="teigRezept8", type=Rezept, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchenForm9", type=PlaetzchenForm, multiplicity=Multiplicity(0, 1))
    }
)
GUI_GUIPlaetzchen: BinaryAssociation = BinaryAssociation(
    name="GUI_GUIPlaetzchen",
    ends={
        Property(name="gUIPlaetzchen10", type=GUIKeksform, multiplicity=Multiplicity(0, 1)),
        Property(name="gUI11", type=GUI, multiplicity=Multiplicity(0, 1))
    }
)
TeigRezept_GUI: BinaryAssociation = BinaryAssociation(
    name="TeigRezept_GUI",
    ends={
        Property(name="gUI12", type=GUI, multiplicity=Multiplicity(0, 1)),
        Property(name="teigRezept13", type=TeigRezept, multiplicity=Multiplicity(0, 1))
    }
)
GUI_KonfigDatei2: BinaryAssociation = BinaryAssociation(
    name="GUI_KonfigDatei2",
    ends={
        Property(name="konfigDatei14", type=KonfigDatei, multiplicity=Multiplicity(0, 1)),
        Property(name="gUI15", type=GUI, multiplicity=Multiplicity(0, 1))
    }
)
GUI_GUIRezept: BinaryAssociation = BinaryAssociation(
    name="GUI_GUIRezept",
    ends={
        Property(name="gUIRezept16", type=GUIRezept, multiplicity=Multiplicity(0, 1)),
        Property(name="gUI17", type=GUI, multiplicity=Multiplicity(0, 1))
    }
)
GUIRezept_TeigRezept: BinaryAssociation = BinaryAssociation(
    name="GUIRezept_TeigRezept",
    ends={
        Property(name="teigRezept18", type=TeigRezept, multiplicity=Multiplicity(0, 1)),
        Property(name="gUIRezept19", type=GUIRezept, multiplicity=Multiplicity(0, 1))
    }
)
PlaetzchenForm_GUIKeksform: BinaryAssociation = BinaryAssociation(
    name="PlaetzchenForm_GUIKeksform",
    ends={
        Property(name="gUIKeksform20", type=GUIKeksform, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchenForm21", type=PlaetzchenForm, multiplicity=Multiplicity(0, 1))
    }
)
DekorRezept_Zutat: BinaryAssociation = BinaryAssociation(
    name="DekorRezept_Zutat",
    ends={
        Property(name="zutat22", type=Zutat, multiplicity=Multiplicity(0, 1)),
        Property(name="dekorRezept23", type=DekorRezept, multiplicity=Multiplicity(0, 1))
    }
)
DekorRezept_GUI: BinaryAssociation = BinaryAssociation(
    name="DekorRezept_GUI",
    ends={
        Property(name="gUI24", type=GUI, multiplicity=Multiplicity(0, 1)),
        Property(name="dekorRezept25", type=DekorRezept, multiplicity=Multiplicity(0, 1))
    }
)
GUI_myException: BinaryAssociation = BinaryAssociation(
    name="GUI_myException",
    ends={
        Property(name="myException26", type=myException, multiplicity=Multiplicity(0, 1)),
        Property(name="gUI27", type=GUI, multiplicity=Multiplicity(0, 1))
    }
)
Zutat_GUI: BinaryAssociation = BinaryAssociation(
    name="Zutat_GUI",
    ends={
        Property(name="gUI28", type=GUI, multiplicity=Multiplicity(0, 1)),
        Property(name="zutat29", type=Zutat, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6f967241_626a_4dfb_b842_da8e167ff233",
    types={Zutat, PlaetzchenForm, Groesse, GUI, GUIKeksform, KonfigDatei, KonfigDatei_, TeigRezept, TeigRezept_, Plaetzchen, Plaetzchen_, ComboBox, PlaetzchenForm_, String_, GUIRezept, DekorRezept, Rezept, Zutat_, GussRezept, List_Zutat___, List_PlaetzchenForm___, List_DekorRezept___, Array_Zutat___, List_TeigRezept___, PL_Groesse_, PL_Form_, Groesse_, App, Object_, ThreadExceptionEventArgs_, Font_, Font_2, myException, KeyPressEventArgs_, PL_Form, PL_Groesse},
    associations={Groesse_PlaetzchenForm, PlaetzchenForm_Plaetzchen, Zutat_TeigRezept, PlaetzchenForm_GUI, PlaetzchenForm_TeigRezept, GUI_GUIPlaetzchen, TeigRezept_GUI, GUI_KonfigDatei2, GUI_GUIRezept, GUIRezept_TeigRezept, PlaetzchenForm_GUIKeksform, DekorRezept_Zutat, DekorRezept_GUI, GUI_myException, Zutat_GUI},
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