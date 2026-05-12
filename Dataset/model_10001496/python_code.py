from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Servicetechniker_Actor:

    pass


class Kunde_Actor:

    pass


class Wechselgeldbeh_lter_leeren_UseCase:

    pass


class Herr_Maier_Actor:

    pass


class Herr_M_ller_Actor:

    pass


class Automat_Actor:

    pass


class Gast_Actor:

    pass





class angestellt_in_der_Verwaltung_external:

    pass


class Kinokarten_kaufen_external:

    pass


class Tagesticket_kaufen_external:

    pass


class _2_Stunden_Ticket_kaufen_external:

    pass


class Professor:

    def __init__(self, Lohn: int, attribute2: str):
        self.Lohn = Lohn
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def Lohn(self):
        return self.__Lohn
    @Lohn.setter
    def Lohn(self, Lohn: int):
        self.__Lohn = Lohn



class Student:

    def __init__(self, Martikelnummer: int, Durchschnittsnote: int):
        self.Martikelnummer = Martikelnummer
        self.Durchschnittsnote = Durchschnittsnote
        
        pass
    @property
    def Durchschnittsnote(self):
        return self.__Durchschnittsnote
    @Durchschnittsnote.setter
    def Durchschnittsnote(self, Durchschnittsnote: int):
        self.__Durchschnittsnote = Durchschnittsnote

    @property
    def Martikelnummer(self):
        return self.__Martikelnummer
    @Martikelnummer.setter
    def Martikelnummer(self, Martikelnummer: int):
        self.__Martikelnummer = Martikelnummer



class Wohnadresse:

    def __init__(self, Strasse: str, Stadt: str, PLZ: int, Land: str, person34: "Person" = None):
        self.Strasse = Strasse
        self.Stadt = Stadt
        self.PLZ = PLZ
        self.Land = Land
        self.person34 = person34
        
        pass
    @property
    def PLZ(self):
        return self.__PLZ
    @PLZ.setter
    def PLZ(self, PLZ: int):
        self.__PLZ = PLZ

    @property
    def Land(self):
        return self.__Land
    @Land.setter
    def Land(self, Land: str):
        self.__Land = Land

    @property
    def Strasse(self):
        return self.__Strasse
    @Strasse.setter
    def Strasse(self, Strasse: str):
        self.__Strasse = Strasse

    @property
    def Stadt(self):
        return self.__Stadt
    @Stadt.setter
    def Stadt(self, Stadt: str):
        self.__Stadt = Stadt

    @property
    def person34(self):
        return self.__person34
    @person34.setter
    def person34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wohnadresse__person34", None)
        self.__person34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wohnadresse35"):
                opp_val = getattr(old_value, "wohnadresse35", None)
                if opp_val == self:
                    setattr(old_value, "wohnadresse35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wohnadresse35"):
                opp_val = getattr(value, "wohnadresse35", None)
                setattr(value, "wohnadresse35", self)



class Name_Interface:

    pass


class _Interface:

    pass


class Person:

    def __init__(self, Name: str, Name1: str, Telefonnummer: int, E_mail: str, wohnadresse35: "Wohnadresse" = None):
        self.Name = Name
        self.Name1 = Name1
        self.Telefonnummer = Telefonnummer
        self.E_mail = E_mail
        self.wohnadresse35 = wohnadresse35
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Telefonnummer(self):
        return self.__Telefonnummer
    @Telefonnummer.setter
    def Telefonnummer(self, Telefonnummer: int):
        self.__Telefonnummer = Telefonnummer

    @property
    def Name1(self):
        return self.__Name1
    @Name1.setter
    def Name1(self, Name1: str):
        self.__Name1 = Name1

    @property
    def E_mail(self):
        return self.__E_mail
    @E_mail.setter
    def E_mail(self, E_mail: str):
        self.__E_mail = E_mail

    @property
    def wohnadresse35(self):
        return self.__wohnadresse35
    @wohnadresse35.setter
    def wohnadresse35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__wohnadresse35", None)
        self.__wohnadresse35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person34"):
                opp_val = getattr(old_value, "person34", None)
                if opp_val == self:
                    setattr(old_value, "person34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person34"):
                opp_val = getattr(value, "person34", None)
                setattr(value, "person34", self)



class Automat_Actor1:

    pass


class Fahrkarte_kaufen_Component:

    pass


class Krankenhaus_System_Component:

    pass


class Gast_Actor1:

    pass


class Kino_besuch_Component:

    pass


class Schwimmbad_Eintritt_Component:

    pass


class Wartung_external:

    pass


class Hilfe_rufen_external:

    pass


class Abbrechen_external:

    pass


class Auswahl_der_Fahrkartenkategorie_external:

    pass


class Patienten_aufnehmen_entlassen_external:

    pass


class Mitarbeiter_verwalten_external:

    pass
