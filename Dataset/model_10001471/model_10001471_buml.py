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
RazredA2 = Class(name="RazredA2")
RazredB2 = Class(name="RazredB2")
PravokotniLik = Class(name="PravokotniLik", is_abstract=True)
Pravokotnik3 = Class(name="Pravokotnik3")
Lik3_Interface = Class(name="Lik3_Interface")
BancniRacun = Class(name="BancniRacun")
RazredA = Class(name="RazredA")
RazredB = Class(name="RazredB")
RazredC = Class(name="RazredC")
RazredD = Class(name="RazredD")
RazredE = Class(name="RazredE")
RazredF = Class(name="RazredF")
RazredG = Class(name="RazredG")
RazredJ = Class(name="RazredJ")
RazredH = Class(name="RazredH")
RazredK = Class(name="RazredK")
RazredL = Class(name="RazredL")
RazredM = Class(name="RazredM")
Class_N = Class(name="Class_N")
ClassP = Class(name="ClassP")
InterfaceO_Interface = Class(name="InterfaceO_Interface")
ClassQ = Class(name="ClassQ")
ClassR = Class(name="ClassR")
ClassS = Class(name="ClassS")
ClassT = Class(name="ClassT")
ClassU = Class(name="ClassU")
ClassV = Class(name="ClassV")
Pes = Class(name="Pes")
Oseba = Class(name="Oseba")
LocalDate = Class(name="LocalDate")
Zaposlen = Class(name="Zaposlen")
Student = Class(name="Student")
LocalDate1 = Class(name="LocalDate1")
RazredA1 = Class(name="RazredA1")
RazredC1 = Class(name="RazredC1")
RazredB1 = Class(name="RazredB1")
Lik = Class(name="Lik", is_abstract=True)
Color = Class(name="Color")
PravokotnikA = Class(name="PravokotnikA")
Pravokotnik2 = Class(name="Pravokotnik2")
Lik2 = Class(name="Lik2", is_abstract=True)
Krog2 = Class(name="Krog2")
Vozen_Interface = Class(name="Vozen_Interface")
Iterator_Interface = Class(name="Iterator_Interface")
Kolo = Class(name="Kolo")
Avtomobil = Class(name="Avtomobil")
Prepoznaven_Interface = Class(name="Prepoznaven_Interface")
Collection_Interface = Class(name="Collection_Interface")
Throwable = Class(name="Throwable")
Exception = Class(name="Exception")
RuntimeException = Class(name="RuntimeException")
IOException = Class(name="IOException")
ArithmeticException = Class(name="ArithmeticException")
IllegalArgumentException = Class(name="IllegalArgumentException")
SecurityException = Class(name="SecurityException")
FileNotFoundException = Class(name="FileNotFoundException")
Lik1 = Class(name="Lik1", is_abstract=True)
Pravokotnik = Class(name="Pravokotnik")
Elipsa = Class(name="Elipsa")
Potnik_Actor = Class(name="Potnik_Actor")
NakupKarte_UseCase = Class(name="NakupKarte_UseCase")
NeDeluje_UseCase = Class(name="NeDeluje_UseCase")
Preklic_UseCase = Class(name="Preklic_UseCase")
NiVra_ila_UseCase = Class(name="NiVra_ila_UseCase")
Potnik__Actor = Class(name="Potnik__Actor")
NakupPosamezneKarte_UseCase = Class(name="NakupPosamezneKarte_UseCase")
ZbiranjeDenarja_UseCase = Class(name="ZbiranjeDenarja_UseCase")
Preklic__UseCase = Class(name="Preklic__UseCase")
NiVra_ila__UseCase = Class(name="NiVra_ila__UseCase")
NakupSkupinskeKarte_UseCase = Class(name="NakupSkupinskeKarte_UseCase")
Razred = Class(name="Razred")
Oseba1 = Class(name="Oseba1")
Oseba2 = Class(name="Oseba2")
BancniRacun1 = Class(name="BancniRacun1")
Pravokotnik1 = Class(name="Pravokotnik1")
Lik3 = Class(name="Lik3", is_abstract=True)
Interface_Interface = Class(name="Interface_Interface")
Oddelek = Class(name="Oddelek")
Class_ = Class(name="Class")
RazredM1 = Class(name="RazredM1")
Class_N1 = Class(name="Class_N1")
Oddelek1 = Class(name="Oddelek1")
Oseba3 = Class(name="Oseba3")
Oseba4 = Class(name="Oseba4")
Oddelek2 = Class(name="Oddelek2")
Vozen_Interface1 = Class(name="Vozen_Interface1")
Kolo1 = Class(name="Kolo1")
Avtomobil1 = Class(name="Avtomobil1")
Prepoznaven_Interface1 = Class(name="Prepoznaven_Interface1")
ClassP1 = Class(name="ClassP1")
InterfaceO_Interface1 = Class(name="InterfaceO_Interface1")
Soba = Class(name="Soba")
Objekt = Class(name="Objekt")
Soba2 = Class(name="Soba2")
Stanovanje = Class(name="Stanovanje")

# RazredA2 class attributes and methods
RazredA2_objektB: Property = Property(name="objektB", type=RazredB2)
RazredA2.attributes={RazredA2_objektB}

# RazredB2 class attributes and methods

# PravokotniLik class attributes and methods
PravokotniLik_sirina: Property = Property(name="sirina", type=StringType)
PravokotniLik_visina: Property = Property(name="visina", type=StringType)
PravokotniLik.attributes={PravokotniLik_visina, PravokotniLik_sirina}

# Pravokotnik3 class attributes and methods
Pravokotnik3_koordinataY: Property = Property(name="koordinataY", type=StringType)
Pravokotnik3_koordinataX: Property = Property(name="koordinataX", type=StringType)
Pravokotnik3.attributes={Pravokotnik3_koordinataX, Pravokotnik3_koordinataY}

# Lik3_Interface class attributes and methods

# BancniRacun class attributes and methods
BancniRacun_lastnik: Property = Property(name="lastnik", type=StringType)
BancniRacun_stanje: Property = Property(name="stanje", type=FloatType)
BancniRacun_aktiven: Property = Property(name="aktiven", type=BooleanType)
BancniRacun.attributes={BancniRacun_lastnik, BancniRacun_aktiven, BancniRacun_stanje}

# RazredA class attributes and methods
RazredA_publicAtribut: Property = Property(name="publicAtribut", type=FloatType)
RazredA_privateAtribut: Property = Property(name="privateAtribut", type=IntegerType)
RazredA_protectedAtribut: Property = Property(name="protectedAtribut", type=StringType)
RazredA_packageAtribut: Property = Property(name="packageAtribut", type=StringType)
RazredA.attributes={RazredA_protectedAtribut, RazredA_publicAtribut, RazredA_privateAtribut, RazredA_packageAtribut}

# RazredB class attributes and methods

# RazredC class attributes and methods
RazredC_publicAtribut: Property = Property(name="publicAtribut", type=FloatType)
RazredC_privateAtribut: Property = Property(name="privateAtribut", type=IntegerType)
RazredC_protectedAtribut: Property = Property(name="protectedAtribut", type=StringType)
RazredC_packageAtribut: Property = Property(name="packageAtribut", type=StringType)
RazredC.attributes={RazredC_packageAtribut, RazredC_publicAtribut, RazredC_privateAtribut, RazredC_protectedAtribut}

# RazredD class attributes and methods

# RazredE class attributes and methods

# RazredF class attributes and methods

# RazredG class attributes and methods

# RazredJ class attributes and methods

# RazredH class attributes and methods

# RazredK class attributes and methods

# RazredL class attributes and methods

# RazredM class attributes and methods

# Class_N class attributes and methods

# ClassP class attributes and methods

# InterfaceO_Interface class attributes and methods

# ClassQ class attributes and methods

# ClassR class attributes and methods

# ClassS class attributes and methods

# ClassT class attributes and methods

# ClassU class attributes and methods

# ClassV class attributes and methods

# Pes class attributes and methods
Pes_vzdevek: Property = Property(name="vzdevek", type=StringType)
Pes_pasma: Property = Property(name="pasma", type=StringType)
Pes_visina: Property = Property(name="visina", type=StringType)
Pes.attributes={Pes_pasma, Pes_vzdevek, Pes_visina}

# Oseba class attributes and methods
Oseba_ime: Property = Property(name="ime", type=StringType)
Oseba_priimek: Property = Property(name="priimek", type=StringType)
Oseba_spol: Property = Property(name="spol", type=StringType)
Oseba_datumRojstva: Property = Property(name="datumRojstva", type=LocalDate)
Oseba.attributes={Oseba_spol, Oseba_datumRojstva, Oseba_ime, Oseba_priimek}

# LocalDate class attributes and methods

# Zaposlen class attributes and methods
Zaposlen_izobrazba: Property = Property(name="izobrazba", type=StringType)
Zaposlen_urnaPostavka: Property = Property(name="urnaPostavka", type=FloatType)
Zaposlen.attributes={Zaposlen_urnaPostavka, Zaposlen_izobrazba}

# Student class attributes and methods
Student_vpisnaStevilka: Property = Property(name="vpisnaStevilka", type=StringType)
Student_studijskiProgram: Property = Property(name="studijskiProgram", type=StringType)
Student_datumVpisa: Property = Property(name="datumVpisa", type=LocalDate1)
Student.attributes={Student_datumVpisa, Student_studijskiProgram, Student_vpisnaStevilka}

# LocalDate1 class attributes and methods

# RazredA1 class attributes and methods
RazredA1_stevilo: Property = Property(name="stevilo", type=StringType)
RazredA1.attributes={RazredA1_stevilo}

# RazredC1 class attributes and methods
RazredC1_stevilo: Property = Property(name="stevilo", type=StringType)
RazredC1.attributes={RazredC1_stevilo}

# RazredB1 class attributes and methods

# Lik class attributes and methods
Lik_x1: Property = Property(name="x1", type=StringType)
Lik_barva: Property = Property(name="barva", type=Color)
Lik_x: Property = Property(name="x", type=StringType)
Lik.attributes={Lik_x, Lik_barva, Lik_x1}

# Color class attributes and methods

# PravokotnikA class attributes and methods
PravokotnikA_stranicaA: Property = Property(name="stranicaA", type=StringType)
PravokotnikA_stranicaB: Property = Property(name="stranicaB", type=StringType)
PravokotnikA.attributes={PravokotnikA_stranicaB, PravokotnikA_stranicaA}

# Pravokotnik2 class attributes and methods

# Lik2 class attributes and methods
Lik2_x: Property = Property(name="x", type=StringType)
Lik2_x1: Property = Property(name="x1", type=StringType)
Lik2_sirina: Property = Property(name="sirina", type=StringType)
Lik2_visina: Property = Property(name="visina", type=StringType)
Lik2_barva: Property = Property(name="barva", type=Color)
Lik2.attributes={Lik2_barva, Lik2_visina, Lik2_sirina, Lik2_x, Lik2_x1}

# Krog2 class attributes and methods

# Vozen_Interface class attributes and methods

# Iterator_Interface class attributes and methods

# Kolo class attributes and methods

# Avtomobil class attributes and methods

# Prepoznaven_Interface class attributes and methods

# Collection_Interface class attributes and methods

# Throwable class attributes and methods

# Exception class attributes and methods

# RuntimeException class attributes and methods

# IOException class attributes and methods

# ArithmeticException class attributes and methods

# IllegalArgumentException class attributes and methods

# SecurityException class attributes and methods

# FileNotFoundException class attributes and methods

# Lik1 class attributes and methods
Lik1_visina: Property = Property(name="visina", type=StringType)
Lik1_barva: Property = Property(name="barva", type=Color)
Lik1_x: Property = Property(name="x", type=StringType)
Lik1_x1: Property = Property(name="x1", type=StringType)
Lik1_sirina: Property = Property(name="sirina", type=StringType)
Lik1.attributes={Lik1_sirina, Lik1_x1, Lik1_barva, Lik1_x, Lik1_visina}

# Pravokotnik class attributes and methods

# Elipsa class attributes and methods

# Potnik_Actor class attributes and methods

# NakupKarte_UseCase class attributes and methods

# NeDeluje_UseCase class attributes and methods

# Preklic_UseCase class attributes and methods

# NiVra_ila_UseCase class attributes and methods

# Potnik__Actor class attributes and methods

# NakupPosamezneKarte_UseCase class attributes and methods

# ZbiranjeDenarja_UseCase class attributes and methods

# Preklic__UseCase class attributes and methods

# NiVra_ila__UseCase class attributes and methods

# NakupSkupinskeKarte_UseCase class attributes and methods

# Razred class attributes and methods
Razred_attribute: Property = Property(name="attribute", type=StringType)
Razred.attributes={Razred_attribute}

# Oseba1 class attributes and methods
Oseba1_ime: Property = Property(name="ime", type=StringType)
Oseba1_priimek: Property = Property(name="priimek", type=StringType)
Oseba1_emso: Property = Property(name="emso", type=StringType)
Oseba1.attributes={Oseba1_priimek, Oseba1_ime, Oseba1_emso}

# Oseba2 class attributes and methods
Oseba2_priimek: Property = Property(name="priimek", type=StringType)
Oseba2_ime: Property = Property(name="ime", type=StringType)
Oseba2_datumRojstva: Property = Property(name="datumRojstva", type=DateType)
Oseba2.attributes={Oseba2_datumRojstva, Oseba2_priimek, Oseba2_ime}

# BancniRacun1 class attributes and methods
BancniRacun1_lastnik: Property = Property(name="lastnik", type=StringType)
BancniRacun1_stanje: Property = Property(name="stanje", type=FloatType)
BancniRacun1_aktiven: Property = Property(name="aktiven", type=BooleanType)
BancniRacun1.attributes={BancniRacun1_aktiven, BancniRacun1_stanje, BancniRacun1_lastnik}

# Pravokotnik1 class attributes and methods
Pravokotnik1_stranicaA: Property = Property(name="stranicaA", type=StringType)
Pravokotnik1_stranicaB: Property = Property(name="stranicaB", type=StringType)
Pravokotnik1.attributes={Pravokotnik1_stranicaB, Pravokotnik1_stranicaA}

# Lik3 class attributes and methods
Lik3_x: Property = Property(name="x", type=StringType)
Lik3_x1: Property = Property(name="x1", type=StringType)
Lik3_barva: Property = Property(name="barva", type=Color)
Lik3.attributes={Lik3_x1, Lik3_barva, Lik3_x}

# Interface_Interface class attributes and methods

# Oddelek class attributes and methods

# Class class attributes and methods

# RazredM1 class attributes and methods

# Class_N1 class attributes and methods

# Oddelek1 class attributes and methods

# Oseba3 class attributes and methods

# Oseba4 class attributes and methods

# Oddelek2 class attributes and methods

# Vozen_Interface1 class attributes and methods

# Kolo1 class attributes and methods

# Avtomobil1 class attributes and methods

# Prepoznaven_Interface1 class attributes and methods

# ClassP1 class attributes and methods

# InterfaceO_Interface1 class attributes and methods

# Soba class attributes and methods

# Objekt class attributes and methods

# Soba2 class attributes and methods

# Stanovanje class attributes and methods

# Relationships
ClassD_ClassE: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassE",
    ends={
        Property(name="classE0", type=RazredE, multiplicity=Multiplicity(0, 1)),
        Property(name="classD1", type=RazredD, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_RazredE: BinaryAssociation = BinaryAssociation(
    name="ClassD_RazredE",
    ends={
        Property(name="classG2", type=RazredG, multiplicity=Multiplicity(0, 1)),
        Property(name="classF3", type=RazredF, multiplicity=Multiplicity(0, 1))
    }
)
RazredD_RazredE: BinaryAssociation = BinaryAssociation(
    name="RazredD_RazredE",
    ends={
        Property(name="classG4", type=RazredJ, multiplicity=Multiplicity(0, 1)),
        Property(name="classF5", type=RazredH, multiplicity=Multiplicity(0, 1))
    }
)
Potnik_NakupKarte: BinaryAssociation = BinaryAssociation(
    name="Potnik_NakupKarte",
    ends={
        Property(name="nakupKarte6", type=NakupKarte_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="potnik7", type=Potnik_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Potnik_NakupKarte2: BinaryAssociation = BinaryAssociation(
    name="Potnik_NakupKarte2",
    ends={
        Property(name="nakupKarte8", type=NakupPosamezneKarte_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="potnik9", type=Potnik__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Potnik__NakupSkupinskeKarte: BinaryAssociation = BinaryAssociation(
    name="Potnik__NakupSkupinskeKarte",
    ends={
        Property(name="nakupSkupinskeKarte10", type=NakupSkupinskeKarte_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="potnik11", type=Potnik__Actor, multiplicity=Multiplicity(0, 1))
    }
)
ClassD_ClassE2: BinaryAssociation = BinaryAssociation(
    name="ClassD_ClassE2",
    ends={
        Property(name="Oseba12", type=Oseba3, multiplicity=Multiplicity(0, 1)),
        Property(name="classD13", type=Oddelek1, multiplicity=Multiplicity(0, 1))
    }
)
Oddelek_Oseba: BinaryAssociation = BinaryAssociation(
    name="Oddelek_Oseba",
    ends={
        Property(name="zaposlen14", type=Oseba4, multiplicity=Multiplicity(1, 9999)),
        Property(name="oddelek15", type=Oddelek2, multiplicity=Multiplicity(1, 9999))
    }
)
ClassD_RazredE2: BinaryAssociation = BinaryAssociation(
    name="ClassD_RazredE2",
    ends={
        Property(name="classG16", type=Soba, multiplicity=Multiplicity(0, 1)),
        Property(name="classF17", type=Objekt, multiplicity=Multiplicity(0, 1))
    }
)
Stanovanje_Soba: BinaryAssociation = BinaryAssociation(
    name="Stanovanje_Soba",
    ends={
        Property(name="soba18", type=Soba2, multiplicity=Multiplicity(0, 1)),
        Property(name="stanovanje19", type=Stanovanje, multiplicity=Multiplicity(0, 1))
    }
)
RazredA_RazredB: BinaryAssociation = BinaryAssociation(
    name="RazredA_RazredB",
    ends={
        Property(name="razredB20", type=RazredB2, multiplicity=Multiplicity(0, 1)),
        Property(name="razredA21", type=RazredA2, multiplicity=Multiplicity(0, 1))
    }
)
RazredA_RazredB1: BinaryAssociation = BinaryAssociation(
    name="RazredA_RazredB1",
    ends={
        Property(name="razredB22", type=RazredB2, multiplicity=Multiplicity(0, 1)),
        Property(name="razredA23", type=RazredA2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8uGwcAlCEeqB3a4sRh_tuQ",
    types={RazredA2, RazredB2, PravokotniLik, Pravokotnik3, Lik3_Interface, BancniRacun, RazredA, RazredB, RazredC, RazredD, RazredE, RazredF, RazredG, RazredJ, RazredH, RazredK, RazredL, RazredM, Class_N, ClassP, InterfaceO_Interface, ClassQ, ClassR, ClassS, ClassT, ClassU, ClassV, Pes, Oseba, LocalDate, Zaposlen, Student, LocalDate1, RazredA1, RazredC1, RazredB1, Lik, Color, PravokotnikA, Pravokotnik2, Lik2, Krog2, Vozen_Interface, Iterator_Interface, Kolo, Avtomobil, Prepoznaven_Interface, Collection_Interface, Throwable, Exception, RuntimeException, IOException, ArithmeticException, IllegalArgumentException, SecurityException, FileNotFoundException, Lik1, Pravokotnik, Elipsa, Potnik_Actor, NakupKarte_UseCase, NeDeluje_UseCase, Preklic_UseCase, NiVra_ila_UseCase, Potnik__Actor, NakupPosamezneKarte_UseCase, ZbiranjeDenarja_UseCase, Preklic__UseCase, NiVra_ila__UseCase, NakupSkupinskeKarte_UseCase, Razred, Oseba1, Oseba2, BancniRacun1, Pravokotnik1, Lik3, Interface_Interface, Oddelek, Class_, RazredM1, Class_N1, Oddelek1, Oseba3, Oseba4, Oddelek2, Vozen_Interface1, Kolo1, Avtomobil1, Prepoznaven_Interface1, ClassP1, InterfaceO_Interface1, Soba, Objekt, Soba2, Stanovanje},
    associations={ClassD_ClassE, ClassD_RazredE, RazredD_RazredE, Potnik_NakupKarte, Potnik_NakupKarte2, Potnik__NakupSkupinskeKarte, ClassD_ClassE2, Oddelek_Oseba, ClassD_RazredE2, Stanovanje_Soba, RazredA_RazredB, RazredA_RazredB1},
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