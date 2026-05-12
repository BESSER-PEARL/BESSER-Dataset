from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################







class NakupSkupinskeKarte_UseCase:

    pass


class NiVra_ila__UseCase:

    pass


class Preklic__UseCase:

    pass


class ZbiranjeDenarja_UseCase:

    pass


class NakupPosamezneKarte_UseCase:

    pass


class Potnik__Actor:

    pass


class NiVra_ila_UseCase:

    pass


class Preklic_UseCase:

    pass


class NeDeluje_UseCase:

    pass


class NakupKarte_UseCase:

    pass


class Potnik_Actor:

    pass





class Stanovanje:

    pass


class Soba2:

    pass


class Objekt:

    pass


class Soba:

    pass


class InterfaceO_Interface1:

    pass


class ClassP1:

    pass


class Prepoznaven_Interface1:

    pass


class Avtomobil1:

    pass


class Kolo1:

    pass


class Vozen_Interface1:

    pass


class Oddelek2:

    pass


class Oseba4:

    pass


class Oseba3:

    pass


class Oddelek1:

    pass


class Class_N1:

    pass


class RazredM1:

    pass


class Class:

    pass


class Oddelek:

    pass


class Interface_Interface:

    pass


class Lik3(ABC):

    def __init__(self, x: str, x1: str, barva: Color):
        self.x = x
        self.x1 = x1
        self.barva = barva
        
        pass
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def x1(self):
        return self.__x1
    @x1.setter
    def x1(self, x1: str):
        self.__x1 = x1

    @property
    def barva(self):
        return self.__barva
    @barva.setter
    def barva(self, barva: Color):
        self.__barva = barva



class Pravokotnik1:

    def __init__(self, stranicaA: str, stranicaB: str):
        self.stranicaA = stranicaA
        self.stranicaB = stranicaB
        
        pass
    @property
    def stranicaB(self):
        return self.__stranicaB
    @stranicaB.setter
    def stranicaB(self, stranicaB: str):
        self.__stranicaB = stranicaB

    @property
    def stranicaA(self):
        return self.__stranicaA
    @stranicaA.setter
    def stranicaA(self, stranicaA: str):
        self.__stranicaA = stranicaA



class BancniRacun1:

    def __init__(self, lastnik: str, stanje: float, aktiven: bool):
        self.lastnik = lastnik
        self.stanje = stanje
        self.aktiven = aktiven
        
        pass
    @property
    def stanje(self):
        return self.__stanje
    @stanje.setter
    def stanje(self, stanje: float):
        self.__stanje = stanje

    @property
    def aktiven(self):
        return self.__aktiven
    @aktiven.setter
    def aktiven(self, aktiven: bool):
        self.__aktiven = aktiven

    @property
    def lastnik(self):
        return self.__lastnik
    @lastnik.setter
    def lastnik(self, lastnik: str):
        self.__lastnik = lastnik



class Oseba2:

    def __init__(self, priimek: str, ime: str, datumRojstva: date):
        self.priimek = priimek
        self.ime = ime
        self.datumRojstva = datumRojstva
        
        pass
    @property
    def ime(self):
        return self.__ime
    @ime.setter
    def ime(self, ime: str):
        self.__ime = ime

    @property
    def priimek(self):
        return self.__priimek
    @priimek.setter
    def priimek(self, priimek: str):
        self.__priimek = priimek

    @property
    def datumRojstva(self):
        return self.__datumRojstva
    @datumRojstva.setter
    def datumRojstva(self, datumRojstva: date):
        self.__datumRojstva = datumRojstva



class Oseba1:

    def __init__(self, ime: str, priimek: str, emso: str):
        self.ime = ime
        self.priimek = priimek
        self.emso = emso
        
        pass
    @property
    def emso(self):
        return self.__emso
    @emso.setter
    def emso(self, emso: str):
        self.__emso = emso

    @property
    def ime(self):
        return self.__ime
    @ime.setter
    def ime(self, ime: str):
        self.__ime = ime

    @property
    def priimek(self):
        return self.__priimek
    @priimek.setter
    def priimek(self, priimek: str):
        self.__priimek = priimek



class Razred:

    def __init__(self, attribute: str):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Elipsa:

    pass


class Pravokotnik:

    pass


class Lik1(ABC):

    def __init__(self, visina: str, barva: Color, x: str, x1: str, sirina: str):
        self.visina = visina
        self.barva = barva
        self.x = x
        self.x1 = x1
        self.sirina = sirina
        
        pass
    @property
    def sirina(self):
        return self.__sirina
    @sirina.setter
    def sirina(self, sirina: str):
        self.__sirina = sirina

    @property
    def x1(self):
        return self.__x1
    @x1.setter
    def x1(self, x1: str):
        self.__x1 = x1

    @property
    def barva(self):
        return self.__barva
    @barva.setter
    def barva(self, barva: Color):
        self.__barva = barva

    @property
    def visina(self):
        return self.__visina
    @visina.setter
    def visina(self, visina: str):
        self.__visina = visina

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: str):
        self.__x = x



class FileNotFoundException:

    pass


class SecurityException:

    pass


class IllegalArgumentException:

    pass


class ArithmeticException:

    pass


class IOException:

    pass


class RuntimeException:

    pass


class Exception:

    pass


class Throwable:

    pass


class Collection_Interface:

    pass


class Prepoznaven_Interface:

    pass


class Avtomobil:

    pass


class Kolo:

    pass


class Iterator_Interface:

    pass


class Vozen_Interface:

    pass


class Krog2:

    pass


class Lik2(ABC):

    def __init__(self, x: str, x1: str, sirina: str, visina: str, barva: Color):
        self.x = x
        self.x1 = x1
        self.sirina = sirina
        self.visina = visina
        self.barva = barva
        
        pass
    @property
    def x1(self):
        return self.__x1
    @x1.setter
    def x1(self, x1: str):
        self.__x1 = x1

    @property
    def visina(self):
        return self.__visina
    @visina.setter
    def visina(self, visina: str):
        self.__visina = visina

    @property
    def sirina(self):
        return self.__sirina
    @sirina.setter
    def sirina(self, sirina: str):
        self.__sirina = sirina

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def barva(self):
        return self.__barva
    @barva.setter
    def barva(self, barva: Color):
        self.__barva = barva



class Pravokotnik2:

    pass


class PravokotnikA:

    def __init__(self, stranicaA: str, stranicaB: str):
        self.stranicaA = stranicaA
        self.stranicaB = stranicaB
        
        pass
    @property
    def stranicaA(self):
        return self.__stranicaA
    @stranicaA.setter
    def stranicaA(self, stranicaA: str):
        self.__stranicaA = stranicaA

    @property
    def stranicaB(self):
        return self.__stranicaB
    @stranicaB.setter
    def stranicaB(self, stranicaB: str):
        self.__stranicaB = stranicaB



class Color:

    pass


class Lik(ABC):

    def __init__(self, x1: str, barva: Color, x: str):
        self.x1 = x1
        self.barva = barva
        self.x = x
        
        pass
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def barva(self):
        return self.__barva
    @barva.setter
    def barva(self, barva: Color):
        self.__barva = barva

    @property
    def x1(self):
        return self.__x1
    @x1.setter
    def x1(self, x1: str):
        self.__x1 = x1



class RazredB1:

    pass


class RazredC1:

    def __init__(self, stevilo: str):
        self.stevilo = stevilo
        
        pass
    @property
    def stevilo(self):
        return self.__stevilo
    @stevilo.setter
    def stevilo(self, stevilo: str):
        self.__stevilo = stevilo



class RazredA1:

    def __init__(self, stevilo: str):
        self.stevilo = stevilo
        
        pass
    @property
    def stevilo(self):
        return self.__stevilo
    @stevilo.setter
    def stevilo(self, stevilo: str):
        self.__stevilo = stevilo



class LocalDate1:

    pass


class Student:

    def __init__(self, vpisnaStevilka: str, studijskiProgram: str, datumVpisa: LocalDate1):
        self.vpisnaStevilka = vpisnaStevilka
        self.studijskiProgram = studijskiProgram
        self.datumVpisa = datumVpisa
        
        pass
    @property
    def vpisnaStevilka(self):
        return self.__vpisnaStevilka
    @vpisnaStevilka.setter
    def vpisnaStevilka(self, vpisnaStevilka: str):
        self.__vpisnaStevilka = vpisnaStevilka

    @property
    def datumVpisa(self):
        return self.__datumVpisa
    @datumVpisa.setter
    def datumVpisa(self, datumVpisa: LocalDate1):
        self.__datumVpisa = datumVpisa

    @property
    def studijskiProgram(self):
        return self.__studijskiProgram
    @studijskiProgram.setter
    def studijskiProgram(self, studijskiProgram: str):
        self.__studijskiProgram = studijskiProgram



class Zaposlen:

    def __init__(self, izobrazba: str, urnaPostavka: float):
        self.izobrazba = izobrazba
        self.urnaPostavka = urnaPostavka
        
        pass
    @property
    def urnaPostavka(self):
        return self.__urnaPostavka
    @urnaPostavka.setter
    def urnaPostavka(self, urnaPostavka: float):
        self.__urnaPostavka = urnaPostavka

    @property
    def izobrazba(self):
        return self.__izobrazba
    @izobrazba.setter
    def izobrazba(self, izobrazba: str):
        self.__izobrazba = izobrazba



class LocalDate:

    pass


class Oseba:

    def __init__(self, ime: str, priimek: str, spol: str, datumRojstva: LocalDate):
        self.ime = ime
        self.priimek = priimek
        self.spol = spol
        self.datumRojstva = datumRojstva
        
        pass
    @property
    def priimek(self):
        return self.__priimek
    @priimek.setter
    def priimek(self, priimek: str):
        self.__priimek = priimek

    @property
    def spol(self):
        return self.__spol
    @spol.setter
    def spol(self, spol: str):
        self.__spol = spol

    @property
    def ime(self):
        return self.__ime
    @ime.setter
    def ime(self, ime: str):
        self.__ime = ime

    @property
    def datumRojstva(self):
        return self.__datumRojstva
    @datumRojstva.setter
    def datumRojstva(self, datumRojstva: LocalDate):
        self.__datumRojstva = datumRojstva



class Pes:

    def __init__(self, vzdevek: str, pasma: str, visina: str):
        self.vzdevek = vzdevek
        self.pasma = pasma
        self.visina = visina
        
        pass
    @property
    def vzdevek(self):
        return self.__vzdevek
    @vzdevek.setter
    def vzdevek(self, vzdevek: str):
        self.__vzdevek = vzdevek

    @property
    def pasma(self):
        return self.__pasma
    @pasma.setter
    def pasma(self, pasma: str):
        self.__pasma = pasma

    @property
    def visina(self):
        return self.__visina
    @visina.setter
    def visina(self, visina: str):
        self.__visina = visina



class ClassV:

    pass


class ClassU:

    pass


class ClassT:

    pass


class ClassS:

    pass


class ClassR:

    pass


class ClassQ:

    pass


class InterfaceO_Interface:

    pass


class ClassP:

    pass


class Class_N:

    pass


class RazredM:

    pass


class RazredL:

    pass


class RazredK:

    pass


class RazredH:

    pass


class RazredJ:

    pass


class RazredG:

    pass


class RazredF:

    pass


class RazredE:

    pass


class RazredD:

    pass


class RazredC:

    def __init__(self, publicAtribut: float, privateAtribut: int, protectedAtribut: str, packageAtribut: str):
        self.publicAtribut = publicAtribut
        self.privateAtribut = privateAtribut
        self.protectedAtribut = protectedAtribut
        self.packageAtribut = packageAtribut
        
        pass
    @property
    def protectedAtribut(self):
        return self.__protectedAtribut
    @protectedAtribut.setter
    def protectedAtribut(self, protectedAtribut: str):
        self.__protectedAtribut = protectedAtribut

    @property
    def privateAtribut(self):
        return self.__privateAtribut
    @privateAtribut.setter
    def privateAtribut(self, privateAtribut: int):
        self.__privateAtribut = privateAtribut

    @property
    def packageAtribut(self):
        return self.__packageAtribut
    @packageAtribut.setter
    def packageAtribut(self, packageAtribut: str):
        self.__packageAtribut = packageAtribut

    @property
    def publicAtribut(self):
        return self.__publicAtribut
    @publicAtribut.setter
    def publicAtribut(self, publicAtribut: float):
        self.__publicAtribut = publicAtribut



class RazredB:

    pass


class RazredA:

    def __init__(self, publicAtribut: float, privateAtribut: int, protectedAtribut: str, packageAtribut: str):
        self.publicAtribut = publicAtribut
        self.privateAtribut = privateAtribut
        self.protectedAtribut = protectedAtribut
        self.packageAtribut = packageAtribut
        
        pass
    @property
    def protectedAtribut(self):
        return self.__protectedAtribut
    @protectedAtribut.setter
    def protectedAtribut(self, protectedAtribut: str):
        self.__protectedAtribut = protectedAtribut

    @property
    def packageAtribut(self):
        return self.__packageAtribut
    @packageAtribut.setter
    def packageAtribut(self, packageAtribut: str):
        self.__packageAtribut = packageAtribut

    @property
    def publicAtribut(self):
        return self.__publicAtribut
    @publicAtribut.setter
    def publicAtribut(self, publicAtribut: float):
        self.__publicAtribut = publicAtribut

    @property
    def privateAtribut(self):
        return self.__privateAtribut
    @privateAtribut.setter
    def privateAtribut(self, privateAtribut: int):
        self.__privateAtribut = privateAtribut



class BancniRacun:

    def __init__(self, lastnik: str, stanje: float, aktiven: bool):
        self.lastnik = lastnik
        self.stanje = stanje
        self.aktiven = aktiven
        
        pass
    @property
    def lastnik(self):
        return self.__lastnik
    @lastnik.setter
    def lastnik(self, lastnik: str):
        self.__lastnik = lastnik

    @property
    def aktiven(self):
        return self.__aktiven
    @aktiven.setter
    def aktiven(self, aktiven: bool):
        self.__aktiven = aktiven

    @property
    def stanje(self):
        return self.__stanje
    @stanje.setter
    def stanje(self, stanje: float):
        self.__stanje = stanje



class Lik3_Interface:

    pass


class Pravokotnik3:

    def __init__(self, koordinataY: str, koordinataX: str):
        self.koordinataY = koordinataY
        self.koordinataX = koordinataX
        
        pass
    @property
    def koordinataX(self):
        return self.__koordinataX
    @koordinataX.setter
    def koordinataX(self, koordinataX: str):
        self.__koordinataX = koordinataX

    @property
    def koordinataY(self):
        return self.__koordinataY
    @koordinataY.setter
    def koordinataY(self, koordinataY: str):
        self.__koordinataY = koordinataY



class PravokotniLik(ABC):

    def __init__(self, sirina: str, visina: str):
        self.sirina = sirina
        self.visina = visina
        
        pass
    @property
    def visina(self):
        return self.__visina
    @visina.setter
    def visina(self, visina: str):
        self.__visina = visina

    @property
    def sirina(self):
        return self.__sirina
    @sirina.setter
    def sirina(self, sirina: str):
        self.__sirina = sirina



class RazredB2:

    pass


class RazredA2:

    def __init__(self, objektB: RazredB2, razredB20: "RazredB2" = None, razredB22: "RazredB2" = None):
        self.objektB = objektB
        self.razredB20 = razredB20
        self.razredB22 = razredB22
        
        pass
    @property
    def objektB(self):
        return self.__objektB
    @objektB.setter
    def objektB(self, objektB: RazredB2):
        self.__objektB = objektB

    @property
    def razredB20(self):
        return self.__razredB20
    @razredB20.setter
    def razredB20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RazredA2__razredB20", None)
        self.__razredB20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "razredA21"):
                opp_val = getattr(old_value, "razredA21", None)
                if opp_val == self:
                    setattr(old_value, "razredA21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "razredA21"):
                opp_val = getattr(value, "razredA21", None)
                setattr(value, "razredA21", self)

    @property
    def razredB22(self):
        return self.__razredB22
    @razredB22.setter
    def razredB22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RazredA2__razredB22", None)
        self.__razredB22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "razredA23"):
                opp_val = getattr(old_value, "razredA23", None)
                if opp_val == self:
                    setattr(old_value, "razredA23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "razredA23"):
                opp_val = getattr(value, "razredA23", None)
                setattr(value, "razredA23", self)

