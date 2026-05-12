from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Contactformulier:

    def __init__(self, tekst: str, klant17: "Klant" = None, beheerder19: set["Beheerder"] = None):
        self.tekst = tekst
        self.klant17 = klant17
        self.beheerder19 = beheerder19 if beheerder19 is not None else set()
        
        pass
    @property
    def tekst(self):
        return self.__tekst
    @tekst.setter
    def tekst(self, tekst: str):
        self.__tekst = tekst

    @property
    def beheerder19(self):
        return self.__beheerder19
    @beheerder19.setter
    def beheerder19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contactformulier__beheerder19", None)
        self.__beheerder19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contactformulier18"):
                    opp_val = getattr(item, "contactformulier18", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contactformulier18"):
                    opp_val = getattr(item, "contactformulier18", None)
                    
                    if opp_val is None:
                        setattr(item, "contactformulier18", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def klant17(self):
        return self.__klant17
    @klant17.setter
    def klant17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contactformulier__klant17", None)
        self.__klant17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contactformulier16"):
                opp_val = getattr(old_value, "contactformulier16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contactformulier16"):
                opp_val = getattr(value, "contactformulier16", None)
                if opp_val is None:
                    setattr(value, "contactformulier16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Afbeelding:

    def __init__(self, naam: str, locatie: str, datum: str, product10: set["Product"] = None, nieuwsbericht24: set["Nieuwsbericht"] = None):
        self.naam = naam
        self.locatie = locatie
        self.datum = datum
        self.product10 = product10 if product10 is not None else set()
        self.nieuwsbericht24 = nieuwsbericht24 if nieuwsbericht24 is not None else set()
        
        pass
    @property
    def datum(self):
        return self.__datum
    @datum.setter
    def datum(self, datum: str):
        self.__datum = datum

    @property
    def naam(self):
        return self.__naam
    @naam.setter
    def naam(self, naam: str):
        self.__naam = naam

    @property
    def locatie(self):
        return self.__locatie
    @locatie.setter
    def locatie(self, locatie: str):
        self.__locatie = locatie

    @property
    def nieuwsbericht24(self):
        return self.__nieuwsbericht24
    @nieuwsbericht24.setter
    def nieuwsbericht24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Afbeelding__nieuwsbericht24", None)
        self.__nieuwsbericht24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afbeelding25"):
                    opp_val = getattr(item, "afbeelding25", None)
                    
                    if opp_val == self:
                        setattr(item, "afbeelding25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afbeelding25"):
                    opp_val = getattr(item, "afbeelding25", None)
                    
                    setattr(item, "afbeelding25", self)
                    

    @property
    def product10(self):
        return self.__product10
    @product10.setter
    def product10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Afbeelding__product10", None)
        self.__product10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "afbeelding11"):
                    opp_val = getattr(item, "afbeelding11", None)
                    
                    if opp_val == self:
                        setattr(item, "afbeelding11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "afbeelding11"):
                    opp_val = getattr(item, "afbeelding11", None)
                    
                    setattr(item, "afbeelding11", self)
                    



class Categorie:

    pass


class Adres:

    def __init__(self, postcode: str, huisnummer: int, bijvoegsel: str, straatnaam: str, stad: str, klant2: set["Klant"] = None):
        self.postcode = postcode
        self.huisnummer = huisnummer
        self.bijvoegsel = bijvoegsel
        self.straatnaam = straatnaam
        self.stad = stad
        self.klant2 = klant2 if klant2 is not None else set()
        
        pass
    @property
    def stad(self):
        return self.__stad
    @stad.setter
    def stad(self, stad: str):
        self.__stad = stad

    @property
    def postcode(self):
        return self.__postcode
    @postcode.setter
    def postcode(self, postcode: str):
        self.__postcode = postcode

    @property
    def bijvoegsel(self):
        return self.__bijvoegsel
    @bijvoegsel.setter
    def bijvoegsel(self, bijvoegsel: str):
        self.__bijvoegsel = bijvoegsel

    @property
    def straatnaam(self):
        return self.__straatnaam
    @straatnaam.setter
    def straatnaam(self, straatnaam: str):
        self.__straatnaam = straatnaam

    @property
    def huisnummer(self):
        return self.__huisnummer
    @huisnummer.setter
    def huisnummer(self, huisnummer: int):
        self.__huisnummer = huisnummer

    @property
    def klant2(self):
        return self.__klant2
    @klant2.setter
    def klant2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Adres__klant2", None)
        self.__klant2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adres3"):
                    opp_val = getattr(item, "adres3", None)
                    
                    if opp_val == self:
                        setattr(item, "adres3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adres3"):
                    opp_val = getattr(item, "adres3", None)
                    
                    setattr(item, "adres3", self)
                    



class Nieuwsbericht:

    def __init__(self, titel: str, tekst: str, hoofdbeheerder8: "Hoofdbeheerder" = None, afbeelding25: "Afbeelding" = None):
        self.titel = titel
        self.tekst = tekst
        self.hoofdbeheerder8 = hoofdbeheerder8
        self.afbeelding25 = afbeelding25
        
        pass
    @property
    def tekst(self):
        return self.__tekst
    @tekst.setter
    def tekst(self, tekst: str):
        self.__tekst = tekst

    @property
    def titel(self):
        return self.__titel
    @titel.setter
    def titel(self, titel: str):
        self.__titel = titel

    @property
    def afbeelding25(self):
        return self.__afbeelding25
    @afbeelding25.setter
    def afbeelding25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nieuwsbericht__afbeelding25", None)
        self.__afbeelding25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nieuwsbericht24"):
                opp_val = getattr(old_value, "nieuwsbericht24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nieuwsbericht24"):
                opp_val = getattr(value, "nieuwsbericht24", None)
                if opp_val is None:
                    setattr(value, "nieuwsbericht24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hoofdbeheerder8(self):
        return self.__hoofdbeheerder8
    @hoofdbeheerder8.setter
    def hoofdbeheerder8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nieuwsbericht__hoofdbeheerder8", None)
        self.__hoofdbeheerder8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post9"):
                opp_val = getattr(old_value, "post9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post9"):
                opp_val = getattr(value, "post9", None)
                if opp_val is None:
                    setattr(value, "post9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Product:

    def __init__(self, naam: str, prijs: int, beschrijving: str, voorraad: int, actief: bool, klant1: set["Klant"] = None, bestelregel5: set["Bestelregel"] = None, categorie7: set["Categorie"] = None, afbeelding11: "Afbeelding" = None, beheerder15: set["Beheerder"] = None):
        self.naam = naam
        self.prijs = prijs
        self.beschrijving = beschrijving
        self.voorraad = voorraad
        self.actief = actief
        self.klant1 = klant1 if klant1 is not None else set()
        self.bestelregel5 = bestelregel5 if bestelregel5 is not None else set()
        self.categorie7 = categorie7 if categorie7 is not None else set()
        self.afbeelding11 = afbeelding11
        self.beheerder15 = beheerder15 if beheerder15 is not None else set()
        
        pass
    @property
    def actief(self):
        return self.__actief
    @actief.setter
    def actief(self, actief: bool):
        self.__actief = actief

    @property
    def beschrijving(self):
        return self.__beschrijving
    @beschrijving.setter
    def beschrijving(self, beschrijving: str):
        self.__beschrijving = beschrijving

    @property
    def naam(self):
        return self.__naam
    @naam.setter
    def naam(self, naam: str):
        self.__naam = naam

    @property
    def prijs(self):
        return self.__prijs
    @prijs.setter
    def prijs(self, prijs: int):
        self.__prijs = prijs

    @property
    def voorraad(self):
        return self.__voorraad
    @voorraad.setter
    def voorraad(self, voorraad: int):
        self.__voorraad = voorraad

    @property
    def categorie7(self):
        return self.__categorie7
    @categorie7.setter
    def categorie7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__categorie7", None)
        self.__categorie7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product6"):
                    opp_val = getattr(item, "product6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product6"):
                    opp_val = getattr(item, "product6", None)
                    
                    if opp_val is None:
                        setattr(item, "product6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def afbeelding11(self):
        return self.__afbeelding11
    @afbeelding11.setter
    def afbeelding11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__afbeelding11", None)
        self.__afbeelding11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product10"):
                opp_val = getattr(old_value, "product10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product10"):
                opp_val = getattr(value, "product10", None)
                if opp_val is None:
                    setattr(value, "product10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def klant1(self):
        return self.__klant1
    @klant1.setter
    def klant1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__klant1", None)
        self.__klant1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product0"):
                    opp_val = getattr(item, "product0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product0"):
                    opp_val = getattr(item, "product0", None)
                    
                    if opp_val is None:
                        setattr(item, "product0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def beheerder15(self):
        return self.__beheerder15
    @beheerder15.setter
    def beheerder15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__beheerder15", None)
        self.__beheerder15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product14"):
                    opp_val = getattr(item, "product14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product14"):
                    opp_val = getattr(item, "product14", None)
                    
                    if opp_val is None:
                        setattr(item, "product14", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def bestelregel5(self):
        return self.__bestelregel5
    @bestelregel5.setter
    def bestelregel5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Product__bestelregel5", None)
        self.__bestelregel5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product4"):
                    opp_val = getattr(item, "product4", None)
                    
                    if opp_val == self:
                        setattr(item, "product4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product4"):
                    opp_val = getattr(item, "product4", None)
                    
                    setattr(item, "product4", self)
                    



class Bestelregel:

    def __init__(self, aantal: int, product4: "Product" = None, factuur21: "Factuur" = None):
        self.aantal = aantal
        self.product4 = product4
        self.factuur21 = factuur21
        
        pass
    @property
    def aantal(self):
        return self.__aantal
    @aantal.setter
    def aantal(self, aantal: int):
        self.__aantal = aantal

    @property
    def product4(self):
        return self.__product4
    @product4.setter
    def product4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bestelregel__product4", None)
        self.__product4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bestelregel5"):
                opp_val = getattr(old_value, "bestelregel5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bestelregel5"):
                opp_val = getattr(value, "bestelregel5", None)
                if opp_val is None:
                    setattr(value, "bestelregel5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def factuur21(self):
        return self.__factuur21
    @factuur21.setter
    def factuur21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bestelregel__factuur21", None)
        self.__factuur21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bestelregel20"):
                opp_val = getattr(old_value, "bestelregel20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bestelregel20"):
                opp_val = getattr(value, "bestelregel20", None)
                if opp_val is None:
                    setattr(value, "bestelregel20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Factuur:

    def __init__(self, datum: str, status: str, btw: int, beheerder12: "Beheerder" = None, bestelregel20: set["Bestelregel"] = None, klant23: "Klant" = None):
        self.datum = datum
        self.status = status
        self.btw = btw
        self.beheerder12 = beheerder12
        self.bestelregel20 = bestelregel20 if bestelregel20 is not None else set()
        self.klant23 = klant23
        
        pass
    @property
    def datum(self):
        return self.__datum
    @datum.setter
    def datum(self, datum: str):
        self.__datum = datum

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def btw(self):
        return self.__btw
    @btw.setter
    def btw(self, btw: int):
        self.__btw = btw

    @property
    def klant23(self):
        return self.__klant23
    @klant23.setter
    def klant23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factuur__klant23", None)
        self.__klant23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bestelregel22"):
                opp_val = getattr(old_value, "bestelregel22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bestelregel22"):
                opp_val = getattr(value, "bestelregel22", None)
                if opp_val is None:
                    setattr(value, "bestelregel22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def beheerder12(self):
        return self.__beheerder12
    @beheerder12.setter
    def beheerder12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factuur__beheerder12", None)
        self.__beheerder12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "factuur13"):
                opp_val = getattr(old_value, "factuur13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "factuur13"):
                opp_val = getattr(value, "factuur13", None)
                if opp_val is None:
                    setattr(value, "factuur13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bestelregel20(self):
        return self.__bestelregel20
    @bestelregel20.setter
    def bestelregel20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Factuur__bestelregel20", None)
        self.__bestelregel20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "factuur21"):
                    opp_val = getattr(item, "factuur21", None)
                    
                    if opp_val == self:
                        setattr(item, "factuur21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "factuur21"):
                    opp_val = getattr(item, "factuur21", None)
                    
                    setattr(item, "factuur21", self)
                    



class Hoofdbeheerder:

    pass


class Beheerder:

    def __init__(self, rechten: bool, factuur13: set["Factuur"] = None, product14: set["Product"] = None, contactformulier18: set["Contactformulier"] = None):
        self.rechten = rechten
        self.factuur13 = factuur13 if factuur13 is not None else set()
        self.product14 = product14 if product14 is not None else set()
        self.contactformulier18 = contactformulier18 if contactformulier18 is not None else set()
        
        pass
    @property
    def rechten(self):
        return self.__rechten
    @rechten.setter
    def rechten(self, rechten: bool):
        self.__rechten = rechten

    @property
    def contactformulier18(self):
        return self.__contactformulier18
    @contactformulier18.setter
    def contactformulier18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Beheerder__contactformulier18", None)
        self.__contactformulier18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "beheerder19"):
                    opp_val = getattr(item, "beheerder19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "beheerder19"):
                    opp_val = getattr(item, "beheerder19", None)
                    
                    if opp_val is None:
                        setattr(item, "beheerder19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def product14(self):
        return self.__product14
    @product14.setter
    def product14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Beheerder__product14", None)
        self.__product14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "beheerder15"):
                    opp_val = getattr(item, "beheerder15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "beheerder15"):
                    opp_val = getattr(item, "beheerder15", None)
                    
                    if opp_val is None:
                        setattr(item, "beheerder15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def factuur13(self):
        return self.__factuur13
    @factuur13.setter
    def factuur13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Beheerder__factuur13", None)
        self.__factuur13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "beheerder12"):
                    opp_val = getattr(item, "beheerder12", None)
                    
                    if opp_val == self:
                        setattr(item, "beheerder12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "beheerder12"):
                    opp_val = getattr(item, "beheerder12", None)
                    
                    setattr(item, "beheerder12", self)
                    



class Klant:

    def __init__(self, telefoonnummer: str, geboortedatum: str, product0: set["Product"] = None, adres3: "Adres" = None, contactformulier16: set["Contactformulier"] = None, bestelregel22: set["Factuur"] = None):
        self.telefoonnummer = telefoonnummer
        self.geboortedatum = geboortedatum
        self.product0 = product0 if product0 is not None else set()
        self.adres3 = adres3
        self.contactformulier16 = contactformulier16 if contactformulier16 is not None else set()
        self.bestelregel22 = bestelregel22 if bestelregel22 is not None else set()
        
        pass
    @property
    def geboortedatum(self):
        return self.__geboortedatum
    @geboortedatum.setter
    def geboortedatum(self, geboortedatum: str):
        self.__geboortedatum = geboortedatum

    @property
    def telefoonnummer(self):
        return self.__telefoonnummer
    @telefoonnummer.setter
    def telefoonnummer(self, telefoonnummer: str):
        self.__telefoonnummer = telefoonnummer

    @property
    def product0(self):
        return self.__product0
    @product0.setter
    def product0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Klant__product0", None)
        self.__product0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "klant1"):
                    opp_val = getattr(item, "klant1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "klant1"):
                    opp_val = getattr(item, "klant1", None)
                    
                    if opp_val is None:
                        setattr(item, "klant1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def bestelregel22(self):
        return self.__bestelregel22
    @bestelregel22.setter
    def bestelregel22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Klant__bestelregel22", None)
        self.__bestelregel22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "klant23"):
                    opp_val = getattr(item, "klant23", None)
                    
                    if opp_val == self:
                        setattr(item, "klant23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "klant23"):
                    opp_val = getattr(item, "klant23", None)
                    
                    setattr(item, "klant23", self)
                    

    @property
    def contactformulier16(self):
        return self.__contactformulier16
    @contactformulier16.setter
    def contactformulier16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Klant__contactformulier16", None)
        self.__contactformulier16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "klant17"):
                    opp_val = getattr(item, "klant17", None)
                    
                    if opp_val == self:
                        setattr(item, "klant17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "klant17"):
                    opp_val = getattr(item, "klant17", None)
                    
                    setattr(item, "klant17", self)
                    

    @property
    def adres3(self):
        return self.__adres3
    @adres3.setter
    def adres3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Klant__adres3", None)
        self.__adres3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "klant2"):
                opp_val = getattr(old_value, "klant2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "klant2"):
                opp_val = getattr(value, "klant2", None)
                if opp_val is None:
                    setattr(value, "klant2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Persoon:

    def __init__(self, voornaam: str, tussenvoegsel: str, achternaam: str, e_mail: str, wachtwoord: str):
        self.voornaam = voornaam
        self.tussenvoegsel = tussenvoegsel
        self.achternaam = achternaam
        self.e_mail = e_mail
        self.wachtwoord = wachtwoord
        
        pass
    @property
    def wachtwoord(self):
        return self.__wachtwoord
    @wachtwoord.setter
    def wachtwoord(self, wachtwoord: str):
        self.__wachtwoord = wachtwoord

    @property
    def tussenvoegsel(self):
        return self.__tussenvoegsel
    @tussenvoegsel.setter
    def tussenvoegsel(self, tussenvoegsel: str):
        self.__tussenvoegsel = tussenvoegsel

    @property
    def voornaam(self):
        return self.__voornaam
    @voornaam.setter
    def voornaam(self, voornaam: str):
        self.__voornaam = voornaam

    @property
    def achternaam(self):
        return self.__achternaam
    @achternaam.setter
    def achternaam(self, achternaam: str):
        self.__achternaam = achternaam

    @property
    def e_mail(self):
        return self.__e_mail
    @e_mail.setter
    def e_mail(self, e_mail: str):
        self.__e_mail = e_mail

